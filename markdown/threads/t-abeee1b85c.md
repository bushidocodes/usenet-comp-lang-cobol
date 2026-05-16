[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/390:DB2 Query

_6 messages · 5 participants · 2000-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### OS/390:DB2 Query

- **From:** "Curious" <leng1@bigfoot.com>
- **Date:** 2000-10-26T10:22:35+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t84c2$phi$1@coco.singnet.com.sg>`

```
Hi,

I have encountered a problem in DB2 when doing the query.

Just wondering, is there a way to SAVE the query that I have
created from the DB2 file so that I can refer back as and
when I want. You see,  I had to always redo the whole
things from scratch to select those fields that I want to see
from the DB2 file, the condition etc and F6 again to execute.

I have asked around and it seems that the answer is No.
I think there must be a way to do it else it will take
up a lot of the time to always do this thing.

Well, hope to hear some comments/solution on this :->


Tks&Rgds :->
```

#### ↳ Re: OS/390:DB2 Query

- **From:** timcoffey@my-deja.com
- **Date:** 2000-10-26T02:46:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t85te$hb7$1@nnrp1.deja.com>`
- **References:** `<8t84c2$phi$1@coco.singnet.com.sg>`

```
In article <8t84c2$phi$1@coco.singnet.com.sg>,
  "Curious" <leng1@bigfoot.com> wrote:
> Hi,
>
…[7 more quoted lines elided]…
>

Is this QMF? I don't use QMF. Are you accessing the mainframe from
a PC using terminal emulation? If so, (and if it supports cut and
paste), you could save the SQL in Notepad and cut and paste onto the
3270 emulator program.

Tim


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: OS/390:DB2 Query

- **From:** "Curious" <leng1@bigfoot.com>
- **Date:** 2000-10-26T12:04:39+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t8abc$q5r$1@coco.singnet.com.sg>`
- **References:** `<8t84c2$phi$1@coco.singnet.com.sg> <8t85te$hb7$1@nnrp1.deja.com>`

```
Hi Tim

Indeed,I am accessing the mainframe from
a PC using terminal emulation.

What do u mean by cut and paste onto the
3270 emulator program ?

My only concern is that whether I can save the
query from my DB2 in the OS/390 and query back as and
when required without having to redo the whole query again.

Even if I cut and paste onto the notepad, I will have to redo
my whole query again for my DB2 in the system if I want to
execute and see again, is it ?  :->




<timcoffey@my-deja.com> wrote in message news:8t85te$hb7$1@nnrp1.deja.com...
> In article <8t84c2$phi$1@coco.singnet.com.sg>,
>   "Curious" <leng1@bigfoot.com> wrote:
…[20 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: OS/390:DB2 Query

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-26T23:22:56+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F82220.520BF573@zip.com.au>`
- **References:** `<8t84c2$phi$1@coco.singnet.com.sg>`

```
Curious wrote:

> Hi,
>
…[14 more quoted lines elided]…
> Tks&Rgds :->

Consider using Batch QMF rather than online.   You then simply save it
and submit the job.

Ken
```

##### ↳ ↳ Re: OS/390:DB2 Query

- **From:** "mangogwr" <mangogrower@telocity.co>
- **Date:** 2000-10-26T22:46:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<156K5.20821$Q8.4200629@newsrump.sjc.telocity.net>`
- **References:** `<8t84c2$phi$1@coco.singnet.com.sg> <39F82220.520BF573@zip.com.au>`

```
My Goodness, everyone with DB2 has SPUFI  don't they?

SPUFI lets you do exactly that
and it comes usually with DB2.

Ken Foskey <waratah@zip.com.au> wrote in message
news:39F82220.520BF573@zip.com.au...
> Curious wrote:
>
…[22 more quoted lines elided]…
>
```

#### ↳ Re: OS/390:DB2 Query

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-10-27T02:57:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001026225754.23735.00000624@ng-ca1.aol.com>`
- **References:** `<8t84c2$phi$1@coco.singnet.com.sg>`

```
Yes there is a way to save your query but at the moment I don't have the
directions.

I'll check my cheat sheet at work and get back to you.

When you run the query you use PF2 to run it and then there is another PF key
to save it once you've got it the way you want from the screen you typed it
into.

As for the cut and paste - open a text document on the desktop of your PC and
then cut/paste from the mainframe screen to it to save the query until I get
back to ya :)

Eileen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
