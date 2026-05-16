[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL QUESTION

_7 messages · 7 participants · 1998-10_

---

### COBOL QUESTION

- **From:** skyraven@home.com (Sue L)
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362b65a5.5133357@news>`

```
Could someone please explain to me what an Operand error is? I have
looked through my text book that I'm working with at the college and
it's not explaining it to where it's actually making any sense. I'm
getting errors and it's driving me batty... someone care to take a
stab at this one?

Sue
```

#### ↳ Re: COBOL QUESTION

- **From:** SkidMike <skidmike@mindspring.com>
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362BC17A.549C48FF@mindspring.com>`
- **References:** `<362b65a5.5133357@news>`

```
what line did you get the error in?  i get them all the time in
arithmetic operations.
```

#### ↳ Re: COBOL QUESTION

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362b664d.0@news1.ibm.net>`
- **References:** `<362b65a5.5133357@news>`

```

Sue L wrote in message <362b65a5.5133357@news>...
>Could someone please explain to me what an Operand error is? I have
>looked through my text book that I'm working with at the college and
>it's not explaining it to where it's actually making any sense. I'm
>getting errors and it's driving me batty... someone care to take a
>stab at this one?


Sue,
always include the code or code snippet with the error.
From the meager information you supplied, I'll guess
that you have forgotten to place spaces on either side
of and operator (such as "+"), e.g.: compute a=b+1
is not valid, but compute a =  b  +  1 is
```

#### ↳ Re: COBOL QUESTION

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-6hTRNdieSMIy@Dwight_Miller.iix.com>`
- **References:** `<362b65a5.5133357@news>`

```
On Mon, 19 Oct 1998 16:08:39, skyraven@home.com (Sue L) wrote:

> Could someone please explain to me what an Operand error is? I have
> looked through my text book that I'm working with at the college and
…[3 more quoted lines elided]…
> 

I can think of several - can you post an example error message?
```

#### ↳ Re: COBOL QUESTION

- **From:** jyazel@freenet.columbus.oh.us (Jack Yazel)
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70fvq6$bru@login.freenet.columbus.oh.us>`
- **References:** `<362b65a5.5133357@news>`

```
Sue L (skyraven@home.com) wrote:
: Could someone please explain to me what an Operand error is? I have
: looked through my text book that I'm working with at the college and
: it's not explaining it to where it's actually making any sense. I'm
: getting errors and it's driving me batty... someone care to take a
: stab at this one?
: Sue
   --------------------------

  The COBOL verbs (such as MOVE, ADD, MULTIPLY, etc.) generally
require additional information to complete successfully. The 
additional pieces of information are called operands.

  In addition, if you are making external calls, one or more
operands may be required.

  For instance, MOVE NAME TO LAST-NAME.

  MOVE is the verb.

  NAME is an operand and LAST-NAME is an operand.

  TO just makes the statement more readable.
```

#### ↳ Re: COBOL QUESTION

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70g1ea$4ja$1@news.igs.net>`
- **References:** `<362b65a5.5133357@news>`

```

Sue L wrote in message <362b65a5.5133357@news>...
>Could someone please explain to me what an Operand error is? I have


Hard to tell without code, but I would guess that you have something
like "-1" in an arithmetic expression. When there is no space, the
compiler interprets it as a sign (as opposed to a "subtract"), thus there
is no operand.
```

#### ↳ Re: COBOL QUESTION

- **From:** "Dennis Gapper" <dgapper@bigpond.com>
- **Date:** 1998-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362ef212.0@139.134.5.33>`
- **References:** `<362b65a5.5133357@news>`

```
Can u say if this is a compiler error message or a runtime error?  If the
latter, then the data in an operand field is at fault - very often as a
result of redefining fields as numeric/alphanumeric, and not being careful
with the contents.

Sue L wrote in message <362b65a5.5133357@news>...
>Could someone please explain to me what an Operand error is? I have
>looked through my text book that I'm working with at the college and
…[4 more quoted lines elided]…
>Sue
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
