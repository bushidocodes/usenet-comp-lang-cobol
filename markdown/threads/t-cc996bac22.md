[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL -> C Number Format Question

_3 messages · 3 participants · 1996-10_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### COBOL -> C Number Format Question

- **From:** "co..." <ua-author-17086691@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55b7l5$knj@news.onramp.net>`

```

I have a data file created by a COBOL program. The field is a PIC
S9(3). In the ASCII output file, it look like this:

00000{

I know that the sign is held in the low order byte (hence the {).

Does anyone have the chart of what that rightmost means and how I can
map it to a format understandable by a C program?

Thank you in advance.

Richard Court
co··.@seq··l.com
```

#### ↳ Re: COBOL -> C Number Format Question

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1996-10-31T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc996bac22-p2@usenetarchives.gap>`
- **In-Reply-To:** `<55b7l5$knj@news.onramp.net>`
- **References:** `<55b7l5$knj@news.onramp.net>`

```

co··.@seq··l.com (Richard Court) wrote:

› I have a data file created by a COBOL program.  The field is a PIC
› S9(3).  In the ASCII output file, it look like this:
 
› 00000{
 
› I know that the sign is held in the low order byte (hence the {).
 
› Does anyone have the chart of what that rightmost means and how I can
› map it to a format understandable by a C program?
 
› Thank you in advance.
 
› Richard Court
› co··.@seq··l.com

A-I is +1 thru +9 you already have +0 10=1{
J-R is -1 thru -9 -10 is 1} -0 is }

+123 is 12C -456 45o (alpha-oh)

JR
```

##### ↳ ↳ Re: COBOL -> C Number Format Question

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-10-31T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc996bac22-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cc996bac22-p2@usenetarchives.gap>`
- **References:** `<55b7l5$knj@news.onramp.net> <gap-cc996bac22-p2@usenetarchives.gap>`

```

Jeff Raben wrote:
› 
› co··.@seq··l.com (Richard Court) wrote:
…[15 more quoted lines elided]…
› +123   is 12C     -456   45o   (alpha-oh)

This is true for some implementations and not for others. Some toggle
a bit on the rightmost byte (the leftmost bit for Tandem, the next to
the leftmost bit for MF). Some fiddle with the leftmost character.
Some do other things. The standard allows the implementor to put the
sign wherever the implementor wants to put it. By using the SIGN
clause, you can specify SEPARATE to get a sign that will be the same
on every implementation. You should read the reference manual for the
product you are using.

By the way, the sign scheme Jeff described is the way it was done with
punched cards. It was very unusual to use A-I (the twelve row was
left blank for positive numbers, but it could also be punched to
represent them). I think IBM uses that scheme (they still use EBCDIC
which is based on punched cards). When I implemented COBOL for
Control Data we had somewhere around six representations of plus and
minus 0, because several implementors had used several different
schemes. The whole thing is a big mess.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
