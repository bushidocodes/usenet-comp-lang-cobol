"""Convert comp.lang.cobol mbox archive to Markdown, grouped by year-month.

Uses a streaming bytes-level parser instead of stdlib `mailbox`, because
the latter chokes on non-ASCII bytes in From_ separator lines.
"""
from __future__ import annotations

import email
import email.policy
import re
import sys
from collections import defaultdict
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from pathlib import Path

from dateutil import parser as dateutil_parser

PROJECT_DIR = Path(__file__).resolve().parent
SRC = PROJECT_DIR / "comp.lang.cobol.mbox"
OUT = PROJECT_DIR / "markdown"
OUT.mkdir(exist_ok=True)

# Real envelope-From lines in this archive all look like: `From <signed-int>`.
# Body text containing "From " (e.g. "From the docs:") is a false positive.
FROM_LINE_RE = re.compile(rb"^From -?[0-9]+[ \t]*\r?\n", re.MULTILINE)


def iter_messages(path: Path):
    """Yield raw bytes blobs, one per message, by splitting on envelope-From lines."""
    with path.open("rb") as f:
        data = f.read()
    starts = [m.start() for m in FROM_LINE_RE.finditer(data)]
    starts.append(len(data))
    for i in range(len(starts) - 1):
        blob = data[starts[i]:starts[i + 1]]
        nl = blob.find(b"\n")
        if nl == -1:
            continue
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


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def parse_date(raw: str):
    """Try RFC 2822 first, then fall back to dateutil for slash-style dates."""
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


def strip_dotall(text: str) -> str:
    text = text.rstrip()
    if text.endswith("\n."):
        text = text[:-2].rstrip()
    return text


def format_message(msg) -> tuple[str, str]:
    subject = decode_header_str(msg.get("Subject")).strip() or "(no subject)"
    sender = decode_header_str(msg.get("From")).strip()
    date_raw = msg.get("Date", "")
    msg_id = (msg.get("Message-ID") or "").strip()
    references = (msg.get("References") or "").strip()
    in_reply_to = (msg.get("In-Reply-To") or "").strip()
    newsgroups = (msg.get("Newsgroups") or "").strip()

    dt = parse_date(date_raw)

    if dt:
        ym = f"{dt.year:04d}-{dt.month:02d}"
        date_iso = dt.isoformat()
    else:
        ym = "undated"
        date_iso = date_raw or "(unknown)"

    body = strip_dotall(get_body(msg))

    parts = [
        f"## {md_escape(subject)}",
        "",
        f"- **From:** {md_escape(sender)}",
        f"- **Date:** {md_escape(date_iso)}",
    ]
    if newsgroups:
        parts.append(f"- **Newsgroups:** {md_escape(newsgroups)}")
    if msg_id:
        parts.append(f"- **Message-ID:** `{msg_id}`")
    if in_reply_to:
        parts.append(f"- **In-Reply-To:** `{in_reply_to}`")
    if references:
        refs_compact = re.sub(r"\s+", " ", references)
        parts.append(f"- **References:** `{refs_compact}`")
    parts += ["", "```", body, "```", "", "---", ""]
    return ym, "\n".join(parts)


def main() -> int:
    print(f"Opening {SRC} ({SRC.stat().st_size / 1e6:.1f} MB)...")
    buckets: dict[str, list[str]] = defaultdict(list)
    counts: dict[str, int] = defaultdict(int)
    total = 0
    errors = 0

    for idx, raw in enumerate(iter_messages(SRC)):
        try:
            msg = email.message_from_bytes(raw, policy=email.policy.compat32)
            ym, section = format_message(msg)
            buckets[ym].append(section)
            counts[ym] += 1
            total += 1
        except Exception as exc:
            errors += 1
            if errors <= 10:
                print(f"  [warn] message {idx}: {exc}", file=sys.stderr)
        if total and total % 5000 == 0:
            print(f"  ...{total} messages processed")

    print(f"\nWriting {len(buckets)} monthly files...")
    for ym in sorted(buckets):
        path = OUT / f"{ym}.md"
        header = f"# comp.lang.cobol — {ym}\n\n_{counts[ym]} messages_\n\n---\n\n"
        with path.open("w", encoding="utf-8") as f:
            f.write(header)
            f.write("\n".join(buckets[ym]))

    print(f"\nDone. {total} messages, {errors} errors. Output: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
