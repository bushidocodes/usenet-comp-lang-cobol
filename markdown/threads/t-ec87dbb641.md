[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Eliminate Name with specific first letter from SORT

_7 messages · 7 participants · 1998-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Eliminate Name with specific first letter from SORT

- **From:** "dhar..." <ua-author-2507587@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

As part of an input procedure prior to the SORT I'm trying to eliminate all
records that have the last name starting with a specific letter.

How would you recommend I approach this. Someone mentioned using a REDFINE or
UNSTRING but didn't go into details.

Thanks,

David Hargette
```

#### ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "hank" <ua-author-88501@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

DHargette wrote in article
<199··.@lad··l.com>...
› As part of an input procedure prior to the SORT I'm trying to eliminate
› all
…[4 more quoted lines elided]…
› UNSTRING but didn't go into details.

You mean like
PARA
IF LAST_NAME(1:1) = "L"
PERFORM READ
GO TO PARA
END-IF
Write record


Hank Ingram 
Programmer,Tea-drinker, former corporate stooge,  member of the dreaded
Religious Right  @ http://www.nr.infi.net/~hingram
Needlessly consuming valuable resources in Blacksburg, Va
```

#### ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-05-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

DHargette wrote:
› 
› As part of an input procedure prior to the SORT I'm trying to eliminate all
…[7 more quoted lines elided]…
› David Hargette

Why not eliminate them with an omit condition in the sort?
```

#### ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

In article <199··.@lad··l.com>, dha··.@a··.com
(DHargette) writes:

› As part of an input procedure prior to the SORT I'm trying to eliminate all
› records that have the last name starting with a specific letter.

Is the last name in a separate field so you could just check a specific byte
position? Is the last name first (again, so you can check a specific byte
position)?

Or do you have to decompose the name into separate fields and make some
assumptions on how to identify the last name?

Is this suppose to be part of a SORT ... INPUT PROCEDURE within a COBOL
program? Or is it to be a separate program that builds a file that SORT will be
using?

Before anyone can fill in any details, you will have to provide details of what
you are trying to do and some information to the organization of data.

Mark A. Young
```

#### ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-05-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

In article <199··.@lad··l.com>,
DHargette wrote:
› As part of an input procedure prior to the SORT I'm trying to eliminate all
› records that have the last name starting with a specific letter.

Do your own homework, please.

DD
```

#### ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p6@usenetarchives.gap>`
- **In-Reply-To:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com>`

```

In <199··.@lad··l.com>, dha··.@a··.com (DHargette) writes:
› As part of an input procedure prior to the SORT I'm trying to eliminate all
› records that have the last name starting with a specific letter.
…[4 more quoted lines elided]…
› Thanks,

This definitely sounds like homework but if you wanted to eliminate
all 'A' how 'bout this - no COBOL code required:

//$ORTPARM DD *
OMIT COND=(1,1,CH,EQ,C'A')
```

##### ↳ ↳ Re: Eliminate Name with specific first letter from SORT

- **From:** "jerry peacock" <ua-author-36061@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ec87dbb641-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ec87dbb641-p6@usenetarchives.gap>`
- **References:** `<1998051320443400.QAA05271@ladder01.news.aol.com> <gap-ec87dbb641-p6@usenetarchives.gap>`

```


Cit··.@Cr··s.Com [Ron] wrote in message
<6jof5a$r.··.@exa··c.net>...
› In <199··.@lad··l.com>, dha··.@a··.com
› (DHargette) writes:
›› As part of an input procedure prior to the SORT I'm trying to eliminate
›› all
›› records that have the last name starting with a specific letter.


Am I missing the point? How about:

IF LAST-NAME(1:1) NOT = SPECIFIC-LETTER
RELEASE SORT-REC.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
