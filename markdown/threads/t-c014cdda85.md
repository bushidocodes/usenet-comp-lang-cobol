[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# STD: In-line comment indicator

_76 messages · 20 participants · 2000-01_

---

### STD: In-line comment indicator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8536vm$ifq$1@nntp5.atl.mindspring.net>`

```
The thread about what would be the best (nicest? most user-friendly?
whatever?) indicator for starting inline comments seems to be dragging on and
on.  Is this just a thread of "wishful thinking" or something else.

The bottom-line is that "*>" is in the draft - and barring some STRONG
argument against it, I doubt that there is much (any?) chance of it changing
now.

If someone really does want it to be changed, then I strongly suggest that
you URGENTLY get your input to J4 (before their Jan 17th meeting).  If not,
can someone tell me why we are still talking about "alternatives" that would
have been nice?

P.S.  As usual, if you want to send your comments to J4, send them to the
chair at:

     doncobol <at> mediaone.net

P.P.S.  No, I am not trying to stop discussion, I just can't tell if anyone
thinks that there is any point to the current thread.
```

#### ↳ Re: STD: In-line comment indicator

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1A52F7B4C4E25404.BFAE0E46CC3B73A0.53D8D14C04D45CE4@lp.airnews.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net>`

```
On Thu, 6 Jan 2000 17:04:41 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> enlightened us:

>The thread about what would be the best (nicest? most user-friendly?
>whatever?) indicator for starting inline comments seems to be dragging on and
…[17 more quoted lines elided]…
>thinks that there is any point to the current thread.

Like you said Bill, there probably isn't any way to change their
minds, but I personally don't like it.  In our company we have our own
4GL type language and a preprocessor that converts the 4GL commands to
Cobol syntax.  In our 4GL we use the /*  */ for inline comments.  Our
designers decided that  because most folks are familiar with writing
MVS JCL and it is similiar to the //* comment string it would be easy
to use.

In short, I'd like to se /*  */ for inline comments be the standard.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Should crematoriums give discounts for burn victims?


Remove nospam to email me.

 Steve
```

#### ↳ Re: In-line comment indicator

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net>`

```
    The discussion seems to have settled on "Does the draft standard say
anything about multiline
comments".  Ie, like the /*   */ pair used in C or Pascal, where entire
blocks of code
can be commented out, like we do now with the "$IF 1 = 0"    "$END"   pair.

    Of course, it that will continue to work, why bother.



William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:8536vm$ifq$1@nntp5.atl.mindspring.net...
> The thread about what would be the best (nicest? most user-friendly?
> whatever?) indicator for starting inline comments seems to be dragging on
and
> on.  Is this just a thread of "wishful thinking" or something else.
>
> The bottom-line is that "*>" is in the draft - and barring some STRONG
> argument against it, I doubt that there is much (any?) chance of it
changing
> now.
>
> If someone really does want it to be changed, then I strongly suggest that
> you URGENTLY get your input to J4 (before their Jan 17th meeting).  If
not,
> can someone tell me why we are still talking about "alternatives" that
would
> have been nice?
>
…[5 more quoted lines elided]…
> P.P.S.  No, I am not trying to stop discussion, I just can't tell if
anyone
> thinks that there is any point to the current thread.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: In-line comment indicator

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3875D11D.D44B9B5A@zip.com.au>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com>`

```
Russell Styles wrote:
> 
>     The discussion seems to have settled on "Does the draft standard
…[3 more quoted lines elided]…
>  pair.

Good idea.

I would personally vote against multiline comments.  I now use '//'
almost exclusively in my C coding (which is compiled under C++ for
tighter checking).  Is is dead clear and it is simple to work with
especially when your editor automatically continues them.

The down side to multiline comments is you simply forget to finish
them.  Not a major issue now with highlighting editors but a lot of
people don't like highlights and switch it off.  Keep the errors out
at the source.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: In-line comment indicator

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3875FD5A.61FF6BA@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au>`

```
The major advantage to a multi-line comment is that it is easy to
comment out a block of code, and uncomment it again later.  Column 7
asterisks aren't sufficient as that block may already have commented out
code - how do you know what to uncomment?

But it is pretty easy now to comment out a paragraph.  Just duplicate
the paragraph name, add an exit, and rename the old paragraph to
something unique:

PERFORM MY-ROUTINE.

MY-ROUTINE. EXIT.
MY-ROUTINE-commented-out.
   ...

I will sometimes use my initials to change:
       ADD 1 TO X.
  *    ADD 3 TO Y.
       ADD 4 to Z.

to
  **hjb commented code starts here
  **hjb ADD 1 to X.
  *     ADD 3 to Y.
  **hjb ADD 4 to Z.
  **hjb commented code ends here.

The trick is that it is necessary for me to know what to uncomment
later.
If I could do:
       /**  block comment starts here
       ADD 1 TO X.
  *    ADD 3 TO Y.
       ADD 4 to Z.
       **/   block comment ends here 

And be able to nest block comments, this could be nice for keeping some
source code which you don't currently want compiled.   A color
highlighting editor would help here.

Do any of the highlighting editors print with the highlight colors?
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<855g45$gdt$1@aklobs.kc.net.nz>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net>`

```
Howard Brazee <brazee@nospamwebaccess.net> wrote:
: The major advantage to a multi-line comment is that it is easy to
: comment out a block of code, and uncomment it again later.  Column 7
: asterisks aren't sufficient as that block may already have commented out
: code - how do you know what to uncomment?

Sorry, but multiline comments are a poor way of disabling a block
of code.  Comments are for commenting, not for source code
control.  There is exactly the problem with multiline comments
that you raise for '*' - the code may already contain a multiline
comment, the terminator of which may terminate the outer one.

Of course one could then insist on nested comments, but these
bring their own problems.

One way of using col 7 asterisks to do source control is easy if
you have an adequate text editor (such as TSE that I use) that has
a block shift function.  Block the code, shift one character
right to preserve the existing comments and add '*' in col 7.

This can be done and undone by a macro which could also add
a couple of bounding lines indicating when done.

: But it is pretty easy now to comment out a paragraph.  Just duplicate
: the paragraph name, add an exit, and rename the old paragraph to
: something unique:

: PERFORM MY-ROUTINE.

: MY-ROUTINE. EXIT.
: MY-ROUTINE-commented-out.
:    ...

This only works if an adequate coding style is used (as I am sure that
yours is).  If this does not work for someone then they should
change their style     ;-)

: If I could do:
:        /**  block comment starts here
:        ADD 1 TO X.
:   *    ADD 3 TO Y.
:        ADD 4 to Z.
:        **/   block comment ends here 

: And be able to nest block comments, this could be nice for keeping some
: source code which you don't currently want compiled.   A color
: highlighting editor would help here.

If the block was extensive (ie more than one screenful) then it
may be that a search would show the code without the comment
start or end markers which would be above and below the current
view.  This may cause confusion.

Even if you print (do people still use paper for programming ?)
it may be that the start and end fall outside the current page.

Shift right one charcter and '*' in col 7 is reliable and reversable
and cannot be missed.
```

###### ↳ ↳ ↳ OT - Have you ever heard of version control software? WAS: In-line comment indicator

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89ud4.13553$g12.438711@news2.rdc1.on.home.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <855g45$gdt$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@kcbbs.gen.nz> wrote in message
news:855g45$gdt$1@aklobs.kc.net.nz...
> Howard Brazee <brazee@nospamwebaccess.net> wrote:
> : The major advantage to a multi-line comment is that it is easy to
…[6 more quoted lines elided]…
> control.

I could not agree more!

Commenting out code is archaic. Delete the damn lines and rely on your
version control software to be able to go back versions should you need to.
What's that you say? You don't have version control software? Get some.
There's nothing worst than wading through unused code, or multiple copies of
unused code trying to separate the wheat from the chaff.

I cannot begin to count the number of times I've been to a client site
sorting out the mess of stuff they call their 'mission critical' software.
They have no idea what assets they have, which one of a dozen versions of
copybooks were used to build a program, or where to start untangling the
mess.

If you are looking for a good, cheap solution try cvs
(http://www.sourcegear.com/CVS). The price is right because it's free. It
may cost you some time configuring it, but the payback is enormous. Store
your build scripts, configuration files and development tools as well since
they're likely to change over time as well.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 4)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<esuTbjiW$GA.263@cpmsnbbsa03>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net>`

```
It seems that you could use a GO TO to branch around the coding you don't
want executed. The compiler should recognize that Code is not used.

123456           GO TO TEMP-BYPASS.
123456          ....... Code without '*" in col 7.
123456 TEMP-BYPASS.

You don't need to worry about currently existing comment lines.
To reinstate the coding remove the GO TO, and Paragraph.
I am of course assuming that you are bypassing the code for debuggging or
testing.

As for commenting out code and leaving it in a program, you can do it. But
if I have to maintain it, they will be gone. People do this because they
aren't sure about what they have done. I don't care about the history of a
routine, I care about what it does now.
As for dates and initials in columns 1-6. I usually set my text editor to
show 7-72. A Renumber in ISPF will wipe this stuff out.

As for in-line comments, I would probably not use them. They would make
Global changes and shifting text more difficult.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3879F8D7.892FE78A@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <esuTbjiW$GA.263@cpmsnbbsa03>`

```
DennisHarley wrote:
> 
> It seems that you could use a GO TO to branch around the coding you don't
…[4 more quoted lines elided]…
> 123456 TEMP-BYPASS.

If there is a label where you want it.  If you want to skip the rewrite
line within an in-line perform you have much more work and chance of
error.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OfTOiE4W$GA.236@cpmsnbbsa02>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <esuTbjiW$GA.263@cpmsnbbsa03> <3879F8D7.892FE78A@NOSPAMwebaccess.net>`

```
Have you ever had to rerun a weeks worth of work because someone turned over
a program with the "temporaily" commented code still commented out?

Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:3879F8D7.892FE78A@NOSPAMwebaccess.net...
> DennisHarley wrote:
> >
> > It seems that you could use a GO TO to branch around the coding you
don't
> > want executed. The compiler should recognize that Code is not used.
> >
…[6 more quoted lines elided]…
> error.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387A1588.2B8D6DE4@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <esuTbjiW$GA.263@cpmsnbbsa03> <3879F8D7.892FE78A@NOSPAMwebaccess.net> <OfTOiE4W$GA.236@cpmsnbbsa02>`

```
DennisHarley wrote:
> 
> Have you ever had to rerun a weeks worth of work because someone turned over
> a program with the "temporaily" commented code still commented out?
> 

No, have you ever had to rerun a week's worth of work because someone
turned over a program with the "temporarily" deleted code still deleted?

Commented out code with words such as 
**** hjbdebug temporary removing next lines:

is much less likely to pass change control than missing lines.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net>`

```
Let me suggest heresy. If the code is going to be commented out, why the
hell not just delete it?

I do.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 5)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8569o1$crki$1@newssvr03-int.news.prodigy.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net>`

```

If the program is short and easy to understand, I would agree.  For longer
programs though, it's been my experience that 90% of the problems are
related to the most recent program change.  Since added, changed and deleted
code all fall into this category, I usually comment out deleted code until
the next time the program gets changed, then I delete the commented code.
I've found that others who maintain these programs usually appreciate a hint
as to what the most recent changes were.  The bottom line for me though is
that each case is individual and we all should use our best judgment as to
how (or how not to) indicate recent changed code.

Michael Mattias <michael.mattias@gte.net> wrote in message
news:_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net...
> Let me suggest heresy. If the code is going to be commented out, why the
> hell not just delete it?
…[9 more quoted lines elided]…
> >comment out a block of code, and uncomment it again later.
```

###### ↳ ↳ ↳ OT: PC Change control

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3877223D.CA1AD9E9@zip.com.au>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <8569o1$crki$1@newssvr03-int.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> If the program is short and easy to understand, I would agree.  For
…[8 more quoted lines elided]…
> how not to) indicate recent changed code.

As pointed out the version control system should cover this.  If you
don't have one use CVS, it's free.

BTW:  Who has experience in PC version control.  Does anyone know if
there is a SCCS compatible PC product (our unix is SCCS, I'd rather be
consistent).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 5)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3876AF58.24D9C936@worldnet.att.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> Let me suggest heresy. If the code is going to be commented out, why the
> hell not just delete it?

Gets my vote.

> I do.

Me, too. I want the source I'm looking at to be the program I'm running.
'Not interested in the changes for multi-bank support in '89, etc. My
employer uses Endevor, so it's a trivial matter to view the changes, if
that's what I'm interested in. I really find a lot of commented out code
& dates in 1-6 a distraction.

Bill Lynch
Proud Survivor of Y2K
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CYKd4.9605$J%4.12617@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3876AF58.24D9C936@worldnet.att.net>`

```
If I weight the pros and cons of saving old code, the cons win.

While I can count on one hand the number of times I've used "the old code"
as a reference, I can't count even using all digits and appendages how many
times I've been fooled by...

099990        MOVE 4 TO KITTY.
100000*       IF  DOGGY EQUAL 6
100010              PERFORM WALK-THE-DOG.
100020        PERFORM POOPER-SCOOPER.

Granted, whomever commented out the "IF " statement did a really (expletive)
thing here, not re-indenting the PERFORM of WALK-THE-DOG, or leaving a note,
but damn if this isn't real life.

MCM

William Lynch wrote in message <3876AF58.24D9C936@worldnet.att.net>...
>Michael Mattias wrote:
>>
…[11 more quoted lines elided]…
>& dates in 1-6 a distraction.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3879F833.918CD605@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3876AF58.24D9C936@worldnet.att.net> <CYKd4.9605$J%4.12617@dfiatx1-snr1.gtei.net>`

```
But I have commented out IN PROCESS code.  I am debugging a program, and
want to skip a process which isn't part of the problem.  I comment out
that process.  

I can do the following:

**hjbdebug    PERFORM REWRITE ROUTINE.

But if it is in-line code, I have to comment it out line by line.  When
I am done debugging the problem, I need to restore this part of the
program.

It isn't a comment for some future maintenance programmer to see what I
have "deleted", (that is rare), but a comment to skip processing some
code which will make my test either resource heavy or updating what I
don't want updated right now.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-FWn5c8v6ropz@localhost>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3876AF58.24D9C936@worldnet.att.net>`

```
On Sun, 7 Jan 3900 22:30:32, William Lynch <wblynch@worldnet.att.net> 
wrote:

> Michael Mattias wrote:
> > 
…[4 more quoted lines elided]…
>

Just yesterday I released some code with a whole section commented 
out.  You see there were two different ways to present the data.  The 
old way I commented out, and included the new way.  The client can use
whichever they desire - both are still available.

-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3879F4DA.E9D49AE8@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net>`

```
It is much harder to undelete deleted code than to uncomment commented
code.

Michael Mattias wrote:
> 
> Let me suggest heresy. If the code is going to be commented out, why the
…[10 more quoted lines elided]…
> >comment out a block of code, and uncomment it again later.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eL3ea93W$GA.269@cpmsnbbsa04>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3879F4DA.E9D49AE8@NOSPAMwebaccess.net>`

```
It is siligtly more difficult in most instances.

It depends on the change management practices of the installation, the
programmer, and the source library software being used.

If you have 2 versions of the same program you can run a file compare
utility to find the changes.

Commented out code, and dead code are a royal pain in the butt.
They make maintenance, and trouble shooting more difficult.

Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:3879F4DA.E9D49AE8@NOSPAMwebaccess.net...
> It is much harder to undelete deleted code than to uncomment commented
> code.
>
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387A13F6.A2ABFEC9@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3879F4DA.E9D49AE8@NOSPAMwebaccess.net> <eL3ea93W$GA.269@cpmsnbbsa04>`

```
When I am working on a program, the only change management is what I do
myself.  Only when I migrate it to production does this enter in.

Maintenance and trouble shooting don't apply here - I will uncomment out
my code or delete it before I migrate.

DennisHarley wrote:
> 
> It is siligtly more difficult in most instances.
…[14 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85e2k4$p9v$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3879F4DA.E9D49AE8@NOSPAMwebaccess.net>`

```

Howard Brazee wrote in message <3879F4DA.E9D49AE8@NOSPAMwebaccess.net>...
>It is much harder to undelete deleted code than to uncomment commented
>code.
>
CD ROM backup is *real* cheap.  Set up an archive.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387B3B66.4C7124EE@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3879F4DA.E9D49AE8@NOSPAMwebaccess.net> <85e2k4$p9v$1@news.igs.net>`

```
donald tees wrote:
> 
> Howard Brazee wrote in message <3879F4DA.E9D49AE8@NOSPAMwebaccess.net>...
…[3 more quoted lines elided]…
> CD ROM backup is *real* cheap.  Set up an archive.

I am not making myself clear.  I am doing maintenance on a program.  I
make significant changes in one part of the program and to test it, I
need to disable another part of that same program.  Once the testing is
finished I want to include both the disabled part (now enabled again)
and the newly changed part of the program.  I have an archive, that is
no problem - but merging two copies of a program give me more chances of
errors than simply removing the block comment.

This is where I would like to have the ability to safely comment out
blocks of code.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85gq4h$ftu$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <3875FD5A.61FF6BA@NOSPAMwebaccess.net> <_Dwd4.1009$tn3.22489@dfiatx1-snr1.gtei.net> <3879F4DA.E9D49AE8@NOSPAMwebaccess.net> <85e2k4$p9v$1@news.igs.net> <387B3B66.4C7124EE@NOSPAMwebaccess.net>`

```
Yes, that makes lots of sense.  When I do that, though, I want to SEE it,
not see it.  I use a macro that puts eight asterisks as the first eight
characters of each and every line blocked out. Another macro removes them. I
can scan that and spot it at 9600 baud.  Makes it easy to search for too.

Howard Brazee wrote in message <387B3B66.4C7124EE@NOSPAMwebaccess.net>...
>donald tees wrote:
>>
…[15 more quoted lines elided]…
>blocks of code.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85907g$5au$1@nntp3.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote in message
news:3875D11D.D44B9B5A@zip.com.au...
> Russell Styles wrote:
> >
…[16 more quoted lines elided]…
> at the source.

I like C's preprocessor #IF and #ENDIF in order to temporarily comment out
lines of code during testing without actually changing the lines themselves.
(Our editor for COBOL at work puts a new date on the line if anything is
changed, even if you change it back later.)  I believe that the new COBOL
standard has something similar, does it not?
```

###### ↳ ↳ ↳ STD: In-line comment indicator

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85922p$ug1$1@nntp1.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <3875D11D.D44B9B5A@zip.com.au> <85907g$5au$1@nntp3.atl.mindspring.net>`

```
The draft standard DOES include

>>IF ... >>ELSE ... >>END-IF

 as well as

>>EVALUATE ... >>WHEN ... >>END-EVALUATE

support.  I wouldn't call this "block comment" support, but it certainly
could be used for that purpose.
```

##### ↳ ↳ STD: Re: In-line comment indicator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<854svd$3u9$1@nntp1.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com>`

```
No, the Standard specifically ONLY addresses comments on a single line, e.g.

If A = B               *>  This is  the
    Display "X"    *> way that you would do
                            *> Multiple lines of comments
Else
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<856abc$9oo$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net>`

```
William M. Klein wrote in message <854svd$3u9$1@nntp1.atl.mindspring.net>...
>No, the Standard specifically ONLY addresses comments on a single line,
e.g.
>
>If A = B               *>  This is  the
…[3 more quoted lines elided]…
>
I like that.  I used to write a lot of assembler, and had as a shop spec
that EVERY line had to have a comment as itemized above.  The effect was a
running dialog of what the code did on the right, with the assembler on the
left.

What I always liked about Cobol, was that the code read like comments.  It
was so easy to read that you did not need to write a dialog explaining what
you were doing.  In fact, I was taught that if your Cobol code was so poorly
written that you needed comments to explain what it did, then you were a
piss-assed-poor programmer.
;<)
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387722FA.808A4B97@zip.com.au>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net>`

```
donald tees wrote:
> 
> 
…[4 more quoted lines elided]…
> explain what it did, then you were a piss-assed-poor programmer.

There was a similar thread on comp. object and the conclusion was
exactly the same.

Good code is lightly sprinkled with comments, to many comments becomes
a repeat of the programming statements anyway.  This is useless,
effective commenting is hard!

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DYKd4.9607$J%4.12617@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <387722FA.808A4B97@zip.com.au>`

```
While I am guilty (?) of excessive commenting in terms of "number of lines"
of code (at least if you keep score that way) , most of those comment lines
come at the start of procedures, as in...


     PRICE-ROUTINE.
  * Get customer's price for an item
  * PERFORMed once for each detail record processed
  * INPUT: THE-PART-NUMBER, CUSTOMER-NO
  * OUTPUT: THE-PRICE

       BLAH BLAH BLAH...


Since I tend to write COBOL using very tiny paragraphs, I end up with a lot
of comment lines.

I really like the lateral (in-line) comments. As a BASIC language
programmer, I'm very used to using the apostrophe to put a comment on
individual lines, as in...

      FOR J = 1 TO NumLines
         GET #Partfile, Partno, PartRec
         PriceQty = OrderRec.Qty / PartRec.HowPriced         ' convert unit
of measure
         CALL GetPrice (CustomerNo, PartNo, PriceQty,Price)
         IF PartRec.ITemClass = taxable
          blah blah blah

MCM

Ken Foskey wrote in message <387722FA.808A4B97@zip.com.au>...
>Good code is lightly sprinkled with comments, to many comments becomes
>a repeat of the programming statements anyway.  This is useless,
>effective commenting is hard!
>
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387879D9.1CB4D10A@zip.com.au>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <387722FA.808A4B97@zip.com.au> <DYKd4.9607$J%4.12617@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> While I am guilty (?) of excessive commenting in terms of "number of
…[7 more quoted lines elided]…
>   * OUTPUT: THE-PRICE

Rename the procedure to get-customers-price and remove the comment. 
The input and output statements are nice and an unfortunate result of
the perform statement in cobol, you implicitly pass information in and
implicitly receive information from it.

With calls (or OO and invoke) you explicitly pass the fields into the
method and receive the data from the call explicitly.  That is so long
as you avoid globals like the plague.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k0e4.26315$J%4.49053@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <387722FA.808A4B97@zip.com.au> <DYKd4.9607$J%4.12617@dfiatx1-snr1.gtei.net> <387879D9.1CB4D10A@zip.com.au>`

```
Ken Foskey wrote in message <387879D9.1CB4D10A@zip.com.au>...
>Michael Mattias wrote:
>>
…[14 more quoted lines elided]…
>


My BASIC code uses almost exclusively passed values, even my Windows code,
where you need to really think things through to avoid (the BASIC
equivalents of) GLOBALs.

This GLOBAL thing is why I was asking last week about the difference between
"stacked" and "nested" multiple-programs-per-COBOL-source-code-file
construction. All I could see with the nested contstruction was that it
facilitated the "feature" (Yechh!) of being able to easily make certain data
GLOBAL; except avoiding GLOBAL data was why I broke up the program in the
first place.

MCM
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mJHd4.5749$ps.67984@news4.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net>`

```
donald tees wrote:
>
>What I always liked about Cobol, was that the code read like comments.  It
…[4 more quoted lines elided]…
>;<)

Sometimes comments are helpful to provide overall perspective, even
when the code itself is crystal clear.  For example, in algorithms that
are complex or somewhat abstract, I like to describe the algorithm in
a comment block, so the reader will know 'why' the code is doing what
it is, even if the 'what' is obvious.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<858bob$gqb$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia>`

```
Yes, I do the same.  But that is about one paragraph per thousand. 99
percent of all paragraphs are not complex or abstract, at least not in
business data processing.

Judson McClendon wrote in message ...
>donald tees wrote:
>>
>>What I always liked about Cobol, was that the code read like comments.  It
>>was so easy to read that you did not need to write a dialog explaining
what
>>you were doing.  In fact, I was taught that if your Cobol code was so
poorly
>>written that you needed comments to explain what it did, then you were a
>>piss-assed-poor programmer.
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85920g$c3e$2@nntp3.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net>`

```
donald tees <donald@willmack.com> wrote in message
news:858bob$gqb$1@news.igs.net...
> Yes, I do the same.  But that is about one paragraph per thousand. 99
> percent of all paragraphs are not complex or abstract, at least not in
> business data processing.

I don't know about that.  I work in banking and ATM processing, and some of
the business logic makes no sense unless there's a comment specifically
saying "this is the rule, and this is why the logic is this way."  The
programmer who's working on it does not necessarily know the business rules
behind each line of code.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8592r9$vqe$1@nntp1.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <85920g$c3e$2@nntp3.atl.mindspring.net>`

```
Frank Swarbrick <infocat@sprynet.com> wrote in message
news:85920g$c3e$2@nntp3.atl.mindspring.net...
> donald tees <donald@willmack.com> wrote in message
> news:858bob$gqb$1@news.igs.net...
…[9 more quoted lines elided]…
>

Long ago and far away <G> when I did COBOL programming for a "major utility,"
I would run into comments similar to this -

   This is the algorithm required by California Senate Bill 1234 which is
     due for review in June of 1984.  Please review the algorithm at that
time
     and update the algorithm to meet the then current regulations.
     NOTE: Table-1234 is updated Jan 15 each year.

I would also get comments like

  This is the logic required by the taxing laws in counties ABC, XYZ, and
LMN.
    For the logic required in counties DEF, GHI, and QRS, see
     pargraph 1234-Other-Counties.

Somehow, no amount of 88-levels is going to "explain" those !!!
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8593c7$2jj8$1@newssvr04-int.news.prodigy.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <85920g$c3e$2@nntp3.atl.mindspring.net>`

```

Frank Swarbrick <infocat@sprynet.com> wrote in message
news:85920g$c3e$2@nntp3.atl.mindspring.net...
> donald tees <donald@willmack.com> wrote in message
> news:858bob$gqb$1@news.igs.net...
…[4 more quoted lines elided]…
> I don't know about that.  I work in banking and ATM processing, and some
of
> the business logic makes no sense unless there's a comment specifically
> saying "this is the rule, and this is why the logic is this way."  The
> programmer who's working on it does not necessarily know the business
rules
> behind each line of code.
>
…[4 more quoted lines elided]…
> Hunt"

I think Frank makes a valid point.  Even though COBOL is COBOL, each
business implements it in a different way, and one of the most difficult
aspects of programming (in my experience) has been to translate the business
rules into COBOL code.  Also, each business has it's own
conventions/standards which may (or may not) make the coding easy or more
difficult to read for a newcomer to that particular shop.  As I mentioned
before, each case is individual and the best we can do is to make our own
value judgments based on our prior experience and the rules of the shop
we're programming for.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cQle4.347$lb5.2288@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net>`

```
The percentage of the code that needs these comments depends on what kind
of programs are being written.  I do agree that, out of all COBOL code,
only a small percentage needs the kinds of comments I'm talking about.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387a7d02_1@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia>`

```
show us ONE

Judson McClendon <judmc@bellsouth.net> wrote in message
news:cQle4.347$lb5.2288@news3.mia...
> The percentage of the code that needs these comments depends on what kind
> of programs are being written.  I do agree that, out of all COBOL code,
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9xIe4.3106$lb5.37933@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net>`

```
Leif Svalgaard wrote:
>show us ONE

You're beating a dead horse.  I've already explained that the only
COBOL examples I have are so involved and embedded into existing
systems that it would take too much effort to give you the necessary
background to understand the situation.  I can remember writing some
that were not very long, I just don't have any at hand.  Why is it
so difficult to understand that if you do not understand the reason
an algorithm works, you are not in a position to debug or modify it,
and that some algorithms use principles or rules that are not
reflected in the code itself in any obvious way?  Sure, a competent
programmer should be able to look at code and figure out what it is
actually doing, in a direct sense.  But if he doesn't know *why* the
code is supposed to work, he is unable to fix it if it is broken, or
to modify it successfully.  I would think this should be obvious,
even to a non-programmer.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387bf1db_4@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <9xIe4.3106$lb5.37933@news3.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:9xIe4.3106$lb5.37933@news3.mia...
> Leif Svalgaard wrote:
> >show us ONE
…[4 more quoted lines elided]…
> background to understand the situation

I thought that was the reason for the comments in the first place.
The way I read your original post of this was that you had constructions
like this:

N lines of explanations of complex code
M lines of complex code that could not be understood
    without the above N lines of explanation.

By definition N is large (otherwise the code is not complex)
and sometimes M is large as well.

What background information is needed to show
N lines followed by M lines?

But, maybe you can't get much out of a dead horse, so
forget it.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator (big!)

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JCJe4.3235$lb5.39214@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net>`

```
Leif Svalgaard wrote:
>show us ONE

Okay, okay!  Just so you'll know I'm not blowing smoke, I'll post one.
I warned you that the only ones I had available were big, so please
don't everyone jump on me for making such a large post.  Even though
it's a large post, there should be routines there that people can use,
so it isn't a complete waste.  It will also take a fair amount of
explaining, so bear with me.

Below are extracted some Working Storage and Procedure Division code
from a program I wrote about 10 years ago.  The program accepts data
from fetal ultrasound measurements (not image data).  It calculates
certain parameters indicating fetal development progress, then prints
a short report including 4 graphics charts plotting fetal development
against established norms.  The only problem is that this program runs
on an EBCDIC mainframe, and the report is transmitted over a 7 bit
ASCII connection to a laser printer connected to a PC, and the laser
printer needs an 8 bit binary stream for the raster graphics images.
The program builds the charts in a 'bit image' table, using one digit
for each bit to make COBOL coding simpler.  The completed chart is
then send raster line by raster line to the printer on the PC.  There
are two problems with sending the binary data to the PC printer.  One
is that the communications is only 7 bits, the other is that the data
will go through an automatic EBCDIC to ASCII conversion in the comm
hardware.  The conversion is necessary for the textual part of the
report, and the text portion of the printer commands, but would trash
the binary data.  To avoid this problem, the binary data is broken down
into 6-bit packets, each of which is converted into a printable EBCDIC
character that, when converted to ASCII, is a printable ASCII character
that when decremented by a fixed offset, returns the original 6 bit
binary packet.  An escape sequence is coded into the data to indicate
when the coded binary data starts and stops.  I wrote a printer driver
on the PC to intercept the escape sequences and reassemble the 6 bit
binary packets back into 8 bit bytes sent to the printer.  As the raw
graphics chart is being converted into horizontal lines of dots for the
printer, an additional complication is that the binary data must be
compressed according to the printer manufacturer's algorithm, to reduce
the huge amount of data being sent over the (then) 9600 BPS line.  The
compressed print line is then sent to the PC using the 6 bit packet
coding method described above for the binary portions.

I've stripped out the report code, except for the part performing
the graphics and print routines.  The code below is the WS data areas
used by the graphics primitives, the chart drawing code, and the
printer graphics, compression and coding data areas, followed by the
graphics and print routines themselves.  The code is highly commented.
In light of the very complex and unorthodox processes being used here,
I am looking forward to seeing how you propose to code the functions
below using no comments, yet making the process just as clear to the
maintenance programmer as the code below is, with liberal comments. :-)

Then, when you submit your solution, let's take a survey on which one
the other programmers would rather face for the first time at 2AM on
a Sunday morning. ;-)
```

###### ↳ ↳ ↳ Re: In-line comment indicator (big!)

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387BA6CF.EB475B45@home.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <JCJe4.3235$lb5.39214@news3.mia>`

```


Judson McClendon wrote:
> 
> Leif Svalgaard wrote:
> >show us ONE
> 
> Okay, okay!  Just so you'll know I'm not blowing smoke, I'll post one.

I really do have to support Judson on this one. Probably over 95% of my
code is written without comments, using meaninful variables to convey
what I want. Move away from the standard bookkeeping stuff, and there
are just instances where it is essential to convey what is going on.
I recall Judson mentioned statistical as an area. The following is not
statistical - but not having the remotest comprehension of Einstein and
all his concepts, you'll see that this rocket scientist got the user to
write me examples so I could test values against the results. 

Is anybody seriously suggesting that it would be possible to comprehend
the following method (previously a paragraph in RM/COBOL) without the
'header' example to let me zero-in on the 'lowest reading', as 'defined'
by the user ?

And pulh-eese don't ask me to explain it - it would take me about half
an hour at least to get into "claculation think mode" <G>

 *>-------------------------------------------------------------- 
 Method-id.  "R100-loss-lowest".                                  
 *>-------------------------------------------------------------- 
*                                                                 
*> PERIOD 2 :                                                     
*> ----------                                                     
*> Period Loss =  (c) - (c - 1 ) * 12000 / Current Time (c)       
*>----------------------------------------------------------------
*>               Sep    Sep   Current  Period                     
*>              1987   1991    Time    Loss                       
*>-------------------------------------------------               
*>Current time           48                                       
*>Total time             48                                       
*>----------------------------------------------------------------
*> Top     1           .960    /  0      .0                       
*>         2           .922    /  0      .0                       
*>         3           .872    /  0      .0                       
*>         4    .890   .852    / 48    -9.5 = Pd Max Loss & Temp Loss
*>         5    .839*  .849*   / 48    +2.5                       
*> Bottom  6    .886   .862    / 48    -6.0                       
*> -------------------------------------------------------------  
*>                                    -13.0 / 6 = -2.2 = Pd Avg Loss
*                                                                 
*>PERIOD 3 :                                                      
*>---------                                                       
*> ---------------------------------------------------------------
*> Period Loss =  (c) - (c - 1 ) *  12000 / Current Time (c)      
*>----------------------------------------------------------------
*>               Sep    Dec           Period                      
*>              1991   1992           Loss                        
*>----------------------------------------------                  
*>Current time    48     15                                       
*>Total time      48     63                                       
*>----------------------------------------------                  
*> Top     1    .960   .954  / 15 =  - 4.8                        
*>         2    .922   .910  / 15 =  - 9.6                        
*>         3    .872   .868  / 15 =  - 3.2                        
*>         4    .852   .845  / 15 =  - 5.6                        
*>         5    .849*  .832* / 15 =  -13.6* = Pd Max Loss & Temp Loss
*> Bottom  6    .862   .847  / 15 =  -12.0                        
*> ---------------------------------------------------------      
*>                                   -48.8 / 6 = -8.1  = Pd Avg Loss
                                                                  
*> NOTE: Having stored the "true" lowest reading "R70-columns", the
*> routine stores as ws-lowest-reading (C) the reading associated 
*> with the ITEM-period-maximum-loss (c). ws-lowest-reading (c) is
*> then used at "S40-life-expectancy" for Life-expectancy         
*> calculation                                                    
                                                                  
 Local-Storage section.                                           
 78 PointInternalBevel                 value 36.                  
 Linkage Section.                                                 
 01 c                                  pic x(4) comp-5.           
 01 n                                  pic x(4) comp-5.           
                                                                  
 Procedure Division using c, n.                                   
                                                                  
   compute READING-period-loss (N) rounded =                      
   ( (READING-value (N, C) - READING-value (N, C - 1))            
      * 12000 ) / ws-current-time (C)                             
                                                                  
   if READING-period-loss (N) <> zeroes                           
      add READING-period-loss (N) to ws-AccumLoss (C)             
                                                                  
      if  READING-point-code (N) <> PointInternalBevel AND        
          READING-period-loss (N) not >                           
          ITEM-period-maximum-loss (C)                            
          invoke self "R105-check-lowest" using c, n              
     End-if                                                       
                                                                 
   End-if                                                         
 End Method "R100-loss-lowest".                                   
 *>---------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: In-line comment indicator (big!)

_(reply depth: 10)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387bef03_1@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <JCJe4.3235$lb5.39214@news3.mia> <387BA6CF.EB475B45@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:387BA6CF.EB475B45@home.com...
> Is anybody seriously suggesting that it would be possible to comprehend
> the following method (previously a paragraph in RM/COBOL) without the
> 'header' example to let me zero-in on the 'lowest reading', as 'defined'
> by the user ?

several comments (no pun):
1) the comments do not say the same as the code,
e.g.:   Period Loss (n,c) = value(n,c) - value(n,c-1) * 12000 /
CurrentTime(c)
would have been more to the point.
2) no need to repeat the wrong comment twice
3) finding the smallest value seems to be a simple thing, I don't see
how the elaborate example helps with this.
4) in judging the usefulness of comments YOU are never the
judge, the other guy (in casu: ME) is, because the comments
were supposedly made for him. And I did not find your comments
useful at all.

>
>  *>--------------------------------------------------------------
…[71 more quoted lines elided]…
>  *>---------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 8)_

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387BBA73.9AE7AB21@boeing.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> show us ONE
> 
I tend to comment short things that remind me what the intent of the
paragraph is, also to document assumptions about the data.  Over the
years I have found that the customer does not always understand all of
their own data.

a sample of my comments:

005090 	 C1-INIT-WORK-AREA.                                             
005100 	*    DISPLAY '-> DEBUG C1-INIT-WORK-AREA'                       
005110 	*---------*---------*---------*---------*---------*---------*   
005120 	* ** FOR FIRST B-TBLE RECORD INITIALIZE ALL HOLD AREAS          
005130 	* ** RE-INIT IS SKIPPED FOR LARGE GROUPS (OVER TABLE MAX)       
005140 	*---------*---------*---------*---------*---------*---------*   
005150 	     INITIALIZE HOLD-FIELDS.                                    
005160 	     INITIALIZE HOLD-NUMERIC-FIELDS                             
005170 	     SET H-IDX                       TO 1.                      
005180 	     MOVE SPACE                      TO H-TBLE-AREA.            
005190 	     MOVE 1                          TO H-CNT.                  
005200 	     MOVE W-SC                       TO LOCAL-SC-SW.            
005210 	     IF W-VALID-JOB = 'N'                                       
005220 	         MOVE 'N'                    TO VALID-JOB-SW            
005230 	     ELSE                                                       
005240 	         MOVE 'Y'                    TO VALID-JOB-SW            
005250 	     END-IF.                                                    
005260 	 C1-INIT-WORK-AREA-END.                                         
005270 	     EXIT.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387beba4_1@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <387BBA73.9AE7AB21@boeing.com>`

```

Susan Allen <susan.a.allen@boeing.com> wrote in message
news:387BBA73.9AE7AB21@boeing.com...
> Leif Svalgaard wrote:
> >
…[16 more quoted lines elided]…
> 005160      INITIALIZE HOLD-NUMERIC-FIELDS

line 005120 does not seem to be necessary because 005150 and 005160
says it all.

What I'm after is not the short little comment, but the long comment that
would
explain very complex COBOL code because the code itself couldn't.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387C948B.13710728@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <387BBA73.9AE7AB21@boeing.com> <387beba4_1@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 

> What I'm after is not the short little comment, but the long comment that
> would
> explain very complex COBOL code because the code itself couldn't.

The person who removes comments, removes both.

Long comments can be used, not to explain what the COBOL does - well
written COBOL shows what it does.  But the long comments can be used to
explain WHY it does what it is doing.  It could explain external
requirements, business rules etc.

When a user complains that a program does something, we can look at the
code and see "yep, that's what it does".  What we need to learn is why,
and what the consequences will be in "fixing" the code.

Someone posted a program which uses pointers to determine DD names in
mainframe IBM JCL.  I tried it and it works, but I have no idea how it
works.  I even posted a request on this news group for assistance in
finding documentation on pointers to JCL.  Whomever wrote the COBOL
program must have had that documentation.  I sure wish he had put some
of it into his code.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85igfa$g00$1@nntp3.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <387BBA73.9AE7AB21@boeing.com> <387beba4_1@news3.prserv.net> <387C948B.13710728@NOSPAMwebaccess.net>`

```
I think if you look at the most recent version of the COBOL program to get
IBM control blocks it DOES know include "comments" to point to the IBM
documentation that explains what it's all about.  See:

  http://members.home.net/gsf/tools/cob2sys.txt

This is an example of "introductory" comments - and use of the sequence area
as a MINIMAL comment.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 12)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387CCA65.3F616228@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net> <387BBA73.9AE7AB21@boeing.com> <387beba4_1@news3.prserv.net> <387C948B.13710728@NOSPAMwebaccess.net> <85igfa$g00$1@nntp3.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I think if you look at the most recent version of the COBOL program to get
…[6 more quoted lines elided]…
> as a MINIMAL comment.

That's not the version I have, but I will look at it.  Comments such as
PSA, CVT, CVTFIX, SCMA, RMCT, HID, & ECVT don't mean much to me, but the
program also showed where to find further documentation.   I have a
place to start research as soon as I stop some fires!
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Nbyf4.157$x3.321@wormhole.dimensional.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <858bob$gqb$1@news.igs.net> <cQle4.347$lb5.2288@news3.mia> <387a7d02_1@news3.prserv.net>`

```
******************************************************************
*                 21100-PROCESS-TIMELINE
*
* THIS PARAGRAPH LOOKS SCARIER THAN IT IS! WHAT WE ARE DOING IS
* REALLY QUITE SIMPLE, BUT TAKES A LOT OF CODE. WE NEED TO
* DETERMINE DATE RANGES THAT FIT THE xxxxx DATA OR LACK THEREOF
* FOR THE TIME COVERED BY THE yyyyy DATA.
*
* TABLE  TIME
*   V    --->
* xxxxx         �---------------------------�
* yyyyy    �--------�      �---------�
*   V
* range        �---�------�---------�------�
*
* WE START WITH THE BGN AND END DAT/TM FOR xxxxx, AND THEN
* IDENTIFY CONDITIONS WHICH WOULD MOVE THE END DAT/TM EARLIER.
* ONCE THE RANGE IS NARROWED TO THE SMALLEST ONE STARTING WITH
* THE BEGIN DAT/TM, WE CHECK THE DATA FOR yyyyy. THE THE BEGIN
* DAT/TM IS SET TO ONE SECOND LATER THAN THE END DAT/TM OF THE
* RANGE, AND WE BEGIN THE PROCESS AGAIN UNTIL THE END DAT/TM OF
* OUR RANGE IS THE END DAT/TM OF THE xxxxx TRANSACTION.
*
******************************************************************

The comments explaining how the timeline is being built make people feel a
lot better about the code, and help them understand it readily.  They nicely
summarize what is going on in the next 350 lines of the source listing which
is otherwise adequately understandable because good data names were used.  I
don't have the source with me at the moment, but there is another similar
comment block for a much lengthier bit of code doing the same thing for 8
different data sources, 6 of them for individual keys and 2 for key ranges,
all beginning and end dated.


Glenn


Leif Svalgaard <lsvalg@ibm.net> wrote in message
news:387a7d02_1@news3.prserv.net...
> show us ONE
>
> Judson McClendon <judmc@bellsouth.net> wrote in message
> news:cQle4.347$lb5.2288@news3.mia...
> > The percentage of the code that needs these comments depends on what
kind
> > of programs are being written.  I do agree that, out of all COBOL code,
> > only a small percentage needs the kinds of comments I'm talking about.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38774dfc_4@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:mJHd4.5749$ps.67984@news4.mia...
> donald tees wrote:
> >
> >What I always liked about Cobol, was that the code read like comments.
It
> >was so easy to read that you did not need to write a dialog explaining
what
> >you were doing.  In fact, I was taught that if your Cobol code was so
poorly
> >written that you needed comments to explain what it did, then you were a
> >piss-assed-poor programmer.
…[6 more quoted lines elided]…
> it is, even if the 'what' is obvious.

Judson,

show us an example from real life.
A problem with block comments is that they
rarely get maintained together with the code.

a common practice among 'maintainers' is
to run the program through a filter to remove
all comments before doing maintenance
on it. Upon questioning on why, they always
answer: 'because I've so often been misled
by the comments'.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85920c$c3e$1@nntp3.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net>`

```
Leif Svalgaard <lsvalg@ibm.net> wrote in message
news:38774dfc_4@news3.prserv.net...
>
> Judson McClendon <judmc@bellsouth.net> wrote in message
…[9 more quoted lines elided]…
> > >written that you needed comments to explain what it did, then you were
a
> > >piss-assed-poor programmer.
> > >;<)
…[18 more quoted lines elided]…
> by the comments'.

IF TXN-AMT IS LESS THAN 100.00
    IF MSC-POS-USER-1-4 IS EQUAL TO '6990'  OR
        MSC-POS-USER-5-6 IS EQUAL TO '08'
        MOVE SPACE TO DMF-CALL-ME-FLAG.

Just tell me exactly what that means.

Actually, I will grant that it could have been made more readable if the
programmer had used 88 levels and better described field names.  But he
didn't.  Certainly a comment or two would be nice!
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85apbc$sko$2@aklobs.kc.net.nz>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net>`

```
:> a common practice among 'maintainers' is
:> to run the program through a filter to remove
:> all comments before doing maintenance
:> on it. Upon questioning on why, they always
:> answer: 'because I've so often been misled
:> by the comments'.

Exactly, no comments is better than wrong comments.  I will
believe comments when the compiler can process them and tell
me that they actually match the code.

: IF TXN-AMT IS LESS THAN 100.00
:     IF MSC-POS-USER-1-4 IS EQUAL TO '6990'  OR
:         MSC-POS-USER-5-6 IS EQUAL TO '08'
:         MOVE SPACE TO DMF-CALL-ME-FLAG.

: Just tell me exactly what that means.

At a guess it is the previous programmer attempt to get free
goods on his POS card number 6990.  If this is the case
then I would not expect a comment to actually say this, it
would waffle on about something completely spurious and
misleading.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3879FB95.BB03E269@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net> <85apbc$sko$2@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Exactly, no comments is better than wrong comments.  I will
> believe comments when the compiler can process them and tell
> me that they actually match the code.
> 

And any code review should also be a comment review.  One reason
programmers hate documentation is that too often, we write a program,
update (or write) the specs to match the program, and then those specs
are stored away where the maintenance programmers are wise in never
looking at them - as they don't get updated with maintenance changes.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8598p8$47a$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net>`

```

Frank Swarbrick wrote in message <85920c$c3e$1@nntp3.atl.mindspring.net>...
>Leif Svalgaard <lsvalg@ibm.net> wrote in message
>news:38774dfc_4@news3.prserv.net...
…[45 more quoted lines elided]…
>


Writing it so it was readable would be nicer.  Adding comments instead is
like writing a book that is unintelligible, then trying to fix it with
footnotes.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net>`

```
Frank Swarbrick wrote in message <85920c$c3e$1@nntp3.atl.mindspring.net>...
>
>IF TXN-AMT IS LESS THAN 100.00
…[4 more quoted lines elided]…
>Just tell me exactly what that means.


If "TXN" stands for "taxation" it means we need a tax cut.

If it stands for "transaction", we still need a tax cut.

MCM
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85aum8$15n$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net> <9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote in message
<9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net>...
>Frank Swarbrick wrote in message <85920c$c3e$1@nntp3.atl.mindspring.net>...
>>
…[11 more quoted lines elided]…
>
I'll bet money that if each of the "shortcuts" (read lazy typing) above were
expanded, then I could tell you exactly what the above did.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 9)_

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85b3cu$t9s$1@nntp2.atl.mindspring.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net> <9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net> <85aum8$15n$1@news.igs.net>`

```
donald tees <donald@willmack.com> wrote in message
news:85aum8$15n$1@news.igs.net...
>
> Michael Mattias wrote in message
> <9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net>...
> >Frank Swarbrick wrote in message
<85920c$c3e$1@nntp3.atl.mindspring.net>...
> >>
> >>IF TXN-AMT IS LESS THAN 100.00
…[11 more quoted lines elided]…
> I'll bet money that if each of the "shortcuts" (read lazy typing) above
were
> expanded, then I could tell you exactly what the above did.

Actually, I did end up rewriting this somewhat, so let's see...

    05  MSC-POS-USER.
        10  MSC-POS-USER-1-4                PIC X(4).
            88  MERCHANT-DIRECT-MARKETING    VALUE '6990'.
        10  MSC-POS-USER-5-6                PIC XX.
            88  POS-COND-CODE-MOTO                    VALUE '08'.

IF  TXN-AMT IS LESS THAN 100.00
    IF MERCHANT-DIRECT-MARKETING  OR
        POS-COND-CODE-MOTO
        MOVE SPACE TO DMF-CALL-ME-FLAG.

Not a big difference.  This is for Visa credit/debit card processing.
Generally, if a customer is over their daily transaction or dollar limit we
will send back a "referral" (or call-me) response, which means the merchant
will call their processor who will call our bank to get a voice approval.
But for mail or telephone order (MOTO) transactions or transactions from
direct marketing merchants, if the transaction is under $100.00 this is
disallowed.  This code will space out the CALL-ME flag in this case, and the
txn or $$ limit response will be sent instead.

Even with the 88 levels I used, I still think a few comments would help
clear things up, don't you?

And as for renaming the MSC-POS-USER field itself, I would agree, but
there's quite a bit of code that uses it as named, so I'm not going to do
that.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mae4.57479$J%4.77151@dfiatx1-snr1.gtei.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <85920c$c3e$1@nntp3.atl.mindspring.net> <9k0e4.26317$J%4.49053@dfiatx1-snr1.gtei.net> <85aum8$15n$1@news.igs.net> <85b3cu$t9s$1@nntp2.atl.mindspring.net>`

```
Frank Swarbrick wrote in message <85b3cu$t9s$1@nntp2.atl.mindspring.net>...
>
>Actually, I did end up rewriting this somewhat, so let's see...

Much Better!

(But  disappointed: no tax cut)


>
>And as for renaming the MSC-POS-USER field itself, I would agree, but
>there's quite a bit of code that uses it as named, so I'm not going to do
>that.
>

CHANGE ' MSC-POS-USR ' ' BETTER-DATA-NAME ' ALL
SAVE


MCM
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DEKd4.6171$ps.72909@news4.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
>Judson McClendon wrote:
>>
…[17 more quoted lines elided]…
>by the comments'.

Is that not rather a statement on maintenance programmers, rather than
on the value of proper comments? ;-)

Let me give three example categories.  If this doesn't satisfy you,
I'm not sure actual code would help, because I would probably have to
write a great deal of background to make the specific issues clear. :-)

1. Doing calculations that can only be understood based on background
   math or other foundation principles that aren't specifically in the
   code.  Unless the programmer happens to know the background material,
   he is unable to evaluate where the code may be incorrect, even if he
   knows what the final result should be.  Occasionally it is necessary
   to do some 'fundamental research' in order to develop and prove a
   complex algorithm (not necessarily mathematical).  The information
   gained by this research is often not readily apparent in the code
   itself.  The same happens in pure math.  When the conclusions and
   results of new math are presented without the process used to derive
   them, they are often extremely difficult to understand, follow and
   verify.

2. In some cases, the reason for choosing a particular implementation
   or algorithm is efficiency, or some other consideration, based on
   empirical data or other non-obvious reasons.  If the reasoning is
   not explained, a maintenance programmer might choose an apparently
   simpler or more efficient replacement without realizing the
   implications.

3. Occasionally the code necessary to accomplish some task can be so
   complex and subtle that even when the routine and all subroutines and
   data names are clearly defined, the reason why the conglomerate works
   may not be readily apparent.  Without explanatory comments, the
   maintenance programmer cannot easily evaluate why the code works, much
   less determine why it is broken.

What I am trying to express is that code can and should be written as
simply and clearly as possible; but some tasks are so difficult, subtle
or obscure that the code alone, no matter how well written, simply does
not provide enough information for a maintenance programmer to understand
how and why the code works.  Some things are just complex and difficult,
and cannot be made simple and clear, no matter how they are coded.  You
may not have seen code like that, but I sure have.  I recently co-wrote
a system so complex that we were often dealing with hundreds of factors
at a time.  Without supporting comments, there is absolutely no way a
maintenance programmer could understand, modify or correct the code
without re-doing an enormous amount of the research and development work
it took to develop the code in the first place.  Not all requirements are
this difficult (Thank God!), and many of you may never have encountered
any.  But if you ever do, you'll know exactly what I'm talking about. :-)
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38778104_2@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia>`

```

Judson McClendon <judmc@bellsouth.net> wrote in message
news:DEKd4.6171$ps.72909@news4.mia...
> Leif Svalgaard wrote:
> >Judson McClendon wrote:
…[15 more quoted lines elided]…
> and cannot be made simple and clear, no matter how they are coded

I disagree strongly with the above. Also if something is TRULY complicated
it will take page after page of supporting comments. That is why I asked for
a REAL example, not just general philosophical comments. If the code
is obscure why would the comments not be equally obscure? If you
can write crystal clear comments, why can't you write crystal clear code?
Maybe it is a question of coding style. There are some styles that
make writing of clear code more difficult. So, I will agree that if the
coding style is poor, maybe some English prose might help.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8591il$slj$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net>`

```

Leif Svalgaard wrote in message <38778104_2@news3.prserv.net>...
>
>Judson McClendon <judmc@bellsouth.net> wrote in message
…[5 more quoted lines elided]…
>> >> when the code itself is crystal clear.  For example, in algorithms
that
>> >> are complex or somewhat abstract, I like to describe the algorithm in
>> >> a comment block, so the reader will know 'why' the code is doing what
…[13 more quoted lines elided]…
>it will take page after page of supporting comments. That is why I asked
for
>a REAL example, not just general philosophical comments. If the code
>is obscure why would the comments not be equally obscure? If you
…[5 more quoted lines elided]…
>
I agree with Leif.  Further, the purpose of the high level language *should*
be to enable the programmer to explain the algorithm in clear, precise
terms.  If the language is incapable of that, then the language is at fault.
The way that I always explained complex mathmatical formulae *to myself* was
to write them out longhand in Cobol.  That made it clear.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3879FA1C.DFE4AE62@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <8591il$slj$1@news.igs.net>`

```
donald tees wrote:
> 
> I agree with Leif.  Further, the purpose of the high level language *should*
…[3 more quoted lines elided]…
> to write them out longhand in Cobol.  That made it clear.

Good code *should* explain what was coded.   But how does it show
whether the business rule is coded correctly?

A comment such as:
**** Joe in accounting says that the federal requirement for this
calculation differs from the state requirement 

May be necessary for a maintenance programmer to avoid breaking a
calculation when Pete says the calculation he receives is wrong.  In
this case, Pete simply has a different business rule than Mary - don't
change the code to Pete's rule without understanding where it came from.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<859511$44a2$1@newssvr04-int.news.prodigy.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net>`

```

> > >show us an example from real life.
> > What I am trying to express is that code can and should be written as
> > simply and clearly as possible; but some tasks are so difficult, subtle
> > or obscure that the code alone, no matter how well written, simply does
> > not provide enough information for a maintenance programmer to
understand
> > how and why the code works.  Some things are just complex and difficult,
> > and cannot be made simple and clear, no matter how they are coded
>
> I disagree strongly with the above. Also if something is TRULY complicated
> it will take page after page of supporting comments. That is why I asked
for
> a REAL example, not just general philosophical comments. If the code
> is obscure why would the comments not be equally obscure? If you
…[3 more quoted lines elided]…
> coding style is poor, maybe some English prose might help.

Except for his signature :), I agree with Judson.  (I'm trying to be more
tolerant of signatures!)  The "crystal clearness" of COBOL is limited by
syntax and usage rules.  Crystal clear code, although desirable, is not
always possible with COBOL and when it isn't, an English description of the
business rules that resulted in the code can clarify why the code was
written as it was.  English, although it has rules too, is not quite as
limiting as COBOL rules.  I personally try to keep programs as simple and
readable as possible.  When functionality is added to a program already in
production, the new function cannot always be easily integrated without
documentation in the form of comments.  I do try to keep comments to a
minimum since I've also run into the situation where changed code is not
always reflected in the associated comments.  Of course, that's true with
documentation in general.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38789b62_1@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <859511$44a2$1@newssvr04-int.news.prodigy.com>`

```
Terry Heinze <terryheinze@prodigy.net> wrote
> > > >show us an example from real life.
> > > What I am trying to express is that code can and should be written as
> > > simply and clearly as possible; but some tasks are so difficult,
subtle
> > > or obscure that the code alone, no matter how well written, simply
does
> > > not provide enough information for a maintenance programmer to
understand
> > > how and why the code works.  Some things are just complex and
difficult,
> > > and cannot be made simple and clear, no matter how they are coded
> >
> > I disagree strongly with the above. Also if something is TRULY
complicated
> > it will take page after page of supporting comments. That is why I asked
for
> > a REAL example, not just general philosophical comments. If the code
> > is obscure why would the comments not be equally obscure? If you
> > can write crystal clear comments, why can't you write crystal clear
code?
> > Maybe it is a question of coding style. There are some styles that
> > make writing of clear code more difficult. So, I will agree that if the
…[5 more quoted lines elided]…
> always possible with COBOL and when it isn't, an English description of
the
> business rules that resulted in the code can clarify why the code was
> written as it was

I asked for (no response yet) a REAL example from one of Judson's
REAL programs (according to Judson there should be many) so that
the ones among us that agree with me collectively could REWRITE
the code to make it clear.
There are cases where comments are good. Not to describe obscure
points, but to link back to requirement specifications. E.g.:
* the following implements CHANGE REQUEST #12345
Maybe this is what Judson meant with "the why rather than the what"?
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2zme4.429$lb5.4228@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <859511$44a2$1@newssvr04-int.news.prodigy.com> <38789b62_1@news3.prserv.net>`

```
Leif Svalgaard wrote:
>
>I asked for (no response yet) a REAL example from one of Judson's
>REAL programs (according to Judson there should be many) so that
>the ones among us that agree with me collectively could REWRITE
>the code to make it clear.

Actually, according to Judson, there should be few. ;-)

>There are cases where comments are good. Not to describe obscure
>points, but to link back to requirement specifications. E.g.:
>* the following implements CHANGE REQUEST #12345
>Maybe this is what Judson meant with "the why rather than the what"?


That's one, but certainly not the only case.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 10)_

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-1tMr8InduFsY@localhost>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <859511$44a2$1@newssvr04-int.news.prodigy.com> <38789b62_1@news3.prserv.net>`

```
On Thu, 1 Jan 1970 00:59:59, "Leif Svalgaard" <lsvalg@ibm.net> wrote:

> I asked for (no response yet) a REAL example from one of Judson's
> REAL programs (according to Judson there should be many) so that
…[5 more quoted lines elided]…
> Maybe this is what Judson meant with "the why rather than the what"?

Here is one example from my code that might shed some light on the 
discussion:

     IF WS-TRW-DOB-YEAR NOT NUMERIC                               
        MOVE '00' TO WS-TRW-DOB-YEAR  WS-TRW-DOB-CENTURY          
     ELSE                                                         
        MOVE '99' TO WS-TRW-DOB-CENTURY.                          
*                                                                 
* THE ABOVE LOOKS BOGUS - THE 99 IN DOB-CENTURY IS TO BE USED AS  
* A SWITCH IN DETERMINING IF WE HAVE A VALID CENTURY OR NOT.      
*                                                                 

Later in the code we determine the century for all dates with 99 in 
the century.  Those with other values either have a proper century, or
we indeed want them to STAY zero.  
-------------------------

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Month=99

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387A2182.363413F0@NOSPAMwebaccess.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <859511$44a2$1@newssvr04-int.news.prodigy.com> <38789b62_1@news3.prserv.net> <Jl0PnHJ5PvPd-pn2-1tMr8InduFsY@localhost>`

```
Thane Hubbell wrote:
> 
> Here is one example from my code that might shed some light on the
…[8 more quoted lines elided]…
> * A SWITCH IN DETERMINING IF WE HAVE A VALID CENTURY OR NOT.

We have had two ways of handling date = 99/99/99.  One was to make sure
all of the windowing routines said:
  IF OLD-DATE = '999999'
     MOVE '99' TO CENTURY
  ...

A less obvious way was to change the application from
   IF ACCOUNT-DATE = '99999999'
 to
   IF ACCOUNT-MM = '99'

Sometimes the second was put in as a quick fix and then kept in while
the common routine was changed.
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38787D38.8122E785@zip.com.au>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 

> I disagree strongly with the above. Also if something is TRULY
> complicated it will take page after page of supporting comments. That
…[6 more quoted lines elided]…
> prose might help.

I agree with you however...

There are things in the logic that deserves a comment.  There are
tools that might eliminate that comment.  If I saw a comment less
program then I would be very concerned.

The second thing is that if you have crap comments then your
implementation procedures need review.  The comments should be
validated to ensure currency at all times.  One instance I had was a
routine was copied from one as a template and the comments were not
changed, talk about confused.  I updated the program that release with
comment changes only, it is surprisingly difficult to get this
approved for implementation.

Bill said:

> This is the logic required by the taxing laws in counties ABC, XYZ,
> and LMN. For the logic required in counties DEF, GHI, and QRS, see
> pargraph 1234-Other-Counties.

Make the code explicit:

	Evaluate country
	   when abc or xyz or lmn
		perform x
	   when def or ghi or qrs
		perform 1234-other-countries.

You get the idea.
Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tpme4.411$lb5.3998@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net>`

```
Leif Svalgaard wrote:
>Judson McClendon wrote:
>>
…[14 more quoted lines elided]…
>coding style is poor, maybe some English prose might help.

Leif, you are missing the point.  There are algorithms where the code
itself, no matter *how* well written, simply does not give all the
information necessary to evaluate whether it is functioning correctly
or not, because it works on rules or principles that are not directly
apparent in the algorithm itself.  Yes, it is possible in some (but
certainly not all) of these situations to 'reverse engineer' the code
to figure out why it was written that way.  But why force that, when a
few comments explaining the basis, or at least the source of the basis,
can resolve the problem?

Most of the COBOL examples I can think of are long and involve too
many factors to use here as examples.  But let me give you one from
a C language calculator program called BIGCALC.  If you have ever done
any calculation of the common functions, such as trig and logs, you
know that a fair amount of background math is involved.  Yes, most
people with a science background know about Taylor's or Maclaurin's
Series.  But common formulas derived from these series are virtually
worthless by themselves to calculate high precision results, because
they converge far too slowly.  After some research, and helpful input
from people already knowledgeable in this area, I learned that the key
to making the functions converge rapidly lies in scaling the arguments,
calculating the function, then making adjustments to accommodate for
the pre scaling.  Many of these methods are very, very difficult to
find.  They are only rarely published, and very few people have any
knowledge of them.  If any normal programmer, even one with a heavy
math background, encountered these calculations without any comments,
even if they were labeled as 'pre scaling' and 'post scaling', the
programmer might know why the code was there, but would have no way of
evaluating the code for correctness without a *lot* of research.  To
say that you could write the code in such a way to make this clear
without comments shows a lack of understanding of the situation.  The
programmer must know the math *behind* the scaling calculations in
order evaluate it.  There's no other way.  And one shouldn't be forced
into re-doing fundamental math research in order to understand how to
debug a program!

While the above example would certainly be unusual for a COBOL program,
I can easily imagine a similar situation arising in certain statistical
calculations.  More commonly, the problem is that some basic research
has been done, and perhaps empirical data generated, in order to create
an appropriate algorithm.  The principles developed by this are sometimes
not directly reflected in the code.  Or this could be because of complex
business logic.  Yes, it is always best to make the code reflect the
business logic clearly enough so no comments are needed.  But in real
life, this is simply not always possible.  Real life is *always* messier
than theory, and hard and inflexible rules "you must *never* do this" or
"you must *always* do that" rarely prove applicable in all situations. :-)
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387a7cd0_2@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <tpme4.411$lb5.3998@news3.mia>`

```
> Leif, you are missing the point.  There are algorithms where the code
> itself, no matter *how* well written, simply does not give all the
…[32 more quoted lines elided]…
> debug a program!

show us the comments and the code even if it is C.

Here are a couple of my examples, complete with scaling etc.
The code speaks for itself, the formulas used are clear.
WHY the math works is not a subject for the code nor the
comments. If you absolutely want a comment, include a
reference to where you found the formulae.

I'm still looking for a COBOL example. It should be easy to do,
simply find a program with comment and code, cut and paste
into a posting. If it is truly HUGE (especially the explanatory comments)
attach the stuff a posting.



036900******************    LOGARITHM 10 FUNCTION    *******************
037400
037500 LOGARITHM-10-FUNCTION.
037600     MOVE MATHPK-ARGUMENT-1 TO WORK-X
037700
037800     IF WORK-X > ZERO
037900         PERFORM COMPUTE-LOGARITHM-FUNCTION
038000         MOVE LOGARITHM-X TO MATHPK-RESULT
038100     ELSE
038200         PERFORM SET-DOMAIN-ERROR
038300     .
038400
038500 COMPUTE-LOGARITHM-FUNCTION.
038600     IF WORK-X < VALUE-ONE
038700         MOVE "NEG" TO SIGN-OF-LOGARITHM
038800         COMPUTE WORK-X = VALUE-ONE / WORK-X
038900     ELSE
039000         MOVE "POS" TO SIGN-OF-LOGARITHM
039100     .
039200     PERFORM REDUCE-X-TO-INTERVAL--1-TO-2
039300     PERFORM RATIONAL-LOG-TRANSFORMATION
039400     PERFORM EVALUATE-LOGARITHM-APPROX
039500
039600     IF LOG-IS-NEGATIVE
039700         COMPUTE LOGARITHM-X = VALUE-ZERO - LOGARITHM-X
039800     .
039900
040000 REDUCE-X-TO-INTERVAL--1-TO-2.
040100     MOVE ZERO TO CHARACTERISTIC-X
040200     PERFORM DIVIDE-BY-TWO
040300       UNTIL WORK-X < VALUE-TWO
040400     .
040500
040600 DIVIDE-BY-TWO.
040700     COMPUTE WORK-X = WORK-X / VALUE-TWO
040800     ADD VALUE-ONE TO CHARACTERISTIC-X
040900     .
041000
041100 RATIONAL-LOG-TRANSFORMATION.
041200     COMPUTE TRANSF--X = (WORK-X - SQRT-TWO)
041300                       / (WORK-X + SQRT-TWO)
041400     COMPUTE TRANSF-XX = TRANSF--X * TRANSF--X
041500     .
041600
041700 EVALUATE-LOGARITHM-APPROX.
041800     COMPUTE MANTISSA-X = ONE-HALF + TRANSF--X * (LOG-COEFF1
041900                                   + TRANSF-XX * (LOG-COEFF3
042000                                   + TRANSF-XX * (LOG-COEFF5
042100                                   + TRANSF-XX *  LOG-COEFF7
042200                                                         )))
042300     COMPUTE LOGARITHM-X ROUNDED = (MANTISSA-X + CHARACTERISTIC-X)
042400                                         / LOG2-OF-TEN
042500     .


049200*********************    ARCTAN FUNCTION    **********************
049700
049800 ARCTAN-FUNCTION.
049900     MOVE MATHPK-ARGUMENT-1 TO WORK-X
050000     PERFORM COMPUTE-ARCTAN-FUNCTION
050100     MOVE ARCTAN-X TO MATHPK-RESULT
050200     .
050300
050400 COMPUTE-ARCTAN-FUNCTION.
050500     IF WORK-X < ZERO
050600         COMPUTE WORK-X = VALUE-ZERO - WORK-X
050700         MOVE "NEG" TO SIGN-OF-ARGUMENT
050800         PERFORM COMPUTE-ARCTAN-APPROX
050900     ELSE
051000     IF WORK-X > ZERO
051100         MOVE "POS" TO SIGN-OF-ARGUMENT
051200         PERFORM COMPUTE-ARCTAN-APPROX
051300     ELSE
051400         MOVE ZERO  TO ARCTAN-X
051500     .
051600
051700 COMPUTE-ARCTAN-APPROX.
051800     PERFORM RATIONAL-TAN-TRANSFORMATION
051900     PERFORM EVALUATE-ARCTAN-APPROX
052000     IF ARGUMENT-IS-NEGATIVE
052100         COMPUTE ARCTAN-X = VALUE-ZERO - ARCTAN-X
052200     .
052300
052400 RATIONAL-TAN-TRANSFORMATION.
052500     COMPUTE TRANSF--X = (WORK-X - VALUE-ONE)
052600                       / (WORK-X + VALUE-ONE)
052700     COMPUTE TRANSF-XX = TRANSF--X * TRANSF--X
052800     .
052900
053000 EVALUATE-ARCTAN-APPROX.
053100     COMPUTE WORK-W = TRANSF-XX * (ATAN-COEFF9
053200                    + TRANSF-XX * (ATAN-COEFF11
053300                    + TRANSF-XX * (ATAN-COEFF13
053400                    + TRANSF-XX *  ATAN-COEFF15)))
053500     COMPUTE WORK-X = TRANSF--X * (ATAN-COEFF1
053600                    + TRANSF-XX * (ATAN-COEFF3
053700                    + TRANSF-XX * (ATAN-COEFF5
053800                    + TRANSF-XX * (ATAN-COEFF7
053900                    + WORK-W))))
054000     COMPUTE ARCTAN-X = PI-QUARTER + WORK-X
054100     .
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wgIe4.3077$lb5.37703@news3.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <tpme4.411$lb5.3998@news3.mia> <387a7cd0_2@news3.prserv.net>`

```
Leif Svalgaard wrote:
>
>show us the comments and the code even if it is C.


Well, okay.  See below.  Remember, this code is calculating to
hundreds of digits of precision.  Many normal approaches, such
as using pre calculated coefficients of polynomials won't work
here.

>Here are a couple of my examples, complete with scaling etc.
>The code speaks for itself, the formulas used are clear.

Well, that's a matter of opinion.  You apparently find the code
clear, but you wrote it and know how it's supposed to work.  I
don't think anyone else coming to the code without prior
knowledge would find it nearly as easy to assimilate the methods
as they would in my C code example with comments, even though C
code is normally not nearly as clear as COBOL code.  I'm not
saying your code is obfuscated or poorly written, but it surely
would be much easier and quicker to assimilate with meaningful
comments, at least to me.

>WHY the math works is not a subject for the code nor the
>comments.

You bet it is important why the math works, if you're trying to debug
the code or modify it!  How in the world are you going to know why
a piece of code produces the wrong answer if you don't know how it
is supposed to work?  I am amazed that you find this concept unclear.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 11)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387dd94a_4@news3.prserv.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <tpme4.411$lb5.3998@news3.mia> <387a7cd0_2@news3.prserv.net> <wgIe4.3077$lb5.37703@news3.mia>`

```
Judson McClendon <judmc@bellsouth.net> wrote
>    if (work[0].sign != work[1].sign) {       /* If signs are different, */
>       work[0].sign = FlipSign(work[0].sign); /*  reverse sign           */
>       return(ExtendedSubtract());            /*  and subtract           */
>       }

>       return(TRUE);                    /*  return zero       */
>       al = &work[1].man[0];                        /* Multiplier left
*/
>       ar = &work[1].man[work[1].digits - 1];       /* Multiplier right
*/
>       bl = &work[0].man[0];                        /* Multiplicand left
*/
>       br = &work[0].man[work[0].digits - 1];       /* Multiplicand right
*/

why not call al 'multiplier_left', ar 'multiplier_right' etc


>     *    **************************************************
>     *    *  SIN(X): Using the power series:               *
>     *    *                  X^3   X^5   X^7       X^n     *
>     *    *     sin(X) = X - --- + --- - --- + ... ---     *
>     *    *                   3!    5!    7!        n!     *

The code clearly shows this as well, as showing the power series
does not explain WHY that converges to SIN(X). If you do not your
match and have to rely on the comments to maintain this program
you should not be maintaining this program.

anyway, maybe let the horse rest.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lSmf4.94$8z5.94@news4.mia>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <tpme4.411$lb5.3998@news3.mia> <387a7cd0_2@news3.prserv.net> <wgIe4.3077$lb5.37703@news3.mia> <387dd94a_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
>>
>>     *    **************************************************
…[8 more quoted lines elided]…
>you should not be maintaining this program.

You don't need to know why the math works to make the algorithm work.
But you do have to know what the math is to make the algorithm do it
correctly.

Four things you miss.  First, a new programmer looking at the code
for the first time can see the formula in 2 seconds by looking at
the comments, but it takes much longer to deduce what the formula
is supposed to be by looking at the code.  Second, if the code is
not functioning correctly, how is the programmer supposed to deduce
the proper formula, since the code is incorrect?  Third, why have
to do serious background math just to find a simple logic bug in an
algorithm?  Fourth, in looking for a bug, comparison of the code
with the comment gives an additional check on the math and logic.

My clients pay me to develop high quality software.  This means not
only that it works correctly, but that it is easy for their in-house
programmers to maintain.  I am often asked to write code that their
in-house staff is not able to do on their own, or would not be able
to do very well.  In this environment, it is imperative that all the
code I write be as clear and easy to understand as I can make it, so
those in-house programmers can maintain it.  I can't assume, and I
don't think anyone should assume, that the maintenence programmer is
going to be as knowledgable and capable as the one writing the code.
They may be, but why make it necessary?  I am certain that not one of
my clients would be pleased if I stopped putting in those comments.
You should see the smiles on their faces when they see the commenting
in the code as they review a new system. :-)

>anyway, maybe let the horse rest.

I agree.  We've covered the subject pretty well already. :-)
```

###### ↳ ↳ ↳ Re: In-line comment indicator

_(reply depth: 12)_

- **From:** "David A. Cobb" <superbiskit@home.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38925818.70DF6041@home.com>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net> <856abc$9oo$1@news.igs.net> <mJHd4.5749$ps.67984@news4.mia> <38774dfc_4@news3.prserv.net> <DEKd4.6171$ps.72909@news4.mia> <38778104_2@news3.prserv.net> <tpme4.411$lb5.3998@news3.mia> <387a7cd0_2@news3.prserv.net> <wgIe4.3077$lb5.37703@news3.mia> <387dd94a_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> Judson McClendon <judmc@bellsouth.net> wrote
…[28 more quoted lines elided]…
> anyway, maybe let the horse rest.

If the CODE were always correct, many of us would be out of paying jobs!
OTOH, many shops have coding stds requiring ASSEMBLER code to have a
comment on every line.  For example --

    L R1,=V(THING)             PUT THE ADDRESS OF THING IN R1

which never gives me a warm fuzzy feeling.

The bottom line is that no quantity of commentary, and no set of coding
standards will prevent stupidity.
```

###### ↳ ↳ ↳ Re: Re: In-line comment indicator

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<857cpr$13n$1@news.igs.net>`
- **References:** `<8536vm$ifq$1@nntp5.atl.mindspring.net> <8542ll$r6m$1@ssauraaa-i-1.production.compuserve.com> <854svd$3u9$1@nntp1.atl.mindspring.net>`

```
William M. Klein wrote in message <854svd$3u9$1@nntp1.atl.mindspring.net>...
>No, the Standard specifically ONLY addresses comments on a single line,
e.g.
>
>If A = B               *>  This is  the
…[3 more quoted lines elided]…
>
I like that.  I used to write a lot of assembler, and had as a shop spec
that EVERY line had to have a comment as itemized above.  The effect was a
running dialog of what the code did on the right, with the assembler on the
left.

What I always liked about Cobol, was that the code read like comments.  It
was so easy to read that you did not need to write a dialog explaining what
you were doing.  In fact, I was taught that if your Cobol code was so poorly
written that you needed comments to explain what it did, then you were a
piss-assed-poor programmer.
;<)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
