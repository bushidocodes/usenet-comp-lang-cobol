[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to check a filesize in JCL

_8 messages · 6 participants · 2003-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How to check a filesize in JCL

- **From:** sahus@hotmail.com (Srini)
- **Date:** 2003-05-09T14:23:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<186e13cf.0305091323.11a9e443@posting.google.com>`

```
Hi JCL Guru's

I would appreciate if you can provide a solution to my problem

Is there a way to determine a filsize in a JCL Step. Basically number
of records in the file.

e.g:-
My job requires to execute STEP1 if there are no records in a
TSOID.FILE.NAME else STEP2.

Right now we are calling a cobol program to do this. Its kind of
getting messy since we are doing this a lot more times than i wanted
it to.

The effort I put on this problem before I posted here is to use
SYNCSORT, FILESZ parameter but this is not really helping my cause.

Thanks for your time
Srini
```

#### ↳ Re: How to check a filesize in JCL

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-05-09T20:18:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C233C3.20184609052003@corp.supernews.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com>`

```
In article <186e13cf.0305091323.11a9e443@posting.google.com>,
 sahus@hotmail.com (Srini) wrote:

> Hi JCL Guru's
> 
…[17 more quoted lines elided]…
> Srini

The only way to make a decision in JCL is based on a return code of a 
previous step.  So you will really need three steps.  The first should 
execute some utility, IDCAMS or IEBGENER can give you an RC=4 if you try 
to copy an empty dataset, or you can roll your own with assembler -- 
open the file and see if the first thing is an end of file marker.

The execute STEP1 with a COND=(STEPTEST,EQ,4) and STEP2 with a 
COND=(STEPTEST,NE,4)...

Hope that helps.
```

#### ↳ Re: How to check a filesize in JCL

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-09T19:30:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305091830.334c3f31@posting.google.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com>`

```
Hi Srini,

Use this step before your other 2 steps.

//  EXEC IDCAMS  
//SYSIN DD *
 PRINT INDATASET=('your.data.set') COUNT(1)

If 'your.data.set' exists and contains no data, the step RC=4.
If 'your.data.set' does not exist             , the step RC=12.
If 'your.data.set' exists and contains data,    the step RC=0.

Now code the COND param of you subsequent steps accordingly.

Regards, Jack.


sahus@hotmail.com (Srini) wrote in message news:<186e13cf.0305091323.11a9e443@posting.google.com>...
> Hi JCL Guru's
> 
…[17 more quoted lines elided]…
> Srini
```

##### ↳ ↳ Re: How to check a filesize in JCL

- **From:** "scarface" <scarface@scarface.com>
- **Date:** 2003-05-11T02:53:58+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2003.05.10.18.53.42.924618@scarface.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com> <8a2d426e.0305091830.334c3f31@posting.google.com>`

```
On Fri, 09 May 2003 19:30:47 -0700, Jack Sleight wrote:

> Hi Srini,
> 
…[35 more quoted lines elided]…
>> Srini

or you can do a repro

  ..
  REPRO INDA('IN.FILE') OUTDA('OUT.FILE') COUNT(1)

  This will fail if IN.FILE is empty and Jacks solution
  applies here as well.
```

###### ↳ ↳ ↳ Re: How to check a filesize in JCL

- **From:** "David Binkowski" <dcbinkowski@ameritech.net>
- **Date:** 2003-05-10T23:11:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VGfva.11898$%_3.6358467@newssrv26.news.prodigy.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com> <8a2d426e.0305091830.334c3f31@posting.google.com> <pan.2003.05.10.18.53.42.924618@scarface.com>`

```
Hey Srini, does your last name begin with a "B" ?
```

##### ↳ ↳ Re: How to check a filesize in JCL

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-10T14:01:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305101301.79d933c2@posting.google.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com> <8a2d426e.0305091830.334c3f31@posting.google.com>`

```
Hi Srini,

Just a clarification of the phrase "contains no data". 

Not every "empty" file returns a valid EOF indication when a read
operation is performed against it.

A file that has been allocated space but never opened and closed for
output operations returns an error indication when a read is
attempted. In this situation the IDCAMS step described below returns
an RC=12.

If the file contained records and all were susequently deleted, or the
file was opened and closed for output operations without writing a
record to the file, then the IDCAMS step returns a RC=4.

Jack.

jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0305091830.334c3f31@posting.google.com>...
> Hi Srini,
> 
…[35 more quoted lines elided]…
> > Srini
```

#### ↳ Re: How to check a filesize in JCL

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-05-11T22:31:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EBF076C.75413BAF@ix.netcom.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com>`

```
Srini wrote:
> 
> Hi JCL Guru's
…[4 more quoted lines elided]…
> of records in the file.

You wouldn't be in Columbus OH would you?

You will want to execute IKJEFT01 (TSO in batch). There you
will want to run either a REXX or CLIST that will query the
type of file (LISTCAT). If VSAM, you can get back the number
of records. If xSAM, then you can find out how much of the
file is used. 

I think the command you are after is STATE.

At any rate, you can make these determinations from with the
the REXX or CLIST and cause the RC to be set accordingly
which you can then process using JCL IF logic.
```

##### ↳ ↳ Re: How to check a filesize in JCL

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-12T13:43:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305121243.203ea712@posting.google.com>`
- **References:** `<186e13cf.0305091323.11a9e443@posting.google.com> <3EBF076C.75413BAF@ix.netcom.com>`

```
Srini,

If you're still out there, drop us a line to clarify what you want to
know.

You ask how to detemine the # of recs in a file, but show an example
that requires to know if the file is "empty" or not.

As you can see from the replies, each requires a different solution.
Actually Steve's solution solves both interpretations, but, in my
opinion, is overkill as an "empty" file solution. (No offense
intended, Steve.)

Regards, Jack. 


Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com> wrote in message news:<3EBF076C.75413BAF@ix.netcom.com>...
> Srini wrote:
> > 
…[29 more quoted lines elided]…
> attorney's fees) for collecting this fee.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
