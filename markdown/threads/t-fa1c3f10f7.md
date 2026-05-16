[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Request for assistance running 2 programs n IBM zOS

_4 messages · 3 participants · 2012-09 → 2012-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Request for assistance running 2 programs n IBM zOS

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2012-09-19T10:14:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com>`

```
I have two programs that I would like to know the results when run with 
Enterprise COBOL on IBM z/OS.  I have put them on the web, so I *think* that 
they can be downloaded and run without any "conversion" problems.  (You may 
need to change the underscores in the program with them in the program-id 
paragrah, depending on what you use for the PGMNAME compilre option). If you 
can't download, compile, and run  them easily, please let me know what 
problems you have.   If there are compiler errors (because I haven't 
compiled them on the mainframe, let me know that too).  They are at:

http://home.comcast.net/~wmklein/OC/FP2.cbl

and

http://home.comcast.net/~wmklein/OC/IF_ALL_4.CBL

P.S.  these use intrinsic functions, so don't try and run them with "older" 
IBM compilers like OS/VS COBOL.
```

#### ↳ Re: Request for assistance running 2 programs n IBM zOS

- **From:** Kerry Liles <kerry.liles@gmail.com>
- **Date:** 2012-09-19T14:34:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k3d38k$r11$1@dont-email.me>`
- **In-Reply-To:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com>`
- **References:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com>`

```
On 9/19/2012 12:14 PM, Bill Klein wrote:
> I have two programs that I would like to know the results when run with
> Enterprise COBOL on IBM z/OS.  I have put them on the web, so I *think* that
…[16 more quoted lines elided]…
>

I have compiled both (with some minor tweaks as noted) and sent the 
results to what I believe is your un-munged email address...

regards,

Kerry Liles
```

##### ↳ ↳ Re: Request for assistance running 2 programs n IBM zOS

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2012-09-19T12:56:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dzo6s.476915$zA2.449629@en-nntp-03.dc1.easynews.com>`
- **References:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com> <k3d38k$r11$1@dont-email.me>`

```
Sorry to anyone esle who treis the program with
   FUNCITON PI

I forgot that this came inwith the '02 Stnadard and that IBM Enterprise 
COBOL doesn't support it.

"Kerry Liles" <kerry.liles@gmail.com> wrote in message 
news:k3d38k$r11$1@dont-email.me...
> On 9/19/2012 12:14 PM, Bill Klein wrote:
>> I have two programs that I would like to know the results when run with
…[29 more quoted lines elided]…
>
```

#### ↳ Re: Request for assistance running 2 programs n IBM zOS

- **From:** Pavel <p.pleva@sh.cvut.cz>
- **Date:** 2012-10-11T11:06:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k5628v$2rns$1@ns.felk.cvut.cz>`
- **In-Reply-To:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com>`
- **References:** `<Wbm6s.701940$Xo4.335532@en-nntp-13.dc1.easynews.com>`

```
> http://home.comcast.net/~wmklein/OC/FP2.cbl

  000006                    05  NUM1     PIC S9(4)V9(5)  VALUE +12.34E+2.
==000006==> IGYGR1080-S A "VALUE" clause literal was not compatible with the data category of the
subject data item.  The "VALUE" clause was discarded.

> http://home.comcast.net/~wmklein/OC/IF_ALL_4.CBL

  000015                    COMPUTE NUM-PI = FUNCTION PI
==000015==> IGYPS2130-S Expected a function-name, but found "PI".  The "COMPUTE" statement was
discarded.

> P.S.  these use intrinsic functions, so don't try and run them with "older" 
> IBM compilers like OS/VS COBOL. 

IBM Enterprise COBOL for z/OS  4.1.0


Regards

Pavel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
