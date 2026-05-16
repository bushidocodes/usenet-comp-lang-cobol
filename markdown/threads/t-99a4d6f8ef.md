[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [NetCOBOL] Which key is invalid

_8 messages · 6 participants · 2005-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### [NetCOBOL] Which key is invalid

- **From:** R.Hendriks@hotmail.com (RH)
- **Date:** 2005-07-07T01:38:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb1940e5.0507070038.7424f484@posting.google.com>`

```
LS,

I have a question on the INVALID KEY that is triggered and which key
triggered it. I have an indexed file (obviously) which has a primekey,
and an alternate key 'with no duplicates'. When writing a record, the
primekey may be invalid, the alternate key may be invalid (no
duplicates allowed!) or both.

The runtime nicely delivers the INVALID KEY mesasge but I have no
(known) way to determine which key is invalid. The file status is only
2 bytes and thus stores 23 and no futher info on which key. In
RM/COBOL there was a function for this (C$ERROR??) to get the deail
error info and thus which of the keys triggered 'invalid'. How can I
do this using NetCOBOL, any ideas?

Attention: I don't mean the contents of the key (which is still in the
FD or WS) but whether it's the prime of alternate key reporting the
error.

Using Fujitsu NetCOBOL v7 for Windows.

RH.
```

#### ↳ Re: [NetCOBOL] Which key is invalid

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-07-07T09:35:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11cqfdjidmsk47a@news.supernews.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com>`

```
RH wrote:
> LS,
>
…[19 more quoted lines elided]…
> RH.

I dunno. As a first approximation:

Close the file.
Open the (physical) file again with a different SELECT specifying WITH 
DUPLICATES on the alternate key.
Repeat the operation
If no error,
  1. It was the alternate key causing the problem.
  2. Clean up the mess
  3. Start over
  4. Handle the error
If error
  1. The primary key is the culprit
```

##### ↳ ↳ Re: Which key is invalid

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-07-07T12:12:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120763540.371293.100760@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<11cqfdjidmsk47a@news.supernews.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com> <11cqfdjidmsk47a@news.supernews.com>`

```

> Open the (physical) file again with a different SELECT specifying WITH
> DUPLICATES on the alternate key.

That will give a '39' error status.
```

#### ↳ Re: Which key is invalid

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-07-07T12:05:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120763155.213393.84220@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<fb1940e5.0507070038.7424f484@posting.google.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com>`

```

> 2 bytes and thus stores 23 and no futher info on which key.

'23' means record missing, it relates to the key on which the operation
was done, probably the primary key.
```

#### ↳ Re: [NetCOBOL] Which key is invalid

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2005-07-07T17:14:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GWgze.62334$%Z2.31653@lakeread08>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com>`

```

"RH" <R.Hendriks@hotmail.com> wrote in message
news:fb1940e5.0507070038.7424f484@posting.google.com...
> LS,
>
…[19 more quoted lines elided]…
> RH.

 Huh! File status 23 is 'record not found' at a failed read. It does not
apply when writing a record.

John
```

##### ↳ ↳ Re: [NetCOBOL] Which key is invalid

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-07-07T14:40:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dak7gd$20r7$1@si05.rsvl.unisys.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com> <GWgze.62334$%Z2.31653@lakeread08>`

```
"John Simpson" <jasimp@earthlink.net> wrote in message
news:GWgze.62334$%Z2.31653@lakeread08...

>  Huh! File status 23 is 'record not found' at a failed read. It does not
> apply when writing a record.

From the viewpoint of standard COBOL, I think what applies to a write is I-O
Status 22:  "An attempt is made to write or rewrite a record that would
create a duplicate prime record key or a duplicate alternate record key
without the DUPLICATES phrase in an indexed file."  (ANSI X3.23-1985 page
IX-4; ISO/IEC 1989:2002 page 152 is similar).

Somebody might also encounter I-O Status 24:  "An attempt is made to write
beyond the externally-defined boundaries of an indexed file.  The
implementor specifies the manner in which these boundaries are defined."
(ibid.)   But I'm not convinced that the problem is the *key* in that
circumstance.

Other than these cases -- illegal duplicates, or attempt to write outside of
the file's boundaries -- I can't think of anything that might cause an
implementation to regard the contents of a primary or alternate record key
as encountered on a WRITE or REWRITE as "invalid" in the first place,
particularly since in '85 COBOL the keys are alphanumeric ('02 expands this
to include national).

    -Chuck Stevens
```

##### ↳ ↳ Re: [NetCOBOL] Which key is invalid

- **From:** R.Hendriks@hotmail.com (RH)
- **Date:** 2005-07-07T23:20:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb1940e5.0507072220.7303b655@posting.google.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com> <GWgze.62334$%Z2.31653@lakeread08>`

```
"John Simpson" <jasimp@earthlink.net> wrote in message news:<GWgze.62334$%Z2.31653@lakeread08>...
> "RH" <R.Hendriks@hotmail.com> wrote in message
> news:fb1940e5.0507070038.7424f484@posting.google.com...
…[26 more quoted lines elided]…
> John

TYPING ERROR!
```

#### ↳ Re: Which key is invalid

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2005-07-08T03:02:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1120816963.270036.43490@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<fb1940e5.0507070038.7424f484@posting.google.com>`
- **References:** `<fb1940e5.0507070038.7424f484@posting.google.com>`

```
When such an error occurs, try

1) reading the record using the primary key of the record you were
trying to write

2) reading the record using the alternate key

this is non-destructive to the file, so no tricky clean up should be
required and whichever was successful will indicate where the problem
is.

With regards, Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
