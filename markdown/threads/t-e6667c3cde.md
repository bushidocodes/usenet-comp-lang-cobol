[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF - CHAIN eats up memory!

_1 message · 1 participant · 1995-10_

---

### MF - CHAIN eats up memory!

- **From:** "izu..." <ua-author-17087862@usenetarchives.gap>
- **Date:** 1995-10-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46boid$nng@nippur.irb.hr>`

```
We are using MF COBOL ver. 1.2.31 (1989.!) for some business applications. Our
menu system uses "CHAIN progname USING menu-block". General idea was to ensure
that all subroutines are canceled at the time of entering new program.

Some time ago we've noticed that every "CHAIN" eats up main memory, and after
certain number of entering programs and returns to main menu user gets error
message 198 (not enough memory). Experiments have showed that every "CHAIN" eatsup the block of memory which corresponds to the size of "USING" data block.
(Method: Shift-Ctrl-Break to dos and MEM/C there).
System is running on DOS, with RTS , and great number of .gnt programs + 2
our own .lbr files with common subroutines. Luckily, our menu-block is not too
big, but nevertheless thing is painful.

Question: Is there any possibility to avoid this! Guru-s from mfltd, please
help me !
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
