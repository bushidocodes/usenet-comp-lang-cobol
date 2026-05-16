[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# sequential file formats

_16 messages · 7 participants · 2005-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### sequential file formats

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-24T22:02:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
I have noticed that every compiler/op sys seems to create a different
format for sequential files.  for instance, a COBOL program on the
mainframe will create a sequential file with a four byte header that
indicates length.  On microfocus on AIX, a COBOL program will create a
similar file but the with a special record as the first record that has
some additional information.

Does anyone know of a comprehensive list of all the different formats
that may be out there?

I will post small sample program that will create a two record
sequential file in hopes that some of you will run the program and
report back the format of the file that is produced.  A hex dump as a
post would be great.  if you can not hex dump on your selected
operating system, then email the output to theador@@@@gmail and I will
hex dump the file and post it.

Hopefully we can cover these combinations:
Fujitsu on UNIX
Fujitsu on WIndows
IBM on AIX
IBM on z/OS
MicroFocus on UNIX
MicroFocus on WIndows
AccuCOBOL
OpenCOBOL

Thanks to those who can help in this experiment,
Theador.
```

#### ↳ Re: sequential file formats

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-07-25T07:53:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11e9o5p4s4ql17e@news.supernews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
theador wrote:
> I have noticed that every compiler/op sys seems to create a different
> format for sequential files.

Should be: "... every programmer seems to create..."


for instance, a COBOL program on the
> mainframe will create a sequential file with a four byte header that
> indicates length.  On microfocus on AIX, a COBOL program will create a
> similar file but the with a special record as the first record that
> has some additional information.

And I can duplicate these on a PC.
```

#### ↳ Re: sequential file formats

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2005-07-25T10:48:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aru9e1tfdudhpg37kdaksuqqj7jr88mpel@4ax.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
On 24 Jul 2005 22:02:28 -0700, "theador" <Theador@gmail.com>
enlightened us:

>I have noticed that every compiler/op sys seems to create a different
>format for sequential files.  for instance, a COBOL program on the
…[4 more quoted lines elided]…
>

Have you noticed that a sequential file on the mainframe, whether
created by COBOL or some other language, can also not have a four byte
header and be fixed length?


>Does anyone know of a comprehensive list of all the different formats
>that may be out there?
…[19 more quoted lines elided]…
>Theador.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


"The early bird may get the worm, 
but the second mouse gets the cheese."
--Steven Wright
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: sequential file formats

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-25T18:10:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122340240.266636.261240@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<aru9e1tfdudhpg37kdaksuqqj7jr88mpel@4ax.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <aru9e1tfdudhpg37kdaksuqqj7jr88mpel@4ax.com>`

```
Ahhh, the fixlength sequential file.  I will write a different test
program and start a new topic if I need to determine the differences
between what programs compiled with different compilers output.  Thanks
for pointing that out.
```

#### ↳ Re: sequential file formats

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-25T18:07:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122340051.268224.81380@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
here is the hexdump of the output file from open-cobol on debian intel
linux:

$ od -h output.dat
0000000 0014 0000 ffff ffff ffff ffff ffff ffff
0000020 ffff ffff ffff ffff 001e 0000 0000 0000
0000040 0000 0000 0000 0000 0000 0000 0000 0000
0000060 0000 0000 0000 0000 0000
0000072

I think this is the same as mainframe cobol.
```

#### ↳ Re: sequential file formats

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-25T19:01:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122339897.498960.298900@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
Here is the test program that I am asking people with access to the
above machines to run and report a hex dump of the output file.  This
was compiled on open-cobol, so there may be different compile errors
that would have to be fixed on your platform. thx.

       IDENTIFICATION   DIVISION.
       PROGRAM-ID.      test1.

       environment division.
       input-output section.
       file-control.
       select AFILE assign to "output.dat"
       organization is relative sequential
       record key is big-record.

       DATA  DIVISION.
       FILE  SECTION.

          fd AFILE
          label records are standard
          record varying from 1 to 50
          depending on a-length
          data record is a-file.

       01 a-file.
          05 big-record pic x(50).
       WORKING-STORAGE  SECTION.

       01 A-GRP.
          05  A-ELE     PIC X(50).

       01 A-LENGTH  COMP PIC S9(4).

       PROCEDURE DIVISION.

           OPEN OUTPUT AFILE.
           MOVE ALL HIGH-VALUES to a-grp.
           MOVE 20 TO A-LENGTH.
           WRITE A-FILE FROM A-GRP.
           MOVE ALL LOW-VALUES to a-grp.
           MOVE 30 TO A-LENGTH.
           WRITE A-FILE FROM A-GRP.
           CLOSE AFILE.

           STOP RUN.
```

##### ↳ ↳ Re: sequential file formats

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-07-25T23:00:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42E5B560.B5ED6985@mb.sympatico.ca>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <1122339897.498960.298900@g44g2000cwa.googlegroups.com>`

```
theador wrote:
> 
> Here is the test program that I am asking people with access to the
…[13 more quoted lines elided]…
> 


Surely a clarification is needed: "organization is relative" is not the
same as "organization is sequential"/a sequential file.   ???

PL
```

##### ↳ ↳ Re: sequential file formats

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-07-25T21:31:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122352319.603705.24890@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1122339897.498960.298900@g44g2000cwa.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <1122339897.498960.298900@g44g2000cwa.googlegroups.com>`

```
>> different format for sequential files.

>      select AFILE assign to "output.dat"
>       organization is relative sequential
>       record key is big-record.

That is _NOT_ a 'sequential file'. It is organization relative, access
sequential which is quite a different thing altogether.

You also cannot have RECORD KEY on relative or sequential so I am
surprised that it compiled.

>          fd AFILE
>          label records are standard
>          record varying from 1 to 50
>          depending on a-length
>          data record is a-file.

If you going to have variable records then there must be _some_
mechanism to indicate where the record ends on the disc and (possibly)
where the next one starts. This is often done with a header on the
record though I do know of other mechanisms that can be used.

Fixed length records may not need the record header or terminator.

>       01 a-file.
>          05 big-record pic x(50).

This should be a problem for the compiler too.  You have defined a
variable key (though this is complete nonsense anyway).
```

#### ↳ Re: sequential file formats

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-26T03:11:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_RhFe.457981$Cl1.101809@fe03.news.easynews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com>`

```
Can you tell us WHY you want this information?  Almost (possibly all) vendors 
provide documentation on their OWN 'file structures" (and often they also 
include OPTIONS for file types).  As others have pointed out on (IBM - not all - 
mainframes) the "RDW" (record descriptor word) ONLY appears for variable length 
(RECFM=V) (or possibly spanned?) records.  For fixed length files this doesn't 
exist.  For BLOCKED files (again IBM mainframe) there is also a 4-byte "block 
descriptor word" before each block of records.  As far as "print" output goes, 
on IBM mainframes, you also need to check out the ADV compiler option and there 
are different syntax options that produce RECFM=FA vs RECFM=FM (ASA characters 
vs Machine characters)

On all (most?) environments where Micro Focus provides a compiler, there are 
bunches and BUNCHES of things that can impact this, for example
 - the RDW compiler directive "emulates" IBM mainframe RDW support
 - RECORD SEQUENTIAL files are stored very differently from LINE SEQUENTIAL 
files (either source code or directives can impact this) - and fixed vs variable 
impacts this as well.

"traditionally" most Windows (and DOS? and OS/2?) compilers use "CR/LF" to 
terminate "line sequential" files - while they ONLY use "LF" (as I recall) for 
Unix and Linux systems.   How they handle "AFTER/BEFORE ADVANCING" (and the 
older POSITIONING) and Report-Writer type files may also vary.

Again, tell us what you REALLY want to know and we may be able to give you 
better information. If this is just a case of "I'm curious" then about your 
SPECIFIC code example, then some people may be able to run it - but I don't 
know.

P.S.  You may want to compile your program with a compiler that has ANSI or FIPS 
"flagging" available (which I don't think Open-COBOL does) to at least get a 
"Standard conforming" source code.  Without checking in detail, I think your 
example (in another post) ignores:
  A-/B-margin
  Assign to shouldn't be a literal
  no paragraph names
   etc

You have
  organization is relative sequential
    record key is big-record.

which means that this is a RELATIVE file with access sequential - which is NOT 
what is "usually" meant be "sequential file" - but instead what is meant by a 
"relative file".  (On an IBM mainframe, this would need to be pointing to a RRDS 
VSAM file and NOT to a QSAM file).  SEQUENTIAL files do not have "keys". 
"Keyed" files have (usually VERY different structures.  See for example the 
Micro Focus INDXFORMAT - or something like that - I didn't check) directive)
```

##### ↳ ↳ Re: sequential file formats

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-26T14:38:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122413922.494578.13640@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<_RhFe.457981$Cl1.101809@fe03.news.easynews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com>`

```
Thank you all for the feed back.  Yes, my program has problems as I am
not a COBOL expert and I was compiling on a substandard compiler
(open-cobol).  I am financially constrained, so I can not afford to buy
a commercial COBOL compiler.  My goal in this exercise is to get sample
data to test routines that convert sequential files between the various
formats.  I am writing the conversion routines in C (a language in
which I am proficient).

At this time I am not concerned about C-ISAM, VSAM, or LINE SEQUENTIAL
FILES.

Theador.
```

###### ↳ ↳ ↳ Re: sequential file formats

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-27T01:13:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wcBFe.651934$iM6.425300@fe01.news.easynews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com>`

```
The following is s SLIGHT modification of your program that should work in any 
(?) '85 Standard (high) COBOL compiler and I think will work with Open-Cobol 
(but I haven't tried it).

I have two commented lines in the Select statement
 - change to the 2nd variation if your compiler doesn't support "literals" in 
ASSIGN TO
- uncomment "RECORD" if your compiler supports both RECORD SEQUENTIAL and LINE 
SEQUENTIAL (which I think O-C does).
- in "My" compiler the "I" of Identification Division is in column 8 - but isn't 
in this text.  That will need to be changed for compilers with A-/B-margin 
restrictions.  Similarly, the B-margin items seem to have been "shifted over" in 
this text (and need to start in column 12 - or later).

I ran this with Fujitsu "flagging" turned on - so if I missed any extensions 
(because their flagging is weak), let me know:

       IDENTIFICATION   DIVISION.
       PROGRAM-ID.      test1.
       environment division.
       input-output section.
       file-control.
           Select AFILE assign to "output.dat"
      *    Select AFILE assign to OUTPFILE
              organization is
      *         RECORD
              sequential
              access is sequential
                 .
       DATA  DIVISION.
       FILE  SECTION.
       FD  AFILE
           record varying in size from 1 to 50
           depending on a-length
            .            .
       01 a-file.
           05 big-record pic x(50).
       WORKING-STORAGE  SECTION.
       01  A-GRP.
           05  A-ELE     PIC X(50).
       01 A-LENGTH  Binary PIC 9(4).

       PROCEDURE DIVISION.
        Mainline.
           OPEN OUTPUT AFILE
           MOVE ALL HIGH-VALUES to a-grp
           MOVE 20 TO A-LENGTH
           WRITE A-FILE FROM A-GRP
           MOVE ALL LOW-VALUES to a-grp
           MOVE 30 TO A-LENGTH
           WRITE A-FILE FROM A-GRP
           CLOSE AFILE
              .
           STOP RUN
             .
```

###### ↳ ↳ ↳ Re: sequential file formats

_(reply depth: 4)_

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-26T21:41:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122439305.218078.203660@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<wcBFe.651934$iM6.425300@fe01.news.easynews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com> <wcBFe.651934$iM6.425300@fe01.news.easynews.com>`

```
Thanks Bill.

I deleted one of the periods on line 18 and your version of the program
compiled.  It also gave the same output file (not surprisingly).

Fujitsu must not care about extra terminating
periods.

Can you post the hex dump of the outputfile?

Thanks for your help!
Theador.
```

###### ↳ ↳ ↳ Re: sequential file formats

- **From:** epc8@juno.com
- **Date:** 2005-07-26T21:47:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122439656.386542.123920@f14g2000cwb.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com>`

```

theador wrote:
> Thank you all for the feed back.  Yes, my program has problems as I am
> not a COBOL expert and I was compiling on a substandard compiler
…[9 more quoted lines elided]…
> Theador.

Then dealing with the differences in record structure will be the
*least* of your problems. Coping with the myriad ways of encoding the
actual data is much more difficult.

The easiest and most reliable way of moving data from COBOL X to COBOL
Y is via text files in which all of the digits in a number and its sign
(if present) are explicitly represented.
```

###### ↳ ↳ ↳ Re: sequential file formats

_(reply depth: 4)_

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-27T16:26:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122506771.018520.173960@f14g2000cwb.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com> <1122439656.386542.123920@f14g2000cwb.googlegroups.com>`

```
epc8@juno.com wrote:

> Then dealing with the differences in record structure will be the
> *least* of your problems. Coping with the myriad ways of encoding the
…[4 more quoted lines elided]…
> (if present) are explicitly represented.

Do you have some specific examples of different ways that different
compilers encode data when writing to a sequential file?  I would be
especially interested in hex dumps of the differences rather than just
a discussion.  I am not doubting you, I would just like to see the
actual examples.  One that I am aware of is that IBM COBOL on AIX
encodes the sign digit of COMP3 data differently than microfocus or IBM
COBOL on zOS.  I dont currently have access to those compilers so I am
afraid I can not provide the hex dumps.

Theador.
```

###### ↳ ↳ ↳ Re: sequential file formats

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-28T00:57:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K3WFe.699573$3V6.135135@fe04.news.easynews.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com> <1122439656.386542.123920@f14g2000cwb.googlegroups.com> <1122506771.018520.173960@f14g2000cwb.googlegroups.com>`

```
Your requests for "hex dumps" of files isn't getting many replies.  I know that 
it isn't something that I am about to try and do.  What you really SHOULD be 
asking for (IMHO) is references to online documentation.  This will (again in my 
opinion) be a much better way of finding out how different compilers and 
run-times handle different "things".

For example,
   Check out how all the different systems handle:
      COMP-1, COMP-2, COMP-3, COMP-4, COMP-5, and COMP-6 (depending upon which 
they have)
      COMP
      Other floating-point (if available)
      Binary (big-endian/little-endian among other things)
      sign-nibbles (Packed-Decimal and Usage Display)
      UTF-16, DBCS, other - for USAGE NATIONAL (if supported)
      ASCII vs EBCDIC (or other) for USAGE DISPLAY
      Do they support BIT data? (or Boolean)
      Do they support unsigned packed-decimal

also, references to "compiler options/directives" that impact sequential file 
formats.  See (for a good starting place)
   http://www.talsystems.com/tsihome_h...oads/C2IEEE.htm

and

"Introduction to COBOL Numeric Data Types
Michael Mattias has created a text and graphics based introduction to COBOL 
numeric data types. It was designed for intermediate to advanced programmers not 
familiar with the COBOL language or COBOL numeric data storage. A Windows Write 
or compatible word processor is recommended, but an ASCII text file format is 
also included). The PKZIP format file includes an executable program file as 
well as PB 3.2 source code. This file is Copyrighted but free for personal use. 
A compiler is NOT required to use this product.
    http://www.flexus.com/ftp/cobdata.zip
```

###### ↳ ↳ ↳ Re: sequential file formats

_(reply depth: 6)_

- **From:** "theador" <Theador@gmail.com>
- **Date:** 2005-07-27T18:49:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1122515355.632430.91460@o13g2000cwo.googlegroups.com>`
- **References:** `<1122264295.228797.240710@o13g2000cwo.googlegroups.com> <_RhFe.457981$Cl1.101809@fe03.news.easynews.com> <1122413922.494578.13640@g49g2000cwa.googlegroups.com> <1122439656.386542.123920@f14g2000cwb.googlegroups.com> <1122506771.018520.173960@f14g2000cwb.googlegroups.com> <K3WFe.699573$3V6.135135@fe04.news.easynews.com>`

```
I am aware of the documentation that is on the COBOL Compiler vendor's
websites.  What I dont have is sample data to run my programs against.
I could hand generate some output using their specification, but that
is not the same as having output that was generated by a compiled
program.

Bill, You went to the work of compiling the sample program, I can not
figure out why you were relunctant to run the program and post a hex
dump of the output.  If you dont have a tool to hex dump I would be
happy to do that if you email a zip file of the output to me.
theador@@@@@gmail......com

Theador.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
