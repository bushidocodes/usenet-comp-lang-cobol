[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The best approach for offloading - comments please

_6 messages · 6 participants · 1995-07_

---

### The best approach for offloading - comments please

- **From:** "pierre blanchette" <ua-author-15702344@usenetarchives.gap>
- **Date:** 1995-07-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3v3voq$8t4@news.aniq.com>`

```
Hi,

We decided to offload our COBOL mainframe development and have set up an
environment with MicroFocus and a couple of other products. Almost nobody
bothers to use it... Almost half a million dollars and no benefits!

I heard a lot of "success stories" but I would be curious to find out how
many shops did a post-evaluation of their offloading project and verified
if the return on investment was true or just another illusion.

We are about to try another approach. We will implement SPF/PC with
customized panels to look as close as possible as those we have on the
host. We will add Workbench, ProxMVS and tools that looks the most like
our mainframe tools (FileAid might be one). Our "ideal" environment would
be one where the programmer can't tell which CPU is running (370 or 486).
Graphics and nice colors may be appealing to pc programmers but it seems
that our mainframe programmers want everything... easy! (Which mean they
don't want to change their working habits)

Then we would add some extra productivity tools, especially for the
analysts. We hope that the excuses will be hard to find that way.

Your thoughs please...

Pierre Blanchette


////////////////////////////////////////////////////////////////////////
// //
// 4D61792074686520666F726365206265207769746820796F75 //
// //
////////////////////////////////////////////////////////////////////////
```

#### ↳ Re: The best approach for offloading - comments please

- **From:** "7161..." <ua-author-17086122@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-50abaaec98-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3v3voq$8t4@news.aniq.com>`
- **References:** `<3v3voq$8t4@news.aniq.com>`

```
Hi Pierre ...

I can't remember where I saw it but there is a product available
that interfaces PC workstations with MVS making file (program
source) movements transparent, i.e. your programmer basically
uses the ISPF panels to select what to edit and the file is
transparently transferred to the PC to be edited...check
Enterprise Systems Journal or Technical Support Magazine....

In any event, IBM's VSE/ESA platform will be supporting just this
type of architecture in it's upcoming releases...the workstation
will be an extension of the VSE environment and data objects will
be passed to the appropriate platform as required...I've also
been told that IBM will be supporting LE/370 type COBOL at the PC
workstation level and that it will be able to be cross-compiled
to any target IBM platform, i.e. MVS, VSE, AS/400, AIX, etc...I
think this will eventually be part of the VisualAge series of
workbenches.

Kevin P. Corkery
Independent Consultant
Voorhees, NJ  08043
COR··.@NAS··M.COM
```

#### ↳ Re: The best approach for offloading - comments please

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-50abaaec98-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3v3voq$8t4@news.aniq.com>`
- **References:** `<3v3voq$8t4@news.aniq.com>`

```
In article <3v3voq$8.··.@new··q.com>
Pierre Blanchette writes:

› 
› Hi,
…[8 more quoted lines elided]…
› 
Dear Pierre:
I've had a similar experience here. Here is my suggestions about
making things work smoothly:

1. Have class on how to use IBM PC and DOS and Windows for the
programmers.

2. Have class on how to use Microfocus animator and other tools.

3. Perhaps have a common server where IMS files are already set-up,
and perhaps have a repeatable set of test data.

Once the programmers are trained in the use of the PC, then
begin to require that the programs are tested using animator before
transfer to mainframe for quality assurance testing (final test).

Try to show the relevancy of using the PC via using client-server
eventually such as visual basic. Offer to transition the programmers
to work on client server.

The reasons programmers continue to use the mainframe are the following:
1. It takes time to create ims files on PC.
2. Transfer code from mainframe.
3. Load files.

versus mainframe:
1. load files.

The two primary advantages of the PC is the superior source-level
debugger (animator) and the saving of machine-cycles of the billable
mainframe machine time.

If you can hook the programmers on the debugger you will win them.
Consider having a system administrator create group wide DB/2 tables
on a server so the programmer don't have to reinvent the wheel for
every test.

Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

#### ↳ Re: The best approach for offloading - comments please

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1995-07-25T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-50abaaec98-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3v3voq$8t4@news.aniq.com>`
- **References:** `<3v3voq$8t4@news.aniq.com>`

```
In article <3v3voq$8.··.@new··q.com>
pbl··.@an··q.com "Pierre Blanchette" writes:
› We decided to offload our COBOL mainframe development and have set up an 
› environment with MicroFocus and a couple of other products. Almost nobody 
…[4 more quoted lines elided]…
› don't want to change their working habits)

Doesn't everyone want everything easy? That's why I prefer
evolution to revolution. Change slowly, automate, work closely
with a couple of users, apply the lessons learnt and soon you have
everyone _demanding_ to be upgraded :-)

If you can use a PC as a mainframe terminal, you're halfway there.

Richard Ross-Langley   +44 1727 852 801
Mine of Information Ltd,  PO BOX 1000,  St Albans AL3 5NY,  GB
=== Independent Computer Consultancy * Established in 1977 ===
```

#### ↳ Re: The best approach for offloading - comments please

- **From:** "rtw..." <ua-author-10778240@usenetarchives.gap>
- **Date:** 1995-07-26T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-50abaaec98-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3v3voq$8t4@news.aniq.com>`
- **References:** `<3v3voq$8t4@news.aniq.com>`

```
› We are about to try another approach. We will implement SPF/PC with 
› customized panels to look as close as possible as those we have on the 
…[5 more quoted lines elided]…
› don't want to change their working habits)

SPF/PC is a great solution if you want a text editor which is identical
to ISPF, but don't use it to create prototypes of mainframe panels.

Flexus has a product called CICS spII which runs on the PC.

It's very easy to learn and use, allows painting of 3270 style screens,
allows prototyping of 3270 screens as well as alowing creation of
complete user interface prototypes which run on the PC.

Mainframe Screens and System prototypes can be automatically turned
into mainframe source code with the code generator. Screen import tools
are also available.

Later on, the screen definitions can be imported directly into our COBOL
GUI solution. For more information, please send an e-mail request to
rtw··.@ep··x.net. Please include your mailing address.

Thanks.

Bob Wolfe
Flexus
************************************************************************
COBOL spII-The only *truly* COBOL-Oriented Graphical User Interface Tool
Phone: 610-588-9400
Fax: 610-588-9475
BBS: 610-863-4740 (must have authorization)
E-Mail:
Warning! This is a shameless, yet subtle product promo! Reader Beware!
************************************************************************
```

#### ↳ Re: The best approach for offloading - comments please

- **From:** "m..." <ua-author-17087552@usenetarchives.gap>
- **Date:** 1995-07-31T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-50abaaec98-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3v3voq$8t4@news.aniq.com>`
- **References:** `<3v3voq$8t4@news.aniq.com>`

```
Chris

I tried to mail you but it bounced so I'll post instead:

We have a PC development environment setup here using MicroFocus Workbench
with IMS and XDB (all Windows versions). I've got a couple of questions
about some of your comments:

[stuff deleted]
›
› 3. Perhaps have a common server where IMS files are already set-up,
› and perhaps have a repeatable set of test data.
Do I understand correctly that you are running the IMS catalogues and data
files off a common file server ? We currently have the files in c:\ims\data
on every PC - which means every user must gen their own PSBs, MFSs etc.
Is IMS designed to handle running against these files over a network (should
just be a matter of changing the env variable) ? Do you have any contention
problems (should only be read at runtime, not updated) ?

›  
› If you can hook the programmers on the debugger you will win them.
› Consider having a system administrator create group wide DB/2 tables
› on a server so the programmer don't have to reinvent the wheel for
› every test.
Are you running DB2 on OS/2 server as your database ? Are your PCs running
Windows or OS/2 ?

›  
› Chris Mason
…[3 more quoted lines elided]…
› LMSC5:  Tons of Beautiful Big Blue Iron...

Any other comments or advice would be appreciated

Thanks
Matt
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
