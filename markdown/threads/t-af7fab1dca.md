[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Syntax ???

_4 messages · 2 participants · 2004-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Syntax ???

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-17T22:18:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l946c.26360$%06.10908@newsread2.news.pas.earthlink.net>`

```
A follow-up on another thread.

As the '85 (much less '74) Standard does not "define" syntax, I wanted to add my
two (or more) cents to a discussion of what is and is not a "syntax error" in an
'85 Standard conforming compiler.

The Standard explicitly allows for an implementation to "set limits" of various
types (where the Standard has an "ellipsis" for multiple occurrences).

It would seem to me that if a vendor documents (for example) that they only
support 15 WHEN phrases in an EVALUATE statement, that coding 16 when statements
*is* a syntax error.  (Hopefully, this isn't "too controversial" a view).

If a vendor documents that they only support 16M of Working-Storage, then I
would also state that if an application creates 16M + 1-byte, that this is a
"syntax error" - even if some of those "bytes" are due to "sync" clauses,
01-level boundaries or "non-visible to the programmer" issues.

Therefore, it would seem to me (and I do accept that this may be controversial)
that if a vendor documents that each paragraph in the procedure division may
result in "only" 1K of storage, that a program that "violates" this rule has
violated a "syntax rule (even if there is no way for the programmer to figure
out how to "code around" this restriction - by simply looking at source code).

If, on the other hand, the vendor does NOT document how large (object code) each
paragraph may be but "blows" registers (or whatever) at compile time, then I see
that as a "compiler error" - or - at least - not a syntax error.

OBVIOUSLY "your mileage may vary" <G>
```

#### ↳ Re: Syntax ???

- **From:** docdwarf@panix.com
- **Date:** 2004-03-18T05:25:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3btfj$soe$1@panix1.panix.com>`
- **References:** `<l946c.26360$%06.10908@newsread2.news.pas.earthlink.net>`

```
In article <l946c.26360$%06.10908@newsread2.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>A follow-up on another thread.
>
>As the '85 (much less '74) Standard does not "define" syntax, I wanted to add my
>two (or more) cents to a discussion of what is and is not a "syntax error" in an
>'85 Standard conforming compiler.

How interesting... before considering this bit o' small change, Mr Klein, 
would you be so kind as to say *where* the syntax ('syntax' being used in 
the sense of '1 a : the way in which linguistic elements (as words) are 
put together to form constitutents (as phrases or clauses') *is* defined?  

Such a thing does not spring, fully-formed, from some Divine brow... or is 
it possible, then, that my example of 'PERFORM PARA-A THRU PARA-C IN ORDER 
GIVING RESULT-FIELD' is, in fact, syntactically valid?

(A quick web-search reveals that 'The vendor independent ANSI COBOL
committee legislates formal, non-vendor-specific syntax and semantic
language standards.' from 
http://www.csis.ul.ie/cobol/Course/COBOLIntro.htm ... but this is, 
admittedly, an intro-level course and such things might be taught as a 
matter of simplicity.)

DD
```

##### ↳ ↳ Re: Syntax ???

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-18T23:10:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D%p6c.47066$aT1.14038@newsread1.news.pas.earthlink.net>`
- **References:** `<l946c.26360$%06.10908@newsread2.news.pas.earthlink.net> <c3btfj$soe$1@panix1.panix.com>`

```
The following is from the 2002 ISO Standard (and really did NOT have an exact
equivalent in any eariler Standard).  There was actually a LOT of work done on
this set of wording - and it still doesn't really answer the question from the
other thread.

"5.2.1 Syntax rules
Syntax rules supplement general formats, identify equivalent words, and define
or clarify the order in which words or elements may be written to form larger
elements such as phrases, clauses, or statements. Syntax rules may also impose
restrictions on individual words or elements, relax restrictions implied by
words or elements, or define a term that may be used in the remaining syntax
rules.

The rules of the PICTURE clause specified in 13.16.38.5, Precedence rules, are
syntax rules.

When syntax rules specify that a word is synonymous with, an abbreviation for,
or equivalent to another word (or words), those words may be written
interchangeably and have the same meaning."

This definition was added (in part) because the 2002 Standard introduces a
totally new requirement (believe it or not) that a compiler MUST "flag" invalid
syntax.  The requirement is worded as follows:

"An implementation shall provide a warning mechanism that optionally can be
invoked by the user at compile time to indicate violations of the general
formats and the explicit syntax rules of standard COBOL. This warning mechanism
shall provide a suboption for selection or suppression of checking for
violations of the set of conformance rules specified in 14.7, Conformance for
parameters and returning items, and in 9.3.7.1.2, Conformance between
interfaces.

There are rules in standard COBOL that are not identified as general formats or
syntax rules, but nevertheless specify elements that are syntactically
distinguishable. This warning mechanism shall indicate violations of such rules.
For elements not specified in general formats or in explicit syntax rules, it is
left to the implementor's judgement to determine what is syntactically
distinguishable.

There are general rules in standard COBOL that could have been classified as
syntax rules. These rules are classified as general rules for the purpose of
avoiding syntax checking, and do not reflect errors in standard COBOL. An
implementation may, but is not required to, flag violations of such rules."

Another "relevant" quotation (for the original question) from the 2002 Standard
is:

"3.1.13 Limits
In general, standard COBOL specifies no upper limit on such things as the number
of statements in a compilation group or the number of operands permitted in
certain statements. A conforming implementation may place such limits. It is
recognized that these limits will vary from one implementation of standard COBOL
to another and may prevent the successful translation by a conforming
implementation of some compilation groups that meet the requirements of standard
COBOL."
```

###### ↳ ↳ ↳ Re: Syntax ???

- **From:** docdwarf@panix.com
- **Date:** 2004-03-18T19:11:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3ddqs$mn5$1@panix1.panix.com>`
- **References:** `<l946c.26360$%06.10908@newsread2.news.pas.earthlink.net> <c3btfj$soe$1@panix1.panix.com> <D%p6c.47066$aT1.14038@newsread1.news.pas.earthlink.net>`

```
In article <D%p6c.47066$aT1.14038@newsread1.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>The following is from the 2002 ISO Standard (and really did NOT have an exact
>equivalent in any eariler Standard).  There was actually a LOT of work done on
…[6 more quoted lines elided]…
>elements such as phrases, clauses, or statements.

This sounds remarkably close to the http://www.m-w.com definition of 
'syntax' as 'the way in which linguistic elements (as words) are put 
together to form constitutents (as phrases or clauses')'


>Syntax rules may also impose
>restrictions on individual words or elements, relax restrictions implied by
…[4 more quoted lines elided]…
>syntax rules.

This appears to agree with my response to Mr Willm in which I mentioned 
the data-type changing syntax (in that the target field of a COMPUTE must 
be numeric/numeric-edited).

>
>When syntax rules specify that a word is synonymous with, an abbreviation for,
…[5 more quoted lines elided]…
>syntax.

To hack up the annoying 'That was then, this is now'... this is now, what 
was that, then?  The COBOL mentioned by Mr Stevens is thirty years old... 
is it possible that there's been no standard of COBOL syntax ever, before 
now?

[snip]

>There are rules in standard COBOL that are not identified as general formats or
>syntax rules, but nevertheless specify elements that are syntactically
>distinguishable.

Here, at least, is a definite statement: there are rules in standard COBOL 
that are not identified as syntax rules.  It does not state whether there 
are rules in standard COBOL which *are* identified as syntax rules... so 
my question of 'where is the syntax of COBOL defined?' remains unanswered.

[snip]

>There are general rules in standard COBOL that could have been classified as
>syntax rules.

And once again... something that 'could have been classified as syntax 
rules'... but nothing about 'that which has been classified as syntax 
rules'.  (I am considering, at present, 'syntax' and 'syntax rules' to be 
equivalent terms given the citing from www.dictionary.com, AHD 2. Computer 
Science. The rules governing the formation of statements in a programming 
language)

Mr Klein has already asserted that neither the ANSI Standard of 1974 nor 
the ANSI Standard of 1985 "define" (quotations original) syntax... and my 
question of 'where, then *is* (or was) it defined?' seems still to be 
unanswered.  It would be *most* droll if no answer is found, if there is 
nothing which can be pointed to and described as 'there is where the 
syntax of COBOL is defined'...

... because if the syntax is undefined how, then, can anyone speak of a 
syntax error?

DD

><docdwarf@panix.com> wrote in message news:c3btfj$soe$1@panix1.panix.com...
>> In article <l946c.26360$%06.10908@newsread2.news.pas.earthlink.net>,
…[26 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
