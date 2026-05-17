[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Coding style

_6 messages · 4 participants · 1996-04_

---

### Coding style

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kohti$22ju@news-s01.ny.us.ibm.net>`

```
By accident, my previous posting on this subject had the
misleading title "Re:Post new article". The present posting
is to point out my mistake (gawd, it's hard to be perfect).
For best result when viewing the posting, use a fixed width
font (otherwise some of the examples of "good indentation"
come out looking rather bad).
Leif Svalgaard
```

#### ↳ Re: Coding style

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-04-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1bcd9a622-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4kohti$22ju@news-s01.ny.us.ibm.net>`
- **References:** `<4kohti$22ju@news-s01.ny.us.ibm.net>`

```
I believe there is one very minor factual error in your long post on
Coding style, at least with regard to IBM mainframe COBOL compilers.

I have encountered many programs in my shop which have NO paragraph name
following the PROCEDURE DIVISION header. For example:

PROCEDURE DIVISION.

PERFORM 1000-INITIALIZE-THE-PROGRAM.
PERFORM 2000-PROCESS-1-RECORD
UNTIL 88-100-ALL-RECORDS-PROCESSED.
PERFORM 3000-PRINT-FINAL-TOTALS.
PERFORM 4000-CLOSE-FILES.
GOBACK.

My experience is that an initial paragraph name is not required, either
for OS/VS COBOL (ANSI 74) or VS COBOL II (ANSI 85). The compiler doesn't
complain at all, and the programs run fine. Our shop standards require
the first paragraph to be named 0000-MAINLINE.

On the whole, I agree with your coding standards. There are a few I
don't care for. I personally do not like the period on a line by itself,
and no one seems to use that in my shop. Our standards require the
paragraph number, and we haven't found it difficult to name paragraphs
with only the remaining 25 characters. We also have a rule against
performing backwards in the structure chart.

We also require that paragraph names begin with an action verb and be
followed by a direct object. Our style checker has a table of over 200
verbs to validate against, and then it checks for additional nodes in the
paragraph name to satisfy the direct object requirement.

We try to enforce alignment in the DATA DIVISION just as you describe.
It does make it easier to read.

A lot of maintenance problems can be avoided just by having all programs
in your shop follow a consistent standard. Having no standards at all
makes it MUCH harder to analyze a program for maintenance.
```

##### ↳ ↳ Re: Coding style

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-04-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1bcd9a622-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1bcd9a622-p2@usenetarchives.gap>`
- **References:** `<4kohti$22ju@news-s01.ny.us.ibm.net> <gap-d1bcd9a622-p2@usenetarchives.gap>`

```
In <4kq3a8$8.··.@mti··t.net>, Arn Trembley writes:
› I believe there is one very minor factual error in your long post on 
› Coding style, at least with regard to IBM mainframe COBOL compilers.
…[17 more quoted lines elided]…
› 
Most ANSI-74 compilers require a beginning paragraph.
It's tru that the IBM compilers don't, but since ETK is
used to write portable programs with, we must take into
account the (real) possibility that there is a compiler
out there that requires it.
Otherwise, thanks for your comments.
Leif Svalgaard
```

##### ↳ ↳ Re: Coding style

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-04-16T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1bcd9a622-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1bcd9a622-p2@usenetarchives.gap>`
- **References:** `<4kohti$22ju@news-s01.ny.us.ibm.net> <gap-d1bcd9a622-p2@usenetarchives.gap>`

```
In article , mor··.@lin··c.nz says...
› 
› In article <4kq3a8$8.··.@mti··t.net> Arn Trembley 
…[4 more quoted lines elided]…
› Yeeeuch!
 
› That's about the only place I use a full stop. Right at the end of a section.
 
› 
›› and no one seems to use that in my shop.  Our standards require the 
…[4 more quoted lines elided]…
› Sounds sensible.

Not neccessarily so. On some compilers it was a lot more efficient to perform
a section/paragraph that had previously been compiled rather than one the
compiler hadn't yet encountered. I remember 9 years ago when I started at MF
maintaining code that was written in 1979 that had loads of backwards performs
and each time critical section had a single letter and a few numbers as a name
as that was more efficient at the time.

Thankfully we don't have to code like that anymore.

›
›› We also require that paragraph names begin with an action verb and be
›› followed by a direct object.
›
› Hmmm.

This sounds like my code. I normally have sections named 'process-events' or
'create-main-dialog-box' but also have sections that are categorized too. eg.
'panels2-create-dialog-box' which is a panels2 call rather than the section
create-main-dialog-box which uses the panels2 call routine but also sets up
the position, title, text etc.

› 
›› We try to enforce alignment in the DATA DIVISION just as you describe.  
›› It does make it easier to read.
› 
› Yep.
 
› It's so easy to do that I don't know why people wouldn't.
 
› 
›› A lot of maintenance problems can be avoided just by having all programs 
…[7 more quoted lines elided]…
› it gets a bit difficult. 

The biggest problem I've come across is coping with mainframe programmers
style. People that have been brought up on ANS85 and Micro Focus COBOL
generally follow a more english flowing style. What helps at Micro Focus is
that people generally know what code is efficient and what verbs to avoid. We
have a set of internal guidelines but the code police don't come around and
kneecap you if you're caught using INSPECT ... REPLACING using huge strings.
You might get laughed at when you do a code walkthough with your peers though
;-)

A lot of ANS74 or mainframe programmers still have hangups they haven't got
rid of. Things like GOBACK and COPY ... REPLACING and typing everything in
UPPERCASE!

› At another site (of a well known oil company) I've seen numerous GOTO labels 
› where the label is outside the section. AND that section was a copybook too! 
 
› EEEK! Forgot about GOTO.
 
› Am I supposed to follow that standard?

If that's the way they want it then I don't see how you can't but you could
give them some strong hints.

›
› At another site they would not use QTY as a suffix (ORDER-QTY) because it
› could stand for quality as well as quantity. That standard would be overkill
› here.

I'm of the fully qualified name approach generally so I'd use 'Order-Quantity'
or whatever anyway. We thankfully don't have conventions on naming things but
almost everyone I know uses full names or for temporary items, the size of the
item for the name. It's not uncommon to see items like 'c2' which is a 2 byte
item or c4 which is 4 byte item. Those would be comp-x hence the c. No-one
uses just comp for temporary items

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

###### ↳ ↳ ↳ Re: Coding style

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1996-04-17T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1bcd9a622-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1bcd9a622-p4@usenetarchives.gap>`
- **References:** `<4kohti$22ju@news-s01.ny.us.ibm.net> <gap-d1bcd9a622-p2@usenetarchives.gap> <gap-d1bcd9a622-p4@usenetarchives.gap>`

```
In article <4l2kkg$6.··.@hyp··o.uk>
s.··.@mfl··o.uk "Shaun C. Murray" of Micro Focus writes:
› What helps at Micro Focus is that people generally know what
› code is efficient and what verbs to avoid. We have a set of
…[3 more quoted lines elided]…
› walkthough with your peers though ;-)

Instead of laughing at the coders, why not scream at the compiler
writers? These are cases where the compiler should be improved.

If a good compiler cannot generate, for example, an efficient
double-indexed string replacement, then it should warn the user
and suggest another method that is easier to compile.

Richard Ross-Langley   +44 1727 852 801
Mine of Information Ltd,  PO BOX 1000,  St Albans AL3 5NY,  GB
=== Independent Computer Consultancy * Established in 1977 ===
```

###### ↳ ↳ ↳ Re: Coding style

_(reply depth: 4)_

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-04-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1bcd9a622-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1bcd9a622-p5@usenetarchives.gap>`
- **References:** `<4kohti$22ju@news-s01.ny.us.ibm.net> <gap-d1bcd9a622-p2@usenetarchives.gap> <gap-d1bcd9a622-p4@usenetarchives.gap> <gap-d1bcd9a622-p5@usenetarchives.gap>`

```
In article <829··.@min··o.uk>, r.··.@min··o.uk says...
› 
› Instead of laughing at the coders, why not scream at the compiler 
› writers?  These are cases where the compiler should be improved.
 
› We do! 
 
› 
› If a good compiler cannot generate, for example, an efficient 
› double-indexed string replacement, then it should warn the user 
› and suggest another method that is easier to compile.

Ours does. It doesn't stop people using bad code though and most of the cases
where the compiler is slow have been dramatically improved. We have a compiler
directive to flag bad code though I believe it may be internal only.

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
