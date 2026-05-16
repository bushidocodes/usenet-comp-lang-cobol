[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: locating Unisys flavored PC Compiler

_8 messages · 7 participants · 2000-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help: locating Unisys flavored PC Compiler

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-11-01T11:13:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001101061320.14720.00000165@nso-ff.aol.com>`

```
Does anyone know of a PC Compiler vendor that has a COBOL
product that works with the Unisys extensions?

Allowing Random/Dynamic access of sequential files,
VALUE OF AREAS, FILENAME, FAMILYNAME in FD,
yadda, yadda, yadda...

I thought at one point in time there was such a vendor,
but the latest compilers that I have been working with are 
more IBM centric.   Any assistance would be greatly appreciated.

BTW, I am specifically interested in compilers that are compatible
with the Unisys A-Series syntax, it would be helpful if it also worked 
with the Unisys V-Series syntax as well.

Thanks all.
```

#### ↳ Re: locating Unisys flavored PC Compiler

- **From:** "Ralph Leiherr" <leiherr@vwda.de>
- **Date:** 2000-11-03T09:04:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ttrjb$3gi$00$1@news.t-online.com>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com>`

```
Hi,

we are change the system from a Unisys A-Series "A4-FS" to Windows-NT and we
also
searching for a compiler who "speak" the Unisys extensions, but we are no
found. Now we use the Merant Cobol-Compiler and we change the code. But we
found for all extensions a way that works on a PC !

Hope this help.

Ralph Leiherr


----- Original Message -----
From: "Sff5ky" <sff5ky@aol.comxxx123>
Newsgroups: comp.lang.cobol
Sent: Wednesday, November 01, 2000 12:13 PM
Subject: Help: locating Unisys flavored PC Compiler


> Does anyone know of a PC Compiler vendor that has a COBOL
> product that works with the Unisys extensions?
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: locating Unisys flavored PC Compiler

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tuv2n$2mm$1@nntp9.atl.mindspring.net>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com> <8ttrjb$3gi$00$1@news.t-online.com>`

```
I have submitted this question to "my sources" at Unisys - and so far not
received any "useful" information.  I will keep the NG aware as the
"research" continues.
```

###### ↳ ↳ ↳ Re: locating Unisys flavored PC Compiler

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a032b45.63709327@207.126.101.100>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com> <8ttrjb$3gi$00$1@news.t-online.com> <8tuv2n$2mm$1@nntp9.atl.mindspring.net>`

```
I think you'll have a hard time getting assistance from Unisys for a
Unisys to PC conversion.


On Fri, 3 Nov 2000 12:11:04 -0600, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>I have submitted this question to "my sources" at Unisys - and so far not
>received any "useful" information.  I will keep the NG aware as the
…[51 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: locating Unisys flavored PC Compiler

_(reply depth: 4)_

- **From:** Fred Snyder <fpsnyder@bellsouth.net>
- **Date:** 2000-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A041467.8E9B0503@bellsouth.net>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com> <8ttrjb$3gi$00$1@news.t-online.com> <8tuv2n$2mm$1@nntp9.atl.mindspring.net> <3a032b45.63709327@207.126.101.100>`

```
Several years ago there were two companies that provided such compilers, base on
the Micro Focus COBOL Workbench. They were Open Systems in Jacksonville and ESI
in Tallahassee both of which "I believe" have moved on to other ventures based on
the lack of need for such software.

Thane Hubbell wrote:

> I think you'll have a hard time getting assistance from Unisys for a
> Unisys to PC conversion.
…[61 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Help: locating Unisys flavored PC Compiler

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2000-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u6uti$oh9$1@mail.pl.unisys.com>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com>`

```
Don't know of any such product, but in general I'd expect there should be
analogous mechanisms available, either in the file system or in the language
itself, for at least some of these on the target system.

The VALUE OF clause specifies "file attributes" in general, and two of the
ones you list describe the external name of the file (FAMILYNAME and
FILENAME; note that TITLE includes both parts of the file's full name).  The
third, the AREAS attribute, specifies the segmentation of the file on disks,
and this, too, is less a function of COBOL than of the file system
implementation being used.   If there are no other significant attributes
being used, these shouldn't be difficult substitutions.

As to DYNAMIC access to SEQUENTIAL files, none of the A Series COBOL
compilers (COBOL(68), COBOL74 or COBOL85) eem to support that, at least as a
documented feature.  RANDOM, yes.  DYNAMIC, no.    DYNAMIC is available only
with RELATIVE and INDEXED file organizations.

And in the case of RANDOM access to SEQUENTIAL files, there's a real
"gotcha" associated with that application approach:  It's always the user's
responsibility to know whether or not a just-read record occurring before
the end of the file was actually written deliberately into the file in the
first place rather than just leftover stuff from some other file that used
to be where the file now is!  RELATIVE has the advantage of getting
"notfound" conditions in the middle of the file, and I think that's a lot
safer overall than perpetuating the brute-force approach of the
RANDOM/SEQUENTIAL combination, which dates back at least to the earliest
days of Burroughs Large System COBOL(68) (and probably earlier!) -- long
before the ANSI-74 extensions that included ISAM were added to that
compiler -- and has been maintained for compatibility and convenience ever
since.  .Better to modernize the application a bit, I think.

    -Chuck Stevens

Sff5ky <sff5ky@aol.comxxx123> wrote in message
news:20001101061320.14720.00000165@nso-ff.aol.com...
> Does anyone know of a PC Compiler vendor that has a COBOL
> product that works with the Unisys extensions?
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help: locating Unisys flavored PC Compiler

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-11-07T01:39:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001106203910.18044.00000050@nso-fz.aol.com>`
- **References:** `<8u6uti$oh9$1@mail.pl.unisys.com>`

```
In article <8u6uti$oh9$1@mail.pl.unisys.com>, "Chuck Stevens"
<charles.stevens@unisys.com> writes:

>to be where the file now is!  RELATIVE has the advantage of getting
>"notfound" conditions in the middle of the file, and I think that's a lot
…[6 more quoted lines elided]…
>

Thanks for the reply.

Unfortunately, most of these programs are from maybe 30 years ago in design
and many years of maintenance.  Some progress has been made to shift from
COBOL68 to COBOL74, but coming any further forward could prove to require 
some major re-writes.  Using such 'Brute force' methods we are able to process
our files significantly faster than using standard access methods.  The ISAM
option
has been used in places where multiple keys are needed , but some cases end 
up reducing run-time efficiency.  
We process millions of records per night and have a VERY tight window
to complete all batch processing requirements before needing to have the
files available for the next day's procesing.

The PC processing option is just an exercise in offloading some reporting 
processes or preliminary file editing processes.
```

#### ↳ Re: locating Unisys flavored PC Compiler

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2000-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ualpg$341q$1@newssvr06-en0.news.prodigy.com>`
- **References:** `<20001101061320.14720.00000165@nso-ff.aol.com>`

```
This may or may not help your specific situation, but assuming you still
have source code for some of these programs, we ended up creating smaller
extract files for PC reports from our V-series main processing programs,
then downloading these work files to a PC via Core Technology Bridge32
download software (Attachmate also makes such a product). WE then processed
the "work" file with Microfocus PC COBOL 3.5.  We changed any FD's from
VALUE OF FILENAME to VALUE OF ID, ignored the FAMILY NAME, etc. and borrowed
much of the actual processing code from the V-series.  We ran into some
snags with Random Access files, since UNISYS and Microfocus handle such
files differently.

However, since we converted to the NX-5600 Clearpath system (formerly the
A-Series), we can now map a network drive to the mainframe itself.  We
switched to Fujitsu PowerCobol 5.0 and we're converting some mainframe
programs into that language.  The neat thing is that we can read most fixed
length files directly from the "mapped" drive and NXServices handles the
EBCDIC to ASCII conversion for you. Thus no download software or FTP process
is needed.  Our approach is to just load the UNISYS source code into
Fujitsu, compile it, and fix the errors.  Obviously, any system "call"
routines have to be examined, but we are primarily just doing this process
for straight-forward reporting type programs that don't need system call
features.  Haven't tried any RANDOM files yet.  Suprisingly, we haven't had
to do as much work as I had originally thought we would.  And the PowerCobol
Windows interface makes it look as though you were writing in any other
Windows programming language.  Can't tell you how many people have asked if
the application was written in Visual Basic, C++, JAVA, etc. :~).

As a disclaimer, we never intended to use any PC COBOL product as a
"pre-compiler" for the UNISYS programs, which is why we moved from
MicroFocus to Fujitsu.  Since us UNISYS folks are "the other guys", we make
do with what we have, and you are correct in stating that most PC products
are slanted towards the IBM world.

Denny

"Sff5ky" <sff5ky@aol.comxxx123> wrote in message
news:20001101061320.14720.00000165@nso-ff.aol.com...
> Does anyone know of a PC Compiler vendor that has a COBOL
> product that works with the Unisys extensions?
…[16 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
