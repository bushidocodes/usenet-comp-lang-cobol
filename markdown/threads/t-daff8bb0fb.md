[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wanted: COBOL Paragraph renumbering tool

_11 messages · 8 participants · 1997-11 → 1997-12_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Language features and syntax`](../topics.md#syntax)

---

### Wanted: COBOL Paragraph renumbering tool

- **From:** "spa..." <ua-author-8337513@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<347cb656.4611237@news.top.net>`

```

Hi.

This is written by a person who's not touched COBOL in years... At my
work we use the 9999-Name-of-paragraph convention, and I really need a
utility to renumber paragraphs. Any help (source code) etc would be
very much appreciated.


Thanks alot!!


Ron
```

#### ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<347cb656.4611237@news.top.net>`
- **References:** `<347cb656.4611237@news.top.net>`

```

Mark and Ron wrote:
› 
› Hi.
…[8 more quoted lines elided]…
› Ron

Most, probably all, restructuring tools do this, although you have to
specify the parameters you need. Some have an option to just reformat
the source without restructuring it - which is what you want. Check what
you have in your installation.

Bill Lynch
```

##### ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "spa..." <ua-author-8337513@usenetarchives.gap>
- **Date:** 1997-11-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p2@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p2@usenetarchives.gap>`

```

On Thu, 27 Nov 1997 02:56:00 -0500, Bill Lynch
wrote:

› Most, probably all, restructuring tools do this, although you have to
› specify the parameters you need. Some have an option to just reformat
…[3 more quoted lines elided]…
› Bill Lynch

I'm on a Tandem mainframe, utilizing their (general purpose) TEDIT
editing utility. While I'm able to renumber source code lines, I have
no way of renumbering paragraphs (which should be read as "renaming
paragraphs") Do you know of perhaps, a DOS shareware editor that
would have this functionality. If so, I could just download my source
code from the Tandem to my PC, do the renaming, and upload it back.

I was thinking maybe on of those "programmer's editors" would to this.

Thanks.


Ron.
```

#### ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<347cb656.4611237@news.top.net>`
- **References:** `<347cb656.4611237@news.top.net>`

```

Mark and Ron wrote:
› 
› This is written by a person who's not touched COBOL in years... At my
› work we use the 9999-Name-of-paragraph convention, and I really need a
› utility to renumber paragraphs. Any help (source code) etc would be
› very much appreciated.

Are you sure you want to automate this? I structure my paragraph numbers to
match my program logic, and find it extremely useful. It seems to me that
any automated renumbering would destroy this relationship.

If you need more numbers, and are currently using four digits, why don't you
replace the four digit numbers with six digits, adding a 0 on the front and
back? (e.g. 1234-XXXX -> 012340-XXXX) This can be quickly done with any
editor that uses regular expression search/replace. For example, using
Brief, I would enter this (without quotes, preceding space intentional):
Replace " {[0-9][0-9][0-9][0-9]}-" By " 0\00-"
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "spa..." <ua-author-8337513@usenetarchives.gap>
- **Date:** 1997-11-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p4@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p4@usenetarchives.gap>`

```

On 28 Nov 1997 12:47:53 GMT, "Judson McClendon"
wrote:
›
› Are you sure you want to automate this? I structure my paragraph numbers to
› match my program logic, and find it extremely useful. It seems to me that
› any automated renumbering would destroy this relationship.
›

Not necessarily. Say for example, all my error handling routines are
in the 9000- series. I have 20 such routines so that the existing
routines are 9000- 9005- 9010- etc I add 9001- 9002- 9003-

I guess I'm just anal retentive, but I really would like to renumber
them equdistant say, 9000 9002 9004 9006 etc.

The only reason I even care about this at all is that it is a company
standard at my shop to use this numbering system. I personally dislike
it and would never use it myself.

To each their own I say. Whatever works, works. I however, operate on
the premise that if this were such a universally recoginized,
extremely useful way of structuring one's program, why is it only
used in COBOL and not (as far as I know) in any other language?

I guess I just have to live with the messy, yucky (not to mention icky
poo) reality of 9000 9001 9002 9005 9010 9020...

:)


Ron
```

###### ↳ ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "steve cooney" <ua-author-907591@usenetarchives.gap>
- **Date:** 1997-11-28T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p5@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p4@usenetarchives.gap> <gap-daff8bb0fb-p5@usenetarchives.gap>`

```

Mark and Ron wrote:
› 
› On 28 Nov 1997 12:47:53 GMT, "Judson McClendon"
…[30 more quoted lines elided]…
› 
I've followed this thread off and on. Are you having any success? If
not how about a COBOL program to read your source code looking for
paragraph names and then generating change records for input to SPF that
would do a global change of from - to (you would have to pre-edit to
provide the new numbers or set some rules that could be programmed). If
you want to work on this let me know. Could also set to run on a PC but
would need to work out the editor to use. (EDIT or SPFPC or BRIEF).
Steve Cooney
st··.@se··p.com
http://www.seadp.com
Copyright (C) 1997 by Steve Cooney, st··.@se··p.com -With explicit 
reservation of all rights, exclusively and without prejudice, 
per UCC 1-207. Any commercial or for-profit use of all or any part 
of this message, in any form, without permission of the author is 
expressly forbidden. Take Care.
```

###### ↳ ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

_(reply depth: 4)_

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p6@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p4@usenetarchives.gap> <gap-daff8bb0fb-p5@usenetarchives.gap> <gap-daff8bb0fb-p6@usenetarchives.gap>`

```

Rather than using an editor for the search/replace, I would just write one.
Unless you are changing the size of the paragraph numbers, there is no line
overflow problems, and you would want to change the paragraph numbers within
comments too, so the task would be simple. My approach would be to write a
simple program to extract all the paragraph names into a file. Then manually
edit that file, inserting some kind of commands to direct the renumbering.
Then write another simple program to read the file with the commands and
replace the paragraph numbers accordingly. It is quicker to write and debug
two or three simple programs than one large complicated one. I like the
'simple software tools' concept. Once you have the tools, they can often be
combined serendipitously and synergistically. You see this far less often
with 'monolithic' solutions.
```

###### ↳ ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

_(reply depth: 4)_

- **From:** "kevin j. hansen" <ua-author-17072510@usenetarchives.gap>
- **Date:** 1997-12-04T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p6@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p4@usenetarchives.gap> <gap-daff8bb0fb-p5@usenetarchives.gap> <gap-daff8bb0fb-p6@usenetarchives.gap>`

```

We have a COBOL program reformatter that renumbers paragraphs (if you select
that option), as well as aligns PIC clauses, verb/END-verb phrases, indents
IF and other statements, and generally makes code more readable. If you're
interested in a commercial product that does this, go to:

http://www.alaska.net/~norcom/Cobclean.htm

and check out our COBCLEAN product (and other COBOL tools, too).
```

#### ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "e. kelly" <ua-author-17073518@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<347cb656.4611237@news.top.net>`
- **References:** `<347cb656.4611237@news.top.net>`

```

"Write One" using the program as the input file, examine for col-7 being
numeric then inspect for first "-" replace leading with a starting num
sequence and add 10 to the num seq and search for the next paragraph to
write to the output file.
Mark and Ron wrote in message <347··.@new··p.net>...
› Hi.
› 
…[10 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p9@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p9@usenetarchives.gap>`

```

›› Mark and Ron wrote in message <347··.@new··p.net>...
››› Hi.
…[7 more quoted lines elided]…
››› 
A global change using a text editor should fix this in short order.
Start with the highest 9xxx- and make it high enough to include
all 9xxx- paragraphs, incremented by 5 or 10 or whatever.
Then work on the next highest 9xxx- etc.. 'til you get to the first.
eg.
change all 9100- to 9200-
change all 9095- to 9190-
etc...
change all 9002- to 9020-
change all 9001- to 9010-
If you have 20 paragraphs it'll take 20 global command changes.
Bill H.
```

###### ↳ ↳ ↳ Re: Wanted: COBOL Paragraph renumbering tool

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-daff8bb0fb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-daff8bb0fb-p10@usenetarchives.gap>`
- **References:** `<347cb656.4611237@news.top.net> <gap-daff8bb0fb-p9@usenetarchives.gap> <gap-daff8bb0fb-p10@usenetarchives.gap>`

```

Bill H. wrote:

› A global change using a text editor should fix this in short order.
 
› change all 9100- to 9200-
› change all 9095- to 9190-
› etc...
 
› If you have 20 paragraphs it'll take 20 global command changes.

If you have 1000 paragraphs it'll take 1000 global command changes. I
think the objective was to be a little more automated than that.

BTW, do you want to renumber just paragraph names, or did you actually
mean procedure names (paragraph and section names)?
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
