[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Y2K Bug found in ACCEPT FROM DATE

_32 messages · 14 participants · 1999-11_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Language features and syntax`](../topics.md#syntax) · [`Date and calendar processing`](../topics.md#dates)

---

### Y2K Bug found in ACCEPT FROM DATE

- **From:** PAL3000 <pduboisREMOVETHIS@enteract.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com>`

```
I don't know if this has been covered, or if a fix is out, but I ran
into the following problem using the runtimes:

RM/COBOL-85 Runtime (Ver 2.02.04) for Xenix 80386

and

MF V1.3 revision 0 build 10/10/252 G; 28691. Run Time System
AXULX/ZZ0/00000N

Both running under SCO Unix 5.

When you do an ACCEPT FROM DATE when the system date is greater than
02/28/2000 it will make the date one day greater.  IE: System date =
02/29/2000, ACCEPT returns 03/01/2000.  ANy dates prior to 02/29/2000
are fine.

I just patched my two systems that use these runtimes by checking the
date and subtracting one day if necessary.

Paul


--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

#### ↳ Re: Y2K Bug found in ACCEPT FROM DATE

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rZHW3.458$rG3.3660@client>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com>`

```
PAL3000 wrote in message <50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com>...
>I don't know if this has been covered, or if a fix is out, but I ran
>into the following problem using the runtimes:
…[13 more quoted lines elided]…
>Paul


Paul,

This is an SCO date function problem.  Did you test your operating system
date function outside of COBOL?  As root set the date to Feb. 28 23:59 2000
and watch the date roll over to March 1.  It is possible that your OS does
not have this problem but the versions of COBOL were linked on a system with
this problem.  If the problem does occur on your SCO system then SCO has
patches to the kernel.
The current release of RM/COBOL version 6.61.00 for SCO UNIX will not have
this problem.   See the SCO SLS UOD426C below:

Support Level Supplement (SLS) UOD426C corrects various date-related
problems reported on SCO UNIX System V/386 and SCO Open Server based
systems.  Note that this SLS _only_ applies to the products specified
below.  A separate SLS is needed for SCO XENIX systems; contact your SCO
supplier for more information.

This SLS is intended for the following warranted operating system
releases and affected warranted SCO products:

       SCO UNIX System V/386 Release 3.2 Operating System Version 4.2
       SCO Open Server Enterprise System Release 3.0
       SCO Open Server Network System Release 3.0
       SCO Open Desktop Release 3.0
       SCO Open Desktop Lite Release 3.0
       SCO FoxBASE+ 386 Release 2.1.2


  2.  The "leap year" problem

    Many commands and utilities do not display dates after February 28th,
    2000 correctly.  For example, running the following command to set the
    date to Tuesday February 29th, 2000:

               # date 0229101000

    will set the date to Tuesday March 1st, 2000 instead.

    The affected binaries and utilities do not correctly recognize the
    year 2000 as a leap year, hence a day is skipped over. The problem
    was found to be a bug in a version of an SCO development system library
    used to build the affected binaries and utilities.

    To correct this problem SLS UOD426C installs a binary patch, fix2000,
    which is run to find all affected binaries and utilities and patch
    in the corrected code.


You can also look in the SCO Technical Articles Search Center for the
problem about the mktime(S) funtion:

The SCO OpenServer Release 5.0.4 mktime(S) function does not correctly
calculate the leap year that occurs in the year 2000.

-
==============================================
Robert A. Heady                                   r.heady@liant.com

Liant Software Corp.
8911 Capital of Texas Hwy.
Austin, TX  78759
Phone:   (512) 343-1010
Fax:       (800) 835-0301
Home Page:  www.liant.com
==============================================
```

##### ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

- **From:** PAL3000 <pduboisREMOVETHIS@enteract.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client>`

```
Just wanted to add that these old runtimes must have been built to
correct for an operating system that didn't recognize 2000 as a leap
year.  Thus they coded the ACCEPT to add one day whenever the date
recvd from the OS was greater than 02/28/2000.

Still pretty amazing that they would build something like that in when
they were programming those runtimes, and also that they would
hardcode the assumption that the machine would always be broken.

Oh well, I am just glad I caught it before the customer.  I had always
used dates in January 2000 when testing with simulated system dates.
Then the other day I just entered 11/09/2000 and that is when I saw
the problem.

Paul
--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80fv3p$6p1$1@nntp6.atl.mindspring.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com>`

```
I'm not sure this is actually a "bug".
Theoretically, 2000 is NOT a leap year. But the calendars all show
it to be one. Personally I can only go by the calendar.

Has anyone tried Cobol-370's Function  current date?

PAL3000 <pduboisREMOVETHIS@enteract.com> wrote in message
news:HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com...
> Just wanted to add that these old runtimes must have been built to
> correct for an operating system that didn't recognize 2000 as a leap
…[15 more quoted lines elided]…
> words REMOVETHIS from my email address
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80fvtu$hu7$1@nntp2.atl.mindspring.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net>`

```
"Theoretically" 2000 *is* a leap year!  (See the rules about divisible by 100
*and* divisible by 400).

Yes, all the IBM mainframe COBOL products handle this correctly.  (Actually,
if you are still running VS COBOL II under VSE *only* there was a problem.
However, there is a fix available for that - and VS COBOL II is *not*
supported under VSE in 2000 anyway.)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 5)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80ie6q$md4$1@nntp3.atl.mindspring.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net>`

```
Well, I've talked to plenty of programmers, and they are split roughly
50/50.

Personally I don't care whether 200 is a leap year on not, except in the
case
of coding.

But as 1Kb=1024 bytes, it seems that Y2K means the year 2024 - not 2000!

And....I was alarmed when I found my (world wide company) client had
considered my suggested fix to Y2K - go to hex dates - so next year would
be 199A - seems clear enough to me !


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:80fvtu$hu7$1@nntp2.atl.mindspring.net...
> "Theoretically" 2000 *is* a leap year!  (See the rules about divisible by
100
> *and* divisible by 400).
>
> Yes, all the IBM mainframe COBOL products handle this correctly.
(Actually,
> if you are still running VS COBOL II under VSE *only* there was a problem.
> However, there is a fix available for that - and VS COBOL II is *not*
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wN3X3.10271$uk.79266@news3.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```
Unbeliever wrote:
>
>And....I was alarmed when I found my (world wide company) client had
>considered my suggested fix to Y2K - go to hex dates - so next year would
>be 199A - seems clear enough to me !

Not quite: 2000 base 10 = 7D0 base 16. :-)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383165FF.40E464FC@NOSPAMhome.com>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <wN3X3.10271$uk.79266@news3.mia>`

```
Unbeliever wrote:
>
>And....I was alarmed when I found my (world wide company) client had
>considered my suggested fix to Y2K - go to hex dates - so next year would
>be 199A - seems clear enough to me !

When programmers use different number base systems for dates, users get
confused - they say we think Christmas is Halloween.   (Dec 25 = Oct 31)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382ccb9f_3@news3.prserv.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```
> But as 1Kb=1024 bytes, it seems that Y2K means the year 2024 - not 2000!

You are correct, we should all say Y2k instead. The "k" means 1000 like in
km (kilometer) and kg (kilogram).

But many programmers work with CAPS LOCK ON ALL THE TIME.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1OlX3.3280$B_1.141533@typhoon01.swbell.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```

Unbeliever <popsider@ix.netcom.com
> wrote in message news:80ie6q$md4$1@nntp3.atl.mindspring.net...

> Well, I've talked to plenty of programmers, and they are split
roughly
> 50/50.
>
According to a recent survey, 40% of Texas' High School Biology
teachers believe dinosaurs were contemporaneous with humans.
Just shows you 40% (or, in your case, 50%) can be, er, confused.

The rules for leap year were set in the 12th century. But I could
be confused about that.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z5mX3.17964$z26.165755@news4.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net>`

```
Jerry P wrote:
>
>According to a recent survey, 40% of Texas' High School Biology
>teachers believe dinosaurs were contemporaneous with humans.
>Just shows you 40% (or, in your case, 50%) can be, er, confused.

They're only confused if God was too stupid to know what He was talking
about when He instructed Moses what to write in Genesis. ;-)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382df4f9_3@news3.prserv.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia>`

```

Judson McClendon <judmc123@bellsouth.net> wrote in message
news:Z5mX3.17964$z26.165755@news4.mia...
> Jerry P wrote:
> >
…[5 more quoted lines elided]…
> about when He instructed Moses what to write in Genesis. ;-)

Judson, please explain why you think the Christian god was too stupid...
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 9)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qCCX3.4240$B_1.188929@typhoon01.swbell.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net>`

```

Leif Svalgaard <lsvalg@ibm.net

> Judson, please explain why you think the Christian god was too
stupid...
>
Me too. I didn't think the Pharonic calendar system had a Y2K problem
with leap years.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aTIX3.23620$Hk.201486@news1.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net>`

```
Leif Svalgaard wrote:
>Judson McClendon wrote:
>> Jerry P wrote:
…[8 more quoted lines elided]…
>Judson, please explain why you think the Christian god was too stupid...

I didn't say that, of course.  My educational background is in the
sciences (physics & math).  Until I was perhaps 30 years old, I too
believed in the theory of evolution.  But there are a number of facts
I have learned that kick the theory of evolution in the teeth.  This
is off topic, and I don't want to start a long discussion here, but I
will point out a couple of facts, both of which point to a history of
Earth very different from the one commonly accepted by the secular
world.  It is, in fact, very consistent with Biblical history.

One fact that is literally ignored and even suppressed by proponents
of evolution, is that there are a number of sites where clearly human
fossils and footprints have been found right alongside clear dinosaur
footprints and fossils.  In one site alone in Texas, there are over
100 places where human footprints are found within inches of dinosaur
footprints, and many of them overlap.  These human footprints would
never be challenged, if they were found somewhere else.  But detailed
stress analysis of the human footprints show them to be absolutely
human, right down to the shifting of the weight during the stride.
Sometimes dinosaur footprints overlap human footprints, and vice-
versa.  In one case, there is a set of dinosaur footprints, and
inside are *three* sets of human footprints, an adult and two
children, where the humans walked right in the dinosaur's footprints.
In a site a few miles away along the same river, some human artifacts
(a metal hammer with handle, etc.) and a fossilized human finger,
were discovered in the same strata, very near dinosaur fossils.  The
finger is so well fossilized that medical forensic experts determined
it was from a human female, and could tell which finger it was, and
from which hand.  These finds are *not* frauds.  The digging was
witnessed by a number of well credentialed people not associated with
the dig.  Some of them don't believe it, even after seeing it.  They
will not believe clear evidence that contradicts their preciously held
belief system, even though they admit it is not a fraud.

Another fact is that, if evolution occurred, then at some point non
living material spontaneously formed itself into a living organism.
In other words, dirt turned itself into a life form, a hypothetical
process called 'autogenesis'.  No matter how you slice it or dice it,
or try to place it far, far back in time, this *must* have happened,
or life was created by some intelligence from *outside* the universe.
There is no other way.  Years ago, before the science of cytology
knew nearly as much about the internal structure of cells, it seemed
somewhat credible that through some process we do not know, nonliving
matter might have undergone a transition into living matter.  But the
internal workings of a single cell are as complex as the whole world
economy, vast and complex beyond imagining.  And there are several
(five, as I remember), major processes that are *interdependent*.
None of the processes can function without the others.  In other
words, the first cell that came into existence had to have a number
of interdependent functions *all operational at the very beginning*.
The mere concept is so farfetched, so improbable, as to be absurd.
A tornado in a junk yard spontaneously building a 747 in flight is
peanuts by comparison.  These days, evolution proponents don't want
to discuss autogenisis.  It is so obviously impossible, they have
nothing to say, no idea how it could possibly happen, and are too
embarrassed to talk about it.

As science learns more and more about the universe, it is becoming
more and more obvious that the universe was 'designed' to support
human beings.  Just do some reading on the 'Anthropic Principle'.
The thing that really amuses me is that the scientists who are
coming up with this stuff are very uncomfortable with it, because
it challenges their carefully indoctrinated belief systems.  But
the data they themselves collect are so strong, they cannot deny
the evidence. :-)

Like I said, I don't want to get into a debate, I just listed these
things in an attempt to pique your curiosity and get you to examine
the facts.  A book you might want to read is "God: The Evidence" by
Patrick Glynn, ISBN 0761509410 (amazon.com has it for $15.40).  I
don't agree with all Glynn's conclusions, but he presents some very
formidable evidence.  He was an agnostic until the facts persuaded
him otherwise.

The question is: are you afraid to have your beliefs challenged by
the facts? :-)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 10)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80nvvk$34ue$1@newssvr04-int.news.prodigy.com>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia>`

```
Strayed a bit from the original question, haven't we?
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yziY3.29920$Hk.259904@news1.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <80nvvk$34ue$1@newssvr04-int.news.prodigy.com>`

```
Terry Heinze wrote:
>Strayed a bit from the original question, haven't we?

Just a 'wee' bit. :-)
```

###### ↳ ↳ ↳ Re: OT, beliefs and facts

_(reply depth: 10)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382f8bac_2@news3.prserv.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia>`

```

Judson McClendon <judmc123@bellsouth.net>
> Leif Svalgaard wrote:
> >Judson McClendon wrote:
…[6 more quoted lines elided]…
> the facts? :-)

You are right, this is not the place...
but I don't have beliefs getting in the way of facts.
```

###### ↳ ↳ ↳ Re: OT, beliefs and facts

_(reply depth: 11)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EC97FC10E180C1E3.2C4F35065FEC4448.205C76727F8501FF@lp.airnews.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <382f8bac_2@news3.prserv.net>`

```
On Sun, 14 Nov 1999 22:28:32 -0600, "Leif Svalgaard" <lsvalg@ibm.net>
enlightened us:

>
>Judson McClendon <judmc123@bellsouth.net>
…[13 more quoted lines elided]…
>

Just a question for Judson.  Would you accept the concept that God was
resposnsible for evolution?  That is, he created the process that
built the first living cell and let nature and time take its course.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

The only time the world beats a path to your door is if you're in the
bathroom.


Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: OT, beliefs and facts

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QFiY3.29972$Hk.260124@news1.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <382f8bac_2@news3.prserv.net> <EC97FC10E180C1E3.2C4F35065FEC4448.205C76727F8501FF@lp.airnews.net>`

```
SkippyPB wrote:
>
>Just a question for Judson.  Would you accept the concept that God was
>resposnsible for evolution?  That is, he created the process that
>built the first living cell and let nature and time take its course.

Of course, God 'could' have done that.  I can't accept that concept,
because it is in serious disagreement with the Bible. :-)

<detailed response by e-mail>
```

###### ↳ ↳ ↳ Re: OT, beliefs and facts

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KBiY3.29944$Hk.260026@news1.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <382f8bac_2@news3.prserv.net>`

```
Leif Svalgaard wrote:
>Judson McClendon <judmc123@bellsouth.net>
>> Leif Svalgaard wrote:
…[10 more quoted lines elided]…
>but I don't have beliefs getting in the way of facts.

I was really 'talking to the audience', rather than to you personally.
Since I don't know what your beliefs are, it would be silly for me to
debate them. :-)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 10)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OtMX3.4831$B_1.227329@typhoon01.swbell.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia>`

```

Judson McClendon <judmc123@bellsouth.net> wrote in message
news:aTIX3.23620$Hk.201486@news1.mia...

> I didn't say that, of course.  My educational background is in the
> sciences (physics & math).  Until I was perhaps 30 years old, I too
> believed in the theory of evolution.  But there are a number of
facts
> I have learned that kick the theory of evolution in the teeth.

1. The Theory of Evolution allows science to develop disease
resistant grains, treat disease, and put the entire biological
universe into a coherent, predictable, and manageable whole.
Special Creation does not.

2. Footprints: There is not an atom of independent
evidence of dinosaurs in Texas (or anywhere else) in the
last 60 million  years and not a scintilla of evidence of
humans in Texas (or anywhere else) before 50,000 years
ago. Throwing out a massive body of science and
compelling scholarship based on the equivalent of crop
circles is not the result of logical thought processes.

A talking squirrel told me the above, and that's good enough
for me.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v5jY3.30066$Hk.260618@news1.mia>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <OtMX3.4831$B_1.227329@typhoon01.swbell.net>`

```
Jerry P wrote:
>Judson McClendon wrote
>
…[8 more quoted lines elided]…
>Special Creation does not.

This is absolute hogwash, and you know it.  It is the understanding
of how organisms function *now* that provides that capability.  What
an organism might have been (if evolution were true) millions of
years ago has *nothing* to do with it.  Such a notion is absured, on
the face of it.

People are miraculously healed all the time.  I have seen it, I have
many friends who have been miraculously healed, and they can produce
medical records that prove it.  A godless viewpoint can't explain
that, but a belief in the Bible's explaination for creation does.
There is a truly vast amount of proof, but nonbelievers simply ignore
it, just as they ignore other evidence.  For if God is real, and He
created us, then we might be accountable to Him for our actions. That
is a very uncomfortable thought for non-believers, so they simply will
not consider that it is true.  That gives a very logical explaination
for non-believers bias against a God based viewpoint.  Now, expain
to me why I, a person educated in physical science, and many others
like me, believers in evolution, would reject it on fact?  There is
no reason, my friend.  What would I have gained by rejecting such
a broadly accepted theory?  I get roasted by people like you.  Don't
get me wrong, I am a firm believer in the scientific method, for
study and understanding of the physical universe.  But science can
not work when invalid priori assumptions are in place.  Nor can it
work when experimentation is impossible.  It is not possible, even
in pronciple, to prove that evolution did occur.  Even if evolution
were proved to be happening now, which it most definitely has not,
it would not prove that evolution was what caused us to get here.

>2. Footprints: There is not an atom of independent
>evidence of dinosaurs in Texas (or anywhere else) in the
…[4 more quoted lines elided]…
>circles is not the result of logical thought processes.

Again, straight hogwash.  I have *seen* the evidence, have you?  Are
you not aware that Copernicus "threw out a massive body of science"
that *worked*, and had worked, for 1400 years.  And as in evolution,
the previous body of science was based on an a priori *assumption*
that was false.  This 'massive body of science' was built up over
almost 200 years by people *who would not even consider* that God
may have created everything, as the Bible says.  Every single
interpretation was based on that a priori assumption.  No wonder it
sometimes seems to conflict.  It is not the evidence that conflicts
with the Bible, it is the millions of interpreations of the evidence
that were made with a viewpoint which completely eliminated God from
their thinking.  If you had bothered to actually read what people
like Darwin wrote, all of it, you would know this.

>A talking squirrel told me the above, and that's good enough
>for me.

That, I can believe. :-)
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 12)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y_pY3.317$Uh1.26266@typhoon01.swbell.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia> <382df4f9_3@news3.prserv.net> <aTIX3.23620$Hk.201486@news1.mia> <OtMX3.4831$B_1.227329@typhoon01.swbell.net> <v5jY3.30066$Hk.260618@news1.mia>`

```

Judson McClendon <judmc123@bellsouth.net

> >1. The Theory of Evolution allows science to develop disease
> >resistant grains... Special Creation does not.
>
> This is absolute hogwash, and you know it.
No I don't. Just this past week some scientists found a gene
responsible for high blood pressue and they can repair the
gene. What's even more amazing is that this repaired gene
is inheritable - meaning succeeding generations won't be
afflicted by high blood pressure.

>It is the understanding
> of how organisms function *now* that provides that capability.  What
> an organism might have been (if evolution were true) millions of
> years ago has *nothing* to do with it.
Sure it does.

> Such a notion is absured, on the face of it.
'Fraid not.


> People are miraculously healed all the time.  I have seen it, I have
> many friends who have been miraculously healed, and they can produce
> medical records that prove it.  A godless viewpoint can't explain
> that, but a belief in the Bible's explaination for creation does.
The Placebo Effect is found in both the faithful and the devout.
Ignorance of the mechanism is not proof of any alternative. "It must
have been a UFO! What else could it have been?"

> There is a truly vast amount of proof, but nonbelievers simply
ignore
> it, just as they ignore other evidence.
There is zip scientific proof.

>For if God is real, and He
> created us, then we might be accountable to Him for our actions.
That
> is a very uncomfortable thought for non-believers, so they simply
will
> not consider that it is true.
I can understand why someone would be uncomfortable with "if"
and "might be."

>That gives a very logical explaination  for non-believers bias
against
>a God based viewpoint.
I don't think so. It's more along the lines of practical experience.
Faith
does not, in fact, move mountains; bulldozers do.


>Now, expain
> to me why I, a person educated in physical science, and many others
> like me, believers in evolution, would reject it on fact?  There is
> no reason, my friend.  What would I have gained by rejecting such
> a broadly accepted theory?  I get roasted by people like you.
I can't explain your actions and I'm not trying to roast you - at
least I don't
think I am.

>Don't
> get me wrong, I am a firm believer in the scientific method, for
> study and understanding of the physical universe.  But science can
> not work when invalid priori assumptions are in place.  Nor can it
> work when experimentation is impossible.
Science can work on invalid prior assumptions (Reducto Ad
Absurdum) and the concepts of science in which experimentation
was (is) impossible are legion (Relativity, all non-Euclidian
mathematics, most of Cosmology and Astronomy, fusion).

>It is not possible, even
> in pronciple, to prove that evolution did occur.  Even if evolution
> were proved to be happening now, which it most definitely has not,
> it would not prove that evolution was what caused us to get here.
The first part of this paragraph is a tad confusing, but I agree that
physical and biological laws we now experience (gravity, for
example) does not mean that the universe acted the same
way in the past.

>
> >2. Footprints: There is not an atom of independent
…[7 more quoted lines elided]…
> Again, straight hogwash.  I have *seen* the evidence, have you?
So, who are you going to believe? The scientific community or your
own lying eyes? Besides, I'm a native Texan and neither I nor
anyone in my family (going back several generations) has seen
a dinosaur in the wild.

>Are
> you not aware that Copernicus "threw out a massive body of science"
> that *worked*, and had worked, for 1400 years. And as in evolution,
> the previous body of science was based on an a priori *assumption*
> that was false.
Sure. The heliocentric system worked. Copernicus found something
that worked better. Just as evolution explains the universe better
than
special creation.

> This 'massive body of science' was built up over
> almost 200 years by people *who would not even consider* that God
> may have created everything, as the Bible says.
Oh, that's not so. Lot's of very religious people adhere to evolution.
For example. me.

>Every single
> interpretation was based on that a priori assumption.  No wonder it
…[4 more quoted lines elided]…
> like Darwin wrote, all of it, you would know this.
I suggest there are more 'interpretations' of what God meant than
there are of the tenets of evolution. I have read Darwin. Many of his
conjectures have proven false (Use/Disuse theory, for example),
but his work was a wonderful first approximation.


I'll let you have the last word.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 8)_

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80nnkn$2qo_002@news.netdirect.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <1OlX3.3280$B_1.141533@typhoon01.swbell.net> <Z5mX3.17964$z26.165755@news4.mia>`

```
In article <Z5mX3.17964$z26.165755@news4.mia>,
   "Judson McClendon" <judmc123@bellsouth.net> wrote:
+Jerry P wrote:
+>
+>According to a recent survey, 40% of Texas' High School Biology
+>teachers believe dinosaurs were contemporaneous with humans.
+>Just shows you 40% (or, in your case, 50%) can be, er, confused.
+
+They're only confused if God was too stupid to know what He was talking
+about when He instructed Moses what to write in Genesis. ;-)

Where does Genesis mention dinosaurs?
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80ikma$j6u$1@aklobs.kc.net.nz>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```
: Well, I've talked to plenty of programmers, and they are split roughly
: 50/50.

It seems that Jan 1 will be the least of the problems next year
then.

: Personally I don't care whether 200 is a leap year on not, except in the
: case
: of coding.

: But as 1Kb=1024 bytes, it seems that Y2K means the year 2024 - not 2000!

Phew, that means there will not be any problems for another 24
years then.  Not.

: And....I was alarmed when I found my (world wide company) client had
: considered my suggested fix to Y2K - go to hex dates - so next year would
: be 199A - seems clear enough to me !

Just trying to untangle this sequence, as far as I can determine
it was:

      You suggested using 199A to your client.
      The client considered this suggestion.
      You became alarmed that they had considered it.

Quite right too, they should have dismissed it out of hand.  After
all, what happens after 199F and how do you get the software to
make this rollover ?
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z5dX3.84$s87.3007@dfiatx1-snr1.gtei.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```
Unbeliever wrote in message <80ie6q$md4$1@nntp3.atl.mindspring.net>...
>Personally I don't care whether 200 is a leap year on not, except in the
>case
…[3 more quoted lines elided]…
>


Maybe you meant Y2K = 2048?

MCM
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 7)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80k212$po1$1@nntp5.atl.mindspring.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net> <z5dX3.84$s87.3007@dfiatx1-snr1.gtei.net>`

```
This is the last time I mis-type a flippant comment!

Michael Mattias <michael.mattias@gte.net> wrote in message
news:z5dX3.84$s87.3007@dfiatx1-snr1.gtei.net...
> Unbeliever wrote in message <80ie6q$md4$1@nntp3.atl.mindspring.net>...
> >Personally I don't care whether 200 is a leap year on not, except in the
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80nnhb$2qo_001@news.netdirect.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <80fvtu$hu7$1@nntp2.atl.mindspring.net> <80ie6q$md4$1@nntp3.atl.mindspring.net>`

```
In article <80ie6q$md4$1@nntp3.atl.mindspring.net>,
   "Unbeliever" <popsider@ix.netcom.com> wrote:
+Well, I've talked to plenty of programmers, and they are split roughly
+50/50.

Then half of the ones you have talked to are wrong. :-)

+Personally I don't care whether 200 is a leap year on not, except in the
+case
+of coding.

200 was not. 2000 is.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382C22C3.FCDD74FD@NOSPAMhome.com>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net>`

```
Unbeliever wrote:
> 
> I'm not sure this is actually a "bug".
> Theoretically, 2000 is NOT a leap year. But the calendars all show
> it to be one. Personally I can only go by the calendar.

Whose theory?  

The currently accepted standards (the word theory doesn't make sense
here) are:

February contains 28 days
  UNLESS
      Year is evenly divisible by 4 then it has 29 days
         UNLESS
             Year is evenly divisible by 100 then it has 28 days
                 UNLESS 
                     Year is evenly divisible by 400 then it has 29 days

This should be good for a while.
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE (2000 IS a leap year)

_(reply depth: 4)_

- **From:** KHansen@screenio.com (Kevin J. Hansen)
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382c4c92.917128@gateway>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net>`

```
On Thu, 11 Nov 1999 19:45:36 -0700, "Unbeliever"
<popsider@ix.netcom.com> wrote:

>I'm not sure this is actually a "bug".
>Theoretically, 2000 is NOT a leap year. But the calendars all show
>it to be one. Personally I can only go by the calendar.


It is a commonly held misconception that 2000 is not a leap year, but
it is indeed a leap year.  The probable source of the misconception
lies in one of the rules of the Gregorian calendar.

Centuries divisible by 400 are leap years, but the others are not, so
1600 was a leap year, but 1700, 1800, and 1900 were NOT leap years.
Since 2000 is divisible by 400, it's a leap year.  Good thing we
didn't have computers back then or things would certainly have been a
mess!

We have an entertaining writeup on the complete rules for the
Gregorian calendar on our web site.  Take the link to Date Routines,
then the one at the bottom of the page to Calendars (Lighthearted).
You'll like it.

Kevin
Kevin Hansen
NORCOM - Developers of COBOL Programming Tools
http://www.screenio.com
```

###### ↳ ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE (2000 IS a leap year)

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382ccd4d_4@news3.prserv.net>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client> <HVMrOJ+4NF2b7wp65waTtQqLQobn@4ax.com> <80fv3p$6p1$1@nntp6.atl.mindspring.net> <382c4c92.917128@gateway>`

```
 History of the Calendar
The history of the calendar is fascinating.  The year of a planet is the
time it takes to orbit the Sun.  There are, however, different types of
year.  The time it takes the Earth to make one complete revolution with
respect to the distant stars is called the sidereal year (deriving from the
Latin word sidus, which meant constella-tion).  The sidereal year  (for
1950) is equal to 365.25636566 days or 31,558,149.993 seconds.
The time it takes for the Earth to return to the same point in its seasonal
cycle (which is what counts as far as the calendar is concerned) is called
the tropical year (after the Greek verb ???????, which means to turn).  The
tropical year is equal to 365.24219342 days or 31,556,925.511 seconds being
about 20 m 25 s shorter than the sidereal year.  The modern definition of a
second is the duration of 9,192,631,770 cycles of the radiation emitted by
the transition between the two hyperfine levels of the ground state of the
133Cs atom.
The tropical year is shorter than the sidereal year because of the
precession of the Earth's axis.  Precession is the motion of the axis of a
spinning top.  The Earth, like a top, has an equatorial bulge caused by the
centrifugal force of its rotation - the equatorial radius is 21.360 km
longer than the polar radius.  This bulge experiences a torque applied by
the gravitational influence of the Moon, the Sun, and the planets.  The
result is a precessional motion of the Earth's axis.  This was discovered by
Hipparchos about 150 BC.
The astronomical motions of the Earth and the Moon provide the basis for the
calendar - the subdivision of time into years, months, weeks, and days.  The
problem with these subdivisions is that they are based on phenomena that
have different periods - the revolution of the Earth around the Sun, the
revolution of the Moon around the Earth, and the rotation of the Earth.  The
periods are not commensurate: there are about 29.53 days in a lunar month,
4.22 weeks in a lunar month, and 365.24 days in a tropical year.  The
development of an accurate calendar has been a vexing problem since
antiquity (the name calendar derives from the Latin name kalendae for the
day of the new Moon, marking the beginning of the lunar month).
The Egyptians started their year in the latter part of July, when the Nile
began flooding the delta.  This was a big event, because the flooding
fertilized the delta.  The Egyptians divided the year into 12 months of 30
days each, giving a total of 360 days, to which they added an extra 5 days
at the end.  In the years around 4241 BC, the Egyptians noticed that the
rising of the Nile coincided with the day when the star Sirius (known as
Sothis) became again visible in the southern sky as seen from the capital
city of Memphis.
The Roman author Censorinus reported in his work De die natali (written in
238 AD and dedicated to his patron on his birthday) that in 139 AD the
rising of Sothis had occurred on July 20.  Now, the Egyptian year of 365
days was shorter by 0.242 day than the tropical year.  As a result, the
Egyptian calendar fell behind by 1 day in 4 years, making one full circle
(called the Sothis cycle) in 4x365 = 1,460 years.  Because the rising of
Sirius at Memphis and the beginning of flooding of the delta coincide only
once in 1,460 years, the Egyptians must have developed their calendar at one
of the following times: 1460 - 139 = 1321 BC, or 1321 + 1460 = 2781 BC, or
2781 + 1460 = 4241 BC...  This last date is the most probable, because the
calendar was already in use about 3000 BC.
The early Greeks adopted the Egyptian calendar, but in the fifth century BC,
the ?????????? was introduced, a period of 8 years in which each year
consisted of 6 lunar months of 30 days and 6 lunar months of 29 days, plus 1
lunar month of 30 days in 3 out of the 8 years.  The total number of days
was thus 2,922, giving an average of exactly 365.25 days per year.  The
Greeks set the beginning of the year at either the summer or winter solstice
(depending on which Greek city).
According to legend, Rome was founded by Romulus, its first king, on April
21, 753 BC.  At that time, the Romans had a calendar of 10 months (Martius
after Mars, the god of war, Aprilis, after Apru, the Etruscian goddess of
love, Maius, after Maia, eldest daughter of At-las, Junius, after Juno, wife
of Jupiter, Quin-tilis, Sextilis, September, October, November, and
December, the fifth month through the tenth month, of which four had 31 days
and the other six had 30 days.  In addition, there were two unnamed months
each in the winter.
The second king of Rome, Numa Pompilius (715-672 BC), is said to have named
the two winter months Ianuarius, after Janus, the two-faced god of gates,
and Febriarius, after Februa, the day of purification (the 15th) and to have
moved the beginning of the year to January 1.  In the reform recommended by
the Alexandrine astronomer Sosigenes and promulgated by Julius Caesar (100 -
44 BC), the year remained equal to 365.25 days, by having 365 days per year,
but adding to the month of February one day every fourth year (the leap
year).  In addition, the names Quintilis and Sextilis were changed to July
and August to honour Julius Caesar and his adopted son Augustus, and both
given a length of 31 days, together with December which also got 31 days.
Poor February was used as a source for extra days.  The first Julian year
began on January 1, 709 AUC (Ab Urbe Condita, i.e. since the founding of the
City), which translates into January 1, 45 BC.
In 526 AD, the Byzantine emperor Justinian asked a monk named Dionysius
Exiguus to change the calendar, reckoning time no longer from the founding
of Rome, but from the birth of Jesus Christ.  Dionysius figured that Jesus
had been born 753 years after the founding of Rome, apparently not knowing
that Herod, under whom Jesus was born, had died 749 years AUC.  Accordingly,
Jesus had to be born at least four years earlier than the good monk thought.
This error was discovered long after the Justinian Calendar had been adopted
by all the Christian nations of Europe.
To complicate things, some recent research indicates that Jesus Christ was
crucified on April 3, 33 AD.  Because He was 33 years old when He died, His
birth could be fixed at the end of the year 1 BC or at the beginning of the
year 1 AD (there is no year zero), four years after Herod had died.  At this
point we notice that there are discrepancies among the four gospels.  Most
important, the earliest gospel, Mark, says nothing about the birth of Christ
or about Herod, and neither does John.  It is thus possible that Dionysius
Exiguus made no mistake after all and that the birth of Christ took place at
the beginning of year 1, after the death of Herod.  In any case, we still
reckon the years from the fix provided by Dionysius Exiguus.  May his soul
rest in peace.
The number of days in a tropical year, as fixed by Julius Caesar's reform is
not quite exact - it is too large by 0.0078 days = 11.23 minutes.  By the
middle of the sixteenth century, the calendar was off by 11.7 days with
respect to the seasons.  Pope Gregory XIII ordered that the day after
Thursday, October 4, 1582, should be henceforth Friday, October 15, 1582; in
addition, from that year on, centennial years should not be leap years, even
though divisible by 4, unless divisible by 400.  In a 400-year cycle,
therefore, there would be (365x400) + 97 = 146097 days, equal to 365.242
days per year.
The Gregorian calendar was not the work of Gregory XIII (just as the Julian
calendar was not the work of Julius Caesar), but of the Jesuit priest
Christopher Clavius (after whom a prominent crater on the Moon is named) and
the Neapolitan astronomer and physician Luigi Lillio Ghiraldi.  The new
calendar was soon adopted in all Catholic countries, but only in 1752 in
England and the British Empire (by which time they were 12 days behind), and
only in 1918 in Russia, when that country was 13 days behind - which is why
the October Revolution was celebrated in November.  Lillian days, named
after Luigi Lillio, are simply days counted from the start of the Gregorian
reform.
In the same year, 1582, that Pope Gregory XIII promulgated his reform of the
calendar, the scholar Joseph Scaliger (1540-1609) devised the Julian period,
which he named after his father, Julius Caesar Scaliger.  The Julian period
is a period of 7,980 years that is obtained by multiplying three cycles, the
solar (28y), Metonic (19y), and indictio (15y) cycles: 28x19x15 = 7,980.
The solar cycle is a period of 28 years that derives from the fact that in
365 days there 52 weeks + 1/7 of a week.  In successive years, therefore,
the same day of the year will fall on the following day of the week.  Were
it not for leap years, in which the day of the week advances by two, the
cycle would be completed in 7 years.  It is instead completed in 7x4 = 28
years.  The Metonic cycle (discovered by the Greek astronomer Meton in the
fifth century BC) is a period of time that is divisible into both a whole
number of years and a whole number of lunar months; it is equal to 19 years
and includes 235 lunar months.  The indictio cycle is an ancient Egyptian
cycle, that beginning with January 1, 313 AD, was adopted by the emperor
Constantine as the Roman taxation cycle.
Scaliger adopted the three cycles not for astronomical reasons, but because
they were already used in Hellenistic, Roman, and Byzantine calendars.
Scaliger set the begin-ning of the current Julian period at January 1 at
12:00 noon Greenwich time, 4713 BC.  Reck-oning from noon is advantageous in
astronomy because most astronomical observations are made at night, meaning
that the observations from one night are not divided into separate days (at
least in Europe).  Days are counted in continuity from that date.  The
Julian period is important, because astronomers, even today, use it to
record the dates of celestial phenom-ena.  Thus January 1, 2000, at 00:00h,
will be Julian date (JD) 2,451,544.50.  Often the term Julian day is used to
mean the day count within a given year.  This is a confusing prac-tice, that
unfortunately has taken root, and is here to stay.
The seven day week dates from antiquity - it appears in Genesis, for
instance.  It may have originated from the observation that the lunar cycle,
29.5 days long, exhibits four phases - new Moon, half Moon, full Moon, half
Moon.  Each phase, therefore, lasting about 7 days.  In fact, in many
languages the word for week derives from the word for seven (e.g. ??????? in
Greek, septimana in Latin).  Noticing, in addition, that there were seven
heavenly bodies, the ancients related each body to a day of the week: Sun
for Sunday, Moon for Monday, Mars for Tuesday (dies Marties in Latin) where
the Norse god Tir takes the place of Mars in the Germanic languages, Mercury
for Wednesday (dies Mercurii), and so on.
```

##### ↳ ↳ Re: Y2K Bug found in ACCEPT FROM DATE

- **From:** PAL3000 <pduboisREMOVETHIS@enteract.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<=k4rOH9xhJwa0UOvapT9wQPov8wg@4ax.com>`
- **References:** `<50cqOC8H1ZSjcMGLq8S1NJdTRNyZ@4ax.com> <rZHW3.458$rG3.3660@client>`

```
Robert,

Thanks for your reply.  This is definetly a COBOL runtime problem on
my unix box.  I am using SCO Unix 3.2v5.0.4 which is ok with dates.

The system will correctly set the date whether I use a date prior to
to 02/29/2000 or after 02/28/2000.  This is when I use the unix date
command.

I also tested by setting the date and time to 02/28/2000 23:59 and it
rolled over to 02/29/2000 with no problem.

We are using these older run-times because we have custom code that
was never upgraded, and now we just need to upgrade for 8 digit dates.
So instead of moving up to a new runtime and having to upgrade every
file, we are staying with the old runtime and just upgrading files
with dates.

Your right! It seams that the runtime is adding one to the day, based
on it's assumption it is on a broken machine.    It's unbeleivable
that this would have been programmed into these older runtimes when
most of the software writtin for them wasn't Y2k compatible anyway.

Thanks for the heads up.  I will check the machines that I am
implementing this on to see if they have the system date problem or
not. 

Thanks,

Paul


On Thu, 11 Nov 1999 17:05:01 -0600, "Robert Heady" <r.heady@liant.com>
wrote:


>This is an SCO date function problem.  Did you test your operating system
>date function outside of COBOL?  As root set the date to Feb. 28 23:59 2000
…[62 more quoted lines elided]…
>

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
