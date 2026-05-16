[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM and COBOL File Status = 39

_4 messages · 3 participants · 2003-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### IBM and COBOL File Status = 39

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-10T23:43:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LoVrb.8715$6c3.1487@newsread1.news.pas.earthlink.net>`

```
To IBM-MAIN & comp.lang.cobol (and CC to others)

When IBM first came out with their '85 Standard compiler (VS COBOL II, V3.0)
all those YEARS ago, one of the major migration inhibitors was "file status
= 39" for "fixed file attribute conflicts".  As I recall it, it was one of
the major reasons that SOME shops stayed with the CMPR2 compiler option.

By the time that this "problem" was identified in IBM's implementation,
ANSI/ISO had already "clarified" the requirement for FS=39 to state that it
was IMPLEMENTOR DEFINED which attributes conflicts (if any?) would cause
this condition to be raised.

I am curious whether FS=39 is *still* a problem with any/many IBM
(mainframe) shops?  Would you "LIKE" it if IBM "enhanced" their
compiler/run-time to NOT issue a FS=39 in certain/all situations and/or if
they provided an "installation" option for modifying this?

It is CLEAR that the current behavior is "fully" conforming to both the '85
and the 2002 ANSI/ISO COBOL Standards.  However, it is equally true that IBM
*could* relax this  and STILL be conforming.

I am *thinking* about creating a SHARE requirement for IBM to make such an
enhancement - but I don't know whether shops have "changed" their
code/situations so that this is no longer a real issue (and not worth IBM
development effort) or whether IBM COBOL application programmers would STILL
like the current restrictions removed.

NOTE:  In a much earlier release, IBM "fixed" the run-time messages so that
it is now "relatively" easy to understand and fix application programs that
have such an error.  However, there are also cases where CMPR2 and pre-VS
COBOL II code "worked fine and expected" with attribute conflicts that now
can't be run/developed.  Do your application programmers find it USEFUL to
"detect" fixed file attribute conflicts - or do they find it a "pain in the
neck" to know at compile-time all these attributes (as they will exist at
run-time)?

  ***

Comments?  Input?
```

#### ↳ Re: IBM and COBOL File Status = 39

- **From:** "Ron" <NoNoSpam@StopSpam.org>
- **Date:** 2003-11-10T18:12:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6idnaZcJdvwtC2iXTWQlg@giganews.com>`
- **References:** `<LoVrb.8715$6c3.1487@newsread1.news.pas.earthlink.net>`

```
NO! Frankly, I think they should leave it as is. The
file definitions in the program should conform to the
characteristics of the file. Allowing it to do otherwise
contributes to sloppy programming, imo.

I'm working now in a shop that still extensively uses
OS/VS Cobol (I know, I know). A lot of files don't
match the programs and they have all kinds of screwed up DCB's.
People don't bother to do it "right" because the compiler
doesn't make them. Then they wonder why there's problems
processing files between different programs. If they
got a few 39's and had to really learn how it's supposed
to be, there would ultimately be a lot less problems.
Soon or later, they're going to have to fix this and it will be
painful in the short term. But doing it right is always the
best thing. Allowing file inconsistencies to pass will do more
harm than good.

Ron


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:LoVrb.8715$6c3.1487@newsread1.news.pas.earthlink.net...
> To IBM-MAIN & comp.lang.cobol (and CC to others)
>
…[42 more quoted lines elided]…
>
```

#### ↳ Re: IBM and COBOL File Status = 39

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2003-11-11T18:16:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031111.18164660@04307839700-0001.dialin.t-online>`
- **References:** `<LoVrb.8715$6c3.1487@newsread1.news.pas.earthlink.net>`

```
Hello

(big letters are code-examples - thank you)

some time ago i wrote in this group about this s... FILESTAT 
implementation!

i.e. RECORDING MODE V RECORD CONTAINS 80 THRU 200 BYTES

the largest record in all files is 40 bytes - the largest!

all DD are DISP=SHR, and DSN=xx.aa.bb

//FILE DD LRECL=500 --> ABEND

//FILE DD DCB=LRECL=204 --> OK

//FILE DD DCB=LRECL=80 --> ABEND

if i use this:

//FILE DD DCB=LRECL=204 --> thist is an empty entry
//     DD DCB=LRECL=80 --> concat, now all work fine
//     DD DCB=LRECL=500 --> concat, now all work fine

on VB-File i want to use a technique to grow a maximal record length 
dynamicly and share it with assembler and other utilities....

VB-File in MVS Environment becomes guilty when the largest record is 
within the recordsize range

VB-Files in COBOL only becomes guilty when the attributes (DCB) 
matches the FD-Entry!!!! :-((

I want to use the following arrangement:

FD FILE RECORDING MODE V RECORD CONTAINS 1 THRU 23994 BYTES.
01 record1 PIC X(100)
01 record2 pic X(200)
01 Recordmax PIC X(23994)

READ FILE INTO working-area-32000-bytes
EVALUATE RECORD-TYP
WHEN ¸A' MOVE working-area to RECORD-A-AREA
WHEN ¸B' MOVE working-area to RECORD-B-AREA
...... 

with all of the //FILE DD DCB=80,204,500 and anything else the largest 
record must be only in the range of 1 to 23994 bytes (DCB 
minimum=1,maximum=32760)

on some applications i can have thousends of programms which can 
access the same file. I can change the record-size on the DCB 
statement without compile and change all of them.

I want to have this fine file handling of COBOL-II back!

Sorry about my english

have a nice day

Andreas Lerch
```

##### ↳ ↳ Re: IBM and COBOL File Status = 39

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-12T00:07:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tResb.9862$6c3.4736@newsread1.news.pas.earthlink.net>`
- **References:** `<LoVrb.8715$6c3.1487@newsread1.news.pas.earthlink.net> <20031111.18164660@04307839700-0001.dialin.t-online>`

```
See my separate note on "file status 39".  Having said that, a couple of things
to be aware of:

A) VS COBOL II *only* allowed mis-matches between FD and (JCL) DCB when the
(discouraged) CMPR2 compiler option was used.

B) If you omit the RECORDING MODE clause and use:
   Record Varying in size from N1 to N2 depending on WS-Item

(where N2 is the REAL maximum size of the VB file) you will be able to use the
value in WS-Item to find out how big a record you have read after each READ.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
