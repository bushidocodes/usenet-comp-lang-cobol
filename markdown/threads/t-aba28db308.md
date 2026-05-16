[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File status 96 - File system not available

_5 messages · 4 participants · 2003-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### File status 96 - File system not available

- **From:** klaus.duttle@online.de (m8java)
- **Date:** 2003-01-14T17:03:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba4d0b76.0301141703.4426fe3e@posting.google.com>`

```
Hi coboler,

my problem occurs in a tiny program, that runs on the host very fine.
To run it on the AIX platform I've compiled with cob2, IBMs Cobol Set
for AIX version 1.1. Now I get in the open-routine a file status 96
and nowhere I found any useful information about this message. Only
in the COBOL Language Reference on page 274 exists a table with brief
hints for each file status:

96 For VSAM file under OS/390 and VM: An OPEN statement with the
   OUTPUT or EXTEND phrase was attempted for an optional file, but no DD
   statement was specified for the file.
   For QSAM file under OS/390 and VM: An OPEN statement with the
   OUTPUT or EXTEND phrase was attempted for an optional file, but no DD
   statement was specified for the file and the CBLQDA(OFF) run-time option
   was specified.
   Under AIX, OS/2, and Windows: File system not available.
   =========

How I can get the file system available?

Here is a snipet of the cobol source:

FILE-CONTROL.
    SELECT LISTE1 ASSIGN TO 'STL-LISTE1'
            FILE STATUS IS STATUS-BYTES.
...
DATA DIVISION.
FILE SECTION.
FD  LISTE1
    RECORDING MODE    IS F.
       01  DL1-ZEILE.
           05 DL1-VSZ          PIC X.
           05 DL1-DATEN        PIC X(132).

       01  QLDD-ZEILE.
           05                    PIC X(001).
           05 QLDD-DATEN         PIC X(132).
...
OPEN-ROUTINE SECTION.
    OPEN  OUTPUT LISTE1
...

Also I've tried an alternate construction in the FILE-CONTROL.
Coding

FILE-CONTROL.
    SELECT LISTE1 ASSIGN USING 'STL-LISTE1'
               FILE STATUS IS STATUS-BYTES.

will result in a severe compiler error IGYDS0093-S:

IGYDS0093-S   "'STL-LISTE1'" was found in the "ASSIGN" clause.
              The clause was discarded.

And again there are nowhere useful documentation for such
error numbers.

The last question to the Cobol experts:
When I have to use the STL file system?
Maybe the file 'LISTE1' has to be a VSAM file.
However the file 'LISTE1' should be created
by the cobol program and located on the AIX
file system.

Thanks

Klaus Duttle
```

#### ↳ Re: File status 96 - File system not available

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2003-01-15T01:33:12
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b02dni$tkb$1@newsg4.svr.pol.co.uk>`
- **References:** `<ba4d0b76.0301141703.4426fe3e@posting.google.com>`

```
Is this '96' a two byte variable (h3936 or h3906) taken from the
file status ? h3906 would be 'unable to write to a read-only file'
on the PC. I have no description for h3936 again on the PC.

"m8java" <klaus.duttle@online.de> wrote in message
news:ba4d0b76.0301141703.4426fe3e@posting.google.com...
> Hi coboler,
>
…[12 more quoted lines elided]…
>    statement was specified for the file and the CBLQDA(OFF) run-time
option
>    was specified.
>    Under AIX, OS/2, and Windows: File system not available.
…[50 more quoted lines elided]…
> Klaus Duttle
```

#### ↳ Re: File status 96 - File system not available

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-01-15T02:25:11-12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b02dk3$1f2$1@aklobs.kc.net.nz>`
- **References:** `<ba4d0b76.0301141703.4426fe3e@posting.google.com>`

```
m8java wrote:

> my problem occurs in a tiny program, that runs on the host very fine.
> To run it on the AIX platform I've compiled with cob2, IBMs Cobol Set
> for AIX version 1.1. 

Isn't that a variety of MicroFocus ?

> Now I get in the open-routine a file status 96

Status codes 9x are vendor specific.  If it is MF then the '6' is the ASCII 
character for decimal 36 and this means: 'File already exists'.  This may 
be a permission issue in that the file exists but you do not have write 
access to it, or to the directory that this is in.

AIX is a variety of Unix and you have to take notice of users, groups and 
permissions.


> Also I've tried an alternate construction in the FILE-CONTROL.
> Coding
…[3 more quoted lines elided]…
>                FILE STATUS IS STATUS-BYTES.

What is 'ASSIGN USING' supposed to be ?
```

##### ↳ ↳ Re: File status 96 - File system not available

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-01-15T12:11:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b0488k$li7$1@slb4.atl.mindspring.net>`
- **References:** `<ba4d0b76.0301141703.4426fe3e@posting.google.com> <b02dk3$1f2$1@aklobs.kc.net.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b02dk3$1f2$1@aklobs.kc.net.nz...
> m8java wrote:
>
…[4 more quoted lines elided]…
> Isn't that a variety of MicroFocus ?

No, CobolSet is *not* an  Micro Focus based product.  (There is a Micro Foc
us product for AIX - and IBM used to "repackage" it as an IBM product but
that hasn't been true for MANY years)
```

#### ↳ Re: File status 96 - File system not available

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-01-15T12:16:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b048ib$dn2$1@slb1.atl.mindspring.net>`
- **References:** `<ba4d0b76.0301141703.4426fe3e@posting.google.com>`

```
1) I think you will find that "ASSIGN USING" requires a data-name following
the USING - while ASSIGN TO can be followed by a literal.

2) In general, have you read the section
    "Identifying Files to the Operating System"

on page 17 of the COBOL Set Programming Guide - available on line at:

    http://www-3.ibm.com/software/ad/cobol/aix/library/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
