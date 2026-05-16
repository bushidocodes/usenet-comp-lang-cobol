[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# JCL question

_9 messages · 9 participants · 2002-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### JCL question

- **From:** "Joe Brault" <jbrault@niu.edu>
- **Date:** 2002-02-04T20:09:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c5eea62_7@news.uncensored-news.com>`

```
Hello,

    I am a Computer Science student at NIU taking a course in COBOL this
semester.  During one of our lectures our professor covered jcl with us, but
didn't say much about it... saying something to the effect: 'everyone uses
it, and so does our server, so you have to include it in your code.'  In my
search for information about jcl, I found a book at my local bookstore from
IBM entitled:  MVS JCL Reference.  I was wondering if anyone could point me
to any references for jcl on the internet?  I would like to get a background
of this language, so I know what it's doing with my code :)  Any help is
appreciated, thanks in advance!

The code hungry student,

 - Joe :)



______________________________________________________________________
Posted Via Uncensored-News.Com - Still Only $9.95 - http://www.uncensored-news.com
   With NINE Servers In California And Texas - The Worlds Uncensored News Source
```

#### ↳ Re: JCL question

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-04T14:47:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3ms1j$i8u$1@nntp9.atl.mindspring.net>`
- **References:** `<3c5eea62_7@news.uncensored-news.com>`

```
There are lots of references for JCL, but what I think you might want to
start with is:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg00/2.1.1?

which talks about the JCL needed at compile time ("2.1.1 Compiling with
JCL")

You may also want to look thru that manual for various "environments" that
you might want to RUN (execute) your program in (such as CICS, IMS, DB2,
Unix, OO) - and how JCL is used at "execution time".

This "programming guide" relates JCL to "COBOL" programs.
```

#### ↳ Re: JCL question

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-02-05T01:20:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1ade3$4b391c60$3d31e641@chottel>`
- **References:** `<3c5eea62_7@news.uncensored-news.com>`

```
I think Gary Deward Brown has the best JCL book.

<snip>
```

#### ↳ Re: JCL question

- **From:** docdwarf@panix.com
- **Date:** 2002-02-04T20:28:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3ncgr$lj5$1@panix1.panix.com>`
- **References:** `<3c5eea62_7@news.uncensored-news.com>`

```
In article <3c5eea62_7@news.uncensored-news.com>,
Joe Brault <jbrault@niu.edu> wrote:

[snippage]

>I was wondering if anyone could point me
>to any references for jcl on the internet?  I would like to get a background
>of this language, so I know what it's doing with my code :)  Any help is
>appreciated, thanks in advance!

Well, it isn't on the web... and it *is* a rather recent volume, my copy 
is the 1985 reprint with corrections... but I have found that it is hard 
to beat a copy of 'OS JCL and Utilities' by Michael Trombetta and Sue 
Carolyn Finkelstein (Addison-Wesley Publishing Co.)

DD
```

#### ↳ Re: JCL question

- **From:** Opus <yo_dog40@hotmail.com>
- **Date:** 2002-02-05T12:11:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uh406ukpsl47apu2jenao30ruj3p369jbi@4ax.com>`
- **References:** `<3c5eea62_7@news.uncensored-news.com>`

```
On 4 Feb 2002 20:09:07 GMT, "Joe Brault" <jbrault@niu.edu> wrote:

>Hello,
>
…[8 more quoted lines elided]…
>appreciated, thanks in advance!

Get the book by Gary Deward Brown.

Jeff..
>
>The code hungry student,
…[8 more quoted lines elided]…
>
```

#### ↳ Re: JCL question

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-02-05T13:03:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ED5D33EB4490D35.644E8757A32C76B0.D75643E16F82B365@lp.airnews.net>`
- **References:** `<3c5eea62_7@news.uncensored-news.com>`

```
On 4 Feb 2002 20:09:07 GMT, "Joe Brault" <jbrault@niu.edu> enlightened
us:

>Hello,
>
…[13 more quoted lines elided]…
>

Where or what is NIU?

JCL is a mainframe computer thing..not a server thing.  It stands for
Job Control Language.  There are, in the IBM mainframe world, two
kinds of JCL..one runs under the VSE operating system and the other
runs under the MVS operating system.  You do not put JCL in your code
unless you are generating JCL to be written to a system reader that
will later be run and execute something else.

As for reference, others in this thread have given you some good
examples.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I don't have a big ego, I'm way too cool for that.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: JCL question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-02-05T13:49:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<imd06uogjj87ql7jtscn80qjg8plvg1e89@4ax.com>`
- **References:** `<3c5eea62_7@news.uncensored-news.com> <6ED5D33EB4490D35.644E8757A32C76B0.D75643E16F82B365@lp.airnews.net>`

```
On Tue, 05 Feb 2002 13:03:22 -0500 SkippyPB <swiegand@neo.rr.com> wrote:

:>On 4 Feb 2002 20:09:07 GMT, "Joe Brault" <jbrault@niu.edu> enlightened
:>us:

:>>    I am a Computer Science student at NIU taking a course in COBOL this
:>>semester.  During one of our lectures our professor covered jcl with us, but
:>>didn't say much about it... saying something to the effect: 'everyone uses
:>>it, and so does our server, so you have to include it in your code.'  In my
:>>search for information about jcl, I found a book at my local bookstore from
:>>IBM entitled:  MVS JCL Reference.  I was wondering if anyone could point me
:>>to any references for jcl on the internet?  I would like to get a background
:>>of this language, so I know what it's doing with my code :)  Any help is
:>>appreciated, thanks in advance!

:>>The code hungry student,

:>Where or what is NIU?

Northern Illinois University.

One of the few colleges still teaches system programming for IBM mainframes.

:>JCL is a mainframe computer thing..not a server thing.  It stands for
:>Job Control Language.  There are, in the IBM mainframe world, two
:>kinds of JCL..one runs under the VSE operating system and the other
:>runs under the MVS operating system.  You do not put JCL in your code
:>unless you are generating JCL to be written to a system reader that
:>will later be run and execute something else.

Or as a wrapper for his job.

The instructor should be providing all JCL required.

:>As for reference, others in this thread have given you some good
:>examples.

Yep.
```

###### ↳ ↳ ↳ Re: JCL question

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-02-07T11:39:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0202071139.23a069d3@posting.google.com>`
- **References:** `<3c5eea62_7@news.uncensored-news.com> <6ED5D33EB4490D35.644E8757A32C76B0.D75643E16F82B365@lp.airnews.net> <imd06uogjj87ql7jtscn80qjg8plvg1e89@4ax.com>`

```
For what it's worth, I've used the following to delete both tape and
disk PS and PO cataloged datasets.

The ,,DEFER keeps tapes from being mounted and the ops guys from
becoming rabid.  The SYSDA and SPACE is ignored if the dataset is a
tape.  The catalog is used to get the UNIT info. The same goes for the
DCB. They're only used if the dataset doesn't exist.

The SET stmt isn't really necessary, but I keep forgetting the comma
(,) when I overtype the DSN, so I use it.

//DELJOB   JOB etc.		
//         SET MYDSN=my.dsn.for.example
//DELSTEP EXEC PGM=IEBBR14
//DELDD     DD DSN=&MYDSN,
//             DISP=(MOD,DELETE,DELETE),
//             UNIT=(SYSDA,,DEFER),
//             SPACE=(TRK,0),
//             DCB=(SYS1.MACLIB,DSORG=PS)



Binyamin Dissen <postingid@dissensoftware.com> wrote in message news:<imd06uogjj87ql7jtscn80qjg8plvg1e89@4ax.com>...
> On Tue, 05 Feb 2002 13:03:22 -0500 SkippyPB <swiegand@neo.rr.com> wrote:
> 
…[35 more quoted lines elided]…
> Yep.
```

###### ↳ ↳ ↳ Re: JCL question

_(reply depth: 4)_

- **From:** Jerry <cormwu@ntsource.com>
- **Date:** 2002-02-10T22:57:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C674F38.80E99ED6@ntsource.com>`
- **References:** `<3c5eea62_7@news.uncensored-news.com> <6ED5D33EB4490D35.644E8757A32C76B0.D75643E16F82B365@lp.airnews.net> <imd06uogjj87ql7jtscn80qjg8plvg1e89@4ax.com> <8a2d426e.0202071139.23a069d3@posting.google.com>`

```
I graduated from NIU.  Yes it is true that NIU still teach mainframe.
I learned mainframe in the college.  I had considered to learn Java to
join internet madness.  I am glad that I still doing mainframe.  Look
at outside of world.  There were too many java, internet developers.
Many of them lose their jobs.  Many people said COBOL and mainframe
would die.  The fact is many big company will not give up with mainframe.
Mainframe can process large amount of data which pc can.  Mainframe
is also much faster then pcs.  I have been working with mainframe for
about 6 years.  I will continue working on mainframe.  I think there many
people agree with me.



Jack Sleight wrote:

> For what it's worth, I've used the following to delete both tape and
> disk PS and PO cataloged datasets.
…[56 more quoted lines elided]…
> > Yep.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
