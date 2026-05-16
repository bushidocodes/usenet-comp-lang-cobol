[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol Sequential Files

_14 messages · 7 participants · 2003-04 → 2003-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### MicroFocus Cobol Sequential Files

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2003-04-25T20:32:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
Hi All,

Forgive me if this topic has been covered, but I'm new to the group and a
search on the subject has not been fruitful.

I have an application where I must create sequential files with variable
length records. This is easy, but the problem is that the end user (HIPAA)
cannot tolerate the CRLF record terminator at the end of each record.

Do any of you Guru's have a solution to write these records without the
CRLF?

Thanks in advance.

John
```

#### ↳ Re: MicroFocus Cobol Sequential Files

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-26T09:19:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8c8r8$rqq$1@aklobs.kc.net.nz>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
John Simpson wrote:

> I have an application where I must create sequential files with variable
> length records. This is easy, but the problem is that the end user (HIPAA)
…[3 more quoted lines elided]…
> CRLF?

Variable length records need to have a terminator of some sort to indicate 
the end of the record.  Either you are using another character to indicate 
end or are putting size counts at the start.

For example EDIFACT uses apostrophe as a segment terminator.

One way to do it is to use a single byte sized sequential file and write 
each byte.  This can be done in some low level routine that is passed each 
complete record.  It can be slow but is standard.

Some vendors offer CALLable routines to do this.  see your vendors user 
manual.
```

#### ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-25T22:02:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
"John Simpson" <jasimp@earthlink.net> wrote in message
news:YXgqa.1933$XE.48494@news1.east.cox.net...
> Hi All,
>
…[8 more quoted lines elided]…
> CRLF?

A. HIPAA is not a user
B. HIPAA specs say nothing about CRLF termination of anything.
C. Records in ORGANIZATION IS SEQUENTIAL files only end with CRLF or LF if
you put them there. (But records in ORGANIZATION IS LINE SEQUENTIAL files
will on PC (CRLF) or 'Nix (LF)).
D. Look up RECORD IS VARYING for the FD

If your user is on PC, there is no such thing as 'variable length records'
which are not terminated (delimited). I suspect what you are trying to do is
create ANSI ASC EDI and are trying to end each record with the segment
terminator character rather than CRLF.

Depending on what O/S you are on, what compiler you use, and maybe even what
software your user is using, this can be a hell of a trick using COBOL. One
way which works more or less 'universally'  is to create the file as
ORGANIZATION SEQUENTIAL with a fixed record size, then count the characters
in each record yourself, wrapping when necessary. When the file is saved to
disk, it will look like a 'continuous stream wrapped'  EDI file. I did this
for AllState Insurance about eight years ago.. real time creation of an ANSI
interchange in response to a CICS transaction. It took me more than an
afternoon. (A lot more!).

Expert EDI progamming assistance available at contact info below.
```

##### ↳ ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-25T20:53:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WdSdndjvV9ATezSjXTWJhQ@giganews.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net>

> > Hi All,
> >
> > Forgive me if this topic has been covered, but I'm new to the group and
a
> > search on the subject has not been fruitful.
> >
> > I have an application where I must create sequential files with variable
> > length records. This is easy, but the problem is that the end user
(HIPAA)
> > cannot tolerate the CRLF record terminator at the end of each record.
> >
…[11 more quoted lines elided]…
> which are not terminated (delimited). I suspect what you are trying to do
is
> create ANSI ASC EDI and are trying to end each record with the segment
> terminator character rather than CRLF.

Not so. In some incarnations of PC COBOL, variable length records do not
have terminators, CRLF or otherwise. These records do, however, have a
record predecessor - that is, some amount of bytes on the front of each
record containing the length of the following record.

LINE SEQUENTIAL records do have a CRLF terminator and often these records
are trailing-blank truncated. While these records are of variable lengths, I
don't think you should call them variable length records (even though they
are).
```

###### ↳ ↳ ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-26T14:42:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Vwqa.3702$%_3.2978000@newssrv26.news.prodigy.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com> <WdSdndjvV9ATezSjXTWJhQ@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:WdSdndjvV9ATezSjXTWJhQ@giganews.com...
>
> > If your user is on PC, there is no such thing as 'variable length
records'
> > which are not terminated (delimited). I suspect what you are trying to
do
> is
> > create ANSI ASC EDI and are trying to end each record with the segment
…[5 more quoted lines elided]…
> record containing the length of the following record.

That's why I said to some extent solving this challenge may depend on the
user's software: to interpret data arranged as suggested...

<length-word><data-of-length-length-word><length-word><data-of-length-length
-word><length-word><data-of-length-length-word>.....

.. the user's software must be ready to handle it. For example, Notepad will
not interpret the above correctly.

It would be best if OP  described exactly the format of the output data, and
on what O/S-compiler this output is to be created..then we could point in
the right direction. (I have thirty cents says what he wants is a stream of
data representing an ANSI ASC X12 interchange).

MCM
```

##### ↳ ↳ Re: MicroFocus Cobol Sequential Files

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-26T20:12:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eaae64d.178306662@news.optonline.net>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:

>A. HIPAA is not a user
>B. HIPAA specs say nothing about CRLF termination of anything.

Yes, they do. You can read about them here:

http://a257.g.akamaitech.net/7/257/2422/14mar20010800/edocket.access.gpo.gov/2003/03-3876.htm

http://aspe.hhs.gov/admnsimp/

A possible (but expensive) solution is here:

http://www.interfaceware.com/download.php?a=4
```

###### ↳ ↳ ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-27T00:47:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xMFqa.3854$%_3.3083513@newssrv26.news.prodigy.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com> <3eaae64d.178306662@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eaae64d.178306662@news.optonline.net...
> "Michael Mattias" <michael.mattias@gte.net> wrote:
>
…[4 more quoted lines elided]…
>
http://a257.g.akamaitech.net/7/257/2422/14mar20010800/edocket.access.gpo.gov
/2003/03-3876.htm

Said document contains no reference to record termination at all. All
standards are referred to official implementation guides at WPC site.

> http://aspe.hhs.gov/admnsimp/

Also says nothing about line termination. (But thanks for making me go back
to that site.. I had missed a couple of updates and was able to refresh my
personal library).

>
> A possible (but expensive) solution is here:
>
> http://www.interfaceware.com/download.php?a=4

A possible but not so expensive solution is here:
```

###### ↳ ↳ ↳ Re: MicroFocus Cobol Sequential Files

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-27T14:56:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eabd449.239240589@news.optonline.net>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com> <3eaae64d.178306662@news.optonline.net> <xMFqa.3854$%_3.3083513@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[14 more quoted lines elided]…
>> http://aspe.hhs.gov/admnsimp/

That's the same page I cited. 

>Also says nothing about line termination. (But thanks for making me go back
>to that site.. I had missed a couple of updates and was able to refresh my
>personal library).

Granted, the ANS X12 (EDI) standard is generalized. In practice, aren't messages
usually comma delimited ASCII terminated by cr-lf or nl? The ones I've seen have
been.
```

###### ↳ ↳ ↳ Re: MicroFocus Cobol Sequential Files

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-27T17:16:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgUqa.4025$%_3.3229368@newssrv26.news.prodigy.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com> <3eaae64d.178306662@news.optonline.net> <xMFqa.3854$%_3.3083513@newssrv26.news.prodigy.com> <3eabd449.239240589@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3eabd449.239240589@news.optonline.net...
>
> Granted, the ANS X12 (EDI) standard is generalized. In practice, aren't
messages
> usually comma delimited ASCII terminated by cr-lf or nl? The ones I've
seen have
> been.

Usually? No. Matter of fact I've never seen comma used as a control
character in ANSI ASC X12 and I've been working with the format for twenty
years (back to when WalMart used a proprietary 'flat' file rather than ANSI
ASC X12). The most common element separator is the asterisk. (No empirical
data, that's just gut feel).

'n/l'  is only a common "printed symbol for the segment terminator" and may
in fact represent different characters. The most common segment terminator
characters I've encountered are "@" , "~" and x'0A' (line feed).

MCM
```

###### ↳ ↳ ↳ Re: MicroFocus Cobol Sequential Files

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-28T01:26:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eac2d2f.262001840@news.optonline.net>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <Nfiqa.3518$%_3.2808196@newssrv26.news.prodigy.com> <3eaae64d.178306662@news.optonline.net> <xMFqa.3854$%_3.3083513@newssrv26.news.prodigy.com> <3eabd449.239240589@news.optonline.net> <cgUqa.4025$%_3.3229368@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eabd449.239240589@news.optonline.net...
…[15 more quoted lines elided]…
>characters I've encountered are "@" , "~" and x'0A' (line feed).

In Unix terminology, x'0A' is called New Line (nl). If Mr. Simpson is going to
send the file via FTP, the solution may be simple. FTP will convert the PC
record terminator 0D0A to the Unix terminator 0A.
```

#### ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "Paul Hoberg" <nospamphoberg@att.net>
- **Date:** 2003-04-26T19:08:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uOAqa.632544$L1.180396@sccrnsc02>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
Hey, John,
I have used Byte-stream files for years.  You can do anything you want - add
whatever number of bytes to the end of the file, read or rewrite anywhere in
the file, etc.  So build your own records, comprised of anything you need,
and use byte-stream to write them.  You just need to keep track of how long
the file is, so you can continue to append each record with your specified
length, then add that length to the current file size, to be ready for the
next record.  And, IT IS THE FASTEST FILE ACCESS I HAVE EVER USED IN
MICROFOCUS COBOL!  Maybe by an order of magnitude!
Good luck,
Paul

"John Simpson" <jasimp@earthlink.net> wrote in message
news:YXgqa.1933$XE.48494@news1.east.cox.net...

Hi All,

Forgive me if this topic has been covered, but I'm new to the group and a
search on the subject has not been fruitful.

I have an application where I must create sequential files with variable
length records. This is easy, but the problem is that the end user (HIPAA)
cannot tolerate the CRLF record terminator at the end of each record.

Do any of you Guru's have a solution to write these records without the
CRLF?

Thanks in advance.

John
```

##### ↳ ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "Paul Hoberg" <nospamphoberg@att.net>
- **Date:** 2003-04-28T23:12:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nzira.677929$S_4.726673@rwcrnsc53>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net> <uOAqa.632544$L1.180396@sccrnsc02>`

```
I didn't mention that NetExpress' help tells how to deal with byte-stream
files.  Here's what it says about byte-stream files, followed by a
description of one of the routines - how to read from the file:
------------------------------------------------------------------------
The byte-stream file routines enable you to read and write data files
without the need to adhere to COBOL record definitions.

CBL_CLOSE_FILE Close byte-stream file
CBL_CREATE_FILE Create byte-stream file
CBL_FLUSH_FILE Flush byte-stream file buffers to disk
CBL_FREE_RECORD_LOCK Release a record lock on a file
CBL_GET_RECORD_LOCK Release a record lock on a file
CBL_OPEN_FILE Open byte-stream file
CBL_READ_FILE Read byte-stream file
CBL_TEST_RECORD_LOCK Obtain a record lock on a file
CBL_WRITE_FILE Write byte-stream file

For all these routines, if the routine is successful the RETURN-CODE
register is set to zero. If the routine fails, the RETURN-CODE register
contains a file status value indicating the failure. This file status is
always the standard ANSI'74 file status value. If no ANSI'74 file status is
defined for the error, an extended file status is returned (9/
nnn where nnn is the run-time system error number).

For this to work you should use RETURN-CODE and not have a RETURNING clause.
If RETURN-CODE is nonzero after calling a byte-stream routine, move it to a
PIC XX COMP-X data item to process it as a file status. For example:

 01 file-stat      pic xx comp-x.

 01    redefines file-stat.
     03 fs-byte-1  pic x.
     03 fs-byte-2  pic x comp-x.
   . . .
     call "CBL_xxx_FILE" using <parameters>
     if return-code not = 0
        move return-code to file-stat
           . . .

At this point fs-byte-1 contains "9" and fs-byte-2 contains the run-time
system error number.

Copyright (C) 2000 MERANT International Ltd. All rights reserved.

------------------------------------------------------------------------

Read bytes from a file.

call "CBL_READ_FILE" using file-handle file-offset byte-count flags buffer

Parameters:

file-handle             pic x(4).

file-offset             pic x(8) comp-x.
byte-count           pic x(4) comp-x.
flags                    pic x comp-x.
buffer                  pic x(n).

On Entry:

file-handle The file handle returned when the file was opened.
file-offset The offset in the file at which to read. This field is currently
limited to a maximum value of x"00FFFFFFFF".
byte-count The number of bytes to read. This field is currently limited to a
maximum value of x"00FFFF".
flags This parameter can take the following values:
 0 Standard read
 128 Return the current file size in file-offset

On Exit:

file-offset Contains the current file size on return if flags is set to 128
on entry.

buffer The buffer into which the bytes are read. It is your responsibility
to ensure that the buffer is large enough to hold the number of bytes to be
read.

Comments:

The success of the call can be checked by examining RETURN-CODE.

When using this routine to read a file that is contained in a .lbr file, the
end-of-file status is not returned. To ensure you only read the file you
want, obtain the size of the file first (set flags to 128), and only read up
to that size.

------------------------------------------------------------------------

"Paul Hoberg" <nospamphoberg@att.net> wrote in message
news:uOAqa.632544$L1.180396@sccrnsc02...

Hey, John,
I have used Byte-stream files for years.  You can do anything you want - add
whatever number of bytes to the end of the file, read or rewrite anywhere in
the file, etc.  So build your own records, comprised of anything you need,
and use byte-stream to write them.  You just need to keep track of how long
the file is, so you can continue to append each record with your specified
length, then add that length to the current file size, to be ready for the
next record.  And, IT IS THE FASTEST FILE ACCESS I HAVE EVER USED IN
MICROFOCUS COBOL!  Maybe by an order of magnitude!
Good luck,
Paul

"John Simpson" <jasimp@earthlink.net> wrote in message
news:YXgqa.1933$XE.48494@news1.east.cox.net...

Hi All,

Forgive me if this topic has been covered, but I'm new to the group and a
search on the subject has not been fruitful.

I have an application where I must create sequential files with variable
length records. This is easy, but the problem is that the end user (HIPAA)
cannot tolerate the CRLF record terminator at the end of each record.

Do any of you Guru's have a solution to write these records without the
CRLF?

Thanks in advance.

John
```

#### ↳ Re: MicroFocus Cobol Sequential Files

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-27T23:54:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304272254.729f743c@posting.google.com>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
"John Simpson" <jasimp@earthlink.net> wrote

> Do any of you Guru's have a solution to write these records without the
> CRLF?

I don't think that you have been asked whether you mean 'without cr
and lf' or 'without cr or lf'.  Do you want it without any control
characters at all because the printable segment terminator character
is sufficient.

I have found that with EDIFACT messages some user want CRLF, some LF
only, some neither, just the segments.

Reading these EDIFACT messages I process the segments and ignore any
control characters.  For output I have a configuration item, per
destination user, for any control character requirements.
```

#### ↳ Re: MicroFocus Cobol Sequential Files

- **From:** "CJ Major" <cj.major@cox.net>
- **Date:** 2003-05-01T20:45:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wRlsa.492$4b3.58@fed1read06>`
- **References:** `<YXgqa.1933$XE.48494@news1.east.cox.net>`

```
HIPAA is the Health Insurance Portability and Accountability Act of 1996.

The act mandates that certain transactions in the health industry (mainly
in the claims and eligibility/enrollment arena) must be in very
specific versions of the X12N standards by October of this year.
(With rather draconian threats of fines if someone does not follow the
standards exactly).

I have written a cobol program to create an X12N 837 Professional.
The output file pass certification both with Claredi and HIPAA-Desk.

It is not pretty, but it does work well.  On a Sun 4800 server with MF
Cobol it processed 350,000 claims in about 15 minutes.  If anyone is
interested I can post the code that does the write of the transaction.

CJ Major
HIPAA TCS Project Lead
Arizona Dept of Health Services
Division of Behavioral Health Services



"John Simpson" <jasimp@earthlink.net> wrote in message
news:YXgqa.1933$XE.48494@news1.east.cox.net...
> Hi All,
>
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
