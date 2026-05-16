[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# copies to printer (Fujitsu)

_1 message · 1 participant · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### copies to printer (Fujitsu)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gcp4p$m30$1@news.igs.net>`

```
Further to that last, re the copy routines.  The bug gets sillier and
sillier.  It appears that it is how you change to the directory that affects
whether the device "LPT" gets recognized.  The error exists in both
DOS (command.com) and in the Fujitsu copy routine. here is an example.
The following was grabbed by a screen capture program, and is my
exact test as done.

Q:\>cd areaname.test
Q:\areaname.test>copy test.rpt lpt1:
Path not found - lpt1
        0 file(s) copied
Q:\areaname.test>cd\areana~1.tes
Q:\areaname.test>copy test.rpt lpt1:
        1 file(s) copied
Q:\areaname.test>

Note that it finds the file in both cases, but cannot find the
printer unless the CD command is done with the 8.3 name.
LPT1 is a captured port, and is actually a printer on a server.

copy test.rpt \\beach1\reports

Works in both cases.  It also appears that both cases work
on a local printer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
