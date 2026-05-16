[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ISPF Tricks

_16 messages · 10 participants · 1999-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### ISPF Tricks

- **From:** "Torix" <Torixx@ameritech.net>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
Greetings,

I am in a fairly competitive program at work learning COBOL.   We are on an
emulated OS/390 system.  Often I find myself waiting for long periods of
time for compiles and submitted jobs to hit my hold Queue so I can see what
I have accomplished.

I know there are tricks to getting around in ISPF, and to speed up compile
and run times.   The manuals only give us the basics.

So I come to the experts, my friends here on the news group :)

Any and all shortcuts will be put to great use and much appreciated.
Thanking everyone ahead of time.

Torix
```

#### ↳ Re: ISPF Tricks

- **From:** "Lanny Levine" <llevine@sprint.ca>
- **Date:** 1999-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QdmD2.3716$SI4.731108@hme2.newscontent-01.sprint.ca>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
Any batch job can be written as a CLIST or REXX exec. When they are executed
they do not end up in a batch queue but run right away. However, your
systems area may not take kindly if everyone started  using CLISTs and/or
REXX execs to avoid the batch turn around time.

Lanny
```

#### ↳ Re: ISPF Tricks

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bm7dd$4i3$1@callisto.clark.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
In article <LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>,
Torix <Torixx@ameritech.net> wrote:

[snippage]

>Any and all shortcuts will be put to great use and much appreciated.
>Thanking everyone ahead of time.

Depending on your environment these 'shortcuts' can get you fired... are
you *sure* you want them?

DD
```

#### ↳ Re: ISPF Tricks

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bnjge$n0q$1@ash.prod.itd.earthlink.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```

Torix wrote in message ...

>Any and all shortcuts will be put to great use and much appreciated.
>Thanking everyone ahead of time.


Do your development on a PC and, when perfected, send the program
 to the mainframe.
```

#### ↳ Re: ISPF Tricks

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_hmD2.705$VR3.2052768@news4.mia>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
There are NO such Shortcuts.

What determines how long it takes is:
Which CLASS=  is used.  Different classes have differrent priorities.
They ALSO have different INITIATORS.  An initiator is what takes a
job from Input Queue and moves it the Active Status.  Sometimes
the Operators or Systems people FORGET to bring all the initiators
BACK UP.   ALSO, if you are remote, and going thru routers, sometimes
you'll be going thru several, and you get an occaissional lag in Interactive
response.

So, check with OPS for different classes, or just start at 1 and go thru 9
and A thru Z.  You'll get a lot where it just 'disappears' and some with
Access violations or not alloweds.

ALSO there is one 'TIP/TRICK', check your 'panels' for FOREGROUND
options, then you'll get almost instant results.
Torix wrote in message ...
>Greetings,
>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: ISPF Tricks

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Qe2F2.2998$bk.8227419@storm.twcol.com>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
>I know there are tricks to getting around in ISPF, and to speed up compile
>and run times.   The manuals only give us the basics.


As previously mentioned....these tips and tricks can get you fired and most
certainly will get you a call from system security. My current record is 2
days. @ days after starting a new account I received a pleasant call from
security warning me of running jobs in inappropriate job classes.

To avoid any problems get a procedure manual which lists the valid job
classes and pick out the ones which are not production/CICS/DB2 job classes.
Submit your job with the same name under as many job classes as you wish.
When one gets in cancel all of the others. This will get you in trouble in a
hurry if you use a production job class.

Converting the JCL to REXX EXECs or CLISTS can get very complicated if you
go beyond simple COBOL compiles. If you have IMS CICs or DB2 you will have
to run some kind of pre compiler. This really just complicates a semi simple
process. If you wish to convert your JCL to a REXX EXEC or CLIST I would
recommend asking the wonderful people in BIT.LISTSERV.TSOREXX or
COMP.LANG.REXX . What you will end up doing is converting each DD statement
to an ALLOC statement. Then you will CALL the compiler with a fully
qualified path such as :

CALL 'SYS1.COB2COMP(IGYCRCTL)'

There are ways around this, but they are beyond the scope of this
discussion.

I have developed several REXX EXECs which do this, but all of them create
JCL which is then submitted. Ask the people in one of the REXX newsgroups
for better detail.

When done dont forget to LINK-EDIT the object module created by the compile.

In the end it may be worth it to just wait, otherwise you will have 10
different versions of a compile EXEC like I do and only 1 works at your
current site. However if you are patient and spend the time to learn how to
do it in a REXX EXEC, especially one used as an EDIT macro, the things you
will learn will help you with many other things under TSO/ISPF/OS390.

REXX is a pandoras box. Once you learn it it will draw you away from what
you are supposed to be doing. So be careful.
```

##### ↳ ↳ Re: ISPF Tricks

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2PgF2.3269$bk.8726429@storm.twcol.com>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com>`

```
I have attached a COBSYNTX REXX EXEC which will compile in the foreground,
check listing for errors, and insert notes in appropriate position in your
source file when using ISPF EDIT or "ISREDIT". I haven't used it in quite a
while and it is rather complicated, but here it is. You will most definitely
have some problems with this as it is specialized to a particular site's
settings. One known problem is that it cannot handle CICS and DB2 programs,
only one or the other not both. You also may get some errors with CICS
programs which are simply CICS syntax embedded in COBOL using an EXEC
CICS/END-EXEC block.

This is intended to be a syntax checker, not a compiler. It does run the
actual compiler, but only to get the LISTING produced by said compiler.
Eventually you will have to submit an actual compile using JCL, but this
should save time debugging most of the syntax errors.

When you eventually do submit your compile you can try a PRTY=15 setting on
the job card. This will set your job to the highest priority and most likely
move to the front of the queue. Sometimes this option is turned off by the
systems programmers to prevent jumping to the front of the line.

It will definitely get you in trouble if you are not allowed to do this.
Even if you are, some people watch the QUEUEs and yell at you when you do
such an inconsiderate thing.

If your compile JCL does not insert the COBOL source code in-stream you can
try submitting your JCL with a TYPRUN=HOLD parameter on the JOB CARD. This
will submit your JCL as normal with no special job priorities and will not
get you more CPU time. IT WILL however eventually get your job to the front
of the QUEUE. Then when you are ready you can release the job and it will
then be the very next job to get into the QUEUE. You may want to submit
several of these at a time to have a few waiting. Otherwise everytime you
release a job you will have to wait in line again to get to the front of the
QUEUE.

As with all of my previous suggestions this may get you in trouble, but
certainly not as much as the previous suggestion. While your jobs may be at
the front of the QUEUE, they are letting everything else through, not tying
anything else up except maybe positions in line.

good luck.
```

##### ↳ ↳ Re: ISPF Tricks

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c3pj9$skl$1@clarknet.clark.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com>`

```
In article <Qe2F2.2998$bk.8227419@storm.twcol.com>, Jeff <a@a.com> wrote:
>>I know there are tricks to getting around in ISPF, and to speed up compile
>>and run times.   The manuals only give us the basics.
…[5 more quoted lines elided]…
>security warning me of running jobs in inappropriate job classes.

Two days?  Laggard!  Slacker!  Slug-a-bed!  Two days, indeed... *I*
usually get *my* call before noon of the first day I'm on site... and it
usually goes something like this:

Ops: 'You shouldn't be running jobs in that class.'
Me:  'No problem, I'm new here... how do I find out what classes are
permitted for my use?'
O: 'Job classes are dependent on the amount of CPU time you need and the
kind of system devices you need; class Q is for Prod and you shouldn't use
that.'
M: 'Yes, I understand... whose job is it to tell me which classes I can
and cannot use?'
O: 'That's your job to find out... ask your Project Leader.'
M: 'Of course... and if my Project Leader is new here, too, and doesn't
know?'
O: 'Then have your Project Leader call us to find out.'
M: 'What will my Project Leader do when he calls you to find out?'
O: 'He'll talk to us then and we'll tell him.'
M: 'Oh... you mean he'll talk to you then and you'll tell him then?'
O: 'Yes, that's right.'
M: 'Well, I'm talking to you now... why can't you tell me now?'
O: 'One moment, please... there, I was just putting your ID on the 'Give
These Jobs One CPU-Cycle Per Week' list'.


Next week... How To Find Out Printer Addresses and Forms!

DD
```

###### ↳ ↳ ↳ Re: ISPF Tricks

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ugF2.3264$bk.8712631@storm.twcol.com>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net>`

```
>Two days?  Laggard!  Slacker!  Slug-a-bed!  Two days, indeed... *I*
>usually get *my* call before noon of the first day I'm on site... and it
…[22 more quoted lines elided]…
>


What about when you use the PRTY=15 job card parameter?
```

###### ↳ ↳ ↳ Re: ISPF Tricks

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c6gl3$40e$1@clarknet.clark.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net> <1ugF2.3264$bk.8712631@storm.twcol.com>`

```
In article <1ugF2.3264$bk.8712631@storm.twcol.com>, Jeff <a@a.com> wrote:
>>Two days?  Laggard!  Slacker!  Slug-a-bed!  Two days, indeed... *I*
>>usually get *my* call before noon of the first day I'm on site... and it
…[25 more quoted lines elided]…
>What about when you use the PRTY=15 job card parameter?

Disabled feature/ignored/superseded by system software/makes men in black
hoods with firearms come out of the wall... the usual.

DD
```

###### ↳ ↳ ↳ Re: ISPF Tricks

_(reply depth: 5)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E703C1.24E63FA1@att.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net> <1ugF2.3264$bk.8712631@storm.twcol.com> <7c6gl3$40e$1@clarknet.clark.net>`

```
docdwarf@clark.net wrote:
> 
(snip)
> 
> Disabled feature/ignored/superseded by system software/makes men in black
> hoods with firearms come out of the wall... the usual.

Such a kinky little fellow you are!

Bill Lynch <g>
```

###### ↳ ↳ ↳ Re: ISPF Tricks

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 1999-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c8ntk$bvl$1@clarknet.clark.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <1ugF2.3264$bk.8712631@storm.twcol.com> <7c6gl3$40e$1@clarknet.clark.net> <36E703C1.24E63FA1@att.net>`

```
In article <36E703C1.24E63FA1@att.net>,
William Lynch  <wblynch@worldnet.att.net> wrote:
>docdwarf@clark.net wrote:
>> 
…[5 more quoted lines elided]…
>Such a kinky little fellow you are!

Sure took you long enough to figure that'un out!

DD
```

###### ↳ ↳ ↳ Re: ISPF Tricks

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c4bfp$3jc$1@news.igs.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net>`

```
You are quite lucky, actually.  My conversations have been going like:

Is the software ready?
Me: In finall testing.  How about the hardware?
Them:Well, we are going to confirm the order this week.
Me:  Wait a minute, I am supposed to install a week Friday.
Then: They assure us it will be ready.
Me: What about the fibre optic runs?  (300 miles of custom cable)
Them: They are starting Friday.
Me:  And it will be ready a week friday?
Them: yes, do not worry about it.
Me:  And you have all the hubs, etc.?
Them:  What is a hub?
Me: Right.  The electrician has been in to install power?
Them.  Power?
Me:  Okay.  Do you have my tape with the test data?
Them:Yes.  Here it is.  You are sure that it will be ready?
Me:  I will have the computer, and the software ready to plug
into the network.
Them:  Good.  I have assured managament that we are on schedule and
everything will run when we throw the switch a week Friday.
Me: When will the network be ready to test?
Them: as soon as the cables are installed.
Me:  Good.  Isn't FM technology wonderfull?
Them: What is FM technology?
Me:  Fucking Magic.

docdwarf@clark.net wrote in message <7c3pj9$skl$1@clarknet.clark.net>...
>In article <Qe2F2.2998$bk.8227419@storm.twcol.com>, Jeff <a@a.com> wrote:
>>>I know there are tricks to getting around in ISPF, and to speed up
compile
>>>and run times.   The manuals only give us the basics.
>>
>>
>>As previously mentioned....these tips and tricks can get you fired and
most
>>certainly will get you a call from system security. My current record is 2
>>days. @ days after starting a new account I received a pleasant call from
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ISPF Tricks

_(reply depth: 4)_

- **From:** "james walker" <james.walker2@worldnet.att.net>
- **Date:** 1999-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be6da1$6fe08560$bc464a0c@fofyplfq>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net> <7c4bfp$3jc$1@news.igs.net>`

```
been there, done that, had that happen!!!!!!

Donald Tees <donald@wilmack.com> wrote in article
<7c4bfp$3jc$1@news.igs.net>...
> You are quite lucky, actually.  My conversations have been going like:
> 
…[26 more quoted lines elided]…
> >In article <Qe2F2.2998$bk.8227419@storm.twcol.com>, Jeff <a@a.com>
wrote:
> >>>I know there are tricks to getting around in ISPF, and to speed up
> compile
…[5 more quoted lines elided]…
> >>certainly will get you a call from system security. My current record
is 2
> >>days. @ days after starting a new account I received a pleasant call
from
> >>security warning me of running jobs in inappropriate job classes.
> >
…[8 more quoted lines elided]…
> >kind of system devices you need; class Q is for Prod and you shouldn't
use
> >that.'
> >M: 'Yes, I understand... whose job is it to tell me which classes I can
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ISPF Tricks

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cgfj7$9kv$1@news.igs.net>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net> <Qe2F2.2998$bk.8227419@storm.twcol.com> <7c3pj9$skl$1@clarknet.clark.net> <7c4bfp$3jc$1@news.igs.net> <01be6da1$6fe08560$bc464a0c@fofyplfq>`

```

james walker wrote in message <01be6da1$6fe08560$bc464a0c@fofyplfq>...

>been there, done that, had that happen!!!!!!


You have my sympathy.
```

#### ↳ Re: ISPF Tricks

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1999-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e53f37.7134968@news.teo-computer.com>`
- **References:** `<LxlD2.441$oq2.474355@nntp0.chicago.il.ameritech.net>`

```
On Wed, 3 Mar 1999 20:31:18 -0500, "Torix" <Torixx@ameritech.net>
wrote:

>Greetings,
>
…[14 more quoted lines elided]…
>

Becareful bypassing the Batch Queue.  Shop management tend to take a
very negative view of mavericks bypassing shop institutited standards.

REXX can greatly facilitate your tool sets if used properly, but used
improperly, it can be a drain on resources.

Example:  If every programmer has and used REXX as a hot reader to
compile programs, the Batch Queue would be brought to it's knees.  

OTOH, if your shop would develop a REXX screen for submitting batch
compiles, capable of submitting multiple programs, from any location
to a range of linklibs, option to link or not, include debugging
options (ie. Intertest, Expeditor, ViaSoft), even an option to hook in
a shop program to check that your program(s) meet shop standards.
Then you wouldn't have to keep multiple compile jobstreams, and take
time to jury-rigging those jobstreams to meet your needs.  (Oh the joy
of waiting in Queue, only to get kicked out with a JCL error, when you
finally execute).

There are REXX ngs:  comp.lang.rexx, and bit.listserv.tsorexx



Tim Oxler
Teo Computer
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
