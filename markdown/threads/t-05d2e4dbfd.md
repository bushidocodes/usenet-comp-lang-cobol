[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Anoterh test request (overlapping oerands again)

_17 messages · 10 participants · 2008-12_

---

### Anoterh test request (overlapping oerands again)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-15T17:04:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
The Standard ('85, '02, whatever) has rules for overlapping operand operations 
being undefined.  I have found (thanks to CLC people) that results DO differed 
for "SET" statements.  I am now interested in arithmetic statements.  I would 
appreciate CLC people testing the following ('85 Standard conforming) program 
with your "compiler of choice" (with compiler options/directives "of choice") 
and letting me know if all 5 tests display a "pass" message.

If all the test pass, just let me know which compiler you have tested with.  If 
any of them FAIL, I would be interested in the compiler and what results you 
get.
(I don't think there should be any "compile-time errors" - but if so, let me 
know that as well).

Test source code follows:

       Identification Division.
        Program-ID. OVERLAP2.
       Data Division.
        Working-Storage Section.
       01  Group1.
           05  Num1 Pic S9(02)
             Sign is Leading.
           05  Pic  X(01).
       01  Group2 redefines Group1.
           05  Num3 Pic S9(01)
            Sign is Leading.
           05  Num2     Pic S9(02)
              Sign is Trailing.
       Procedure Division.
        Mainline.
           Perform Add-Test
           Perform Subtract-Test
           Perform Multiply-Test
           Perform Divide-Test-1
           Perform Divide-Test-2
           Stop Run
             .
         Add-Test.
           Display " --> Start ADD test"
           Move -91  to Num2
           Move +23  to Num1
           Evaluate
               Num1 Numeric
                 Also
               Num2 Numeric
             When False also False
               Display "Neither Numeric"
             When False also True
               Display "Num1 not numeric"
             When True also False
               Display "Num2 not numeric"
             When Other
               Add Num1 to Num2
                   On Size Error
                       Display "Size Error"
               End-ADD
               If Num2 Numeric
                   If Num2 = -8
                       Display "ADD Test passed, Num2=" Num2
                   Else
                       Display "ADD Test Failed, Num2=" Num2
                   End-If
               Else
                   Display "ADD Test Failed, Num2=" Group2 (2:)
               End-IF
           End-Evaluate
           Display " -->   End ADD test"
            .
         Subtract-Test.
           Display " --> Start Subtract test"
           Move -91  to Num2
           Move +23  to Num1
           Evaluate
               Num1 Numeric
                 Also
               Num2 Numeric
             When False also False
               Display "Neither Numeric"
             When False also True
               Display "Num1 not numeric"
             When True also False
               Display "Num2 not numeric"
             When Other
               Subtract Num1 from Num2
                   On Size Error
                       Display "Size Error"
               End-Subtract
               If Num2 Numeric
                   If Num2 = -54
                       Display "SUBTRACT Test passed, Num2=" Num2
                   Else
                       Display "SUBTRACT Test Failed, Num2=" Num2
                   End-If
               Else
                   Display "SUBTRACT Test Failed, Num2=" Group2 (2:)
               End-IF
           End-Evaluate
           Display " -->   End Subtract test"
            .
         Multiply-Test.
           Display " --> Start Multiply test"
           Move -93  to Num2
           Move +2  to Num1
           Evaluate
               Num1 Numeric
                 Also
               Num2 Numeric
             When False also False
               Display "Neither Numeric"
             When False also True
               Display "Num1 not numeric"
             When True also False
               Display "Num2 not numeric"
             When Other
               Multiply Num1 by Num2
                   On Size Error
                       Display "Size Error"
               End-Multiply
               If Num2 Numeric
                   If Num2 = -46
                       Display "MULTIPLY Test passed, Num2=" Num2
                   Else
                       Display "MULTIPLY Test Failed, Num2=" Num2
                   End-If
               Else
                   Display "MULTIPLY Test Failed, Num2=" Group2 (2:)
               End-IF
           End-Evaluate
           Display " -->   End MULTIPLY test"
            .

         Divide-Test-1.
           Display " --> Start DIVIDE test 1"
           Move +99  to Num2
           Move -5  to Num1
           Evaluate
               Num1 Numeric
                 Also
               Num2 Numeric
             When False also False
               Display "Neither Numeric"
             When False also True
               Display "Num1 not numeric"
             When True also False
               Display "Num2 not numeric"
             When Other
               Divide Num1 into Num2
                   On Size Error
                       Display "Size Error"
               End-DIVIDE
               If Num2 Numeric
                   If Num2 = -11
                       Display "DIVIDE Test passed, Num2=" Num2
                   Else
                       Display "DIVIDE Test Failed, Num2=" Num2
                   End-If
               Else
                   Display "DIVIDE Test Failed, Num2=" Group2 (2:)
               End-IF
           End-Evaluate
           Display " -->   End DIVIDE test 1"
            .

         Divide-Test-2.
           Display " --> Start DIVIDE test 2"
           Move +99  to Num2
           Move -5  to Num1
           Evaluate
               Num1 Numeric
                 Also
               Num2 Numeric
             When False also False
               Display "Neither Numeric"
             When False also True
               Display "Num1 not numeric"
             When True also False
               Display "Num2 not numeric"
             When Other
               Divide Num1 into Num2
                Giving Num2
                Remainder Num3
                   On Size Error
                       Display "Size Error"
               End-DIVIDE
               If Num2 Numeric
                   If Num2 = -11
                    And Num3 = +4
                       Display "DIVIDE Test passed, Num2=" Num2
                       DIsplay "                    Num3=" Num3
                   Else
                       Display "DIVIDE Test Failed, Num2=" Num2
                       Display "                    Num3=" Num3
                   End-If
               Else
                   Display "DIVIDE Test Failed, Num2=" Group2 (2:)
               End-IF
           End-Evaluate
           Display " -->   End DIVIDE test 2"
            .

****** end of source code
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** btiffin@canada.com
- **Date:** 2008-12-15T19:40:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3649cef-2b1c-4229-92f6-d887f36ab568@k8g2000yqn.googlegroups.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
On Dec 15, 6:04 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> The Standard ('85, '02, whatever) has rules for overlapping operand operations
> being undefined.  I have found (thanks to CLC people) that results DO differed
…[17 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

Bill, here is the run from OpenCOBOL

 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2

$ cobc -V
cobc (OpenCOBOL) 1.1.0
Copyright (C) 2001-2008 Keisuke Nishida / Roger While
Built    Dec 15 2008 22:35:39
Packaged Dec 13 2008 21:48:02 CET

Cheers,
Brian
```

##### ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** btiffin@canada.com
- **Date:** 2008-12-15T19:45:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e10dff6a-e6f9-49ef-9868-e280962eb601@s37g2000vbp.googlegroups.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <d3649cef-2b1c-4229-92f6-d887f36ab568@k8g2000yqn.googlegroups.com>`

```
On Dec 15, 10:40 pm, btif...@canada.com wrote:
> On Dec 15, 6:04 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
> wrote:
…[50 more quoted lines elided]…
> Brian

Sorry, for completeness, this is a Compaq EVO Debian system
$ uname -a
Linux homenode 2.6.26-1-686 #1 SMP Wed Nov 26 19:14:11 UTC 2008 i686
GNU/Linux

Thanks to Paul for reminding me that architecture matters. :)

Cheers,
Brian Tiffin
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2008-12-15T21:40:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49472318$0$5484$bbae4d71@news.suddenlink.net>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
On 2008-12-15 17:04:58 -0600, "William M. Klein" 
<wmklein@nospam.ix.netcom.com> said:

>        Identification Division.
>         Program-ID. OVERLAP2.
…[181 more quoted lines elided]…
>             .

Well, it reports success under OpenVMS 8.3 on Itanium, but the results 
look - odd:
(HP compiler)

$ run test1
 --> Start ADD test
ADD Test passed, Num2=0Q
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=5M
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=4O
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=1J
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=1J
                    Num3=D
 -->   End DIVIDE test 2

and under OpenCobol 1.1 compiled for Itanium
paul@ilin110:~/cobsrc> ./test1
 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2


and under OpenCOBOL 1.1 compiled for MacOS (PowerPC)
kermit:~/cobsrc Paul$ ls
test1		test1.cbl
kermit:~/cobsrc Paul$ ./test1
 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2

And to be a little different, under MPE/IX using the MPE/IX COBOL compiler...
LinkEd> link test1.obj,test1.bin
 
:run test1.bin

 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2

END OF PROGRAM



Because of the really odd results on OpenVMS Itanium, I will go power 
up an OpenVMS Alpha machine and try it there. I can run it against a 
few other compilers as well, if nobody else does. :)

-Paul
```

##### ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-15T23:07:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CIG1l.100099$5i4.7863@en-nntp-05.dc1.easynews.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net>`

```
The "odd" results on VMS are not really "odd".  The Standard doesn't tell HOW a 
compiler is supposed to DISPLAY signed numeric fields.  IBM also does "funny" 
things with these displays.  They "combine" the number and the sign-nibble and 
display it as an alphabetic.

This is "conforming" and as the value shows as "passed" this is OK.
```

###### ↳ ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2008-12-16T00:05:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4947452c$0$5491$bbae4d71@news.suddenlink.net>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net> <CIG1l.100099$5i4.7863@en-nntp-05.dc1.easynews.com>`

```
On 2008-12-15 23:07:48 -0600, "William M. Klein" 
<wmklein@nospam.ix.netcom.com> said:

> The "odd" results on VMS are not really "odd".  The Standard doesn't tell HOW a
> compiler is supposed to DISPLAY signed numeric fields.  IBM also does "funny"
…[3 more quoted lines elided]…
> This is "conforming" and as the value shows as "passed" this is OK.

I wondered!  Thanks for that explanation. -Paul
```

###### ↳ ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-16T09:45:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kmmfk4tpsafut2kaj14io6lf4a54afoolb@4ax.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net> <CIG1l.100099$5i4.7863@en-nntp-05.dc1.easynews.com>`

```
On Mon, 15 Dec 2008 23:07:48 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>The "odd" results on VMS are not really "odd".  The Standard doesn't tell HOW a 
>compiler is supposed to DISPLAY signed numeric fields.  IBM also does "funny" 
…[3 more quoted lines elided]…
>This is "conforming" and as the value shows as "passed" this is OK.

Switching between IBM, Univac 1100 and Burroughs I remember having to
change my display syntax - but I forget what syntax I needed for
displays at this date.
```

###### ↳ ↳ ↳ Re: Anoterh test request (overlapping oerands again)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-16T11:32:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oCR1l.348509$6p1.200467@en-nntp-07.dc1.easynews.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net> <CIG1l.100099$5i4.7863@en-nntp-05.dc1.easynews.com> <kmmfk4tpsafut2kaj14io6lf4a54afoolb@4ax.com>`

```
In general, if you want to MAKE CERTAIN that a "signed" numeric gets DISPLAYed 
correctly, you need to move it to a numeric-edited field first - or (I think) 
use the SIGN IS SEPARATE clause.
```

###### ↳ ↳ ↳ Re: Anoterh test request (overlapping oerands again)

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-16T10:44:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r5qfk4tlhes9cqrburtkueokml6qeu3c81@4ax.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net> <CIG1l.100099$5i4.7863@en-nntp-05.dc1.easynews.com> <kmmfk4tpsafut2kaj14io6lf4a54afoolb@4ax.com> <oCR1l.348509$6p1.200467@en-nntp-07.dc1.easynews.com>`

```
On Tue, 16 Dec 2008 11:32:03 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>In general, if you want to MAKE CERTAIN that a "signed" numeric gets DISPLAYed 
>correctly, you need to move it to a numeric-edited field first 

That will always work.    Some compilers translate for you though.

>- or (I think) use the SIGN IS SEPARATE clause.

I doubt if that will always work.
```

##### ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-12-22T20:57:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1230004354_12@isp.n>`
- **In-Reply-To:** `<49472318$0$5484$bbae4d71@news.suddenlink.net>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49472318$0$5484$bbae4d71@news.suddenlink.net>`

```
Paul wrote:
> On 2008-12-15 17:04:58 -0600, "William M. Klein" 
> <wmklein@nospam.ix.netcom.com> said:
> 
>>        Identification Division.
[snipped]
> Well, it reports success under OpenVMS 8.3 on Itanium, but the results 
> look - odd:
…[18 more quoted lines elided]…
> -->   End DIVIDE test 2
[snipped]
> Because of the really odd results on OpenVMS Itanium, I will go power up 
> an OpenVMS Alpha machine and try it there. I can run it against a few 
> other compilers as well, if nobody else does. :)
> 
> -Paul

Paul, see for DISPLAY ... WITH CONVERSION
<http://h71000.www7.hp.com/doc/82final/6296/6296pro_063.html#display_com>

Jeff





----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Robert <no@e.mail>
- **Date:** 2008-12-15T23:45:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cecek49tch1fo1pn4d7psmbkpdole04o7h@4ax.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
On Mon, 15 Dec 2008 17:04:58 -0600, "William M. Klein" <wmklein@nospam.ix.netcom.com>
wrote:

>If all the test pass, just let me know which compiler you have tested with. 

All tests passed under Funitsu v3.0 (V30L10).
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2008-12-16T08:54:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49475eb9$0$2846$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
Bill,
here are the results :

C:\COBOL\CobolIT\samples>overlap
 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2

cobc (COBOL-IT) 1.0.0 Build date Oct  2 2008 18:17:06
Based on Keisuke Nishida / Roger While Open-COBOL
Open-COBOL Copyright (C) 2001-2008 Keisuke Nishida / Roger While
Copyright (C) 2008 CobolIT

Regards,

Alain
```

##### ↳ ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2008-12-16T09:40:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49476998$0$2847$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<49475eb9$0$2846$ba620e4c@news.skynet.be>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com> <49475eb9$0$2846$ba620e4c@news.skynet.be>`

```
And also :

 --> Start ADD test
ADD Test passed, Num2=-08
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=-54
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=-46
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                    Num3=+4
 -->   End DIVIDE test 2

with
cobc (COBOL-IT) 1.2.4.0 Build date Nov 27 2008 13:05:10
Based on Keisuke Nishida / Roger While Open-COBOL
Open-COBOL Copyright (C) 2001-2008 Keisuke Nishida / Roger While
Copyright (C) 2008 CobolIT

both are under Vista Pro SP1.

Regards


Alain Reymond a ï¿½crit :
> Bill,
> here are the results :
…[27 more quoted lines elided]…
>
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-12-16T09:14:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gi7o1a$pab$1@nntp.fujitsu-siemens.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> schrieb im Newsbeitrag 
news:woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com...
> The Standard ('85, '02, whatever) has rules for overlapping operand 
> operations being undefined.  I have found (thanks to CLC people) that 
…[10 more quoted lines elided]…
> me know that as well).

Test results with Fujitsu Siemens Compiler COBOL2000 V1.4B under BS2000 OSD 
V8.0 operating system:

 --> Start ADD test
ADD Test passed, Num2=0Q
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=5M
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=4O
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=1J
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=1J
                    Num3=4
 -->   End DIVIDE test 2

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-12-16T11:43:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DMR1l.24576$hs1.3393@newsfe04.iad>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com...
> The Standard ('85, '02, whatever) has rules for overlapping operand
operations
> being undefined.  I have found (thanks to CLC people) that results DO
differed
> for "SET" statements.  I am now interested in arithmetic statements.  I
would
> appreciate CLC people testing the following ('85 Standard conforming)
program
> with your "compiler of choice" (with compiler options/directives "of
choice")
> and letting me know if all 5 tests display a "pass" message.
>
> If all the test pass, just let me know which compiler you have tested
with.  If
> any of them FAIL, I would be interested in the compiler and what results
you
> get.
> (I don't think there should be any "compile-time errors" - but if so, let
me
> know that as well).
>
>

VISUAL COBOL Compiler
 Version  2.10 (MS-DOS)
Copyright (C) 1987,1989 mbp Software & Systems
 XXXXXXXXXX    No Error(s)/Warning(s) found
    No Error(s) found,    No Warning(s) issued
 Compilation finished



:C:\My Documents>overlap2
 --> Start ADD test
ADD Test passed, Num2= 8-
 -->   End ADD test
 --> Start Subtract test
SUBTRACT Test passed, Num2=54-
 -->   End Subtract test
 --> Start Multiply test
MULTIPLY Test passed, Num2=46-
 -->   End MULTIPLY test
 --> Start DIVIDE test 1
DIVIDE Test passed, Num2=11-
 -->   End DIVIDE test 1
 --> Start DIVIDE test 2
DIVIDE Test passed, Num2=11-
                    Num3= 4
 -->   End DIVIDE test 2
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-12-17T04:53:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cB%1l.80574$_Y1.13210@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
William M. Klein wrote:
> The Standard ('85, '02, whatever) has rules for overlapping operand operations 
> being undefined.  I have found (thanks to CLC people) that results DO differed 
…[9 more quoted lines elided]…
> know that as well).

Passed all tests with the following:

********************************* TOP OF DATA ******
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
     XREF(FULL)
     YEARWINDOW(1900)
     ZWB
PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1


********************************* TOP OF DATA *******************
  --> Start ADD test
ADD Test passed, Num2=0Q
  -->   End ADD test
  --> Start Subtract test
SUBTRACT Test passed, Num2=5M
  -->   End Subtract test
  --> Start Multiply test
MULTIPLY Test passed, Num2=4O
  -->   End MULTIPLY test
  --> Start DIVIDE test 1
DIVIDE Test passed, Num2=1J
  -->   End DIVIDE test 1
  --> Start DIVIDE test 2
DIVIDE Test passed, Num2=1J
                     Num3=D
  -->   End DIVIDE test 2
Options Report for Enclave OVERLAP2 12/16/08 10:14:05 AM
Language Environment V01 R08.00

Please forgive me for omitting the the LE options report.  It was even 
longer than the COBOL options report.
```

#### ↳ Re: Anoterh test request (overlapping oerands again)

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-12-22T20:42:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1230003415_10@isp.n>`
- **In-Reply-To:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`
- **References:** `<woB1l.347451$6p1.210393@en-nntp-07.dc1.easynews.com>`

```
William M. Klein wrote:
> The Standard ('85, '02, whatever) has rules for overlapping operand operations 
> being undefined.  I have found (thanks to CLC people) that results DO differed 
…[10 more quoted lines elided]…
> 
All 5 passed:

OpenVMS (TM) Alpha Operating System, Version V8.3 on node PWS600
Compaq COBOL V2.8-1286

$ cobo overlap2
$ link overlap2
$ run  overlap2

  --> Start ADD test
ADD Test passed, Num2= -8
  -->   End ADD test
  --> Start Subtract test
SUBTRACT Test passed, Num2=-54
  -->   End Subtract test
  --> Start Multiply test
MULTIPLY Test passed, Num2=-46
  -->   End MULTIPLY test
  --> Start DIVIDE test 1
DIVIDE Test passed, Num2=-11
  -->   End DIVIDE test 1
  --> Start DIVIDE test 2
DIVIDE Test passed, Num2=-11
                     Num3= 4
  -->   End DIVIDE test 2
$

Jeff


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
