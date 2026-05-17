[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GoTo Gauntlet

_6 messages · 5 participants · 1997-06 → 1997-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### GoTo Gauntlet

- **From:** "john hofstad-parkhill" <ua-author-6589075@usenetarchives.gap>
- **Date:** 1997-06-23T21:40:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc803f$40b91e60$4c9e09ce@p200>`

```

I wrote:

›› Those that stick to GOTO don't understand structured
pogramming at all, especially as it pertains to the scope of the
function (paragraph). Creating more "efficient" code is, in the
larger scope of things much less efficient, besides being a cop
out.
<<

"J" wrote

› John Hofstad-Parkhill is misinformed. There are situations in
› which it is necessary to use GO TO.

It is never necessary to use a GO TO. Not ever. The context in this case is
creation of a new application. Maintenance of an existing application -
that retains GOTO cannot be predicted.

› These are rare in modern 
› Cobols.  However, some compilers in common use are still based 
› upon the old 1974 standard.
 
› Where I grew up, but structured development pre-dates ANSI '74 COBOL
 
› In these cases, it is quite often 
› necessary to use GO TO, since EXIT PERFORM, EXIT PERFORM CYCLE, 
› EXIT PARAGRAPH, EXIT SECTION and the END-* reserved words have 
› not been implemented.  In other cases, the use of GO TO simply 
› improves clarity.

I'm not familiar with "EXIT PERFORM", "EXIT PERFORM CYCLE", "EXIT
PARAGRAPH", "EXIT SECTION", at least as a verb/clause statement.

As for clarity, I refer to another posting that covered what essentially is
short term memory As you don't limit the scope of your GOTO use to that
within a paragraph, but even assuming you are, a GOTO remains a
discontiguous piece of logic.

Use of any such exits is a clear signal that the paragraph in question has
already exceeded it's scope.

›› Whether one is writing in a "structured" way is independent of
›› whether one writes "flat" code (using GO TO).

Well if we can define "structured" so vaguely. My use of the word
"structured" incorporates a design method that has no requirements for GO
TO, I believe this to be common, although there is an army that accepts
GOTO paragraph exit, I do not.

›› John acquires a copy of Principles of Progam Design, by Michael 
›› Jackson, which covers this issue quite effectively.
 
›› Why is Mike Jackson an authority ? Because he folds to GOTO?
 
›› I have been programming for over twenty years and also lectured 
›› on Jackson Structured Programming at a university.

I don't recognize this as a certificate of understanding structured design.

I could throw out my resume as well but, instead challange any who have too
much free time to show me an example of where GOTO is required. Obviously
rules such as "must be contained in one paragraph" make no sense.

I assert I can do anything you "GOTOer's" can do, as clearly if not more
so. I'm avoiding the word "better" as obviously this is a subjective term.
However, I have a keen eye for efficient code and have a deeper
understanding of compiler generated code then many.

Best I can do - put my "money" where my "mouth is".

And, I recognize the immense size of my own ego.
```

#### ↳ Re: GoTo Gauntlet

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7aa96fa83d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc803f$40b91e60$4c9e09ce@p200>`
- **References:** `<01bc803f$40b91e60$4c9e09ce@p200>`

```

Peter Clark wrote:
› 
› In article <01bc803f$40b91e60$4c9e09ce@p200> "John Hofstad-Parkhill"  writes:
…[5 more quoted lines elided]…
› A common problem amongst people with hyphenated surnames :-)

What, An immense ego, or recognising it ????????
```

#### ↳ Re: GoTo Gauntlet

- **From:** "ian larsen" <ua-author-17071368@usenetarchives.gap>
- **Date:** 1997-06-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7aa96fa83d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc803f$40b91e60$4c9e09ce@p200>`
- **References:** `<01bc803f$40b91e60$4c9e09ce@p200>`

```

John Hofstad-Parkhill wrote:
<>

› 
› I could throw out my resume as well but, instead challange any who have too
…[10 more quoted lines elided]…
› And, I recognize the immense size of my own ego.

John,
Have you ever had to contend with DMS statements on a Unysis 1100/2200
system?? Soe of the error trapping, I you want any level of control over
it, offers coders little option but to use the "ON ERROR GO TO" clause. 
And as a result of this you then have to code "forward pointing" GO TO
jumps to get around the error paragraphs at the bottom of the SECTION.

Generally I agree that GO TO's suck.  Sometimes the are not "required"
but can save a lot of unnecessary (?) inefficient code.  After all,
coding time is $$$$$.  So long as strict standards are adhered to and
the "rules" of "structured" programming are not completely ignored.
Can't we agree that there are different strokes for different folks??

Just my $0.02 worth (convert to local curreny and allow for exchange
rates)


-------------------------------------------------------------------
The words NOT.HERE are added to my email address to avoid those 
reprehensible individuals/companies who send unsolicited email to
people who have to pay per K for the privelege!
-------------------------------------------------------------------
The opinions expressed here, though they be many and (most probably)
wrong, are not those of my employer or any client organisation. ;-)
-------------------------------------------------------------------
```

##### ↳ ↳ Re: GoTo Gauntlet

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-06-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7aa96fa83d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7aa96fa83d-p3@usenetarchives.gap>`
- **References:** `<01bc803f$40b91e60$4c9e09ce@p200> <gap-7aa96fa83d-p3@usenetarchives.gap>`

```

Ian Larsen wrote:
› 
› [snip] 
…[4 more quoted lines elided]…
› jumps to get around the error paragraphs at the bottom of the SECTION.

[snip]

I've never done Unisys, so I ask out of ignorance: is GO TO the only
kind of statement which can follow ON ERROR? E.g. can you code:

ON ERROR PERFORM 9800-BOO-BOO

..or:

ON ERROR SET UH-OH TO TRUE

..?

If so, then I would have to deem the Unisys dialect defective.
Tastes may vary.

On an IBM mainframe, Cobol II (so far as I can tell from the manual)
does not have ON ERROR. However it has ON SIZE ERROR and ON
OVERFLOW, either of which may be followed by any imperative
statement, not just GO TO.

Michael C. Kasten mck9.swbell.net
```

###### ↳ ↳ ↳ Re: GoTo Gauntlet

- **From:** "ross klate" <ua-author-932727@usenetarchives.gap>
- **Date:** 1997-06-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7aa96fa83d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7aa96fa83d-p4@usenetarchives.gap>`
- **References:** `<01bc803f$40b91e60$4c9e09ce@p200> <gap-7aa96fa83d-p3@usenetarchives.gap> <gap-7aa96fa83d-p4@usenetarchives.gap>`

```

I have done a lot of programming on Unisys--though I have never seen
one of the Sperry-based 1100 machines.
Certainly, on the Burroughs-based A-Series you have a fairly wide
range of options for DMS error coding.

(a) Tailor the error code:
ON EXCEPTION
IF DMSTATUS (NOTFOUND)
MOVE "NOT FOUND" TO ERROR-MSG
MOVE 1 TO ERROR-FLAG
ELSE
IF DMSTATUS (DEADLOCK)
DISPLAY "DEADLOCK--RESUBMITTING"
PERFORM RESUBMIT-ROUTINE
ELSE
IF DMSTATUS

.
etc.

(b) Hope there are no errors, and if there are, blow up:
ON EXCEPTION
CALL SYSTEM DMTERMINATE.

(c) Branch to error routines:
ON EXCEPTION
GO TO ERROR-HANDLING-ROUTINE.
or
ON EXCEPTION
PERFORM ERROR-HANDLING-SECTION.

(d) Use no exception code at all.
FIND EMPLOYEE-SET AT EMPLOYEE-KEY = 0.


The 2200 machine has the reputation of being a "screamer"
number-cruncher, and I would be astounded if the DMS error
handling procedures were as primitive as suggested by Mr. Larsen.
```

###### ↳ ↳ ↳ Re: GoTo Gauntlet

_(reply depth: 4)_

- **From:** "ian larsen" <ua-author-17071368@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7aa96fa83d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7aa96fa83d-p5@usenetarchives.gap>`
- **References:** `<01bc803f$40b91e60$4c9e09ce@p200> <gap-7aa96fa83d-p3@usenetarchives.gap> <gap-7aa96fa83d-p4@usenetarchives.gap> <gap-7aa96fa83d-p5@usenetarchives.gap>`

```

Ross Klate wrote:
› 
› I have done a lot of programming on Unisys--though I have never seen
…[3 more quoted lines elided]…
› 
<>
Nice for some Ross ;-)

›
› The 2200 machine has the reputation of being a "screamer"
› number-cruncher, and I would be astounded if the DMS error
› handling procedures were as primitive as suggested by Mr. Larsen.
›

Get no argument from me. I personally would like to see an ON ERROR
PERFORM or ON ERROR
› 
›› [snip]
…[9 more quoted lines elided]…
›› 
<>

The Unysis 2200 (note not the A-series) can really hoot along in terms
of processing but the COBOL DMS1100 is pretty strict with it's syntax. 
The INVOKE clause does allow a default error trapping destination for
the ON ERROR clause but then you can't always determine wher you have
come from.
And I don't want to get into a "my platform is bigger than yours"
discussion.  Let's just face the fact that sometimes things (eg GO TO's)
aren't as cut and dried as some like to believe due to platform
dependancies.

-------------------------------------------------------------------
The words NOT.HERE are added to my email address to avoid those 
reprehensible individuals/companies who send unsolicited email to
people who have to pay per K for the privelege!
-------------------------------------------------------------------
The opinions expressed here, though they be many and (most probably)
wrong, are not those of my employer or any client organisation. ;-)
-------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
