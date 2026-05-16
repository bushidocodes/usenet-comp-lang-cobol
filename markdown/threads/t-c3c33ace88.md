[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# On DECLARATIVES

_1 message · 1 participant · 2004-05_

---

### On DECLARATIVES

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-12T19:22:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XPuoc.17535$V97.16262@newsread1.news.pas.earthlink.net>`

```
Just a new thread based on a comment in another thread on my view of
DECLARATIVES.

1) DECLARATIVES (similar to PL/I on-units) are BY DEFINITION "non-structured"
code.  They ALWAYS act like a "go to" and only some of them have options to
"return" whence you came.  This leads to all the POSSIBLE problems with
non-structured code.  (Unlike earlier Standards - I think - with the '85
Standard and later you can "branch" out of declaratives - so spaghetti code is
"fully" supported)

2) DECLARATIVES are (IMHO) a *great* (under-used) way to write "generic" error
handling routines.  This can be brought into all your shop's programs via a
"simple" COPY statement.  (Generic "error handling routines" can provide for
"ease" in problem resolution and "known to all" expectations.)

3)  There are SOME things which can *only* be handled by DECLARATIVES
  - SORT/MERGE I/O errors
  - many "exceptional" Report Writer ("normal") processing situations
 - *ALL* of the "new" common exception handling situations (ISO 2002)

4) To the best of my knowledge, there are NO "things" (of the I/O or similar
error/exception category)  that can be handled in-line that cannot ALSO be
handled via DECLARATIVES - *if* (BIG IF) you don't need to "recover" and restart
processing at the next COBOL statement.  (With the ISO 2002 RESUME statement
some - but not IMHO all - situations allow for "resume" processing)

5) Creating *specific* error processing/recovery logic in DECLARATIVES is
"clumsy" at best and difficult to maintain.  At worst it is almost
incomprehensible and is NOT something that I would like to deal with at 3 a.m.

   ***

Bottom-Line:
  If you think you will ever have an ISO 2002 conforming compiler (or one with
"common exception handling") get to know "and love" DECLARATIVES.
  Creation and use of "shop standard" GENERIC declaratives for "un-handled" I/O
problems is something that I *do* recommend.
  Use "in-line" File Status checking for "file specific" (and/or program
specific) application processing.

  ***

I hope this "clarifies" my (personal) position on DECLARATIVES.  (Can we say
"right tool for the right job"?)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
