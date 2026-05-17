[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do Non-COBOL

_15 messages · 11 participants · 1994-11 → 1994-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to do Non-COBOL

- **From:** "joe.k..." <ua-author-12816976@usenetarchives.gap>
- **Date:** 1994-12-16T13:35:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
mis··.@ats··d.com wrote in a message to All:

›› I've been coding COBOL for lots of years, using "strutured, top-down" 
›› coding which requires the use of sub-programs. I have been able to do 
…[9 more quoted lines elided]…
› 
ma> I've been using COBOL for almost 18 years and GOBACK has
ma> always been a COBOL verb. In fact, I have run across
ma> compilers that do not accept EXIT PROGRAM.

GOBACK is an IBM extension to COBOL. It's not in the actual COBOL ANSI
standard, if I'm not mistaken.

Later,
Joe
---------
Fidonet: Joe Klemmer 1:109/370
Internet: Joe··.@f37··t.org
```

#### ↳ Re: How to do Non-COBOL

- **From:** "ia..." <ua-author-15560912@usenetarchives.gap>
- **Date:** 1994-11-27T16:36:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
Don't use GOTOs.
The *possible* exception being in the DECLARATIVES Section where you may need
to skip over some code to get to an exit.
```

#### ↳ Re: How to do Non-COBOL

- **From:** "har..." <ua-author-2202518@usenetarchives.gap>
- **Date:** 1994-11-28T01:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
In Article <3b882g$9.··.@ixn··m.com>, kur··.@ix.··m.com (Kurt
Miscovich) wrote:

› Although you can use GO TO the use of GO TO in a COBOL program is 
› frowned upon. Using GO TO leads to spagetti code and should be avoided 
› at any costs. However GO TO can be used if it will make the program 
› simpler. But I have never found a case were GO TO would make the program 
› simpler.

My main argument against using GO TO is that you can't easily lift code out
of a program that uses GO TO. You have to carefully examine the code before
you lift it. Copying code from a structured program that doesn't use GO TO
is MUCH easier because you can copy a subroutine and paste it into any other
program. About the only thing you have to watch out for is conflicting
variable names.

The other reason to stop using GO TO is that COBOL is about the only
language that still supports this construct these days. Most modern
programming languages that are being developed these days lack a verb like
GO TO, so you might as well get used to not using it.

Also, programs that use GO TO are sometimes harder to understand (IMHO).
Every time I come across a GO TO in a program I'm not familiar with I have
to search for a paragraph label. Sometimes while searching for the
paragraph label, I forget where I was. I'll admit, the same thing can
happen with nested performs....
---
* Harry Myhre
```

#### ↳ Re: How to do Non-COBOL

- **From:** "pat..." <ua-author-16283716@usenetarchives.gap>
- **Date:** 1994-11-29T07:21:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```



› Hi, I would like to know how to do GOTO in COBOL ANSI 85.
›
› Like where and how to put the LABEL.
 
›› Stuff Deleted

I am a programming student who has just finished a long COBOL course and
the topic of GO TO was raised a lot. I was taught by someone who came from
the days of spaghetti code (no disrespect intended) and so we were initially
taught that it was never to be used. Later on though, it was allowed to be
used as long as it was only to the EXIT of the paragraph or section that it
was issued in.

I would first ask what is the GO TO being used for. Is it being used to get
out of a situation due to bad design? or is it being used because it avoids
complcated code and improves readability.

Allowing for my inexperience, I can't see how any decent programmer would
condone the former or condemn the latter.

************************
```

#### ↳ Re: How to do Non-COBOL

- **From:** "codecr..." <ua-author-7766424@usenetarchives.gap>
- **Date:** 1994-12-06T17:06:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p5@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
› Richard Ross-Langley wrote:
 
› Another thing Dijkstra is reputed to have said, in about
› 1978, is that microcomputers will "set computing back 10 years".
› It seems it was nearer 15 years :-)
› 
› 
Unfortunately for us COBOL types he also said (in a marvellously
opinionated article called "How do we tell truths that might hurt?" in
1974):

"The use of COBOL cripples the mind; its teaching, therefore, must be
regarded as a criminal offence".

I'd plead Nolo Contendre and not bother with the argument, personally :-)

Pete

(cod··.@cix··o.uk)
```

#### ↳ Re: How to do Non-COBOL

- **From:** "john beatty" <ua-author-106704@usenetarchives.gap>
- **Date:** 1994-12-07T22:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p6@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
Hello, McFly, is anybody in there???

GOTOs are *NOT* good for anything. We shoot our developers
for even *considering* them..

John Beatty
Sprint, Kansas City, MO
-----------------------


On 6 Dec 1994, Robert Dewar wrote:

› Matt, the real point is that you should not have an aversion to the GO TO
› verb, instead you should have an aversion to improper use of the GO TO.
…[6 more quoted lines elided]…
›
```

#### ↳ Re: How to do Non-COBOL

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-08T14:42:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p7@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: Anyway a little question for Joseph I. Tsatskin, how would you program
: a finite statge machine with lots of states in COBOL. It is vrey neat to
: encode the state in the program counter, and this is the one place where
: many people feel the goto solution IS appropriate (note that in some sense
: a finite state transition diagram is spaghetti to start with, and has
: no decomposable structure, or at least need not have any decomposable
: structure!)

Strangely enough, we use FSMs a *whole* lot in our work, in Cobol.
One of the best ways to write a serious program, interactive or batch.
Yet, not one single GOTO in something like a million lines of very
maintainable code. (Though lots of STOP RUNs, one per main program...)
If anyone seriously wants to know how to program an efficient and
readable FSM in Cobol (or C, or Fortran, or assembler, or PL/I, or
Basic, ...) drop me a line.
```

#### ↳ Re: How to do Non-COBOL

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-08T14:59:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p8@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
Vadim Maslov (va··.@cs.··d.edu) wrote:
: Not using GOTOs is the same kind of extremism as drinking decaffeinated
: coffee (what a name!). Mr. Dewar has a valid point here, that state
: machines do need GOTOs. I've written several lexical analyzers
: which all happen to be state machines, and they all use GOTOs.
: Programming them without GOTOs would be a real disaster.

When I started developing state machines in Cobol, I failed to recognise
the danger of not using GOTOs, and so, for a decade, I have failed to
use GOTOs in state machines in Cobol, C, and lots of other languages.
Pure ignorance, I know, and I'll not be able to sleep until all those
pending disasters are properly rewritten to use GOTOs. I hope my
clients will one day forgive me. :-(

You know that the language you use defines the way you think. If you
feel that a GOTO will help, you'll find any reason to justify it. If
you never heard of GOTO, you'll just do it another way.

I once knew a programmer who had total fear of using COMPUTE. He had
one particular program that was several thousand lines long, and mostly
consisted of one long IF statement. Something like:

IF QUANTITY = 1
MOVE 17 TO RESULT
.
IF QUANTITY = 2
MOVE 34 TO RESULT
...
IF QUANTITY = 1000
MOVE 17000 TO RESULT
.
```

#### ↳ Re: How to do Non-COBOL

- **From:** "jeff gentile" <ua-author-17073935@usenetarchives.gap>
- **Date:** 1994-12-09T15:02:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p9@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
› ==========Vadim Maslov, 12/8/94==========
› 
 
› (Stuff deleted to save bandwidth.  See comment below.)
 
› 
› Summary: there are several disciplines of writing code.
…[9 more quoted lines elided]…
› 

My first COBOL teacher from my college days, had a suggestion which
I took to heart regarding GO TOs. It was basically that, if your GO TO
procedure name isn't one page up or down on your printout, you might
want to rethink your code. Of course, now days it might be one screen
display up or down. Like most things in life, the good/badness of GO
TOs are in shades of gray.

For most PERFORM and GO TO bigots, it is a mute issue in ANSI
COBOL 85 because of nested programs. The implementations I've seen
of this feature, make is a structured programers dream. Nested programs
end up being equated to modules that some of us are familiar with in
other languages.

Jeff Gentile
AT&T GIS Service Technology
jef··.@day··r.com
513 445-5283
"Never trust a distorted mirror"
```

#### ↳ Re: How to do Non-COBOL

- **From:** "codecr..." <ua-author-7766424@usenetarchives.gap>
- **Date:** 1994-12-10T16:43:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p10@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
› Matt Harmon at mh1··.@xx.··e.edu wrote:
 
›  [ apologies for the crap quoting ]
 
›     What I really dislike is using sections to process the results of a 
› sort
…[14 more quoted lines elided]…
› retain sections in the procedure division?

There are lots of possible answers, but (taking your points in turn):

a) Lots of COBOL instructors insist on teaching people to use paragraphs.
There's nothing wrong with that - until you start
using
(for example) internal sorts. I personally incline to the view of
using
*only* sections - the sort rules fit well, and (this is the flame-bait
bit), I like to use "Go to Section-Exit" for situations like
skip-this-
branch/office/whatever. I'd suggest using SECTION all the time (face
it, the extra typing won't kill you) for this reason and also because
it's a bit more robust -- mixing performed sections and paragraphs
in the same program is error-prone to say the least, absolutely
f**kwitted to say the most -- don't do it!

It's also fair to say that you'll learn more looking at a good manual
than *any* tutor has time to give you. Take a look at what sections
have to offer -- it's a lot.

b) For backward compatibility purposes, and also because they're *very*
useful.

Cheers!

Pete

(cod··.@cix··o.uk)
```

#### ↳ Re: How to do Non-COBOL

- **From:** "ku..." <ua-author-13068511@usenetarchives.gap>
- **Date:** 1994-12-13T09:47:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p11@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
mis··.@ats··d.com (Bill Comegna) writes:

› In article <329··.@kcb··n.nz>, Ric··.@kcb··n.nz (Richard Plinston) writes...
››› 
…[4 more quoted lines elided]…
››› "goback?"

Don't know about how a GOBACK works in a main program, but I do know that
as of version 4.0 of VAX COBOL, the EXIT PROGRAM only functions correctly
within a called program or subroutine. If you use EXIT PROGRAM in the main
calling program it will fall through to the next executable statement within
your main program. I found that out the hard way and had to go through
every main program in a software package Clemson wrote to change all EXIT
PROGRAM to STOP RUN.

›› So where you say "I've been coding COBOL ... goback ...".  This is
›› not COBOL.  It would be EXIT PROGRAM and STOP RUN if it was COBOL.
›› 
 
› I've been using COBOL for almost 18 years and GOBACK has always been
› a COBOL verb.   In fact, I have run across compilers that do not
› accept EXIT PROGRAM.

The GOBACK was/is used in an IBM environment when I was in school. VAX
COBOL uses EXIT PROGRAM and doesn't recognize GOBACK.

Sallie

Courtesy Liz "BB" Fox via someone's bumper | Sallie Kudra, Sr. Sys. Analyst
sticker: | Information Systems Development
| Clemson Univ., Clemson, SC
Wild Women Don't Get the Blues | ku··.@hub··n.edu
```

#### ↳ Re: How to do Non-COBOL

- **From:** "ku..." <ua-author-13068511@usenetarchives.gap>
- **Date:** 1994-12-14T08:12:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p12@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
Martyn Woerner writes:


› Sallie, I guess you misunderstand the EXIT PROGRAM function (as specified
› in the ANSI standard).  If its in a called program, then it returns control 
…[6 more quoted lines elided]…
› to putting both the EXIT and the STOP (unless someone else knows differently).

No, I understand it does exactly what it was intended. What I found was that
the software package I had inherited had used the EXIT PROGRAM *as* a STOP
RUN in all of the main programs. And up until version 4.0 of VAX COBOL the
EXIT PROGRAM *did* function like a STOP RUN. Hence why I had to change all
main programs EXIT PROGRAM to STOP RUN after the installation of version 4.0.
Now, the EXIT PROGRAM functions as what it was intended - a way out of a
called subroutine or a subprogram without stopping the calling program execution
as well. At least in VAX COBOL.

I know this is what happens because of a very complicated extract program that
had an EXIT PROGRAM instead of STOP RUN. Before version 4.0, the program exe-
cution terminated using EXIT PROGRAM. After version 4.0, the program attempted
to continue execution by creating all the extract files again (opened 32 files)
and only died when it hit a SORT statement within the main code. After I
pored over the release notes for the 4.0 version I found exactly what I
describe above - that the EXIT PROGRAM was to be used to exit from called
routines not as a STOP RUN.

Sallie
Courtesy Liz "BB" Fox via someone's bumper | Sallie Kudra, Sr. Sys. Analyst
sticker: | Information Systems Development
| Clemson Univ., Clemson, SC
Wild Women Don't Get the Blues | ku··.@hub··n.edu
```

#### ↳ Re: How to do Non-COBOL

- **From:** "chr..." <ua-author-6409325@usenetarchives.gap>
- **Date:** 1994-12-15T11:20:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p13@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
In article <3cg9k8$4.··.@ixn··m.com> RDN··.@ix.··m.com (Robert Noyes) writes:

› I've been coding COBOL for lots of years, using "strutured, top-down" 
› coding which requires the use of sub-programs. I have been able to do 
› this without ever using "stop run." Indeed, "goback" has worked fine in 
› everything I've ever coded, "main" included. Have you tried using 
› "goback?"

I must agree with you. "GOBACK" has been the recommended method for *all*
program termination since at least the mid '70s.

I have written many COBOL apps on MVS, DOS VSE, and even MS-DOS (using at
least 3 different compilers for the latter) both before ANSI '85 COBOL and
after, including CALLing sub-programs in all of the above environments,
without ever needing to code STOP RUN.



Christopher N. Baucom When you come to a fork in the road,
Gastonia, NC take it! - Yogi Berra
```

#### ↳ Re: How to do Non-COBOL

- **From:** "chr..." <ua-author-6409325@usenetarchives.gap>
- **Date:** 1994-12-15T12:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p14@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
In article <199··.@at··s.com> bru··.@at··s.com (Bruce Arbuckle) writes:
› You should also keep in mind that "structured" programming, COBOL
› or otherwise has been on the scene only for about 15 years in
› an ACCEPTEDD mode by many MIS departments.

If by accepted you mean as a common "shop standard" then you're pretty close,
though I can tell you that the government standard required structured
(GOTO-less) COBOL in 1978. And that by that time they were quite attimate
about the no GOTO rule. Though enforcement of that standard was, like all
"standards", dependent upon the shop/project manager's feelings on the
matter.

› [...] It also takes a while for some programmers to change (and some
› never will) to the new method. Just look at the difference between the old
› top down structured method and the new OOD.

This will always be true. And despite all efforts to require adherance to
standards, it would require "Big Brother" tactics (which I detest more than
GOTO's) to insure 100% compliance.

› So, just because you have 11 years doesn't mean that your exposure
› is wide enought to see enough possible cases where a GOTO will not
› create bad code or un maintainable code.

I can assure you that I have been exposed to plenty of cases where GOTOs
(mostly written before or around the time structured standards were put in
place) created bad and un-maintainable code. I have had to untangle horrific
spagetti code which despite shop standards had been patched a gazillion times
because everyone had given up on following the merry chase the GOTOs led.

› If someone is doing maintaince on a program in todays environment
› and they don't have good documentation (like, yikes a FLOW CHART)
…[4 more quoted lines elided]…
› and some damn GOTO wont be a GOTCHA.

Unfortunately, it is more the rule than the exception that such documentation
does not exist on legacy systems. And even more rare to find $ in the budget
to fund bringing the documentation up to date.

› [...]I don't think that its years of exeprience that count as much as where 
› the experience has been gained.  Have you experienced many types of 
› business and government applications?  I would much rather employ
› someone with a varied background than some one with the same years
› in one or two similar business applications.

Consulting in Government, Manufacturing, Banking, Retail, Insurance (16 yrs.)

Seriouly, no flame intended here. In a perfect world what you say is true. I
don't believe GOTO's are inherently evil. I simply have seen far too many
examples of their misuse to ever endorse or accept *new* code which contains
GOTO's.

ps - I have never run accross a problem I couldn't solve, in a more
readable format, with structured programming. Especially since COBOL '85.
(Which I think is the greatest thing since sliced bread!)
Christopher N. Baucom When you come to a fork in the road,
Gastonia, NC take it! - Yogi Berra
```

#### ↳ Re: How to do Non-COBOL

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1994-12-15T14:03:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ada2330de7-p15@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`
- **References:** `<ua-fallback-XtuYxlp0A2I@usenetarchives.gap>`

```
In article <3cl9ar$f.··.@sat··z.au> Stephen Wales,
ste··.@min··z.au writes:
› John Beatty (bea··.@tyr··l.net) wrote:
› : Hello, McFly, is anybody in there???
…[8 more quoted lines elided]…
› these lines:
 
› some stuff with lots of PERFORMs
 
› etc etc etc
› 
…[20 more quoted lines elided]…
› that pays your salary.
 
› Why use sections and paragraphs for really short pieces of code at all?
 
› You code to their standards whether you like it or not.  I was shocked
› when I
…[4 more quoted lines elided]…
› 
Do any of these standards recognize in-line PERFORM statements?
All of the examples I see don't recognize that they exist.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
