[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL II Compiler Options

_7 messages · 6 participants · 1996-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### VS COBOL II Compiler Options

- **From:** "ccam..." <ua-author-17086113@usenetarchives.gap>
- **Date:** 1996-11-14T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56i9k4$pa@hacgate2.hac.com>`

```

Some of the postings related to standards checking have gotten into VS COBOL II
compiler options. We have the compiler, but it is underutilized (programmers
are still using OS/VS COBOL about 75% of the time).

We want to push the ratio way up (toward 100% VS COBOL II).

Yesterday, one programmer came by to ask about different results he was getting,
having compiled his existing (OS/VS) production program with VS COBOL II. We
tried NUMPROC(MIG) to get him equivalent results, and we _think_ it works.

Can anyone speak clearly about the options TRUNC and NUMPROC with respect to the
upgrade issue? Are there others that can affect equivalent results? I've tried
to study this and come up with a single solution, but I'm not there yet.

Does COBOL for MVS&VM change things in any way?

Thanks,
Colin Campbell
```

#### ↳ Re: VS COBOL II Compiler Options

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-11-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<56i9k4$pa@hacgate2.hac.com>`
- **References:** `<56i9k4$pa@hacgate2.hac.com>`

```

NUMPROC(MIG) is a fair approximation of OS/VS COBOL behavior but only an
approximation. For most code this provides probably 99%+
compatability.... but..... where the data involved in numberic
calculations will not pass IF NUMERIC all bets are off.

You should also be concerned with TRUNC. If OS/VS COBOL used NOTRUNC,
TRUNC(OPT) is a good approximation. If OS/VS COBOL used TRUNC, then
TRUNC(STD) is beleived to be identical. TRUNC(BIN) is only for some
special cases.

TRUNC and NUMPROC do not exhibit any known differences across COBOL II
R3.0 thru COBOL for MVS and VM.

A thorough discussion of this topic takes about 1/2 day (of a 3 or 3 1/2
day course) of lecture in "Planning COBOL MIgration" offered by Edge
Information Group, Inc (cg··.@i··.net).

Option control is CRITICAL, not only compile time but execution time,
including some hidden options only activiated by superzaps.

A single source program with a single file can be persuaded to exhibit
perhaps 192 different behaviors based only on compile time options.


Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

##### ↳ ↳ Re: VS COBOL II Compiler Options

- **From:** "arn burkhoff" <ua-author-9172704@usenetarchives.gap>
- **Date:** 1996-11-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a236da1c7b-p2@usenetarchives.gap>`
- **References:** `<56i9k4$pa@hacgate2.hac.com> <gap-a236da1c7b-p2@usenetarchives.gap>`

```

rwi··.@a··.com wrote:
› 
› NUMPROC(MIG) is a fair approximation of OS/VS COBOL behavior but only an
…[24 more quoted lines elided]…
› survive in a legacy based world.

Rex

Regarding the special hidden options only activated by superzaps. Would
you please post what they are and the zaps to activate them.

Thanks
Arn Burkhoff
```

#### ↳ Re: VS COBOL II Compiler Options

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1996-11-15T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<56i9k4$pa@hacgate2.hac.com>`
- **References:** `<56i9k4$pa@hacgate2.hac.com>`

```

Your assumption about NUMPROC(MIG) is correct and should continue with COBOL
for MVS etc. I went into this in more detail in a reply to one of the
postings on standards checking. You definitely should review all of the
compile options and the reasons behind them. You also should review the
differences manual and if you have a large inventory of programs your
organization should seriously consider one of the conversion packages.
Calculate 1-3 hours per program at the fully loaded salary rate or average
contractor rate for each program converted manually to see how much you can
afford to spend and still save money.
›  
› Some of the postings related to standards checking have gotten into VS   
…[24 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at morrisc.nbnet.nb.ca
```

#### ↳ Re: VS COBOL II Compiler Options

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-15T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<56i9k4$pa@hacgate2.hac.com>`
- **References:** `<56i9k4$pa@hacgate2.hac.com>`

```

cca··.@csc··c.com(Colin Campbell) wrote:

› Some of the postings related to standards checking have gotten into VS COBOL II 
› compiler options.  We have the compiler, but it is underutilized (programmers 
› are still using OS/VS COBOL about 75% of the time).
 
› We want to push the ratio way up (toward 100% VS COBOL II).
 
› Yesterday, one programmer came by to ask about different results he was getting,
› having compiled his existing (OS/VS) production program with VS COBOL II.  We 
› tried NUMPROC(MIG) to get him equivalent results, and we _think_ it works.
 
› Can anyone speak clearly about the options TRUNC and NUMPROC with respect to the
› upgrade issue?  Are there others that can affect equivalent results?  I've tried
› to study this and come up with a single solution, but I'm not there yet.
 
› Does COBOL for MVS&VM change things in any way?
 
› Thanks,
› Colin Campbell

I have two books by Harvey Bookman, on on COBOL II, and one on
COBOL/370 (which IBM is now calling COBOL for MVS and VM). According
to Bookman, all features of VS COBOL II release 3 and above work in
the same manner under COBOL/370.

With regard to NUMPROC options, NUMPROC(PFD) assumes that the
programmer is maintaining preferred signs in numeric data, and the
generated code does NOT do any sign fixup. This is according to
Bookman. NUMPROC(MIG) produces preferred signs only on the target
fields of MOVE statements and arithmetic statements. NUMPROC(NOPFD)
does sign fixup on both the sending and receiving fields.

I encountered at least one case where a program I wrote got a S0C7
abend when compiled with NUMPROC(MIG) but produced correct results
with the same data when compiled with NUMPROC(NOPFD).

I recommend using either NUMPROC(MIG) or NUMPROC(NOPFD). If you use
NUMPROC(PFD) the compiler will generate CLC instructions rather than
CP instructions, which would cause packed fields to compare unequal if
one is signed positive and the other is unsigned positive. X'123C'
would be less than X'123F', when a C(ompare) P(acked) instruction
would indicate the fields are arithmatically equal.

Bookman devotes a lot of time to discussing the various TRUNC options,
and basically says that TRUNC(BIN) is implemented inefficiently. He
seems to recommend TRUNC(OPT) as producing the most efficient code
with the least undesirable results. On page 266 of his COBOL/370 boo,
he has a sample of code used to test the three COBOL/370 TRUNC options
against OS/VS COBOL TRUNC and NOTRUNC options.

Based on my reading of those test results, TRUNC(STD) is equivalent to
OS/VS COBOL TRUNC, but neither TRUNC(OPT) nor TRUNC(BIN)
produce results identical to the OS/VS COBOL NOTRUNC option. So if
you want to emulate the old NOTRUNC option for CICS programs, you're
probably stuck with TRUNC(OPT).

TRUNC(STD) should always truncate the results to match the picture
clause.

Based on some bad experiences we had when migrating to COBOL II, I
recommend using the PROCESS or CBL statements to embed the
compile-time options in your source code prior to the IDENTIFICATION
DIVISION statement. This will guarantee that you get repeatable
results even if the source listing is lost.

I hope this helps!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: VS COBOL II Compiler Options

- **From:** "arn burkhoff" <ua-author-9172704@usenetarchives.gap>
- **Date:** 1996-11-16T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a236da1c7b-p5@usenetarchives.gap>`
- **References:** `<56i9k4$pa@hacgate2.hac.com> <gap-a236da1c7b-p5@usenetarchives.gap>`

```

Regarding the Cobol II NUMPROC(MIG) option. MIG is short for migrate,
which means the compiler works like the older IBM compilers with regards
to packed (comp-3) field data. If the PFD (preferred sign option) is
selected one of the packed field signs is no longer acceptable and you
bomb out reading a file with the non-preferred sign on any packed field.
Not a healty situation for a shop with a mixed bag of older cobol, COBOL
II and assembler programs. I am unsure what NOPFD does at the moment
becuase I don't have a manual here at home.

TRUNC effects the generation of code for binary fields. I settled on
TRUNC(OPT) and s9(8) not s9(9) for comp fields after finding some very
nasty code generated by the COBOL II compiler with other TRUNC options.
OPT generates the least code but does no checking for overflows. BTW
checking for overflows caused a simple "add 1 to a comp-field" statement
to generate well over twenty instructions including divides and
multiplies. I could hardly beleive my eyes when I looked at the
generated code! The solution we used ( TRUNC(OPT) and s9(8) comp fields
) came directly from IBM.

BTW I only found this because I was working on a client project to build
an online Automatic Teller Machine message processing system and I was
very concerned about the code generated by the ISO-8583 message
explosion module I wrote in COBOL. I wanted it to be as efficient as
possible. (Please don't tell me I should have done it in assembler, who
would maintain it and the final CObol II code is actually quite
efficient) I was generating the Assembler map and verifying the
generated code. I was also very surprised how a simple change from a
COMPUTE to an ADD or SUBTRACT would sometimes change the generated code.

Arn Burkhoff
Warren, NJ
```

##### ↳ ↳ Re: VS COBOL II Compiler Options

- **From:** "djwi..." <ua-author-17086964@usenetarchives.gap>
- **Date:** 1996-11-21T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a236da1c7b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a236da1c7b-p5@usenetarchives.gap>`
- **References:** `<56i9k4$pa@hacgate2.hac.com> <gap-a236da1c7b-p5@usenetarchives.gap>`

```

In article <56k2nl$e.··.@mti··t.net>,
arn··.@wor··t.net says...
› 
› cca··.@csc··c.com(Colin Campbell) wrote:
…[5 more quoted lines elided]…
› etc....
The specific problem I ran into was the old program had a series
of condition steps with IF ELEMENT NOT +0. Problem was, even though the
field was signed, the data coming in wasn't. It was haphazard whether a zero
was a hex 'C0', 'D0', or 'F0'.

To make matters worse, even recompiling the original program as OS/VS with our
upgraded Capex compiler caused the program to deliver slightly different results
(although it appears to be in a different area of the program dealing with a table lookup).

The original program is about 15 years old, with maintenance work about every 3
years. And yes, I would have liked to completely rewrite the sucker, but I was working
under a deadline.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
