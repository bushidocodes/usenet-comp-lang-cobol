[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Largest Progran was: what is the avarage length of cobol programs

_1 message · 1 participant · 1999-12_

---

### Re: Largest Progran was: what is the avarage length of cobol programs

- **From:** cagoodey@home.com (Chris A. Goodey)
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385d7fc5.10924241@news>`
- **References:** `<82gbnr$bb2$1@news.netvision.net.il> <82n91g$ij5$1@hermes.enternet.co.nz> <384F2041.5C7823A8@home.com> <82pii90209t@enews2.newsguy.com> <38512C2B.928D03F9@prodigy.net> <MPG.12baf51f290d9884989686@news.transport.com> <82rm8e$gd2$1@nntp5.atl.mindspring.net> <3851D425.F551C640@worldnet.att.net>`

```
The latest HP3000 Cobol compiler was enhanced to be able to handle
200,000 plus lines of code in a single compilation unit. The older
limit was closer to 100,000 lines. 

Of course, large applications typically call lots of separately
compiled subroutines. One order entry system I worked on was well over
100,000 lines for a single program, but was in functional units often
10,000 lines or so long. These modules accessed much common data
structures, and then had their own unique temporary areas.

On my current work with an HP3000 application called MACS, some of the
larger programs are (from a failing memory) 30 to 40,000 lines, and I
think the largest single program is under 100,000. Of course, this is
NOT counting copy libraries (include files) or common library
routines.

There are also lots of smaller programs in the thousands to ten or
fifteen thousand lines of code.

I would argue that few well-written programs need be this large. Long
before they get this large they should be broken into some
sub-programs or even separate programs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
