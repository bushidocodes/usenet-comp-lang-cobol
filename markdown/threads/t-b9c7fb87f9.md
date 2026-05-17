[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mathematical Library & Y2K

_4 messages · 4 participants · 1998-08_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Mathematical Library & Y2K

- **From:** "g. van vlimmeren" <ua-author-2468186@usenetarchives.gap>
- **Date:** 1998-08-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdc9bb$4f2a9520$2c050380@s70>`

```
Hi,

A small tip for all users of the 'ACCEPT FROM DATE'.

With this Y2K-demon breathing down our necks, it's nice to know someone
thought of an alternative for this commonly used YYMMDD format that results
from the ACCEPT.

If your Cobol-compiler supports Addendum X3.23A-1989 of the Cobol ANSI
X3-23-1985 version
(aka 'Cobol 89'):

MOVE FUNCTION CURRENT-DATE TO will give you the the date
CCYYMMDD, the time and the difference from GMT.

No more use for this

IF YEAR > 30 MOVE 19 TO CENTURY ELSE MOVE 20 TO CENTURY crap.

Probably old news for most of you, but I'm bored at the moment, so I
thought I'd give some meaning to my shallow life by pointing this out :)

G. van Vlimmeren
Syson Automatisering
Bull DPS Cobol Scratcher
```

#### ↳ Re: Mathematical Library & Y2K

- **From:** "rich rohde" <ua-author-17074938@usenetarchives.gap>
- **Date:** 1998-08-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9c7fb87f9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdc9bb$4f2a9520$2c050380@s70>`
- **References:** `<01bdc9bb$4f2a9520$2c050380@s70>`

```

G. van Vlimmeren wrote in message <01bdc9bb$4f2a9520$2c050380@s70>...
› Hi,
›
› A small tip for all users of the 'ACCEPT FROM DATE'.
›

Why not: ACCEPT FROM DATE YYYYMMDD?

(Micro Focus COBOL NetExpress V2)

Rich
```

##### ↳ ↳ Re: Mathematical Library & Y2K

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9c7fb87f9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b9c7fb87f9-p2@usenetarchives.gap>`
- **References:** `<01bdc9bb$4f2a9520$2c050380@s70> <gap-b9c7fb87f9-p2@usenetarchives.gap>`

```

Judson McClendon wrote in message ...
› Rich Rohde wrote:
›› 
…[7 more quoted lines elided]…
› 
It is not a Standard construct YET. It is part of the draft of the next
Standard (due out after Jan 1, 2000 - unfortunately) and it is being
implemented by more and more vendors. I know that Micro Focus, IBM, and
Fujitsu all have it generally available NOW - I think some others may have
it now or soon.

P.S. Of course the Function Current-Date is also available in any '85 +
intrinsic function compiler - so I am not saying that you shouldn't use it -
but I do think that the ACCEPT from DATE YYYYMMDD format is also pretty
acceptable and often requires less coding changes.
```

###### ↳ ↳ ↳ Re: Mathematical Library & Y2K

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-08-19T13:54:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9c7fb87f9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b9c7fb87f9-p3@usenetarchives.gap>`
- **References:** `<01bdc9bb$4f2a9520$2c050380@s70> <gap-b9c7fb87f9-p2@usenetarchives.gap> <gap-b9c7fb87f9-p3@usenetarchives.gap>`

```
Rich Rohde wrote in message ...
› Judson McClendon wrote in message ...
›› William M. Klein wrote:
…[40 more quoted lines elided]…
› code I have written to validate data.


Well, there are two issues here, at least for myself. I agree that the
"ACCEPT FROM DATE YYYYMMDD" construct will almost certainly be
in the new standard, and I like it. But that is not *certain*. Also, while
I use Micro Focus COBOL, I also program for a variety of platforms, mostly
Unisys A Series and PC DOS/Win3x/Win9x. My clients on the Unisys A Series
still use COBOL 74 because the compiler is significantly faster than the
COBOL 85 compiler. One of the most significant ways I maintain a very high
productivity (~200k LOC/year) is through extensive code reuse. To facilitate
that, I tend to code for the lowest common denominator, and work very hard
for consistency, consistency, consistency. I simply do not want to start
using a new construct unless 1) I *know* I will be able to continue to use
it, and/or 2) it is so extremely useful that it is worth dealing with
compatibility issues. For example, I use the COBOL 85's END-PERFORM, END-IF,
etc. and Micro Focus '78' constants because they are extremely useful. But
I still program using PERFORM 123400-PARAGRAPH THRU 123400-EXIT, instead of
dropping the EXIT and using EXIT PARAGRAPH, because that would cause too
much disruption if I were constantly switching between them. Once I no
longer have to code a lot in COBOL 74, I will gladly drop the EXIT's forever.

There are two ever conflicting forces, the need for innovation and the need
for standardization. To satisfy either without sufficient concern for the
other results in inefficiency and waste, so you need to strike a balance
between the two. When you have a large body of developed code to be
maintained, as my client's and I do, you must consider the impact on changing
programming standards. Finding the 'proper' balance for any given situation
is largely a judgment call. I would likely chose a different balance if I
were in somebody else's shoes, and they would likely chose a different
balance than I have, were they in my shoes. Different circumstances,
different experience and judgment.

When I worked as an employee, I was not nearly so concerned about my personal
productivity. I was mostly concerned with doing the job correctly, with not
nearly so much concern for programming costs as I have now as a consultant.
But now that I charge clients a pretty good chunk of change for every hour I
work, I must make it count, or I won't get more business. The customer is
surely aware of my productivity and what it costs. :-) I still use a DOS
programmer's editor (Brief), because it is such second nature to me, that it
would take me months to even approach the productivity I have with Brief. I
bought a Windows editor (Multi-Edit) early last year, but I will need to wait
for the right time to switch, when I am not heavily into coding, and under
time pressure. However, I just finished an 18 month, $410k project with an
associate, and our delivered price was less than $2/LOC. The highest price I
ever charged, but this system was *tough*. It came up clean as a whistle,
and they *love it*.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
