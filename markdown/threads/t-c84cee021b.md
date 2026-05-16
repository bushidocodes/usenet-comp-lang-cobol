[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SAME AS ('02 Standard) Clause - and circulatiy

_14 messages · 3 participants · 2007-08_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-30T00:24:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com>`

```
I was going to respond to Pete's question about circularity of reference with 
the answer that this was explicitly prohibited.  I can see that there was an 
(elementary) attempt to do so, but I would be interested in the input of those 
(like Roger and Karl) who have actually worked with it.

SR(3) of the SAME AS clause says,

"The description of data-name-1, including its subordinate data items, shall not 
contain a SAME AS clause that references the subject of the entry or any group 
item to which this entry is subordinate."

Clearly (to me) this was trying to avoid circular references, but I don't THINK 
that it (or any other obvious to me place) prohibits (the impossible).

01  AAA Same as BBB.
01  BBB Same as CCC.
01  CCC Same as AAA.

Does anyone see where (how) this is prohibited?  I certainly THOUGHT that we 
dealt with it when developing the Standard, but I don't see where.  I think that 
SR(3) was supposed to have some sort of "directly or indirectly" in it - that 
isn't there in the final text.
```

#### ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-30T00:39:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JkoBi.214751$sR4.61918@fe08.news.easynews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com>`

```
To add to my quandry,  GR(1) of the SAME AS clause says,

"The effect of the SAME AS clause is as though the data description identified 
by data-name-1 had been coded
in place of the SAME AS clause, excluding the level-number, name, and the 
EXTERNAL, GLOBAL, REDEFINES,
and SELECT WHEN clauses specified for data-name-1; level numbers of subordinate 
items may be adjusted as
described in general rule 2.

  NOTE This rule, in combination with the syntax rules for this clause, 
prohibits direct or indirect circular reference"

I, personally, don't see how you get from the syntax rules and GR(1) to the 
(informative) note under GR(1).
```

##### ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-29T21:08:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dc6aj9nnt2h21@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <JkoBi.214751$sR4.61918@fe08.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:JkoBi.214751$sR4.61918@fe08.news.easynews.com...
> To add to my quandry,  GR(1) of the SAME AS clause says,
>
> "The effect of the SAME AS clause is as though the data description
identified
> by data-name-1 had been coded
> in place of the SAME AS clause, excluding the level-number, name, and the
> EXTERNAL, GLOBAL, REDEFINES,
> and SELECT WHEN clauses specified for data-name-1; level numbers of
subordinate
> items may be adjusted as
> described in general rule 2.
…[4 more quoted lines elided]…
> I, personally, don't see how you get from the syntax rules and GR(1) to
the
> (informative) note under GR(1).
>
…[5 more quoted lines elided]…
> >I was going to respond to Pete's question about circularity of reference
with
> >the answer that this was explicitly prohibited.  I can see that there was
an
> >(elementary) attempt to do so, but I would be interested in the input of
those
> >(like Roger and Karl) who have actually worked with it.
> >
> > SR(3) of the SAME AS clause says,
> >
> > "The description of data-name-1, including its subordinate data items,
shall
> > not contain a SAME AS clause that references the subject of the entry or
any
> > group item to which this entry is subordinate."
> >
> > Clearly (to me) this was trying to avoid circular references, but I
don't
> > THINK that it (or any other obvious to me place) prohibits (the
impossible).
> >
> > 01  AAA Same as BBB.
…[3 more quoted lines elided]…
> > Does anyone see where (how) this is prohibited?  I certainly THOUGHT
that we
> > dealt with it when developing the Standard, but I don't see where.  I
think
> > that SR(3) was supposed to have some sort of "directly or indirectly" in
it -
> > that isn't there in the final text.

The above is effectively,

01 AAA.
  02 BBB.
    03 CCC same as AAA.

01 BBB.
  02 CCC.
    03 AAA same as BBB.

01 CCC.
  02 AAA.
    03 BBB same as CCC.

Thus all three data-description-entries have cicular references.
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-30T01:49:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lmpBi.24304$1J4.22640@fe06.news.easynews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <JkoBi.214751$sR4.61918@fe08.news.easynews.com> <13dc6aj9nnt2h21@corp.supernews.com>`

```
I see - from your expansion (using the GR), the expanded text violates the SR. 
Therefore, this circularity IS prohibited by the current rules (even if it isn't 
totally "obvious" - to me - but possibly it is obvious to others).
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-29T21:55:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dc91jb5dle31a@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <JkoBi.214751$sR4.61918@fe08.news.easynews.com> <13dc6aj9nnt2h21@corp.supernews.com> <lmpBi.24304$1J4.22640@fe06.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:lmpBi.24304$1J4.22640@fe06.news.easynews.com...
> I see - from your expansion (using the GR), the expanded text violates the
SR.
> Therefore, this circularity IS prohibited by the current rules (even if it
isn't
> totally "obvious" - to me - but possibly it is obvious to others).

I decided I wasn't being clear, so I worked on a
clarification that might prove better.
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-29T21:51:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dc8q3e6dm0v7e@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <JkoBi.214751$sR4.61918@fe08.news.easynews.com> <13dc6aj9nnt2h21@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:13dc6aj9nnt2h21@corp.supernews.com...
[snip]
> The above is effectively,
>
…[12 more quoted lines elided]…
> Thus all three data-description-entries have cicular references.

Perhaps I was not sufficiently clear.

In each case, when SR(3) is applied at level-number 3, the
circularity is revealed.

The sequence, in each case, is:
    level-number 1: SR(3), GR(1) and GR(2)
    level-number 2: SR(3), GR(1) and GR(2)
    level-number 3: SR(3) <syntax error>

I hope that clarifies.
```

#### ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-30T12:47:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jmickFau60U1@mid.individual.net>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:Q6oBi.4946$i91.105@fe01.news.easynews.com...
>I was going to respond to Pete's question about circularity of reference 
>with the answer that this was explicitly prohibited.  I can see that there 
…[21 more quoted lines elided]…
>

Rather than making a specific staement in every place where it might arise, 
I would have thought a simple concise GENERAL statement would do it. (Each 
specific could then refer to the "Circular Reference" warning.) The trouble 
with doing it for every specifc instance is that the wording then becomes 
inconsistent.

> "The description of data-name-1, including its subordinate data items, 
> shall not contain a SAME AS clause that references the subject of the 
> entry or any group item to which this entry is subordinate."
(33 words)

"If you use a SAME AS clause, there must not be any subordinate SAME AS 
clauses that would cause a circular reference back to it."
(25 words - a 25% improvement with no loss of meaning, and much more easily 
assimilable for most people.)

Has anybody noticed how "dry" and legalistic the wording of this standard 
is? Insurance companies, Banks, and even the Legal profession itself, have 
all benefited greatly from the campaign for simple English.

Pete.
```

#### ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-30T10:41:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ddluk7ihjpmc2@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com>`

```
In the game "Break the Standard", I came up with one
that appears to have anomalous behavior

1 C SAME AS A2 OF B.
1 B.
    2 B1 PIC X.
    2 B2 TYPE TO A.
1 A IS TYPEDEF.
    2 A1 PIC X.
    2 A2 PIC X.

SAME AS SR(1) permits qualified names; SR(7) permits
reference to an elementary item; and GR(1) covers
expansion using A2 OF B. However A2 OF B can not
be known until B2 of B is expanded and I find no
general rule requiring the expansion of  B2 OF B to reveal
A2; nor any syntax rule limiting [SAME AS] data-name-1
to what is explicitly defined in source code.

Reverse the order of the level-number 1 items and expansion
of B2 OF B makes A2 OF B known before the expansion
of C.

In other words, as written, it appears to be a syntax error;
reversed, there appears to be no error.
```

##### ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-30T19:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DwEBi.220952$Bo7.80428@fe07.news.easynews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com>`

```
Rick,
   Once again, you can submit an interpretation request IF YOU WANT TO, but my 
impression is that you think the standard does (or should) tell implementers in 
what order to do things.  Other than the "text manipulation" and "compilation" 
stages, this is simply NOT true.  The Standard tells them what to do and it is 
up to them to figure out HOW.  If you changed your example to:

 1 C SAME AS A2 OF B.
 1 B.
    2 B1 PIC X.
    2 B2.
    COPY  A.

with a COPY member of A that read
    3 A1 PIC X.
    3 A2 PIC X.

I think you would agree that an implementer could (and would) be able to resolve 
it.  Therefore, as the SRs and GRs ALLOW for your original source code, it is up 
to the implementer to figure out how (even if it requires multiple passes) to do 
it.
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-30T18:30:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13deheh482ri440@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com> <DwEBi.220952$Bo7.80428@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:DwEBi.220952$Bo7.80428@fe07.news.easynews.com...
> Rick,
>    Once again, you can submit an interpretation request IF YOU WANT TO,
but my
> impression is that you think the standard does (or should) tell
implementers in
> what order to do things.  Other than the "text manipulation" and
"compilation"
> stages, this is simply NOT true.

I think you may have meant "logical conversion" (one line at
a time) and "text manipulation" (three phases).
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-31T01:31:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PbKBi.24130$nT6.17542@fe03.news.easynews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com> <DwEBi.220952$Bo7.80428@fe07.news.easynews.com> <13deheh482ri440@corp.supernews.com>`

```
According to page 29 of the approved '02 Standard,

"The actions of compiler directing statements and compiler directives occur in 
two logical stages of compilation group processing - the text manipulation stage 
and the compilation stage.

The text manipulation stage accepts an initial compilation group, performs 
modifications specified by COPY and REPLACE statements and conditional 
compilation directives, and substitutes compilation variables into constant 
entries. The result is a structured compilation group for processing by the 
compilation stage.

The compilation stage completes the compilation process utilizing the structured 
compilation group."

Are we talking about different things here?
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-30T22:59:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13df16qdkumu47a@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com> <DwEBi.220952$Bo7.80428@fe07.news.easynews.com> <13deheh482ri440@corp.supernews.com> <PbKBi.24130$nT6.17542@fe03.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:PbKBi.24130$nT6.17542@fe03.news.easynews.com...
> According to page 29 of the approved '02 Standard,

This quote appears to be from page 30 of WD 1.7, though
I notice it is missing the marks identifying changes from the
2002 standard. Was the FDIS changed during the approval
process?

> "The actions of compiler directing statements and compiler directives
occur in
> two logical stages of compilation group processing - the text manipulation
stage
> and the compilation stage.
>
> The text manipulation stage accepts an initial compilation group, performs
> modifications specified by COPY and REPLACE statements and conditional
> compilation directives, and substitutes compilation variables into
constant
> entries. The result is a structured compilation group for processing by
the
> compilation stage.
>
> The compilation stage completes the compilation process utilizing the
structured
> compilation group."
>
> Are we talking about different things here?

Maybe! You wrote "... the standard does (or should) tell
implementers in what order to do things." Then in the following
sentence and compensating for the double negative formed by
"Other" and "NOT", you identified "'text manipulation' and
'compilation'" as specifying "in what order to do things".

However "compilation", the processing of the structured
compilation group, is the where I try to find order, while you
insist that "HOW" of this processing is determined by the
implementor. Thus I saw your statements as inconsistent.

Furthermore, you mention "stages" while I mention those
items where "order" is mentioned, or implied.

From page 28, "The rules of logical conversion are applied
to each line of a compilation group in the order that lines of
source text and library text are obtained by the compiler."

From page 30, the phrases "input lines are accepted
sequentially", "processed in the order encountered", and
"applied in order" express certain actions of the three
phases of text manipulation.

If the compilation stage were described in such terms, we
would not have had these conversations and all would be
right with the world. <g>


> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:13deheh482ri440@corp.supernews.com...
…[13 more quoted lines elided]…
> > a time) and "text manipulation" (three phases).
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-31T03:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yQLBi.16969$VU2.9343@fe02.news.easynews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com> <DwEBi.220952$Bo7.80428@fe07.news.easynews.com> <13deheh482ri440@corp.supernews.com> <PbKBi.24130$nT6.17542@fe03.news.easynews.com> <13df16qdkumu47a@corp.supernews.com>`

```
Clearly I made a mistake in saying

 "the standard does (or should) tell  implementers in what order to do things"

what I meant to say was

 "the standard does NOT (or should NOT) tell  implementers in what order to do 
things"

I do have WD 1.7 (of the NEXT standard) but don't want to quote that now - as 
the direction is to go back to WD 1.6 (to get rid of the TR's that are now not 
going into the next revision).

As far as "6.4 Logical conversion" as described on page 28 and following, this 
applies (as I think you may have recognized) during the "text manipulation 
stage" (because that is where "source text" and "library text" is dealt with.

When you say,

"If the compilation stage were described in such terms, we would not have had 
these conversations and all would be  right with the world. <g>"

This is indeed the "crux of the matter", i.e. the COBOL Standard is very careful 
in NOT providing rules for the order in which stuff needs to be done during the 
compilation stage.  It tells implementers what they must do - but leaves it up 
to them how to accomplisth it.
```

###### ↳ ↳ ↳ Re: SAME AS ('02 Standard) Clause - and circulatiy

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-31T00:09:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13df5adhurje98a@corp.supernews.com>`
- **References:** `<Q6oBi.4946$i91.105@fe01.news.easynews.com> <13ddluk7ihjpmc2@corp.supernews.com> <DwEBi.220952$Bo7.80428@fe07.news.easynews.com> <13deheh482ri440@corp.supernews.com> <PbKBi.24130$nT6.17542@fe03.news.easynews.com> <13df16qdkumu47a@corp.supernews.com> <yQLBi.16969$VU2.9343@fe02.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:yQLBi.16969$VU2.9343@fe02.news.easynews.com...
> Clearly I made a mistake in saying
>
>  "the standard does (or should) tell  implementers in what order to do
things"
>
> what I meant to say was
>
>  "the standard does NOT (or should NOT) tell  implementers in what order
to do
> things"

No, that part was OK! There was, effectively, another
negative that I compensated for to get to a positive form.
I showed an ellipsis. Correctly restated assertions might
be "The standard tells implementers in what order to do
things only in the text manipulation stage.", or "The
standard does not tell implementers in what order to do
things in the compilation stage."

The effective negative that I omitted was concerning
your belief in my thinking ("... my impression is that you
think ..."); which, when taken out of context, is actually
a very nice thing to say. <g>


> I do have WD 1.7 (of the NEXT standard) but don't want to quote that now -
as
> the direction is to go back to WD 1.6 (to get rid of the TR's that are now
not
> going into the next revision).
>
> As far as "6.4 Logical conversion" as described on page 28 and following,
this
> applies (as I think you may have recognized) during the "text manipulation
> stage" (because that is where "source text" and "library text" is dealt
with.
>
> When you say,
>
> "If the compilation stage were described in such terms, we would not have
had
> these conversations and all would be  right with the world. <g>"
>
> This is indeed the "crux of the matter", i.e. the COBOL Standard is very
careful
> in NOT providing rules for the order in which stuff needs to be done
during the
> compilation stage.  It tells implementers what they must do - but leaves
it up
> to them how to accomplisth it.
>
…[17 more quoted lines elided]…
> >> two logical stages of compilation group processing - the text
manipulation
> > stage
> >> and the compilation stage.
> >>
> >> The text manipulation stage accepts an initial compilation group,
performs
> >> modifications specified by COPY and REPLACE statements and conditional
> >> compilation directives, and substitutes compilation variables into
…[45 more quoted lines elided]…
> >> >>    Once again, you can submit an interpretation request IF YOU WANT
TO,
> >> > but my
> >> >> impression is that you think the standard does (or should) tell
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
