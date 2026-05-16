[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deleted records

_45 messages · 10 participants · 1999-03_

---

### Deleted records

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bpkes$pte$1@news.imp.ch>`

```
hello

I am using RM Cobol since 1988 and I am currently using RM Cobol for Windows
6.51
Since 89 RM cobol (Cobol 5.xx and Cobol 6.xx and Cobol 6.51) DID and DOES
NOT RECOVER
space once occupied by deleted records WITH ME automaticly. It seems, that I
did not read the manuals
correctly as Tim mentions IT DOES.
Therefore I would be very thankful for a tip where to find the info.
Example File 10'000 records size 2.732 MB, I delete 3000 records new (old)
size 2.732 MB
therefore
I open the file with the deleted records, open a new physical file (call it
new) and move
record 1 from old file to record 1 of new and so on.
That's the way I do it with dozens of files size more than 10 years and now
I have to
read from TIM, RMCobol did this always automaticly!

Please inform me, how RM cobol did (or does it)! Imagine all the time I
spent for writing these
simple but time consuming copy routines, all for nothing....

I use all four maximum YES levels (physical writes and so on) on my RM
Datafiles in a Network.

Thank you

Although all that work I still use the ISAM File System from RM. After
testing SQL 6.5 from MS (consulting the prices for the SQL SERVER for 50)
users and all the bywork I decided that the flat DATABASE for RM is not ONLY
faster and surer, easier to manage, but also a little bit cheaper!
Now I am going to buy some flowers for my wife, I take the bike, not a
lorry!
```

#### ↳ Re: Deleted records

- **From:** "BAC" <bac@biosys.net>
- **Date:** 1999-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bpokh$sm7$1@mail.dstsystems.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch>`

```
It is such a relief to see a fellow RMCobol fan. I fully agree that a
properly designed system in RM can beat all this so called superior
database.

I had personally designed larger applications ranging from financials,
banking...etc.,
I still feel that the conventional flat database of RM is so versatile,
functional, practical.
Maybe if the company had known how to market it, like say call the product
itself as cbl++ (Thank God MS didn't know I was here !), it would had a
better market.

BTW, how many people are still left as our breed ?

-BAC-
```

#### ↳ Re: Deleted records

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e09983.251193672@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch>`

```
On Fri, 5 Mar 1999 23:08:02 +0100, "John Casagrande"
<john@casagrande.ch> wrote:

>hello
>
…[21 more quoted lines elided]…
>

I think you misunderstand.

With RM and Realia and Fujitsu - if you have a file of say... 1000
records, that takes up... oh, say...100000 bytes. If you delete one
record, the file still takes up 100000 bytes.  BUT-- if you THEN
insert a record, it will STILL take up 100000 bytes - the space that
was used by the deleted record is recovered and used again.


To contrast, the same file with MicroFocus COBOL:  1000 records,
100000 bytes, delete a record - file size 100000 bytes - insert a
record file is 1000100 bytes - the space used by the deleted record is
never reclaimed or reused.

Your reorganization was not a waste.  If records are deleted and
others not inserted to take their place, you are recovering lost
space.  Also, it can help speed performance to reorganize the data
file.
```

##### ↳ ↳ Re: Deleted records

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bsc8c$lj9$1@news.imp.ch>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net>`

```
Hello Thane

thank you for your information. I was surprised to hear that MF Cobol does
not reuse the space once
used by a deleted record. I did understand before the mechanism RM uses. I
just do not understand
why there is no utility from the producer of the Cobol to reorganise a file.
Before 1988 I used to work with Burroughs Cobol and I remember they had a
utility called "SQUASH"
to "delete" deleted records from a file. In these times space on hard disks
was more expensive then today and maybe therefore people did think about how
to solve space.
I imagine it would be possible to make a utility to "reorganise" such blown
up files and help us programers to avoid such routine work. In an indexed
file there is in minimum the information about the keys.

Or is there not enough information in the file to reconstruct the
content of the file?
Have a nice time
john@casagrande.ch, lucerne switzerla


Thane Hubbell schrieb in Nachricht <36e09983.251193672@news1.ibm.net>...
>On Fri, 5 Mar 1999 23:08:02 +0100, "John Casagrande"


>I think you misunderstand.
>
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bshph$e9o$1@news-2.news.gte.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch>`

```
Don't tell me that was "CMS COBOL", where "squash" was the utility command,
"SQ."

(Why not tell me? It will make me count birthdays).

MCM

John Casagrande wrote in message <7bsc8c$lj9$1@news.imp.ch>...
>Hello Thane
>Before 1988 I used to work with Burroughs Cobol and I remember they had a
>utility called "SQUASH" to "delete" deleted records from a file...
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7btlia$406$1@news.imp.ch>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <7bshph$e9o$1@news-2.news.gte.net>`

```
hy mattias
It "WAS" CMS Cobol and I remember that a compilation for a 8000 line file
took about 30 minutes.
We lived in the same house (like the computer) and my wife loved these so
called "compiling pauses"
because this was a opportunity for us to drink some tea and to do some other
things....
When I changed to a NCR PC8 System (286 8 MHZ) and compiled the same source
with some changes
and the source became 9000 lines long, the whole thing took about 3 minutes.
I first thought, something
went wrong. Then my wife became sad. What do you do in 3 minutes?
Today the same source has exploded to 20000 lines and the compiling goes 3
seconds on a Pentium 400.
And my wife definitely does not like the name Pentium anymore but she brings
me the tea to the computer!

Michael Mattias schrieb in Nachricht <7bshph$e9o$1@news-2.news.gte.net>...
>Don't tell me that was "CMS COBOL", where "squash" was the utility command,
>"SQ."
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bv4fp$hir$2@news-2.news.gte.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <7bshph$e9o$1@news-2.news.gte.net> <7btlia$406$1@news.imp.ch>`

```
Hmm, were you on a B-80/B-800? B90-B900? I was GM of a CMS VAR, and we had
about 500 COBOL programs in our system, and I remember setting up compile
jobs which would run all day and all night. (This was before I programmed
myself; I recall that compiling seemed "awfully fast" when it only took ten
minutes for a 500-line program).

Also, I just remembered: "SQ" compressed the disk (i.e., defragment); it was
"FS" which performed the (F)ile (S)quash.

MCM

John Casagrande wrote in message <7btlia$406$1@news.imp.ch>...
>hy mattias
>It "WAS" CMS Cobol and I remember that a compilation for a 8000 line file
>took about 30 minutes.
> [Stuff about SQUASH]
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 6)_

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c3vpj$82j$1@news.imp.ch>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <7bshph$e9o$1@news-2.news.gte.net> <7btlia$406$1@news.imp.ch> <7bv4fp$hir$2@news-2.news.gte.net>`

```

Michael Mattias schrieb in Nachricht <7bv4fp$hir$2@news-2.news.gte.net>...
>Hmm, were you on a B-80/B-800? B90-B900? I was GM of a CMS VAR, and we had
>about 500 COBOL programs in our system, and I remember setting up compile
…[4 more quoted lines elided]…
>Also, I just remembered: "SQ" compressed the disk (i.e., defragment); it
was
>"FS" which performed the (F)ile (S)quash.


You are very right it was "FS". I had first a B91 and then a B96.
We decided to change to NCR PC 8 because the price of 1 PC System was about
6000 US Dollars
but we paid about 10'000 Dollars a year for servicing the B96!
One Video screen was costing US $ 5000 but for that it had green characters
and the PC System
"only" had a colour screen. Once I ordered an extra long cable for a 230cps
printer of 8 meters and
Burroughs asked me for 500 Dollars! I have all the old invoices in a book
and once I will write a book
about "Good (expensive) old times.
By the way, I started programming because we also ordered programs for the
machine. And when I saw that the programer just started learning programing
I thought I better start too! And after 3 months I did not need the
programer anymore (but a lot more time of the days)!
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e1e349.335628764@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch>`

```
On Sun, 7 Mar 1999 00:06:26 +0100, "John Casagrande"
<john@casagrande.ch> wrote:

>Hello Thane
>
…[12 more quoted lines elided]…
>file there is in minimum the information about the keys.

Not sure what it is called in RM - but such utilities exist for each
compiler I have used.  With CA-Realia it's REALCOPY, with Fujitsu it's
the File Utility, with MicroFocus it's REBUILD.  In the early days of
Realia we did it ourselves - but past early version 2 there was a
utility.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bsros$gpl@dfw-ixnews11.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <36e1e349.335628764@news1.ibm.net>`

```
Thane Hubbell wrote in message <36e1e349.335628764@news1.ibm.net>...
>On Sun, 7 Mar 1999 00:06:26 +0100, "John Casagrande"
><john@casagrande.ch> wrote:
…[5 more quoted lines elided]…
>>used by a deleted record.
   <much snippage>

>Not sure what it is called in RM - but such utilities exist for each
>compiler I have used.  With CA-Realia it's REALCOPY, with Fujitsu it's
>the File Utility, with MicroFocus it's REBUILD.  In the early days of
>Realia we did it ourselves - but past early version 2 there was a
>utility.


Thane,
  Speaking of Micro Focus "REBUILD" - doesn't that recover the space that
doesn't get used by added new records?  I guess I always thought of this as
the way to "go" in an MF environment.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e27ebf.375432491@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <36e1e349.335628764@news1.ibm.net> <7bsros$gpl@dfw-ixnews11.ix.netcom.com>`

```
On Sat, 6 Mar 1999 21:28:15 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:


>Thane,
>  Speaking of Micro Focus "REBUILD" - doesn't that recover the space that
>doesn't get used by added new records?  I guess I always thought of this as
>the way to "go" in an MF environment.

Well, that's what I was trying to say.  Each COBOL has a utility to
recover lost space, and compact files.... with MicroFocus it is
Rebuild.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bu44s$678$1@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <36e1e349.335628764@news1.ibm.net> <7bsros$gpl@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote in message <7bsros$gpl@dfw-ixnews11.ix.netcom.com>...
[...]
>  Speaking of Micro Focus "REBUILD" - doesn't that recover the space that
>doesn't get used by added new records?  I guess I always thought of this as
>the way to "go" in an MF environment.
>
REBUILD is good choice for that purpose but it is not necessarily
the best choice.

The system I maintain has a history file that is purged every year.
I could delete the archived records from the indexed file, then run
REBUILD to recover the space. Instead, I split the data into a
sequential archive and a new indexed file. When finished, I delete
the old file and rename the new. Should the purge process fail, the
original indexed file is unchanged and the process can be rerun
without restoring files.
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e31cab.415866784@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <36e1e349.335628764@news1.ibm.net> <7bsros$gpl@dfw-ixnews11.ix.netcom.com> <7bu44s$678$1@server.cntfl.com>`

```
On Sun, 7 Mar 1999 09:55:32 -0500, "Rick Smith"
<ricksmith@aiservices.com> wrote:


>The system I maintain has a history file that is purged every year.
>I could delete the archived records from the indexed file, then run
…[4 more quoted lines elided]…
>without restoring files.

It may not be obvious - but running REBUILD without specifying  a
SEPARATE output file does not recover any space.

ie:  REBUILD INDEXED.FIL 

recreates the index portion, which is a separate file.

REBUILD INDEXED.FIL,INDEXED.NEW - creates a new file, recovering
space.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bvi87$9pj$1@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bsc8c$lj9$1@news.imp.ch> <36e1e349.335628764@news1.ibm.net> <7bsros$gpl@dfw-ixnews11.ix.netcom.com> <7bu44s$678$1@server.cntfl.com> <36e31cab.415866784@news1.ibm.net>`

```

Thane Hubbell wrote in message <36e31cab.415866784@news1.ibm.net>...
>On Sun, 7 Mar 1999 09:55:32 -0500, "Rick Smith"
><ricksmith@aiservices.com> wrote:
…[5 more quoted lines elided]…
>SEPARATE output file does not recover any space.

Well, yes. I was thinking in terms of using REBUILD to reorganize
the file, which does recover the space.

>ie:  REBUILD INDEXED.FIL
>
…[3 more quoted lines elided]…
>space.

Which will fail due to a conflict over INDEXED.IDX ! The name of
the indexed file for both INDEXED.FIL and INDEXED.NEW.

REBUILD OLD.DAT, NEW.DAT will work.
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

##### ↳ ↳ Re: Deleted records

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bsca7$ljc$1@news.imp.ch>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net>`

```
Hello Thane

thank you for your information. I was surprised to hear that MF Cobol does
not reuse the space once
used by a deleted record. I did understand before the mechanism RM uses. I
just do not understand
why there is no utility from the producer of the Cobol to reorganise a file.
Before 1988 I used to work with Burroughs Cobol and I remember they had a
utility called "SQUASH"
to "delete" deleted records from a file. In these times space on hard disks
was more expensive then today and maybe therefore people did think about how
to solve space.
I imagine it would be possible to make a utility to "reorganise" such blown
up files and help us programers to avoid such routine work. In an indexed
file there is in minimum the information about the keys.

Or is there not enough information in the file to reconstruct the
content of the file?
Have a nice time
john@casagrande.ch, lucerne switzerla
```

##### ↳ ↳ Re: Deleted records

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bu451$678$2@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net>`

```

Thane Hubbell wrote in message <36e09983.251193672@news1.ibm.net>...
[...]
>
>To contrast, the same file with MicroFocus COBOL:  1000 records,
…[3 more quoted lines elided]…
>
I can say that statement is not true of any Micro Focus product
I have used during the past 15 years.
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e31d19.415976813@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bu451$678$2@server.cntfl.com>`

```
On Sun, 7 Mar 1999 09:56:33 -0500, "Rick Smith"
<ricksmith@aiservices.com> wrote:

>
>Thane Hubbell wrote in message <36e09983.251193672@news1.ibm.net>...
…[8 more quoted lines elided]…
>I have used during the past 15 years.

Really?  I'm suprised.  I thought it was given that deleted records
are only marked logically deleted with MicroFocus COBOL and the space
used by them is never reused.  Is this incorrect?  I'm certain I
gained this knowledge from the MicroFocus manuals - but it could be
the "Level II" indexed files were this way, and the "newer" ones are
not, and I did not renew my information with the format change.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bvh5e$85t$1@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bu451$678$2@server.cntfl.com> <36e31d19.415976813@news1.ibm.net>`

```

Thane Hubbell wrote in message <36e31d19.415976813@news1.ibm.net>...
>On Sun, 7 Mar 1999 09:56:33 -0500, "Rick Smith"
><ricksmith@aiservices.com> wrote:
…[18 more quoted lines elided]…
>
Your statement appears to be incorrect with respect to certain
Micro Focus products that have been produced since 1985.

The test program, below, was run using a Level II product. The
program creates an indexed file of 1000 records of 100 bytes
each. The program then deletes the first 500 records then adds
500 more records. I animated the program by using Perform Step
in the initial paragraph. After each PERFORM statement, I checked
the size of the data file. In each case, it was 102,000 bytes. (The
same program using MF WB 3.2 had a file size of 104,128 bytes
after each step.)

This is not the earliest MF product I have used. It is the earliest
(oldest) one that I have available. I cannot dispute whether older
Level II products reused deleted records; but, I can confirm that
this product does. I can also confirm that later products through
WB 3.2 also reuse deleted records. This means that since 1985
Micro Focus has had products that reuse deleted records.

The term "logically delete" is part of the COBOL standard and
appears in all language reference manuals. I searched through
older MF manuals and could find no information about reusing
deleted records. It is, as if, "it goes without saying." I didn't check
them all since I have about 40 or 50 MF manuals. The
MF WB 3.2 System Reference Manual has this comment.

"(Free space consists of the spaces in the data file occupied by
  deleted records. Information about these areas is normally
  retained, and the areas reused for new records as appropriate.)"

Although this comment is in the section on Rebuild, it is the
only comment that I found that actually says that space from
deleted records will be reused. The "as appropriate" could apply
to variable length records; that is, it cannot reuse space that is
too small to hold the record.

-------- Test program, ANSI 74 for MF Professional Cobol 1.1
       IDENTIFICATION DIVISION.
       PROGRAM-ID. IDX-TEST.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT IDX-FILE
                ASSIGN TO "IDX-FILE.DAT"
                ORGANIZATION IS INDEXED
                ACCESS IS DYNAMIC
                RECORD KEY IS IDX-KEY
                FILE STATUS IS IDX-STAT.
       DATA DIVISION.
       FILE SECTION.
       FD  IDX-FILE.
       01  IDX-RECORD.
            05  IDX-KEY    PIC 9(6).
            05  IDX-DATA    PIC X(94).
       WORKING-STORAGE SECTION.
       01  IDX-STAT    PIC XX.
       01  RECORD-SEQUENCE     PIC 9(6).
       PROCEDURE DIVISION.
            OPEN OUTPUT IDX-FILE
            CLOSE IDX-FILE
            PERFORM CREATE-INITIAL-RECORDS
            PERFORM DELETE-SOME-RECORDS
            PERFORM ADD-MORE-RECORDS
            STOP RUN.

       CREATE-INITIAL-RECORDS.
            OPEN I-O IDX-FILE.
            PERFORM ADD-A-RECORD
                VARYING RECORD-SEQUENCE FROM 1 BY 1
                UNTIL RECORD-SEQUENCE > 1000.
            CLOSE IDX-FILE.

       DELETE-SOME-RECORDS.
            OPEN I-O IDX-FILE.
            PERFORM DELETE-A-RECORD
                VARYING RECORD-SEQUENCE FROM 1 BY 1
                UNTIL RECORD-SEQUENCE > 500.
            CLOSE IDX-FILE.

       ADD-MORE-RECORDS.
            OPEN I-O IDX-FILE.
            PERFORM ADD-A-RECORD
                VARYING RECORD-SEQUENCE FROM 1001 BY 1
                UNTIL RECORD-SEQUENCE > 1500.
            CLOSE IDX-FILE.

       ADD-A-RECORD.
            MOVE RECORD-SEQUENCE TO IDX-KEY.
            MOVE SPACES TO IDX-DATA.
            WRITE IDX-RECORD
              INVALID KEY
                NEXT SENTENCE.

       DELETE-A-RECORD.
            MOVE RECORD-SEQUENCE TO IDX-KEY.
            READ IDX-FILE
              INVALID KEY
                NEXT SENTENCE.
            DELETE IDX-FILE
              INVALID KEY
                NEXT SENTENCE.
--------
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c0atd$t6v@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bu451$678$2@server.cntfl.com> <36e31d19.415976813@news1.ibm.net> <7bvh5e$85t$1@server.cntfl.com>`

```
FYI,
  My "usually reliable source" at MERANT sent me the following,

"Deleted records are certainly reused in MF indexed files.  They may not be
reused immediately, but they are added to a free space list and made
available to future updates."

I think this corresponds with Rick's empirical evidence.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e3d3e1.462488909@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bu451$678$2@server.cntfl.com> <36e31d19.415976813@news1.ibm.net> <7bvh5e$85t$1@server.cntfl.com>`

```
On Sun, 7 Mar 1999 22:42:48 -0500, "Rick Smith"
<ricksmith@aiservices.com> wrote:

...snip snip snip...

>The term "logically delete" is part of the COBOL standard and
>appears in all language reference manuals. I searched through
…[8 more quoted lines elided]…
>

Thanks for the correction and additional information.  Very
interesting.  My old "memories" have come back to haunt me as
erroneous "facts".   Thanks Rick, I really do appreciate the
correction.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c33s1$jh9$1@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <7bu451$678$2@server.cntfl.com> <36e31d19.415976813@news1.ibm.net> <7bvh5e$85t$1@server.cntfl.com> <36e3d3e1.462488909@news1.ibm.net>`

```

Thane Hubbell wrote in message <36e3d3e1.462488909@news1.ibm.net>...
[...]
>Thanks for the correction and additional information.  Very
>interesting.  My old "memories" have come back to haunt me as
>erroneous "facts".   Thanks Rick, I really do appreciate the
>correction.

It happens to the best of us. You might recall that I, recently,
had a faulty recollection concerning packed BCD and numeric
co-processors.
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

##### ↳ ↳ Re: Deleted records

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E4031C.9250754@NOSPAMhome.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net>`

```
> With RM and Realia and Fujitsu - if you have a file of say... 1000
> records, that takes up... oh, say...100000 bytes. If you delete one
…[12 more quoted lines elided]…
> file.

I'm a curious mainframe guy.
What kind of files are you talking about, indexed, relative?  
Why is it COBOL's function to organize file reclamation instead of the
OS's?
What happens when you have variable length records?  Do you need to do a
periodic defrag of the file?
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c19hi$905@sjx-ixn5.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com>`

```
Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...

>
>I'm a curious mainframe guy.
…[4 more quoted lines elided]…
>periodic defrag of the file?

When I first moved from IBM mainframe environments to PC COBOLs it came has
a HORRIBLE shock to me that the "operating system" did NOT have any type of
indexed files.  Each COBOL product on Workstations (OS/2, Windows, or UNIX)
needs to EITHER "invent their own" or use 3rd party products (such as
C-isam).  For an IBM mainframe, this is a "real eye opener" - especially if
you are interested in "portability".
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1a9o$s7a$1@news.igs.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com>`

```
Indexed files.  The reason that it is that the Cobol needs a facility
to rebuild an Isam file is because the file format is proprietary, and
the structure is part of the Cobol package.  I would expect that VSAM
probably has some sort of repair facility as well ... though since VSAM
is a one-vendor type of thing, whether it is part of Cobol or part of the
OS is just semantics.

Defrag is completely different.  The rebuild facility that is being
discussed deals with logical structure within the file only.  The physical
location of the file on the drive is solely within the OS, and a standard
defrag works on Cobol files.


Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...
>> With RM and Realia and Fujitsu - if you have a file of say... 1000
>> records, that takes up... oh, say...100000 bytes. If you delete one
…[19 more quoted lines elided]…
>periodic defrag of the file?
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E43777.CC252CCD@NOSPAMhome.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <7c1a9o$s7a$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Indexed files.  The reason that it is that the Cobol needs a facility
…[9 more quoted lines elided]…
> defrag works on Cobol files.

I wasn't thinking of a fragmented disk with different parts of a file in
different locations, I was thinking of a file with different sized null
records in it.  You don't care too much if the records are the same size
- when you add a record it will always fit where a deleted one was
removed (it may be at an inconvenient spot, but that's a different
problem).  But if you have variable length records, you could have a 50
byte hole and a 100 byte record.   Of course this can be fixed by
whatever maintenance is being done to move records around to make the
key search more efficient - maybe an unload-reload.

> Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...
> >> With RM and Realia and Fujitsu - if you have a file of say... 1000
…[20 more quoted lines elided]…
> >periodic defrag of the file?
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1oqa$7l8$1@news.igs.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <7c1a9o$s7a$1@news.igs.net> <36E43777.CC252CCD@NOSPAMhome.com>`

```

Howard Brazee wrote in message <36E43777.CC252CCD@NOSPAMhome.com>...

>I wasn't thinking of a fragmented disk with different parts of a file in
>different locations, I was thinking of a file with different sized null
>records in it.  You don't care too much if the records are the same

Yes, that makes sense.  I have not really faced this, as I tend to use
fixed length Isam records.
```

###### ↳ ↳ ↳ Re: Deleted records

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BMWE2.943$Tw3.148552@client.news.psi.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com>`

```
Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...
[snip]
>I'm a curious mainframe guy.
>What kind of files are you talking about, indexed, relative?

Indexed, in this discussion, relative having fallen into 'relative' disuse.

>Why is it COBOL's function to organize file reclamation instead of the
>OS's?

Simply because no OS (including MVS and VMS), save a very distinct few (two
of which I helped write), provides indexed IO at its very core.  The indexed
IO methods  of MVS and VMS are so entrenched that it seems as if their
indexed methods are part pf the OS.

So, for those nonproprietary platforms (Windows (r), UNIX (r)) where there
has been no single dominant indexed method (or, more to the point, COBOL
implementation) available, it falls to the vendors of COBOL systems to
provide some very essential services if COBOL is to be usable.  Exact
decimal arithmetic, for example, is not supported by the hardware or OS;
decimal arithmetic support must be supplied by the COBOL vendor.

And so it is with indexed, relative, AND COBOL STANDARD CONFORMING
sequential IO.

As far as I am aware, all the major COBOL vendors on these nonproprietary
platforms reclaim and reuse the physical space claimed by records that have
been logically deleted from their indexed file system implementations.


>What happens when you have variable length records?

Since most (all?) nonproprietary COBOL vendors provide on-the-fly
compression of the data in indexed records, virtually all data is stored in
structures that are well aware of variable length records.  The issue is not
variable length records, but intelligent reuse of space relinquished by
deleted records.

>Do you need to do a
>periodic defrag of the file?

Won't hurt.  Again, most (all?) nonproprietary COBOL vendors provide
rebuild/recovery utilities that help to reoptimize a file.

The original subject of this thread, RM/COBOL, has such a utility that will
shuffle much of the unused space to the 'physical' end-of-file and then
relinquish the unused space to the OS (assuming that the OS has a means of
taking back part of a file).

I hope that this has been helpful.

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1uvk$lpk@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net>`

```
Tom Morrison wrote in message ...
 <snip>
>
>Simply because no OS (including MVS and VMS), save a very distinct few (two
>of which I helped write), provides indexed IO at its very core.  The
indexed
>IO methods  of MVS and VMS are so entrenched that it seems as if their
>indexed methods are part pf the OS.
>

Actually, although you are correct about MVS, you are out-of-date when
speaking of OS/390 (MVS' replacement).  IBM has now "bundled" in many
components that used to be "tightly integrated" products.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e4a17f.515134992@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <7c1uvk$lpk@dfw-ixnews4.ix.netcom.com>`

```
On Mon, 8 Mar 1999 19:53:44 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:


>Actually, although you are correct about MVS, you are out-of-date when
>speaking of OS/390 (MVS' replacement).  IBM has now "bundled" in many
>components that used to be "tightly integrated" products.

Try to configure or run OS/390 without VSAM......I think it's pretty
tight.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 6)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wu9F2.1$QR3.11131@client.news.psi.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <7c1uvk$lpk@dfw-ixnews4.ix.netcom.com> <36e4a17f.515134992@news1.ibm.net>`

```
Thane Hubbell wrote in message <36e4a17f.515134992@news1.ibm.net>...
>On Mon, 8 Mar 1999 19:53:44 -0600, "William M. Klein"
><wmklein@nospam.netcom.com> wrote:
…[7 more quoted lines elided]…
>tight.

I knew when I wrote that that I risked some flamage.  But, then again, my
"mainframe" experience is a bit closer to Autocoder than OS/390!
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Yjfg1K6jU0Ym@Dwight_Miller.iix.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <7c1uvk$lpk@dfw-ixnews4.ix.netcom.com> <36e4a17f.515134992@news1.ibm.net> <wu9F2.1$QR3.11131@client.news.psi.net>`

```
On Tue, 9 Mar 1999 13:37:32, "Tom Morrison" <t.morrison@liant.com> 
wrote:

> Thane Hubbell wrote in message <36e4a17f.515134992@news1.ibm.net>...
> >On Mon, 8 Mar 1999 19:53:44 -0600, "William M. Klein"
…[13 more quoted lines elided]…
> 

My message was terser than I intended, no flame was supposed to leave 
the thrower!

-------------------------
Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 8)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c48na$igv$1@client2.news.psi.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <7c1uvk$lpk@dfw-ixnews4.ix.netcom.com> <36e4a17f.515134992@news1.ibm.net> <wu9F2.1$QR3.11131@client.news.psi.net> <Jl0PnHJ5PvPd-pn2-Yjfg1K6jU0Ym@Dwight_Miller.iix.com>`

```
I forgot my emoticon.  No flame was actually presumed.  Just trying to
establish my seniority rights!

Tom Morrison

Thane Hubbell wrote in message ...
>On Tue, 9 Mar 1999 13:37:32, "Tom Morrison" <t.morrison@liant.com>
>wrote:
[snip]
>My message was terser than I intended, no flame was supposed to leave
>the thrower!
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E439BE.AAB448F7@NOSPAMhome.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net>`

```
Tom Morrison wrote:
> 
> Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...
…[50 more quoted lines elided]…
> Liant Software Corporation


It has, thanks.   I wonder why relative files aren't used much in PC
environments.  It does have several advantages, especially where you
don't already have a well developed indexed system.

I think I would skip indexed files altogether on most PC environments,
opting instead to some type of DBMS - just for universality.  Java seems
to do this.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1p3g$7m4$1@news.igs.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com>`

```

Howard Brazee wrote in message

>I think I would skip indexed files altogether on most PC environments,
>opting instead to some type of DBMS - just for universality.  Java seems
>to do this.

I think that if I were writing code for general bussiness applcations, in
effect inhouse code, I might do the same.  However, I do not.  I am writing
self contained, standalone systems. In that type of application (keep in
mind Cobol is used on PC's mainly by VARS), there is far less neccessity to
be able to "code on the fly" in several languages.
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e4a048.514823750@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com>`

```
On Mon, 08 Mar 1999 13:57:34 -0700, Howard Brazee
<brazee@NOSPAMhome.com> wrote:


>It has, thanks.   I wonder why relative files aren't used much in PC
>environments.  It does have several advantages, especially where you
>don't already have a well developed indexed system.
>

I use relative files for some things - but interestingly, different
platforms offer different support.  For example:  With Realia I can
access a sequential file using relative access *IF* I define it as a
bytestream file.

With MicroFocus I can access a sequential file (not line sequential)
as if it were a relative file, simply by saying it is in the select.

With Realia, and NON bytestream files, there are added bytes in each
record to allow Realia to identify the relative key. The same is true
of Fujitsu.  

Most of the advantages of a relative file can be acquired by useing an
indexed file with a record number for the key - and I think this is
easier for most programmers to understand.  Also, some implenentations
of relative access are FAST while others are dismally slow.  (ie RSDS
file access with VSAM).
```

###### ↳ ↳ ↳ Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c3dr7$nvf$1@server.cntfl.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com>`

```

Howard Brazee wrote in message <36E439BE.AAB448F7@NOSPAMhome.com>...
[...]
>> Howard Brazee wrote in message <36E4031C.9250754@NOSPAMhome.com>...
>> >I'm a curious mainframe guy.
[...]
>[... ]  I wonder why relative files aren't used much in PC
>environments.  It does have several advantages, especially where you
>don't already have a well developed indexed system.

Firstly, I think indexed file management in COBOLs on PCs is
well-developed.

Secondly, it seems to me, the primary advantage of relative files
is the fast direct access for data that cannot be held in memory.
With virtual memory and disk caching there is little use for relative
files. (I do use a relative file to off-load a large table to disk; but the
application is still restricted to 640K. I off-loaded three other tables
as an indexed file since the lookup was random rather than relative.
Furthermore, these files tend to reside in disk cache.)

Any other comments?
-------------------------------
Rick Smith
e-mail: < ricksmith at aiservices dot com >
```

###### ↳ ↳ ↳ Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 6)_

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c3s15$gd2$1@news.igs.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com>`

```

Rick Smith wrote in message <7c3dr7$nvf$1@server.cntfl.com>...

>Secondly, it seems to me, the primary advantage of relative files
>is the fast direct access for data that cannot be held in memory.
…[4 more quoted lines elided]…
>Furthermore, these files tend to reside in disk cache.)


I am starting to wonder about using files at all.  I am converting a Cobol
system that ran for ten years with a 40 meg disk drive to run on a 128
megabyte machine.  A customer name address file of 25000 records is probably
in the 6-7 megabyte range.  Perhaps just loading the whole thing into a
table on startup is the way to do it.
```

###### ↳ ↳ ↳ Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com>`

```
On Tue, 9 Mar 1999 15:13:05, "Rick Smith" <ricksmith@aiservices.com> 
wrote:

>> Secondly, it seems to me, the primary advantage of relative files
> is the fast direct access for data that cannot be held in memory.
…[5 more quoted lines elided]…
> 

I've done this two ways, when using compilers restricted to 64K 
tables.

First - only offload to a relative file when the table size is 
exceeded.

Second - make 64K "images" of the table, so it's in chunks, and then 
decide which chunk to search based on it's first and last entries.  
The files are not relative - they are "flat" and placed enmass in the 
table area of working storage when required.
```

###### ↳ ↳ ↳ Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c4545$1vu@sjx-ixn9.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com> <Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com>`

```


Thane Hubbell wrote in message ...
>On Tue, 9 Mar 1999 15:13:05, "Rick Smith" <ricksmith@aiservices.com>
>wrote:
>
  <snip>
>
>Second - make 64K "images" of the table, so it's in chunks, and then
…[4 more quoted lines elided]…
>

I ask this every few months (and this comment certainly brings it to mind),

Are there any IBM mainframe COBOL programs out there that actually USE "Data
in Virtual"?  (For non-IBM mainframe people, this is a system that lets you
store "large chunks of data" in a file system - that can then be read -
sort-of - into your program as a table - or whatever. This is a cruddy
explanation of what it is, but then again, I don't know many COBOL
programmers who actually use it.)
```

###### ↳ ↳ ↳ Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 8)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e70b34.83826596@news3.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com> <Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com> <7c4545$1vu@sjx-ixn9.ix.netcom.com>`

```
On Tue, 9 Mar 1999 15:50:48 -0600, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Are there any IBM mainframe COBOL programs out there that actually USE "Data
>in Virtual"?  (For non-IBM mainframe people, this is a system that lets you
…[3 more quoted lines elided]…
>programmers who actually use it.)

When DIV came around (some 10-13 years ago)  I wrote a small test program to see if it
really worked - in assembler, of course - and then wrote a COBOL wrapper fo rit.  I never
used the provided IBM CALL interfaces for higher languages, though
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 8)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e671a8.633977103@news1.ibm.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com> <Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com> <7c4545$1vu@sjx-ixn9.ix.netcom.com>`

```
On Tue, 9 Mar 1999 15:50:48 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>
>
…[21 more quoted lines elided]…
>

I've done it "Manually" but not with any particular (special) IBM
product.  There is/was such a beast?
```

###### ↳ ↳ ↳ Data In Virtual (was Re: Usefullnes of Relative Files (was: Re: Deleted records)

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c6c6p$smg@dfw-ixnews5.ix.netcom.com>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com> <Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com> <7c4545$1vu@sjx-ixn9.ix.netcom.com> <36e671a8.633977103@news1.ibm.net>`

```
Thane Hubbell wrote in message <36e671a8.633977103@news1.ibm.net>...
  <snip>
>>
>>Are there any IBM mainframe COBOL programs out there that actually USE
"Data
>>in Virtual"?  (For non-IBM mainframe people, this is a system that lets
you
>>store "large chunks of data" in a file system - that can then be read -
>>sort-of - into your program as a table - or whatever. This is a cruddy
…[5 more quoted lines elided]…
>product.  There is/was such a beast?

Thane,
  That depends on what you mean by "manually".  There is a documented CALL
interface for "data in virtual".  There is no native COBOL syntax for this -
but the CALL interface is fairly reasonable for IBM COBOL mainframe
programmers.
```

###### ↳ ↳ ↳ Re: Usefulness of Relative Files (was: Re: Deleted records)

_(reply depth: 8)_

- **From:** SimonLElliott <"Simon.L.Elliott[Delete.Me]"@CapGemini.Co.UK>
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E6BD73.EEBA4096@CapGemini.Co.UK>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <36E439BE.AAB448F7@NOSPAMhome.com> <7c3dr7$nvf$1@server.cntfl.com> <Jl0PnHJ5PvPd-pn2-V1Pmvdc2EVgD@Dwight_Miller.iix.com> <7c4545$1vu@sjx-ixn9.ix.netcom.com>`

```

With my CICS Sysprog hat on.

It's possible that as an applications programmer in an IBM mainframe environment
you may be using (if I understand the term correctly) Data in Virtual without
knowing it.

MVS and CICS quite merrily buffer data in storage whenever possible (one of my
jobs is to tune CICS file buffering). Add to that, controller and disk cache,
solid state disks, as well as the use of 'Dataspaces' for a really big files and
there's a good chance that reading a record doesn't necessarily result in a
'traditional'  physical I/O (head movement over spinning disk or a few more tape
revolutions) at all.

Referring to the subject of PCs and indexed records. I would guess that one
reason for the poor implementation would be that it's not required (or
demanded). A box capable of holding a 16M file in storage is going to be pretty
fast at finding a record, keyed access or not. Presumably this means that all
these wonderful PC database systems are using 'flat' files - even DB2?
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 4)_

- **From:** "John Casagrande" <john@casagrande.ch>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c3v4u$7ra$1@news.imp.ch>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net>`

```

Tom Morrison wrote:

>
>The original subject of this thread, RM/COBOL, has such a utility that will
…[3 more quoted lines elided]…
>

Hello Tom,
I am using RM Cobol for Windows 6.51 under Windows 98.
Is there such an utility in this RM version and what is the NAME of the
Utility?

I am quite new in Newgroups and I am very INSPIRED  of the way you guys and
girls handle
such a simple question "deleted records"!
Compliments to all of you!
```

###### ↳ ↳ ↳ Re: Deleted records

_(reply depth: 5)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c48vf$ijp$1@client2.news.psi.net>`
- **References:** `<7bpkes$pte$1@news.imp.ch> <36e09983.251193672@news1.ibm.net> <36E4031C.9250754@NOSPAMhome.com> <BMWE2.943$Tw3.148552@client.news.psi.net> <7c3v4u$7ra$1@news.imp.ch>`

```
John Casagrande wrote in message <7c3v4u$7ra$1@news.imp.ch>...
[snip]
>I am using RM Cobol for Windows 6.51 under Windows 98.
>Is there such an utility in this RM version and what is the NAME of the
>Utility?

It was introduced in v6.6.  A new recovery utility (described in Appendix G
of the User Guide) has made the previous recovery utilities obsolete.  (But,
in the tradition of COBOL, we continue to ship the obsolete modules for
compatibility.)

>
>I am quite new in Newgroups and I am very INSPIRED  of the way you guys and
>girls handle such a simple question "deleted records"!
>Compliments to all of you!


I extend thanks from all of us at Liant!

Best regards,
Tom Morrison
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
