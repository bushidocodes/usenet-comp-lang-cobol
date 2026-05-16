[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem in MicroFocus Dialog System (GUI)

_3 messages · 3 participants · 2000-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Problem in MicroFocus Dialog System (GUI)

- **From:** "Awais Baig" <awais22@khi.comsats.net.pk>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hdnh5$119a$1@news.interpacket.net>`

```
Please help me if someone knows the solution of this
problem.

I want to execute my application in differet
windows 95 sessions silutaniously more than one
time from the same folder and same data folder.

I created an Icon on my desktop to execute this
appilication. After one time successfully execution
when I again open that application from that Icon
while previous one is already open, the system
is not opening another sessions, it just show me the
previous screen. Its mean that user is now restricted
with only one microfocus runtime product in one time.

But in character based (Dos or Unix based) Microfocus
runtime product I was able to execute my application on the
same machine simultaniously as many time as my system
memory support. I think this problem is due to using
Dialog System (GUI). Other wise charecter base works
very well. Other windows applications like MS Word can
be opened in many sessions (in one time we can open lot
of MS Words).  Please help me if someone knows the
solution of this problem.

I am using following Product of Microfocus.

Compiler :
Micro Focus COBOL
Version 3.2.46

RUN TIME ENVIRONMENT :
Micro Focus COBOL Toolset Version 3.2.46

Dialog System - V2.5.42
```

#### ↳ Re: Problem in MicroFocus Dialog System (GUI)

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hfmn0$268$1@hyperion.mfltd.co.uk>`
- **References:** `<8hdnh5$119a$1@news.interpacket.net>`

```
Awais,

I am afriad this is a restriction of 16 bit Windows EXEs.  I believe
they are LARGE MODEL and only one instance can be run.  This
restriction has been removed in 32 bit.

They are a couple of ways around this...

1) You can create multiple EXEs and assign a shortcut/icon to
each.  This is not very elegant but it does work with the built
environment.

2) Some OBJ modules called MFREUSED.OBJ and MFREUSEX.OBJ
are provided which can be linked in to EXE/DLLs.  These allow EXEs and
DLLs to be reused.

Hope this helps.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International


Awais Baig <awais22@khi.comsats.net.pk> wrote in message
news:8hdnh5$119a$1@news.interpacket.net...
> Please help me if someone knows the solution of this
> problem.
…[34 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Problem in MicroFocus Dialog System (GUI)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393C99BF.3F2C@Azonic.co.nz>`
- **References:** `<8hdnh5$119a$1@news.interpacket.net> <8hfmn0$268$1@hyperion.mfltd.co.uk>`

```
Paddy Coleman wrote:
> 
> I am afriad this is a restriction of 16 bit Windows EXEs.  I believe
…[16 more quoted lines elided]…
> > Version 3.2.46

See page 12-33 of the Cobol User Guide for MF 3.2.  Usinf the MF
supplied mfreusex.obj causes the program (.EXE) to be renamed when it
loads so that another copy can be loaded (and this takes another new
name).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
