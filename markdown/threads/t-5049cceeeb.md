[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II Date Conversion routines that handle ccyy...

_6 messages · 6 participants · 1996-08 → 1996-09_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Compilers and vendors`](../topics.md#compilers) · [`Date and calendar processing`](../topics.md#dates)

---

### COBOL II Date Conversion routines that handle ccyy...

- **From:** "markm" <ua-author-17086856@usenetarchives.gap>
- **Date:** 1996-08-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vghjh$vlh@thea.dynanet.com>`

```

I am looking for a general date conversion subroutine that can take a date or
dates, and perform generic stuff like convert from gregorian to julian, and if
fed two dates, can send back the difference in days....stuff like that.
Routine performed would be controlled by parameter passed to it. We have one
where I work, however, it cannot handle the dreaded 'year 2000' problem. No
one seems worried (...'3 years off') but I'd like to get a jump. Any help
would be appreciated. Thanks.
```

#### ↳ Re: COBOL II Date Conversion routines that handle ccyy...

- **From:** "spam.f..." <ua-author-17086140@usenetarchives.gap>
- **Date:** 1996-08-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5049cceeeb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4vghjh$vlh@thea.dynanet.com>`
- **References:** `<4vghjh$vlh@thea.dynanet.com>`

```

markm@dynanet. com (mark) wrote:
› I am looking for a general date conversion subroutine that can take a date or
› dates, and perform generic stuff like convert from gregorian to julian, and if
…[4 more quoted lines elided]…
› would be appreciated.  Thanks.

If your compiler supports the 'Intrinsic Functions' extension to the -85 standard,
you're home free. There are several functions built in that will do just what you want.

Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

#### ↳ Re: COBOL II Date Conversion routines that handle ccyy...

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-08-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5049cceeeb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4vghjh$vlh@thea.dynanet.com>`
- **References:** `<4vghjh$vlh@thea.dynanet.com>`

```

In <4vghjh$v.··.@the··t.com>, markm@dynanet. com (mark) writes:
› I am looking for a general date conversion subroutine that can take a date or 
› dates, and perform generic stuff like convert from gregorian to julian, and if 
…[4 more quoted lines elided]…
› would be appreciated.  Thanks.

----------------------

If your compiler does not have functions you could try to download
the ETK portable subroutine library from http://www.toscintl.com
(click on ETK). The CALRPK routine has just what you need.
Leif Svalgaard
```

##### ↳ ↳ Re: COBOL II Date Conversion routines that handle ccyy...

- **From:** "ka..." <ua-author-6588812@usenetarchives.gap>
- **Date:** 1996-08-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5049cceeeb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5049cceeeb-p3@usenetarchives.gap>`
- **References:** `<4vghjh$vlh@thea.dynanet.com> <gap-5049cceeeb-p3@usenetarchives.gap>`

```

lsv··.@i··.net wrot. We have one
›› where I work, however, it cannot handle the dreaded 'year 2000' problem

Well geez month = (Century - 19) * 12 + month will stuff all the
centuries up to 2600 in the extra space in months. Reverse to test or
get it out.
```

#### ↳ Re: COBOL II Date Conversion routines that handle ccyy...

- **From:** "ken mackenzie" <ua-author-4360810@usenetarchives.gap>
- **Date:** 1996-08-26T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5049cceeeb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4vghjh$vlh@thea.dynanet.com>`
- **References:** `<4vghjh$vlh@thea.dynanet.com>`

```

mark wrote:
›
› I am looking for a general date conversion subroutine that can take a date or
› dates, and perform generic stuff like convert from gregorian to julian, and if
› fed two dates, can send back the difference in days....stuff like that.If you have access to the LE/370 routines then you can call various
routines such as "CEEDATE" "CEEDAYS" etc. They are wonderful!
```

#### ↳ Re: COBOL II Date Conversion routines that handle ccyy...

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-09-23T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5049cceeeb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4vghjh$vlh@thea.dynanet.com>`
- **References:** `<4vghjh$vlh@thea.dynanet.com>`

```

I beleive that "The Bridge to the Next Century" may fill the bill.

This set of standard (1968, 1974, 1985) compliant COBOL routines was
designed to support the 5 date intrinsic functions for compilers such as
VS COBOL II that do not have the 1985 standard addendum FUNCTIONS
implemented.

Equivalent function is provided for CURRENT-DATE, DAY OF INTEGER, DATE OF
INTEGER, INTEGER OF DATE and INTEGER OF DAY standardized functions.

All in COBOL. (A change will be required to the implementation in 2096,
happy to ship it 100 years early).

Easy transition to the ANSI addendum functions when you finally get to
COBOL/370 or COBOL for MVS and VM or other implenetation which provides
the functions.

For information: Carl Gehr, Edge Information Group, Inc.
734··.@com··e.com


Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
