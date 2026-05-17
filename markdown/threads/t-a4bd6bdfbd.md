[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to use Visual Basic with ISAM file

_8 messages · 7 participants · 1996-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### How to use Visual Basic with ISAM file

- **From:** "kit..." <ua-author-15671806@usenetarchives.gap>
- **Date:** 1996-02-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4esva7$9u@senior.nectec.or.th>`

```
Is there anyone know about how to use Visual Basic with to read
COBOL ISAM file ? I don't clear about this, and where I can find
the library for manage it ?

Thank you,
Mr. Nopparut W.

Please respond to : eng··.@cdg··o.th ( or
kit··.@moz··o.th )
```

#### ↳ Re: How to use Visual Basic with ISAM file

- **From:** "jjag..." <ua-author-17086461@usenetarchives.gap>
- **Date:** 1996-02-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4esva7$9u@senior.nectec.or.th>`
- **References:** `<4esva7$9u@senior.nectec.or.th>`

```
You will find it easier to convert the ISAM file to a VSAM file. ISAM
files died
out over a decade ago but a few ISAM applications still exist as you can
attest..

If you have Cobol programs that are still reading and/or updating the ISAM
file,
then the Cobol programs can also be very quickly converted to read/update
a VSAM file instead of the old ISAM file. I performed dozens of these
types
of conversions in the early 80s.

The major advantage VSAM had over ISAM was that VSAM allows Cobol programs
to physically delete records from the VSAM file at run-time. This
allowed programs to reuse the space that was occupied by the deleted
record immediately.

ISAM, on the other hand, required Cobol programs to logically delete
records by placing a non-blank character in the field known as the
Delete-Byte (usually
the first byte on ISAM records). The record remained on the file until a
utility
was executed to reorg the ISAM file and release the space. Cobol programs
would "transparently" interrogate the Delete-Byte whenever record(s) were
retrieved on the ISAM file. If the Delete-Byte was "on", then the program
would
issue a "Not Found" condition even though the record was still physically
on file.

If you would like more info on converting from ISAM to VSAM, please email
me.

John Jung
Houston
Please email me if you would like more
information.
```

##### ↳ ↳ Re: How to use Visual Basic with ISAM file

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-02-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a4bd6bdfbd-p2@usenetarchives.gap>`
- **References:** `<4esva7$9u@senior.nectec.or.th> <gap-a4bd6bdfbd-p2@usenetarchives.gap>`

```
Correct me if I'm wrong, PC COBOLs still uses a form of ISAM while its
mainframe counterparts are VSAM. I have a couple of PC COBOL
compilers (IBM and Microsoft) the syntax hints at a ISAM processing
method - that is, you still need a special program to "clean up" an
indexed file (one that will removed any "tagged for deletion"
records). I think there may be a limitation of PC DOS in preventing
full usage of VSAM technology. Or VSAM is an IBM proprietary product.

If VB can't access COBOL-created indexed files directly, perhaps a
COBOL program to extract records to a sequential file followed by
importing that file to VB.

Just my two cents.
Boyce Williams
```

#### ↳ Re: How to use Visual Basic with ISAM file

- **From:** "he..." <ua-author-17086174@usenetarchives.gap>
- **Date:** 1996-02-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4esva7$9u@senior.nectec.or.th>`
- **References:** `<4esva7$9u@senior.nectec.or.th>`

```
kittie erzÃ¤hlte am 02.02.96 was Ã¼ber
How to use Visual Basic with ISAM file ...
Moment! Hexe meint dazu... :-))
--------------------------------------------------------------------------

k>Is there anyone know about how to use Visual Basic with to read
k>COBOL ISAM file ? I don't clear about this, and where I can find
k>the library for manage it ?
k>
k>Thank you,
k>Mr. Nopparut W.
k>
k>Please respond to : eng··.@cdg··o.th ( or
k> kit··.@moz··o.th )

First you need the professional version of Visual Basic.
Only this version can handle with ISAM files.
I think, you have to give an option in Cobol to say, this file
will be used of other programs (non-cobol), too
Sorry, I'm not that firm in Visaul Basic :-(


hear from you soon
Hexe :)
```

#### ↳ Re: How to use Visual Basic with ISAM file

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1996-02-05T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4esva7$9u@senior.nectec.or.th>`
- **References:** `<4esva7$9u@senior.nectec.or.th>`

```
Two ways:
1. Write a Windows COBOL DLL which you call from Visual BASIC.
The COBOL DLL program would open the COBOL Isam and return values
to the Visual BASIC program. This would require having a COBOL
compiler which can produce DLL routines.

2. Use a ODBC driver for Micro Focus ISAM if it exists.


Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: How to use Visual Basic with ISAM file

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1996-02-05T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4esva7$9u@senior.nectec.or.th>`
- **References:** `<4esva7$9u@senior.nectec.or.th>`

```
Two ways:
1. Write a Windows COBOL DLL which you call from Visual BASIC.
The COBOL DLL program would open the COBOL Isam and return values
to the Visual BASIC program. This would require having a COBOL
compiler which can produce DLL routines.

2. Use a ODBC driver for Micro Focus ISAM if it exists.


Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: How to use Visual Basic with ISAM file

- **From:** "j..." <ua-author-6042917@usenetarchives.gap>
- **Date:** 1996-02-12T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<4esva7$9u@senior.nectec.or.th>`
- **References:** `<4esva7$9u@senior.nectec.or.th>`

```
kit··.@moz··o.th (Kittivud Eabcharoen) wrote:

› Is there anyone know about how to use Visual Basic with to read
› COBOL ISAM file ? I don't clear about this, and where I can find
› the library for manage it ?

Liant Software makes a product called Relativity that allows Micro
Focus COBOL ISAM files to be represented as a relational database.
They may then be accessed by any ODBC-compliant frontend application,
including VB.

Liant can be reached at rel··.@ri.··t.com or 512-719-7000.

Regards,
John
```

##### ↳ ↳ Re: How to use Visual Basic with ISAM file

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1996-02-13T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a4bd6bdfbd-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a4bd6bdfbd-p7@usenetarchives.gap>`
- **References:** `<4esva7$9u@senior.nectec.or.th> <gap-a4bd6bdfbd-p7@usenetarchives.gap>`

```
› kit··.@moz··o.th (Kittivud Eabcharoen) wrote:
› 
›› Is there anyone know about how to use Visual Basic with to read
›› COBOL ISAM file ? I don't clear about this, and where I can find
›› the library for manage it ?

I spotted this bit on the MF web pages:

CorrelateÂ v1.0

Detailed Product Information


Micro Focus Correlate allows ODBC-enabled applications to access data
held in Micro Focus COBOL data files. COBOL
record layouts are mapped onto relational database tables by a
management tool, which creates a data dictionary for use by an
ODBC driver. Micro Focus Correlate makes it possible for popular desktop
tools such as Excel, IQ, Crystal Reports, Forest &
Trees, Q+E, Visual Basic, PowerBuilder and Delphi to use COBOL data. The
data is not modified in any way, and COBOL
applications can run alongside Micro Focus Correlate. It is possible to
update COBOL data via Micro Focus Correlate, but an
administrative option can disable this if required. Micro Focus
Correlate is available as a standalone package (Single-tier) for use
with Microsoft Windows, and as a client/server package (Multiple-tier)
for use with Microsoft Windows workstations, Windows
NT, and UNIX servers.

Phone nos were UK: 01635 32646 and US: (415) 856-4161 / (800) 872-6265

Else look on http://www.mfltd.co.uk/Corporate/distrib.htm

Martyn      (m.··.@mfl··o.uk)
Phone: +44 (0)1635 565 358, fax +44 (0)1635 565 567
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
