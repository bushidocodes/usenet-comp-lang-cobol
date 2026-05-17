[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q:What was Cobol 88 called?

_7 messages · 7 participants · 1997-07_

---

### Q:What was Cobol 88 called?

- **From:** "dr..." <ua-author-5745961@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`

```

Does anyone know what the technical term is for a COBOL Level 88? It seems
there was a name for it like "Working Storage Boolean Constant" or some similar
nonsense. Someone asked me this question yesterday and I couldn't remember the
answer. It's been at least 6 years since I coded any COBOL, so I'm more than a
little rusty.

Dave Rupp
Texas Instruments
Dallas, Texas USA
dr··.@t··.com
http://www.ti.com/
```

#### ↳ Re: Q:What was Cobol 88 called?

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`

```

Dave Rupp wrote:
› 
› Does anyone know what the technical term is for a COBOL Level 88?  It seems
…[9 more quoted lines elided]…
› http://www.ti.com/



A level-88 identifies a condition name entry that is associated with a
particular value for the conditional variable. For example:

01 COLOR-TYPE PIC X.
88 BLUE VALUE "1".
88 RED VALUE "2".
88 YELLOW VALUE "3".

When coding an IF statement, the sentence can be written as:

IF BLUE
PERFORM ....
ELSE
IF RED
PERFORM ...
Etc....

This same thing can be coded as:

IF COLOR-TYPE = "1"
PERFORM
ELSE
IF COLOR-TYPE = "2"
PERFORM
Etc...


Mike Dodas
```

##### ↳ ↳ Re: Q:What was Cobol 88 called?

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-07-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c0b70b8ac6-p2@usenetarchives.gap>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com> <gap-c0b70b8ac6-p2@usenetarchives.gap>`

```

Dave Rupp wrote:
› 
› Does anyone know what the technical term is for a COBOL Level 88?  It seems
…[3 more quoted lines elided]…
› little rusty.

I should look it up, but I've got no manual to hand. From memory
though, I seem to recall that they are called "condition names".

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

#### ↳ Re: Q:What was Cobol 88 called?

- **From:** "gtru..." <ua-author-17071275@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`

```

On 21 Jul 1997 13:45:20 GMT, dr··.@t··.com (Dave Rupp) wrote:

› Does anyone know what the technical term is for a COBOL Level 88?  It seems
› there was a name for it like "Working Storage Boolean Constant" or some similar
…[9 more quoted lines elided]…
› 
It's a condition name. The variable it's associated with is a
conditional variable.

George Trudeau
```

#### ↳ Re: Q:What was Cobol 88 called?

- **From:** "bowil..." <ua-author-6589065@usenetarchives.gap>
- **Date:** 1997-07-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`

```

dr··.@t··.com (Dave Rupp) wrote:

› Does anyone know what the technical term is for a COBOL Level 88?  It seems
› there was a name for it like "Working Storage Boolean Constant" or some similar
…[9 more quoted lines elided]…
› 
Both my Welburn and IBM books calls 88-level items "Condition-Names".
As IBM defines it on page 550 in the "COBOL Language Reference":

"A user-defined word that assigns a name to a subset of values that
a conditional variable may assume; or a user-defined word assigned to
a status of an implementor defined switch or device. When
"condition-name" is used in the general formats, it represents a
unique data item reference consisting of a systactically correct
combination of a "condition-name", together with qualifiers and
subsripts, as required for uniqueness of reference."

It is used with a "conditional variable" defined in IBM as:

"A data item one or more values of which has a condition-name
assigned to it."

Together, the condition-name and condition variable are used in a
"condition-name condition" defined as in the same book as:

"The proposition, for which a truth value can be determined, that
the value of a conditional variable is a member of the set of values
attributed to a condition-name associated with the conditional
valiable."

Heeyyy, it's real simple,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

##### ↳ ↳ Re: Q:What was Cobol 88 called?

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-07-21T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c0b70b8ac6-p5@usenetarchives.gap>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com> <gap-c0b70b8ac6-p5@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
› dr··.@t··.com (Dave Rupp) wrote:
…[57 more quoted lines elided]…
› '---------------------------------------------------------------------'
Anyone I ever talked to just called it an "88-Level" (noun), as in:
"Why don't you just define a new 88-Level?"
Cheers :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Q:What was Cobol 88 called?

- **From:** "greg ferro" <ua-author-1009304@usenetarchives.gap>
- **Date:** 1997-07-22T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c0b70b8ac6-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`
- **References:** `<5qvp5g$jvc$1@tilde.csc.ti.com>`

```

A level 88 entry is called a "Condition Name".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
