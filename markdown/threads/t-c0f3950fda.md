[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] SVC 107 Authority Determined by... Library?

_12 messages · 4 participants · 2002-04_

---

### [OT] SVC 107 Authority Determined by... Library?

- **From:** docdwarf@panix.com
- **Date:** 2002-04-05T09:16:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8kbkb$ola$1@panix1.panix.com>`

```


All right... here's a cute one.

My client has a home-brewed utility (IBM mainframe), written in ASM, which 
when passed an appropriate set of parameters will invoke CEMT to do... 
stuff.  I have a program that extracts some data from the billing files 
and have been directed to use this utility to make sure that the online 
billing program is DISabled so that no updates occur when I do my 
extracts.  The parameters used are something like:

PRODREGN,CEMT S TRAN(BILL) DIS

... where PRODREGN is the Prod CICS region name and CEMT S TRAN(BILL) DIS 
are more-or-less self-explanatory to those familiar with such things.

Anyhow... I code up a set of parameters like

TESTREGN,CEMT S TRAN(BILL) DIS

... for testing purposes and hit... a wall; I have no auth to use the 
utility.  When I ask what the reason for this is I am told that the 
utility is an 'all or none' affair and if I have the auth to use it I have 
the auth to invoke CEMT in *any* region.

This confuses me... so I do a bit of digging and find out that the utility 
issues an SVC 107 (MODESET); system security s set up so that auth to 
issue this CALL is determined by library (or so ABEND-AID tells me in the 
dump).

My question, to Those Who Know (And Might Deign To Answer) is... eh?  This 
is a first for me (an applications-jockey); never before have I run across 
a program whose auth is determined by the library from which it is 
invoked.  That bit of novelty aside... is it the case that a program 
authorised to issue an SVC 107 has the authority to do this to any CICS 
region?

It seems to me - and my system-level knowledge is *very* limited - that 
this is what The Professionals call 'a bunch o' hooey' and that a 
configuration can be made where programmers such as I can be given auth to 
invoke the utility for Test regions and the More Trustworthy Folks (like 
the CA7 scheduler, if that is a 'folk') can have auth for Prod... but 
someone is either unable or unmotivated to figure out just how.

Meanwhile, of course, I am stuck with a jobstream that I cannot test; the 
Security folks have told me that I need to arrange with one of their own 
to get this thing run even in the Test region.  I find this... tedious, to 
say the least, and dislike going, cap in hand, to other people and saying 
'Please, Sir, may I have another run?' instead of being allowed to merely 
Do My Own Job.

DD
```

#### ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-04-05T19:32:04+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com>`

```
Doc,

<sysprog mode>
<teacher mode>
when using MODESET (SVC 107) the issuing program must run authorized.
How is this done?  The program must be linked with

//S1 EXEC PGM=IEWL,PARM='...,AC=1,....'
//SYSLMOD DD DISP=SHR,DSN=apf.lib.pds


Where apf.lib.pds is a PDS (or PDSE) named in the APF LIST.  The APF
list is either maintained in member IEAAPFxx in SYS1.PARMLIB, or in
member PROGxx in PARMLIB


If the program has not been linked into an authorized lib, tough luck,
you will get ABEND S047

And mere applications developing mortals don't normally get write
access to APF libs.  Whoever places programs in the APF libs present
potential danger to system integrity.

You wouldn't need to come to my office with cap in hand.  But you
would need to come to my office.  It would be me who would (look at
the prog and then) compile and link it into an APF library on a
sandbox system/LPAR.  And a bottle of wine wouldn't be needed either,
but if provided, would be appreciated and shared with you after the
program performs as wanted/advertised without any adverse side effects
</teacher mode>
</sysprog mode>

On 5 Apr 2002 09:16:43 -0500, docdwarf@panix.com wrote:

>
>
…[49 more quoted lines elided]…
>DD

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Remember, even if you win the rat race -- you're still a rat. -- Lily Tomlin
      
        (Another bit of Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeeds.Com, Uncensored Usenet News ==----------
   http://www.newsfeeds.com       The Largest Usenet Servers in the World!
------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

##### ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** docdwarf@panix.com
- **Date:** 2002-04-05T12:54:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8kod2$gik$1@panix1.panix.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com>`

```
In article <p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com>,
Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
>Doc,
>
><sysprog mode>
><teacher mode>

[snip mode]

>It would be me who would (look at
>the prog and then) compile and link it into an APF library on a
>sandbox system/LPAR.

Ahhhh... let me see if I have made myself clear and now understand.  It is 
not *my* program which does the SVC 107, it is a home-grown utility 
(e.g., RUNCEMT) which is invoked by my job.  RUNCEMT lives in 
SYSTEM.PROD.UTILS and that library has the appropriate auth for modules to 
invoke CEMT in PRODREGN.

When you say '... into an APF library on a sandbox system/LPAR' what I 
understand is that there can be another library containing another copy of 
the program - say, SYSTEM.TEST.UTILS(RUNCEMT) - which has CEMT auth in 
TESTREGN but not PROD.

Is this the case?  (the local sysprogs have said 'no, auth in TEST means 
auth in PROD' but I have trouble believing that)

Your patience and precision are both appreciated and, of course, 
undeserved by me.

DD
```

###### ↳ ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-04-06T09:05:40+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2g6tauoq32rn7ip56sld2hj7uui8tcolqb@4ax.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com> <a8kod2$gik$1@panix1.panix.com>`

```
Doc,

Ahh, you got me a bit confused there for a moment, there are two
different problems here with the same name:  authorization

The module RUNCEMT issues the MODESET SVC, which requires that the
module is authorized (must be in an authorized library)

If a module comes from an authorized lib, the OS allows it to do
MODESET (et al), and thus issue OS commands, for example

In comes RACF, of ACF2, or Top Secret, or whatever security package
you are using.  Here we define which users may run the RUNCEMT
program.  If DD is not in the list of authorized people, tough luck.

If, indeed, DD is a member of the elite list, he can use RUNCEMT
against every  CICS system around.

I understand the sysprog to be reluctant about this.

How can this be solved?  By writing a better RUNCEMT program.

As I understand you now, the following is the JCL to run the utility

//DDJOB    JOB (RUNCEMT),'DD'
//S1      EXEC PMGF=RUNCEMT,PARM='PRODCICS,CEMT P SHUTDOWN IMMED'
//SYSPRINT DD  SYSOUT=*

With a little bit of work one can help you rather easily, but you will
need the SYSPROG and/or security administrator for this as well:

I use RACF samples from now on,  Top secret should be very similar,
and I don't know anything about ACF2 (except that it exists)

Define a RACF facility called RUNCEMT.*   with universal access NONE

(Nobody may use RUNCEMT against any CICS)

then do 

PERMIT RUNCEMT.TESTCICS ID(DD) ACCESS(READ)

which would allow DD to use the facility RUNCEMT.TESTCICS  (but not
PRODCICS)

Then the source of RUNCEMT must be amended to contain a RACF check to
test if the user has read access to RUNCEMT.first_parm_in_JCL

voila


Please contact me offline if you are interested in a sample program

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Time: nature's way of keeping everything from happeningallatonce.
      
        (Another bit of Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeeds.Com, Uncensored Usenet News ==----------
   http://www.newsfeeds.com       The Largest Usenet Servers in the World!
------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

###### ↳ ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-04-06T09:06:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2j7tau8rssvr5dt1ikkmg92cm0ksivk3s9@4ax.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com> <a8kod2$gik$1@panix1.panix.com>`

```
Doc,

(Sending this again, got an error message on the previous attempt)

Ahh, you got me a bit confused there for a moment, there are two
different problems here with the same name:  authorization

The module RUNCEMT issues the MODESET SVC, which requires that the
module is authorized (must be in an authorized library)

If a module comes from an authorized lib, the OS allows it to do
MODESET (et al), and thus issue OS commands, for example

In comes RACF, of ACF2, or Top Secret, or whatever security package
you are using.  Here we define which users may run the RUNCEMT
program.  If DD is not in the list of authorized people, tough luck.

If, indeed, DD is a member of the elite list, he can use RUNCEMT
against every  CICS system around.

I understand the sysprog to be reluctant about this.

How can this be solved?  By writing a better RUNCEMT program.

As I understand you now, the following is the JCL to run the utility

//DDJOB    JOB (RUNCEMT),'DD'
//S1      EXEC PMGF=RUNCEMT,PARM='PRODCICS,CEMT P SHUTDOWN IMMED'
//SYSPRINT DD  SYSOUT=*

With a little bit of work one can help you rather easily, but you will
need the SYSPROG and/or security administrator for this as well:

I use RACF samples from now on,  Top secret should be very similar,
and I don't know anything about ACF2 (except that it exists)

Define a RACF facility called RUNCEMT.*   with universal access NONE

(Nobody may use RUNCEMT against any CICS)

then do 

PERMIT RUNCEMT.TESTCICS ID(DD) ACCESS(READ)

which would allow DD to use the facility RUNCEMT.TESTCICS  (but not
PRODCICS)

Then the source of RUNCEMT must be amended to contain a RACF check to
test if the user has read access to RUNCEMT.first_parm_in_JCL

voila


Please contact me offline if you are interested in a sample program

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Time: nature's way of keeping everything from happeningallatonce.
      
        (Another bit of Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeeds.Com, Uncensored Usenet News ==----------
   http://www.newsfeeds.com       The Largest Usenet Servers in the World!
------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

###### ↳ ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-07T03:24:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8os7g$72k$1@panix1.panix.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <p8nraucsq87n60tpsqgjcg9ovnd34cntb5@4ax.com> <a8kod2$gik$1@panix1.panix.com> <2j7tau8rssvr5dt1ikkmg92cm0ksivk3s9@4ax.com>`

```
[posted and emailed]

In article <2j7tau8rssvr5dt1ikkmg92cm0ksivk3s9@4ax.com>,
Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
>Doc,
>
>(Sending this again, got an error message on the previous attempt)

Then I'll reply to this and not the previous attempt.

>
>Ahh, you got me a bit confused there for a moment, there are two
…[3 more quoted lines elided]…
>module is authorized (must be in an authorized library)

Correct.

>
>If a module comes from an authorized lib, the OS allows it to do
…[7 more quoted lines elided]…
>against every  CICS system around.

This was asserted by the sysprog, aye... it seems you are verifying this.

>
>I understand the sysprog to be reluctant about this.

So can I.

>
>How can this be solved?  By writing a better RUNCEMT program.

This will, in all probability, happen after I have a snowball-fight with 
Satan.

>
>As I understand you now, the following is the JCL to run the utility
…[6 more quoted lines elided]…
>need the SYSPROG and/or security administrator for this as well:

... and this is where it must end.  You see, the sysprog is a Traditional 
Type and as such he adheres to Rule #0: Nobody Wants To Do Any Work.

(it is #0 because it is too lazy to be #1)

You are most generous and I thank you much.

DD
```

#### ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-04-06T05:44:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CAE8B12.F966A361@worldnet.att.net>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> All right... here's a cute one.
…[11 more quoted lines elided]…
> are more-or-less self-explanatory to those familiar with such things.

Hey, Doc, there is a similar program in my shop, named something like
"XXXCOMDR".  We use it to send commands into CICS regions.  Sometimes
they are CEMT commands, and sometimes it's simply a command to execute
a named CICS transaction ID, one written by us application programmers
to open our secondary VSAM files, refresh primaries to secondaries,
close the primary files, and update some global flags in our CICS
application.

> 
> Anyhow... I code up a set of parameters like
…[6 more quoted lines elided]…
> the auth to invoke CEMT in *any* region.

And I had a similar problem with the XXXCOMDR program in my shop.

> 
> This confuses me... so I do a bit of digging and find out that the utility
…[9 more quoted lines elided]…
> region?

I was unable to locate the source code for XXXCOMDR in my shop,
although I can remember looking at it around 1995, when I had a
similar testing problem.  But I found the executable in a library only
the sysprogs can update.  So I disassembled it with the HLASM
toolkit.  The program in my shop also uses SVC 107 MODESET.

The reason I needed to test XXXCOMDR was that the operators needed to
enter the CICS transaction-ID to switch between primary and secondary
files in my CICS region, and the plan was to automate it by initiating
the command from a batch job.  This would help reduce operator errors,
and relieve them of the extra work.  The way it was explained to me at
the time did not include any discussion of APF Authorized libraries. 
Apparently, some programs can alter the system in such dangerous ways
that those programs must be APF authorized and reside in
APF-authorized libraries.  

No, the way it was explained to me in 1995 was this:  By executing the
XXXCOMDR program in a batch job, I could send ANY operator command to
the MVS Operator's Console, and it would execute with exactly the same
authority as if the "Bastard Operator From Hell" had entered it!  That
would be a very dangerous capability to give to a mere applications
jockey.

But like you, I needed to test it.  The compromise solution was they
gave me authority to execute this program under my userid for three
weeks, just for testing.  If it makes any difference to this
explanation, the security package in my shop is ACF2 instead of RACF. 
I was told that they couldn't protect the system from me entering any
console operator command I wanted, but ACF2 would have an audit trail
of anything I did.  So if I caused an unscheduled IPL, they would know
who to blame.  Since I have never worked as an MVS operator, I don't
even know any useful operator commands, although I believe the utility
in our shop submits "F" or "MODIFY" commands to CICS regions. 
Basically, any text on the control card is slammed into the MVS
console command reader, hence the COMDR portion of the program name. 
I suppose I could have shut down VTAM or performed an LLA refresh (if
I knew the command syntax).

> 
> It seems to me - and my system-level knowledge is *very* limited - that
…[4 more quoted lines elided]…
> someone is either unable or unmotivated to figure out just how.

It's not completely hooey.

Yeah, it's possible all right, but it would be a much more complicated
program.  The program would have to determine what permissions the
submitting userid/jobname actually has, and then analyze the submitted
operator command to see if the userid is allowed to do that particular
command.  The program would have to use whatever API is available to
talk to the security system, RACF or ACF2 or Top Secret.

As far as I know, it is rare to code your own applications program to
perform security checking.  ACF2, RACF, and such do all the security
checking for you when you log on, or when the job is submitted to
JES.  User permissions are determined by the userid or the jobname. 
You need to submit operator commands, but the assembler program has no
ability to figure out which operator commands you are allowed to
execute. 

There are some other solutions of course.  You could learn how to
writeo your own EXCI programs (are you running at least CICS 4.1 or
Transaction Server?) to allow a batch job to interact with a CICS
region.  That probably has similar security issues.  Most shops just
purchase something like MacKinney Systems "Batch CEMT" (MTPBATCH),
which allows a batch job to open and close CICS files, and submit
other CEMT commands, with security checking to see if the
userid/jobname is allowed to talk to the requested CICS region.  Then
you can have batch CEMT authority for a test CICS region without also
having it for a production CICS region. 

> 
> Meanwhile, of course, I am stuck with a jobstream that I cannot test; the
…[6 more quoted lines elided]…
> DD

Unless your shop has a product similar to MTPBATCH, it looks like you
will have to go "cap in hand".

Sorry about that.
```

##### ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** docdwarf@panix.com
- **Date:** 2002-04-07T03:30:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8osih$7eu$1@panix1.panix.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <3CAE8B12.F966A361@worldnet.att.net>`

```
In article <3CAE8B12.F966A361@worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>docdwarf@panix.com wrote:

[snip]

>No, the way it was explained to me in 1995 was this:  By executing the
>XXXCOMDR program in a batch job, I could send ANY operator command to
…[3 more quoted lines elided]…
>jockey.

Precisely... I could not believe that this was the case but both you and 
Mr Bandke - neither of whom has a vested interest in Avoiding Work on my 
present job-site - have verified this.

>> 
>> It seems to me - and my system-level knowledge is *very* limited - that
…[9 more quoted lines elided]…
>program.

Bingo... again, as Mr Bandke suggested, someone would actually have to Do 
Some Work.

Such is Life... thanks much, anyhow!

DD
```

#### ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 2002-04-06T08:26:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CAEB16B.CFF4C9DB@acm.org>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com>`

```
The actual action of the utility you mention is undoubtably done by
issuing a console command of the form
F PRODREGN,CEMT S TRAN(BILL) DIS
in response to the PRODREGN,CEMT S TRAN(BILL) DIS parameter, as this is
the method for sending CICS commands from outside CICS.

It is quite possible that this utility was written to merely add a "F "
in front the parameters and issue the resulting command, as this would
by far be the simplest way to write it.  In that case, it can do
anything to any CICS region and do nasty things to other started tasks
as well -- much too dangerous for general consumption.  If it were smart
enough apply strict validation on its parameters, and to allow a
different class of users authority to issue commands only to TEST CICS
regions (and this could be done through checks with some special
installation-defined RACF security profiles), then it might be possible
to allow wider access to the utility.   But,... if it isn't already
coded with that flexibility in place, someone is going to have to find
time and resources to extend and throughly validate it first. 
Otherwise, it would allow you to do all sorts of nasty things, like
shutdown production CICS regions and other system started tasks, etc.

MVS integrity and security design only allows "dangerous" system
requests to be performed by authorized code.  This means the program
involved must be linked as authorized (anyone can do this), must ALSO be
loaded from an authorized library (these are carefully protected), and
must not be running in an address space containing any other executing
modules from a nonauthorized library (such modules might attempt to
corrupt the in memory copy of the authorized program code in some way). 
The ability to define a library as authorized is restricted, and the
ability to update the content of authorized libraries is also restricted
in order to prevent users from creating their own utilities that bypass
MVS security or compromise MVS integrity.  If an "approved" authorized
utility is deemed dangerous in the wrong hands, its use may be
restricted through the RACF Security Server by either disallowing READ
access to the authorized library where it resides or by disallowing
permission to execute that specific load module.

Some of the standard IBM utilities and some TSO commands run as
"authorized" programs.

docdwarf@panix.com wrote:
> 
> All right... here's a cute one.
…[48 more quoted lines elided]…
> DD
```

##### ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** docdwarf@panix.com
- **Date:** 2002-04-07T03:34:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8ospd$7p7$1@panix1.panix.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <3CAEB16B.CFF4C9DB@acm.org>`

```
In article <3CAEB16B.CFF4C9DB@acm.org>, Joel C. Ewing <jcewing@acm.org> wrote:

[snip]

>If it were smart
>enough apply strict validation on its parameters, and to allow a
…[5 more quoted lines elided]…
>time and resources to extend and throughly validate it first. 

And again, bingo... what I have been told three times is true.  You, Mr 
Trembley and Mr Bandke have all reported that someone will have to Do Some 
Work; this is, to say the least, unlikely.

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-04-09T21:33:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tdg6bus2arr1q1kjs1f2opio2strptqqhr@4ax.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <3CAEB16B.CFF4C9DB@acm.org> <a8ospd$7p7$1@panix1.panix.com>`

```
The work is already done, and yours for the asking

On 7 Apr 2002 03:34:05 -0400, docdwarf@panix.com wrote:

>In article <3CAEB16B.CFF4C9DB@acm.org>, Joel C. Ewing <jcewing@acm.org> wrote:
>
…[17 more quoted lines elided]…
>DD

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      The reward of a thing well done is to have done it. -- Emerson
      
        (Another bit of Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeeds.Com, Uncensored Usenet News ==----------
   http://www.newsfeeds.com       The Largest Usenet Servers in the World!
------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

###### ↳ ↳ ↳ Re: [OT] SVC 107 Authority Determined by... Library?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-09T15:59:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8vh7r$4ch$1@panix1.panix.com>`
- **References:** `<a8kbkb$ola$1@panix1.panix.com> <3CAEB16B.CFF4C9DB@acm.org> <a8ospd$7p7$1@panix1.panix.com> <tdg6bus2arr1q1kjs1f2opio2strptqqhr@4ax.com>`

```
In article <tdg6bus2arr1q1kjs1f2opio2strptqqhr@4ax.com>,
Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
>The work is already done, and yours for the asking

Most Honored, Respected, Generous and Gracious Mr Bandke... the work may 
have been done by you, granted, but the implementation of it here would 
require that someone here Do Work and... Rule #0 and all that; for me to 
have a Solution in hand to present to folks and then have to listen to all 
the Very Good Reasons that would be given for not implementing it would be 
a shame, a disappointment, a heart-break...

... what the hell, my heart is strong, this week.  Send it on to me, 
please, if you would be so kind.

DD

>
>On 7 Apr 2002 03:34:05 -0400, docdwarf@panix.com wrote:
…[35 more quoted lines elided]…
>------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
