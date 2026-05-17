[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading a PDS file in Cobol?

_13 messages · 11 participants · 1997-08_

---

### Reading a PDS file in Cobol?

- **From:** "eric bakke" <ua-author-8453873@usenetarchives.gap>
- **Date:** 1997-08-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

I need to read a PDS dataset (w/members) in a cobol program. Has anybody
done this and have some code examples on how to read the directory and
process its members??

Eric B.
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

Eric Bakke wrote in article
<5rvbn2$7ht$1.··.@exc··h.net>...
›  I need to read a PDS dataset (w/members) in a cobol program.  Has
› anybody
…[3 more quoted lines elided]…
› Eric B.

I did this years ago - the calling lanuage isn't important, but the calling
argument structure is. If I can find the code, I'll repost. Basically,
fill in the blanks of the structure and call a short assembler subroutine
which calls the system function needed to read/write a PDS member.

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

##### ↳ ↳ Re: Reading a PDS file in Cobol?

- **From:** "bill - netcom" <ua-author-17071652@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-01debbd9df-p2@usenetarchives.gap>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net> <gap-01debbd9df-p2@usenetarchives.gap>`

```

If we're talking IBM mainframe use the Library Management Facilities.
They are a set of callable functions that enable you to process PDS's,
members of PDS's etc.

Bill

Eugene A. Pallat wrote:

› Eric Bakke  wrote in article
› <5rvbn2$7ht$1.··.@exc··h.net>...
…[25 more quoted lines elided]…
› notice and will send a certified check forthwith.
```

##### ↳ ↳ Re: Reading a PDS file in Cobol?

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-01debbd9df-p2@usenetarchives.gap>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net> <gap-01debbd9df-p2@usenetarchives.gap>`

```

Eugene A. Pallat wrote:
› 
› Eric Bakke  wrote in article
…[17 more quoted lines elided]…
› Orion Data Systems

If you can find the code, I would be very interested in it as well.

Thanks in advance!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "steve cooney" <ua-author-907591@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

Eric Bakke wrote:
› 
›  I need to read a PDS dataset (w/members) in a cobol program.  Has anybody
…[3 more quoted lines elided]…
› Eric B.
Get a utilities manual for the system you are working on. Find the
utility that will write out the directory and all members to a listing
file. Direct the listing file to DASD. Read the listing file and parse
the data. This is a non-sophisticated way, i.e. reading a report file
and extracting the data you want.

A quick and dirty assembler program would be faster and easier.
Steve Cooney
st··.@se··p.com
http:/www.seadp.com
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "ann..." <ua-author-1626967@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```


You don't say how many members are expected. (give good specs- get
better answers).
Solution 1 for smaller/manageable number of members :
I would just set each member as a separate FD and let FD & JCL keep
track of them.
Soultion 2:
If you're trying to mass - edit the PDS- which I could assume has
many more members than solution 1 would help- there are utilities
which unfortunately I can't name (I know our tech area folks use them
all the time). Try your tech folks for advice. Cobol is not always the
best solution.

_______________________________________________________________
"Eric Bakke" wrote:

› I need to read a PDS dataset (w/members) in a cobol program.  Has anybody
› done this and have some code examples on how to read the directory and
…[5 more quoted lines elided]…
›
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "william lynch" <ua-author-97506@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

Eric wrote:

› need to read a PDS dataset (w/members) in a cobol program.  Has anybody
› done this and have some code examples on how to read the directory and
…[3 more quoted lines elided]…
› 

The reading of the PDS could easily be done in a REXX program and the data
passed to a Cobol for processing (one member at a time). I use this
technique when dealing with multiple Librarian members (copying/moving
source code). If you don't know REXX ask around your installation,
someone's bound to know it, or email me with your followup question(s).

Hope this is helpful
Bill Lynch
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "eric bakke" <ua-author-8453873@usenetarchives.gap>
- **Date:** 1997-08-04T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

Thanks for all of your bits of advice...I am well aware of the various
utilities, MVS/TSO, IBM, Fileaid, DYL280, REXX, etc., that can process PDSes
quickly and easily. The reason for wanting to use CoBOL is twofold...the
shop I work at discourages putting into production any program that isn't
written in CoBOL for maintainability reasons and the other is to be able to
use some of the Intinsic functions available in COBOL/370 as well as other
CoBOL specific features that simplify the tool that I'm trying to write. I
remember reading somewhere in IBM's Bookmanager how to do this but can't
find the doco.

Thanks for your help!

Eric Bakke wrote in article <5rvbn2$7ht$1.··.@exc··h.net>...

› I need to read a PDS dataset (w/members) in a cobol program.  Has anybody
› done this and have some code examples on how to read the directory and
…[5 more quoted lines elided]…
›
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "bill - netcom" <ua-author-17071652@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

The way you're supposed to read PDS's in COBOL (IBM mainframe TSO
environment) is with IBM's library management facilities - a set of
callable subroutines whose sole function is to manage PDS's (read
directory, list members in a directory, amend pds statistics (last
updates etc), read a member of a pds, copy a member of a pds.....)

Bill


Frederick Rust, IntraNet, Inc. wrote:

› In article <5rvbn2$7ht$1.··.@exc··h.net>, "Eric Bakke"
›  writes:
…[28 more quoted lines elided]…
› are easier and more reliable.
```

##### ↳ ↳ Re: Reading a PDS file in Cobol?

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-01debbd9df-p9@usenetarchives.gap>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net> <gap-01debbd9df-p9@usenetarchives.gap>`

```

Actually, you can use STOW and FETCH calls, and a number of other system
services from COBOL II, or from VS COBOL with a very small (like 10 lines)
assembler stub. This leaves the essential part of the logic in COBOL,
which I assume you would prefer. Dynamic allocate may also be the thing
for you here. The tricky part is making COBOL copybooks for system data
management blocks, and putting them into the LINKAGE section so you can
look at them (fortunately MVS does not let you actually *change* most of
these things from your program). Many of the things you used to need
assembler for can be done just by using Linkage section structures, and the
SET ADDRESS OF in COBOL II (in VS COBOL you write a little assembler stub
to do the SET ADDRESS OF - which I saw in the Consco Accounting Information
System I worked on years ago, who deserve the credit for the idea).

Using that sort of linkage, you map the DCB (which is a control block
generated from your FD), and some other things it points to, by something
like

DATA DIVISION.
FILE SECTION.
FD PDS-MEMBER-FILE ...

LINKAGE SECTION.
01 DCB-DSECT.
05 DCB-FIELD-1
05 DCB-FIELD-2
-------------- a bunch of fields --------------------
05 DCB-JFCB-POINTER PIC S9(08) COMP.
-------------- and a bunch of other fields --------------------

01 JFCB-DSECT.
05 JFCB-FIELD-1
05 JFCB-DSECT-2
-------------- and more fields --------------------
05 JFCB-FILENAME PIC X(44).
-------------- and still more --------------------

PROCEDURE DIVISION.
SET ADDRESS OF DCB-DSECT TO PDS-MEMBER-FILE.
SET ADDRESS OF JFCB-DSECT TO DCB-JFCB-POINTER.
MOVE 'YOUR.FILENAME(MEMBER)' TO JFCB-FILENAME.
OPEN PDS-MEMBER-FILE.

This, BTW, works in batch as well as TSO, where library management is not
available.

I do not have the DSECT mapping macros here to look at, so I can't be sure
of exactly which blocks you need, but I will try to research it tommorrow
at work (do not try to use the code above verbatim...). I will also bring
in the stub to do this with VS COBOL, and a stub to make an SVC call, if I
can find them. They are useful for things like getting the generation
number of a GDG, the blockisize, the volser, etc. for reporting after you
open the dataset, getting the JES ID-submit
date/time-jobname/stepname/procstepname, and a whole bunch of other simple
things you may want to know for which COBOL does not have special
registers. The truly scary programmer can even modify downstream steps of
their JCL on the fly (not recommended for beginners...)

Two warnings about this whole idea are in order. First, since you have to
make a COBOL structure for the system control blocks you wish to map, you
either need to understand enough assembler to translate from the DSECT
mapping macros, or use a logic manual (e.g., MVS SYSTEM DATA AREAS) to
construct it. Secondly, if IBM ever changes the block you have mapped
(rare for the published ones, but it does happen) you will have to update
your program accordingly. This is what products like SMP are meant to warn
you about, by registering what data areas you use, so when system
maintenance is applied you know what programs are affected. However, when
you go to your system programmer and say you want to register your COBOL
program as using something like the TCB DSECT map, he/she will probably
have your logon ID off the system before they start breathing again!

Bill - Netcom wrote in article
<33E··.@ix.··m.com>...
› The way you're supposed to read PDS's in COBOL (IBM mainframe TSO
› environment) is with IBM's library management facilities - a set of
…[43 more quoted lines elided]…
›
```

#### ↳ Re: Reading a PDS file in Cobol?

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1997-08-07T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p11@usenetarchives.gap>`
- **In-Reply-To:** `<5rvbn2$7ht$1@excalibur.flash.net>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net>`

```

Eric Bakke wrote:

›  I need to read a PDS dataset (w/members) in a cobol program.  Has
› anybody
…[4 more quoted lines elided]…
› Eric B.



I have only seen example on this in C/370, and it uses
"sprintf(ISPF_LM_command)"...
The same may probably be used in Cobol, but you must contact your
Sysprogs. or read manuals
to find how to link this with the ISPF load-libraries I guess...
It is basically a matter of using LMGET, LMOPEN etc.. from your
COBOL-prog..


Geir Knaplund
```

##### ↳ ↳ Re: Reading a PDS file in Cobol?

- **From:** "einar clementz" <ua-author-6588781@usenetarchives.gap>
- **Date:** 1997-08-09T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-01debbd9df-p11@usenetarchives.gap>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net> <gap-01debbd9df-p11@usenetarchives.gap>`

```

Geir Knaplund wrote:
› 
› Eric Bakke wrote:
…[17 more quoted lines elided]…
› Geir Knaplund


Yes, thats all through. COBOL and ISPF services work very well together.
I have used ISPF from COBOL, it's just to know the rigth API's. Look in
the ISPF manuals concerning library services. There you find COBOL
examples for all ISPF API's. Or you can use the MODEL command in the
ISPF edit and you get examples into your edit session.
At Link-time and run-time you need the ISPF libraries available.


Einar Clementz
Oslo, Norway
email: ecl··.@onl··e.no
```

###### ↳ ↳ ↳ Re: Reading a PDS file in Cobol?

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-08-10T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-01debbd9df-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-01debbd9df-p12@usenetarchives.gap>`
- **References:** `<5rvbn2$7ht$1@excalibur.flash.net> <gap-01debbd9df-p11@usenetarchives.gap> <gap-01debbd9df-p12@usenetarchives.gap>`

```

Einar Clementz wrote:
› 
› Geir Knaplund wrote:
…[30 more quoted lines elided]…
› email: ecl··.@onl··e.no

AFAIK you _do_ need an active ISPF environment to do this, which means
you'll have to execute your COBOL program from ISPF. In other words, by
running program IKJEFT01 or equivalent with ISPSTART PGM(yerpgm) etc..
Not that there's anything wrong with this, but I thought it needed
mentioning 'cause you do need a lot of extra JCL to do this.
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
