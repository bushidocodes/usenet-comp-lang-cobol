[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# JCL, Cobol and "Call Parameters"

_49 messages · 12 participants · 2007-01 → 2007-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### JCL, Cobol and "Call Parameters"

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-01-24T03:56:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`

```
Hello,

we are in the evaluation phase of converting a bunch of applications to
MF/Cobol. The Programms work fine and right now I am trying to figure
out the best way to handle all this JCL-Stuff. Eg.

The JCL says :

* $$JOB JNM=REI-V94,DISP=D,CLASS=0,PRI=8
* $$LST CLASS=A,DISP=H,FNO=33AE,FCB=FCB000Z8,LST=B0E
// JOB ZAKMTE ---- UNVERFALLBARKEIT
// ASSGN SYS010,B0E
   LIBDEF *,SEARCH=ALLES.TEST
// EXEC VSB094,SIZE=512K
99  70000000 98000000
/*
/&
* $$EOJ

COBOL uses this :

       FILE-CONTROL.
           SELECT LISTFILE
                  ASSIGN TO SYS010-UR-3203-S.

So the Name of the Spool File is dynamically setted by the JCL. How do
I do this with a shell script or a call to the MF/Cobol Runtime
"runcob32".

For SYSIPT I have done the following. According to the JCL-Above

#!/bin/bash
echo "99  70000000 98000000" | ./VSB094

This is then used in COBOL with

       01  ACC-IPT1.
           05  FILLER                  PIC XXXX.
           05  VLK-VNR-BEGINN          PIC X(8).
           05  FILLER                  PIC X(1).
           05  VLK-VNR-ENDE            PIC X(8).

ACCEPT ACC-IPT1 FROM SYSIPT.

And I have the Parameters. But how to handle those filenames ?

Kind regards

Michael
```

#### ↳ Re: JCL, Cobol and "Call Parameters"

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-01-24T06:38:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1169649515.449950.244830@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`

```

> And I have the Parameters. But how to handle those filenames ?


cob32 -iv -C ASSIGN=EXTERNAL -o VSB390M.int VSB390M.cbl

and in the shell script

export SYS010UR3203S=filename.txt

does the job. Of course the ACCEPT has to be modified to

 SELECT LISTENDATEI
            ASSIGN TO SYS010UR3203S.
*           ASSIGN TO SYS010-UR-3203-S.

Because Unix does not want "-" in Environmentvariable names.
```

#### ↳ Re: JCL, Cobol and "Call Parameters"

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-01-24T15:08:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51q3mlF1lgdlrU2@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`

```
I don't have an answer, but I do have a comment.
You're converting from VSE to Micro Focus?  Traitor!

:-)

Oh, one other comment.  I believe Micro Focus has a product that will allow
you to keep you VSE JCL.  You might try contacting them.

Frank

michael.bierenfeld@web.de<michael.bierenfeld@web.de> 01/24/07 4:56 AM >>>
>Hello,
>
…[42 more quoted lines elided]…
>And I have the Parameters. But how to handle those filenames ?


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: JCL, Cobol and "Call Parameters"

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-01-26T04:12:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1169813541.926374.70560@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<51q3mlF1lgdlrU2@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net>`

```

> You're converting from VSE to Micro Focus?  Traitor!

As an act of compassion :-)

> Oh, one other comment.  I believe Micro Focus has a product that will allow
> you to keep you VSE JCL.  You might try contacting them.
>

I will keep this as an option. I have contacted a company which has
some sort of JCL-Interpreter. The MF/Stuff is somwhat to tightly
integrated into their stuff. This would lead from one addiction to
another.

Kind Regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-01-26T09:26:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51uoe5F1mclreU3@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com>`

```
michael.bierenfeld@web.de<michael.bierenfeld@web.de> 01/26/07 5:12 AM >>>
>
>> You're converting from VSE to Micro Focus?  Traitor!
…[3 more quoted lines elided]…
>> Oh, one other comment.  I believe Micro Focus has a product that will
allow
>> you to keep you VSE JCL.  You might try contacting them.
>>
…[4 more quoted lines elided]…
>another.

Seriously, though, I have to ask what type of VSE workload do you have that
you are migrating to MF and Unix?  Are you migrating just batch
applications, or CICS applications as well?  If CICS, what are you using on
the Unix side to run them?  Mainframe Express MTO?

We're not looking to move off of VSE, but sometimes (often) VSE seriously
pisses me off...

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 4)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2007-01-26T11:53:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46721$45ba321d$d066072d$28103@FUSE.NET>`
- **In-Reply-To:** `<51uoe5F1mclreU3@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net>`

```
Frank Swarbrick wrote:
> michael.bierenfeld@web.de<michael.bierenfeld@web.de> 01/26/07 5:12 AM >>>
>>> You're converting from VSE to Micro Focus?  Traitor!
…[19 more quoted lines elided]…
> Frank

Just curious:  What level of VSE are you using?  Have you checked the 
new z/VSE V4.1?
> http://www.ibm.com/common/ssi/rep_ca/3/897/ENUS207-003/ENUS207003.PDF

I'm not a VSE person.  I deal with z/OS exclusively. I'm just curious, 
and sometimes the most recent IBM announcements to not always make it to 
the people who need it most.
Carl
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-01-26T17:53:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51vm3nF1mea4aU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <46721$45ba321d$d066072d$28103@FUSE.NET>`

```
CG<Carl.Gehr.ButNoSPAMStuff@MCGCG.Com> 01/26/07 9:53 AM >>>
>Frank Swarbrick wrote:
>> michael.bierenfeld@web.de<michael.bierenfeld@web.de> 01/26/07 5:12 AM
…[13 more quoted lines elided]…
>> Seriously, though, I have to ask what type of VSE workload do you have
that
>> you are migrating to MF and Unix?  Are you migrating just batch
>> applications, or CICS applications as well?  If CICS, what are you using
on
>> the Unix side to run them?  Mainframe Express MTO?
>> 
>> We're not looking to move off of VSE, but sometimes (often) VSE
seriously
>> pisses me off...
>> 
…[8 more quoted lines elided]…
>the people who need it most.

Most of the new features of 4.1 are "system" type stuff.  No new COBOL stuff
(other than Y2K stuff nothing major in over ten years).  No new CICS stuff
(nothing in at least five years).

Anyway, we are on v 2.7, but going to 3.1 "any day now".  Hopefully soon
followed by 4.1, but I won't get my hopes up.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 4)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-09T08:55:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171040159.707445.177060@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<51uoe5F1mclreU3@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net>`

```
> Seriously, though, I have to ask what type of VSE workload do you have that
> you are migrating to MF and Unix?  Are you migrating just batch
> applications, or CICS applications as well?  If CICS, what are you using on
> the Unix side to run them?  Mainframe Express MTO?
>

It is not a question of workload. You dont find to many companies here
in Germany that do offer VSE support (outsourcing). On the other side
Software Development with "modern" Tools like Microfocus is different
than using VM/VSE Tools.

Yep we are planing to migrate CICS and Batch Jobs. For CICS its
planned to use MTO. Batch will be native Cobol with UC4 as Scheduling
system. JCL interpreted or ported to Shell Scripts (not decided yet)

Kind regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-09T17:12:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<534guoF1r0f5uU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com>`

```
michael.bierenfeld@web.de<michael.bierenfeld@web.de> 02/09/07 9:55 AM >>>
>> Seriously, though, I have to ask what type of VSE workload do you have
that
>> you are migrating to MF and Unix?  Are you migrating just batch
>> applications, or CICS applications as well?  If CICS, what are you using
on
>> the Unix side to run them?  Mainframe Express MTO?
>>
…[8 more quoted lines elided]…
>system. JCL interpreted or ported to Shell Scripts (not decided yet)

Sounds like an interesting project.  I'd be very interested to hear the
results once you are done.  I definitely find VSE to not be an ideal
environment often times.

What I meant by my question about workload is, do you consider your workload
(online and batch) to be "large"?  We are one of the largest VSE shops in
the world (workload-wise), from what I've heard.  We have a an IBM z9 BC,
model 2096-U02, running at 526 MIPS.  Any idea what size your VSE box is? 
One thing (among others) that I would worry about if moving to MF and Unix
would be performance.

Oh, another question.  What type of data access do you use on VSE?  VSAM? 
DB2?  DL/I?

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 6)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-12T05:11:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171285904.789486.46390@v45g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<534guoF1r0f5uU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net>`

```

> model 2096-U02, running at 526 MIPS.  Any idea what size your VSE box is?
> One thing (among others) that I would worry about if moving to MF and Unix
> would be performance.
>

We have approx. 20MIPS. Recent Tests esp. with DB2 (8.x on AIX) and MF-
Cobol on a midsize AIX System do show factor 20 in Performance
(better).

> Oh, another question.  What type of data access do you use on VSE?  VSAM?
> DB2?  DL/I?

DL/I is elliminated. VSAM and DB2 are the only access systems. VSAM
because of performance (see above).

:-) as the thing goes on I am shure that I will post again.

Kind regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-12T11:56:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53briaF1rqtioU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net> <1171285904.789486.46390@v45g2000cwv.googlegroups.com>`

```
michael.bierenfeld@web.de<michael.bierenfeld@web.de> 02/12/07 6:11 AM >>>
>
>> model 2096-U02, running at 526 MIPS.  Any idea what size your VSE box
is?
>> One thing (among others) that I would worry about if moving to MF and
Unix
>> would be performance.
>>
…[5 more quoted lines elided]…
>> Oh, another question.  What type of data access do you use on VSE? 
VSAM?
>> DB2?  DL/I?
>
…[3 more quoted lines elided]…
>:-) as the thing goes on I am shure that I will post again.

How long ago did you eliminate DL/I?  Did you "convert" the DL/I databases
to DB2?  Was this done "by hand", with a tool, or what?  (We're looking into
perhaps doing this.)

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 8)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-13T03:15:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171365319.618801.203940@v45g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<53briaF1rqtioU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net> <1171285904.789486.46390@v45g2000cwv.googlegroups.com> <53briaF1rqtioU1@mid.individual.net>`

```
> How long ago did you eliminate DL/I?  Did you "convert" the DL/I databases
> to DB2?  Was this done "by hand", with a tool, or what?  (We're looking into
> perhaps doing this.)

DL/I is now DB2. The conversion has been done "by Hand". But we were
in the lucky situation that we did not have to many of them.

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-02-12T21:01:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i0l1t2lcagm0nrpketjtragq23n2fbpdqq@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net> <1171285904.789486.46390@v45g2000cwv.googlegroups.com>`

```
On 12 Feb 2007 05:11:44 -0800, "michael.bierenfeld@web.de"
<michael.bierenfeld@web.de> wrote:

>
>> model 2096-U02, running at 526 MIPS.  Any idea what size your VSE box is?
…[16 more quoted lines elided]…
>Kind regards
Do full volume stress testing.  The design points of the two boxes are
different.  Also be aware that 20 MIPS is small potatoes in the
current z world and that you might be able to actually get a z system
that will run your current load cheaper (lower electricity and cooling
costs, software deals, etc.).  Comparing an old box with a new one
doesn't really give the full picture.  AIX, VSE or z/OS all have
interesting capabilities for business and depending on the business,
one has a better set of tradeoffs.  If there is a lot of task and
context switching, the AIX box may well do worse than the z box.  In
addition, overall your organization may be better off on an i series
(successor to the AS400).  The business plan and goals can help
determine direction.
>
>Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 8)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-13T03:48:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171367294.743978.97930@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<i0l1t2lcagm0nrpketjtragq23n2fbpdqq@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net> <1171285904.789486.46390@v45g2000cwv.googlegroups.com> <i0l1t2lcagm0nrpketjtragq23n2fbpdqq@4ax.com>`

```
> Do full volume stress testing.  The design points of the two boxes are
> different.  Also be aware that 20 MIPS is small potatoes in the
> current z world

Thats one of the reasons the migration is planned. We are not such a
big shop that z makes sense (too expensive for the workload)

We do outperform our needs on the target platform. So we are on the
secure side.

michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 9)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-02-16T00:13:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mlt9t2d7tgdophkrjvs62984q1kbnpsbfl@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <534guoF1r0f5uU1@mid.individual.net> <1171285904.789486.46390@v45g2000cwv.googlegroups.com> <i0l1t2lcagm0nrpketjtragq23n2fbpdqq@4ax.com> <1171367294.743978.97930@a75g2000cwd.googlegroups.com>`

```
On 13 Feb 2007 03:48:14 -0800, "michael.bierenfeld@web.de"
<michael.bierenfeld@web.de> wrote:

>> Do full volume stress testing.  The design points of the two boxes are
>> different.  Also be aware that 20 MIPS is small potatoes in the
…[3 more quoted lines elided]…
>big shop that z makes sense (too expensive for the workload)

Did you check out the new z BC class machines?  IBM may have gotten
the pricing for the hardware/software combination back down out of the
stratosphere.
>
>We do outperform our needs on the target platform. So we are on the
>secure side.
>
>michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 5)_

- **From:** "HansJ" <hjigel@kup.de>
- **Date:** 2007-02-13T01:23:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171358585.390735.54180@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<1171040159.707445.177060@s48g2000cws.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com>`

```
On 9 Feb., 17:55, "michael.bierenf...@web.de"
<michael.bierenf...@web.de> wrote:
> > Seriously, though, I have to ask what type of VSE workload do you have that
> > you are migrating to MF and Unix?  Are you migrating just batch
…[14 more quoted lines elided]…
> Michael

Michael,
I can tell you that AIX on pSeries is an excellent target platform.
One of the recent migration projects we did was from a Unisys
Clearpath 2200 mainframe to AIX pSeries. Excellent performance results
and an very stable system.
The system is productive since about 18 month now and there where no
problems whatsoever, neither in AIX, MF COBOL or Oracle.
Here are just a few figures:
COBOL batch programs: 600
COBOL online programs: 300
COBOL Subprograms: 1.000
Lines of COBOL source code: 1.1 million
Job control runs: 1.500
Record types in database: 550
and lots of special interfaces

Target system:
IBM p570 HCMP Cluster
AIX 5.2
Oracle 9
MF Server Express
Number of online users > 1.500
Number of concurrent users about 1.000
Transaction response time < 0.3 seconds
Number of database accesses / Transaction > 30

Unix to replace a mainframe is always a matter of what the workload is
going to be, in most cases there a viable Unix offerings providing the
expected performance and stability. For those that see performance as
a problem, there is still Linux on the zSeries systems, providing the
best of both worlds. A zSeries system is hower most likely just only
to be considered for the largest implementations.

There are lots of choices these days.

Regards HansJ
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 6)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-02-13T11:04:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171393493.484389.33090@k78g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1171358585.390735.54180@j27g2000cwj.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com>`

```
On 13 Feb, 09:23, "HansJ" <hji...@kup.de> wrote:
> Unix to replace a mainframe is always a matter of what the workload is
> going to be, in most cases there a viable Unix offerings providing the
…[4 more quoted lines elided]…
>

Just for fun visit: www.actscorp.com/reboothill.htm
It tells a few horror tales about going to Unix.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-13T19:17:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqt2sk$k7u$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com>`

```
In article <1171393493.484389.33090@k78g2000cwa.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>On 13 Feb, 09:23, "HansJ" <hji...@kup.de> wrote:
>> Unix to replace a mainframe is always a matter of what the workload is
…[8 more quoted lines elided]…
>It tells a few horror tales about going to Unix.

I've visited this website before... and without names, dates or anything 
verifiable it seems to fall into the category of 'A guy told me...'

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 8)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-02-14T13:21:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171488112.624829.61880@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<eqt2sk$k7u$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <eqt2sk$k7u$1@reader2.panix.com>`

```

docdwarf@panix.com wrote:
> In article <1171393493.484389.33090@k78g2000cwa.googlegroups.com>,
> Alistair <alistair@ld50macca.demon.co.uk> wrote:
…[15 more quoted lines elided]…
> DD

Too true, but naming names leads to litigation. For what it is worth,
I have seen two attempts to migrate to non-mainframe solutions (DRS
and then AS400) fail and I left before the third bore fruit (rotten on
the vine or otherwise). I hope that those who review the site take
note of the lessons that can be learned before bolloxing up their own
migrations.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 7)_

- **From:** "HansJ" <hjigel@kup.de>
- **Date:** 2007-02-14T02:13:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171448006.079649.182260@l53g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1171393493.484389.33090@k78g2000cwa.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com>`

```
On 13 Feb., 20:04, "Alistair" <alist...@ld50macca.demon.co.uk> wrote:
> On 13 Feb, 09:23, "HansJ" <hji...@kup.de> wrote:
>
…[8 more quoted lines elided]…
> It tells a few horror tales about going to Unix.

Alistair,
I have no doubts that there is some truth behind any of those stories,
but you're not going to tell me that this is typical for migration
projects. Most of the stories found there tried to implement something
new and failed. I have similar stories I could tell, but it is
typically not a migration project that fails.
Unix is a rock-solid operating system when we talk about the main
brands (HPUX, Solaris, AIX).
Just read the numbers of the sample I stated.
During the normal business hours (between 7:00am and 4:00pm - between
950 and 1.000 concurrent users and an average response time at about
0.3 seconds with quite some database accesses - what else are you
asking for...???).
This is just one of many examples that I can tell about, though we are
only playing in the Unisys fields.

Michael, keep going, you're on the right track...

Regards HansJ
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 8)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-02-14T13:24:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171488253.785130.227760@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1171448006.079649.182260@l53g2000cwa.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171448006.079649.182260@l53g2000cwa.googlegroups.com>`

```

HansJ wrote:
> On 13 Feb., 20:04, "Alistair" <alist...@ld50macca.demon.co.uk> wrote:
> > On 13 Feb, 09:23, "HansJ" <hji...@kup.de> wrote:
…[29 more quoted lines elided]…
> Regards HansJ

It is intended as a warning. I have worked on Unix (Sun Solaris V) and
consider it to be a Mickey Mouse OS. Now I'm gonna be sued by Disney
for TM infringement.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-15T00:33:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er09p7$4u3$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171448006.079649.182260@l53g2000cwa.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com>`

```
In article <1171488253.785130.227760@a75g2000cwd.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>It is intended as a warning. I have worked on Unix (Sun Solaris V) and
>consider it to be a Mickey Mouse OS. Now I'm gonna be sued by Disney
>for TM infringement.

If http://209.161.33.50/dictionary/mickey%20mouse is permitted as evidence 
they might have a difficult time winning.

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 10)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-02-15T07:35:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171553700.163457.299880@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<er09p7$4u3$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171448006.079649.182260@l53g2000cwa.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com> <er09p7$4u3$1@reader2.panix.com>`

```
On 15 Feb, 00:33, docdw...@panix.com () wrote:
> In article <1171488253.785130.227...@a75g2000cwd.googlegroups.com>,
>
…[11 more quoted lines elided]…
> DD

Now I should be able to sleep at nights again.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-15T16:14:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er20t8$41$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com> <er09p7$4u3$1@reader2.panix.com> <1171553700.163457.299880@h3g2000cwc.googlegroups.com>`

```
In article <1171553700.163457.299880@h3g2000cwc.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>On 15 Feb, 00:33, docdw...@panix.com () wrote:
>> In article <1171488253.785130.227...@a75g2000cwd.googlegroups.com>,
…[12 more quoted lines elided]…
>Now I should be able to sleep at nights again.

Yep, that's me, the sure-fire cure for insomnia... why, I remember once, 
when I was a lad, we was ridin' the rods on th' Monan road, me 'n ol' 
Lefty... called 'im Lefty 'cause... well, 'cause that's what we called 
'im, ain't ever'thin' got a reason behind it... like callin' this chair a 
'chair' or callin' yer dawg Phideaux 'er an'athin' like that... anyhow, we 
was ridin' th' rods on the Monan road, right pleasant bed it had, too... 
not as good as the Phoebe Snow, now *there* was road, all anthracite-fired 
an' slicker'n a hound's tooth... not like Phideaux, no, he's always showed 
a bit of a shadow on the left bicuspidor... anyhow, me 'n Lefty, we was 
ridin' the rods on the Monan road...

... zzzzzzZZZZZZzzzzz...

DD
```

###### ↳ ↳ ↳ OT Monon, not Monan was Re: JCL, Cobol and "Call Parameters"

_(reply depth: 12)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-02-16T00:09:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdt9t2dim8fria6mtnr1g5j7h5o2rlqrde@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com> <er09p7$4u3$1@reader2.panix.com> <1171553700.163457.299880@h3g2000cwc.googlegroups.com> <er20t8$41$1@reader2.panix.com>`

```
On Thu, 15 Feb 2007 16:14:32 +0000 (UTC), docdwarf@panix.com () wrote:

>> snip 
>
…[9 more quoted lines elided]…
>ridin' the rods on the Monan road...

That was the Monon Railroad named after Monon, Indiana.  The Phoebe
Snow was a train on the Delaware, Lackawanna, and Western named after
a fictional woman they had used in their advertising in the early
1900's.
>
>... zzzzzzZZZZZZzzzzz...
>
>DD
```

###### ↳ ↳ ↳ Re: OT Monon, not Monan was Re: JCL, Cobol and "Call Parameters"

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-16T10:12:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er4037$be0$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171553700.163457.299880@h3g2000cwc.googlegroups.com> <er20t8$41$1@reader2.panix.com> <bdt9t2dim8fria6mtnr1g5j7h5o2rlqrde@4ax.com>`

```
In article <bdt9t2dim8fria6mtnr1g5j7h5o2rlqrde@4ax.com>,
Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
>On Thu, 15 Feb 2007 16:14:32 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>Yep, that's me, the sure-fire cure for insomnia... why, I remember once, 
>>when I was a lad, we was ridin' the rods on th' Monan road, me 'n ol' 
>>Lefty...

[snip of soporofisms]

>That was the Monon Railroad named after Monon, Indiana.  The Phoebe
>Snow was a train on the Delaware, Lackawanna, and Western named after
>a fictional woman they had used in their advertising in the early
>1900's.

Really now, Mr Morris... do you expect *that* much of a hobo's spelling?

DD
```

###### ↳ ↳ ↳ Re: OT Monon, not Monan was Re: JCL, Cobol and "Call Parameters"

_(reply depth: 14)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-02-16T21:43:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb9ct29a8ee9i85mi7fdptlpkjpftqagdk@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171553700.163457.299880@h3g2000cwc.googlegroups.com> <er20t8$41$1@reader2.panix.com> <bdt9t2dim8fria6mtnr1g5j7h5o2rlqrde@4ax.com> <er4037$be0$1@reader2.panix.com>`

```
On Fri, 16 Feb 2007 10:12:55 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <bdt9t2dim8fria6mtnr1g5j7h5o2rlqrde@4ax.com>,
>Clark F Morris  <cfmpublic@ns.sympatico.ca> wrote:
…[15 more quoted lines elided]…
>Really now, Mr Morris... do you expect *that* much of a hobo's spelling?

No, I'm just a railfan being pedantic.
>
>DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-15T08:49:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5809t29id80o8nelhe1hjl2srn4mbbtlb0@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171448006.079649.182260@l53g2000cwa.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com>`

```
On 14 Feb 2007 13:24:13 -0800, "Alistair"
<alistair@ld50macca.demon.co.uk> wrote:

>It is intended as a warning. I have worked on Unix (Sun Solaris V) and
>consider it to be a Mickey Mouse OS. Now I'm gonna be sued by Disney
>for TM infringement.

I thought Disney used Univac machines.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 10)_

- **From:** "HansJ" <hjigel@kup.de>
- **Date:** 2007-02-15T09:06:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171559188.747903.186480@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<5809t29id80o8nelhe1hjl2srn4mbbtlb0@4ax.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171448006.079649.182260@l53g2000cwa.googlegroups.com> <1171488253.785130.227760@a75g2000cwd.googlegroups.com> <5809t29id80o8nelhe1hjl2srn4mbbtlb0@4ax.com>`

```
On 15 Feb., 16:49, Howard Brazee <how...@brazee.net> wrote:
> On 14 Feb 2007 13:24:13 -0800, "Alistair"
>
…[5 more quoted lines elided]…
> I thought Disney used Univac machines.

Howard,

at least they did at some point in time...

Walt Disney Pictures & Television
Burbank, California, USA
Migration from Unisys OS 2200 mainframe to UNIX and Sybase

Migration of Unisys ACOB to Micro Focus COBOL.
Migration from MSAM to Sybase on Digital UNIX.
Migration of DPS Screens.
Conversion of ECL to Bourne shell scripts.

Long long time ago... done by Inglenet

regards HansJ
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 7)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-14T03:51:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171453867.284714.316160@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<1171393493.484389.33090@k78g2000cwa.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <51q3mlF1lgdlrU2@mid.individual.net> <1169813541.926374.70560@q2g2000cwa.googlegroups.com> <51uoe5F1mclreU3@mid.individual.net> <1171040159.707445.177060@s48g2000cws.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com>`

```

> Just for fun visit:www.actscorp.com/reboothill.htm
> It tells a few horror tales about going to Unix.

I can tell you a lot of stories about projects that failed. Some of
them have been migration projects some of them not.

Nobody would do such a thing if there is no need.

So we take the risk and do it.

Kind regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-14T13:46:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqv3sc$c6l$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com>`

```
In article <1171453867.284714.316160@v33g2000cwv.googlegroups.com>,
michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
>
>> Just for fun visit:www.actscorp.com/reboothill.htm
…[5 more quoted lines elided]…
>Nobody would do such a thing if there is no need.

What constitutes a 'need', Mr Bierenfeld, may be seen as a matter of 
perception.  Consider:

Most life, as it is presently defined, needs SCHNOPPS - Sodium, Carbon, 
Hydrogen, Nitrogen, Oxygen, Potassium, Phosphorus and Sulfur - in order to 
exist.

Most employees, as they are presently defined, need to make a good show of 
doing what their boss tells them in order to keep their jobs.

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-15T23:01:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53ipcmF1sqf6iU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:eqv3sc$c6l$1@reader2.panix.com...
> In article <1171453867.284714.316160@v33g2000cwv.googlegroups.com>,
> michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
…[20 more quoted lines elided]…
>
I wonder if MR GINER (Movement, Respiration, Growth & Repair, Irritability 
(in the sense of stimulus response or nervous system), Nutrition, Excretion, 
and Reproduction - the functions which determine for a Zoologist whether 
something is a life form - Botanists have slightly different criteria :-)) 
comes home at the end of a hard day and takes a shot of SCHNOPPS...

Pete.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 10)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-02-15T07:34:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171553657.725268.267530@v45g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<53ipcmF1sqf6iU1@mid.individual.net>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com> <53ipcmF1sqf6iU1@mid.individual.net>`

```
On 15 Feb, 10:01, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:eqv3sc$c6l$1@reader2.panix.com...
> > In article <1171453867.284714.316...@v33g2000cwv.googlegroups.com>,
…[30 more quoted lines elided]…
> - Show quoted text -

Sorry to be pedantic but shouldn't SCHNOPPS be NaCH2N2O2KPS? where the
2 is supposed to be a subscript.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-15T16:19:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er216p$5mf$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com> <53ipcmF1sqf6iU1@mid.individual.net> <1171553657.725268.267530@v45g2000cwv.googlegroups.com>`

```
In article <1171553657.725268.267530@v45g2000cwv.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>On 15 Feb, 10:01, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
>wrote:
>> <docdw...@panix.com> wrote in messagenews:eqv3sc$c6l$1@reader2.panix.com...

[snip]

>> > Most life, as it is presently defined, needs SCHNOPPS - Sodium, Carbon,
>> > Hydrogen, Nitrogen, Oxygen, Potassium, Phosphorus and Sulfur - in order to
>> > exist.

[snip]

>Sorry to be pedantic but shouldn't SCHNOPPS be NaCH2N2O2KPS? where the
>2 is supposed to be a subscript.

It should if one might wish to reduce its value as a mnemonic device to 
those who are familiar with English names for elements, perhaps.

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 9)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-19T06:40:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171896055.714830.218530@m58g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<eqv3sc$c6l$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171358585.390735.54180@j27g2000cwj.googlegroups.com> <1171393493.484389.33090@k78g2000cwa.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com>`

```

> What constitutes a 'need', Mr Bierenfeld, may be seen as a matter of
> perception.  Consider:

The need is :

- lack of outsourcers here in germany
- prize
- Development to unflexible. Compare it with Eclipse or MF-IDE and you
will see
- Developers have to be quick-frozen and defrosted on demand

> Most employees, as they are presently defined, need to make a good show of
> doing what their boss tells them in order to keep their jobs.
>

Agreed :-)

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-19T15:23:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ercfds$hvl$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com> <1171896055.714830.218530@m58g2000cwm.googlegroups.com>`

```
In article <1171896055.714830.218530@m58g2000cwm.googlegroups.com>,
michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
>
>> What constitutes a 'need', Mr Bierenfeld, may be seen as a matter of
…[8 more quoted lines elided]…
>- Developers have to be quick-frozen and defrosted on demand

Ahhhh... it seems like a variation of the ever-popular exchange:

Programmer: I can get it to you on time, according to specification or 
withih the budget; pick two.

Manager: I pick all three.

P: That wasn't one of the choices.

M: I made it one, it is a choice now.

P: You are a programmer now, too; you make new choices, you write new 
code.

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 11)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-20T02:05:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171965926.094570.259470@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<ercfds$hvl$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171453867.284714.316160@v33g2000cwv.googlegroups.com> <eqv3sc$c6l$1@reader2.panix.com> <1171896055.714830.218530@m58g2000cwm.googlegroups.com> <ercfds$hvl$1@reader2.panix.com>`

```
On 19 Feb., 16:23, docdw...@panix.com () wrote:
> In article <1171896055.714830.218...@m58g2000cwm.googlegroups.com>,
>
…[27 more quoted lines elided]…
> DD

M and P have to think in both directions. Thats my opinion.

Most ot the business stuff is now handled by SAP/Peoplesoft. Whats
left is a lot of specific software written in years and years. The
entropy in that code is quite high.

So retirement is an issue. And do you think you find talented people
that do wanna work in the dusty environment like their ancestors.

michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-20T10:17:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<erehsg$ah4$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171896055.714830.218530@m58g2000cwm.googlegroups.com> <ercfds$hvl$1@reader2.panix.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com>`

```
In article <1171965926.094570.259470@h3g2000cwc.googlegroups.com>,
michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
>On 19 Feb., 16:23, docdw...@panix.com () wrote:

[snip]

>> Ahhhh... it seems like a variation of the ever-popular exchange:
>>
…[14 more quoted lines elided]…
>M and P have to think in both directions. Thats my opinion.

What 'has to be' is not, in my experience, necessarily the same as 'is', 
Mr Bierenfeld... and I will be polite and not mention what my Drill 
Sergeant taught us back in Basic Training for the United States Air Force 
about 'opionion'; his language was very... Sergeantly.

>
>Most ot the business stuff is now handled by SAP/Peoplesoft. Whats
>left is a lot of specific software written in years and years. The
>entropy in that code is quite high.

I was taught that 'entropy' is tendency, in a closed thermodynamic system, 
for the components thereof to assume their least-ordered configuration; I 
am having difficulty seeing how this applies to compiled programs unless 
you mean that the tapes on which they are being stored are losing their 
magnetic substrate.

>
>So retirement is an issue. And do you think you find talented people
>that do wanna work in the dusty environment like their ancestors.

I find that talented people enjoy doing a variety of things, one of them 
being 'making a decent dollar for a job well-done'.  Is your management 
saying 'we cannot find people with these skills' or 'we cannot find people 
with these skills at the prices we wish to pay'?

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 13)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-20T03:37:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171971469.831108.159240@k78g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<erehsg$ah4$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171896055.714830.218530@m58g2000cwm.googlegroups.com> <ercfds$hvl$1@reader2.panix.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com>`

```
> What 'has to be' is not, in my experience, necessarily the same as 'is',
> Mr Bierenfeld... and I will be polite and not mention what my Drill
> Sergeant taught us back in Basic Training for the United States Air Force
> about 'opionion'; his language was very... Sergeantly.

The 'is' is irrelevant in means of busines. Because you have it
already. What 'has to be' is the future. And greetings to your drill
sergeant.

> I was taught that 'entropy' is tendency, in a closed thermodynamic system,
> for the components thereof to assume their least-ordered configuration; I
> am having difficulty seeing how this applies to compiled programs unless
> you mean that the tapes on which they are being stored are losing their
> magnetic substrate.

The tendency for software, over time, to become difficult and costly
to maintain. New functionality, changes, bug fixes. What's so hard to
understand ?

> Is your management
> saying 'we cannot find people with these skills' or 'we cannot find people
> with these skills at the prices we wish to pay'?
>

Exactly. But it is an "and".

Regards

Michael

I will not answer any more
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-20T12:39:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ereq59$cj4$1@reader2.panix.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com>`

```
In article <1171971469.831108.159240@k78g2000cwa.googlegroups.com>,
michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
>> What 'has to be' is not, in my experience, necessarily the same as 'is',
>> Mr Bierenfeld... and I will be polite and not mention what my Drill
…[3 more quoted lines elided]…
>The 'is' is irrelevant in means of busines.

If that is how it is, Mr Bierenfeld... then that, in means of business, is 
irrelevant.

[snip]

>> I was taught that 'entropy' is tendency, in a closed thermodynamic system,
>> for the components thereof to assume their least-ordered configuration; I
…[6 more quoted lines elided]…
>understand ?

What I find to understand, Mr Bierenfeld, is how flaws in software design 
(for instance, hard-coded values) or changes in a business' fundamentals 
are given a label which is defined as a tendency for a system to go to 
disorder.  What you posit seems to more and/or new rules, an *increase* in 
order.

>
>> Is your management
…[4 more quoted lines elided]…
>Exactly. But it is an "and".

It may be perceived as an 'and', Mr Bierenfeld, but I wonder if an 
experiment would reflect this appearance.  The next time you hear someone 
saying 'we cannot find people with these skills' ask if they have tried 
doubling the rate offered for the position.

>
>Regards
…[3 more quoted lines elided]…
>I will not answer any more

A pity... there's *so* much to discuss, too!

DD
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 15)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-02-20T18:26:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<erfb0u$o9k$03$1@news.t-online.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com>`

```
I am here in Germany,
I am the developer for OpenCOBOL
and I am available for hire :-)

Roger

<docdwarf@panix.com> schrieb im Newsbeitrag 
news:ereq59$cj4$1@reader2.panix.com...
> In article <1171971469.831108.159240@k78g2000cwa.googlegroups.com>,
> michael.bierenfeld@web.de <michael.bierenfeld@web.de> wrote:
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 16)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-21T04:05:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172059522.526834.304660@l53g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<erfb0u$o9k$03$1@news.t-online.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com>`

```
On 20 Feb., 18:26, "Roger While" <s...@sim-basis.de> wrote:
> I am here in Germany,
> I am the developer for OpenCOBOL
> and I am available for hire :-)
>

:-) Do you now VisualAge for Cobol ? We have a bunch of VisualAge
Programs that have to be transferred to Microfocus Cobol. Automatic
translation may be an option.

Regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-21T20:02:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4z1Dh.338445$jd2.206851@fe09.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com>`

```
Michael,
  Are you using Micro Focus "Net Express" or "Mainframe Express" product? 
Either way, source code conversion from IBM VisualAge COBOL to any Micro Focus 
product should be (mostly) just a matter of selecting the right directives.

If you have CICS and JCL issues, then MF also provides solutions for that as 
well.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 18)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-23T07:27:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172244444.263017.308950@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<4z1Dh.338445$jd2.206851@fe09.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com> <4z1Dh.338445$jd2.206851@fe09.news.easynews.com>`

```
>   Are you using Micro Focus "Net Express" or "Mainframe Express" product?
> Either way, source code conversion from IBM VisualAge COBOL to any Micro Focus
> product should be (mostly) just a matter of selecting the right directives.

Hello,

we are using "Server Express". VisualAge Cobol does not look like
Cobol it is some sort of "high level" COBOL. Can you give me a
reference for that ?

Kind regards

michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-23T18:10:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S6GDh.343948$Oc2.170212@fe07.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com> <4z1Dh.338445$jd2.206851@fe09.news.easynews.com> <1172244444.263017.308950@v33g2000cwv.googlegroups.com>`

```
Sounds to me as if you are using "VisualAge GENERATOR" and not "VisualAge 
COBOL".  The former product is a follow-up to the earlier (mainframe) CSP 
product - and is an "application generator" product.  It does provide an option 
(as I recall) to "generate" COBOL source code, but the "development" is done in 
a high-level language.

Check out:
  http://www-306.ibm.com/software/awdtools/visgen/

and see if that is what you currently have.  If so, you COULD migrate to Micro 
Focus "APS" - which is a "similar" product.  I do NOT know if they (MF) do or 
don't have migration strategies from the IBM generator to theirs - but I think 
they might - if you contact them and ask about it.
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 20)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-27T04:33:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172579615.417643.216770@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<S6GDh.343948$Oc2.170212@fe07.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com> <4z1Dh.338445$jd2.206851@fe09.news.easynews.com> <1172244444.263017.308950@v33g2000cwv.googlegroups.com> <S6GDh.343948$Oc2.170212@fe07.news.easynews.com>`

```

> Sounds to me as if you are using "VisualAge GENERATOR" and not "VisualAge
> COBOL"

Yes we are using VisualAge generator. The Highlevel Code is
transformed to cobol and then used on the Host.

> and see if that is what you currently have.  If so, you COULD migrate to Micro
> Focus "APS" - which is a "similar" product.  I do NOT know if they (MF) do or
> don't have migration strategies from the IBM generator to theirs - but I think
> they might - if you contact them and ask about it.

We do not want to replace VisualAge Generator with MF-APS. The goal is
to have transfered VisualAge -> Cobol running with MF under AIX.

Kind regards

Michael
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 21)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-27T17:33:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IXZEh.36939$ff2.9225@fe02.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com> <4z1Dh.338445$jd2.206851@fe09.news.easynews.com> <1172244444.263017.308950@v33g2000cwv.googlegroups.com> <S6GDh.343948$Oc2.170212@fe07.news.easynews.com> <1172579615.417643.216770@j27g2000cwj.googlegroups.com>`

```
Michael,
I remember the code that CSP used to create and it was pretty obscure, but I 
don't think I have ever seen what VisualAge Generator creates.  You certainly 
COULD

  - Step 1, run VisualAge Generator to create COBOL code (Selecting CICS as the 
target environment)
 - Transfer THAT code (not the high-level stuff) to AIX
 - Use Micro Focus to compile and maintain the generated COBOL code - with a 
CICS add-on

However, my best guess is that the code you would be working with would be 
pretty ugly.  I also suspect that there MIGHT be some VA Gen specific run-time 
modules that you would need to "emulate" on AIX.

    NOTE: Some Micro Focus features such as REVOLVE and their "refactory 
facilities" MIGHT help you convert
                VisualAge Generator created COBOL to "maintainable" source code.

Having said all of this, my BEST suggestion would be for you to contact MF 
directly and ask for their migration assistance/advice.  If you would like me 
to, even though I don't work for MF, I could send some enquiries and find out 
who would be the best person in MF to work with you and have them get in touch 
with you directly.  If this sounds good to you, please email me directly - 
off-list.

Am I correct from the ".de" in your email address that you are in Germany?  This 
might impact who can/should work with you.  Do you have a purchased copy of 
Server Express - or are you still working under "evaluation"?
```

###### ↳ ↳ ↳ Re: JCL, Cobol and "Call Parameters"

_(reply depth: 22)_

- **From:** "michael.bierenfeld@web.de" <michael.bierenfeld@web.de>
- **Date:** 2007-02-28T03:23:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172661829.805901.325420@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<IXZEh.36939$ff2.9225@fe02.news.easynews.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com> <1171965926.094570.259470@h3g2000cwc.googlegroups.com> <erehsg$ah4$1@reader2.panix.com> <1171971469.831108.159240@k78g2000cwa.googlegroups.com> <ereq59$cj4$1@reader2.panix.com> <erfb0u$o9k$03$1@news.t-online.com> <1172059522.526834.304660@l53g2000cwa.googlegroups.com> <4z1Dh.338445$jd2.206851@fe09.news.easynews.com> <1172244444.263017.308950@v33g2000cwv.googlegroups.com> <S6GDh.343948$Oc2.170212@fe07.news.easynews.com> <1172579615.417643.216770@j27g2000cwj.googlegroups.com> <IXZEh.36939$ff2.9225@fe02.news.easynews.com>`

```

The "ugly" code from VisualAge Generator has been considered
unmaintainable by the Cobol people. There is another approach
automatically transform the "High" Level Code. But there are still
problems and we are not yet convinced that the tool we are using is
the best.

>
>     NOTE: Some Micro Focus features such as REVOLVE and their "refactory
…[6 more quoted lines elided]…
>

Yep Germany. Munich in fact. Its all purchased.

Kind Regards

Michael
```

#### ↳ Re: JCL, Cobol and "Call Parameters"

- **From:** "Fabrizio Calabretta" <fabrizio.calabretta@gmail.com>
- **Date:** 2007-02-13T09:17:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171387055.971865.293420@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`
- **References:** `<1169639791.645092.212490@v45g2000cwv.googlegroups.com>`

```
On Jan 24, 12:56 pm, "michael.bierenf...@web.de"
<michael.bierenf...@web.de> wrote:
> Hello,
>
…[46 more quoted lines elided]…
> Michael

If your considering migrating from VSE to Linux, take a look at XFRAME
(www.htwc.com)
It seems they have a solution for cobol/cics/vse to linux

Bye
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
