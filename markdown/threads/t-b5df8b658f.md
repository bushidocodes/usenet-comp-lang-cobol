[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Abend handling using Language Environment

_4 messages · 4 participants · 1998-12 → 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Abend handling using Language Environment

- **From:** georgelnj@my-dejanews.com
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,comp.programming,comp.protocols.ibm
- **Message-ID:** `<76gnvd$ahp$1@nnrp1.dejanews.com>`

```


How are ABENDS handled differently while running under Language
Environment (LE) ?

Any experiences and/or examples would be appreciated

George Lewycky
NY City Transit Authority

lewycky@idt.net

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Abend handling using Language Environment

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,comp.programming,comp.protocols.ibm
- **Message-ID:** `<76gu3r$c79@dfw-ixnews10.ix.netcom.com>`
- **References:** `<76gnvd$ahp$1@nnrp1.dejanews.com>`

```

georgelnj@my-dejanews.com wrote in message
<76gnvd$ahp$1@nnrp1.dejanews.com>...
>
>
>How are ABENDS handled differently while running under Language
>Environment (LE) ?

The easy answer is "VERY differently".
  I will work on getting you a more helpful answer - but this is a HUGE
question and is one of the major issues related to LE migrations.  (Have you
read the LE Migration Guide from IBM yet?  That would certainly be the first
place to start.)

>
>Any experiences and/or examples would be appreciated
…[7 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Abend handling using Language Environment

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,comp.programming,comp.protocols.ibm
- **Message-ID:** `<368c38d1.249537471@news1.ibm.net>`
- **References:** `<76gnvd$ahp$1@nnrp1.dejanews.com> <76gu3r$c79@dfw-ixnews10.ix.netcom.com>`

```
On Thu, 31 Dec 1998 16:34:34 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>
>georgelnj@my-dejanews.com wrote in message
…[10 more quoted lines elided]…
>place to start.)


It's interesting.  I have programmed on mainframes, minis and PC's.
On the PC we used the lastest and greatest from Realia and MicroFocus.


But our mainframes were antique.  We used COBOL/VS.  So I got used to
how abends worked under that - under VSE.   When I changed jobs I went
straight to LE.  I am sure Dwight remembers my asking, when a job blew
up, "Where's my dump?".  Anyway, I've come around to the LE way of
doing things. 

When it is truly an application problem the abend is within the
address range of your verb list.  I have seen abends outside that
address range however - and in every case it has been a "setup"
problem.  A problem with the data definitions matching etc.  The
Reason codes are very accurate and explicit in LE.
```

#### ↳ Re: Abend handling using Language Environment

- **From:** Inga Campbell <ingac@ibm.net>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol,comp.programming,comp.protocols.ibm
- **Message-ID:** `<368C0BF2.45BB@ibm.net>`
- **References:** `<76gnvd$ahp$1@nnrp1.dejanews.com>`

```
georgelnj@my-dejanews.com wrote:
> 
> How are ABENDS handled differently while running under Language
…[10 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own

Our shop decided to upgrade to LE for language support while upgrading
to OS/390.  This decision has led to experiences  requiring a lot of
"catch up".  The majority of programs, both on line and batch, are
running with LE and not creating any problems.  Others, such a COBOL
programs called as subroutines by Assembler callers, can cause BIG
headaches.  LE has also been poorly supported by some third party
product vendors, though several have by now upgraded to make their tools
"LE Conforming".

Be sure to look into LE run time option settings for your most important
language (I haven't determined whether the settings recommended for the
various supported languages are 100% compatible).  Also, read about
ABPERC and the method for specifying that certain abend codes should be
"percolated" (not handled by LE).  We use an abend routine which
produces a U=999 abend, with or without a dump.  LE intercepts it and
always dumps!  The additional output (messages on SYSOUT and CEEDUMP
output) need to be handled, too.

I have studied the LE Migration Guide, read the entire COBOL for MVS &
VM Migration Guide, and also had to get into parts of the guides for
FORTRAN and PL/1.

It is my plan to attend SHARE in San Francisco on February 21 - 26,
where about 28 sessions dealing with LE are scheduled.  I would
recommend this as a good place to get knowledge and contacts, who may be
able to help you avoid a lot of pain.

Depending on your shop's mix of new and old COBOL compilers (and those
for other languages), LE could be simple or really, really, tough.

Lots of work and, to me, FUN!
Colin Campbell
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
