[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ZOS Compiler options TEST OPT

_8 messages · 3 participants · 2013-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### ZOS Compiler options TEST OPT

- **From:** "charles.leviton" <ua-author-14486870@usenetarchives.gap>
- **Date:** 2013-07-10T16:57:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com>`

```
hi,
With Enterprise cobol 4.2 if I want to use TEST=SEP as a compiler option so I can debug my program I'm not allowed to have OPT=STD.

My question is what do shops who want to be able to test but also have the optimized code feature do? Do their SCMs have 2 sets of compiler options, one for development and another for staging/QA?

Thanks!
```

#### ↳ Re: ZOS Compiler options TEST OPT

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-10T22:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com>`

```
cha··n@gm··l.com wrote:
› hi,
› With Enterprise cobol 4.2 if I want to use TEST=SEP as a compiler
…[6 more quoted lines elided]…
› Thanks!

Historically, there has never been any point in optimizing generated code
while it is being debugged.

But you raise a good point. The practice is predicated on the assumption
that optimizing the code will not change the logic of it in any way.
(Originally, optimization was about removing superfluous instructions that
were inserted by the compiler in case they were needed; it has come a long
way since then...)

Generally, you can trust the optimization process not to change your logic.
I can think of ONE occasion where optimizing a COBOL program caused it to
produce a different result from the non-optimized code, and that is in over
40 years of COBOL programming. It was NOT on a zOS platform.

So, in answer to your question, yes, it would be usual to have two sets of
compile options, one for development and one for production. There would be
nothing to prevent a third set for QA or pre-production.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: ZOS Compiler options TEST OPT

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2013-07-10T23:47:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p2@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap>`

```
On Thu, 11 Jul 2013 14:30:22 +1200, "Pete Dashwood"
wrote:

› cha··n@gm··l.com wrote:
›› hi,
…[16 more quoted lines elided]…
› way since then...)


Not really sure about that. I'd not consider, say strength reduction,
to be merely "removing superfluous instructions that were inserted by
the compiler in case they were needed", and yet that was implemented
in the very first Fortran compilers.

Unless your definition of originally goes back further than that...
```

###### ↳ ↳ ↳ Re: ZOS Compiler options TEST OPT

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-11T08:59:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p3@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap> <gap-2b18a4ffc3-p3@usenetarchives.gap>`

```
Robert Wessel wrote:
› On Thu, 11 Jul 2013 14:30:22 +1200, "Pete Dashwood"
›  wrote:
…[27 more quoted lines elided]…
› Unless your definition of originally goes back further than that...

I can't speak to Fortran as I only used it "in passing" in the late 60s and
had no idea at that time what actual optimizations it was performing.

However, around that time, I did spend some time comparing optimized and
non-optimized assembler code produced by COBOL compilers on both IBM and
Burroughs equipment, and that led me to believe that most of the
optimization had to do with removal of superfluous low level instructions,
especially on the Burroughs equipment. For example, the B500 compiler always
generated code for an IF with a possible ELSE branch, whether ELSE was
specified in the COBOL source or not. The optimize pass removed these
instructions if they weren't required. (As well as doing other stuff). I am
well aware that modern optimizers are way more advanced than that.

I think the main point is that there is an implicit contract that if you
debug code, the logic of it will not be changed by compiler optimization.

And that principle should be true whatever high level language you are
writing in.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: ZOS Compiler options TEST OPT

_(reply depth: 4)_

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2013-07-11T16:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p4@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap> <gap-2b18a4ffc3-p3@usenetarchives.gap> <gap-2b18a4ffc3-p4@usenetarchives.gap>`

```
On Fri, 12 Jul 2013 00:59:21 +1200, "Pete Dashwood"
wrote:

› Robert Wessel wrote:
›› On Thu, 11 Jul 2013 14:30:22 +1200, "Pete Dashwood"
…[41 more quoted lines elided]…
› well aware that modern optimizers are way more advanced than that.


Certainly I've expressed my opinion of the quality of Cobol optimizers
in general more than once, much to many people's annoyance in these
parts.

Still, dead code removal *is* a quite standard optimization, although
most compilers don't go quite so far out of their way to actually
insert dead code as you describe (dead code usually arises from other
optimizations).

My point was merely that optimization covered a much broader area than
that, essentially back to be beginnings of compilers. The quality of
any particular implementation notwithstanding.


› I think the main point is that there is an implicit contract that if you 
› debug code, the logic of it will not be changed by compiler optimization.
› 
› And that principle should be true whatever high level language you are 
› writing in.


It may be implicit, but there have certainly been many issues over the
years. If you ever worked with PL/1 in the early days, the odds of
your program working (or working the same way) the first time when
switching from the checkout to the optimizing compiler were
depressingly low.

And these days, especially you start to see some odd effects as
optimization get more sophisticated, especially with languages that
expose undefined behavior or low level details. A number of
optimization "bugs" have bitten various C and C++ have bitten projects
as big as the Linux kernel over the last decade.

Even simple things can cause problems. The initial values of
uninitialized stack (auto) variables is a good example - at the very
least, it involves the interpretation of stack garbage, which can
obviously change as the compiler optimizes the code. In some case the
debug versions explicitly clear the stack variable area. For a C
compiler, for example, any of those is valid, and you cannot actually
depend on the values, but more than a few programs do.

An interesting, and subtle, debate is exactly what then makes a valid
C program, and exactly under what conditions that remains true. In
one Linux kernel example, for instance, the compiler elided a test for
a null pointer because the pointer was dereferenced earlier in the
routine, and for a *normal* environment that would have lead to a
trap, as most environments make low addresses invalid, thus a
reference to a typical null pointer results in a trap, and that
behavior was assumed by the compiler. In the Linux, that's *not* true
when you're in kernel mode, so the assumed trap never happened, and
the then the elided null pointer check (obviously) didn't happen, and
then there was a security exposure. Oopsie.

The problem is significantly reduced with languages that are very
closely specified (Java, for example), and that don't expose low level
details (no raw pointers, for example). OTOH, C and C++ have
certainly been accused of not being high level languages, so perhaps
that's the answer. (And just to stay topical, Cobol exposes a number
of the same problems with it's broadly uncontrolled unions).
```

###### ↳ ↳ ↳ Re: ZOS Compiler options TEST OPT

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-11T20:39:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p5@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap> <gap-2b18a4ffc3-p3@usenetarchives.gap> <gap-2b18a4ffc3-p4@usenetarchives.gap> <gap-2b18a4ffc3-p5@usenetarchives.gap>`

```
Robert Wessel wrote:
› On Fri, 12 Jul 2013 00:59:21 +1200, "Pete Dashwood"
›  wrote:
…[108 more quoted lines elided]…
› of the same problems with it's broadly uncontrolled unions).

Thanks Robert.

I found your post interesting and informative. (Even though I don't
currently use C/C++ or Linux).

Compiler optimization in general is a huge topic and there are some very
clever people working in it.

Pete.

"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: ZOS Compiler options TEST OPT

- **From:** "charles.leviton" <ua-author-14486870@usenetarchives.gap>
- **Date:** 2013-07-11T09:35:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p2@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap>`

```
On Wednesday, July 10, 2013 10:30:22 PM UTC-4, Pete Dashwood wrote:

› 
›› hi,
…[59 more quoted lines elided]…
› "I used to write COBOL...now I can do anything."

Thanks Pete, for confirming and the addnl insight.
```

###### ↳ ↳ ↳ Re: ZOS Compiler options TEST OPT

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-12T00:21:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2b18a4ffc3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2b18a4ffc3-p7@usenetarchives.gap>`
- **References:** `<36bb6e03-eb5c-43ae-88c9-c8c791fbf1ac@googlegroups.com> <gap-2b18a4ffc3-p2@usenetarchives.gap> <gap-2b18a4ffc3-p7@usenetarchives.gap>`

```
cha··n@gm··l.com wrote:
› On Wednesday, July 10, 2013 10:30:22 PM UTC-4, Pete Dashwood wrote:
› 
…[72 more quoted lines elided]…
› Thanks Pete, for confirming and the addnl insight.

No problem, glad to help :-)

Pete.

"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
