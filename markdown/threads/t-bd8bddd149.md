[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Your Comments...

_20 messages · 16 participants · 1999-04_

---

### Your Comments...

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
OK,

I am strong advocate and promoter of the COBOL language. I have 15+ years
experience in the industry and can program in C, VB, Delphi, COBOL and many
others. I am fed up with people stating ' COBOL is dead...'. Statements like
these are only spoken by ignorant, insecure people that want to project that
they know a lot in order to impress. My belief is that each language holds
its own.

One thing I'd noticed though, in the last few years, is that I can do more
and more in COBOL than before, without having to resort in any of the other
languages. Take the case of Fujitsu's PowerCOBOL for example. I no longer
have a need to use VB as much any longer.

However. It looks like some of our "own" COBOL people want to prevent this
progression of the language (I feel). The other day, I had a discussion
(maybe an argument?) with another fellow COBOL programmer, who insisted that
certain COBOL extentions are not necessary. His view was also sahred by
others...!

Based on that, I've assembled a list of questions that anyone can contribute
to. These were the "sticky points" of our conversations.

1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
MAINFRAME COBOL2 COMPILER.

3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
SITES I WORKED AT. SMALL PROGRAM BUT...).

8) LEVEL 66 AND 77 OBSOLETE.


Regards

Theo

COBOL lives...
```

#### ↳ Re: Your Comments...

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3707553F.7BC36329@worldnet.att.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
Westley Lodge Pty Ltd wrote:
> 
> OK,
…[23 more quoted lines elided]…
> THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

I'm no fan of OOP.  But I might try out O-O extensions if they're
available in the compiler, and I can figure out how it would help me.

> 
> 2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
…[3 more quoted lines elided]…
> MAINFRAME COBOL2 COMPILER.

Construct two equivalent examples, one with nested IF's and one with an
EVALUATE.  Generate the disassembly (use the LIST option in IBM COBOL II
and higher).  Inspect the generated code.  I doubt there's any
particular efficiency advantage one way or the other in the generated
code.  I use EVALUATE and like it, and that's in IBM COBOL II.

> 
> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
> PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

Again, if efficiency in the generated code is your criterion, run your
own tests and inspect the generated code.  In my experience, COBOL II
and higher use a very sophisticated optimizer, so code you've put in a
paragraph may end up being copied in-line where it's called.

I user in-line PERFORM loops.  New features are frequently shunned by
those people who say, "we've always done it this way in OS/VS COBOL,
anything else is probably bad".

My only recommendation is to use short in-line PERFORM's.  If the
indented code is quite complex it probably ought to be moved into a
paragraph of its own.  That may be more of a personal preference than an
absolute judgement on best practices.

> 
> 4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
> COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
> STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
> REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

I've used this feature, NOT AT END, END-READ, and like it.  The shop
standards people may blow a fuse.  Where I work, there's a general rule
that any I-O statement must be isolated in a paragraph by itself. 
Doesn't mean it can't be a loop, or can't set an EOF switch, or count
the number of records read/written, or perform some edit in a lower
level paragraph.  

> 
> 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
> INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

This subject frequently gets a lot of heated debate here.  I'm not
convinced that calling a section is faster than calling a paragraph. 
Again, generate some assembly code and see what the compiler really
does.  The current shop standards where I work are:  paragraphs only,
and no GO TO's or perform thru exit's.  Of course, there are a lot of
older programs that have GO TO and PERFORM ... THRU EXIT.

I haven't used SECTIONs in the procedure division in years, not even
with internal sorts.  
 
> 
> 6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
> GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
> WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

MOVE CORRESPONDING is no help to me.  I work with shop standards that
require each data division item to have a consistent prefix throughout
the 01 record.  So the datanames cannot legally by qualified and comply
to the shop standards I work with.

Saves some typing, though.

> 
> 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
> ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
> SITES I WORKED AT. SMALL PROGRAM BUT...).

Here's an interesting one.  I have seen compilers that re-ordered the
data division so that all 01 records with any initial data were grouped
together, and all 01 records with NO initial data were placed in a
seperate group.  If you rely on the order of 01 records when analyzing a
storage dump, this can be very frustrating.

Putting the entire working-storage section in one 01 record would solve
this problem the hard way.  I prefer to add VALUE clauses to every data
item in the working-storage section.

> 
> 8) LEVEL 66 AND 77 OBSOLETE.

I've been coding COBOL for 20 years now, and I've never used level 66,
nor have I ever worked on a production program that had a level 66.  I
don't miss level 77, and I don't believe it had any effect in the IBM
mainframe COBOL compilers I have worked with, except for requiring
elementary data items.

Based on a comment a few weeks ago, I believe some early COBOL compilers
actually used level 77 to manage storage in an unusual way.

> 
> Regards
…[3 more quoted lines elided]…
> COBOL lives...
```

##### ↳ ↳ Re: Your Comments...

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3707c6aa.8530731@netnews>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <3707553F.7BC36329@worldnet.att.net>`

```
'Twas Sun, 04 Apr 1999 07:04:15 -0500, when Arnold Trembley
<arnold.trembley@worldnet.att.net> illuminated comp.lang.cobol thusly:

>Based on a comment a few weeks ago, I believe some early COBOL compilers
>actually used level 77 to manage storage in an unusual way.

I assume that your definition of "early" includes the entire 20th century.
```

#### ↳ Re: Your Comments...

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3707584B.3909@zag.si>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
Westley Lodge Pty Ltd wrote:
> 
> OK,
…[6 more quoted lines elided]…
> its own.
I have 15 years exp. in Pascal,C,Delphi,Cobol,Clipper,Macro,SQL etc. and
I totally
agree with you. There is no perfect language at all. Actually when I
program things end-user would like to have, I see Cobol more powerfull
than
any other languages. Why ?
It runs on almost every platforms including MsDos, which is most cheaper
then
any other. I've been in position to watch our concurence stuffing PC's
with
some Visual stuff in the place of current VAX/Vms Machine. 
Each PC cost avg. $2000-$2500 to work properly with Win NT's. They have
200 PC's,
so 200x$2000=400000$, server is another $20000. 
Each change at their program written in Delphi tooks at least 2-3 days.
I don't
agree with people saying well it is almost year 2000, now is Visual
stuff trend.
They usually don't know even how a program would looks like at the end,
not to
mention how to come to some results. Thru my prg.years I made several
libraries
for several platforms including currently VAX/VMS Cobol. 
I can make a program who on example collects some data, then shows it
into a table,
sorting printing etc. in a 4 hrs. I hadnt been able to do that even in
Clipper,
I am a fast writer tho. Not to mention even data dameges, broken indexes
etc..

> 1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
> THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.
Don't quite understand this.

> 2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
> STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
> NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
> BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
> MAINFRAME COBOL2 COMPILER.

Cobol's IF is much faster then EVALUATE on VAX, Alpha and PC platform.
It depends
on how cobol compiler is writen tho. But EVALUATE is more readble then
IF, so
at the points where if have to decide which one will be in the code, 
I use EVALUATE's at the places they execute only few times, and IF's in
several PERFORM's
where I need efficient code.

> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
> PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

What is INLINE PERFORM ?

> 4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
> COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
> STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
> REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

I never actually use AT END or INVALID form. I rather check every error
at the
run-time and then decide will program be continuing or not 
So I use declarative section
DECLARATIVES.
Start-Dec.
   USE STANDARD ERROR..... <All file handles>
End-Dec. 
END DECLARATIVES.

and then issusing READ <file> REGARDLESS
                  IF FS-Ok THEN
                  ...

> 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
> INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

Actually I didn't test that, but I think difference is more logicaly
then physical.
Compiled code would produce CALL to that routine and then RETurn. But as
I've said
didn't test it.

> 
> 6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
> GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
> WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

I use MOVE CORR only in stupid program's (don't get me wrong, I call
them stupid,
when they aren't part of main code, but they are more some kind of
util's).
MOVE CORR has to be very danger in cases, you are changing program after
5 years
and puting some new variables in that group. So I prefer taking control
over each
field in a group.

> 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
> ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
> SITES I WORKED AT. SMALL PROGRAM BUT...).

At working-storage I usually do grouping, like an example

01 c-CONSTANTS.
   03 c-Current-Date PIC 9(8).
   03 c-Current-User PIC 9(4) COMP.
01 a-ACCEPTS.
   03 a-Date.
      05 a-Year	 PIC 9(4).
      05 a-Month PIC 9(2).
      05 a-Day   PIC 9(2).
   03 a-User   PIC 9(4) COMP.

> 8) LEVEL 66 AND 77 OBSOLETE.

I never had to use 66's and 77's. Just 88's
> 
> Regards
…[3 more quoted lines elided]…
> COBOL lives...
YEAH
```

#### ↳ Re: Your Comments...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37078649.576315143@news1.ibm.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
On Sun, 4 Apr 1999 20:40:12 +1000, "Westley Lodge Pty Ltd"
<wlodge@hotkey.net.au> wrote:


>1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
>THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.
>

Based on observations of OO systems that HAVE met their doom, I can
tell you that it's the PLANNING and the implementation of OO that is
the problem, not the platform.  

Melding an OO system into a non OO system is a big mistake - IMHO -
and virtually impossible.  So, for brand NEW development OO might be
the way to go - given a large enough project that can take advantage
of the benefits of OO.   

There will be initial prejudice against it, just like the changes in
the 1985 standard that were/are slow to be accepted.  Given the
difficulty many companies claim in finding experienced COBOL
programmers, it will be even harder to find skilled OO COBOL
programmers.  This too will lead to the lack of use of OO COBOL.

Presently, I am VERY reluctant to make use of OO COBOL -- the
different vendors all implement the proposed standard (under flux)
differently - if at all - and it's something I only want to learn
ONCE, not learn and re-learn and re-learn.  

The root question, is it NEEDED?  It will make interface to divergent
systems (COBRA - which in theory I really do like) easier.  It will
give COBOL programmers the advantages of the OO programming style.  

Disclaimer:  I'm NOT a big OO fan.  For small projects, the design
overhead is significant - if you want it to work.  I'm on the fence as
to it's economy.  Cost of development is what will make or break it.
If it's cheaper it'll thrive, if not it will die.  Even if the OO
portion of the COBOL standard is not accepted, COBOL will continue.

One last comment on the issue - COBOL has a great opportunity to get
OO right.  I've seen many OO projects DIE - and I'm not sure if it was
because they were OO, because they were in C++ (A language not best
suited for business development).  However, I do know, first hand,
that even those programming with OO, on many occasion, struggled with
the implenentation of the Theory, and often had trouble explaining
what they though they understood about OO.  These were very
intelligent people, not designing or coding their first OO system.
This scares me. 


>2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
>STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
…[3 more quoted lines elided]…
>

This is just patently false.  I can give you example after example of
Code that is hard to read and understand - even when the rules are
clearly stated, that is CLEAR and EASY to understand once the Evaluate
is introduced to the code.  Check out the example in my book, Chapter
9, pp147-153 - Sams Teach Yourself COBOL in 24 Hours.  This should
help make it clear.  

>3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
>PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
>PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?
>

No, you are right - generally.  I was in exactly your position at my
last shop.  Imagine my pleasure upon changing positions and finding
code I am to maintain that already uses these, and is much easier to
maintain.  

I find the style faster, but when I first started using it I went
overboard.  I had code with pages and pages of statements between
Perform and End-Perform, with lots of nested performs and nested IF's.
This is better coded by breaking out the large blocks of code into
paragraphs and performing them inside the in-line logic.  

When you make use of this style, the different optimizers can do a
better job and lead to faster executing programs.  

This one is almost political.  Violating even the informal standards
of a shop can lead to hate and discontent.  You need to educate, and
not force this on them.

>4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
>COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
>STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
>REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?
>

I think this is two questions in one.  

4A - it's mostly ignorance.  The don't know it's there.  Get a copy of
Don Nelsons "Cobol 85 for Programmers" and keep it on your desk.
Refer to it often, and let others borrow it.  It'll make a difference.
There is nothing wrong with using NOT INVALID and INVALID - but I have
seen some differences in what the different COBOL vendors allow you to
use within these.  Some will let you get away with more reads with
invalid/not invalid - nesting these imperitives, while others will
not.  From the way I read the standard, nesting them is not allowed. 

I tend to use them and PERFORM other things within them.

4B - I think you are asking about report writer.  On a mainframe (when
it's avaialble)  it's a fine thing.  On most PC and UNIX
implementations, it's OK.  Under Windows, if you want to use native
Windows printing, or any third party printing tools, it's next to
useless. 

>5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
>THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
>INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?
>

I think you mean Performing not calling.  Sections were designed to
allow memory segmentation - something not necessary today.  If writing
a new program I do not use sections.  If modifying a new one, if it
has ANY sections in the procedure division, I use a section for any
new paragraphs.  This makes sure that if a section is perfromed,  the
program will not fall through my new paragraph by accident. I also add
them at the END of the program, for this same reason - I don't want to
break a fall through that presently exists.  

Today, with a modern compiler, there is no reason to use a Section in
the procedure division.

>6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
>GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
>WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)
>

This too is a political issue.  I used to HATE it when I saw items in
a program that had to be qualified.  I've since come around.  However,
if you are a slow typist, and you want to modify only a single item,
having to qualify it can make you angry.  I tend to use this only for
control break programs, making the code much cleaner and easier to
maintain.  I never introduce it into an existing program that does not
use it.

>7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
>ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
>SITES I WORKED AT. SMALL PROGRAM BUT...).
>

Depends on the machine.  One thing it will prevent is erroneous
redefines.  Secondly, I have seen CICS programs that used this to save
off all of WS into Temp Storage or the communications area. There can
be advantages in storage use also.  I tend to group like used items so
that I can use Initialize against the group.

>8) LEVEL 66 AND 77 OBSOLETE.

77 -- On SOME platforms there's no advantage.

66 - I have found it quite useful in Y2K remediation - using more of
it in the last year than I have in the last 16.  I would not call it
obsolete.  But I would not use it frivolously.

>
>
…[4 more quoted lines elided]…
>COBOL lives...

With Gusto!
```

#### ↳ Re: Your Comments...

- **From:** Jeffrey Friedman <jfriedm@ibm.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37079A0D.D4265100@ibm.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
See my responses below:

Westley Lodge Pty Ltd wrote:

> OK,
>
…[22 more quoted lines elided]…
> THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

No - if you don't like them, don't use them.  But lots of folks will eventually
jump on the OO bandwagon - and the COBOL committee has gone out of its way to
make sure it is obvious whenever OO language elements are being used.

> 2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
> STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
> NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
> BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
> MAINFRAME COBOL2 COMPILER.

It is probably never faster than IF's - but in a simple form EVALUATE is a much
nicer form of case statement than pages of nested IF statements.It is designed
around design table processing so allows for the more complex formats. And that
is probably why in general it does not general as efficient code as IF as it is
a much more complex statement to optimize (in general).  But for those folks who
use decision tables, the facility is there.  For the rest of us, in its simplest
form, COBOL finally got a case statement!

>
> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
> PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

All of the ANSI85 structured facilities are great - but I do have to admit that
inline performs are probably the most useful.  I use them all the time.  I would
guess that in general you are probably correct:  since the code is generated
locally to the test/branch there is probably no page faults involved with its
execution - whereas old "remote" performs typically page-fault to get to the
performed routine, then page-fault when it comes back to test the condition,
etc..  If the code being executed is anything more than trivial though, I tend
to prefer the remote perform for maintainability of the program - once code
becomes nested more than 2 or 3 levels deep I find it harder to maintain.  Also,
if a given piece of code's function  can be given a name (i.e. if it
"compress-account-number") then I prefer making a paragraph so named and using
it - often it can be used from more than one place.

>
> 4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
> COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
> STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
> REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

Nope - nothing wrong with these at all.  I use them all the time.

> 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
> INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

Everyone has a different opinion here.  My opinion is that either is ok, only
that you be consistent.  If you PERFORM section-name then always PERFORM
section-name; if you PERFORM A THRU A-EXIT then always use that structure.  When
a program has a mix of different PERFORM types, it is harder to determine where
a given routine ends.

>
> 6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
> GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
> WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

Yes, but.  Almost nobody understand the CORR rules well enough to maintain code
which uses ADD, SUBTRACT, or MOVE CORRESPONDING.  It often does not do what
people expect.  It is usually more important for maintainability to avoid it.
But again, I have spoken with folks who a big into data-driven design and
CORRESPONDING is one of their favorite features.  I usually avoid it myself
though - even for trivial YY/MM/DD moves, it is easy enough to replicate the 3
MOVE statements using most editors today.

>
> 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
> ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
> SITES I WORKED AT. SMALL PROGRAM BUT...).

Implementation-specific question.  Probably not a good thing though as most
implementations have limits on 01-sizes whereas the entire Working-Storage
Section can be much larger.  Also, on machines with segmented addressing
structures (such as the 80x86 not in 32bit addressing), dealing with
multi-segmented data structures often leads to much less efficient generated
code.  You usually cannot go crazy with 01's either though - as many
implementation have a limit on the number of 01-level data items.  Grouping data
as appropriate may result in more efficient code - so putting data which is used
together in the same 01 is often a good idea.

> 8) LEVEL 66 AND 77 OBSOLETE.

I agree there is little need for 77's anymore.  And anything you can do with a
66 you can do with REDEFINES.  Not worth the incompatibilities to obsolete them
in the Standard, but they could probably be declared archaic. Espcially with the
new SAME AS proposed feature to make fields which are the same as some other
field.

>
> Regards
…[3 more quoted lines elided]…
> COBOL lives...

Just some of my opinions.

Jeff Friedman
```

##### ↳ ↳ Re: Your Comments...

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3708CAF6.DE85940A@NOSPAMhome.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <37079A0D.D4265100@ibm.net>`

```
> > 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> > THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
…[6 more quoted lines elided]…
> a given routine ends.

As soon as COBOL has the ability to exit paragraphs, the contingent in
favor of either of the above will go away.  It can't come soon enough.

My opinion is that NEITHER are ok.  I'd like to see a switch which
disallowed all dropping through to paragraphs.
```

###### ↳ ↳ ↳ Re: Your Comments...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3709625a.698206179@news1.ibm.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <37079A0D.D4265100@ibm.net> <3708CAF6.DE85940A@NOSPAMhome.com>`

```
On Mon, 05 Apr 1999 08:38:46 -0600, Howard Brazee
<brazee@NOSPAMhome.com> wrote:

>My opinion is that NEITHER are ok.  I'd like to see a switch which
>disallowed all dropping through to paragraphs.

I'd like to at least see them flagged so the code can be fixed.  In
the shop I was in prior to this one, programs were broken on a regular
basis by inserting paragraphs betwen paragraphs that were subject to
the HEINOUS fall through logic.
```

###### ↳ ↳ ↳ Re: Your Comments...

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ecu37$8ip$1@news.igs.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <37079A0D.D4265100@ibm.net> <3708CAF6.DE85940A@NOSPAMhome.com> <3709625a.698206179@news1.ibm.net>`

```
Maybe instead of ending every paragraph with
PARAGRAPH-EXIT.
       EXIT.
the spec should change to ending every paragraph with
PARAGRAPH-EXIT.
       DISPLAY "ERROR".
       GOBACK.
I certainly write code as if that were the case.

Thane Hubbell wrote in message <3709625a.698206179@news1.ibm.net>...
>On Mon, 05 Apr 1999 08:38:46 -0600, Howard Brazee
><brazee@NOSPAMhome.com> wrote:
…[7 more quoted lines elided]…
>the HEINOUS fall through logic.
```

###### ↳ ↳ ↳ Re: Parser

_(reply depth: 5)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7een6f$rku$2@bgtnsc01.worldnet.att.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <37079A0D.D4265100@ibm.net> <3708CAF6.DE85940A@NOSPAMhome.com> <3709625a.698206179@news1.ibm.net> <7ecu37$8ip$1@news.igs.net>`

```
Hi,

As the result of figuring out how to run the parser program and making the
necessary changes,  these items were identified.

1.  If the input file contains option specs before the ID, the "@" symbol is
not handled. This means you have two copies of the source, or logic to
handle this line like a comment is needed.

2. The tables are not large enough to process the parser program.

3. The displays in the program scream by on the screen so that they are of
no use.
Writing them to a file would be more useful perhaps.

There is no To in this message because several of you are doing something
with this
and I wanted to share my experience with you before doing anything esle.

Warren Simmons
```

#### ↳ Re: Your Comments...

- **From:** "Steve King" <steve.king8@virgin.net>
- **Date:** 1999-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e8f55$gu7$1@nclient5-gui.server.virgin.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
>1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
>THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

My company will be implementing IBM's latest OS390 COBOL compiler later this
year and this has OO features - I certainly plan to take advantage of them
(we already use Java).

>2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
>STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
>NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
>BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
>MAINFRAME COBOL2 COMPILER.

IBM's COBOL2 compiler generates almost identical code for Evaluate and If
statements, so the issue is more about maintainability, not performance. I'd
use Evaluate every time, as it generally makes it much easier to add new
conditions and remove old ones. If you use the IBM COBOL2 compiler then set
the LIST option when you compile your programs; you can then compare the
COBOL code line-by-line with the generated Assembler code.

>3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
>PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
>PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

In-line Performs are more efficient with COBOL2, but you will find that most
optimizing compilers can generate in-line code for performed sections or
paragraphs, thus making the in-line Perform a little redundant. However, I
find code with in-line Performs much easier to read and maintain.

>4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
>COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
>STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
>REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

I agree. Most COBOL programmers seem to stick with the smallest subset of
the language that will enable them to do their job, and there is a marked
reluctance to learn anything new. I must admit that I soon get bored with
coding programs in the same way, so I am continually looking out for new
ways of doing things (this doesn't endear me to the standards people,
though!).

>5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
>THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
>INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND
WHY?

I've noticed that performing paragraphs seems to be a common practice in the
US (I'm from the UK) - but is this really the case? I have only worked at
sites where sections are performed and paragraphs are used as labels within
sections for GOTOs (heresy!) or EXITs.

However, my personal preference is to use nested sub-programs instead of
sections or paragraphs as this gives you additional flexibility, although
the coding is a little more involved. Benefits include easy conversion to
separately-compiled modules and the ability to manage working-storage more
effectively (each program can have its own working-storage and communication
between modules can be accomplished exclusively via parameters, instead of
global working-storage - just like "real" block-structured languages).

As to the efficiency concerns, this depends very much on how good your
compiler is at optimizing code - I don't see why nested programs should
necessarily be any less efficient than performed sections or paragraphs; in
fact, the IBM COBOL2 compiler can choose to generate in-line code for all
three types of subroutine invocation.

>6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
>GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
>WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

I don't like Move Corresponding simply because I have to refer back to the
record layouts to see what it's actually doing! Another disadvantage is that
you also need to be aware of the little quirks that are designed to trip up
unwary programmers (Initialize is good for this too!). Code efficiency
should be the same as for "hand-coded" Moves.

>7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED
AS
>ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
>SITES I WORKED AT. SMALL PROGRAM BUT...).

Some optimizing compilers move the 77 and 01 items around in storage, so you
may find dump analysis a little frustrating sometimes! Having just one 01
record would obviously solve the problem, but probably at the expense of
maintainability.

>8) LEVEL 66 AND 77 OBSOLETE.

I've never felt the need to use 66 levels, but 77 levels can be useful on
certain platforms. There doesn't appear to be any benefit to be gained from
77 levels on IBM MVS systems, but I did use 77 levels effectively on
Burroughs (now Unisys) A-series mainframes; the Burroughs MCP operating
system is stack-based and 77 level items (less than or equal to one 48-bit
word) were placed directly in the stack, thus enjoying much faster access
(they could also be interrogated directly while the program was running, via
the OT command - I'd love to be able to do this on our IBM systems!). It was
also possible to set up stack arrays with 01 COMP-1 items - Burroughs really
knew how to build good operating systems, but they weren't so good at
selling them!

MCP was written using an ALGOL-like language and most of the system software
was written in ALGOL too. That's also something I miss from my Burroughs
days - the ability to write powerful programs in ALGOL or decent job control
with WFL (an ALGOL-based job control language). Now I have to resort to IBM
Assembler or Clist/Rexx procedures to do anything useful. No contest!

That's enough reminiscing (the good old days are always the best.......)

Steve
```

#### ↳ Re: Your Comments...

- **From:** Warren Porter <warrenp21@ASPMnetdoor.com>
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3708DABF.8F177E05@ASPMnetdoor.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
> 1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
> THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

No way.  OO extensions simply wouldn't be used except in a few installations.

> 2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
> STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
> NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
> BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
> MAINFRAME COBOL2 COMPILER.

It makes more sense than a series of IF-ELSE-IF-ELSE-IF-ELSE etc, stairstepping
down.  Before the EVALUATE statement, COBOL did not have a convenient way to
implement a case test.

> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
> PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

If the code is used only in one place, go ahead.  It's easier to maintain when
there is no need to locate the performed code elsewhere in the program.

> 4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
> COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
> STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
> REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

If one uses inline performs or the one-period-per-paragraph style, these may be
mandatory.  BTW, please define "fantastic".  If someone wants to add a record to
an indexed file and reads that hopefully nonexistant record, NOT INVALID is
indeed the error to check for.

> 8) LEVEL 66 AND 77 OBSOLETE.

I use 66 as an "after the fact" redefinition when testing, allowing me to check
out certain areas in a record normally not in a group.  I don't use it in
production though.
```

#### ↳ Re: Your Comments...

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7earov$ide@sjx-ixn6.ix.netcom.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
Some general comments - not in direct response to the question - but to what
I think are the underlying "thoughts". (This is semi-long - sorry if that is
a problem to some readers)

1) "Efficiency" is - by definition - compiler dependent.  I don't think that
there is any "general structure" that is ALWAYS more efficient in every
variation on every platform.  On the other hand, the more "generalized" a
language structure is - the more likely it is to be LESS efficient in any
specific code example than doing that logic via more "basic" constructs.
For example, STRING, UNSTRING, INSPECT, etc - are probably ALWAYS less
efficient that coding your own character by character loop - that can be
optimized to EXACTLY what you are looking for in this case.  ON THE OTHER
HAND, getting to know and use the more general verbs will PROBABLY (but not
always) provide you with a general feature that can be used to quickly code
a correct (less error prone) and maintainable piece of code.  (see next
comment)

2) "Efficiency" versus "maintainability".  There is NO feature of COBOL that
is so self-documenting that it is "easy to maintain" by people who don't
understand and use that feature.  On the other hand, if your shop (or
specific programmers) do KNOW and understand a "complex" feature, then the
more powerful the feature, the better it is for "self documenting" and easy
to maintain functionality.  This is true for everything from INSPECT to MOVE
CORR to Report-Writer - to nested programs.

3) "Efficiency" - do you really need it?  In a recent discussion on the
INITIALIZE verb's efficiency, I mentioned the distinction between something
in a "tight loop" versus something performed infrequently.  When you are
comparing using the most efficient (run-time) construct versus a "more
generalized" powerful structure,  do think about how often that code will be
performed? There are two times that I think that run-time efficiency should
be considered:
 - in a tight logic loop (something that is performed many MANY times in a
single execution of a program)
 - something that occurs in a "short" sub-second online program. (for
example, in an INITIALIZE in a subprogram that is used to "refresh" a screen
frequently in an online environment)

If your code construct is used 1 to 10 times in a multi-hour batch program,
then I don't think that saving a few machine instructions is at all useful -
when compared to using a really "self documenting" and less error-prone
general purpose language feature.  ON THE OTHER HAND, there is no reason to
get used to using a "really inefficient" construct when an equally clear
code segment can be written which is more efficient.

4) Extensions, advanced features, platform specific stuff etc.
 ABSOLUTELY, vendors should provide features (extensions) that are optimized
for their environment or which provide interfaces to system-specific
facilities.  (For example, having "line sequential" in the PC/Unix
environment is critical - while allowing it on MVS or OS/390 would be
silly.)  Programmers writing code targeted at a specific environment should
use such features whenever appropriate.  Separating them into COPYBOOKs or
CALLed subprograms is useful - if you think your code may EVER be ported to
a different environment, but - for example - writing a CICS program where
you put all your EXEC CICS statements in called subprograms would be silly
(On the other hand, separating "business logic" from "screen interaction"
might be useful.).

 I know of (at least) 4 types of extensions that vendors support:
   A) upward compatibility extensions (for example support for COMP-3 when
Packed-Decimal would do the same thing).  It is also true that in Micro
Focus - you can use the TRANSFORM verb in the middle of a nested program.
  B) from the "next Standard" (or another Standard) - examples are EXIT
PARAGRAPH/SECTION which has been talked about a bunch in this NG.  Another
example is COMP-5 which was in the X/Open Standard or DBCS which was in the
MIA Standard.
  C)  Here's a "good idea" that our customers like  or wanted - so let's
just add it.  (Micro Focus has bunches of this now - and IBM used to do it
more than anyone else).  I can think of the CHAIN verb,  GOBACK (in the
past - now it is in category "B"), and bunches of others.
 D) Interfaces with specific operating system resources (for example EXEC
CICS, EXEC SQL or COLLATING SEQUENCE EBCDIC)

It is "great" when a programmer can avoid ALL of these extensions and only
create "fully portable" code.  On the other hand, I encourage the use of
type "B" (with the warning that things MAY change before the Standard ever
gets approved).  Type "C" is often not just useful, but so thoroughly "in
grained" in programmers environments that their continued use is a "de
facto" standard - on the other hand, I have seen extensions used here that
really are NOT needed and just reflect programmers without adequate
training.  Type D is clearly critical for some applications.  Type A should
be "killed off" when possible - but you do need to think about how long you
will still be maintaining "legacy" code that still uses the old technique.

5) For SECTIONS versus PARAGRAPHS, please see DejaNews.  (I will confirm
what one other poster says - PARAGRAPHS are almost all that is used in the
US - while SECTIONS are incredibly popular in the UK.  There are exceptions,
but this does seem to be a "national" as well as "religious" debate.)

6) In general, COBOL programmers (particularly in large mainframe shops)
just do NOT get adequate training on new features.  As stated earlier, no
feature is so self-documenting that it is "easy" to use without learning how
and when to use it.  On the other hand, most COBOL programmers just are not
given the tools much less the training to learn to exploit all the
facilities that are now available to them.
```

##### ↳ ↳ Re: Your Comments...

- **From:** tim.oxler@NOSPAMteo-computer.com (Tim Oxler)
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370cc4af.9252206@news.teo-computer.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <7earov$ide@sjx-ixn6.ix.netcom.com>`

```
On Mon, 5 Apr 1999 12:25:11 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Some general comments - not in direct response to the question - but to what
>I think are the underlying "thoughts". (This is semi-long - sorry if that is
>a problem to some readers)
>

>6) In general, COBOL programmers (particularly in large mainframe shops)
>just do NOT get adequate training on new features.  As stated earlier, no
…[4 more quoted lines elided]…
>

Agreed.  But I have to say, not just mainframe.  One of the worst
written COBOL app that I'd ever seen was on PC.  It looked just like
20yr old COBOL '74 code.  And maybe that hi-lights the training
problem.

Most (or at least many) COBOL programmers seem to learn a particular
style and stick with it for years, regardless of the changes that come
along.  The attitude seems to be "If it works, don' fixit".

Shops do very little to change this.  When training is offered, it's
offered mainly to entry level or those who don't know it at all.

After seeing so much PERFORM-less, goto branching, goto looping I
lobbied hard for COBOL training for the veterans at a particular shop.
The reply was always the same, "They already know COBOL".



Tim Oxler
Teo Computer
http://www.teo-computer.com
Take the Y2k Quiz
http://www.teo-computer.com/dev/quiz.html
```

#### ↳ Re: Your Comments...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e9kkt$70b$1@news.igs.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
Westley Lodge Pty Ltd wrote in message ...
>
>1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
>THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.


I think we have to wait and see how usefull they become.  I cannot see how
they can do any harm, any more than the "commuication section" did.  If
nobody buys them, in another thirty years they will be dropped.
>
>2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
…[3 more quoted lines elided]…
>MAINFRAME COBOL2 COMPILER.


Irelevant.  Code it so that you like the way it reads, and let the compiler
worry about that stuff. You could change speed of your program far more by
spending $25 more on your video card. In the day of the GUI, the logic of
your code counts for about 1/10000 of the execution time.  The difference
should be immeasurable.

>3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
>PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
>PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?
>
Ditto to the above.  Make it easy to read, first and formost. Adhere to the
shop standard if it has one, and adopt the one you like best if it does not.
Personally, I like to keep routine sizes down, and tend not to use in line
performs unless it is a couple of very tight loops.  I see absolutely no
reason on earth to "choose" one way or another.  Use both or either.

>4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
>COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
>STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
>REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?


I try out most new things.  If I like it, then I start using it.  If I do
not, then I do not.  I have no idea if other people are so resistant or not.
>
>5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
>THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
>INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND
WHY?


The idea of sections is out of date by years.  It may work well on some
obscure platform or under weird conditions, but it is not the norm, and
serves no usefull purpose.  (IMNSHO)
>
>6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
>GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
>WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

>
Yes(?)
>
>7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED
AS
>ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
>SITES I WORKED AT. SMALL PROGRAM BUT...).
>
About the only one I can think of is that you could then get the length ...

>8) LEVEL 66 AND 77 OBSOLETE.
>

I use 77, but it is habit.  There are a few machines than may run faster
with 77's coded correctly.
```

#### ↳ Re: Your Comments...

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#6SGpvKg#GA.122@nih2naaf.prod2.compuserve.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
See below.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Westley Lodge Pty Ltd wrote in message ...

>1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
>THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

===> I'd like to be on a project where they're used appropriately, however
you do that in Cobol.

>
>2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
>STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE
OR
>NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
>BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT
IBM'S
>MAINFRAME COBOL2 COMPILER.
>
>3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
>PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
>PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

===> I don't give a rat's @$$ about obsessing with efficiency
considerations - sure, don't write obviously very inefficient code, but
concentrate on writing good readable code. Both of the above are very
helpful with this. Keeping each paragraph within a page on the listing
makes for good readability, and both of these above techniques can help
with this, and can also be overused and overflow the page.

>
>4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
>COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
>STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
>REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

===> I'm so glad the not at end and not invalid key phrases were added, now
you don't even have to set a flag any more if all you wanted to do could be
put under the not at end clause.

>
>5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS'
IN
>THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
>INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND
WHY?

===> Sections are useful as a transatory tool when cleaning up a program,
to help get rid of the Perform Thru's. A dummy section at the end helps
protect isolated paragraphs, e.g. ABC Section, End-Of-ABC Section. Put
newly written/moved paragraphs in Single-Paragraph-Routines Section. When
the whole program is cleaned up, no Exits, no GoTo's, no Perform Thru's,
then you can get rid of all the sections.

>
>6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
>GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
>WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

===> Depends on the situation.

>
>7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED
AS
>ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
>SITES I WORKED AT. SMALL PROGRAM BUT...).

===> Illogical, inefficient, confusing, and unnecessary.
>
>8) LEVEL 66 AND 77 OBSOLETE.

===> 66 is handy especially after COPYing a copybook you don't dare change,
but watch out for changes.
```

#### ↳ Re: Your Comments...

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3709E3BA.A9370A38@zip.com.au>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
In most cases I support basically what Thane has said.

> 1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY.
> THEY WILL COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

The way of the future!  (door opens and light shines)

Has anyone considered that 88 levels were the original OO you could bind
data values to a variable.

Once it is done well though there are major benefits.  Like most
programming it is actually difficult to do well.

This will not take off for Cobol until something like Rational generates
the basic structures of OO directly from the design. I would not
consider doing an OO design any other way.

> 2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
> STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
> NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
> BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
> MAINFRAME COBOL2 COMPILER.

I had some stewing on this.  There would not be any difference or
evaluate would be faster (computed goto under compiler optimization).
but...

There might be a tendency for a programmer to repeat the same condition
so that a set of if's

if a
   if b
   end-if
   if c
   end-if
else
   if b
   end-if
   if c
   end-if

becomes:

evaluate true
 when a & b
 when a & c
 when b
 when c
end-evaluate

In the evaluate the A variable would be evaluated twice but the if
statement would do it once.
 
> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
> PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

More efficient 'probably'.  It is very unlikely to be less efficient.

Is it clearer.  If not used to much then YES.
 
> 4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
> COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
> STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
> REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

The bottom line is that most programmers just program.  I would estimate
that there are 3 of 50 programmers at work that read the news group. 
Most are busy producing and don't have time to study.

Write a refresher course giving the new Cobol stuff and present to your
peers.  Get the boss to provide Pizza, at least you wont be alone.

I would consider that I know probably 50% of the cobol language.  I have
been successfully coding for 16 years with this subset.  I use string
and unstring so rarely I always RTFM when I code them.

> 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
> INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

Religious debate, I wont go here today.  I use paragraphs only.
 
> 6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
> GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
> WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

Move corresponding where it helps the code.  It is harder to find
modifications using a find though and can trip you up.  Better cross
reference by the compiler listing (when a group is modified then all
subordinate variables are implicitly modified) would be a boon here.

( I am and MVS programmer, do PC tools help here? )
 
> 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
> ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
> SITES I WORKED AT. SMALL PROGRAM BUT...).

Prefer to group logically.  If they are moved as a group (TSQ's etc.)
then don't break them up, otherwise the clarity of grouping is
important.
 
> 8) LEVEL 66 AND 77 OBSOLETE.

Never used them, would have to read the manual to find out what they do.
```

#### ↳ Re: Your Comments...

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<923400970.962001@woody.hotkey.net.au>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
OK,

Being the one that originated the topic, I think it's a good idea to respond
back with some of my observasions from the responses I received. I stress
that these are my observations, but I will try and be as objective as I can.
Please don't "letter-bash" me if I am wrong. I think that it is both
courteous and the right thing to respond to the topic I started.

As I explained, I originated these questions when, to my surprise, COBOL
developers I had a discussion with, did not agree with certain features of
'our' language COBOL, and the way it was heading.

1) OO COBOL EXTENTIONS TO THE COBOL STANDARD ARE NOT NECESSARY. THEY WILL
COMPLICATE THE LANGUAGE AND RESULT IN ITS DOOM.

From the responses I received, both at the group, and the ones addressed to
me (god... so many), it is obvious that a majority of us don't mind these
changes. I also suspect, from the responses I received, a great many COBOL
developers will aproach the OO extentions with  a "wait and see" approach.
Not because they mind it, but because they are professionals and they want
to only invest their time, effort and money, where it's most logical
(profitable) at the moment.  A few also claimed to have tried it out, and
gave it up because of its added complexity.

Myself I believe the best response was given by Thane Hubbell who suggested
that
'Based on observations of OO systems that HAVE met their doom, I can
tell you that it's the PLANNING and the implementation of OO that is
the problem, not the platform"

2) IS THE 'EVALUATE' STATEMENT MORE EFFICIENT (FASTER) THAN THE 'IF'
STATEMENT, IN THE WAY IT GETS EXECUTED (NOT WHETHER IT IS EASIER TO CODE OR
NOT)? SOME PEOPLE THINK, IT COMPLICATES  CODING, AND IT PROVIDES NO
BENEFITS. IF THE ANSWER DEPENDS ON THE INDIVIDUAL COMPILER, HOW ABOUT IBM'S
MAINFRAME COBOL2 COMPILER.

As far as the EVALUATE statement being more efficient than the 'IF'
statement, I believe the general consensus is that it sure makes programs
more readable, but there is no gain, as most COBOL compilers now days
optimise both EVALUATE and IF statement to look / perform the same.


3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
PROGRAMMING AND FASTER EXECUTION CODE. AM I WRONG?

I was very surprised as to the number of people that 'embraced' / are using
the inline PERFORM. Also it was generally agreed that these should be kept
short. Main reasons developers specified they use it for are
        a) one does not have to hunt around for the performed
paragraph/section to see "...what is moved what/where", especially in table
handling
        b) string handling
        c) In cases where the number of iterations is deemed to be too many.
This last point again, many also suggested that it comes down to how good
the optimizer is

4) THERE SEEMS TO BE A TENDENCY OF NOT USING SOME FANTASTIC COBOL 85
COMMANDS AND OPTIONS. FOR EXAMPLE THE 'NOT INVALID' OPTION OF THE FILE I-O
STATEMENTS. IS THERE ANYTHING WRONG WITH USING THESE? WHAT ABOUT A SIMPLE
REPORT PROGRAM(WHY USE EAZYTRIEVE?) IN A 'READ, END-READ' LOOP?

While many people use a lot of the COBOL 85 syntax, only two have used the
'NOT INVALID' option.  'READ... END-READ" loops did not score much mention
either


5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS>
INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?

Big response to this. It highlighted that a lot of COBOL shops have their
own standards and they stick to it. Some agree that it is better to use
SECTIONS because it is faster than performing paragraphs, one after the
other. Others went the other way, and coded in paragraphs to avoid having to
use 'GOTO Exit' statements. A couple have even coded in SECTIONS that don't
have any GOTO statements (Does this qaulify this as a paragraph?)


6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)

Not a developer favorite. almost 100% agree that this statement adds to the
complexity of the program, since you end up with more than one sets of
variables with the same name which then must be qualified


 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED
AS ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF
THE SITES I WORKED AT. SMALL PROGRAM BUT...).

Nobody responded to have done this. All agree that it's best to break up the
Working Storage into logical group.

8) LEVEL 66 AND 77 OBSOLETE.
Again not a developer favorite, with only a handful ever using it.


Regards

Theo

COBOL lives...
```

#### ↳ Re: Your Comments...

- **From:** sven_schneider@my-dejanews.com
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7eg5lk$eap$1@nnrp1.dejanews.com>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net>`

```
In article <PjHN2.37$EW1.867@vic.nntp.telstra.net>,
  "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au> wrote:
> OK,

<snip>

>
>
…[8 more quoted lines elided]…
>

the 'evaluate' statement makes code easier to read. the best advantage of this
statement is the 'when other' condition. using this, you can avoid crashing
programs caused by "senseless" conditions.
the difference of execution time from the 'if' and the 'evaluate' statements
depends first on the compiler and second on the speed of the machine you are
using. both is uninteresting today.


> 3) WHERE I CURRENTLY CONSULT, IT SEEMS I AM THE ONLY ONE USING 'INLINE
> PERFORMS'. AS FAR AS I AM CONCERNED, THEY RESULT IN BOTH MORE EFFICIENT
…[6 more quoted lines elided]…
>
 there is nothing wrong with using the new commands described by cobol 85. I'm
using them everywhere. It's easier for me to code with the new features.


> 5) THERE IS A PLACE FOR 'SECTIONS' AND THERE IS A PLACE FOR 'PARAGRAPHS' IN
> THE LANGUAGE. CALLING A SECTION IS MUCH FASTER THAN CALLING PARAGRAPHS
> INDIVIDUALLY. SHOULD ONE CODE IN SECTIONS OR PARAGRAPHS EXCLUSIVELY AND WHY?
>

we are using sections. paragraphs are only markers for the end of a section
followed by a 'exit.' statement.

> 6) 'MOVE CORRESPONDING' DOESN'T RESULT IN FASTER EXECUTABLE CODE, THAN A
> GROUP OF INDIVIDUAL 'MOVE' STATEMENTS, BUT RATHER IT FACILITATES AN EASIER
> WAY OF CODING (AGAIN BASED ON IBM'S COBOL2 COMPILER)
>

using 'move corr' is a good way to avoid tons of 'move' statements. we work
on DB2-tables with more than 30 columns. it's easier to transport the datas
with one statement instead using a extra section with 30 ore more  'move'
statements. The only problem is to follow the data-flow in detail. in that
case you must always take a look to the working storage. 'loosing' of data
could also happen caused by different names for the same thing. a other pity
is that you must use a full qualify of the data if you want to use them
alone.


> 7) ARE THERE ANY BENEFITS IN HAVING A WHOLE WORKING-STORAGE SECTION CODED AS
> ONE 'SINGLE' "01" LEVEL (BELIEVE ME. I'VE ACTUALLY SEEN THIS IN ONE OF THE
> SITES I WORKED AT. SMALL PROGRAM BUT...).
>

it is useful if you are working on cics and you must debug a program.

> 8) LEVEL 66 AND 77 OBSOLETE.

i never used this levels. could be sometimes.

>
> Regards
…[5 more quoted lines elided]…
>

----------------------------------------------------------------------

i hope that all is understood. in a foreign language discussing problems are
more difficult than the problems themselves.

Sven Schneider
Germany
BEKO Informatik GmbH

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Your Comments...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7egg1c$og5$1@news.igs.net>`
- **References:** `<PjHN2.37$EW1.867@vic.nntp.telstra.net> <7eg5lk$eap$1@nnrp1.dejanews.com>`

```
sven_schneider@my-dejanews.com wrote in

>i hope that all is understood. in a foreign language discussing problems
are
>more difficult than the problems themselves.


After 30 years of Cobol, it is not a problem ...
;<)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
