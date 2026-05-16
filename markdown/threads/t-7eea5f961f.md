[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen Section, Screen Events, Declaratives

_14 messages · 9 participants · 2004-09 → 2004-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Screen Section, Screen Events, Declaratives

- **From:** "Lueko Willms" <lw-nospam@t-online.de>
- **Date:** 2004-09-22T17:38:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de>`

```

I'm starting to study the "screen section" and related items in the
2002 standard and in the Fujitsu 3.0 compiler which I use.  BTW - does
anybody know in how far these differ (and then the Fujitsu as
Microfocus compatibility items...)? 

Anyway, what I am missing is a capability to react to screen events,
i.e. entering and leaving a field, clicking and double-clicking,
mouse-over etc. All those events one can study e.g. in Javascript or
Visual Basic or similar development tools. 

The form most best fitting in the basic ideas of COBOL, as I see it,
would be procedures in the DECLARATIVES part of the PROCEDURE DIVISION.


Like "USE ON {FIELD-ENTRY | FIELD-EXIT | DOUBLE-CLICK | MOUSE-OVER |
...}  OF screen-data-name-1"

similar to the "USE BEFORE REPORTING report-group-1"

Isn't it there, or did I overlook something? 

This applies, of course, only to interactive programs running on the
workstation which control every aspect of the screen display, not for
programs which exchange data blockwise  with a remote screen, be that
an IBM 3270, Unisys Uniscope or Poll/Select-Terminal, or a HTML
Browser. 


Yours, 
L. Willms
------------------------------ all rights reserved ------------------------
```

#### ↳ Re: Screen Section, Screen Events, Declaratives

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-09-22T09:46:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cisa96$2pk7$1@si05.rsvl.unisys.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de>`

```

"Lueko Willms" <lw-nospam@t-online.de> wrote in message
news:yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de...
>
> I'm starting to study the "screen section" and related items in the
> 2002 standard and in the Fujitsu 3.0 compiler which I use.  BTW - does
> anybody know in how far these differ (and then the Fujitsu as
> Microfocus compatibility items...)?

Personal opinion only:

The Screen Section is a "processor dependent" module of 2002 standard COBOL,
and my *personal* (but carefully-considered) opinion is that it was about
fifteen years too late.  It is fundamentally a "green-screen" terminal-style
interface, and the industry has gone way beyond that.  I remember
considerable sentiment to scrap it altogether late in the process of
standardization; I think the final result enabled its use as a "style guide"
for implementors to do whatever they wanted to do for a more modern
interface.  I suspect that's what both MF and FJ have done, perhaps others;
I'm not sure what "real world" assistance the 2002 standard is going to
provide you in this context.

> The form most best fitting in the basic ideas of COBOL, as I see it,
> would be procedures in the DECLARATIVES part of the PROCEDURE DIVISION.
...

From the standards standpoint, we'd need a better interface than the Screen
Section as it now stands before adding other structural widgets.

    -Chuck Stevens
```

##### ↳ ↳ Re: Screen Section, Screen Events, Declaratives

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-09-22T15:15:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10l3jsj2sof6he3@corp.supernews.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:cisa96$2pk7$1@si05.rsvl.unisys.com...
[snip]
> Personal opinion only:
>
> The Screen Section is a "processor dependent" module of 2002 standard
COBOL,
> and my *personal* (but carefully-considered) opinion is that it was about
> fifteen years too late.  It is fundamentally a "green-screen"
terminal-style
> interface, and the industry has gone way beyond that.

One might argue that the inclusion of Screen Section in
XOPEN, ages ago, means that ANSI/ISO 'was about
fifteen years too late.'
```

##### ↳ ↳ Re: Screen Section, Screen Events, Declaratives

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-22T15:26:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409221426.24a1569@posting.google.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote 

> The Screen Section is a "processor dependent" module of 2002 standard COBOL,
> and my *personal* (but carefully-considered) opinion is that it was about
> fifteen years too late.  

It derives from the X/Open standard of 20 years ago or more.
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

- **From:** Esmond Pitt <esmond.pitt@not.bigpond.com>
- **Date:** 2004-10-06T08:20:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qVN8d.16053$5O5.6476@news-server.bigpond.net.au>`
- **In-Reply-To:** `<217e491a.0409221426.24a1569@posting.google.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com> <217e491a.0409221426.24a1569@posting.google.com>`

```
Richard wrote:

> It derives from the X/Open standard of 20 years ago or more.

It originally derives from Data General ICOBOL of around 1978-9. 
Definitely green-screen stuff & definitely should have become a 
USE-procedure-based event-driven thing in COBOL-2002. I did some work on 
a prototype for this about 1992 so we are really a terribly long way 
behind the state of the art now.

Esmond Pitt
formerly of Austec International Ltd
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-10-06T11:53:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9INXB7X9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au>`

```
.    Am  06.10.04
schrieb  esmond.pitt@not.bigpond.com (Esmond Pitt)
    auf  /COMP/LANG/COBOL
     in  qVN8d.16053$5O5.6476@news-server.bigpond.net.au
  ueber  Re: Screen Section, Screen Events, Declaratives

EP> Definitely green-screen stuff & definitely should have become a
EP> USE-procedure-based event-driven thing in COBOL-2002.

   Or part of the data definition in the Screen Section, i.e. in a  
form where one specifies the procedure names to call for the various  
events. I am vacillating between the two ...

   Although, really, COBOL provides all conditions for event-driven  
programming with the DECLARATIVES.


EP> I did some work on a prototype for this about 1992 so we are
EP> really a terribly long way behind the state of the art now.

   A specification or actual software?


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Das Volk, das ein anderes Volk unterjocht, schmiedet seine eigenen
Ketten."                         - Karl Marx           (1. Januar 1870)
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 5)_

- **From:** Esmond Pitt <esmond.pitt@not.bigpond.com>
- **Date:** 2004-10-08T02:31:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WZm9d.17818$5O5.7293@news-server.bigpond.net.au>`
- **In-Reply-To:** `<9INXB7X9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au> <9INXB7X9flB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:

>    Although, really, COBOL provides all conditions for event-driven  
> programming with the DECLARATIVES.

That's what I meant, USE PROCEDURES are in the DECLARITIVES.

> EP> I did some work on a prototype for this about 1992 so we are
> EP> really a terribly long way behind the state of the art now.
> 
>    A specification or actual software?

Both.
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 6)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-10-08T06:30:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9IVkPXbuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <9INXB7X9flB@jpberlin-l.willms.jpberlin.de> <WZm9d.17818$5O5.7293@news-server.bigpond.net.au>`

```
.    Am  08.10.04
schrieb  esmond.pitt@not.bigpond.com (Esmond Pitt)
    auf  /COMP/LANG/COBOL
     in  WZm9d.17818$5O5.7293@news-server.bigpond.net.au
  ueber  Re: Screen Section, Screen Events, Declaratives

LW>>    Although, really, COBOL provides all conditions for
LW>> event-driven programming with the DECLARATIVES.

EP> That's what I meant, USE PROCEDURES are in the DECLARITIVES.

   As I wrote in the message which opened this thread, dated 22.09.04,  
17:38, Msg-Id  yhrxbjvyyzfgbayvarqr.i4gpgi6.pminewsnews.t-online.de

   I was just considering the way I work with VDP (a database-oriented  
development tool) and Visual Basic, where one works with a graphical  
interface on the screen form and specifies the events and how to  
handle them more or less as properties of the fields and the form  
itself.

   This is something which I would like to have for a COBOL program.  
This tool should produce a COPY element for the SCREEN SECTION and  
another COPY element for the DECLARATIVES part of the PROCEDURE  
DIVISION. The program would then be compiled and linked with a screen  
handling run time module.

   Back in my Univac days, I worked with DPS (Display Processing  
Sytsem), which worked in a similar way, i.e. there is a program which  
allows to design a form, which then produces a COPY element to be used  
in the COBOL program (or for another language).

   The difference is of course that there is no screen event  
processing for the DECLARATIVES since that part is handled by the  
terminal which sends the data in one chunk to the 'big iron' host.


EP>>> I did some work on a prototype for this about 1992 so we are
EP>>> really a terribly long way behind the state of the art now.

LW>>    A specification or actual software?

EP> Both.

   And that went under with this Australian company whose fate you  
described in the other message?

   Nothing transferred to RM/COBOL? A pity.

   To use ACCEPT and DISPLAY unter control of a program with its  
strict sequence is, in my opinion, not the proper way to handle screen  
events.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Ohne Pressefreiheit, Vereins- und Versammlungsrecht ist keine
Arbeiterbewegung mï¿½glich"        - Friedrich Engels      (Februar 1865)
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 7)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-10-08T13:49:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mVw9d.3469$q%7.1916@newssvr11.news.prodigy.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <9INXB7X9flB@jpberlin-l.willms.jpberlin.de> <WZm9d.17818$5O5.7293@news-server.bigpond.net.au> <9IVkPXbuflB@jpberlin-l.willms.jpberlin.de>`

```
"Lueko Willms" <l.willms@jpberlin.de> wrote in message 
news:9IVkPXbuflB@jpberlin-l.willms.jpberlin.de...
[snip]
> EP>>> I did some work on a prototype for this about 1992 so we are
> EP>>> really a terribly long way behind the state of the art now.
…[8 more quoted lines elided]…
>   Nothing transferred to RM/COBOL? A pity.

If Esmond did this in 1992, it was several years after the dissolution of 
Austec.

>
>   To use ACCEPT and DISPLAY unter control of a program with its
> strict sequence is, in my opinion, not the proper way to handle screen
> events.

I certainly agree with this.  The 'strict sequence' tends to cause the 
combination of business rules with the presentation of data, confusing the 
distinction between the two.  This confusion leads in many cases to confused 
code.

Tom Morrison
Liant Software Corporation
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 4)_

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2004-10-06T21:19:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EIOdndXYDLgkBPncRVn-vw@comcast.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au>`

```
> formerly of Austec International Ltd

Now there's a name I haven't heard for a while.  We used ACE Cobol back in
the 80's to move our software from DG to Unix and used it until we switched
to Acucobol (after Austec was bought by RM or something like that).

"Esmond Pitt" <esmond.pitt@not.bigpond.com> wrote in message
news:qVN8d.16053$5O5.6476@news-server.bigpond.net.au...
> Richard wrote:
>
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 5)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-10-07T15:36:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ynd9d.1693$Lk3.210@newssvr12.news.prodigy.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au> <EIOdndXYDLgkBPncRVn-vw@comcast.com>`

```
"JJ" <jj@nospam.com> wrote in message 
news:EIOdndXYDLgkBPncRVn-vw@comcast.com...
>> formerly of Austec International Ltd
>
…[3 more quoted lines elided]…
> to Acucobol (after Austec was bought by RM or something like that).

Actually, it was the other way around.

Austec purchased Ryan-McFarland Corporation (RMC) from Don Ryan and Dave 
McFarland.  Austec, a publicly traded company in Australia, had a very rough 
go when the major stock market downturn caught it in the undertow.  Language 
Processors Inc (LPI) purchased the assets of Austec, including RMC, in the 
late 1980s.  The combined companies were renamed Liant Software Corporation. 
The corporate geneology actually goes back to the 1960s in the RMC branch. 
See http://www.liant.com/about/.

I got to travel to Melbourne (Austec's corporate HQ) as the folks in RMC and 
Austec began to learn about each others' technology.  Esmond, a VP in Austec 
at the time, was a gracious host and is a top-rate mind.

Tom Morrison

>
> "Esmond Pitt" <esmond.pitt@not.bigpond.com> wrote in message
> news:qVN8d.16053$5O5.6476@news-server.bigpond.net.au...
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 6)_

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2004-10-07T21:18:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16ednXi3vtmcdvjcRVn-iA@comcast.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au> <EIOdndXYDLgkBPncRVn-vw@comcast.com> <Ynd9d.1693$Lk3.210@newssvr12.news.prodigy.com>`

```
OK, thanks for the memory refresh.  I remembered that something went on with
RM Cobol and we continued using ACE Cobol until around the time of the LPI
acquisition.

"Tom Morrison" <t.morrison@liant.com> wrote in message
news:Ynd9d.1693$Lk3.210@newssvr12.news.prodigy.com...
> "JJ" <jj@nospam.com> wrote in message
> news:EIOdndXYDLgkBPncRVn-vw@comcast.com...
> >> formerly of Austec International Ltd
> >
> > Now there's a name I haven't heard for a while.  We used ACE Cobol back
in
> > the 80's to move our software from DG to Unix and used it until we
> > switched
…[5 more quoted lines elided]…
> McFarland.  Austec, a publicly traded company in Australia, had a very
rough
> go when the major stock market downturn caught it in the undertow.
Language
> Processors Inc (LPI) purchased the assets of Austec, including RMC, in the
> late 1980s.  The combined companies were renamed Liant Software
Corporation.
> The corporate geneology actually goes back to the 1960s in the RMC branch.
> See http://www.liant.com/about/.
>
> I got to travel to Melbourne (Austec's corporate HQ) as the folks in RMC
and
> Austec began to learn about each others' technology.  Esmond, a VP in
Austec
> at the time, was a gracious host and is a top-rate mind.
>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section, Screen Events, Declaratives

_(reply depth: 6)_

- **From:** Esmond Pitt <esmond.pitt@not.bigpond.com>
- **Date:** 2004-10-08T02:29:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HYm9d.17817$5O5.14885@news-server.bigpond.net.au>`
- **In-Reply-To:** `<Ynd9d.1693$Lk3.210@newssvr12.news.prodigy.com>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de> <cisa96$2pk7$1@si05.rsvl.unisys.com> <217e491a.0409221426.24a1569@posting.google.com> <qVN8d.16053$5O5.6476@news-server.bigpond.net.au> <EIOdndXYDLgkBPncRVn-vw@comcast.com> <Ynd9d.1693$Lk3.210@newssvr12.news.prodigy.com>`

```
Tom Morrison wrote:

> Austec, a publicly traded company in Australia, had a very rough 
> go when the major stock market downturn caught it in the undertow.

Hi Tom, you're much too kind. Austec expired from a bad case of 
founder's disease, started to acquire things it knew nothing about, took 
its eye completely off the RMC ball (at one point I believe actually 
*ran out of stock* of RM/COBOL installation diskettes), and blew $30m in 
listing capital which should have kept us going from then until now. 
Eventually it missed an interest payment, the bank moved in, and we all 
moved on. Onwards and upwards of course ... I got my money out in time.

> I got to travel to Melbourne (Austec's corporate HQ) as the folks in RMC and 
> Austec began to learn about each others' technology.  Esmond, a VP in Austec 
> at the time, was a gracious host and is a top-rate mind.

Again Tom you're too kind but I also greatly enjoyed your hospitality in 
Texas and found several top-rate minds at RM including yourself.

Best regards

Esmond Pitt
```

#### ↳ Re: Screen Section, Screen Events, Declaratives

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-09-22T21:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xJl4d.477081$M95.111526@pd7tw1no>`
- **In-Reply-To:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de>`
- **References:** `<yhrxbjvyyzfgbayvarqr.i4gpgi6.pminews@news.t-online.de>`

```
Lueko Willms wrote:

>I'm starting to study the "screen section" and related items in the
>2002 standard and in the Fujitsu 3.0 compiler which I use.  BTW - does
…[34 more quoted lines elided]…
>
Leuko,

Would suggest your starting point should be the following :-

F/J -  NetCOBOL V 7 - http://www.netcobol.com/download/manuals_online.htm#2

M/F - N/E V 4.0 - 
http://supportline.microfocus.com/supportline/documentation/books/nx40/nx40indx.htm

It's a guess but I think the above F/J reference will probably closely 
follow what you have in V 3.0 and should be near the 2002 standard.. I 
have no knowledge of F/J - but I do recall that Richard wrote it wasn't 
a particularly helpful tool. (Mind you he *really* does like his own 
stuff  :-)    )

As regards M/F - look at the Language Reference Manual, chapter for 
Screen Section and pick out any extensions indicated by a balloon (MF). 
Going back to DOS days, M/F had a set of CBL_SCREEN routines, 
screen-attributes, colouring, blinking etc.,  plus use of Mouse to get 
events, (same thing, but not Windows events as intended with GUIs). 
There is a separate manual on Character Screen Handling - and I'm fairly 
certain it now contains two of those old DOS programs, one called LogPer 
(Logical Progression ?) and the other ADMOUSE lets you point the mouse 
at a cell in a two-dimensional table. Haven't looked for years, so don't 
know whether or not 2002 has the feature, but in the program for Mouse 
use, it allows you to build the outline 2D table with an occurs.

As to your questions about trying to interface with other 'screening' - 
I would have my doubts.

If you need Logper or Admouse source - e-mail me dropping second "J" in 
my e-mail addresss.

Jimmy, Calgary AB.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
