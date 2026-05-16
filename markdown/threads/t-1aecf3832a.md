[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# You're invited to critique my new Cobol page I started

_170 messages · 36 participants · 2000-01 → 2000-02_

---

### You're invited to critique my new Cobol page I started

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net>`

```
It's at http://rmpcp.com/cobol.html - I'm not finished with it obviously
but I think it's off to a good start.
```

#### ↳ Re: You're invited to critique my new Cobol page I started

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3891A410.7DABF28B@neo.rr.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net>`

```
Being an ALC hacker there is nothing wrong with the judicious use
of GO TO.  However, if it is your wish to practice religion, then
sacrifice yourself upon the ALTER.

I don't know where you want to go with your COBOL page, but, if
you haven't already, check out alt.cobol (too) and you may get
some more ideas of what to do on your page/site.

"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> It's at http://rmpcp.com/cobol.html - I'm not finished with it obviously
> but I think it's off to a good start.
> 
<snip>
```

##### ↳ ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com>`

```
Cute pun. Understandable about GoTo's in assembler; unless they've
implemented a nice set of structured programming macros like I did for MIX
in college, you pretty much have to put your own structures together with
the various kinds of branches. Of course, Cobol is supposed to be a higher
level language with the control structures already included, so to me
GoTo's are not only unnecessary, they're unnecessarily dangerous. And of
course I have noticed over the years that various opinions about these
issues exist and sometimes even become fanatic. So I may as well come out
of the closet on this one (not that I was ever in it anyway) - yes, I am a
structured programming fanatic and proud of it. The GoTo stops here. :)
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<86tlo0$h33$1@bgtnsc02.worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net>`

```
However, Robert, you are a latter day saint. In 1960 go to was skip u.

Isn't it rewarding to have a reserved word list that grows like the
dictionary?

Bad at one time was considered unexceptable, now to some it means good. <G>

Warren Simmons
"Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
wrote in message
news:pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net...
> Cute pun. Understandable about GoTo's in assembler; unless they've
> implemented a nice set of structured programming macros like I did for
MIX
> in college, you pretty much have to put your own structures together with
> the various kinds of branches. Of course, Cobol is supposed to be a
higher
> level language with the control structures already included, so to me
> GoTo's are not only unnecessary, they're unnecessarily dangerous. And of
> course I have noticed over the years that various opinions about these
> issues exist and sometimes even become fanatic. So I may as well come out
> of the closet on this one (not that I was ever in it anyway) - yes, I am
a
> structured programming fanatic and proud of it. The GoTo stops here. :)
>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<86tj0t0vee@enews3.newsguy.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net>`

```
CoBOL (COmmon Business Oriented Language) programs have been around for 
years, so many of them are of very poor quality <snip>.

-- this is simply not true.  What do you define as quality?  Readability?
No, quality is software that works and I've seen no discernible difference
in quality between our old stuff and our new stuff.


As a result, there is no longer any excuse for new Cobol programs to be
written with GoTo's, Alter's, Perform Thru's, fall thru's, Next Sentence,
Sections, simple Exit statements, or periods on executable statements
themselves.

--- I've had no problems using (most) of these constructs and I've been
programming COBOL only for a year.


An example of poor design in Cobol itself is the ability of a paragraph or
section in the Procedure Division to be used in several ways, by fallthru,
GoTo, Perform, Perform Thru, etc. even several ways at once in the same
program from different points.

--- This is a good point.  I guess that's the purpose of a shop standard.
We use Perform Thru and many programs use GOTO.  But fallthru is generally
dangerours especially for the maintenance programmer.


 Some languages support some overlap between subroutines and functions but
those are still modularly invoked, while GoTo's may never come back and you
never know where without following the spaghetti.

--- This 'modularity' you describe is the result of quality code and
testing, not the language it's written in.



 At least when you look at a piece of code you can tell how it's executed
without having to look everywhere else.

--- Again, I don't feel that COBOL has anything to do with this.  Quality
code is good code.  I have seen plenty of total crap code in all
languages... most of it never makes production or does anything useful.  The
purpose of good code is to make the computer do what you want.  I kind of
think the page has a general negative attitude toward the language that many
of us make a good living off of.  Sometimes when we're greedy and selfish we
don't realize it, but being a programmer is a hell of a good job nomatter
what language.  But good page... I like the attack toward style.  Please
include some sort of style section!

Jeff
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<86tt3e$aku$1@bgtnsc03.worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com>`

```
Jeff's reply to this critique request covers a lot of  my reaction to the
material presented.
Presentation should be directed to attracting someone to the service
offered. Since it seems to be
to do it in COBOL, stressing the positives of the modern version of the
language will interest more
potential customers, and a stiring of the pot of the evolution.

Warren Simmons
"Jeff Baynard" <union27@macconnect.com> wrote in message
news:86tj0t0vee@enews3.newsguy.com...
> CoBOL (COmmon Business Oriented Language) programs have been around for
> years, so many of them are of very poor quality <snip>.
>
> -- this is simply not true.  What do you define as quality?  Readability?
> No, quality is software that works and I've seen no discernible
difference
> in quality between our old stuff and our new stuff.
>
…[10 more quoted lines elided]…
> An example of poor design in Cobol itself is the ability of a paragraph
or
> section in the Procedure Division to be used in several ways, by
fallthru,
> GoTo, Perform, Perform Thru, etc. even several ways at once in the same
> program from different points.
>
> --- This is a good point.  I guess that's the purpose of a shop standard.
> We use Perform Thru and many programs use GOTO.  But fallthru is
generally
> dangerours especially for the maintenance programmer.
>
>
>  Some languages support some overlap between subroutines and functions
but
> those are still modularly invoked, while GoTo's may never come back and
you
> never know where without following the spaghetti.
>
…[10 more quoted lines elided]…
> languages... most of it never makes production or does anything useful.
The
> purpose of good code is to make the computer do what you want.  I kind of
> think the page has a general negative attitude toward the language that
many
> of us make a good living off of.  Sometimes when we're greedy and selfish
we
> don't realize it, but being a programmer is a hell of a good job nomatter
> what language.  But good page... I like the attack toward style.  Please
> include some sort of style section!
>
> Jeff
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<8iGk4.4566$Sa2.171003@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com> <86tt3e$aku$1@bgtnsc03.worldnet.att.net>`

```
Good point, a more positive focus would help, even when the service offered
is cleanup of bad code.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<2iGk4.4565$Sa2.171003@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com>`

```
See replies below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389431B2.78FE267A@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com> <2iGk4.4565$Sa2.171003@newsread2.prod.itd.earthlink.net>`

```
Robert Pritchett wrote:
> CoBOL (COmmon Business Oriented Language) programs have been around
> for years, so many of them are of very poor quality <snip>.

To which   Steve Thompson wrote:
> This is simply not true.  What do you define as quality?
> Readability? No, quality is software that works and I've seen no
> discernible difference in quality between our old stuff and our new
> stuff.

And Robert responded :
> ===> I'm not saying that all old programs are of poor quality, just
> that there's a high correlation. There are lots of poorly written
> programs out there. And a quality program is not only correct in
> execution but also easy to read and understand so that it's easy to
> maintain.

If a program works and needs no changes then there really is no
quality problem.  Even if the code is truly awful, the design was good
enough to survive the test of time.

The issue arises when you are asked to make a change to a currently
running system.  You then need to carefully graft your extra features
into an existing framework.  If the original code is good then it is
relatively trivial to graft additional features and reuse some
sections of the code.  If it is poor then it requires great skill to
rework the existing process into a reliable changed program.

I have so many times seen modifications that work but are not the best
change that could be applied because the programmer did a minimal
change even if this approach was not the clearest.  This is entropy at
it best after about ten of these modifications you can't make a change
without breaking something and you have to totally rework the code
from scratch again.  Once again the choice to rework the program is
rarely done and programmers complain bitterly and suffer long testing
cycles with the 'monster program from hell'

Refactoring: The process of changing the program code without changing
the functionality.

Change:  Refactor the program first to make your change easy, then
implement the new functionality.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3895B35F.ED55DB41@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com> <2iGk4.4565$Sa2.171003@newsread2.prod.itd.earthlink.net> <389431B2.78FE267A@zip.com.au>`

```
Ken Foskey wrote:
> 
> The issue arises when you are asked to make a change to a currently
…[4 more quoted lines elided]…
> rework the existing process into a reliable changed program.

Of course if your business doesn't change at all, then they won't need
maintenance programmers.  Or anybody else for that matter, as more
adaptable competitors take over.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<ioMl4.342$w%5.12468@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com> <2iGk4.4565$Sa2.171003@newsread2.prod.itd.earthlink.net> <389431B2.78FE267A@zip.com.au>`

```
I'll point out your contradiction below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38980FDF.14063CB9@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <86tj0t0vee@enews3.newsguy.com> <2iGk4.4565$Sa2.171003@newsread2.prod.itd.earthlink.net> <389431B2.78FE267A@zip.com.au> <ioMl4.342$w%5.12468@newsread2.prod.itd.earthlink.net>`

```
"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> >If a program works and needs no changes then there really is no
…[5 more quoted lines elided]…
> program quality.

This is a derivation of if a branch falls in the forest and no one
notices, did the branch fall at all.

When was the last time you looked at a system that did not require any
changes?

I strongly agree with what you are saying though apart from that.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<#wgNZYia$GA.307@cpmsnbbsa02>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net>`

```
I use GO to frequently. GO TO ABEND-ROUTINE.

I have seen people use PERFORM ABEND-ROUTINE, but they are only spelling "GO
TO" incorrectly.

Even C has a GOTO.

If the coding is easier to understand with the use of a GO TO, why not use
it?

Robert M. Pritchett - RMP Consulting Partners LLC <EL.Bus.News@rmpcp.com>
wrote in message
news:pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net...
> Cute pun. Understandable about GoTo's in assembler; unless they've
> implemented a nice set of structured programming macros like I did for MIX
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02>`

```
If the code is "easier to understand" with a GoTo, that's because it's not
as cleanly structured as it should be, and/or it's those programmers who
never quite fully understood structured programming who would find it
"easier to understand". Which again supports my contention that old coding
standards in many shops, which are afraid to challenge the intelligence of
their staff, effectively reduce software quality to the lowest common
denominator.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<OTCvwZta$GA.255@cpmsnbbsa02>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net>`

```
Give me your solution:

GO TO ABEND-ROUTINE.
PERFORM ABEND-ROUTINE
or what?

Robert M. Pritchett - RMP Consulting Partners LLC <EL.Bus.News@rmpcp.com>
wrote in message
news:2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net...
> If the code is "easier to understand" with a GoTo, that's because it's not
> as cleanly structured as it should be, and/or it's those programmers who
> never quite fully understood structured programming who would find it
> "easier to understand".

Understanding Structured Programming is not the issue.
The problem is that you want support of the rules you feel are valid.
Anyone who disagrees with you doesn't understand.

You disapprove of limited use of explicit GO TO statements.
Isn't CONTINUE an implicit GO TO?
Don't we interpret IF, THEN, ELSE constructions with an implied GO TO?

>
> Robert M. Pritchett, President - RMP Consulting Partners LLC
…[15 more quoted lines elided]…
> >If the coding is easier to understand with the use of a GO TO, why not
use
> >it?
> >
>
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02>`

```
DennisHarley wrote in message ...
>Give me your solution:
>
>GO TO ABEND-ROUTINE.
>PERFORM ABEND-ROUTINE
>or what?

MOVE Big-number to return-code.
CLOSE (all open files)
GOBACK.

MCM
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<8722pv$pdb$1@nntp5.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net>`

```
For those not familiar with them "return-code" and "goback" are IBM
(mainframe primarily) extensions.  Some other COBOL compilers also support
one or both of these extensions.  The next Standard will add "goback" (but
not return-code) as "standard COBOL".  The next Standard also introduces a
new way of "communicating" a value during a STOP RUN (or GOBACK) - but
doesn't use the "return-code" methodology.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<#$FsM4#a$GA.315@cpmsnbbsa03>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net>`

```
I work in the OS/390 environment:

The purpose of an ABEND-ROUTINE is to get the attention of Computer
Operations.
A non-zero RETURN-CODE does not get the same attention as an ABEND.

We force ABENDs because of serious errors at run time.

This is normally done with a User ABEND-ROUTINE which calls ILBOABN0, or
CEEABEND.

The User ABEND is also used to invoke the ABEND options for dataset
disposition in the MVS OS/390 world.

The ABEND routine will, among other things:
Call DSNTIAR to format DB2 Error messages (if this is a DB2 error).
Display Error Messages.
Display Control Counts.
CALL the user abend program of your choice.

When running DB2 programs under IJKEFT01, ABENDS are trapped, and a return
code of 12 is issued.
I have seen this cause problems with dataset disposition.
The solution is to run under IJKEFT1B, which does not trap ABENDs.

Even with your solution you need a routine.
The situations which cause the need for a User ABEND are scattered
trroughout a program.
Are you going to going to CLOSE you files all over the place? Will you have
multiple GOBACKs?

Michael Mattias <michael.mattias@gte.net> wrote in message
news:TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net...
> DennisHarley wrote in message ...
> >Give me your solution:
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03>`

```
I hope you realize my proposed solution is somewhat idealistic. I, too, work
a lot in the IBM mainframe environment, where the Second Coming would not
get the attention of the operators unless it's also accompanied by an abend.

However, most mainframe sites I've worked at have a program which does
nothing but abend, allowing you to set that up as a separate job step,
trigger it based on condition code, and terminate the current (offending)
program in an "orderly" fashion.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38961CF0.9A636456@neo.rr.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net>`

```
I could stay out of this no longer.

<Soapbox>
If you are going to program in CICS, then you will need to use
GOTO if you want to make your programs run as quickly as
possible.  Perform... perform... perform etc. leads to a lot of
code that has to be backed out of in order to get into and out of
CICS for the next I/O with the USER's terminal (assuming you are
doing Pseudo conversational code).  Now, all of this is based on
my not having done any CICS COBOL coding since CICS 1.7.  And,
given the EXEC command expansion, as I recall, there is no way
around it doing GOTO.  Performing routines would mean having to
write restrictions into how one could use the EXEC commands for
dealing with AID processing (just to name one).

Next, in the area of ABENDs.  Orderly cleanup of files is done by
OS/390 (or good ol' MVS) during ABEND processing.  The only way
this does NOT get done is if you were somehow able to FREEMAIN
the DEB associated with that file (or somehow over-write that
storage).  This is where DECLARATIVES come into play within COBOL
- to deal with unusual or ERROR (ABEND) situations/conditions. 
And, since I don't have the latest IBM COBOL-II/COBOL-LE IMS-DB/2
manuals in front of me, I can't tell you for sure what
features/functions exist within the DECLARATIVE sections for
cleaning up a database.  BUT, to get to DEB storage, you have to
somehow get into SUPERVISOR state and/or KEY0/5.  If you were
able to do this, you have managed to find a security hole, or,
buggy system level software.  If you happen to clobber your
DCB/ACB, the system will still get the file closed (in the case
of VSAM, you may have a corrupted Index, but, you'd have done
that one to yourself anyway).

If one is doing XMEM calls for database I/O or other services
(via CALLs to external routines), then one must have an RTM exit
in place to make sure of proper cleanup (even if you exit your
program nicely, the service provider may HAVE to know you went
away in order to free storage up in (E)CSA/(E)SQA reserved for
your Address space, or, "non-releasable" storage in the (E)LSQA.

Given this, one could call an ALC program to issue whatever ABEND
you'd like (including the one's that IBM says are NO NOs -
although some x22's do get special treatment that you may not
want, come to think of it).  The point is, the I/O and XMEM
control blocks would get properly cleaned up (the XMEM part, if
and only if the storage was GETMAINed correctly).

Ok, back to the original religious argument.  GOTO (within COBOL)
is one of those things which can be used to make the code more
readable.  PERFORM is one of those things that can be used to
make code less readable.  Again, as I said in a much earlier post
on a.c.c., this is one topic that starts religious wars.  And if
you really want a Jihad, let's talk about ALTER (which as I
recall was written out of the language - THANK YOU! -- Even in
ALC I really try to avoid self-altering/modifying code - makes
reading a dump at 0400 much easier, and with 2GB of memory these
days, as opposed to 8KB of memory on the whole machine, why drive
yourself nuts?).

The idea of structured code was to make it readable and
maintainable.  To flatly say, NO GO TO may be used is to build a
house and say that you can't use a philips screw-driver (I
specifically avoided the hammer routine :-) ).  You can drive a
philips screw with a hammer, or, you can use a small straight
blade screwdriver -- but it sometimes takes alot of strength to
keep from stripping the head of the screw.  The similarity in
COBOL is this:  A GO TO used for clarity makes convoluted PERFORM
logic easier to read.

NOW, all that said, the availability of "END-xxx" (e.g., END-IF)
has obviated one of the reasons that I would use a GO TO.  But,
still, if that GO TO would make the code clearer, I'd use it in a
heartbeat.

<\Soapbox>

Michael Mattias wrote:
> 
> I hope you realize my proposed solution is somewhat idealistic. I, too, work
…[6 more quoted lines elided]…
> program in an "orderly" fashion.
<snip>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3896D22B.7399CC3E@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com>`

```
Steve Thompson on his soapbox wrote:
> 
> Ok, back to the original religious argument.  GOTO (within COBOL)
…[9 more quoted lines elided]…
> yourself nuts?).

This religious war is what this group is really about :-}

Firstly I don't strongly disagree with what you have said.  In some
instances a well placed goto makes life easier.  The problem is
deciding when this is the time.  I prefer to ban them, if you come up
with a compelling argument I will accept it.

Is your argument compelling?  No.

When I was doing CICS (and listening to Frank Zappa).  My screens were
validated all fields and the errors marked in read for the operator to
clean up.  One pass of the data, no escaping half done.

The issue with multiple performs is just no really an issue.  As
pointed out the compiler can optimize them away and as I have said
before efficiency at such a low level is rarely an issue. Unless it is
run about once per second or maybe once per minute do not bother with
micro optimization.

Do the performs create a rats nest of a program.  Yes in some
instances they do but, just like your argument for goto, if you do it
well then this is not an issue.  For a CICS screen (validation) my
program would look like (using real names not field 1):

   validate-screen-1.
	perform validate-feild-1
        perform validate-field-2
        perform validate-field-3
        if field-1-ok and field-3-ok
             perform cross-validate-field-1-and-field3
        end-if
        ....

This gives a clear flow of the program and the procedures
automatically document the code. No comments required because the
performs tell you what is going on.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

PS:  Question.  A logical cupacino to the person who answers
correctly.

Why do I not imbed the cross-validate into validate field-3?
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<877e0u$u50$2@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com> <3896D22B.7399CC3E@zip.com.au>`

```
: Steve Thompson on his soapbox wrote:
:> 
:> Ok, back to the original religious argument.  GOTO (within COBOL)
:> is one of those things which can be used to make the code more
:> readable.  PERFORM is one of those things that can be used to
:> make code less readable.  Aga

Whether GO TO or PERFORM is 'more readable' is purely a function
of the reader.  If the programmer is looking at and writing GO TOs
in programs then he will see this as the 'more readable' form and
PERFORMs will confuse him.  and vice versa.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<dGMl4.377$w%5.3972@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com> <3896D22B.7399CC3E@zip.com.au> <877e0u$u50$2@aklobs.kc.net.nz>`

```
I disagree. It's partly true, different programmers are used to different
practices and this will influence what they understand easily, but in
structured programming there's also an inherent improvement in readability,
maintainability, and even developing it correctly in the first place, which
is the point. I think a programmer who fully understands both structured
(with and without GoTo's) and non-structured styles would find well
structured, GoTo-less programs easier to write and maintain.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<pxMl4.353$w%5.13013@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com> <3896D22B.7399CC3E@zip.com.au>`

```
To keep the validate-3 routine concerned only with field-3 and promote the
higher level cross dependency to the appropriate higher code level.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38965606.DC89CD48@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com>`

```
Steve Thompson wrote:
> 
> I could stay out of this no longer.
…[12 more quoted lines elided]…
> dealing with AID processing (just to name one).

Disagree completely. All my CICS (batch, too) programs are structured in
the manner Bob Pritchett (thank you, Bob!) described and contain no
GOTO's (shudder). Sounds at though you were coding HANDLE CONDITION
commands specifying paragraph names to be invoked when a certain
condition arose, e.g., NOTFND, QZERO, etc. That's a very old fashioned
way to do it. What I do is code RESP(field-name) in every command, then
check EIBRESP afterward. Everything is nice and clean that way, no
hopscotching around the program and repetitive HANDLE CONDITIONs when I
want different error logic for this command vs. the last one. As far as
citing a real world example in which structured COBOL source didn't
produce a performance hit, I converted a sister application's file
handler from Assembler to VS COBOL II (a dramatic increase of
everything, source, load module size, instruction paths, etc.). At the
time, 1993, it was linked to approx. 5 million times per day. I said
then if we were ever to see an example of taking a noticeable
performance hit from COBOL's overhead, this would be it. No problems
noted and it's linked to more than 20 million times/day currently (22
million today).

Re: backing out of the PERFORMs, I suspect you were working with OS/VS
COBOL back in your CICS 1.7 days. From VS COBOL II on, if you specify
OPTIMIZE when you compile, most of those PERFORMed routines are placed
inline, no backout required.

(snip)
> 
> If one is doing XMEM calls for database I/O or other services
…[4 more quoted lines elided]…
> your Address space, or, "non-releasable" storage in the (E)LSQA.

If "XMEM" means cross memory, I don't know how you'd ever do that from a
COBOL program. And how would a COBOL program ever diddle LSQA? Are these
"external routines" Assembler? If so, you have an Assembler cleanup job,
not COBOL.

(snip)

> Ok, back to the original religious argument.  GOTO (within COBOL)
> is one of those things which can be used to make the code more
> readable. 

This is more a matter of what one is used to, rather than a fact. I
certainly find structured source *much* easier to follow, but that's the
way I code.

As you mentioned, this kind of discussion sometimes degenerates into a
religious war. I don't want to do that and am happy to agree that we
have different opinions and we'll agree to disagree (the way grownups
are supposed to):-)

Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<lxMl4.352$w%5.13013@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03> <k8hl4.72$qH.5477@dfiatx1-snr1.gtei.net> <38961CF0.9A636456@neo.rr.com>`

```
Interesting, but I think there are remedies now that can bring us back into
agreement, see below:
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<moMl4.344$w%5.12468@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <TX_k4.2783$aZ4.52133@dfiatx1-snr1.gtei.net> <#$FsM4#a$GA.315@cpmsnbbsa03>`

```
Fine, make your program nicely structured, and at the end, if a fatal error
was detected, THEN call your abend routine.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3895AE78.88CC4854@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02>`

```


DennisHarley wrote:
> 
> Give me your solution:
…[3 more quoted lines elided]…
> or what?

I like GO TO ABEND-ROUTINE in the name of honesty, but I am aware that
some compilers do a pre-search for GO TO, and if they find it put out
less efficient code.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<DWpl4.514$qH.32509@dfiatx1-snr1.gtei.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <3895AE78.88CC4854@NOSPAMwebaccess.net>`

```
OK, I'll be the sucker who bites. I am as anal-retentive as anyone on the
topic of writing efficient code, but if you are GO[ing] TO an ABEND-ROUTINE,
why does efficiency matter?

MCM

Howard Brazee wrote in message <3895AE78.88CC4854@NOSPAMwebaccess.net>...
>
>
…[10 more quoted lines elided]…
>less efficient code.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3896EF71.2E9976E0@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <3895AE78.88CC4854@NOSPAMwebaccess.net> <DWpl4.514$qH.32509@dfiatx1-snr1.gtei.net>`

```
I have heard that some compilers look to see if there is a GO TO.  If there is,
then they use one optimizing technique for the whole program, otherwise they use
a different optimizing technique for the whole program.  It isn't the particular
GO TO which is optimized, it is the program.  I don't recall which compiler(s)
have this feature.

Michael Mattias wrote:

> OK, I'll be the sucker who bites. I am as anal-retentive as anyone on the
> topic of writing efficient code, but if you are GO[ing] TO an ABEND-ROUTINE,
…[17 more quoted lines elided]…
> >less efficient code.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<6qLl4.1026$zg2.28272@dfiatx1-snr1.gtei.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <3895AE78.88CC4854@NOSPAMwebaccess.net> <DWpl4.514$qH.32509@dfiatx1-snr1.gtei.net> <3896EF71.2E9976E0@NOSPAMwebaccess.net>`

```
Ok, good answer! Now I understand!

MCM


Howard Brazee wrote in message <3896EF71.2E9976E0@NOSPAMwebaccess.net>...
>I have heard that some compilers look to see if there is a GO TO.  If there
is,
>then they use one optimizing technique for the whole program, otherwise
they use
>a different optimizing technique for the whole program.  It isn't the
particular
>GO TO which is optimized, it is the program.

>
>Michael Mattias wrote:
>
>> OK, I'll be the sucker who bites. I am as anal-retentive as anyone on the
>> topic of writing efficient code, but if you are GO[ing] TO an
ABEND-ROUTINE,
>> why does efficiency matter?
>>
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000207231115.29352.00002512@ng-fk1.aol.com>`
- **References:** `<6qLl4.1026$zg2.28272@dfiatx1-snr1.gtei.net>`

```
>
>Ok, good answer! Now I understand!
>

Please, Michael, folks living here in CheeseLand are never sarcastic, unless,
of course, the topic is "DA BEARS!"
Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3896D10F.CDE4787E@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02>`

```
DennisHarley wrote:
> 
> Give me your solution:
…[4 more quoted lines elided]…
> 

Call abend-routine.

It places the call to the abend function in one module.  When you
migrate to windows you can log the error and send a kill program
message to yourself.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<#zjjj6Lb$GA.318@cpmsnbbsa03>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <3896D10F.CDE4787E@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au> wrote in message
news:3896D10F.CDE4787E@zip.com.au...
> DennisHarley wrote:
> >
…[9 more quoted lines elided]…
> It places the call to the abend function in one module.

Nice solution.

However, the systems I work on do not normally have a canned callable
module.
I could devote time to writing and implementing one, but experience tells me
that no one else will use it, and it would delay the delivery of the project
I am currenly working on.

The problem is not just ABENDing, but also displaying additional
information: KEY fields, File Status, record counts etc., which would aid in
the problem resolution process. While a common module with the necessary
flexibility could be written, there would also be the need for a message
formatting routine.

The solution would be:
PERFORM FORMAT-ABEND-MESSAGE
CALL ABEND-ROUTINE USING ABEND-MESSAGE-AREA.

> When you
> migrate to windows you can log the error and send a kill program
> message to yourself.

To be honest there isn't even a slight chance that the systems I work on
will be migrated to Windows.
Some of the places I have worked have multiple mainframes running the same
application to support the volume. GUI front ends using TCP/IP connections
to CICS are being developed, but the bulk of the processing is done in
batch.

> Thanks
> Ken Foskey
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000207230828.29352.00002510@ng-fk1.aol.com>`
- **References:** `<#zjjj6Lb$GA.318@cpmsnbbsa03>`

```
>However, the systems I work on do not normally have a canned callable
>module.
>I could devote time to writing and implementing one, but experience tells me
>that no one else will use it, and it would delay the delivery of the project
>I am currenly working on.

I assume, since you mention "mainframes" in another part of the message, that
you are talking about IBM OS/390.  The LE that is now "bundled" with that op
system assumes that exactly that kind of software asset will be developed (see
Exception Handling in the Migration Guides).  This is one place where the IBM
labs have found real, almost-immediate, and easily-found code reusability,
which is why they built it into Language Environment.  It is the classic "low
hanging fruit" of code reuse, and I suggest you copy the relevant pages of a
Migration Guide to a memo outlining your proposed handler and its development
cost.  You might just be selling your managers short - I was!


Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<joMl4.343$w%5.12468@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02>`

```
If you understood structured programming well enough you wouldn't have
these questions. See further below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<O$p1#HZb$GA.89@cpmsnbbsa04>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <joMl4.343$w%5.12468@newsread2.prod.itd.earthlink.net>`

```

Robert M. Pritchett - RMP Consulting Partners LLC <EL.Bus.News@rmpcp.com>
wrote in message
news:joMl4.343$w%5.12468@newsread2.prod.itd.earthlink.net...
> If you understood structured programming well enough you wouldn't have
> these questions. See further below.
…[17 more quoted lines elided]…
> ===> Neither. Set a flag if you have to and test it wherever appropriate
in
> the proper constructs and the proper levels. Then everything almost takes
> care of itself (since you have to include error handling code either way),
> and if you need to change how one error is handled without making the same
> change to related errors (or with making the same change to related errors
> but not others), it's much easier this way.

I've seen this done, and it creates a mess.
Instead of:
   PERFORM  ROUTINE-A
   PERFORM  ROUTINE-B
   PERFORM  ROUTINE-C
you get:
IF NOT FATAL-ERROR
   PERFORM  ROUTINE-A
   IF NOT FATAL-ERROR
       PERFORM  ROUTINE-B
       IF NOT FATAL-ERROR
           PERFORM  ROUTINE-C
       END-IF
   END-IF
END-IF.

Every major routine winds up testing the FATAL-ERROR condition. And
unfortunately, if the FATAL-ERROR condition is not tested when it should be,
you may trigger a system Abend which masks the true nature of the problem.

The bottom line is that when you dectect a fatal error, Abend immediately.

> >
> >Robert M. Pritchett - RMP Consulting Partners LLC <EL.Bus.News@rmpcp.com>
…[4 more quoted lines elided]…
> >> as cleanly structured as it should be, and/or it's those programmers
who
> >> never quite fully understood structured programming who would find it
> >> "easier to understand".
…[11 more quoted lines elided]…
> >

When we read programs we process the code in our head. We interpret what we
read. We follow the flow of the program.

When I see a CONTINUE, I have to establish the scope it is contained in, and
find the corresponding Scope Terminator. Processing continues after the
scope terminator.

I interpret the CONTINUE as a "GO TO END-EVALUATE", "GO TO END-SEARCH", "GO
TO END-IF", etc.
Even though there is no explicit GO TO involved, it is interpreted as a GO
TO.

The generic nature of the CONTINUE sometimes leads to confusion. It may have
been beneficial to have an unambiguous form which specified the terminator.

When in-line comments are supported, don't be surprised to see:

           CONTINUE  *> GO TO END-EVALUATE
or       CONTINUE  *>  END-EVALUATE

BTW: I use the GO TO for ABEND routines only, everthing else is GO TO-less.
I break a program down into small provable paragraphs, and let the OPTIMIZER
do its job.
My latest crusade is to get more people to use nested programs.
> >>
> >>
>
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87a126$k8o$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <joMl4.343$w%5.12468@newsread2.prod.itd.earthlink.net> <O$p1#HZb$GA.89@cpmsnbbsa04>`

```
In comp.lang.cobol DennisHarley <LegacyBlue@email.msn.com> wrote:

: When I see a CONTINUE, I have to establish the scope it is contained in, and
: find the corresponding Scope Terminator. Processing continues after the
: scope terminator.

: I interpret the CONTINUE as a "GO TO END-EVALUATE", "GO TO END-SEARCH", "GO
: TO END-IF", etc.
: Even though there is no explicit GO TO involved, it is interpreted as a GO
: TO.

Each and every WHEN in an EVALUATE execues the following code and
then _Processing_continues_after_the_scope_terminator_.  The 
CONTINUE is not a special case (except there is nothing to
actually do).  The CONTINUE is _NOT_ a 'GO TO END-EVALUATE' any
more than there is an implicit goto at the end of each and every
block under a WHEN.

If you 'interpret' it this way then, it seems, you are still
trying to handle the code as a mental 'flowchart' and don't
'get it' yet.

: The generic nature of the CONTINUE sometimes leads to confusion. It may have
: been beneficial to have an unambiguous form which specified the terminator.

If you are confused by CONTINUE then you could always try abusing
the NEXT SENTENCE with a movable full stop.


: When in-line comments are supported, don't be surprised to see:

:            CONTINUE  *> GO TO END-EVALUATE
: or       CONTINUE  *>  END-EVALUATE

I am seldom surprised by comments anymore, they are often either
useless (as above) of simply wrong.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<LL1m4.1281$Gi4.41810@newsread1.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <joMl4.343$w%5.12468@newsread2.prod.itd.earthlink.net> <O$p1#HZb$GA.89@cpmsnbbsa04>`

```
See below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000207231536.29352.00002514@ng-fk1.aol.com>`
- **References:** `<O$p1#HZb$GA.89@cpmsnbbsa04>`

```
>The bottom line is that when you dectect a fatal error, Abend immediately.
>

And what is your definition of "fatal-error".  The current strategy of the IBM
folks is to create exception handlers which will report, fix and/or isolate the
problem, and then resume processing without abending.  Abends need to be last
resort - and, at least in IBM shops, we are trying harder all the time not to
use it.


Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<unpkCXic$GA.265@cpmsnbbsa04>`
- **References:** `<O$p1#HZb$GA.89@cpmsnbbsa04> <20000207231536.29352.00002514@ng-fk1.aol.com>`

```
See Below:

Steve Newton <stevenln@aol.comnospam> wrote in message
news:20000207231536.29352.00002514@ng-fk1.aol.com...
> >The bottom line is that when you dectect a fatal error, Abend
immediately.
> >
>
> And what is your definition of "fatal-error".  The current strategy of the
IBM
> folks is to create exception handlers which will report, fix and/or
isolate the
> problem, and then resume processing without abending.  Abends need to be
last
> resort - and, at least in IBM shops, we are trying harder all the time not
to
> use it.

Fatal Errors could be:

DB2 Timestamp errors.

File Timestamp or version errors, where a system has multiple "master"
datasets which all have a version that must be in sync for processing.

File sequence, or duplicate key errors (including getting more that one row
from a DB2 select where one row is the maximum possible, if the data are
correct).

Missing required data (relational integrity).
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A03E14.D0AD6359@cusys.edu>`
- **References:** `<O$p1#HZb$GA.89@cpmsnbbsa04> <20000207231536.29352.00002514@ng-fk1.aol.com>`

```
But the primary requirement is to make sure that operators and users do not think
that a bad job ran OK.  Often this means ABEND.

Steve Newton wrote:

> >The bottom line is that when you dectect a fatal error, Abend immediately.
> >
…[8 more quoted lines elided]…
> Still the best
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Robert W. McAdams" <fambright@sigmais.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389B13CD.1709EDD3@sigmais.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02>`

```
DennisHarley wrote:

> Isn't CONTINUE an implicit GO TO?
> Don't we interpret IF, THEN, ELSE constructions with an implied GO TO?

Yes.  What's your point?

The problem with explicit GO TOs is that they require paragraph names to "go
to".  And every time you add a paragraph name, it forces a programmer who is
reading the program to spend time evaluating where and how the paragraph is
referenced.  Implicit GO TOs do not have this problem.


Bob
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<ubs0B1yb$GA.267@cpmsnbbsa02>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com>`

```
I have edit macros which make finding paragraph names and data names easier.


Robert W. McAdams <fambright@sigmais.com> wrote in message
news:389B13CD.1709EDD3@sigmais.com...
> DennisHarley wrote:
>
…[5 more quoted lines elided]…
> The problem with explicit GO TOs is that they require paragraph names to
"go
> to".  And every time you add a paragraph name, it forces a programmer who
is
> reading the program to spend time evaluating where and how the paragraph
is
> referenced.  Implicit GO TOs do not have this problem.

I have written edit macros which make finding paragraph names and data names
easier.
It takes about 5-10 seconds to determine where something is referenced.


>
>
> Bob
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87ff54$14o$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <ubs0B1yb$GA.267@cpmsnbbsa02>`

```
In comp.lang.cobol DennisHarley <LegacyBlue@email.msn.com> wrote:

:> > Isn't CONTINUE an implicit GO TO?
:> > Don't we interpret IF, THEN, ELSE constructions with an implied GO TO?
:>
:> Yes.  What's your point?
:>
:> The problem with explicit GO TOs is that they require paragraph names to
: "go
:> to".  And every time you add a paragraph name, it forces a programmer who
: is
:> reading the program to spend time evaluating where and how the paragraph
: is
:> referenced.  Implicit GO TOs do not have this problem.

: I have written edit macros which make finding paragraph names and data names
: easier.
: It takes about 5-10 seconds to determine where something is referenced.

Finding where things are referrenced is only a small part of
the problems associated with GO TOs and their labels.

Having explicit references to a label within a block of code
makes it more difficult and more error prone to reuse that
code elsewhere.  This is especially true where a GO TO is
only executed in exceptional circumstances.  This path may
not be followed during testing.

So if a block is copied for reuse and the GO TO is accidentally
overlooked (perhaps because it looks exactly like every other
GO TO 6440-EXIT instead of 6448-EXIT), then it is a bomb
waiting for some mug at 2am.  These type of problems are almost
impossible to find because complete loss of control from a rogue
GO TO may cause a diagnostic that is in a completely different
part of the program.

Judson has the solution, but it isn't a standard part of 
compiling and testing systems.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqLkm92b$GA.70@cpmsnbbsa04>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <ubs0B1yb$GA.267@cpmsnbbsa02> <87ff54$14o$1@aklobs.kc.net.nz>`

```
Richard,
I have posted my reply under topic "Verification of the scope of the GO TO".
We are getting too far off the initial topic.

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:87ff54$14o$1@aklobs.kc.net.nz...
> In comp.lang.cobol DennisHarley <LegacyBlue@email.msn.com> wrote:
>
> :> > Isn't CONTINUE an implicit GO TO?
> :> > Don't we interpret IF, THEN, ELSE constructions with an implied GO
TO?
> :>
> :> Yes.  What's your point?
> :>
> :> The problem with explicit GO TOs is that they require paragraph names
to
> : "go
> :> to".  And every time you add a paragraph name, it forces a programmer
who
> : is
> :> reading the program to spend time evaluating where and how the
paragraph
> : is
> :> referenced.  Implicit GO TOs do not have this problem.
>
> : I have written edit macros which make finding paragraph names and data
names
> : easier.
> : It takes about 5-10 seconds to determine where something is referenced.
…[26 more quoted lines elided]…
> -------------------------------------------------------------- */
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87frim$m2d$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com>`

```
Robert W. McAdams wrote in message <389B13CD.1709EDD3@sigmais.com>...
>DennisHarley wrote:
>
…[4 more quoted lines elided]…
>

No.  It is a no-op.  It does nothing.  Not go to anything, implied or
otherwise.   I can slide my eyes right over it knowing that if the condition
before it is true, absolutely nothing happens.  Program control does not
change in the slightest way.

That is *precisely* why it was added, as the "next sentence" IS an implied
go to.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<uH0Nt73b$GA.252@cpmsnbbsa02>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net>`

```

donald tees <donald@willmack.com> wrote in message
news:87frim$m2d$1@news.igs.net...
> Robert W. McAdams wrote in message <389B13CD.1709EDD3@sigmais.com>...
> >DennisHarley wrote:
…[8 more quoted lines elided]…
> otherwise.   I can slide my eyes right over it knowing that if the
condition
> before it is true, absolutely nothing happens.  Program control does not
> change in the slightest way.

You are correct. I was wrong.
The next word may trigger a transfer of control.  (i.e. WHEN in SEARCH, or
EVALUATE, or ELSE in IF)

> That is *precisely* why it was added, as the "next sentence" IS an implied
> go to.
>
Correct again.
>
>
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Todd Bueler <buell@nostuff.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389B8FF6.78E8AC8A@nostuff.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02>`

```
Is it just me or has this thread tuned into a BIG technical discussion?  What
does the technical intricacies of the COBOL language have to do with the
business aspects of Computer Consulting?  Take it to a technical COBOL newsgroup
please boys.

Todd Bueler
Toronto

DennisHarley wrote:

> donald tees <donald@willmack.com> wrote in message
> news:87frim$m2d$1@news.igs.net...
…[25 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87gaak$urp$1@nntp3.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02> <389B8FF6.78E8AC8A@nostuff.com>`

```
Todd,
  I wanted to send this to you via "private email" - but your spam protector
ID makes this impossible.

FYI - mostly this conversation HAS been moved to comp.lang.cobol.  (It is
SIGNIFICANTLY longer there.) I hadn't even noticed that some of the posts
were (still) going to alt.computer.consultants.

Believe me, we (many of us) are "tired" of the thread in c.l.c - but I
certainly don't see ANY purpose in it being in the alt.computer consultants
NG.

Sorry for any cross-posting problems that this thread has caused you.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-05T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<w83n4.801$Ba4.17662@news.swbell.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02> <389B8FF6.78E8AC8A@nostuff.com>`

```
So how come you're talking about computer consultants on a COBOL
language technical newsgroup?

Todd Bueler <buell@nostuff.com> wrote in message
news:389B8FF6.78E8AC8A@nostuff.com...
> Is it just me or has this thread tuned into a BIG technical
discussion?  What
> does the technical intricacies of the COBOL language have to do with
the
> business aspects of Computer Consulting?  Take it to a technical
COBOL newsgroup
> please boys.
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** Todd Bueler <buell@nostuff.com>
- **Date:** 2000-02-05T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389CD5D6.9734FC37@nostuff.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02> <389B8FF6.78E8AC8A@nostuff.com> <w83n4.801$Ba4.17662@news.swbell.net>`

```
Because this thread has been cross posted to alt.computer.consultants, or
didn't you see that?

Todd Bueler
Toronto

Jerry P wrote:

> So how come you're talking about computer consultants on a COBOL
> language technical newsgroup?
…[10 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<eGqn4.827$nF5.34025@news.swbell.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02> <389B8FF6.78E8AC8A@nostuff.com> <w83n4.801$Ba4.17662@news.swbell.net> <389CD5D6.9734FC37@nostuff.com>`

```
I saw it. I guess what I meant was if YOU wanted to talk to
CONSULTANTS, why did YOU post to a language group? And then complain
about (apparently) cross-posting?
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 13)_

- **From:** Todd Bueler <buell@nostuff.com>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389F55D0.528AC6D4@nostuff.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <OTCvwZta$GA.255@cpmsnbbsa02> <389B13CD.1709EDD3@sigmais.com> <87frim$m2d$1@news.igs.net> <uH0Nt73b$GA.252@cpmsnbbsa02> <389B8FF6.78E8AC8A@nostuff.com> <w83n4.801$Ba4.17662@news.swbell.net> <389CD5D6.9734FC37@nostuff.com> <eGqn4.827$nF5.34025@news.swbell.net>`

```
Well, because the people on the COBOL newsgroup are also cross-posting
to the Consulting newsgroup.

Todd Bueler
Toronto

Jerry P wrote:

> I saw it. I guess what I meant was if YOU wanted to talk to
> CONSULTANTS, why did YOU post to a language group? And then complain
> about (apparently) cross-posting?
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<CV3l4.1986$rC3.59488@news3.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net>`

```
Robert M. Pritchett - RMP Consulting Partners LLC wrote:
>If the code is "easier to understand" with a GoTo, that's because it's not
>as cleanly structured as it should be, and/or it's those programmers who
>never quite fully understood structured programming who would find it
>"easier to understand

I have seen lots of code that is easier to understand with GO TO.
Unless you have seen all the kinds of code and algorithms that must
be written, you are hardly in a position to make such sweeping and
blanket statements.  Any time someone says "this is never" or "this
is always" is showing a restricted viewpoint.  I would agree with
you that GO TO is generally not justified, and should be avoided the
majority of the time.  But how many structured languages can you
name that do not have statements to exit from the middle of a code
block?  Error conditions can sometimes demand it.  There is currently
no command in COBOL to do this.  We have had a number of long threads
on this issue, but there are certain kinds of code that can only be
made more complex and obfuscated by eliminating GO TO as an exit from
the middle of a paragraph.  Not because it is poorly structured, but
because of the functions the code is doing.  Curare is a deadly poison
that is fatal in very small doses.  In general, it is a good idea not
to inject curare into your bloodstream.  However, millions of people
go to hospitals all over the world and curare derivatives are injected
into their bloodstream in extremely small quantities to keep them from
going into shock on the operating table.  If the people who developed
this treatment had taken your exact viewpoint, a lot of people who are
walking around would be dead.  Just because something can be harmful
when misused, and even if it is generally to be avoided, does not mean
that it must always be avoided in every possible situation.  One of
the marks of real genius is looking at a situation where 'everybody
knows' that such and such is true or false, but they see anther view
where it isn't, that everybody else missing by being to fixed and
narrow in their viewpoint.  Always be very, very careful how you
select your dogmas. :-)
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<873vuj$2mg$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia>`

```
Judson McClendon wrote in message ...

>narrow in their viewpoint.  Always be very, very careful how you
>select your dogmas. :-)

Yes Judson.
<G>
;<)
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "David Olson" <dqolson@fastdial.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<s9b8srmr5io51@corp.supernews.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:CV3l4.1986$rC3.59488@news3.mia...
> I have seen lots of code that is easier to understand with GO TO.
> Unless you have seen all the kinds of code and algorithms that must
…[11 more quoted lines elided]…
> because of the functions the code is doing.

 -snipped lots of good stuff _


I agree that there is *nothing* inherently wrong with a forward GO TO. In
fact, using one can make code that it a whole lot more readable,
understandable, and maintainable. It can make a lot of sense to always
PERFORM a subroutine from the mainline, and then exit from the subroutine
with a GO TO the exit if it turns out you really don't want to be there!

As an example, I once found a piece of code in a program we inherited that
used a stupidly long and complex nested IF statement just to avoid a GO TO.
I posted that piece of code for my group with the comment..."If anyone in my
group does this...I'll make you eat the entire listing I find it in" <G>.

David
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<dPMl4.395$w%5.13898@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <s9b8srmr5io51@corp.supernews.com>`

```
See below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A159F5.B5DA858C@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <s9b8srmr5io51@corp.supernews.com>`

```
David Olson wrote:
> 
> 
…[11 more quoted lines elided]…
> entire listing I find it in" <G>.

I was looking at some code today and another approach struck me (I use
it all the time in C programming).

I have a data line with nine fields, I check each one in a subroutine
and return if there is an error.  This is the implied goto of the
error checking above.  The best bit is that the code can be safely
copied and at times broken up and reused.

How do we do the same thing in Cobol:  easy nested programs:

call nestedErrorCheck using some-data.

...  nestedErrorCheck ....

procedure division

if test-1-failed
   goback.
if test-2-failed
   goback
if test-3 failed
   goback.

This is just another approach to the problem.  I don't expect any
converts just documenting another approach.

As an aside there are reasons why this style of coding makes it easy
to introduce polymorphic OO programming, but that is another story.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3895BF99.A79C2E89@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia>`

```
Judson McClendon wrote:
> 

> I have seen lots of code that is easier to understand with GO TO.
> Unless you have seen all the kinds of code and algorithms that must
…[6 more quoted lines elided]…
> block?  Error conditions can sometimes demand it.  

When I write a new program, the only exits needed from the middle of a
paragraph are those going to an ABORT routine.  It is not hard to design
a program so that it doesn't use switches and it doesn't need GO TO
EXIT.  Once this technique is learned, it becomes first nature.

There are lots of ways to structure a program.  Some structures have GO
TO XXXX-EXIT statements in them.  Others do not need these.
```

###### ↳ ↳ ↳ SV: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<Knjl4.18598$in5.324969@news1.online.no>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net>`

```
Or simply GO TO 99.
Like

 nn-XXXXXX SECTION
*+---------------------------------------------
*!
*+----------------------------------------------
00.
      ......
      GO TO 99.
      .....

99.
       EXIT.



Howard Brazee <brazee@NOSPAMwebaccess.net> skrev i
meldingsnyheter:3895BF99.A79C2E89@NOSPAMwebaccess.net...

>
> There are lots of ways to structure a program.  Some structures have GO
> TO XXXX-EXIT statements in them.  Others do not need these.
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3895DDE2.C08392C1@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <Knjl4.18598$in5.324969@news1.online.no>`

```
I suppose that's a structure, but it is one which I abhor.  I have found
though that I don't have the ability to persuade people who like GOTO
EXIT to give that up unless I have the ability to force them to.  It's
just as well, as I also need the authority to allocate time to teach
them to do it right.  Replacing all GOTOs with switches is a cure worse
than the disease.

Bjorn Alvik wrote:
> 
> Or simply GO TO 99.
…[19 more quoted lines elided]…
> > TO XXXX-EXIT statements in them.  Others do not need these.
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<874rcq$eak$1@nntp5.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <Knjl4.18598$in5.324969@news1.online.no> <3895DDE2.C08392C1@NOSPAMwebaccess.net>`

```
This is time for my "usual plug" for the next revision where "EXIT
PARAGRAPH/EXIT SECTION" is added to the Standard (as they are already
supported as extensions in some existing compilers).
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<tWml4.5616$rC3.127664@news3.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <Knjl4.18598$in5.324969@news1.online.no> <3895DDE2.C08392C1@NOSPAMwebaccess.net> <874rcq$eak$1@nntp5.atl.mindspring.net>`

```
William M. Klein wrote:
>
>This is time for my "usual plug" for the next revision where "EXIT
>PARAGRAPH/EXIT SECTION" is added to the Standard (as they are already
>supported as extensions in some existing compilers).

Yes!
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<CWpl4.513$qH.32509@dfiatx1-snr1.gtei.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <Knjl4.18598$in5.324969@news1.online.no> <3895DDE2.C08392C1@NOSPAMwebaccess.net> <874rcq$eak$1@nntp5.atl.mindspring.net> <tWml4.5616$rC3.127664@news3.mia>`

```
Also, "EXIT PERFORM [CYCLE]". Yes! Yes! Yes!
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<pPMl4.397$w%5.13898@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <Knjl4.18598$in5.324969@news1.online.no> <3895DDE2.C08392C1@NOSPAMwebaccess.net> <874rcq$eak$1@nntp5.atl.mindspring.net>`

```
That might be tolerable, at least I'd much prefer it over GoTo's. Exit
Perform would probably be cleaner.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net>`

```
Right, and the go to exit technique is a trap, a maintenance nightmare
waiting to happen. Someone will eventually take advantage of the convenient
label or standard to add more goto's and/or labels.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<879vhn$4l9$1@nntp1.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net>`

```

Robert M. Pritchett - RMP Consulting Partners LLC <EL.Bus.News@rmpcp.com>
wrote in message news:pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net...
> Right, and the go to exit technique is a trap, a maintenance nightmare
> waiting to happen. Someone will eventually take advantage of the convenient
> label or standard to add more goto's and/or labels.
>

Which is why the new (next revision) "EXIT PARAGRAPH/SECTION" syntax is so
much bettiner (IMHO).  There is no "label" involved and, thus, no way for the
next programmer to use an exit paragraph name in any statement.

NOTE WELL:
  If your current "vendor of choice" doesn't already support this syntax
(from the draft revision), I really DO suggest that you go thru their
"enhancement request" procedures to get this added BEFORE they provide a full
20xx conforming standard.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<5sfm4.3484$pk.33948@news3.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net>`

```
Robert M. Pritchett - RMP Consulting Partners LLC wrote:
>Right, and the go to exit technique is a trap, a maintenance nightmare
>waiting to happen. Someone will eventually take advantage of the convenient
>label or standard to add more goto's and/or labels.

It is not a 'trap' if you impose two policies.

 1. Always use a code scanner that flags PERFORM THRU wrong exit,
    GO TO outside of the paragraph and unmatched paragraph/exit.

 2. Make it a firing offense if anybody uses a GO TO outside a
    paragraph on purpose, or places a program into production
    without running the code scanner on it first.

Believe me, that works.  Hopefully, EXIT PARAGRAPH will be in the
next standard, and we can eliminate this issue altogether.
```

###### ↳ ↳ ↳ SV: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<6Nfm4.21155$in5.373836@news1.online.no>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia>`

```
Hey, Judson
Agree with you.
By the way, do you have that kind of a scanner.
Or do you know where to get it?
Bjorn
Judson McClendon <judmc@bellsouth.net> skrev i
meldingsnyheter:5sfm4.3484$pk.33948@news3.mia...
> Robert M. Pritchett - RMP Consulting Partners LLC wrote:
> >Right, and the go to exit technique is a trap, a maintenance nightmare
> >waiting to happen. Someone will eventually take advantage of the
convenient
> >label or standard to add more goto's and/or labels.
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<XRfm4.3530$pk.34488@news3.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no>`

```
Bjorn Alvik wrote:
>Hey, Judson
>Agree with you.
>By the way, do you have that kind of a scanner.
>Or do you know where to get it?

Yes, I wrote my own a long time ago.  However, my particular scanner
is so tailored to my own coding style (it checks other things too,
such as missing and extra periods), that it would be of little value
to anyone with different coding standards.  They're actually not very
difficult to write. :-)
```

###### ↳ ↳ ↳ SV: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<R5gm4.21174$in5.374009@news1.online.no>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia>`

```
Thank you.
I supposed it was that way.
The reason I asked, is my searching for tools to scan Wang Cobol for certain
syntax, in order to be able to do some kind of refactoring, conversion etc.
I do think that I need to have a big COBOL parser to perform my tasks, at
least not by the current moment. And I really cannot afford much time on
writing my own.
Got an idea? After all, the topic should be of general interest, I think.
Bjorn
Judson McClendon <judmc@bellsouth.net> skrev i
meldingsnyheter:XRfm4.3530$pk.34488@news3.mia...
> Bjorn Alvik wrote:
> >Hey, Judson
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<Dngm4.336$45.7212@news2.rdc1.on.home.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no>`

```
Micro Focus Revolve is supposed to handle Wang COBOL, assuming you can get
it to the PC for analysis.

If all you want to do is find certain text strings then there are a zillion
utilities for looking for doing text searches including the 'FIND' utility
that ships with DOS, Windows, OS/2, etc. I tend to use GNU utilities since
they support regular expression. (http://www.gnu.org)

-- Karl Wagner


It's been too long since I've been on a Wang but there ought to be a USERAID
utility to do this.

"Bjorn Alvik" <bjorn.alvik@asp.no> wrote in message
news:R5gm4.21174$in5.374009@news1.online.no...
> Thank you.
> I supposed it was that way.
> The reason I asked, is my searching for tools to scan Wang Cobol for
certain
> syntax, in order to be able to do some kind of refactoring, conversion
etc.
> I do think that I need to have a big COBOL parser to perform my tasks, at
> least not by the current moment. And I really cannot afford much time on
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 13)_

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87c72a$h04$1@starburst.uk.insnet.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no> <Dngm4.336$45.7212@news2.rdc1.on.home.com>`

```
Oscar T. Grouch <dustbin@home.com> wrote in message
news:Dngm4.336$45.7212@news2.rdc1.on.home.com...
> Micro Focus Revolve is supposed to handle Wang COBOL, assuming you can get
> it to the PC for analysis.
>
> If all you want to do is find certain text strings then there are a
zillion
> utilities for looking for doing text searches including the 'FIND' utility
> that ships with DOS, Windows, OS/2, etc. I tend to use GNU utilities since
…[5 more quoted lines elided]…
> It's been too long since I've been on a Wang but there ought to be a
USERAID
> utility to do this.

We used SCANSRC for searching for strings in source on WANG.  You could have
multiple strings and multiple source libraries.  The only problems are that
this is case dependent as I remember and when one of the strings was found
in a source, then that source was ended and the next source was searched.
This was a batch process that produce a report at the end.

Alternatively there was FINDTEXT which would look for a single string in a
source library.  This could be case independent.

Rick

>
> "Bjorn Alvik" <bjorn.alvik@asp.no> wrote in message
…[7 more quoted lines elided]…
> > I do think that I need to have a big COBOL parser to perform my tasks,
at
> > least not by the current moment. And I really cannot afford much time on
> > writing my own.
> > Got an idea? After all, the topic should be of general interest, I
think.
> > Bjorn
> > Judson McClendon <judmc@bellsouth.net> skrev i
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol scanning tools for Wang VS

_(reply depth: 12)_

- **From:** einomoto@compuserve.com (Edmond J. Inomoto)
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00000103110052.OUI52.einomoto@compuserve.com>`
- **References:** `<3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no>`

```
Hello,

On February 03 2000, "Bjorn Alvik" <bjorn.alvik@asp.no> wrote:

> Thank you.
> I supposed it was that way.
…[6 more quoted lines elided]…
> think. Bjorn


We used Netron's Wang I-Tools for our Y2K remediation. They were a real
help, and we still use them for routine scans. Netron started on the
Wang VS but is now almost exclusively NT-based. If you ask, I'm sure
they'll be willing to bargain. They're located in Toronto, Ontario and
their web site is http://www.netron.com. HTH.


p.s. The date on this posting is probably wrong - my newsreader is
having a bad hair millenium.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<CMCm4.3147$Sx.56564@news4.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no>`

```
Bjorn Alvik wrote:
>I supposed it was that way.
>The reason I asked, is my searching for tools to scan Wang Cobol for certain
…[4 more quoted lines elided]…
>Got an idea? After all, the topic should be of general interest, I think.

I don't know your requirements, but for a simple PERFORM THRU/GO TO
checker, you don't need to completely parse the entire program.  In
my own personal coding standard I use paragraph numbers, which makes
this task much simpler, because a paragraph and its exit will always
have the same number.  You only need to check that each PERFORM has
a THRU with the same paragraph number, with '-EXIT' on the end of
the paragraph name.  Within a paragraph, remember the paragraph's
number, then check all GO TOs within to make sure they have the same
number.  Test the exit paragraph as well.  Also verify that all the
paragraph numbers are ascending with no duplicates.  With paragraph
numbers, this is all you need for simple PERFORM THRU/GO TO tests,
because the compiler will syntax any other problems, if you test for
these.

Without paragraph numbers, I would highly recommend using the form

    PERFORM THIS-PARAGRAPH
       THRU THIS-PARAGRAPH-EXIT.

This will permit you to test GO TOs within the paragraph without
having to build paragraph name tables in order to match them
with their exits and GO TOs within them.  If you do this, the logic
is pretty much the same, because if you have duplicate paragraph
names, the compiler will flag them.

I always assume the code is syntax free, which simplifies parsing
a bit, and you only need to look at the Procedure Division.  If
you eliminate comments and literals from the line before parsing
the line, you can depend on a space delimited "PERFORM" being an
actual command, and the next word following the paragraph name
must be "THRU" or "THROUGH", followed by the same paragraph name,
with "-EXIT" appended.  My code checker looks for improperly
indented code and missing/extra periods, etc.  Essentially, it
checks the indenting of the code against period placement, to
make sure they are in agreement.  This program has caught many
thousands of errors, hundreds of them in programs that had been
running for years, until the scanner was run against them.  It
is also useful to enforce certain coding style standards.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 13)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389B030A.DFB3DCF9@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no> <CMCm4.3147$Sx.56564@news4.mia>`

```
Judson McClendon wrote:

> I don't know your requirements, but for a simple PERFORM THRU/GO TO
> checker, you don't need to completely parse the entire program.

I highly recommend that if someone chooses to write programs with drop through
logic to write utilities to catch mistakes caused by this style, and to enforce
the standard that these utilities have to be used.

Or alternatively switch to a coding style where these checks are not necessary,
and enforce that style.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 13)_

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-02-05T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<LYXm4.22921$in5.403208@news1.online.no>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no> <CMCm4.3147$Sx.56564@news4.mia>`

```
Hi, again, Judson.
Of course I do not need a complete parser to perform my task. That was what
I meant, I forgot a "no" in my message, though.
But beside looking for Performs and impertinent branching, I also want to
find propriatary elements, like the "DISPLAY AND READ"-statement, by
example.
And a lot of more things.
Thanks,
Bjorn
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<oOom4.1408$Mk2.42679@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no>`

```
I've always wanted to write one and haven't had time. 
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 13)_

- **From:** lucien2@frontiernet.net (Lucien T. Elliott)
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87mkbh$8jm6$1@node17.cwnet.frontiernet.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no> <oOom4.1408$Mk2.42679@newsread2.prod.itd.earthlink.net>`

```
Careful Robert,
they can be terribly addictive!  just too much fun... ;^)


"Robert M. Pritchett - RMP Consulting Partners LLC"
<EL.Bus.News@rmpcp.com> wrote:

>I've always wanted to write one and haven't had time. 

>-- 

>Robert M. Pritchett, President - RMP Consulting Partners LLC
>http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA 
>"Quality means doing it right the first time!"
>Contractors: tired of hearing "W-2 only"? Join us and let us help you get
>that same contract on a 1099 as a self-employed independent contractor! 



Lucien T. Elliott
Warwick Information Technology
http://www.frontiernet.net/~lucien2
Just Slightly Behind the BLEEDING Edge
29 Hawthorn Ave
Warwick NY 10990 
914 986 5139
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389CD8D9.A72F1460@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia> <6Nfm4.21155$in5.373836@news1.online.no> <XRfm4.3530$pk.34488@news3.mia> <R5gm4.21174$in5.374009@news1.online.no>`

```
Bjorn Alvik wrote:
> 
> Thank you.
…[9 more quoted lines elided]…
> Bjorn

I thought it would be general interest as well.  It generated little
interest.  I have one that parses the syntax into keywords and
identifiers for you to analyse if you want.

What it is missing is the code to go down into the copybooks (I could
not figure a portable way to do this).  Then you can just put your
filters onto the keywords passed back.

The full source is available on my web page.  I have not had time to
go back to this project in a while.  I am waiting more inspiration.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<kOom4.1407$Mk2.42679@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3895BF99.A79C2E89@NOSPAMwebaccess.net> <pPMl4.396$w%5.13898@newsread2.prod.itd.earthlink.net> <5sfm4.3484$pk.33948@news3.mia>`

```
In a maintenance situation where the code is already like this, a scanner
can be useful to check for traps, but no NEW code should be written like
this, including code added during maintenance. With proper use of
structured programming, no more goto's should need to be added.
```

###### ↳ ↳ ↳ SV: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3S9l4.18045$in5.317914@news1.online.no>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia>`

```
Thank you for this, Judson.
I also think that we should  tell them that SECTIONing of programs is not at
all bad.
Bjorn

Judson McClendon <judmc@bellsouth.net> skrev i
meldingsnyheter:CV3l4.1986$rC3.59488@news3.mia...
> Robert M. Pritchett - RMP Consulting Partners LLC wrote:
> >If the code is "easier to understand" with a GoTo, that's because it's
not
> >as cleanly structured as it should be, and/or it's those programmers who
> >never quite fully understood structured programming who would find it
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** fmcduff@terraworld.net (F. George McDuffee)
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38953eb8.13680117@news.terraworld.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no>`

```
> <SNIP>
>> I have seen lots of code that is easier to understand with GO TO.
…[11 more quoted lines elided]…
>> the middle of a paragraph.  

Its been a while since I programmed in COBOL, but the GOTO
question is not just a COBOL problem.  In many ways it is like a
pair of Vise-Grips.  In most cases a mechanic or technicial will
never use a pair of Vise-Grips as they have the correct tool
available which can be used with much less risk to both the
fastener and mechanic/technician, there are however cases where
the only practible solution is a good pair of Vise-Grips and the
skilled mechanic/technician will recognize this.

So to for the skilled programmer.  In normal conditions
constructs other than GOTO are much the better choice,
never-the-less a GOTO is sometimes the correct choice.  However
just as the skillful mechanic avoids the use of Vise-Grips the
skillful programmer avoids the use of GOTO.

George
If Education is the answer, what was the question?
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389656E0.FAE525E0@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no> <38953eb8.13680117@news.terraworld.net>`

```
"F. George McDuffee" wrote:
> 
> > <SNIP>
…[5 more quoted lines elided]…
> skillful programmer avoids the use of GOTO.

Maybe I haven't encountered the right circumstances, but I haven't run
into a situation in which I wanted to use a GOTO, or thought it was a
better choice. This is usually a matter of concentrating on a top down
design.

Bill Lynch
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZdEl4.7761$qU.173233@news4.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no> <38953eb8.13680117@news.terraworld.net> <389656E0.FAE525E0@worldnet.att.net>`

```
William Lynch wrote:
>"F. George McDuffee" wrote:
>>
…[9 more quoted lines elided]…
>design.

The only cases I can think of where I would use GO TO, other than if
I were programming for optimum speed (rare), have to do with the kind
of program being written.  In many online programs I am familiar with,
there are many very long paragraphs consisting of many similar tests
or operations against a series of data fields.  There is no logical
point where it makes sense to break it down into smaller paragraphs,
unless you just break it up arbitrarily, which certainly does not add
clarity. :-)  Each successive test or operation can require the rest
of the paragraph to be skipped.  Top down design has no effect on this,
because the entire series of tests is logically a single block of code,
unless you break it down into single field tests, which would require
literally hundreds of extra paragraph names and Performs.  In such
cases, there is no way I have ever seen (I started a thread a while
back to ask for them), that is simpler and clearer than a GO TO EXIT,
unless you have an EXIT PARAGRAPH statement, which COBOL 85 does not
support.  Some of the methods suggested to avoid the GO TO EXIT were
preferred by some others, simply because they got rid of the 'dreaded
GO TO'.  But every single other method involved extra code, was to an
objective observer less clear, much less efficient, or a combination.
Not one of them was nearly as simple, clear and efficient as a GO TO
EXIT.  EXIT PARAGRAPH would eliminate the need for GO TO EXIT.

As an example of where GO TO might be used for ultimate speed, I once
wrote a p-code interpreter in COBOL (only language available).  This
was in a very frequently used utility program, and performance was a
premium, because the code would be executed hundreds to millions of
times in a single run.  The user supplied the 'source code' to the
program on each run, which was compiled into p-code.  I used GO TO
DEPENDING, instead of PERFORM, to call the appropriate routines for
the p-code opcodes, sort of like a threaded p-code, and at the end
of each routine I did a GO TO back to a common return point.  It was
structured, and in this case it was worth it for the performance gain.
I rarely do this kind of thing in COBOL, though.  In an assembly
version of the program for another machine, I compiled to machine code
on the fly.  It ran like blazes. :-)
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<877dk2$u50$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no> <38953eb8.13680117@news.terraworld.net> <389656E0.FAE525E0@worldnet.att.net> <ZdEl4.7761$qU.173233@news4.mia>`

```
Judson McClendon <judmc@bellsouth.net> wrote:

: The only cases I can think of where I would use GO TO, other than if
: I were programming for optimum speed (rare), have to do with the kind
: of program being written.  In many online programs I am familiar with,
: there are many very long paragraphs consisting of many similar tests
: or operations against a series of data fields.  There is no logical

I suspect that you have 'online' programs where all the fields are
keyed and then sent into the system as a complete block.  ie
quasi-interactive.

I have only written fully interactive field-by-field processing
where each field is accepted and checked and function keys can
be used by the user to control the flow.  In general I have a
(simpified) structure where:

           MOVE 1    TO Field-Number
            PERFORM Get-Fields
               UNTIL Field-Number > Field-Limit

           .....

        Get-Fields.

            IF ( Field-Number = 1 )    *> or use 88s or constants
                PERFORM Screen-IN      *> sets screen colour
                 DISPLAY Cust-Code  AT Screen-Pos(Cust-Field)
                 ACCEPT     "                "
                PERFORM Check-KeyStatus
                   check customer
            END-IF

            IF ( field-Number = Date-Field )
                etc


When the user is stepping through the fields normally the Field-Number
will step forward by one and then each block withing the paragraph 
will be executed in sequence.  If the user does a 'back field' then
one will be subtracted and the paragraph will recycle until it finds
the previous block.  On error the Field-Number will stay at the
same value and the field will be redone.  If the user exits then
a high value is set in the Field-Number.

This can be table driven and I have programs that will generate
this code from text file screen layouts.

There would be no advantage in using GO TO to jump out as it is
only in exceptions (error, back field, exit, etc) that the 
paragraph recycles.
```

###### ↳ ↳ ↳ Re: SV: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yxHl4.896$Fk.4158@news2.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no> <38953eb8.13680117@news.terraworld.net> <389656E0.FAE525E0@worldnet.att.net> <ZdEl4.7761$qU.173233@news4.mia> <877dk2$u50$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
>Judson McClendon wrote:
>: The only cases I can think of where I would use GO TO, other than if
…[7 more quoted lines elided]…
>quasi-interactive.

This is true.  On PC systems using interactive interface, I haven't
seen this pattern, or the need to use GO TO for this purpose.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<7PMl4.394$w%5.13898@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <3S9l4.18045$in5.317914@news1.online.no>`

```
Sections don't have to be bad, they just make it easier for programmers to
add multiple paragraphs in a section and then you have fallthrus and
inviting targets for goto's. Where sections are useful is as a transitional
tool for cleanups, in getting rid of perform thru's.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia>`

```
An exit in the middle of a loop is like the classic read until EOF problem.
Sure, Cobol only provides this kind of construct for such specific cases
e.g. at end and not at end clauses, invalid key and not invalid key, etc.
but you can still use the existing structures to implement the technique.
This is far preferable to using a GoTo which has so much potential to be
changed (by poor maintenance) to go anywhere and then you're out of
control. Even if you have to repeat a test by having an If inside which
duplicates some of the tests in the outer Perform, this is still preferable
to a GoTo.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<FOfm4.3524$pk.34355@news3.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net>`

```
Robert M. Pritchett - RMP Consulting Partners LLC wrote:
>An exit in the middle of a loop is like the classic read until EOF problem.
>Sure, Cobol only provides this kind of construct for such specific cases
…[6 more quoted lines elided]…
>to a GoTo.

You snipped the example in my message that doesn't match what you say.
Consider a program that contains many paragraphs like this, with
perhaps 30 to 60 sets of field validation tests, or other similar
operations, on a series of fields.  There is no logical point to
split the tests into groups.  The fields are each autonomous and
unique, they are of different sizes and types, so you can't subscript
them.  Please show us a way to code this without the GO TO that does
not require substantially more coding and is much less readable.
This example is not contrived, I can show you hundreds of programs at
my clients that must do these kind of tests.  Bear in mind that we had
a long thread on this a while back, and though there were some very
clever suggestions, not one of them was clearer or simpler than the
GO TO exit.  The only logical difference here between using GO TO EXIT
and EXIT PARAGRAPH is the GO TO EXIT presents the opportunity to
PERFORM THRU the wrong exit, and you can do a GO TO outside the
paragraph.  You address this with a simple code checker that flags
those errors.  With the code checker, the GO TO EXIT is just as safe as
the EXIT PARAGRAPH, and simpler and clearer than trying to do it with
hugely embedded IF/ELSE, or setting flags which are tested every time,
etc.  When coded, those look like abominations, and are hardly clearer
than GO TO EXIT. :-)

PARAGRAPH.
    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    <validate field>
    IF <error>
        GO TO PARAGRAPH-EXIT.

    ...
PARAGRAPH-EXIT.
    EXIT.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** shine98@my-deja.com
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87csi0$uol$1@nnrp1.deja.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia>`

```
I'm sure you know this but here is the "proper" way to do this, with no
"go to"'s and no switches (if you don't count ws-error-sw, er, I mean
msg):

PARAGRAPH.

    move spaces to ws-error-msg

    <validate field 1>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 1' to ws-error-msg
        end-if
    end-if

    <validate field 2>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 2' to ws-error-msg
        end-if
    end-if

    <validate field 3>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 3' to ws-error-msg
        end-if
    end-if

    <validate field 4>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 4' to ws-error-msg
        end-if
    end-if

    <validate field 5>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 5' to ws-error-msg
        end-if
    end-if

    <validate field 6>
    IF <error>
        if ws-error-msg not = spaces
            move 'error message 6' to ws-error-msg
        end-if
    end-if.

Personally, I like your way better. And I used to argure with a guy
about "go to"s. One of my arguments was that COBOL hasn't got a the
necessary implied goto's that C++ has, such as "continue" or "break" and
as such was a crippled language that occaisionally required using
goto's. He told me that he wrote C++ and he didn't use *those*
constructs. Maybe some adhere to the rules tightly so they won't fail
and others understand the rules and can
break them when needed. UMMV.

In article <FOfm4.3524$pk.34355@news3.mia>,
  "Judson McClendon" <judmc@bellsouth.net> wrote:
> Robert M. Pritchett - RMP Consulting Partners LLC wrote:
> >An exit in the middle of a loop is like the classic read until EOF
problem.
> >Sure, Cobol only provides this kind of construct for such specific
cases
> >e.g. at end and not at end clauses, invalid key and not invalid key,
etc.
> >but you can still use the existing structures to implement the
technique.
> >This is far preferable to using a GoTo which has so much potential to
be
> >changed (by poor maintenance) to go anywhere and then you're out of
> >control. Even if you have to repeat a test by having an If inside
which
> >duplicates some of the tests in the outer Perform, this is still
preferable
> >to a GoTo.
>
…[16 more quoted lines elided]…
> those errors.  With the code checker, the GO TO EXIT is just as safe
as
> the EXIT PARAGRAPH, and simpler and clearer than trying to do it with
> hugely embedded IF/ELSE, or setting flags which are tested every time,
…[37 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3899FCC6.FE9708DD@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <87csi0$uol$1@nnrp1.deja.com>`

```
This seems odd to me.  Either you will want to check all fields, and when
done, respond accordingly, or you will want to quit when you find your first
error.

Also, typically a screen will have a pattern:
    PERFORM CHECK-HEADER-FIELDS
    IF MY-STATUS-OK
        PERFORM CHECK-ACCOUNTS
    END-IF
    IF MY-STATUS-OK
        PERFORM CHECK-AMOUNTS
    END-IF
This will allow breaking up your testing into manageable hunks.

shine98@my-deja.com wrote:

> I'm sure you know this but here is the "proper" way to do this, with no
> "go to"'s and no switches (if you don't count ws-error-sw, er, I mean
…[137 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87d0h6$62om$1@newssvr03-int.news.prodigy.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <87csi0$uol$1@nnrp1.deja.com>`

```

<shine98@my-deja.com> wrote in message news:87csi0$uol$1@nnrp1.deja.com...
> I'm sure you know this but here is the "proper" way to do this, with no
> "go to"'s and no switches (if you don't count ws-error-sw, er, I mean
…[46 more quoted lines elided]…
>     end-if.

Your code, as written, uses ws-error-msg as a switch and if more than one
field is in error, your code will only put out the error message for the
last one detected. The error message for each field found in error will
overlay the previous error message.  I probably would have coded:

VALIDATE-FIELDS.
    VALIDATE FIELD-1
    IF IN-ERR
        SET FIELD-1-IN-ERR TO TRUE
    END-IF
    VALIDATE FIELD-2
    IF IN-ERR
        SET FIELD-2-IN-ERR TO TRUE
    END-IF
    VALIDATE FIELD-3
    IF IN-ERR
        SET FIELD-3-IN-ERR TO TRUE
    END-IF
    VALIDATE FIELD-4
    IF IN-ERR
        SET FIELD-4-IN-ERR TO TRUE
    END-IF
    VALIDATE FIELD-5
    IF IN-ERR
        SET FIELD-5-IN-ERR TO TRUE
    END-IF
    VALIDATE FIELD-6
    IF IN-ERR
        SET FIELD-6-IN-ERR TO TRUE
    END-IF
    .
DISPLAY-ERRS.
    IF FIELD-1-IN-ERR
        DISPLAY ERR-1
    END-IF
    IF FIELD-2-IN-ERR
        DISPLAY ERR-2
    END-IF
    IF FIELD-3-IN-ERR
        DISPLAY ERR-3
    END-IF
    IF FIELD-4-IN-ERR
        DISPLAY ERR-4
    END-IF
    IF FIELD-5-IN-ERR
        DISPLAY ERR-5
    END-IF
    IF FIELD-6-IN-ERR
        DISPLAY ERR-6
    END-IF
    .

Of course for more than a half dozen fields, I would've used subscripts or
indexes to set the error switches and to display the corresponding error
messages.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<dQom4.1411$Mk2.47303@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <87csi0$uol$1@nnrp1.deja.com> <87d0h6$62om$1@newssvr03-int.news.prodigy.com>`

```
Actually in this case the validate routine for each field would've set the
flag that that field was bad (as well as setting a flag that at least one
field was bad), completely avoiding the need for your the If's inside your
entire first half of the code. But yes, I like your approach better.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** shine98@my-deja.com
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87enc2$6ht$1@nnrp1.deja.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <87csi0$uol$1@nnrp1.deja.com> <87d0h6$62om$1@newssvr03-int.news.prodigy.com>`

```
The code is efficient because usually errors won't be found and avoids
alot of setting of switches which I see as a problem. Years ago, for
batch updates, I coded the error message in a table with a switch and
would print the transaction and all errors listed afterwards. But online
(CICS) where you have one error message line on the screen, I just print
the most important error first by editing the most lethal conditions
first. Our users are very sharp and meke few errors anyway, I don't see
the value in "over coding" for events that are not likely (or
infrequently) to happen.



In article <87d0h6$62om$1@newssvr03-int.news.prodigy.com>,
  "Terry Heinze" <terryheinze@prodigy.net> wrote:
>
> <shine98@my-deja.com> wrote in message
news:87csi0$uol$1@nnrp1.deja.com...
> > I'm sure you know this but here is the "proper" way to do this, with
no
> > "go to"'s and no switches (if you don't count ws-error-sw, er, I
mean
> > msg):
> >
…[46 more quoted lines elided]…
> Your code, as written, uses ws-error-msg as a switch and if more than
one
> field is in error, your code will only put out the error message for
the
> last one detected. The error message for each field found in error
will
> overlay the previous error message.  I probably would have coded:
>
…[47 more quoted lines elided]…
> Of course for more than a half dozen fields, I would've used
subscripts or
> indexes to set the error switches and to display the corresponding
error
> messages.
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389a2890_4@news3.prserv.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia>`

```
Your comments are generally true. The only
problem I have is that your validation plods along
one field at a time. The way I do things is to check
as many fields as possible in one go, to minimize
1) the transaction load on the machine and the communications line
2) the end-user aggravation ("why can't it check all fields at a time")

If you try to do this, the GO TO exit is not the thing to do.
You should normally check the fields from the bottom
up, highlight the ones that are in error, and put the cursor
on the topmost error, with an error message pertaining
to that only. Your coding style does not really support
this, so your users become victims of your convenience.

An argument against my point of view is that users
normally only make one error at a time, so it doesn't
matter.


Judson McClendon <judmc@bellsouth.net> wrote in message
news:FOfm4.3524$pk.34355@news3.mia...
> Robert M. Pritchett - RMP Consulting Partners LLC wrote:
> >An exit in the middle of a loop is like the classic read until EOF
problem.
> You snipped the example in my message that doesn't match what you say.
> Consider a program that contains many paragraphs like this, with
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87eo3q$bg$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net>`

```
Leif Svalgaard wrote in message
>
>An argument against my point of view is that users
>normally only make one error at a time, so it doesn't
>matter.
>
Can I have some of your users?
;<)
```

###### ↳ ↳ ↳ Field editing

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389AEAC0.A87B0DD9@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <87eo3q$bg$1@news.igs.net>`

```
In the good old days, programs edited the data entry for, say numeric
values before they used that field as a key to look up something on the
database.  With faster machines, I would rather have simpler code and
just not find the record.  And if they ever change to allow alpha
characters it will still work.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<CsCm4.3100$Sx.55678@news4.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
>Your comments are generally true. The only
>problem I have is that your validation plods along
…[14 more quoted lines elided]…
>matter.

There's two more arguments that are paramount in these programs.
They generally have very complex validations involving multiple
fields.  This is necessary to meet design requirements.  Once an
error is detected in a field, it is indefinite what other fields
may or may not be in error.  Also, the way the error messages
are returned (a special line at the bottom of the screen that
the terminal or emulator supports for this purpose) only has
space for one error message. :-)  At one time I devised a system
where the bottom two lines of the screen were divided into four
error messages.  But this eventually had to be dropped, because
the user's data screens have so many data fields that it is not
possible to do it.  Many of their later systems require multiple
screens to do one transaction, just to fit all the data on the
screens.  In the Unisys A Series COMS environment, this presents
special problems and makes processing the transactions much more
complicated for the programmer and the user.  I have two large
clients, both of whom have similar situations.  True interactive
systems wouldn't have these particular problems, of course. :-)
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 10)_

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87f2h1$g0n$1@starburst.uk.insnet.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:CsCm4.3100$Sx.55678@news4.mia...
> Leif Svalgaard wrote:
> >Your comments are generally true. The only
…[40 more quoted lines elided]…
>

 I didn't really  want to get into this but I'm really fed up with this
thread.  BTW I kind of support both of you on validation.

As Bill Klein said earlier (more than somewhat) in this thread; in the UK we
tend to use sections all the time.  This seems to be anathema to some
people, but tough.

So as far as validation goes, I would have a section which dealt with the
validation of a whole screen, which could perform subsidiary sections for
complex validation of individual fields.  I would certainly validate the
screen as a whole, and highlight all invalid fields even if I only had room
to describe the error on the first field.  Users can normally recognise what
is wrong with a field if it is highlighted.  They don't need to have a 'Must
be numeric' message to tell them.  If they don't understand the error, they
fix what they can and press enter to get the next message. So that's Lief's
point of view.

But I agree with Judson that there's no point in doing cross validation if
any fields are in error.  However we validate for content first and only
validate for context if all content is OK.

BTW I would tend to do full screen validation even on Windows or using
curses on Unix although I might allow the users to configure whether they
wanted to have their typing interrupted on each error.  In my experience,
they don't take that option.

What I don't  agree with is this fundamentalist view, that has driven this
thread, that there is only one correct way to program.   Total tosh.  I've
been programming for 35 years.  I've programmed in 4-5 different assemblers,
COBOL, PL/I, various BASICS, C and languages whose initials I can't
remember.  I know that I write code that is generally easy to maintain.  I
also know that I have frequently had to write code that is going to be hard
to understand, even by me, a little way down the line.  Its no good saying
it shouldn't be so.  It is so.  In these cases I try to comment what I'm
doing so that it explains why I did what I did.  But even that's not always
possible.

I agree that structured programming is nice.  In fact I think I was using it
before it had a name.  But its not the meaning of life.  Its just a tool and
you always have to use the right tool for the job.  In my time there have
been many philosophies/languages that were going to transform programming
and solve all problems.  Most of them disappeared, while some of them just
became another tool.  But all of them had worshippers who thought they were
the only way to do things.

Some times you just have to use GO TO.  Sometimes code has GO TO in it
because of its age.  We have modules working on our WANG that were last
compiled in 1980.  Similarly we have modules on the AS400 that were last
compiled in 1990.  Unfortunately there doesn't seem to be this sort of
stability/upward compatibility in UNIX but certainly we are still compiling
old COBOL source.  They all still work.  If I had to change them I would
just do the change.  I wouldn't rewrite them no matter how many GO TOs they
had.   If anybody in our organisation rewrote something because they don't
like the structure they would have to find another job.

I have never found major problems maintaining other peoples code because it
has GO TOs in it.  Maybe using sections in COBOL make GO TOs easier to
control and follow.  But that would just show that GO TOs are not inherently
wrong.  They just cause problems in some styles of programs.

One thing that worries me is,  if these programs are so difficult to
maintain, how can they be understood well enough to allow them to be
rewritten and totally revalidated.

Have a nice weekend everyone. :-)
Rick
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87f3g2$oom$1@nntp9.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net>`

```
I don't mind a "good discussion" (aka debate) - but I must say that I find
this particular thread incredibly "unproductive".  I haven't heard anyone
convincing anyone else of anything !!! (much less presenting some fact that
the other readers didn't already know)

Being of "good German Jewish stock," I won't mention that specific nasty
Austrian, but I think that allowing this thread to die a well deserved death
might be "in order".
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<bxEm4.3401$Sx.60386@news4.mia>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <87f3g2$oom$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote:
>I don't mind a "good discussion" (aka debate) - but I must say that I find
>this particular thread incredibly "unproductive".  I haven't heard anyone
…[5 more quoted lines elided]…
>might be "in order".

I agree with you that the thread has run its course, and that none of
us has convinced the other. :-)  But I think these threads are good,
once in a while.  Not only do newbies get exposed to the experienced
opinions of old timers, but I believe it's good for us old timers to
re-think our reasons for doing things from time to time.  Even if I
don't agree with another opinion, I often gain perspective when it
is clearly articulated. :-)
```

###### ↳ ↳ ↳ VALADATE (was: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87f3aq$o11$1@nntp9.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net>`

```
Another "plug" for the revision of the Standard which includes the (new)
VALIDATE verb.  As it is (at least somewhat) on-topic, this verb actually
goes thru 5 "phases". As described in the draft of the next Standard,

"4) The VALIDATE statement is executed in five stages. Each stage is executed
for all the elements of the operand before each next stage. Any given stage
may be omitted because of the absence of any clause applying to that stage,
or because all the elements of the operand failed an earlier stage. The five
stages are listed below, together with the clauses that apply to each stage:

    a) Format validation: the DEFAULT clause, the PICTURE clause, the SIGN
clause, and the USAGE clause.
    b) Input distribution: the DESTINATION clause.
    c) Content validation: the CLASS clause and the VALUE clause.
    d) Relation validation: the ALLOW clause and the INVALID clause.
    e) Error indication: the ERROR clause.

At each stage, the execution of the VALIDATE statement will be affected also
by any OCCURS clause, REDEFINES clause, or PRESENT WHEN clause that is
specified in the data description entry for any of the elements of the
operand."

  ***

Certainly sounds to me like this will "solve" many of the problems brought up
in this (incredibly UNproductive) thread.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 11)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<fLEm4.2619$Mk2.99871@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net>`

```
Some good points here, and most of what I said was in regard to writing
totally new code. In maintenance situations, there's usually not time for
much cleanup, and lots of spaghetti may need to be left as is. However, the
part that needs to be changed, and certainly any new code added, and often
the immediately surrounding or interfacing code, should be clean. The idea
is for program quality to get better with each change, instead of worse.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389B1927.ACD03B55@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net>`

```
Rick Price wrote:

> What I don't  agree with is this fundamentalist view, that has driven this
> thread, that there is only one correct way to program.

Certainly.  But certain techniques are generally better for some purposes than
others.  Gradually, I have switched from techniques designed primarily for
hardware efficiency towards techniques designed for maintenance programming
efficiency.


> Some times you just have to use GO TO.  Sometimes code has GO TO in it
> because of its age.

Sometimes we have code designed around GO TO.  Therefore we use it.  Other times
people who don't understand structured programming but who know that GO TOs are
"bad", make code worse than they would have if they had kept in the GO TOs.  But
if I am writing a new program, I don't put in any drop through logic and my only
GO TO are to abort routines.  Maybe someday I'll come across a reason to put in
an old fashioned GO TO, but having done maintenance on all kinds of code, I
doubt it (not counting if my employer's standards want a GO TO EXIT, which many
do).

> I have never found major problems maintaining other peoples code because it
> has GO TOs in it.

I have found many cases where people have had troubles maintaining code which
troubles were enhanced by coding styles which are associated with GO TOs.

> One thing that worries me is,  if these programs are so difficult to
> maintain, how can they be understood well enough to allow them to be
> rewritten and totally revalidated.

Virtually the only times I have seen programs re-written for style purposes have
been when a vendor wants to sell his programs.  Then it is a marketing decision,
not a programming decision.  I have often seen people (including myself) TEMPTED
to re-write a monster program which has high maintenance costs, but those
re-writes have always been on a back-burner waiting until someone skilled has
enough time free to do the job right (with skilled users for reanalyzing the
business needs and for testing the complex monster, etc.) ... which is never.
But the answer to your question is that a skilled programmer can understand the
code well enough to do a re-write, while the beginner can't understand it well
enough to do efficient maintenance.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389CDCE9.6A3DD6CA@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net>`

```
Howard Brazee wrote:
> 
> 
…[11 more quoted lines elided]…
> maintenance.

The answer is piece by piece.  Rewrite the section you are working on
today and leave the rest alone.  The clustering principle says that
the section you maintain today will be the likely place to change
tomorrow. 

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87kkf1$a36$1@nntp8.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au>`

```

Ken Foskey <waratah@zip.com.au> wrote in message
news:389CDCE9.6A3DD6CA@zip.com.au...
> Howard Brazee wrote:
> >
…[21 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/

Ken,
  Actually, this is an approach that I disagree with (or at least would only
do with a GREAT DEAL of care).  If you have a program that uses PERFORM
SECTION and GO TO EXIT techniques and start changing "bits and pieces" to
PERFORM Para thru Para-Exit, you are quite likely to end up with a disaster.
Now some code is well enough structured, that you can change a "portion"
without impacting the rest of the program - but the chances are that such
programs are the ones that don't need "updating" anyway.  The programs that
really NEED re-structuring, often are the hardest to change a "little" bit
without surprising (and unwanted side-effects).
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 14)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea0BzNRc$GA.259@cpmsnbbsa03>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net>`

```
see below:

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:87kkf1$a36$1@nntp8.atl.mindspring.net...
>
> Ken Foskey <waratah@zip.com.au> wrote in message
…[20 more quoted lines elided]…
> > tomorrow.

I agree.
Sometimes just changing cryptic field names makes a program more readable,
and understandable.

This is a time wher you can change:
PERFORM  0300-routine-a
        THRU   0500-exit.
to
PERFORM  0300-routine-a
        THRU   0300-exit
PERFORM  0400-routine-b
        THRU   0400-exit
PERFORM  0500-routine-c
        THRU   0500-exit
and avoid the fall-thru nightmare for yourself, and the next person who gets
to maintain it.

The business functionality is what usually changes.
You usually don't have to address overall program control, like file and
table handling, or higher level decision logic.

> >
> > Thanks
…[4 more quoted lines elided]…
>   Actually, this is an approach that I disagree with (or at least would
only
> do with a GREAT DEAL of care).  If you have a program that uses PERFORM
> SECTION and GO TO EXIT techniques and start changing "bits and pieces" to
> PERFORM Para thru Para-Exit, you are quite likely to end up with a
disaster.

Agreed. You cannot change the SECTIONs to Paragraphs without some risk.
The size and complexity of the program also affect what you can do.

> Now some code is well enough structured, that you can change a "portion"
> without impacting the rest of the program - but the chances are that such
> programs are the ones that don't need "updating" anyway.

I have seen a program with 23 END-IFs in a performed section of code.
I would be tempted to change it, if I were modifying that section of code.
I would also add that I knew the system, and it was a new development
effort.

> The programs that
> really NEED re-structuring, often are the hardest to change a "little" bit
> without surprising (and unwanted side-effects).
>
 You are right on the money here.
I have seen source "re-structing" programs used to rewrite small systems.
Unfortunately the "re-structured" programs produced results that did not
match the original output.

The key to successful re-structuring is comprehensive testing.

> --
> Bill Klein
>     wmklein <at> ix dot netcom dot com
>
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 14)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87ldpj$sq2$1@newssvr04-int.news.prodigy.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net>`

```

> Ken,
>   Actually, this is an approach that I disagree with (or at least would
only
> do with a GREAT DEAL of care).  If you have a program that uses PERFORM
> SECTION and GO TO EXIT techniques and start changing "bits and pieces" to
> PERFORM Para thru Para-Exit, you are quite likely to end up with a
disaster.
> Now some code is well enough structured, that you can change a "portion"
> without impacting the rest of the program - but the chances are that such
> programs are the ones that don't need "updating" anyway.  The programs
that
> really NEED re-structuring, often are the hardest to change a "little" bit
> without surprising (and unwanted side-effects).
…[3 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com

Bill,
    Since the subject of PARAGRAPHs and SECTIONs have been brought up, I'd
like to mention that several places I've contracted at have had the standard
of using SECTIONs instead of PARAGRAPHs.  (Also, these were US companies,
not UK.)  Anyway, in my skeleton batch COBOL program, I have it laid out in
SECTIONs with the one exception of a SECTION reserved for miscellaneous
routines.  PARAGRAPHs within this SECTION all end by a GO TO SECTION-EXIT.
I prevent fall-through logic from happening by coding a fall-thru SECTION
immediately after the SECTION-EXIT.  Coding a PERFORM paragraph instead of
PERFORM paragraph thru SECTION-EXIT will be caught (at execution time) by
the fall-through section.  This method seems to work very well although it
does include PARAGRAPHs and SECTIONs in the same program.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 14)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389E86CF.3A254B0B@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> Ken,
…[9 more quoted lines elided]…
> "little" bit without surprising (and unwanted side-effects).

You are right.  I do not use thru nor sections so I would be stripping
these and migrating to paragraphs (personal choice).

If the program were coded in sections I would leave the sections on
the paragraphs until the last minute to avoid confusion.  The thru's
would be left in but reduced to a 'paragraph' format with an exit
until the last minute.

I use a production regression test and a passably comprehensive system
test for the stuff that I do.  If I find a problem I upgrade the
system test, remove the problems at it's source.

The code I restructure is the code between the groups.  Make it clean
and easily read.  Often this will involve replacing variable names
which helps the other parts of the program as well.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Changing parts of programs was Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 14)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-02-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B549EC.4D245794@istar.ca>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net>`

```
Actually the example you give is one of the easier ones to fix part by
part.  If the standard is always PERFORM section-name and GO TO
paragraph-name within section, then all you have to do is remove the GO
TO's within that section making it a single paragraph section.  This may
involve the performing of other single paragraph sections.  The time to
do that is when a section needs noticeable change anyway.  Testing
should include verification that you haven't introduced unintended
changes.  The testing requirement is the main reason to restrict
re-writes to times when major change is needed anyway so that the
testing that is required because of the rewrite is also required because
of the major change.

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca   

"William M. Klein" wrote:
> 
> Ken Foskey <waratah@zip.com.au> wrote in message
…[39 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: Changing parts of programs was Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<896nbg$s1$1@nntp3.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net> <38B549EC.4D245794@istar.ca>`

```
In the case that you talk about (PERFORM section-name, and GO TO
EXIT-paragraph as the only "GO TO"), I wouldn't even suggest "redoing" the
program.  This meets MOST definitions of structured programs.  The problem is
that most (many? some?) programs that originally STARTED this way, have ended
up adding "just a couple" of GO TO's that are to some place OTHER than the
exit-paragraph.  Once this happens, "all bets are off".  This is IMHO the
excellent "reason" for the new EXIT PARAGRAPH/SECTION feature - which really
does "enforce" this type of structure, and doesn't lead to (basically doesn't
allow for) those other "funny" GO TOs.
```

###### ↳ ↳ ↳ Re: Changing parts of programs was Re: You're invited to critique my new Cobol page I started - comment and rant

_(reply depth: 15)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#v1XH4#f$GA.253@cpmsnbbsa05>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <CsCm4.3100$Sx.55678@news4.mia> <87f2h1$g0n$1@starburst.uk.insnet.net> <389B1927.ACD03B55@NOSPAMwebaccess.net> <389CDCE9.6A3DD6CA@zip.com.au> <87kkf1$a36$1@nntp8.atl.mindspring.net> <38B549EC.4D245794@istar.ca>`

```

Clark F. Morris, Jr. <cfmtech@istar.ca> wrote in message
news:38B549EC.4D245794@istar.ca...
> Actually the example you give is one of the easier ones to fix part by
> part.  If the standard is always PERFORM section-name and GO TO
…[3 more quoted lines elided]…
> do that is when a section needs noticeable change anyway.

There are other thing you can do during maintenance.
Rename cryptic field names.
Move large blocks of in-line coding to a performed Paragraph or Section.
Detect and correct Fall through performs.

You don't want to rewrite the entire program, but if you can make life
easier for the next lucky soul who gets to maintain your changes to the
program you should do it.

> Testing
> should include verification that you haven't introduced unintended
> changes.

You are 100% correct.

>The testing requirement is the main reason to restrict
> re-writes to times when major change is needed anyway so that the
> testing that is required because of the rewrite is also required because
> of the major change.
>
The testing requirements for minor or major changes are about the same.
Major changes often introduce new data elements to a system, so it may be
better to test reworked coding during a minor change.
In any event, if you have to rework coding, do it first, run a regression
test, and then make your modifications.
Sometimes reworked coding will give you different results, but the
differences are because the previous coding was erroneous. Every now and
again I have to tell a user that previously unknown errors have been
detected.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<0ysm4.1794$Mk2.63820@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net>`

```
Right, some examples others have posted help with this. Given a choice, I
like to have room for a few error lines at the bottom of the screen, then I
can do something similar (pseudocode):

(#errs and err msg table set as global in cobol program)

#errs = 0
if fld1 bad
  call append-err-msg using 1
endif
if fld2 bad
  call append-err-msg using 2
endif
...
if #errs > 0
  perform show-err-msgs
else
  perform this-screen-ok-now-process-data
endif

...

(nested program) append-err-msg using msg#
#errs = #errs + 1
if #errs <= max # errs there are lines for
  msg-lines (#errs) = error-msg-text (msg#)
endif
goback

You can see the general idea - there are lots of ways to do this. The final
perform of the this screen ok routine moves on to the next phase of the
processing without getting into deeper nested if's. Or it could be where
the cross checks and more complicated validations are done.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389CDB81.D93D8CB0@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net> <0ysm4.1794$Mk2.63820@newsread2.prod.itd.earthlink.net>`

```
"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> Right, some examples others have posted help with this. Given a
…[18 more quoted lines elided]…
> 

The best system I have seen is one where error message 1 goes on the
bottom of the screen and PF1 shows a screen with all the error
messages (even some long text if required).

Easy to implement and looks good.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389CDABA.F11D3AD5@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <2dGk4.4560$Sa2.177286@newsread2.prod.itd.earthlink.net> <CV3l4.1986$rC3.59488@news3.mia> <fGMl4.378$w%5.3972@newsread2.prod.itd.earthlink.net> <FOfm4.3524$pk.34355@news3.mia> <389a2890_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> If you try to do this, the GO TO exit is not the thing to do.
…[4 more quoted lines elided]…
> this, so your users become victims of your convenience.

This is an example of coupling.  The order of the checks within the
validation routine is important.

If a maintenance programmer put a field at the bottom of the screen
and at the bottom of the validation process then it would produce
unexpected results.

This is not an easy one to solve, it is just an excellent example of
coupling.

This is where a comment is definitely required :-}

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38942B5D.E3CF898E@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02>`

```
DennisHarley wrote:
> 
> Even C has a GOTO.
> 

I have only once seen a goto used in a C program.  It was a low level
internal routine of Linux.  Goto's ate not required in C programming. 
There are absolutely minimal reasons that they should appear in CObol.
I personally never code them.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** "Dan Harpold" <danharp@mediaone.net>
- **Date:** 2000-01-30T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<21%k4.4536$hE1.9659366@ronws01.ce.mediaone.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au>`

```
What's your opinion of using a GOTO (in C/C++) to retry an operation within
the same function? I have used GOTOs to back up a few lines and retry a save
operation, for example...

...
try_to_save_data
if_error
    if_contention_error
        retry_save_up_to_five_times
...

alternate method
...
try_to_save_up_to_five_times
    if_succeeded_then_continue
    else_if_not_contention_error_then_handle_it
    else_next_save
...

I find the first method, although it does use the dreaded GOTO, is cleaner
and easier to read...



"Ken Foskey" <waratah@zip.com.au> wrote in message
news:38942B5D.E3CF898E@zip.com.au...
> DennisHarley wrote:
> >
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38957CAA.F0CD0D5A@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <21%k4.4536$hE1.9659366@ronws01.ce.mediaone.net>`

```
Dan Harpold wrote:
> I have used GOTOs to back up a few lines and retry a save
> operation, for example...
…[5 more quoted lines elided]…
>         retry_save_up_to_five_times
	^^^  goto assumed...

Why not code:

  perform until saved or some-arbitrary-limit-exceeded.
	try-and-save
        if OK
	   set saved to true
        end-if
  end-perform

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** Jerry Peters <gapeters@worldnet.att.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<872mka$3mm$1@bgtnsc02.worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au>`

```
You have not looked at much of the Linux kernel have you?
goto's are used extensively to exit various constructs for error
conditions and to improve the common code paths for performance. 
Linus has explicitely stated that _he_ uses goto's when
he thinks it's necessary. He also has rejected patches which remove
goto's, especially when he's used them for performance reasons.

I've had to fix some idiots goto'less code in Cobol. Have you ever tried
to figure out an if statement that spans several pages and nests 8 or more
levels deep? Especially when a few goto's would have greatly simplified
the code? You can design a well structured program using goto's; you can
also design a monstrosity by _not_ using goto's. It has much less to do
with goto's than with coding ability and logical thinking.
 
	Jerry

In alt.computer.consultants Ken Foskey <waratah@zip.com.au> wrote:
> DennisHarley wrote:
>> 
>> Even C has a GOTO.
>> 

> I have only once seen a goto used in a C program.  It was a low level
> internal routine of Linux.  Goto's ate not required in C programming. 
> There are absolutely minimal reasons that they should appear in CObol.
> I personally never code them.

> Thanks
> Ken Foskey
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38957DFA.BBF69AED@zip.com.au>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net>`

```
Jerry Peters wrote:
> 
> You have not looked at much of the Linux kernel have you?

Yes that right.  I code applications not rocket science.

> goto's are used extensively to exit various constructs for error
> conditions and to improve the common code paths for performance.
> Linus has explicitely stated that _he_ uses goto's when
> he thinks it's necessary. He also has rejected patches which remove
> goto's, especially when he's used them for performance reasons.

Performance is rarely an issue with application code.  Write it well
first time and then attempt to refactor for performance.  Well written
code outshines badly written code every time.

If you follow up with C++ you would use exception to escape a
sequential process that errors.  This closely follows the use case
that you would build for the system. That is another argument though.

> I've had to fix some idiots goto'less code in Cobol. Have you ever
> tried to figure out an if statement that spans several pages and
> nests 8 or more levels deep?

Yes.  I then break it up into functional groups with a named paragraph
that is called to describe what is occurring.  That is I leave
footprints of my path to the next poor sucker (err programmer).

> Especially when a few goto's would have greatly simplified the code?
> You can design a well structured program using goto's; you can
> also design a monstrosity by _not_ using goto's. It has much less to
> do with goto's than with coding ability and logical thinking.

Could not agree more.

Setting good style guidelines for new players adds to your chance of
getting a comprehensible mess rather than an incomprehensible.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<8741m3$3af$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net>`

```
Jerry Peters wrote in message
>
>I've had to fix some idiots goto'less code in Cobol. Have you ever tried
…[5 more quoted lines elided]…
>

While I agree that rules for the sake of rules are silly, and while I agree
that there is, indeed, a place for the odd (very odd) goto, laying the blame
for the above sort of code on the head of "structure" is ridiculous.

An eight page IF statement is the result of poor programming and is not
predicated by topdown structure. In fact, I would not consider it topdown at
all.  Topdown refers to the practice of sub-dividing a complex method into
multiple simple methods.  To equate it to simply avoiding the "GO TO"
statement reveals a profound misunderstanding of the entire methodology.

Readable code is created by trying, real hard, to write code that is easy to
read, then reading it back and changing it until it is easy to read.  With
practice, a programmer can even do it the first time. If it were possible to
just make a rule, then have the code magically become readable, then we
would not need programmers.

I could write readable code without "PERFORMS"; using *only* "GOTO's" for
flow control.  I have written thousands of lines of code in assembler that
way, simply because that is the most readable way of writing it.  I could
even write readable code using nothing but the ALTER statement if I had to.

Rules like "avoid GOTO" are training wheels for beginner programmers.
Structure is just that:  the way program parts are put together.  You can do
it logically and neatly so that it can be followed, or you can just jam it
all into a source code module and leave a mess.  Applying a label to the
various methods does not change their basic nature, nor does it affect
readability.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38958f9e_3@news3.prserv.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net>`

```

donald tees <donald@willmack.com> wrote
> Jerry Peters wrote in message
> Rules like "avoid GOTO" are training wheels for beginner programmers.
> Structure is just that:  the way program parts are put together.  You can
do
> it logically and neatly so that it can be followed, or you can just jam it
> all into a source code module and leave a mess.  Applying a label to the
> various methods does not change their basic nature, nor does it affect
> readability.

It is amazing that 32 years after Dijkstra's GOTO-paper this discussion
still goes on. (just for the record, Dijkstra has also stated that the
teaching and use of COBOL ought to be a criminal offense).

As readable assembler code clearly shows, the GOTO is not the
problem. The programmer is the problem.

For COBOL there is a special problem that once you use a GOTO
you have lost the 'way back'. That is: if you perform A, that performs
B, that go to C, you can't get back to where you performed A. This
means that perform and goto cannot be mixed while retaining a
reasonable structure (except with the artifice of using sections).
This alone relegates GOTOs to error exits and abends where
a GOTO might save the day. Personally, I have never used a
GO TO in COBOL, for the simple reason that I have never
*needed* to, but different applications (and people) may have
different perceived needs.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<874pe4$56q$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <38958f9e_3@news3.prserv.net>`

```
In comp.lang.cobol Leif Svalgaard <lsvalg@ibm.net> wrote:

: It is amazing that 32 years after Dijkstra's GOTO-paper this discussion
: still goes on. (just for the record, Dijkstra has also stated that the
: teaching and use of COBOL ought to be a criminal offense).

: As readable assembler code clearly shows, the GOTO is not the
: problem. The programmer is the problem.

It is mmy view that, in Cobol, the problem with GO TO is not the
GO TO at all.  When reading or writing code the GO TO is always
clear and explicit as to what will happen at that point (it may
be wrong but it is always clear).

This gives the impression that a GO TO may be a clearer way of
expressing the program.

The problem with GO TO is that it must have a label.  Generally
this means that the program must have more labels (paragraph and
section names).  The usual way of increasing the number of labels
to cater for GO TO is to have sections and to add paragraph  labels
within this.  In Cobol a label can be used in several different
ways: Performed, GOne TO, dropped into, and are of two types
(section and paragraph) which can be made to overlap in
complex ways.

Other languages use different label types for different purposes:
a label that may be used as a target for a goto cannot be used
for any other purpose; a procedure name cannot be used to goto.

When examining a part of the code in a Cobol program where a
mixture of PERFORM and GO TO is used it is necessary to determine
all the paths through the code by examination of the whole
program.  That is, if the part of the program being examined 
contains a label, for example:

          calculate, say, price of item.
      calc-paragraph-label.
           calculate tax on item.

If it is necessary to change the code such that the price and
tax calculations are revised then the presence of the label
_may_ indicated that it is:

      target for a goto
      terminates a perform of the paragraph above
      target for a perfrom
      drops through

So the code above and below the label may be executed separately
or together in arbitrary ways.

The only solution is to examine the whole source code to determine
every possible path involving this label and the labels above.

If, in examining some code, a GO TO is found, this is trivial to
trace and is an entirely different issue.

One way of reducing the complexity of determining program flow is 
to lay down standards which can be guaranteed.  This may be, for
example, that the only GO TOs are to the end of a performed section
with a guaranteed name.  It is thus only necessary to confirm
the guarantee.  In the above case the label must be spurious and
should be commented out (because it is not the end of a section
and is not a section).

Another way of reducing complexity is to guarantee that all labels
only have one type of use.  As PERFORM is the most useful statement
then this should eliminate all other ways that a label could be 
used.  Thus GO TO is banned, as are drop throughs and thus
THRU.

Thus when examining the example code above one can be guaranteed
that the pricing and tax are always done separately by specific
performs of the paragraphj above and the label shown and this
can be searched for without needing to understand the whole
program.

One of the skills of programming is to reduce the complexity.
There are several ways of doing this, each can work. I prefer
the way that has no sections and the only reference allowed to
a label is a perform (without thru).

Those that have used other mechanisms (such as perform section
and goto exit) usually raise objections based on applying
their styles to this different mechanism and don't see that a
completely different style is required which, once, adopted
actually produces much less complexity.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3896378c_2@news3.prserv.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <38958f9e_3@news3.prserv.net> <874pe4$56q$1@aklobs.kc.net.nz>`

```
well said, Richard

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:874pe4$56q$1@aklobs.kc.net.nz...
> In comp.lang.cobol Leif Svalgaard <lsvalg@ibm.net> wrote:
>
…[91 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000131231931.24953.00000886@ng-bj1.aol.com>`
- **References:** `<3896378c_2@news3.prserv.net>`

```
Lots of interesting stuff here, but the original question, I thought, was:

PERFORM ABEND-ROUTINE.
 or
GO TO ABEND-ROUTINE.

My preference is for the latter, since, presumbably, there is no intent on
returning from the abend routine (implied by using the PERFORM).  However, with
the post-OSVS releases of COBOL, that may be the only time I would use GO TO,
since the END-xxx statements seem to be fairly effective and comprehensive.

For those who insist on NEVER using GO TOs, I would suggest that is one of
those "foolish inconsistencies that are the hallmark of ........". Oh well, you
get the idea!


Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<875ne7$3an$1@nntp9.atl.mindspring.net>`
- **References:** `<3896378c_2@news3.prserv.net> <20000131231931.24953.00000886@ng-bj1.aol.com>`

```
Actually, besides the GO TO/PERFORM abend-paragraph, there is another case
like this that seems similar to me.  Somewhere in this thread the topic of
(IBM mainframe) CICS programming came up. Thinking about this (and it has
been a LONG time since I actually coded CICS - so my memory may be entirely
wrong) - if I were creating a pseudo-conversational application program, I
would probably  PERFORM (not GO TO) a paragraph with an

    EXEC CICS RETURN TRANSID(xxxx)

statement.  This stands as little chance of ever "returning" from the PERFORM
as does one with an "ABEND" in it.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3896B3C1.98A0BC30@worldnet.att.net>`
- **References:** `<3896378c_2@news3.prserv.net> <20000131231931.24953.00000886@ng-bj1.aol.com> <875ne7$3an$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> Actually, besides the GO TO/PERFORM abend-paragraph, there is another case
…[9 more quoted lines elided]…
> as does one with an "ABEND" in it.

In the parlance of the COBOL analysis & restructuring business this is
called "terminating logic" and is PERFORMed.

Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38965C63.D519DB2C@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <38958f9e_3@news3.prserv.net> <874pe4$56q$1@aklobs.kc.net.nz>`

```
This has nothing to do with Rich Plinston, and everything to do with
"structured code". The following is the best description I've seen
regarding structured code. Interestingly enough, it's from one of the
manuals for HLASM:

                      (this is it)

The complexity of control flow in a program strongly affects the ease of
reading it, the early detection of coding errors, and the effort needed
modify it later. Control flow can usually be simplified (though sometime
at the cost of less efficiency and more redundant code) by restricting
the ways in which branches occur.  One way to restrict branches is to
use on those necessary to implement a few basic structures such as:

 	Executing one of two blocks of code according to a true-false
condition

 	Executing a block of code repeatedly until some limit is reached

 	Executing the nth block of code in a given set, where n is previously
computed

*	Calling another module as a subroutine


If statements exist for all these structures in a programming language,
then they are used exclusively.  If some are missing, then simple branch
are used to simulate those structures but only in standard patterns.  In
the case of OS Assembler Language, only the basic branch and
branch-and-link instructions are implemented but macros that simulate
the first three structures are available.

It has been shown that the four structures above (in fact, the first two
are sufficient to implement any "proper" program (that is, with one
entry point and one exit) provided that its blocks of code are suitably
ordered. It is assumed that the structures may be nested to any depth.
The technique of writing programs using only these structures for
branching known as "structured programming".

The standard structured programming figures have been implemented for
the assembler language programmer through the following five sets of
related macros.

*   The IF macro set:

        IF
        ELSE (optional)
        ENDIF.

*   The DO macro set:

        DO
        DOEXIT (optional)
        ENDDO.

*   The CASE macro set:

        CASENTRY
        CASE (one must be present)
        ENDCASE.

*   The SEARCH macro set:

        STRTSRCH
        EXITIF
        ORELSE
        ENDLOOP
        ENDSRCH

*   The SELECT macro set:

        SELECT
        WHEN
        OTHRWISE (optional)
        ENDSEL

              (end definition)

I trust no one on this NG has any problem relating these constructs to
COBOL.
Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<f4Nl4.25$3v6.1570@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <38958f9e_3@news3.prserv.net> <874pe4$56q$1@aklobs.kc.net.nz>`

```
You've explained this and especially my other point about Cobol (almost
uniquely) having the multi-use label problem (perform/goto/etc.) much
better than I did. Thanks.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** Jerry Peters <gapeters@worldnet.att.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net>`

```
In alt.computer.consultants donald tees <donald@willmack.com> wrote:
> Jerry Peters wrote in message
>>
…[6 more quoted lines elided]…
>>

> While I agree that rules for the sake of rules are silly, and while I agree
> that there is, indeed, a place for the odd (very odd) goto, laying the blame
> for the above sort of code on the head of "structure" is ridiculous.

I _would_ agree, except to many people, structured means no goto's.

> An eight page IF statement is the result of poor programming and is not
> predicated by topdown structure. In fact, I would not consider it topdown at
> all.  Topdown refers to the practice of sub-dividing a complex method into
> multiple simple methods.  To equate it to simply avoiding the "GO TO"
> statement reveals a profound misunderstanding of the entire methodology.

That's what I tend to do in assembler, which is my main language. I create a
stack of register save areas, then create relatively simple subroutines to do
all of the work. The problem with doing that in COBOL is that there is no
argument passing, which makes using subroutines a pain.

> Readable code is created by trying, real hard, to write code that is easy to
> read, then reading it back and changing it until it is easy to read.  With
> practice, a programmer can even do it the first time. If it were possible to
> just make a rule, then have the code magically become readable, then we
> would not need programmers.

Of course, but COBOL was designed under tha assumption that bean counters could
do the coding, if only the language were simple enough (English like, I assume).
    
> I could write readable code without "PERFORMS"; using *only* "GOTO's" for
> flow control.  I have written thousands of lines of code in assembler that
> way, simply because that is the most readable way of writing it.  I could
> even write readable code using nothing but the ALTER statement if I had to.

I once maintained a system that used alter-goto's instead of performs, because
using even one perform caused the program to become much larger (this was under
360 DOS). The alter-goto's were only used to emulate performs, not as part of
the logic. It worked and was not hard to maintain.

> Rules like "avoid GOTO" are training wheels for beginner programmers.
> Structure is just that:  the way program parts are put together.  You can do
…[3 more quoted lines elided]…
> readability.

The problem is that nobody seems to emphasize that the code should be readable,
certainly not in college. One of the first things I learned was to make my code
readable; in 6 months or a year even I'll need all the help I can get to understand
what the code is doing, let alone some other poor maintenance programmer who get
stuck fixing or modifying the code. Yet I'm amazed to see others who don't do that.
Especially in assembler where they code offsets from some base register rather than
using dsects. You may as well be reading a hex dump of the object code.

	Jerry
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<OV0Um6Eb$GA.286@cpmsnbbsa03>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`

```

Jerry Peters <gapeters@worldnet.att.net> wrote in message
news:Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net...
>
> > An eight page IF statement is the result of poor programming and is not
> > predicated by topdown structure. In fact, I would not consider it
topdown at
> > all.  Topdown refers to the practice of sub-dividing a complex method
into
> > multiple simple methods.  To equate it to simply avoiding the "GO TO"
> > statement reveals a profound misunderstanding of the entire methodology.
>
> That's what I tend to do in assembler, which is my main language. I create
a
> stack of register save areas, then create relatively simple subroutines to
do
> all of the work. The problem with doing that in COBOL is that there is no
> argument passing, which makes using subroutines a pain.

I think using nested programs may address the argument passing.
The other benefit is localization of work areas.

>
> I once maintained a system that used alter-goto's instead of performs,
because
> using even one perform caused the program to become much larger (this was
under
> 360 DOS). The alter-goto's were only used to emulate performs, not as part
of
> the logic. It worked and was not hard to maintain.

Oh my God!!! You maintained my first COBOL Program.
When I wrote my first COBOL program, I was forced to use ALTERS, when I
tried using PERFORMs the program was too large to run in the 40K partition.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Jerry Peters <gapeters@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<5hJl4.1418$Vy.137384@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net> <OV0Um6Eb$GA.286@cpmsnbbsa03>`

```
In alt.computer.consultants DennisHarley <LegacyBlue@email.msn.com> wrote:

> Jerry Peters <gapeters@worldnet.att.net> wrote in message
> news:Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net...
…[14 more quoted lines elided]…
>> argument passing, which makes using subroutines a pain.

> I think using nested programs may address the argument passing.
> The other benefit is localization of work areas.

>>
>> I once maintained a system that used alter-goto's instead of performs,
…[5 more quoted lines elided]…
>> the logic. It worked and was not hard to maintain.

> Oh my God!!! You maintained my first COBOL Program.
> When I wrote my first COBOL program, I was forced to use ALTERS, when I
> tried using PERFORMs the program was too large to run in the 40K partition.

That's about it. The bank had a "large" 256K mdoel 40 (or maybe that was the 
360-50, it's been a long time). The machine I'm writing this on has 64M, 
current 967x's ship with a minimum of 1G, I think. 

	Jerry
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<876kli$ll7$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`

```
Jerry Peters wrote in message ...
>
>The problem is that nobody seems to emphasize that the code should be
readable,
>certainly not in college. One of the first things I learned was to make my
code
>readable; in 6 months or a year even I'll need all the help I can get to
understand
>what the code is doing, let alone some other poor maintenance programmer
who get
>stuck fixing or modifying the code. Yet I'm amazed to see others who don't
do that.
>Especially in assembler where they code offsets from some base register
rather than
>using dsects. You may as well be reading a hex dump of the object code.
>
Yes, I agree.  I have often thought that school exercises should include
changing the previous classes code.  I have written thousands of pages of
assembler for at least twenty CPU's, and can write assembler as clear as
COBOL. It is simply a matter of developing the right habits.

I have an entire general ledger system here that still works, written in
1981 for a PC with a 360k single sided floppy. The run module is 4k.
Including the online (syntax sensitive) help, it resides in 45k.
How times change.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3896340B.EE1C02B4@neo.rr.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`

```

Jerry Peters wrote:
<snip>
> The problem is that nobody seems to emphasize that the code should be readable,
> certainly not in college. One of the first things I learned was to make my code
…[6 more quoted lines elided]…
>         Jerry

I taught a COBOL class many years ago.  One of the things I told
the students on their third program was, make sure you write this
program so that it is readable, because you will be graded on
that for program number four.

They all got the point when they had to pass their programs on to
another person in the class who had to modify program #3 written
by someone else, to do what program #4 required.  And, they were
not allowed to go and ask questions of the author.

My very obvious point was, yes, you can make your paragraph names
single characters, just like you can your data names.  But, when
you have to fix it later, how much sense will it make?

I told them all to remember this little exercise, because they
never knew which program I'd do it with next (just like the
golfer with the two gotcha's -- you don't use the second one, all
you needed was the first).
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<876kp8$ll9$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net> <3896340B.EE1C02B4@neo.rr.com>`

```
Great exercise.  I hope you allowed the students to mark the previous
students work (IE:- the person who's code they had to revise)<G>

Steve Thompson wrote in message <3896340B.EE1C02B4@neo.rr.com>...
>
>Jerry Peters wrote:
><snip>
>> The problem is that nobody seems to emphasize that the code should be
readable,
>> certainly not in college. One of the first things I learned was to make
my code
>> readable; in 6 months or a year even I'll need all the help I can get to
understand
>> what the code is doing, let alone some other poor maintenance programmer
who get
>> stuck fixing or modifying the code. Yet I'm amazed to see others who
don't do that.
>> Especially in assembler where they code offsets from some base register
rather than
>> using dsects. You may as well be reading a hex dump of the object code.
>>
…[29 more quoted lines elided]…
>in use
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<ccOl4.129$3v6.7965@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`

```
Actually you can do that now, Cobol now supports local nested procedures
like Pascal etc. so you have effectively a "Perform Using". And of course
you can still call an externally compiled subroutine as you always could.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** "Robert W. McAdams" <fambright@sigmais.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389D5B5B.462487E4@sigmais.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <8741m3$3af$1@news.igs.net> <Eapl4.185$Vu3.22631@bgtnsc04-news.ops.worldnet.att.net>`

```
Jerry Peters wrote:

> I _would_ agree, except to many people, structured means no goto's.

I have also found that, to many of them, "no GO TOs" also means "structured" (i.e., the
code must be structured if it doesn't have any GO TOs).  This belief can lead to an
interesting phenomenon which I like to call "structured spaghetti logic".


Bob
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3895C14D.C6776F8@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net>`

```
Jerry Peters wrote:
> 
> I've had to fix some idiots goto'less code in Cobol. Have you ever tried
…[6 more quoted lines elided]…
>         Jerry

It isn't hard for someone who doesn't understand how to structure simple
GOTO-less, switch-less to mess up a program entirely by attempting to
remove GOTOs.  But someone who knew what he was doing could have done
that same program much more clear and maintainable - WITHOUT resorting
to GOTO statements.

Don't create a rule or standard for a shop without teaching the
programmers how to properly code using that rule or standard.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389657EF.826A71E3@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net>`

```
Jerry Peters wrote:
> 
> You have not looked at much of the Linux kernel have you?

Nope, never seen it.

> goto's are used extensively to exit various constructs for error
> conditions and to improve the common code paths for performance.
> Linus has explicitely stated that _he_ uses goto's when
> he thinks it's necessary. He also has rejected patches which remove
> goto's, especially when he's used them for performance reasons.

But Linus isn't coding COBOL, is he?

> I've had to fix some idiots goto'less code in Cobol. Have you ever tried
> to figure out an if statement that spans several pages and nests 8 or more
…[3 more quoted lines elided]…
> with goto's than with coding ability and logical thinking.

I have fixed *far* more convoluted piles of other peoples' GOTO crap
than anyone's ever had to fix in mine (a LOT).

'Hoping I don't post to this thread anymore,
Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3896F071.F121BCC4@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net>`

```
William Lynch wrote:

> I have fixed *far* more convoluted piles of other peoples' GOTO crap
> than anyone's ever had to fix in mine (a LOT).

Me too.  Even with GOTO EXIT code.  The only common coding technique which is
worse is GOTO less code where the person replaced the GOTOs with switches and
didn't learn a thing about structured programming.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** shine98@my-deja.com
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8776vg$puu$1@nnrp1.deja.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net>`

```
Not to get off the subject or anything but I am coming through
Deja.com and the link to the initial message is snarled. Can anyone
tell me what the link for the COBOL web page the guy wanted an opinion
on? Thanks.

goto's? I like the flexibility. I use them sparingly and can code either
way. Around here we code *everything* in sections with an exit. And we
go to the exit when we need to. We can in our shop:

 PROCEDURE DIVISION.
 0-MAIN SECTION.
	PERFORM A-SECTION
	PERFORM B-SECTION
	PERFORM C-SECTION
	GOBACK.
 0-EXIT. EXIT.

 A-SECTION SECTION.
*Notethelittleprograminthemidstofthelargerprogram
	PERFORM A-INIT-PARA
	PERFORM A-PROCESS-PARA
	PERFORM A-FINISH-PARA
	GO TO A-EXIT.

 A-INIT-PARA.
*INITIALIZE VARIABLES LOCAL TO THE "A" PROCESS
	MOVE 'N' TO FATAL-SNAFU-SW.

 A-PROCESS-PARA.
	MOVE 'Y' TO FATAL-SNAFU-SW.
	IF FATAL-SNAFU
		GOTO A-EXIT
	END-IF.

 A-FINISH-PARA.
 A-EXIT.EXIT.

 B-SECTION SECTION.
	PERFORM B-INIT-PARA
	PERFORM B-PROCESS-PARA
	PERFORM B-FINISH-PARA
	GO TO B-EXIT.

 B-INIT-PARA.
*INITIALIZE VARIABLES LOCAL TO THE "B" PROCESS
	MOVE 'N' TO FATAL-SNAFU-SW.

 B-PROCESS-PARA.
	MOVE 'Y'TO FATAL-SNAFU-SW.
	IF FATAL-SNAFU
		GO TO B-EXIT
	END-IF.

 B-FINISH-PARA.
 B-EXIT. EXIT.

 C-SECTION SECTION.
*INITIALIZE VARIABLES LOCAL TO THE "C" PROCESS
	MOVE 10 TO WS-COUNT
	PERFORM WS-COUNT TIMES
		IF TRUE
			DISPLAY 'HELLO WORLD!'
		ELSE
			GO TO C-EXIT
		END-IF
	END-PERFORM
	MOVE 0 TO WS-COUNT
C-EXIT.EXIT.

I am sure that by now some of you are thinking that this is code so
ugly only a mother could love, but! it is easy to maintain and very
flexible. The whole goto problem stems from the fact that COBOL is not a
block structured language (I'd trade all those END-IF's, END_READ's,
END-PERFORM's, etc for a simple a simple BEGIN and END. But that's
another post.


I hope my saying this won't reduce my chances of getting that URL <g>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e$FFL2Pb$GA.276@cpmsnbbsa04>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com>`

```
In the past few years, I have seen only 1 recently written program that uses
SECTIONs.
It turns out that the user was writing programs.

The problem with using SECTIONs is that you can fall thru the subordinate
paragraphs if you are not careful.

From what I can see you can remove the " SECTION. ", and GO TO EXITs.
(Change:  A-SECTION SECTION. to A-SECTION.)

You will also have to test your FATAL-SNAFU-SW before you invoke the
FINISH-PARA
paragraph.

<shine98@my-deja.com> wrote in message news:8776vg$puu$1@nnrp1.deja.com...
>
> goto's? I like the flexibility. I use them sparingly and can code either
…[75 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ SECTIONS/PARAGRAPHS (yet again) (was: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<877m57$usm$1@nntp3.atl.mindspring.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <e$FFL2Pb$GA.276@cpmsnbbsa04>`

```
I will bet almost anything that you are in the US.  From past threads (and my
own experience) for some (TOTALLY UNKNOWN reason), this is a real "cultural"
difference between the US and UK (with most of Europe doing as is done in the
UK - and most of Canada doing as the US does),

In the US, you almost NEVER see a program with SECTIONS (or at least
new/significantly modified code with SECTIONS).

In the UK, almost every program uses SECTIONS.

HOWEVER, even in the UK use of SECTIONS, there are rarely more than a main
and an "exit" paragraph - even those two.

I won't go thru the lengthy threads we have gone thru in the past, but the
bottom-line is that you can write "good" structured code using either
technique - but trying to mix the two - or trying to modify code that uses
one technique with a portion that uses the other, leads to highly error-prone
code.
```

###### ↳ ↳ ↳ Re: SECTIONS/PARAGRAPHS (yet again) (was: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ot1RVrQb$GA.241@cpmsnbbsa02>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <e$FFL2Pb$GA.276@cpmsnbbsa04> <877m57$usm$1@nntp3.atl.mindspring.net>`

```
You would win the bet.

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:877m57$usm$1@nntp3.atl.mindspring.net...
> I will bet almost anything that you are in the US.  From past threads (and
my
> own experience) for some (TOTALLY UNKNOWN reason), this is a real
"cultural"
> difference between the US and UK (with most of Europe doing as is done in
the
> UK - and most of Canada doing as the US does),
>
…[11 more quoted lines elided]…
> one technique with a portion that uses the other, leads to highly
error-prone
> code.
This is definately TRUE.

>
> --
…[9 more quoted lines elided]…
> > The problem with using SECTIONs is that you can fall thru the
subordinate
> > paragraphs if you are not careful.
> >
…[7 more quoted lines elided]…
> > <shine98@my-deja.com> wrote in message
news:8776vg$puu$1@nnrp1.deja.com...
> > >
> > > goto's? I like the flexibility. I use them sparingly and can code
either
> > > way. Around here we code *everything* in sections with an exit. And we
> > > go to the exit when we need to. We can in our shop:
…[63 more quoted lines elided]…
> > > flexible. The whole goto problem stems from the fact that COBOL is not
a
> > > block structured language (I'd trade all those END-IF's, END_READ's,
> > > END-PERFORM's, etc for a simple a simple BEGIN and END. But that's
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: SECTIONS/PARAGRAPHS (yet again) (was: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8793vv$85b$1@starburst.uk.insnet.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <e$FFL2Pb$GA.276@cpmsnbbsa04> <877m57$usm$1@nntp3.atl.mindspring.net>`

```
I think you're right Bill.   We certainly always use sections.   It may be
because we didn't like the PERFORM ... THRU ... construct.   This was
certainly true in my case from many years ago.  I always found programs that
used this really difficult to maintain (i.e unmaintainable).  If a group of
paragraphs had to be processed together then this seemed to logically form a
section.  If any paragraphs from this group could be performed individually
then they would be made sections and always performed.

I think this may have been our version of the GO TO wars.

I like structured programs but I also use GO TO, depending on the style of
the program I'm maintaining.  Its horses for courses.

I've been reading this thread bemused by the depth of feeling against GO
TOs.  I couldn't think what the problem was.   Now you've mentioned that in
the US sections are rarely used, I understand.  Certainly if we didn't use
sections  then I would be strongly against the use of GO TO.

BTW I don't think we need to start a thread pro and anti use of sections.

Rick

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:877m57$usm$1@nntp3.atl.mindspring.net...
> I will bet almost anything that you are in the US.  From past threads (and
my
> own experience) for some (TOTALLY UNKNOWN reason), this is a real
"cultural"
> difference between the US and UK (with most of Europe doing as is done in
the
> UK - and most of Canada doing as the US does),
>
…[11 more quoted lines elided]…
> one technique with a portion that uses the other, leads to highly
error-prone
> code.
>
…[10 more quoted lines elided]…
> > The problem with using SECTIONs is that you can fall thru the
subordinate
> > paragraphs if you are not careful.
> >
…[7 more quoted lines elided]…
> > <shine98@my-deja.com> wrote in message
news:8776vg$puu$1@nnrp1.deja.com...
> > >
> > > goto's? I like the flexibility. I use them sparingly and can code
either
> > > way. Around here we code *everything* in sections with an exit. And we
> > > go to the exit when we need to. We can in our shop:
…[63 more quoted lines elided]…
> > > flexible. The whole goto problem stems from the fact that COBOL is not
a
> > > block structured language (I'd trade all those END-IF's, END_READ's,
> > > END-PERFORM's, etc for a simple a simple BEGIN and END. But that's
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<877f53$ukb$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com>`

```
shine98@my-deja.com wrote:
: go to the exit when we need to. We can in our shop:

:  PROCEDURE DIVISION.
:  0-MAIN SECTION.
: 	PERFORM A-SECTION
: 	PERFORM B-SECTION
: 	PERFORM C-SECTION
: 	GOBACK.
:  0-EXIT. EXIT.

:  A-SECTION SECTION.
: *Notethelittleprograminthemidstofthelargerprogram
: 	PERFORM A-INIT-PARA
: 	PERFORM A-PROCESS-PARA
: 	PERFORM A-FINISH-PARA
: 	GO TO A-EXIT.

:  A-INIT-PARA.
: *INITIALIZE VARIABLES LOCAL TO THE "A" PROCESS
: 	MOVE 'N' TO FATAL-SNAFU-SW.

:  A-PROCESS-PARA.
: 	MOVE 'Y' TO FATAL-SNAFU-SW.
: 	IF FATAL-SNAFU
: 		GOTO A-EXIT
: 	END-IF.

:  A-FINISH-PARA.
:  A-EXIT.EXIT.

: I am sure that by now some of you are thinking that this is code so
: ugly only a mother could love, but! it is easy to maintain and very
: flexible. 

This code uses PERFORMs of both sections and paragraphs and GO TOs
to the exit of a section.  I'll ignore that you are jumping
out of the scope of a PERFORM which _may_ have an effect on the
perform stack.

The code would need an inordinate amount of checking and is likely
to have a high requirement for debugging (compared to simpler
structures).  (BTW this is a style I tried a couple of decades
ago so I am talking from experience).  It may well be suitable
for 'batch' orientated programs which can be layered in a 
formal structure, but will have difficulties (compared to
other structures) when applied to more flexible usage, such
as event driven or fully interactive.

There are also difficulties in reusing code.  For example if
A-Process-Para were required to be reused at some later time
in the program then it cannot because it may fail and GO TO
A-Exit causing complete loss of control.

This may lead to the paragraph being copied to duplicate the
functionality and then it must be changed to have a different
GO TO (whereas 'EXIT PARAGRAPH') has no such problem.

When I did try this style it was part of a progression that
I was making to a 'better' style than PERFORM SECTIONs only.
Breaking the section into performed paragraphs was an
improvement over 'drop through or gotoexit' and did not
incur the high overheads of create new complete sections with
new number and exit paragraph, but it required two levels of
checking:  sections terminate at the next SECTION (and not at
the EXIT statement), paragraphs at the next label.

ie it is just too complex when complexity reduction should be
an aim of programming.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 10)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e6gwX8Pb$GA.269@cpmsnbbsa04>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <877f53$ukb$1@aklobs.kc.net.nz>`

```

Richard Plinston <riplin@kcbbs.gen.nz> wrote in message
news:877f53$ukb$1@aklobs.kc.net.nz...
> The code would need an inordinate amount of checking and is likely
> to have a high requirement for debugging (compared to simpler
> structures).

I agree.

>  It may well be suitable
> for 'batch' orientated programs which can be layered in a
> formal structure, but will have difficulties (compared to
> other structures) when applied to more flexible usage, such
> as event driven or fully interactive.

I work mainly in batch, this is not suitable.

> ie it is just too complex when complexity reduction should be
> an aim of programming.

I agree again, there is no real need for sections.  SECTIONs cannot be
justified because they have no advantage over Paragraph Names, and they
jeopardize the integrity of the system.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 11)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<878s7h$3pl$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <877f53$ukb$1@aklobs.kc.net.nz> <e6gwX8Pb$GA.269@cpmsnbbsa04>`

```
DennisHarley wrote in message ...

>I agree again, there is no real need for sections.  SECTIONs cannot be
>justified because they have no advantage over Paragraph Names, and they
>jeopardize the integrity of the system.
>

Well, that is not *quite* true.  You could be writing code for some 26K byte
machine made in 1959 or so, and need multiple sections above the section
limit for the overlay feature ...

I remember way back before electricity was invented, when we had to walk 15
miles every morning to computer science school, and poke holes in those
paper tapes with our pencils because all the SR33's were busy, we used to do
that all the time.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 12)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38984038.D6CD2685@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net> <389657EF.826A71E3@worldnet.att.net> <3896F071.F121BCC4@NOSPAMwebaccess.net> <8776vg$puu$1@nnrp1.deja.com> <877f53$ukb$1@aklobs.kc.net.nz> <e6gwX8Pb$GA.269@cpmsnbbsa04> <878s7h$3pl$1@news.igs.net>`

```
donald tees wrote:

> DennisHarley wrote in message ...
>
…[7 more quoted lines elided]…
> limit for the overlay feature ...

When we had to have SECTIONS for internal sorts, I would have something like
this:

SORT-OUTPUT-SECTION SECTION.
    PERFORM SORT-OUTPUT-PARAGRAPH.
REST-OF-THE-PROGRAM SECTION.
SORT-OUTPUT-PARAGRAPH.

Kind of ugly, but it made sure that a maintenance programer could add a new
paragraph without worrying too much about it being performed inadvertently.

Since we have a standard error routine which is required in all of our IDMS
programs which includes a SECTION, I get rid of a warning message as follows:

PROCEDURE DIVISION.
GET-RID-OF-WARNING SECTION.
0000-MAIN.
      PERFORM 0100-INITIALIZE.
      ...

We very rarely have any need for Declaratives, so I wish we had no PROCEDURE
DIVISION sections at all.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
- **Date:** 2000-02-02T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<kXMl4.7$3v6.469@newsread2.prod.itd.earthlink.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <#wgNZYia$GA.307@cpmsnbbsa02> <38942B5D.E3CF898E@zip.com.au> <872mka$3mm$1@bgtnsc02.worldnet.att.net>`

```
See below.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "Robert W. McAdams" <fambright@sigmais.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389D59E6.D6306094@sigmais.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net>`

```
Robert M. Pritchett - RMP Consulting Partners LLC wrote:

> Understandable about GoTo's in assembler; unless they've
> implemented a nice set of structured programming macros like I did for MIX
> in college, you pretty much have to put your own structures together with
> the various kinds of branches.

Actually, assembler is a more structured language than COBOL in one respect:
Unless you resort to rather convoluted logic, there is no way in assembler
both to perform a routine (i.e., to invoke it via a BAL) and to fall through
it.


Bob
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<87kie1$rfv$1@aklobs.kc.net.nz>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com>`

```
In comp.lang.cobol Robert W. McAdams <fambright@sigmais.com> wrote:
: Robert M. Pritchett - RMP Consulting Partners LLC wrote:

: Actually, assembler is a more structured language than COBOL in one respect:

Which of the several hundred completely different 'assembler's are
you referring to ?

: Unless you resort to rather convoluted logic, there is no way in assembler
: both to perform a routine (i.e., to invoke it via a BAL) and to fall through
: it.

What actually stops you falling _into_ it ?  I suspect that
the inablity to fall _through_ it is that it will completely
screw up before it gets to the end.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** "Robert W. McAdams" <fambright@sigmais.com>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389F59A6.C7AC90C7@sigmais.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> In comp.lang.cobol Robert W. McAdams <fambright@sigmais.com> wrote:
> : Robert M. Pritchett - RMP Consulting Partners LLC wrote:
…[4 more quoted lines elided]…
> you referring to ?

What I said is true of all of the assemblers with which I am familiar.  I know of
no assembler (no machine code, actually) for which there is a provision that
allows you to either call a section of code as a subroutine or fall through it.

> : Unless you resort to rather convoluted logic, there is no way in assembler
> : both to perform a routine (i.e., to invoke it via a BAL) and to fall through
…[4 more quoted lines elided]…
> screw up before it gets to the end.

There's no reason it should "completely screw up before it gets to the end" if you
wrote with the intention that it should be possible to fall through it.  The
trouble is what happens at the end.  I've never seen a machine code that provided
a way to say, e.g., "execute the 18 instructions starting at the specified label
and then come back."  Instead, you have to code a return instruction of some kind
after instruction #18, and then the problem becomes how to prevent the return
instruction from blowing up when you fall through.

What's peculiar, in retrospect, is why the inventors of COBOL put a feature in the
language that isn't easily translatable into any computer's machine code, and
which also (if it is used) makes programs harder to read.


Bob
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<389F4BD1.8D0FD10@neo.rr.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz>`

```
Actually, mainframe assembly language does allow you to fall
through a "performed" routine.

Because of the side effect of BASR/BALR, one should NOT use it to
establish addressability to the immediately following code (In
DOS systems, this was THE protocol for the base program in a
partition).  If a "wild branch" lands on the BA_R of your
"subroutine" and you have a BALR/BASR coded thusly  BAxR  12,0 
and the code is "based" on GPR12, 12 is now correctly
initialized.  However, where this routine will exit, or return,
to may be quite difficult to determine.  And trying to solve this
kind of problem is a pure pain in the, uhmmm, neck.

Now, in another case, if BCT/BCTR is mis-used (among others), you
can fall through a routine, rather than looping some number of
times (the referenced Count register must contain 1 upon hitting
the BCT/BCTR for fall through - if it contains 0, the register
will be treated LOGICALLY -- unsigned -- and you may well loop
through this routine 2**32 times!).

In cases where the code is self-modifying OR is written using an
EX (EXecute of another instruction - this is an "immediate call"
of one instruction), it is quite possible to fall through a
routine or "perform" it.

So, yes, you can fall through "performed" code using mainframe
assembly.

Richard Plinston wrote:
> 
> In comp.lang.cobol Robert W. McAdams <fambright@sigmais.com> wrote:
…[19 more quoted lines elided]…
> -------------------------------------------------------------- */
```

###### ↳ ↳ ↳ BASR? (Was:You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** Warren Porter <wb999port@bellsouth12.net>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38A048AD.A78CF36A@bellsouth12.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz> <389F4BD1.8D0FD10@neo.rr.com>`

```
What does BASR do?  I used BAL & BALR (and have seen it generated in the back of
COBOL listings) but havn't been on an IBM mainframe for a while.  TIA

Steve Thompson wrote:

> Actually, mainframe assembly language does allow you to fall
> through a "performed" routine.
…[9 more quoted lines elided]…
> kind of problem is a pure pain in the, uhmmm, neck.
```

###### ↳ ↳ ↳ Re: BASR? (Was:You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<6FE339881E9DFA43.2E2B5FA2D7C49045.9D1714F5E257F85A@lp.airnews.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz> <389F4BD1.8D0FD10@neo.rr.com> <38A048AD.A78CF36A@bellsouth12.net>`

```
On Tue, 08 Feb 2000 10:47:42 -0600, Warren Porter
<wb999port@bellsouth12.net> enlightened us:

>What does BASR do?  I used BAL & BALR (and have seen it generated in the back of
>COBOL listings) but havn't been on an IBM mainframe for a while.  TIA
>

You should probably ask this question in comp.lang.asm370 for a more
thorough answer, but in short BASR is a mneonic used in TPF processing
on the mainframe in the OS/390 environment.  A short example is:

Program 0, which is the initial routine, is the initial entry to the
CP environment. Load the stack register with the proper stack from
prefix page. Call first routine. 

             Without Macros                    

               .                                  . 
               .                                  . 
               .                                  . 
               .                                  . 
               L   R13,PFXSSAVE                 
               .                                  . 
               .                                  . 
               .                                  . 
               .                                  . 
               ST  R15,STKR15(R13)                . 
               L   R15,=A(PROG1)                   
               BASR R14,R15   

Regards,
                    .
>Steve Thompson wrote:
>
…[11 more quoted lines elided]…
>> kind of problem is a pure pain in the, uhmmm, neck.

          ////
         (o o)
-oOO--(_)--OOo-

If the shoe fits, get another one just like it.


Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: BASR? (Was:You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<r9f3as4abfu290vju7ksenh4q68lvt6hno@4ax.com>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz> <389F4BD1.8D0FD10@neo.rr.com> <38A048AD.A78CF36A@bellsouth12.net>`

```
On Tue, 08 Feb 2000 10:47:42 -0600 Warren Porter <wb999port@bellsouth12.net>
wrote:

:>What does BASR do?  I used BAL & BALR (and have seen it generated in the back of
:>COBOL listings) but havn't been on an IBM mainframe for a while.  TIA

In 31 bit mode it is the same as BALR.

In 24 bit mode, BAS/R places zeroes in the high order byte of the return
address while BAL/R inserts the ILC, condition code and program mask.

BAS/R is slightly faster as it simply copies the low order word of the PSW.

   [ snipped ]
```

###### ↳ ↳ ↳ Re: BASR? (Was:You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** Warren Porter <wb999port@bellsouth12.net>
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<38A2311F.75B26759@bellsouth12.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz> <389F4BD1.8D0FD10@neo.rr.com> <38A048AD.A78CF36A@bellsouth12.net> <r9f3as4abfu290vju7ksenh4q68lvt6hno@4ax.com>`

```
Thanks.  Stands for Branch And Save? Register?!?  The high order bit info makes sense.

Binyamin Dissen wrote:

> On Tue, 08 Feb 2000 10:47:42 -0600 Warren Porter <wb999port@bellsouth12.net>
> wrote:
…[9 more quoted lines elided]…
> BAS/R is slightly faster as it simply copies the low order word of the PSW.
```

###### ↳ ↳ ↳ Re: BASR? (Was:You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38A25837.2312CFC@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <87kie1$rfv$1@aklobs.kc.net.nz> <389F4BD1.8D0FD10@neo.rr.com> <38A048AD.A78CF36A@bellsouth12.net> <r9f3as4abfu290vju7ksenh4q68lvt6hno@4ax.com> <38A2311F.75B26759@bellsouth12.net>`

```
Warren Porter wrote:
> 
> Thanks.  Stands for Branch And Save? Register?!?  The high order bit info makes sense.

IIRC, Branch & Store Register. Like BALR/BAL, there's a BASR/BAS, as
well. Interestingly enough, IBM recommended using BASx instead of BALx
in their manuals concerning using XA storage (sorry I can't remember the
titles, there were two of them - it was the early 90's). However, their
macros still generate BALx instructions.

Do as I say, not as I do?

Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 4)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ahfn4.139$as3.1999590@news.netdirect.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com>`

```
In article <389D59E6.D6306094@sigmais.com>, "Robert W. McAdams" <fambright@sigmais.com> wrote:
>Robert M. Pritchett - RMP Consulting Partners LLC wrote:
>
…[9 more quoted lines elided]…
>
Oh, sure there is -- all you have to do is forget to code the BR at the end of 
the *previous* routine. I've even seen some programs where this was done 
*intentionally*.
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net>`

```
On Sun, 06 Feb 2000 14:03:09 GMT, dxmixxer@netdirect.net (Douglas
Miller) enlightened us:

>In article <389D59E6.D6306094@sigmais.com>, "Robert W. McAdams" <fambright@sigmais.com> wrote:
>>Robert M. Pritchett - RMP Consulting Partners LLC wrote:
…[13 more quoted lines elided]…
>*intentionally*.

You can also load the return register with another address and go
somewhere completely different in your program (or out of your program
if you really screw up!).  That action would be akin to the ALTER verb
in Cobol.  You can also set the BR instruction to a NOP before you get
to it, thus rendering the return nil.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Do you need a silencer if you are going to shoot a mime? 


Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 6)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389E4F0E.A9268CED@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net> <9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net>`

```
SkippyPB wrote:
> 
(snip)
> 
> You can also load the return register with another address and go
> somewhere completely different in your program (or out of your program
> if you really screw up!). 

In this case the subroutine is still the classic single entry & single
exit. You're using the flexibility of the Assembler to cause the BR at
the end of the subroutine to return to somewhere other than the NSI of
whatever branch instruction gets you to the subroutine. 

> That action would be akin to the ALTER verb in Cobol.  You can also set the BR instruction to a NOP before you get
> to it, thus rendering the return nil.

Agghh, you're going to modify the program (not reentrant)?

Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F0E66D89DAC79BD9.8BCCEAED2970888B.486D2E00BDA9FD4F@lp.airnews.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net> <9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net> <389E4F0E.A9268CED@worldnet.att.net>`

```
On Mon, 07 Feb 2000 04:50:21 GMT, William Lynch
<wblynch@worldnet.att.net> enlightened us:

>SkippyPB wrote:
>> 
…[16 more quoted lines elided]…
>Bill Lynch

Not recommending any of these things.  Just commenting on what you can
do.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

If the shoe fits, get another one just like it.


Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87mrm4$df4$1@news.igs.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net> <9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net> <389E4F0E.A9268CED@worldnet.att.net>`

```
You are talking about one specific assembler.  I have worked in several
assemblers for pre-stack architectures that you could fall through in the
exact same way as Cobol.  The Mostek F8 comes to mind, as does the PDP-8,
though the PDP-8 stored the address in the call location, and would exit to
location zero if executed rather than called.  With *all* assemblers, it is
quite simple to code routines that would behave exactly like Cobol.  Out of
the dozen or so that I have coded for, I never saw one that would allow
topdown structure as a native construction.  In all cases, you had to code
the constructs required for topdown methods, either as macros or as actual
code.  That can be done in any language.

William Lynch wrote in message <389E4F0E.A9268CED@worldnet.att.net>...
>SkippyPB wrote:
>>
…[11 more quoted lines elided]…
>> That action would be akin to the ALTER verb in Cobol.  You can also set
the BR instruction to a NOP before you get
>> to it, thus rendering the return nil.
>
>Agghh, you're going to modify the program (not reentrant)?
>
>Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 8)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389FD82A.82B16F19@worldnet.att.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net> <9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net> <389E4F0E.A9268CED@worldnet.att.net> <87mrm4$df4$1@news.igs.net>`

```
donald tees wrote:
> 
> You are talking about one specific assembler.

Yes, it seemed to me that SkippyPB was discussing IBM's 360/370/390
Assembler. Let me toss in my standard disclaimer about my background
being limited to IBM mainframes.

Bill Lynch
```

###### ↳ ↳ ↳ Re: You're invited to critique my new Cobol page I started

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-02-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C2D795A8E45EBD18.F300A8BC4603BA7B.6C9CD1D537009CE4@lp.airnews.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net> <3891A410.7DABF28B@neo.rr.com> <pUpk4.3121$Sa2.119928@newsread2.prod.itd.earthlink.net> <389D59E6.D6306094@sigmais.com> <ahfn4.139$as3.1999590@news.netdirect.net> <9B5CDF2C62E2EBE4.6053C1502F578A45.942FB1817B2FF80D@lp.airnews.net> <389E4F0E.A9268CED@worldnet.att.net> <87mrm4$df4$1@news.igs.net> <389FD82A.82B16F19@worldnet.att.net>`

```
On Tue, 08 Feb 2000 08:47:36 GMT, William Lynch
<wblynch@worldnet.att.net> enlightened us:

>donald tees wrote:
>> 
…[6 more quoted lines elided]…
>Bill Lynch

You are correct.  I was.  The only other assembler I've ever coded in
was the PDP-11 and whatever it was the Commodore-64 used (so long ago
I don't remember).  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

If the shoe fits, get another one just like it.


Remove nospam to email me.

 Steve
```

#### ↳ Re: You're invited to critique my new Cobol page I started

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<3891A6DF.5DAB1507@NOSPAMwebaccess.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net>`

```


"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> It's at http://rmpcp.com/cobol.html - I'm not finished with it obviously
> but I think it's off to a good start.

The only web pages I do is documentation for programs.  One thing which
I have been trying to find out (I use Netscape Composer) is how to make
a URL open a new version of Navigator instead of using the old one. 
Then I saw your newsgroup message did that - How is this determined?
```

#### ↳ Re: You're invited to critique my new Cobol page I started

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** alt.computer.consultants,comp.lang.cobol
- **Message-ID:** `<86sekt$a28$1@news.cerf.net>`
- **References:** `<4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net>`

```
"Robert M. Pritchett - RMP Consulting Partners LLC" <EL.Bus.News@rmpcp.com>
wrote in message
news:4Z9k4.3741$%87.112611@newsread1.prod.itd.earthlink.net...
> It's at http://rmpcp.com/cobol.html - I'm not finished with it obviously
> but I think it's off to a good start.

My compliments. A structured and informative page. A pleasure to read your
main article which I found to be very informative. A real value for
programmers that are non Cobol and want to know what it is all about. I
believe non-programmers won't get much, but they are probably not the target
either?

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
