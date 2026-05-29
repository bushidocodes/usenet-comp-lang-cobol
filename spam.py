"""Spam detection for the comp.lang.cobol mbox archive.

Drive-by URL-shortener / redirect spam, MLM/scam, porn link spam, and
similar promotional posts with no relation to COBOL. The actual mbox
source is left intact; this module filters spam threads out of the
generated markdown indexes via `archive.thread_summaries()`.

A *message* is spam (`_is_spam_message`) when it matches any of:
  - a known spam host / free-hosting TLD (`SPAM_HOSTS` / `SPAM_HOST_SUFFIXES`);
  - dense dating/adult promotional phrases (`message_is_promo_spam`);
  - pornography subject/body phrases (`message_is_adult_spam`);
  - counterfeit-goods "wholesale/replica" vocabulary (`message_is_wholesale_spam`);
  - the Italian defamation/troll campaign (`message_is_rant_spam`).
A *thread* is spam when its root is spam and no later message has
substantive original *human* content — so threads where humans replied
(even with one-line jokes) are preserved, but bot/troll-flooded threads
(where every "reply" is itself spam) are not. Threads whose root subject is
an unmistakable dating/adult/porn ad (`SPAM_SUBJECT_RE` / `ADULT_SUBJECT_RE`)
are dropped in their entirety.
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
    # Escort/dating spam clusters (added when UA-supplemental scrape surfaced
    # 2015–2020 threads with subjects like "Adult Search", "Married Women
    # Seeking Men", "Find Girlfriend Near Me"). Each domain appears only
    # inside that handful of clearly-spam threads in this archive.
    "vipmodel-escorts.com",
    "jaipurescorts.club",
    "jaipurescortsservice.net.in",
    "juhi-escorts.com",
    "seniorsizzle.com",
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
    # 1997 porn-site spam
    "2bornot2b.com",
    "nasty-schoolgirls.com",
    "dirtyteens.com",
    "fantazma.com",
    # Counterfeit "wholesale/replica" goods spam (2007–2010 crosspost floods)
    "cncircle.com",
    "hng-shoes.com",
    "wholesale-watches.org",
    "cnshoes007.com",
    "stefsclothes.com",
    "niketrade08",       # niketrade08.cn
    "supertradeonline",  # supertradeonline06.com
    "24hour-buy.com",
    "24hours-online.com",
    "watchesblog.cn",
    "sneaker-shop08.com",
    "nbashoe.com",
    "gotoorder.cn",
    "king-trade.cn",
    "trade8.cc",
    # "Earn money from home" / online-gambling spam
    "earnparttimejobs.com",
    "casino.de",
    # More porn-site spam
    "pornoduel.com",
    "servik.com",
    "coolpage.biz",
    "euro-net.com/web/users/hotdate",  # 1996 dating-spam shortcut URL
    # SEO / "services" spam
    "needhelp.net.in",
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
    ".psend.com",      # free hosting — only porn spam in this archive
)

# Subjects that are unmistakable commercial dating/adult advertisements. In
# this archive these match *only* bot-flood spam threads (2020–2022 scrape):
# dozens of one-off fake senders posting near-identical promo bodies under a
# shared subject. No legitimate comp.lang.cobol thread carries such a subject,
# so a thread rooted in one of these is dropped whole — every "reply" is more
# bot promo. Verified to match exactly the four known offenders corpus-wide.
_SPAM_SUBJECT_PATTERNS: tuple[str, ...] = (
    r"\bdating site\b",
    r"\bdating website\b",
    r"\bfind girlfriend\b",
    r"\bgirlfriend near\b",
    r"\bmarried women seeking\b",
    r"\bextra ?marital affair\b",
    r"\bherpes dating\b",
    r"\bstd\b.{0,15}\bdating\b",
    r"\bpositive singles\b",
    r"\bsex personals\b",
    r"\bsingles women dating men\b",
    r"\bwomen seeking men\b",
)
SPAM_SUBJECT_RE = re.compile("|".join(_SPAM_SUBJECT_PATTERNS), re.IGNORECASE)

# Dating/adult promotional phrases. Multi-word so they don't fire on incidental
# single words ("date", "single") in genuine prose. A message dense with these
# (>= _PROMO_PHRASE_MIN distinct hits) is promo spam — used to catch standalone
# dating/porn ads and, crucially, to stop bot promo "replies" from counting as
# the genuine human content that would otherwise keep a spam thread alive.
_PROMO_PHRASES: tuple[str, ...] = (
    "dating site", "dating website", "dating service", "adult dating",
    "online dating", "casual dating", "casual hookup", "casual date",
    "casual encounters", "one night stand", "sex partner", "sex partners",
    "sex dating", "sex personals", "sex encounters", "personal ads",
    "extramarital", "extra marital", "married women seeking", "married personals",
    "married dating", "married but lonely", "discreet relationships",
    "find girlfriend", "find a girlfriend", "positive singles", "discrete dating",
    "discreet dating", "swingers", "adultfriendfinder", "local single",
    "local women", "women seeking men", "men seeking women", "women looking men",
    "girls looking", "find sex", "find local sex", "find a casual",
    "find partner", "adult services", "hookup", "milf", "fuck buddy", "get laid",
    "single women", "singles women", "find love", "soul mate", "meet singles",
    "meet ladies", "herpes dating", "std dating", "naughty", "horny", "escorts",
    "call girls", "sex life", "looking for sex", "get a girlfriend",
)
_PROMO_RE = re.compile(
    "|".join(re.escape(p) for p in _PROMO_PHRASES), re.IGNORECASE
)
# Distinct promo phrases needed to call a single message promotional spam.
_PROMO_PHRASE_MIN = 2

# Unmistakable pornography subject phrases. A single one of these in a SUBJECT
# is spam — verified against every subject in the archive to match only the
# 1997-era porn-site floods and later adult ads, never a genuine c.l.cobol post.
_ADULT_SUBJECT_PATTERNS: tuple[str, ...] = (
    r"\bsex site", r"\bfree sex\b", r"\bteen sex\b", r"\bteenage sex\b",
    r"\bhardcore sex\b", r"\bsex party\b", r"\bsex show\b", r"\blive sex\b",
    r"\blive teen\b", r"\bnude teen", r"\badult xxx\b", r"\bxxx rated\b",
    r"\bxxx site", r"\bsex toys\b", r"\bsucking cock\b", r"\battract girls\b",
    r"\bsex dating\b", r"\badult hookup\b", r"\bsex password\b", r"\bsex scene\b",
    r"\bporno\b", r"\bfree porn\b", r"\bporn site", r"\bsex personals\b",
    r"\bgirls for (?:sex|fuck)\b", r"\binstant sex appeal\b", r"\bcocksucking\b",
    r"\banal teen\b", r"\bhottest adult\b", r"\bfree xxx\b", r"\bsex movies\b",
    r"\bgroupsex\b", r"\bsexvideos\b", r"\bsex videos\b",
)
ADULT_SUBJECT_RE = re.compile("|".join(_ADULT_SUBJECT_PATTERNS), re.IGNORECASE)

# Multiword pornography phrases for *body* detection. Two distinct hits mark a
# message as porn spam. Multiword on purpose: genuine OT/COBOL threads that
# mention "sex"/"nude"/"porn" in passing don't stack commercial porn phrases,
# so a single ambiguous word never trips the filter.
_ADULT_BODY_PHRASES: tuple[str, ...] = (
    "sex site", "sex sites", "free sex", "teen sex", "teenage sex", "hardcore sex",
    "sex party", "sex show", "live sex", "live video sex", "nude teen", "nude teens",
    "adult xxx", "xxx rated", "xxx material", "xxx chat", "free xxx", "sex toys",
    "sucking cock", "sucking dick", "attract girls", "attract women", "sex dating",
    "adult hookup", "sex scene", "free porn", "porn site", "porn videos",
    "flash porn", "sex videos", "sex movies", "nude pics", "nude celebs",
    "busty women", "horny girls", "anal teen", "cocksucking", "schoolgirls",
    "groupsex", "sexvideos",
)
_ADULT_BODY_RE = [
    re.compile(r"\b" + re.escape(p) + r"\b", re.IGNORECASE) for p in _ADULT_BODY_PHRASES
]
_ADULT_BODY_MIN = 2

# Counterfeit-goods "wholesale/replica" spam (2007–2010): crossposted floods
# hawking knockoff Nike/Gucci/LV/etc. with "paypal payment" / "free shipping".
# These bodies repeat the vocabulary dozens of times, so we count *total*
# occurrences and require several — an incidental "wholesale price" in a real
# post never gets close.
_WHOLESALE_PHRASES: tuple[str, ...] = (
    "wholesale", "paypal payment", "free shipping", "replica", "nike shox",
    "air max", "air force one", "ed hardy", "louis vuitton", "lacoste",
    "timberland boots", "ugg boots", "jordan shoes", "brand sports shoes",
    "nike shoes", "jerseys", "handbag",
)
_WHOLESALE_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(p) for p in _WHOLESALE_PHRASES) + r")\b",
    re.IGNORECASE,
)
_WHOLESALE_MIN = 4

# Vocabulary of a long-running Italian defamation/troll campaign crossposted
# into comp.lang.cobol (2015 + 2021–2022): all-caps rants accusing public
# figures (Berlusconi/Mediaset, bankers, lawyers) of laundering mafia money,
# pedophilia, etc. These Italian profanity/defamation terms never appear in a
# legitimate English-language COBOL post; the campaign stacks many per message.
# A message with >= _RANT_PHRASE_MIN *distinct* terms is flagged — verified to
# catch all 54 campaign messages corpus-wide with zero false positives, whereas
# a single term (e.g. "bastardi" inside "bastardized") would not.
_RANT_PHRASES: tuple[str, ...] = (
    "figlio di puttana", "figli di puttana", "figlio di troia", "figli di troia",
    "figlio di troiona", "figli di troiona", "figlio di troiaccia", "di troiaccia",
    "figlio di pedofilo", "figli di pedofili", "pedofilomosessuale", "pedofilo",
    "pederasta", "pedofili", "bastardo", "bastardi", "assassino", "assassini",
    "ricicla", "riciclaggio", "soldi mafiosi", "montagne di soldi", "soldi sporchi",
    "mafia e massoneria", "massoneria", "massone", "massona", "ndranghetista",
    "ndrangheta", "ciuccia cazzi", "cazzi di cavallo", "sborrato", "incula",
    "ninfomane", "cocainomane", "criminalissim", "truffatore",
    "puttana", "troia", "mafiaset", "mediaforeurope",
)
# Word-boundary anchored so short terms don't substring-match English words
# ("bastardi" in "bastardized", "troia" in larger tokens, etc.).
_RANT_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(p) for p in _RANT_PHRASES) + r")\b",
    re.IGNORECASE,
)
# Distinct rant terms needed to call a single message defamation-campaign spam.
_RANT_PHRASE_MIN = 2

# Off-topic religious-proselytizing (dawah) spam from a serial crossposter who
# flooded the group with "Introducing Islam" / "Concept of God" / "Why did
# Prophet Muhammad..." posts under throwaway handles. Caught two ways:
#  - the throwaway-email pattern (a 2-letter prefix repeated 3x with digits:
#    bv8bv8bv8, bv5bv5bv5, cv33cv33cv33) — matches only this spammer corpus-wide;
#  - a proselytizing SUBJECT plus a body dense with religious terms (catches the
#    same posts re-scraped under anonymized usenetarchives handles).
# A genuine OT religious tangent in a COBOL thread is not affected: the subject
# anchor + density requirement keeps it from firing, and even when a regular
# *replies* to one of these spam threads, only the spam-rooted thread is dropped.
_DAWAH_HANDLE_RE = re.compile(r"\b([a-z]{2})\d+\1\d+\1\d*\b", re.IGNORECASE)
_DAWAH_SUBJECT_RE = re.compile(
    r"\b(islam|muslim|muhammad|qur'?an|allah|prophet|monotheism|oneness of god"
    r"|the messenger|peace be upon|dawah|god in islam|introducing islam)\b",
    re.IGNORECASE,
)
_DAWAH_BODY_PHRASES: tuple[str, ...] = (
    "islam", "muslim", "muhammad", "qur'an", "quran", "allah", "prophet",
    "peace be upon him", "the messenger of allah", "oneness", "worship god",
    "non-muslims", "non muslims", "verily", "almighty", "glory be",
)
_DAWAH_BODY_RE = [re.compile(r"\b" + p + r"\b", re.IGNORECASE) for p in _DAWAH_BODY_PHRASES]
_DAWAH_BODY_MIN = 4

# Reply-prefix detector. The dawah *content* rule fires only on original posts,
# never on replies — so a regular who answers one of these threads (inheriting
# the religious subject and quoting the post) is not mistaken for the spammer
# and can keep a thread with genuine human debate alive.
_REPLY_PREFIX_RE = re.compile(r"^\s*(re|fw|fwd|aw|sv|antw|odp|res|rif)\s*:", re.IGNORECASE)

# Minimum words of substantive content for a message to "count" as a real reply.
_SUBSTANTIVE_WORD_MIN = 3

_WORD_RE = re.compile(r"\b[a-zA-Z]{3,}\b")

# Real Usenet/email quote lines start at column 0 with one or more `>` (or
# `|`, or `›` for UsenetArchives.com gap-period scrapes) followed by a space
# — `> reply text`, `›› grandparent`. Spam decoration like `   > http://link <`
# or `>>> link <<<` has leading whitespace (or no trailing space after the
# chevrons), so it stays as part of the original message content.
_QUOTE_LINE_RE = re.compile(r"^[>|›]+(\s|$)")

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


def message_is_promo_spam(entry: dict) -> bool:
    """True if a message is dense with dating/adult promotional phrases.

    Counts *distinct* promo phrases in the non-quoted text; >= 2 marks the
    message as an ad. Two-phrase minimum keeps a stray "I went on a date last
    single weekend" in a genuine post from tripping the filter, while the
    relentlessly on-message bot bodies in the 2020–2022 dating-spam threads
    clear it easily.
    """
    body = entry.get("body") or ""
    if not body:
        return False
    text = _non_quoted(body)
    seen = {m.group(0).lower() for m in _PROMO_RE.finditer(text)}
    return len(seen) >= _PROMO_PHRASE_MIN


def message_is_rant_spam(entry: dict) -> bool:
    """True if a message is the Italian defamation/troll campaign spam.

    Counts *distinct* campaign terms (`_RANT_PHRASES`) in the subject plus the
    non-quoted body; >= 2 marks it spam. The subject is included because the
    rant is usually right there in the header (and carries through "Re:"
    replies), while requiring two distinct terms keeps an incidental single
    foreign word from tripping the filter.
    """
    text = (entry.get("subject") or "") + "\n" + _non_quoted(entry.get("body") or "")
    seen = {m.group(0).lower() for m in _RANT_RE.finditer(text)}
    return len(seen) >= _RANT_PHRASE_MIN


def message_is_adult_spam(entry: dict) -> bool:
    """True if a message is pornography spam.

    Either an unmistakable porn phrase in the subject (`ADULT_SUBJECT_RE`) or
    >= 2 distinct multiword porn phrases across the subject + non-quoted body.
    The multiword body requirement avoids flagging genuine OT threads that
    merely mention "sex"/"nude"/"porn" once in passing.
    """
    subject = entry.get("subject") or ""
    if ADULT_SUBJECT_RE.search(subject):
        return True
    text = subject + "\n" + _non_quoted(entry.get("body") or "")
    return sum(1 for rx in _ADULT_BODY_RE if rx.search(text)) >= _ADULT_BODY_MIN


def message_is_wholesale_spam(entry: dict) -> bool:
    """True if a message is counterfeit-goods "wholesale/replica" spam.

    Counts *total* occurrences of the knockoff-retail vocabulary in the subject
    + non-quoted body; these floods repeat it many times, so a high count is a
    clean signal that an incidental "wholesale price file" mention never hits.
    """
    text = (entry.get("subject") or "") + "\n" + _non_quoted(entry.get("body") or "")
    return len(_WHOLESALE_RE.findall(text)) >= _WHOLESALE_MIN


def message_is_dawah_spam(entry: dict) -> bool:
    """True if a message is the serial religious-proselytizing crossposter.

    Either the throwaway-handle email pattern, or a proselytizing subject plus a
    body dense with religious terms (catches the anonymized re-scrapes).
    """
    email = entry.get("email") or ""
    local = email.split("@", 1)[0] if email else ""
    if _DAWAH_HANDLE_RE.search(local):
        return True
    if (entry.get("display_name") or "").strip().upper() == "BV BV":
        return True
    subject = entry.get("subject") or ""
    # Content rule applies only to original posts — never to replies, so genuine
    # human debate in these threads is preserved.
    if _REPLY_PREFIX_RE.match(subject):
        return False
    if not _DAWAH_SUBJECT_RE.search(subject):
        return False
    text = subject + "\n" + _non_quoted(entry.get("body") or "")
    return sum(1 for rx in _DAWAH_BODY_RE if rx.search(text)) >= _DAWAH_BODY_MIN


def message_is_misc_spam(entry: dict) -> bool:
    """Distinctive single-campaign spam signatures with no broader pattern.

    Each test is a fingerprint specific enough that it only ever appears in the
    named campaign — not a general heuristic. Add new ones here as serial spam
    is identified.
    """
    text = (
        (entry.get("subject") or "") + "\n" + _non_quoted(entry.get("body") or "")
    ).lower()
    # Textbook "solutions manual" reseller (handle: solutionsmanual2019@gmail).
    if "solutionsmanual" in text:
        return True
    # "Maan Al Sanea" money-laundering YouTube-video spam campaign.
    if "maan alsaan" in text or "maan al sanea" in text:
        return True
    # Detox-tea / weight-loss spam.
    if "detox tea" in text and "belly fat" in text:
        return True
    # "Heather Kennett / Con Zacharakis" harassment-defamation campaign.
    if "heather kennett" in text and "con zacharakis" in text:
        return True
    return False


def subject_is_spam(subject: str) -> bool:
    """True if a subject is an unmistakable dating/adult/porn advertisement.

    Such subjects appear only on spam in this archive, so a thread rooted in
    one is dropped whole (every reply shares the subject and is more spam).
    """
    if not subject:
        return False
    return bool(SPAM_SUBJECT_RE.search(subject) or ADULT_SUBJECT_RE.search(subject))


def _is_spam_message(entry: dict) -> bool:
    """True if a single message matches any message-level spam signal."""
    return (
        message_is_spam(entry)
        or message_is_promo_spam(entry)
        or message_is_rant_spam(entry)
        or message_is_adult_spam(entry)
        or message_is_wholesale_spam(entry)
        or message_is_dawah_spam(entry)
        or message_is_misc_spam(entry)
    )


def _has_substantive_content(entry: dict) -> bool:
    """True if the message has original (non-quoted, non-header) prose."""
    body = entry.get("body") or ""
    text = _non_quoted(body)
    text = _QUOTE_HEADER_RE.sub("", text)
    return len(_WORD_RE.findall(text)) >= _SUBSTANTIVE_WORD_MIN


def thread_is_spam(summary: dict, msgs: dict) -> bool:
    """True if the entire thread can be dropped from generated indexes.

    Conservatively keeps any thread where at least one message has
    substantive original *human* content — even a one-line joke reply
    counts — so that human engagement is preserved even when the inciting
    post was spam. A reply that is itself spam (any `_is_spam_message`
    signal: known host, dating/adult promo, porn, counterfeit-goods, or the
    Italian defamation rant) does not count as human, which prevents
    bot/troll-flooded threads from rescuing themselves.

    Threads whose root subject is an unmistakable dating/adult/porn ad are
    dropped outright: in this archive those subjects appear only on spam,
    and every reply shares the subject and is more spam.
    """
    root_id = summary.get("root")
    root_msg = msgs.get(root_id) if root_id else None
    if not root_msg:
        return False
    if subject_is_spam(summary.get("subject", "")):
        return True
    if not _is_spam_message(root_msg):
        return False
    for mid in summary.get("msg_ids", ()):
        msg = msgs.get(mid)
        if msg is None:
            continue
        if _is_spam_message(msg):
            continue
        if _has_substantive_content(msg):
            return False
    return True
