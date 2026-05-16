[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL emulators

_4 messages · 4 participants · 2010-09_

---

### COBOL emulators

- **From:** RealInfo <therightinfo@gmail.com>
- **Date:** 2010-09-07T13:09:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com>`

```
Hi all
Is it possible to develop COBOL based applications on PC so that they
will
run eventually on a MAINFRAME ?

I want to develop COBOL  based applications for mainframes.
the thing is I do not have a mainframe , so are there some mainframe
emulators
that run on pc so it can be done ?

Thanks
EC
```

#### ↳ Re: COBOL emulators

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2010-09-07T16:17:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i666lu$ota$1@news.eternal-september.org>`
- **References:** `<70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com>`

```
"RealInfo" <therightinfo@gmail.com> wrote in message 
news:70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com...
> Hi all
> Is it possible to develop COBOL based applications on PC so that they
…[6 more quoted lines elided]…
> that run on pc so it can be done ?


It would be helpful if you indicated which mainframe (including OS and other 
relevant software) you are thinking about (eg: IBM z/OS with~without CICS). 
It is a big world out there...
```

#### ↳ Re: COBOL emulators

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2010-09-07T23:06:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c86a929$0$6274$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com>`
- **References:** `<70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com>`

```
Am 07.09.2010 22:09, schrieb RealInfo:
> I want to develop COBOL  based applications for mainframes.
> the thing is I do not have a mainframe , so are there some mainframe
> emulators
> that run on pc so it can be done ?

   Look for Microfocus COBOL, they specialize in that domain.


Cheers,
L.W.
```

#### ↳ Re: COBOL emulators

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-09-07T17:32:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I3zho.128109$Bh.66425@en-nntp-12.dc1.easynews.com>`
- **References:** `<70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com>`

```
"RealInfo" <therightinfo@gmail.com> wrote in message 
news:70f04476-247e-4b83-ab4c-9ac0280dbdb1@l20g2000yqe.googlegroups.com...
> Hi all
> Is it possible to develop COBOL based applications on PC so that they
…[10 more quoted lines elided]…
>
Assuming you are aiming for IBM z/OS (those are the people who most often 
think "mainframe" is enough to say),

There are 3 (maybe 4) main vendors that provide full IBM mainframe 
development systems

 - IBM (see the RDz product)
 - Micro Focus (look for the Mainframe Express products)
 - Fujitsu (now Alchemy)
 - CA (I don't know if they are continuing develoment on their Realia 
products or not)

All of these products are VERY expensive for the "average" developer. 
However, they include JCL emulators, CICS, IMS, and DB2 options, Often 
IDCAMS and other utilities, etc.  In other words, they are true "IBM 
mainframe emulator environments". Many of these vendors also target the 
"port from the IBM mainframe to Windows or Unix/Linux" development tasks. 
In some cases, it is this "porting away from the mainframe" approach that is 
the primary buisness direction of the company.

If you simply want to develop (write, compile, and debug) COBOL on a PC, 
there are several otehr options.  Most of the other options have "IBM 
compatibiiity" options for syntax (and run-time behavior).  Some (not all) 
have EBCDIC support.  These other options range from "free" to inexpensive. 
However, they don't provide a "real" IBM mainframe type environment and 
often (usually?) don't stay current with new features and facilities 
available to IBM mainframe programmers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
