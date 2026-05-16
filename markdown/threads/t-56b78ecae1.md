[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# bar/pie charts on mainframe using COBOL?

_5 messages · 4 participants · 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### bar/pie charts on mainframe using COBOL?

- **From:** "Gary R Hamaker" <gary.r.hamaker@gte.net>
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<773mmb$6e1$1@news-1.news.gte.net>`

```
I help maintain a billing system written in COBOL. The output from our
process is an AFP file that is sent to a printer. Presently our graphics
capability is pretty limited. Does anyone have knowledge of how to output
bar and pie charts in an AFP file on a mainframe? I've read a little about
an IBM product called GDDM; could this be one way to achieve my goal?
Your advice is appreciated.
```

#### ↳ Re: bar/pie charts on mainframe using COBOL?

- **From:** "Gary Roush" <support@adtools.com>
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<77hlt1$7uc$1@remarQ.com>`
- **References:** `<773mmb$6e1$1@news-1.news.gte.net>`

```
Hi Gary,

You may want to look up Fujitsu COBOl as having the product to answer your
needs. Take a look at the website at:
http://www.adtools.com/

In version 4, when it is purchases includes the Crystal Reports program and
they now use version 6.0.  Makes for a very powerful report generator using
the data that could be transferred from the mainframe to PC. Something to
think about.

Regards,
Gary Roush
Fujitsu COBOL support


Gary R Hamaker wrote in message <773mmb$6e1$1@news-1.news.gte.net>...
>I help maintain a billing system written in COBOL. The output from our
>process is an AFP file that is sent to a printer. Presently our graphics
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: bar/pie charts on mainframe using COBOL?

- **From:** "Gary Roush" <support@adtools.com>
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<77ipu2$5lr$1@remarQ.com>`
- **References:** `<773mmb$6e1$1@news-1.news.gte.net> <77hlt1$7uc$1@remarQ.com>`

```
Gary,

I neglected to say in the last message about the GDDM product from IBM to
use on the mainframe. I used that product a long time ago. It works, but can
be a tedious project in setting up the program settings to get the pie-chart
you want. They may have upgraded the program since then so it's well worth
the look and seeing if it's worth the money to purchase it and use it. It
does use up a lot of CRU's or computer resources, but works.

When I was talking about Fujitsu COBOL and Crystal Reports in my previous
post, I was suggesting that the pie charts could be created on the PC by
downloading the data from the mainframe and running it through a COBOL
program that creates an ODBC database and then Crystal Reports could be used
to read that data and produce the pie charts or any type of report wanted.
Hope this is clearer and not an misunderstanding to the last post I wrote.

Gary

Gary Roush wrote in message <77hlt1$7uc$1@remarQ.com>...
>Hi Gary,
>
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ AFP/API newsgroup or help on AFPIOBJ

- **From:** joehoeller@my-dejanews.com
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<78k3ek$dmc$1@nnrp1.dejanews.com>`
- **References:** `<773mmb$6e1$1@news-1.news.gte.net> <77hlt1$7uc$1@remarQ.com> <77ipu2$5lr$1@remarQ.com>`

```
Hi,
maybe this is not the right newsgroup, so if somebody knows a newsgroup
for AFP/API it would be nice to tell me this newsgroup.

My Problem:
I am creating output files by using AFP/API.
I try to put an IOCA-image on a page by using AFPIOBJ. This call returns
no error but when ending this page he errorcode 255 (="a logic error in the
formatter code occured") is returned by AFPEPAG. Can anybody help ?

   Thanks in advance
Joachim Hoeller


-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: bar/pie charts on mainframe using COBOL?

- **From:** 100.162651@germanynet.de (Eckhard Prinz)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<369ee6fe.640425@news-ma.rhein-neckar.de>`
- **References:** `<773mmb$6e1$1@news-1.news.gte.net>`

```

Have a look for the ISIS-toolset at:


 AFP Software Solutions by ISIS Papyrus
www.isis-papyrus.com/

They have done colored graphics for insurance policies, I
was rather impressed.

---
eckhard



On Thu, 7 Jan 1999 20:33:13 -0500, "Gary R Hamaker"
<gary.r.hamaker@gte.net> wrote:

>I help maintain a billing system written in COBOL. The output from our
>process is an AFP file that is sent to a printer. Presently our graphics
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
