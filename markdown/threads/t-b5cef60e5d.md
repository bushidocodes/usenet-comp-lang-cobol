[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: I need cobol program analysis tools

_12 messages · 6 participants · 2002-11 → 2002-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help: I need cobol program analysis tools

- **From:** luisdereyna@mundofree.com (luis de reyna)
- **Date:** 2002-11-23T01:46:28-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<36ee84f5.0211230146.62d5c25a@posting.google.com>`

```
I need basic metrics and complexity metrics for some megabytes of
source cobol code. I'm looking for a tool.

It has to be public domain or free, and (of course) I'd prefer source
code for linux o unix, but anything will do (say windows, os390 etc.).

Home made or experimental will do, too.

Could somebody help please?

Thanks.
```

#### ↳ Re: I need cobol program analysis tools

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2002-11-23T13:18:42-06:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<3ddfd304$1@giga.realtime.net>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com>`

```

"luis de reyna" <luisdereyna@mundofree.com> wrote in message
news:36ee84f5.0211230146.62d5c25a@posting.google.com...
> I need basic metrics and complexity metrics for some megabytes of
> source cobol code. I'm looking for a tool.
>
> It has to be public domain or free, and (of course) I'd prefer source
> code for linux o unix, but anything will do (say windows, os390 etc.).

We have Windows-based tools that can parse COBOL and can easily be
configured
to produce all kinds of arbitrary metrics.
See http://www.semdesigns.com/Products/DMS/DMSToolkit.html.
Not free, though.
```

##### ↳ ↳ Re: I need cobol program analysis tools

- **From:** luisdereyna@mundofree.com (luis de reyna)
- **Date:** 2002-11-26T00:20:47-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<36ee84f5.0211260020.1db0c564@posting.google.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3ddfd304$1@giga.realtime.net>`

```
"Ira Baxter" <idbaxter@semdesigns.com> wrote in message news:<3ddfd304$1@giga.realtime.net>...
> 
> We have Windows-based tools that can parse COBOL and can easily be
…[3 more quoted lines elided]…
> Not free, though.

I'm looking for public domain or free sw.

Thank you anyhow.
```

##### ↳ ↳ Re: I need cobol program analysis tools

- **From:** luisdereyna@mundofree.com (luis de reyna)
- **Date:** 2002-11-26T00:42:07-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<36ee84f5.0211260042.52e04d58@posting.google.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3ddfd304$1@giga.realtime.net>`

```
"Ira Baxter" <idbaxter@semdesigns.com> wrote in message news:<3ddfd304$1@giga.realtime.net>...
> "luis de reyna" <luisdereyna@mundofree.com> wrote in message
> news:36ee84f5.0211230146.62d5c25a@posting.google.com...
…[10 more quoted lines elided]…
> Not free, though.

Thanks again here for your posting.

But, why my original posting has disappeared, and then yours is here,
answering mine?

Sort of magic.
```

#### ↳ Re: Help: I need cobol program analysis tools

- **From:** Niels Veerman <nveerman@cs.vu.nl>
- **Date:** 2002-11-26T10:47:41+01:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<3DE3433D.5DB5B1B6@cs.vu.nl>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com>`

```
luis de reyna wrote:

> I need basic metrics and complexity metrics for some megabytes of
> source cobol code. I'm looking for a tool.
…[8 more quoted lines elided]…
> Thanks.

We are working on parsing and transformation of Cobol from an academic
viewpoint. However, we have no tools ready for distribution yet (we only
have experimental tools). We are working on linux and unix platforms.
If you can tell what kind of metrics you need maybe we can help you.
Eventually, you will be able to install the tools yourself.
```

##### ↳ ↳ Re: Help: I need cobol program analysis tools

- **From:** luisdereyna@mundofree.com (luis de reyna)
- **Date:** 2002-11-26T10:55:10-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<36ee84f5.0211261055.51516780@posting.google.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl>`

```
Niels Veerman <nveerman@cs.vu.nl> wrote in message news:<3DE3433D.5DB5B1B6@cs.vu.nl>...
> luis de reyna wrote:
> 
…[16 more quoted lines elided]…
> Eventually, you will be able to install the tools yourself.

Thank you very much for answering. I'll explain what we are working
in.

We plan to migrate some applications, some in cobol, some in an xbase
like language. We want to compare the results of basic statistics, say
lines, variables (fields), records, sentences paragraphs, verbs or
whatever components the tool may account for, with those of some other
applications we have already migrated, so we can have an estimate of
the work to do.

If the program can give an estimate or parameter for the "complexity"
of the programs, or for the complete system, that will also be of use,
because we could compare it with that of the known programs.

I'm a Linux supporter, and I love to install and try things by myself,
and there are some other Linux guys here.

So, if you are willing to give us a chance, we will try your program,
and tell you about the results.

Thank you in advance. 

Best regards.
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

- **From:** Niels Veerman <nveerman@cs.vu.nl>
- **Date:** 2002-11-27T11:22:12+01:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<3DE49CD4.1BD5BA5C@cs.vu.nl>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com>`

```

Do you have an email address? The supplied address does not seem to accept email.

luis de reyna wrote:

>
>
…[22 more quoted lines elided]…
> Best regards.
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

_(reply depth: 4)_

- **From:** mlittle@transoft.com (Michelle)
- **Date:** 2002-12-02T05:20:28-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<ca97b565.0212020520.7d9a43e9@posting.google.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com> <3DE49CD4.1BD5BA5C@cs.vu.nl>`

```
Hi Luis

I work for a company called Transoft & we are authors of the renowned
evolveIT analysis workbench & a wide range of COBOL programming,
Componantisation & Migration tools. I would be happy to send you some
more information and get one of our technical experts to answer any
questions you may have.


Michelle Little
mlittle@transoft.com

Transoft Ltd, 5J Langley Business Centre, Station Road, Langley,
Slough, SL3 8DS England
Tel: +44 (0)1753 778000		Fax: +44 (0)1753 773050

Transoft is a leading international provider of application assembly,
transformation and integration solutions. The Transoft Intelligent
Adapters enable existing critical business application functions to be
easily exposed and re-used as application and Web services, to build
new scalable, integrated (e)business applications faster and with less
risk

Niels Veerman <nveerman@cs.vu.nl> wrote in message news:<3DE49CD4.1BD5BA5C@cs.vu.nl>...
> Do you have an email address? The supplied address does not seem to accept email.
> 
…[26 more quoted lines elided]…
> > Best regards.
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

_(reply depth: 5)_

- **From:** luisdereyna@mundofree.com (luis de reyna)
- **Date:** 2002-12-03T06:56:02-08:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<36ee84f5.0212030656.28b948aa@posting.google.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com> <3DE49CD4.1BD5BA5C@cs.vu.nl> <ca97b565.0212020520.7d9a43e9@posting.google.com>`

```
Thank you Michelle. 

Right now we need only a rough estimate, and are not planning for an
investment. Maybe later we may need some renowned tools. By now,
unless you can give us a free trial ride, we'll have to do with some
other thing.

Best regards.


mlittle@transoft.com (Michelle) wrote in message news:<ca97b565.0212020520.7d9a43e9@posting.google.com>...
> Hi Luis
> 
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

_(reply depth: 5)_

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2002-12-03T20:36:02+01:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<asj1bj$ngc$1@reader11.wxs.nl>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com> <3DE49CD4.1BD5BA5C@cs.vu.nl> <ca97b565.0212020520.7d9a43e9@posting.google.com>`

```
Hi Michelle,

It's a small world after all eh?

Greetings from Danny.

Maijer ICT Services
Alkemaderschans 13
3432 CH  Nieuwegein
Tel: 030-6579755
GSM: 0621-242789
E-mail : info@maijerict.net
Web : www.maijerict.net (Dutch alas)


"Michelle" <mlittle@transoft.com> schreef in bericht
news:ca97b565.0212020520.7d9a43e9@posting.google.com...
> Hi Luis
>
…[21 more quoted lines elided]…
> Niels Veerman <nveerman@cs.vu.nl> wrote in message
news:<3DE49CD4.1BD5BA5C@cs.vu.nl>...
> > Do you have an email address? The supplied address does not seem to
accept email.
> >
> > luis de reyna wrote:
…[25 more quoted lines elided]…
> > > Best regards.
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

_(reply depth: 6)_

- **From:** "xpyttl" <xpyttl_nospam@earthling.net>
- **Date:** 2002-12-03T21:25:26-05:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<uuqpv5gb0qc1d@corp.supernews.com>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com> <3DE49CD4.1BD5BA5C@cs.vu.nl> <ca97b565.0212020520.7d9a43e9@posting.google.com> <asj1bj$ngc$1@reader11.wxs.nl>`

```
It's a very small world.  In spite of being trapped in the frozen north of
the U.S for most of my life, I worked in the bustling metropolis of
Nieuwegein many moons ago.

..

"Danny Maijer" <info@liveartists.com> wrote in message
news:asj1bj$ngc$1@reader11.wxs.nl...
> Hi Michelle,
>
…[10 more quoted lines elided]…
> Web : www.maijerict.net (Dutch alas)
```

###### ↳ ↳ ↳ Re: Help: I need cobol program analysis tools

_(reply depth: 7)_

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2002-12-04T10:48:23+01:00
- **Newsgroups:** comp.lang.cobol,comp.software-eng
- **Message-ID:** `<askja7$t6g$1@reader08.wxs.nl>`
- **References:** `<36ee84f5.0211230146.62d5c25a@posting.google.com> <3DE3433D.5DB5B1B6@cs.vu.nl> <36ee84f5.0211261055.51516780@posting.google.com> <3DE49CD4.1BD5BA5C@cs.vu.nl> <ca97b565.0212020520.7d9a43e9@posting.google.com> <asj1bj$ngc$1@reader11.wxs.nl> <uuqpv5gb0qc1d@corp.supernews.com>`

```
Many moons ago I used to work for a great company called COSS.....It fell
apart when Management Share took over and screwed up...Rings any bell ?


"xpyttl" <xpyttl_nospam@earthling.net> schreef in bericht
news:uuqpv5gb0qc1d@corp.supernews.com...
> It's a very small world.  In spite of being trapped in the frozen north of
> the U.S for most of my life, I worked in the bustling metropolis of
…[20 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
