[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# entry

_48 messages · 18 participants · 2000-04_

---

### entry

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>`

```
I had read in my cobol manual about the entry statement, allowing you
to jump to any section of code an execute it. does anyone have a short
and dirty example of how it would work?

first-program.
	call "somewhere-in-module"

procedure division.
perform some-code
exit program
.

somewhere-in-module.

*where is entry placed? does it use the linkage section by default?


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: entry

- **From:** "Searcher" <mangogwr@bellsouth.net>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54tH4.2895$At2.219@news4.mia>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>`

```
First off: the 'PROCEDURE DIVISION USING' creates an
'ENTRY _pgmid' in the object module.
Entry is a way to provide an alternate 'entry point' and some
packages (IMS for instance) require specific 'entry points' for the
user apps.

In COBOL, the ENTRY statement is to allow a routine to be
entered at different points.
a very good example is a date_calc routine.
An all-purpose date_calc routine is written that handles
all date calcs for a shop.
PROGRAM-ID.  DATE-CALC.
PROCEDURE DIVISION USING LS-DATE-PARM.
...
GO TO QUIT-ALL.

ENTRY YMDCYMD.
...
GO TO QUIT-ALL.

ENTRY JULCYMD.
...
GO TO QUIT-ALL.

ENTRY JULGREG.
...
    GO TO QUIT-ALL.
QUIT-ALL.
EXIT PROGRAM.

6.2.12 ENTRY Statement

The ENTRY statement establishes an alternate entry point into a COBOL called
subprogram.

The ENTRY statement cannot be used in:

   Programs that specify a return value using the Procedure Division
RETURNING phrase.  For details, see
    the discussion of the RETURNING phrase under "The Procedure Division
Header" in topic 6.1.2.

   Nested program.  See "Nested Programs" in topic 2.1.1 for a description
of nested programs.


When a CALL statement naming the alternate entry point is executed in a
calling program, control is
transferred to the next executable statement following the ENTRY statement.

+--- Format -------------------------------------------------------------+
�                                                                        �
� >>---ENTRY--literal-1------------------------------------------------> �
�                                                                        �
� >----------------------------------------------------------.-------->< �
�    �        <-----------------------------------------+ �              �
�    �                                  <------------+  � �              �
�    +-USING-----------------------------identifier-1-----+              �
�                +---------REFERENCE-�                                   �
�                � +-BY-+            �                                   �
�                +---------VALUE-----+                                   �
�                  +-BY-+                                                �
�                                                                        �
+------------------------------------------------------------------------+
literal
    Must be nonnumeric and conform to the rules for the formation of a
program-name in the outermost
    program (see "PROGRAM-ID Paragraph" in topic 3.1.1).

    Must not match the program-id or any other ENTRY literal in this
program.

    Must not be a figurative constant.


Execution of the called program begins at the first executable statement
following the ENTRY statement
whose literal corresponds to the CALL statement literal or identifier.

The entry point name on the ENTRY statement can be affected by the PGMNAME
compiler option.  For
details, see the IBM COBOL Programming Guide for your platform.

Subtopics
6.2.12.1 USING Phrase


G Moore <gvwmoore@spam.ix.netcom.com> wrote in message
news:2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com...
> I had read in my cobol manual about the entry statement, allowing you
> to jump to any section of code an execute it. does anyone have a short
…[15 more quoted lines elided]…
> reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: entry

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cjq7v$st4$1@slb6.atl.mindspring.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>`

```
The ENTRY statement is a (relatively common) extension which MANY COBOL
programmers think is a VERY bad idea.  When it is used, you use it as a place
that is CALLED - not performed.  In other words, a main program can have

Program-Id. MainPgm.
...
 Procedure Division.
     ...
          Call "sub123"
              ...
          Call "sub456"
             ...

and your subprogram is coded,

Program-Id. SubPgm.
  ...
Procedure Division.
      ...
     Entry sub123.
          ...
      Entry sub456.
         ...

NOTE WELL, that unless there is a Stop Run (or goback - or exit program) in
Subpgm *before* the 2nd entry statement, you will "fall thru" to sub456 -
even when you enter at sub123.

There are also rules (if you are on an IBM mainframe) about when you have to
CANCEL the program between calls to multiple entry points  and linkage editor
considerations.

Generally, I would recommend using multiple subprograms rather than this
technique.
```

##### ↳ ↳ Re: entry

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F86702.10A9@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> The ENTRY statement is a (relatively common) extension which MANY COBOL
> programmers think is a VERY bad idea.  

...and which at least ONE COBOL programmer thinks is VERY useful when
used appropropriately.

Naturally it can be abused or misused, as can every other programming
construct.

> When it is used, you use it as a place
> that is CALLED - not performed.  In other words, a main program can have
…[23 more quoted lines elided]…
> even when you enter at sub123.

True enough.  It is also true that, in the absence of an ENTRY
statement, the first paragraph will "fall through" into the second
unless it encounters a STOP RUN, GOBACK, or EXIT PROGRAM.

The possibility of "fall through" logic is no more a reason to avoid
ENTRY statements than it is a reason to avoid subprograms.  It is a
hazard inherent in COBOL syntax.  It is a reason to write your code
carefully.

> There are also rules (if you are on an IBM mainframe) about when you have to
> CANCEL the program between calls to multiple entry points  and linkage editor
> considerations.

For years I routinely used ENTRY statements on an IBM mainframe and
never ever wrote a CANCEL statement.

I think you are referring to the fact that the WORKING-STORAGE items
in a subprogram retain their values between calls, unless you CANCEL.
Consequently the results of calling one entry point may depend on
previous calls to other entry points.

If you don't understand the interface you're using, this behavior
might indeed seem confusing.  For a well-designed module, however,
such dependencies should be perfectly natural.  Some routines set the 
scene for other routines, or clean up after them.  You have to call them 
in a sensible sequence, just as you have to open a file before you
can read it.

I don't know what linkage editor considerations you're referring to.
I never had any linking problems attributable to the use of ENTRY
statements.

(IMS imposes some awkwardness because your top-level program is not 
really the the top-level program in the load module -- it's a subprogram 
to IMS and has to be given a specific entry point name in the control
cards for the linker.  Or something like that...it's been a while.)

> Generally, I would recommend using multiple subprograms rather than this
> technique.

Generally, I would recommend using multiple entry points when it makes
sense to do so.

When does it make sense?  When you want to be able to perform any of
several different operations on an encapsulated resource, or set of
resources.

You can't do that very well with multiple subprograms.  Separately
compiled subprograms can't access the same resource (such as a file
or WORKING-STORAGE items) unless you declare the resource EXTERNAL -- 
thereby breaking the encapsulation, and inviting maintenance headaches.

The typical workaround is to have a single do-everything entry point
and pass it an action code to tell it which operation to perform.

The use of action codes creates an unnecessary opportunity for mistakes:
you can pass an invalid action code.  The compiler can't catch this 
mistake.  You can catch it only at run time.

A worse problem is that different operations may require different
kinds of parameters.  Suppose, for example, that you encapsulate an
indexed file, with different action codes corresponding to OPEN,
START, READ NEXT, CLOSE, and so forth.  The OPEN operation needs
an access mode, and maybe a file name; START needs a key; READ NEXT
needs a record buffer; CLOSE needs none of the above.  With a 
one-size-fits-all interface you have to pass everything every time, 
relevant or not.

(Strictly speaking that's not true: you can omit later parameters
if you know they won't be used.  However this practice merely 
replaces one ugliness with another.  In any case you can't omit a
parameter at the beginning, or in the middle, without omitting all
of the subsequent ones.)

The worst problem arises when you add a new operation with a new
kind of parameter.  In the example of the file module, you might need
an operation to count the records in a specified range, so that you
have to pass a beginning key and an ending key.  With a one-size-
fits-all interface you have to recode every program that calls the
module, in order to pass an unused dummy field.

With separate entry points none of these problems arise.  You can't
pass an invalid action code because you don't pass any action codes.
You only pass what you need to pass.  If you need to add a new 
operation, add it -- none of the old interfaces need to change.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html

> --
> Bill Klein
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: entry

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000415101243.16023.00001564@ng-ck1.aol.com>`
- **References:** `<38F86702.10A9@swbell.net>`

```
Michael C. Kasten writes ...

[a lot of accurate stuff about ENTRY points]

I would add that using ENTRY points can accomplish a lot of the functionality
people brag about for DLLs (Dynamic Link Libraries - a PC / UNIX construct that
has migrated to the mainframe).

<Ad>
Our three day course "Inter-Language Communication in OS/390" includes
discussions on ENTRY functionality for the four languages covered in the course
(COBOL, PL/I, C, and Assembler) as well as a wealth of related information,
including DLLs in the mainframe environment. Please check out our website (see
signature), go to Topics, then Language Environment (LE), this will point you
to the course description and topical outline.)
</Ad>

Regards,



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: entry

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Iq%J4.17065$0o4.116170@iad-read.news.verio.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net>`

```
In article <38F86702.10A9@swbell.net>,
Michael C. Kasten <mck9@swbell.net> wrote:

[snippage]

>The possibility of "fall through" logic is no more a reason to avoid
>ENTRY statements than it is a reason to avoid subprograms.  It is a
>hazard inherent in COBOL syntax.  It is a reason to write your code
>carefully.

With all due respect, Mr Kasten, this sort of wording has been applied to
such 'useful' statements as the ALTER TO PROCEED TO, the GO TO DEPENDING
ON, the MOVE CORRESPONDING, the 66 RENAMES, the use of COMP
(binary) numbers to allow for bit-level manipulations...

... *all* of these are 'hazard(s) inherent in COBOL syntax' and
'reason(s) to write your code carefully'; seeing the ENTRY statement
placed in such illustrious company gives me a bit of... pause, to say the
least.

DD
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net>`

```
I never realized you were a Language Luddite, Doc.

ALTER and GO TO DEPENDING ON were new tools in the kit; they were at least
worth a try; after-the fact criticism is nothing more than 20-20 hindsight.

Hell, Microsoft at least gave 'Bob' the ole college try!
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ku2K4.17072$0o4.116285@iad-read.news.verio.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net>`

```
In article <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
>I never realized you were a Language Luddite, Doc.

I never realised that you were not conversant with the accepted definition
of 'Luddite', Mr Mattias; according to http://www.m-w.com it is:

--begin quoted text:

broadly : one who is opposed to especially technological change

-end quoted text

Please be so kind as to point out what I have written which causes you to
conclude that I am opposed to such things?

>
>ALTER and GO TO DEPENDING ON were new tools in the kit; they were at least
>worth a try; after-the fact criticism is nothing more than 20-20 hindsight.

Mr Mattias, I have offered no criticism... a careful reading of what I
have written (if, in fact, you mgiht find someone to perform the task of
doing so as it seems to be beyond your abilities) might show that I have
placed another bit of then language into a class which had been described
by the very language used.  I have criticised *nothing* (except for you,
of course) and I defy your ability to show where I have done so in this
thread.

(pardon my rather... *curt* dismissal (and gratuitous insults, as
well) but I, for one, would *not* like to get a 2:am call because someone
had to fix a subroutine which used the ENTRY feature and didn't quite
understand how to deal with it)

>
>Hell, Microsoft at least gave 'Bob' the ole college try!

... and I don't recall that I criticised them for that, either.

DD

>
><docdwarf@clark.net> wrote in message
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8db6bo$on8$1@news.inet.tele.dk>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net> <ku2K4.17072$0o4.116285@iad-read.news.verio.net>`

```
Mr. DD

According to your kind link, Luddite could refer to Ned Ludd. A very
destuctive person, an naive too. By the way - many workers were killed
during the strike.

The meaning of luddite is not always to be translated in the 'broadly'
meaning. You could perhaps add some flavours to it, depending on the
context. Unfortunately your kind link is unable to help us there.

Please have a look:
http://www.harcourt.com/dictionary/def/6/0/4/0/6040300.html

http://www.iversonsoftware.com/sociology/l.html#Luddite

You will learn from my links that there is a difference between being a
luddite and to be luddite.

Just thought you'd like to know,

Regards
Ib



docdwarf@clark.net skrev i meddelelsen ...
>In article <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net>,
>Michael Mattias <michael.mattias@gte.net> wrote:
…[16 more quoted lines elided]…
>>worth a try; after-the fact criticism is nothing more than 20-20
hindsight.
>
>Mr Mattias, I have offered no criticism... a careful reading of what I
…[22 more quoted lines elided]…
>>> With all due respect, Mr Kasten, this sort of wording has been applied
to
>>> such 'useful' statements as the ALTER TO PROCEED TO, the GO TO DEPENDING
>>> ON, the MOVE CORRESPONDING, the 66 RENAMES, the use of COMP..
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fjK4.17111$0o4.116708@iad-read.news.verio.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net> <ku2K4.17072$0o4.116285@iad-read.news.verio.net> <8db6bo$on8$1@news.inet.tele.dk>`

```
In article <8db6bo$on8$1@news.inet.tele.dk>, Ib Tanding <ib@tanding.dk> wrote:
>Mr. DD
>
>According to your kind link, Luddite could refer to Ned Ludd.

This is, or so I was taught, why one sites definitions and sources... they
are a beginning, that is all.

The term (according to the link) 'perhaps from Ned Ludd'... and I recall
reading, someplace, that this might be a fictional character as well,
similar to the American Paul Bunyan.

>A very
>destuctive person, an naive too. By the way - many workers were killed
…[3 more quoted lines elided]…
>meaning.

This agrees with my experience, Mr Tanding... *nothing* is 'always',
including this statement... hence my including the definition from the
start.  If there's a disagreement in definition then it should be settled
before Logic is done... or so I was taught, so long ago.

>You could perhaps add some flavours to it, depending on the
>context. Unfortunately your kind link is unable to help us there.
…[7 more quoted lines elided]…
>luddite and to be luddite.

Greatly appreciated, Mr Tanding, but what I see to be central to all
definitions is an antipathy (based on fear or ignorance) towards
technological advances; I fail to see where I have demonstrated this and
thus my rather... pointed reply to Mr Mattias.

DD

>docdwarf@clark.net skrev i meddelelsen ...
>>In article <AG0K4.381$hA6.75035@dfiatx1-snr1.gtei.net>,
…[53 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 4)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F8A4D2.626A@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
> In article <38F86702.10A9@swbell.net>,
…[17 more quoted lines elided]…
> least.

My point was not "Use it carefully and you'll be okay," a sentiment
which has indeed been applied to various evil constructs.  My point
was that using ENTRY statements doesn't require any more caution,
with regard to fall-through logic, than you need to exercise anyway.

In the absence of an explicit ENTRY statement, the PROCEDURE DIVISION
statement plays exactly the same role, except that it doesn't assign
a distinct name to the (single) entry point.  Whichever place the
flow of control begins, it flows downward until something stops it.

Mr. Klein's posting seemed to imply that the risk of fall-through
logic was a reason to avoid ENTRY statements.  (Maybe he didn't mean
it that way; maybe he merely meant to clarify the semantics.)  There
may be reasons to avoid ENTRY statements, but this isn't one of them.
There is an equal risk of fall-through logic whether you use ENTRY or 
not, except of course that ENTRY statements can give you more places to
start falling.

When I use ENTRY statements it usually looks approximately like this:

 PROCEDURE DIVISION.

    ENTRY JKOPEN USING WHATEVER.
    PERFORM 0000-JKOPEN.
    EXIT PROGRAM.

    ENTRY JKSTART USING WHATEVER-ELSE.
    PERFORM 1000-JKSTART.
    EXIT PROGRAM.

    ENTRY JKREADN USING ANOTHER-THING.
    PERFORM 2000-JKREADN.
    EXIT PROGRAM.

    ...etc...

 0000-JKOPEN.
    ...

With this approach the various entry points function as separate
modules listed conveniently at the top of the PROCEDURE DIVISION,
each with a distinct name and a single exit point.  They generally
access some of the same resources and perform some of the same 
underlying paragraphs; that's the reason for putting them in the same 
subprogram.

The compiler doesn't require your entry points to be so tidy.  You
can sprinkle them throughout the PROCEDURE DIVISION and make a thorough
hash of things if you want to.  I have yet to see a language that does
not permit you to exercise bad judgement, and COBOL is more permissive
than most.

There are two main disadvantages of using multiple entry points:

1. The name of an entry point needn't bear any relationship to the
name of the subprogram where it resides.  Consequently it may be hard
to keep track of which entry points are where.  You have to rely on some 
combination of memory, naming standards, and documentation.

2. Typically a given entry point receives as its parameters only a
subset of the items in the LINKAGE SECTION.  Consequently it is 
possible for an entry point to reference a parameter which was never
passed to it.  The compiler won't complain, but the results at run
time are likely to be unpleasant.

Whether the benefits are worth the risks is one of those judgement
calls that we're paid to make.  In my own experience, the use of
multiple entry points has often enabled me to do things that would have
been much clumsier to do by any other means.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 5)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f92cd0.41938214@nntp.sprynet.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net>`

```
On Sat, 15 Apr 2000 12:20:18 -0500, "Michael C. Kasten"
<mck9@swbell.net> wrote:

>When I use ENTRY statements it usually looks approximately like this:
>
…[48 more quoted lines elided]…
>been much clumsier to do by any other means.

Is it possible to use ENTRY points in a dynamically called program?
It seems to me it's not, because how do you specify the name of the
executable module to load?

Just wondering.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LguK4.8286$_H2.186282@news.swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38f92cd0.41938214@nntp.sprynet.com>`

```

Frank Swarbrick <infocat@sprynet.com
>
> Is it possible to use ENTRY points in a dynamically called program?
> It seems to me it's not, because how do you specify the name of the
> executable module to load?
>

You're correct. You can't expect the operating system to examine every
DLL in the system to find the entry points. Usually you have to tell
the linkage editor (of the main program) which dynamically-loaded
modules contain which entry points. Using the Fijutsu compiler on the
PC, you tell the Fijutsu run-time via an INI-type file which DLLs
contain which entry points.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dbmpl$ci9$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38f92cd0.41938214@nntp.sprynet.com>`

```
see bottom


Frank Swarbrick <infocat@sprynet.com> wrote in message
news:38f92cd0.41938214@nntp.sprynet.com...
> On Sat, 15 Apr 2000 12:20:18 -0500, "Michael C. Kasten"
> <mck9@swbell.net> wrote:
…[62 more quoted lines elided]…
>

    The way I handle it is to call the "real" name before calling the entry
point.
The "real" (or normal) part of the program can be used to initalize
the working storage, etc.

    Also, if using MF int/gnt, if you build the program into an LBR, and
open
the LBR, than all of the entry points will be visable.  This is how MF
handles workbench and (I think) Netx.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fa6b2f.31742003@nntp.sprynet.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38f92cd0.41938214@nntp.sprynet.com> <8dbmpl$ci9$1@ssauraaa-i-1.production.compuserve.com>`

```
On Sun, 16 Apr 2000 02:32:08 -0400, "Russell Styles"
<RWSTYLES@COMPUSERVE.COM> wrote:

>Frank Swarbrick <infocat@sprynet.com> wrote in message
>news:38f92cd0.41938214@nntp.sprynet.com...
…[20 more quoted lines elided]…
>handles workbench and (I think) Netx.

Can you give me an example?  Can you do something like:

CALL DYNAMIC-NAME
CALL ENTRY-POINT

Doesn't seem likely.  I wonder if it depends on the platform, though.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 8)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dgpps$jv3$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38f92cd0.41938214@nntp.sprynet.com> <8dbmpl$ci9$1@ssauraaa-i-1.production.compuserve.com> <38fa6b2f.31742003@nntp.sprynet.com>`

```

Frank Swarbrick <infocat@sprynet.com> wrote in message
news:38fa6b2f.31742003@nntp.sprynet.com...
> On Sun, 16 Apr 2000 02:32:08 -0400, "Russell Styles"
> <RWSTYLES@COMPUSERVE.COM> wrote:
…[12 more quoted lines elided]…
> >> "Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch
Hunt"
> >>
> >
> >    The way I handle it is to call the "real" name before calling the
entry
> >point.
> >The "real" (or normal) part of the program can be used to initalize
…[17 more quoted lines elided]…
>

    Yes, that is what I was saying.  I stated MF workbench and netx
products.
 I think that the unix products work the same way.

    Example (dos/windows/netx):

    CALL "PROGRAMX".
    CALL "ENTRY_POINT_NUMBER_001" USING PARM1 PARM2 PARM3.
    CALL "ENTRY_POINT_NUMBER_002" USING PARM3 PARM4 PARM5.
    CANCEL "PROGRAMX".

    The call to "PROGRAMX" can be ommitted if PROGRAMX is built into an open
LBR
file.  Note that PROGRAMX is limited to 8 characters.  Use Call statement to
open an LBR.
Ie, CALL "XYZ.LBR".  Will NOT do anything, even if XYZ.INT or XYZ.GNT exist
in XYZ.LBR.
But now, any entry point in any program in XYZ.LBR will be visable.

    Note that a mismatch between (physical) file name and program ID can
cause problems.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000416092846.25753.00001902@ng-fk1.aol.com>`
- **References:** `<38f92cd0.41938214@nntp.sprynet.com>`

```
Frank Swarbrick writes...

[snip]

>
>Is it possible to use ENTRY points in a dynamically called program?
…[3 more quoted lines elided]…
>Just wondering.

In the MVS, OS/390 world, you can dynamically call ENTRY points if the ENTRY
names are established in the load library directory as ALIASes of the main
module.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fa6ba2.31857009@nntp.sprynet.com>`
- **References:** `<38f92cd0.41938214@nntp.sprynet.com> <20000416092846.25753.00001902@ng-fk1.aol.com>`

```
On 16 Apr 2000 13:28:46 GMT, scomstock@aol.com (S Comstock) wrote:

>Frank Swarbrick writes...
>
…[11 more quoted lines elided]…
>module.

Now that sounds interesting.  Any idea if this works for VSE?

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"Ignorance and prejudice - and fear walk hand in hand" --Rush "Witch Hunt"
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FB32A1.652C427F@Azonic.co.nz>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net>`

```
Michael C. Kasten wrote:

> which has indeed been applied to various evil constructs.  My point
> was that using ENTRY statements doesn't require any more caution,
…[47 more quoted lines elided]…
> than most.


ENTRYs are not paragraphs, ENTRYs are not sections.  While your code may
work fine and there is no obvious problems likely to occur your "You can
sprinkle them thoughout PD" is rather misleading when taken in
cojunction with your example code.

For example is someone took your code and 'sprinkled' an ENTRY into PD
thus:

      PROCEURE DIVISION.
      Main SECTION.
      Normal-entry.

          PERFORM Xyz
          EXIT PROGRAM.       
   
      Xyz.

          do this
          do that
          .

     ENTRY JKSTART USING WHATEVER-ELSE.
         PERFORM 1000-JKSTART.
         EXIT PROGRAM.

This will have exactly the drop-through problem you seem to dismiss. 
Perhaps you never realised that this drop-through will occur and never
saw the implication in the manual but managed to avoid it with
dumb-luck, or just never noticed when it happened.

Not that one would need to avoid ENTRY, it just needs more care than you
advocate.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FBA920.179D@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz>`

```
Richard Plinston wrote:

[snip -- quoting me]

> > The compiler doesn't require your entry points to be so tidy.  You
> > can sprinkle them throughout the PROCEDURE DIVISION and make a thorough
…[7 more quoted lines elided]…
> cojunction with your example code.

When I wrote that "You can sprinkle tnem throughout the PD", I meant
only that the compiler won't stop you.  I never meant to imply that
you *should* sprinkle them, nor did I expect that anyone would read
it that way.  The code you show below is a good example of why you 
*shouldn't* sprinkle them.

> For example is someone took your code and 'sprinkled' an ENTRY into PD
> thus:
…[21 more quoted lines elided]…
> dumb-luck, or just never noticed when it happened.

I managed to avoid it by knowing what I was doing, and by structuring
my code in such a way as to minimize the hazards.  I can't eliminate
the hazards.  In particular I can't eliminate the hazard of inept
maintenance.

Yes, ENTRY has some drawbacks.  So do the alternatives.

> Not that one would need to avoid ENTRY, it just needs more care than you
> advocate.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dgfen$h3r$1@news.igs.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net>`

```
I find it amusing that such fuss is raised over entry points.  The new
constructs of Begin Object and End Object are specifically designed to
prevent that type of problem(multiple methods within one object-module).
They also add the functionality of parameter checking at link time so that
you do not get the problem of badly matched parameters that vary between the
methods. Commonality of code is nicely broken out buy sub methods that can
be SELF referenced without any overhead.

Even if the modern Cobol programmer never plans to use "objects" as building
blocks, the object oriented new things in the language should be learned as
a replacement for subroutines. Cobol Subroutine methodology is well suited
for top top design, but poor for bottom up tools.  The new "OOP" stuff is
the exact opposite. A file object makes a thousand times more sense than a
file subroutine.

Michael C. Kasten wrote in message <38FBA920.179D@swbell.net>...
>Richard Plinston wrote:
>
…[52 more quoted lines elided]…
>> advocate.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dhnct$1bh8$1@news.hitter.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dgfen$h3r$1@news.igs.net>`

```

donald tees wrote in message <8dgfen$h3r$1@news.igs.net>...
>I find it amusing that such fuss is raised over entry points.
[...]
> A file object makes a thousand times more sense than a
>file subroutine.

Ironically, I find it amusing that any effort is being spent creating
file classes (not objects) that return records. This seems the
antithesis of OO and, therefore, makes no sense at all. ;-)

The beauty and power of OO lies in its ability to deal with
abstraction while hiding the details of the implementation.
Both file and record are implementation details and should
be hidden within the class.

A collection returning objects and implemented as a file of
records does make sense and fits well within the "thesis"
of OO.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dg44p$2l8t$1@news.hitter.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net>`

```

Michael C. Kasten wrote in message <38FBA920.179D@swbell.net>...
>Richard Plinston wrote:
[...]
>> For example is someone took your code and 'sprinkled' an ENTRY into PD
>> thus:
>>
[.... snipped fall-through example]
>>
>> This will have exactly the drop-through problem you seem to dismiss.
…[7 more quoted lines elided]…
>maintenance.

I avoided the problem by enclosing the high-level procedure for
each ENTRY within its own paragraph. As in,

gregorian-6-to-integer.
    entry "dateg6i" using g6 integer-date.
    *> high-level code
    *> performing common low-level code
    exit program
    .
By placing all such paragraphs, together, at the beginning of the
program, the effect is, as if, there are X number of "first" paragraphs.

With this arrangement and using only PERFORM paragraph-name,
there can be no problem with fall-through.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dvr7d$lkd$1@nnrp1.deja.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net>`

```
In article <38FBA920.179D@swbell.net>,
  mck9@swbell.net wrote:
> Richard Plinston wrote:

> I managed to avoid it by knowing what I was doing, and by structuring
> my code in such a way as to minimize the hazards.  I can't eliminate
> the hazards.  In particular I can't eliminate the hazard of inept
> maintenance.

While you had arranged the code so that the hazard didn't occur, I
would suggest that in order to help eliminate the hazard you should put
paragraph or section headers before the ENTRY statements (as I do).

An 'open' ENTRY is an invitation to later maitenance causing a drop
through.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 8)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3903AA53.2EE9@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com>`

```
riplin@kcbbs.gen.nz wrote:
> 
> In article <38FBA920.179D@swbell.net>,
>   mck9@swbell.net wrote:
> > Richard Plinston wrote:

[Actually *I* wrote the following, in response to Richard Plinston:]

> > I managed to avoid it by knowing what I was doing, and by structuring
> > my code in such a way as to minimize the hazards.  I can't eliminate
…[8 more quoted lines elided]…
> through.

Please explain.  I don't see why the addition of superfluous paragraph
or section headers would reduce the risk of faulty maintenance.

In no case does a paragraph header affect the flow of control if control 
falls through it -- unless it is the object of a THRU clause, which is 
not likely in this context.  Whether control falls through depends on 
what's in the earlier paragraph, and on how it's invoked.

I think the rules are a little different for sections, but since I 
don't use them, I'm a little hazy on the details.  In any case I don't 
see any more advantage from section headers than from paragraph headers.

When I group my ENTRY points up at the top of the PROCEDURE DIVISION,
the very absence of paragraph headers gives this region of code a
distinctive appearance, emphasizing that this code is *not* the
usual sort of procedural code that one normally sees -- but rather a
separate interface area within the PROCEDURE DIVISION.

The presence of a paragraph or section header would make the ENTRY
statement harder to spot, because it would make the paragraph look
more like other paragraphs.  It would also imply, to my eyes at
least, that the paragraph or section was intended to be the object of a 
PERFORM or GO TO -- neither of which is likely to be appropriate for an 
entry point, especially when the ENTRY statement includes a USING 
clause.

What have I missed?  Why do you think a paragraph or section header
offers any protection?

(Context: In an earlier post I had outlined my usual way of coding
ENTRY statements:

 PROCEDURE DIVISION.

    ENTRY JKOPEN USING WHATEVER.
    PERFORM 0000-JKOPEN.
    EXIT PROGRAM.

    ENTRY JKSTART USING WHATEVER-ELSE.
    PERFORM 1000-JKSTART.
    EXIT PROGRAM.

    ENTRY JKREADN USING ANOTHER-THING.
    PERFORM 2000-JKREADN.
    EXIT PROGRAM.

    ...etc...

 0000-JKOPEN.
    ...
)

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 9)_

- **From:** "The COBOL Frog" <H.Klink@IMN.NotThisPart.nl>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e10m0$fra$1@porthos.nl.uu.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net>`

```
--> (RESPONSES INSERTED)

Michael C. Kasten <mck9@swbell.net> wrote in message news:3903AA53.2EE9@swbell.net...
> riplin@kcbbs.gen.nz wrote:
> > 
…[24 more quoted lines elided]…
> what's in the earlier paragraph, and on how it's invoked.

--> I think [s]he (riplin@kcbbs.gen.nz) means with "invitation to later maitenance causing a drop through":

{{enlarged change for necessary repairing maintenance because of the possible drop-through whenever the statement before the entry statement is reached under control of a perform statement}}

> 
> I think the rules are a little different for sections, but since I 
…[7 more quoted lines elided]…
> separate interface area within the PROCEDURE DIVISION.

--> Very true. I agree.

> 
> The presence of a paragraph or section header would make the ENTRY
…[5 more quoted lines elided]…
> clause.

--> Very true. I agree.

> 
> What have I missed?  Why do you think a paragraph or section header
> offers any protection?

--> See above.

Like you show in the code hereafter, I prefer ENTRY's in the main para/section. And by rule, an ENTRY statement is either the first one in the procedure division or preceded by an EXIT PROGRAM (or STOP RUN or GOBACK (an IBM-invented extension until the next standard)).

The code shown below is f.e. the perfect mask/template for creating a DLL.
(Minor details in this discusson: The entry names should in quotes and a paragraph name is missing after the procedure header).

> 
> (Context: In an earlier post I had outlined my usual way of coding
…[23 more quoted lines elided]…
> http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 10)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3904E3B3.3789@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e10m0$fra$1@porthos.nl.uu.net>`

```
The COBOL Frog wrote, amid snippage:
> 
> Michael C. Kasten <mck9@swbell.net> wrote in message news:3903AA53.2EE9@swbell.net...
> > riplin@kcbbs.gen.nz wrote:
.> > > While you had arranged the code so that the hazard didn't occur,
I
> > > would suggest that in order to help eliminate the hazard you should put
> > > paragraph or section headers before the ENTRY statements (as I do).
…[16 more quoted lines elided]…
> statement is reached under control of a perform statement}}

I understand that [s]he  is referring to later maintenance.  What I
don't understand is how superfluous procedure headers will make
future maintenance less likely to produce inadvertent drop-through
logic.

The way I code my ENTRY statements, nothing preceding any ENTRY 
statement can ever be the target of a PERFORM (or GO TO for that 
matter).  As long as that convention is followed, the only way to drop 
through an ENTRY statement is for someone to omit an EXIT PROGRAM (or 
GOBACK, or whatever).

Later maintenance can always disrupt my tidy schemes.  When that
happens, a paragraph header will not prevent an inadvertent 
drop-through.

> (Minor details in this discusson: The entry names should in quotes and > a paragraph name is missing after the procedure header).

You're right, of course, about the quotes.  Oops. 

I don't know what you mean about a paragraph name missing from the 
procedure header.  The only procedure header shown is "0000-JKOPEN.",
which *is* a paragraph name.

Perhaps by "procedure header" you are referring to the PROCEDURE
DIVISION statement.  However with the compilers I'm familiar with,
the PROCEDURE DIVISION statement does not need to be followed by a
paragraph name (or section name).  It's possible to write an entire
PROCEDURE DIVISION with no paragraph names or section names at all.
Not necessarily wise, but possible.

> > (Context: In an earlier post I had outlined my usual way of coding
> > ENTRY statements:
…[19 more quoted lines elided]…
> > )

Michael C. Kasten mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 11)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e2uv2$951$1@news.igs.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e10m0$fra$1@porthos.nl.uu.net> <3904E3B3.3789@swbell.net>`

```
Michael C. Kasten wrote in message <3904E3B3.3789@swbell.net>...
>The COBOL Frog wrote, amid snippage:
>>
>> Michael C. Kasten <mck9@swbell.net> wrote in message
news:3903AA53.2EE9@swbell.net...
>> > riplin@kcbbs.gen.nz wrote:
>.> > > While you had arranged the code so that the hazard didn't occur,
>I
>> > > would suggest that in order to help eliminate the hazard you should
put
>> > > paragraph or section headers before the ENTRY statements (as I do).
>> > >
…[6 more quoted lines elided]…
>> > In no case does a paragraph header affect the flow of control if
control
>> > falls through it -- unless it is the object of a THRU clause, which is
>> > not likely in this context.  Whether control falls through depends on
>> > what's in the earlier paragraph, and on how it's invoked.
>>
>> --> I think [s]he (riplin@kcbbs.gen.nz) means with "invitation to > >
later maitenance causing a drop through":
>>
>> {{enlarged change for necessary repairing maintenance because of the
…[7 more quoted lines elided]…
>
Well, first you adopt a standard making "THRU" compulsory, so that programs
can get screwed up.  Then you adopt a standard making "EXIT" compulsory so
that you cannot screw up. Then, when they get screwed up anyway, you adopt
another standard to put in section headers so that the screw ups are
invisible.  Then everything works, but nobody knows why.  It is really
simple when you understand it.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 11)_

- **From:** "The COBOL Frog" <H.Klink@IMN.NotThisPart.nl>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e6qe3$3la$1@porthos.nl.uu.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e10m0$fra$1@porthos.nl.uu.net> <3904E3B3.3789@swbell.net>`

```
Michael C. Kasten <mck9@swbell.net> wrote in message news:3904E3B3.3789@swbell.net...
> The COBOL Frog wrote, amid snippage:
8<
> I understand that [s]he  is referring to later maintenance.  What I
> don't understand is how superfluous procedure headers will make
> future maintenance less likely to produce inadvertent drop-through
> logic.

It will lessen the likelyhood of a fall-through *under perform-control*. I'll demonstrate:

When you code f.e:

PARA.
    :
    :
    MOVE AA TO BB *> Or whatever imparative statement
                  *> execpt EXIT PROGRAM / STOP RUN / GOBACK
    ENTRY "ENTNAM" USING ...
    MOVE BB TO AA *> Or whatever statement

then a PERFORM PARA (or a PERFORM xxx THRU PARA or even a PERFORM sectionContainingPara) will execute bove MOVE's shown. When inserting an extra paragraph like:

PARA.
    :
    :
    MOVE AA TO BB *> Or whatever imparative statement
                  *> execpt EXIT PROGRAM / STOP RUN / GOBACK
EXTRA-PARA-2-PREVENT-FALL-THRU.
    ENTRY "ENTNAM" USING ...
    MOVE BB TO AA *> Or whatever statement

then a PERFORM PARA (or a PERFORM xxx THRU PARA) will execute bove MOVE's shown. The perform of a section containing PARA will still give a fall-through. When one is used to use sections, than insert a SECTION header as well, like:

PARA.
    :
    :
    MOVE AA TO BB *> Or whatever imparative statement
                  *> execpt EXIT PROGRAM / STOP RUN / GOBACK
EXTRA-SECTION SECTION.
EXTRA-PARA-2-PREVENT-FALL-THRU.
    ENTRY "ENTNAM" USING ...
    MOVE BB TO AA *> Or whatever statement

> The way I code my ENTRY statements, nothing preceding any ENTRY 
> statement can ever be the target of a PERFORM (or GO TO for that 
> matter).  As long as that convention is followed, the only way to drop 
> through an ENTRY statement is for someone to omit an EXIT PROGRAM (or 
> GOBACK, or whatever).

Right. That's why I like your style.

8<

> I don't know what you mean about a paragraph name missing from the 
> procedure header.  The only procedure header shown is "0000-JKOPEN.",
…[7 more quoted lines elided]…
> Not necessarily wise, but possible.

Omitting all paragraphs is non-standard. At least one paragraph is required in COBOL'85. The omission is allowed in COBOL 20xx. (Hopefully thinking that at least ONE of those X-es will be turn out to be a zero)
> 
> > > (Context: In an earlier post I had outlined my usual way of coding
…[3 more quoted lines elided]…
> > >
       Missing-Paragraph. *> under COBOL 85

> > >     ENTRY JKOPEN USING WHATEVER.
> > >     PERFORM 0000-JKOPEN.
…[17 more quoted lines elided]…
> http://home.swbell.net/mck9/cobol/cobol.html

Teaching Frog
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 12)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e9tq4$kvj$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e10m0$fra$1@porthos.nl.uu.net> <3904E3B3.3789@swbell.net> <8e6qe3$3la$1@porthos.nl.uu.net>`

```
<SNIP>


    You should have an exit program after the procedure division,
in case
someone calls the main program.

Omitting all paragraphs is non-standard. At least one paragraph
is required in COBOL'85. The omission is allowed in COBOL 20xx.
(Hopefully thinking that at least ONE of those X-es will be turn
out to be a zero)
>
> > > (Context: In an earlier post I had outlined my usual way of
coding
> > > ENTRY statements:
> > >
> > >  PROCEDURE DIVISION.
> > >
       Missing-Paragraph. *> under COBOL 85

> > >     ENTRY JKOPEN USING WHATEVER.
> > >     PERFORM 0000-JKOPEN.
…[17 more quoted lines elided]…
> http://home.swbell.net/mck9/cobol/cobol.html

Teaching Frog
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e5cug$d9j$1@nnrp1.deja.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net>`

```


> > > I managed to avoid it by knowing what I was doing, and by
structuring
> > > my code in such a way as to minimize the hazards.  I can't
eliminate
> > > the hazards.  In particular I can't eliminate the hazard of inept
> > > maintenance.

No but you could help.

> Please explain.  I don't see why the addition of superfluous
paragraph
> or section headers would reduce the risk of faulty maintenance.


> In no case does a paragraph header affect the flow of control if
control
> falls through it -- unless it is the object of a THRU clause, which
is
> not likely in this context.  Whether control falls through depends on
> what's in the earlier paragraph, and on how it's invoked.

Quite. But an ENTRY is _NOT_ a pargraph header, even if it looks like
one (by being in Column 8).

> When I group my ENTRY points up at the top of the PROCEDURE DIVISION,
> the very absence of paragraph headers gives this region of code a
> distinctive appearance, emphasizing that this code is *not* the
> usual sort of procedural code that one normally sees -- but rather a
> separate interface area within the PROCEDURE DIVISION.

You may see it this way.  Later maintenance programmers may not see it
quite the same way.


> The presence of a paragraph or section header would make the ENTRY
> statement harder to spot, because it would make the paragraph look
> more like other paragraphs.

ENTRYs already look too much like a paragraph, making them actually be
a paragraph will make them _work_ like a paragraph too.

> It would also imply, to my eyes at
> least, that the paragraph or section was intended to be the object of

It is to the eyes of a later maintenance programmer that is important.

 > PERFORM or GO TO -- neither of which is likely to be appropriate for
 an
 > entry point, especially when the ENTRY statement includes a USING
 > clause.

There is no reason at all that an ENTRY cannot be deliberately part of
the current execution sequence, as long as any linkage parameters have
the correct setting at the time the code is executed.

It is perfectly correct code to have:

      Write-Log.
      ENTRY "WriteLog" USING Message-Text.

         code to write message-text to a log file.

This could be executed from outside by CALL "writelog" USING ...
or it could be PERFORM Write-Log as long as Message-Text was valid
(for example by a SET or by the current call into the module).  This
may be bad practice but it is not necessarily inappropriate.

> What have I missed?  Why do you think a paragraph or section header
> offers any protection?

Because if there was a pargraph above the entry, or one was added by a
later programmer, then the code after the ENTRY would be included
within the scpoe of a PERFORM of that paragraph.  An ENTRY is _NOT_ a
paragraph header and does not terminate the paragraphs above.


> (Context: In an earlier post I had outlined my usual way of coding
> ENTRY statements:

Exactly, but you had also said that ENTRYs may be scattered throughout
the PD.

While your specific code groups all its ENTRYs at the head of the PD
this is not a requirement for ENTRYs, nor will later programmers
necessarily think it useful.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 10)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390659C0.4876@swbell.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e5cug$d9j$1@nnrp1.deja.com>`

```
riplin@kcbbs.gen.nz wrote:
> > Please explain.  I don't see why the addition of superfluous
> paragraph
…[10 more quoted lines elided]…
> one (by being in Column 8).

True, but utterly irrelevant.  I never said that an ENTRY is a
paragraph header, nor, in my example, did they start in column 8.  As
I recall they don't have to start in column 8.  I could be mis-
remembering on that point.

> > When I group my ENTRY points up at the top of the PROCEDURE DIVISION,
> > the very absence of paragraph headers gives this region of code a
…[5 more quoted lines elided]…
> quite the same way.

Neither you nor I can predict how later maintenance programmers will
see it.  All I can do is provide the best hints I can by various
stylistic devices.  I suppose I could include a fat comment block
hurling dire imprecations upon the heads of anyone corrupting the
purity of my design.  So far I haven't resorted to that.

> > The presence of a paragraph or section header would make the ENTRY
> > statement harder to spot, because it would make the paragraph look
…[3 more quoted lines elided]…
> a paragraph will make them _work_ like a paragraph too.

I don't *want* them to work like paragraphs.  I don't want them to
be PERFORMed or GOne TO.  I don't want to make it easy for anyone
to PERFORM them or GO TO them.

> > It would also imply, to my eyes at
> > least, that the paragraph or section was intended to be the object of
> 
> It is to the eyes of a later maintenance programmer that is important.

To *anyone's* eyes, it should be clear that my style of ENTRY cannot
possibly be PERFORMed or GOne TO unless you go to the extra trouble of
adding a paragraph or section header.  There's no way even to try.  It's 
not a matter of taste, opinion or perception.  There is no ambiguity 
whatsoever -- until someone adds a header.

>  > PERFORM or GO TO -- neither of which is likely to be appropriate for
>  an
…[17 more quoted lines elided]…
> may be bad practice but it is not necessarily inappropriate.

I regard it as abominable to PERFORM code which includes an ENTRY ...
USING statement.  I do not wish to encourage this practice by making it
easy to do, either deliberately or (more likely) by accident.

> > What have I missed?  Why do you think a paragraph or section header
> > offers any protection?
…[4 more quoted lines elided]…
> paragraph header and does not terminate the paragraphs above.

Again: I never said that an ENTRY is a paragraph header.  I cannot
fathom why you keep emphasizing this obvious fact, as if to correct me.

I don't put a paragraph above the entry.  Period.

Someone else might indeed do so, without realizing the inappropriate
fall-through that would result from PERFORMing it.  I try to reduce the 
likelihood of that mistake by giving the interface portion of the PD a 
distinctive, paragraph-free appearance, but it can still happen.

If I added a superfluous paragraph header such as you recommend, it 
would prevent the fall-through.  However it would make a different
kind of blunder possible: a PERFORM of what is really an entry point. 

There's room for disagreement about which kind of blunder is more
likely.  However the only way to be sure that no one will corrupt
your code in the future is to delete the source code and just keep
the object.  (I'm *not* recommending this practice.)

> > (Context: In an earlier post I had outlined my usual way of coding
> > ENTRY statements:
> 
> Exactly, but you had also said that ENTRYs may be scattered throughout
> the PD.

...which was a true statement.  It can be done.  The compiler permits
it (at least in COBOL II; since ENTRY is a non-standard extension I
can't make blanket statements about all compilers).

However I have repeatedly emphasized that I don't *favor* the scattering 
of ENTRY statements throughout the PD.  I was recommending precisely
the opposite practice.  My wording must not have been as clear as I
had thought, because both you and Richard Plinston appear to have
construed my meaning exactly backwards.
 
> While your specific code groups all its ENTRYs at the head of the PD
> this is not a requirement for ENTRYs, nor will later programmers
> necessarily think it useful.

No, it isn't a requirement for ENTRYs.  I already said as much.  Neither
is it a requirement to have ENTRYs in paragraphs.  As far as 
requirements are concerned, there aren't many.  We are at the mercy
of our own judgement.

Yes, later programmers may not necessarily think it useful.  So what?
Am I to confine myself to practices which everyone will necessarily
find useful?  Do you know of any such practices?

Later programmers may disagree with my preferences in any respect 
whatsoever.  But if I set precedents, and establish a consistent 
style across the application, there is some hope that my preferences 
will survive my departure for at least a few years.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 11)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vj7hgsg297aidf1kdd6n8g4b800f6dqosb@4ax.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB32A1.652C427F@Azonic.co.nz> <38FBA920.179D@swbell.net> <8dvr7d$lkd$1@nnrp1.deja.com> <3903AA53.2EE9@swbell.net> <8e5cug$d9j$1@nnrp1.deja.com> <390659C0.4876@swbell.net>`

```
"Michael C. Kasten" <mck9@swbell.net> wrote:
>>       Write-Log.
>>       ENTRY "WriteLog" USING Message-Text.
>> 
>>          code to write message-text to a log file.
 
>> This could be executed from outside by CALL "writelog" USING ...
>> or it could be PERFORM Write-Log as long as Message-Text was valid
>> (for example by a SET or by the current call into the module).  This
>> may be bad practice but it is not necessarily inappropriate.

>I regard it as abominable to PERFORM code which includes an ENTRY ...
>USING statement.  I do not wish to encourage this practice by making it
>easy to do, either deliberately or (more likely) by accident.

i was working on some correlation softwaare, and came across the need
for variables (sum of x's) to be run in different sections of code.
and obviously some sections of code will be run and some others won't.
so do you place every independant piece of code in it's own entry
statement, untouchable by other code? yes. but some other code you may
want to be performed by the entry statement. that might be the oo
code, but it is untouchable to the entry and procedure calls anyways.

and as others have pointed out, oo doesn't handle static stored
procedures (oltp) very well. you have to rely on the disk cache, if
there is one.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FB1040.943FC48F@cusys.edu>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net>`

```
"Michael C. Kasten" wrote:
> 
> Whether the benefits are worth the risks is one of those judgement
> calls that we're paid to make.  In my own experience, the use of
> multiple entry points has often enabled me to do things that would have
> been much clumsier to do by any other means.

I have been a bit intrigued by this command, but haven't ever been
tempted to use it.  What kind of function is simplified by having
multiple entry points?
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8det62$16tc$1@news.hitter.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu>`

```

Howard Brazee wrote in message <38FB1040.943FC48F@cusys.edu>...
>"Michael C. Kasten" wrote:
>>
…[7 more quoted lines elided]…
>multiple entry points?

I first used it for date and time validation and conversion routines.
Originally, I had 47 (IIRC) entries and 20 or so linkage items. I reduced
that number when I determined that some date formats were not used
in the system.

For validation and for conversion to a common integer form, each
ENTRY begins with a NUMERIC check, where appropriate,
followed by normalization of the value into a common work area.
Common routines (paragraphs) validate the values and convert
to INTEGER-OF-xxx form.

For conversion from the common integer form to an external format,
xxx-OF-INTEGER is used to create a normalized value that is
trimmed and formated as necessary.

By using OMITTED parameters, the last integer date calculated
is used in the conversion.

For example,
    move ws-week-start-date to ws-j5-date
    call "datej5i" using ws-j5-date omitted
    call "dateic6f" using omitted ws-pr1-report-start-date
    move ws-week-end-date to ws-j5-date
    call "datej5i" using ws-j5-date omitted
    call "dateic6f" using omitted ws-pr1-report-end-date
would window and convert 5-digit Julian dates to integer dates
followed by a conversion to formated 6-digit calendar dates.

Another example,
    call "datevc4" using ws-transaction-MMDD ws-valid-flag
    if ws-date-valid
        call "dateij7" using omitted ws-j7-date
        move ws-j7-date to ws-transaction-date
    else
        *> code for invalid date
    end-if
would window and convert a 4-digit calendar date to an normallized
8-digit gregorian date, validate the values, set the flag, and store
the result as an integer. The subsequent call returns a 7-digit Julian
date.

One final example,
    call "dateg6i" using ws-week-start-date ws-integer-date
    add 7 to ws-integer-date
    call "dateig6" using ws-integer-date ws-week-start-date
increments a 6-digit gregorian date by 1 week and had no problems
with Y2K and has no problems with leap years or transistions from
one month to the next.

IMO, for these date problems, there is no other COBOL solution as
easy to implement or as easy to use as a subprogram with multiple
entry points.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FBFD1B.30D2@Azonic.co.nz>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu> <8det62$16tc$1@news.hitter.net>`

```
Rick Smith wrote:
>     call "dateg6i" using ws-week-start-date ws-integer-date
>     add 7 to ws-integer-date
…[7 more quoted lines elided]…
> entry points.

ENTRY points have an advantage in that they may allow a module with
entries to be split into separate modules without changing the calling
programs.  The reverse is also that several called modules can be
combined into one by supplying ENTRY points to replace the module names
used by the calls.

However, I don't see that it is any less easy for your examples to be
done by having a single module entry (ie no ENTRY statements) and
include a function parameter.  This at least would make it easier to
find out what is going on.  When a new programmer comes across your code
he may spend some time looking for a 'dateg6i.cbl' source file.

What is less 'easy' about:

      CALL "datefun" USING Gregorian-to-Days
                           WS-week-start-date
                           WS-interger-date
      ADD 7             TO WS-integer-date
      CALL "datefun' USING Days-to-Gregorian
                           WS-integer-date
                           WS-week-start-date

The function codes can be defined in a copy book and can be used in an
EVALUATE inside the module.  Why do you think that ENTRYs are 'easier' ?

Richard
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dflmh$23tb$1@news.hitter.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu> <8det62$16tc$1@news.hitter.net> <38FBFD1B.30D2@Azonic.co.nz>`

```

Richard Plinston wrote in message <38FBFD1B.30D2@Azonic.co.nz>...
>Rick Smith wrote:
>>     call "dateg6i" using ws-week-start-date ws-integer-date
…[33 more quoted lines elided]…
>EVALUATE inside the module.  Why do you think that ENTRYs are 'easier' ?

Assume a system has 58 programs, 38 of which use the date/time
functions. Those 38 programs, collectively, call the date/time
functions in 600 statements. Comparing single-entry versus
multiple-entry we have: 1 additional source file, the copy book;
38 additional COPY statements; 600 additional parameters;
and 1 fewer CALL, the initial call to 'datetime' to make the entry
points available. IMO, using multiple-entry points is 'easier'
because there is less code.

My point was not that there is a huge difference; but that there
is enough difference to make multiple-entry programs worthwhile.

I would hope that new programmers would first read the system
documentation to understand how the system is built. Should
they do so, they will easily locate 'dateg6i'.

I would also hope that these new programmers would quickly
learn to appreciate the value of a library of well-tested subprograms.
Should they do so, they will not look for the source code until
they can demonstrate, with a test program, that the routine fails
with a given set of values.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yhXK4.37$OG4.9170@dfiatx1-snr1.gtei.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu> <8det62$16tc$1@news.hitter.net> <38FBFD1B.30D2@Azonic.co.nz> <8dflmh$23tb$1@news.hitter.net>`

```

Rick Smith <ricksmith@aiservices.com> wrote in message
news:8dflmh$23tb$1@news.hitter.net...
> I would hope that new programmers would first read the system
> documentation to understand how the system is built.


Um, new programmers should be aware that sometimes there is no such thing as
"system documentation" and that you are lucky if you find "individual
program" documentation.

Nonetheless, if there is a module called from more than one program, good
chance it's called from more than two programs, too.

MCM
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 10)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sYK4.17281$0o4.118602@iad-read.news.verio.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <38FBFD1B.30D2@Azonic.co.nz> <8dflmh$23tb$1@news.hitter.net> <yhXK4.37$OG4.9170@dfiatx1-snr1.gtei.net>`

```
In article <yhXK4.37$OG4.9170@dfiatx1-snr1.gtei.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
>
>Rick Smith <ricksmith@aiservices.com> wrote in message
…[7 more quoted lines elided]…
>program" documentation.

Why, Mr Mattias... whatever are you saying!  There's *always*
documentation... and sometimes it even reaches levels of thoroughness and
completeness as exemplified here:

<http://x41.deja.com/[ST_rn=ps]/getdoc.xp?AN=420073905&search=thread&CONTEXT=956060361.1320288277&HIT_CONTEXT=956060328.1321533440&hitnum=6>

DD
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dvs3o$mns$1@nnrp1.deja.com>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu> <8det62$16tc$1@news.hitter.net> <38FBFD1B.30D2@Azonic.co.nz> <8dflmh$23tb$1@news.hitter.net>`

```
In article <8dflmh$23tb$1@news.hitter.net>,
  "Rick Smith" <ricksmith@aiservices.com> wrote:

> Assume a system has 58 programs, 38 of which use the date/time
> functions. Those 38 programs, collectively, call the date/time
…[5 more quoted lines elided]…
> because there is less code.

If 'less code' meant 'easier' programming then everyone should be
writing in APL, or in as concise a form of C as it allows.

In fact the advantage of Cobol is a result of it _not_ being 'less
code'.

The real question is: which is easier to understand:

 >>     call "dateg6i" using ws-week-start-date ws-integer-date
or
> >      CALL "datefun" USING Gregorian-to-Days
> >                           WS-week-start-date
> >                           WS-interger-date

> My point was not that there is a huge difference; but that there
> is enough difference to make multiple-entry programs worthwhile.

That's OK, noone is trying to stop you using them.  I would prefer to
have the advantage of more descriptive function calls than the saving
of a few keystrokes (especially when I can easily cut and paste with my
development system).

> I would hope that new programmers would first read the system
> documentation to understand how the system is built. Should
> they do so, they will easily locate 'dateg6i'.

'System documentation' ?  You mean you have some ?  You mean it is
actually up to date ?  You mean someone actually bothers to read it ?


> I would also hope that these new programmers would quickly
> learn to appreciate the value of a library of well-tested
subprograms.

Whis is a point irrelevant to the argument.

> Should they do so, they will not look for the source code until
> they can demonstrate, with a test program, that the routine fails
> with a given set of values.

First they have to know which are 'correct results' and which are
failures.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e1jds$134i$1@news.hitter.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com> <8cjq7v$st4$1@slb6.atl.mindspring.net> <38F86702.10A9@swbell.net> <Iq%J4.17065$0o4.116170@iad-read.news.verio.net> <38F8A4D2.626A@swbell.net> <38FB1040.943FC48F@cusys.edu> <8det62$16tc$1@news.hitter.net> <38FBFD1B.30D2@Azonic.co.nz> <8dflmh$23tb$1@news.hitter.net> <8dvs3o$mns$1@nnrp1.deja.com>`

```

riplin@kcbbs.gen.nz wrote in message <8dvs3o$mns$1@nnrp1.deja.com>...
[...]
>'System documentation' ?

As in,
  "This is how to build (or rebuild) the system."
  "These are the required and optional components."
  "This is where you will find the library batch files."
  "This is how you create a distribution."
   etc.

> You mean you have some ?

Yes, but don't tell my boss! He has a weak heart!

> You mean it is actually up to date ?

No, there were some recent changes affecting both the
system docs and user manuals. These changes have not
yet been incorporated.

> You mean someone actually bothers to read it ?

To the best of my knowledge, no one else has ever seen,
or read, the system docs. I hope no one ever does.

The system is supposed to be discontinued. I will be the
last programmer to ever work with the code. The only reason
anyone would ever have to read the system docs is that I died
before the replacement system was completed.

Three times I inherited code that was poorly written and
undocumented. Three times I complained. The first two
times I ask for and was refused permission to rewrite the
systems. The third time I did not ask; I told.

[Summary of "poorly-written".
  First system: COBOL, 50K+ lines 5K+ GO TO, abbreviated
    identifiers, an outdated system flow chart showing relationship
    of some programs and files.
  Second system: C (some assembler), 20K+ lines 500+ goto,
    abbreviated identifiers (as in FORTRAN 66 with no identifier
    longer than 6 positions).
  Third system, Embedded C/ASM, 5K+ lines, abbreviated
    identifiers, 50% assembler, same areas defined separately
    in both C and ASM.]

My employer wanted me to adapt the code, from the third
system, to provide a great deal of specialization for each of
two large customers. I refused. Instead I wrote the system for one
customer from scratch, then adapted that code for the second.
Result? Customer happy, employer happy, programmer happy,
code well-written, easily understood, and documented.

For me, to not provide some useful documentation for code
I produce is unthinkable.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 8)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000418122911.20856.00000917@nso-fm.aol.com>`
- **References:** `<38FBFD1B.30D2@Azonic.co.nz>`

```
In article <38FBFD1B.30D2@Azonic.co.nz>, Richard Plinston <riplin@Azonic.co.nz>
writes:

>
>The function codes can be defined in a copy book and can be used in an
>EVALUATE inside the module.  Why do you think that ENTRYs are 'easier' ?
>

Having ENTRY points permits defining different working 'passed' parameters.
In the event of creating a global services sub-program that has character
manipulation,  date conversion, number formatting, and digit or bit extraction
routines all rolled into one.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39007DB4.7E2D@Azonic.co.nz>`
- **References:** `<38FBFD1B.30D2@Azonic.co.nz> <20000418122911.20856.00000917@nso-fm.aol.com>`

```
Sff5ky wrote:
> 
> In article <38FBFD1B.30D2@Azonic.co.nz>, Richard Plinston <riplin@Azonic.co.nz>
…[10 more quoted lines elided]…
> routines all rolled into one.

This doesn't answer why it is _easier_.  Without using ENTRYs exactly
the same can be done quite easily.  Just redefine the linkage sections
01 levals as required and use those redefinitions that match the
parameters being passed in.

       LINKAGE SECTION.
       01  Function-Type           PIC X.
           <  88 levels here if you like that sort of thing >
	    or use 78s or PIC X with values
		
       01  Parameter-1             PIC X(20).
       01  In-Date REDEFINES Parameter-1.
           03  In-CC               PIC 99.
           03  In-YY   etc
       01  In-Days REDEFINES Parameter-1 PIC s9(8).
           etc

       01  Parameter-2
           etc

       01  Parameter-3 etc

       PROCEDURE DIVISION USING Function-Type Parameter-1 Param        	
etc
       EVALUATE Function-Type
       WHEN Date-to-Days	
            use In-Date, Out-Days

       WHEN Days-to-Date
            use In-Days, Out-Date


Why would you think that this is harder ?
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 10)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390060E6.563C49A4@cusys.edu>`
- **References:** `<38FBFD1B.30D2@Azonic.co.nz> <20000418122911.20856.00000917@nso-fm.aol.com> <39007DB4.7E2D@Azonic.co.nz>`

```
Certainly it would give fewer programmers pause when it was time for
them to do maintenance.

If a coding technique is unfamiliar it should be significantly better to
be worth while adding it to code which will be maintained by someone
other than yourself.  Your code is familiar.  Multiple Entry code isn't
yet.

Heck - the reason Report Writer didn't have the wide acceptance which
its advocates wanted was because it wasn't THAT much easier than
conventional code.  And Report Writer had demonstrateable advantages.

So far I am agreeing with you.  But I would like to be sold on a new
technique - for real gains.

Richard Plinston wrote:
> 
> Sff5ky wrote:
…[45 more quoted lines elided]…
> Why would you think that this is harder ?
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000418122905.20856.00000916@nso-fm.aol.com>`
- **References:** `<38FB1040.943FC48F@cusys.edu>`

```
In article <38FB1040.943FC48F@cusys.edu>, Howard Brazee
<howard.brazee@cusys.edu> writes:

>
>I have been a bit intrigued by this command, but haven't ever been
>tempted to use it.  What kind of function is simplified by having
>multiple entry points?
>

This may not be a single function so much as a utility services DLL
or externally callable module.  Rather than coding function routines 
into multiple libraries and 'including' into multiple programs, put all the
utility functions into one global services DLL that is called by all programs.
Using dynamic linking, any changes to the functions within the DLL 
will become apparent in al programs upon implementation without having
to perform a massive recompile of your entire production library.  
Recovery is quick too if there is a problem, by restoring the previous 
version of the DLL.
I personally have not worked with the ENTRY point syntax on the mainframe
as yet, but hope to get there.  Currently, I am working with a mainline that 
receives a parameter that must match a function available within the
sub-program.
At some future date I hope to figure out how to get dynamic linkage to work
with multilpe entry point programs.
```

###### ↳ ↳ ↳ Re: entry

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FC9830.8E60CF0E@cusys.edu>`
- **References:** `<38FB1040.943FC48F@cusys.edu> <20000418122905.20856.00000916@nso-fm.aol.com>`

```


Sff5ky wrote:
> 
> In article <38FB1040.943FC48F@cusys.edu>, Howard Brazee
…[22 more quoted lines elided]…
> with multilpe entry point programs.

Please let us know of your results.  In my mainframe environment, it
still seems to be more bother than its worth - beyond playing with it a
couple of times.
```

#### ↳ Re: entry

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ckj2m$s5g$1@news.igs.net>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>`

```
Just use the entry statement exactly the same as if you were putting in
another PROCEDURE DIVISION statement, IE --entry using ..., then use a
GOBACK.

I've never used it in a mainline, and am not sure if it will work that way
or not.  Where I have used it is to provide several call methods for a
subroutine.

G Moore wrote in message <2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>...
>I had read in my cobol manual about the entry statement, allowing you
>to jump to any section of code an execute it. does anyone have a short
…[15 more quoted lines elided]…
>reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: entry

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cngrf$mhn$1@news.inet.tele.dk>`
- **References:** `<2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>`

```
Hi, I found something with local-storage in NetExpress:

======================
An example that shows how to use recursion to search a family tree:

identification division.
 program-id. family.
    . . .
 working-storage section.
 01  family-tree.
     03  individual    occurs 50.
         05  ind-name           pic x(30).
         05  eldest-pointer     pic 9(2).
         05  sibling-pointer    pic 9(2).

 local-storage section.
 01  tree-pointer      pic 9(2).

 linkage section.
 01  parent-pointer    pic 9(2).

 procedure division.
     move 1 to tree-pointer
     call "children" using tree-pointer
     stop run.

* If this person has no eldest child, routine "children"
* displays the person's name and does nothing more. Otherwise,
* this routine starts with the person's eldest child and calls
* itself for each sibling in turn.
  entry "children" using parent-pointer
     move eldest-pointer(parent-pointer) to tree-pointer
     if tree-pointer = 99
         display ind-name(parent-pointer)
     else
         perform until tree-pointer = 99
             call "children" using tree-pointer
             move sibling-pointer(tree-pointer)to tree-pointer
         end-perform
     end-if.
==========================
Was that what you are looking for. I have many examples on the Entry
statement, but I couldn't help it - I just had to put an new angle to the
local-storage discussion.

G Moore skrev i meddelelsen <2nvpes0v1senrol9hg1h9lm0gk5frrghef@4ax.com>...
>I had read in my cobol manual about the entry statement, allowing you
>to jump to any section of code an execute it. does anyone have a short
…[10 more quoted lines elided]…
>somewhere-in-module.


>
>*where is entry placed? does it use the linkage section by default?
>
>
>reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
