[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Xpeditor

_5 messages · 5 participants · 2002-07 → 2002-08_

---

### Xpeditor

- **From:** "Tim Cordsen" <extern.tim.cordsen@volkswagen.de>
- **Date:** 2002-07-23T11:07:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahj6d9$6bh2@doiweb4.volkswagen.de>`

```
Hello everybody,
is there anyone experienced in using Xpeditor?
I just wrote a dialo-program and tried to run it, but it doesn't, so I would
like to use Xpeditor to find the logical errors.
But it is not installed in my Host-Account. Can anybody tell me what I have
to do to use it, are there any files I should have in my working area? How
will I have to change compiling?
The system I work on is IBM OS/390 DB/2 and a tool named proba, where you
can combine functions to a compile-job, you just have to type prodpr.

Thanks in advance for your advices.

Tim Cordsen
```

#### ↳ Re: Xpeditor

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-07-24T03:52:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020723235242.25081.00000346@mb-fs.aol.com>`
- **References:** `<ahj6d9$6bh2@doiweb4.volkswagen.de>`

```
>From: "Tim Cordsen" extern.tim.cordsen@volkswagen.de 
>Date: 7/23/02 5:07 AM Eastern Daylight Time

>I would
>like to use Xpeditor to find the logical errors.
>But it is not installed in my Host-Account. 

I don't quite understand what you mean by this statement.  Are you saying your
TSO account doesn't have access to Xpeditor or that it isn't available period? 
I'm assuming also batch Xpeditor.

Yes there are certain files you need to use it.  Off the top of my head I don't
remember the names so I'll have to pull up my TSO profile and get them for you.
 It may be that my shop has renamed them (which they love to do) but you can
probably find out the equivalents where you are.
```

##### ↳ ↳ Re: Xpeditor

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-07-24T10:42:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DE2A082DC14266CC.9151217B97733C7D.36DC8CE6F368FCA9@lp.airnews.net>`
- **References:** `<ahj6d9$6bh2@doiweb4.volkswagen.de> <20020723235242.25081.00000346@mb-fs.aol.com>`

```
On 24 Jul 2002 03:52:42 GMT, yukonmama@aol.com (YukonMama) enlightened
us:

>>From: "Tim Cordsen" extern.tim.cordsen@volkswagen.de 
>>Date: 7/23/02 5:07 AM Eastern Daylight Time
…[12 more quoted lines elided]…
>probably find out the equivalents where you are.

In addition, your program has to be compiled using certain CBL options
and the output has to be placed in an Xpeditor file.  

I'm not famaliar with Xpeditor in batch, but can help with Xpeditor in
CICS.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #105:

Yesterday it worked.
Today it is not working.
Windows is like that.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Xpeditor

- **From:** "Kjeld Hansen" <paabol@12mail.dk>
- **Date:** 2002-07-27T00:25:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d41cc3e$0$195$edfadb0f@dspool01.news.tele.dk>`
- **References:** `<ahj6d9$6bh2@doiweb4.volkswagen.de>`

```
First of all, you should contact someone responsible for the software
licenses on your installation, to find out if your installation have an
active Xpediter software license. If so, you could try invoking Xpediter by
typing XPEDITER or TSO XPEDITER on a TSO command line.

You dont't have to code special statements to use Xpediter, but you will
have modify your compiling rutines to include a processor that will generate
a symbolics member from the program module (actually from the compile list).
A symbolics member contains the source statements and maps the data and
program  storage to the source statements, and it is stored in a separate
PDS . This change should be implemented by the persons that are responsible
for installing software.

If you can start Xpediter, the only things needed is to allocate the data
files your program needs, with the ALLOC command. You can select the
DD-names from your test JCL and save the allocation specification for later
user. Then you have to specify load module name and a DB2 plan name, and you
are up and running!

If you are not familiar with Xpediter commands, you could try pressing PF1,
which will bring up Xpediter's help screens. Basically you can single step
your way through your module's statements, insert breakpoints to make
execution stop on certain points, inspect and modify data storage, and
insert commands in the execution sequence, with or without conditional
tests.

Kjeld P. Hansen

"Tim Cordsen" <extern.tim.cordsen@volkswagen.de> skrev i en meddelelse
news:ahj6d9$6bh2@doiweb4.volkswagen.de...
> Hello everybody,
> is there anyone experienced in using Xpeditor?
> I just wrote a dialo-program and tried to run it, but it doesn't, so I
would
> like to use Xpeditor to find the logical errors.
> But it is not installed in my Host-Account. Can anybody tell me what I
have
> to do to use it, are there any files I should have in my working area? How
> will I have to change compiling?
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Xpeditor

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2002-08-01T15:00:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D49AF7A.7C263308@attglobal.net>`
- **References:** `<ahj6d9$6bh2@doiweb4.volkswagen.de>`

```
If your shop doesn't have Xpediter, you might have the IBM Debug Tool (which
supports COBOL for OS/390 & VM, PL/1 FORTRAN, and C/C++).  This tool is fully
capable of debugging a COBOL program, even one running under CICS or IMS, or
using DB2.

If you have BookManager READ on the mainframe (and it's a standard part of
OS/390 and z/OS), and have a COBOL for OS/390 bookshelf, there should be a book
there telling about Debug Tool.

Tim Cordsen wrote:

> Hello everybody,
> is there anyone experienced in using Xpeditor?
…[10 more quoted lines elided]…
> Tim Cordsen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
