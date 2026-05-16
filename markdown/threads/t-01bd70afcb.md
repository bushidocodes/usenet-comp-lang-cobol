[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 390 Qs

_9 messages · 7 participants · 1999-07 → 1999-08_

---

### COBOL 390 Qs

- **From:** "marvy x" <marvy@teleport.com>
- **Date:** 1999-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
My shop is setting up COBOL 390 on our MVS system.  It should be up and
available within a couple of months.  We are setting up our COBOL 390
compiler with a default of NOCMPR2 and without the OO extensions.  I'm kind
of excited because COBOL 390 has some neat features that I want to start
using like the NumVal() functions and it has a better language interface.
These new functions should be helpful because we have Peoplesoft installed
on MVS and Peoplesoft uses the SQR language a lot and SQR produces data for
C, not COBOL.  With COBOL 390's improved handling of C type of data we
should be able to make our Peoplesoft batch interface programs much
friendlier and easier to work on.

Anyway, I have a couple of questions that someone here may know something
about.

1.  We currently have Expediter in our shop.  I don't use it because I've
had problems in the past with interactive debuggers not executing exactly
the same as the compiled binary.  For example, when we first started using
Expediter a few years ago one programmer used it to verify that a search
worked correctly.  When the program went into production it bombed because
the Expediter search worked a little differently than the compiled
production search.  Has anyone found any similar problems with the COBOL 390
debugger?  Is COBOL 390's debugger more or less useful than Expediter?

2.  I would love to have dynamic internal table sizes when I load flat file
tables.  In our shop we get a lot of table overflow ABENDs when clients
increase table sizes without the courtesy of letting us know they are doing
so before-hand.  Someone in my shop said that you could create dynamically
sized tables in COBOL 390, but I don't see how this could be done.  COBOL
390 does have a better language interface, so maybe tables could be
dynamically loaded using C subroutines using it's malloc() function.   If a
C subroutine was used a C binary search subroutine would be needed as well
as a free() subroutine when the COBOL program ended.  Which sounds like a
lot of overhead.  Has anyone gotten COBOL 390 to do dynamically sized
internal tables?  I know that I could define some bodaciously sized variable
length tables, but this would require using a lot of region space,
especially in programs with a just a few internal tables.   Maybe there is a
trick that can be done using the OO extensions?

Scott
```

#### ↳ Re: COBOL 390 Qs

- **From:** docdwarf@clark.net ()
- **Date:** 1999-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_FLo3.374$hC5.19072@iad-read.news.verio.net>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
In article <JOJo3.24584$9.888923@news1.teleport.com>,
marvy x <marvy@teleport.com> wrote:

[snippage about stuff outside of my bailiwick]

>2.  I would love to have dynamic internal table sizes when I load flat file
>tables.  In our shop we get a lot of table overflow ABENDs when clients
>increase table sizes without the courtesy of letting us know they are doing
>so before-hand.  Someone in my shop said that you could create dynamically
>sized tables in COBOL 390, but I don't see how this could be done.

Leaving aside the ever-popular OCCURS n TO nn TIMES DEPENDING ON... I
would say that such ABENDs are a Very Good Thing as they prevent a
programming from outgrowing its design.

A coding solution, especially one which depends on internal tables, is
*rarely*, in my experience, One Size Fits All.

DD
```

#### ↳ Re: COBOL 390 - Using OO

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A392E3.28BCCFA@home.com>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
marvy x wrote:
> 
> internal tables?  I know that I could define some bodaciously sized variable
…[4 more quoted lines elided]…
> Scott

I can just see them now, here he goes again.

Glad you have access to OO. I have no idea what your 390 product
includes, but if you've got access to arrays/collections/dictionaries
that maybe your solution. I'm using dynamic table creation,
(collections/dictionaries) in NetExpress on a PC - obviously volumes
aren't the same. If relevant - let me know if you want to pursue this -
I'd need to know what method-names you may have. How many entries, max,
in your tables - not an OO problem but memory availability.

Been searching, even went to an IBM retail shop. Can you point me to a
site which covers IBM OO ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: COBOL 390 - Using OO

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o0bpc$e2j@dfw-ixnews19.ix.netcom.com>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com> <37A392E3.28BCCFA@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:37A392E3.28BCCFA@home.com...
  <snip>

> Been searching, even went to an IBM retail shop. Can you point me to a
> site which covers IBM OO ?
>
> Jimmy, Calgary AB

For an insight into the IBM approach to OO (with COBOL) - available on
OS/390, OS/2, Windows, and Unix, see

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/3%2e0

which is (for the web-less), the chapter,
  "3.0 Part 3. Object-Oriented Programming Topics"

in
 Title: COBOL for OS/390 & VM Programming Guide
  Document Number: SC26-9049-04
```

###### ↳ ↳ ↳ Re: COBOL 390 - Using OO

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A3CE55.9BC40EA8@home.com>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com> <37A392E3.28BCCFA@home.com> <7o0bpc$e2j@dfw-ixnews19.ix.netcom.com>`

```
William M. Klein wrote:
> 
> James J. Gavan <jjgavan@home.com> wrote in message
…[6 more quoted lines elided]…
> 
Thanks Bill, you're a gem.

Jimmy, Calgary AB
```

#### ↳ Re: COBOL 390 Qs

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990731223824.13701.00002643@ngol03.aol.com>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
In article <JOJo3.24584$9.888923@news1.teleport.com>, "marvy x"
<marvy@teleport.com> writes:

>dynamically loaded using C subroutines using it's malloc() function.   If a
>C subroutine was used a C binary search subroutine would be needed as well
…[6 more quoted lines elided]…
>

I can't say for OS/390 as we have not yet made a successful migration yet, but
under MVS we use Assembler routines for most flat file table lookup processes.
This does run in to problems when the total table size gets to be 800M.  I have
started using COBOL ISAM lookup sub-programs that read the flat file into a
temporary ISAM structure at BOJ then does a RANDOM READ NEXT for the 
entries needed.  This has reduced the memory requirements of my programs from
800M for the table to 800K for the I/O routines and record area.
```

#### ↳ Re: COBOL 390 Qs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o2269$bg1@dfw-ixnews6.ix.netcom.com>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
See below for replies,
```

##### ↳ ↳ Re: COBOL 390 Qs

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990801190043.04836.00005992@ng-bk1.aol.com>`
- **References:** `<7o2269$bg1@dfw-ixnews6.ix.netcom.com>`

```
In response to an earlier question, Bill Klein wrote...

[snip]

>
>B) LE (Language Environment) - which is the required run-time feature for
…[12 more quoted lines elided]…
>

Or <commercial alert>, you could bring us in to teach our course "Application 
Design Using LE Services + Beyond COBOL II" (four days), which covers LE
concepts, 
all the LE callable services (in Assembler, COBOL, PL/I, and C) as well as a 
thorough discussion of changes in IBM COBOL compilers from VS COBOL II to the 
present. We even have an example of using LE services to dynamically change 
table size in COBOL (with appropriate cautions).
<\commercial>.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: COBOL 390 Qs

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A4E4AD.B8AFDDBA@zip.com.au>`
- **References:** `<JOJo3.24584$9.888923@news1.teleport.com>`

```
marvy x wrote:
> 
> 1.  We currently have Expediter in our shop.  I don't use it because
…[7 more quoted lines elided]…
> more or less useful than Expediter?

Xpeditor is still the debugger of choice for MVS IMHO.  Intertest is a
bit clunky on the interface side as mentioned elsewhere.  Neither of
these come automatically with the installation so check what you are
really getting.

The problem with compiler output changing does not go away.  It is
very typical for development to be done with optimizations turned off
to speed the compile, when it goes into production it is turned on for
run time efficiency.

Work around:   Turn on SSRANGE in development.  The compiler is 99.9%
not the problem it is the code.  Table overruns when the working
storage is moved around it changes the nature of the abend (took 3
months to find one, bombs in production works perfectly in
development).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
