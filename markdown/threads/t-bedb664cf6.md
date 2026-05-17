[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help! Adding COMP into COMP-3

_5 messages · 4 participants · 1998-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Help! Adding COMP into COMP-3

- **From:** "darius cooper" <ua-author-16041747@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p0i2j$occ$1@news.megsinet.net>`

```
I have a program with an odd problem. [ Using MF-COBOL on AIX. ]

The working storage has the following fields:

05 WS-SUM PIC S9(11)V9(5) COMP-3.
01 WS-REC-01.
05 WS-EMP-ID PIC X(9).
...
05 WS-AMT PIC S9(4) COMP.
...

At some point in the procedure division, I have the following code:

MOVE ZERO TO WS-SUM
PERFORM UNTIL END-OF-CHAIN
MOVE TBL-REC-01(IDX) TO WS-REC-01
ADD WS-AMT TO WS-SUM
.... other code, not related to either WS-AMT nor to WS-SUM

END-PERFORM

Problem #1:

The loop is executed 3 times. Each time, the field WS-AMT has the value
11111. If I DISPLAY WS-SUM just after the ADD statement, it displays
+0000001111100000 the first time, and +0000002222200000, the second time.
But, after the third add, it displays a strange number: something
like -0000001430213452 (this is not the exact number). It is almost as
though I was adding to a 2-byte integer and it overflowed and wrapped
around. But, why should this happen.

I tried a simple program to see what would happen and it worked fine. Could
something somewhere else in the program be effecting this code?
I also have a very similar program that contains the sane code (it's in a
copybook. And *that* works fine.)

Problem #2:

If I DISPLAY WS-AMT it prints out as +11111. But, if I first DISPLAY WS-SUM
and *then* display WS_AMT, it prints out with a trailing zero (+111110).

Any ideas of what I should be looking for would be much appreciated.

- Darius Cooper
```

#### ↳ Re: Help! Adding COMP into COMP-3

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bedb664cf6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6p0i2j$occ$1@news.megsinet.net>`
- **References:** `<6p0i2j$occ$1@news.megsinet.net>`

```

Darius Cooper wrote in message <6p0i2j$occ$1.··.@new··t.net>...
› I have a program with an odd problem. [ Using MF-COBOL on AIX. ]

MicroFocus is notorious for buggy code with COMP.
Try this: remove the COMP-3 and make WS-SUM display.
If that does not work, make a temp variable for WS-AMT also
with usage display and move WS-AMT to it first, then add the
result to WS-SUM.

If this works, you have a bug in the compiler.


› 
› The working storage has the following fields:
…[45 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Help! Adding COMP into COMP-3

- **From:** "dennis j. minette" <ua-author-8528253@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bedb664cf6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bedb664cf6-p2@usenetarchives.gap>`
- **References:** `<6p0i2j$occ$1@news.megsinet.net> <gap-bedb664cf6-p2@usenetarchives.gap>`

```
If this is a word or byte boundary problem, I've heard that keeping an odd
number of 9's in the signed picture might help make things act more
predictably. Try
05 WS-SUM PIC S9(12)V9(5) COMP-3.
in place of your
05 WS-SUM PIC S9(11)V9(5) COMP-3.

Or you could make it an elementary data item at the 01 level and rely on the
compiler to get the byte boundary established correctly?

Just another stab in the dark at a COBOL demon. Since disk storage got to a
reasonable price level, and MIPS have greatly increased, I haven't messed
around much with any kind of COMP values - I like to see DISPLAY values in
file dumps and just skip all that hex math!

CCCO

Leif Svalgaard wrote in message <35b··.@new··m.net>...
› 
› Darius Cooper wrote in message <6p0i2j$occ$1.··.@new··t.net>...
…[61 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Help! Adding COMP into COMP-3

- **From:** "darius cooper" <ua-author-16041747@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bedb664cf6-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bedb664cf6-p2@usenetarchives.gap>`
- **References:** `<6p0i2j$occ$1@news.megsinet.net> <gap-bedb664cf6-p2@usenetarchives.gap>`

```
Thank you Leif, I shall try it and report back.

I forgot to mention in my post that I tried redefining WS-SUM as PIC S9(11)
COMP-3
(i.e., I removed the decimals) and it was summing stuff correctly.
However, I really want the decimals because the code in the copybook uses
REPLACING and WS-AMT may have decimals.

- Darius

Leif Svalgaard wrote in message <35b··.@new··m.net>...
› 
› Darius Cooper wrote in message <6p0i2j$occ$1.··.@new··t.net>...
…[61 more quoted lines elided]…
›
```

#### ↳ Re: Help! Adding COMP into COMP-3

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-07-25T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bedb664cf6-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6p0i2j$occ$1@news.megsinet.net>`
- **References:** `<6p0i2j$occ$1@news.megsinet.net>`

```
Darius Cooper wrote:

› 05 WS-AMT PIC S9(4) COMP.
 
› The loop is executed 3 times. Each time, the field WS-AMT has the value
› 11111.

The data doesn't fit the picture. Your compiler might be generating
some buggy truncation code.

› Problem #2:
›
› If I DISPLAY WS-AMT it prints out as +11111. But, if I first DISPLAY WS-SUM
› and *then* display WS_AMT, it prints out with a trailing zero (+111110).

That's got to be a bug.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net      mailto:Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  MSMSMSMSMSMS 6/28/107                      Happy Trails To You
e    |\ Can you solve the BBA-CAB-DBB series?
Y    |/                 http://members.aol.com/PanicYr00/Sequence.html
o    |\ The Zeros Are Coming!         http://members.aol.com/PanicYr00
u    |/ The Zeros Are Coming!         http://members.aol.com/PanicYr00
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
