"""Shared mbox parsing for the comp.lang.cobol archive scripts.

Parses the mbox once and caches the result to disk; downstream scripts get
the parsed thread tree in ~1s instead of re-running the ~90s parse every time.
Other modules use `parse_archive()`.
"""
from __future__ import annotations

import email
import email.policy
import hashlib
import pickle
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from pathlib import Path

from dateutil import parser as dateutil_parser

PROJECT_DIR = Path(r"C:\Users\sean\projects\usenet-cobol")
SCRIPT_DIR = Path(__file__).resolve().parent
SRC = PROJECT_DIR / "comp.lang.cobol.mbox"
CACHE = PROJECT_DIR / ".archive_cache.pickle"
OUT = SCRIPT_DIR / "markdown"
THREADS_DIR = OUT / "threads"

# Bump to invalidate older caches when the parser semantics change.
CACHE_VERSION = 3

FROM_LINE_RE = re.compile(rb"^From -?[0-9]+[ \t]*\r?\n", re.MULTILINE)
MSGID_RE = re.compile(r"<[^<>\s]+>")
SUBJ_PREFIX_RE = re.compile(
    r"^(\s*(re|fw|fwd|aw|sv|antw|odp|res|rif)\s*(\[\d+\])?\s*:\s*)+",
    re.IGNORECASE,
)
EMAIL_RE = re.compile(r"([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})")

FAR_FUTURE = datetime.max.replace(tzinfo=None)


def iter_messages(path: Path):
    with path.open("rb") as f:
        data = f.read()
    starts = [m.start() for m in FROM_LINE_RE.finditer(data)]
    starts.append(len(data))
    for i in range(len(starts) - 1):
        blob = data[starts[i]:starts[i + 1]]
        nl = blob.find(b"\n")
        if nl != -1:
            yield blob[nl + 1:]


def decode_header_str(value) -> str:
    if not value:
        return ""
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return str(value)


def decode_payload(part) -> str:
    payload = part.get_payload(decode=True)
    if payload is None:
        return ""
    charset = part.get_content_charset() or "utf-8"
    for enc in (charset, "utf-8", "latin-1", "cp1252"):
        try:
            return payload.decode(enc, errors="replace")
        except (LookupError, UnicodeDecodeError):
            continue
    return payload.decode("latin-1", errors="replace")


def get_body(msg) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and not part.is_multipart():
                return decode_payload(part)
        for part in msg.walk():
            if part.get_content_type() == "text/html" and not part.is_multipart():
                return "[HTML part — not converted]\n\n" + decode_payload(part)
        return ""
    return decode_payload(msg)


def parse_date(raw: str):
    if not raw:
        return None
    try:
        dt = parsedate_to_datetime(raw)
        if dt is not None:
            return dt
    except (TypeError, ValueError, IndexError):
        pass
    try:
        return dateutil_parser.parse(raw, fuzzy=True)
    except (ValueError, TypeError, OverflowError):
        return None


def date_key(dt):
    """Normalize naive/aware datetimes to a comparable sort key."""
    if dt is None:
        return FAR_FUTURE
    if dt.tzinfo is not None:
        return dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt


def normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip() if s else s


def normalize_subject(subj: str) -> str:
    if not subj:
        return ""
    return SUBJ_PREFIX_RE.sub("", subj).strip()


def extract_msgid(raw: str) -> str:
    if not raw:
        return ""
    m = MSGID_RE.search(raw)
    return m.group(0) if m else ""


def parse_refs(raw: str):
    return MSGID_RE.findall(raw or "")


def strip_dotall(text: str) -> str:
    text = text.rstrip()
    if text.endswith("\n."):
        text = text[:-2].rstrip()
    return text


SIG_DELIM_RE = re.compile(r"^-- ?$")


def _is_quote_line(line: str) -> bool:
    """Detect a quoted line (Usenet/email reply prefix)."""
    s = line.lstrip()
    if not s:
        return False
    return s[0] in ">|"


def clean_body(body: str, quote_threshold: int = 5) -> str:
    """Strip signatures and collapse long quote runs.

    - Lines from a `-- ` (sig delimiter) onward are dropped.
    - Runs of consecutive quoted lines longer than `quote_threshold` are
      replaced by the first 2 lines, an elision marker with the count,
      and the last line.
    """
    if not body:
        return body
    lines = body.split("\n")

    # Drop signature
    for i, line in enumerate(lines):
        if SIG_DELIM_RE.match(line):
            lines = lines[:i]
            break

    out: list[str] = []
    i = 0
    while i < len(lines):
        if _is_quote_line(lines[i]):
            j = i
            while j < len(lines) and _is_quote_line(lines[j]):
                j += 1
            run = j - i
            if run > quote_threshold:
                out.extend(lines[i:i + 2])
                out.append(f"…[{run - 3} more quoted lines elided]…")
                out.append(lines[j - 1])
            else:
                out.extend(lines[i:j])
            i = j
        else:
            out.append(lines[i])
            i += 1

    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


def extract_email(sender: str) -> str:
    """Pull the bare email out of a `Name <addr>` / `addr (Name)` From header."""
    if not sender:
        return ""
    m = EMAIL_RE.search(sender)
    return m.group(1).lower() if m else ""


def extract_display_name(sender: str) -> str:
    """Best-effort display name from a From header."""
    if not sender:
        return ""
    s = sender.strip()
    # `"Name" <email>` or `Name <email>`
    m = re.match(r"\s*\"?([^\"<(]+?)\"?\s*<", s)
    if m:
        return m.group(1).strip()
    # `email (Name)` (old-style Usenet)
    m = re.match(r".+@\S+\s*\(([^)]+)\)", s)
    if m:
        return m.group(1).strip()
    return s


def thread_anchor(root_id: str) -> str:
    """Stable in-page anchor for a thread, derived from its root msg ID."""
    h = hashlib.md5(root_id.encode("utf-8", errors="replace")).hexdigest()[:10]
    return f"t-{h}"


def _parse_full():
    print(f"Parsing {SRC} ({SRC.stat().st_size / 1e6:.1f} MB)...")
    msgs = {}
    errors = 0
    parsed = 0
    for idx, raw in enumerate(iter_messages(SRC)):
        try:
            m = email.message_from_bytes(raw, policy=email.policy.compat32)
            mid = extract_msgid(m.get("Message-ID") or "")
            subject = normalize_whitespace(
                decode_header_str(m.get("Subject")).strip() or "(no subject)"
            )
            sender = normalize_whitespace(decode_header_str(m.get("From")).strip())
            email_addr = extract_email(sender)
            display_name = extract_display_name(sender)
            date_raw = m.get("Date", "")
            references = parse_refs(m.get("References", ""))
            irt_raw = (m.get("In-Reply-To") or "").strip()
            irt_list = parse_refs(irt_raw)
            parent = irt_list[0] if irt_list else (references[-1] if references else None)
            newsgroups = (m.get("Newsgroups") or "").strip()
            dt = parse_date(date_raw)
            ym = f"{dt.year:04d}-{dt.month:02d}" if dt else "undated"
            date_iso = dt.isoformat() if dt else (date_raw or "(unknown)")
            body = strip_dotall(get_body(m))
            key = mid or f"<__noid_{idx}__>"
            if key in msgs:
                key = f"<__dup_{idx}__{key.strip('<>')}>"
            msgs[key] = {
                "id": key,
                "original_id": mid,
                "subject": subject,
                "norm_subject": normalize_subject(subject),
                "sender": sender,
                "email": email_addr,
                "display_name": display_name,
                "date_iso": date_iso,
                "date_raw": date_raw,
                "dt": dt,
                "ym": ym,
                "body": body,
                "body_len": len(body),
                "references": references,
                "in_reply_to_raw": irt_raw,
                "parent": parent,
                "newsgroups": newsgroups,
                "idx": idx,
            }
            parsed += 1
            if parsed % 20000 == 0:
                print(f"  ...{parsed} parsed")
        except Exception as exc:
            errors += 1
            if errors <= 5:
                print(f"  [warn] message {idx}: {exc}", file=sys.stderr)
    print(f"Parsed {parsed} messages, {errors} errors")
    return msgs


def _build_threads(msgs):
    print("Building thread index...")
    children = defaultdict(list)
    for mid, entry in msgs.items():
        parent = entry.get("parent")
        if parent and parent in msgs and parent != mid:
            children[parent].append(mid)
    for kids in children.values():
        kids.sort(key=lambda cid: date_key(msgs[cid]["dt"]))

    root_cache: dict[str, str] = {}
    for mid in msgs:
        chain = []
        cur = mid
        while True:
            if cur in root_cache:
                root = root_cache[cur]
                break
            if cur in chain:
                root = cur
                break
            chain.append(cur)
            par = msgs[cur].get("parent") if cur in msgs else None
            if par and par in msgs and par != cur:
                cur = par
                continue
            root = cur
            break
        for m in chain:
            root_cache[m] = root

    depth: dict[str, int] = {}
    for root in set(root_cache.values()):
        if root in depth or root not in msgs:
            continue
        stack = [(root, 0)]
        while stack:
            node, d = stack.pop()
            if node in depth:
                continue
            depth[node] = d
            for child in children.get(node, ()):
                if child not in depth:
                    stack.append((child, d + 1))

    return dict(children), root_cache, depth


def parse_archive(use_cache: bool = True):
    """Return (msgs, children, root_cache, depth). Cached to disk by default."""
    if use_cache and CACHE.exists():
        try:
            print(f"Loading cache from {CACHE.name}...")
            with CACHE.open("rb") as f:
                cached = pickle.load(f)
            if cached.get("version") == CACHE_VERSION:
                print(f"  cache hit: {len(cached['msgs'])} messages")
                return (
                    cached["msgs"],
                    cached["children"],
                    cached["root_cache"],
                    cached["depth"],
                )
            print("  cache version mismatch, re-parsing")
        except Exception as exc:
            print(f"  cache load failed ({exc}), re-parsing")

    msgs = _parse_full()
    children, root_cache, depth = _build_threads(msgs)

    if use_cache:
        print(f"Writing cache to {CACHE.name}...")
        with CACHE.open("wb") as f:
            pickle.dump(
                {
                    "version": CACHE_VERSION,
                    "msgs": msgs,
                    "children": children,
                    "root_cache": root_cache,
                    "depth": depth,
                },
                f,
                protocol=pickle.HIGHEST_PROTOCOL,
            )

    return msgs, children, root_cache, depth


def filter_msgs(msgs, summaries):
    """Return only the messages belonging to the given thread summaries.

    Use this in generators that iterate over `msgs.values()` directly,
    so they see the same spam-filtered subset that `thread_summaries()`
    returned.
    """
    kept = {mid for s in summaries for mid in s["msg_ids"]}
    return {mid: msgs[mid] for mid in kept if mid in msgs}


def thread_summaries(msgs, root_cache, include_spam: bool = False):
    """Compute one summary per thread: subject, count, span, months, participants.

    Spam threads are dropped by default — see `spam.thread_is_spam`. Pass
    `include_spam=True` to recover them (useful for diagnostics).
    """
    from spam import thread_is_spam

    by_root: dict[str, list[str]] = defaultdict(list)
    for mid in msgs:
        by_root[root_cache[mid]].append(mid)

    out = []
    dropped = 0
    for root, mids in by_root.items():
        mids_sorted = sorted(mids, key=lambda x: date_key(msgs[x]["dt"]))
        first = msgs[mids_sorted[0]]
        last = msgs[mids_sorted[-1]]
        if root in msgs:
            subj = msgs[root]["norm_subject"] or msgs[root]["subject"]
        else:
            subj = first["norm_subject"] or first["subject"]
        if not subj:
            subj = "(no subject)"
        months = sorted({msgs[mid]["ym"] for mid in mids if msgs[mid]["ym"] != "undated"})
        participants = {msgs[mid]["email"] for mid in mids if msgs[mid]["email"]}
        summary = {
            "root": root,
            "anchor": thread_anchor(root),
            "subject": subj,
            "count": len(mids),
            "first_ym": first["ym"],
            "last_ym": last["ym"],
            "first_dt": first["dt"],
            "months": months,
            "participants": participants,
            "msg_ids": mids,
        }
        if not include_spam and thread_is_spam(summary, msgs):
            dropped += 1
            continue
        out.append(summary)
    if dropped:
        print(f"  filtered {dropped} spam threads")
    return out


if __name__ == "__main__":
    # Run directly to (re)build the cache.
    parse_archive(use_cache=True)
