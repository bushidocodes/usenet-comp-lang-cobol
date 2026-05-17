[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL ISAM Conversion

_6 messages · 4 participants · 1996-07 → 1996-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### COBOL ISAM Conversion

- **From:** "kevin mayes" <ua-author-9056996@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31FFDC6F.36AC@dpie.gov.au>`

```

we have 100MB of data hidden away in MS COBOL ISAM files
we have no source code, no documentation, etc
is there a way we can convert ISAM to MSAccess?
urgent
```

#### ↳ Re: COBOL ISAM Conversion

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e8a4cb7f7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31FFDC6F.36AC@dpie.gov.au>`
- **References:** `<31FFDC6F.36AC@dpie.gov.au>`

```

Kevin Mayes wrote:

› we have 100MB of data hidden away in MS COBOL ISAM files
› we have no source code, no documentation, etc
› is there a way we can convert ISAM to MSAccess?
› urgent

are you saying you have no layouts?
data can be determined by lotsa work.
once record layout is defined, flat ascii is built for import to
access.
what have you got for info?

JR


and stir with a Runcible spoon...
```

#### ↳ Re: COBOL ISAM Conversion

- **From:** "kevin mayes" <ua-author-9056996@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e8a4cb7f7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<31FFDC6F.36AC@dpie.gov.au>`
- **References:** `<31FFDC6F.36AC@dpie.gov.au>`

```

› we have 100MB of data hidden away in MS COBOL ISAM files
› we have no source code, no documentation, etc
› is there a way we can convert ISAM to MSAccess?
› urgent

can't any one take up the challenge?
```

##### ↳ ↳ Re: COBOL ISAM Conversion

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e8a4cb7f7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8e8a4cb7f7-p3@usenetarchives.gap>`
- **References:** `<31FFDC6F.36AC@dpie.gov.au> <gap-8e8a4cb7f7-p3@usenetarchives.gap>`

```

Kevin Mayes wrote:

›› we have 100MB of data hidden away in MS COBOL ISAM files
›› we have no source code, no documentation, etc
›› is there a way we can convert ISAM to MSAccess?
›› urgent
 
› can't any one take up the challenge?

not much of a challenge.....been there, done that...

what's it worth....and can you prove it's yours....

JR

you don't have to reply Palladin





and stir with a Runcible spoon...
```

##### ↳ ↳ Re: COBOL ISAM Conversion

- **From:** "m..." <ua-author-17086281@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e8a4cb7f7-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8e8a4cb7f7-p3@usenetarchives.gap>`
- **References:** `<31FFDC6F.36AC@dpie.gov.au> <gap-8e8a4cb7f7-p3@usenetarchives.gap>`

```

Kevin Mayes (kma··.@dpi··v.au) wrote:
: > we have 100MB of data hidden away in MS COBOL ISAM files
: > we have no source code, no documentation, etc
: > is there a way we can convert ISAM to MSAccess?
: > urgent

: can't any one take up the challenge?

OK, I will take the challenge. the answer to your question is yes.
sarcasm intended.

If you want answers, give information.
fixed length records?
are we to assume a ms-dos platform?
is the data all ascii or is there some binary data in the files?

try using MicroFocus's tools to dump the data. MS and MF are very similiar
and microfocus's generic data tools might read the files.
Look up finfo in mF manuals to find the section with the file manipulation
tools.
dump each record in hex format and look at it, if you see a 07041776 in
the hex dump, you might assume that that field is a year. If you
see something like 'joe smith' that might be a persons name.

I seem to remember a data conversion tool that might help, send e-mail to
me to remind me to find it.

Michael Potter
pot··.@li··p.com
my opinions are my own.
```

#### ↳ Re: COBOL ISAM Conversion

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-08-01T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e8a4cb7f7-p6@usenetarchives.gap>`
- **In-Reply-To:** `<31FFDC6F.36AC@dpie.gov.au>`
- **References:** `<31FFDC6F.36AC@dpie.gov.au>`

```

In message <<31F··.@dpi··v.au>> Kevin Mayes writes:
› we have no source code, no documentation, etc
› is there a way we can convert ISAM to MSAccess?
› urgent

I would first suggest that you do a trail run of MS Access by
generating 100 Mb of test data into it. Then test the performance
of accessing this, then decide on a database system that will
be adequate when given this volume of data.

Only after this will it be worth the effort of working out a
conversion strategy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
