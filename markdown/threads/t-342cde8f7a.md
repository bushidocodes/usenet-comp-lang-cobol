[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# question

_25 messages · 13 participants · 2002-01_

---

### question

- **From:** "M turner" <miturner70@hotmail.com>
- **Date:** 2002-01-09T02:52:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```
I have an output field with a pic x(8) value.  I need to find the best way
to check the 7th or 8th character by itself to see if it is a certain value.
How do i set up to do this? if you have a good idea please email to me at
miturner70@hotmail.com
```

#### ↳ Re: question

- **From:** "Rational One" <noreligion@nogod.com>
- **Date:** 2002-01-09T04:26:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```

you must be new to programming....... so here goes....

working-storage section.
01  ws-fieldname.
      03  filler     pic x(6).
      03  ws-field1    pic x.
      03  ws-field2    pic x.
procedure division.
move your-field to ws-fieldname.
if ws-field1 = "V"  next sentence
if ws-field2 = "v" next sentence.....yada yada yada
or perhaps
if ws-field1 = x"30" next sentence   if you need to look for hex 30  (zero)
for example


of course you could also make a pic x(1) field occurring 8 times and inspect
in a table
you could also just use the inspect tallying trick too




"M turner" <miturner70@hotmail.com> wrote in message
news:bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com...
> I have an output field with a pic x(8) value.  I need to find the best way
> to check the 7th or 8th character by itself to see if it is a certain
value.
> How do i set up to do this? if you have a good idea please email to me at
> miturner70@hotmail.com
>
>
```

##### ↳ ↳ Re: question

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-01-09T04:32:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net>`

```
    Wouldn't M Turner benefit more by doing his/her own homework if he/she
is truly new to programming?
```

###### ↳ ↳ ↳ Re: question

- **From:** "Rational One" <noreligion@nogod.com>
- **Date:** 2002-01-09T05:53:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hVQ_7.32575$Sf2.292887@rwcrnsc52>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com>`

```
I agree but think of this....COBOL is such an easy language to learn but
most people consider programming to be the domain of brainiacks because of
crummy undocumenting (self) languages such as "C" so we need to let the
newbees learn that COBOL is THE truly easy to learn language
try doing something simple like this in "C" ......you have to actually think
and they don't pay me enough for that

also - if "C++" is such a great language then why does it not rate an "A++"
mu ha ha ha ha ha



"Terry Heinze" <terryheinze@prodigy.net> wrote in message
news:xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com...
>     Wouldn't M Turner benefit more by doing his/her own homework if he/she
> is truly new to programming?
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-09T20:29:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c3bf699_5@Usenet.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52>`

```
Given that you are going to rob M Turner of the pleasure of finding things
out for him/herself,
and given that you are such an experienced programmer and not a learner
yourself,
and given that you describe COBOL as being easy,
Why then wouldn't you describe the simplest solution to the problem?

field (7:1)  or field (8:1)

It's called "Reference Modification". Maybe you can call on M turner and the
two of you could read the Manual a bit more?

Ah, but then I forgot... they don't pay you to think, do they <G>?

And there's no way you are going to think for free in your own time...

Pete.

Rational One <noreligion@nogod.com> wrote in message
news:hVQ_7.32575$Sf2.292887@rwcrnsc52...
> I agree but think of this....COBOL is such an easy language to learn but
> most people consider programming to be the domain of brainiacks because of
> crummy undocumenting (self) languages such as "C" so we need to let the
> newbees learn that COBOL is THE truly easy to learn language
> try doing something simple like this in "C" ......you have to actually
think
> and they don't pay me enough for that
>
> also - if "C++" is such a great language then why does it not rate an
"A++"
> mu ha ha ha ha ha
>
…[4 more quoted lines elided]…
> >     Wouldn't M Turner benefit more by doing his/her own homework if
he/she
> > is truly new to programming?
> >
…[33 more quoted lines elided]…
> > > > I have an output field with a pic x(8) value.  I need to find the
best
> > way
> > > > to check the 7th or 8th character by itself to see if it is a
certain
> > > value.
> > > > How do i set up to do this? if you have a good idea please email to
me
> > at
> > > > miturner70@hotmail.com
…[7 more quoted lines elided]…
>





 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 5)_

- **From:** Fred Snyder <fred_snyder@hotmail.com>
- **Date:** 2002-01-09T08:05:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3C4032.7C0A6B45@hotmail.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <3c3bf699_5@Usenet.com>`

```
Peter, I am suprised you were the only one to suggest that!!!! Is the quality of
COBOL programmers fading????

"Peter E. C. Dashwood" wrote:

> Given that you are going to rob M Turner of the pleasure of finding things
> out for him/herself,
…[94 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 4)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2002-01-09T14:18:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1hjfm$2et$1@ins22.netins.net>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52>`

```
I have always told my students that there are three elements to learning 
to write a program:

1.  Learn to use the compiler, linker, etc.

This is, of course, the easiest part.  It will take single lecture - with 
later followups on compiling multiple compilation units and using the 
debugger, etc.

2.  Learn the syntax

This is a bit more difficult - but with most languages haveing between 50 
and 100 keywords, it is not too difficult.  If this was all there was to 
programming, I could almost hand out a list of keywords on the first day 
of class and have a memory test on the last day.

3.  Learn to solve problems

This is the most important part.   It is why it takes two to three 
semester to adequately cover a students first language.  No employer would 
allow an employee 1-1/2 years to learn a new language.  But, if the tools 
and skills needed for problem solving are learned well (and properly) they 
provide the background needed to learn other languages relatively quickly.

In practice, at least at my institution, this means that students will 
have three semesters to learn Java and programming skills [:(].  But they 
have the File Structures (i.e. COBOL) course after having two semesters of 
Java.  During their junior or senior year they have a programming 
languages course.  One of the requirements for this course is to prepare a 
manual (20+ pages) and three hours of instruction on a language they have 
not previous seen.  Students in the class then must use these language as 
part of their final exam.  This fall, languages included APL, Prolog, and 
ADA.  Final exam questions included

	Develop a HI-LOW game in APL and ADA
	Create a sin table using the Taylor series in ADA
	Report the average of all elements in a PROLOG list

There were two or three others - I don't remember them sitting here.  But 
the point is that students have moved from having 1-1/2 years of 
instruction to having 3 hours of formal instruction in a language - and be 
able to produce working (useful ?) code.  

COBOL is easy - programming is not.  

Floyd Johnson

Rational One (noreligion@nogod.com) wrote:
: I agree but think of this....COBOL is such an easy language to learn but
: most people consider programming to be the domain of brainiacks because of
: crummy undocumenting (self) languages such as "C" so we need to let the
: newbees learn that COBOL is THE truly easy to learn language
: try doing something simple like this in "C" ......you have to actually think
: and they don't pay me enough for that

: also - if "C++" is such a great language then why does it not rate an "A++"
: mu ha ha ha ha ha



: "Terry Heinze" <terryheinze@prodigy.net> wrote in message
: news:xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com...
: >     Wouldn't M Turner benefit more by doing his/her own homework if he/she
: > is truly new to programming?
: >
: > --
: >
: > ....Terry
: > "Rational One" <noreligion@nogod.com> wrote in message
: > news:yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net...
: > >
: > > you must be new to programming....... so here goes....
: > >
: > > working-storage section.
: > > 01  ws-fieldname.
: > >       03  filler     pic x(6).
: > >       03  ws-field1    pic x.
: > >       03  ws-field2    pic x.
: > > procedure division.
: > > move your-field to ws-fieldname.
: > > if ws-field1 = "V"  next sentence
: > > if ws-field2 = "v" next sentence.....yada yada yada
: > > or perhaps
: > > if ws-field1 = x"30" next sentence   if you need to look for hex 30
: > (zero)
: > > for example
: > >
: > >
: > > of course you could also make a pic x(1) field occurring 8 times and
: > inspect
: > > in a table
: > > you could also just use the inspect tallying trick too
: > >
: > >
: > >
: > >
: > > "M turner" <miturner70@hotmail.com> wrote in message
: > > news:bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com...
: > > > I have an output field with a pic x(8) value.  I need to find the best
: > way
: > > > to check the 7th or 8th character by itself to see if it is a certain
: > > value.
: > > > How do i set up to do this? if you have a good idea please email to me
: > at
: > > > miturner70@hotmail.com
: > > >
: > > >
: > >
: > >
: >
: >
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-09T18:04:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3C8723.6A535AD3@shaw.ca>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net>`

```


Floyd Johnson wrote:

> I have always told my students that there are three elements to learning
> to write a program:
>
> 1.  Learn to use the compiler, linker, etc. <snip>

> 2.  Learn the syntax <snip>

> 3.  Learn to solve problems <snip>

As you've indicated, the real problem is the lack of time you are allowed to cover
these elements or a language. Programming is an end-tool. What really concerns me
now that the title Systems Analyst is defunct - exactly where do upcoming students
learn to design comprehensive, and truly, 'user-friendly' business applications,
before even starting to tap out code on a keyboard ?

Jimmy
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 6)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2002-01-09T19:17:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1i50i$lbm$1@ins22.netins.net>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca>`

```
Good questions.  This is the last year that we are including a systems 
analysis course in the curriculum.  Beginning next year, this course is 
being replaced by "Human-Computer Interaction".  The focus will will be 
designing I/O that will interact with the user.  Though there will be a 
unit on general design, the focus will be on I/O issues.  There is some 
instruction on program design in entry level programming courses (now 
Java, but always subject to change).  

"Computer Science" education seems to be in the midst of change.  When I 
first started teaching the general advice is to use different languages in 
different classes as appropriate (e.g. File Structures in COBOL, Graphics 
in C++, Numerical Analysis in FORTRAN, etc.).  There are some, though I am 
not sure how many, that now advocate using the same language throughout 
the curriculum.  The single exception being Programming Language.  I don't 
know how this will shake out in the future.

Floyd Johnson 

===========================================================================

James J. Gavan (jjgavan@shaw.ca) wrote:


: Floyd Johnson wrote:

: > I have always told my students that there are three elements to learning
: > to write a program:
: >
: > 1.  Learn to use the compiler, linker, etc. <snip>

: > 2.  Learn the syntax <snip>

: > 3.  Learn to solve problems <snip>

: As you've indicated, the real problem is the lack of time you are allowed to cover
: these elements or a language. Programming is an end-tool. What really concerns me
: now that the title Systems Analyst is defunct - exactly where do upcoming students
: learn to design comprehensive, and truly, 'user-friendly' business applications,
: before even starting to tap out code on a keyboard ?

: Jimmy
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-10T11:13:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c3cc51f_9@Usenet.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca>`

```

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C3C8723.6A535AD3@shaw.ca...
>
>....exactly where do upcoming students
> learn to design comprehensive, and truly, 'user-friendly' business
applications,
> before even starting to tap out code on a keyboard ?
>
It's a good point. There is a wider and wider divide between the Computer
Science and Commerce Faculties in many institutions of learning. You would
think they would be moving closer together.

We would also hope that what Floyd terms "learning to program" could be
covered without remote abstract mathematical examples. Why not real world
system examples?

But then, they can always come to CLC and see how it's REALLY done <G>...

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-10T02:11:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3CF959.33FDFD92@shaw.ca>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca> <3c3cc51f_9@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> James J. Gavan <jjgavan@shaw.ca> wrote in message
> news:3C3C8723.6A535AD3@shaw.ca...
…[15 more quoted lines elided]…
>

Pete,

You make a further good point. Within one institution the CS and Commerce
faculties should be aligned, ideally using a business model which can be used
by both faculties. Although I may not know specifics, I'm aware that B.Coms
certainly take computer courses as part of their curriculum.

So the following is food for thought for Floyd (and friends in academia).  I
most certainly am not going to detract from either Thane's (TYCI24H) or Will
Price's (EofOOC). Both are excellent and naturally to get the ideas across,
deal in modules.
What's missing is a merging of the various themes into one real-world
application.

A good example (and this is OO of course) would be the appendix in Ed
Arranga's book dealing with an in-house library application. (For Gawd's sake,
don't latch on to the ATM model that J4 and others use !). As an example this
particular application would allow introduction to design, Accept/Display, and
file handling - although data files are W/S Tables in this particular
reference.

The major stage would be a non-OO approach, introducing 3-tier systems. In
Floyd's academy, regardless of language being taught, it  could be developed
by instructors, and paralleled in each language. Of course, if somebody is
taking Java or C++ they steal a jump on COBOL because they in effect can't
work without GUIs.  For a realistic file system both these require ESQL -
meanwhile on the COBOL course, initially COBOL file handling is taught;
subsequently introduce ESQL. Certainly the same model used in several
languages is going to cause some positive reaction from students as to the
merits or demerits of the respective languages they are learning.

Logically the COBOL course should introduce OO - taking the same business
model and switching it from non-OO to OO, and a GUI tool of choice.

Meanwhile our friends in the Commerce faculty want a model that they can play
with and query. You can get them into SQL/ESQL using the same model DB to
raise queries and produce statistics.

Give it a thought Floyd - and your first hurdle will be the instructors for
the computer group.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 8)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-01-09T21:55:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ck7%7.28282$os5.2641032@news20.bellglobal.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca> <3c3cc51f_9@Usenet.com> <3C3CF959.33FDFD92@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3C3CF959.33FDFD92@shaw.ca...
>
>
…[9 more quoted lines elided]…
> > >

<big snipage>

I am reminded of a good friend, a writer with a dozen books under his belt.
We were discussing writing, and a young grad, dealing with ejection slips,
asked him how he learnt the ropes.

He said "Any idiot can learn to write.  Most have mastered it by the time
they get to high school.  What most people never master is learning WHAT to
write. The only way to do that is to write for a few years. After about
twenty, you start to get a feel for it."

I do not think you can "teach" someone to construct large systems.  You can
teach them technique, and you can teach them methodology.  However, learning
to write a large system from scratch takes practice, and I do not see how
you can possibly get that in an student capacity.  There is simply not the
time for a student to build a 25 or 30 thousand line application, and it is
all just academic until you actually roll up your sleeves and do it.  In
fact, I would venture you have not really gotten there until you have
maintained it for the first 35 or 40 users. It takes that long for reality
to rear it's ugly head.

Donald
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-10T06:05:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3D3016.66E17FDD@shaw.ca>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca> <3c3cc51f_9@Usenet.com> <3C3CF959.33FDFD92@shaw.ca> <ck7%7.28282$os5.2641032@news20.bellglobal.com>`

```


Donald Tees wrote:

> I do not think you can "teach" someone to construct large systems.  You can
> teach them technique, and you can teach them methodology.  However, learning
…[7 more quoted lines elided]…
>

Don,

Oh I agree - you can't teach systems design, as opposed to programming - only
the principles and the concept that program 'units' are part of the 'whole'. But
it is interesting to note that Floyd's school is considering User Interaction as
a topic, with the intent of making screens intuitive and full and comprehensive
validity checks - I'm guessing, but I bet that's where he is going.

Quite correctly you would need a MONSTER application to cover everything.
But at the back of my mind is Ed Arranga's Library application - it is not big
but it does lend itself to COBOL file handling and/or DBs - not too many files
or tables, incorporates things like date checks and money - related to late
fines. Further you could spin-off reports for 'Library members' or inventory
checks on books.

It represents an application which could be designed in non-OO and obviously
adapts to OO.

So now HELP WANTED - who has any ideas ?

1. I have a copy of Ed's book - but be damned if I'm going to tear the relevant
pages out of mine. I'll see if he has a spare copy.
2. Nor am I going to laboriously type it all in line by line.
3. Given that I can get a copy of the pages  - Can they be scanned so that the
images can finish up in text files, i.e. COBOL source files ?

Jimmy
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-01-09T22:18:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7l3%7.1307$97.181158@paloalto-snr1.gtei.net>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <yDP_7.9931$DG5.96158@rwcrnsc53.ops.asp.att.net> <xJP_7.3764$JH4.498062370@newssvr16.news.prodigy.com> <hVQ_7.32575$Sf2.292887@rwcrnsc52> <a1hjfm$2et$1@ins22.netins.net> <3C3C8723.6A535AD3@shaw.ca>`

```
James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C3C8723.6A535AD3@shaw.ca...
>... the title Systems Analyst is defunct - exactly where do upcoming
students
> learn to design comprehensive, and truly, 'user-friendly' business
applications,
> before even starting to tap out code on a keyboard ?

If you've ever used Microsoft Word, you already know the answer: they don't
ever learn.

MCM
```

#### ↳ Re: question

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-01-09T04:27:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wEP_7.3762$gG4.497967127@newssvr16.news.prodigy.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```
    Check the manual for the Redefines clause and read up on subscripting or
reference modification.
```

#### ↳ Re: question

- **From:** docdwarf@panix.com
- **Date:** 2002-01-09T06:14:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1h8ni$qlo$1@panix1.panix.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```
In article <bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>,
M turner <miturner70@hotmail.com> wrote:
>I have an output field with a pic x(8) value.

Please do your own homework.

DD
```

#### ↳ Re: question

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-01-09T08:16:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pkX_7.22727$os5.2278691@news20.bellglobal.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```
"M turner" <miturner70@hotmail.com> wrote in message
news:bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com...
> I have an output field with a pic x(8) value.  I need to find the best way
> to check the 7th or 8th character by itself to see if it is a certain
value.
> How do i set up to do this? if you have a good idea please email to me at
> miturner70@hotmail.com
>
>

The easiest way is with reference modification.  The 7th character of

     02 this-field    picture x(8).
is
     this-field (7:1).  Characters 5 and 6 are this-field (5:2), and so on.
```

#### ↳ Re: question

- **From:** "M turner" <miturner70@hotmail.com>
- **Date:** 2002-01-09T23:04:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com>`

```
ok to those who helped thank you, i did manage to figure it out this
afternoon at work. for those of you who think i should do my own homework, i
am not in school i am an entry level programmer/analyst working for Geico
Direct in macon, ga.  True i have no experience programming prior to this
and all they did was put me through a 14 week 'bootcamp' teaching us jcl,
endevor, xpeditor, file-aid, and cobol.  so you can see why i may have some
questions.
"M turner" <miturner70@hotmail.com> wrote in message
news:bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com...
> I have an output field with a pic x(8) value.  I need to find the best way
> to check the 7th or 8th character by itself to see if it is a certain
value.
> How do i set up to do this? if you have a good idea please email to me at
> miturner70@hotmail.com
>
>
```

##### ↳ ↳ Re: question

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-01-10T03:38:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020109223813.28515.00000571@mb-mp.aol.com>`
- **References:** `<q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>`

```
>From: "M turner" miturner70@hotmail.com 
>Date: 1/9/02 6:04 PM Eastern Standard Time

>, i
>am not in school i am an entry level programmer/analyst working for Geico
>Direct in macon, ga. 

I offer no apologies for the group, but had you identified yourself from the
get go your reception would have been a bit friendlier.

A new semester/quarter is starting and they'll be coming thick and fast :) 

Time to duck and cover!

Eileen
```

###### ↳ ↳ ↳ Re: question

- **From:** "Rational One" <noreligion@nogod.com>
- **Date:** 2002-01-10T04:29:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_M8%7.1529$JF.14788@rwcrnsc52.ops.asp.att.net>`
- **References:** `<q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com> <20020109223813.28515.00000571@mb-mp.aol.com>`

```

but we should all (in my humble opinion) give everyone a fair shake to start
with
and at least engage in friendly dialogue until we find out otherwise
even after 20 years I still ask questions, partly because I like to talk,
partly because manuals are written by people who have no concept of teaching
the end-user and partly because it is quicker and some people really like to
help, especially if it is an easy gesture
don't we all feel better after doing a good deed ?


"YukonMama" <yukonmama@aol.com> wrote in message
news:20020109223813.28515.00000571@mb-mp.aol.com...
> >From: "M turner" miturner70@hotmail.com
> >Date: 1/9/02 6:04 PM Eastern Standard Time
…[5 more quoted lines elided]…
> I offer no apologies for the group, but had you identified yourself from
the
> get go your reception would have been a bit friendlier.
>
…[4 more quoted lines elided]…
> Eileen
```

###### ↳ ↳ ↳ Re: question

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2002-01-10T06:07:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1jskt$fnm$1@panix1.panix.com>`
- **References:** `<q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com> <20020109223813.28515.00000571@mb-mp.aol.com> <_M8%7.1529$JF.14788@rwcrnsc52.ops.asp.att.net>`

```
In article <_M8%7.1529$JF.14788@rwcrnsc52.ops.asp.att.net>,
Rational One <noreligion@nogod.com> wrote:

[snippage]

>don't we all feel better after doing a good deed ?

Allowing someone to get away without doing their own homework is not, in 
my opinion, a 'good deed' for *anyone* involved.

DD
```

##### ↳ ↳ Re: question

- **From:** "Rational One" <noreligion@nogod.com>
- **Date:** 2002-01-10T04:24:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LH8%7.17749$762.146215@rwcrnsc54>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>`

```
M.

glad to hear you had success
I myself spent some time in 'Disgusta' so know Ga well
also - I taught myself COBOL entirely so I have sympathy that perhaps others
do not.

me, not being mensa bright, feel that if I can write COBOL programs for many
Fortune 1000 companies then anyone can. As any teacher will tell you - the
only stupid question is the one never asked, or something to that effect

what some of the other writers indicated is correct, there are very few key
words in COBOL or any language you just need a comfort level with the
basics, some creativity and persistence


have a good day.....




"M turner" <miturner70@hotmail.com> wrote in message
news:q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com...
> ok to those who helped thank you, i did manage to figure it out this
> afternoon at work. for those of you who think i should do my own homework,
i
> am not in school i am an entry level programmer/analyst working for Geico
> Direct in macon, ga.  True i have no experience programming prior to this
> and all they did was put me through a 14 week 'bootcamp' teaching us jcl,
> endevor, xpeditor, file-aid, and cobol.  so you can see why i may have
some
> questions.
> "M turner" <miturner70@hotmail.com> wrote in message
> news:bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com...
> > I have an output field with a pic x(8) value.  I need to find the best
way
> > to check the 7th or 8th character by itself to see if it is a certain
> value.
> > How do i set up to do this? if you have a good idea please email to me
at
> > miturner70@hotmail.com
> >
> >
>
>
```

###### ↳ ↳ ↳ Re: question

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-01-10T13:50:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1k60k$2pf$1@peabody.colorado.edu>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com> <LH8%7.17749$762.146215@rwcrnsc54>`

```

On  9-Jan-2002, "Rational One" <noreligion@nogod.com> wrote:

>  As any teacher will tell you - the
> only stupid question is the one never asked, or something to that effect

Maybe.  But the question "Will you do my homework for me?" can be stupid -
if the answer is "sure, here's the answer".
```

##### ↳ ↳ Re: question

- **From:** docdwarf@panix.com
- **Date:** 2002-01-10T06:04:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1jsgq$fhq$1@panix1.panix.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>`

```
In article <q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>,
M turner <miturner70@hotmail.com> wrote:
>ok to those who helped thank you, i did manage to figure it out this
>afternoon at work. for those of you who think i should do my own homework, i
>am not in school i am an entry level programmer/analyst working for Geico
>Direct in macon, ga.

One can have homework from places other than a school; next time you have 
such a difficulty you'll receive different welcome if you first post here 
the work you've already done.

DD
```

##### ↳ ↳ Re: question

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-01-10T21:55:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3E0DB7.227904A3@boeing.com>`
- **References:** `<bgO_7.35626$LQ1.11132605@news2.nash1.tn.home.com> <q04%7.37776$LQ1.11669077@news2.nash1.tn.home.com>`

```


M turner wrote:
> 
> ok to those who helped thank you, i did manage to figure it out this
…[5 more quoted lines elided]…
> questions.

You really should invest in a couple of reference books (over a certain
percentage of income they are even tax deductible)

I like:
COBOL Unleashed (for the more advanced stuff)
Teach Yourself COBOL in 24 hours (for the basics) by Thane Hubbell

Also Advanced COBOL by Gary Brown (I can not recall the exact title) is
very good for Structured programming; he also has one for OO programming

Read the FAQ - is has a ton of information; links; examples and
tutorials

	Susan A
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
