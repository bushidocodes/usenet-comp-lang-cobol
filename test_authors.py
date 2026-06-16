"""Lightweight tests for authors.py merge/bridge logic.

Runs without the mbox or pickle cache (importing authors does not parse the
archive). Run directly: ``python test_authors.py``.
"""
from __future__ import annotations

from authors import UA_AUTHOR_NAMES, bridge_name, merge_key


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


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"ok  {fn.__name__}")
    print(f"\n{len(fns)} passed")
