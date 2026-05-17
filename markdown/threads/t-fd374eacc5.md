[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform thru exit

_13 messages · 12 participants · 1997-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Perform thru exit

- **From:** "mario alvarez" <ua-author-17072425@usenetarchives.gap>
- **Date:** 1997-02-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<330CD0CD.21C5@app1.dor.state.sc.us>`

```

Forgive me if this is a stupid question. I am mainly an online
programmer(idms/adso) but occasionally I write batch
cobol(IBM/mvs,cobol-II). I have seen reference in other postings about
not using "perform xxx-module thru xxx-exit". Was I just seeing things
or is there a reason for this and if so was is the alternative.

Mario Alvarez
Systems Analyst
S.C Department of Revenue
```

#### ↳ Re: Perform thru exit

- **From:** "year 2000 man" <ua-author-8447820@usenetarchives.gap>
- **Date:** 1997-02-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<330CD0CD.21C5@app1.dor.state.sc.us>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us>`

```

I have used PERFORM xxxxxx THRU XXXXXX and I like to use them from a pure
readability point of view if only from a maintenance stand point. However,
you can use simple PERFORMs without the THRU parameter...this requires that
paragraph names be SECTIONS as in A-1000-WRITE-HEADERS SECTION.

The PERFORM will keep executing code until it hits a SECTION...this is what
causes the program to return to the line of code following the PERFORM.

As to why you should not use the PERFORM....THRU....to tell you the truth,
I do not remember why you shouldn't but I think it really comes down to
personal preference but perhaps someone else can shed some light on it....I
have actually had MORE problems with the PERFORM without the THRU because,
should you forget the SECTION on the paragraph name, as I said earlier the
code like the Energizer bunny, keeps on going and going and going,,,,,

Mario Alvarez wrote in article
<330··.@app··c.us>...
› Forgive me if this is a stupid question.  I am mainly an online
› programmer(idms/adso) but occasionally I write batch
…[7 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Perform thru exit

- **From:** "bill seymour" <ua-author-6720964@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap>`

```

There is exactly one reason to write PERFORM...THRU: so that
you can have a paragraph name in the range of the PERFORM.

There is exactly one reason to have a paragraph name in the range
of a PERFORM: so that you can GO TO it.

If every PERFORM has a THRU, then THRU has no meaning; but when
used only where it's actually needed, it has an important meaning:
look out for the GO TO!

--Bill
```

##### ↳ ↳ Re: Perform thru exit

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap>`

```

What makes you think that PERFORM... without the THRU... requires the use
of SECTIONs? Absolutely not! If you PERFORM a single paragraph, a return
is implied immediately before the next paragraph.

As to why the PERFORM...THRU... construct is not recommended by many
(including myself), I ask why you need to perform multiple paragraphs. If
you wanted to perform AAA, BBB, and CCC, why not just use three separate
PERFORM verbs instead of PERFORM AAA THRU CCC? The latter generates three
situations that are best avoided. (1) The ordering of AAA, BBB, and CCC
is expected, but there is nothing to show you that. If you were to move
BBB elsewhere, the program not longer works as expected. (2) Some use
this as an excuse to insert a "GO TO", especially if CCC is actually
AAA-EXIT. If you do not allow PERFORMs of SECTIONs or PERFORM...THRU, then
you can't easily use a GOTO. (3) Someone could insert a paragraph between
AAA and BBB or between BBB and CCC, not knowing that it is part of the
PERFORM range and will be executed perhaps when not expected.

Bottom line -- I recommend not using PERFORM...THRU's (or PERFORM's of
SECTIONs). If you need to perform several paragraphs, either use several
PERFORM verbs, or ask whether you need several paragraphs instead of one.
```

##### ↳ ↳ Re: Perform thru exit

- **From:** "mca..." <ua-author-4356057@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap>`

```

"Year 2000 Man" wrote:

› I have used PERFORM xxxxxx THRU XXXXXX and I like to use them from a pure
› readability point of view if only from a maintenance stand point.  However,
› you can use simple PERFORMs without the THRU parameter...this requires that
› paragraph names be SECTIONS as in A-1000-WRITE-HEADERS    SECTION.
› 
Not True... Leave the sections off entirely, and you will only perform
that paragraph and return. There will be no fall through. The only
thing you lose is the ability to GOTO XXXXX-EXIT, and many of us feel
that is not at all a bad thing. Personally, I lose the A-1000 type
prefixes altogether. so code looks more like:

PERFORM OPEN-FILE
PERFORM READ-FILE
PERFORM UNTIL END-OF-INPUT-FILE
PERFORM PROCESS-AAA
PERFORM PROCESS-BBB
PERFORM READ-FILE
END-PERFORM

The basic idea (in my mind) is to lose all of the noise in the source
code. THRU EXIT doesn't tell you anything useful, and neither do the
paragraph prefixes (IMHO). Not using perform thru, also allows you to
assume in reading all of the code that there will be absolutely NO
falling through the end of one paragraph into the next.

I could go on and on, but that's some of the basic idea.

I would also ask what other structured programming language has ever
adopted the habit of numbering the procedures, or a perform thru type
notation? None that I know of, and for very good structured
programming reasons.

› The PERFORM will keep executing code until it hits a SECTION...this is what
› causes the program to return to the line of code following the PERFORM.
…[19 more quoted lines elided]…
››
```

###### ↳ ↳ ↳ Re: Perform thru exit

- **From:** "doug mckibbin" <ua-author-6588989@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p5@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap> <gap-fd374eacc5-p5@usenetarchives.gap>`

```

Mike Cargal wrote:
› 
› "Year 2000 Man"  wrote:
…[7 more quoted lines elided]…
› that paragraph and return.  There will be no fall through.  The only
[snip]
Technically, it is true. Assuming there is a main driver paragraph
execution will fall through it unless there is a GOBACK or STOP RUN at
the end of the main driver paragraph. FWIW, I also believe sections
should be avoided at all costs. I also believe in using exit
paragraphs. Some people do not like them because there are usually GO
TOs to them, but as long as they are the only GO TOs I have no problem
with them. Exit paragraphs can make code easier to maintain by
eliminating some nested IF/EVALUATE statements.

Regards,
Doug McKibbin
```

###### ↳ ↳ ↳ Re: Perform thru exit

- **From:** "tony trimboli" <ua-author-17073357@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p5@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap> <gap-fd374eacc5-p5@usenetarchives.gap>`

```

Mike Cargal wrote:
› 
› "Year 2000 Man"  wrote:
…[54 more quoted lines elided]…
››› 

I'm new to the group, but wanted to throw .02 on the sections
discussion. I don't actually perform sections, but I put them in my
program as a way to organize my source code. For example,

LEVEL-1 SECTION.

MAIN-LOGIC.
PERFORM OPENING-PROC.

IF OPENING-PROC-OK
PERFORM USUAL-BS UNTIL SICK-AND-TIRED-OF-IT.

PERFORM CLOSING-PROC.

MAIN-LOGIC-EXIT.
GOBACK.

LEVEL-2 SECTION.

USUAL-BS.

Then if necessary I use LEVEL-3 thru about LEVEL-5.
Next I use names like

FILE-IO-ROUTINES SECTION.
COMMON-UTILITIES SECTION.
DSPLY-ROUTINES SECTION.
ENTRY-ROUTINES SECTION.

This way I can keep 'like' paragraphs grouped together. It makes it
easier to search for those routines with my editor. It also makes it
easier to do cut and paste operations. For instance, if I had 3
paragraphs for the CUST-FILE and needed to add the CUSTDETL-FILE to the
program, I am more than likely going to have a large enough edit window
to cut and paste, without scrolling through the entire program.

I had a bad experience with performing sections a few years back. My
boss and I were the only programmers, and we both knew the system pretty
well. Well we hired some experienced programmers that were really
newbies in disguise (don't believe everything you read on a resume).
They didn't know anything about sections. They started putting routines
into the sections, not realizing that they would be fallen into by other
routines. Inadequate testing allowed this to get to a customer's site.
And people wonder why programmers work 60 hour weeks all the time.

Tony Trimboli
```

###### ↳ ↳ ↳ Re: Perform thru exit

_(reply depth: 4)_

- **From:** "dlmiller_at_inetdirect.net" <ua-author-20631@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p7@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap> <gap-fd374eacc5-p5@usenetarchives.gap> <gap-fd374eacc5-p7@usenetarchives.gap>`

```

Tony Trimboli wrote:
[previous discussion of sections snipped]

› I'm new to the group, but wanted to throw .02 on the sections
› discussion. I don't actually perform sections, but I put them in my
…[18 more quoted lines elided]…
› 

Having code in one section that PERFORMs paragraphs within another
section is not a recommended practice, and some compilers will produce
a warning diagnostic in that situation.


› Then if necessary I use LEVEL-3 thru about LEVEL-5.
› Next I use names like
…[11 more quoted lines elided]…
› to cut and paste, without scrolling through the entire program.

It's just as easy to use similar paragraph names -- and that doesn't
introduce difficulties such as the one you describe below.

› 
› I had a bad experience with performing sections a few years back. My
…[8 more quoted lines elided]…
› Tony Trimboli

A perfect illustration of why using sections in the Procedure Division is
a terrible idea: because it makes maintenance much more difficult. In my
opinion, this problem is 10% the fault of the maintenance programmer who
failed to realize the effect of adding paragraphs within a section, and 90%
the fault of the original programmer whose inferior program design made
such a situation possible in the first place.

Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

###### ↳ ↳ ↳ Re: Perform thru exit

- **From:** "lebl..." <ua-author-14800849@usenetarchives.gap>
- **Date:** 1997-02-22T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p5@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap> <gap-fd374eacc5-p5@usenetarchives.gap>`

```

Hi Mike,

I agree with your reasoning on Perform Thru statements. But there is
one good reason for numbering paragraphs in COBOL. I have seen some
monsterous COBOL programs, with 10,000 to 25,000 or more procedure
divison lines. I am not proposing that anyone write programs this
large, but I had to maintain programs that were already written. I
used the existing paragraph numbering scheme, with some enhancements,
just so I could tell where I was in the program.

I have not seen paragraph numbering in any other language, except for
FORTRAN and IBM 360 assembler. But I haven't seen monsterous programs
in other languages either.

Just my .02

Dilbert


mca··.@min··g.com (Mike Cargal) wrote:

› (snip)
› The basic idea (in my mind) is to lose all of the noise in the source
…[11 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Perform thru exit

- **From:** "dlmiller_at_inetdirect.net" <ua-author-20631@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap>`

```

"Year 2000 Man" wrote:
› I have used PERFORM xxxxxx THRU XXXXXX and I like to use them from a pure
› readability point of view if only from a maintenance stand point.  However,
› you can use simple PERFORMs without the THRU parameter...this requires that
› paragraph names be SECTIONS as in A-1000-WRITE-HEADERS    SECTION.

Sorry, this is just plain false. There is no requirement, ever, to use SECTIONs
in the Procedure Division (unless you're using a Cobol-74 or earlier compiler).

›
› The PERFORM will keep executing code until it hits a SECTION...this is what
› causes the program to return to the line of code following the PERFORM.

This is also false. PERFORM transfers control to ,
executes the instructions there, and *returns* to the statement following the
PERFORM. What you are describing is the behavior of PERFORM ,
not PERFORM -- an excellent reason for never using sections.

› 
› As to why you should not use the PERFORM....THRU....to tell you the truth,
…[4 more quoted lines elided]…
› code like the Energizer bunny,  keeps on going and going and going,,,,,

Your problems are caused not by using PERFORM without THRU, but by
using SECTIONs in the Procedure Division -- misusing them, actually.

Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

##### ↳ ↳ Re: Perform thru exit

- **From:** "mike jones" <ua-author-18408@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p2@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap>`

```

Year 2000 Man wrote:
› 
› I have used PERFORM xxxxxx THRU XXXXXX and I like to use them from a pure
…[6 more quoted lines elided]…
› 

Many programmers labor under this mistaken concept.

If you simply perform a paragraph (using no SECTION's or
even with SECTION's) IBM Cobol
compilers will not proceed thru paragraph after paragraph. The reason
for many "fall-thru" programs is that some programmers (not casting any
stones here...) will use "GO TO xxxx-exit"'s which *do* fall-thru
to the end of a program, since it overrides the perform save cells, when
you don't use the corresponding THRU clause on the PERFORM. Also, in
SORT/MERGE sections, if an EXIT is not hit, the code will repeat the
THRU range until falling into an abort condition.

One drawback to the THRU range, however, is that if you introduce a
new paragraph between the end of the range, you will introduce a
"fall-thru"
condition and an 'unexpected program feature.'

Yes, it is a matter of personal preference, but I often will mingle the
two styles--using thru-exits to take an early exit of performed logic
block.
Of course, with Cobol II, it is possible to use CONTINUE's and
IF/ELSE/END-IF blocks and inline-performs(PERFORM/END-PERFORM's)
to avoid this sort of logic.

› Mario Alvarez  wrote in article
› <330··.@app··c.us>...
…[8 more quoted lines elided]…
›› S.C Department of Revenue

This Perform/thru hassle is being done because many "structurist"
programmers
(programmers who would die before coding a "GO TO") hold this view. It
is
a positive view given the malignment COBOL gets from many C/C++
programmers
who boast that their languages are more "structured" than COBOL and
doesn't
support "goto" [this is also another incorrect belief, C/C++ supports
goto
and the misuse of it]. But it is also impractical when you consider
the timing constraints on many Cobol apps where the time to:

read file-1
at end set end-file-1-sw to true
end-read
if end-file-1-sw
....
else
....
end-if

adds to the execution timing with a decision--a decision in a repeated
loop,
no less. Thus, the following pairs of logic are better for timing and
readibility:

Exam 1:
...
read file-1
at end set end-file-1-sw to true
end-read

perform read-para
until end-file-1-sw
...
read-para.

read file-1
at end set end-file-1-sw to true
end-read.

Exam 2:
perform read-para thru read-exit
until end-file-1-sw
read-para.
read file-1
at end set end-file-1-sw to true
go to read-exit
end-read
.
read-exit. exit.

======================================================

Enoch
IA dept. revenue & finance
```

###### ↳ ↳ ↳ Re: Perform thru exit

- **From:** "kdr3" <ua-author-17072820@usenetarchives.gap>
- **Date:** 1997-02-25T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fd374eacc5-p11@usenetarchives.gap>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us> <gap-fd374eacc5-p2@usenetarchives.gap> <gap-fd374eacc5-p11@usenetarchives.gap>`

```

With Cobol II, I haven't used a 'go to' since 1992 in any new programs I
have written. I do not perfoem thru exit because it's not necessary. The
machine knows where the end of paragraph is. I never use sections
unless an internal sort has to be done. I try to do all sorts 'outside'
the program using syncsort or dfsort.

I've included a Cobol II version of a do/while loop I use to read an
input file until eof:

Procedure Division.
Perform 9000-init.
Perform 2000-mainline.
Perform 3000-end.

2000-mainline.
Perform until ws-no-more-in-recs
Read in-file
at end
move ws-y to ws-in-file-ind
End-read
If ws-more-in-recs
add ws-1 to ws-in-ctr
Perform p2100-process-rec
End-if
end-perform.

working storage:

05 ws-y pic x value 'y'.
05 ws-in-file-ind pic x value spaces.
88 ws-more-in-recs value spaces.
88 ws-no-more-in-recs value 'y'.

For readability i put ws at the bottom.
Hope this helps.

Ken Robinson
```

#### ↳ Re: Perform thru exit

- **From:** "ron peterson" <ua-author-14911@usenetarchives.gap>
- **Date:** 1997-02-20T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fd374eacc5-p13@usenetarchives.gap>`
- **In-Reply-To:** `<330CD0CD.21C5@app1.dor.state.sc.us>`
- **References:** `<330CD0CD.21C5@app1.dor.state.sc.us>`

```

Mario Alvarez wrote:
› 
› Forgive me if this is a stupid question.  I am mainly an online
…[4 more quoted lines elided]…
› 

The reason for not using "PERFORM ... THRU ..." is because using it
implies that you are not using structured programming (i. e.
no GOTOs). You shouldn't need to use SECTIONs to avoid the THRU
option.

Ron
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
