[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IMS Questions

_11 messages · 7 participants · 2002-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IMS Questions

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-01-21T17:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4C4CFB.77D4177F@boeing.com>`

```
I find that suddenly I need to interface with an IMS database - this is
one I managed to avoid for years - 

Any excellent references for getting up to speed?

I want to build a COBOL routine that extracts the required information
from the IMS tables and insert it into a DB2 table.  Once tested I want
to turn this into a Web based user request.

I understand that I am mixing Hierarchical and relational data (and
reading segments)

My system is OS 390 ((2.6) with DB2 V5)

	Thanks
		Susan A
	(staying humble with old applications)
```

#### ↳ Re: IMS Questions

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-01-21T13:12:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sNY28.1994$JM6.946794@news20.bellglobal.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
"Susan A Allen" <susan.a.allen@boeing.com> wrote in message
news:3C4C4CFB.77D4177F@boeing.com...
> I find that suddenly I need to interface with an IMS database - this is
> one I managed to avoid for years -
…[14 more quoted lines elided]…
> (staying humble with old applications)

That is CURRENT with old applications Susan not humble.

Donald  ;<)
```

##### ↳ ↳ Re: IMS Questions

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-01-21T20:20:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4C7822.788D0863@boeing.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com> <sNY28.1994$JM6.946794@news20.bellglobal.com>`

```


Donald Tees wrote:
> > My system is OS 390 ((2.6) with DB2 V5)
> >
…[5 more quoted lines elided]…
> 

The code I am deconstructing would keep anyone humble.

COBOL Unleashed had a nice chapter on the topic IMDB; still I think I
want to do what no one else thought about (Which would be a stored
procedure in an ideal world).

	Susan A
```

###### ↳ ↳ ↳ Re: IMS Questions

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-01-21T15:43:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14%28.2239$JM6.1001514@news20.bellglobal.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com> <sNY28.1994$JM6.946794@news20.bellglobal.com> <3C4C7822.788D0863@boeing.com>`

```
hehe.  I have some of that code myself.  The really humbling part is that I
wrote it myself about twenty, twenty-five years back.  The nasty part is
that it was not that bad, when I wrote it.  All these years of hacking it up
have degenerated it, though.  Now I am a bit afraid to try a complete
re-write, as the stuff actually works quite well.  It is just ugly, ugly
ugly.

Donald

"Susan A Allen" <susan.a.allen@boeing.com> wrote in message
news:3C4C7822.788D0863@boeing.com...
>
>
…[16 more quoted lines elided]…
> Susan A
```

#### ↳ Re: IMS Questions

- **From:** Steve Thompson <sthompsonNOSPAM@ix.netcom.com>
- **Date:** 2002-01-21T16:53:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4C8DC5.BB4E69EC@ix.netcom.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
Susan A Allen wrote:
> 
> I find that suddenly I need to interface with an IMS database - this is
> one I managed to avoid for years -
> 
> Any excellent references for getting up to speed?
<snip>        

I have an old book that I still reference, "IMS Programming
Techniques, A Guide to Using DL/I"
by Dan Kapp & Joseph F. Leben, Van Nostrand Reinhold Co.  

The "IMS Programming Techniques" explains several things
about IMS and what you are attempting to do within your
COBOL program and how it communicates with IMS.  Then, once
you get the data you are after, it is up to you to get it
correctly formatted to write to the DB/2 table.
```

##### ↳ ↳ Re: IMS Questions

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-01-22T01:04:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4CBA8D.35586B6E@boeing.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com> <3C4C8DC5.BB4E69EC@ix.netcom.com>`

```


Steve Thompson wrote:
> 
> Susan A Allen wrote:
…[16 more quoted lines elided]…
> 

Thanks! -- located one at a bargain price at half.com

old tech books never die

	Susan A
```

#### ↳ Re: IMS Questions

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-01-22T04:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1a2f9$b9f3bec0$0431e641@chottel>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
Mick Murach has two books on IMS for the Cobol Programmer

http://www.murach.com/books/mainframe.htm

Susan A Allen <susan.a.allen@boeing.com> wrote in article
<3C4C4CFB.77D4177F@boeing.com>...
> I find that suddenly I need to interface with an IMS database - this is
> one I managed to avoid for years - 
…[15 more quoted lines elided]…
>
```

#### ↳ Re: IMS Questions

- **From:** LSoens@t-online.de (Lothar Soens)
- **Date:** 2002-01-23T19:58:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<INZNCBOtXuBC-pn2-8WuKiRKsuw9u@lsoens.dialin.t-online.de>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
speed? Don't know <g>

You might consider to search in IBM's online books for the keywords: 
IMS, CBLTDLI, DBD, PSP, segment, SSA , ...

Good luck

Regards 
Lothar


On Mon, 21 Jan 2002 17:16:43, Susan A Allen <susan.a.allen@boeing.com>
wrote:

> I find that suddenly I need to interface with an IMS database - this is
> one I managed to avoid for years - 
…[14 more quoted lines elided]…
> 	(staying humble with old applications)

___
Flying Warp4.51 & Fp1 from DUS (Germany)
```

#### ↳ Re: IMS Questions

- **From:** Mark Allen Framness <farmer@netnet.net>
- **Date:** 2002-01-23T21:49:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02012321554600.03455@framnett>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
On Mon, 21 Jan 2002, Susan A Allen wrote:
>I find that suddenly I need to interface with an IMS database - this is
>one I managed to avoid for years - 

I went to our company's boot camp they spent a week teaching IMS batch
programming and told us we would never use it.  Both of my mainframe gigs had
extensive use of both IMS batch and IMS online (the last one was all IMS online
for myself).

Anyway the book I use is IMS for the COBOL Programmer by Steve Eckols.  There
are two books one for batch and another for online, however it sounds like you
will not be working in the online environment at all.  I guess there are better
ones, I am not extremely impressed with this book but it is okay.




>
>Any excellent references for getting up to speed?
…[3 more quoted lines elided]…
>to turn this into a Web based user request.

How much business rule filtering does it have to pass through?  Or is the data
just going to be exported from from IMS to DB2 straight away?  One would almost
think that FILE AIDS-IMS could extract the IMS data to a sequential dataset
(SDS) for you and then just write a batch to read that SDS, format the records
and insert to DB2.

Anyway good luck!
```

##### ↳ ↳ Re: IMS Questions

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-01-25T23:43:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C51EDAB.E3ADC5E3@boeing.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com> <02012321554600.03455@framnett>`

```


Mark Allen Framness wrote:
> 
> On Mon, 21 Jan 2002, Susan A Allen wrote:
> >I find that suddenly I need to interface with an IMS database 

> 
> Anyway the book I use is IMS for the COBOL Programmer by Steve Eckols.  There
…[3 more quoted lines elided]…
> 

	Thanks!
```

#### ↳ Re: IMS Questions

- **From:** someone@euronet.nl (Marc)
- **Date:** 2002-01-28T00:48:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b6a38ea.0201280048.135df46d@posting.google.com>`
- **References:** `<3C4C4CFB.77D4177F@boeing.com>`

```
Susan A Allen <susan.a.allen@boeing.com> wrote in message > 
> I want to build a COBOL routine that extracts the required information
> from the IMS tables and insert it into a DB2 table.  Once tested I want
…[3 more quoted lines elided]…
> reading segments)

Hello Susan,

If you want to use IMS, you must have knowlegde of Program
Specification Blocks e.d. It's not easy for someone with a relational
mind!

I suggest: 

An IMS database is nothing more than a sequential file. You can read
it, sort it, etc.

So, define the IMS tables you need, ask for a copys of those tables(or
make a copy yourself) to be sure nothing can go wrong!.

Sort the files in such an order, Jackson would be delighted. Than make
one, or several cobol programs to read (balance-line) an insert the
records in your DB2 table.

Greetings,

M.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
