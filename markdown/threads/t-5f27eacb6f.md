[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing large amount of data

_9 messages · 7 participants · 2000-09_

---

### Passing large amount of data

- **From:** "Brad Prothero" <brad.prothero@clarica.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ap9y5.806$KK1.92257@news.corpcomm.net>`

```
Hi, My name is Brad Prothero. I am having a problem knowing what to do with
a project that I am working on.
Environment: I am using Win98 and Fujitsu 5.0 COBOL compiler.
Project: Do calculations for a policy before hand instead of as the proposal
is being printed.
Problem: The calculations are in an array with a total size of 2.5MB. That
data will be passed once to another COBOL program for each proposal that is
illustrated.

Question 1) We are assuming that passing that much between COBOL programs is
a problem. Is it?

Question 1a) If it is a problem, Is there another way to handle this? We are
looking into writting it to a DB and reading it in the other program. That
works as long as I am not writting any Binary data.

Question 2) Has anybody found a way to access a BLOB Data Type using SQL in
Fujitsu 5.0? I tried but I could not figure out how to handle the Blob
address that is sent back. I am using InterBase as the DB engine.

Thank you,
Brad Prothero
Clarica Life Insurance-US
Fargo, ND
```

#### ↳ Re: Passing large amount of data

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c947cd.654100@news>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net>`

```
On Wed, 20 Sep 2000 15:48:32 -0500, "Brad Prothero"
<brad.prothero@clarica.com> wrote:

>Question 1) We are assuming that passing that much between COBOL programs is
>a problem. Is it?
…[7 more quoted lines elided]…
>address that is sent back. I am using InterBase as the DB engine.

Brad,

1)  I'm assuming that you're calling a COBOL subroutine to process the
data in the array.  If so, passing the data is no problem because when
you call a subroutine, you're not really passing the data, only the
address where the data resides; in C terms, a pointer.

2)  So there is no problem if my assumption is true.

3)  BLOB?  That's a new one on me!

Kevin



Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

##### ↳ ↳ Re: Passing large amount of data

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ca548f.21145054@news.epix.net>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net> <39c947cd.654100@news>`

```
Support@ScreenIO.com (Kevin J. Hansen) wrote:

>On Wed, 20 Sep 2000 15:48:32 -0500, "Brad Prothero"
><brad.prothero@clarica.com> wrote:
…[21 more quoted lines elided]…
>3)  BLOB?  That's a new one on me!

Kevin:

BLOB is short for binary large object, a collection of binary data
stored as a single entity in a database management systems (DBMS).
BLOBs are used primarily to hold multimedia objects such as images,
videos, and sound, though they can also be used to store programs or
even fragments of code. Not all DBMSs support BLOBs. 


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Passing large amount of data

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfe90$g0c$1@nnrp1.deja.com>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net> <39c947cd.654100@news>`

```

>
> 3)  BLOB?  That's a new one on me!
>
> Kevin

Hi:

BLOB = Big Lump Of Bytes?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Passing large amount of data

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-09-22T00:12:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000921201203.01965.00000089@nso-fy.aol.com>`
- **References:** `<39c947cd.654100@news>`

```
In article <39c947cd.654100@news>, Support@ScreenIO.com (Kevin J. Hansen)
writes:

>
>3)  BLOB?  That's a new one on me!
>
>

Isn't this Binary-Large-OBject, for handling multi-media type objects?
```

#### ↳ Re: Passing large amount of data

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c986f3.93255581@207.126.101.100>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net>`

```
Query - what database (for the Blob)?

On Wed, 20 Sep 2000 15:48:32 -0500, "Brad Prothero"
<brad.prothero@clarica.com> wrote:

>Hi, My name is Brad Prothero. I am having a problem knowing what to do with
>a project that I am working on.
…[23 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Passing large amount of data

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000921072428.21659.00000074@nso-mg.aol.com>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net>`

```
In article <Ap9y5.806$KK1.92257@news.corpcomm.net>, "Brad Prothero"
<brad.prothero@clarica.com> writes:

>
>Question 1) We are assuming that passing that much between COBOL programs is
…[6 more quoted lines elided]…
>

I have not worked with anything quite that large, but passing large blocks 
of data is a time issue.  I was able to get around the passing of the data 
by using the 'reference'.  This requires that both programs have the same
layout 
and add the 'BY REFERENCE' to explicitly define that you are only passing
a reference pointer to the data in the calling program.  Use of reference
pointers
allows the called program to change the data , so you need to be careful of
what is done in the called program.
```

#### ↳ Re: Passing large amount of data

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-22T03:10:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cacd78.3193639@207.126.101.100>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net>`

```
Well, my experience is only with Oracle and their LONG and LONG BINARY
- for these we use PIC X(2000000) varying... or something similar.  



On Wed, 20 Sep 2000 15:48:32 -0500, "Brad Prothero"
<brad.prothero@clarica.com> wrote:

>Hi, My name is Brad Prothero. I am having a problem knowing what to do with
>a project that I am working on.
…[23 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Passing large amount of data

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0zVy5.5124$5p.33303@news2.mia>`
- **References:** `<Ap9y5.806$KK1.92257@news.corpcomm.net> <39cacd78.3193639@207.126.101.100>`

```
BLOB = Binary Large OBject.

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39cacd78.3193639@207.126.101.100...
> Well, my experience is only with Oracle and their LONG and LONG BINARY
> - for these we use PIC X(2000000) varying... or something similar.
…[6 more quoted lines elided]…
> >Hi, My name is Brad Prothero. I am having a problem knowing what to do
with
> >a project that I am working on.
> >Environment: I am using Win98 and Fujitsu 5.0 COBOL compiler.
> >Project: Do calculations for a policy before hand instead of as the
proposal
> >is being printed.
> >Problem: The calculations are in an array with a total size of 2.5MB.
That
> >data will be passed once to another COBOL program for each proposal that
is
> >illustrated.
> >
> >Question 1) We are assuming that passing that much between COBOL programs
is
> >a problem. Is it?
> >
> >Question 1a) If it is a problem, Is there another way to handle this? We
are
> >looking into writting it to a DB and reading it in the other program.
That
> >works as long as I am not writting any Binary data.
> >
> >Question 2) Has anybody found a way to access a BLOB Data Type using SQL
in
> >Fujitsu 5.0? I tried but I could not figure out how to handle the Blob
> >address that is sent back. I am using InterBase as the DB engine.
…[10 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
