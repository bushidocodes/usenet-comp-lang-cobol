[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sections

_76 messages · 25 participants · 2002-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Sections

- **From:** "Eddy Scheire" <fa099784@skynet.be>
- **Date:** 2002-03-16T10:59:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
Hi,

I'd like to know the difference between the next coding examples :

DO-SOMETHING section.
    IF condition
       statement
    ELSE
       statement
    END-IF
    PERFORM something
    MOVE something TO something
1000.
   EXIT.

and

DO-SOMETHING.
    IF condition
       statement
    ELSE
       statement
    END-IF
    PERFORM something
    MOVE something TO something
    .

I mean why should one use sections? To me it looks like unnecessary code.
```

#### ↳ Re: Sections

- **From:** none@none.com (freewheelin)
- **Date:** 2002-03-16T12:34:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c934702.42107902@news.earthlink.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
It depends on *how* you use them.   SECTION and PARAGRAPH are most
usefull with a nested structure. They provide a two tier control break
with the PERFORM statement.  The PERFORM SECTION has a higher level
control break than PERFORM PARAGRAPH, sort of like an implied PERFORM
THRU.   A SECTION can nest many PARAGRAPHs (with no SECTION labels)
and the SECTION is terminated by the beginning of the next SECTION
header or the physical end of the program.  Now then, consider PERFORM
THRU with SECTION labels and you create a third, higher level control
break.  Coding no SECTIONs or coding all paragraphs as SECTIONs hides
this feature and that is the usage you are questioning.  

On Sat, 16 Mar 2002 10:59:58 +0100, "Eddy Scheire"
<fa099784@skynet.be> wrote:

>Hi,
>
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sections

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-16T22:20:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CyPk8.15604$Ex5.1394378@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <3c934702.42107902@news.earthlink.net>`

```
An unintended conequence of the original purpose, but still viable.

Warren Simmons

freewheelin <none@none.com> wrote in message
news:3c934702.42107902@news.earthlink.net...
> It depends on *how* you use them.   SECTION and PARAGRAPH are most
> usefull with a nested structure. They provide a two tier control break
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

- **From:** none@none.com (freewheelin)
- **Date:** 2002-03-17T13:05:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c94af87.1522917@news.earthlink.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <3c934702.42107902@news.earthlink.net> <CyPk8.15604$Ex5.1394378@bgtnsc04-news.ops.worldnet.att.net>`

```

On Sat, 16 Mar 2002 22:20:18 GMT, "398199821"
<warren.simmons@worldnet.att.net> wrote:

>An unintended conequence of the original purpose, but still viable.

Thats what I thought too, a left over from segmentation, until I tried
an internal SORT.  Some compilers won't sort without it.

>Warren Simmons
>
…[48 more quoted lines elided]…
>
```

#### ↳ Re: Sections

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-16T14:39:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```

"Eddy Scheire" <fa099784@skynet.be> wrote in message
news:3c931758$0$29682$ba620e4c@news.skynet.be...
> Hi,
>
…[25 more quoted lines elided]…
> I mean why should one use sections? To me it looks like unnecessary code.

SECTIONS are an artifact, a fossil, a construct from a primative time.

Their major original function was to partition the code into overlayable
chunks to conserve memory. SECTIONS today permit no unique (or even useful)
purpose. Their presence does, however, tend to confuse or bewilder those who
have never encountered them - or those, like me, who haven't seen SECTIONS
in twenty years.

Check out LEVEL numbers for SECTIONS for more confusion:

   (PRINT-IT SECTION 73.).
```

##### ↳ ↳ Re: Sections

- **From:** tom heitbrink <gizmo@hot.a2000.nl>
- **Date:** 2002-03-16T16:31:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com>`

```
On Sat, 16 Mar 2002 14:39:26 GMT, "JerryMouse" <nospam@invalid.com>
wrote:

>
>"Eddy Scheire" <fa099784@skynet.be> wrote in message
…[31 more quoted lines elided]…
>
that's your opinion. 

>Their major original function was to partition the code into overlayable
>chunks to conserve memory. SECTIONS today permit no unique (or even useful)
…[3 more quoted lines elided]…
>
See them everyday, and think use of sections makes program structure
more visible.

>Check out LEVEL numbers for SECTIONS for more confusion:
>
>   (PRINT-IT SECTION 73.).
>
```

###### ↳ ↳ ↳ Re: Sections

- **From:** "Eddy Scheire" <fa099784@skynet.be>
- **Date:** 2002-03-16T20:31:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c939d52$0$260$ba620e4c@news.skynet.be>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com>`

```
Well, thanx to both of you for your opinion and just like you, Tom, I see
them every day but in association with GO TO-statements all over the
program. And as I try to write structured COBOL-programs I hate to see GO TO
in a program.

"tom heitbrink" <gizmo@hot.a2000.nl> schreef in bericht
news:f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com...
> On Sat, 16 Mar 2002 14:39:26 GMT, "JerryMouse" <nospam@invalid.com>
> wrote:
…[31 more quoted lines elided]…
> >> I mean why should one use sections? To me it looks like unnecessary
code.
> >
> >SECTIONS are an artifact, a fossil, a construct from a primative time.
…[4 more quoted lines elided]…
> >chunks to conserve memory. SECTIONS today permit no unique (or even
useful)
> >purpose. Their presence does, however, tend to confuse or bewilder those
who
> >have never encountered them - or those, like me, who haven't seen
SECTIONS
> >in twenty years.
> >
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** tom heitbrink <gizmo@hot.a2000.nl>
- **Date:** 2002-03-16T20:47:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vv779uc689j79mu0745nth6asojnt3gto5@4ax.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be>`

```
I also never use the Go To statement, but one advantage of the
sections is the simple statement EXIT SECTION.

Using sections doens't mean programmer can use GOTO en Perform ...
thru ...  

At our office we use sections because it allows the use of exit
section and it's easier to search for specific parts. Paragraphs
cannot be easily searched, while section. shows the start of every
section, just like Working storage section and file-section. 

It's something that's COBOL-own, and like I said earlier, doesn't let
the porgrmmer free to write junk. 
just like the point to exit an IF-statment. 

Both make programs very unclear to people who need to perform
maintenance on the program later. 

On Sat, 16 Mar 2002 20:31:35 +0100, "Eddy Scheire"
<fa099784@skynet.be> wrote:

>Well, thanx to both of you for your opinion and just like you, Tom, I see
>them every day but in association with GO TO-statements all over the
…[62 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-16T22:44:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203162244.71aa499e@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com>`

```
tom heitbrink <gizmo@hot.a2000.nl> wrote in message news:<vv779uc689j79mu0745nth6asojnt3gto5@4ax.com>...
> I also never use the Go To statement, but one advantage of the
> sections is the simple statement EXIT SECTION.
> 
> {snip}

EXIT SECTION and EXIT PARAGRAPH and EXIT PERFORM and EXIT PERFORM
CYCLE (all to become standard in the next Standard), are GO TO
statements dressed up fancy.  If you do not use GO TO, you should not
be using any of these heretical additions to the language.  J4 spent
years rewriting the syntax rules for these instructions, to make sure
that the flow of control would GO TO the right place, unambiguously.

Piece of crap.

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-17T01:02:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a71f1l$l7i$1@nntp9.atl.mindspring.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com>`

```
This is something upon which  I disagree with Stephen completely.

The problem with "GO TO's" is *not* that you do a "branch and don't return".
The problem is that when used in some cases, you can get "crossing"
branches - and that you can get UNINTENTIONAL branches.

Most (but certainly not all) theories of "structured programming" allow for
an "escape from currently performed procedure" as this does NOT violate any
"single entrance / single exit" philosophy - and has no inherent maintenance
problems.

It is true that if you have a "philosophical" (not practical, not
maintenance, not understanding) objection to an "escape to the exit of the
currently running procedure" facility, that you should NOT use the new EXIT
PARAGRAPH/PERFORM/SECTION facilities (when they are available).  However, if
you are opposed to "GO TO's" because of readability and maintainability
reasons, then they need not be any problem - and can actually help you get
rid of "PERFORM x THRU y" structures - which CAN be maintenance problems.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-18T08:16:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C95A247.226E2E18@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com> <a71f1l$l7i$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote:

> The problem with "GO TO's" is *not* that you do a "branch and don't return".
> The problem is that when used in some cases, you can get "crossing"
> branches - and that you can get UNINTENTIONAL branches.

Do you mean 'GO TO the wrong label' ? as in 'GO TO 1081-Exit' when in
'1801-dosomething SECTION' ?

Yes the EXIT SECTION would reduce that problem.

> Most (but certainly not all) theories of "structured programming" allow for
> an "escape from currently performed procedure" as this does NOT violate any
> "single entrance / single exit" philosophy - and has no inherent maintenance
> problems.

It has no maintenance problems as long as the maintainers know what to
examine and what clues to look for.  If they are used to code that has
GO TO nnnn-exit then they will check whether it happens in the code they
are trying to understand.


> It is true that if you have a "philosophical" (not practical, not
> maintenance, not understanding) objection to an "escape to the exit of the
…[3 more quoted lines elided]…
> reasons, then they need not be any problem - 

If it were possible to have all code completely rewritten replacing all
existing exit mechanisms  with 'EXIT type' then I might agree with you
(or a may not, depending on how I felt at the time).  However, it is
likely that these EXITs would be _in_addition_ to the existing
mechanisms and thus the usable sub-set is extended.  This does have a
significant _practical_ impact on understanding the code (or parts of
it) at a later time as now more different ways need to be checked for.

> and can actually help you get
> rid of "PERFORM x THRU y" structures - which CAN be maintenance problems.

PERFORM .. THRU  should be removed entirely using all means possible
(such as 'rm *').
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-18T07:59:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C959E4E.FDD74ED7@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com>`

```
Stephen J Spiro wrote:
> 
> EXIT SECTION and EXIT PARAGRAPH and EXIT PERFORM and EXIT PERFORM
> CYCLE (all to become standard in the next Standard), are GO TO
> statements dressed up fancy.  If you do not use GO TO, you should not
> be using any of these heretical additions to the language. 

There is actually nothing wrong with a GO TO statement.  It is perfectly
what its action is and, where the GO TO occurs, there is no confusion
over the logic flow.

Where the problem lies is at the label (or implied label) that is the
target of the GO TO.  At that point there is no indication of the actual
logic flow that may occur.

Taking a random label in a program then logic paths may drop through
from above (if this is a performed section or thru),  may end here (if
the previous paragraph is performed), or may start here (if this is
performed or gone to).

In programs that may use all possible Cobol constructs the only way to
resoleve the logic flow at any particular point (paragraph label) is to
examine the _whole_ program and track every flow.  If ALTER were allowed
then it would not be enough to track the flow statically, but it would
also be necessary to track it dynamically by passing through it with
sample data values.

In other languages the task of identifying logic flow is simplified by
having different types of labels for different operations.  One cannot
goto a label that is used to call (perform), you cannot use a label to
end the range of an operation.

It is usually impractical for a maintainer to understand a whole program
unless he wrote it, and it should be unnecessary to understand more than
the small part that needs adjusting.  The smaller the part required the
more efficient the maintenance.

Many structured Cobol mechanisms are designed specifically to reduce
what a label may be used for (though the rules are expressed in
different terms).  In doing so it then becomes a trivial task to
understand what happens at each label (or specifically what the
programmer wanted to happen).

For example if the rules are: "PERFORM sections and allow GO TO
exit-pargraph", then this simplifies the examination of the labels to
be:  if there is a SECTION keyword then this is performed, if not then
this should be an exit-paragraph that is dropped into or GO TOed.  There
is no need to examine the whole program - as long as the rules have been
followed correctly (and there are other considerations such as there
being a SETION keyword following and the right exit-labels used every
time).

The Rule: "Only ever PERFORM paragraphs", simplifies the examination of
a part of the program even further. Each paragraph starts when it is
PERFORMed and exits at the next label.  There are no drop throughs (if
done correctly) and no GO TOs.

NEXT SENTENCE is a particular problem because it is effectively a GO TO
to the next full stop.  In ANS74 this is not an issue because that is a
fixed position relative to the outer IF statement.  With AN86 however a
problem arises because the full stop 'label' by be moved using END-IFs. 
This means that the logic of a program may be changed at one point by
adjusting code at some different point.

That is: by moving or removing a full-stop it is possible to change the
effect of a NEXT SENTENCE that is inside an IF .. END-IF.  That is why
it is not allowed.

With EXIT PARAGRAPH or EXIT SECTION (when used correctly inside the
appropriate PERFORMed label) there is _no_label_.  This means that it is
in the same class as GO TO in the sense that it is clear what its effect
is at the point of being written, but it is neutral at the point of
examing logic flow at a label.

This means that the EXIT ~ statements, while being classed as GO TOs, do
not impact on logic flows in the same way, and do not suffer the same
pitfalls.  They do have their own pecularities, however, such as if an
EXIT PARAGRAPH is used in a PERFORMed SECTION (or vv), this complicates
changing a program from sections to paragraphs or vv, meaning that they
would not work identically unless these EXIT ~ were also changed.

Reducing the sub-set of usable Cobol constructs (such as no GO TO, no
THRU, no SECTION, etc) simplifies the problems of understanding
programs, or specifically of small parts of programs as is required to
maintain them.  EXIT SECTION and EXIT PARAGRAPH are different enough in
their operation that they would extend the usable sub-set and thus
increase the complexity of understanding a program part. But they are
simpler than the use of GO TO.

If a program, or preferably a complete site, could be converted from 'GO
TO exit-label' style to 'EXIT SECTION' style, then there would be a huge
saving in complexity (by removal of all the exit- labels and EXIT
statements.  If this could then be converted to remove all the SECTION
keywords and convertion to EXIT PARAGRAPH then this would also represent
a further simplification (because there would be no problems arising
from forgotten SECTION keywords).

However, this is unlikely to happen and the introduction of 'EXIT type'
would be in _addition_ to existing mechanisms causing an _increase_ in
the usable sub-set, an increase in complexity, an increase in the number
of things requiring to be checked when examing a part of a program, and
thus an increase in potential bugs.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T11:56:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544ec_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com> <3C959E4E.FDD74ED7@Azonic.co.nz>`

```
This is a good argument and I have thought about it a lot.

I'm not totally convinced, but I'm more sympathetic than I was <G>.

I take your point about Exit paragraphs, Richard, but if the alternative is
to have EXIT SECTION/ WHATEVER sprinkled all through the code, I'd like that
even less. At least with a Paragraph it sticks out and you can SEE it...<G>.

However, I am persuaded by your argument for labels being typed and can see
the benefits you outline. This is really a good idea which maybe you should
have suggested to J4 some time ago? (No, I'm not being facetious...<G>). The
point is that if you have a good idea and it is not propagated it remains
simply a good idea... While my differences with J4 are a matter of record,
the only way there is any chance of getting something like this included in
the Language at the moment is by getting it into the standard.

Unfortunately, by the time this is likely to happen now, COBOL will be a
dead Language like Latin...

Pete.
<snipped excellent discourse from Richard>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-03-18T21:27:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1cec3$ab17e8e0$f534e641@chottel>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com>`

```
People who hate any use of "GO TO" statements should only program computers
that don't have branch onstructions.

Stephen J Spiro <stephenjspiro@mail.com> wrote in article
<928495c6.0203162244.71aa499e@posting.google.com>...
> tom heitbrink <gizmo@hot.a2000.nl> wrote in message
news:<vv779uc689j79mu0745nth6asojnt3gto5@4ax.com>...
> > I also never use the Go To statement, but one advantage of the
> > sections is the simple statement EXIT SECTION.
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-03-22T16:18:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7fl81$a8r$1@peabody.colorado.edu>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com> <01c1cec3$ab17e8e0$f534e641@chottel>`

```

On 18-Mar-2002, "Charles Hottel" <chottel@cpcug.org> wrote:

> People who hate any use of "GO TO" statements should only program
> computers that don't have branch onstructions.

People who want to do things the computer's way instead of what way works
best for businesses should use machine language only.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2002-03-24T07:53:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9D85E8.F90D0C09@optonline.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <928495c6.0203162244.71aa499e@posting.google.com> <01c1cec3$ab17e8e0$f534e641@chottel> <a7fl81$a8r$1@peabody.colorado.edu>`

```
On 18-Mar-2002, "Charles Hottel" <chottel@cpcug.org> wrote:

> People who hate any use of "GO TO" statements should only program
> computers that don't have branch onstructions.

This is a completely specious argument, the discussion of structured
code has nothing at all to do with the binary file generated by the
compiler. The objective is to write readable/maintainable *source* code. 

LiamD
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-17T10:27:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C946F8E.F17D4390@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com>`

```
tom heitbrink wrote:
> 
> I also never use the Go To statement, but one advantage of the
> sections is the simple statement EXIT SECTION.

EXIT SECTION is not yet part of any current Cobol standard (though it
will be in the next one).

That is not an advantage of SECTIONs.  Wherever I have seen 'EXIT
SECTION' implemented there is also 'EXIT PARAGRAPH' which is exactly
equivalent for non-SECTION.

Thus there is no advantage to using SECTION.

There is also a danger in using EXIT SECTION (or PARAGRAPH) in that some
compilers will not complain if 'EXIT' is used.  However, EXIT by itself
does absolutely nothing, yet the programmer may treat it as if it were
an EXIT SECTION and fail to notice the bug.


> Using sections doens't mean programmer can use GOTO en Perform ...
> thru ...

Given that the use of SECTIONs for overlaying is obsolete, then the
_only_ actual reason for using SECTIONs (or PERFORM THRU) is to cater
for the use of GO TO out of a PERFORM.

If there are no GO TOs then there is no functional need for paragraph
names within a PERFORMed SECTION (they can be commented out).  When the
only label is the SECTION name the word SECTION can be removed
throughout the procedure division (changing EXIT SECTION to EXIT
paragraph) without any changes to how the program operates.

> and it's easier to search for specific parts. Paragraphs
> cannot be easily searched, while section. shows the start of every
> section, just like Working storage section and file-section.

Your search would also show every EXIT SECTION.

It is just not hard to search for every paragraph name, if you have
adequate tools.  It is also not hard to search for where a paragraph is,
rather than where it is used.  eg "<space><space>name" will skip PERFORM
name because there is only one space.

Where the use of SECTION fails in any searching is where the SECTION
keyword has been omitted.  This omition causes bugs which may be hard to
find, yet are also difficult to search for.

The reverse, where only paragraphs are PERFORMed, can be verified quite
easily by seaching for the SECTION keyword.  Any found in PD are
potential problems.


> It's something that's COBOL-own, and like I said earlier, doesn't let
> the porgrmmer free to write junk.

Removing SECTIONs (and PERFORM THRU) makes it much harder for the
programmers to write junk, and also make it much harder to get code
wrong.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** "Tim Scrivens" <tim.scrivens@nz.eds.com>
- **Date:** 2002-03-19T08:58:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a75kd4$vun$1@hermes.nz.eds.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <3C946F8E.F17D4390@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3C946F8E.F17D4390@Azonic.co.nz...
> tom heitbrink wrote:
> >
…[5 more quoted lines elided]…
> wrong.

I disagree with your last statement, fairly emphatically.

In my own experience, using both Sections and Paragraphs actually aids
Maintenance, particularly when most of the shop is working in other
languages, and hit the COBOL code once every few months.  I believe that it
allows the code to much more accurately reflect the structured logic
diagrams that we (tinw) base our code on.

Interestingly, one shop I worked in only allowed GO TO in very specific
circumstances.  It was ONLY allowed within a section, and only allowed to
point to the EXIT of that section.  Made for nice, easy maintenance, as it
did not turn the code into logical spagetti (always a danger with an
unrestricted GO TO).  We were not allowed to use PERFORM through, though -
you would often end up with a control section that was merely a list of
PERFORMS that did this in effect.  Still perfectly easy to follow, IMHO.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T10:39:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C97154D.2E1F7673@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <f8p69u0dq1t8onun7dtto4o6u405gu6rbf@4ax.com> <3c939d52$0$260$ba620e4c@news.skynet.be> <vv779uc689j79mu0745nth6asojnt3gto5@4ax.com> <3C946F8E.F17D4390@Azonic.co.nz> <a75kd4$vun$1@hermes.nz.eds.com>`

```
Tim Scrivens wrote:
> >
> > Removing SECTIONs (and PERFORM THRU) makes it much harder for the
…[6 more quoted lines elided]…
> Maintenance, 

Yet others here argue they should never be mixed.

> We were not allowed to use PERFORM through, though -

Presumably you were 'not allowed to use PERFORM thru' because it made it
easier to get code wrong.

> you would often end up with a control section that was merely a list of
> PERFORMS that did this in effect.  Still perfectly easy to follow, IMHO.

You seem to use the word 'section' informally.

Given that you use both Sections and Paragraphs, I suspect that your
structure is like:

       Do-something SECTION.
       Do-something-Control.
           PERFORM Do-Something-Initialise
           PERFORM Do-something-process
           etc.
       Do-something-Initialsise.
           ...

Where the rest of the program does a PERFORM Do-Something-Control.  If
the section label were performed then a GO TO Do-something-Exit would be
required to take it to the end of the section.

I may have completely misunderstood your description though, but if this
is what you do it is _not_ PERFORMed sections, but is performed
paragraphs with the section being merely a grouping of the paragraph
into related blocks.  If you commented out the SECTION labels would the
program compile and work the same ?
```

##### ↳ ↳ Re: Sections

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-16T22:51:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u%Pk8.351$xe2.5113@castor.casema.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com>`

```
I'm using them for 19 years now.
And when you use meaningfull names and contence to them they keep your
programs easy to maintain.
It also makes it easy to have your standard routines in copyfiles.
I'm glad everybody else whose programs I've to modify also did.
How else can you modify a program you've never seen before and you don't
want to try to get what it is doing except for the section where you have to
be for you modification?
I'm even using in my menuprogram(calls every other program because of
security reasons) the segmentation because I don't want to keep all initial
checkups(like: do files need a conversion(auto convert files during startup
after an update)) in memory.

So keep on using sections and meaningfull titles!!

Ronald Leenheer

"JerryMouse" <nospam@invalid.com> schreef in bericht
news:yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com...
>
> "Eddy Scheire" <fa099784@skynet.be> wrote in message
…[28 more quoted lines elided]…
> > I mean why should one use sections? To me it looks like unnecessary
code.
>
> SECTIONS are an artifact, a fossil, a construct from a primative time.
>
> Their major original function was to partition the code into overlayable
> chunks to conserve memory. SECTIONS today permit no unique (or even
useful)
> purpose. Their presence does, however, tend to confuse or bewilder those
who
> have never encountered them - or those, like me, who haven't seen SECTIONS
> in twenty years.
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-17T15:59:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C94BD48.CC3D9E6A@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <yOIk8.16804$1g.904321@bin3.nnrp.aus1.giganews.com> <u%Pk8.351$xe2.5113@castor.casema.net>`

```
ronald leenheer wrote:
> 
> I'm using them for 19 years now.
> And when you use meaningfull names and contence to them they keep your
> programs easy to maintain.

Using meaningful names helps later maintenance and this is completely
independant of whether you use SECTIONs or not.

> It also makes it easy to have your standard routines in copyfiles.

This is completely independant of whether SECTIONs are used or not.  It
makes no difference at all as long as a simple rule is followed: _all_
SECTIONs or _no_ SECTIONs.

> How else can you modify a program you've never seen before and you don't
> want to try to get what it is doing except for the section where you have to
> be for you modification?

This is completely independant of whether SECTIONs are used or not.  

> I'm even using in my menuprogram(calls every other program because of
> security reasons) the segmentation because I don't want to keep all initial
> checkups(like: do files need a conversion(auto convert files during startup
> after an update)) in memory.

This is not a particular good use for overlay SECTIONs.  It is, in fact,
better to use dynamic loading rather than overlaying.  A small 'core'
program can cycle CALLing and CANCELing programs that are in an
interface area.  One of these programs is a default menu program.  Once
the menu has decided that a program can be used it simply put the name
in the interface area and EXIT PROGRAM.  The core will CANCEL it and
CALL the selected program.  Initial checkup files, to will just be
CALLed and CANCELed if required.

By using dynamic structure the programs can be more flexible, for
example by changing menu program during running.

Simplified core program:

      W-S.
      01  Interface.
          03  Program-Name          PIC X(20).
          03  Next-Program          PIC X(20).
          03  Menu-Program          PIC X(20).
          03  Other useful stuff: login name, security level, Company
code, etc
       PD.
           MOVE "mymenu"     TO Menu-Program
           MOVE "checkup"    TO Program-Name
           PERFORM
               UNTIL Next-Program = "FINISH"
              
               MOVE Menu-Program  TO Next-Program
               CALL Program-Name
                   USING Interface
                   ON EXCEPTION ...
               CANCEL Program-Name
               MOVE Next-Program  TO Program-Name
           END-PERFORM
           STOP RUN
           .

Al that the menu program need do is move the selected (and checked for
security) name into Next-Program.  It could also change Menu-Program to
a different program, and _any_ program can move a program name into
Next-Program.  This allows, say, the Invoice Post program to set the
Invoice Print program as being next (if there are any needing printing)
without having to return to the menu program.     

Building all that menuing and check program into one huge program that
then has to be overlayed to keep memory usage down is much less modular
than small functional programs dynamically loaded.

As for security, this is built into my core module.  Having a system
where there is only one place where programs are CALLed means that I can
have the security code _once_ in the system.  The core PERFORM actually
incorporates additional checks where the program name is looked up in a
security file where it may be marked as needing a password, or a certain
operator level or usage flag.

> So keep on using sections and meaningfull titles!!

Always use meaningful labels regardless of whether you use SECTIONs or
not.
```

#### ↳ Re: Sections

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2002-03-16T11:00:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0203161100.43baccce@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
"Eddy Scheire" <fa099784@skynet.be> wrote in message news:<3c931758$0$29682$ba620e4c@news.skynet.be>...
> Hi,
> 
…[25 more quoted lines elided]…
> I mean why should one use sections? To me it looks like unnecessary code.

Hello Eddy

There is no difference as they have been expressed, however, you
should remember that a section only ends just before the next section
header or at the end of the program, if you forget this and don't
organise the whole program in sections, then you are liable to get
overruns when performing sections.  A section can contain none or many
paragraphs.

Although as mentioned earlier in this thread, there are opposing camps
regarding the use of sections, I myself prefer them as it I think they
provide more flexibility and make it easier to amend programs
subsequently.

If you can completely avoid the use of go to statements, then you can
reasonably do without sections, but you have to be very careful to
then avoid excessively complex conditional statements that may arise
as a consequence.

What I think you should definitely try to avoid is the need for
perform paragraph-1 thru paragraph-2 type statements, much better to
use sections.

Genererally, you will probably have to follow the local house-style
and, when amending programs, it is usually best to follow the way the
rest of the program has been written.

Robert
```

##### ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-17T10:52:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C947575.78F1331F@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <fcd09c56.0203161100.43baccce@posting.google.com>`

```
Robert Jones wrote:
> 
> There is no difference as they have been expressed, however, you
…[4 more quoted lines elided]…
> paragraphs.

It is also important to realise that 'EXIT' does not exit.  It is not a
C return(), it does not do what it says it does.  It is better, even
when SECTIONs are used to not have the xxxx-exit paragraph and
especially not the EXIT statement.


> Although as mentioned earlier in this thread, there are opposing camps
> regarding the use of sections, I myself prefer them as it I think they
> provide more flexibility 

In what way ?

> and make it easier to amend programs subsequently.

In what way ?

> If you can completely avoid the use of go to statements, then you can
> reasonably do without sections, but you have to be very careful to
> then avoid excessively complex conditional statements that may arise
> as a consequence.

There is no particular care needed to 'avoid excessively complex
conditionals', there are just different ways of doing so.

In general programmers who PERFORM SECTIONs tend to have a view that
creating a new 'function' as being an expensive operation.  It requires
constructing a new name, putting it into the structure diagram at the
correct level, adding several lines of code (SECTION header, start
paragraph, exit paragraph, EXIT, etc) and finding its place in the code.
So they avoid doing this.  It is easier for them to just use GO TO
xxxx-EXIT or EXIT SECTION.

Once you get over all that and realise that with decent tools it just
doesn't matter, then PERFORMed paragraphs can be broken in situ as
required.  'Complex' conditionals can be broken down very easily into
small paragraphs.  More especially the actions can be put into a small
paragraph just following the current one and this action can be reused
as required to simplify the conditionals.

Instead of:

       IF ( condition 1 )
       OR ( codition2 AND yetanother )
       OR ( someother )
           sequence of actions
           that are too expensive to reapeats
           and I can't be bothered to
           put them in a section
        END-IF

the 'SECTION' programmer will tend to 'simplify' by using GO TO or EXIT
SECTION to create 'simple' IFs that jusp out.

But is it just as easy to have:

       IF ( condition 1)
           PERFORM named-actions
       ELSE
       IF ( condition 2 
        AND yetanother
          )
           PERFORM named-actions
       ELSE etc
       END-IF
       .
    named-actions.
       sequence of actions ..

It is also _much_ easier to reuse code.  If from somewhere else I only
want to use half of named-actions, the I can break it in-situ and add a
PERFORM of one half from the other and then reuse as required.

With SECTIONs this cannot be easily done because the code needs to be
taken out of the scope of the SECTION and must itself be a SECTION.  It
is just too complicated a task to simplify, so GO TOs and their evil
cousins EXIT something are used.
    
> What I think you should definitely try to avoid is the need for
> perform paragraph-1 thru paragraph-2 type statements, much better to
> use sections.

And far better to use neither.

> Genererally, you will probably have to follow the local house-style
> and, when amending programs, it is usually best to follow the way the
> rest of the program has been written.

Often the 'house style' has been written by the person who is now some
manager and will refuse any idea that it isn't perfect and modern
because he hasn't been in touch for several decades.
```

###### ↳ ↳ ↳ Re: Sections

- **From:** docdwarf@panix.com
- **Date:** 2002-03-16T17:53:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a70ie4$ltl$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <fcd09c56.0203161100.43baccce@posting.google.com> <3C947575.78F1331F@Azonic.co.nz>`

```
In article <3C947575.78F1331F@Azonic.co.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>Robert Jones wrote:

[snippage]

>> Genererally, you will probably have to follow the local house-style
>> and, when amending programs, it is usually best to follow the way the
…[4 more quoted lines elided]…
>because he hasn't been in touch for several decades.

... which, Mr Plinston, in no wise alters the fact that s/he still is a 
manager and signs one's timesheets.

When in Rome and all that.

DD
```

#### ↳ Re: Sections

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-16T11:07:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203161107.3e3ba1fc@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
Hi Eddy,

I'm not a fan of sections either. I always forget to code "SECTION"
and my pgm goes haywire.

But getting back to your question. Sections allow you to logically
"block" your code. As an example, you can code a "PROCESS-INPUT-RECORD
SECTION" and include paragraphs to read a record, match it to a table,
and process the match.

So, you can code:

PROCESS-INPUT-RECORD SECTION.
READ-IP-REC.
    some code
    .
SEARCH-XYZ-TBL.
    some more code
    .
PROCESS-MATCH.
    etc.
    .
NEXT SECTION.

A PERFORM PROCESS-INPUT-RECORD stmt will execute all the pgraphs
following the SECTION heading until another SECTION header is
encountered. You can prematurely terminate execution by issuing a GO
TO stmt to an EXIT pgraph or issuing an EXIT SECTION stmt in some
COBOL dialects. Seems kind of thin to me.

So there you have it. Your instincts seem sound to me. However, I'm
sure you'll be hearing from some adherents soon.

Regards, Jack. 

"Eddy Scheire" <fa099784@skynet.be> wrote in message news:<3c931758$0$29682$ba620e4c@news.skynet.be>...
> Hi,
> 
…[25 more quoted lines elided]…
> I mean why should one use sections? To me it looks like unnecessary code.
```

##### ↳ ↳ Re: Sections

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-16T15:56:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203161556.7064aad@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <8a2d426e.0203161107.3e3ba1fc@posting.google.com>`

```
My apologies to all for covering ground already covered. When I posted
"Eddy Scheire's" post was the only recent one displayed.

You see, I use Yahoo to access CLC and they boast a 3 to 9 hour delay
in posting. Finally, "truth in advertizing". :)

Regards, Jack.


jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0203161107.3e3ba1fc@posting.google.com>...
> Hi Eddy,
> 
…[61 more quoted lines elided]…
> > I mean why should one use sections? To me it looks like unnecessary code.
```

#### ↳ Re: Sections

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-16T15:14:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a70ckg$nmn$1@slb6.atl.mindspring.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
Use of sections vs paragraphs TENDS to be a religious war - with no
conclusion (that I have ever seen).  A few statements that GENERALLY get
agreement.

1) Use of GO TO *other* than to an EXIT paragraph (or to the top of a
paragraph/section for a "loop") is usually a "bad idea". "Spaghetti code" is
almost always harder to debug and maintain than structured code.

2) If your compiler already supports EXIT PARAGRAPH *and* EXIT SECTION (that
will be Standard in the next COBOL revision), then you probably NEVER need
to use a GO TO. (Contrary to what one note in this thread implied, I know of
NO current compiler that supports EXIT SECTION that doesn't also support
EXIT PARAGRAPH)

3) There is NO "logical structure" that can be done with SECTIONS that can't
also be done with PARAGRAPHS - and vice versa.

4) *MIXING* of both paragraphs and sections (other than EXIT paragraphs -
within sections) is almost always a "bad idea" - for maintenance purposes -
even though allowing for "grouping of procedures" by paragraphs within
sections was the original language design.

5) Use of "PERFORM xyz THRU abc"  is both very common (especially when "abc"
is an exit paragraph/section and there are NO paragraph/section-names
located between "xyz" and "abc").  However, unless you have "standards
software" that ENFORCES the fact that there are never any paragraph/section
names between xyz and abc, this is bound to end up as "spaghetti code" via
some maintenance some day.  If you DO use PERFORM-THRU exit-procedure, there
are no "inherit" advantages of doing PERFORM paragraph-name THRU para-exit
over PERFORM section-name THRU sect-exit.  Again, anything that you can do
with one, you can do with the other.
 On the other hand, if you do a "simple" PERFORM section-name, you can do a
GO TO para-exit (at the end of that SECTION) and get the same "logical"
behavior as an EXIT SECTION statement from the next Standard.  This is
dangerous (again) if there is ever any chance of another paragraph getting
inserted into the section.

6) Use of all SECTIONS (and no or minimal paragraphs) is very common in the
UK - and the rest of Europe.  Use of all PARAGRAPHS (and no or minimal
sections) is very common in the US.

7) SECTIONS *used* to provide solutions to two problems
  - user defined segmentation
 - old rules on SORT/MERGE Input/Output Procedures
Neither of these issues are of "great concern" today - but lots of
applications show that they USED TO BE important.
```

##### ↳ ↳ Re: Sections

- **From:** docdwarf@panix.com
- **Date:** 2002-03-16T17:57:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a70ikv$med$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net>`

```
In article <a70ckg$nmn$1@slb6.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Use of sections vs paragraphs TENDS to be a religious war - with no
>conclusion (that I have ever seen).

Such is often heard from Unbelieving Poopie-Heads... back, *back*, Unclean 
One!

DD
```

##### ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-17T16:20:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C94C233.2F34F6C7@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Use of sections vs paragraphs TENDS to be a religious war - with no
> conclusion (that I have ever seen). 

It is always useful to see other's opinions, even if they are completely
wrong   ;-)

> 3) There is NO "logical structure" that can be done with SECTIONS that can't
> also be done with PARAGRAPHS - and vice versa.

But with SECTIONs you _can_ just sneak in a GO TO where you cannot
figure out a structured way of doing it.  Not using SECTIONs (or THRU)
ensures that GO TOs cannot be used and a different 'easy way out'
mechanism used, such as breaking code into many small performed
paragraphs that are reused.

The issue is code reusability.  Large SECTIONs and GO TOs (or EXIT ~)
tend to reduce reusability.

>  On the other hand, if you do a "simple" PERFORM section-name, you can do a
> GO TO para-exit (at the end of that SECTION) and get the same "logical"
> behavior as an EXIT SECTION statement from the next Standard.  This is
> dangerous (again) if there is ever any chance of another paragraph getting
> inserted into the section.

That is not the only danger.  Others are:  Forgetting to have the next
label as a SECTION; thinking that EXIT does anything; using the wrong
para-exit.

The last is especially a problem where code is pasted from another
similar section.
```

###### ↳ ↳ ↳ Re: Sections

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T12:14:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544ee_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C94C233.2F34F6C7@Azonic.co.nz...
> William M. Klein wrote:
> >
…[5 more quoted lines elided]…
>
Absolutely!

> > 3) There is NO "logical structure" that can be done with SECTIONS that
can't
> > also be done with PARAGRAPHS - and vice versa.
>
…[8 more quoted lines elided]…
>
Not in my experience. Or in my programs. I have no problem whatsoever with
re-using sectioned code. Show me an exaple of how you believe sectioning
reduces re-usability. I can perform a section just as easily as you can
perform a paragraph (and I do).

> >  On the other hand, if you do a "simple" PERFORM section-name, you can
do a
> > GO TO para-exit (at the end of that SECTION) and get the same "logical"
> > behavior as an EXIT SECTION statement from the next Standard.  This is
> > dangerous (again) if there is ever any chance of another paragraph
getting
> > inserted into the section.
>
Why?  I see no danger. The exit paragraph is still at the end of the
section. As a programmer it is your responsibility to see that when you
insert code into a program you put it in the right place...

> That is not the only danger.  Others are:  Forgetting to have the next
> label as a SECTION; thinking that EXIT does anything; using the wrong
> para-exit.
>
The "NOOPerativeness" of an EXIT is really irrelevant, although I agree that
it doesn't do what it says it does (well, it doesn't sometimes...<G>) Forget
ting to have the next label as a section is no danger if you are used to
coding that way. I am. I've never had a problem with mixing sections and
paragraphs because I DON'T DO IT!


> The last is especially a problem where code is pasted from another
> similar section.

Hmmm...all I can see here is that a certain style of coding is problematic
to people who don't ascribe to it. To those who do, these "problems" and
"dangers" are simply prevarications, shadows, and phantoms with no real
substance. I cut and paste code all the time. Never encountered the
"problem" expressed above. I suggest that there is much more "danger" in
getting code right, than there is in the form of it. And I don't accept the
argument that a form which I have used successfully for many years is error
prone and "dangerous"...It might be when YOU do it; it isn't when I do it!

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T06:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96DC1E.4CF0B9C8@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz>`

```
> > The issue is code reusability.  Large SECTIONs and GO TOs (or EXIT ~)
> > tend to reduce reusability.
…[3 more quoted lines elided]…
> reduces re-usability.

_Large_ sections reduce reusability because of lack of granularity. 
Large paragraphs may reduce reusability too.  However, the ability to
use GO TO (which requires that it be a section or THRU) is more likely
to result in larger sections.  This is because it is mostly easier to
'bail out' with a GO TO than it is to split the section to break down
complex conditional structures.

When only paragraphs are used then GO TO cannot and alternatives used. 
If there are few outside constraints on where and how paragraphs are
broken then a smaller granuality occurs and/or may be created
deliberately in order to perform the resulting paragraphs.

It is more likely that small paragraphs are performed from different
points rather than just copy/pasting the code from one section to
another.

GO TOs also tend to reduce reusability in the copy/paste sense because
of the adjustment required.
```

###### ↳ ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T06:56:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96E13B.D68D5AD@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz>`

```
> The "NOOPerativeness" of an EXIT is really irrelevant, although I agree that
> it doesn't do what it says it does (well, it doesn't sometimes...<G>) 

I have seen EXIT used in an IF as if it was EXIT SECTION.  MF doesn't
complain about this.

> Forget
> ting to have the next label as a section is no danger if you are used to
> coding that way. I am. I've never had a problem with mixing sections and
> paragraphs because I DON'T DO IT!

So you are saying that it is not a problem because you have _never_
forgotten, and no one who will work on your code will ever forget
either.

I assume that your SECTIONs don't have any paragraph labels at all and
that you thus don't use GO TO Exit-paragraph.

> > using the wrong para-exit.

> To those who do, these "problems" and
> "dangers" are simply prevarications, shadows, and phantoms

Now you have said that you don't mix sections and paragraphs so you
can't be 'using the wrong para-exit'.  Not using GO TO and para-exit
means that you have avoided the dangers.

> all I can see here is that a certain style of coding is problematic
> to people who don't ascribe to it.

I have worked in many different styles.  Some because the existing
systems were that way, others because I had a free hand in developing
styles as I wished, even more because I worked in other languages with
certain idioms.  This allows me to do comparisons.  My comments are from
experience of my and other's coding.

There was even one here who developed specific checking programs to
ensure that these dangers did not actuate.  

This is not to say that people using sections are bad programmers, or
even forgetful, but there are things that benefit from checking (whether
this be automatic or automated) that won't occur in other styles.  I am
merely raising the issue that these things need to be checked, you never
forget to check them, excellent.  I never need to check those (but I do
check other things).

>  And I don't accept the
> argument that a form which I have used successfully for many years is error
> prone and "dangerous"...It might be when YOU do it; it isn't when I do it!

It must be such a strain to be perfect   ;-)
```

###### ↳ ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T07:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96E5DB.CA224074@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz>`

```
> I take your point about Exit paragraphs, Richard, but if the alternative is
> to have EXIT SECTION/ WHATEVER sprinkled all through the code, I'd like that
> even less. 

There are other alternatives.

> At least with a Paragraph it sticks out and you can SEE it...<G>.

Hmm. People like to see what they are used to. If fact some (I am not
referring to you here ;-) only see what they are used to even if it is
not there.
 
> However, I am persuaded by your argument for labels being typed and can see
> the benefits you outline. This is really a good idea which maybe you should
> have suggested to J4 some time ago? 

I did send it in a couple of years ago.  I posted it here too, so it
should be on Google.

Basically I added qualifers to the labels such as LOCAL (only within
current paragraph), FROM (only used for a GO TO), PERFORMED (only usable
by PERFORM) and ABOVE (may be dropped into).  A section then may be:

         XYZ PERFORMED SECTION.
         XYZ-Start LOCAL ABOVE.
  
              blah blah
                  GO TO XYZ-Exit


         XYZ-Exit LOCAL FROM ABOVE.
             EXIT.
         ZZX PERFORMED SECTION.
         etc

If there is a label qualifier then any usage other than that given would
be a compile time or run-time error.  This would (if used) eliminate
wrong exit-paras, drop-thrus and other things that are possible with
section_and_gotoexit style.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T08:46:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96FAE6.296E4474@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz> <3C96E5DB.CA224074@Azonic.co.nz>`

```
Richard Plinston wrote:
> 
> > However, I am persuaded by your argument for labels being typed and can see
…[4 more quoted lines elided]…
> should be on Google.

I just had a look at Google and I first outlined my ideas on label
qualifiers at the end of 1996 in thread 'Re: Sections vs. Paragraphs -
Challenge'

Looking through these old messages indicates that 'section vs paragraph'
is an annual event.
```

###### ↳ ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T07:48:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96ED4A.1B0DF36C@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <a70ckg$nmn$1@slb6.atl.mindspring.net> <3C94C233.2F34F6C7@Azonic.co.nz>`

```
> > Either these labels are non-functional (not referenced) or you are using
> > GO TOs in a spagetti like way.
> 
> Your analysis is correct. The point you may be missing is that paragraph
> names (labels) are NOT always used as branch destinations.

I don't think that I missed that at all, I had included 'not refereced'
as an option.

> Sometimes they
> simply serve to document the function of the next bit of code. There is
> therefore nothing wrong in having "non-functional (not referenced) " labels,
> particularly in a self-documenting language like COBOL.

Well actually I think that there _is_ something wrong in having
non-functional labels.

When the _next_ programmer comes to work on the code to change some
small part (due to, say, a business change) then he wants to understand
the minimum amount of that code in order to get the change done in the
shortest time.  This is the whole point of modular and structured
programming anyway.

In order to understand the code then the logic must be understood, each
paragraph label is a potential 'logic point' that must be examined.  If
it is merely commentary then it wastes times and should be commented
out.  It may, after all, be a pargraph that is performed from outside
and this requires a search of the complete source code (though I would
comment them out and recompile to check this).

In fact in my proposal for label qualifiers also included one mechanism
for measuring program complexity.  This was a metric given by adding 1
for every label (section or paragraph) and 1 for every type of usage of
these beyond the first type of use.

Type of use is PERFORM, THRU, GO TO, Drop-through.  ALTER adds 10,000
for each use.

In the case of 'commentary' labels they are only Dropped through and so
count 1.  Exit-paras may be both droped through and GO TOed and so may
count 2.  If a specific GO TO exit-para is added immediately before the
label then this stops the drop and reduces the complexity metric.  Does
it reduce the complexity ?  It may do to the _next_ programmer because
it is a specific signal about what happens.  EXIT SECTION also reduces
the complexity metric if the exit-para label is removed so ensuring that
there is not both EXIT SECTION _and_ GO TO exit-para.

In general the particular styles do have the effect of minimising the
complexity by restricting labels to have only one type of usage.  This
metric reflects that.

Commenting out the non-functional labels does indeed reduce the workload
for the next programmer while retaining the comments that should assist
him, it also reduces the complexity metric.
```

#### ↳ Re: Sections

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-17T09:44:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544e7_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```

Eddy Scheire <fa099784@skynet.be> wrote in message
news:3c931758$0$29682$ba620e4c@news.skynet.be...
>
> I mean why should one use sections? To me it looks like unnecessary code.
>
This is a recurrent theme in CLC.

If you think it is unnecessary, don't use it.

That's the nice thing about writing COBOL, there are many different ways to
do it and many different styles can be supported.

I use sections for a number of  reasons:

1. In the early days (1960s) I used PERFORM...THRU. I figured that this
nicely documents the range of the PERFORM. It does, but it suffers from the
disadvantage that you can have overlapping ranges and this creates chaos...

Remember, at the time I was doing this, there were NO "accepted
practices"... we wrote programs and experimented. Anything that worked was
"Good".

Then I was exposed to some code that used SECTIONs. No overlapping ranges.
Add new paragraphs without problem... looked like good stuff. Tried it,
liked it. So my first reason for using SECTIONs in COBOL is that it
organises the functionality into separate chunks and avoids troublesome
"drop thrus".

2. In those days (before Virtual Memory was invented) we used to overlay
programs and this could only be achieved in COBOL by using segment priority
numbers on the SECTIONS. This is no longer relevant today, but having gone
through it, it does cause you to look at segmented functionality  in a
program. I no longer think in terms of overlays, but I certainly think in
terms of encapsulation and isolation of function (particularly when it comes
to OO COBOL, where I use sections within OO Methods to logically break up
the functionality. Often an OO Method will be a single SECTION.) and using
SECTIONS is a good way to document this.

3. It gives me a simple structure with which to organise a given function. I
know that in MY code, PERFORMS will either be in-line or of a SECTION. I
know that each SECTION has one, and only one, exit point (the last paragraph
is an EXIT. I rarely use GO TO but when I do it will NEVER be outside the
SECTION it is coded in, and it will usually be to the exit point. Sometimes
it will be to the beginning of the section (like in filtering input, when
the record I fetched is not one I want and I need to get the next
one...PERFORM GET-A-RECORD will ensure that I get a record that qualifies.)
There are many ways of achieving the same effects I have described here and
I would not insist that SECTIONs must be used; just that they work for me...

Unfortunately (or maybe not...<G>) I cannot see some of the posts that have
been made here as there is the usual server echoing problem that means some
of what is posted doesn't get echoed outside the US. I saw some quoted stuff
from JerryMouse where he was responding rationally to some hysterical abuse
of anyone who uses sections...the poster was raving on about archaic code
and dinosaurs and so on... I don't understand why people are SO uptight
about coding. It is computer programming, NOT Life and Death.

Anyway, I use SECTIONs and I really don't care whether YOU do or not...<G>

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Sections

- **From:** "Rufio" <davecawdell@cox.net>
- **Date:** 2002-03-16T22:01:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jhPk8.7308$Es6.333398@news2.west.cox.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
I don't see any easy way to write Structured Code, with using paragraphs.
Personally, I build paragraphs in sections, so that I can perform a section,
rather than performing a range of paragraphs. There are many pitfalls
performing a range of paragraphs, and sections remove some of them.

If you don't write structured code - why not ?

(I'm trying to modify my clients 6000-line online (updating) IMS
conversational program, with NO PARAGRAPHS & NO SECTIONS - think I'll just
throw it away & start again ! ).



"Eddy Scheire" <fa099784@skynet.be> wrote in message
news:3c931758$0$29682$ba620e4c@news.skynet.be...
> Hi,
>
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sections

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2002-03-16T22:49:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C94204D.43283EDA@mb.sympatico.ca>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net>`

```
Rufio wrote:

> (I'm trying to modify my clients 6000-line online (updating) IMS
> conversational program, with NO PARAGRAPHS & NO SECTIONS - think I'll just
> throw it away & start again ! ).
>

Throw it away.  While you can probably rewrite it with no paragraphs or
sections,  it's something of a tour-de-force to accomplish - more something to
be in awe of rahter than be pleased with - and TPB who has to maintain it will
curse you, as it's 10000 time more difficult to understand, not to mention much
more fragile when it comes toadding code or modifying the flow.

PL
```

##### ↳ ↳ Re: Sections

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2002-03-17T09:01:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C945B32.DD6A34B8@worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net>`

```
Rufio wrote:
> 
> I don't see any easy way to write Structured Code, with using paragraphs.
…[4 more quoted lines elided]…
> If you don't write structured code - why not ?

In the religious wars, my position is paragraphs only, no sections
(sorry!).

The rules in my shop are:
1.  No SECTION keywords in the Procedure Division.
2.  No THRU keywords on the PERFORM statement.
3.  No GO TO statements (and obviously, no ALTER statements).
4.  PERFORM may only reference a procedure farther down in the code. 
In-line PERFORM is not affected by this rule.

I did not establish these rules, I just use them.  Rule 1 could be
changed to require SECTION for all procedure names and the program
could still be considered "structured" (exactly one entry and one exit
for every procedure).  Any use of PERFORM...THRU or GO TO would mean
the program was not structured.  Rule 4 was intended to reduce the
likelihood of infinite loops.

> 
> (I'm trying to modify my clients 6000-line online (updating) IMS
> conversational program, with NO PARAGRAPHS & NO SECTIONS - think I'll just
> throw it away & start again ! ).

Although I have never verified it, I was told more than ten years ago
that using SECTION in a CICS COBOL program created very inefficient
code.  That might have been a problem limited to OS/VS COBOL.

> (section/paragraph example snipped)
> > and
…[13 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Sections

- **From:** "Eddy Scheire" <fa099784@skynet.be>
- **Date:** 2002-03-17T10:29:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9461a4$0$29687$ba620e4c@news.skynet.be>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net>`

```
Hi all of you,

I didn't want to start a "SECTIONS/NO SECTIONS-war", just wanted to know the
difference between sections and paragraphs. Anyway, statements like these
Arnold wrote down sound great to me. I wish I could work in such an
environment. And FYI, I've written quite some COBOL-programs and never used
SECTIONS nor GO TO nor EXIT. And they run without any problem.

Eddy

"Arnold Trembley" <arnold.trembley@worldnet.att.net> schreef in bericht
news:3C945B32.DD6A34B8@worldnet.att.net...
> Rufio wrote:
> >
> > I don't see any easy way to write Structured Code, with using
paragraphs.
> > Personally, I build paragraphs in sections, so that I can perform a
section,
> > rather than performing a range of paragraphs. There are many pitfalls
> > performing a range of paragraphs, and sections remove some of them.
…[22 more quoted lines elided]…
> > conversational program, with NO PARAGRAPHS & NO SECTIONS - think I'll
just
> > throw it away & start again ! ).
>
…[17 more quoted lines elided]…
> > > I mean why should one use sections? To me it looks like unnecessary
code.
> > >
> > >
…[3 more quoted lines elided]…
> http://arnold.trembley.home.att.net/
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2002-03-17T18:42:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9537DE.8FBE0BE2@mb.sympatico.ca>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <3c9461a4$0$29687$ba620e4c@news.skynet.be>`

```
Eddy Scheire wrote:

> Hi all of you,
>
…[7 more quoted lines elided]…
>

Good.  But: so?  Lots of people have written programs that use all three, and
the programs run without any problem.  And (but herein lies the rub) if they're
well-written, they are easy to maintain.  Just the same as well-written programs
that don't use sections or goto's or exits.

PL
```

###### ↳ ↳ ↳ Re: Sections

- **From:** docdwarf@panix.com
- **Date:** 2002-03-17T10:10:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a72bl9$hfg$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net>`

```
In article <3C945B32.DD6A34B8@worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>In the religious wars, my position is paragraphs only, no sections
>(sorry!).
…[13 more quoted lines elided]…
>likelihood of infinite loops.

Hmmmmm... are you sure about that?  My memory is, admittedly, porous but I 
recall someone, somewhen, telling me that an Anciente Compiler would 
compile, without belch or error, a backwards-referring PERFORM... but the 
resulting load/executable module would not execute it.

Are there any Olde Fartes out there who recall such a thing?

DD
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-03-17T10:20:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1v2l8.658$V94.92769@news20.bellglobal.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com>`

```
As I remember it, the section level number controled it.  Above a certain
level number (section 50 rings a bell), sections were non resident, and the
rule was that a no resident section could only be executed by a non resident
section.  The default resident number could be varied to affect program
size.

Donald

<docdwarf@panix.com> wrote in message news:a72bl9$hfg$1@panix1.panix.com...
> In article <3C945B32.DD6A34B8@worldnet.att.net>,
> Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-03-17T19:43:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C94F1B1.2993D2D4@shaw.ca>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com> <1v2l8.658$V94.92769@news20.bellglobal.com>`

```


Donald Tees wrote:

> As I remember it, the section level number controled it.  Above a certain
> level number (section 50 rings a bell), sections were non resident, and the
…[5 more quoted lines elided]…
>

Your memory serves you well Don <G>. The magic number was 50, 0 thru 49 being
resident with 50 thru 127 as overlays. With RM/COBOL and 64K on a Radio Shack,
typically I used the segmentation for "once only routines", opening files,
setting up tables etc.

Checking back on my code, my Mainline Section always had a reference to perform
X000-OPEN-FILES SECTION, tucked away at the end of the source. Occasionally,
because of number of files limitation, (this was ANSI '74), I additionally had
X010-OPEN-CLOSE SECTION -  close specific files, open specific files, associated
with SAME FILE and RECORD areas.

As for Stephen and his, "Don't use EXITS....". Well .....!!! You do it your way
and I'll do it mine <G>.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-03-18T11:46:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F8785D1B3AB075F8.1C6FACA18A10EC19.81D5A7908D2452FB@lp.airnews.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com> <1v2l8.658$V94.92769@news20.bellglobal.com> <3C94F1B1.2993D2D4@shaw.ca>`

```
On Sun, 17 Mar 2002 19:43:49 GMT, "James J. Gavan" <jjgavan@shaw.ca>
enlightened us:

>
>
…[26 more quoted lines elided]…
>

On an IBM or IBM clone mainframe, a Section priority number of from 0
- 49 was defined as a "permanent" segment and made up the "fixed"
portion of memory.  Ideally, all program segments having priority
numbers ranging from 0 - 49 were treated as permanent segments.
However, when insufficient storage was available to contain all
permanent segments plus the largest overlayable segment, it became
necessary to decrease the number of permanent segments.  The
SEGMENT-LIMIT feature provided the coder with a means by which they
could reduce the number of permanent segments in the program, while
these permanent segments would still retain the logical properties of
the fixed portion segments.

Priorities of from 50 - 99 were defined as "independent"  segments.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

When confronted by a difficult problem, you can solve it more easily by 
reducing it to the question, "How would the Lone Ranger handle this?"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-18T01:43:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZCbl8.15432$tP2.1345429@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com> <1v2l8.658$V94.92769@news20.bellglobal.com>`

```
I vote for Donald's memory. It's the same as mine.

warren simmons
Donald Tees <donald_tees@sympatico.ca> wrote in message
news:1v2l8.658$V94.92769@news20.bellglobal.com...
> As I remember it, the section level number controled it.  Above a certain
> level number (section 50 rings a bell), sections were non resident, and
the
> rule was that a no resident section could only be executed by a non
resident
> section.  The default resident number could be varied to affect program
> size.
…[3 more quoted lines elided]…
> <docdwarf@panix.com> wrote in message
news:a72bl9$hfg$1@panix1.panix.com...
> > In article <3C945B32.DD6A34B8@worldnet.att.net>,
> > Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[20 more quoted lines elided]…
> > Hmmmmm... are you sure about that?  My memory is, admittedly, porous but
I
> > recall someone, somewhen, telling me that an Anciente Compiler would
> > compile, without belch or error, a backwards-referring PERFORM... but
the
> > resulting load/executable module would not execute it.
> >
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T12:32:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544f5_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:a72bl9$hfg$1@panix1.panix.com...

>
> Hmmmmm... are you sure about that?  My memory is, admittedly, porous but I
…[5 more quoted lines elided]…
>
As it is my 50-somethingth birthday on Wednesday I guess I qualify as an
"Olde Farte"... (Thanks, Doc....<G>)

Don and Jimmy both mentioned segmentation with a limit of 50. Some compilers
actually implemented the SEGMENT-LIMIT clause and you could have permanent,
quasi-permanent, and resident overlays controlled by it. However, I believe
the problem you are referring to was one from the early days of Virtual
Memory. Backward PERFORM references caused the system to page the remainder
of the load module searching for the reference, not find it, then start
again at the beginning. Horrifically inefficient. (We took advantage of this
when we were trying to persuade our Management that Virtual Memory was a
"Bad Thing"...using this effect to thrash the paging device to death and
cause applications to increase their run times many fold...See, we didn't
like seeing the Art of programming being "de-skilled"  ...I can smile about
it now, but it was really very naughty...<G>)

I don't think it was true that it WOULDN'T execute it...just that it took an
inordinately long time to do so...

HTH,

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-19T08:25:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C96F5DC.CC1C2E8D@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com> <3c9544f5_8@Usenet.com>`

```
freewheelin wrote:

>  The GO TO DEPENDING structure solved it with
> ease and clarity.  

As would several other different mechanisms, EVALUATE springs to mind.
'Table driven' also could be appropriate.  I have in fact reduced code
that was originally in a GO TO Depending on into a very small core of
PERFORMed code that used a table (basically indexed by the depending on
variable).  This made it far easier to maintain as changes were to one
piece of code and a table.  In fact the table could be read in from a
configuration file so the changes could be made without any coding.

> We eventually banned PERFORM structure from such
> programs.

How ironic that you admonished Ruffio for 'compromising flexability' by
setting rules, and then you apply a ban.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-19T00:28:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yCvl8.19593$Ex5.1737386@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com> <3c9544f5_8@Usenet.com> <3C96F5DC.CC1C2E8D@Azonic.co.nz>`

```
Of no particular import, GO TO DEPENDING ON was the result of a common
practice with C-10 instructions (U1).
A go to looked like this 000000 u00nnn. It was easy to 'add' to the nnn to
get the next go to address in C-10.  When it
came to implementation on the Univac, the thought was that "nnn" would have
the value of  A thru Z (26) branches.
This was a stickler for the U 1 coders, and had to be changed. As one can
SEE, it was a machine related feature at that
time, and clearly not as advanced as some of todays features.

Warren Simmons

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C96F5DC.CC1C2E8D@Azonic.co.nz...
> freewheelin wrote:
>
…[15 more quoted lines elided]…
> setting rules, and then you apply a ban.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2002-03-17T18:46:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9538CD.2B333EB5@mb.sympatico.ca>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <a72bl9$hfg$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>
>
…[7 more quoted lines elided]…
> DD

Can't see how the location of a performed paragraph would have anything to do
with it.  If you wrote a program with all the performed paragraphs right at
the beginning, before the mainline, it should work fine, and AFAIK always
did.  Although of course it's possible that a compiler was written with some
sort of restriction like this;  perhaps in a 32K environment there would have
been too much overhead (although again I can't imagine why).  Mayeb a c-l-c
urban myth.

PL
```

###### ↳ ↳ ↳ Re: Sections

- **From:** none@none.com (freewheelin)
- **Date:** 2002-03-18T14:48:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c96164f.7270214@news.earthlink.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net>`

```
On Sun, 17 Mar 2002 09:01:26 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>Rufio wrote:
>> 
…[13 more quoted lines elided]…
>3.  No GO TO statements (and obviously, no ALTER statements).

Thats the problem with good intentions.  Flexibility is compromised.
The proof is in the pud, so to speak.  The best case I have seen for
avoiding the PERFORM statement is an EDI interface where the
translator creates flat file records identified by sequence numbers.
There may be duplicate record numbers from EDI segment loops or there
may be none, depending on the transmission.  Reading the file with the
PERFORM structure is a nightmare.  Something similar to a priming read
is required for 'some' record types - if they exist at all. That means
switches, control breaks and nesting the flow for PERFORM structure.
The obfuscation, based on shop standards,  was unecessary and simply
wasted time (and money).  The GO TO DEPENDING structure solved it with
ease and clarity.  We eventually banned PERFORM structure from such
programs.

>4.  PERFORM may only reference a procedure farther down in the code. 
>In-line PERFORM is not affected by this rule.
…[36 more quoted lines elided]…
>http://arnold.trembley.home.att.net/
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-03-18T16:14:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a753i3$lu6$1@peabody.colorado.edu>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <3c96164f.7270214@news.earthlink.net>`

```

On 18-Mar-2002, none@none.com (freewheelin) wrote:

> >The rules in my shop are:
> >1.  No SECTION keywords in the Procedure Division.
…[15 more quoted lines elided]…
> programs.

Places that I have worked for with standards have had procedures for gaining
OK's when it makes sense to avoid standards.

But in your example, why wouldn't an EVALUATE statement work within the
older standards and still be easy to read and perform?  The EVALUATE
statement would also have the advantage of being able to handle an OTHERWISE
condition.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** none@none.com (freewheelin)
- **Date:** 2002-03-18T23:54:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c969450.3581661@news.earthlink.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C945B32.DD6A34B8@worldnet.att.net> <3c96164f.7270214@news.earthlink.net> <a753i3$lu6$1@peabody.colorado.edu>`

```
On Mon, 18 Mar 2002 16:14:55 GMT, "Howard Brazee"
<howard.brazee@cusys.edu> wrote:

>
>On 18-Mar-2002, none@none.com (freewheelin) wrote:
…[24 more quoted lines elided]…
>older standards and still be easy to read and perform?  

No doubt it would work. I recall the EVALUATE caused difficulty and
unfortunately I can't recall exactly why.  It was 10 years ago.  GO TO
DEPENDING was easier, for driving this type of program.  


>The EVALUATE
>statement would also have the advantage of being able to handle an OTHERWISE
>condition.
```

##### ↳ ↳ Re: Sections

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T12:17:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544f2$1_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net>`

```

Rufio <davecawdell@cox.net> wrote in message
news:jhPk8.7308$Es6.333398@news2.west.cox.net...
> I don't see any easy way to write Structured Code, with using paragraphs.
> Personally, I build paragraphs in sections, so that I can perform a
section,
> rather than performing a range of paragraphs. There are many pitfalls
> performing a range of paragraphs, and sections remove some of them.
…[7 more quoted lines elided]…
>
Agree completely, Dave. It makes me nostalgic to think of you maintaining
IMS/DC that is that badly written... Even in my day we structured such code
into sections exactly as you describe.

Good Luck!

Pete.





 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-18T07:03:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C959143.59F1721A@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net>`

```
Rufio wrote:
> 
> I don't see any easy way to write Structured Code, with using paragraphs.
> Personally, I build paragraphs in sections, so that I can perform a section,
> rather than performing a range of paragraphs. There are many pitfalls
> performing a range of paragraphs, and sections remove some of them.

It seems that you PERFORM sections where these sections contain a number
of paragraph labels.

Either these labels are non-functional (not referenced) or you are using
GO TOs in a spagetti like way.

What definition of 'structured code' do you use ?
```

###### ↳ ↳ ↳ Re: Sections

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-18T12:39:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9544fb_8@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <jhPk8.7308$Es6.333398@news2.west.cox.net> <3C959143.59F1721A@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C959143.59F1721A@Azonic.co.nz...
> Rufio wrote:
> >
> > I don't see any easy way to write Structured Code, with using
paragraphs.
> > Personally, I build paragraphs in sections, so that I can perform a
section,
> > rather than performing a range of paragraphs. There are many pitfalls
> > performing a range of paragraphs, and sections remove some of them.
…[7 more quoted lines elided]…
> What definition of 'structured code' do you use ?

Your analysis is correct. The point you may be missing is that paragraph
names (labels) are NOT always used as branch destinations. Sometimes they
simply serve to document the function of the next bit of code. There is
therefore nothing wrong in having "non-functional (not referenced) " labels,
particularly in a self-documenting language like COBOL.

The same effect can be achieved with comments, some people use both comments
and labels... the point is that it is a style choice which comes down to the
individual. I believe it is wrong to labour the "rightness" or "wrongness"
of this. Any approach which works is viable.

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Sections

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-16T22:20:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```
Eddy,

When COBOL was first defined, hardware was considerably different than now.
Here is a description of
one of the systems in use then. It may seem funny now as your desktop makes
it look very old.'

Input and output was by tape OR a type-in by the operator/programmer.
The RAM  was made up of circuits using a Mercury Delay Line and conversion
between
digital and sound. This RAM consisted of 1000 twelve six bit words
construted of a sign
and eleven other characters OR TWO six character instructions. The
instructions were
limited to the range of the binary equivalent and matched the typewriter
range of the day (64). Oh, and
of course the range of the punched card which could be used via separate
devices that
wrote to tape, or printed or punched from tape. The printer (also separate)
had a memory using
vacume tube that could represent a total of 120 characters and print 600
lines a minute.

There was NO operating system! Either the operator set up instructions which
read the tape to obtain
code that would control operations or after some time, this first block of
instructions became what
was called a program locator and was placed on the tape. In the case of a
library of programs this
block was between each program. The I/O buffer held 720 characters (60
words). For the simple program
with one input and one output (on tape) 120 words were used to buffer the
I/O.  Sorts for example
would use two or three input and output tape drives. Ten drives were common.
For the three way
sort, little code space was left after allocating buffers for each drive in
use. The program libary tape could
be very busy loading and reloading code for the program.

You could do much of what can be done today with this hardware, but it did
not stay up for years,
months, days, or hours at a time without a team of engineers on the ready to
find and fix problems.

A tape held 1000 blocks, and yet at 60 minutes per tape sort, it was faster
than a card sort.

If more code was needed beyond the memory available, an OVERLAY could be
done.'

Overlay became known as a SEGMENT.  Now days, it seldom is used in this
manner, but
some people use it instead of a paragraph name as a supper paragraph. There
are some differences
in the way this works.

So, some features of COBOL are OLD like I am. They sometimes have a use.
Read your
manual.

Warren Simmons
Eddy Scheire <fa099784@skynet.be> wrote in message
news:3c931758$0$29682$ba620e4c@news.skynet.be...
> Hi,
>
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sections

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-17T15:29:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C94B65A.1470082D@Azonic.co.nz>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net>`

```
398199821 wrote:
> 
> When COBOL was first defined, hardware was considerably different than now.
…[7 more quoted lines elided]…
> digital and sound. 

Name one machine based on mercury delay line memory that ever
implemented a COBOL compiler.

In fact COBOL is quite unsuitable for use on MDL memory.  In order to
obtain best performance from MDL the instructions had to be placed
correctly in memory to reduce 'fetch' time to a minimum.  Typically an
instruction could be performed by the CPU in the time it took for the
memory to move forward a few, or a few tens of instructions.  It was
completely inappropriate to wait for the whole memory to cycle pass
waiting for the 'next' instruction, it had to be timed out and placed
where it could be fetched quickest.  This meant that each instruction
had to contain the address of the next one.  As there were usually
several tubes the address included the tube and word.  These tubes had
to be synchronised (they drifted due to temperature and air pressure) so
that the best performance could be reliably obtained.

For a programming example see "Early British Computers".
```

###### ↳ ↳ ↳ Re: Sections

- **From:** "398199821" <warren.simmons@worldnet.att.net>
- **Date:** 2002-03-17T18:22:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz>`

```
Richard, you seem to know your mercury delay lines.  However, the first
COBOL compiler was on a Univac I called

Flowmatic. This program was full of overlays and worked in 1000 words. When
we adopted it prior to COBOL, we got an early Univac II which had "solid
state" memory (unless the dew point got out of wack). But it had 2000 words
instead of one,
and we commissioned the addition of a multiply "generator" for Flowmatic.
That genearator was the only piece of the Flocmatic compiler that used 2000
words. AFLC using Flowmatic adjusted to create 1100 object code took all day
to geneate one program. Latency time on the Univac could be an advantage in
some cases, but
like the situation today on data types, it made little difference because
changes got the latency out of wack at ehe first
modificatiion. This practice was a waste of time on Data Processing
applications. The first CODASYL COBOL compiler ran on U I's and U II's and
did not spend much time with latency.
Warren Simmons
Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C94B65A.1470082D@Azonic.co.nz...
> 398199821 wrote:
> >
> > When COBOL was first defined, hardware was considerably different than
now.
> > Here is a description of
> > one of the systems in use then. It may seem funny now as your desktop
makes
> > it look very old.'
> >
> > Input and output was by tape OR a type-in by the operator/programmer.
> > The RAM  was made up of circuits using a Mercury Delay Line and
conversion
> > between
> > digital and sound.
…[17 more quoted lines elided]…
> For a programming example see "Early British Computers".
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 4)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-17T22:02:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203172202.489f8028@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net>`

```
My own general rule is that I never want an "escape" from a paragraph
unless I want to force an ABEND.

Any time the logic is so complex that you NEED an "escape" from the
module, my suspicion is that the logic is expressed inelegantly and
could/should be simplified.  Particularly with the EVALUATE
instruction, complex combined conditions can be expressed quite
clearly, and relatively simple subroutines can be performed.  One of
the frequently overlooked principles of modular structured programming
is that of COHESION: each module should contain only statements which
are tightly-coupled logically or functionally.  If done right, the
need for "escapes" from such routines is non-existent.

I will recommend to my clients that they prohibit the use of EXIT
PERFORM, EXIT PERFORM CYCLE, EXIT PARAGRAPH and EXIT SECTION, just as
many of them now prohibit GO TO and PERFORM THRU.

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-19T02:09:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c95f7cb_2@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com>`

```
Stephen,

I understand your arguments and the feelings behind them. As I have no real
problem with what you wrote (neither strongly agree nor disagree), normally
I wouldn't comment. But there is one thing that worries me a lot...

That word "prohibit".

Does it not strike you as kind of senseless to spend time on J4 arguing for
(or against) constructs that you (or someone else) then intend to
"prohibit"? If you argued against certain constructs and were overruled,
doesn't it make a mockery of the whole process if you do not accept the
decision of the committee?

It's like saying, "Well, I couldn't persuade my peers, but I'll damn well
persuade my customers..." (presumably the customers are less well informed
than your peers and so rely on your advice...)

Even leaving that aside, here's a different aspect on how we might deal with
"troublesome" or "dangerous" constructs (Ooooooohhhh)...(I'm really getting
tired of people saying certain constructs or styles of coding are
"dangerous"... when was someone hospitalised by an Altered GO TO? Who got a
broken arm from a nested IF?  It is computer code for Chrissake! )

What if, instead of "prohibiting", "forbidding", "banning", or generally
disallowing certain constructs, we actually banned NOTHING (not even ALTER
<ARRRGHHH! Shock! Heresy!>), but instead we educated people in the way to
use these things?

What if we actually called ourselves "programmers" and made it our business
to understand "programming"?

What if, instead of imposing constraints and forcing a given style of
programming, we actually gave guidelines, but encouraged people to develop
their own style of programming? The prime criterion being simply that the
program should work correctly. And then we saw to it that everyone on site
was properly educated in the use of the Language. What if the "Installation
Standards" evolved from basic guidelines laid down by the wise, through the
consensus of the people working in the place. Just suppose we treated people
as intelligent, responsible, creative, programmers who were capable of doing
the job, instead of half crazy malcontents whose sole purpose in life is to
disrupt and destroy the business and who should be kept away from sharp
objects and allowed to write cobol on big sheets of paper in non-joined-up
writing, by means of a crayon....

But what about  "ease of maintenance"?! We can't have everybody just doing
their own thing...

 Well, see, I'm not persuaded that such a loose installation would have
difficulty with that. It doesn't necessarily follow that because anything is
allowed, people will deliberately write esoteric code. Especially not if
they know they are likely to have to maintain it....

I have a bit of a problem with taking tools out of the box just because
little Johnny cut his finger... My approach would be to explain to Johnny
that certain tools must be respected, not because they are inherently
dangerous, but because they are powerful... "If you hold the chisel like
this, Johhny, you CAN'T cut your fingers...".

Over the years I have been responsible for writing Programming Standards on
so many sites I have lost track of them. When I first started doing this I
tended to be pretty strict about all the usual things although I never
really liked the idea of "banning" a construct. My feeling was (and still
is) that if the construct is in the Language, it must be there for a reason.
Part of the joy of COBOL programming is that there are MANY ways to skin
cats... some people search tables with an iterative subscript, some use
indexes, some use SEARCH...who is right?

All of them, if the process returns the correct table entry.

I have worked on sites where PERFORM...VARYING was "banned" (too complex),
SEARCH was banned (too modern and nobody understood it), EVALUATE was banned
(Why not just use IF?)... and so on. Sites where IFs must not be negated
(Too confusing ?!) and the TRUE branch must be positive. (So, instead of  IF
NOT NUMERIC...DO SOMETHING  we got: IF NUMERIC ... DON'T Do SOMETHING (or
"CONTINUE" ...Man, that phrase has a lot to answer for...<G>)...ELSE... DO
SOMETHING... and so on. A number of people here have argued that the
installation standards must be complied with... hands up those who would
comply with all of the above?

(I didn't. I got the Standards changed...Lunchtime sessions on "Advanced
Programming"... Once they realised that nested IFs are not going to bring
about the downfall of the Western World (provided you nest them properly)
and that PERFORM ...VARYING can save a lot of wheels within wheels... and
Boolean Operators (AND, OR and NOT) don't have to make IF Statements
unreadable, there was no stopping them.<G>)

I guess the real point is that we shouldn't "prohibit" the use of certain
constructs just because we personally don't like them. I don't currently use
EXIT PERFORM or EXIT SECTION but I wouldn't mind betting that I will once
they are generally available... And I will gladly maintain someone else's
code that uses them (whether I personally approve or not). That's why I call
myself a programmer; I understand programming. I have opinions about it, but
I would never enforce those opinions on anyone else by writing restrictive
standards. (Instead I just try and persuade people through forums like
this...<G>) As I said before, it is only Computer Programming. Not Life and
Death.

Summing up, I believe it is better not to stifle the creativity of
individuals even if this means some of the code may be a bit "strange".
That's why you're a programmer...it's your job to understand it.

If we extended this argument to the construction industry, nobody would use
power tools because someone once lost his finger with a bandsaw, or someone
once shot a rivet through his hand. It is a stupid argument to blame the
tools; educate the user of the tools...

And "discourage for the following reasons" or "avoid because" but DON'T
"prohibit" ...(You can legitimately ask someone to justify why they used
certain constructs if you really believe the code is bad; that's not the
same as "banning" stuff...)

Pete.

Stephen J Spiro <stephenjspiro@mail.com> wrote in message
news:928495c6.0203172202.489f8028@posting.google.com...
> My own general rule is that I never want an "escape" from a paragraph
> unless I want to force an ABEND.
…[15 more quoted lines elided]…
> Stephen J Spiro



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2002-03-18T10:17:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a750e4$e5q$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com>`

```
In article <3c95f7cb_2@Usenet.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>Stephen,
>
…[14 more quoted lines elided]…
>than your peers and so rely on your advice...)

My take on Mr Spiro's comments was a bit different... I saw him making the 
leap from 'My own general rule is that I never want an "escape" from a 
paragraph unless I want to force an ABEND' to 'I will do my best to make 
my own general rule mandatory for everyone else at sites over which I have 
any influence', a variation of 'I don't like/understand it so nobody 
should do it'.

>
>Even leaving that aside, here's a different aspect on how we might deal with
…[3 more quoted lines elided]…
>broken arm from a nested IF?  It is computer code for Chrissake! )

Here, too, I must disagree... nobody might be hospitalised by an Altered 
GO TO but someone might miss getting to a hospital in a timely manner 
because of one.

Years ago I worked with a fellow in Manhattan - Al Herman, may he sleep 
with the angels - who worked on the first citywide Emergency Dispatching 
System (the 911 system, in England I think they use 999).  He said 
something like:

'After working on that I swore off, I promised myself that I'd only work 
on financial systems.  You screw up on 911 dispatching and an ambulance 
gets sent to the wrong address and somebody with a heart attack dies.  You 
screw up on a financial system and the worst thing that'll happen is that 
someone'll lose money.

'Now they might want you to *think* that's just as bad but let me tell 
you... it's only money, losing money ain't no freakin' heart attack.'

[snippette]

>As I said before, it is only Computer Programming. Not Life and
>Death.

As pointed out above... Computer Programming can well spell Life or Death.

DD

>Stephen J Spiro <stephenjspiro@mail.com> wrote in message
>news:928495c6.0203172202.489f8028@posting.google.com...
…[25 more quoted lines elided]…
>                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-19T10:31:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c975e8d_10@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:a750e4$e5q$1@panix1.panix.com...
> In article <3c95f7cb_2@Usenet.com>,
>
…[3 more quoted lines elided]…
>
When I wrote this I KNEW that someone would bring up critical applications
where computers DO mean Life and Death. (I didn't think it would be you,
Doc, because I figured you'd catch my drift...<G>)

Yes, There ARE systems where people's lives depend on computer code.
Hospitals, the Space Program, everyday commercial and military aircraft.

However, there are three reasons why I believe these can be excluded from
the argument regarding the relative importance of COBOL programming:

1. Life critical systems are usually not written in COBOL. Even when they
are, they are written and tested to destruction.  (See point 2).

2. Life critical systems are written and tested to destruction before being
released. Furthermore, the criteria for development are NOT the same as
those we use when developing commercial systems. (see below).

3. The number of COBOL programmers in this forum who have worked on Life
Critical systems is minute, in comparison to the ones who haven't. (this is
really a restatement of point 1 above). As I wish to address my comments and
observations to the widest, rather than the narrowest audience, I am
addressing the majority when I say COBOL programming is NOT Life and Death.
(Maybe I should qualify that to be "In MOST cases, COBOL programming is NOT
Life and Death"? But you know how I hate wishy washy statements...<G>)

> Years ago I worked with a fellow in Manhattan - Al Herman, may he sleep
> with the angels - who worked on the first citywide Emergency Dispatching
…[11 more quoted lines elided]…
>
He is absolutely right and I feel the same way. However, I have worked on
one Life Critical system in my career (it was for Auckland Hospital) and I
took EXTREME care to ensure that that everything was tested and re-tested.
(Even more than I always do...<G>) I figured it could be my life that
depended on it sometime so it had to be the best I could do...<G>) Oddly
enough, considerations like programming style didn't come into it. It simply
had to be unbreakable and correct. I believe that the three of us who worked
on that project realised how serious it was and we were much more concerned
with ensuring that the correct functionality was in place than we were with
whether SECTIONs were performed or paragraphs... Criteria change when the
goal changes.

> [snippette]
>
…[4 more quoted lines elided]…
>
Yes, Doc, I concede that. However, it does not do so for the majority of
COBOL programmers employed in developing commercial applications. To act as
though it does, is simply pretentious and stupid.

Every year we have a Religious War here over SECTIONs. While lively debate
is a good thing, to re-iterate the same arguments is simply boring. The
intensity and depth of feeling about this is staggering to me. I believe
that perspective has been lost, and that's what prompted my comment.

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** "Paul Raulerson" <praulerson@NOSPAM-hot.rr.com>
- **Date:** 2002-03-19T16:17:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PwJl8.26385$Vl.1489662@typhoon.austin.rr.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com> <3c975e8d_10@Usenet.com>`

```
<grin> Who said anything about critical embedded systems?
What if the ambulance driver's paycheck doesn't get printed,
or worse yet, is direct deposited to the wrong place?

Of the right part to fix the ambulance isn't available because of
computer problems? :)

I'm being a little ridiculous of course, but we live in a very
interconnected world.
Things can sometimes fall apart for the simplest and most innocent reasons.

And on this subject - structured COBOL programming without the use of GOTO's
and so on (which, by the way, are often included not because they are the
best way
to program something, but just to prove that the programmer is 'good
enough'... (*sigh*))
has been around a long time now, and it works. Further, it works better than
unstructured programming in COBOL. If you need to use GOTO's - you probably
should
be coding in assembler.

I think it would be a really nice thing to remove ALTER and GOTO from the
language spec myself.
Heck, with the advent of USAGE IS POINTER and ADDRESS OF and PROCEDURE
POINTERs
who needs them anyway?
-Paul


"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3c975e8d_10@Usenet.com...
>
> <docdwarf@panix.com> wrote in message
news:a750e4$e5q$1@panix1.panix.com...
> > In article <3c95f7cb_2@Usenet.com>,
> >
…[17 more quoted lines elided]…
> 2. Life critical systems are written and tested to destruction before
being
> released. Furthermore, the criteria for development are NOT the same as
> those we use when developing commercial systems. (see below).
>
> 3. The number of COBOL programmers in this forum who have worked on Life
> Critical systems is minute, in comparison to the ones who haven't. (this
is
> really a restatement of point 1 above). As I wish to address my comments
and
> observations to the widest, rather than the narrowest audience, I am
> addressing the majority when I say COBOL programming is NOT Life and
Death.
> (Maybe I should qualify that to be "In MOST cases, COBOL programming is
NOT
> Life and Death"? But you know how I hate wishy washy statements...<G>)
>
…[7 more quoted lines elided]…
> > gets sent to the wrong address and somebody with a heart attack dies.
You
> > screw up on a financial system and the worst thing that'll happen is
that
> > someone'll lose money.
> >
…[8 more quoted lines elided]…
> enough, considerations like programming style didn't come into it. It
simply
> had to be unbreakable and correct. I believe that the three of us who
worked
> on that project realised how serious it was and we were much more
concerned
> with ensuring that the correct functionality was in place than we were
with
> whether SECTIONs were performed or paragraphs... Criteria change when the
> goal changes.
…[6 more quoted lines elided]…
> > As pointed out above... Computer Programming can well spell Life or
Death.
> >
> Yes, Doc, I concede that. However, it does not do so for the majority of
> COBOL programmers employed in developing commercial applications. To act
as
> though it does, is simply pretentious and stupid.
>
…[13 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2002-03-19T11:45:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a77pvh$djm$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com> <3c975e8d_10@Usenet.com>`

```
In article <3c975e8d_10@Usenet.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:a750e4$e5q$1@panix1.panix.com...
…[7 more quoted lines elided]…
>where computers DO mean Life and Death.

Wow... what a talent for Predicting the Future!  Maybe you should give up 
coding and make your living doing stock-market trades!

>(I didn't think it would be you,
>Doc, because I figured you'd catch my drift...<G>)

Ummmmmm... cancel that stock-market suggestion, then.

[snippage]

>As I wish to address my comments and
>observations to the widest, rather than the narrowest audience, I am
>addressing the majority when I say COBOL programming is NOT Life and Death.

With all due respect, Mr Dashwood, your original assertion was about 
'computer programming', not COBOL programming.

>(Maybe I should qualify that to be "In MOST cases, COBOL programming is NOT
>Life and Death"? But you know how I hate wishy washy statements...<G>)

Maybe I do... maybe I don't.  Let me think about it.

>
>> Years ago I worked with a fellow in Manhattan - Al Herman, may he sleep
…[13 more quoted lines elided]…
>He is absolutely right and I feel the same way.

Hmmmmm... the fact that you feel the same way has *nothing* to do with his 
absolute rightness... right?

[snippissmus]

>> [snippette]
>>
…[5 more quoted lines elided]…
>Yes, Doc, I concede that.

Fair enough... in fact, any more fair and it would sunburn easily.

>However, it does not do so for the majority of
>COBOL programmers employed in developing commercial applications. To act as
>though it does, is simply pretentious and stupid.

I can absolutely and categorically declare... yes and no.  On the one hand 
Sun T'zu tells us 'If you keep on fighting - even if you are winning - 
your edges will become blunted' (continuous expenditure of energy degrades 
performance), on the other hand... how does one prepare for the Real Deal 
except by practising during times of UnReality?  An example I have used 
before:

I was taught, long ago, that one should think out one's actions and put as 
much into an ISPF command-line as possible before pressing Enter because 
my terminal was in one place and the mainframe was thousands of miles 
away... and every time I hit Enter I would incur communications lags and 
expenses.  To this day I will, at the drop of a hat, pound out lines 
like...

=2;;s c2;c prognam1 prognam2 all;sub;;can;split;isdf da;pre myuid*

... even though The Iron is just on the other side of the wall.  

Is this overkill?  Of course not... but only because *I* do it, naturally.  
To bench-check code for hours because you have only two compiles per day?  
Now *that's* overkill... because I *don't* do it.

As the Germans used to say... 'In media felicitas est'.

DD
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-03-19T21:56:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c97b2b8.2828206@news.epix.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com> <3c975e8d_10@Usenet.com>`

```
Peter:

One of our US customers uses Micro Focus COBOL, COBOL sp2, FormPrint
and Thin Client for an Enhanced 911 dispatch system.

For those of you who are not so familiar with E-911 systems, they are
used by emergency services workers who dispatch emergency services
workers (police, firefighters and ambulance personnel).

The system has been running for many years and operates works great!



"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

>
><docdwarf@panix.com> wrote in message news:a750e4$e5q$1@panix1.panix.com...
…[81 more quoted lines elided]…
>                http://www.usenet.com


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-20T12:02:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c97d67c_11@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com> <3c975e8d_10@Usenet.com> <3c97b2b8.2828206@news.epix.net>`

```

Bob Wolfe <rtwolfe@flexus.com> wrote in message
news:3c97b2b8.2828206@news.epix.net...
> Peter:
>
…[8 more quoted lines elided]…
>
I'm pleased to hear it Bob, and I don't mind you hijacking my argument for a
shameless plug...<G>

So that's ONE.

How many customers do you have who are not connected with Life Critical
systems?

(It's rhetorical...)

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-18T15:12:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203181512.56fa7e83@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<a750e4$e5q$1@panix1.panix.com>...
> In article <3c95f7cb_2@Usenet.com>,
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:

<SNIP>

> >It's like saying, "Well, I couldn't persuade my peers, but I'll damn well
> >persuade my customers..." (presumably the customers are less well informed
…[7 more quoted lines elided]…
> should do it'.
 
I UNDERSTAND it perfectly well. That is WHY I don't like it, and why
nobody should do it.

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2002-03-18T20:51:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a765jq$pt1$1@panix1.panix.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <3c95f7cb_2@Usenet.com> <a750e4$e5q$1@panix1.panix.com> <928495c6.0203181512.56fa7e83@posting.google.com>`

```
In article <928495c6.0203181512.56fa7e83@posting.google.com>,
Stephen J Spiro <stephenjspiro@mail.com> wrote:
>docdwarf@panix.com wrote in message news:<a750e4$e5q$1@panix1.panix.com>...
>> In article <3c95f7cb_2@Usenet.com>,
…[16 more quoted lines elided]…
>nobody should do it.

Of course, Mr Spiro... based on *your* understandings and likes 
everybody/nobody should do things in a particular way.

There's a fellow who posts here who shares what seems to be a similar 
outlook... have you ever met Mr Dilworth?

DD
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2002-03-18T15:01:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C9655A4.3903D1C@mb.sympatico.ca>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:

> Stephen,
>
…[6 more quoted lines elided]…
> <snip>

> What if, instead of imposing constraints and forcing a given style of
> programming, we actually gave guidelines, but encouraged people to develop
…[10 more quoted lines elided]…
>

<snip>

Peter, if you ever want to run for king, let me know,because I'll vote for you
as often as I can.  Your message is the essence of common sense.  It doesn't
really matter WHAT language constructs are used: if the program is properly
planned, it will work and be maintable forever.

Peter Lacey
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-19T10:33:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c975e8f_10@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <3C9655A4.3903D1C@mb.sympatico.ca>`

```
Thanks for the encouragement, Peter.

I can't run for King because the Doc already occupies that position...<G>

Pete.

Peter Lacey <lacey@mb.sympatico.ca> wrote in message
news:3C9655A4.3903D1C@mb.sympatico.ca...
> "Peter E. C. Dashwood" wrote:
>
> > Stephen,
> >
> > I understand your arguments and the feelings behind them. As I have no
real
> > problem with what you wrote (neither strongly agree nor disagree),
normally
> > I wouldn't comment. But there is one thing that worries me a lot...
> >
…[5 more quoted lines elided]…
> > programming, we actually gave guidelines, but encouraged people to
develop
> > their own style of programming? The prime criterion being simply that
the
> > program should work correctly. And then we saw to it that everyone on
site
> > was properly educated in the use of the Language. What if the
"Installation
> > Standards" evolved from basic guidelines laid down by the wise, through
the
> > consensus of the people working in the place. Just suppose we treated
people
> > as intelligent, responsible, creative, programmers who were capable of
doing
> > the job, instead of half crazy malcontents whose sole purpose in life is
to
> > disrupt and destroy the business and who should be kept away from sharp
> > objects and allowed to write cobol on big sheets of paper in
non-joined-up
> > writing, by means of a crayon....
> >
…[3 more quoted lines elided]…
> Peter, if you ever want to run for king, let me know,because I'll vote for
you
> as often as I can.  Your message is the essence of common sense.  It
doesn't
> really matter WHAT language constructs are used: if the program is
properly
> planned, it will work and be maintable forever.
>
> Peter Lacey
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 6)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-18T15:08:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203181508.1e349695@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3c95f7cb_2@Usenet.com>...
> Stephen,
> 
…[10 more quoted lines elided]…
> decision of the committee?


Not senseless at all. It is done all the time.  Many shops have
PROHIBITED the use of ALTERed GO TOs for many years.  Many shops have
prohibited the use of simple  GO TO for many years. In fact, on the
mainframe, there are tools which work with the compiler  to flag an
assortment of "legal" syntax which violates company standards.


> It's like saying, "Well, I couldn't persuade my peers, but I'll damn well
> persuade my customers..." (presumably the customers are less well informed
> than your peers and so rely on your advice...)


My clients are interested in having maintainable code.  There are few
members of J4 who make their livings writing application programs. 
There are people on the committee whose knowledge of COBOL awes me. 
But I would not hire some of them to write application programs
because I have heard them describe their styles.  And I consider it
unmaintainable garbage in some of their cases.


> Even leaving that aside, here's a different aspect on how we might deal with
> "troublesome" or "dangerous" constructs (Ooooooohhhh)...(I'm really getting
> tired of people saying certain constructs or styles of coding are
> "dangerous"... when was someone hospitalised by an Altered GO TO? Who got a
> broken arm from a nested IF?  It is computer code for Chrissake! )

Ummm, see the posting about the Emergency response system.

> 
> What if, instead of "prohibiting", "forbidding", "banning", or generally
> disallowing certain constructs, we actually banned NOTHING (not even ALTER
> <ARRRGHHH! Shock! Heresy!>), but instead we educated people in the way to
> use these things?


This is NOT the way J4 does it; the following list specifies items
dropped from the new standard (they will now be PROHIBITED):

Obsolete elements. The following features that were classified as
obsolete in the previous COBOL standard,
have been removed from this draft International Standard:
ï¿½ Double character substitution
ï¿½ ALL literal and numeric or numeric edited item (association of a
multi-character ALL literal with a numeric
or numeric-edited data item)
ï¿½ AUTHOR, INSTALLATION, DATE-WRITTEN, DATE-COMPILED, and SECURITY
paragraphs
ï¿½ MEMORY SIZE clause
ï¿½ RERUN clause
ï¿½ MULTIPLE FILE TAPE clause
ï¿½ LABEL RECORDS clause
ï¿½ VALUE OF clause
ï¿½ DATA RECORDS clause
ï¿½ ALTER statement
ï¿½ KEY phrase of the DISABLE statement
ï¿½ KEY phrase of the ENABLE statement
ï¿½ ENTER statement
ï¿½ The optionality of procedure-name-1 in GO TO statement  
ï¿½ REVERSED phrase of the OPEN statement
ï¿½ STOP literal statement
ï¿½ Segmentation module
ï¿½ Debug module 


> What if we actually called ourselves "programmers" and made it our business
> to understand "programming"?
…[3 more quoted lines elided]…
> their own style of programming? 

Formula for disaster!  Maintenance nightmare!

>The prime criterion being simply that the
> program should work correctly. And then we saw to it that everyone on site
…[7 more quoted lines elided]…
> writing, by means of a crayon....

CREATIVE? I've had to do maintainance on programs written by
"creative" programmers. Formula for disaster!

> 
> But what about  "ease of maintenance"?! We can't have everybody just doing
…[5 more quoted lines elided]…
> they know they are likely to have to maintain it....

Of course they will -- and do.  THEY know their little tricks, they
usually CAN maintain them.  The less qualified ones do it on purpose,
as "job security".

> 
> I have a bit of a problem with taking tools out of the box just because
…[3 more quoted lines elided]…
> this, Johhny, you CAN'T cut your fingers...".

Your sarcasm does not contribute to the discussion.

> Over the years I have been responsible for writing Programming Standards on
> so many sites I have lost track of them. When I first started doing this I
…[7 more quoted lines elided]…
> All of them, if the process returns the correct table entry.

WRONG! I, and many of my colleagues, have made a nice dollar or two
doing performance tuning:  Going into programs which produced correct
output, but which used too much storage, or ran too long.  In order to
be useful, information must be timely as well as accurate, and the
cost of retrieving it must be appropriate to its usefulness.

> 
> I have worked on sites where PERFORM...VARYING was "banned" (too complex),
…[7 more quoted lines elided]…
> comply with all of the above?

Yup, there are a lot of wrong reasons for making standards.  This does
not mean that there are no GOOD reasons for making standards.

> 
> (I didn't. I got the Standards changed...Lunchtime sessions on "Advanced
…[15 more quoted lines elided]…
> Death.

I will also gladly maintain someone else's code that uses all manner
of awful constructions, and my clients will pay a lot of money for me
to do it.  It will have been cheaper for them to have adopted my
standards in the first place.

> Summing up, I believe it is better not to stifle the creativity of
> individuals even if this means some of the code may be a bit "strange".
> That's why you're a programmer...it's your job to understand it.

That's why I'm a CONSULTANT. The programmer's job was to do it right
the first time.

> 
> If we extended this argument to the construction industry, nobody would use
…[3 more quoted lines elided]…
> 

Wrong straw men, intellectually dishonest.
The construction industry (at least in the USA) is one of the most
standardized industries in the country.  For instance: Windows in a
residential building MUST be certain specified sizes, FOR EASE OF
MAINTAINANCE. I once replaced a window in an old building, which was
NOT a standard size.  I spent four times longer than I otherwise would
have, because I had to build out the frame to fit a standard window.
(I COULD Have had a window made to order, but that would have cost
more than my budget.)  Pipes are standard sizes, fucking flat-head
screws are standard sizes! Everything is standard size or technique or
composition, and if you do "get creative", the building inspector will
tell you to rip it out and do it over.


> And "discourage for the following reasons" or "avoid because" but DON'T
> "prohibit" ...(You can legitimately ask someone to justify why they used
…[32 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-18T18:49:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7623f$7p6$1@slb5.atl.mindspring.net>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <928495c6.0203181508.1e349695@posting.google.com>`

```
Stephen,

Where did you get this "view" of what OBSOLETE means?

>
> This is NOT the way J4 does it; the following list specifies items
…[4 more quoted lines elided]…
> have been removed from this draft International Standard:

What it MEANS is that it won't be part of the new Standard.  There is
NOTHING that prohibits vendors from continuing to support any, all, or none
of the items in the OBSOLETE (in '85 Standard) items - once (if) they
implement a 200x product.
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 8)_

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2002-03-22T22:19:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0203222219.79d6b2ab@posting.google.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <928495c6.0203181508.1e349695@posting.google.com> <a7623f$7p6$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<a7623f$7p6$1@slb5.atl.mindspring.net>...
> Stephen,
> 
…[13 more quoted lines elided]…
> implement a 200x product.

Bill,
I'm sorry, I forgot you don't do Rhetoric, only Literal.

I've been on J4 long enough to know exactly what OBSOLETE means.  The
intention of the post was to say that once a fature is no longer in a
compiler ("implementation"), the inability to make use of the feature
is the existential equivalent of a PROHIBITION.  The implementation
will not "allow" the program to compile successfully.

Dropping features from the standard usually means they will eventually
be dropped from the commercial implementations.

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: Sections

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-20T03:25:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c975e95_10@Usenet.com>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be> <AyPk8.15603$Ex5.1394656@bgtnsc04-news.ops.worldnet.att.net> <3C94B65A.1470082D@Azonic.co.nz> <N95l8.17036$Ex5.1531690@bgtnsc04-news.ops.worldnet.att.net> <928495c6.0203172202.489f8028@posting.google.com> <3c95f7cb_2@Usenet.com> <928495c6.0203181508.1e349695@posting.google.com>`

```

Stephen J Spiro <stephenjspiro@mail.com> wrote in message
news:928495c6.0203181508.1e349695@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3c95f7cb_2@Usenet.com>...
> >
> > Does it not strike you as kind of senseless to spend time on J4 arguing
for
> > (or against) constructs that you (or someone else) then intend to
> > "prohibit"? If you argued against certain constructs and were overruled,
…[4 more quoted lines elided]…
> Not senseless at all. It is done all the time.

So it isn't senseless because it is done all the time? That's like saying
that wearing large trousers makes you fat.

> Many shops have
> PROHIBITED the use of ALTERed GO TOs for many years.  Many shops have
> prohibited the use of simple  GO TO for many years.

That is precisely the action that I questioned in my post. Just stating that
it is so doesn't address the value of it.

> In fact, on the
> mainframe, there are tools which work with the compiler  to flag an
> assortment of "legal" syntax which violates company standards.
>

Oh Man, I can't wait to work on a site like that...<G> (THAT was
sarcasm...when I use it it is called "irony"<G>. You accused me of it when I
wasn't guilty...)

This is exactly what I was getting at, Stephen. You can treat people as
idiots who are out to destroy the Company and must be controlled at all
costs, or you can take a more positive view. As I have spent the last 15
years of my life managing people who were sometimes much smarter than me, I
have learned that "Management" is not just about control. It is about
chanelling and stimulating and supporting as well. Laying down rigid rules
based on one person's view, is NOT the way to get the best from programmers.
(Or anybody else, as it happens...).


>
> > It's like saying, "Well, I couldn't persuade my peers, but I'll damn
well
> > persuade my customers..." (presumably the customers are less well
informed
> > than your peers and so rely on your advice...)
>
…[7 more quoted lines elided]…
>

Fair enough. I'm sure they speak very highly of you too...<G>.

The flaw in the argument here is that you are arguing that your customers
can only obtain "maintainable code" by enforcing prohibitions in the use of
COBOL.

I refute that. I also vehemently refute the proposition that, as it is done
that way and has been for years, it must be the ONLY successful approach.(I
know from experience that is NOT the only way; in fact, it isn't even a GOOD
way...It just makes some people feel good to think they're in control.)
>
> > Even leaving that aside, here's a different aspect on how we might deal
with
> > "troublesome" or "dangerous" constructs (Ooooooohhhh)...(I'm really
getting
> > tired of people saying certain constructs or styles of coding are
> > "dangerous"... when was someone hospitalised by an Altered GO TO? Who
got a
> > broken arm from a nested IF?  It is computer code for Chrissake! )
>
> Ummm, see the posting about the Emergency response system.
>

Ummm, see my response to it. <G>


> >
> > What if, instead of "prohibiting", "forbidding", "banning", or generally
> > disallowing certain constructs, we actually banned NOTHING (not even
ALTER
> > <ARRRGHHH! Shock! Heresy!>), but instead we educated people in the way
to
> > use these things?
>
…[3 more quoted lines elided]…
>
<snipped list>

I see that as a sad reflection on J4, but then, I would say that...<G>. To
be fair to them, they are probably only implementing what they see as the
Customer's wishes. I just think there is a better way...it involves
education rather than prohibition.


> Obsolete elements. The following features that were classified as
> obsolete in the previous COBOL standard,
…[6 more quoted lines elided]…
> paragraphs

Now, what Harm did these (above) constructs ever do? I mean they're not
exactly critical, are they?

> - MEMORY SIZE clause
> - RERUN clause
…[13 more quoted lines elided]…
>

Ah, so many old friends...like scales falling off the dinosaur as it sinks
into the tar pit... There goes STOP LITERAL... we used to scare the Bejeezus
out of Console Operators with that one... LABEL RECORDS OMITTED for print
files...(A quick way to identify them)... ENTER PLAN (on the old 1900s),
ENTER NEAT (on the NCR 315), ENTER ASM (on the Burroughs B500) .... No more
ALTERed first time switches...incredibly efficient on severely constrained
hardware...all fading into the sunset as the COBOL Language slowly gets
ground down by the people who should be protecting and treasuring it.

>
> > What if we actually called ourselves "programmers" and made it our
business
> > to understand "programming"?
> >
> > What if, instead of imposing constraints and forcing a given style of
> > programming, we actually gave guidelines, but encouraged people to
develop
> > their own style of programming?
>
> Formula for disaster!  Maintenance nightmare!
>
Yes, I should've known you'd react like that....<G>

> >The prime criterion being simply that the
> > program should work correctly. And then we saw to it that everyone on
site
> > was properly educated in the use of the Language. What if the
"Installation
> > Standards" evolved from basic guidelines laid down by the wise, through
the
> > consensus of the people working in the place. Just suppose we treated
people
> > as intelligent, responsible, creative, programmers who were capable of
doing
> > the job, instead of half crazy malcontents whose sole purpose in life is
to
> > disrupt and destroy the business and who should be kept away from sharp
> > objects and allowed to write cobol on big sheets of paper in
non-joined-up
> > writing, by means of a crayon....
>
> CREATIVE? I've had to do maintainance on programs written by
> "creative" programmers. Formula for disaster!
>
I've had to do it on programs written by people with very little
imagination, having had it knocked out of them by a restrictive set of
installation standards...

Here's a "Formula for disaster":   Repressive Control freak Management + low
expectation of staff + "It's our Policy" = high staff turnover + low morale
+ achievement of expectation.

> >
> > But what about  "ease of maintenance"?! We can't have everybody just
doing
> > their own thing...
> >
> >  Well, see, I'm not persuaded that such a loose installation would have
> > difficulty with that. It doesn't necessarily follow that because
anything is
> > allowed, people will deliberately write esoteric code. Especially not if
> > they know they are likely to have to maintain it....
…[4 more quoted lines elided]…
>
There's no "Us" and "Them" at your place, right Stephen <G>?

And why would a highly experienced professional consultant like yourself be
intimidated by the "less qualified ones"?

Another way to interpret the above could be: "Stomp on the SmartArses
because we don't really understand what they're doing..."   As a
professional programmer I would make it my business to understand what they
were doing. Maybe we could all learn something. Then we could amend the
Standards in the light of our new knowledge...

> >
> > I have a bit of a problem with taking tools out of the box just because
> > little Johnny cut his finger... My approach would be to explain to
Johnny
> > that certain tools must be respected, not because they are inherently
> > dangerous, but because they are powerful... "If you hold the chisel like
> > this, Johhny, you CAN'T cut your fingers...".
>
> Your sarcasm does not contribute to the discussion.

Hey! That was NOT sarcasm! I meant every word of it and it was intended as
one of my usual colourful analogies <G>.

Besides, even if it HAD been sarcasm it DOES contribute to the discussion.
It contributes by supporting the point of view that what one person
considers to be dangerous and should be locked away, may be considered as a
useful tool that simply needs a little training with, to another person.
(OK, it was a terrible sentence structure, but you know what I'm
saying...<G>)
>
> > Over the years I have been responsible for writing Programming Standards
on
> > so many sites I have lost track of them. When I first started doing this
I
> > tended to be pretty strict about all the usual things although I never
> > really liked the idea of "banning" a construct. My feeling was (and
still
> > is) that if the construct is in the Language, it must be there for a
reason.
> > Part of the joy of COBOL programming is that there are MANY ways to skin
> > cats... some people search tables with an iterative subscript, some use
…[4 more quoted lines elided]…
> WRONG!

So, in Spiroville it is RIGHT if it returns the WRONG table entry?! I'm
beginning to see how you could have trouble with other people's code...(Most
of us have a different concept of what constitutes correct processing...<G>
[sorry, that was almost irony...<G>])

> I, and many of my colleagues, have made a nice dollar or two
> doing performance tuning:  Going into programs which produced correct
> output, but which used too much storage, or ran too long.

Was that on sites where they banned certain COBOL so that only a subset of
the Language could be used <G>?

Did you maintain the installation standards when you "improved" it?

(Don't answer that, it is a loaded question...If you say, "YES" then it is
apparent that you didn't do anything the people themselves couldn't have
done, because you were working with the same toolset. They just paid for
their lack of experience (or stifled creativity...<G>).

If you say "NO" then you are refuting your own argument for banning certain
constructs; you don't adhere to it yourself.)

This was really a very unworthy rhetorical device on my part and I am truly
ashamed I resorted to it...(takes another shot of Jack and conscience goes
and lies in the corner...)

> In order to
> be useful, information must be timely as well as accurate, and the
> cost of retrieving it must be appropriate to its usefulness.
>
Yes, that is a fair statement. but some aspects of it are more important
than others. Accuracy, is a higher priority than timeliness although both
play a part, as you observed.

Making information timely does not necessarily make it useful (see analogy
with large trousers and fat people, above). For example, if we consider the
piece of information: "Japanese Gentlemen like to be slapped on the head,
and that is why they incline their heads to you when they meet you.", it
really doesn't matter whether you receive this information before or after
your trip to Japan. As it is plain wrong, it is of no value irrespective of
its timeliness.

On the other hand, the piece of information: "In Japanese culture it is not
polite to yell "Banzai!" when drinking saki: the correct toast is
"Kampai!"", then the timeliness of this piece of information definitely
affects its value. (It is of much less value to find this out when you
return from your trip to Japan, having yelled "Banzai!" every time they
raised the little saki cups...)

Marshall MacLuhan (the founder of  Information Theory) said something along
the lines that information has value according to its unexpectedness. (He is
also famous for saying that "the media IS the message"). I guess I must've
looked at some very valuable memory dumps in my time because I've seen my
share of unexpectedness in them...<G>
> >
> > I have worked on sites where PERFORM...VARYING was "banned" (too
complex),
> > SEARCH was banned (too modern and nobody understood it), EVALUATE was
banned
> > (Why not just use IF?)... and so on. Sites where IFs must not be negated
> > (Too confusing ?!) and the TRUE branch must be positive. (So, instead of
IF
> > NOT NUMERIC...DO SOMETHING  we got: IF NUMERIC ... DON'T Do SOMETHING
(or
> > "CONTINUE" ...Man, that phrase has a lot to answer for...<G>)...ELSE...
DO
> > SOMETHING... and so on. A number of people here have argued that the
> > installation standards must be complied with... hands up those who would
…[4 more quoted lines elided]…
>
The question of having standards is not in dispute here. I worked in a time
when there weren't any, and I work in the modern world too. Standards are
essential. (It is the understanding of this that gets me SO mad at J4...)
What I think we are debating is what should BE in the standards. I don't
want prohibitions and vetos (any more than I approve of having censorship in
movies and newspapers), but I also accept that my requirements only work if
people are adult and responsible. Experience has shown that most computer
programmers are pretty bright, intelligent, people. I reckon it is better to
stimulate and encourage them than it is to suppress and limit them. That is
really the nub of my argument here.

>
> I will also gladly maintain someone else's code that uses all manner
…[3 more quoted lines elided]…
>

No comment....

> > Summing up, I believe it is better not to stifle the creativity of
> > individuals even if this means some of the code may be a bit "strange".
…[4 more quoted lines elided]…
>
LOL! So those who can't do it right first time become consultants...<G>? I'm
more of an "Insultant" myself... I reckon a dose of healthy abuse is
beneficial for some Managers...(The repressive control freaks for a
start...<G>)

> >
> > If we extended this argument to the construction industry, nobody would
use
> > power tools because someone once lost his finger with a bandsaw, or
someone
> > once shot a rivet through his hand. It is a stupid argument to blame the
> > tools; educate the user of the tools...
> >
>
> Wrong straw men, intellectually dishonest.

Dishonest?! Moi?! Never!!!

> The construction industry (at least in the USA) is one of the most
> standardized industries in the country.  For instance: Windows in a
…[8 more quoted lines elided]…
> tell you to rip it out and do it over.

All fine as far as it goes, but I was talking abut the use of TOOLS, not
STANDARDS...

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Sections

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-03-18T14:57:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a74v0p$jd2$1@peabody.colorado.edu>`
- **References:** `<3c931758$0$29682$ba620e4c@news.skynet.be>`

```

On 16-Mar-2002, "Eddy Scheire" <fa099784@skynet.be> wrote:

> I mean why should one use sections? To me it looks like unnecessary code.

Sections started off in the days when you didn't have much memory - you
could segment memory via sections.  For a long time, sort procedures had to
be sections, but not anymore.

Some places made sections their standard, but if they do, they probably GO
TO EXIT logic.   European companies are more likely to use sections than
American companies.

I don't care for GO TO EXIT logic, PERFORM THRU, nor sections.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
