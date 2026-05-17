"""Spam detection for the comp.lang.cobol mbox archive.

Drive-by URL-shortener / redirect spam, MLM/scam, porn link spam, and
similar promotional posts with no relation to COBOL. The actual mbox
source is left intact; this module filters spam threads out of the
generated markdown indexes via `archive.thread_summaries()`.

A *message* is spam when its non-quoted text references a known spam
host or free-hosting TLD (`SPAM_HOSTS` / `SPAM_HOST_SUFFIXES`). A
*thread* is spam when its root message is spam and no later message
has substantive original content beyond auto-quote-headers — so
threads where humans replied (even with one-line jokes) are preserved.
"""
from __future__ import annotations

import re

# Hosts that appeared in obvious spam during the initial archive sweep.
# Add new hosts here when more spam is discovered.
SPAM_HOSTS: frozenset[str] = frozenset([
    # URL-shortener / drive-by spam
    "find-365.com",
    "web-sweb.com",
    "i-finally-found.cn",
    "my-best-web.com",
    "web-for-you.cn",
    "full-base.com",
    "searchfu.info",
    "wed-bew.cn",
    "search-results.cn",
    "gr8search.cc",
    "wd-content.cc",
    "netresults-online.com",
    "pakwer.com",
    # Pharma / MLM / "earn money"
    "123maza.com",
    "msi-team.com",
    "all4you007.blogspot.com",
    "medicines4u.cn",
    "awsurveys.com",
    "gpstakesyou.com",
    # Wholesale knockoffs
    "brandtrade10.com",
    # Promotional blog spam
    "googleiloveu.blogspot.com",
    "want-to-be-sure.blogspot.com",
    "jcil.blogspot.com",
    "s0x0.blogspot.com",
    "kumaripud.blogspot.com",
    "vasiliyucecozavy.blogspot.com",
    # Porn link spam (non-free-hosting domains)
    "ragdai.info",
    "video48.net",
    "adultisp.com",
    "asians.usatown.net",
    "my-black.we.bs",
    # Specific spam .tk hosts (tcl.tk is the legitimate TCL programming
    # language site — so we list bad .tk hosts explicitly rather than
    # banning the whole TLD)
    "beninbeachgirlsvideos.tk",
    "easylivevideos.tk",
    "finlandsoftgirlsdatingvideos.tk",
    "getinstantmoney.tk",
    "howtogethigchyourincom.tk",
    "indianwomensfashion.tk",
    "jaisahata.tk",
    "midnightdatingvideosinbenin.tk",
    "namithawithoutbradatingvideos.tk",
    "qualitycontent.tk",
    "smallandbig.tk",
    "sweetyshilpa.tk",
])

# Domain suffixes that, in this archive, host *only* spam. Every URL with
# one of these suffixes in the message bodies of comp.lang.cobol turned
# out to be a redirect/affiliate/porn page — no legitimate cobol-related
# content uses these free-hosting TLDs.
SPAM_HOST_SUFFIXES: tuple[str, ...] = (
    ".co.cc",          # free Cocos Islands subdomains (deactivated 2011)
    ".byethost",       # free shared hosting (.byethostN.com)
    ".freetzi.com",    # free hosting
    ".com.cm",         # Cameroon catchall (typo-squat market)
    ".4-all.org",      # affiliate redirect
    ".us.tt",          # Trinidad & Tobago free
    ".we.bs",          # we.bs free hosting
    ".euro.st",        # São Tomé free
    ".50webs.com",     # free webhost
    ".blogspot.in",    # Indian-locale Blogger — 100% spam in this archive
)

# Minimum words of substantive content for a message to "count" as a real reply.
_SUBSTANTIVE_WORD_MIN = 3

_WORD_RE = re.compile(r"\b[a-zA-Z]{3,}\b")

# Real Usenet/email quote lines start at column 0 with one or more `>` (or
# `|`) followed by a space — `> reply text`, `>> grandparent`. Spam
# decoration like `   > http://link <` or `>>> link <<<` has leading
# whitespace (or no trailing space after the chevrons), so it stays as
# part of the original message content.
_QUOTE_LINE_RE = re.compile(r"^[>|]+(\s|$)")

# Lines that are unambiguously auto-generated quote headers from common
# clients ("On <date>, <name> wrote:", "Name wrote:", Chinese "X 写道：", etc.).
# Used to recognize replies that quote a parent but add no original content.
_QUOTE_HEADER_RE = re.compile(
    r"""^\s*(?:
        .{0,120}\bwrote\b\s*:\s*$           # "Pete wrote:" / "On X, Pete wrote:"
        | .{0,120}\bsaid\b\s*:\s*$          # "Pete said:"
        | in\s+article\b.*$                 # "In article <id> Name writes:"
        | on\s+.{0,80}\bwrites?\b.*$        # "On <date> Name writes:"
        | .{0,80}\b写道\b.{0,5}[:：]\s*$    # Chinese "在 ... 写道："
    )""",
    re.IGNORECASE | re.VERBOSE | re.MULTILINE,
)


def _non_quoted(body: str) -> str:
    """Return only the non-quoted lines of a message body."""
    return "\n".join(
        line for line in body.split("\n")
        if not _QUOTE_LINE_RE.match(line)
    )


def _has_spam_url(text_lower: str) -> bool:
    """True if any exact spam host or known-bad TLD suffix appears in the text.

    Uses substring matching for both: the suffixes are all distinctive
    enough not to occur in normal English prose, and substring match
    also catches URLs that some mail clients wrap across line breaks
    (e.g. `AThttp://\\nsomehost.co.cc`).
    """
    if any(host in text_lower for host in SPAM_HOSTS):
        return True
    return any(suffix in text_lower for suffix in SPAM_HOST_SUFFIXES)


def message_is_spam(entry: dict) -> bool:
    """True if this single message is an unambiguous spam advertisement.

    A known spam host appearing in the message's non-quoted text is
    sufficient — `SPAM_HOSTS` is a curated allowlist of known-bad
    redirect/SEO domains, no legitimate cobol-related site is on it,
    and replies that quote spam (without re-promoting it) have the URL
    only inside quoted lines, which `_non_quoted` strips.
    """
    body = entry.get("body") or ""
    if not body:
        return False
    return _has_spam_url(_non_quoted(body).lower())


def _has_substantive_content(entry: dict) -> bool:
    """True if the message has original (non-quoted, non-header) prose."""
    body = entry.get("body") or ""
    text = _non_quoted(body)
    text = _QUOTE_HEADER_RE.sub("", text)
    return len(_WORD_RE.findall(text)) >= _SUBSTANTIVE_WORD_MIN


def thread_is_spam(summary: dict, msgs: dict) -> bool:
    """True if the entire thread can be dropped from generated indexes.

    Conservatively keeps any thread where at least one message has
    substantive original content — even a one-line joke reply counts —
    so that human engagement is preserved even when the inciting post
    was spam.
    """
    root_id = summary.get("root")
    root_msg = msgs.get(root_id) if root_id else None
    if not root_msg or not message_is_spam(root_msg):
        return False
    for mid in summary.get("msg_ids", ()):
        msg = msgs.get(mid)
        if msg is None:
            continue
        if message_is_spam(msg):
            continue
        if _has_substantive_content(msg):
            return False
    return True
