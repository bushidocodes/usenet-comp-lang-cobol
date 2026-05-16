[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PIC syntax

_5 messages · 5 participants · 2000-01_

---

### PIC syntax

- **From:** mohrin@sharmahd.com (Torsten Mohrin)
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387edc28.5090079@news.aball.de>`

```
Dear collegues!

I need to convert some data files. I have a record declaration in
COBOL. It's some years ago since I wrote my last COBOL program, so I
can't remember some of PIC syntax (what's "V"? for example).

Is there an overview of the PIC syntax available online. I don't want
to buy a COBOL book.

Thank you very much.

Torsten
```

#### ↳ Re: PIC syntax

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85l0af$6qp$1@nnrp1.deja.com>`
- **References:** `<387edc28.5090079@news.aball.de>`

```
In article <387edc28.5090079@news.aball.de>,
  mohrin@sharmahd.com wrote:
> Dear collegues!
>
…[16 more quoted lines elided]…
>

Torsten,

You can download free the IBM COBOL Language Reference in PDF format
(readable with Adobe Acrobat) at:
http://www-4.ibm.com/software/ad/cobol/coblib.htm
BTW: the 'V' is the decimal place: '1234567' in a PIC 9(3)V9(4) has the
meaning of 123.4567.
```

#### ↳ Re: PIC syntax

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4nnf4.150$8z5.2131@news4.mia>`
- **References:** `<387edc28.5090079@news.aball.de>`

```
Well, 'V' means 'implied decimal point'.  It establishes where the
decimal point would be, but takes up no memory.

Right now on this newsgroup there is a thread on IBM OS/390 reference
books, all of which are available online.  You can check that out,
or you can go to www.adtools.com and download the documentation (and
compiler) for Fujitsu COBOL v3.
```

#### ↳ Re: PIC syntax

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-EtiOSfCY679C@localhost>`
- **References:** `<387edc28.5090079@news.aball.de>`

```
On Sun, 13 Jan 3900 14:15:20, mohrin@sharmahd.com (Torsten Mohrin) 
wrote:

> Is there an overview of the PIC syntax available online. I don't want
> to buy a COBOL book.
> 
> Thank you very much.
> 

Go to http://www.barnesandnoble.com and search for my book, Sams Teach
Yourself COBOL in 24 Hours.  The sample chapter that you can read 
there is Chapter 3 of my book which explains what you want to know.  I
would prefer that you buy the book, and maybe you will after reading 
the sample.  There are a few typos in it that are not in the printed 
book, but nothing that detracts from the information presented.

You can find the same sample chapter at the http://www.mcp.com site.

-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: PIC syntax

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Evwf4.1645$bQ1.31041@dfiatx1-snr1.gtei.net>`
- **References:** `<387edc28.5090079@news.aball.de>`

```
Go to http://www.flexus.com/softwaredownload.html and get file COBDATA.ZIP.
This is a text and graphics tutorial on COBOL datatypes. Note: this is *not*
a comprehensive guide to PICTURE clauses, which is part of what you are
asking about.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
