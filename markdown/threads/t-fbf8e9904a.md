[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Flowcharting

_17 messages · 12 participants · 2000-08_

---

### Flowcharting

- **From:** "M S" <maz@websurf.fsnet.co.uk>
- **Date:** 2000-08-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk>`

```
Hi
This is a student's question.
Can somebody please let me know, are there any websites
relating how to draw FLOWCHARTS for Programs. ie. I just
need some examples to refer because at the moment
I only use some of the
SQUARE BOXES for process line...
DIAMOND for decision....etc..(the basic ones)

I cant workout how to make a flowchart for the follwing
paragraph in a program..


SORTING-PROCESS.
     SORT   WORK-FILE
     ON ASCENDING CUST-CODE-KEY
     USING  CUSTOMER-FILE
     GIVING SORTED-FILE.


Can someone please give some hints on the above paragraph
for flowcharting.

Thankyou

Best regards
M S
```

#### ↳ Re: Flowcharting

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk>`

```
On Tue, 8 Aug 2000 21:45:48 +0100, "M S" <maz@websurf.fsnet.co.uk>
enlightened us:

>Hi
>This is a student's question.
…[25 more quoted lines elided]…
>

There are several ways you could show the SORT in your flowchart.  One
way is to use the defined symbol for SORT which is two triangles
attached at the base.  Another is to use the symbol for a predefined
process, which is a rectangle with interior verticle lines on each
side.

Hope that helps.

Regards,

  
          ////
         (o o)
-oOO--(_)--OOo-

I have six locks on my door all in a row. When I go out, I lock every
other one. I figure no matter how long somebody stands there picking the
locks, they are always locking three.






Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

 Steve
```

##### ↳ ↳ Re: Flowcharting

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ms04c$sk6$1@nnrp1.deja.com>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net>`

```
In article
<DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net>,
  SkippyPB <swiegand@neo.rr.com.nospam> wrote:
> On Tue, 8 Aug 2000 21:45:48 +0100, "M S" <maz@websurf.fsnet.co.uk>
> enlightened us:
>

First of all I would point out the obvious that the flow chart is done
before the program.  Then you take the flowchart and design the
program.

Not every line of code actually converts to a symbol or direction on a
flowchart.  Sort is just a process or a box.  Sort is built in process
in the compiler we dont need to know everything about it.  If you want
to make a separate process for sort where it looks at all possible
option that could be a separate process. This process could include the
files in and out and whether ascending or descending etc.

Your book may give you the complete list of options for all possible
sorts.  The compiler just looks at all of your parameters and executes
a bit of code that it has pre-programmed for sorting.

On a mainfram often the sort is done outside of the COBOL program by a
utility program.  The concept is the same you tell it the file going in
the fields to sort on and what type of sort for each field.  Then you
tell it about the output.

The actually sorting process is far more difficult from ordering a deck
of cards; especially when the deck is one million records; try laying
that out on the table!


> >Hi
> >This is a student's question.
…[42 more quoted lines elided]…
> other one. I figure no matter how long somebody stands there picking
the
> locks, they are always locking three.
>
…[7 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Flowcharting

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399320A8.350673EA@larich.com>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com>`

```
lcccpiasabird@my-deja.com wrote:
> 
> 
…[3 more quoted lines elided]…
> 

In what universe?   :-)
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mv9n3$9s5$1@slb3.atl.mindspring.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com>`

```

"David W. Furin" <dfurin@larich.com> wrote in message
news:399320A8.350673EA@larich.com...
> lcccpiasabird@my-deja.com wrote:
> >
…[7 more quoted lines elided]…
>

The universe of "acedemia" - which is the PRIMARY place where flowcharting is
still used.
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 4)_

- **From:** firdaus <callfirdaus@hotmail.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sp8e0khjn4t79@corp.supernews.com>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com>`

```
I think people who don't use the flowcharts are either
Very good programmers OR Very bad programmers OR just lay-easy!!
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 5)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44Zk5.7432$4T.434598@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com>`

```
firdaus continued the flowcharting string so I'll give my opinion.

Depending upon how much time students get on the computer, use flowcharting
to help teach and review learning.

Flow chart the program on the computer to create documentation for the
person that follows.

Adopt a uniform method for flowcharting.

Warren Simmons
"firdaus" <callfirdaus@hotmail.com> wrote in message
news:sp8e0khjn4t79@corp.supernews.com...
> I think people who don't use the flowcharts are either
> Very good programmers OR Very bad programmers OR just lay-easy!!
…[6 more quoted lines elided]…
> http://www.help.com/
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399465BB.3F638E7D@brazee.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <44Zk5.7432$4T.434598@bgtnsc07-news.ops.worldnet.att.net>`

```
Warren Simmons wrote:

> Flow chart the program on the computer to create documentation for the
> person that follows.

Use a drawing program, or using a computer program to generate the flow chart?

I use flow charts to document job flow (run the accounting feed before the bank
reconciliation), but find that well written COBOL is easier to read than flow
charts.  And generated flow charts don't know what is important, listing
everything.  This certainly is useless.
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n3klc$spb$1@news.igs.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com>`

```
For a good programmer, every flowchart is identical ...

firdaus wrote in message ...
>I think people who don't use the flowcharts are either
>Very good programmers OR Very bad programmers OR just lay-easy!!
…[6 more quoted lines elided]…
>http://www.help.com/
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 6)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bggl5.33246$RG6.2593371@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <8n3klc$spb$1@news.igs.net>`

```
Consequently, a great tool for beginners.

Warren
"donald tees" <donald@willmack.com> wrote in message
news:8n3klc$spb$1@news.igs.net...
> For a good programmer, every flowchart is identical ...
>
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n4fv1$de6$1@news.igs.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <8n3klc$spb$1@news.igs.net> <bggl5.33246$RG6.2593371@bgtnsc05-news.ops.worldnet.att.net>`

```
You have me there.  That is very true.  I seldom(never) formally  flowchart
anymore, though I do tend to use them as sketches when thinking. They are
also a great way to talk to other programmers when you have a blackboard.
One shop I know keeps an instant camera beside a whiteboard, and snapshots
of discussions go into the documentation.

Warren Simmons wrote in message ...
>Consequently, a great tool for beginners.
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 8)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mql5.34407$RG6.2682578@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <8n3klc$spb$1@news.igs.net> <bggl5.33246$RG6.2593371@bgtnsc05-news.ops.worldnet.att.net> <8n4fv1$de6$1@news.igs.net>`

```
By golly, I know a site like that myself. Back in the 60's our company
selected a computer on the basis of the software among other things.  CSC
was the vendor of the software, and this was one of my assignments.  See
that the COBOL spec would meet our needs.  I spent two weeks with this
group, and they used a Polaroid camera just to keep track of they
developments on the black board.  They also had a "universal" assembler
system they used to work between platforms.  I remember one name only, Owen
Mock.  Long time ago.

Warren Simmons
"donald tees" <donald@willmack.com> wrote in message
news:8n4fv1$de6$1@news.igs.net...
> You have me there.  That is very true.  I seldom(never) formally
flowchart
> anymore, though I do tend to use them as sketches when thinking. They are
> also a great way to talk to other programmers when you have a blackboard.
> One shop I know keeps an instant camera beside a whiteboard, and
snapshots
> of discussions go into the documentation.
>
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 9)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n6du8$fd4$1@news.igs.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <8n3klc$spb$1@news.igs.net> <bggl5.33246$RG6.2593371@bgtnsc05-news.ops.worldnet.att.net> <8n4fv1$de6$1@news.igs.net> <9mql5.34407$RG6.2682578@bgtnsc05-news.ops.worldnet.att.net>`

```
    mAYBE THINGS DO NOT (<-- See what happens when you change from COBOL to
human? Note the start in Column 8) change as much as we think.  I just
thought of a flowchart that I used in the last year.  I was down in
Pennsylvania at a customer site, reviewing the data flow between a system
that I wrote and the in house SAP system.  They had a whiteboard with an
RS-232-C interface ... one of the neatest toys I have seen in a long time.
After you sketched on it with a marker, you pressed a button and it
downloaded into your PC as a PC-paint bit map. They had it hooked up to
their network, and I just plugged my PC into a hub. Full colour, four by
four foot whiteboard.  Hate to think what it cost.

We designed a really simple interface.  They would deposit my updates as
flat files in a specific directory on the net, and I would poll that
directory at specific intervals.  When I found a file, I would do  batch
update, and move the file to either an "OKAY" directory, or to an "ERROR"
directory.  I would also leave transactions that I originated in a fourth
directory, and would do my backup to a fifth.  We sketched all that out as
flowcharts on the board, and each grabbed our copy.  Then we headed back to
our respective locales (they to Europe, me to Canada, the US guys to
Chicago, etc.) and we did the rest by Email.

"Universal Assemblers" used to be common, though I only used one once(I
evolved it out of the need for migration).  I think most of them were really
just particularly good macro assemblers that somebody decided to use the
macro facility to write code for a different platform.  That is what
happened to me.  I used to write all my assembler using an extensive macro
library.  I expanded the macro library to include several OS's, then finally
to several CPU's before I retired the code.  I have re-written most of the
code in Cobol now ... it seems really wasteful to write something like a
device driver in Cobol, but it is a lot easier to maintain and keep current.
Pretty cheap, too, when I can devote an entire computer to an I/O subsystem,
and hook it into a world sized net for a thousand bucks worth of parts.


Warren Simmons wrote in message
<9mql5.34407$RG6.2682578@bgtnsc05-news.ops.worldnet.att.net>...
>By golly, I know a site like that myself. Back in the 60's our company
>selected a computer on the basis of the software among other things.  CSC
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Flowcharting

_(reply depth: 8)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<amql5.34408$RG6.2682093@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk> <DAE70E45DD04E7DA.DA50115ECFDEDEFE.C54F27F848E31B39@lp.airnews.net> <8ms04c$sk6$1@nnrp1.deja.com> <399320A8.350673EA@larich.com> <sp8e0khjn4t79@corp.supernews.com> <8n3klc$spb$1@news.igs.net> <bggl5.33246$RG6.2593371@bgtnsc05-news.ops.worldnet.att.net> <8n4fv1$de6$1@news.igs.net>`

```
By golly, I know a site like that myself. Back in the 60's our company
selected a computer on the basis of the software among other things.  CSC
was the vendor of the software, and this was one of my assignments.  See
that the COBOL spec would meet our needs.  I spent two weeks with this
group, and they used a Polaroid camera just to keep track of they
developments on the black board.  They also had a "universal" assembler
system they used to work between platforms.  I remember one name only, Owen
Mock.  Long time ago.

Warren Simmons
"donald tees" <donald@willmack.com> wrote in message
news:8n4fv1$de6$1@news.igs.net...
> You have me there.  That is very true.  I seldom(never) formally
flowchart
> anymore, though I do tend to use them as sketches when thinking. They are
> also a great way to talk to other programmers when you have a blackboard.
> One shop I know keeps an instant camera beside a whiteboard, and
snapshots
> of discussions go into the documentation.
>
…[23 more quoted lines elided]…
>
```

#### ↳ Re: Flowcharting

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3990866B.9E757BB2@Josella-Simone-Playton.de>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk>`

```
2000-08-09 00:17:00 MESZ

M S wrote:
> 
> ...

Wouldn't you consider to use Nassi-Shneiderman diagrams
instead? Programs written that way have a tendency to work
as expected - in any language.

Herwig
```

#### ↳ Re: Flowcharting

- **From:** "Colonel" <psxzone@btinternet.com>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OK0k5.16530$gv3.554101@news-east.usenetserver.com>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk>`

```
Hi M S.
Being a student myself I know what you mean.

Personally I take each COBOL `verb` ( in your example the SORT verb ) and
translate it to the respective flowchart symbol. So being that the SORT verb
uses INPUT and OUTPUT files, I would use the respective INPUT/OUTPUT symbol.

Hope this helps. ( If you can understand it )

Colonel
psxzone@btinternet.com

M S <maz@websurf.fsnet.co.uk> wrote in message
news:8mprsn$ktj$1@newsg2.svr.pol.co.uk...
> Hi
> This is a student's question.
…[26 more quoted lines elided]…
>
```

#### ↳ Re: Flowcharting

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3992c354.947156@news1.frb.gov>`
- **References:** `<8mprsn$ktj$1@newsg2.svr.pol.co.uk>`

```
On Tue, 8 Aug 2000 21:45:48 +0100, M S wrote:

>This is a student's question.
>Can somebody please let me know, are there any websites
>relating how to draw FLOWCHARTS for Programs. 

Use your favorite search engine.  I entered "flowchart symbols" into
http://www.snap.com/ , and it came up with several web pages
containing information on flowchart symbols and their application.

[snippage]
>I cant workout how to make a flowchart for the follwing
>paragraph in a program..
[...]
>     SORT   WORK-FILE
>     ON ASCENDING CUST-CODE-KEY
[...]
>Can someone please give some hints on the above paragraph
>for flowcharting.

I have seen SORTs diagrammed using any of the PROCESS (rectangle),
PREDEFINED PROCESS (rectangle with double vertical lines), or
AUXILIARY PROCESS (square) symbols.

You might see this diagrammed as:
       |
       |
       V
---------------
|| Sort      ||
|| WORK-FILE ||
||       ... ||
---------------
       |
       |
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
