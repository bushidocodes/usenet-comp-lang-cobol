[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Re Report Writer

_9 messages · 5 participants · 2002-04_

---

### Re Report Writer

- **From:** AlfredLanger@T-online.de (Alfred Langer)
- **Date:** 2002-04-23T07:24:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa2r5g$dca$04$1@news.t-online.com>`

```
When you make a report, what do you use.
```

#### ↳ Re: Re Report Writer

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-23T17:28:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC59936.1336214@shaw.ca>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com>`

```


Alfred Langer wrote:

> When you make a report, what do you use.

A printer ? <G>. Would you care to expand on what you are after to get a
more specific reply.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Re Report Writer

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-04-23T17:02:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fXjx8.10253$h02.1621552@news20.bellglobal.com>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3CC59936.1336214@shaw.ca...
>
>
…[8 more quoted lines elided]…
>

Hell, I'd never go that far if a verbal report would do.

Donald
```

###### ↳ ↳ ↳ Re: Re Report Writer

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-04-24T04:47:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mNqx8.47662$QC1.3361407@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca> <fXjx8.10253$h02.1621552@news20.bellglobal.com>`

```
    Have you ever thought about stone tablets?

"Donald Tees" <donald_tees@sympatico.ca> wrote in message
news:fXjx8.10253$h02.1621552@news20.bellglobal.com...
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3CC59936.1336214@shaw.ca...
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Re Report Writer

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-04-24T14:39:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa6fpu$nif$1@peabody.colorado.edu>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca> <fXjx8.10253$h02.1621552@news20.bellglobal.com>`

```

On 23-Apr-2002, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> > A printer ? <G>. Would you care to expand on what you are after to get a
> > more specific reply.
…[4 more quoted lines elided]…
> Hell, I'd never go that far if a verbal report would do.

I would expect that the printer would print a verbal report.  I suppose it
could print a picture instead.
```

##### ↳ ↳ Re: Re Report Writer

- **From:** AlfredLanger@t-online.de (Alfred Langer)
- **Date:** 2002-04-24T06:45:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cc65013.3998872@news.t-online.de>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca>`

```
On Tue, 23 Apr 2002 17:28:10 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

>
>
…[7 more quoted lines elided]…
>Jimmy, Calgary AB

I'm a bookkeeper and I often had to make complex reports. 

In this case I will replace an ACCESS Report because it's for my
co-workers to diffcult, or  they don't won't to do this, to do all the

steps which are necessary to get the report from Excel-datas.

The report looks like:

 
header:           bill of costs
 
detail header   Accounting

                       Josef                Wood     233,00
                       Alfred                Win        343,00

                                                              576,00

  
detail header  Shipping
  
                      Mary                Nail          345,00 
                      Sarah	     Dixon        243,00

                            	                      588,00



The report goes over 50 sites. I want the line after accounting. 
I think its only a real problem for my eyes. A further question is,
how can I get the detail header in bold.
```

###### ↳ ↳ ↳ Re: Re Report Writer

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-24T17:26:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC6EA43.A9F10A68@shaw.ca>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca> <3cc65013.3998872@news.t-online.de>`

```


Alfred Langer wrote:

> On Tue, 23 Apr 2002 17:28:10 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> wrote:
…[41 more quoted lines elided]…
> how can I get the detail header in bold.

Thanks for giving more specific information Alfred. Hmmm. As I read what you
wrote, my immediate reaction (and I don't use the product), was perhaps to
put it into Excel. But you are saying that's not viable. Perhaps somebody who
is familiar with Excel can make a suggestion.

I can see why you want to use R/W because of its automatic heading,
subtotaling capability. And given you are using Access as your DB, there is
absolutely no reason why you couldn't import the data into COBOL R/W. In a
Micro Focus context, having established your Table in MS Access, the MF  ESQL
Assistant generates a copyfile containing "cobol", host and null-variable
fields. Typically most of the "cobol" numeric fields are generated as pic
s9(14)v9(04), a few they put out as comp-3. So providing you are using the
"cobol" variables, they fit nicely into R/W as the "source" to format for
your print lines.

(Briefly - use an SQL query to obtain the data from the DB and pass it back
in "cobol" format to your program which contains R/W.)

Currently as to changing fonts or styles, (ironically, a topic I'm currently
discussing with a small group), you are screwed. It can't be done. The best
you could do is set your printer to "condensed", but you just don't have
control to modify the initial settings,as you switch from line to line.

Even given the above, a lot depends upon your programming capability. You say
you are a bookkeeper. Does that mean your prime role is accounting, and is
this reporting done on the side,  or are you a programmer who is an ex
bookkeeper ?
If you are not truly into programming, then the above is a big challenge.

I really hope somebody who knows Excel can give you some decent alternatives.
I'm aware Access can't do it for you, just giving you a very nice print-out,
but in row and column order. (It might just pay off if you get into a
Microsoft Newsgroup that discusses Excel - they may give you some decent
pointers).

A closing thought - can you yourself produce a decent report in Excel ? If
so, why not e-mail/fax/zipfile them a copy of the report you generated ? (Is
it one global report going to all 50 sites, or an individual report per site
?)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Re Report Writer

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-25T01:54:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC76133.E8F8A84B@shaw.ca>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com> <3CC59936.1336214@shaw.ca> <3cc65013.3998872@news.t-online.de>`

```
Alfred,

A follow-up to my previous message.

1 - If you *aren't* a programmer, why are you going through this hassle ?
This should be fairly easy for a programmer to do, but not the fonts/styles
within R/W.

2. Oops ! If you *are* a programmer, then I guess you can call this a
'learning experience' <G>. I just noted from an earlier message you are using
Fujitsu. You could take a look at SP2's printing module, (go to
www.flexus.com).

Real purpose of this message - assuming you are a non-programmer. Take a look
at MS Word. I've never done it, but you can import from Access and merge.
(Use MS Word help and the keywords "import" and "merge"). The most typical
example is mailing lists, but you can get quite sophisticated, setting
different fonts and styles, and similarly to Report Writer you can probably
set receiving fields in Word for the incoming data.

.Bit of a devious route, you might need to go Access to Excel to get
calculations and totaling, and then Excel to Word. Could be worth a try if
you are firmly stuck with the problem..

Jimmy, Calgary AB
```

#### ↳ Re: Re Report Writer

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-04-23T17:56:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aa46v0$cbp$1@peabody.colorado.edu>`
- **References:** `<aa2r5g$dca$04$1@news.t-online.com>`

```

On 22-Apr-2002, AlfredLanger@T-online.de (Alfred Langer) wrote:

> When you make a report, what do you use.

It depends on what I need.   My native language is CoBOL, so I don't have to
think about writing a report program in standard CoBOL.  With a bit of work,
I can make a simpler report using CoBOL report writer or EasyTrieve. 
Depending on what I need, I have even used DFSort, TSO Option 3.14, & Rexx.

Actually most written reports I make are just typed into a word processor. 
I use my vocal cords for oral reports.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
