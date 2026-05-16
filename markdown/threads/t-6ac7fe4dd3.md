[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Alphabets

_60 messages · 10 participants · 2003-06_

---

### Re: Alphabets

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-13T10:27:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com>`

```
I left out a few words.

For

> If the problem is that all pre-Realia PC COBOL compilers produced
> intermediate code of some sort that was subsequently interpreted, it
doesn't
> seem to me that the language the program that produced that intermediate
> code is particularly relevant to the question of the performance of that
> code.

:Let's try:

If the problem is that all pre-Realia PC COBOL compilers produced
intermediate code of some sort that was subsequently interpreted, it doesn't
seem to me that the source language in which the program that produced that
intermediate code was written is particularly relevant to the question of
the performance of that code.

    -Chuck Stevens
```

#### ↳ Re: Alphabets

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-13T18:03:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcd3l0$sfu$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com>`

```
In order to really test the Report Writer feature of CoBOL, that part of the
compiler needs to be created with the Report Writer feature of CoBOL.

I like it when hammer manufacturers make hammers out of hammers as well.   If a
bicycle is a tool, then the best ones need to be made from bicycles.
```

##### ↳ ↳ Re: Alphabets

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-13T11:41:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcd5th$2tsd$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcd3l0$sfu$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bcd3l0$sfu$1@peabody.colorado.edu...
> In order to really test the Report Writer feature of CoBOL, that part of
the
> compiler needs to be created with the Report Writer feature of CoBOL.
>
> I like it when hammer manufacturers make hammers out of hammers as well.
If a
> bicycle is a tool, then the best ones need to be made from bicycles.

A better simile, I think:

if a hammer is a tool, then the *only* tool appropriate for use in
hammer-making is the hammer.

If a bicycle is a tool, then the *only* tool appropriate for use in
bicycle-making is a bicycle.

    -Chuck Stevens
```

#### ↳ Re: Alphabets

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-14T07:06:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eeac912.236758765@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>I left out a few words.
>
…[15 more quoted lines elided]…
>the performance of that code.

mbp was pre-Realia and it produced native code.
```

##### ↳ ↳ Re: Alphabets

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-16T11:01:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcl0mm$27n2$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3eeac912.236758765@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
…[7 more quoted lines elided]…
> >> seem to me that the language the program that produced that
intermediate
> >> code is particularly relevant to the question of the performance of
that
> >> code.
> >
…[3 more quoted lines elided]…
> >intermediate code of some sort that was subsequently interpreted, it
doesn't
> >seem to me that the source language in which the program that produced
that
> >intermediate code was written is particularly relevant to the question of
> >the performance of that code.
>
> mbp was pre-Realia and it produced native code.

And what's the point?

If its object code was inefficient it's because the author(s) of the
compiler didn't generate the machine instructions in a sequence conducive to
efficiency.  It could have been that the authors didn't know what
constituted efficient code.  It could have been that the authors didn't know
how to organize the compiler in such a fashion as to foster the generation
of efficient code.   But if the optimal code for a MOVE SPACES to a 27-byte
transfer looks something like B05002A61004B21BE6 on a given machine, I'd
defy anyone to detect whether that B05002A61004B21BE6 was generated using a
program written in ALGOL, Pascal, RPG, APL, Philco 2000 ALTAC, Burroughs
Assembler for the L2000 Accounting Machine, or Interdata machine code
entered through the console switches as a cross-compiler, either by
examination of the operator sequence itself or by timing repeated executions
of it.   The ability, or inability, of a compiler to generate efficient code
is completely orthogonal to the language in which that compiler is written.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-17T06:30:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eeeaedd.207409527@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3eeac912.236758765@news.optonline.net...
…[42 more quoted lines elided]…
>is completely orthogonal to the language in which that compiler is written.

Your point is valid but, as a minor quibble, I've found it's usually easy to
tell what language an executable was written in. Not from one move instruction,
rather from the library functions it calls, the way it controls loops or the way
it calls local functions. For instance, if it shares memory with and doesn't
pass parameters to local functions, it is COBOL. If local variables are all on
the stack, it probably was written in  C or Pascal.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-17T07:32:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcn8ql$p5o$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eeeaedd.207409527@news.optonline.net...

> Your point is valid but, as a minor quibble, I've found it's usually easy
to
> tell what language an executable was written in.

Irrelevant to your point, and irrelevant to my point.  We are discussing
what language the compiler that compiled the program was written in, not
which language the program itself was written in.  Can you tell from the way
a printed COBOL report is formatted which language the compiler that
compiled the program that produced the report was written in?  I can't,
because the report is formatted according to COBOL rules.  Same with
executable.

> Not from one move instruction,
> rather from the library functions it calls, the way it controls loops or
the way
> it calls local functions. For instance, if it shares memory with and
doesn't
> pass parameters to local functions, it is COBOL. If local variables are
all on
> the stack, it probably was written in  C or Pascal.

Really?   Are you sure that's a universal rule?  Everything's on the stack,
one way or another, in our environment, and CALLs to nested COBOL programs
that have the extension-predecessor-synonym to RETURNING  clauses are
indistinguishable from CALLs to valued nested procedures in ALGOL or Pascal
programs.   It's true that you might be able to tell what language a
compiler was written in by the way it handles *some* of these things, but
it's not true that you can tell what language the compiler was written in by
the output produced by a program compiled by it.

To paraphrase the immortal description of the mythical Fitchew sports car by
Dick O'Kane, this description may Fitchew but it definitely doesn't Fitme.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-18T00:42:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eefb101.273503437@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[8 more quoted lines elided]…
>which language the program itself was written in. 

I didn't know. I thought we were discussing the source program. 

I agree that you can't tell what language the compiler was written in. Possible
exception, if you see a SEARCH on an array of bytes rendered as single
instruction 'repne scasb', you can be pretty sure the compiler writers rendered
it to intermediate code correctly, and back-end writers understood the intent.
If the compiler had been written in another language, the semantics would have
been lost in translation. 

> Can you tell from the way
>a printed COBOL report is formatted which language the compiler that
>compiled the program that produced the report was written in?  I can't,
>because the report is formatted according to COBOL rules.  Same with
>executable.

Agreed.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-18T07:15:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcps5k$2k7l$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3eefb101.273503437@news.optonline.net...

> >Irrelevant to your point, and irrelevant to my point.  We are discussing
> >what language the compiler that compiled the program was written in, not
> >which language the program itself was written in.
>
> I didn't know. I thought we were discussing the source program.

You did?  Why would you think that?  This particular subthread began with
the premise that our RPG compiler should have been written in RPG rather
than ALGOL.

> I agree that you can't tell what language the compiler was written in.
Possible
> exception, if you see a SEARCH on an array of bytes rendered as single
> instruction 'repne scasb', you can be pretty sure the compiler writers
rendered
> it to intermediate code correctly, ...

What intermediate code?  All of our compilers produce executable object code
directly.

> and back-end writers understood the intent.

What back-end writers?

> If the compiler had been written in another language, the semantics would
have
> been lost in translation.

Semantics of what?  If a compiler produces executable object code, the
semantics of the original language, as well as the conformance of the
executable object code to good practice, are matters entirely within the
purview of the compiler writer.  Parsing of source code and generation of
object code may be in different parts of the compiler, but they're not
inherently separate components.

We do have a set of compilers that shares an object code generator module,
but the folks that work on that object code generator are the same folks
that work on all of the language parsers that use it, and the boundary
between the parser and the object code generator is invisible to the end
user of the compilers; it appears monolithic at that level.

Are you laboring under the assumption that all compilers generate
intermediate code that is then turned into executable by some other process?
If so, you are indeed laboring under an incorrect assumption.  Some do;
perhaps even *many* do, but by no means *all*.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-18T16:39:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef08efb.330337761@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[30 more quoted lines elided]…
>Semantics of what?  

Semantics of the SEARCH verb. If the front-end had turned it into a loop, the
back-end would have generated code for a loop.

>If a compiler produces executable object code, the
>semantics of the original language, as well as the conformance of the
…[9 more quoted lines elided]…
>user of the compilers; it appears monolithic at that level.

At compiler companies I'm familiar with, there are two programming groups. The
front-end folks work in a high level language; the back-end folks work in
assembly or a low level language. MetroWerks, whose Code Warrior compiles C to
many many cpus, mostly imbedded, has three back-end groups -- one for CISC, one
for RISC, and one for TI processors. 

The separation between front- and back-end is obvious with Java, .Net and Micro
Focus.

>Are you laboring under the assumption that all compilers generate
>intermediate code that is then turned into executable by some other process?
>If so, you are indeed laboring under an incorrect assumption.  Some do;
>perhaps even *many* do, but by no means *all*.

Thanks for the info about Unisys.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-18T17:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcq75v$1sf$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net>`

```

On 18-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> >> If the compiler had been written in another language, the semantics would
> >> have been lost in translation.
…[4 more quoted lines elided]…
> back-end would have generated code for a loop.

You're making less and less sense to me at each iteration of this thread.  
Programming is about getting the requirements, making the design, coding, and
testing.   The requirements of implementing the SEARCH verb are more clear and
less ambiguous than most business rules requirements that a typical programmer
comes across.

Once I have the requirements, I can use whatever tool makes sense to implement
them.   If I don't do the analysis but instead guess what is wanted, then it
helps to be fluent in the user's tools to make a good guess.   But such a
compiler writer won't be in business long.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-19T09:06:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef16e60.51799416@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 18-Jun-2003, robert@wagner.net (Robert Wagner) wrote:
…[13 more quoted lines elided]…
>comes across.

You just described the application development process. In systems programming,
there is more art. You're not writing *A* single program, you're writing a layer
in a larger hierarchy. In the instant case, you're translating a SEARCH into
intermediate code which will eventually produce machine language. The only hard
and fast Requirement is that it works according to the COBOL standard. Internal
details of *how* it works are up to you. If you disdain the language, you'll do
it sloppily; if you love the language, you'll do it right. 

>Once I have the requirements, I can use whatever tool makes sense to implement
>them.   If I don't do the analysis but instead guess what is wanted, then it
>helps to be fluent in the user's tools to make a good guess.   But such a
>compiler writer won't be in business long.

Longevity is most often a function of business and marketing, not logic. We
programmers are pawns on the chess board of life.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-19T14:55:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcsitc$84u$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net>`

```

On 19-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> You just described the application development process. In systems
> programming,
…[8 more quoted lines elided]…
> do it sloppily; if you love the language, you'll do it right.

What makes writing the code to do a SEARCH command in a compiler different from
writing the code to write a piece of business code in any other integrated
system?

I suppose the big difference is in that the SEARCH command is very well defined.
  Another difference is that it certainly will be designed in easy to use
components.   But once the programmer writes his code to match the definitions,
it doesn't matter whether he knows how programmers use that word.   In fact, we
have seen that programmers sometimes have mistaken ideas about how a CoBOL
command is supposed to work.  If they use their "common sense" concept about how
it works instead of the published specs, the code won't work right for anybody
except themselves.

There are times when we can be too familiar with the way we do things - enough
so that our biases cause us to not conform to the specs.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-20T01:03:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef24124.105763852@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 19-Jun-2003, robert@wagner.net (Robert Wagner) wrote:
…[15 more quoted lines elided]…
>system?

Because systems software has more room for creativity. There are many ways to do
a SEARCH, all within the Requirements. 

>I suppose the big difference is in that the SEARCH command is very well
defined.
>  Another difference is that it certainly will be designed in easy to use
>components.   

Forget components. The fastest solution is in-line code, preferably one machine
language instruction. That's do-able on an Intel processor.  

>But once the programmer writes his code to match the definitions,
>it doesn't matter whether he knows how programmers use that word.   In fact, we
>have seen that programmers sometimes have mistaken ideas about how a CoBOL
>command is supposed to work.  If they use their "common sense" concept about
how
>it works instead of the published specs, the code won't work right for anybody
>except themselves.

I've seen those claims on CLC, but not in real life. Real world programmers do
read the published specs.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-20T07:50:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcv70i$c4c$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net>`

```

Howard Brazee wrote:

> >I suppose the big difference is in that the SEARCH command is very well
> defined.
> >  Another difference is that it certainly will be designed in easy to use
> >components.

Robert Wagner countered:

> Forget components. The fastest solution is in-line code, preferably one
machine
> language instruction. That's do-able on an Intel processor.


What single Intel instruction would you generate for either of the following
two SEARCH statements:

search A varying SOME-INDEX at end perform SEARCH-DONE
when Z = B or C or > D or < E perform FIRST-CONDITION
when Y > F or G or < H or = I perform SECOND-CONDITION
end-search

SEARCH ALL A at end perform SEARCH-DONE
when Z EQUAL B AND Y = I perform FIRST-CONDITION
end-search

> >But once the programmer writes his code to match the definitions,
> >it doesn't matter whether he knows how programmers use that word.   In
fact, we
> >have seen that programmers sometimes have mistaken ideas about how a
CoBOL
> >command is supposed to work.  If they use their "common sense" concept
about
> how
> >it works instead of the published specs, the code won't work right for
anybody
> >except themselves.
>
> I've seen those claims on CLC, but not in real life. Real world
programmers do
> read the published specs.

Given that many of your assertions about what the standards have said over
the past few months (particularly early on in your participation in this
forum) have been directly refuted by simple quotations from those standards,
it appears that you've finally, and explicitly, acknowledged that you are
not a member of any group that could be termed "real world programmers".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-20T21:41:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef351cc.16220282@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bcv70i$c4c$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>Howard Brazee wrote:
>
…[21 more quoted lines elided]…
>end-search

A single machine instruction (e.g. IBM's TRT or Intel's scasb) can be used only
if the program is looking for equal in a table of bytes. Searching for a
delimiter or TRUE indicator is a fairly common use of SEARCH. 

FWIW, your SEARCH ALL wouldn't compile. Its conditional can only look for an
equal in A. 

>Given that many of your assertions about what the standards have said over
>the past few months (particularly early on in your participation in this
>forum) have been directly refuted by simple quotations from those standards,
>it appears that you've finally, and explicitly, acknowledged that you are
>not a member of any group that could be termed "real world programmers".

In the real world, I'd look it up if I wasn't sure. I've learned to do that here
as well.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-23T14:40:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd73hk$5tf$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net>`

```

On 19-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> >What makes writing the code to do a SEARCH command in a compiler different
> >from
…[4 more quoted lines elided]…
> do a SEARCH, all within the Requirements.

So are you implying that when writing business code in any other integrated
system, there is less room for creativity, with not so many ways to solve their
needs, all within the Requirements?

And because applications programmers do not have this room, we don't need to
understand the system as much as compiler writers?

If this is what you're implying, could you please back up your explanation one
level and tell us what is the cause of this difference?   Please direct your
explanation to someone like myself who is so ignorant that I haven't noticed
this lack of room.


> >But once the programmer writes his code to match the definitions,
> >it doesn't matter whether he knows how programmers use that word.   In fact,
…[8 more quoted lines elided]…
> read the published specs.

That has been my impression as well - in which case, the SEARCH command can be
designed with whatever tool does the SEARCH command well - and that previous
CoBOL knowledge is not needed.   The specs will tell the compiler writer what is
needed.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-23T17:10:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef72409.34745107@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bd73hk$5tf$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 19-Jun-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[10 more quoted lines elided]…
>needs, all within the Requirements?

When writing business application code, I avoid creativity unless there is a
legitimate need. My goal is clarity to the next programmer. When I do have to
get fancy, usually for speed, I isolate that section of code and write comments
explaining what it's doing and why. 

>And because applications programmers do not have this room, we don't need to
>understand the system as much as compiler writers?

What are you responding to? I said nothing about understanding the system.


>> >But once the programmer writes his code to match the definitions,
>> >it doesn't matter whether he knows how programmers use that word.   In fact,
…[7 more quoted lines elided]…
>> I've seen those claims on CLC, but not in real life. Real world programmers
do
>> read the published specs.
>
>That has been my impression as well - in which case, the SEARCH command can be
>designed with whatever tool does the SEARCH command well - and that previous
>CoBOL knowledge is not needed.   The specs will tell the compiler writer what
is
>needed.

Specs define expected results; they don't tell you how to achieve those results.
More importantly, they don't tell you which operations should be optimized
because they are frequently used, and which aren't worth the effort. An
experienced Cobol programmer knows that; a compiler author who has not written
Cobol would not know that. 

Using SEARCH as an example, a non-Cobol programmer would see the full syntax in
the standard and write code to compile it. A Cobol programmer would  know that
90% of SEARCHes will look for an equal on one key, therefore that case warrants
optimization and the others don't.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-23T12:58:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd7f4s$1b5$1@slb2.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bd73hk$5tf$1@peabody.colorado.edu> <3ef72409.34745107@news.optonline.net>`

```
For those not familiar with comp.lang.cobol,
     Check google for the accuracy track-record of this poster (R. Wagner) -
and the <lack of> regard with which most of his comments are viewed by many
in this newsgroup before reading his post below.

NOTE Well -
   This note has nothing to do with "Alphabets" (as left in the subject).

Also note (in particular) unsubstantiated generalizations/statements such as

 - "because applications programmers do not have this room ..."
 - "Specs define expected results; they don't tell you how to achieve those
results. ... An  experienced Cobol programmer knows that; ..."
 - "A Cobol programmer would  know that 90% of SEARCHes will look for an
equal on one key ..."
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-23T20:33:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd7o5v$f20$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bd73hk$5tf$1@peabody.colorado.edu> <3ef72409.34745107@news.optonline.net>`

```

On 23-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> When writing business application code, I avoid creativity unless there is a
> legitimate need. My goal is clarity to the next programmer. When I do have to
> get fancy, usually for speed, I isolate that section of code and write
> comments explaining what it's doing and why.

So a compiler writer doesn't expect anyone will want to maintain his code?  He
will get fancy without legitimate need, eschewing comments?


> >And because applications programmers do not have this room, we don't need to
> >understand the system as much as compiler writers?
>
> What are you responding to? I said nothing about understanding the system.

OK, be familiar with the system (in the case of a compiler writer, the system is
CoBOL).
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-24T07:42:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef7fd06.90302963@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bd73hk$5tf$1@peabody.colorado.edu> <3ef72409.34745107@news.optonline.net> <bd7o5v$f20$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 23-Jun-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[6 more quoted lines elided]…
>will get fancy without legitimate need, eschewing comments?

He can assume the maintainer has a higher level of competence. I comment code
that's not obvious to me.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-24T14:04:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd9loq$krj$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcq75v$1sf$1@peabody.colorado.edu> <3ef16e60.51799416@news.optonline.net> <bcsitc$84u$1@peabody.colorado.edu> <3ef24124.105763852@news.optonline.net> <bd73hk$5tf$1@peabody.colorado.edu> <3ef72409.34745107@news.optonline.net> <bd7o5v$f20$1@peabody.colorado.edu> <3ef7fd06.90302963@news.optonline.net>`

```

On 24-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> >So a compiler writer doesn't expect anyone will want to maintain his code?
> >He
…[3 more quoted lines elided]…
> that's not obvious to me.

I comment code that's may not be obvious to others.

Sometimes I comment why I made a particular choice - in the case of a SEARCH
command, this could be useful.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-18T12:31:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcqeln$31j6$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ef08efb.330337761@news.optonline.net...

> At compiler companies I'm familiar with, there are two programming groups.
The
> front-end folks work in a high level language; the back-end folks work in
> assembly or a low level language. MetroWerks, whose Code Warrior compiles
C to
> many many cpus, mostly imbedded, has three back-end groups -- one for
CISC, one
> for RISC, and one for TI processors.

Have you truly never encountered an environment in which the language
compilers are written to produce code for a particular machine?   I don't
think Unisys is uncommon in this regard, particularly when the entire course
of the history of computers (mainframe and otherwise) is taken into account!

 >
> The separation between front- and back-end is obvious with Java, .Net and
Micro
> Focus.

It may not be as obvious in cases in which a machine vendor provides or
markets a compiler that is specifically intended solely for use in a single
environment.  I would not, for example, expect the Optimizing Fortran
compiler associated with the Cray CF90 Programming Environment to produce
object code for anything other than a Cray Supercomputer, and I would not
expect the process of getting from source code to executable object code on
that system to involve two processes.  I might be wrong, but my expectation
would be that that compiler produces Cray object code and nothing but Cray
object code.

> Thanks for the info about Unisys.

I don't think it's just Unisys.  I think it's what I'd expect for any system
vendor producing a compiler designed and intended for use on that particular
machine and none other.  I wouldn't expect, for example, an RPG compiler
intended to produce optimized code for use on AS/400 systems to produce code
for anything other than AS/400 systems, or to parse any RPG dialect other
than that intended for use on AS/400 systems.  Some optimization can be done
at the object code level, but some relies on an interaction between the
source parsing process and the code generation process, and when they are
divorced such optimizations aren't necessarily practical.

In a single-architecture environment, about the only justification for
re-compiling from intermediate into executable code is if multiple compilers
are going to make use of the code generator, and unless that's likely, the
disadvantages may make that impractical.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Front-/Back-end (was: Alphabets

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-18T14:54:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcqg25$2rr$1@slb0.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:bcqeln$31j6$1@si05.rsvl.unisys.com...
>
> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3ef08efb.330337761@news.optonline.net...
>
> > At compiler companies I'm familiar with, there are two programming
groups.
> The
> > front-end folks work in a high level language; the back-end folks work
in
> > assembly or a low level language. MetroWerks, whose Code Warrior
compiles
> C to
> > many many cpus, mostly imbedded, has three back-end groups -- one for
…[5 more quoted lines elided]…
> think Unisys is uncommon in this regard, particularly when the entire
course
> of the history of computers (mainframe and otherwise) is taken into
account!
>
>  >
> > The separation between front- and back-end is obvious with Java, .Net
and
> Micro
> > Focus.
>
> It may not be as obvious in cases in which a machine vendor provides or
> markets a compiler that is specifically intended solely for use in a
single
> environment.  I would not, for example, expect the Optimizing Fortran
> compiler associated with the Cray CF90 Programming Environment to produce
> object code for anything other than a Cray Supercomputer, and I would not
> expect the process of getting from source code to executable object code
on
> that system to involve two processes.  I might be wrong, but my
expectation
> would be that that compiler produces Cray object code and nothing but Cray
> object code.
…[3 more quoted lines elided]…
> I don't think it's just Unisys.  I think it's what I'd expect for any
system
> vendor producing a compiler designed and intended for use on that
particular
> machine and none other.  I wouldn't expect, for example, an RPG compiler
> intended to produce optimized code for use on AS/400 systems to produce
code
> for anything other than AS/400 systems, or to parse any RPG dialect other
> than that intended for use on AS/400 systems.  Some optimization can be
done
> at the object code level, but some relies on an interaction between the
> source parsing process and the code generation process, and when they are
…[3 more quoted lines elided]…
> re-compiling from intermediate into executable code is if multiple
compilers
> are going to make use of the code generator, and unless that's likely, the
> disadvantages may make that impractical.
>
>     -Chuck Stevens
>

From my experience (with PC's, Unix, and <primarily IBM> mainframes), it is
my perception that it is most common (not universal) that in "mainframe"
environments, the vendor of the hardware is the vendor of the operating
system is the vendor of the compiler(s) (regardless of language).  There may
be alternative compilers available, but the *most* common (probably default)
is the hardware-O/S vendor's compiler to be used.

In PC and Unix environments, it is quite common for the relationship between
Hardware, Operating System, and compilers to be "unpredictable" (i.e. any
specific vendor may provide 1, 2, or 3 of the above).  For those vendors who
*do* provide compilers but do not also provide "full" operating systems,
they often (not always) provide "portable" compilers with "tailored"
run-times for various O/S (and hardware).  Those vendors often (again not
always) distinguish between "front-end", "back-end" and "run-time"
developers.  I know of some where the back-end developers are also the
run-time developers - and others where the back-end developers are also the
front-end developers - and I think (but am not positive) some where
developers work on all 3.

   ***

Now back to part of the original thread.

If someone were to use the term "p-code" in a conversation with me, I would
think of that as code created by a compiler "front-end" to run under a
"virtual" (or pseudo-) machine.

If someone were to use the term "pseudo-code" in a conversation with me, I
would think that this was an "outline" (sort-of replacement for various
flow-charting) of an application's logic (or a portion of its logic).  Such
code is used by a programmer to "design" an application.

I might understand what was meant if someone "confused" these terms when
talking to me, but these are the NORMAL meanings that I would expect -
unless "context" made it highly unlikely.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-19T09:06:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef17a3a.54833963@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
>news:bcqeln$31j6$1@si05.rsvl.unisys.com...

>From my experience (with PC's, Unix, and <primarily IBM> mainframes), it is
>my perception that it is most common (not universal) that in "mainframe"
…[3 more quoted lines elided]…
>is the hardware-O/S vendor's compiler to be used.

That was true during the Golden Age '70s. It hasn't been true since the PC,
twenty years ago. Neither Intel nor Microsoft offers a COBOL compiler. 

>In PC and Unix environments, it is quite common for the relationship between
>Hardware, Operating System, and compilers to be "unpredictable" (i.e. any
…[8 more quoted lines elided]…
>developers work on all 3.

It's a question of scale. In a one man company, obviously one person works on
all three levels. As companies grow larger, the 'natural' division of interests
emerges. 

>If someone were to use the term "p-code" in a conversation with me, I would
>think of that as code created by a compiler "front-end" to run under a
…[5 more quoted lines elided]…
>code is used by a programmer to "design" an application.

I concur. That's normal usage. 

What's a flow-chart? In 40 years experience, I've never flow-charted a program.
I've flow-charted systems, but not programs. Sounds like another Bad Idea from
the '70s.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 11)_

- **From:** "Don Leahy" <don.leahy@nospamwhatever.leacom.ca>
- **Date:** 2003-06-19T16:22:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3YoIa.2528$%91.358373@news20.bellglobal.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net>`

```
>
> What's a flow-chart? In 40 years experience, I've never flow-charted a
program.
> I've flow-charted systems, but not programs. Sounds like another Bad Idea
from
> the '70s.
>
The main purpose of a  Program flow-chart was to slow down the coding
process in order to ease the workload of the the keypunch department.   :-)
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-06-20T09:59:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bctbrl$vpo$1@aklobs.kc.net.nz>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net>`

```
Robert Wagner wrote:


> What's a flow-chart? In 40 years experience, I've never flow-charted a
> program. I've flow-charted systems, but not programs. Sounds like another
> Bad Idea from the '70s.

Why do you think that a graphic and symbolic representation of program flow 
is a 'bad idea', yet, presumably, the graphic and symbolic representation 
of a system flow is a 'good idea'.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-20T02:51:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef272bf.118464406@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>of a system flow is a 'good idea'.

Because a program flowchart is for the 'logic impaired'.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-19T22:54:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306192154.136371ef@posting.google.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> What's a flow-chart? In 40 years experience, I've never flow-charted a
> >> program. I've flow-charted systems, but not programs. Sounds like another
…[6 more quoted lines elided]…
> Because a program flowchart is for the 'logic impaired'.

In what way does documentation in the form of a graphical and symbolic
representation indicate that the programmer is 'logic impaired' ?

Does a map indicate 'directionally impaired' ?

Does a wiring diagram indicate 'electrically impaired' ?

Now if the flowchart was _wrong_ or inconsistent it may indicate thet
the author was 'logic impaired', but why do you think (or not) that
the mere presence of one indicates that ?
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 14)_

- **From:** "Warren Simmons" <wsimmons5@cox.net>
- **Date:** 2003-06-20T00:10:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hryIa.77013$%42.15859@fed1read06>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com>`

```
Grace would find this very funny. At DOD she had six low paid sailers who
learned
from her, and created some very nice tools written in COBOL. One of them was
a program to create a flow chart on the printer. I know it was very usefull
for newbees
to grasp what they had written, and how to fix the problem they created. I
feel anyone
who learns to program has a higher logical quotient than other, yet might
find other
endevors difficult. It's not nice to label groups of people based upon your
opinion,
and doing so is like pissing in the wind.

Warren Simmons
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-23T14:47:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd73ul$5u7$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <hryIa.77013$%42.15859@fed1read06>`

```

On 20-Jun-2003, "Warren Simmons" <wsimmons5@cox.net> wrote:

> Grace would find this very funny. At DOD she had six low paid sailers who
> learned
…[3 more quoted lines elided]…
> to grasp what they had written, and how to fix the problem they created.

I saw the output of such a program in 1970.   It was a big waste of paper,
making simple code take up lots of space.   CoBOL source does it better.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-20T21:41:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef36fd6.23911364@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[11 more quoted lines elided]…
>representation indicate that the programmer is 'logic impaired' ?

Program flowcharts weren't used to document, they were used to help the
programmer understand complex conditional logic. The hope was a picture would
make it easier to understand. 

>Does a wiring diagram indicate 'electrically impaired' ?

That's a good analogy. Old-fashioned circuits were designed and documented with
wiring diagrams. The diagram tool is hopelessly inadequate to design an
integrated circuit. ICs are designed in VHDL or Verilog, which are programming
languages quite similar to the ones we use. They have standards committees
(under IEEE); there is even talk about going OO.  VHDL source is compiled to RTL
code, which is a hardware description (any hardware, not just electronics) that
can be executed by simulators running test procedures also written in VHDL.
After the RTL is found to work, it is compiled to GDSII, a graphic language
which can be fed into CAD for a mask. Alternatively, RTL can be burned into
microcode or firmware without the need for a mask. That's how ASIC chips in your
DVD player and cellphone were designed.  

A chip designer who drew a wiring diagram would be laughed out of the lab.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 15)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-20T18:48:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306201748.62e49021@posting.google.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> >> What's a flow-chart? In 40 years experience, I've never flow-charted a
> >> >> program. I've flow-charted systems, but not programs. Sounds like another
> >> >> Bad Idea from the '70s.

> >> Because a program flowchart is for the 'logic impaired'.
> >
> >In what way does documentation in the form of a graphical and symbolic
> >representation indicate that the programmer is 'logic impaired' ?

> Program flowcharts weren't used to document, they were used to help the
> programmer understand complex conditional logic. The hope was a picture would
> make it easier to understand. 

They were used as a design tool, _and_ as a documentation tools.
 
> >Does a wiring diagram indicate 'electrically impaired' ?
> 
> That's a good analogy. Old-fashioned circuits were designed and documented
>  with wiring diagrams. 

So then why, in the 70s, were flowcharts a 'bad idea' as a design and
documentation tool ?

> The diagram tool is hopelessly inadequate to design an
> integrated circuit. 

Tools should be appropriate for the task.  Not all cicuits are ICs. 
My car for example has a wiring diagram and it is an ideal form for
documentation of this.  It is also used for cicuits where the ICs are
components.

> ICs are designed in .. 

ICs _are_ wiring diagrams reproduced photographically.

> A chip designer who drew a wiring diagram would be laughed out of the lab.

What for ? using a pencil instead of having it printed out ?
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-21T19:15:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef496c1.19685386@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> >> >> What's a flow-chart? In 40 years experience, I've never flow-charted a
>> >> >> program. I've flow-charted systems, but not programs. Sounds like
another
>> >> >> Bad Idea from the '70s.

>> >Does a wiring diagram indicate 'electrically impaired' ?
>> 
…[4 more quoted lines elided]…
>documentation tool ?

Because wiring diagrams were the only or primary documentation of a circuit's
details. In programming, source code is the primary repository. 

Now that circuits are described in source code, engineers no longer use
diagrams.

>> The diagram tool is hopelessly inadequate to design an
>> integrated circuit. 
…[4 more quoted lines elided]…
>components.

Agreed. 

>> ICs are designed in .. 
>
>ICs _are_ wiring diagrams reproduced photographically.

Correct, but soon to change. The wavelength of light is 400-800 nm. At 120 nm,
chip features are less than half that now, and rapidly shrinking. Below 120nm,
fabrication will go to direct write e-beam, which uses no mask at all, x-ray
lithography, which IBM has been using for years, or some other exotic 
imaging technique. Light is obsolete.

>> A chip designer who drew a wiring diagram would be laughed out of the lab.
>
>What for ? using a pencil instead of having it printed out ?

A pencil cannot draw a line 90 nanometers wide.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-21T17:24:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd2luu$udh$1@slb0.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net>`

```
For those not familiar with comp.lang.cobol,
     Check google for the accuracy track-record of this poster (R. Wagner) -
and the <lack of> regard with which most of his comments are viewed by many
in this newsgroup before reading his post below.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 17)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-24T15:19:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306241419.39ccfde8@posting.google.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >So then why, in the 70s, were flowcharts a 'bad idea' as a design and
> >documentation tool ?
> 
> Because wiring diagrams were the only or primary documentation of a circuit's
> details. In programming, source code is the primary repository. 

That doesn't answer the question which was: Why, in the 70s, were
flowcharts a 'bad idea' as a design and documentation tool ?

> Now that circuits are described in source code, engineers no longer use
> diagrams.

You are always so black-and-white about things: "NO ENGINEER EVER USES
DIAGRAMS ANYMORE".

What crap.  Some engineers use source, some use paper and pencil, some
scratch diagrams in the sand.

In any case the source description is used to construct diagrams on
screen, it is just that they less often do manual tracking.

> Correct, but soon to change. The wavelength of light is 400-800 nm. At 120 nm,
> chip features are less than half that now, and rapidly shrinking. Below 120nm,
> fabrication will go to direct write e-beam, which uses no mask at all, x-ray
> lithography, which IBM has been using for years, or some other exotic 
> imaging technique. Light is obsolete.

_SOME_ ICs will be made by exotic techniques.  Many will still keep
the existing photo machines going, some will still be made by even
cruder techniques.

> A pencil cannot draw a line 90 nanometers wide.

Do you think that _ALL_ circuits are made 90 nm wide ?

Do you think that the ICs in my car will _ever_ be this delicate ? 
Hint: how much current at 12volts will a 90 nm track carry ?
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-25T03:20:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef8fca7.155753327@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[7 more quoted lines elided]…
>flowcharts a 'bad idea' as a design and documentation tool ?

They were bad for design because they were a waste of time and shouldn't have
been necessary. I never used them.

They were bad for documentation because programmers didn't trust them to be kept
up to date. When I want to see what a program does, I look at source code, not
some external documentation.

>> Now that circuits are described in source code, engineers no longer use
>> diagrams.
…[5 more quoted lines elided]…
>scratch diagrams in the sand.

Pray tell, how do they test a design scratched on paper? All ICs are tested on
sumulators before a mask is made. Depending on resolution, a mask can cost tens
of thousands of dollars. And that's just for one layer. 

>> Correct, but soon to change. The wavelength of light is 400-800 nm. At 120
nm,
>> chip features are less than half that now, and rapidly shrinking. Below
120nm,
>> fabrication will go to direct write e-beam, which uses no mask at all, x-ray
>> lithography, which IBM has been using for years, or some other exotic 
…[4 more quoted lines elided]…
>cruder techniques.

Correct. Regions within a single chip may use different imaging techniques. 

>Do you think that _ALL_ circuits are made 90 nm wide ?

No, but as manufacturing equipment wears out, it is not being replaced. A friend
in the calculator business kept complaining because he could no longer buy 75
micron (75000 nm) chips for $1. He had to spend twice as much for higher speed
that wasn't necessary. 

>Do you think that the ICs in my car will _ever_ be this delicate ? 
>Hint: how much current at 12volts will a 90 nm track carry ?

You're on the right track, but asking the wrong question. ICs never ran at 12
volts, that was for fans and disk motors. ICs originally ran at 5 volts. Modern
ones run at 1.3. But the Itanium 2 consumes 130 watts, which means it is drawing
100 amps. (Try getting that from a laptop battery.)

The limiting factor in ICs is not trace size, it is heat dissipation. If we
calculate heat per surface area, an Itanium is higher than an electric hotplate.
The next generation will probably consume twice the power in one fourth the
surface area. It will have to be liquid cooled unless there's a breakthru idea.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-06-25T08:14:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdc3mo$sqs$1@panix1.panix.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net>`

```
In article <3ef8fca7.155753327@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>It will have to be liquid cooled unless there's a breakthru idea. 

My Sense of The Perverse is tickled by the image of a Halon-equipped 
'clean room' built for laptop use.

DD
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-25T14:23:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdcb8i$agb$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net>`

```

On 24-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> They were bad for design because they were a waste of time and shouldn't have
> been necessary. I never used them.

Some people used them successfully, especially with shared projects.   They
weren't always a waste of time.

> They were bad for documentation because programmers didn't trust them to be
> kept
> up to date. When I want to see what a program does, I look at source code, not
> some external documentation.

Agreed.


> No, but as manufacturing equipment wears out, it is not being replaced. A
> friend
> in the calculator business kept complaining because he could no longer buy 75
> micron (75000 nm) chips for $1. He had to spend twice as much for higher speed
> that wasn't necessary.

But some of the earlier computer chips are still being produced in incredible
amounts.   So they're overkill - they're still cheap as dirt.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 19)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-25T15:52:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306251452.581f6e70@posting.google.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >That doesn't answer the question which was: Why, in the 70s, were
> >flowcharts a 'bad idea' as a design and documentation tool ?
> 
> They were bad for design because they were a waste of time and shouldn't have
> been necessary. 

You seem to be advocating the 'forget the design phase, just write the
code' approach.

If you have been rewriting the same program for the last few decades
then skipping the design phase is viable.  However, no one here had
been rewriting the same program for decades back in the 70s.

I do occasionally do a design when I have a new style of program to
write, sometimes this may even resemble some form of flowchart. Back
in the early 70s when I didn't have a terminal on my desk, I even had
to do this using paper and pencil.

Would you also say that house plans are 'a waste of time and shouldn't
be necessary' ?  Just start by cutting lumber and nailing it together
?

> I never used them.

But then you seem to have always been so exceptional - in one way or
another.

> They were bad for documentation because programmers didn't trust them to be
> kept
> up to date. When I want to see what a program does, I look at source code, not
> some external documentation.

I think that comments also should be ignored because programmers can't
be trusted to update them, yet you claim to write them.  Why is that ?
 Aren't they just a waste of time too ?

However, when looking a system new to me, I do think that where
specifications and design documents are available they used be used as
a preliminary overview of what the system is intended to do, and how.
 
> Pray tell, how do they test a design scratched on paper? All ICs are tested on
> sumulators before a mask is made. Depending on resolution, a mask can cost
> tens of thousands of dollars. And that's just for one layer. 

Not all circuits are ICs. You seem to have processed from 'wiring
diagrams' all the way up to the extremes of 90 nm ICs where light is
obsolete, as if that was the only thing that electronics is doing
these days.

Most electronics is still fairly mundane circuit boards where
'testing' can be done using calculations, or by bread boarding.
 
Of course the extremities may suit your argument better so you just
blank off the rest and deny it exists.

> >Do you think that _ALL_ circuits are made 90 nm wide ?
> 
…[3 more quoted lines elided]…
> micron (75000 nm) chips for $1.

But I guarantee that the calculator _also_ has a circuit board.

> >Do you think that the ICs in my car will _ever_ be this delicate ? 
> >Hint: how much current at 12volts will a 90 nm track carry ?
 
> You're on the right track, but asking the wrong question. ICs never ran at 12
> volts, 

Actually there are ICs that handle 12 volts - for serial ports for
example. But your view of what an 'IC' is is rather restricted (yet
again). Not all ICs are made for computers, or run at computer
voltages.

> The next generation will probably consume twice the power in one fourth the
> surface area. 

Actually the reduction in track width _should_ result in requiring
less power, however Intel use the reduction in size to increase the
number of components which then leads to increase in power
requirements.  That is the next generation _may_ consume twice the
power but only because they keep the _same_ surface area and use this
for more components.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 20)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-26T13:42:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3efa4ff6_9@news.athenanews.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0306251452.581f6e70@posting.google.com...
> robert@wagner.net (Robert Wagner) wrote
>
<snip>
>
> If you have been rewriting the same program for the last few decades
> then skipping the design phase is viable.

So, I wonder what Tony "Foodman" Dilworth is doing these days...<G>?

Ah, of course...(rewriting the same program....)

> However, no one here had
> been rewriting the same program for decades back in the 70s.
…[5 more quoted lines elided]…
>

Me too. I still have the template I used... It is a treasured souvenir that
still gets used occasionally.

> Would you also say that house plans are 'a waste of time and shouldn't
> be necessary' ?  Just start by cutting lumber and nailing it together
> ?
>

I have used flowcharts and found them useful.
(still do when trying to get my head around multiple threads, for example).

This really comes down to how different people visualize. We all accept that
the source code is the ultimate authority, but sometimes a graphic overview
can be very useful as a set of "hooks" to hang things on...

> > I never used them.
>
> But then you seem to have always been so exceptional - in one way or
> another.
>
I'm getting worried about the use of "exceptional" in CLC. .<G>

You and Howard aren't using the same dictionary, are you <G>?

<snip>
>
> However, when looking a system new to me, I do think that where
> specifications and design documents are available they used be used as
> a preliminary overview of what the system is intended to do, and how.
>

Agree completely.

<snip>
>
> Of course the extremities may suit your argument better so you just
> blank off the rest and deny it exists.
>

When the frost bites, focus moves to the extremities...

<snipped>
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-26T14:54:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdf1g1$i6u$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com> <3efa4ff6_9@news.athenanews.com>`

```

On 25-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > But then you seem to have always been so exceptional - in one way or
> > another.
…[3 more quoted lines elided]…
> You and Howard aren't using the same dictionary, are you <G>?

Don't worry here.  But I might want to use his dictionary occasionally in the
future.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-26T05:38:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3efa4c01.241616514@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[4 more quoted lines elided]…
>> been necessary. 

>I do occasionally do a design when I have a new style of program to
>write, sometimes this may even resemble some form of flowchart. Back
>in the early 70s when I didn't have a terminal on my desk, I even had
>to do this using paper and pencil.

You described a system flowchart; the quotations were about a detailed
line-by-line program flowchart. I said earlier that I have no objection to a
system flow. 

When designing a new system, I usually use a text description and a prototype. I
find text and programs easier to change. 

>Would you also say that house plans are 'a waste of time and shouldn't
>be necessary' ?  Just start by cutting lumber and nailing it together?

Lumber isn't as malleable as program code. 

>> They were bad for documentation because programmers didn't trust them to be
>> kept
>> up to date. When I want to see what a program does, I look at source code,
not
>> some external documentation.
>
>I think that comments also should be ignored because programmers can't
>be trusted to update them, yet you claim to write them.  Why is that ?
> Aren't they just a waste of time too ?

Not if you're reasonable. My mid-code comments document only things that are not
obvious from reading the code. Thus, when you see a comment, it was put there
for a reason. It's a caution flag. Those conditions change infrequently.  I also
comment at the top of each program at least one sentence saying what it does,
usually a paragraph describing where it fits into the system or the business
reason it serves. 

I've seen programs containing so much superfluous verbiage that the reader tuned
out comments. For example, these three comment lines contain no information.
They say the same thing the program says.

  compute-net-pay.
* This paragraph computes the employee's net pay and moves it to the paycheck 
* Compute net pay in working-storage
   compute net-pay = gross-pay - deductions
* Next move net pay to the paycheck transaction
   move net-pay to check-net-pay.

>However, when looking a system new to me, I do think that where
>specifications and design documents are available they used be used as
>a preliminary overview of what the system is intended to do, and how.

I agree.
 
>> Pray tell, how do they test a design scratched on paper? All ICs are tested
on
>> sumulators before a mask is made. Depending on resolution, a mask can cost
>> tens of thousands of dollars. And that's just for one layer. 
…[4 more quoted lines elided]…
>these days.

With the exception of small production volume, it's almost always less expensive
to put the whole circuit in one IC. Modems used to sell for $100+. Now they sell
for $15 because the whole circuit is in single chip costing $3. 

>Most electronics is still fairly mundane circuit boards where
>'testing' can be done using calculations, or by bread boarding.

I don't know how you measure "most". Retail units sold? Logic gates?

>> >Do you think that _ALL_ circuits are made 90 nm wide ?
>> 
…[3 more quoted lines elided]…
>> micron (75000 nm) chips for $1.
[self correction: .75 micron (750 nm)]

>But I guarantee that the calculator _also_ has a circuit board.

Only to provide edge connectors. You can count the chips on one finger. 

>> You're on the right track, but asking the wrong question. ICs never ran at 12
>> volts, 
>
>Actually there are ICs that handle 12 volts - for serial ports for example. 

That's true, but UARTs are no longer discrete components. Their function is in
your PC's 'front porch', which amplifies its working voltage to approx. 12
volts. 

>> The next generation will probably consume twice the power in one fourth the
>> surface area. 
…[6 more quoted lines elided]…
>for more components.

Why are CPUs so inefficient? Why do they waste so much energy as heat?

The answer is chip architecture, which is driven by economics. To double thruput
there are three approaches: 
.Double the clock speed, which is what they've been doing.
.Execute two instructions in parallel, Itanium and Alpha already do. That costs
more because it doubles the number of pipelines. 
.Put two CPUs on the same chip, divide the program into threads which can run in
parallel. Requires a lot of help from the compiler. Really requires a  new
programming paradigm. 

I personally believe the last is the 'unspoken' driving force behind OO,
functional languages and artificial intelligence. They need to wean us
programmers away from von Neumann architecture, where instructions execute
sequentially.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 21)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-26T03:08:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306260208.735e38b5@posting.google.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com> <3efa4c01.241616514@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >I do occasionally do a design when I have a new style of program to
> >write, sometimes this may even resemble some form of flowchart. Back
…[3 more quoted lines elided]…
> You described a system flowchart; 

I did ? where was that ?  Do you actually read or do you use some
different mechanism to decide what it 'says' ?  How does 'style of
program' become 'system' ?

> the quotations were about a detailed
> line-by-line program flowchart. 

Were they ?  when did 'line by line' come into it ?  The quotations
were about 'program flowchart'.  You obviously took your usual
extremist view and decided that must only mean 'every single line
diagrammed'.

Anything taken to extreme can become a waste, so you assume that and
condemn all. It must either be no design or line-by-line.  Black or
white.

> I personally believe the last is the 'unspoken' driving force behind OO,
> functional languages and artificial intelligence. They need to wean us
> programmers away from von Neumann architecture, where instructions execute
> sequentially.

Is this some sort of conspiracy theory ?  Mind control by Intel to
make programmers demand new CPU architectures ?
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-26T14:59:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdf1o9$iah$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <3ef272bf.118464406@news.optonline.net> <217e491a.0306192154.136371ef@posting.google.com> <3ef36fd6.23911364@news.optonline.net> <217e491a.0306201748.62e49021@posting.google.com> <3ef496c1.19685386@news.optonline.net> <217e491a.0306241419.39ccfde8@posting.google.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com> <3efa4c01.241616514@news.optonline.net>`

```

On 25-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> You described a system flowchart; the quotations were about a detailed
> line-by-line program flowchart.

I missed that part.  (detailed line-by-line).   Occasionally messages don't make
it to all of us at the same rate.

> I said earlier that I have no objection to a system flow.

It is quite possible to have something bigger than "detailed line-by-line" and
smaller than "system flow", especially in some of the larger, more complex
programs.

I've never charted the flow of a multiple-thread program, I wonder how that is
done.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-06-26T11:00:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdf1r3$he4$1@panix1.panix.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3ef8fca7.155753327@news.optonline.net> <217e491a.0306251452.581f6e70@posting.google.com> <3efa4c01.241616514@news.optonline.net>`

```
In article <3efa4c01.241616514@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>riplin@Azonic.co.nz (Richard) wrote:

[snip]

>>I think that comments also should be ignored because programmers can't
>>be trusted to update them, yet you claim to write them.  Why is that ?
…[3 more quoted lines elided]…
>obvious from reading the code.

Mr Wagner, it seems that you are equating being 'reasonable' with 'doing 
it the Wagner Way'.

Are you able to come up with any methods which you would call 'reasonable'
*other* than 'the Wagner Way'?

('Of course it is 'reasonable'... it is the way *I* do it!')

DD
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-23T14:45:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd73qt$5u5$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz>`

```

On 19-Jun-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > What's a flow-chart? In 40 years experience, I've never flow-charted a
> > program. I've flow-charted systems, but not programs. Sounds like another
…[4 more quoted lines elided]…
> of a system flow is a 'good idea'.

I think flow charts are useful when the components are designed by others,
and/or the connections aren't obvious.   There are job dependencies which have
to be followed in a batch environment - and we can't look at the CoBOL to see
these dependencies.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-23T17:10:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef72ed7.37511824@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <bd73qt$5u5$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On 19-Jun-2003, Richard Plinston <riplin@Azonic.co.nz> wrote:
>
…[11 more quoted lines elided]…
>these dependencies.

You raise an excellent point. When I see such dependencies, the first thought
that comes to mind is "redesign". In a perfect world, there wouldn't be
dependencies like that. 

My second choice is automation. For example, if A must run just before B, make A
write a timestamp somewhere and B check it. 

If neither is practical, I document the dependency at both ends.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-23T13:02:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd7fc2$dh1$1@slb3.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <bd73qt$5u5$1@peabody.colorado.edu> <3ef72ed7.37511824@news.optonline.net>`

```
For those not familiar with comp.lang.cobol,
     Check google for the accuracy track-record of this poster (R. Wagner) -
and the <lack of> regard with which most of his comments are viewed by many
in this newsgroup before reading his post below.

Note also, that his reply has left the subject as something that doesn't
have anything to do with his post.
```

###### ↳ ↳ ↳ Re: Front-/Back-end (was: Alphabets

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-23T18:41:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd7hla$c03$1@peabody.colorado.edu>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <bcqeln$31j6$1@si05.rsvl.unisys.com> <bcqg25$2rr$1@slb0.atl.mindspring.net> <3ef17a3a.54833963@news.optonline.net> <bctbrl$vpo$1@aklobs.kc.net.nz> <bd73qt$5u5$1@peabody.colorado.edu> <3ef72ed7.37511824@news.optonline.net>`

```

On 23-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> You raise an excellent point. When I see such dependencies, the first thought
> that comes to mind is "redesign". In a perfect world, there wouldn't be
…[6 more quoted lines elided]…
> If neither is practical, I document the dependency at both ends.

We automate such dependencies, but it can be useful to have charts anyway -
applications programmers don't use CA-7, and we do need to be aware of
dependencies and have some knowledge on how our changes can effect process flow.

I don't know that all dependencies can be redesigned away.   Sometimes we DO
need to make sure that close of business accounts are what are shown in the next
day's balance.    Business needs have dependencies which cannot be redesigned
away by programmers.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-19T00:05:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef0fceb.22750191@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[14 more quoted lines elided]…
>of the history of computers (mainframe and otherwise) is taken into account!

Yes, I have. Burroughs Large Systems wrote some 'one pass compilers'. The
architect told me it was a bad idea, in retrospect. He'd never again design a
one pass compiler. 

That doesn't directly address the question of intermediate code, but it's
symptomatic of myopic design. Suppose you're working for Burroughs and spitting
machine language for the one-and-only processor. Then the boss waves his hands
and says 'We've just been acquired by Unisys (or vice versa). How much trouble
(they always say 'how much trouble' rather than 'how fast can you') would it be
to emit code for another machine?' 

If you'd designed the compiler in two tiers, the addition would be relatively
painless. If you'd glommed it all together, you'd be in deep trouble. 

>> The separation between front- and back-end is obvious with Java, .Net and
>Micro
…[10 more quoted lines elided]…
>object code.

Cray was acquired by Silicon Graphics in 1996, then acquired by Tera Computer in
2000. The Tera/Cadence platform was quite a bit different from the IBM 390
platform that Cray initially emulated. I picture Cray compiler writers
scrambling rather than sitting content. 

DEC and Tandem have been acquired by Compaq. I picture their compiler writers
also under the gun.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-19T10:25:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcsrmn$1nnr$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ef0fceb.22750191@news.optonline.net...

> >Have you truly never encountered an environment in which the language
> >compilers are written to produce code for a particular machine?   I don't
> >think Unisys is uncommon in this regard, particularly when the entire
course
> >of the history of computers (mainframe and otherwise) is taken into
account!
>
> Yes, I have. Burroughs Large Systems wrote some 'one pass compilers'. The
> architect told me it was a bad idea, in retrospect. He'd never again
design a
> one pass compiler.

Burroughs Large Systems also wrote some "two-pass compilers" (for various
languages) in which the code-generation "pass" was aware of the underlying
language constructs.  Whether a given monolithic (or even modular)
executable program that functions to consume programmer's source code and
produce directly-executable object code goes through the source file once,
twice, or any number of times is irrelevant to whether the part of the
compiler that produces object code has knowledge or "memory" of what source
construct it is that the compiler's producing code for.   The number of
"passes" relates to the source images, not to the "passing" of any
intermediate structure (on disk or in memory).  Most often a "true" two-pass
compiler passes the source -- or some text-based massaging of the source -- 
twice in an effort to ensure that additional information developed by the
compiler is correctly coordinated with the source images for the listing;
any other information can be communicated from the parser to the rest of the
compilation through more direct means.

Based on my experience with both one- and multi-pass compilers, I would say
the most important criterion as to whether the compiler for a given language
should be one-pass or more-than-one-pass is the nature of the language being
compiled.  For languages in which everything "meaningful" about an element
of the program can be determined before it is necessary to generate code
associated with that element, there is no particular reason for the compiler
to have to process the entirety of the program first.  For example, either
some form of "forward-reference template" for an ALGOL or Pascal procedure,
or the procedure itself, must be encountered by the compiler before any
reference to that procedure may appear in the program.  Thus, I would place
both ALGOL and Pascal in the category of languages for which "one-pass
compilers" are adequate.  It is not necessary for the compiler to have
"seen" a future statement in an ALGOL or Pascal program before generating
object code for the current statement.  COBOL as a language is *less*
well-suited to generating object code as each statement is encountered; for
example, I personally think that, because of the way nested programs are
structured, there are compromises associated with generating object code for
a program upon encountering the end of that program.  I also think that
there are some reasonable optimizations that can take place in data mapping
and allocation that can only occur if the entirety of the code that accesses
the data has been "seen" before the final allocation process begins.

>
> That doesn't directly address the question of intermediate code, but it's
> symptomatic of myopic design. Suppose you're working for Burroughs and
spitting
> machine language for the one-and-only processor. Then the boss waves his
hands
> and says 'We've just been acquired by Unisys (or vice versa). How much
trouble
> (they always say 'how much trouble' rather than 'how fast can you') would
it be
> to emit code for another machine?'

Before that question is answered, one must also ask "Do they already have
the ability to emit code for their own machine?"  Using the B6900/U2200
analogy, if there's already a suite of COBOL products for the Univac 2200
that works just fine thank you very much, and a suite of COBOL products for
the B6900 that works just fine thank you very much, what's the incentive to
having one cross-compile for the other?   Is there a *business case* for
providing yet another environment on either, or both, systems?   Is there a
business case for suggesting to the existing users of either system that
they need to stop doing what they're doing, and spend lots and lots of money
to convert to another way of doing exactly what they're already doing?

> Cray was acquired by Silicon Graphics in 1996, then acquired by Tera
Computer in
> 2000. The Tera/Cadence platform was quite a bit different from the IBM 390
> platform that Cray initially emulated. I picture Cray compiler writers
> scrambling rather than sitting content.

I haven't kept up with the Cray saga; I was using it as an example of a
proprietary architecture, and the Fortran compiler as an example of a
compiler intended only to produce object code for a proprietary
architecture.

> DEC and Tandem have been acquired by Compaq. I picture their compiler
writers
> also under the gun.

Whatever you "picture" may or may not bear any relationship to reality.
Since a likely candidate for Someone Who Should Know Or Could Find Out is
readily available to you -- the HP representative on the J4 mailing list
which is posted on the J4 web site -- rather than engaging in idle
speculation you might want to query that individual to find out exactly how
much effort the various ex-DEC, ex-Tandem, ex-whichever-flavor-of-HP
compiler writers are expending in revising each of their compilers to
generate object code for any or all of the others, and if they are "under
the gun", exactly what sort of gun it is that they are under!  I don't know,
but I wouldn't be so rash as to speculate.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-21T19:15:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef4966f.19603578@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ef0fceb.22750191@news.optonline.net...

>Based on my experience with both one- and multi-pass compilers, I would say
>the most important criterion as to whether the compiler for a given language
…[18 more quoted lines elided]…
>the data has been "seen" before the final allocation process begins.

Forward references are easily handled by:
..Leaving a blank pointer in object code and fixing it up at the end (1.1 pass?)
..Getting the linker to do it 
..Letting the run-time guy do it. Variation: Microsoft's 'fixups' in .exe files.


I think a better reason for multi-pass is cleaner compiler architecture. I liken
it to application architecture. In the days of anemic computers, we made one
sequential pass through a 'master file' and crammed all processing into one,
often monolithic, program. Now we can afford to package logic more functionally.


The new generation of processors, notably Itanium, *requires* multiple passes ..
not on source code but on intermediate code. The hardware depends on compiler
optimization of predication, speculation (necessary for multi-threading), loop
unrolling, pipelining, inlining, etc. Intel, HP and others provide standard
components to optimize intermediate code and then produce machine language.
Intel's code generator is called ECG. 

In previous generations, the hardware guys did their own optimizations in
hardware. Now it has become too complicated, so they're relying on software to
do it for them.

>I haven't kept up with the Cray saga; I was using it as an example of a
>proprietary architecture, and the Fortran compiler as an example of a
>compiler intended only to produce object code for a proprietary
>architecture.

Proprietary architectures are going away. Consider:

..Tandem (/Compaq/HP) has announced they'e dropping proprietary processors in
favor of Itanium. 
..DEC (/Compaq/HP) dropped their proprietary VAX processors in favor of Alpha.
..HP has dropped their very successful PA processors and the HP-3000 line in
favor of Itanium. Why? Because they couldn't figure out how to make PA 64-bit.
They jumped in bed with Intel and messed up the Itanium 1 with their EPIC
concept, which had the compiler doing optimization rather than using separate
optimizers. Intel had to shove them out in order to get back on track with the
Itanium 2. 

>Whatever you "picture" may or may not bear any relationship to reality.
>Since a likely candidate for Someone Who Should Know Or Could Find Out is
…[7 more quoted lines elided]…
>but I wouldn't be so rash as to speculate.

I don't want to waste Mr. Murray's time asking for publically available
information (above).
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-21T17:22:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd2lqe$jlh$1@slb0.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com> <3ef4966f.19603578@news.optonline.net>`

```
For those not familiar with comp.lang.cobol,
     Check google for the accuracy track-record of this poster (R. Wagner) -
and the <lack of> regard with which most of his comments are viewed by many
in this newsgroup before reading his post below.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-06-22T12:53:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vfbnpoqak460bd@corp.supernews.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com> <3ef4966f.19603578@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ef4966f.19603578@news.optonline.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
…[3 more quoted lines elided]…
> >Based on my experience with both one- and multi-pass compilers, I would
say
> >the most important criterion as to whether the compiler for a given
language
> >should be one-pass or more-than-one-pass is the nature of the language
being
> >compiled.  For languages in which everything "meaningful" about an
element
> >of the program can be determined before it is necessary to generate code
> >associated with that element, there is no particular reason for the
compiler
> >to have to process the entirety of the program first.  For example,
either
> >some form of "forward-reference template" for an ALGOL or Pascal
procedure,
> >or the procedure itself, must be encountered by the compiler before any
> >reference to that procedure may appear in the program.  Thus, I would
place
> >both ALGOL and Pascal in the category of languages for which "one-pass
> >compilers" are adequate.  It is not necessary for the compiler to have
> >"seen" a future statement in an ALGOL or Pascal program before generating
> >object code for the current statement.  COBOL as a language is *less*
> >well-suited to generating object code as each statement is encountered;
for
> >example, I personally think that, because of the way nested programs are
> >structured, there are compromises associated with generating object code
for
> >a program upon encountering the end of that program.  I also think that
> >there are some reasonable optimizations that can take place in data
mapping
> >and allocation that can only occur if the entirety of the code that
accesses
> >the data has been "seen" before the final allocation process begins.
>
> Forward references are easily handled by:
> ..Leaving a blank pointer in object code and fixing it up at the end (1.1
pass?)
> ..Getting the linker to do it
> ..Letting the run-time guy do it. Variation: Microsoft's 'fixups' in .exe
files.

Forward references are but one of the reasons mentioned.
There are potential optimizations, what Mr Stevens calls
'data mapping and allocation', that cannot be achieved until
the procedure division has be analyzed.

The COBOL standard specifies, in the general rules, how
various syntax accomplishes some end. The implementor
is free to use any means to accomplish that end, 'as if' the
rules of COBOL were followed.

For example, a programmer may define an item as numeric
display within a group. During analysis of the procedure division,
it is determined that the item is used only as a subscript to a
table and that it has no other relation with the group in which
it is defined. (This may occur when 'subscripts-and-indexes' are
collected into one group.) Any of the following may occur:

-- the item is removed from the group
-- the item is changed to binary (or packed decimal)
-- the item is changed to an index or pointer
-- the item is placed on a stack
-- the item is deleted due to loop unrolling

To accomplish this, a two-pass compiler is required.

>
> I think a better reason for multi-pass is cleaner compiler architecture.

There can be no better reason than a requirement!
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-22T23:55:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef6411a.45357894@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com> <3ef4966f.19603578@news.optonline.net> <vfbnpoqak460bd@corp.supernews.com>`

```
Rick Smith" <ricksmith@mfi.net> wrote:

>
>Robert Wagner <robert@wagner.net> wrote in message
…[75 more quoted lines elided]…
>There can be no better reason than a requirement!

As I said in another posting, optimization is moving out of the compiler's
domain, thanks largely to the Intel Itanium. Optimizations once performed in
hardware now depend on the compiler. Now that hardware guys are in bed with us,
they want some control over optimization. 

Intel's compiler suite -- C++ and Fortran -- expect the compiler to produce
rough native code in ELF format (native code) and DWARF (symbol table). These
are Linux standards.  It then runs four optimizers on that code, probably with
two passes each, before running ECG to produce an executable. 

Microsoft wants the compiler to emit PE (formerly COFF) and STI.  Same deal,
multiple optimization passes. 

JVM and dot-net have their own standards for intermediate code, and move JIT
compiling (optimization + code generation) to the desktop. 

Yet another contender is EFI byte code (EBC), which works on multiple cpus.

The pattern emerging here is:

..Compiler --> intermediate code
..Optimizer --> optimized intermediate code
..Code generator --> native code

Even assembly language is being optimized. There is no more 'close to metal' as
there used to be. Assembly language is archaic on the Itanium. 

Micro Focus and Fujitsu offer compilers optimized for Itanium. I'd wager one or
both are using Intel's back end optimizers. HP has announced their intention to
use Intel back ends, and HP-UX is the only Itanium platform supported by Micro
Focus.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 14)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-06-22T21:27:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vfcltsco8dfg62@corp.supernews.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com> <3ef4966f.19603578@news.optonline.net> <vfbnpoqak460bd@corp.supernews.com> <3ef6411a.45357894@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ef6411a.45357894@news.optonline.net...
> Rick Smith" <ricksmith@mfi.net> wrote:
>
…[8 more quoted lines elided]…
> >> >Based on my experience with both one- and multi-pass compilers, I
would
> >say
> >> >the most important criterion as to whether the compiler for a given
…[5 more quoted lines elided]…
> >> >of the program can be determined before it is necessary to generate
code
> >> >associated with that element, there is no particular reason for the
> >compiler
…[4 more quoted lines elided]…
> >> >or the procedure itself, must be encountered by the compiler before
any
> >> >reference to that procedure may appear in the program.  Thus, I would
> >place
> >> >both ALGOL and Pascal in the category of languages for which "one-pass
> >> >compilers" are adequate.  It is not necessary for the compiler to have
> >> >"seen" a future statement in an ALGOL or Pascal program before
generating
> >> >object code for the current statement.  COBOL as a language is *less*
> >> >well-suited to generating object code as each statement is
encountered;
> >for
> >> >example, I personally think that, because of the way nested programs
are
> >> >structured, there are compromises associated with generating object
code
> >for
> >> >a program upon encountering the end of that program.  I also think
that
> >> >there are some reasonable optimizations that can take place in data
> >mapping
…[5 more quoted lines elided]…
> >> ..Leaving a blank pointer in object code and fixing it up at the end
(1.1
> >pass?)
> >> ..Getting the linker to do it
> >> ..Letting the run-time guy do it. Variation: Microsoft's 'fixups' in
.exe
> >files.
> >
…[26 more quoted lines elided]…
> >> I think a better reason for multi-pass is cleaner compiler
architecture.
> >
> >There can be no better reason than a requirement!
>
> As I said in another posting, optimization is moving out of the compiler's
> domain, [snip]

I removed it from my earlier reply as irrelevant to the optimization
of COBOL; that is, optimization of COBOL by a COBOL compiler.
I removed the remainder of your response to my reply for the
same reason. I don't care if you have to PE or if a doctor stuck
his hand in your crotch and told you to COFF. I don't care what
you do with an ELF.

Mr Stevens suggested improved optimization of COBOL with
a multi-pass compiler. You appreared to have dismissed his
comments by addressing only 'forward references' and fixups
with a '1.1 pass?' compiler. I supported his comments by giving
a example based upon what you appear to have dismissed.
You went off on a tangent for some other cicle.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-22T20:58:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd5msa$dqg$1@slb0.atl.mindspring.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqeln$31j6$1@si05.rsvl.unisys.com> <3ef0fceb.22750191@news.optonline.net> <bcsrmn$1nnr$1@si05.rsvl.unisys.com> <3ef4966f.19603578@news.optonline.net> <vfbnpoqak460bd@corp.supernews.com> <3ef6411a.45357894@news.optonline.net>`

```
For those not familiar with comp.lang.cobol,
     Check google for the accuracy track-record of this poster (R. Wagner) -
and the <lack of> regard with which most of his comments are viewed by many
in this newsgroup before reading his post below.
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-18T12:46:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcqfig$p5$1@si05.rsvl.unisys.com>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ef08efb.330337761@news.optonline.net...

> >> If the compiler had been written in another language, the semantics
would
> >have
> >> been lost in translation.
…[3 more quoted lines elided]…
> Semantics of the SEARCH verb. If the front-end had turned it into a loop,
the
> back-end would have generated code for a loop.

As with Howard, I haven't a clue what you're trying to say here.

Nothing other than the compiler vendor's desires mandates whether a given
compiler produces an intermediate product that is then processed into object
code.  Nothing other than the compiler designer's lack of foresight
precludes the parsing process of the compiler from passing whatever
information the code generation process needs to enable it to make wise
decisions on efficient object code generation.  Nothing other than the
compiler vendor's choices and the marketplace needs that compiler is
intended to meet mandates whether the code generation process they use is
built into the compiler, compiled in as a separate procedure, or obtained,
purloined or co-opted from another party.

There's nothing whatever to prevent the compiler designer from informing a
code generation process provided by that same vendor that the code it's
generating is for the SEARCH verb.  If the code generation process has been
developed by the same folks that provided the parsing process, I'd be very
surprised if they didn't communicate well enough to ensure that the code
generation process was given enough information by the parser to generate
relatively optimal code!  Are you assuming that, generally speaking, COBOL
compilers produce code that's actually turned into object code by a program
built/developed/marketed by someone other than the compiler vendor?  I don't
think that's all that common.

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alphabets

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-19T09:06:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef16667.49757663@news.optonline.net>`
- **References:** `<bcd1ie$2qcv$1@si05.rsvl.unisys.com> <3eeac912.236758765@news.optonline.net> <bcl0mm$27n2$1@si05.rsvl.unisys.com> <3eeeaedd.207409527@news.optonline.net> <bcn8ql$p5o$1@si05.rsvl.unisys.com> <3eefb101.273503437@news.optonline.net> <bcps5k$2k7l$1@si05.rsvl.unisys.com> <3ef08efb.330337761@news.optonline.net> <bcqfig$p5$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>There's nothing whatever to prevent the compiler designer from informing a
>code generation process provided by that same vendor that the code it's
…[7 more quoted lines elided]…
>think that's all that common.

Historically, it had not been common. But current compiler design, as seen in
JVM and .Net (and, I suspect, LE) are changing that precept.

Earlier, the separation between front-end and back-end was not so evident to the
end-user (programmer), but may have resulted from political dynamics within the
compiler producer. Noting it already had an INT->native translator for languages
X and Y, and a limited budget for the Z compiler, it would be tempting to reuse
it even though it's not optimized for Z.  Management sees the issue as technical
quibbling rather than strategic.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
