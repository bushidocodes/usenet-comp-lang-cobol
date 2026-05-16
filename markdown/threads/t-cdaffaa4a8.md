[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM COBOL Question

_6 messages · 4 participants · 2008-07 → 2008-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM COBOL Question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-03T12:05:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d2jdnFhqkeU1@mid.individual.net>`

```
I was told that RM COBOL cannot randomly access an ISAM file using a 
secondary key, with READ... KEY IS.

Instead, it is necessary to use a START on the secondary key, then issue a 
READ NEXT.

This seems like such a violation of the standard (and so grossly 
inefficient...) that I wondered if anyone using RM COBOL might confirm, deny 
or comment on it?

(It has some important impacts when converting to RDB...)

Pete.
```

#### ↳ Re: RM COBOL Question

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-07-03T03:04:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PkXak.48262$kx.3296@pd7urf3no>`
- **In-Reply-To:** `<6d2jdnFhqkeU1@mid.individual.net>`
- **References:** `<6d2jdnFhqkeU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I was told that RM COBOL cannot randomly access an ISAM file using a 
> secondary key, with READ... KEY IS.
…[10 more quoted lines elided]…
> Pete.

Methinks, somebody is feeding you a load of guff !

----------------------------------------------------------
The Indexed File Control Entry :
---------------------------------
SELECT file-name
ASSIGN TO RANDOM 	("external-file-name")
			(data-name-1)
RESERVE integer(AREA/AREAS)
ORGANIZATION is INDEXED
ACCESS MODE IS (SEQUENTIAL/RANDOM/DYNAMIC)
RECORD KEY IS data-name-2
ALTERNATE RECORD KEY IS data-name-3 (WITH DUPLICATES) OR 'without'
FILE STATUS is data-name-4

Check Liant on-line manuals to expand on a definition of data-names 2 and 3

ISAM READ : The READ Statement (Relative and Indexed I/O)
---------------------------------------------------------

Format 1 :

READ file-name (NEXT) RECORD (WITH NO LOCK) (INTO identifier)
	AT END imperative-statement)

Format 2 :

READ file-name RECORD (WITH NO LOCK) (INTO identifier)
	KEY IS data-name
	INVALID KEY imperative-statement

Format 1 is used for files in sequential access mode.
Format 2 is used for files in random access mode or for files in dynamic 
access mode; I always specified 'Dynamic' for my ISAMs.

The KEY phrase may be specified only when the organization is 'ISAM'. 
When the KEY clause is present, data-name must be the name of one of the 
record keys associated with file-name. Data-name may be qualified.

Obviously more than above - but check out latest Liant manuals; they are 
up to Version 11 I believe.

-----------------------------------------------------------------------

Your informant had better take an RM Refresher Course. The extract I've 
given above is from Version 2.0b, obsolete and no longer supported and 
published in 1984 - so that makes it COBOL '78 ?

Jimmy
```

##### ↳ ↳ Re: RM COBOL Question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-03T22:29:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d3o15Fmo7nU1@mid.individual.net>`
- **References:** `<6d2jdnFhqkeU1@mid.individual.net> <PkXak.48262$kx.3296@pd7urf3no>`

```


"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:PkXak.48262$kx.3296@pd7urf3no...
> Pete Dashwood wrote:
>> I was told that RM COBOL cannot randomly access an ISAM file using a 
…[14 more quoted lines elided]…
>

Thanks, Jimmy, that was my feeling too. I did a quick search for Liant 
manuals online but couldn't find much.

Cheers,

Pete.
<snip>
```

#### ↳ Re: RM COBOL Question

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-02T21:37:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0e6fe4c-8340-4bfb-9a81-2f7dc599038d@a9g2000prl.googlegroups.com>`
- **References:** `<6d2jdnFhqkeU1@mid.individual.net>`

```
On Jul 3, 12:05 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I was told that RM COBOL cannot randomly access an ISAM file using a
> secondary key, with READ... KEY IS.

There is a problem if duplicates are allowed as it will not be
possible to access every record using this.

Perhaps he was talking about a specific file or situation.

> Instead, it is necessary to use a START on the secondary key, then issue a
> READ NEXT.

It may well be necessary to use this, or a READ followed by READ NEXT
until key changes, if duplicates are allowed.

> This seems like such a violation of the standard (and so grossly
> inefficient...) that I wondered if anyone using RM COBOL might confirm, deny
> or comment on it?

> (It has some important impacts when converting to RDB...)
```

##### ↳ ↳ Re: RM COBOL Question

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-03T22:39:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d3ojcFmp1gU1@mid.individual.net>`
- **References:** `<6d2jdnFhqkeU1@mid.individual.net> <a0e6fe4c-8340-4bfb-9a81-2f7dc599038d@a9g2000prl.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:a0e6fe4c-8340-4bfb-9a81-2f7dc599038d@a9g2000prl.googlegroups.com...
On Jul 3, 12:05 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I was told that RM COBOL cannot randomly access an ISAM file using a
> secondary key, with READ... KEY IS.

There is a problem if duplicates are allowed as it will not be
possible to access every record using this.

Perhaps he was talking about a specific file or situation.

[Pete]

Thanks Richard. I think they tend to use duplicates with their secondary 
indexes so that may be where it came from.

Is this a known bug? Certainly Fujitsu allow access on a secondary key 
without using START, even if duplicates are permitted. I see your point that 
it isn't possible to know WHICH duplicate will be returned, but, as far as I 
know the COBOL standard also allows this.

[/Pete}

> Instead, it is necessary to use a START on the secondary key, then issue a
> READ NEXT.

It may well be necessary to use this, or a READ followed by READ NEXT
until key changes, if duplicates are allowed.

[Pete]

Yes, I see what you're saying.

[/Pete]


> This seems like such a violation of the standard (and so grossly
> inefficient...) that I wondered if anyone using RM COBOL might confirm, 
> deny
> or comment on it?

> (It has some important impacts when converting to RDB...)

[Pete]

Given your points above, I guess it makes sense.

Thanks for this.

Pete.
```

#### ↳ Re: RM COBOL Question

- **From:** EJP <esmond.not.pitt@not.bigpond.com>
- **Date:** 2008-08-14T04:29:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RwOok.28112$IK1.6574@news-server.bigpond.net.au>`
- **In-Reply-To:** `<6d2jdnFhqkeU1@mid.individual.net>`
- **References:** `<6d2jdnFhqkeU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I was told that RM COBOL cannot randomly access an ISAM file using a 
> secondary key, with READ... KEY IS.
> 
> Instead, it is necessary to use a START on the secondary key, then issue a 
> READ NEXT.

I worked on this product many years ago and I ssure you that this is not 
correct. I agree with the other posters that the issue probably 
originated as a statement about how to process duplicate keys ... in 
which case it has nothing to do with RM-Cobol, it's just a statement 
about duplicate keys ... which of course can only arise on an alternate key.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
