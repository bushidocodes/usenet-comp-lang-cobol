"""Top-author profiles for the comp.lang.cobol archive.

Aggregates by *display name* when possible (so "Pete Dashwood" posting from
three different addresses over a decade is one entry, not three) and falls
back to per-email entries when the display name is empty/ambiguous.

Emits `markdown/authors.md`.
"""
from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict

from archive import OUT, date_key, filter_msgs, parse_archive, thread_summaries
from utils import md_escape, trim

TOP_AUTHORS = 100
TOP_THREADS_PER_AUTHOR = 10

# Synthetic email minted by scrape_gap.py for UA.com-scraped authors.
UA_EMAIL_RE = re.compile(r"^ua-author-(\d+)@usenetarchives\.gap$")

# Curated bridge: UA.com author ID -> canonical display name (issue #28).
#
# UA.com strips emails and often truncates display names ("rtw...", "docd...",
# "dashwood"), so a long-running poster splits into a UA-gap entry and a
# separate Giganews entry. merge_key() can't reunite them — the truncated name
# normalizes to a different key than the real one. This map overrides the UA
# author's canonical name so it merges into the right group.
#
# The value MUST be a name whose merge_key() equals the target Giganews group's
# key (i.e. the name that group already canonicalizes to), or the merge won't
# happen. Each entry below was confirmed against the generated authors.md:
# matching email local-parts, overlapping active spans, and topic fingerprint.
UA_AUTHOR_NAMES = {
    # Pete Dashwood — dashwood@enternet.co.nz; the 2013-2022 COBOL-advocacy tail
    # (#27 "dashwood") split across four UA IDs.
    "14501808": "Pete Dashwood",
    "2154790": "Pete Dashwood",
    "6590328": "Pete Dashwood",
    "14256666": "Pete Dashwood",
    # docdwarf — docdwarf@erols.com; "docd..." (#55), 1996-1998, merges into #45.
    "514273": "docdwarf",
    # Bob Wolfe — rtwolfe@flexus.com; "rtw..." (#83), per issue #28, merges into #31.
    "6550399": "Bob Wolfe",
    # Randall Bart — "randallbart" (#80), 1997-1998, merges into #57 "Randall Bart".
    "464041": "Randall Bart",
    # William "Bill" Lynch — wblynch@att.net; "bill lynch" (#64), merges into #30.
    "92065": "William Lynch",
    # Richard Plinston — riplin@azonic.co.nz; "rip..." (#97), merges into #5 "Richard".
    "6589535": "Richard",
}


def bridge_name(email: str, fallback: str) -> str:
    """Map a synthetic UA.com author email to its curated canonical name.

    Returns ``fallback`` unchanged for non-UA emails and for UA author IDs
    that aren't in the bridge map. See ``UA_AUTHOR_NAMES`` and issue #28.
    """
    m = UA_EMAIL_RE.match(email)
    if m:
        return UA_AUTHOR_NAMES.get(m.group(1), fallback)
    return fallback


def best_display_name(name_counts: Counter) -> str:
    for name, _ in name_counts.most_common():
        if name and not name.startswith("<"):
            return name
    return ""


def merge_key(name: str) -> str:
    """Canonical key for matching the same author across multiple emails.

    Returns "" if the name is too short/empty to be a reliable identifier.
    """
    if not name:
        return ""
    n = re.sub(r"[^\w\s]", "", name.lower())
    n = re.sub(r"\s+", " ", n).strip()
    # Drop very short names; high false-merge risk
    if len(n) < 5:
        return ""
    return n


def slug(s: str) -> str:
    h = hashlib.md5(s.encode("utf-8")).hexdigest()[:10]
    return f"a-{h}"


# ---------------------------------------------------------------------------
# Cross-alias reconciliation (issue #8)
#
# merge_key() above groups a person's emails by canonical display name. That
# catches the easy cases but misses aliases that normalize differently:
# "Bill Klein" vs "William M. Klein", "Leahy, Don" vs "Don Leahy", or the same
# handle posted from several addresses with no display name at all.
#
# The reliable signal is the *intersection* of two weak ones: a shared
# distinctive email local-part AND name agreement. Neither alone is safe —
# common given-name local-parts (john@, paul@) and shared/role addresses
# collide across unrelated people, and display-name match alone merges
# different "John Smith"s. So we reconcile primary groups only when both agree.
# ---------------------------------------------------------------------------

# Local-parts that recur across unrelated people: roles, anonymous remailers,
# and the most common given names in this archive. Never a merge signal.
GENERIC_LOCALPARTS = {
    "info", "admin", "sales", "support", "webmaster", "postmaster", "mail",
    "email", "news", "newsreader", "usenet", "nobody", "anonymous", "anon",
    "remailer", "mixmaster", "me", "myself", "test", "user", "guest", "root",
    "contact", "office", "service", "abuse", "noreply", "list", "owner",
    "john", "paul", "chris", "steve", "mike", "dave", "david", "mark", "jim",
    "james", "bob", "tom", "jerry", "bill", "ken", "don", "gary", "rich",
    "richard", "peter", "scott", "robert", "william", "michael", "brian",
    "kevin", "alan", "dan", "joe", "frank", "george", "andy", "pete",
}
# Name suffixes (collapsed) to drop before keying on a surname.
NAME_SUFFIXES = {"jr", "sr", "ii", "iii", "iv", "cdp", "phd", "esq", "md",
                 "msc", "cpa", "bsc", "ba", "cissp"}
# Anti-spam decoration spliced into local-parts; stripped before comparison.
MUNGE_TOKENS = ("nospam", "no-spam", "removethis", "spam", "invalid", "n0spam",
                "inospam", "dontspam", "notspam", "deletethis", "remove")


def _collapse(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _name_tokens(name: str) -> list[str]:
    """Lowercased name tokens, suffix-stripped, with 'Last, First' un-inverted."""
    n = name.strip()
    if "," in n:
        parts = [p.strip() for p in n.split(",") if p.strip()]
        parts = [p for p in parts if _collapse(p) not in NAME_SUFFIXES]
        if len(parts) == 2:  # genuine "Last, First" inversion
            n = f"{parts[1]} {parts[0]}"
    toks = re.sub(r"[^\w\s]", " ", n.lower()).split()
    return [t for t in toks if t not in NAME_SUFFIXES]


def _is_weak_name(name: str) -> bool:
    """A name with no human content: empty, email-derived, or a bracket dump."""
    return (not name) or ("@" in name) or name.startswith("<")


def _name_core(name: str) -> str:
    """Comparison core: the embedded local-part for weak names, else collapsed."""
    if "@" in name:
        return _collapse(name.split("@", 1)[0])
    return "".join(_name_tokens(name))


def distinctive_localpart(email: str) -> str:
    """Demunged email local-part, or "" if it's not a reliable identity signal.

    Synthetic UA.com addresses are excluded (each numeric ID is already a
    distinct author), as are short, purely numeric, and generic local-parts.
    """
    if not email or "usenetarchives.gap" in email:
        return ""
    lp = email.split("@", 1)[0].lower() if "@" in email else email.lower()
    for m in MUNGE_TOKENS:
        lp = lp.replace(m, "")
    lp = re.sub(r"[^a-z0-9]", "", lp)
    if len(lp) < 5 or lp.isdigit() or lp in GENERIC_LOCALPARTS:
        return ""
    return lp


def _lev_le1(a: str, b: str) -> bool:
    """True if edit distance(a, b) <= 1 (cheap, no full matrix)."""
    if a == b:
        return True
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la == lb:  # at most one substitution
        return sum(x != y for x, y in zip(a, b)) == 1
    # one insertion/deletion: a is the shorter
    if la > lb:
        a, b = b, a
    i = j = diff = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            diff += 1
            j += 1
            if diff > 1:
                return False
    return True


# Common nickname → formal given name, both directions resolved to the formal
# form. Conservative and well-known only; a wrong entry could mis-merge, though
# a shared distinctive local-part is still required alongside.
NICKNAMES = {
    "bill": "william", "billy": "william", "will": "william", "willy": "william",
    "bob": "robert", "bobby": "robert", "rob": "robert", "robbie": "robert",
    "dick": "richard", "rick": "richard", "ricky": "richard", "rich": "richard",
    "jim": "james", "jimmy": "james", "jamie": "james",
    "tom": "thomas", "tommy": "thomas",
    "mike": "michael", "mick": "michael", "mickey": "michael",
    "dave": "david", "davey": "david",
    "joe": "joseph", "joey": "joseph",
    "chuck": "charles", "charlie": "charles", "chas": "charles",
    "dan": "daniel", "danny": "daniel",
    "don": "donald", "donnie": "donald",
    "pete": "peter", "ken": "kenneth", "kenny": "kenneth",
    "ed": "edward", "eddie": "edward", "ned": "edward",
    "steve": "steven", "stephen": "steven", "stevie": "steven",
    "greg": "gregory", "jeff": "jeffrey", "tony": "anthony", "andy": "andrew",
    "matt": "matthew", "chris": "christopher", "nick": "nicholas",
    "sam": "samuel", "ben": "benjamin", "alex": "alexander", "ron": "ronald",
    "larry": "lawrence", "pat": "patrick", "phil": "philip", "ray": "raymond",
    "russ": "russell", "doug": "douglas", "vince": "vincent", "gabe": "gabriel",
}


def _first_compatible(fa: str, fb: str) -> bool:
    """Could two first names belong to the same person?"""
    na, nb = NICKNAMES.get(fa, fa), NICKNAMES.get(fb, fb)
    if na == nb:
        return True
    if len(fa) == 1:  # single initial
        return fb.startswith(fa)
    if len(fb) == 1:
        return fa.startswith(fb)
    # Unlisted diminutive: one is a prefix of the other ("jon"/"jonathan").
    if len(na) >= 3 and len(nb) >= 3 and (na.startswith(nb) or nb.startswith(na)):
        return True
    return False


def _names_compatible(a: str, b: str, *, strong: bool) -> bool:
    """Could names a and b be the same person? See module header.

    strong=True (used when only the local-part is *near*-matching) requires a
    full-name match; strong=False (exact local-part) also trusts weak-vs-weak
    and bare-first-name matches.
    """
    if _is_weak_name(a) or _is_weak_name(b):
        # No human name on one side: rely on the shared local-part. Only the
        # exact-local-part caller (strong=False) reaches a merge here.
        ka, kb = _name_core(a), _name_core(b)
        return (not strong) and bool(ka) and ka == kb
    ta, tb = _name_tokens(a), _name_tokens(b)
    if not ta or not tb:
        return False
    if "".join(ta) == "".join(tb):
        return True
    # A bare first name ("Richard") vs the full form ("Richard Plinston").
    if not strong and len(ta) == 1 and len(ta[0]) >= 4 and ta[0] in (tb[0], tb[-1]):
        return True
    if not strong and len(tb) == 1 and len(tb[0]) >= 4 and tb[0] in (ta[0], ta[-1]):
        return True
    # Two full names: same surname is not enough (there's more than one
    # "* Jones") — the first names must also be compatible.
    if len(ta) >= 2 and len(tb) >= 2 and len(ta[-1]) >= 3 and ta[-1] == tb[-1]:
        return _first_compatible(ta[0], tb[0])
    return False


def _reconcile(primary, email_to_canonical, email_msgs):
    """Union primary group keys that are the same person; return pkey -> rep."""
    parent = {pk: pk for pk in primary}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    # Representative (most-prolific) canonical name per primary group.
    pname = {
        pk: email_to_canonical.get(max(emails, key=lambda e: email_msgs.get(e, 0)), "")
        for pk, emails in primary.items()
    }

    # Pass 1: exact shared distinctive local-part + compatible names.
    lp_to_pks: dict[str, set] = defaultdict(set)
    for pk, emails in primary.items():
        for e in emails:
            lp = distinctive_localpart(e)
            if lp:
                lp_to_pks[lp].add(pk)
    for pks in lp_to_pks.values():
        pks = list(pks)
        if len(pks) < 2:
            continue
        # A local-part shared by >2 distinct real surnames is a role/placeholder
        # address (e.g. a shared newsreader login), not one person.
        surnames = {
            _name_tokens(pname[pk])[-1]
            for pk in pks
            if not _is_weak_name(pname[pk]) and _name_tokens(pname[pk])
        }
        if len(surnames) > 2:
            continue
        for i in range(len(pks)):
            for j in range(i + 1, len(pks)):
                if _names_compatible(pname[pks[i]], pname[pks[j]], strong=False):
                    union(pks[i], pks[j])

    # Pass 2: same surname + near-identical local-part (catches "jgavan" vs
    # "jjgavan"). Bucketed by surname so it stays cheap and high-precision.
    sur_to_pks: dict[str, list] = defaultdict(list)
    for pk in primary:
        toks = _name_tokens(pname[pk])
        if (
            toks
            and len(toks[-1]) >= 4
            and toks[-1] not in GENERIC_LOCALPARTS
            and not _is_weak_name(pname[pk])
        ):
            sur_to_pks[toks[-1]].append(pk)
    for pks in sur_to_pks.values():
        if len(pks) < 2:
            continue
        lps = {
            pk: [lp for e in primary[pk] if (lp := distinctive_localpart(e))]
            for pk in pks
        }
        for i in range(len(pks)):
            for j in range(i + 1, len(pks)):
                a, b = pks[i], pks[j]
                if find(a) == find(b):
                    continue
                # Same surname is the bucket; the near local-part and the first
                # name must both agree before we merge two full names.
                if _names_compatible(pname[a], pname[b], strong=True) and any(
                    _lev_le1(la, lb) for la in lps[a] for lb in lps[b]
                ):
                    union(a, b)

    # Pick each cluster's representative: the primary group with the most msgs.
    pkey_msgs = {
        pk: sum(email_msgs.get(e, 0) for e in emails)
        for pk, emails in primary.items()
    }
    clusters: dict[str, list] = defaultdict(list)
    for pk in primary:
        clusters[find(pk)].append(pk)
    rep = {}
    for members in clusters.values():
        best = max(members, key=lambda pk: pkey_msgs[pk])
        for pk in members:
            rep[pk] = best
    return rep


def group_authors(msgs: dict):
    """Group a person's many email addresses into one entry.

    Shared by authors.py and export_json.py so the Markdown profiles and the
    website agree. Returns ``(groups, email_to_group, email_to_canonical)``:
      * groups: group key -> list of member emails
      * email_to_group: email -> group key
      * email_to_canonical: email -> canonical (UA-bridged) display name
    """
    email_names: dict[str, Counter] = defaultdict(Counter)
    for entry in msgs.values():
        email = entry.get("email", "")
        if not email:
            continue
        email_names[email][entry.get("display_name", "")] += 1
    email_to_canonical = {
        e: bridge_name(e, best_display_name(c)) for e, c in email_names.items()
    }
    email_msgs = {e: sum(c.values()) for e, c in email_names.items()}

    # Primary grouping by display-name merge key (unmergeable names → own group).
    primary: dict[str, list] = defaultdict(list)
    for email, name in email_to_canonical.items():
        primary[merge_key(name) or f"__email__{email}"].append(email)

    # Reconcile aliases that the name key alone missed, then relabel to reps.
    rep = _reconcile(primary, email_to_canonical, email_msgs)
    groups: dict[str, list] = defaultdict(list)
    email_to_group: dict[str, str] = {}
    for pkey, emails in primary.items():
        gk = rep[pkey]
        groups[gk].extend(emails)
        for e in emails:
            email_to_group[e] = gk
    return groups, email_to_group, email_to_canonical


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)
    summary_by_root = {s["root"]: s for s in summaries}
    msgs = filter_msgs(msgs, summaries)

    # Group each person's emails into one entry (display-name merge + email
    # local-part reconciliation; see group_authors and issues #8/#28).
    groups, email_to_group, _ = group_authors(msgs)

    # Aggregate stats per group
    group_msgs: dict[str, int] = defaultdict(int)
    group_threads: dict[str, set] = defaultdict(set)
    group_started: dict[str, set] = defaultdict(set)
    group_first: dict[str, tuple] = {}
    group_last: dict[str, tuple] = {}
    group_emails: dict[str, set] = defaultdict(set)
    group_name_counts: dict[str, Counter] = defaultdict(Counter)

    for key, emails in groups.items():
        group_emails[key].update(emails)

    for mid, entry in msgs.items():
        email = entry["email"]
        if not email:
            continue
        gk = email_to_group[email]
        group_msgs[gk] += 1
        root = root_cache[mid]
        group_threads[gk].add(root)
        group_name_counts[gk][entry["display_name"]] += 1
        if root in msgs and msgs[root]["email"] == email and msgs[root]["id"] == root:
            group_started[gk].add(root)
        dt = entry["dt"]
        if dt is not None:
            sk = date_key(dt)
            if gk not in group_first or sk < group_first[gk][0]:
                group_first[gk] = (sk, entry["ym"])
            if gk not in group_last or sk > group_last[gk][0]:
                group_last[gk] = (sk, entry["ym"])

    # Per-group, per-thread message counts (for "top threads")
    group_thread_msgs: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    group_email_msgs: dict[str, Counter] = defaultdict(Counter)
    for mid, entry in msgs.items():
        email = entry["email"]
        if not email:
            continue
        gk = email_to_group[email]
        group_thread_msgs[gk][root_cache[mid]] += 1
        group_email_msgs[gk][email] += 1

    # Rank groups by message count
    ranked = sorted(group_msgs.items(), key=lambda kv: -kv[1])
    top = ranked[:TOP_AUTHORS]

    print(f"Writing top {len(top)} authors (after display-name merging)...")
    out = OUT / "authors.md"
    with out.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Years](years.md) · [Stats](stats.md) · [Subjects](subjects.md) · [Links](links.md)\n\n")
        f.write("# comp.lang.cobol — Top Authors\n\n")
        f.write(
            f"The {len(top)} most prolific posters by message count. "
            "Aggregated by display name across email addresses where possible "
            "(so the same person posting from multiple accounts merges into one entry). "
            "Bot/recruiter accounts will still appear — heavy raw count doesn't imply signal.\n\n"
        )

        # Quick reference
        f.write("## Quick reference\n\n")
        f.write(
            "| # | Author | Msgs | Threads | Started | Aliases | Active |\n"
            "|---:|---|---:|---:|---:|---:|---|\n"
        )
        for rank, (gk, _msg_count) in enumerate(top, 1):
            name = best_display_name(group_name_counts[gk]) or "—"
            tcount = len(group_threads[gk])
            scount = len(group_started[gk])
            aliases = len(group_emails[gk])
            first_ym = group_first.get(gk, (None, "?"))[1]
            last_ym = group_last.get(gk, (None, "?"))[1]
            span = first_ym if first_ym == last_ym else f"{first_ym} → {last_ym}"
            anchor = slug(gk)
            f.write(
                f"| {rank} | [{md_escape(trim(name, 40))}](#{anchor}) | "
                f"{_msg_count:,} | {tcount:,} | {scount:,} | {aliases} | {span} |\n"
            )
        f.write("\n")

        # Per-author detail
        for rank, (gk, msg_count) in enumerate(top, 1):
            name = best_display_name(group_name_counts[gk]) or gk
            tcount = len(group_threads[gk])
            scount = len(group_started[gk])
            first_ym = group_first.get(gk, (None, "?"))[1]
            last_ym = group_last.get(gk, (None, "?"))[1]
            span = first_ym if first_ym == last_ym else f"{first_ym} → {last_ym}"
            anchor = slug(gk)

            f.write(f"## #{rank}. {md_escape(name)} <a id='{anchor}'></a>\n\n")

            # Aliases (sorted by message count under each email)
            alias_list = ", ".join(
                f"`{md_escape(e)}` ({c:,})"
                for e, c in group_email_msgs[gk].most_common()
            )
            f.write(f"{alias_list}\n\n")

            f.write(
                f"**{msg_count:,} messages** in **{tcount:,} threads** "
                f"({scount:,} started) · active **{span}**\n\n"
            )

            # Other display names this person used
            other_names = [
                n for n, _ in group_name_counts[gk].most_common(5)
                if n and n != name
            ]
            if other_names:
                trimmed = ", ".join(md_escape(trim(n, 50)) for n in other_names[:3])
                f.write(f"_Also posted as: {trimmed}._\n\n")

            top_thread_roots = sorted(
                group_thread_msgs[gk].items(),
                key=lambda kv: -kv[1],
            )[:TOP_THREADS_PER_AUTHOR]
            if top_thread_roots:
                f.write("**Top threads:**\n\n")
                for root, n in top_thread_roots:
                    s = summary_by_root.get(root)
                    if not s:
                        continue
                    label = trim(s["subject"])
                    link = f"[{md_escape(label)}](threads/{s['anchor']}.md)"
                    started_marker = " · _started_" if root in group_started[gk] else ""
                    f.write(f"- {link} — **{n}** of {s['count']} msgs{started_marker}\n")
                f.write("\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
