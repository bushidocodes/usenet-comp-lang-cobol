[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VM/ESA data exception error

_6 messages · 6 participants · 1996-10_

---

### VM/ESA data exception error

- **From:** "jl..." <ua-author-17072453@usenetarchives.gap>
- **Date:** 1996-10-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0_0/0_0_26fe4420@fidonet.org>`

```


Hello,

The following code works well with the student version of
the RM McFarland Cobol-85 dos compiler as well as with
Visual Age for COBOL for OS/2 :

COMPUTE DISCOUNT-CNTR = DISCOUNT-CNTR +
INVOICE-AMOUNT-IN * DISCOUNT-RATE-IN.
COMPUTE TOTAL-AMOUNT-TMP = INVOICE-AMOUNT-IN -
INVOICE-AMOUNT-IN * DISCOUNT-RATE-IN.

It crases on the first record, I did move
spaces to all the counters to make sure they
were clear.

However, on a VM/ESA 9120 using IBM COBOL for VSE/ESA 1.1.0
it crashes the program with a data exception error. It appears to be the "*" sign that does it, because it works fine if
I change that sign to a "+". I am really curious why it
works/runs on the other two systems, but can't work on the
VM/ESA system. Can anyone explain this to me?

Another question: Is it possible to set up either the
RM McFarland dos compiler and run time or the Visual Age
for COBOL for OS/2 to act and treat the source code
and object code exactly as the VM/ESA mainframe would?
It would be really advantageous if I could find these
differences at home rather than waste so much valuable
computer lab time at school tracking down the reason
a program crashes.


Thanks in advance.


Greetings,
joe



--- timEd/2 1.10
* Origin: 0 (0:0/0)
```

#### ↳ Re: VM/ESA data exception error

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-10-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad06f7dd0f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_26fe4420@fidonet.org>`
- **References:** `<0_0/0_0_26fe4420@fidonet.org>`

```

In <0_0/0_0··.@fid··t.org>, jl··.@pro··g.net writes:
› 
› Hello,
…[12 more quoted lines elided]…
› were clear.
 
› You should move ZEROES rather than SPACES to the counters.
 
› 
› However, on a VM/ESA 9120 using IBM COBOL for VSE/ESA 1.1.0
…[3 more quoted lines elided]…
› VM/ESA system. Can anyone explain this to me?
```

##### ↳ ↳ Re: VM/ESA data exception error

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad06f7dd0f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad06f7dd0f-p2@usenetarchives.gap>`
- **References:** `<0_0/0_0_26fe4420@fidonet.org> <gap-ad06f7dd0f-p2@usenetarchives.gap>`

```

lsv··.@i··.net wrote in article <54vphc$25v0$1.··.@new··m.net>...
› In <0_0/0_0··.@fid··t.org>, jl··.@pro··g.net writes:
›› The following code works well with the student version of
…[6 more quoted lines elided]…
›› . Can anyone explain this to me?

IBM has, through the ages, required numeric items to actually contain
numeric data when used as operands of numeric operations. However,
RM/COBOL and its predecessors (many, many minicomputers of the 70's and
80's ran a variant of what became RM/COBOL) has always been more tolerant,
because toleration took less memory in those memory constrained days.

RM/COBOL-85 originally enforced the IBM rules. The designers actually
thought this to be a good idea. However, our customers soon persuaded us
that compatibility with RM/COBOL was more important, since they had many
data files with 'dirty' numeric data. So, we changed the behavior of
RM/COBOL-85 to match that of RM/COBOL.

[I can't speak for VisualAge for COBOL.]


Tom Morrison, T.M··.@li··t.com
Liant Software Corp
512-719-7019  FAX:512-719-7070  WWW: http://www.liant.com/
```

###### ↳ ↳ ↳ Re: VM/ESA data exception error

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad06f7dd0f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad06f7dd0f-p3@usenetarchives.gap>`
- **References:** `<0_0/0_0_26fe4420@fidonet.org> <gap-ad06f7dd0f-p2@usenetarchives.gap> <gap-ad06f7dd0f-p3@usenetarchives.gap>`

```

Tom Morrison wrote:
› 
›› You should move ZEROES rather than SPACES to the counters.
…[12 more quoted lines elided]…
› RM/COBOL-85 to match that of RM/COBOL.

The next standard resolves this quandry by providing exception
checking. The user can tell the compiler to trap references to such
stuff by using the TURN directive - as in ">>TURN EC-DATA-INCOMPATIBLE
CHECKING ON". Using this, the code is portable across any
implementation. Without using it, the implementor is free to do what
he wants to with bad data. In my opinion, being "tolerable" is a
really bad idea. This can cause all kinds of disasters.
Unfortunately, my implementation is somewhat tolerable. Basically a
mistake on my part.

As another aside, I wrote a proposal to make MOVE SPACES TO
numeric-item illegal in the standard. The rule is that the figurative
constant has to have a numeric value. It passed ANSI X3J4 and is now
being voted on at the ISO level (WG4). The arguments against is are
basically that it used to work (you got garbage data) so it should
keep on working rather than produce a diagnostic.

Another common error people make is MOVE ZEROS TO a-group-item where
the group contains non-DISPLAY items. This can also wreak havoc.
However, nothing can be done about that.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: VM/ESA data exception error

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad06f7dd0f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_26fe4420@fidonet.org>`
- **References:** `<0_0/0_0_26fe4420@fidonet.org>`

```

In message <<0_0/0_0··.@fid··t.org>> jl··.@pro··g.net writes:
› Hello,
› 
…[11 more quoted lines elided]…
› were clear.

Spaces ? Numeric items should be set to ZERO before being added
into. Some run-times may cater for space filled DISPLAY NUMERIC
fields by treating them as having a zero value but this should
not be relied on.
```

#### ↳ Re: VM/ESA data exception error

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad06f7dd0f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_26fe4420@fidonet.org>`
- **References:** `<0_0/0_0_26fe4420@fidonet.org>`

```

jl··.@pro··g.net wrote:


› Hello,
 
› The following code works well with the student version of
› the RM McFarland Cobol-85 dos compiler as well as with
› Visual Age for COBOL for OS/2 :
 
›      COMPUTE DISCOUNT-CNTR = DISCOUNT-CNTR +
›          INVOICE-AMOUNT-IN * DISCOUNT-RATE-IN.
›      COMPUTE TOTAL-AMOUNT-TMP = INVOICE-AMOUNT-IN -
›          INVOICE-AMOUNT-IN * DISCOUNT-RATE-IN.
 
› It crases on the first record, I did move
› spaces to all the counters to make sure they
› were clear.

You got lucky.

Move zero not space. You probably got a low-level diagnostic.

JR


and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
