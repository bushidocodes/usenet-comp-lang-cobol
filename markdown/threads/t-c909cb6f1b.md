[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convert or Port ?

_10 messages · 7 participants · 1999-10_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Convert or Port ?

- **From:** "van Daal, Peter" <Peter.vanDaal@nl.origin-it.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com>`

```
We have a COBOL program, doing communication with the mainframe, that need
also to run on Windows and Unix.
We could :
1) Convert the programs to C or 2) port the cobol programs.
With 1) we need a convert cobol to c package, with 2) we need a strong cobol
compiler (supporting vsam files etc..).

Any suggestions ?

Peter
```

#### ↳ Re: Convert or Port ?

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u21ga$lja$1@nnrp1.deja.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com>`

```
In article
<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-
it.com>,
  "van Daal, Peter" <Peter.vanDaal@nl.origin-it.com> wrote:
> We have a COBOL program, doing communication with the mainframe, that
need
> also to run on Windows and Unix.
> We could :
> 1) Convert the programs to C or 2) port the cobol programs.
> With 1) we need a convert cobol to c package, with 2) we need a
strong cobol
> compiler (supporting vsam files etc..).
>
> Any suggestions ?
>

Try CA-Realia Workbench 3.0. It's extremely good for mainframe and
Windows development.
> Peter
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Convert or Port ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u23hf$8a4$1@nntp2.atl.mindspring.net>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com>`

```
It probably isn't the only solution but going with IBM VisualAge COBOL
(Windows) and IBM COBOLSet (I think that's its current name) and IBM CICS
(MVS, AIX, and Windows) all of which support IBM VSAM would sound the
"simplest" for your particular needs.
```

##### ↳ ↳ Re: Convert or Port ?

- **From:** "van Daal, Peter" <Peter.vanDaal@nl.origin-it.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net>`

```
I need to port a communication program (now running on mvs) to PC.
The application connects to a CICS system using the OS390 tcp/ip Socket
Interface (ezasoket).
Can that be done (tcp/ip socket connection to cics) with IBM VisualAge cobol
?
Thanks for your reply.

Peter

William M. Klein wrote in message <7u23hf$8a4$1@nntp2.atl.mindspring.net>...
>It probably isn't the only solution but going with IBM VisualAge COBOL
>(Windows) and IBM COBOLSet (I think that's its current name) and IBM CICS
…[7 more quoted lines elided]…
>news:0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-i
t.
>com...
>> We have a COBOL program, doing communication with the mainframe, that
need
>> also to run on Windows and Unix.
>> We could :
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Convert or Port ?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3805ceb5.26274616@news1.attglobal.net>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net> <0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com>`

```
On Thu, 14 Oct 1999 14:05:17 +0200, "van Daal, Peter"
<Peter.vanDaal@nl.origin-it.com> wrote:

>I need to port a communication program (now running on mvs) to PC.
>The application connects to a CICS system using the OS390 tcp/ip Socket
…[3 more quoted lines elided]…
>Thanks for your reply.

From what I have *heard* the VisualAge COBOL does not support the EZA
calls, but you can make the interface making direct calls to the
Windows API - you can go to my site for some examples (In the download
section - sockets.zip) that are geared toward MicroFocus and Fujitsu,
but I think they are sufficiently clear to get you started with VA
COBOL calling the API.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Convert or Port ?

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u5s2j$q26$1@news.igs.net>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net> <0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com> <3805ceb5.26274616@news1.attglobal.net>`

```
You can also get quite cheap RS-232 driver libraries(as DLL's).  I purchased
on from MarshalSoft, and the RS-232C part was quite painless.

Thane Hubbell wrote in message <3805ceb5.26274616@news1.attglobal.net>...
>On Thu, 14 Oct 1999 14:05:17 +0200, "van Daal, Peter"
><Peter.vanDaal@nl.origin-it.com> wrote:
…[4 more quoted lines elided]…
>>Can that be done (tcp/ip socket connection to cics) with IBM VisualAge
cobol
>>?
>>Thanks for your reply.
…[9 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Convert or Port ?

_(reply depth: 4)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nCnN3.278$P6.13695@news2.rdc1.on.home.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net> <0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com> <3805ceb5.26274616@news1.attglobal.net>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:3805ceb5.26274616@news1.attglobal.net...
> On Thu, 14 Oct 1999 14:05:17 +0200, "van Daal, Peter"
> <Peter.vanDaal@nl.origin-it.com> wrote:
…[4 more quoted lines elided]…
> >Can that be done (tcp/ip socket connection to cics) with IBM VisualAge
cobol
> >?
> >Thanks for your reply.
…[9 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/

... and if you want to minimize the changes to your source code you can
write a EZASOKET subroutine API that maps the EZASOKET calls to windows
socket calls.
```

###### ↳ ↳ ↳ Re: Convert or Port ?

_(reply depth: 5)_

- **From:** "van Daal, Peter" <Peter.vanDaal@nl.origin-it.com>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0E16861EE7BCD111BE9400805FE6841F0BFE41D2@c1s5x001.cor.srvfarm.origin-it.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net> <0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com> <3805ceb5.26274616@news1.attglobal.net> <nCnN3.278$P6.13695@news2.rdc1.on.home.com>`

```
Oscar

To prevent inventing the wheel (Dutch saying) again :
is there a EZASOKET subroutine API that maps the EZASOKET calls to windows
socket calls somewhere ????.
Thanks,
Peter


Oscar T. Grouch wrote in message ...
>
>Thane Hubbell <thaneH@softwaresimple.com> wrote in message
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Convert or Port ?

_(reply depth: 6)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7NvP3.2478$Ua7.53318@news2.rdc1.on.home.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com> <7u23hf$8a4$1@nntp2.atl.mindspring.net> <0E16861EE7BCD111BE9400805FE6841F0BE9B159@c1s5x001.cor.srvfarm.origin-it.com> <3805ceb5.26274616@news1.attglobal.net> <nCnN3.278$P6.13695@news2.rdc1.on.home.com> <0E16861EE7BCD111BE9400805FE6841F0BFE41D2@c1s5x001.cor.srvfarm.origin-it.com>`

```
Peter,

The company that I work for has an EZASOKET implementation for Micro Focus
CICS or Mainframe Express CICS option. It is a tiny part of a bigger
development suite and is not sold as a separate product so it may be less
expensive to write your own EZASOKET interface, especially if you are
comfortable with the WinSock API.  It depends on the value you place on your
time.

More information is available in a reply to your e-mail message. I try to
avoid using the newsgroup for advertising.

Karl

van Daal, Peter <Peter.vanDaal@nl.origin-it.com> wrote in message
news:0E16861EE7BCD111BE9400805FE6841F0BFE41D2@c1s5x001.cor.srvfarm.origin-it
.com...
> Oscar
>
…[15 more quoted lines elided]…
> >> >The application connects to a CICS system using the OS390 tcp/ip
Socket
> >> >Interface (ezasoket).
> >> >Can that be done (tcp/ip socket connection to cics) with IBM VisualAge
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Convert or Port ?

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 1999-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3813801a.4996472@nntp.ix.netcom.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0BE30108@c1s5x001.cor.srvfarm.origin-it.com>`

```
On Wed, 13 Oct 1999 09:19:57 +0200, "van Daal, Peter"
<Peter.vanDaal@nl.origin-it.com> wrote:

>We have a COBOL program, doing communication with the mainframe, that need
>also to run on Windows and Unix.
…[3 more quoted lines elided]…
>compiler (supporting vsam files etc..).

>Any suggestions ?

definitely choice 2. aside from the fact that there are no good cobol
to c converters, if you change to c code, you throw out your
programmers onto the street, AND you have to write in c code from now
on. c is generally a more expensive market, and harder to program in,
and outside of device drivers, compilers and games, you don't want it.


newsreader is lagged. to reply via email send
to gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
