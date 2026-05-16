[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What are the test results ?

_20 messages · 14 participants · 2008-05 → 2008-06_

---

### What are the test results ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-07T22:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
I would like to know what the results are from compiling and running the 
following source code on as many compilers/platforms as possible.  (I don't 
think it should mater about compiler options/directives - although the Micro 
Focus BYTEMOVE *might* impact it.)  I believe this is '85 Standard conforming so 
it should compile (and run) on most systems.

If you want to, you can reply to me off-line or via CLC.
 (leading spaces may be funny - because of font changes - check for A-/B-margin 
correctness)

        Identification Division.
         Program-ID. OverLapI.
        Data Division.
         Working-Storage Section.
        01  Test-Ind1.
              05 Save-Index Usage Index.
        01  Group1.
              05  Group1a.
                   10  Ind1 Usage Index.
                   10  Filler Pic X.
             05  Group1b redefines Group1a.
                   10  Filler Pic X.
                   10  Test-Ind2.
                         15  Ind2 Usage Index.
        01  Group2.
              05  Tabl.
                     10  Each-Row occurs 345 times
                             indexed by IndA IndB.
                           15 Elem Pic X(33).
        Procedure Division.
         Mainline.
            Move all "N" to Tabl
            Move spaces to Group1
            Set IndB to 1
            Set IndA to 267
            Set Save-Index to IndA
            Move all "Y" to Elem (IndA)
            Set Ind1 to IndA
            Set Ind2 to Ind1
            If Test-Ind1 = Test-Ind2
                Display "Bytes Match"
            Else
                Display "Bytes do NOT match"
            End-If
            Set IndB to Ind2
            If IndA = IndB
                Display "Index values match"
            Else
                Display "index values do NOT match"
            End-If
            Stop Run
               .
```

#### ↳ Re: What are the test results ?

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-05-07T17:16:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eccb5b17-928a-44a0-a983-da06d05fb56b@j33g2000pri.googlegroups.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On May 8, 10:00 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I would like to know what the results are from compiling and running the
> following source code on as many compilers/platforms as possible.  

Fujitsu 7 for Linux:

Bytes Match
Index values match
```

#### ↳ Re: What are the test results ?

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-07T20:25:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jl424de8hvjc1emgahrnoc6kd4m4anshd@4ax.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On Wed, 07 May 2008 22:00:45 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>I would like to know what the results are from compiling and running the 
>following source code on as many compilers/platforms as possible.  (I don't 
>think it should mater about compiler options/directives - although the Micro 
>Focus BYTEMOVE *might* impact it.)  I believe this is '85 Standard conforming so 
>it should compile (and run) on most systems.

Fujitsu says both match.
```

#### ↳ Re: What are the test results ?

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-07T21:12:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On Wed, 07 May 2008 22:00:45 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>I would like to know what the results are from compiling and running the 
>following source code on as many compilers/platforms as possible.  (I don't 
>think it should mater about compiler options/directives - although the Micro 
>Focus BYTEMOVE *might* impact it.)  I believe this is '85 Standard conforming so 
>it should compile (and run) on most systems.

Realia 16 bit says:
Bytes do NOT match
Index values match

test-ind1 = 4a220000    
test-ind2 = 4a222020

The group names embrace two synchronization bytes.
```

##### ↳ ↳ Re: What are the test results ?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-05-08T05:48:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com>`

```
Robert wrote:
> On Wed, 07 May 2008 22:00:45 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
> 
…[13 more quoted lines elided]…
> The group names embrace two synchronization bytes. 

I can confirm these results on probably a different Realia compiler 
from around 1990.

Realia COBOL Educational Version 1.00      C:OVERLAPI.COB

LINE LVL                       ERROR TEXT

    4 W SOURCE-COMPUTER paragraph assumed before 'WORKING-STORAGE'
    4 W OBJECT-COMPUTER paragraph assumed before 'WORKING-STORAGE'
   22 W Improper quote character accepted in column 22
   27 W Improper quote character accepted in column 22
   31 W Improper quote character accepted in column 25
   33 W Improper quote character accepted in column 25
   37 W Improper quote character accepted in column 25
   39 W Improper quote character accepted in column 25

overlapi has   8 Warning  messages

Bytes do NOT match
Index values match

If I can find the time this week, I'll try it with Enterprise COBOL 
for z/OS and let you know what happens.
```

###### ↳ ↳ ↳ Re: What are the test results ?

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-05-08T21:41:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com> <GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net...
> Robert wrote:
>> On Wed, 07 May 2008 22:00:45 GMT, "William M. Klein" 
…[42 more quoted lines elided]…
> http://arnold.trembley.home.att.net/

On Enterprise COBOL for z/OS I got:

Bytes match
Index values match

I got a warning on the ELSE that the code could not be reached.
```

###### ↳ ↳ ↳ Re: What are the test results ?

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-05-13T07:12:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wbbWj.197235$D_3.189382@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com> <GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net> <RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
> news:GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net...
…[49 more quoted lines elided]…
> I got a warning on the ELSE that the code could not be reached.

You beat me to it.  Here's the gory details:

PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1 
    Date 05/12/2008  Time 10:23:33   Page     1

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
PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1 
     Date 05/12/2008  Time 10:23:33   Page     2

     NOWORD
       XREF(FULL)
       YEARWINDOW(1900)
       ZWB

(snip the boring stuff)

PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1 
OVERLAPI  Date 05/12/2008  Time 10:23:33   Page    12

LineID  Message code  Message text

     33  IGYOP3091-W   Code from "DISPLAY (line 33.01)" to "DISPLAY 
(line 33.01)" can never be executed and was therefore discarded.


Messages    Total    Informational    Warning    Error    Severe 
Terminating

Printed:       1                          1


* Statistics for COBOL program OVERLAPI:
*    Source records = 42
*    Data Division statements = 12
*    Procedure Division statements = 16

End of compilation 1,  program OVERLAPI,  highest severity 4.

Return code 4

(and now for the execution):


BYTES MATCH
INDEX VALUES MATCH

Options Report for Enclave OVERLAPI 05/12/08 10:23:53 AM
Language Environment V01 R08.00

*****************

I skipped the Language Environment storage report.  If anyone is 
really interested in that, please email me.

I don't know why they say COBOL is verbose...
```

###### ↳ ↳ ↳ Re: What are the test results ?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-13T18:26:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3lWj.725738$Gl5.124163@fe02.news.easynews.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com> <GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net> <RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com> <wbbWj.197235$D_3.189382@bgtnsc05-news.ops.worldnet.att.net>`

```
Arnold,
   Could you (or someone else with Enterprise COBOL) try it with NOOPT 
specified?  I know that will get rid of the warning message, but I don't THINK 
it will change the run-time results.
```

###### ↳ ↳ ↳ Re: What are the test results ? (Enterprise COBOL with NOOPT)

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-05-15T06:47:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M%QWj.337645$cQ1.187044@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<g3lWj.725738$Gl5.124163@fe02.news.easynews.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com> <GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net> <RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com> <wbbWj.197235$D_3.189382@bgtnsc05-news.ops.worldnet.att.net> <g3lWj.725738$Gl5.124163@fe02.news.easynews.com>`

```
William M. Klein wrote:
> Arnold,
>    Could you (or someone else with Enterprise COBOL) try it with NOOPT 
> specified?  I know that will get rid of the warning message, but I don't THINK 
> it will change the run-time results.
> 

It does eliminate the compile time messages, but it also changes the 
run-time results:

PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1 
    Date 05/14/2008  Time 11:31:02   Page     1

Invocation parameters:
XREF(FULL),NORENT,X(FULL)

PROCESS(CBL) statements:
        PROCESS NOOPT

(elisions)

* Statistics for COBOL program OVERLAPI:
*    Source records = 42
*    Data Division statements = 12
*    Procedure Division statements = 16

End of compilation 1,  program OVERLAPI,  no statements flagged.

Return code 0

(and now for the execution...)

BYTES DO NOT MATCH
INDEX VALUES DO NOT MATCH

Options Report for Enclave OVERLAPI 05/14/08 11:31:51 AM
Language Environment V01 R08.00

(storage report snipped for brevity)

*************

I inadvertently converted the entire source file to upper-case, but I 
don't think that affects anything in the tun-time test results other 
than the displayed messages being in upper case.
```

###### ↳ ↳ ↳ Re: What are the test results ? (Enterprise COBOL with NOOPT)

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-05-15T09:46:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<482C068F.6F0F.0085.0@efirstbank.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <k7n424pek1e3gcvhr1edj095jjul6k5ug5@4ax.com> <GuwUj.305057$cQ1.11746@bgtnsc04-news.ops.worldnet.att.net> <RrOdnSK0z-JONr7VnZ2dnUVZ_tuonZ2d@earthlink.com> <wbbWj.197235$D_3.189382@bgtnsc05-news.ops.worldnet.att.net> <g3lWj.725738$Gl5.124163@fe02.news.easynews.com> <M%QWj.337645$cQ1.187044@bgtnsc04-news.ops.worldnet.att.net>`

```
>>> On 5/15/2008 at 12:47 AM, in message
<M%QWj.337645$cQ1.187044@bgtnsc04-news.ops.worldnet.att.net>, Arnold
Trembley<arnold.trembley@worldnet.att.net> wrote:
> William M. Klein wrote:
>> Arnold,
>>    Could you (or someone else with Enterprise COBOL) try it with NOOPT 
>> specified?  I know that will get rid of the warning message, but I don't

> THINK 
>> it will change the run-time results.
…[33 more quoted lines elided]…
> (storage report snipped for brevity)

This is the same for VSE.  My original run had NOOPT, and I got both "do not
match".
With OPT both match.
And in fact I also get the following warning:

  000030         000031     If Test-Ind1 = Test-Ind2                        
                      5 13
  000031      1  000032         Display "Bytes Match"                       
                          
  000032         000033     Else                                            
                          
  000033      1  000034         Display "Bytes do NOT match"                
                          
                                                                            
                          
==000033==> IGYOP3091-W CODE FROM "DISPLAY (LINE 33.01)" TO "DISPLAY (LINE
33.01)" CAN NEVER BE        
                        EXECUTED AND WAS THEREFORE DISCARDED.               
                          


Frank
```

#### ↳ Re: What are the test results ?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-07T22:48:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yOWdnb6vy7-N97_VnZ2dnUVZ_qGknZ2d@mid-floridainternet>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:gEpUj.141986$XH2.60405@fe03.news.easynews.com...
> I would like to know what the results are from compiling and running the
> following source code on as many compilers/platforms as possible.

Micro Focus COBOL Version 3.2.50 [DOS]
Microsoft Windows 2000 [Version 5.00.2195]
-----
Bytes do NOT match
index values do NOT match
-----
```

#### ↳ Re: What are the test results ?

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-05-07T22:19:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fluUj.1993$tM1.1510@newsfe20.lga>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
Here's an oldie: MBP Visual Cobol v2.10 (for DOS) (c) 1989:

complied clean,

Bytes match
Index values match

PL
```

#### ↳ Re: What are the test results ?

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-05-08T10:43:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvvdkq02is4@news5.newsguy.com>`
- **In-Reply-To:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
William M. Klein wrote:
> I would like to know what the results are from compiling and running the 
> following source code on as many compilers/platforms as possible.  (I don't 
…[3 more quoted lines elided]…
> 

Micro Focus Net Express 5.0 WS04:

	Bytes do NOT match
	index values do NOT match

with or without BYTEMODEMOVE (which I assume is the directive you're 
referring to).
```

#### ↳ Re: What are the test results ?

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-05-08T10:20:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4822D3F8.6F0F.0085.0@efirstbank.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
Bytes do NOT match       
index values do NOT match

IBM COBOL FOR VSE/ESA 1.1.1

n 5/7/2008 at 4:00 PM, in message
<gEpUj.141986$XH2.60405@fe03.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
> I would like to know what the results are from compiling and running the 
> following source code on as many compilers/platforms as possible.  (I 
…[53 more quoted lines elided]…
>                .
```

#### ↳ Re: What are the test results ?

- **From:** Blondie <gordcrawshaw@hotmail.com>
- **Date:** 2008-05-08T12:54:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<895dc45c-f9c4-4759-9f97-6a1895785920@d1g2000hsg.googlegroups.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
Net Express V 3.1.11 on Windows XP Pro

Bytes do NOT match
index values do NOT match
```

#### ↳ Re: What are the test results ?

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-05-08T22:41:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1210307578_1883@isp.n>`
- **In-Reply-To:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
William M. Klein wrote:
> I would like to know what the results are from compiling and running the 
> following source code on as many compilers/platforms as possible.  (I don't 
…[6 more quoted lines elided]…
> correctness)

[snipped]

OpenVMS (TM) Alpha Operating System, Version V8.3
Compaq COBOL V2.8-1286

$ run overlapi
Bytes Match
Index values match
$


Jeff


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

#### ↳ Re: What are the test results ?

- **From:** "Crebassa.Gilles@gmail.com" <Crebassa.Gilles@gmail.com>
- **Date:** 2008-05-09T02:00:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19d7c74b-bc27-46e9-8b36-3b9efd27009a@d1g2000hsg.googlegroups.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On May 8, 12:00 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I would like to know what the results are from compiling and running the
> following source code on as many compilers/platforms as possible.  (I don't
…[53 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

./uname -a
AIX CW5 2 5

./cobc -version
cobc (OpenCOBOL) 1.1.0 Build date Apr 23 2008 09:10:17
Copyright (C) 2001-2008 Keisuke Nishida / Roger While


./cobtest
Bytes Match
Index values match
```

##### ↳ ↳ Re: What are the test results ?

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2008-05-12T09:42:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lHYVj.284$hJ5.7@nlpi068.nbdc.sbc.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com> <19d7c74b-bc27-46e9-8b36-3b9efd27009a@d1g2000hsg.googlegroups.com>`

```
<Crebassa.Gilles@gmail.com> wrote in message 
news:19d7c74b-bc27-46e9-8b36-3b9efd27009a@d1g2000hsg.googlegroups.com...
> On May 8, 12:00 am, "William M. Klein" <wmkl...@nospam.netcom.com>
> wrote:
>> I would like to know what the results are from compiling and running the
>> following source code on as many compilers/platforms as possible.

RM/COBOL Version 11.01 for 32-Bit Windows:

Bytes Match
Index values match

Compiles with syntax error:
361: E Size of redefinition exceeds size of item referred to by REDEFINES 
clause:   GROUP1B OF GROUP

This is due to auto-synchronization of the index data items.

Robert Heady
Liant Software
```

#### ↳ Re: What are the test results ?

- **From:** charles.goodman@bell.ca
- **Date:** 2008-06-03T13:32:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd449519-499e-4299-b744-d3f1af4593f1@b9g2000prh.googlegroups.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On May 7, 5:00 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I would like to know what the results are from compiling and running the
> following source code on as many compilers/platforms as possible.  (I don't

Bill, here is an other.....

228$ cob -v OVERLAPI.CBL
cob -vC warning=2 notrunc spzero nolist -v OVERLAPI.CBL
* Micro Focus COBOL for Unix         V3.1 revision 060 Compiler
* Copyright (C) 1984-1994 Micro Focus Ltd.     URN AXCGG/ZZ0/00000A
* Accepted - VERBOSE
* Accepted - WARNING(2)
* Accepted - NOTRUNC
* Accepted - SPZERO
* Accepted - NOLIST
* Compiling OVERLAPI.CBL
* Total Messages:     0
* Data:       12424     Code:         222
229$ cobrun OVERLAPI
Bytes do NOT match
index values do NOT match
230$
```

#### ↳ Re: What are the test results ?

- **From:** charles.goodman@bell.ca
- **Date:** 2008-06-03T13:47:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ea9fdf7-1b8a-49fe-ab28-d9a681ddce38@l17g2000pri.googlegroups.com>`
- **References:** `<gEpUj.141986$XH2.60405@fe03.news.easynews.com>`

```
On May 7, 5:00 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I would like to know what the results are from compiling and running the
> following source code on as many compilers/platforms as possible.  (I don't

and one more.....


Linux xxx.xxxxxxxx.com 2.6.18-53.el5PAE #1 SMP Wed Oct 10 16:48:18 EDT
2007 i686 i686 i386 GNU/Linux

NetCOBOL V7.0L10

$cobol -dy -M -P OVERLAPI.lst -WC,"SOURCE,COPY,XREF,BINARY(BYTE)" -o
OVERLAPI OVERLAPI.CBL
STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
$./OVERLAPI
Bytes Match
Index values match


Best Regards,

Charlie
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
