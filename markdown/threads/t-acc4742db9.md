[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Year 2000 Date Calculations

_7 messages · 7 participants · 1997-12 → 1998-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### Year 2000 Date Calculations

- **From:** "russell strope" <ua-author-17075062@usenetarchives.gap>
- **Date:** 1997-12-31T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`

```

Are there any standard COBOL algorithms to perform date calculations or
conversions: For example, convert a date in the gregorian format 19980101
to the julian format 1998001 and vice versa. I also need a routine to
determine the day of the week using a given date.
```

#### ↳ Re: Year 2000 Date Calculations

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-31T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`

```

Russell Strope wrote:
› 
› Are there any standard COBOL algorithms to perform date calculations or
› conversions: For example, convert a date in the gregorian format 19980101
› to the julian format 1998001 and vice versa.   I also need a routine to
› determine the day of the week using a given date.

If you have Cobol-85 with the x3.23a-1989 function extensions, there are
four functions that will help you out: DATE-OF-INTEGER, DAY-OF-INTEGER,
INTEGER-OF-DATE, and INTEGER-OF-DAY. "DATE" means Gregorian YYYYMMDD,
"DAY" means Julian YYYYDDD, and INTEGER means the number of days since
1600-12-31 (eg, 2000-12-31 is 146097). To convert use

MOVE FUNCTION DATE-OF-INTEGER
(FUNCTION INTEGER-OF-DAY (JUL)) TO GREG

MOVE FUNCTION DAY-OF-INTEGER
(FUNCTION INTEGER-OF-DATE (GEEG)) TO JUL

You can also use these functions to validate dates, because invalid
dates return zero.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: Year 2000 Date Calculations

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-12-31T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-acc4742db9-p2@usenetarchives.gap>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net> <gap-acc4742db9-p2@usenetarchives.gap>`

```

RandallBart wrote:
› 
› Russell Strope wrote:
…[21 more quoted lines elided]…
› I  |\   Randall Bart                      mailto:Bar··.@usa··m.net

I recently had a discussion with one of our tech services guys. IBM's
COBOL for MVS and VM has an installation option that affects the
behavior of INTEGER. IBM recommends ANSI which uses 1600-12-31 as the
base date, but also allows the LILLIAN option which changes the base
date to 1582-10-15 (or something like that) for compatibility with
LE/MVS.

It could have an effect if you intend to exchange INTEGER dates with
other systems. If you only use INTEGER dates internally to calculate
date intervals or generate new dates or perform conversions it probably
doesn't matter.

Just another complication to beware of.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

##### ↳ ↳ Re: Year 2000 Date Calculations

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-01-01T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-acc4742db9-p2@usenetarchives.gap>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net> <gap-acc4742db9-p2@usenetarchives.gap>`

```

RandallBart wrote:
› 
› ...snip...
…[16 more quoted lines elided]…
› I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
...snip....

Randall,

MVS only accepts the FUNCTION stuff in a compute for numerical
functions. This was covered in a previous thread but just in case.

Ken
```

#### ↳ Re: Year 2000 Date Calculations

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-12-31T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`

```

Russell Strope wrote:
› 
› Are there any standard COBOL algorithms to perform date calculations or
› conversions: For example, convert a date in the gregorian format 19980101
› to the julian format 1998001 and vice versa.   I also need a routine to
› determine the day of the week using a given date.

Do a web-search for etkpak.zip and you should find it there... I can
never remember the URL for it.

DD
```

#### ↳ Re: Year 2000 Date Calculations

- **From:** "colin lucas" <ua-author-7055304@usenetarchives.gap>
- **Date:** 1997-12-31T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`

```


Russell Strope wrote in message <68h7f0$i.··.@bgt··t.net>...
› Are there any standard COBOL algorithms to perform date calculations or
› conversions: For example, convert a date in the gregorian format 19980101
› to the julian format 1998001 and vice versa.   I also need a routine to
› determine the day of the week using a given date.
› 

The Intrinsic functions handle this well.....

To convert use...

COMPUTE WS-JULIAN = FUNCTION DAY-OF-INTEGER(
FUNCTION
INTEGER-OF-DATE(WS-GREGORIAN))

For day-of-Week

COMPUTE WS-DAY-OF-WEEK = FUNCTION REM(
FUNCTION
INTEGER-OF-DATE(WS-GREGORIAN), 7)

This returns 0 for Sunday, 1 for Monday etc.
```

#### ↳ Re: Year 2000 Date Calculations

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-01-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-acc4742db9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`
- **References:** `<68h7f0$i4t@bgtnsc02.worldnet.att.net>`

```

Russell,
Judson McClendon, a frequent visitor of the cobol news groups, has
donated a very useful set of cobol date calculation algorithms at the
following url: http://www.infogoal.com/cbd/src/date.zip

Compile datet.cob to see the date functions in action.

Dan Maltes
Applied Systems Technology

Russell Strope wrote in message <68h7f0$i.··.@bgt··t.net>...
› Are there any standard COBOL algorithms to perform date calculations or
› conversions: For example, convert a date in the gregorian format 19980101
› to the julian format 1998001 and vice versa.   I also need a routine to
› determine the day of the week using a given date.
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
