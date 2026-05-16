[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Batch COBOL Immediate S0C1

_7 messages · 7 participants · 2001-07_

---

### Batch COBOL Immediate S0C1

- **From:** "Alex Browne" <Alex@StarbayLtd.Nospam.BTInternet.co.uk>
- **Date:** 2001-07-06T21:22:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i56m1$eki$1@uranium.btinternet.com>`

```
 Can someone tell me why a batch COBOL program running within a DB2 region
under TSO should immediately abend with a S0C1? I'm guessing it's something
to do with the linkedit, but am getting nowhere.....

 Thanks
 Alex
```

#### ↳ Re: Batch COBOL Immediate S0C1

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-06T22:01:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7zq17.2727$7J5.219311@dfiatx1-snr1.gtei.net>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com>`

```
Alex Browne <Alex@StarbayLtd.Nospam.BTInternet.co.uk> wrote in message
news:9i56m1$eki$1@uranium.btinternet.com...
> Can someone tell me why a batch COBOL program running within a DB2 region
> under TSO should immediately abend with a S0C1? I'm guessing it's
something
> to do with the linkedit, but am getting nowhere.....
>

That would be my guess, too, but I given you have a batch program, I would
really, really really double-check any passed parameters to insure the
number and sizes are correct. I think if you don't pass enough parameters
you get a S0C1.

MCM
```

#### ↳ Re: Batch COBOL Immediate S0C1

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2001-07-06T17:31:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i5dt7$guvr0$1@ID-39920.news.dfncis.de>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com>`

```

Alex Browne <Alex@StarbayLtd.Nospam.BTInternet.co.uk> wrote in message
news:9i56m1$eki$1@uranium.btinternet.com...
> Can someone tell me why a batch COBOL program running within a DB2 region
> under TSO should immediately abend with a S0C1? I'm guessing it's
something
> to do with the linkedit, but am getting nowhere.....
>
>  Thanks
>  Alex
>

There are lots of things that could get you a S0C1.  Are there any messages
in your JES log?  Sysout?  JCL log?

Your linkedit could be to blame, but I would also check your parm and
DD's....
```

#### ↳ Re: Batch COBOL Immediate S0C1

- **From:** Bill <wfsent@optonline.net>
- **Date:** 2001-07-07T01:06:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B466083.C811FB98@optonline.net>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com>`

```
INCLUDE DSNELI ?

Bill

Alex Browne wrote:

>  Can someone tell me why a batch COBOL program running within a DB2 region
> under TSO should immediately abend with a S0C1? I'm guessing it's something
…[3 more quoted lines elided]…
>  Alex
```

##### ↳ ↳ Re: Batch COBOL Immediate S0C1

- **From:** "Kjeld Paab���l Hansen" <paabol@12mail.dk>
- **Date:** 2001-07-08T01:56:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b47a1d5$0$304$edfadb0f@dspool01.news.tele.dk>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com> <3B466083.C811FB98@optonline.net>`

```
At some installations, at least it holds true in the one I'm working at, DB2
entry points vil be included thru the module DSNHLI which is normally used
to connect to DB2 via IMS. When creating TSO/DB2 modules you will have to
force TSO connection to DB2 with the module DSNELI by adding the control
card which Bill mentioned, to linkage editor input.

Kjeld P. Hansen

"Bill" <wfsent@optonline.net> skrev i en meddelelse
news:3B466083.C811FB98@optonline.net...
> INCLUDE DSNELI ?
>
…[4 more quoted lines elided]…
> >  Can someone tell me why a batch COBOL program running within a DB2
region
> > under TSO should immediately abend with a S0C1? I'm guessing it's
something
> > to do with the linkedit, but am getting nowhere.....
> >
> >  Thanks
> >  Alex
>
```

###### ↳ ↳ ↳ Re: Batch COBOL Immediate S0C1

- **From:** engelhardt@dvoid.org (Heiner Engelhardt)
- **Date:** 2001-07-13T11:07:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<225570b2.0107131007.4183562d@posting.google.com>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com> <3B466083.C811FB98@optonline.net> <3b47a1d5$0$304$edfadb0f@dspool01.news.tele.dk>`

```
The abend S0C1 is comming if the system detects unexecutable
instructions (like exec cics in an batch environment). A DB2 Module
thet you whant to call in a CICS- and also in a BATCH-environment you
must have 2 load modules: for batch link the DB2 Modul including
DSNALI and for CICS link DB2 Module including DSNHLI and your
prpogramm will run. You have to be sure thet you dont use cics
instruction in your programm.

"Kjeld Paab? Hansen" <paabol@12mail.dk> wrote in message news:<3b47a1d5$0$304$edfadb0f@dspool01.news.tele.dk>...
> At some installations, at least it holds true in the one I'm working at, DB2
> entry points vil be included thru the module DSNHLI which is normally used
…[22 more quoted lines elided]…
> >
```

##### ↳ ↳ Re: Batch COBOL Immediate S0C1

- **From:** "warren.simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-07-17T15:07:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GwY47.40105$C81.3351435@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<9i56m1$eki$1@uranium.btinternet.com> <3B466083.C811FB98@optonline.net>`

```
Bill,

DSNELI does what?  How or where is it included?  Open up a little Bill,
AFAIK knowone bytes in this forum despite the name calling, and childish
behaviour from time to time.

Warren Simmons
warren.simmons@worldnet.att.net

Bill <wfsent@optonline.net> wrote in message
news:3B466083.C811FB98@optonline.net...
> INCLUDE DSNELI ?
>
…[4 more quoted lines elided]…
> >  Can someone tell me why a batch COBOL program running within a DB2
region
> > under TSO should immediately abend with a S0C1? I'm guessing it's
something
> > to do with the linkedit, but am getting nowhere.....
> >
> >  Thanks
> >  Alex
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
