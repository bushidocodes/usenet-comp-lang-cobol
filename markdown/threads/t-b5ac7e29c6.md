[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (IBM) LE for z/OS V1R7

_6 messages · 4 participants · 2005-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### (IBM) LE for z/OS V1R7

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-28T19:56:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com>`

```
Just in case anyone (who cares) in this newsgroup missed it,  IBM did come out 
with their "availability" announcement (Sept 30) for LE for z/OS V1R7.  See:

 http://www.ibm.com/isource/cgi-bin/goto?it=usa_annred&on=205-167

Of POSSIBLE (I hope not) interest to some in the COBOL world is the (long 
announced) total removal of "ISAM" support.  For those NOT familiar with IBM 
terminology, this does not mean removal of support for COBOL
   "organization is indexed"
files, but for an older access method that was used for this.   Current support 
is available via VSAM KSDS.

What I haven't been able to figure out (yet) is what happens to OS/VS COBOL 
programs that used "true" ISAM if

 A) compiled with NORES and link-edited with earlier run-times and run in an LE 
1.7 environment
B) compiled with RES and run under LE 1.7

I assume they will "die" - but I don't know whether this will be a 
"user-friendly" OS/VS COBOL specific ABEND or some type of "generic" z/OS ABEND. 
I assume we will hear "sooner than later".  Hopefully,

  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg30/4.1.4.1.1

which says

"Manual conversion actions: If the design of your application makes it 
impossible to convert to VSAM, you can restructure the application to separate 
the ISAM statements into an I/O program that can be compiled by the OS/VS COBOL 
compiler. You can then separate the rest of the application logic into programs 
that can be upgraded to Enterprise COBOL.

You can then run your application consisting of both OS/VS COBOL programs and 
Enterprise COBOL programs under Language Environment."

will be updated in a "timely" manner (after - or even better before - Sep 30, 
2005).
```

#### ↳ Re: (IBM) LE for z/OS V1R7

- **From:** "Ron" <NoSpam@SpamSucks.Org>
- **Date:** 2005-07-28T17:14:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hKednZEbo9QuxXTfRVn_vA@giganews.com>`
- **References:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com>`

```
Any shop still using native ISAM deserves whatever
happens to them.
```

##### ↳ ↳ Re: (IBM) LE for z/OS V1R7

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-07-28T23:09:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CAdGe.663419$pI6.295170@fe06.news.easynews.com>`
- **References:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com> <hKednZEbo9QuxXTfRVn_vA@giganews.com>`

```
And, what's more, the chances of them staying current on hardware (z9's) or 
software (LE V1R7) is minimal.

But I did think I would point it out any way.
```

#### ↳ Re: (IBM) LE for z/OS V1R7

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-07-29T15:45:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcdiuc$ri2$1@theodyn.ncf.ca>`
- **References:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com>`

```

"William M. Klein" (wmklein@nospam.netcom.com) writes:
> 
> Of POSSIBLE (I hope not) interest to some in the COBOL world is the (long 
> announced) total removal of "ISAM" support.  For those NOT familiar with IBM 

I haven't seen or used ISAM since VS2. 
 
I wonder if the reason people are still using it could be that they don't
have program source to modify and have just been relinking it with the LE
etc. migration INCLUDE/REPLACE jobs provided by IBM.
```

##### ↳ ↳ Re: (IBM) LE for z/OS V1R7

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2005-07-29T18:07:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20050729.18072809@rechner12.lerch.xl>`
- **References:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com> <dcdiuc$ri2$1@theodyn.ncf.ca>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 29.07.05, 15:45:16, schrieb bo774@FreeNet.Carleton.CA (Kelly Bert 
Manning) zum Thema Re: (IBM) LE for z/OS V1R7:


> "William M. Klein" (wmklein@nospam.netcom.com) writes:
> >
> > Of POSSIBLE (I hope not) interest to some in the COBOL world is the 
(long
> > announced) total removal of "ISAM" support.  For those NOT familiar 
with IBM

> I haven't seen or used ISAM since VS2.

> I wonder if the reason people are still using it could be that they 
don't
> have program source to modify and have just been relinking it with the 
LE
> etc. migration INCLUDE/REPLACE jobs provided by IBM.

I am sorry, but several people does not migrate from COBOL/VS to 
COBOL/II. My oldest compile is 1995, last century, because 
megaproject. If this project does not apear. we have code and compile 
back to 1985, that's nearly 20 years. WICH MIKISOFT could say, to be 
compatible to 1980th. I like IBM, because they do there job: to be 
compatible.......

Thats live and cost not more than a grine.

Einen schoenen Tag
)sorry about my bad englich(
Andreas Lerch
```

###### ↳ ↳ ↳ Re: (IBM) LE for z/OS V1R7

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-07-29T18:01:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcdqt5$2et$1@theodyn.ncf.ca>`
- **References:** `<HLaGe.658394$ub.65517@fe07.news.easynews.com> <dcdiuc$ri2$1@theodyn.ncf.ca> <20050729.18072809@rechner12.lerch.xl>`

```

Andreas Lerch (andreas@andreas-lerch.de) writes:
> 
> I am sorry, but several people does not migrate from COBOL/VS to=20
…[12 more quoted lines elided]…
> Andreas Lerch

A date editing and transformation routine I coded in 1977 for a "no extra
cost" pre-ANS cobol compiler on VS2 is still in use. It even handled 
century years correctly, without needing any coding changes. IBM COBOL
can be very stable, across decades of changes in the hardware and software
environment, as you say. It was recompiled with LE COBOL for Y2K.
  
As a minimum I think most people would want to get 24 bit addressing
constraint relief. VS COBOL object code has to run below the line, let
alone below the bar, doesn't it?

(flash back to a 1990 meeting with MSA/DBS local vendor staff where we
 discussed an impending processor upgrade. 
 MSA "guru": Hey, could you guys maybe get some more memory to help 
     avoid those "Short On Storage" situations we keep getting?
 me: You are using 24 bit versions of CICS and COBOL. Our staff who have
     been to GUIDE and SHARE tell us that IBM has desperately trying to
     contact MSA/DBS to give you direction on migrating to 31 bit versions
     of CICS and COBOL. You can't use any more memory below the line.
 MSA "guru" to someone at a hosted reception later:
     What was that 24 bit and 31 bit stuff Kelly was talking about?
)   

Having to sort out a difference in what code a compiler accepts is something
I'd rather learn about early on, not when a program fails and has to be 
recompiled. I've seen IMS DBD or PSB source fail to assemble when
IBM supplied "minor maintenance" to LE. I'd rather have managment tell
me that something isn't important to them than to have to explain that
I knew of a risk and did not think it was worth doing a risk evaluation
review with them. The code can always be fixed, but as downtime becomes
more expensive the cost of delays rises.
 
IBM's ability to integrate new software applications, such as UNIX, on the
same processor that legacy code runs on is just as important as their 
backwards compatibility, in my opinion.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
