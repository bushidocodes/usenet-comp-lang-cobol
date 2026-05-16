[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# After Advancing 2 lines - unrecognized verb

_13 messages · 11 participants · 1999-11_

---

### After Advancing 2 lines - unrecognized verb

- **From:** dc606@my-deja.com
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
I have tried using:

Write Print-Line after Advancing 2 Lines and I get following error:

"Unrecognized verb" for this statement.

Any idea why?



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382367D5.4843@saif.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
dc606@my-deja.com wrote:
> 
> I have tried using:
…[8 more quoted lines elided]…
> Before you buy.

The syntax you posted here looks fine for mainframe LE/370 COBOL.  Maybe
you are in a different compiler that doesn't support it?  Older
mainframe COBOL required "AFTER POSITIONING" instead of "AFTER
ADVANCING".

Pete
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** Cityboy@Concentric.Net [Ron]
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<802mtg$e74@chronicle.concentric.net>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
>I have tried using:
>
…[5 more quoted lines elided]…
>

AFTER ADVANCING has worked on every IBM compiler I've ever used going
back to IBM DOS (mainframe) on a 360. A period makes no difference
unless it prematurely terminates the statement.  The syntax is fine
for an IBM compiler. If this is *exactly* the the way you have it
coded in the program AND you are using an older IBM compiler such as
OS Cobol or VS Cobol II, it may not recognize the verb in lower case.
If that's not it, please post more of code and what compiler you are
using so we see.
```

##### ↳ ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** JohnTrifon <jtrifon@ix.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826DD9B.9B711289@ix.netcom.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com> <802mtg$e74@chronicle.concentric.net>`

```
There is nothing syntactically incorrect about your 'WRITE...'. You may
want to look to see if it starts in Col 12, and not 11 (or less)
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<800631$ino$1@news.inet.tele.dk>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
You didn't forget a period, huh?
Regards
Ib
dc606@my-deja.com skrev i meddelelsen <7vuv0i$qvg$1@nnrp1.deja.com>...
>I have tried using:
>
…[9 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "Barvin" <barvin@mwis.net>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q5QU3.427$mf7.4993@newsfeed.slurp.net>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
have you tried different ways to please any compiler quarks?
WRITE PRINT-LINE AFTER ADVANCING 2
or
WRITE PRINT-LINE AFTER 2
or perhaps
WRITE THE *@&^! PRINT-LINE ALREADY PRETTY-PLEASE
:-)

but then again perhaps there is a missing period and the WRITE has it at a
total loss.

David
barvin@mwis.net
The Barvin Web Site
http://barvin.mwis.net


<dc606@my-deja.com> wrote in message news:7vuv0i$qvg$1@nnrp1.deja.com...
> I have tried using:
>
…[9 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "ChrisOsborne" <chris_n_osborne@email.msn.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#E2m0fWK$GA.235@cpmsnbbsa03>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
Please post the entire paragraph containing the statement. :)  Maybe a type
somewhere else is causing this error.



<dc606@my-deja.com> wrote in message news:7vuv0i$qvg$1@nnrp1.deja.com...
> I have tried using:
>
…[9 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1TsV3.179$Av4.7108@typhoon.columbus.rr.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
>Write Print-Line after Advancing 2 Lines and I get following error:
>
>"Unrecognized verb" for this statement.
>
>Any idea why?


Code all paragraphs with just ONE and ONLY ONE period at the end of the
paragraph.

USE SCOPE TERMINATORS for all statements where possible.

Eliminat one word at a time from the offending statement until the syntax
error disappears. This may reveal the error.
```

##### ↳ ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806ov0$dcl$1@news.igs.net>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com> <1TsV3.179$Av4.7108@typhoon.columbus.rr.com>`

```
What nonsense.  There is a difference between syntax and style.

Gumbo wrote in message <1TsV3.179$Av4.7108@typhoon.columbus.rr.com>...
>>Write Print-Line after Advancing 2 Lines and I get following error:
>>
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xCmW3.1891$Av4.37866@typhoon.columbus.rr.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com> <1TsV3.179$Av4.7108@typhoon.columbus.rr.com> <806ov0$dcl$1@news.igs.net>`

```
>What nonsense.  There is a difference between syntax and style.
I said the same thing when I was first told to eliminate periods and use
scope terminators.

Style techiniques can and do eliminate syntax errors. The only way to find
out is to develop a relatively complex program from scratch and check it out
yourself.

It not only eliminates errant period erros but allows for easy insertion of
code into complicated IF and PERFORM blocks.
```

###### ↳ ↳ ↳ Re: After Advancing 2 lines - unrecognized verb

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80ebn4$p01$1@news.igs.net>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com> <1TsV3.179$Av4.7108@typhoon.columbus.rr.com> <806ov0$dcl$1@news.igs.net> <xCmW3.1891$Av4.37866@typhoon.columbus.rr.com>`

```

Gumbo wrote in message ...
>>What nonsense.  There is a difference between syntax and style.


>I said the same thing when I was first told to eliminate periods and use
>scope terminators.
>
>Style techiniques can and do eliminate syntax errors. The only way to find
>out is to develop a relatively complex program from scratch and check it
out
>yourself.


I have.  Several. maybe even several thousand. It is still nonsense when
someone is told to revise a programs style from scratch to fix a bug that
has nothing to do with style.

>
>It not only eliminates errant period erros but allows for easy insertion of
>code into complicated IF and PERFORM blocks.
>
I do not use complicated if and perform blocks.  I simplify them.
```

###### ↳ ↳ ↳ Re: After Advancing 2 lines - unrecognized verb

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382ACF4F.ABE28B1B@NOSPAMhome.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com> <1TsV3.179$Av4.7108@typhoon.columbus.rr.com> <806ov0$dcl$1@news.igs.net> <xCmW3.1891$Av4.37866@typhoon.columbus.rr.com> <80ebn4$p01$1@news.igs.net>`

```
donald tees wrote:

> >It not only eliminates errant period erros but allows for easy insertion of
> >code into complicated IF and PERFORM blocks.
> >
> I do not use complicated if and perform blocks.  I simplify them.

Bravo.  That makes much more sense than eliminating periods from code
which already is using scope terminators.

Scope terminators and simplified logic clarify your code.  Eliminating
periods does not.
```

#### ↳ Re: After Advancing 2 lines - unrecognized verb

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991111162257.29850.00000045@ng-co1.aol.com>`
- **References:** `<7vuv0i$qvg$1@nnrp1.deja.com>`

```
>I have tried using:
>
…[4 more quoted lines elided]…
>Any idea why?

I sometimes beat myself to death trying to figure out why a
simple line of code like this won't work, only to find out I
have misspelled a reserved word.  Remember the thread
a few months ago about ASSIGN and ASSGIN? And
PERFORM and PERFROM?

Advancing can easily become Adanvcing when your fingers
get ahead of your brain.  Try re-typing the line carefully
and I'll bet you it works.

JC Jones.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
