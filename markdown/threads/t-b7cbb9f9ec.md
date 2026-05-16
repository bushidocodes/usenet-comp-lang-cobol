[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Keeping Files Open after program termination in IBM COBOL?

_23 messages · 17 participants · 2004-08 → 2004-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Keeping Files Open after program termination in IBM COBOL?

- **From:** "Michael A. Newell, WB4HUC" <mike.newell@sas.com>
- **Date:** 2004-08-27T14:31:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```
Hello,

Is there any way to force a file NOT to be closed when a 
COBOL batch program ends?

This particular program may be called many times. The
first time it's called it opens a sequential output report
file, writes the headings and one detail line for the 
record that it processed, then it ends via a GOBACK
statement.

The next time the program is called it knows this isn't
the first time, so it just tries to write the output line
for the record it processed, but I get an error because
it's trying to write to a file that isn't open.

I need the file to stay open between invocations of
the program, but according to the Enterprise COBOL
Programming Guide, the run-time environment will
close any open files during a normal program 
termination.

This COBOL program is a user exit within a
software package and is called by an assembler
module.

The environment is:

Z/OS 1.4
IBM Enterprise COBOL for z/OS and OS/390 3.1.1  
LE/370


Any help is appreciated.
```

#### ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-27T20:51:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H9NXc.280$8d1.194@newsread2.news.pas.earthlink.net>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```
You seem to be mixing apples and oranges - or I am confused by what you are 
saying.

Are you talking about a batch COBOL application where a main COBOL program calls 
(repeatedly) a COBOL subprogram - and it is the subprogram that does the File 
I/O
   OR
are you talking about the program that has the I/O actually doing a stop run?

   ***

It is true that a STOP RUN (or a GOBACK in a MAIN program) closes all files. 
See:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr20/6.2.36

However, this is NOT true for an EXIT PROGRAM (or GOBACK in a subprogram).  See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr20/6.2.16

The only exception to this is if the subprogram has the "IS INITIAL" clause in 
the Program-ID paragraph or if the main program (calling program) does a CANCEL 
of the subprogram.


"Michael A. Newell, WB4HUC" <mike.newell@sas.com> wrote in message 
news:be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com...
> Hello,
>
…[38 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** JD <nobody@dazoo.org>
- **Date:** 2004-08-28T14:32:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns95536B2F3C8A8dragonslayerdazooorg@38.144.126.79>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <H9NXc.280$8d1.194@newsread2.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in
news:H9NXc.280$8d1.194@newsread2.news.pas.earthlink.net: 

> You seem to be mixing apples and oranges - or I am confused by what you
> are saying.

How so?

> 
> Are you talking about a batch COBOL application where a main COBOL
…[5 more quoted lines elided]…
> 

Neither.  He specifically said an ASSEMBLER module made repeated calls to a 
COBOL module.

He also specifically said the COBOL module does a GOBACK, not a STOP RUN.

>    ***
> 
…[56 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-28T16:48:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VH2Yc.930$w%6.307@newsread1.news.pas.earthlink.net>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <H9NXc.280$8d1.194@newsread2.news.pas.earthlink.net> <Xns95536B2F3C8A8dragonslayerdazooorg@38.144.126.79>`

```
I did reply to an off-list note from the original poster, but just to clarify 
here:

- If you have an Assembler "driver" that repeatedly calls a COBOL program (in an 
IBM "MVS-ish" environment, possibly elsewhere), then one of two types of 
"environments" that may exist.

A) if you do nothing in the Assembler driver to "establish" a COBOL or LE 
environment, then each time the COBOL program is called, it is called as a 
"main" program - it establishes the COBOL (LE) environment at start up and tears 
it down when it exits.  In this environment, a GOBACK works like a STOP RUN, not 
like an EXIT PROGRAM.

B) If you take some "special" actions to establish the COBOL (LE) environment, 
then the first time you call a COBOL program it is placed in "initial state" and 
the 2nd thru Nth time, it is reached in "last used state". In this environment 
any GOBACK in the COBOL program works like an EXIT PROGRAM, not a STOP RUN. 
(Last used state leaves files as they were).

  ***

There are a number of discussions in the IBM documentation on how to establish 
the COBOL (LE) environment from an Assembler driver.  Among others are:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg20/APPENDIX1.4.7.2 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg20/3.3.11.2http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2150/5.3--Bill Klein wmklein <at> ix.netcom.com"JD" <nobody@dazoo.org> wrote in messagenews:Xns95536B2F3C8A8dragonslayerdazooorg@38.144.126.79...> "William M. Klein" <wmklein@nospam.netcom.com> wrote in> news:H9NXc.280$8d1.194@newsread2.news.pas.earthlink.net:>>> You seem to be mixing apples and oranges - or I am confused by what you>> are saying.>> How so?>>>>> Are you talking about a batch COBOL application where a main COBOL>> program calls (repeatedly) a COBOL subprogram - and it is the subprogram>> that does the File I/O>>    OR>> are you talking about the program that has the I/O actually doing a stop>> run?>>>> Neither.  He specifically said an ASSEMBLER module made repeated calls to a> COBOL module.>> He also specifically said the COBOL module does a GOBACK, not a STOP RUN.>>>    ***>>>> It is true that a STOP RUN (or a GOBACK in a MAIN program) closes all>> files. See:>>    http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr20/6.>>    2.36>>>> However, this is NOT true for an EXIT PROGRAM (or GOBACK in a>> subprogram).  See:>>   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr20/6.2>>   .16>>>> The only exception to this is if the subprogram has the "IS INITIAL">> clause in the Program-ID paragraph or if the main program (calling>> program) does a CANCEL of the subprogram.>>>>>> "Michael A. Newell, WB4HUC" <mike.newell@sas.com> wrote in message>> news:be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com...>>> Hello,>>>>>> Is there any way to force a file NOT to be closed when a>>> COBOL batch program ends?>>>>>> This particular program may be called many times. The>>> first time it's called it opens a sequential output report>>> file, writes the headings and one detail line for the>>> record that it processed, then it ends via a GOBACK statement.>>>>>> The next time the program is called it knows this isn't>>> the first time, so it just tries to write the output line>>> for the record it processed, but I get an error because>>> it's trying to write to a file that isn't open.>>>>>> I need the file to stay open between invocations of>>> the program, but according to the Enterprise COBOL>>> Programming Guide, the run-time environment will>>> close any open files during a normal program termination.>>>>>> This COBOL program is a user exit within a>>> software package and is called by an assembler module.>>>>>> The environment is:>>>>>> Z/OS 1.4>>> IBM Enterprise COBOL for z/OS and OS/390 3.1.1>>> LE/370>>>>>>>>> Any help is appreciated.>>>>>> -->>> Mike Newell>>> Austin, TX>>>>>>>>>>>>>>
```

#### ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2004-08-27T18:51:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ReWdnZWO6-ereLLcRVn-qQ@adelphia.com>`
- **In-Reply-To:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```
Michael A. Newell, WB4HUC wrote:

>Hello,
>
…[17 more quoted lines elided]…
>
Mike,
Your problem is that your COBOL subroutine looks like a main program to 
Language Environment (the run time which supports current IBM COBOL 
compilers).

I believe you need to do one of two things:
1.  Make the Assembler driver "LE-conforming", or
2.  Write a COBOL driver which invokes the Assembler program.  
(Procedure Div will just be a CALL and a GOBACK - you decide whether to 
make the CALL static or dynamic).

Either way, the COBOL "environment" gets set up, making the COBOL 
subroutine that is called by your Assembler program a subroutine in the 
Language Environment sense.  This will keep LE from trying to "clean up" 
when the subroutine executes the GOBACK, and will leave your file open 
to accept more output.

Start with this Web site:
http://www-306.ibm.com/software/awdtools/cobol/

Then, choose your compiler where you see "Select a product".  Click "Go" 
or press Enter, then you'll be taken to a page for your compiler (such 
as Enterprise COBOL for z/OS and OS/390) that shows several choices down 
the left side of the page.  Select for "Library", and download the PDF 
versions of the Migration Guide, Language Reference, and Programming 
Guide (at a minimum). 

Then, back up to the original page for your compiler and under "Related 
Software", choose "Language Environment".  Click on Library there, then 
select your OS/390 or z/OS version, and get the PDF versions of  the 
most likely manuals there.  I think you'll need at least the Programming 
Guide, to tell you how to make an Assembler program LE-compliant, then 
you'll need to go back for the Programming Reference to help you code 
the macros.  You may also want the Concepts Guide, and other manuals.

The Enterprise COBOL Migration Guide will talk about Assembler Language 
routine requirements and you can search for the term LE-conforming and 
get started learning about how to convert an Assembler driver to run 
under LE.  This should lead you to the required LE manuals.

I suggest the PDF versions because (1) you can read portions and do 
limited searches  online, and (2) you can print any part of a manual or 
the entire manual and have a learning tool.  NOTE: Be sure to find a 
printer with the "Duplex" feature for two-sided printing, and to print 
manuals in sections, like pages 1 - 100, so you don't tie up the printer 
for too long.

Your operating system comes with BookManager Read, and I hope your 
systems programmers have loaded a useful set of manuals in BookManager 
format.  If Enterprise COBOL, LE, and the like aren't there, ask that 
they be loaded.  This is an excellent place to go when you are searching 
for the facts on a known subject.  (It is not so good for learning a 
product from scratch.)

One other suggestion:
If you do not have IBM Debug Tool, try to get it, including the optional 
part (Utilities and Advanced Functions) that includes language 
conversion aids.  This is an excellent debugger, and is quite cost 
effective.  I believe it cost 10% of the cost of a debugger I'll call 
Brand X.
```

#### ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-28T08:00:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2m%Xc.30586$5s3.952@fe40.usenetserver.com>`
- **In-Reply-To:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```
Michael A. Newell, WB4HUC wrote:
> Hello,
> 
…[12 more quoted lines elided]…
> it's trying to write to a file that isn't open.

I've never worked on an IBM mainframe, but if it knows it's been called 
before, it could do an "Open Extend" on the file, as opposed to "Open 
Output".

> I need the file to stay open between invocations of
> the program, but according to the Enterprise COBOL
> Programming Guide, the run-time environment will
> close any open files during a normal program 
> termination.

The above doesn't meet that requirement, though.
```

##### ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-28T20:58:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1m6Yc.239619$M95.163306@pd7tw1no>`
- **In-Reply-To:** `<2m%Xc.30586$5s3.952@fe40.usenetserver.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <2m%Xc.30586$5s3.952@fe40.usenetserver.com>`

```
LX-i wrote:

> Michael A. Newell, WB4HUC wrote:
>
…[29 more quoted lines elided]…
>
OK Michael,

Let's see. Bill has already pointed you at the manuals - that's the way 
to go if you can do it. If anybody can figure this - it will be Bill - 
he knows roughly what I'm doing with OO.

Firstly I looked at an old M/F DOS example with an external filename - 
called a program to write a series of records and then called another 
program to read those records without any intervening CLOSE and re-OPEN. 
Without studying it not sure how it achieved that . Certainly the STOP 
RUN on exiting the demo program would automatically CLOSE any files.

IBM-wise Bill, could he do anything calling a File program with entry 
-points ? I'm thinking of OO where I have a separate class for a File 
which is invoked as necessary. In theory any class could open it.  (I've 
recently added a flag FileOpened/FileNotOpened, which of course allows 
you to check that you don't do a 'double' OPEN or CLOSE.). Even when I 
quit the Business Class that is using the File Class the file doesn't 
automatically get CLOSEd - I specifically have to invoke it to do that. 
Quitting the Master Menu jumps you to a STOP RUN which would CLOSE 
anything outstanding..

Now following on Michael's thoughts. He wants to pick up on this OPENed 
file in many spots in the batch processing. Assuming the entry-point 
technique would work, if it is the batch start program that does the 
opening/closing then can it treat the File as a sub-program via 
entry-points and can intermediary programs also access through those 
same entry-points, without clobbering the file when the intermediaries 
come to EXIT PROGRAM  ?

If Michael had the OO module for Enterprise - he might have a neat solution.

Jimmy, Calgary AB
```

#### ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-28T13:43:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-F4CDAD.13435228082004@knology.usenetserver.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```
In article <be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>,
 "Michael A. Newell, WB4HUC" <mike.newell@sas.com> wrote:

> Hello,
> 
…[38 more quoted lines elided]…
> 

Just don't close the file.  Normal termination processing will only 
occur at the end of the job step.

You might need to provide more info about the software package and the 
assembler module -- are they LE compliant?
```

#### ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "x.ray" <pasbon@noos.fr>
- **Date:** 2004-08-29T13:07:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com>`

```

"Michael A. Newell, WB4HUC" <mike.newell@sas.com> a ï¿½crit dans le message de
news:be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com...
> Hello,
>
…[28 more quoted lines elided]…
> LE/370


PROCEDURE DIVISION.

FIRST-TIME.
     GO TO OPEN-FILE.

OPEN-FILE.

    OPEN OUTPUT myfile.
    PERFORM WRITE-HEADER.
    ALTER FIRST-TIME TO PROCEED TO OTHER-TIMES.

OTHER-TIMES.

    PERFORM WRITE-DETAIL.

    GOBACK.

WRITE-HEADER.
    ...............
    EXIT.

WRITE-DETAIL.
    ..........
    EXIT.
```

##### ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-08-29T12:59:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KqkYc.8355$FV3.2800@newssvr17.news.prodigy.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net>`

```
> "Michael A. Newell, WB4HUC" <mike.newell@sas.com> a �crit dans le message
de
> news:be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com...
> > Hello,
> > This COBOL program is a user exit within a
> > software package and is called by an assembler
> > module.

You sure this software package is not issuing CANCEL or equivalent after
each EXIT call?

MCM
```

##### ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-29T09:43:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net>`

```
In article <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net>,
 "x.ray" <pasbon@noos.fr> wrote:
> 
> PROCEDURE DIVISION.
…[23 more quoted lines elided]…
> 


Wow...that is very quaint.  Why all the contortions and self-mutalating 
code?  Why not just a simple:

Procedure Division.

   If FIRST-TIME
      Perform Open-File
      Perform Write-Header
      Set OTHER-TIMES TO TRUE
   End-If

   Perform Write-Detail

   Goback.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-29T10:57:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:
> Wow...that is very quaint.  Why all the contortions and
> self-mutalating code?  Why not just a simple:
…[11 more quoted lines elided]…
>    Goback.

I always liked:

Procedure Division.
ON 1
     Perform Open-file
     Perform Write Header.
Perform Write-Detail.
Goback.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 4)_

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-08-29T16:40:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0408291540.5d09a386@posting.google.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com> <6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>...
> Joe Zitzelberger wrote:
> > Wow...that is very quaint.  Why all the contortions and
…[21 more quoted lines elided]…
> Goback.

I think you are missing the point made by Bill Klein earlier, that the
program is being terminated by the operating system after each call as
though it were a main program for the reasons he gave and that when a
program is terminated by the operating system as though it were an
independent run unit, then there is a clean up of resources that
includes closing all open files.

Robert
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 5)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-08-29T21:26:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xsvYc.5104$7i2.192058@news20.bellglobal.com>`
- **In-Reply-To:** `<6dd8322.0408291540.5d09a386@posting.google.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com> <6YqdnUGNIPmeYKzcRVn-vQ@giganews.com> <6dd8322.0408291540.5d09a386@posting.google.com>`

```
Robert Jones wrote:
> "JerryMouse" <nospam@bisusa.com> wrote in message news:<6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>...
> 
…[34 more quoted lines elided]…
> Robert

Don't use goback.  Change it to exit program, and it will not assume it 
is a mainline in the first place. Therefore the files will remain open. 
Everything else is irrelevant.

Donald.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-30T00:03:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408292303.60f73c0@posting.google.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com> <6YqdnUGNIPmeYKzcRVn-vQ@giganews.com> <6dd8322.0408291540.5d09a386@posting.google.com> <xsvYc.5104$7i2.192058@news20.bellglobal.com>`

```
Donald Tees <donald_tees@sympatico.ca> wrote

> Don't use goback.  Change it to exit program, and it will not assume it 
> is a mainline in the first place. Therefore the files will remain open. 
> Everything else is irrelevant.

Using an EXIT PROGRAM weon't change whether it thinks that it is a
main program or not.  What will happen is that if it thinks that it is
a main program the EXIT PROGRAM will act as a NULL statement and
execution will continue.  This may then drop down through the
remainder of the code until it 'falls off the end' of the source and
executes an implicit STOP RUN.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 5)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-29T22:40:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-42C649.22402129082004@knology.usenetserver.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com> <6YqdnUGNIPmeYKzcRVn-vQ@giganews.com> <6dd8322.0408291540.5d09a386@posting.google.com>`

```
In article <6dd8322.0408291540.5d09a386@posting.google.com>,
 rjones0@hotmail.com (Robert Jones) wrote:

> "JerryMouse" <nospam@bisusa.com> wrote in message 
> news:<6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>...
…[32 more quoted lines elided]…
> Robert

No, I caught that point.  I mentioned that it will only work if the 
callers are LE compliant.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-08-30T09:05:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v7qdnUntcYKTqa7cRVn-qA@giganews.com>`
- **References:** `<be2vi0puaareigi53qucc3nm9b2ba4daho@4ax.com> <4131b8f6$0$2360$79c14f64@nan-newsreader-07.noos.net> <joe_zitzelberger-29D8E7.09435829082004@knology.usenetserver.com> <6YqdnUGNIPmeYKzcRVn-vQ@giganews.com> <6dd8322.0408291540.5d09a386@posting.google.com>`

```
Robert Jones wrote:
> "JerryMouse" <nospam@bisusa.com> wrote in message
> news:<6YqdnUGNIPmeYKzcRVn-vQ@giganews.com>...
…[30 more quoted lines elided]…
> includes closing all open files.

No, I wasn't missing the point. I was re-writing the code I referenced.

I saw no need to comment on the original thread: how many ways can one say
the COBOL run-time closes all open files when there's no more COBOL to
execute? Who would have it any other way?

Maybe one could say this to the original-original-original poster: Use a
dummy COBOL front-end that calls the assembly-language routine in the first
place.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-09-02T04:04:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040902000426.03719.00000034@mb-m26.aol.com>`
- **References:** `<6dd8322.0408291540.5d09a386@posting.google.com>`

```
Maybe I missed something in the discussion here but if I remember the original
problem was an assembler program called a Cobol program which created a file
and then it got closed when the Cobol program ended and the poster wanted it to
stay open because the next time the Cobol program ran it wanted to write more
records.

If this is the case why isn't the output file  DISP=MOD?  This would allow more
records to be written to the same file...

Or...

Output file be a GDG and when needed as input use the file without bias and get
all GDG's and then create an empty one for the next days processing etc etc.

If I'm way off base I'll just retire to the dugout.

And for I think Joe Z...   ON 1 is still supported on the mainframe with OS/390
Cobol?
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-09-02T04:47:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FBxZc.543235$Gx4.74868@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<20040902000426.03719.00000034@mb-m26.aol.com>`
- **References:** `<6dd8322.0408291540.5d09a386@posting.google.com> <20040902000426.03719.00000034@mb-m26.aol.com>`

```


YukonMama wrote:
> (snip)
> And for I think Joe Z...   ON 1 is still supported on the mainframe with OS/390
> Cobol?

I think "ON 1 ..." went away with IBM VS COBOL II.  As far as I know, 
it was a non-standard IBM extension for testing.

Within the last year I had to recompile a program with Enterprise 
COBOL for z/OS that was last compiled with IBM OS/VS COBOL.  It had 
"ON 1 ..." in it and it would not compile clean.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-02T05:22:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7abdj0he3r1k0k3snc4shq2usjam7m8p6o@4ax.com>`
- **References:** `<6dd8322.0408291540.5d09a386@posting.google.com> <20040902000426.03719.00000034@mb-m26.aol.com>`

```
On 02 Sep 2004 04:04:26 GMT, yukonmama@aol.com (YukonMama) wrote:

>And for I think Joe Z...   ON 1 is still supported on the mainframe with OS/390
>Cobol?

That's New Cobol. Better to stick with the time-tested
WS01-FIRST-TIME-FLAG .

ASCII dumb question, getty dumb ANSI
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-09-02T05:29:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch6p5i$kda$1@panix5.panix.com>`
- **References:** `<6dd8322.0408291540.5d09a386@posting.google.com> <20040902000426.03719.00000034@mb-m26.aol.com>`

```
In article <20040902000426.03719.00000034@mb-m26.aol.com>,
YukonMama <yukonmama@aol.com> wrote:

[snip]

>And for I think Joe Z...   ON 1 is still supported on the mainframe with OS/390
>Cobol?

Right along with WRITE... AFTER POSITIONING, I believe, which might be a 
reason for Mr Zitzelberger using it as a response to an example which 
contained ALTER.

DD
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 7)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-09-09T01:47:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040908214721.22107.00003220@mb-m07.aol.com>`
- **References:** `<ch6p5i$kda$1@panix5.panix.com>`

```
>From: docdwarf@panix.com
>Date: 9/2/04 5:29 AM Eastern Daylight Time

>
>Right along with WRITE... AFTER POSITIONING, I believe, which might be a 
>reason for Mr Zitzelberger using it as a response to an example which 
>contained ALTER.
>

Aaaahhhh :)

WRITE AFTER POSITIONING the ALTERed furniture ON 1 side of the room with the
TRANSFORMation of the CORRESPONDING furniture on the other.

Gotcha.
```

###### ↳ ↳ ↳ Re: Keeping Files Open after program termination in IBM COBOL?

_(reply depth: 6)_

- **From:** JD <nobody@dazoo.org>
- **Date:** 2004-09-02T11:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns95584FDDAA5A1dragonslayerdazooorg@38.144.126.79>`
- **References:** `<6dd8322.0408291540.5d09a386@posting.google.com> <20040902000426.03719.00000034@mb-m26.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote in
news:20040902000426.03719.00000034@mb-m26.aol.com: 

> Maybe I missed something in the discussion here but if I remember the
> original problem was an assembler program called a Cobol program which
…[16 more quoted lines elided]…
> OS/390 Cobol?

Not only are you way off base, you are proposing a performance nightmare, 
especially if the guy is processing any significant number of transactions 
requiring calls to the COBOL subprogram.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
