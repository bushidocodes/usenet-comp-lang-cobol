[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AIX Cobol II and Packed Decimal fields

_14 messages · 6 participants · 2005-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### AIX Cobol II and Packed Decimal fields

- **From:** "alf" <alf@itxpurts.com.au>
- **Date:** 2005-10-26T23:32:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com>`

```
We are doing a conversion from IBM mainframe to AIX. We are trying to
do a minimal approach due to cost (of course). The problem is we have
variable length files which have COMP-3 (packed decimal). We are NOT
using CICS and want just a regular UNIX type file. We have tried the
RSD format and the NAT format but cant quite get it to work... the
files we are processing are rather big and making them all fixed length
will chew a lot of disk space.

I know there is a problem using LINE SEQUENTIAL as the COMP fields
could be misconstrued to be record terminators.

Any help would be appreciated...
```

#### ↳ Re: AIX Cobol II and Packed Decimal fields

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-10-27T12:39:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gU38f.4507$Kv.3211@newssvr22.news.prodigy.net>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com>`

```
"alf" <alf@itxpurts.com.au> wrote in message
news:1130394756.656497.253930@g49g2000cwa.googlegroups.com...
> I know there is a problem using LINE SEQUENTIAL as the COMP fields
> could be misconstrued to be record terminators.

That's not a problem at all. It's an impossibility, so don't waste any
effort trying to make it 'work.'

> We have tried the RSD format and the NAT format

I never heard of those, but if they require the use of 0x0A (line feed) as
anything other than a record delimiter, they won't work, either.

"In theory" you might get away with ORGANIZATION IS LINE SEQUENTIAL,since
0x0A should never appear in USAGE PACKED-DECIMAL data (but *can* be valid in
USAGE BINARY data) , and it's 'unlikely'  0x0A is - in this particular
application - a valid data character in any USAGE DISPLAY PICTURE IS X(any)
..field..... (hmm... unless you 'filter' the data FIRST?).

But if you have to filter the data first, you can't use LINE SEQUENTIAL for
that anyway, so you may as well just change your program to use ORGANIZATION
SEQUENTIAL with either fixed or variable-length records.

FWIW, here's a freebie tutorial I wrote a few years ago on using
COBOL-created data on other systems or with non-COBOL programs. Maybe it
will give you an alternate idea:
http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

MCM
```

#### ↳ Re: AIX Cobol II and Packed Decimal fields

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-10-27T16:04:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wU68f.37122$3k2.25235@fe08.news.easynews.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com>`

```
If you want the files to be "useable" in AIX in NON-COBOL programs, you *might* 
find it useful to:

A) convert the files to Line Sequential
   *AND*
B) convert all numeric fields (COMP and COMP-3) to
   USAGE DISPLAY SIGN IS LEADING SEPARATE

This would (certainly) take more storage (and require a "conversion program") 
but might be more useful in the long run.

Otherwise, exactly what problems are you having with using the files "as is" 
(variable length with COMP-3)?
```

##### ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

- **From:** "alf" <alf@itxpurts.com.au>
- **Date:** 2005-10-27T16:21:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130455317.980798.283120@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<wU68f.37122$3k2.25235@fe08.news.easynews.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com>`

```
The error we get when we try and read the file is...

IWZ039S  An invalid overpunched sign was detected.

As soon as we make it fixed length it is ok... but the files increase
in size dramtically. eq one file has about 4 million records and are
mostly 100 bytes in length...  but the maximum record length is 480.

We could convert the files and have looked into doing that but it would
add at least 3 months to the project as there are a lot of programs to
look at and we didnt really want to fiddle with to much code changing
(as we are doing it for another company and there is NO documentation
lol).

The thing thats confusing me is that I have searched high and low and
have not found this documented.

William M. Klein wrote:
> If you want the files to be "useable" in AIX in NON-COBOL programs, you *might*
> find it useful to:
…[29 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-27T23:51:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djrp6t$o96$1@reader2.panix.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com>`

```
In article <1130455317.980798.283120@g43g2000cwa.googlegroups.com>,
alf <alf@itxpurts.com.au> wrote:
>The error we get when we try and read the file is...
>
…[4 more quoted lines elided]…
>mostly 100 bytes in length...  but the maximum record length is 480.

Time for the project leader to make a Management Decision: which is more 
desireable, a smaller file that doesn't work or a larger file that does?

>
>We could convert the files and have looked into doing that but it would
…[3 more quoted lines elided]…
>lol).

You are, some might say, fortunate; no documentation means no 
documentation to mislead you into believing that the code does what the 
documentation says it is supposed to be doing.  As for 'the other 
company'... if it were easy or fun they would have done it themselves; 
have the project leader inform them that there is an ancient list:

On Time
On Spec
On Budget

... and that they should pick two.

DD
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 4)_

- **From:** "alf" <alf@itxpurts.com.au>
- **Date:** 2005-10-27T17:22:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130458972.955036.322840@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<djrp6t$o96$1@reader2.panix.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <djrp6t$o96$1@reader2.panix.com>`

```
At the moment we have made a call to make the files fixed length. This
still means we have to make some coding changes (ie change the writes
and reads) but is a lot less impact then Un-COMPing.... There are
several copybooks within copybooks.
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-27T17:06:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130457991.992931.190090@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1130455317.980798.283120@g43g2000cwa.googlegroups.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com>`

```
>>> IBM mainframe to AIX. ... COMP-3 (packed decimal)

> IWZ039S  An invalid overpunched sign was detected.

IBM Mainframe is EBCDIC, AIX is ASCII.

How did you do the conversion from one code set to the other ? How does
this manage the sign conversions ?
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 4)_

- **From:** "alf" <alf@itxpurts.com.au>
- **Date:** 2005-10-27T17:19:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130458761.714904.61310@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1130457991.992931.190090@o13g2000cwo.googlegroups.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com>`

```
To be honest i'm not sure how it was done. We got the data files given
to us from the "Company" in the correct format. They do have access to
an AIX box onsite so I suppose they wrote a conversion program...  They
dont seem to have a lot of time so we have had to fly by our pants
basically. Still waiting for a comment from a data file we produced for
them to look at over 2 weeks ago.. lol
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-27T18:08:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130461725.220629.221050@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1130458761.714904.61310@g47g2000cwa.googlegroups.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com>`

```
> We got the data files given
> to us from the "Company" in the correct format.

If you were to write a new file in variable format containing all the
values from -10 to +10 then you should be able to see the sign values
actually used by the AIX compiler. You should also be able to read this
file back without failure.

You should also be able to examine the converted file and check that
the sign values are correct or have been converted wrongly.

You may also want to know whether the problem is that the 'depending
on' value has been converted correctly or not.  If for example a file
record claims that there are 2 occurances, but only one exists in the
file record, then it is quite possible that the program looks at
occurance 2 and gets junk (ie gives your error). Having all occurances
in the record, with the trailing ones initialised will mask the
problem.

The problem may be that the 'depending on' value is set wrongly by the
conversion _OR_ the depending on value is correct but the data items
were not all put into the converted record.
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 6)_

- **From:** "alf" <alf@itxpurts.com.au>
- **Date:** 2005-10-27T19:34:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130466859.900004.324230@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1130461725.220629.221050@o13g2000cwo.googlegroups.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com> <1130461725.220629.221050@o13g2000cwo.googlegroups.com>`

```
Thanks Richard. I just created a file with the numbers -10 to 100 in
Signed Packed Decmial (COMP-3)
and guess what. -10 is represented as 010d   arrrrrrrgggggg which means
the 0d a carriage return...
which means you cant have SIGNED PACKED DECIMAL in a variable length
file in a UNIX type file format on AIX....

Here is the file output  as a hex dump there are 2 number fields see
code below...

                  -    0   1     00 01 0-
00000000  2D 30 31 30 00 01 0D 0A    -010....
00000008  2D 30 30 39 00 00 9D 0A    -009...
00000010  2D 30 30 38 00 00 8D 0A    -008...
00000018  2D 30 30 37 00 00 7D 0A    -007..}.
00000020  2D 30 30 36 00 00 6D 0A    -006..m.
00000028  2D 30 30 35 00 00 5D 0A    -005..].
00000030  2D 30 30 34 00 00 4D 0A    -004..M.
00000038  2D 30 30 33 00 00 3D 0A    -003..=.
00000040  2D 30 30 32 00 00 2D 0A    -002..-.
00000048  2D 30 30 31 00 00 1D 0A    -001....
00000050  2B 30 30 30 00 00 0C 0A    +000....
00000058  2B 30 30 31 00 00 1C 0A    +001....
00000060  2B 30 30 32 00 00 2C 0A    +002..,.
00000068  2B 30 30 33 00 00 3C 0A    +003..<.
00000070  2B 30 30 34 00 00 4C 0A    +004..L.
00000078  2B 30 30 35 00 00 5C 0A    +005..\.
00000080  2B 30 30 36 00 00 6C 0A    +006..l.
00000088  2B 30 30 37 00 00 7C 0A    +007..|.
00000090  2B 30 30 38 00 00 8C 0A    +008...
00000098  2B 30 30 39 00 00 9C 0A    +009...
000000A0  2B 30 31 30 00 01 0C 0A    +010....

Here is the program I used

       IDENTIFICATION DIVISION.
       PROGRAM-ID. alf.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT ALF-FILE ASSIGN TO NAT-VAR
                           organization is LINE sequential.
       DATA DIVISION.
       FILE SECTION.
       FD  ALF-FILE
           recording mode is V.
       01  ALF-REC         pic X(7).
       WORKING-STORAGE SECTION.
       01  WS-REC.
           03  WS-NUM    PIC S9(3) sign leading separate.
           03  WS-NUM-CM PIC S9(3) COMP-3.
       PROCEDURE DIVISION.
       000-START SECTION.
           open output ALF-FILE.
           move -10               to WS-NUM
                                     WS-NUM-CM.
           move WS-REC           to ALF-REC.
           DISPLAY ALF-REC.
           write ALF-REC.
       010-add.
           add 1                  to WS-NUM.
           move WS-NUM           to WS-NUM-CM.
           move WS-REC           to ALF-REC.
           DISPLAY ALF-REC.
           write ALF-REC.
           if  WS-NUM            not =  10
           go to 010-add.
       020-end.
           CLOSE ALF-FILE.
           stop run.
           EXIT.
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-27T19:56:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130468188.817154.177380@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1130466859.900004.324230@g49g2000cwa.googlegroups.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com> <1130461725.220629.221050@o13g2000cwo.googlegroups.com> <1130466859.900004.324230@g49g2000cwa.googlegroups.com>`

```
> the 0d a carriage return... which means you cant have SIGNED
> PACKED DECIMAL in a variable length
> file in a UNIX type file format on AIX....

You cannot have any packed or comp in a _LINE_ sequential file, but
that isn't the only way to have a variable length file in Cobol.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. alf.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT ALF-FILE ASSIGN TO NAT-VAR
                           organization is sequential.
       DATA DIVISION.
       FILE SECTION.
       FD  ALF-FILE
           recording mode is V.
       01  ALF-REC.
           03  Alf-Count    PIC S9(4).
           03  Alf-Parts    OCCURS 1 TO 25 DEPENDING ON Alf-Count.
               05  Alf-Packed          PIC S9(7).
       WORKING-STORAGE SECTION.
       01  WS-REC.
           03  WS-NUM    PIC S9(3) sign leading separate.
           03  WS-NUM-CM PIC S9(3) COMP-3.
       01  Nat-Var               PIC X(20) VALUE "TESTVLEN.DAT".
       PROCEDURE DIVISION.
       000-START SECTION.
           open output ALF-FILE.
           MOVE 1                 TO Alf-Count
           move -10               to WS-Num
           MOVE WS-Num            TO Alf-Packed(Alf-Count)

           DISPLAY ALF-REC.
           write ALF-REC.
       010-add.
           add 1                  to WS-NUM.
      *     move WS-NUM           to WS-NUM-CM.
      *     move WS-REC           to ALF-REC.
           ADD 1                  TO Alf-Count
           MOVE WS-Num            TO Alf-Packed(Alf-Count)
           DISPLAY ALF-REC.
           write ALF-REC.
           if  WS-NUM            not =  10
           go to 010-add.
       020-end.
           CLOSE ALF-FILE.
           stop run.
      *     EXIT.
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-10-28T03:56:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9kh8f.101337$Qu4.49617@fe07.news.easynews.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com> <1130461725.220629.221050@o13g2000cwo.googlegroups.com> <1130466859.900004.324230@g49g2000cwa.googlegroups.com> <1130468188.817154.177380@z14g2000cwz.googlegroups.com>`

```
Rather than using the RECORDING MODE V (IBM extension),

I would recommend using the ('85 Standard - supported on all IBM platforms)

Record Varying in Size from n to n Depending on WS-Item.

If you do that and define the file as (record) Sequential, I believe the AIX 
COBOL should work "fine".
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-27T21:18:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130473133.317205.206740@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<9kh8f.101337$Qu4.49617@fe07.news.easynews.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com> <1130461725.220629.221050@o13g2000cwo.googlegroups.com> <1130466859.900004.324230@g49g2000cwa.googlegroups.com> <1130468188.817154.177380@z14g2000cwz.googlegroups.com> <9kh8f.101337$Qu4.49617@fe07.news.easynews.com>`

```
> Rather than using the RECORDING MODE V (IBM extension),

Testing with Fujitsu shows that can be left off and it still notices
that the record is variable.

> Record Varying in Size from n to n Depending on WS-Item.

Moving Alf-Count into WS works too.  Using 'record varying' implies
that one would have to use the number of bytes to determine record size
while ODO only needs the number of recurring items.
```

###### ↳ ↳ ↳ Re: AIX Cobol II and Packed Decimal fields

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-10-28T01:41:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11m3ejdscltr8c3@corp.supernews.com>`
- **References:** `<1130394756.656497.253930@g49g2000cwa.googlegroups.com> <wU68f.37122$3k2.25235@fe08.news.easynews.com> <1130455317.980798.283120@g43g2000cwa.googlegroups.com> <1130457991.992931.190090@o13g2000cwo.googlegroups.com> <1130458761.714904.61310@g47g2000cwa.googlegroups.com> <1130461725.220629.221050@o13g2000cwo.googlegroups.com> <1130466859.900004.324230@g49g2000cwa.googlegroups.com> <1130468188.817154.177380@z14g2000cwz.googlegroups.com> <9kh8f.101337$Qu4.49617@fe07.news.easynews.com> <1130473133.317205.206740@f14g2000cwb.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1130473133.317205.206740@f14g2000cwb.googlegroups.com...
[snip]
> > Record Varying in Size from n to n Depending on WS-Item.
>
> Moving Alf-Count into WS works too.  Using 'record varying' implies
> that one would have to use the number of bytes to determine record size
> while ODO only needs the number of recurring items.


RECORD VARYING without the remaining phrases works
if the file description entry describes different length records,
either with different length 01s or an ODO.
[Tested on Micro Focus COBOL V3.24]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
