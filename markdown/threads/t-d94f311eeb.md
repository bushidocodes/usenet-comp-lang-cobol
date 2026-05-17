[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Future

_5 messages · 5 participants · 1997-07_

---

### COBOL Future

- **From:** "paruka" <ua-author-17072563@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`

```

This is probably an often asked question but I would appeciate input as I
am a relative newbie to COBOL.

We are working on a OLTP client-server architecture consisting primarily of
HP-UNIX and Win '95 OS's. WE have decided to do our future server-based
application development in Microfocus COBOL (client-side Powerbuilder).

We have not legacy COBOL, no real skills, yet the powers that be have
decided. I would appreciate input on :
1. The future of COBOL, is it a dead or dying language
2. Why would I want to use it if I have no legacy in it. Does it have any
useful features that make it attractive over C/C++ for example. I always
assumed it was a viable route in order to protect the COBOL investment not
as a fresh tool. "Challenge all assumptions"
3. What are the down-sided to using COBOL - eg application development
environments, shortage of skills

Are there any other issues I should be aware of in terms of, in order to
setup a well structured development environment eg COBOLs impact on
shorter/longer development times, increased/reduced quality etc?

Much appreciated
Ashraff
```

#### ↳ Re: COBOL Future

- **From:** "the..." <ua-author-96015@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d94f311eeb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`
- **References:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`

```

FYI - Believe it or not, many of the "state of the art" PeopleSoft
proponents who look down on COBOL developers are totally unaware that
PeopleSoft has a COBOL foundation and ships with a Microfocus compiler.
```

##### ↳ ↳ Re: COBOL Future

- **From:** "k..." <ua-author-612019@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d94f311eeb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d94f311eeb-p2@usenetarchives.gap>`
- **References:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za> <gap-d94f311eeb-p2@usenetarchives.gap>`

```

On 16 Jul 1997 02:51:32 GMT, the··.@a··.com (Theo DP) wrote:

› FYI - Believe it or not, many of the "state of the art" PeopleSoft
› proponents who look down on COBOL developers are totally unaware that
› PeopleSoft has a COBOL foundation and ships with a Microfocus compiler.

True, I took an "intro" course onsite by the vendor. They were very
open about how their system works and I was amazed that the pc code we
were looking at was Cobol. I believe their basic concept was to
modularize the functions for reusability.

Cheers,

Kevin........."Due to SPAM, remove KEV and replace
with KKLT1 when replying by email"
```

#### ↳ Re: COBOL Future

- **From:** "john m. saxton, jr" <ua-author-17071440@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d94f311eeb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`
- **References:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`

```

PARUKA wrote:
› 
› This is probably an often asked  question but I would appeciate input as I
…[23 more quoted lines elided]…
› 
Since I don't know your exact application, I may inadvertently make
some incorrect assumptions... however,

IMHO... I firmly believe that COBOL is the best language to express /
solve business problems, ie produce reports, manage accounts, insurance,
financials, etc. There are a lot of language based features that you can
take for granted in COBOL, such as the moving and handling of strings,
moving data between different data types. These features may be
important to your business app.

In terms of dying languages... though I don't know the exact number,
there are millions of programs written in COBOL. There is a huge number
of people who are qualified to develop in this language.

In terms of quality... any language is a tool. How it is used effects
over all quality. If the project takes the time to set up adequate
standards, set up a project architecture, and communicate it then it is
fair to expect a quality result. How the project is managed effects
the ability to deliver on time, not the language (unless the wrong
tools are chosen, ie COBOL to write system level code)

I don't want to start a flame war over which language is best... I think
that one should pick the right tool for the job at hand, so please, no
heat...
Return address is John underscore Saxton at ML dot com
```

#### ↳ Re: COBOL Future

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1997-07-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d94f311eeb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`
- **References:** `<01bc910f$f6a55aa0$0a346e93@duvi.eskom.co.za>`

```

PARUKA wrote:
...
› 1. The future of COBOL, is it a dead or dying language

IMHO COBOL is unkillable. Too much investment, too many wheels to
reinvent eg there's lots of stuff like mainframe DB access that uses
COBOL as a run-time environment/scaffolding language.

› 2. Why would I want to use it if I have no legacy in it.  Does it have any
› useful features that make it attractive over C/C++ for example.  I always
› assumed it was a viable route in order to protect the COBOL investment not
› as a fresh tool.  "Challenge all assumptions"

Portability to mainframes? eg for galactic-scale servers. Generally
speaking COBOL systems are a lot simpler than C ones, due to the
language having fewer capabilities eg you don't get production problems
from memory leakage or dangling pointers in COBOL! So maintenance is
cheaper & availability is better. BTW 'legacy' is a pejorative term
invented by PeeCeeWeeNees for the readership of PC magazines; the term
actually refers to the systems currently running the enterprise.

› 3. What are the down-sided to using COBOL - eg application development
› environments, shortage of skills

One reason businesses keep on with COBOL is that there is no shortage of
COBOL skills in the market. Although the Y2K problem is showing that it
is finite that is a relatively short-term problem & after about 2001
COBOL skills will be plentiful and cheapish.

yours, Patrick
________________________________________________________
Patrick Herring at work, her··.@rls··o.uk
Disclaimer: The form is BT but the essence is me.

"Occam's razor is so sharp, I bought the whole argument"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
