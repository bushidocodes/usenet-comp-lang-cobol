[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question and Answer from the GNU-COBOL project

_1 message · 1 participant · 2000-01_

---

### Question and Answer from the GNU-COBOL project

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84n5rg$d5p$1@nntp5.atl.mindspring.net>`

```
I thought the following question(s) and my answers might be of interest to
all of c.l.c.

> Bill,
>
…[32 more quoted lines elided]…
> feel my questions are particularly dumb ;-)

   ****

Your questions are not dumb.  Furthermore, they are all issues that get
discussed and RE-discussed at J4 (ANSI) and WG4 (ISO) groups regularly.  I
can try to answer from my perspective but do want you to understand that I
*often* disagree with J4 - and this is why I have just recently rejoined it
after several years of being off it.

"OPTIONALITY"
  Getting rid of the '85 Standard concepts of "optional modules" and
different "levels" of support was a "design goal" early in the revision work.
It was felt that one of COBOLs biggest "selling points" is its portability
(which - pardon the expression - is considered MUCH better than that of C,
for example, where you can't even tell from ANSI/ISO C how big an "int" is.)

Report Writer was the "prime" example of how "optionality" was the "kiss of
death" to portability.  Back in the 60's when it was first introduced, it was
"state-of-the-art".  Yet, it was not universally implemented, so programmers
didn't rely on it, so it got less used, so less implementors implemented it,
etc, etc.  The decision was made that ANY feature that was worth defining was
worth requiring WHEN/WHERE the "processor" could support it.  (Therefore, it
isn't required to support Report-Writer for a compiler that isn't used on
machines with "printers" - nor is it required to support the new
ACCEPT/DISPLAY in environments without character-capable screens).

OK, lets look at some of the "specific" examples of required features.

Enhanced ACCEPT/DISPLAY (based on the existing X/Open definition and in
COMMON use among UNIX and Workstation compilers - as an extension - today).
   This is WITHOUT DOUBT the most "controversial" required new feature.  One
country (Germany) has done everything they can (via the ISO channels) to get
this removed.  It is interesting to me that when they first started
complaining about this "feature", they told us all that GUIs would be all
that ANYONE would be using come the "next millennium".  Anyone on this list
want to tell me what GUI *standard* interface is available YET for UNIX?  How
about the number of "green-screen" applications still running in IBM
mainframe environments, (and I believe several other proprietary systems).
   My personal opinion is that this feature is a useful feature and will be
used in the following cases:
  - To port X/Open conforming applications into the new Standard
  - As a "debugging tool" (similar to the "old" DISPLAY statement) when you
don't want/need a "full debugger"
  - for almost NO "new" development of "production code"

       ***

Report-Writer:
  Another controversial (still) decision.  It has been enhanced as well as
being made mandatory.  I can tell you that when IBM "dropped" it from their
mainframe compiler (between OS/VS COBOL and VS COBOL II), they THOUGHT that
it wasn't used very much.  Experience since then has caused a VERY lucrative
business for an "add-on" product that provides this support for any existing
or new IBM COBOL site.  Personally, I still think that there are more COBOL
programs being written and maintained with "report output" than there are
with "GUI" *OR* character interfaces.  It is true that such programs COULD be
written in COBOl with "output" to 4th GLs, but for those of us who "know and
love" RW, this really is an incredibly easy-to-learn and use and FLEXIBLE
tool. (And yes, I am a report writer "bigot" so this is one area that I
*hope* stays required.)

Note:
  You may want to look at the new VALIDATE facility for another case of where
a "new COBOL feature" seems - to some - to be adding support now for
technology of the '70s or '80s.  The interesting thing is that this feature
WAS first defined for COBOL in the '70s (I think, certainly by the '80s) but
is only now getting into the Standard.

OO:
  Well, you said it - look at C versus C++.  The WHOLE point that J4 and WG4
made was that they did NOT want the language divided into two languages.
Personally, (and I have some friends who HATE me for this) I wouldn't mind a
BIT if OO were made optional.  Given the lack of "truly" portable class
libraries,  I question the portability of applications that use this feature
(for the foreseeable future).  I used to follow "CORBA" - but have yet to be
convinced that "portable" stuff for the COBOL language to interface with is
there now.  If you gave me the choice of having ONE feature added to the
"optional" list, this would be it.  On the other hand, it is the MOST
"publicized" selling-point for the "new COBOL" - so I don't see any real
chance of
this happening.

   ***

Words "reserved in context"
  Actually, the intrinsic function module first introduced this (when
"FUNCTION" wasn't a reserved word - but acted like one MOST of the time). The
correction amendment ('91) reversed this, but it COULD have been "reserved in
context" all along.
  One of the complaints that COBOL has had from "outsiders" is the number of
reserved words that it has.  This isn't just a "theoretical" complaint but is
a complaint from existing programmers who have tried "upgrading" their source
code from one standard to the next - only to find that their data-names and
procedure-names have become "reserved".  This new feature is an attempt to
minimize this problem.  It is thought that it doesn't matter MUCH how much
work it takes for the compiler vendors - as long as life is "easier" for the
programmers.  (My words, not those of J4)

  ***

Publishing "rationales" is not something that the ANSI/ISO rules encourage
(EXCEPT in the case of incompatible changes).  If you think that it takes too
long now to get a new Standard (and almost all of us do think that) it would
be FOREVER if J4 and WG4 had to agree to the wording of their "reasoning".
On the other hand, all J4 documents and minutes "are public" and if you have
any question on the rationale of a specific feature, you can send a note to
the J4 chair (or NCITS - the former X3) asking to see the proposal that added
a feature.  These do include a "justification" section, but I think you would
be disappointed if you ever read them. OTOH, WG4 stuff is NOT publicly
available, "don't ask, don't tell" is pretty much their way of working. (A
reason that I usually do NOT join the US delegation to WG4 meetings.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
