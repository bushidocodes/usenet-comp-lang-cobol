[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/ASM370 KNOWLEDGE

_2 messages · 2 participants · 1995-04_

---

### COBOL/ASM370 KNOWLEDGE

- **From:** "kra..." <ua-author-821003@usenetarchives.gap>
- **Date:** 1995-04-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3mrkes$7nh@news1.delphi.com>`

```

I'm an entry-level COBOL programmer working in an MVS environment with DB2,
IMS, and CICS. I've also had two classes in 370/Assembly but I am by no
means an expert, and Assembly is not something I come in contact with right
now in my duties.

Here's my question. What specific understandings of Assembly will assist me
most in COBOL, particularly in debugging abend situations. I already have a
grasp of how data is represented in memory as far as reading a hex dump
is concerned, whether it's packed or character, and how it represented at
the nibble level. What other items from my limited Assembly knowledge
should I expand upon to make me a better COBOL programmer?


Don Kramer
kra··.@del··i.com

Rainbow V 1.14.1 for Delphi - Registered
```

#### ↳ Re: COBOL/ASM370 KNOWLEDGE

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1995-04-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-faaddd395e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3mrkes$7nh@news1.delphi.com>`
- **References:** `<3mrkes$7nh@news1.delphi.com>`

```
› Here's my question.  What specific understandings of Assembly will assist me
› most in COBOL, particularly in debugging abend situations.  I already have a
…[3 more quoted lines elided]…
› should I expand upon to make me a better COBOL programmer?

Interesting question. I've always said every COBOL programmer should know
assembly language.
1. A clear understanding of what will happen inside the machine will help
you to write more efficient code. For example: Understanding how subscripts
will be converted to register pointers for table accesses will make them
execute faster. Knowing how arithmetic will be performed at the
assembly level will enable to set up the COBOL variables in the
most efficient manner. Understanding what's going on when converting
from one data format to another will save you loads of run time.
In general, know how the code will be translated is of great benefit in
writing efficient COBOL.
2. With all the fancy debugging stuff they have these days, Abend-aid,
COBOL fdumps, Xpediter, etc. I don't have to do this as often as I
used to, but sometimes when I just can't figure out what is wrong...
I get the assembly language translation to find out what it's REALLY
doing.
3. Knowing how to read a dump and find what the COBOL program was
doing at time of abend...locating the displacement in machine of
COBOL instruction...finding where the data is really located...etc.

You don't have to be a first class assembler programmer but if you know
what's really happening behind the scenes you'll be head and shoulders above
a lot of COBOL programmers today and valuable asset to your company.

Ron.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
