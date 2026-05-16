[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# request for some help in testing specific code

_37 messages · 17 participants · 2008-02_

---

### request for some help in testing specific code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-21T23:15:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
to CLC
 I would like to know what as many compilers as possible do with some specific
syntax.  (My guess is that many - possibly MOST, maybe all) disallow it, but I
am curious.   I do NOT need/want this actually run, I just want to know what
compilers do with it. (You can use whatever settings you want, but I want to
know about any compiler informational, warning, or error messages.) Other than
the commented out "record varying in size" line, I think that this should
compile the same with any '74 or later compiler.  As I say, I *expect* compiler
messages (on the WRITE and READ statements), but I want to know:

A) does any compiler compile this cleanly?
 B) if not do you get messages on both the WRITE and the READ
 C) what messages do you get

Hopefully, I can get some "mainframe" (IBM and non-IBM) as well as PC/Unix/Linux
results.

       IDENTIFICATION DIVISION.
        PROGRAM-ID. TEST1.
       ENVIRONMENT DIVISION.
        INPUT-OUTPUT SECTION.
         FILE-CONTROL.
           SELECT AFILE ASSIGN TO SOMEFILE.
       DATA DIVISION.
        FILE SECTION.
       FD AFILE
      *     REMOVE ASTERISK FROM FOLLOWING LINE UNLESS USING 74 STANDARD
COMPILER
      *    RECORD VARYING IN SIZE FROM 10 TO 100
             .
       01  SMALL-REC   PIC X(10).
       01  LARGE-REC.
           05  FILLER  PIC X(90).
           05  LAST-PART  PIC X(10).
       PROCEDURE DIVISION.
        MAINLINE.
           OPEN OUTPUT AFILE
           MOVE ALL "X" TO LAST-PART
           WRITE SMALL-REC FROM LAST-PART
           CLOSE AFILE
      *
           OPEN INPUT AFILE
           READ AFILE INTO LAST-PART
           CLOSE AFILE
            .
      *
           STOP RUN.

* * *

Thanks in advance for your help on this.
```

#### ↳ Re: request for some help in testing specific code

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-21T22:08:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jisr3hnrpf6ldjel56rbs0thmm8umuvja@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
On Thu, 21 Feb 2008 23:15:05 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>to CLC
> I would like to know what as many compilers as possible do with some specific
…[10 more quoted lines elided]…
> C) what messages do you get

Fujitsu says:

'LAST-PART' OF 'FROM' PHRASE AND RECORD-NAME 'SMALL-REC' CANNOT OCCUPY THE SAME STORAGE
SPACE.

 'LAST-PART' OF INTO PHRASE AND RECORD AREA CANNOT OCCUPY THE SAME STORAGE SPACE.
```

#### ↳ Re: request for some help in testing specific code

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-02-21T21:42:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1203654815_147@isp.n>`
- **In-Reply-To:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
William M. Klein wrote:
> to CLC
>  I would like to know what as many compilers as possible do with some specific
…[49 more quoted lines elided]…
> 

A - Not mine 8-)  see below
B -  No
C - see below:

Jeff

--------------------------------------

    Welcome to OpenVMS (TM) Alpha Operating System, Version V7.3-1 on node AS600

TEST1                           Source Listing                  21-FEB-2008 20:54:21
   Compaq COBOL V2.8-1286            Page 1

               1 IDENTIFICATION DIVISION.
               2 PROGRAM-ID. TEST1.
               3 ENVIRONMENT DIVISION.
               4 INPUT-OUTPUT SECTION.
               5 FILE-CONTROL.
               6     SELECT AFILE ASSIGN TO SOMEFILE.
                 ...........1
%COBOL-F-REANOLCLH, (1) INVALID KEY clause, AT END clause, or USE procedure
required for READ on file

               7 DATA DIVISION.
               8 FILE SECTION.
               9     FD AFILE
              10 *    REMOVE ASTERISK FROM FOLLOWING LINE UNLESS USING 74
STANDARD COMPILER
              11         RECORD VARYING IN SIZE FROM 10 TO 100
              12     .
              13 01  SMALL-REC   PIC X(10).
              14 01  LARGE-REC.
              15     05  FILLER  PIC X(90).
              16     05  LAST-PART  PIC X(10).
              17 *
              18 PROCEDURE DIVISION.
              19 MAINLINE.
              20     OPEN OUTPUT AFILE
              21     MOVE ALL "X" TO LAST-PART
              22     WRITE SMALL-REC FROM LAST-PART
              23     CLOSE AFILE
              24 *
              25     OPEN INPUT AFILE
              26     READ AFILE INTO LAST-PART
                 ....................1
%COBOL-E-NOVERLAP, (1) Operand must not share storage with record area -
reference allowed

              27     CLOSE AFILE
              28     .
              29 *
              30     STOP RUN
              31     .
```

#### ↳ Re: request for some help in testing specific code

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2008-02-22T10:00:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
On Thu, 21 Feb 2008 23:15:05 GMT "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

:>to CLC
:> I would like to know what as many compilers as possible do with some specific
:>syntax.  (My guess is that many - possibly MOST, maybe all) disallow it, but I
:>am curious.   I do NOT need/want this actually run, I just want to know what
:>compilers do with it. (You can use whatever settings you want, but I want to
:>know about any compiler informational, warning, or error messages.) Other than
:>the commented out "record varying in size" line, I think that this should
:>compile the same with any '74 or later compiler.  As I say, I *expect* compiler
:>messages (on the WRITE and READ statements), but I want to know:

:>A) does any compiler compile this cleanly?
:> B) if not do you get messages on both the WRITE and the READ
:> C) what messages do you get

:>Hopefully, I can get some "mainframe" (IBM and non-IBM) as well as PC/Unix/Linux
:>results.

:>       IDENTIFICATION DIVISION.
:>        PROGRAM-ID. TEST1.
:>       ENVIRONMENT DIVISION.
:>        INPUT-OUTPUT SECTION.
:>         FILE-CONTROL.
:>           SELECT AFILE ASSIGN TO SOMEFILE.
:>       DATA DIVISION.
:>        FILE SECTION.
:>       FD AFILE
:>      *     REMOVE ASTERISK FROM FOLLOWING LINE UNLESS USING 74 STANDARD
:>COMPILER
:>      *    RECORD VARYING IN SIZE FROM 10 TO 100
:>             .
:>       01  SMALL-REC   PIC X(10).
:>       01  LARGE-REC.
:>           05  FILLER  PIC X(90).
:>           05  LAST-PART  PIC X(10).
:>       PROCEDURE DIVISION.
:>        MAINLINE.
:>           OPEN OUTPUT AFILE
:>           MOVE ALL "X" TO LAST-PART
:>           WRITE SMALL-REC FROM LAST-PART
:>           CLOSE AFILE
:>      *
:>           OPEN INPUT AFILE
:>           READ AFILE INTO LAST-PART
:>           CLOSE AFILE
:>            .
:>      *
:>           STOP RUN.

Is there any COBOL compiler that violates the standards and allows the record
area and the INTO/FROM area to overlap?
```

##### ↳ ↳ Re: request for some help in testing specific code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-22T13:48:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<moAvj.239845$9w2.140479@fe12.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com>`

```
There is a GREAT deal of question (at the moment) about exactly what is and is 
not prohibited ('85 or '02) Standards.

As already reported here, at least one compiler (OpenVMS) allows the WRITE FROM 
case.  It should be noted that although the "FROM" identifier in the write is 
within the "record area" - it is also true that it does NOT share any actual 
storage with the specific record being written.

So fat (off list) I have also received a note about one compiler that allows 
BOTH the read and WRITE statements.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-22T08:42:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com>`

```
On Fri, 22 Feb 2008 13:48:03 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>There is a GREAT deal of question (at the moment) about exactly what is and is 
>not prohibited ('85 or '02) Standards.
…[7 more quoted lines elided]…
>BOTH the read and WRITE statements.

The Standards are making are making an assumption that the record area is a pointer into a
buffer, it's not locally allocated like working-storage. That was true in the Good Old
Days, especially on IBM mainframe. It caused bugs when programs tried to reference an
output record after it had been written. For this reason, many shops adopted a house
standard that reads were always INTO and writes always FROM working-storage.

Reading INTO an area beyond the record would definitely be a bug, because you'd be
stepping on the next record. Writing FROM an area beyond the current record would not
cause an error. 

Does any modern compiler still work that way?  I doubt it
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-22T18:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45Evj.264615$ST4.65010@fe07.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com>`

```
Robert,
  Where does the Standard ('85 or '02 - ir any other) say something that 
"assumes" the use of a "buffer" for the record area?  What rule or rules? what 
definitions?

It does work for such implementations (which I think include most of the 
existing mainframe - IBM and otherwise - compilers), but I don't see anything 
that even vaguely hints at this as an assumption.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-22T20:59:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com>`

```
On Fri, 22 Feb 2008 18:00:34 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Robert,
>  Where does the Standard ('85 or '02 - ir any other) say something that 
>"assumes" the use of a "buffer" for the record area?  What rule or rules? what 
>definitions?

Why did the question come up? It is legal to read into and write from working-storage.
There must be something in the Standards that distinguishes record areas from
working-storage.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-23T07:07:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aDPvj.250853$m_6.25683@fe01.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com>`

```
No, the relevant restriction (that isn't very clear) in the Standard has to do 
with "overlapping storage".  So if the Read/Write is done against the record 
area, then the question is what (if any) parts of the record area can be used in 
the FROM/INTO identifiers.   Nothing to do with "buffers".

FYI,
  There is "sort-of" a related issue the Standard that is NOT very commonly 
implemented today and that is the CLOCK CONTAINS information.  Other than (some) 
mainframe environments, the use of "blocking" (in the COBOL sense) is not very 
common today - but even this has little or nothing directly to do with the 
"buffer" concept that you mentioned.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-23T18:32:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com>`

```
On Sat, 23 Feb 2008 07:07:50 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>No, the relevant restriction (that isn't very clear) in the Standard has to do 
>with "overlapping storage".  So if the Read/Write is done against the record 
>area, then the question is what (if any) parts of the record area can be used in 
>the FROM/INTO identifiers.   Nothing to do with "buffers".

I changed WRITE FROM into MOVE followed by WRITE, and READ INTO to READ followed by MOVE. 
Functionally it's the same, but the Fujitsu compiler that formerly complained about
overlapping FROM and INTO, stopped complaining when I wrote the MOVEs explicitly. 

           OPEN OUTPUT AFILE
           MOVE ALL "X" TO LAST-PART
           MOVE LAST-PART TO SMALL-REC
           WRITE SMALL-REC
           CLOSE AFILE
      *
           OPEN INPUT AFILE
           READ AFILE
           MOVE SMALL-REC TO LAST-PART
           CLOSE AFILE.

>FYI,
>  There is "sort-of" a related issue the Standard that is NOT very commonly 
…[3 more quoted lines elided]…
>"buffer" concept that you mentioned.

Blocking has been replaced by cacheing in the operating system or disk controller. Iinput
files smaller than say 4M  are usually read into memory when opened.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-24T05:22:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ca7wj.270012$Ib6.221580@fe03.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com...
> On Sat, 23 Feb 2008 07:07:50 GMT, "William M. Klein" 
> <wmklein@nospam.netcom.com> wrote:
<snip>
> Blocking has been replaced by cacheing in the operating system or disk 
> controller. Iinput
> files smaller than say 4M  are usually read into memory when opened.

OK, Robert - for which mainframe-SPECIFIC operating systems is this true? (and 
for which is it false?)

NOTE: "Linux" running on a mainframe, is NOT a "mainframe specific" operating 
system.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-24T00:09:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fk12s3h2qm3ukpe3b5361fgkrk5tjnqpr9@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <Ca7wj.270012$Ib6.221580@fe03.news.easynews.com>`

```
On Sun, 24 Feb 2008 05:22:42 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com...
…[11 more quoted lines elided]…
>system.

I didn't say anything about mainframe. I was talking about widely used operating systems. 

The machines I work on have one terrabyte of real memory. There's no way to fill it with
programs. The memory is used to cache files and databases.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-24T16:27:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XVgwj.351071$KG4.7128@fe09.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <Ca7wj.270012$Ib6.221580@fe03.news.easynews.com> <fk12s3h2qm3ukpe3b5361fgkrk5tjnqpr9@4ax.com>`

```
O<,  did you mean
  "SOME widely used operating systems"
        or
 do you think that mainframe-specific operating systems aren't widely used

   ***

This may just be your inability (as often discussed in the forum before) of 
distinguishing general statements that you write as if they were universal, from 
general statements that you INTEND to apply so some - (possibly many) but not 
universal (or even necessarily the majority) of cases.

I would certainly agree that there are MANY current "widely used operating 
system" that don't use any type of "buffering" for file I/O (and of course, the 
current COBOL Standard works "just fine" for them.)

This, however, is no more interesting (to me) than stating

 "Many widely used operating systems use 8-bit Ascii - and the current COBOL 
Standard supports this"
    or
"many widely used operating systems are based on a 16-bit "mode" and the current 
COBOL Standard works just fine in such environments, just as it does in 8-bit 
and 64-bit environments - which are also widely used operating systems.)
     or (even more extreme)
"Many widely used operating systems have built-in or add-on features for GUI 
user interfaces, and the current COBOL Standard allows this - but provides no 
specific support for it"
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-24T12:36:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2tc3s3p0reat7ckv699me6a4l11p4mr899@4ax.com>`
- **References:** `<j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <Ca7wj.270012$Ib6.221580@fe03.news.easynews.com> <fk12s3h2qm3ukpe3b5361fgkrk5tjnqpr9@4ax.com> <XVgwj.351071$KG4.7128@fe09.news.easynews.com>`

```
On Sun, 24 Feb 2008 16:27:36 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>O<,  did you mean
>  "SOME widely used operating systems"
>        or
> do you think that mainframe-specific operating systems aren't widely used

"There are now only about 10,000 mainframes left in
the world.

Actually, there have never been more, yet thatï¿½s been a
large enough number to be the computing cornerstone
of the world economy. But, as the total power of the
mainframes supporting the largest organizations on earth
increases, their number is slowly decreasing."
http://ca.com/files/WhitePapers/strat_vend_con_fut_mf_wp_un_es.pdf

" November 1, 2005

The total number of servers installed globally can be estimated based on some insider
market statistics. The values can be compared against IDC Market Research Information,
however the comparison fails by a factor of two because of a significant use of computers
that are sold as workstations that are actually used as servers in the <20 and 20-99
employee market segments (see Table 5). When the estimated use of workstations that
function as servers is removed, the installed server base compares favorably with the IDC
estimate of 21 million machines sold as servers"
http://www.linuxplanet.com/linuxplanet/reviews/6062/4/

100 * 10K / 20M = .05% of back-end machines are mainframes.

>This may just be your inability (as often discussed in the forum before) of 
>distinguishing general statements that you write as if they were universal, from 
>general statements that you INTEND to apply so some - (possibly many) but not 
>universal (or even necessarily the majority) of cases.

I was referring to 99.95% of cases, excluding desktop machines.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-24T20:16:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ugkwj.358349$X56.80042@fe06.news.easynews.com>`
- **References:** `<j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <Ca7wj.270012$Ib6.221580@fe03.news.easynews.com> <fk12s3h2qm3ukpe3b5361fgkrk5tjnqpr9@4ax.com> <XVgwj.351071$KG4.7128@fe09.news.easynews.com> <2tc3s3p0reat7ckv699me6a4l11p4mr899@4ax.com>`

```
Robert,
  I just have to ask if you think you have ANY credibility when you post things 
like this.

Counting the number of "machines" that are mainframes and/or counting 
"servicers" must be useful to your own sense of worth - but its relevance to 
limiting what is - and is not - "widely used operating systems" is so minimal 
that you simply are making a fool of yourself.

As usual, you simply won't admit your errors.  If you were just willing to admit 
that what you MEANT was "SOME widely used operating systems" the whole thing 
could be dropped.  However, you just can't admit your error and move on.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-24T05:24:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oc7wj.317704$rl3.34741@fe02.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com>`

```
Gee, do you think the difference between
  WRITE ... FROM
      and
  MOVE ..
  WRITE

MAY have something to do with the fact that the Standard specifically has a rule 
that talks about the WRITE FROM identifier and not the same rule about more, 
then write.  This still isn't a "buffer" issue, it is simply that the Standard 
has rules for specific statements and phrases.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-23T23:51:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d512s3dn4t1jpinig0tobd5clud13r00hd@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <oc7wj.317704$rl3.34741@fe02.news.easynews.com>`

```
On Sun, 24 Feb 2008 05:24:36 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Gee, do you think the difference between
>  WRITE ... FROM
…[7 more quoted lines elided]…
>has rules for specific statements and phrases.

MOVE followed by WRITE is the same as WRITE FROM. If the Standard and Fujitsu think
they're different then the Standard and Fujitsu are simply wrong. 

>Bill Klein
> wmklein <at> ix.netcom.com
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 10)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2008-02-24T10:09:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vc92s31dnrc4n50qgo4pg83tvj45lgtpql@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <oc7wj.317704$rl3.34741@fe02.news.easynews.com> <d512s3dn4t1jpinig0tobd5clud13r00hd@4ax.com>`

```
On Sat, 23 Feb 2008 23:51:30 -0600 Robert <no@e.mail> wrote:

:>On Sun, 24 Feb 2008 05:24:36 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

:>>Gee, do you think the difference between
:>>  WRITE ... FROM
:>>      and
:>>  MOVE ..
:>>  WRITE

:>>MAY have something to do with the fact that the Standard specifically has a rule 
:>>that talks about the WRITE FROM identifier and not the same rule about more, 
:>>then write.  This still isn't a "buffer" issue, it is simply that the Standard 
:>>has rules for specific statements and phrases.

:>MOVE followed by WRITE is the same as WRITE FROM. If the Standard and Fujitsu think
:>they're different then the Standard and Fujitsu are simply wrong. 

The standard does not allow the WRITE FROM in that way. 

There is no rule regarding the MOVE.

Similarly, one can redefine an alphabetic field as numeric and use it in an
arithmetic instruction, even though one cannot use the alphabetic item in that
way.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 11)_

- **From:** sro0220@gmail.com
- **Date:** 2008-02-24T08:41:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d2c4f352-5565-467d-a2d3-794220fbee3a@m23g2000hsc.googlegroups.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <oc7wj.317704$rl3.34741@fe02.news.easynews.com> <d512s3dn4t1jpinig0tobd5clud13r00hd@4ax.com> <vc92s31dnrc4n50qgo4pg83tvj45lgtpql@4ax.com>`

```
On Feb 24, 2:09 am, Binyamin Dissen <postin...@dissensoftware.com>
wrote:
> On Sat, 23 Feb 2008 23:51:30 -0600 Robert <n...@e.mail> wrote:
>
…[33 more quoted lines elided]…
> especially those from irresponsible companies.

Unisys OS2200 cobol '85 gave these errors:
*ERROR(MAJOR) UCOB2244: 'LAST-PART' illegal FROM/INTO identifier -
statement ignored
 
v
31             1                   WRITE SMALL-REC FROM LAST-
PART.
32             1                   CLOSE
AFILE.
33
*
34             1                   OPEN INPUT
AFILE.

*ERROR(MINOR) UCOB2276: AT END/INVALID KEY phrase is required for this
statement ignored
 
v
*ERROR(MAJOR) UCOB2244: 'LAST-PART' illegal FROM/INTO identifier -
statement ignored
 
v
35             1                   READ AFILE INTO LAST-
PART.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-24T16:18:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DNgwj.116876$DH7.96708@fe11.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <84ntr3hpljm5gmpnses17gg27o3cnu1r3h@4ax.com> <45Evj.264615$ST4.65010@fe07.news.easynews.com> <jm2vr3hahsf6iajkaa7g4nr7vp7pvo2h6s@4ax.com> <aDPvj.250853$m_6.25683@fe01.news.easynews.com> <v8c1s39o0ohev13raokpdg8utarggtln68@4ax.com> <oc7wj.317704$rl3.34741@fe02.news.easynews.com> <d512s3dn4t1jpinig0tobd5clud13r00hd@4ax.com>`

```
Nice to know tht you know how COBOL *should* be defined.  Just so you DO know 
what the Standard actually does say (and what the rlevant rule is).  It is in 
the '02 Standard as:
  WRITE Statement, Syntax Rule 4 (in part)
   "Record-name-1 and identifier-1 shall not reference the same storage area"

and the "storage area" for record-name-1 is the "record area" for the file.

FYI,
  Currently this is a SYNTAX rule - while all references to "like a move 
followed by a write" are in General Rules. If you huderstaand how the current 
(all all past) COBOL Standards work, then you would understand taht syntax rules 
can prohibt PARTS of things that could (otherwise) be handled by general rules. 
That is simply the way the Standard works.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

- **From:** sgbojo@gmail.com
- **Date:** 2008-02-22T06:45:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0dbedf6f-4fed-4f8a-995c-7f7116f1c87b@i7g2000prf.googlegroups.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com>`

```
This code compiles cleanly with the current version of Net Express and
ACUCOBOL-GT.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-22T19:19:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2fFvj.109765$DH7.99703@fe11.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <moAvj.239845$9w2.140479@fe12.news.easynews.com> <0dbedf6f-4fed-4f8a-995c-7f7116f1c87b@i7g2000prf.googlegroups.com>`

```
Well, my tests with NetExpress indicate that it depends on your definition of 
"cleanly".  If you compile with WARNING(3), I think you will see a message on 
the READ, but not on the WRITE.
```

##### ↳ ↳ Re: request for some help in testing specific code

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-02-22T14:06:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QFAvj.12695$R84.5294@newssvr25.news.prodigy.net>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com>`

```
> Is there any COBOL compiler that violates the standards and allows the 
> record
> area and the INTO/FROM area to overlap?

Use SAME RECORD AREA clause in SELECT?  (It's been a while so that might be 
wrong but it's Friday so I get one guess without RTFM).

???

MCM
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-22T08:44:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rqntr3lh3rrv3dnv3g8jcrengo9bchao02@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <j10tr35q2tcs1tqhcar634mgfnrfvqbd8p@4ax.com> <QFAvj.12695$R84.5294@newssvr25.news.prodigy.net>`

```
On Fri, 22 Feb 2008 14:06:40 GMT, "Michael Mattias" <mmattias@talsystems.com> wrote:

>> Is there any COBOL compiler that violates the standards and allows the 
>> record
…[3 more quoted lines elided]…
>wrong but it's Friday so I get one guess without RTFM).

SAME RECORD AREA is for sharing memory between two files. Two records in the same file are
implicitly the same area.
```

#### ↳ Re: request for some help in testing specific code

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-02-22T16:06:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47BEF2FC.6F0F.0085.0@efirstbank.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
>>> On 2/21/2008 at 4:15 PM, in message
<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
> to CLC
>  I would like to know what as many compilers as possible do with some 
…[56 more quoted lines elided]…
> Thanks in advance for your help on this.

COBOL for VSE/ESA compiles with no warnings at all.
Well, none related to the issue in question.  I do get one still warning:
A "RECORDING MODE" OF "V" WAS ASSUMED FOR FILE "AFILE".
But that can be eliminated by changing the select to treat the file as VSAM
sequential instead of regular sequential (using the AS- prefix).

Frank
```

#### ↳ Re: request for some help in testing specific code

- **From:** Cathy Sullivan <cesulliv@cac.washington.edu>
- **Date:** 2008-02-22T16:48:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fpnqhm$l0t$1@gnus01.u.washington.edu>`
- **In-Reply-To:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
On a Unisys A-Series Cobol 85 compiler,


* 006000     SELECT AFILE ASSIGN TO SOMEFILE.
                                     1
    1) ERROR:  896 : SYNTAX ERROR; SYMBOL RESPELLED TO BE -----> SORT ***
* 026000           READ AFILE INTO LAST-PART
                                    1
    1) WARNING:  605 : THE LENGTH OF THE SENDING ITEM IS GREATER THAN 
THE LENGTH
             OF THE RECEIVING ITEM. ALL EXCESS DATA WILL BE TRUNCATED 
AFTER THE
             RECEIVING ITEM HAS BEEN FILLED.
   Compile Failed



When I change 'SOMEFILE' to 'DISK', that error goes away and the warning 
is left:

* 026000           READ AFILE INTO LAST-PART
                                    1
    1) WARNING:  605 : THE LENGTH OF THE SENDING ITEM IS GREATER THAN 
THE LENGTH
             OF THE RECEIVING ITEM. ALL EXCESS DATA WILL BE TRUNCATED 
AFTER THE
             RECEIVING ITEM HAS BEEN FILLED.
   Compile Succeeded
   Temporary object CANDE/NXEDIT/CODE576231 created


I had to change 'CLOSE AFILE' to 'CLOSE AFILE WITH SAVE'

It created a file with one 100 character record with 10 X's at the 
beginning and 10 X's at the end.







On 2/21/2008 3:15 PM, William M. Klein wrote:
> to CLC
>  I would like to know what as many compilers as possible do with some specific
…[49 more quoted lines elided]…
>
```

#### ↳ Re: request for some help in testing specific code

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2008-02-23T02:04:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ggvur31gpud77fk4ro04n4cnfscdputrsb@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
On Thu, 21 Feb 2008 23:15:05 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>to CLC
> I would like to know what as many compilers as possible do with some specific
…[48 more quoted lines elided]…
>Thanks in advance for your help on this.
With a MINOR change.
SELECT AFILE ASSIGN TO DISK SOMEFILE.

and
Working-storage section
 01  SOMEFILE PIC X(10).

It compiles fine with RM/COBOL 5.35 (85 compliant)


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: request for some help in testing specific code

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-22T21:03:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<553vr3d4inp7f9rmpvagrrrjmfvfhdsvek@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
On Thu, 21 Feb 2008 23:15:05 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>to CLC
> I would like to know what as many compilers as possible do with some specific
>syntax.  (My guess is that many - possibly MOST, maybe all) disallow it, but I
>am curious. 

Micro Focus Server Express V4.0 gives no error or warning.
```

#### ↳ Re: request for some help in testing specific code

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-02-23T08:42:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10Rvj.249284$MJ6.181378@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
William M. Klein wrote:
> to CLC
>  I would like to know what as many compilers as possible do with some specific
…[11 more quoted lines elided]…
> (snip) 

PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1
Invocation parameters:
XREF(FULL),NORENT,X(FULL)
Options in effect:
     NOADATA
       ADV
       APOST
       ARITH(EXTEND)
       AWO
       BUFSIZE(27998)
     NOCICS
       CODEPAGE(1140)
     NOCOMPILE(E)
     NOCURRENCY
       DATA(31)
     NODATEPROC
     NODBCS
     NODECK
       DIAGTRUNC
     NODLL
     NODUMP
       DYNAM
     NOEXIT
     NOEXPORTALL
       FASTSRT
       FLAG(I,W)
     NOFLAGSTD
       INTDATE(LILIAN)
       LANGUAGE(EN)
       LIB
       LINECOUNT(60)
     NOLIST
       MAP
     NOMDECK
     NONAME
       NSYMBOL(DBCS)
     NONUMBER
       NUMPROC(NOPFD)
       OBJECT
       OFFSET
       OPTIMIZE(FULL)
       OUTDD(SYSOUT)
       PGMNAME(COMPAT)
     NORENT
       RMODE(ANY)
     NOSEQUENCE
       SIZE(MAX)
       SOURCE
       SPACE(1)
     NOSQL
       SQLCCSID
     NOSSRANGE
       TERM
     NOTEST
     NOTHREAD
       TRUNC(OPT)
     NOVBREF
     NOWORD

----+-*A-1-B--+----2----+----3----+----4----+----5----+----6---
        IDENTIFICATION DIVISION.
         PROGRAM-ID. TEST1.
        ENVIRONMENT DIVISION.
         INPUT-OUTPUT SECTION.
          FILE-CONTROL.
            SELECT AFILE ASSIGN TO SOMEFILE.
        DATA DIVISION.
         FILE SECTION.
        FD AFILE
       *     REMOVE ASTERISK FROM FOLLOWING LINE UNLESS USING
       *     1974 STANDARD COMPILER
       *    RECORD VARYING IN SIZE FROM 10 TO 100
              .
        01  SMALL-REC   PIC X(10).
        01  LARGE-REC.
            05  FILLER  PIC X(90).
            05  LAST-PART  PIC X(10).
        PROCEDURE DIVISION.
            OPEN OUTPUT AFILE
            MOVE ALL "X" TO LAST-PART
            WRITE SMALL-REC FROM LAST-PART
            CLOSE AFILE
       *
            OPEN INPUT AFILE
            READ AFILE INTO LAST-PART
            CLOSE AFILE
             .
       *
            STOP RUN.

IGYPA3043-E Data-item "LAST-PART (ALPHANUMERIC)" and record
"LARGE-REC (GROUP)" had overlapping storage.  Movement of data may
not occur at execution time.



Compile failed with RC=08, so no linkedit.

Sorry, I didn't save the line number where the error was detected.  Do 
you need that?

I believe it was on the "WRITE SMALL-REC FROM LAST-PART" line.

With kindest regards,
```

##### ↳ ↳ Re: request for some help in testing specific code

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-23T14:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ztWvj.340159$KG4.309496@fe09.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <10Rvj.249284$MJ6.181378@bgtnsc05-news.ops.worldnet.att.net>`

```
Was this against the Read, the Write - or both
```

#### ↳ Re: request for some help in testing specific code

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2008-02-26T05:41:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fq05a6$6hd$01$1@news.t-online.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```

"William M. Klein" scribeth
> to CLC
>  I would like to know what as many compilers as possible do with some
specific
> syntax.  (My guess is that many - possibly MOST, maybe all) disallow it,
but I
> am curious.   I do NOT need/want this actually run, I just want to know
what
> compilers do with it. (You can use whatever settings you want, but I want
to
> know about any compiler informational, warning, or error messages.) Other
than
> the commented out "record varying in size" line, I think that this should
> compile the same with any '74 or later compiler.  As I say, I *expect*
compiler
> messages (on the WRITE and READ statements), but I want to know:
>
…[4 more quoted lines elided]…
> Hopefully, I can get some "mainframe" (IBM and non-IBM) as well as
PC/Unix/Linux
> results.
>
…[34 more quoted lines elided]…
>


Compiles and runs fine with OpenCOBOL.
OC generates a MOVE/WRITE sequence for WRITE FROM and
a READ/MOVE sequence for READ INTO.

This would seem to be in accordance with 2002
standard.
eg. For WRITE, reference 14.8.47.3, (3)

Roger
```

#### ↳ Re: request for some help in testing specific code

- **From:** David Essex <nospam@nobloodyspam.nospam>
- **Date:** 2008-02-27T09:48:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
According to an old (COBOL-85) IBM language reference:

READ file-name-1 INTO identifier-1 ...
...
The record area associated with file-name-1 and identifier-1 must not be 
the same storage area.

One of the first things I learned when working with COBOL files, is to 
always move records in/from working-storage.
The reason for this practice, I was told, was to do with file buffers.
This problem was later resolved by the use of file 'double buffers'.

I don't know if this was ever part of any COBOL standard.
I suspect that file buffers may have been an issue when core memory was 
at premium.

If so, this is a legacy issue and may explain the different compiler 
behaviour.


David Essex
```

##### ↳ ↳ Re: request for some help in testing specific code

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-27T15:48:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fq40nq$q1f$1@reader2.panix.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA>`

```
In article <5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA>,
David Essex  <nospam@nobloodyspam.nospam> wrote:

[snip]

>One of the first things I learned when working with COBOL files, is to 
>always move records in/from working-storage.
>The reason for this practice, I was told, was to do with file buffers.
>This problem was later resolved by the use of file 'double buffers'.

Hmmmmm... let me see... ahhhh, there it is.  Back in ought-four I started 
a thread with a posting that contained:

(from 
<http://groups.google.com/group/comp.lang.cobol/msg/fee1c188d1805333?dmode=source>)

--begin quoted text:

This, of course, is what was taught to me lo, those many decades back; the 
specific of 'Thou shalt not perform arithmetic manipulations in file 
buffers' was expanded into the zero-tolerance rule of 'Thou shalt not 
touch file buffers; all will be done in WORKING-STORAGE via READ INTO and 
WRITE FROM.'

[snip]

Does anyone know of harm/damage/bad stuff (outside of that which can be 
chalked up to sloppiness, e.g. changing a key's position/length and not 
updating the WORKING-STORAGE layout to match) which might happen due to 
continuing to adhere to this?

--end quoted text

... and as far as I can tell nobody's mind was changed about anything.

DD
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-02-27T12:18:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<21212d21-ec88-4781-a62d-881f673011d1@34g2000hsz.googlegroups.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA> <fq40nq$q1f$1@reader2.panix.com>`

```
On 27 Feb, 15:48, docdw...@panix.com () wrote:
> In article <5c26d$47c5786c$cf701d9b$13...@PRIMUS.CA>,
> David Essex  <nos...@nobloodyspam.nospam> wrote:
…[33 more quoted lines elided]…
> DD

Slightly off topic: yes, but only when using blocks/buffers in
Assembler. In an application that I maintained the first record of
each block was always the same library record and the one that should
have been there was never physically written.

Cobol would never have done that.

I believe that the real reason for writing from/reading into working
storage is the laziness of some programmers who don't like calculating
displacements.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-02-27T14:05:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44kbs3taq2nakkp3ep7sspl2pprqc8qf9n@4ax.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA> <fq40nq$q1f$1@reader2.panix.com> <21212d21-ec88-4781-a62d-881f673011d1@34g2000hsz.googlegroups.com>`

```
On Wed, 27 Feb 2008 12:18:43 -0800 (PST), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>Slightly off topic: yes, but only when using blocks/buffers in
>Assembler. In an application that I maintained the first record of
…[7 more quoted lines elided]…
>displacements.

But not for CoBOL programmers.
```

###### ↳ ↳ ↳ Re: request for some help in testing specific code

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-27T23:05:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fq4qb9$fcv$1@reader2.panix.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com> <5c26d$47c5786c$cf701d9b$13876@PRIMUS.CA> <fq40nq$q1f$1@reader2.panix.com> <21212d21-ec88-4781-a62d-881f673011d1@34g2000hsz.googlegroups.com>`

```
In article <21212d21-ec88-4781-a62d-881f673011d1@34g2000hsz.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 27 Feb, 15:48, docdw...@panix.com () wrote:
>> In article <5c26d$47c5786c$cf701d9b$13...@PRIMUS.CA>,
…[32 more quoted lines elided]…
>> ... and as far as I can tell nobody's mind was changed about anything.

[snip]

>I believe that the real reason for writing from/reading into working
>storage is the laziness of some programmers who don't like calculating
>displacements.

I barely know mine own lazinesses, Mr Maclean, let alone those of 'some 
programmers'... but the [snip] part of what I quoted above just happens to 
be:

--begin quoted text:

A few years back... not too long ago, maybe 1988, 1989, I was called in to 
help a coder who was getting some whacky results... and sure enough, he 
was doing arithmetice manipulations on the FDand the numbers were coming 
out screwy. Granted, the platform was WANG VS... but the Ancient Teaching 
was proven right.

--end quoted text

... so there was, according to my memory - which is, admittedly, porous - 
a situation where it wasn't a matter of calculating displacements, it was 
a matter of arithmetic manipulations performed in a file buffer generating 
'some whacky results'.

DD
```

#### ↳ Re: request for some help in testing specific code

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2008-02-28T22:04:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47c77652$0$16686$4c368faf@roadrunner.com>`
- **In-Reply-To:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`
- **References:** `<ZBnvj.246728$ST4.136547@fe07.news.easynews.com>`

```
Here are test results for a Unisys OS2200 series system.

First, from the UCOB (COBOL 85) compiler:

*ERROR(MAJOR) UCOB2244: 'LAST-PART' illegal FROM/INTO identifier - statement 
ignored
                                                        v
21             1                   WRITE SMALL-REC FROM LAST-PART

*ERROR(MINOR) UCOB2276: AT END/INVALID KEY phrase is required for this 
statement - statement accepted
                                   v
*ERROR(MAJOR) UCOB2244: 'LAST-PART' illegal FROM/INTO identifier - statement 
ignored
                                                   v
25             1                   READ AFILE INTO LAST-PART


And then, from the ACOB (COBOL 74) compiler:

       22                  WRITE SMALL-REC FROM LAST-PART
                                                ^
 **  874 **    SEV. S      COL. 33            FROM/INTO IDENTIFIER INVALID
       26                  READ AFILE INTO LAST-PART
                                      ^
 **  848 **    SEV. W      COL. 23            SIZE OF FIRST RECORD USED FOR 
INTO CLAUSE
                                           ^
 **  874 **    SEV. S      COL. 28            FROM/INTO IDENTIFIER INVALID
                           ^
 **  706 **    SEV. S      COL. 12            (AT END/INVALID KEY) MISSING; 
STATEMENT OMITTED


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:ZBnvj.246728$ST4.136547@fe07.news.easynews.com...
> to CLC
> I would like to know what as many compilers as possible do with some 
…[61 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
