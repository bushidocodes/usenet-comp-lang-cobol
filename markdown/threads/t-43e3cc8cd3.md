[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is the OF construct?

_4 messages · 3 participants · 1996-04 → 1996-05_

---

### What is the OF construct?

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-04-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4k26oq$40lc@news-s01.ny.us.ibm.net>`

```
If a data-item has the SAME name in more than one data structure,
you can specify which one by using the OF construct like this:
MOVE SPACE TO DATA-ITEM OF STRUCTURE1
that's all; no big deal. Some compilers do not (did not?) support
this (properly called "qualification") which is why it is sometimes
outlawed.
```

#### ↳ Re: What is the OF construct?

- **From:** "7467..." <ua-author-2473760@usenetarchives.gap>
- **Date:** 1996-05-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43e3cc8cd3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4k26oq$40lc@news-s01.ny.us.ibm.net>`
- **References:** `<4k26oq$40lc@news-s01.ny.us.ibm.net>`

```

lsv··.@i··.net wrote:

› If a data-item has the SAME name in more than one data structure,
› you can specify which one by using the OF construct like this:
…[3 more quoted lines elided]…
› outlawed.

Good prefix's on your variable names can assist here if you don't want
to use fully qualified variable names. A two to four character
prefix, a dash, and the rest of your name.

ie. D11-CUST-ID

In our shop the prefix means System D (Accounts Recievable), Files 11,
first master file.

The ISO Cobol standard guanentees no reserved word will contain a dash
"-" prior to position 5 (I believe its 5) so a two to four character
prefix with a dash will never be a reserved word, regardless of the
compiler used.

Fred Young
National Business Consultants
Greater Los Angeles Micro Focus Users Group
Phn: (310) 395-5127
Eml: 746··.@com··e.com
```

##### ↳ ↳ Re: What is the OF construct?

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-05-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43e3cc8cd3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43e3cc8cd3-p2@usenetarchives.gap>`
- **References:** `<4k26oq$40lc@news-s01.ny.us.ibm.net> <gap-43e3cc8cd3-p2@usenetarchives.gap>`

```

In <4no829$1.··.@new··t.com>, 746··.@com··e.com (Fred Young) writes:
› lsv··.@i··.net wrote:
› 
…[20 more quoted lines elided]…
› 
The problem with ANY STANDARD is that there is ALWAYS someone
out there that violates it. This malaise is known as the "extended subset".
Here is a list of reserved words on various systems that violate your rule:

B-AND IBM Cobol II, Bull GCOS7
B-EXOR "
B-LESS "
B-NOT "
B-OR "
H-2000 Bull GCOS8
H-2400 "
I-O ANSI
CP-6 Bull GCOS
CS-BASIC "
CS-GENERAL "
DB-xxxxx VAX VMS
NO-ECHO MicroFocus
NO-SPACE MicroFocus, HP3000
PP-xxx Realia V4
CBL-CTR Siemens BS-2000
CRT-UNDER Realia
CYL-OVERFLOW Siemens BS-2000
DAY-OF-WEEK MicroFocus, many others
END-xxx ANSI-85
LOW-VALUES ANSI-74
SUB-xxxx "
CODE-SET "
COMP-x "
DATE-x "
FILE-xxx MicroFocus, and others
HIGH-VALUES Ansi-74
SORT-xxx Ansi, MF, HP3000
UPSI-xx Various IBM

You will that hyphens occur in col 2, 3, 4, ...
You are never safe. God knows what comes in the
next version of any compiler.

This is, of course, also true is you do not use a hyphen.
Some people use two hyphens (like MYFILE--MY-STUFF).
I have not seen that yet in any compiler, but who knows?

Leif-Svalgaard
```

##### ↳ ↳ Re: What is the OF construct?

- **From:** "joan colley" <ua-author-15559010@usenetarchives.gap>
- **Date:** 1996-05-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43e3cc8cd3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43e3cc8cd3-p2@usenetarchives.gap>`
- **References:** `<4k26oq$40lc@news-s01.ny.us.ibm.net> <gap-43e3cc8cd3-p2@usenetarchives.gap>`

```

Fred Young wrote:
› 
› lsv··.@i··.net wrote:
…[28 more quoted lines elided]…
› 


Don't overlook the occassional need to have record layouts which differ in
arrangement but contain the same data names allowing for a 'move
corresponding'.

Joan Colley.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
