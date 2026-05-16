[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ISO Utility to convert FDs to layout format

_12 messages · 10 participants · 1998-11_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### ISO Utility to convert FDs to layout format

- **From:** jamesj@usit.net (James Jones)
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365438c7.1644174@news.usit.net>`

```
For the past 2 days I've been converting COBOL file descriptions to
record layout, ie:

FIELD NAME                 STARTS   LENGTH      FORMAT

CUSTOMER NUMBER           1             6           ALPHA
CUSTOMER NAME                7           25           ALPHA
CUSTOMER SLSMN            32             3           NUMERIC
etc.etc.etc. until the end of time....

To say this is boring work makes light of Y2K remediation.
Has anyone written a utility to perform this type of operation?  If
not I just may write one myself.

Thanks,
James Jones.
```

#### ↳ Re: ISO Utility to convert FDs to layout format

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365473D4.C04240EB@ASPMnetdoor.com>`
- **References:** `<365438c7.1644174@news.usit.net>`

```
I wrote a program to produce that type of information on COBOL FD's or
WS areas, but it's in C.  This might not be the right usegroup for it.

James Jones wrote:

> For the past 2 days I've been converting COBOL file descriptions to
> record layout, ie:
…[10 more quoted lines elided]…
> not I just may write one myself.
```

#### ↳ Re: ISO Utility to convert FDs to layout format

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3654BEEC.CE31FFBD@siber.com>`
- **References:** `<365438c7.1644174@news.usit.net>`

```
James Jones wrote:
> 
> For the past 2 days I've been converting COBOL file descriptions to
…[6 more quoted lines elided]…
> CUSTOMER SLSMN            32             3           NUMERIC

We have a tool called CobolReporter that produces exactly what you need.
It even produces more than you need:
- Offset from the start of parent DD level
- Offset from the start of 01 DD level
- Offset from the start of WS/FILE/LINKAGE section
- Length of the data item

The tool is not officially released yet
(will be released in 1-2 weeks), but I can send you an
evaluation copy today. The price for the tool is $495.

Please note that we correctly compute lengths and offsets
in presence of REDEFINES and RENAMES clauses.

You also can specify your own memory model
(how many bytes you have in your words, alignment rules, etc.),
so the tool can compule lengths&offsets for any CPU architecture.

Sample of the CobolReporter output is enclosed.

The tool is built using CobolTransformer, and by the way,
you have all this data on the Program Tree produced by CobolTransformer
so if you decide to automate the documenting/migration process
you can simply license CobolTransformer and have it do this work for you.

http://www.siber.com/sct/


Best regards,
Vadim Maslov

-------------------------------------------------------

=== test-sct offsets cbl-report xxx/sam.cob -lang=ms -copylib-dir=xxx ===
+cbl-report xxx/sam.cob -lang=ms -copylib-dir=xxx -mem-offsets
Lines:         1919
LinesOfCode:   1718
Tokens:        7508
TreeNodes:    14456

PROGRAM-ID:         SAM650

Sections:        15
Paragraphs:      65
Sentences:      429
Statements:    1585

File IO:         99
ADIS Screen:    186

CALL:             1 'sam200'            
CALL:             1 'EXIST'             
CALL:             2 'syscmd'            
CALL:             2 'REMOVE'            


Records for FILE: REMITTANCE-ADVICES  (global/offset-01/offset-local/length)

(  0/  0/  0/ 80) 01  R1-DETAIL-LINE
(  0/  0/  0/ 10)     03  R1-DATE PIC X(10)
( 10/ 10/ 10/ 11)     03  R1-TRAN-DESC PIC X(10)B
( 21/ 21/ 21/  9)     03  R1-REFERENCE PIC X(9)
( 30/ 30/ 30/ 10)     03  R1-DB-CR PIC Z(6).ZZ-
( 40/ 40/ 40/ 12)     03  R1-BALANCE PIC Z(8).ZZ-
( 52/ 52/ 52/  1)     03  FILLER PIC X
( 53/ 53/ 53/ 27)     03  R1-RM-ALTERNATE-DESCRIP
( 53/ 53/  0/  7)       05  R1-RM-REFERENCE PIC X(7)
( 60/ 60/  7/ 10)       05  R1-RM-DB-CR PIC Z(6).ZZ-
( 70/ 70/ 17/ 10)       05  R1-RM-BALANCE PIC Z(6).ZZ-

(  0/  0/  0/ 78) 01  R2-AGED-LINE
(  0/  0/  0/ 11)     03  R2-3
(  0/  0/  0/ 11)       05  R2-3MONTH PIC Z(7).ZZ-
( 11/ 11/ 11/  3)     03  FILLER PIC XXX
( 14/ 14/ 14/ 11)     03  R2-2MONTH PIC Z(7).ZZ-
( 25/ 25/ 25/  2)     03  FILLER PIC XX
( 27/ 27/ 27/ 11)     03  R2-1
( 27/ 27/  0/ 11)       05  R2-1MONTH PIC Z(7).ZZ-
( 38/ 38/ 38/ 12)     03  R2-CURRENT PIC Z(7)9.99-
( 50/ 50/ 50/  6)     03  FILLER PIC X(6)
( 56/ 56/ 56/ 11)     03  R2-RM PIC X(11)
( 67/ 67/ 67/ 11)     03  R2-RM-BALANCE PIC Z(6)9.99-

(  0/  0/  0/ 80) 01  R3-ADDRESS-LINE
(  0/  0/  0/ 11)     03  FILLER PIC X(11)
( 11/ 11/ 11/ 43)     03  R3-NAME
( 11/ 11/  0/ 24)       05  FILLER PIC X(24)
( 35/ 35/ 24/  6)       05  R3-POSTCODE PIC Z(6)
( 41/ 41/ 30/  8)       05  R3-DATE PIC Z9/99/99
( 49/ 49/ 38/  5)       05  FILLER PIC X(5)
( 11/ 11/ 11/ 43)     03  R3-PG-DT REDEFINES R3-NAME
( 11/ 11/  0/ 29)       05  FILLER PIC X(29)
( 40/ 40/ 29/  8)       05  R3-PAGE-1 PIC X(8)
( 48/ 48/ 37/  2)       05  R3-PAGE-NO-1 PIC Z9
( 50/ 50/ 39/  4)       05  FILLER PIC X(4)
( 54/ 54/ 54/ 26)     03  R3-CREDITOR-NAME
( 54/ 54/  0/ 20)       05  FILLER PIC X(20)
( 74/ 74/ 20/  6)       05  R3-DEB-PC PIC Z(6)
( 54/ 54/ 54/ 26)     03  R3-REM-PG REDEFINES R3-CREDITOR-NAME
( 54/ 54/  0/ 16)       05  FILLER PIC X(16)
( 70/ 70/ 16/  8)       05  R3-PAGE-2 PIC X(8)
( 78/ 78/ 24/  2)       05  R3-PAGE-NO-2 PIC Z9

(  0/  0/  0/ 80) 01  R4-HEAD-LINE
(  0/  0/  0/  9)     03  FILLER PIC X(9)
(  9/  9/  9/ 30)     03  R4-COMPANY-NAME PIC X(30)
( 39/ 39/ 39/ 24)     03  FILLER PIC X(24)
( 63/ 63/ 63/ 17)     03  R4-DT-ACC
( 63/ 63/  0/  2)       05  FILLER PIC XX
( 65/ 65/  2/  5)       05  R4-DATE-LIT PIC X(5)
( 70/ 70/  7/  8)       05  R4-DATE PIC X(8)
( 78/ 78/ 15/  2)       05  FILLER PIC XX
( 63/ 63/ 63/ 17)     03  R4-ACC-DT REDEFINES R4-DT-ACC
( 63/ 63/  0/ 11)       05  R4-ACC-LIT PIC X(11)
( 74/ 74/ 11/  6)       05  R4-CUSTOMER-NO PIC X(6)

... (complete listing is too long, cut here) ...
```

#### ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EX452.49$NF5.250905@storm.twcol.com>`
- **References:** `<365438c7.1644174@news.usit.net>`

```

>FIELD NAME                 STARTS   LENGTH      FORMAT
>
…[7 more quoted lines elided]…
>not I just may write one myself.


I don't mean to sound like an add for Compuware, but FileAid does this exact
thing. You would extract the FD or 01 to a copybook and use the
PRINT->RECORD LAYOUT option. This can be done in batch and run against many
different copybooks.

Since you are probably asking this because you don't have FileAid, I can
suggest a techique I partially developed in the past. Extract all FD's to
copybooks. Set up a COBOL compile with
IN-STREAM COBOL in the compile instead of referring to a PDS member. The
COBOL code contained would contain a skeleton which does nothing, but must
contain a WORKING-STORAGE section. Within the WORKING-STORAGE SECTION put
the copybook you wish to get a cross reference for IN-STREAM:

......
WORKING-STORAGE SECTION.
/*
//         DD DSN=USERID.COPYLIB(COPYMEM),DISP=SHR
//         DD *
...... rest of COBOL skeleton

or even:
//SYSIN    DD DSN=USERID.COPYLIB(TOP),DISP=SHR         TOP SECTION OF COBOL
SKELETON
//         DD DSN=USERID.COPYLIB(COPYMEM),DISP=SHR     COPYBOOK OF FD
//         DD DSN=USERID.COPYLIB(BOT),DISP=SHR         BOTTOM SECTION OF
COBOL SKELETON

Rout the COBOL listing to a DSN. Feed LISTING into a program, such as REXX
or COBOL whatever is easier for you. Use the REXX/COBOL program to parse out
each fields offsets near the right margin. Keep a running total of the field
lengths to generate your report.


Its not the easiest way, but it works, and of course it is free.

You could possibly even write an EDIT MACRO to do something similar in an
EDIT session and insert your offset report into the source code as a comment
or INFOLINE.

Hope some of this helps.
```

##### ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981120182527.25359.00000310@ngol01.aol.com>`
- **References:** `<EX452.49$NF5.250905@storm.twcol.com>`

```

In article <EX452.49$NF5.250905@storm.twcol.com>, "Jeff" <a@a.com> writes:

>
>Rout the COBOL listing to a DSN. Feed LISTING into a program, such as REXX
…[13 more quoted lines elided]…
>

This sounds familiar to what we have done in the past.  Except that the sysout
is downloaded and brought into EXCEL where one of our more industrious PC types
setup up something to convert the binary offsets to decimal start positions.
```

###### ↳ ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgo52.9$fz6.53476@storm.twcol.com>`
- **References:** `<EX452.49$NF5.250905@storm.twcol.com> <19981120182527.25359.00000310@ngol01.aol.com>`

```

>This sounds familiar to what we have done in the past.  Except that the
sysout
>is downloaded and brought into EXCEL where one of our more industrious PC
types
>setup up something to convert the binary offsets to decimal start
positions.


I used REXX, but before I finished I moved to a site with FileAid and I used
it instead.
```

#### ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3654445f.0@news1.ibm.net>`
- **References:** `<365438c7.1644174@news.usit.net>`

```

James Jones wrote in message <365438c7.1644174@news.usit.net>...
>For the past 2 days I've been converting COBOL file descriptions to
>record layout, ie:
…[10 more quoted lines elided]…
>not I just may write one myself.


There are such tools (I have one), but why would you need one?
What does the conversion buy over the Cobol FD?
```

##### ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981119112957.21869.00000069@ng-fq1.aol.com>`
- **References:** `<3654445f.0@news1.ibm.net>`

```
>There are such tools (I have one), but why would you need one?
>What does the conversion buy over the Cobol FD?
>
Leif, 

We're buying a package of non-COBOL software that will
use some of my data files as input on a regular basis.  I have
to describe the files for them.  We're buying this package 
because I'm too busy cleaning up Y2K to write anything new.

The programmers I'm dealing with can't gork a COBOL FD.
Hence the record layout exercise.

Is the tool you have for sale?

Thanks,
James Jones.
(AKA jamesj@usit.net)
```

###### ↳ ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36544f8d.0@news1.ibm.net>`
- **References:** `<3654445f.0@news1.ibm.net> <19981119112957.21869.00000069@ng-fq1.aol.com>`

```

JCJ0347 wrote in message <19981119112957.21869.00000069@ng-fq1.aol.com>...
>>There are such tools (I have one), but why would you need one?
>>What does the conversion buy over the Cobol FD?
…[11 more quoted lines elided]…
>Is the tool you have for sale?


Yes it is.
The tool actually produces an SQL create table statement
from a Cobol copy book. Can be easily configured to
produce the output in any format you wish.
```

###### ↳ ↳ ↳ Re: ISO Utility to convert FDs to layout format

_(reply depth: 4)_

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365542A0.10AE13CF@infonet.com.py>`
- **References:** `<3654445f.0@news1.ibm.net> <19981119112957.21869.00000069@ng-fq1.aol.com> <36544f8d.0@news1.ibm.net>`

```


Leif Svalgaard wrote:

> The tool actually produces an SQL create table statement
> from a Cobol copy book. Can be easily configured to
> produce the output in any format you wish.

I went the other way around. Wrote a program to turn a SQL-like table
definition into an FD, along with SELECT and I/O routines. It even has groups,
redefines, conditionals and domains. But it is pretty home brewn. Don't think
I would like to impose it on any one. And it only works on Unix (uses lex and
yacc).

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Scott Williamson" <scott.williamson@east-ayrshire.gov.uk>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4si137.1pd.ln@gate.east-ayrshire.gov.uk>`
- **References:** `<3654445f.0@news1.ibm.net> <19981119112957.21869.00000069@ng-fq1.aol.com>`

```

JCJ0347 wrote in message <19981119112957.21869.00000069@ng-fq1.aol.com>...
>>There are such tools (I have one), but why would you need one?
>>What does the conversion buy over the Cobol FD?
…[12 more quoted lines elided]…
>

I've got some COBOL code that should do the job - it was originally written
to create data dictionary entries from FDs, but it also outputs a report in
a format similar to your requirements.
If you're interested let me know and I'll dig out the code.  I've also got
some half-written C code to do the same thing but it needs a lot of work.

Scott Williamson
scott.williamson@east-ayrshire.gov.uk
or syw@cdvdc.demon.co.uk
```

##### ↳ ↳ Re: ISO Utility to convert FDs to layout format

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OxJWwMFF#GA.228@upnetnews05>`
- **References:** `<365438c7.1644174@news.usit.net> <3654445f.0@news1.ibm.net>`

```

Leif Svalgaard wrote in message <3654445f.0@news1.ibm.net>...
>
>James Jones wrote in message <365438c7.1644174@news.usit.net>...
…[17 more quoted lines elided]…
>


Data definition documentation for non-programmers?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
