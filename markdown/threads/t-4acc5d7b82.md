[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Final (I hope) Overlapping Artihmetic test

_10 messages · 7 participants · 2008-12_

---

### Final (I hope) Overlapping Artihmetic test

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-19T02:23:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`

```
Once again, could kindly CLC readers try the following source code on various 
compilers and let me know what the restuls are.

Testing portability of "BINARY" stuff is almost impossible.  Not only do 
"standard" vs "normal NON-COBOL" truncation rules come into play, but 
big-/little-endian issues and word/byte boundaries and synchronozation also 
impacts how compilers do this.

THEREFORE, it won't surprise me if many compilers "fail" this test.  I but in a 
"check" for big-/little-endian, but couldn't try all the variations of sync and 
binary storatge issues.

This may not even compile on all compilers as I have used "hex-literals" and 
some other stuff that isn't standard.

If anyone has any suggestions on how to test this in a "more portable" way (for 
BINARY data items), please let me know.

Please, just let me know the results.

  * * * * * * * *

       Identification Division.
        Program-ID. OVERLAP4.
       Data Division.
        Working-Storage Section.
       01  Check-Format.
           05  Test-Bin  Pic S9(09) Binary  Value +12345678.
       01  Group1.
           05  Num1  Pic S9(09) Binary.
           05   Pic  X(04).
       01  Group2 Redefines Group1.
           05   Pic  X(02).
           05  Num2  Pic S9(09) Binary.
       01  Group3 Redefines Group1.
           05                   Pic  X(04).
           05  Num3  Pic S9(04) Binary.
           05   Pic  X(02).
       01  Group4 Redefines Group1.
           05  Num4             Pic S99999V99 Binary.
           05  Num5             Pic S99V999 Binary.
       Procedure Division.
        Mainline.
           Evaluate Check-Format
             When X"00BC614E"
              Perform Big-Endian
             When X"4E61BC00"
                Perform Little-Endian
             When Other
                Display "Unexpected Binary Format, no tests Performed"
           End-Evaluate
    Stop Run
     .
       Big-Endian.
           Display "==> Start Big-Endian Tests"
           Move Zeroes   to Num2
           Move +10101010  To Num1
           Add Num1 to Num2
               On Size Error
                   Display "-> ADD had an ON SIZE ERROR"
           End-ADD
           If Num2 = +564928786
               Display "      ADD Test Passed, Num2=" Num2
           Else
               Display "      ADD Test Failed, Num2=" Num2
           End-If
           Move Zeroes   to Num3
           Move +1234567 To Num2
           Subtract Num3 From Num2
               On Size Error
                   Display "-> SUBTRACT had an ON SIZE ERROR"
           End-SUBTRACT
           If Num2 = +1245184
               Display " SUBTRACT Test Passed, Num2=" Num2
           Else
               Display " SUBTRACT Test Failed, Num2=" Num2
           End-If
           Move Zeroes  to Num2
           Move +123  to Num3
           Multiply Num3 By Num2
               On Size Error
                   Display "-> MULTIPLY had an ON SIZE ERROR"
           End-MULTIPLY
           If Num2 = +15129
               Display " MULTIPLY test Passed, Num2=" Num2
           Else
               Display " MULTIPLY test Failed, Num2=" Num2
           End-If
           Move Zeroes  to Num1
                                   Num3
           Move +7286841 to Num2
           Divide Num2 by Num3
             Giving Num4
             Remainder Num5
               On Size Error
                   Display "-> DIVIDE had an ON SIZE ERROR"
           End-Divide
           If   Num4 = +590.26
            and Num5 = +81.3
               Display "   DIVIDE test Passed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           Else
               Display "   DIVIDE test Failed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           End-IF
           Display "==>   End Big-Endian Tests"
            .
       Little-Endian.
           Display "==> Start Little-Endian Tests"
           Move Zeroes   to Num2
           Move +10101010  To Num1
           Add Num1 to Num2
               On Size Error
                   Display "-> ADD had an ON SIZE ERROR"
           End-ADD
           If Num2 = +10101164
               Display "      ADD Test Passed, Num2=" Num2
           Else
               Display "      ADD Test Failed, Num2=" Num2
           End-If
           Move Zeroes   to Num3
           Move +1234567 To Num2
           Subtract Num3 From Num2
               On Size Error
                   Display "-> SUBTRACT had an ON SIZE ERROR"
           End-SUBTRACT
           If Num2 = +1234549
               Display " SUBTRACT Test Passed, Num2=" Num2
           Else
               Display " SUBTRACT Test Failed, Num2=" Num2
           End-If
           Move Zeroes  to Num2
           Move +4915200 to Num2
           Multiply Num3 By Num2
               On Size Error
                   Display "-> MULTIPLY had an ON SIZE ERROR"
           End-MULTIPLY
           If Num2 = +368640000
               Display " MULTIPLY test Passed, Num2=" Num2
           Else
               Display " MULTIPLY test Failed, Num2=" Num2
           End-If
           Move Zeroes  to Num1
                                   Num3
           Move +864224 to Num2
           Divide Num2 by Num3
             Giving Num4
             Remainder Num5
               On Size Error
                   Display "-> DIVIDE had an ON SIZE ERROR"
           End-Divide
           If   Num4 = +66478.76
            and Num5 = +0.120
               Display "   DIVIDE test Passed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           Else
               Display "   DIVIDE test Failed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           End-IF
           Display "==>   End Little-Endian Tests"
            .             .
* * * * * End of sample source code.
```

#### ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-12-19T12:59:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gig2b8$eur$1@nntp.fujitsu-siemens.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> schrieb im Newsbeitrag 
news:URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com...
> Once again, could kindly CLC readers try the following source code on 
> various compilers and let me know what the restuls are.
…[16 more quoted lines elided]…
> Please, just let me know the results.

All tests passed (big endian) with Fujitsu Siemens Compiler COBOL2000 V1.4B 
and operating system BS2000 OSD V8.0
(BINARY data items were aligned on byte boundaries without SYNC)

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

#### ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2008-12-19T10:05:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e495c4c-178a-4402-a8bd-3163cfdba6c2@s14g2000vbp.googlegroups.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`

```
On Dec 19, 2:23 am, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> Once again, could kindly CLC readers try the following source code on various
> compilers and let me know what the restuls are.
…[163 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

Passes on OpenCOBOL compiler 1.1.0 for Itanium Linux (Suse 10.2),
MacOS 10.5.4 on PowerPC, MacOS 10.5.6 on Intel,
and on OpenVMS.  Won't compile under HP3K MPE/IX, and failed on an
iSeries running 5.3.

paul@ilin110:~/cobsrc> cobc -version
cobc (OpenCOBOL) 1.1.0
Copyright (C) 2001-2008 Keisuke Nishida / Roger While
Built    Nov 15 2008 14:14:38
Packaged Nov 09 2008 19:18:09 CET
paul@ilin110:~/cobsrc> ./test2
==> Start Big-Endian Tests
      ADD Test Passed, Num2=+564928786
 SUBTRACT Test Passed, Num2=+001245184
 MULTIPLY test Passed, Num2=+000015129
   DIVIDE test Passed, Num4=+00590.26
                       Num5=+81.300
==>   End Big-Endian Tests

and on PowerPC
==> Start Big-Endian Tests
      ADD Test Passed, Num2=+564928786
 SUBTRACT Test Passed, Num2=+001245184
 MULTIPLY test Passed, Num2=+000015129
   DIVIDE test Passed, Num4=+00590.26
                       Num5=+81.300
==>   End Big-Endian Tests
kermit:~/cobsrc Paul$

----

Also passes on OpenVMS Itanium

$ cobol /version
HP COBOL V2.9-1453 on OpenVMS IA64 V8.3-1H1
$ run test2
==> Start Little-Endian Tests
      ADD Test Passed, Num2=¬!
 SUBTRACT Test Passed, Num2=uÖ
 MULTIPLY test Passed, Num2=ù
   DIVIDE test Passed, Num4=Dpe
                       Num5=x
==>   End Little-Endian Tests

---
Will not compile as in on HP3K Cobol
LINE #   SEQ #  COL  ERROR  SEV   TEXT OF MESSAGE
------  ------  ---  -----  ---   ---------------


 00024          08    051    W    REDEFINING ITEM GROUP2 IS SMALLER
THAN
                                  REDEFINED ITEM.
 00037          19    356    Q    UNDEFINED DATA NAME X.
 00037          20    004    W    MISSING SPACE.
 00037          20    410    S    SYNTAX ERROR.  FOUND: 00BC614E;
EXPECTING ONE
                                  OF THE FOLLOWING: <RM-LPAR> <SUB-
LPAR> IN OF
                                  a_verb ENTRY
 00038          15    980    I    ATTEMPTING TO RECOVER FROM SYNTAX
ERROR.
 00039          19    356    Q    UNDEFINED DATA NAME X.
 00039          20    004    W    MISSING SPACE.
 00039          20    410    S    SYNTAX ERROR.  FOUND: 4E61BC00;
EXPECTING ONE
                                  OF THE FOLLOWING: <RM-LPAR> <SUB-
LPAR> IN OF
                                  a_verb ENTRY
 00040          17    980    I    ATTEMPTING TO RECOVER FROM SYNTAX
ERROR.


2 ERROR(s), 2 QUESTIONABLE, 3 WARNING(s)

------
It failed on a PowerPC based iSeries machine.
Running 5.4

Job 214032/PAULR/PXRDSP1 started on 12/19/08 at 09:51:42 in subsystem
QINTER
==> Start Big-Endian
Tests
      ADD Test Passed,
Num2=564928786
-> SUBTRACT had an ON SIZE
ERROR
 SUBTRACT Test Failed,
Num2=001234567
 MULTIPLY test Passed,
Num2=000015129
-> DIVIDE had an ON SIZE
ERROR
   DIVIDE test Failed,
Num4=0000111
 
Num5=58368
==>   End Big-Endian
Tests


-Paul
```

##### ↳ ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-19T18:18:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IRW2l.41054$Rp1.37736@en-nntp-01.dc1.easynews.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com> <6e495c4c-178a-4402-a8bd-3163cfdba6c2@s14g2000vbp.googlegroups.com>`

```
Looks like HP3K Cobol doesn't support hex-literals (not part of the '85 
Standard).

I don't fully understand the  PowerPC based iSeries machine problem, but I think 
it has to do with how many bytes are allocated for which size binary field. 
Which compiler were you using on that machine? I see "5.4" but don't know what 
compiler that is.  (Is that ILE COBOL or COBOL/400 or something else?)
```

###### ↳ ↳ ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2008-12-19T21:52:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<494c6c04$0$5477$bbae4d71@news.suddenlink.net>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com> <6e495c4c-178a-4402-a8bd-3163cfdba6c2@s14g2000vbp.googlegroups.com> <IRW2l.41054$Rp1.37736@en-nntp-01.dc1.easynews.com>`

```
On 2008-12-19 18:18:47 -0600, "William M. Klein" 
<wmklein@nospam.ix.netcom.com> said:

> Looks like HP3K Cobol doesn't support hex-literals (not part of the '85
> Standard).
…[5 more quoted lines elided]…
> compiler that is.  (Is that ILE COBOL or COBOL/400 or something else?)

I actually screwed that up, I meant to compile on a 5.3 partition, and 
compiled instead on a 5.2 partition:

 5722WDS V5R2M0  020719 LN  IBM ILE COBOL

Should not be any major changes between that and 5.4 though. .... and 
there isn't. I just recompiled on 5.3 and on
5.4 with exactly the same results. I don't have a 6.x machine to test 
it on though.

-Paul
```

###### ↳ ↳ ↳ Re: Final (I hope) Overlapping Artihmetic test

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-19T22:17:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hl_2l.457939$5p1.237886@en-nntp-06.dc1.easynews.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com> <6e495c4c-178a-4402-a8bd-3163cfdba6c2@s14g2000vbp.googlegroups.com> <IRW2l.41054$Rp1.37736@en-nntp-01.dc1.easynews.com> <494c6c04$0$5477$bbae4d71@news.suddenlink.net>`

```
I have come up with a variation of my original test code that should be MORE 
portable.  I think it will compile on HP, but will probably still have a problem 
on iSeries.

If anyone is interested in testing and hasn't already, please use this code 
instead of the original code:

       Identification Division.
        Program-ID. OVERLAP5.
       Data Division.
        Working-Storage Section.
       01  Group1.
           05  Num1  Pic S9(09) Binary.
           05   Pic  X(04).
       01  Group2 Redefines Group1.
           05   Pic  X(02).
           05  Num2  Pic S9(09) Binary.
       01  Group3 Redefines Group1.
           05                   Pic  X(04).
           05  Num3  Pic S9(04) Binary.
           05   Pic  X(02).
       01  Group4 Redefines Group1.
           05  Num4             Pic S99999V99 Binary.
           05  Num5             Pic S99V999 Binary.
       01  Sep.
           05  Num1-Sep  Pic S9(09) Binary Sync.
           05  Num2-Sep  Pic S9(09) Binary Sync.
           05  Num3-Sep  Pic S9(04) Binary Sync.
           05  Num4-Sep  Pic S99999V99 Binary Sync.
           05  Num5-Sep  Pic S99V999 Binary Sync.
       Procedure Division.
        Mainline.
           Perform Add-test
           Perform Subtract-test
           Perform Multiply-Test
           Perform Divide-Test
          Stop Run
            .
       ADD-Test.
           Move Zeroes   to Num2
           Move +10101010  To Num1
           Move Num2  to Num2-Sep
           Add Num1 to Num2-Sep
               On Size Error
                   Display "-> ADD had an ON SIZE ERROR"
           End-ADD
           Move Zeroes   to Num2
           Move +10101010  To Num1
           Add Num1 to Num2
               On Size Error
                   Display "-> ADD had an ON SIZE ERROR"
           End-ADD
           If Num2 = Num2-Sep
               Display "      ADD Test Passed, Num2=" Num2
           Else
               Display "      ADD Test Failed, Num2=" Num2
           End-If
            .
       Subtract-Test.
           Move Zeroes   to Num3
           Move +1234567 To Num2
           Move Num2  to Num2-Sep
           Subtract Num3 From Num2-Sep
               On Size Error
                   Display "-> SUBTRACT had an ON SIZE ERROR"
           End-SUBTRACT
           Move Zeroes   to Num3
           Move +1234567 To Num2
           Subtract Num3 From Num2
               On Size Error
                   Display "-> SUBTRACT had an ON SIZE ERROR"
           End-SUBTRACT
           If Num2 = Num2-Sep
               Display " SUBTRACT Test Passed, Num2=" Num2
           Else
               Display " SUBTRACT Test Failed, Num2=" Num2
           End-If
            .
       Multiply-Test.
           Move Zeroes  to Num2
           Move +123  to Num3
           Move Num2  to Num2-Sep
           Multiply Num3 By Num2-Sep
               On Size Error
                   Display "-> MULTIPLY had an ON SIZE ERROR"
           End-MULTIPLY
           Move Zeroes  to Num2
           Move +123  to Num3
           Multiply Num3 By Num2
               On Size Error
                   Display "-> MULTIPLY had an ON SIZE ERROR"
           End-MULTIPLY
           If Num2 = Num2-Sep
               Display " MULTIPLY Test Passed, Num2=" Num2
           Else
               Display " MULTIPLY Test Failed, Num2=" Num2
           End-If
            .
       Divide-Test.
           Move Zeroes  to Num1
                                   Num3
           Move +7286841 to Num2
           Move Num4  to Num4-Sep
           Move Num5  to Num5-Sep
           Divide Num2 by Num3
             Giving Num4-Sep
             Remainder Num5-Sep
               On Size Error
                   Display "-> DIVIDE had an ON SIZE ERROR"
           End-Divide
           Move Zeroes  to Num1
                                   Num3
           Move +7286841 to Num2
           Divide Num2 by Num3
             Giving Num4
             Remainder Num5
               On Size Error
                   Display "-> DIVIDE had an ON SIZE ERROR"
           End-Divide
           If   Num4 = Num4-Sep
            and Num5 = Num5-Sep
               Display "   DIVIDE Test Passed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           Else
               Display "   DIVIDE Test Failed, Num4=" Num4
               DISPLAY "                       Num5=" Num5
           End-IF
            .

**** Source code ends here
```

#### ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2008-12-20T19:16:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<494d98d8$0$5499$bbae4d71@news.suddenlink.net>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`

```
On 2008-12-19 02:23:15 -0600, "William M. Klein" 
<wmklein@nospam.ix.netcom.com> said:

> Once again, could kindly CLC readers try the following source code on various
> compilers and let me know what the restuls are.
…[16 more quoted lines elided]…
> Please, just let me know the results.

Here are the results from the 400.  I am having a little difficulty in 
getting the new version to
run on MPE/IX, it has an unresolved link error. I asked about the error 
on the HP3K list, and I suspect
someone will know the answer. :)

-Paul

 Job 214085/PAULR/PXRDSP1 started on 12/20/08 at 17:10:45 in subsystem QINTER 
       ADD Test Passed, Num2=564928786                                        
 -> SUBTRACT had an ON SIZE ERROR                                             
 -> SUBTRACT had an ON SIZE ERROR                                             
  SUBTRACT Test Passed, Num2=001234567                                        
  MULTIPLY Test Passed, Num2=000015129                                        
 -> DIVIDE had an ON SIZE ERROR                                               
 -> DIVIDE had an ON SIZE ERROR                                               
    DIVIDE Test Passed, Num4=0000111                                          
                        Num5=58368
```

#### ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-12-22T21:38:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1230006785_14@isp.n>`
- **In-Reply-To:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com>`

```
William M. Klein wrote:
> Once again, could kindly CLC readers try the following source code on various 
> compilers and let me know what the restuls are.
…[16 more quoted lines elided]…
> Please, just let me know the results.

OpenVMS (TM) Alpha Operating System, Version V8.3
Compaq COBOL V2.8-1286

All Little-Endian Tests passed.


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

##### ↳ ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-12-23T13:19:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zRa4l.7376$sC4.2920@newsfe04.iad>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com> <1230006785_14@isp.n>`

```
 William M. Klein wrote:
> > Once again, could kindly CLC readers try the following source code on
various
> > compilers and let me know what the restuls are.
> >
> > Testing portability of "BINARY" stuff is almost impossible.  Not only do
> > "standard" vs "normal NON-COBOL" truncation rules come into play, but
> > big-/little-endian issues and word/byte boundaries and synchronozation
also
> > impacts how compilers do this.
> >
> > THEREFORE, it won't surprise me if many compilers "fail" this test.  I
but in a
> > "check" for big-/little-endian, but couldn't try all the variations of
sync and
> > binary storatge issues.
> >
> > This may not even compile on all compilers as I have used "hex-literals"
and
> > some other stuff that isn't standard.
> >
> > If anyone has any suggestions on how to test this in a "more portable"
way (for
> > BINARY data items), please let me know.
> >
> > Please, just let me know the results.
>


On this ancient compiler, the third test program failed as Evaluate with
NUMERIC wouldn't compile.

The last two tests:

PL
_________________

 VISUAL COBOL Compiler
 Version  2.10 (MS-DOS)
Copyright (C) 1987,1989 mbp Software & Systems
 XXXXXXXXXX    No Error(s)/Warning(s) found
    No Error(s) found,    No Warning(s) issued
 Compilation finished





C:\My Documents>overlap4
==> Start Little-Endian Tests
      ADD Test Passed, Num2= 10101164
 SUBTRACT Test Passed, Num2=  1234549
 MULTIPLY test Passed, Num2=368640000
   DIVIDE test Passed, Num4=  66478.76
                       Num5=     0.120
==>   End Little-Endian Tests

C:\My Documents>overlap5
      ADD Test Passed, Num2= 10101164
 SUBTRACT Test Passed, Num2=  1234549
 MULTIPLY Test Passed, Num2=991494144
   DIVIDE Test Passed, Num4=  65647.21
                       Num5=     0.690

C:\My Documents>
```

###### ↳ ↳ ↳ Re: Final (I hope) Overlapping Artihmetic test

- **From:** Duh_OZ <ozzy.kopec@gmail.com>
- **Date:** 2008-12-30T09:45:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6456eafd-d7b3-49f8-bc6f-da2107c1cbef@w24g2000prd.googlegroups.com>`
- **References:** `<URI2l.457520$5p1.197206@en-nntp-06.dc1.easynews.com> <1230006785_14@isp.n> <zRa4l.7376$sC4.2920@newsfe04.iad>`

```
MF 3.2.20

OMF"GNT"
MF"8"
COPYLIST
REF
REFNO
LISTWIDTH"132"
NOMFCOMMENT
NOBOUND
NOCHKDIV
NOALTER
OPTSPEED
SEQUENTIAL"LINE"


      ADD Test Passed, Num2=+564928786
 SUBTRACT Test Passed, Num2=+001245184
 MULTIPLY test Passed, Num2=+000015129
   DIVIDE test Passed, Num4=+0059026
                       Num5=+81300
=========================================
Realia 4.209

* A tad different than the MF output.

COMP-4
NODCHK
OPT
NOCALL
NOSUBCHK
STRCHK
ANSITRUNC
NOSMALLCOMP
NODCALL
NODIVZERO
NOEPDCALL
QUOTE
ASCII
STATABORT
MOVELINK
NOBLL4K
ARGCHK
UPLOW
WRITEAFTER
SOSI
NOCOPY68
MD:  200
NOFLAG-COM
NOFLAG-SEG
NOFLAG-FIPS
NODEBUG
DIALECT-REALIA4



W - 'STOP' in invalid area; assume valid

      ADD Test Passed, Num2=010101164
 SUBTRACT Test Passed, Num2=001234549
 MULTIPLY test Passed, Num2=991494144
   DIVIDE test Passed, Num4=6564721
                       Num5=00690
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
