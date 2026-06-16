"""Lightweight tests for authors.py merge/bridge logic.

Runs without the mbox or pickle cache (importing authors does not parse the
archive). Run directly: ``python test_authors.py``.
"""
from __future__ import annotations

from authors import (
    UA_AUTHOR_NAMES,
    bridge_name,
    distinctive_localpart,
    group_authors,
    merge_key,
    _names_compatible,
)


def test_bridge_maps_known_ua_ids() -> None:
    for uid, name in UA_AUTHOR_NAMES.items():
        email = f"ua-author-{uid}@usenetarchives.gap"
        assert bridge_name(email, "TRUNCATED") == name, uid


def test_bridge_names_have_mergeable_keys() -> None:
    # A curated name only reunites the author if merge_key() accepts it
    # (non-empty) and equals the target Giganews group's key.
    for name in UA_AUTHOR_NAMES.values():
        assert merge_key(name), name


def test_bridge_targets_match_giganews_keys() -> None:
    # Keys confirmed against the generated markdown/authors.md.
    expected = {
        "Pete Dashwood": "pete dashwood",   # #1
        "docdwarf": "docdwarf",             # #29 (UA-gap entries consolidated)
        "Bob Wolfe": "bob wolfe",           # #25
        "Randall Bart": "randall bart",     # #36
        "William Lynch": "william lynch",   # #23
        "Richard": "richard",               # #5 (riplin / Richard Plinston)
    }
    for name in set(UA_AUTHOR_NAMES.values()):
        assert merge_key(name) == expected[name], name


def test_passthrough_for_unmapped_and_real_emails() -> None:
    # Real Giganews emails are never rewritten.
    assert bridge_name("dashwood@enternet.co.nz", "Pete Dashwood") == "Pete Dashwood"
    # UA emails whose ID isn't curated keep their (possibly truncated) name.
    assert bridge_name("ua-author-99999@usenetarchives.gap", "whoever") == "whoever"
    assert bridge_name("ua-author-3041905@usenetarchives.gap", "Bill Klein") == "Bill Klein"


# ---------------------------------------------------------------------------
# Cross-alias reconciliation (issue #8)
# ---------------------------------------------------------------------------

def test_distinctive_localpart_filters_noise() -> None:
    # Distinctive, demunged local-parts pass through.
    assert distinctive_localpart("wmklein@nospam.netcom.com") == "wmklein"
    assert distinctive_localpart("dashwood@removethis.enternet.co.nz") == "dashwood"
    # Generic first-names, roles, synthetic UA, short, and numeric are rejected.
    assert distinctive_localpart("john@example.com") == ""
    assert distinctive_localpart("webmaster@example.com") == ""
    assert distinctive_localpart("ua-author-123@usenetarchives.gap") == ""
    assert distinctive_localpart("bob@example.com") == ""        # < 5 chars
    assert distinctive_localpart("12345@example.com") == ""      # all digits


def test_names_compatible_accepts_real_aliases() -> None:
    # Nickname, initial, bare-first-name, and "Last, First" forms.
    assert _names_compatible("William M. Klein", "Bill Klein", strong=True)
    assert _names_compatible("Pete Dashwood", "Peter E. C. Dashwood", strong=True)
    assert _names_compatible("Richard", "Richard Plinston", strong=False)
    assert _names_compatible("Don Leahy", "Leahy, Don", strong=True)
    assert _names_compatible("Warren Simmons", "Warren G. Simmons", strong=True)


def test_names_compatible_rejects_different_people() -> None:
    # Same surname, different first name — the classic false-merge trap.
    assert not _names_compatible("Doug Miller", "Dean T. Miller", strong=True)
    assert not _names_compatible("Oliver Wong", "Howard Wong", strong=True)
    assert not _names_compatible("Dan Jones", "Kevin Jones", strong=True)
    assert not _names_compatible("Steve Thompson", "William Thompson", strong=True)
    # A bare first name does NOT match on the strong (near-local-part) path.
    assert not _names_compatible("Richard", "Richard Plinston", strong=True)


def test_group_authors_merges_and_separates() -> None:
    # Synthetic archive: two distinct D. Millers (same surname + local-part but
    # different first names) must stay split; a nickname alias must merge.
    def msg(email, name):
        return {"email": email, "display_name": name}

    msgs = {
        "1": msg("wmklein@netcom.com", "William M. Klein"),
        "2": msg("wmklein@ix.netcom.com", "Bill Klein"),
        "3": msg("dmiller@aol.com", "Doug Miller"),
        "4": msg("dmiller@compuserve.com", "Dean Miller"),
    }
    _, email_to_group, _ = group_authors(msgs)
    assert email_to_group["wmklein@netcom.com"] == email_to_group["wmklein@ix.netcom.com"]
    assert email_to_group["dmiller@aol.com"] != email_to_group["dmiller@compuserve.com"]


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"\n{len(fns)} passed")
