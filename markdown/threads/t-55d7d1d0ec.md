[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# pl/i

_6 messages · 3 participants · 2003-10_

---

### pl/i

- **From:** "Louis De Bevere" <louis.de.bevere@pandora.be>
- **Date:** 2003-10-15T18:05:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be>`

```
Hi,

I am not a cobol programmer (although i know it a little), but for the
current project we need a cobol program that will call a pl/i program.
Anyone knows how?  What things i have to consider?

Louis
```

#### ↳ Re: pl/i

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-15T18:12:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net>`
- **References:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be>`

```
You don't tell us your environment (operating system or compiler) - but if
this HAPPENS to be an IBM mainframe environment (where PL/I is medium
common), check out:

 "11.0 Chapter 11. Communicating between COBOL and PL/I"

at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA4110/11.0
```

##### ↳ ↳ Re: pl/i

- **From:** "Louis De Bevere" <louis.de.bevere@pandora.be>
- **Date:** 2003-10-15T19:54:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EBhjb.79957$Hy2.4273190@phobos.telenet-ops.be>`
- **References:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be> <T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net>`

```
Thanks!

And it is a IBM mainframe...

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net...
> You don't tell us your environment (operating system or compiler) - but if
> this HAPPENS to be an IBM mainframe environment (where PL/I is medium
…[24 more quoted lines elided]…
>
```

##### ↳ ↳ Re: pl/i

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-10-16T17:52:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmmi3i$u51$1@hyperion.microfocus.com>`
- **References:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be> <T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net>`

```
Hi Bill,

Is there any other implementation of PL/1 in use? Apart from the coverage
Micro Focus gives it.

Paul

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net...
> You don't tell us your environment (operating system or compiler) - but if
> this HAPPENS to be an IBM mainframe environment (where PL/I is medium
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ OT: pl/i

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-16T22:34:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k2Fjb.3207$7a4.1533@newsread4.news.pas.earthlink.net>`
- **References:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be> <T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net> <bmmi3i$u51$1@hyperion.microfocus.com>`

```
"Paul Barnett" <paul.barnett@nospam.microfocus.com> wrote in message
news:bmmi3i$u51$1@hyperion.microfocus.com...
> Hi Bill,
>
…[4 more quoted lines elided]…
>

From the PL/I "FAQ"

"(Q2) On what systems is it available?
.
     PL/I is available on at least the following systems:
.
 IBM PC and compatibles (80x86).
.
        *  IBM VisualAge PL/I: is available in 2 versions:
  Professional Edition } Details at the bottom of this posting
                Personal Edition        }
  accompanied by the
  live editor LPEX
  ---available from IBM
.
        *  Liant Open PL/I, for Intel running Windows XP, 2000, Me/98.
  Comes with Codewatch, Liant's powerful GIU source code debugger.
  ---available from Liant Software Corporation,
         8911 N Capital of Texas Hwy 354 Waverley Street
         Austin, Texas 78759-7267 Framingham, MA 01702
         USA USA
         Toll free: 1-800-349-9222
         Tel: (512) 343-1010 (508) 416-1614 Direct
         Fax: (512) 343-9487 or
                                  Tel: (800) 818-4754 X1614 (USA Only)
                                  Fax: (508) 278-3841
  (their PL/I generally is available on Unix-based systems)
                See            http://www.liant.com/products/pl1
  for a full range of PL/I products.
.
        *  Windows NT -- available from IBM as VisualAge PL/I Professional
       and Personal editions, with the live parsing editor LPEX.
.
 *  Liant Open PL/I for Redhat Linux (Intel).
.
 *  Solaris ix (Intel)
.
     IBM AS/400
      --- available from IBM.
.
     IBM mainframes
  --- The followng versions are available from IBM:
            IBM Enterprise PL/I for z/OS and OS/390
      provides access to DB2, CICS, IMS, and other data and
      transactions systems.
.
 *     VisualAge PL/I for OS/390
.
 *     PL/I for MVS & VM
.
 *     PL/I for VSE
.
 *     PL/I for VSE/ESA is for MVS & VM
.
        * IBM OS/390 (IBM z/OS) available as Enterprise PL/I.
.
     HP 9000 HP-UX
  --- available from Liant Software Corporation.
  Comes with Codewatch, Liant's powerful GIU source code debugger.
.
     UNIX.
  Older versions of Liant Open PL/I exist for Unix variants,
  sold off-the-shelf with limited support. Users can
  inquire at http://www.liant.com
.
     SPARC Solaris 2.x
  --- available from Liant Software Corporation.
  Comes with Codewatch, Liant's powerful GIU source code debugger.
.
     IBM RS/6000 AIX
  --- available from Liant Software Corporation (address above);
                    Comes with Codewatch, Liant's powerful GIU source
      code debugger.
  --- also available from IBM as Enterprise PL/I.
.
     Data General AViiON with DG-UX
  --- available from Liant Software Corporation
                    Comes with Codewatch, Liant's powerful GIU source
      code debugger.
.
     Compaq (formerly Digital Equipment Corporation) on Open VMS and Alpha
    AXP systems (Tru64 Unix)
  ---The compilers from Kednos Corporation for these systems are
     called "PL/I for Open VMS" and "PL/I for Tru64 Unix"
     respectively.  They took over support for PL/I from UniPrise.
.
  Take a look at Kednos' web page: http://www.kednos.com
  for manuals and compilers.
  For infomation, contact tom@kednos.com
.
     Stratus Computer, Inc. under VOS on all their systems except AX/R-S.
  --- available from Stratus Computer, Inc.
   55 Fairbanks Boulevard,
   Marlboro, Massachusetts 01752.
.
     Wang/Getronics systems.  Recent updates make the compiler Y2K
compliant.
  --- available from Wang Laboratories, Billerica, Mass.
.
     Fujitsu-Siemens BS2000 system.
  --- visit them at:
  http://www.fujitsu-siemens.com/servers/pl1/pl1_us.htm
  where you can download a specification brochure in PDF format."
```

###### ↳ ↳ ↳ Re: pl/i

_(reply depth: 4)_

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-10-21T10:37:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn2uj9$9if$1@hyperion.microfocus.com>`
- **References:** `<u%fjb.79698$TT1.4164667@phobos.telenet-ops.be> <T5gjb.2187$s93.102@newsread3.news.pas.earthlink.net> <bmmi3i$u51$1@hyperion.microfocus.com> <k2Fjb.3207$7a4.1533@newsread4.news.pas.earthlink.net>`

```
Thanks. ;-)

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:k2Fjb.3207$7a4.1533@newsread4.news.pas.earthlink.net...
> "Paul Barnett" <paul.barnett@nospam.microfocus.com> wrote in message
> news:bmmi3i$u51$1@hyperion.microfocus.com...
> > Hi Bill,
> >
> > Is there any other implementation of PL/1 in use? Apart from the
coverage
> > Micro Focus gives it.
> >
…[111 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
