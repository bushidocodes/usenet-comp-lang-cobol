[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Quantum extensions in HL-languages

_16 messages · 8 participants · 2001-01_

---

### Quantum extensions in HL-languages

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2001-01-17T23:20:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de>`

```
2001-01-17 23:23:23 MET

A few weeks ago, I was speculating about quantum computing
concepts in high level languages and high level language
compilers right here. I did some reading in the meantime, but I
did not get much wiser.

As a new standard for COBOL is being defined at this time,
one could include a few quantum concepts, without affecting
other parts of the language. But the practical value is
nothing more than a sort of marketing gag. It would sound
swell indeed: "COBOL first quantum computing language!"

But that's all. No immediate practical value.

However, it is legitimate to ponder which concepts could be
included into a programming language right now safely. To
my mind, there are three:

1) The ability to define qbit data. In COBOL, this would be an
   extension to the PIC clause.

2) The Hadamard operator. This is needed for doing a quantum
   rotation on single qbits in order to effect the superposition
   of 0 and 1. In COBOL, it could have the form of an intrinsic
   function.

3) Decoherence - either implied, that is, decoherence takes
   place anytime qbit data are moved back into ordinary data -
   or explicit, also in the form of an intrinsic function.

That's all for now. Computing with qbits needs reversible
operations - and most of the ordinary things one can do in a
programming language are not reversible by themselves. They
*can* be made reversible, but the point is, there are operations
which are more easily expressed as reversible. Fast Fourier
Transforms, for instance, is easily done in a reversible manner,
but a simple addition is not (It could be made, but the logic
has to be constructed specially for qbits, out of Toffoli
gates and such. Thats an issue of hardware-architecture.).

So one had to decide (somewhen in the future) which operations
are allowed for qbit-data and which ones are not, and which
kind of new operations should be included into the language.

Then, a few sequentional computations must be possible while
taking care not to effect decoherence too early (which is
quite a challenge for hardware engineers!). The language
must allow that. But it is not possible, in any language,
to examine qbit data by inspection. No IF and no EVALUATE,
at least on qbit data! - I expect, a working compiler for
quantum code should have a look on this (for that reason,
I would prefer an explicit decoherence operator above
so that a compiler can do some checking - that's a cleaner
solution.).
```

#### ↳ Re: Quantum extensions in HL-languages

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-18T13:14:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<945fu4$g96$1@hermes.enternet.co.nz>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de>`

```

Herwig Huener & Josella Simone Playton wrote in message
<3A661AB1.1D38CDA9@Josella-Simone-Playton.de>...
>2001-01-17 23:23:23 MET


>As a new standard for COBOL is being defined at this time,
>one could include a few quantum concepts, without affecting
>other parts of the language.

Have you any idea of how difficult it is to get ANYTHING into this standard?
The process which is followed involves committees and reviews and drafts and
public reviews and then a final draft (a year later...). We are having a
very hard time just getting Object Oriented Extensions which everyone can
agree on, into the 2001 Standard. And this is REAL!

A submission to J4 with Quantum extensions as you describe would necessarily
push the whole process even further back, and the chance of anyone
understanding and supporting the proposed extensions is "small but finite"
(about the same chance as the molecules of your body aligning with the
spaces in the wall, thus allowing you to pass through it...it COULD happen,
but you might have to wait longer than the age of the Universe for it to
occur...<G>)

>>>
>But the practical value is
…[4 more quoted lines elided]…
>
<<<
Agree it SOUNDS good... but it would also make COBOL look very stupid when
we explained that it is impossible to implement...


>>>
>However, it is legitimate to ponder which concepts could be
…[14 more quoted lines elided]…
>
<<<
Now it's just getting silly...

I'll suspend belief (for  the sake of your argument) and buy number 1
above...the ability to define a qbit.

Now we come to number 2... The Hadamard operator. As soon as you try and do
ANY kind of operation on a qbit you collapse the wave function and drop it
into Reality...Even just LOOKING at it will do this.

Now consider that I  am a COBOL compiler writer. (As I once was, "long ago,
in a distant Galaxy"...)

You are asking me to define storage that I must NEVER reference...!

Option 3 hardly needs to be an intrinsic function; you can  (and will) get
decoherence just by referencing the qbit.

The current state of computing (based on the sequential Von Neumann model)
is not ready for Quantum Computing. This includes the compiler writers.

Neither is the Engineering community. The fact that some extremely expensive
projects in some Academic ivory towers have managed to produce a Quantum
device with 4 Qbits, does NOT mean that such devices are "just around the
corner".

There are still enough questions over the whole field to confine it to the
marble halls of Acadaemia for the foreseeable future.

Assuming such a device COULD be built, and software to operate it COULD be
written, it is VERY unlikely that COBOL will be the language of choice. By
the time such a device is operating (if EVER) COBOL programming will have
been relegated to the history books and will be about as relevant as Latin
is today. (Useful for research and history, not practical current
applications...)


>
>So one had to decide (somewhen in the future) which operations
>are allowed for qbit-data and which ones are not, and which
>kind of new operations should be included into the language.
>
Well that's pretty easy...EXISTS or NOT EXISTS just about covers it for a
Qbit...

The whole concept of "operations" on Qbits is a contradiction in terms. As
soon as you do ANY kind of operation on it, it is no longer a Qbit.

>>>
>Then, a few sequentional computations must be possible while
…[4 more quoted lines elided]…
>at least on qbit data! -
<<<
You got that right...!!! And it is a "cop out" to suggest that delaying
decoherence is an engineering problem.

The whole concept is unworkable within the framework of Von Neumann
computing.

And that is the framework within which current programmers (and the COBOL
Language) exist.


>>>
>This was the limited supply of ideas I have now. I have found
>not much information in the net on how a sequential quantum
>algorithm should look like - and a programmer in a quantum
>language should be fluent in such things.
<<<
I have tried to show that a "Sequential Quantum Algorithm" is a
contradiction in terms (like "Military Intelligence" or "Customer Service"
from your Bank...<G>).

It doesn't suprise me you have found nothing. Quantum Algorithms (IF and
when we EVER achieve a practical implementation of them) MUST be parallell
by their very nature. A Quantum Algorithm would operate across the
Multiverse until decoherence. It cannot be sequential.

OK, Herwig, a refreshing and stimulating idea (not to mention good fun) but
please don't
get serious about connecting it to COBOL.

COBOL is having enough image problems at the moment without being labelled
as a "crank" vehicle.

Regards,

Pete.
```

##### ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-18T01:20:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a664494.130011228@news1.attglobal.net>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz>`

```
Why not sumbit the Quantum extension to J4 as a "Candidate for a
future revision".  Why?  Because COBOL can leap frog the
"competition".  No new proposals will get any real consideration at
this point  -- for this draft -- but can go on the "candidate for a
future revision" list.

On Thu, 18 Jan 2001 13:14:38 +1300, "Peter E. C. Dashwood"
<dashwood@enternet.co.nz> wrote:

>
>Herwig Huener & Josella Simone Playton wrote in message
…[142 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2001-01-18T08:35:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A669CD0.46FA99B2@Josella-Simone-Playton.de>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3a664494.130011228@news1.attglobal.net>`

```
2001-01-18 08:38:00 MET

Thane Hubbell wrote:
> 
> Why not sumbit the Quantum extension to J4 as a "Candidate for a
…[3 more quoted lines elided]…
> future revision" list.

I consider that. But I have yet to make myself wiser - it
is a difficult subject, you know.

But I do not want to keep these thoughts a secret.

Herwig
```

##### ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** Herwig Huener & Josella Simone Playton <webmaster@Josella-Simone-Playton.de>
- **Date:** 2001-01-18T08:33:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A669C3C.50711B50@Josella-Simone-Playton.de>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz>`

```
2001-01-17 08:36:00 MEZ

"Peter E. C. Dashwood" wrote:
> 
> Herwig Huener & Josella Simone Playton wrote in message
…[7 more quoted lines elided]…
> Have you any idea of how difficult it is to get ANYTHING into this standard?

Yes!

> ...

> Agree it SOUNDS good... but it would also make COBOL look very stupid when
> we explained that it is impossible to implement...

Not really. We can blame the hardware-engineers.

...

> Now we come to number 2... The Hadamard operator. As soon as you try and do
> ANY kind of operation on a qbit you collapse the wave function and drop it
> into Reality...Even just LOOKING at it will do this.

The Hadamard operator is a quantum operator. It will not
collapse the wave-function.

> ...

> Now consider that I  am a COBOL compiler writer. (As I once was, "long ago,
> in a distant Galaxy"...)
> 
> You are asking me to define storage that I must NEVER reference...!

Unless you want to do decoherence. Then you may.

> ...

> Option 3 hardly needs to be an intrinsic function; you can  (and will) get
> decoherence just by referencing the qbit.

Not as long as the reference is done by reversible logic.

> ...

> The current state of computing (based on the sequential Von Neumann model)
> is not ready for Quantum Computing. This includes the compiler writers.

This is correct. The Turing machine does not exist. And,
as I said, there is not yet a engineer-discipline for
writing quantum algorithms.

> Neither is the Engineering community. The fact that some extremely expensive
> projects in some Academic ivory towers have managed to produce a Quantum
…[4 more quoted lines elided]…
> marble halls of Acadaemia for the foreseeable future.

Yep.

> Assuming such a device COULD be built, and software to operate it COULD be
> written, it is VERY unlikely that COBOL will be the language of choice. By
…[3 more quoted lines elided]…
> applications...)

What are you saying about  COBOL in a COBOL-newsgroup?
If there are classical programming languages around,
sowill COBOL.

> ...

> >So one had to decide (somewhen in the future) which operations
> >are allowed for qbit-data and which ones are not, and which
…[6 more quoted lines elided]…
> soon as you do ANY kind of operation on it, it is no longer a Qbit.

You may have a point there. Maybe one could call a reversible
operation not "operation". No idea.

> ...
> 
> The whole concept is unworkable within the framework of Von Neumann
> computing.

Which must be the case, because, as I said, Quantum Computing
is a step beyond classical computing.

> And that is the framework within which current programmers (and the COBOL
> Language) exist.

> ...
> 
…[3 more quoted lines elided]…
> Multiverse until decoherence. It cannot be sequential.

Misunderstanding there. A few quantum computation steps
might be carried out in succession.

> ...
> OK, Herwig, a refreshing and stimulating idea (not to mention good fun) but
…[4 more quoted lines elided]…
> as a "crank" vehicle.

Well, thinking aloud is legitimate, isn't it?

Herwig
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-19T03:04:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<946vho$iv7$4@hermes.enternet.co.nz>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3A669C3C.50711B50@Josella-Simone-Playton.de>`

```

Herwig Huener & Josella Simone Playton wrote in message
<3A669C3C.50711B50@Josella-Simone-Playton.de>...
>2001-01-17 08:36:00 MEZ
>
>"Peter E. C. Dashwood" wrote:

>>>
>> Agree it SOUNDS good... but it would also make COBOL look very stupid
when
>> we explained that it is impossible to implement...
>
>Not really. We can blame the hardware-engineers.
<<<
Hahaha! I LOVED that, Herwig! Excellent!

>>>
>
>> Now we come to number 2... The Hadamard operator. As soon as you try and
do
>> ANY kind of operation on a qbit you collapse the wave function and drop
it
>> into Reality...Even just LOOKING at it will do this.
>
>The Hadamard operator is a quantum operator. It will not
>collapse the wave-function.
<<<
er... in that case, it can NEVER be implemented in a Quantum computer.

Herwig, we MUST draw a distinction between theory and practice if you are
for one minute serious about officially extending the COBOL standard.
Irrespective of theoretical operations, in PRACTICE (certainly in THIS
Reality) ANY operation on QBits (other than superposition of states; which
is an inherent property and NOT an Operation) WILL collapse the wave
function with immediate consequent decoherence. Now, this might be OK if you
define your operation to occur AFTER decoherence...


>>>
>> Now consider that I  am a COBOL compiler writer. (As I once was, "long
ago,
>> in a distant Galaxy"...)
>>
>> You are asking me to define storage that I must NEVER reference...!
>
>Unless you want to do decoherence. Then you may.
<<<
OK. So EVERYTHING you are discussing is only achievable AFTER decoherence,
by analagous bits in this Universe.

Why have a Quantum Computer at all? Just build something with REAL bits in
it that emulates EVERY possible superposition and "train" it to examine
EVERY possible result, selecting the ones which might be a solution...(Bit
like a Super Chess program really...)

I would agree that that COULD be programmed in COBOL. In fact, it would
require no additions to the language spec...<G>

>>>
>> Option 3 hardly needs to be an intrinsic function; you can  (and will)
get
>> decoherence just by referencing the qbit.
>
>Not as long as the reference is done by reversible logic.
<<<
Well, I should've guessed that anyone who's prepared to take on J4 in order
to get non-implementable extensions to the COBOL Language, certainly
wouldn't hesitate to defy the Laws of Physics...<G>

Decoherence will occur whether the Qbit is referenced with reversible logic
or not.  But you know that...is this a wind up? <G>


>>>
>> Assuming such a device COULD be built, and software to operate it COULD
be
>> written, it is VERY unlikely that COBOL will be the language of choice.
By
>> the time such a device is operating (if EVER) COBOL programming will have
>> been relegated to the history books and will be about as relevant as
Latin
>> is today. (Useful for research and history, not practical current
>> applications...)
…[3 more quoted lines elided]…
>so will COBOL.
<<<
Well, my COBOL credentials are strong enough that I can be realistic about
the fate of the language.

(Indeed, "computer programming" in general. There is a limited life for the
current model.)

My comment is not a criticism of COBOL; it's a reflection of when Quantum
Computing is likely to become a reality...<G>

>>>
>Which must be the case, because, as I said, Quantum Computing
>is a step beyond classical computing.
<<<
As Science Fiction is a step beyond Science...

>>>
>> It doesn't suprise me you have found nothing. Quantum Algorithms (IF and
>> when we EVER achieve a practical implementation of them) MUST be
parallell
>> by their very nature. A Quantum Algorithm would operate across the
>> Multiverse until decoherence. It cannot be sequential.
>
>Misunderstanding there. A few quantum computation steps
>might be carried out in succession.
<<<
Yes, they MIGHT. BUT ONLY AFTER decoherence!

There is ONE possibility in all of this which MIGHT be a Show-Stopper or an
Enabler. The EPR effect (Einstein-Podolsky-Rosen). If the Qbit could be
constructed in such a way that it was composed of a wavicle AND an
anti-wavicle (notice I did NOT specify particle or wave), AND these two
wavicles could be subject to EPR separation, it MIGHT be possible to deduce
the state of a Qbit WITHOUT actually looking at it and thereby causing
decoherence. It's a pretty big MIGHT...and I have no idea how a device which
used such wavicles could be built in the Real world, but an EPR experiment
was successfully carried out in Paris in 1983, confirming the theoretical
predictions of Nils Bohr against those of Einstein, Podolsky, and Rosen. In
this regard, Quantum Mechanics violates Relativity and information "travels"
faster than light, being available at a distance instantaneously. Of course,
a Qbit which utilized the EPR effect could only be used ONCE... (unless
someone comes up with a bright idea to get round this...I believe the
University of Sussex are working on it (at least, they were in the
mid-Eighties...heard nothing since, which does NOT imply success...)

Come to think of it, this is more likely to be a Show-stopper...the probable
result would be an Infinity as the Qbit adopted the superposition and could
never return a bit state. So no useful information could be obtained, the
Uncertainty Principle is not violated, and God and Heisenberg chalk up
another one over Einstein...

All we are getting out of this is that there is no point in applying
conventional logic to the weird world of Quantum Mechanics.

I for one don't have enough in-depth knowledge in this field to predict the
outcomes, once you get away from the basic fundamental principles.

I DO understand enough to know what is feasible in the Real World at this
time. (At least I think I do...I'm really Uncertain  <G>)




>>>
>Well, thinking aloud is legitimate, isn't it?
<<<
Not only legitimate, but to be encouraged.

However, the bottom line is that Quantum extensions to COBOL are unrealistic
for the following reasons:

1. They cannot be implemented.

2. They cannot be implemented.

3. They cannot be implemented.

Pete.



>Herwig
>
…[4 more quoted lines elided]…
>GruberStrasse 10 A / D-85655 GrossHelfenDorf / Bayern / EU
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

_(reply depth: 4)_

- **From:** Herwig Huener <Herwig.Huener!@!fujitsu-siemens.com>
- **Date:** 2001-01-18T17:20:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9475bm$j6b$1@news.mch.sbs.de>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3A669C3C.50711B50@Josella-Simone-Playton.de> <946vho$iv7$4@hermes.enternet.co.nz>`

```
2001-01-18 17:19:21 MEZ

"Peter E. C. Dashwood" schrieb:
> 
> ...

> >The Hadamard operator is a quantum operator. It will not
> >collapse the wave-function.
> <<<
> er... in that case, it can NEVER be implemented in a Quantum computer.

What? It is most essential for a quantum computer. It is the device
which makes the superposition. You move a logical '0' to a qbit
and the hadamard operator creates the superposition

|0|   -->   x |0> + y |1>

(x and y same size)

If you wish, you can read that qbit right now, an decoherence will
happen, and you get either 0 or 1. But most probably you will do
something with those thusly prepared qbits.

> ...

> Herwig, we MUST draw a distinction between theory and practice if you are
> for one minute serious about officially extending the COBOL standard.

I have not yet thought about my degree of seriousness.

> Irrespective of theoretical operations, in PRACTICE (certainly in THIS
> Reality)

:-)

> ANY operation on QBits (other than superposition of states; which
> is an inherent property and NOT an Operation) WILL collapse the wave
> function with immediate consequent decoherence. Now, this might be OK if you
> define your operation to occur AFTER decoherence...

which would be ordinary logical operations. Those collapse indeed,
but for those, wee need no quantum computer.

Operations which do not destroy information do not necessarily
make decoherence - and the class of hadamard operators belong to
those (might be that those operations are called "unitary operators",
but my knowledge of QM is feeble).

I would categorize hardware gates as follows:

---------------------+-----------------------------
ordinary logic       |     causes decoherence
gates (AND, OR,      |     & generates entropy
NAND, NOR, XOR)      |     classical logic
---------------------+-----------------------------
reversible logic     |     no decoherence
gates (Fredkin,      |
Toffoli, NOT, ...)   |
---------------------+-----------------------------
reversible quantum   |     no decoherence,
rotations            |     causing interference
(Hadamard, ...)      |     of superpositions
---------------------+-----------------------------

Today, our computers are build from the first category of gates,
the other two would be needed for a quantum computer. As for
me, I regard the second row of gates as a way to compute
reversibly with different data, and the third row as a way
to compute with the same data in different superpositions.
The third row extends quantum algorithms into the direction
of multiverses. Therefrom comes the power of quantum algorithms.

As far as I have grasped it.

> ...

> Why have a Quantum Computer at all? Just build something with REAL bits in
> it that emulates EVERY possible superposition and "train" it to examine
> EVERY possible result, selecting the ones which might be a solution...(Bit
> like a Super Chess program really...)

Of course you can simulate a quantum program with classical logic.
In some cases, a few 10^100 computation steps are necessary -
depending on your data.

> ...

> Well, I should've guessed that anyone who's prepared to take on J4 in order
> to get non-implementable extensions to the COBOL Language, certainly
> wouldn't hesitate to defy the Laws of Physics...<G>

Well, let us see the results of the public review.
Maybe J4 will be drowned in non-implementable
extensions!

> ...

> >What are you saying about  COBOL in a COBOL-newsgroup?
> >If there are classical programming languages around,
…[6 more quoted lines elided]…
> current model.)

Yes! But (OT now): COBOL is oftenly the language in large
institutions. Large institutions suffer from Bureaucracy.
Bureaucracy is for ever. So COBOL is forever. - OT end.

> ...

> >> It doesn't suprise me you have found nothing. Quantum Algorithms (IF and
> >> when we EVER achieve a practical implementation of them) MUST be
…[7 more quoted lines elided]…
> Yes, they MIGHT. BUT ONLY AFTER decoherence!

No. What I have in mind is a compiler analyzing several
successive quantum operations, compute a reversible
net of gates which do exactly that computations and
generate instructions which command the hardware to
assemble those gates into that logical network so
that they might do this sequence of operations in
a reversible manner in one step.

You are right: We are in the Science Fiction business
now.

BTW (OT again): Suppose the commity draft would get
the famous HUGO-Award (an award for Science Fuction).
Would they be offended or flattered? - OT off.

> ...

> There is ONE possibility in all of this which MIGHT be a Show-Stopper or an
> Enabler. The EPR effect (Einstein-Podolsky-Rosen). If the Qbit could be
…[4 more quoted lines elided]…
> decoherence.

It cannot be done. Suppose I prepare two entagled qbits:

x |00> + y |11> + 0 |01> + 0 |10>

(x and y same size)

If you look on one of the qbits in order to find out
what the state of the other one is, you cause
decoherence for both. In the multiverse-view, you find
yorself either in the universe with both bits 1 or in
the universe with both bits 0. The universes with the
qbit combinations 01 and 10 do not exist.
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-19T13:03:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9482d4$kfu$1@hermes.enternet.co.nz>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3A669C3C.50711B50@Josella-Simone-Playton.de> <946vho$iv7$4@hermes.enternet.co.nz> <9475bm$j6b$1@news.mch.sbs.de>`

```
Some interesting ideas, Herwig.

I agree you are correct about entanglement. Decoherence in both universes
would occur; that's why I suggested that such a Qbit device could be used
only once...It is totally impractical and arose from my effort to try and
see SOME way we could view or deduce the actual state of a qbit. This is
completely fallacious as the actual state of the Qbit is the superposition
and anything else is irrelevant...I guess a lifetime of computer programming
causes us to think in certain ways, which are completely inappropriate to
QM...

It seems to me that your grasp of Theory is excellent but you may have
missed the practical problems of translating this into the current Reality
(whatever the Hell THAT is...!)

I also believe that the Universe shrouds her secrets behind things like the
Uncertainty Principle and there may be some nasty surprises in store when we
actually start to build Quantum Computers.

I liked your analogy of the eye, the telescope and the photons, but I am
still not totally persuaded...

Anyway, I can't spend any more time on this. Thanks for the stimulation and
keep taking the tablets...!

Pete.
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

_(reply depth: 6)_

- **From:** Herwig Huener <Herwig.Huener!@!fujitsu-siemens.com>
- **Date:** 2001-01-19T10:29:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9491kt$2mh$1@news.mch.sbs.de>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3A669C3C.50711B50@Josella-Simone-Playton.de> <946vho$iv7$4@hermes.enternet.co.nz> <9475bm$j6b$1@news.mch.sbs.de> <9482d4$kfu$1@hermes.enternet.co.nz>`

```
2001-01-19 10:33:01 MET

"Peter E. C. Dashwood" schrieb:
> 
> Some interesting ideas, Herwig.
…[8 more quoted lines elided]…
> QM...

A nice way to say that we are too old to learn new concepts!
And that is certainly right: I have my difficulties with
QM. Back in the old days when I made my diploma, I tried to
avoid QM. Successful.

> It seems to me that your grasp of Theory is excellent but you may have
> missed the practical problems of translating this into the current Reality
> (whatever the Hell THAT is...!)

One could be depressed when one sees the first prototypes
of qbits which are built this time. But then, technical
progress comes in surprises. And, as I told, we have
already quantum computation devices, such as optical
instruments. So we know it's not impossible, and we
should somehow be prepared.

Just the small detail of rewriting the foundations of
computer science is yet unfinished, but I trust David
Deutsch will do a good job there.

With the proof that the classical Turing machine does not
exist, it follows that no classical programming language
exists. Including COBOL.

But we wont tell our customers and continue to
sell a COBOL-compiler!

> I also believe that the Universe shrouds her secrets behind things like the
> Uncertainty Principle and there may be some nasty surprises in store when we
> actually start to build Quantum Computers.

One of the nasty surprises is (might be) that the universe
is isomorph to a mathematical structure. Then it is not
necessary that the universe exists - we would not see the
difference!

> I liked your analogy of the eye, the telescope and the photons, but I am
> still not totally persuaded...
> 
> Anyway, I can't spend any more time on this. Thanks for the stimulation and
> keep taking the tablets...!

Now and then I shall continue to drop some ideas here.
But I also cannot spend more time on this right
now because my employer expects me contributing to our
COBOL compiler, and not proving that no COBOL and no
computers exist.

Herwig
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-22T02:20:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a6adea8.54982763@news1.attglobal.net>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <945fu4$g96$1@hermes.enternet.co.nz> <3A669C3C.50711B50@Josella-Simone-Playton.de>`

```
There's a good article on Quantum computers and quantum computing in a
recent Dr. Dobbs Journal.  Just FYI.

On Thu, 18 Jan 2001 08:33:16 +0100, Herwig Huener & Josella Simone
Playton  <webmaster@Josella-Simone-Playton.de> wrote:

>2001-01-17 08:36:00 MEZ
>
…[128 more quoted lines elided]…
>GruberStrasse 10 A / D-85655 GrossHelfenDorf / Bayern / EU

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Quantum extensions in HL-languages

- **From:** "TJ Dombrowski" <keldin@earthlink.not>
- **Date:** 2001-01-18T05:50:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de>`

```
I would be satisfied if Cobol would have unsigned comp-3 as a datatype for
reading data from
unix programmers that don't know how to pack data properly.
Why do unix "programmers" (used lightly)  insist on packing data as  4321
instead of   S999 or S99999.  s9(3) comp-3 or s9(5) comp-3. I keep getting
data from people packing it as 9999 (packed with no sign)
signed comp-3 should always be odd so the sign fits in the field. It's
getting anoying to fix these fields.
Currently using MVS COBOL II, does the lastest OS/390 COBOL II have a new
type for these?

Have fun
TJ

"Herwig Huener & Josella Simone Playton"
<webmaster@Josella-Simone-Playton.de> wrote in message
news:3A661AB1.1D38CDA9@Josella-Simone-Playton.de...
> 2001-01-17 23:23:23 MET
>
…[3 more quoted lines elided]…
> did not get much wiser.

> 1) The ability to define qbit data. In COBOL, this would be an
>    extension to the PIC clause.
```

##### ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-18T00:44:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9463d6$cgd$1@nntp9.atl.mindspring.net>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>`

```
No, the latest IBM mainframe (or workstation) COBOL compiler does NOT
provide a data-type for unsigned packed-decimal items.  (You can "specify" a
PIC 999 COMP-3 or Packed-Decimal data description - but it still assigns
storage for the sign-nibble).

The ANSI/ISO Standard (past, current, and future) allow the implementor to
decide what to do with such fields.  Some vendors have a "COMP-6" usage
specifically for this - but not IBM.

P.S.  Of course you CAN always do a SHARE requirement to ask for this - but
I don't think you should hold your breath until IBM provides it.
```

##### ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-01-18T12:31:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010118073125.06843.00000880@nso-fc.aol.com>`
- **References:** `<muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>`

```
In article <muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>, "TJ
Dombrowski" <keldin@earthlink.not> writes:

>I would be satisfied if Cobol would have unsigned comp-3 as a datatype for
>reading data from
…[8 more quoted lines elided]…
>

Unix is not the only other flavor out there that does not believe in the 
requirement of a 'sign' on a packed-decimal field.
The Unisys Small and Medium systems come to mind as this is where
I cut my teeth on most of my learning experiences.  Now in the process
of migrating to Large systems and I have not yet devled into the intricacies
of data presentation.  I am having enough opportunities with straight COBOL
code migration and feature / function aspects that do not exist on the new 
platform.
```

###### ↳ ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2001-01-18T22:22:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<947qab$fk$1@nnrp1.deja.com>`
- **References:** `<muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net> <20010118073125.06843.00000880@nso-fc.aol.com>`

```
I have been using a product that uses assembly to strip off the sign
bit by starting from a given half-byte, either left or right. I don't
know what good that would do if at all compared to how COBOL reads the
data.  When I was taking Assembly, when we packed a number, it had an
initially non-signed state, but it still had a sign bit.  Then when you
moved it or used it in an operation it had a specific sign applied to
it.  In assembly it also took 5 steps to add the dollar sign without a
macro; Of course we used an assembler that fit on one floppy disk.


In article <20010118073125.06843.00000880@nso-fc.aol.com>,
  sff5ky@aol.comxxx123 (Sff5ky) wrote:
> In article <muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>, "TJ
> Dombrowski" <keldin@earthlink.not> writes:
>
> >I would be satisfied if Cobol would have unsigned comp-3 as a
datatype for
> >reading data from
> >unix programmers that don't know how to pack data properly.
> >Why do unix "programmers" (used lightly)  insist on packing data as
4321
> >instead of   S999 or S99999.  s9(3) comp-3 or s9(5) comp-3. I keep
getting
> >data from people packing it as 9999 (packed with no sign)
> >signed comp-3 should always be odd so the sign fits in the field.
It's
> >getting anoying to fix these fields.
> >Currently using MVS COBOL II, does the lastest OS/390 COBOL II have
a new
> >type for these?
> >
>
> Unix is not the only other flavor out there that does not believe in
the
> requirement of a 'sign' on a packed-decimal field.
> The Unisys Small and Medium systems come to mind as this is where
> I cut my teeth on most of my learning experiences.  Now in the process
> of migrating to Large systems and I have not yet devled into the
intricacies
> of data presentation.  I am having enough opportunities with straight
COBOL
> code migration and feature / function aspects that do not exist on
the new
> platform.
>
>


Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ unsigned comp-3

_(reply depth: 4)_

- **From:** "TJ Dombrowski" <keldin@earthlink.not>
- **Date:** 2001-01-19T03:15:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LjO96.4644$tD2.289826@newsread1.prod.itd.earthlink.net>`
- **References:** `<muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net> <20010118073125.06843.00000880@nso-fc.aol.com> <947qab$fk$1@nnrp1.deja.com>`

```
COBOL in MVS needs the sign nibble for COMP-3 or you cant use the field.
so if you send a file from some other system to an IBM mainframe.  You
should
save room for the sign and use an odd number of digits.

These people think they are saving space in transmission of half a byte.
They have no idea that they are making all of these fields very difficult to
use.

Their standard response is well SAS can read it.  Well thats fine and dandy
but SAS isnt production COBOL is.     See the anaylsts who do the
requirements
don't care if the programmers that have to load the crap have trouble.
since they use SAS 98% of the time what do they care.

Its seems to be happing more and more.




<lcccpiasabird@my-deja.com> wrote in message
news:947qab$fk$1@nnrp1.deja.com...
> I have been using a product that uses assembly to strip off the sign
> bit by starting from a given half-byte, either left or right. I don't
…[48 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Quantum extensions in HL-languages

- **From:** Liam Devlin <LiamD@optonline.net>
- **Date:** 2001-01-19T05:22:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A67CEFA.FBE4DA2@optonline.net>`
- **References:** `<3A661AB1.1D38CDA9@Josella-Simone-Playton.de> <muv96.326$tD2.32052@newsread1.prod.itd.earthlink.net>`

```
TJ Dombrowski wrote:

> I would be satisfied if Cobol would have unsigned comp-3 as a datatype for
> reading data from
…[7 more quoted lines elided]…
> type for these?

This is a hardware specification, not a COBOL one. It's the way packed-decimal
numbers have been implemented on IBM boxes since the S/360's (almost 40 years
ago, they were announced in April, 1964).

LiamD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
