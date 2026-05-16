[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol problem

_39 messages · 9 participants · 2005-02_

---

### Cobol problem

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-03T22:03:16+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`

```
Hi,
Did sent an earlier posting for advise but alignment seems to be out.
Will post it again here.

Would appreciate someone out there can advise/enlightened ??
I have provided the code below and hope someone could help to advise
what need to be change as I had indeed did my initialisation and still
can't figure out why.

Basically the objective is to extract the full record from the input file 
(fixed length)
and output to an o/p file (fixed length of input file + another 
11bytes(date+indic field)
with the following format :

Input
======
xxxxx  xxxxx  xxxxx  xxxxx

Ouput
======
YYYY-MM-DDx   xxxxx xxxxx xxxxx xxxxx
* o/p need to include a 10 byte date field and a 1 byte indicator field,
   followed by the input file records that were extracted.

As the input copybook consists of a lot of fields (incl OCCURS stt etc),
hence I thought of just writing out the full record to an o/p FLAT file,
done with a single declaration in the o/p copybk (ie no individual field
declaration, just a flat file declaration in the OUTPUT file)

However, when I do that, part of the record extracted out contain
the prev record data from the input file which is weird as I did
initialised it and it only happen to some records extracted and not all.

In short , o/p will be something like this :

<----------(Ok)---------><---(Not ok)contain prev i/p rec data--->
YYYY-MM-DDX  xxxxx  xxxxx xxxxx  xxxxx  xxxxx  xxxxx  xxxxx

In addition, the record o/p happen only from column 700 of the input file
onward of the data to be o/p. The rest of the field are extracted correctly.

If not, must I really declared my o/p file field by field and write each out 
by a
'MOVE' statement. That's will be a massive effort.

Below are my code :

*=====================
 INPUT-OUTPUT SECTION.
*=====================
 FILE-CONTROL.
*=============

SELECT TRANS-FILE  ASSIGN TO AQTFILE
       ORGANIZATION IS INDEXED
        ACCESS       IS SEQUENTIAL
        RECORD KEY   IS TFKEY
        FILE STATUS  IS TRANS-STATUS.

SELECT TREXTR-FILE  ASSIGN TO AQEXTR.


*==============
 DATA DIVISION.
*==============
 FILE SECTION.
*=============

FD  TRANS-FILE
       LABEL RECORDS STANDARD
       RECORD CONTAINS 700 TO 1527 CHARACTERS <=**Take note
       BLOCK CONTAINS 0 RECORDS.

01  TRANS-FILE-REC.
      05  TFKEY.
           10  xxx           PIC XX.
           10  xxx           PIC X(20).
           10  xxx           PIC X(11).
           10  xxx           PIC X(13).
           10  xxx           PIC XX.
           10  xxx           PIC 99.
       05  FILLER       PIC X(34).
       05  xxx              PIC 9(8).
       05  FILLER       PIC X(1435).

01  TRANS-FILE-REC2.
      05  xxx                 PIC X(50).
      05  FILLER          PIC X(650).

FD  TREXTR-FILE
       LABEL RECORDS STANDARD
       BLOCK CONTAINS 0 RECORDS.

      COPY AQEXTR.

** The above copybk(AQEXTR) consist of just a single
length declaration for the header, detail and footer.
ie, Did NOT declare field by field for the detail part.
Just specified the full length for it)


 30000-PROCESS-TRANS.
*====================
 PERFORM UNTIL xxxx
   MOVE TRANS-FILE-REC TO TRANS-RECORD  <==
   PERFORM 32000-EXTRACT-ATRANS
   PERFORM 33000-GET-NEXT-TRANS
 END-PERFORM.


 32000-EXTRACT-ATRANS.
*====================
 INITIALIZE ATRANS-RECORD.    <== Did initialise here of the o/p rec
 PERFORM 33000-WRITE-TRANS-HEADER.
 PERFORM 34000-WRITE-TRANS-DETAIL.


 34000-WRITE-TRANS-DETAIL.
*=========================
 MOVE WS-BIZ-DATE TO ATRANS-BIZ-DATE
 MOVE ' ' TO ATRANS-DML-TAG

**=>move all i/p to o/p for 'detail'part of o/p file
 MOVE TRANS-RECORD TO ATRANS-RECORD.
**==>Write the record
 WRITE ATRANS-DETAIL.
```

#### ↳ Re: Cobol problem

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-03T14:29:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11052d8ng7an6a7@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`

```
Rick wrote:
> Hi,
> Did sent an earlier posting for advise but alignment seems to be out.
…[124 more quoted lines elided]…
> WRITE ATRANS-DETAIL.

How does your program know which of two records to read? One is 700 bytes, 
the other is 1757. Not knowing any differently, the program will read the 
1757 bytes.

1. Are the records delimited (CR/LF)? If so, change SEQUENTIAL in the SELECT 
statement to LINE SEQUENTIAL.

2. Do you know, in advance, the length of the record you are about to read? 
If so, you can dynamically adjust the record size just before the read [01 
FILLER OCCURS 1 TO 1757 DEPENDING ON NUMBYTE PIC X.]

Absent these two possibilities, you're pretty-much screwed for any simple 
read process.
```

##### ↳ ↳ Re: Cobol problem

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-04T22:17:49+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctvtld$stv$1@reader01.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <11052d8ng7an6a7@news.supernews.com>`

```

"JerryMouse" <nospam@bisusa.com>
> How does your program know which of two records to read? One is 700 bytes, 
> the other is 1757. Not knowing any differently, the program will read the 
> 1757 bytes.
===> If this is the case, any advise that can resolve the issue?
I try to remove the part under FD ( RECORD CONTAINS 700 TO 1527 CHARACTERS),
but the o/p is still the same (ie some records extracted fine, for some 
other record extracted,
their fields's extracted are ok, but some fields, which is supposed to be 
blank, however,
contain prev input record fields' value, which resulted in my o/p being 
wrong.
Fyi, my INPUT file contains a lot of fields and those OCCURS statement, not 
sure
is this that caused my pgm's bug.


> 1. Are the records delimited (CR/LF)? If so, change SEQUENTIAL in the 
> SELECT statement to LINE SEQUENTIAL.
====> No


> 2. Do you know, in advance, the length of the record you are about to 
> read? If so, you can dynamically adjust the record size just before the 
> read [01 FILLER OCCURS 1 TO 1757 DEPENDING ON NUMBYTE PIC X.]
==> Can further elaborate on the above and feel free to let me know where
and how it can be done in my pgm's code that was posted earlier.
How's is the syntax like? Can give an eg.
```

###### ↳ ↳ ↳ Re: Cobol problem

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-04T10:01:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<110773jjmvtmk96@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <11052d8ng7an6a7@news.supernews.com> <ctvtld$stv$1@reader01.singnet.com.sg>`

```
Rick wrote:
> "JerryMouse" <nospam@bisusa.com>
>> How does your program know which of two records to read? One is 700
…[25 more quoted lines elided]…
> How's is the syntax like? Can give an eg.

PART I
======

On OUTPUT, you decide which record (of a multi-record file) to write. You, 
therefore, implicitly determine the number of bytes to write to the output 
file. This is NOT the case when reading the file.

FD MYFILE.
01  MYREC-1   PIC X(10000).
01  MYREC-2   PIC X(10).

Whether you WRITE MYREC-1 or WRITE MYREC-2 determines whether the program 
writes 10,000 bytes or only ten. This is not the case for READs.

Every READ against the above file will input 10000 bytes.

Okay, here's the drill. If you have a "SEQUENTIAL" input file with:
1. Records of varying size, and
2. These records are not delimited (by, for example, CR/LF), and
3. You do not know in advance the length of the next record to be read, then
the program has NO WAY of knowing how much of the file to transfer when you 
issue a READ command. The program, by definition, always transfers the 
number of bytes equal to the maximum record.


This does not mean the file is inaccessible in COBOL, but the techniques for 
doing so are fairly advanced and require hand-crafting. Some advanced 
methods that come to mind are:

1. Read the file into a humongous array and de-construct each record. When 
you get within (max-record-size) of the end of the array, bump the residual 
of the block to the top, read more of the file, rinse, repeat.

2. Read the file one byte at a time (01 MYREC PIC X.) building a record as 
you go. Presumably you know when a record is complete. (This is S-L-O-W and 
should be avoided in a production environment)

3. Use more primitive routines to transfer data that involve STARTING-BYTE & 
BYTES-TO-TRANSFER  variables. If on a PC, the compiler authors may have also 
provided these DOS-oriented routines (CBL_OPEN_FILE, etc.).

PART II.
======

If you know, in advance, how long the next record is supposed to be, you can 
easily handle the file. In the example below, each "header" record (of 80 
bytes) tells you how many "detail" records follow (each of 10,000 bytes). 
This arrangement fulfills the requirement of knowing in advance the length 
of the next record to read.

FD MYFILE.
01  MYREC.
   02  FILLER OCCURS 1 TO 10000 DEPENDING ON RECSIZE PIC X.

WORKING STORAGE.
01  HEADER-REC.
   02  FILLER   PIC X(30).
   02  NUM-DETAILS  PIC 999.
   02  FILLER  PIC X(67).

01  DETAIL-REC  PIC X(10000).

01  RECSIZE   PIC 9(5).

PROCEDURE DIVISION.
...
   OPEN INPUT MYFILE.
   PERFORM PROCESS-LOOP UNTIL EOF = 'YES'
   CLOSE MYFILE.
   STOP RUN.

PROCESS-LOOP.
   MOVE 80 to RECSIZE
   READ MYFILE into HEADER-REC
      AT END MOVE 'YES' to EOF
      NOT AT END
         MOVE 10000 to RECSIZE
         PERFORM READ-DETAIL NUM-DETAILS TIMES
  END-READ.

READ-DETAIL.
   READ MYFILE INTO DETAIL-REC.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 4)_

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-05T17:55:25+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cu22la$vd5$1@reader01.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <11052d8ng7an6a7@news.supernews.com> <ctvtld$stv$1@reader01.singnet.com.sg> <110773jjmvtmk96@news.supernews.com>`

```

"JerryMouse" <nospam@bisusa.com> >
PART II.
> ======
>
…[8 more quoted lines elided]…
>   02  FILLER OCCURS 1 TO 10000 DEPENDING ON RECSIZE PIC X.
====> Hi Jerry, my input cpybook has  a length of 1527 and contains a lot of 
fields
and only some fields(not all) contains OCCURS statement, so does the above 
sytax
should be written as :
02  FILLER OCCURS 1 TO 1527 DEPENDING ON RECSIZE PIC X.
=>**what does PIC X value be then??1527??




>
> WORKING STORAGE.
…[27 more quoted lines elided]…
>
===> Hi, my problem is the WRITE part. My o/p is correct for some
records that were extracted, but in some record, part of the fields are
moved correctly while some of the fields, which is supposed to be blank,
get populated by the values of my prev record input files and it only
happen from columns 700 onwards. Not sure is it because of the OCCURS
stt in my input copybook (declared in some fields) and that my o/p is just a
flat file with declaration of a single length.

Feel free to look at my inital post on the coding and feel free to advise
from there how the code could be improved. :-)  Tks Jerry for your kind 
advise
given all along :-)
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-06T11:01:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<110cjblopgf079@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <11052d8ng7an6a7@news.supernews.com> <ctvtld$stv$1@reader01.singnet.com.sg> <110773jjmvtmk96@news.supernews.com> <cu22la$vd5$1@reader01.singnet.com.sg>`

```
Rick wrote:
> "JerryMouse" <nospam@bisusa.com> >
> PART II.
…[17 more quoted lines elided]…
> =>**what does PIC X value be then??1527??

PIC X be one byte. There be RECSIZE number of them in one record. You be 
setting the value of RECSIZE before you be reading the file.

>
>
…[39 more quoted lines elided]…
> just a flat file with declaration of a single length.

Okay, if you say so. I say otherwise. Your problem is in the READ portion of 
the program.

>
> Feel free to look at my inital post on the coding and feel free to
> advise from there how the code could be improved. :-)  Tks Jerry for
> your kind advise
> given all along :-)

I did. Your problem is with the READ statement - you do not explicitly tell 
the program how much to read, so it reads the maximum amount declared in the 
FD.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 6)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-02-06T10:46:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107715618.694005.267060@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<110cjblopgf079@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <11052d8ng7an6a7@news.supernews.com> <ctvtld$stv$1@reader01.singnet.com.sg> <110773jjmvtmk96@news.supernews.com> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com>`

```
This thread doesn't seem to be going anywhere.  Can we agree that the
file Rick is attempting to read is NOT a fixed length file?  It
contains 2 types of records of differing lengths.  By definition fixed
length files contain records of a single fixed length.  That leaves 2
possibilities: variable length recs or undefined recs.

Rick, can you enlighten us?

If the recs are undefined you can't solve your problem unless you can
identify each rec's type (and therefore its length).  Then you can
de-block the recs in the block.

If the recs are variable (i.e. contain BDW/RDWs) you can take your lead
from Bill Klein's post.

The key here is to determine what kind of recs you're dealing with.

Regards, Jack.


JerryMouse wrote:
> Rick wrote:
> > "JerryMouse" <nospam@bisusa.com> >
…[3 more quoted lines elided]…
> >> If you know, in advance, how long the next record is supposed to
be,
> >> you can easily handle the file. In the example below, each
"header"
> >> record (of 80 bytes) tells you how many "detail" records follow
> >> (each of 10,000 bytes). This arrangement fulfills the requirement
of
> >> knowing in advance the length of the next record to read.
> >>
…[3 more quoted lines elided]…
> > ====> Hi Jerry, my input cpybook has  a length of 1527 and contains
a
> > lot of fields
> > and only some fields(not all) contains OCCURS statement, so does
the
> > above sytax
> > should be written as :
…[3 more quoted lines elided]…
> PIC X be one byte. There be RECSIZE number of them in one record. You
be
> setting the value of RECSIZE before you be reading the file.
>
…[36 more quoted lines elided]…
> > are moved correctly while some of the fields, which is supposed to
be
> > blank, get populated by the values of my prev record input files
and
> > it only happen from columns 700 onwards. Not sure is it because of
> > the OCCURS stt in my input copybook (declared in some fields) and
that my
> > o/p is
> > just a flat file with declaration of a single length.
>
> Okay, if you say so. I say otherwise. Your problem is in the READ
portion of
> the program.
>
> >
> > Feel free to look at my inital post on the coding and feel free to
> > advise from there how the code could be improved. :-)  Tks Jerry
for
> > your kind advise
> > given all along :-)
>
> I did. Your problem is with the READ statement - you do not
explicitly tell
> the program how much to read, so it reads the maximum amount declared
in the 
> FD.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 6)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-06T19:05:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9QMFBviPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com>`

```
.    On  06.02.05
  wrote  nospam@bisusa.com (JerryMouse)
     on  /COMP/LANG/COBOL
     in  110cjblopgf079@news.supernews.com
  about  Re: Cobol problem


n> Your problem is with the READ statement - you do not explicitly
n> tell the program how much to read, so it reads the maximum amount
n> declared in the FD.

   No, this is not UNIX and C, where the program has to tell the file  
system the number of bytes it wants to read.

   COBOL file I/O READs simply the next record, as large as it is in  
the file.

   If the program has declared the record to be of variable size, like  
this:

   RECORD IS VARYING IN SIZE
             FROM minimal-size TO maximal-size CHARACTERS
             DEPENDING ON this-record-size


   then a sequential READ will read the next record, and simply put  
the size of the record read into the data item "this-record-size".


   Coming back on Rick X's problem, maybe a previous program has  
erroneously written the file as having fixed length records, and thus  
left the contents of the previous record, what now puzzles poor Rick.

   He should get a dump of the file, and check its actual contents.



Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

A. Der Mann hat viele Kinder. B. Ja, aber ich glaube, von den meisten hat er bloï¿½ die Korrektur besorgt.  -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 7)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-02-06T15:46:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107733572.392607.319030@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<9QMFBviPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de>`

```

Lueko Willms wrote:
> .    On  06.02.05
>   wrote  nospam@bisusa.com (JerryMouse)
…[9 more quoted lines elided]…
>    No, this is not UNIX and C, where the program has to tell the file

> system the number of bytes it wants to read.
>
>    COBOL file I/O READs simply the next record, as large as it is in

> the file.
>
n> Your problem is with the READ statement - you do not explicitly
n>


tell the program how much to read, so it reads the maximum amount


n> declared in the FD.

   No, this is not UNIX and C, where the program has to tell the file

system the number of bytes it wants to read.


   COBOL file I/O READs simply the next record, as large as it is in
the file.

No, "COBOL I/O" reads the next BLOCK into the buffer and aligns the 1st
databyte of the buffer w/the 1st byte defined in the FD 01 level.  When
the length of the FD 01 definition is greater than the true length of
the rec in the buffer you erroneously see some of the next rec(s) in
the buffer.  This may also appear as some of the I/P recs being
"missing" in the O/P.

With subsequent READs the buffer ptr is manipulated to point to the
next rec until all data in the buffer is presented to the pgm, then a
new block is READ into the buffer.

END of REPLY



>    If the program has declared the record to be of variable size,
like
> this:
>
…[10 more quoted lines elided]…
> erroneously written the file as having fixed length records, and thus

> left the contents of the previous record, what now puzzles poor Rick.
>
…[5 more quoted lines elided]…
> Lüko Willms
http://www.willms-edv.de
> /--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --
>
> A. Der Mann hat viele Kinder. B. Ja, aber ich glaube, von den meisten
hat er bloß die Korrektur besorgt.  -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-06T23:50:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P2yNd.1049497$B07.148466@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <1107733572.392607.319030@z14g2000cwz.googlegroups.com>`

```
"slade2" <jacksleight@hotmail.com> wrote in message 
news:1107733572.392607.319030@z14g2000cwz.googlegroups.com...

<snip>

No, "COBOL I/O" reads the next BLOCK into the buffer and aligns the 1st
databyte of the buffer w/the 1st byte defined in the FD 01 level.  When
the length of the FD 01 definition is greater than the true length of
the rec in the buffer you erroneously see some of the next rec(s) in
the buffer.  This may also appear as some of the I/P recs being
"missing" in the O/P.

With subsequent READs the buffer ptr is manipulated to point to the
next rec until all data in the buffer is presented to the pgm, then a
new block is READ into the buffer.

What you describe is how SOME implementations may work - but is certainly NOT 
anything the COBOL Standard requries. Even on IBM mainframes where (unlike most 
Workstation compiilers/systems) "BLOCKS" still have meaning, what you describe 
doesn't always happen (and hasn't ever since COBOL has supported 31-bit 
addressing).

Assuming that "records are in a buffer" (addressable from the FD) is incredibly 
DANCEROUS - and is something that I have never heard of any vendor actually 
"supporting" (or documenting as valid).
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 9)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-02-06T19:55:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107748534.190708.227720@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<P2yNd.1049497$B07.148466@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <1107733572.392607.319030@z14g2000cwz.googlegroups.com> <P2yNd.1049497$B07.148466@news.easynews.com>`

```
I keep forgetting to mention that my remarks are intended to be  viewed
from the IBM mainframe  perspective.

BK wrote:
"Assuming that "records are in a buffer" (addressable from the FD) is
incredibly
DANCEROUS - and is something that I have never heard of any vendor
actually
"supporting" (or documenting as valid)."

What I was saying there was that the FD 01 data structure acts as an
"overlay" for the data in the buffer, similar to the way "passed" data
is referenced in the LINKAGE SECTION of a COBOL pgm.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-07T07:39:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JWENd.1362564$f47.231539@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <1107733572.392607.319030@z14g2000cwz.googlegroups.com> <P2yNd.1049497$B07.148466@news.easynews.com> <1107748534.190708.227720@z14g2000cwz.googlegroups.com>`

```
Still not true with current IBM mainframe COBOL compilers.

The FD *may* point to storage in the buffer - but it often does not.  For 
example:

 - when the EXTERNAL attribute is specified for a file
 - for some (not all) programs compiled with RENT and DATA(31) -    for some 
QSAM Files the "area" under the FD is a copy (above the line) of a buffer below 
the line.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-06T21:45:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<110dp28s6bu47ac@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  06.02.05
>  wrote  nospam@bisusa.com (JerryMouse)
…[13 more quoted lines elided]…
> the file.

No. Absolutely not. It is the program that determines the record size. If 
some program wrote a file consisting of 100-byte records and my program that 
reads the file declares the records to be 57 bytes, then, by God, the 
records are 57 bytes!

>
>   If the program has declared the record to be of variable size, like
…[8 more quoted lines elided]…
> the size of the record read into the data item "this-record-size".


You've got it backwards. It is "this-record-size" that determines how much 
to read, not the read determining "this-record-size."
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 8)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-07T09:33:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9QQIFynPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com>`

```
.    On  06.02.05
  wrote  nospam@bisusa.com (JerryMouse)
     on  /COMP/LANG/COBOL
     in  110dp28s6bu47ac@news.supernews.com
  about  Re: Cobol problem


>>   No, this is not UNIX and C, where the program has to tell the file
>> system the number of bytes it wants to read.
>>
>>   COBOL file I/O READs simply the next record, as large as it is in
>> the file.

n> No. Absolutely not. It is the program that determines the record size.

   In the FD, but not in the READ statement

n> If some program wrote a file consisting of 100-byte records and my
n> program that reads the file declares the records to be 57 bytes, then,
n> by God, the records are 57 bytes!

   This is from COBOL-2002 on the READ statement:

13) If the number of bytes in the record that is read is less than the minimum size specified by the record
description entries for file-name-1, the portion of the record area that is to the right of the last valid character
read is undefined. If the number of bytes in the record that is read is greater than the maximum size specified
by the record description entries for file-name-1, the record is truncated on the right to the maximum size. In
either of these cases, the READ statement is successful and an I-O status is set indicating a record length
conflict has occurred. (See 9.1.12, I-O status.)

   So you are right -- when the file is declared with a recordsize  
which does not match the actual recordsize of the file, then shit will  
happen.

   But this does not depend on putting some value in the DEPENDING ON  
date-name-1 of the VARYING FD clause, at least not for a READ. The  
program has no means to determine how long the _next_ record, the one  
not yet read, might be. It has to rely on what the run-time-system  
supplies.


>>   If the program has declared the record to be of variable size, like
>> this:
…[7 more quoted lines elided]…
>> the size of the record read into the data item "this-record-size".


n> You've got it backwards. It is "this-record-size" that determines how
n> much to read, not the read determining "this-record-size."

   If you change the "read" in your remark to "WRITE", then you are  
right:


This is from the COBOL-1985 standard specification, on the RECORD  
clause of the File Definition in the Sequential I/O module:

(8) If data-name-l is specified, the number of character positions in
the record must be placed into the data item referenced by data-name-l
before any RELEASE, REWRITE, or WRITE statement is executed for the
file.

(11) If data-name-l is specified, after the successful execution of a
READ or RETURN statement for the file, the contents of the data item
referenced by data-name-l will indicate the number of character
positions in the record just read.


"data-name-1" refers to the item "DEPENDING ON" which the VARYING
size of the record is indicated or determined.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Der Mann hatte soviel Verstand, daï¿½ er zu fast nichts mehr in der Welt zu gebrauchen war. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-02-07T09:27:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<110f266f0kroc92@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <9QQIFynPflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  06.02.05
>  wrote  nospam@bisusa.com (JerryMouse)
…[41 more quoted lines elided]…
> supplies.

You say: "The program has no means to determine how long the _next_ 
record..." is correct. The programmer must decide how much to read, not the 
runtime system. He does that by setting the DEPENDING ON value.

Remember, we are talking about undelimited records.

So, pretend:

01  MYREC.
  02  FILLER OCCURS 1 TO 10000 TIMES DEPENDING ON nnn PIC X.

I want to read the first 80 bytes of the file. What to do?

I say set "nnn" to "80" and issue the read.





>
>
…[18 more quoted lines elided]…
> right:

And, for undelimited sequential files, if I leave the statement alone, I'm 
also right.

>
>
…[15 more quoted lines elided]…
> size of the record is indicated or determined.

The above simply cannot be true for a sequential (byte-stream), undelimited 
file. The operating system simply has no way of knowing the length of the 
record.

Here's my whole file:
ABCDEFGHIJKLMNOPQRSTUVWXYZ.

Here's my FD
01  MYREC.
  02  Filler OCCURS 1 TO 26 DEPENDING ON NNN PIC X.

I want to read the first "record." What do I do? (Remember, you hold that 
the OS will tell me how big this first record is.)

Alternatively, I want to read the first ten bytes. What do I do?
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-07T18:22:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TlONd.1405345$f47.238273@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <9QQIFynPflB@jpberlin-l.willms.jpberlin.de> <110f266f0kroc92@news.supernews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message 
news:110f266f0kroc92@news.supernews.com...
> Lueko Willms wrote:
<snip>
>
> Here's my whole file:
…[9 more quoted lines elided]…
> Alternatively, I want to read the first ten bytes. What do I do?

Jerry,
   An ANSI/ISO '85 Standard (or later <G>) conforming compiler that has the
     Record Varying in Size

phrase in its FD *must* be able to return the record size of each record when 
read.  Either your example isn't the "full" file (which would need to include 
record length information) *or* the information must be stored in some side 
file.  ("Line sequential" files - although not a part of the ANSI/ISO Standard 
also provide a way of getting this information.)

As for "reading the first 10 bytes" as if it were a record - if the first record 
isn't 10 bytes long, then you are out of luck.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-07T10:28:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107800930.981428.139360@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<110f266f0kroc92@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <9QQIFynPflB@jpberlin-l.willms.jpberlin.de> <110f266f0kroc92@news.supernews.com>`

```
> The programmer must decide how much to read, not the
> runtime system. He does that by setting the DEPENDING ON value.

You are confused.  The programmer sets the depending on value for
WRITEing, but for READing it is set by the externally detrermined size
of the actual record.

> Remember, we are talking about undelimited records.

In standard '85 Cobol, if records are undelimited (or unheaded) then
they must be fixed size.

If you were using other languages, such as C, then the read() statement
can specify an arbitrary number of bytes to be transferred.

> I want to read the first 80 bytes of the file. What to do?
> I say set "nnn" to "80" and issue the read.

The nnn will be completely ignored, the first record will be read and
nnn will be set to the size of that actual first record.  If the file
is not of a format that caters for the record sizes to be explicitly
known, by headers or terminators, then it will be a fixed length record
file and you should get a run-time error 39 indicating the file
structure does not match the FD.

In fact I tried this just to prove the point and I got a '39' file
status.  Have you tried the code that you proposed ?

> The above simply cannot be true for a sequential (byte-stream),
undelimited
> file. The operating system simply has no way of knowing the length of
the
> record.

Hmmm, so it is the Cobol standard that is wrong.

The way in standard '85 Cobol of reading an arbitrary byte-stream file
is to use a single byte record.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 8)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-07T08:12:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OOJNd.1442$504.188122@news20.bellglobal.com>`
- **In-Reply-To:** `<110dp28s6bu47ac@news.supernews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com>`

```
JerryMouse wrote:
> Lueko Willms wrote:
>>
…[32 more quoted lines elided]…
> 

Not on any Cobol I have used. The read statement *SETS* the 
this-record-size parameter, just as stated. It does say it is a 
sequential file, and I have never tried to use a variable record size on 
anything but sequential and Isam, but with those, the read statements 
sets the parameter.

Donald
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-07T07:50:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%mKNd.6657$Xi2.2339@fe40.usenetserver.com>`
- **In-Reply-To:** `<OOJNd.1442$504.188122@news20.bellglobal.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <OOJNd.1442$504.188122@news20.bellglobal.com>`

```
Donald Tees wrote:
> 
> Not on any Cobol I have used. The read statement *SETS* the 
…[3 more quoted lines elided]…
> sets the parameter.

You know, this jogged something in my memory.  We have a FD with a 
varying record size - and, before every read, we set the size to the 
maximum possible.  After the read, the size is reset to what we actually 
got.

So - I second that.  :)  If I can remember, I'll shoot the relevant 
pieces of code home today, and post them this evening.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 10)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-07T13:57:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dSONd.2159$504.230645@news20.bellglobal.com>`
- **In-Reply-To:** `<%mKNd.6657$Xi2.2339@fe40.usenetserver.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <OOJNd.1442$504.188122@news20.bellglobal.com> <%mKNd.6657$Xi2.2339@fe40.usenetserver.com>`

```
LX-i wrote:
> Donald Tees wrote:
> 
…[16 more quoted lines elided]…
> 

The following works just fine on Fujitsu.(with line sequential files, 
all records variable in size ... never tried it on pure sequential).

	open input input-file.
	move zero to file-size-count, record-count.
	read input-file at end
		move "Y" to end-flag.
	perform read-the-file
  	    until end-flag is equal to "Y".
	if linux-machine
		continue
	else
		multiply record-count by 2
			giving .
	add record-count to file-size-count.
	display "characters in file = " file-size-count.

read-the-file.
	add record-size-indicator to file-size-count.
	add 1 to record-count.
	read input-file at end
		move "Y" to end-flag.

Donald
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-12T19:05:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qJxPd.26894$2V1.4574@fe40.usenetserver.com>`
- **In-Reply-To:** `<dSONd.2159$504.230645@news20.bellglobal.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <OOJNd.1442$504.188122@news20.bellglobal.com> <%mKNd.6657$Xi2.2339@fe40.usenetserver.com> <dSONd.2159$504.230645@news20.bellglobal.com>`

```
Donald Tees wrote:
>     if linux-machine
>         continue
>     else
>         multiply record-count by 2
>             giving .

Giving what?  :)
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-07T11:27:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107804437.493203.5960@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<%mKNd.6657$Xi2.2339@fe40.usenetserver.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cu22la$vd5$1@reader01.singnet.com.sg> <110cjblopgf079@news.supernews.com> <9QMFBviPflB@jpberlin-l.willms.jpberlin.de> <110dp28s6bu47ac@news.supernews.com> <OOJNd.1442$504.188122@news20.bellglobal.com> <%mKNd.6657$Xi2.2339@fe40.usenetserver.com>`

```
> You know, this jogged something in my memory.  We have a FD with a
> varying record size - and, before every read, we set the size to the
> maximum possible.  After the read, the size is reset to what we
actually
got.

You probably set the size to max and then did an initialize or move
spaces to ensure that there was no residual data from the previous
record.  If you left it at some value that was less than maximum then
these would only work on the lesser size.

But note that the 'depending on' size has no effect on what is read and
the read sets the size to match the actual record.  The FD record area
beyond the actual record size is not cleared or changed by the read
(whereas the INTO area is cleared as if a MOVE had been done).
```

#### ↳ Re: Cobol problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-03T20:38:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ZvMd.711437$B07.99827@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`

```
If you change

FD  TRANS-FILE
       LABEL RECORDS STANDARD
       RECORD CONTAINS 700 TO 1527 CHARACTERS <=**Take note
       BLOCK CONTAINS 0 RECORDS.

to

 FD  TRANS-FILE
       LABEL RECORDS STANDARD
       RECORD varying in size from  700 TO 1527 CHARACTERS
           Depending on WS-Length
      BLOCK CONTAINS 0 RECORDS.

and add an
  01 WS-Length   Pic  999.

statement to your data division, then you will be guaranteed of getting a 
"variable length" file - which the original code does not do.  Also, it will 
allow you to test the WS-Length field after every READ to determine which size 
record you have actually read.

P.S.  The LABEL phrase is probably "useless" while the BLOCK CONTAINS clause may 
be useless - depending upon which compiler and what operating system you are 
using.
```

##### ↳ ↳ Re: Cobol problem

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-02-05T11:29:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107631760.302778.250740@c13g2000cwb.googlegroups.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <2ZvMd.711437$B07.99827@news.easynews.com>`

```
Hi Rick,

Addiing to Bill's remarks, you use a similar approach in setting up
your O/P FD using the same WS-Length field, and you would probably set
up your O/P file rec description in WS or the FD to look something
like:

01  OP-rec.
      05  your-MMDDYY-  pic x(010).
      05  OUT-IP-rec         pic x(yyy).
where,
yyy = the max rec size of the IP file.

Before WRITEing the OP rec, ADD 10 to WS-Length.

Regardless of the length of the I/P rec you're reWRITEing, WS-Length
will assure that the correct O/P length rec is written. 

Regards, Jack.
```

##### ↳ ↳ Re: Cobol problem

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-07T12:11:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107807068.107245.174200@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<2ZvMd.711437$B07.99827@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <2ZvMd.711437$B07.99827@news.easynews.com>`

```
> RECORD varying in size from  700 TO 1527 CHARACTERS
>          Depending on WS-Length

>  01 WS-Length   Pic  999.

A very minor point: it needs to be at least PIC 9(4).
```

#### ↳ Re: Cobol problem

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-07T10:54:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107802486.993492.242640@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`

```
> However, when I do that, part of the record extracted out
> contain the prev record data from the input file which is
> weird as I did initialised it and it only happen to some records
> extracted and not all.

Record areas in the FD are not cleared prior to reading a record nor is
the area past the record length space filled.  This means that when
reading a varaible record file when a short record is read the area
past the length of that record still has data from the previous longer
record.

When a variable record area is initialized it should be done with the
longest record area and any 'depending on' set to maximum value.

A simple case:

     FD InFile.
     01    A                 PIC X(10).
     01    B                 PIC X(20).

'INITIALIZE A' only clears 10 characters and leaves the last 10
characters with whatever was previously in B.

If 'READ InFile' reads a 'B' record of 20 characters is followed by a
'READ InFile' that reads a 'A' record then the record area will contain
the 10 bytes of the 'A' record followed by the last 10 bytes of the
previous 'B' record.

'READ' is not 'MOVE' (unless it is a READ INTO).

Solutions:

1) If you INITIALIZE (or MOVE SPACES) before each READ then do so using
the longest record area.

2) Identify the record actually read and use the corresponding record
area of the correct length when MOVEing it somewhere else.

3) WRITE the correct length output record.  If an 'A' record arrives
then WRITE OutA, if a 'B' record Arrives then WRITE OutB where these
are the correct length to contain the data required.

4) Use an working-storage area of the length of the largest record and
do 'READ InFile INTO WS-Record'.  This will read the next record into
the FD record area and then move that record to the ws record area and
will space fill beyond the actual record length.
```

##### ↳ ↳ Re: Cobol problem

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-08T16:33:37+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cu9qvk$be0$1@reader01.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <1107802486.993492.242640@z14g2000cwz.googlegroups.com>`

```
Hi Richard,
Guess I have done that based on your suggested "solution" given below.
Feel free to look at my coding at the very initial posting.
Can advice from there where the code can be further enhanced.

By the way, it only happen for some records starting from column 700
like that, where the field is supposed to be blank, yet it get
populated by prev input records fields.

Not sure is it because of my FD coding as below :
FD  TRANS-FILE
       LABEL RECORDS STANDARD
       RECORD CONTAINS 700 TO 1527 CHARACTERS <=**Take note
       BLOCK CONTAINS 0 RECORDS.

Even if I remove "RECORD CONTAINS 700..." coding, it still did not solve
my problem.

Tks in advance richard for your advise all along....   :-)


"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1107802486.993492.242640@z14g2000cwz.googlegroups.com...
>> However, when I do that, part of the record extracted out
>> contain the prev record data from the input file which is
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-08T09:33:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZH%Nd.1176594$B07.167393@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <1107802486.993492.242640@z14g2000cwz.googlegroups.com> <cu9qvk$be0$1@reader01.singnet.com.sg>`

```
Rick,
   We still don't understand exactly what the records in your file are like. 
From what you have said, it could be any of the following:

A) *ALL* records are actually 1527  long - but some only use 700 of those bytes 
(and the final part of those records are spaces).

B) some of the records are 1527 bytes long and others are 700 bytes long - but 
none are any other length

C) the shortest record is 700 bytes long the longest are 1527 bytes long - and 
there are records of various length in-between.

   ***

We (and you) must know exactly WHICH of those is true for you input file - in 
order to figure out how to help you.

Finally, have you told us which compiler and operations system you are working 
on?  Also, is it another COBOL program that creates your input file - or is 
created by a "text editor" or some non-COBOL program.  This *might* impact how 
to read the file.
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-08T20:44:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jw9Od.331290$Xk.147283@pd7tw3no>`
- **In-Reply-To:** `<ZH%Nd.1176594$B07.167393@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <1107802486.993492.242640@z14g2000cwz.googlegroups.com> <cu9qvk$be0$1@reader01.singnet.com.sg> <ZH%Nd.1176594$B07.167393@news.easynews.com>`

```
William M. Klein wrote:
> Rick,
>    We still don't understand exactly what the records in your file are like. 
> From what you have said, it could be any of the following:
> 
<snip>

This goes on an on..... Rick are you using a compiler for DOS/Windows ? 
If so, I can e-mail you two old PC Magazine DOS routines DR.COM and 
CO.COM which will display ANY file, except that in the case of comp 
fields they come out in gibberish - but a least you can get a handle on 
individual record layouts whether ISAM or Sequential.

If you want the routines, e-mail me as above dropping 'deletethis'.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Cobol problem

_(reply depth: 5)_

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-09T17:36:43+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cucjvu$9ib$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <1107802486.993492.242640@z14g2000cwz.googlegroups.com> <cu9qvk$be0$1@reader01.singnet.com.sg> <ZH%Nd.1176594$B07.167393@news.easynews.com> <Jw9Od.331290$Xk.147283@pd7tw3no>`

```
Hi James,
Using OS/390 :-)

"James J. Gavan" <jgavandeletethis@shaw.ca>
> This goes on an on..... Rick are you using a compiler for DOS/Windows ? If 
> so, I can e-mail you two old PC Magazine DOS routines DR.COM and CO.COM 
…[6 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Cobol problem

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-08T01:34:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107855246.188352.171190@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<cu9qvk$be0$1@reader01.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <1107802486.993492.242640@z14g2000cwz.googlegroups.com> <cu9qvk$be0$1@reader01.singnet.com.sg>`

```
> Guess I have done that based on your suggested "solution" given
below.

No you haven't, not in the fragments of code that I looked at.

> Feel free to look at my coding at the very initial posting.
> Can advice from there where the code can be further enhanced.

I'll go over this again for you, read this again:

RP> Record areas in the FD are not cleared prior to reading a record
nor is
RP> the area past the record length space filled.  This means that when
RP> reading a varaible record file when a short record is read the area
RP> past the length of that record still has data from the previous
longer
RP> record.

First read is of a record 20 bytes long containing all 'A':

Record Area:  AAAAAAAAAAAAAAAAAAA

Second Read is a record 10 bytes long containg all 'B':

Record Area: BBBBBBBBBBAAAAAAAAAA

Is this not what you are getting ?

Solution:  MOVE SPACES TO Trans-File-Rec before the READ.

If you still have the same problem then it may be that the actual
records in the file are longer than the 700 bytes you expect.

While you do carefully initialise the output ATrans-Record this is
pointless because the MOVE Trans-Record TO ATrans-Record completely
overwrites this.  You need to clear the _INPUT_ record area before the
READ and/or only move the _appropriate_ record size from the FD record
area to the working-storage (I assume) Trans-Record.

ie:
IF ( something or other )
      MOVE Trans-File-Rec2   TO Trans-Record
ELSE
     MOVE Trans-File-Rec      TO Trans-Record
END-IF

Because you are not clearing the input file record area before the read
and always moving the longest record area (Trans-File-Rec) you are
getting previous record's contents added to the 700 byte records.
```

#### ↳ Re: Cobol problem (INPUT File Format)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-08T22:22:15+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cuagbc$7j0$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg>`

```
Hi,
Pertaining to my earlier posting, here's basically how the
INPUT file look like. Just a format only below. Basically it's a
huge file with many fields and with 'redefines', 'occurs' all
that declare in the file.

Take note that there are
- REDEFINES
- OCCURS
- REDEFINES within a REDEFINES
use in the input file.

But my OUTPUT file is basically a flat file declaration only.

That's y not sure what the problem that's causing my o/p of
some of the field to contain prev input values when indeed
it's suppose to be blank.

Actually, my pgm correctly pick the record to be extracted(based on
condition),  just that some fields populate wrong values, when it's
supposed to be blanks. Weird.

For the code, refer to my initial posting.  :-)
Tks in advance for advise :-)


INPUT File <FORMAT>
=================
01  TRN-HEADER.

    05  TRN-xxxx-xxx     PIC X(50).

    05  TRN-DTE          PIC 9(06).

    05  FILLER           PIC X(1471).





01  TRN-RECORD           REDEFINES TRN-HEADER. <==**

    05  TRANS-KEY.

        10  xxxxx        PIC X(??).

        10  xxxxx        PIC X(??).

        10  xxxxx        PIC X(??).





    05  TRN-DETLS        PIC X(1260).          <==Take note

    05  TRN-CR-DETLS     REDEFINES  TRN-DETLS. <==**

        10  xxxxx        PIC X(??).

        10  xxxxx        PIC 9(??).



    05  TRN-DR-DETLS     REDEFINES  TRN-DETLS.

        10  xxxxx        PIC X(??).

        10  xxxxx  OCCURS 2.            <===**

            15  xxxxx    PIC X(??).

            15  xxxxx    PIC X(??).



    05  TRN-INT-DETLS    REDEFINES  TRN-DETLS.

        10  xxxxx        PIC X(??).

        10  xxxxx        PIC 9(??).

        10  xxxxx REDEFINES RMK-FLD-1    PIC X(??). <==**

        10  xxxxx        PIC X(??).

        10  xxxxxx REDEFINES RMK-FLD-2   PIC X(??).

        10  xxxxx        PIC 9(??).
```

##### ↳ ↳ Re: Cobol problem (INPUT File Format)

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-02-08T09:58:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ws4Od.3034$504.397597@news20.bellglobal.com>`
- **In-Reply-To:** `<cuagbc$7j0$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg>`

```
Rick wrote:
> Hi,
> Pertaining to my earlier posting, here's basically how the
…[9 more quoted lines elided]…
> 

Remove the 01 level redefines clauses.  Redefines is implictit with FD 
records ... I would have expected it to give you a compile error.

Donald
```

###### ↳ ↳ ↳ Re: Cobol problem (INPUT File Format)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-09T17:29:40+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cucjio$9i0$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg> <ws4Od.3034$504.397597@news20.bellglobal.com>`

```
Hi Donald,
Just a notice.
I can't just remove the 01 from the 'existing' INPUT file that is also used 
by many programs.



"Donald Tees" <donald_tees@sympatico.ca> wrote in message 
news:ws4Od.3034$504.397597@news20.bellglobal.com...
> Rick wrote:
>> Hi,
…[15 more quoted lines elided]…
> Donald
```

##### ↳ ↳ Re: Cobol problem (INPUT File Format)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-08T18:23:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<as7Od.1491709$f47.254857@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg>`

```
You still haven't answered my questions.  I don't want to know how you have 
defined the file in your program.  I want to know how the file ACTUALLY exists 
as a physical file.

Again, simply tell me WHICH of the following 3 descriptions matches the physical 
input file

1) All records are PHYSICALLY the same length - but some of them only use 700 
bytes - and have trailing spaces

2) Some physical records are 700 bytes long and some physical records are 1500+ 
bytes long

3) Some records are 700 bytes long; some records are 1500+ bytes long; and some 
physical records are any length in-between.

  ***

Your use of the term "flat file" and "file contains fields" sound like you don't 
understand how physical files exist.

Until you can answer my questions about the physical file you are working with 
for input, there is really no way we are going to be able to help you.  If you 
don't understand my questions, try and get a more experienced programmer in you 
shop to help you.
```

###### ↳ ↳ ↳ Re: Cobol problem (INPUT File Format)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-02-09T18:01:01+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cucldg$9jd$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg> <as7Od.1491709$f47.254857@news.easynews.com>`

```
Info as below for

'INPUT' file :

===============

ORGANIZATION  : VSAM KSDS - VARIABLE

RECORD SIZE   : 700 - 1527 BYTES



- The format of the input file, can see my initial posting

based on above subject :-) .



- Basically, all records are the same length.



- The record info store this way.Assume the input file

comprise of info on CR, DR,INTEREST transaction and if

the transaction is on CR , the input file for that record

will be populated for fields of those CR transaction,

wherelse the rest of those fields for DR and INTEREST

of the same record will be blanks. (inside this input field,

there are OCCURS, REDEFINES etc used based on the copybook)



- Of course, certain fields are mandatory for ALL records, like

userid, trans reference, date entered, time entered,  etc..



****

Basically, my definition of 'flat file' refer to my 'o/p'

file, with a single declaration length (no individual

fieldname declaration).



When mentioned 'file contains field', what I am trying to

say is that there are certain values being written to the o/p

file of certain columns, though there's really didn't exist a

'fieldname' there in the o/p file, as it's basically a flat file

for o/p.



Not sure how I should better elaborate.. :-)



Tks William :-)






"William M. Klein" <wmklein@nospam.netcom.com>
> You still haven't answered my questions.  I don't want to know how you 
> have defined the file in your program.  I want to know how the file 
…[123 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol problem (INPUT File Format)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-09T10:52:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EXlOd.1582995$f47.272202@news.easynews.com>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg> <as7Od.1491709$f47.254857@news.easynews.com> <cucldg$9jd$1@mawar.singnet.com.sg>`

```
Rick,
   PLEASE - answer my question.

You have now told us (for the first time) that the input is a VSAM KSDS file 
(which to non-IBM people is an INDEXED file).

In this same note you say

   "VSAM KSDS - VARIABLE
 RECORD SIZE   : 700 - 1527 BYTES"

    and

 "Basically, all records are the same length"

***

If you do an IDCAMS LISTCAT ALL on the file, then

If AVGLRECL equals MAXLRECL
    the PHYSICAL KSDS file is "fixed length"

If AVGLRECL does NOT equals MAXLRECL
  then the PHYSICAL KSDS file is VARIABLE

If the former, then define (in the FD) the file with
    RECORD CONTAINS "MAXLRECL"

If the latter, then define (in the FD) the file with

  Record VARYING IN SIZE from 700 to "MAXLRECL" size
          Depending ON WS-item


Do *not* use the
    "RECORD CONTAINS  n TO nn" clause for a variable length KSDS file - unless 
you have some other way of determining what size record you have.

***

Once again, until/unless you get your Select/Assign and FD definitions correct 
(matching the ACTUAL physical file layout) you simply will NOT get your READs to 
work correctly.
```

###### ↳ ↳ ↳ Re: Cobol problem (INPUT File Format)

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-09T17:05:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zprOd.342085$Xk.199437@pd7tw3no>`
- **In-Reply-To:** `<cucldg$9jd$1@mawar.singnet.com.sg>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg> <as7Od.1491709$f47.254857@news.easynews.com> <cucldg$9jd$1@mawar.singnet.com.sg>`

```
Rick wrote:
> Info as below for
> 
…[18 more quoted lines elided]…
> 
Well at least we know you are working on a mainframe. The above phrase 
just DOESN'T JIVE. There are 'no basicallys' in programming, either true 
or false. Either your have FIXED or you have VARIABLE records.

As you are working at a mainframe site ASK ONE  OF YOUR PEERS, as 
somebody else recently suggested. If you are afraid to admit you don't 
know, then eventually you will finish up in the doggy doo, and your 
career will go down the tubes. Try and pick a fellow worker with a 
sympathetic ear - we all learn from one another. And no matter how many 
decades we have been at the 'game', we all had to go through a learning 
cycle - and can still learn new things !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Cobol problem (INPUT File Format)

_(reply depth: 5)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-02-13T10:33:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108319612.303590.96380@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<zprOd.342085$Xk.199437@pd7tw3no>`
- **References:** `<ctt9c1$jfv$1@mawar.singnet.com.sg> <cuagbc$7j0$1@mawar.singnet.com.sg> <as7Od.1491709$f47.254857@news.easynews.com> <cucldg$9jd$1@mawar.singnet.com.sg> <zprOd.342085$Xk.199437@pd7tw3no>`

```
Hi Rick,

You say you can't change the copybook to get rid of the 01 level
redefines.  What is your compiler saying about your putting it in the
FD?

Although this doesn't appear to be the biggest problem you face you can
work around it by placing the copybook in WS and use the READ INTO
option.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
