[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

_6 messages · 4 participants · 1999-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** renfrew@erols.com (Dave Miner)
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ni6kd$qpb$1@autumn.news.rcn.net>`

```
Environment: Novell Netware 4.11 server, with WIN98 client.  Micro-Focus COBOL 3.4.
 
I am trying to run a rather large program in Animator mode, but when I try to "zoom" the 
execution to a specific event it keeps stopping at EARLIER events.  It apparently thinks that 
these earlier events are breakpoints because it says "program breakpoint" at the bottom of the 
animator screen.  But these are NOT breakpoints!?!  To make sure, I even tried to unset a 
breakpoint at these places, but it then confirms that there is no breakpoint to unset.  

I know that the first tree one should bark up when having Animator problems is to look for an 
old/obsoleted AIF file, but I have already done this.  Any suggestions?  

1KTIA, 
DaveM
```

#### ↳ Re: Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379d3b3f.261008887@news1.ibm.net>`
- **References:** `<7ni6kd$qpb$1@autumn.news.rcn.net>`

```
On 26 Jul 1999 17:41:33 GMT, renfrew@erols.com (Dave Miner) wrote:

>Environment: Novell Netware 4.11 server, with WIN98 client.  Micro-Focus COBOL 3.4.
> 
…[7 more quoted lines elided]…
>old/obsoleted AIF file, but I have already done this.  Any suggestions?  

Windows will "FIND" an old AIF file if it is in your PATH.  Something
interesting about Windows few people know, but many have been bit by.
Try writing a program.  Don't EXPLICITLY specify a path for the file,
just assign it to "INPUT.FIL" - then put that file somewhere in your
path, different from your current directory and run the program.  WALA
- windows finds the file.  Very bad.  Anyway, scour your hard drive
for old AIF files and make sure the ONLY think on your system for this
program ANYWHERE is the source - recompile then try animating.

Still have a problem, when the first break hits perform the "unset all
break points" function, then reset your break and continue.
```

##### ↳ ↳ Re: Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379D4981.DD54580F@home.com>`
- **References:** `<7ni6kd$qpb$1@autumn.news.rcn.net> <379d3b3f.261008887@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On 26 Jul 1999 17:41:33 GMT, renfrew@erols.com (Dave Miner) wrote:
…[3 more quoted lines elided]…
> >I am trying to run a rather large program in Animator mode, but when I try to "zoom" ......

Thane wrote :

> Windows will "FIND" an old AIF file if it is in your PATH.  Something
> interesting about Windows few people know, ........

**##@**##!!! Can't remember - How did Michael Mattias delicately phrase
it when referring to Mr. Microsoft's family lineage ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57in3.72$bm.3139@dfiatx1-snr1.gtei.net>`
- **References:** `<7ni6kd$qpb$1@autumn.news.rcn.net> <379d3b3f.261008887@news1.ibm.net>`

```
WALA?  WALA?!!!

SACK REBLUE!

MCM

Thane Hubbell wrote in message <379d3b3f.261008887@news1.ibm.net>...
>just assign it to "INPUT.FIL" - then put that file somewhere in your
>path, different from your current directory and run the program.  WALA
>- windows finds the file...
```

##### ↳ ↳ Re: Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57in3.73$bm.3139@dfiatx1-snr1.gtei.net>`
- **References:** `<7ni6kd$qpb$1@autumn.news.rcn.net> <379d3b3f.261008887@news1.ibm.net>`

```
Thane Hubbell wrote in message <379d3b3f.261008887@news1.ibm.net>...
>Windows will "FIND" an old AIF file if it is in your PATH....

Windows' path search I don't mind. MVS' STEPLIB and JOBLIB I don't mind. But
the one that scares me is the LIBLIST on the AS/400, where programs find
datafiles based on some search path.

I'm sure this is terrific for testing/developing, but as a non-400-guy,
every time I work with one I am deathly afraid that someone has changed the
LIBLIST (which I don't know how to check) and I am about to screw up the
production datasets.

MCM
```

###### ↳ ↳ ↳ Re: Ghost breakpoints in ANIMATOR (MF COBOL 3.4)

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379e8dcf.347694347@news1.ibm.net>`
- **References:** `<7ni6kd$qpb$1@autumn.news.rcn.net> <379d3b3f.261008887@news1.ibm.net> <57in3.73$bm.3139@dfiatx1-snr1.gtei.net>`

```
What scares me is the logicals on the VMS system.  


On Tue, 27 Jul 1999 13:04:01 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Thane Hubbell wrote in message <379d3b3f.261008887@news1.ibm.net>...
>>Windows will "FIND" an old AIF file if it is in your PATH....
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
