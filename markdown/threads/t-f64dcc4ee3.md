[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANSI 85 vs COBOL2

_7 messages · 3 participants · 1995-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### ANSI 85 vs COBOL2

- **From:** "dan..." <ua-author-15699386@usenetarchives.gap>
- **Date:** 1995-04-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<950403220531927@star-tech.com>`

```
I am a new programmer starting out and will be working with an IBM 3090
MVS environment usion COBOL II. My studies have previously covered ANSI
COBOL 74 and 85 but all coding was on PC's using RM COBOL and Micro
Focus Personal COBOL.

My question is what specific differences are there between COBOL 85 and
COBOL II? Can anyone suggest a book that would be ideal for someone in
my situation for learning the differences?

All comments and suggestions are gratefully accepted!
```

#### ↳ Re: ANSI 85 vs COBOL2

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-04-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<950403220531927@star-tech.com>`
- **References:** `<950403220531927@star-tech.com>`

```
On Mon, 3 Apr 1995 13:46:04 GMT, Dan Hite (dan··.@sta··h.com) wrote:
› I am a new programmer starting out and will be working with an IBM 3090
› MVS environment usion COBOL II.  My studies have previously covered ANSI
› COBOL 74 and 85 but all coding was on PC's using RM COBOL and Micro
› Focus Personal COBOL.
 
› My question is what specific differences are there between COBOL 85 and
› COBOL II?  Can anyone suggest a book that would be ideal for someone in
› my situation for learning the differences?

COBOL 85 is the ANSI standard. IBM's COBOL II (starting with release
3) is IBM's implementation of that standard. It does not implement
some of the current standard's features (like intrinsic functions),
but is generally compatible. IBM's most recent crack at the COBOL
compiler was called COBOL/370 and is now called "COBOL for MVS and VM"
(what a "catchy" name). It implements intrinsic functions and
procedure pointers, but it also shares library routines with other IBM
compilers (C and PL/I).
```

#### ↳ Re: ANSI 85 vs COBOL2

- **From:** "dan..." <ua-author-15699386@usenetarchives.gap>
- **Date:** 1995-04-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<950403220531927@star-tech.com>`
- **References:** `<950403220531927@star-tech.com>`

```
IBM's most recent crack at the COBOL
-> compiler was called COBOL/370 and is now called "COBOL for MVS and VM
-> (what a "catchy" name). It implements intrinsic functions and
-> procedure pointers, but it also shares library routines with other IB
-> compilers (C and PL/I).

Can you tell me more about intrinsic functions and procedure pointers?
I am not familiar with those.
```

##### ↳ ↳ Re: ANSI 85 vs COBOL2

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-04-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f64dcc4ee3-p3@usenetarchives.gap>`
- **References:** `<950403220531927@star-tech.com> <gap-f64dcc4ee3-p3@usenetarchives.gap>`

```
On Wed, 5 Apr 1995 11:31:32 GMT, Dan Hite (dan··.@sta··h.com) wrote:
›                         IBM's most recent crack at the COBOL
› -> compiler was called COBOL/370 and is now called "COBOL for MVS and VM
…[5 more quoted lines elided]…
› I am not familiar with those.

I haven't used procedure pointers, so can't comment on them. The
intrinsic functions let you do things like this:

COMPUTE TOTAL-FIELD = FUNCTION SUM (TABLE-ARRAY(ALL))

This will add all elements of TABLE-ARRAY and place results into
TOTAL-FIELD. If I am not mistaken, there are 42 functions available
in COBOL.
```

#### ↳ Re: ANSI 85 vs COBOL2

- **From:** "dan..." <ua-author-15699386@usenetarchives.gap>
- **Date:** 1995-04-07T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<950403220531927@star-tech.com>`
- **References:** `<950403220531927@star-tech.com>`

```
-> A book I found helpful was "VS COBOL II for the COBOL Programmer".
-> It's one of those little hardcovered books that McGraw-Hill puts
-> out under the J.Ranade IBM Series.
->
-> If you are already familiar with ANSI 85, some of this book will
-> be review, but it does hit the high points of the IBM implementation,
-> and goes into such things as compiler directives and debugging
-> support.

Thanks for the suggestion! I have checked out "COBOL II" which is
another McGraw-Hill book of the same series. In the intro it described
itself as being for "programmers who have used VS COBOL and wish to
move on to COBOL II" which, strictly speaking I am not since I havn't
used VS COBOL. Your suggestion sounds more ideal! Thanks!

- Dan Hite
```

##### ↳ ↳ Re: ANSI 85 vs COBOL2

- **From:** "klaw..." <ua-author-17087619@usenetarchives.gap>
- **Date:** 1995-04-08T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f64dcc4ee3-p5@usenetarchives.gap>`
- **References:** `<950403220531927@star-tech.com> <gap-f64dcc4ee3-p5@usenetarchives.gap>`

```
In article <950··.@sta··h.com>, dan··.@sta··h.com (Dan Hite) says:
› 
› -> A book I found helpful was "VS COBOL II for the COBOL Programmer".
…[14 more quoted lines elided]…
› - Dan Hite

Dan,

Here's some better information about that book:

VS COBOL II for COBOL Programmers
Author: Paul Kavanagh
1989, Multiscience Press, Inc.
Pubisher: McGraw-Hill Book Company
ISBN 0-07-033571-0

Keith
```

#### ↳ Re: ANSI 85 vs COBOL2

- **From:** "klaw..." <ua-author-17087619@usenetarchives.gap>
- **Date:** 1995-04-07T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f64dcc4ee3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<950403220531927@star-tech.com>`
- **References:** `<950403220531927@star-tech.com>`

```
In article <950··.@sta··h.com>, dan··.@sta··h.com (Dan Hite) says:
› 
› I am a new programmer starting out and will be working with an IBM 3090
…[8 more quoted lines elided]…
› All comments and suggestions are gratefully accepted!

Dan,

A book I found helpful was "VS COBOL II for the COBOL Programmer".
It's one of those little hardcovered books that McGraw-Hill puts
out under the J.Ranade IBM Series.

If you are already familiar with ANSI 85, some of this book will
be review, but it does hit the high points of the IBM implementation,
and goes into such things as compiler directives and debugging
support.

Hope this helps.

Keith
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
