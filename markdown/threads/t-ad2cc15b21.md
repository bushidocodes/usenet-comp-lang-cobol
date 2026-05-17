[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I Need Professional Help!

_38 messages · 12 participants · 1995-01_

---

### I Need Professional Help!

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-05T18:06:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ehu1i$rlr@panix3.panix.com>`

```
My stupid shop has this stupid standard [I'm in a foul mood]: all
paragraphs must be PERFORMed THRU an EXIT paragraph, to give lazy
programmers somewhere to GO TO.

Well, my whole 5 years in the Cobol biz at this place, I have flagrantly
violated this horrible standard. I do not GO TO. I am allergic to it,
it's against my religion, & I just wasn't raised that way. So I have no
need of EXITs, nor of PERFORMing THRU, which is always a bad idea. Cobol
is a structured language. I see no need to turn it into Assembler.

Well, I've been found out. I'm starting work on a new project, & my
director says to me today, "Oh yeah, one more thing. Uh... I don't want
you to get..." Voice trails off. "Well, I was looking at your [one of
my] programs one time, & I noticed you don't use EXIT paragraphs. That
is a standard, you know." I've been discovered & am now going to be
politely forced to write bad code.

Putting in extra EXIT paragraphs that I never use will be hard enough.
But PERFORMing each and every routine THRU an EXIT is just going to kill
me. Help me. I need support. The wasted space, the wasted typing, the
wasted execution time, the ugliness, the wordiness, the uselessness, the
room for error in forgetting an exit or misnaming an exit... the pain is
going to rip through me every time I type those hated words THRU and
EXIT. Does the pain go away? Does it get easier? Do you think I can
make it through this? O unhappy day.
```

#### ↳ Re: I Need Professional Help!

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-05T22:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
THis is indeed a very nasty standard (exit paras required everywhere). It
is contemtuous of reasonable style. Even those of us who would occasionally
use gotos would never put up with this kind of nonsense, so I certainly
sympatheize.

Why not write a little utility that takes your nice code and uglifies it.
You can probably write two utilities, since, at least for your code where
the exit paras will come only from the uglifier, a corresponding prettifier
can be easily written. Then you can get the code, prettify it, work on it,
and uglify it again before putting it back in the configuration system.
Of course if someone else touches your code and stuffs in junk gotos, then
the prettifier might not work.

This is disheartening, COBOL is a pretty nice language (let's say for me it
is my second favorite language, after Ada 95), and it is a shame for people
to adopt coding standard that guarantee that the code will look terrible and
be hard to read.
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "cgo..." <ua-author-7675889@usenetarchives.gap>
- **Date:** 1995-01-07T12:35:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p2@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p2@usenetarchives.gap>`

```
I have a reccomendation. Use all inline performs so you can ensure pure structured code and keep you concience clean about using THRU and EXIT.

You whole program could be written with only the initial paragraph name (Some compilers don't even need this,

i.e. PERFORM
blab
blab
END-PERFORM

Another approach is to ensure your code is purely structures
Use no GO TOs at all and only insert a period as a seperate line ONLY at the end if the paragraph. This will ensure good clean structure. If forced, you could then add GO TO ---Exit as the last statmeent in the para.

Charles Godwin - Ottawa ON
tel (613) 761-1420
fax (613) 761-1422
```

#### ↳ Re: I Need Professional Help!

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-01-06T04:33:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
tip··.@pa··x.com (Christine Tiplady) wrote:
›
› My stupid shop has this stupid standard [I'm in a foul mood]: all
› paragraphs must be PERFORMed THRU an EXIT paragraph, to give lazy
› programmers somewhere to GO TO.
..

PERFORM THRU has the problem that it allows overlapping perform ranges.
The effects of overlapping perform ranges depend on how the return addresses
are held in the COBOL system. ANSI does not specify how return addresses
are held so each compiler writer can choose his own method.

Net effect is that programs using PERFORM THRU are less likely to be
portable between different COBOL systems. The rules in your shop seem
to make portable programs less likely whatever the other benefits.

Overlapping perform ranges are hardly easier to understand either. Here's
an example of what I mean:

procedure division.
a. perform b thru d-exit display "a1".
perform b thru e-exit display "a2".
go to f-exit.
b. perform c thru e-exit display "b".
c. display "c".
d-exit. display "d".
e-exit. display "e".
f-exit. stop run.

At run time the results for
MF COBOL: c d e b c d a1 c d e b c d e a2
OS/VS COBOL: c d a1 c d e b c d e a2
RM/COBOL: c d a1 c d e b c d e

(nb. above is native MF COBOL, it has directives to emulate the others)

Useful ammo for you Christine or are there other rules (enforced?) to
prevent this sort of thing?
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-06T06:01:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p4@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p4@usenetarchives.gap>`

```
On 6 Jan 1995 09:33:59 GMT, Martyn Woerner (m.··.@mfl··o.uk) wrote:
› tip··.@pa··x.com (Christine Tiplady) wrote:
›› 
…[3 more quoted lines elided]…
› ..
 
› PERFORM THRU has the problem that it allows overlapping perform ranges.
› The effects of overlapping perform ranges depend on how the return addresses
› are held in the COBOL system.  ANSI does not specify how return addresses
› are held so each compiler writer can choose his own method.
 
› Net effect is that programs using PERFORM THRU are less likely to be
› portable between different COBOL systems.  The rules in your shop seem
› to make portable programs less likely whatever the other benefits.
 
› Overlapping perform ranges are hardly easier to understand either.  Here's
› an example of what I mean:
 
› procedure division.
› a. perform b thru d-exit display "a1".
…[6 more quoted lines elided]…
› f-exit. stop run.
 
› At run time the results for
› MF COBOL:    c  d  e  b  c  d  a1 c  d  e  b  c  d  e  a2
› OS/VS COBOL: c  d  a1 c  d  e  b  c  d  e  a2
› RM/COBOL:    c  d  a1 c  d  e  b  c  d  e

Not to defend a silly standard, but the way PERFORM THRU exit paragraph is
usually used is to have an exit paragraph at the end of each paragraph.
The exit paragraph should then have one and only one verb (EXIT). In other
words something like this:

PERFORM A THRU A-EXIT.
PERFORM B THRU B-EXIT.
A.
PERFORM C THRU C-EXIT.
IF SOME-CONDITION
GO TO A-EXIT.
DISPLAY 'NO-EXIT'.
A-EXIT.
EXIT.
B.
....
B-EXIT.
EXIT.
C.
....
C-EXIT.

As Christine correctly pointed out, this was used as a relatively safe way
for some lazy programmers to use 'GO TO' verb. At least safer than this:

PERFORM A.
PERFORM B.
A.
PERFORM C.
IF SOME-CONDITION
GO TO B.
DISPLAY 'NO EXIT'.
B.
....
C.
....
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-06T15:49:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p4@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p4@usenetarchives.gap>`

```
Martyn, the exact effect of perform in all cases is specified by the
standard and is totally portable. It is true that if programs use
(disirable) limitations on perform, it is possible to use simplified
implementation schemes, but any standard COBOL compiler MUST properly
implement the general case.

So portability is a thin argument against this horrible standard (there
are plenty of solid arguments!)
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-01-09T05:51:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p6@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p4@usenetarchives.gap> <gap-ad2cc15b21-p6@usenetarchives.gap>`

```
de··.@cs.··u.edu (Robert Dewar) wrote:
› 
› Martyn, the exact effect of perform in all cases is specified by the
…[7 more quoted lines elided]…
› 

Robert, its the COBOL standard that imposes the restriction: "Thus, an active
PERFORM statement, whose execution point begins within the range of another
active PERFORM statement, must not allow control to pass to the exit of the
other active PERFORM statement; furthermore, two or more such active PERFORM
statements must not have a common exit."

Hows a poor proggy to best avoid this, especially when changing a 'legacy'
app? Well, I suggest outlawing PERFORM THRU is a good start.

Yup, there are plenty of solid arguments that presumably fall on deaf
ears in Christines shop, but enhancing conformity to the standard and
hence portability of COBOL apps seems pretty solid to me.
```

#### ↳ Re: I Need Professional Help!

- **From:** "ro..." <ua-author-10922535@usenetarchives.gap>
- **Date:** 1995-01-06T09:56:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p8@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
In article <3ehu1i$r.··.@pan··x.com>,
Christine Tiplady wrote:
› I have no
› need of EXITs, nor of PERFORMing THRU, which is always a bad idea. Cobol
› is a structured language. I see no need to turn it into Assembler.
›
Some of the COBOL programming conventions are a carry over from the
old key-punch days such as putting gaps in data structures (e.g. 1 5 10
15 instead of 1 2 3 4). Another symptom of the perform thru disease
is the numbering of paragraphs instead of putting paragraph names
in alphabetic order.

My suggestion is to use callable subroutines as much as is reasonable.
You will be able to reuse more of your code and by separately testing
your subroutines will be able to improve the quality of your programs.

Ron
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-06T17:42:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p8@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap>`

```
In <3ejlmg$6.··.@daf··c.edu> ro··.@sun··c.edu (Ron Peterson) writes:
› 15 instead of 1 2 3 4). Another symptom of the perform thru disease
› is the numbering of paragraphs instead of putting paragraph names
› in alphabetic order.

Huh? Put paragraph names in alphabetical order regardless of flow
order? With all due respect, sir, are you out of your mind!?

Or do you mean prefixing meaningful paragraph names with letters rather
than numbers? Why the hack is that better? I prefer numbers. A nice
4-digit number gives you lots of room.
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-06T20:08:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p8@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap>`

```
On 6 Jan 1995 14:56:15 GMT, Ron Peterson (ro··.@sun··c.edu) wrote:
› In article <3ehu1i$r.··.@pan··x.com>,
› Christine Tiplady  wrote:
…[8 more quoted lines elided]…
› in alphabetic order.
 
› Why???  What's wrong with prefixing paragraph names with numbers?
 
› My suggestion is to use callable subroutines as much as is reasonable.
› You will be able to reuse more of your code and by separately testing
› your subroutines will be able to improve the quality of your programs.

It may also have an interesting side-effect of degrading performance.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-07T09:50:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p10@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap>`

```
"It [using CALL] maye have the .. side effect of degrading performance"

If it does, then find another compiler. There is no excuse whatsoeever for
subprogram calls in COBOL to be any less efficient than calls in any
other language. Actually if you compare a call to a parameterless program
with a perform, then generally the call can be much MORE efficient if the
compiler is handling the general case of PERFORM. Most compilers have
options to treat perform efficiently assuming it is used in a reasonable
way, but this should only even the playing ground and result in equivalent
code for a call and perform.

There is a tradition in COBOL of writing giant programs and avoiding the
use of CALL, you even find experienced COBOL programmers today who don't
know that COBOL has, and has had for a LONG time, a perfectly usable,
perfectly general mechanism for calling procedures with parameters.

It is quite true that, following this tradition, some COBOL vendors have
provided incredibly horrible inefficient implementations of CALL (for
example, by not special casing the case of static linking which is possible
when a literal is used for the program name), but it is time to stop putting
up with such rubbish from COBOL compilers.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-07T22:09:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p11@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap>`

```
On 7 Jan 1995 09:50:48 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› "It [using CALL] maye have the .. side effect of degrading performance"
 
› If it does, then find another compiler.

Are you out of your mind??? Most of us who work in large shops, don't have
a choice of compiler. These are standardized long before silly little
rules about coding PERFORMs.

› There is no excuse whatsoeever for
› subprogram calls in COBOL to be any less efficient than  calls in any
…[5 more quoted lines elided]…
› code for a call and perform.

Actually, I have done this sort of comparison last year. This was done on
an MVS machine with OS/VS COBOL, COBOL II, and COBOL/370. In all three
cases performance was better when using PERFORMs over creating a
subroutine. When linking dynamically, the difference was even bigger.
BTW, COBOL/370 showed most dramatic difference, since its optimizer inlined
the PERFORMed code. Also, calling nested program reduced the performance
penalty drastically.

› There is a tradition in COBOL of writing giant programs and avoiding the
› use of CALL, you even find experienced COBOL programmers today who don't
› know that COBOL has, and has had for a LONG time, a perfectly usable,
› perfectly general mechanism for calling procedures with parameters.

I am not arguing for bloated programs or against subroutines, but it's
insane to create (and maintain) a separate program when a single paragraph
will do.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-08T00:07:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p12@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap>`

```
"I am not arguing for bloated programs or against subroutines, but it's
insane to create (and maintain) a separate program when a single paragraph
will do."

well of course I am assuming the use of nested programs, this is after
all 1995, the COBOL standard is now ten years old! So of course I am
not thinking in terms of creating "a separate program".
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 6)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-08T13:43:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p13@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap> <gap-ad2cc15b21-p13@usenetarchives.gap>`

```
On 8 Jan 1995 00:07:32 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› "I am not arguing for bloated programs or against subroutines, but it's
› insane to create (and maintain) a separate program when a single paragraph
› will do."
 
› well of course I am assuming the use of nested programs, this is after
› all 1995, the COBOL standard is now ten years old! So of course I am
› not thinking in terms of creating "a separate program".

Nested programs are fine, but they don't solve one of the maintenance
problems: huge (10,000-20,000 line) program files. Also, unfortunately too
many COBOL programmers are unclear on the concept of this and other parts
of the 85 standard. I recently wrote a 100 line EVALUATE statement (doing
it with IF...ELSE would have several times more), and then had to spend an
hour explaining it to a coworker who had never seen an EVALUATE before.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 7)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-09T22:24:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p14@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap> <gap-ad2cc15b21-p13@usenetarchives.gap> <gap-ad2cc15b21-p14@usenetarchives.gap>`

```
On Mon, 9 Jan 1995 20:47:21 GMT, John Watkins (jwa··.@cix··o.uk) wrote:
›› of the 85 standard.  I recently wrote a 100 line EVALUATE statement (doing 
›› it with IF...ELSE would have several times more), and then had to spend an 
›› hour explaining it to a coworker who had never seen an EVALUATE before.
 
› Wouldn't a database solution have been easier?

I am confused. What are you talking about? What "database solution"?
What I had was a truth table. I fail to see what databases have to do with
it.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-01-08T18:59:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p12@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap>`

```
jts··.@pri··t.com (Joseph I. Tsatskin) wrote:

› Actually, I have done this sort of comparison last year.  This was done on 
› an MVS machine with OS/VS COBOL, COBOL II, and COBOL/370.  In all three
…[4 more quoted lines elided]…
› penalty drastically.

This is true and for good reason. At a GUIDE talk a number of years
ago, Ellen MacPherson of COBOL development gave "What Makes COBOL Run"
and a number of reprise/enhanced versions.

The key difference between a PERFORM (or CALL of a nested program)
and an external CALL is that the external CALL can't be sure of the
environment it is transfering into. In the case of COBOL, there is
a significant run-time environment created to support the execution.
This means that an external call goes through a longer path length,
because it needs to check for/create that environment.

Remember: COBOL doesn't have to call COBOL... there are other
languages and they can ALL be used from COBOL. But up until the
(relatively recent) LE/370 & COBOL/370, each had their own unique
run time.

FWIW and from memory, the path length of an OS/VS call was about
100-150 instructions, and a VS COBOL II call was 600. There have
been improvements... but the 4x penalty hit some users pretty hard
when moving to the new compiler.

-----Burton
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 6)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-08T23:21:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p16@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap> <gap-ad2cc15b21-p16@usenetarchives.gap>`

```
600 instructions for a COBOL call is absurdly long, and actually 150
instructions is absurd for any other call, but then the calling sequence
on the IBM mainframes has always been an appalling mess!
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 7)_

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-01-09T07:29:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p17@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p11@usenetarchives.gap> <gap-ad2cc15b21-p12@usenetarchives.gap> <gap-ad2cc15b21-p16@usenetarchives.gap> <gap-ad2cc15b21-p17@usenetarchives.gap>`

```
de··.@cs.··u.edu (Robert Dewar) wrote:

› 600 instructions for a COBOL call is absurdly long, and actually 150
› instructions is absurd for any other call, but then the calling sequence
› on the IBM mainframes has always been an appalling mess!

It is and it isn't... how much setup is there in that C++ compiler +
UNIX environment??? Especially if you do an equal comparison. Unlike
'modern' machines, the 360/370/390 series architecture doesn't have
'support' for process initialization and environment setup like some
other architectures do. So if you count the work done by the OS to
support the call, what's your path length in another environment?
Especially if you don't use CISC instructions like ENTER/LEAVE to do
the work...

-----Burton
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

- **From:** "ro..." <ua-author-10957933@usenetarchives.gap>
- **Date:** 1995-01-09T01:10:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p10@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap>`

```
In article <3ekphp$k.··.@new··t.com>,
Joseph I. Tsatskin wrote:
› Why??? What's wrong with prefixing paragraph names with numbers?
›
Paragraph numbers are not necessary, require extra keying, and can
not be easily remembered.

Regarding Christine's comment on paragraph order is that it is easier
to find a paragraph in the source if the paragraphs are in alphabetical
order. (The only reason for using a number prefix). If a program is
well structured there shouldn't be any drop thru's to the next paragraph.

› It (callable subroutines) may also have an interesting side-effect
› of degrading performance.

Callable subroutines have a minimal performance impact, but have
the advantage of modular developement, resulting in higher quality
programs.

Ron
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-09T02:25:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap>`

```
On 9 Jan 1995 06:10:54 GMT, Ron Peterson (ro··.@sun··c.edu) wrote:
› In article <3ekphp$k.··.@new··t.com>,
› Joseph I. Tsatskin  wrote:
…[3 more quoted lines elided]…
› not be easily remembered.
 
› Do you have trouble remembering 3-digit numbers?
 
› Regarding Christine's comment on paragraph order is that it is easier
› to find a paragraph in the source if the paragraphs are in alphabetical
› order. (The only reason for using a number prefix). If a program is 
› well structured there shouldn't be any drop thru's to the next paragraph.

So you suggest that I code my paragraphs in alphabetic sequence and then
scroll all over the program listing trying to find the next line of code.
That's a pretty bizarre concept.

›› It (callable subroutines) may also have an interesting side-effect 
›› of degrading performance.
 
› Callable subroutines have a minimal performance impact, but have
› the advantage of modular developement, resulting in higher quality
› programs.

When I did some measurements last year, I found that there was a
significant performance penalty when using external subroutines.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-09T09:20:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p20@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p20@usenetarchives.gap>`

```
Joseph asks if people have trouble remembering three digit numbers? Most
certainly the answer is yes. If a large COBOL program has hundreds of
paragraphs with reasonable names, there is no conceivable way that anyone
could remember the associated numbers.

Of course it should never be necessary, the editor or other tool should
supply these numbers (the idea that a programmer would have to look them
up and type them in is truly appalling). On the other hand, with any kind
of decent tools, these paragraph numbers are redundant junk in any case.

THe real objection to paragraph numbers for me is that they are cluttering
junk which intefere with the readability, and thus maintainability, of the
program.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 6)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-09T22:43:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p21@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p20@usenetarchives.gap> <gap-ad2cc15b21-p21@usenetarchives.gap>`

```
On 9 Jan 1995 09:20:14 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› THe real objection to paragraph numbers for me is that they are cluttering
› junk which intefere with the readability, and thus maintainability, of the
› program.

Actually, if properly used, paragraph numbering can enhance readability.
While it's stupid to simply sequentially number paragraphs, the paragraph
numbers can be used to document the hierarchical structure of the program.
Thus you could know that 275-xxxx paragraph is performed from 270-xxxx
paragraph; 320-xxxx is performed from 300-xxxx; and so on.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "ro..." <ua-author-10957933@usenetarchives.gap>
- **Date:** 1995-01-10T10:29:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p20@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p20@usenetarchives.gap>`

```
In article <3eqocp$j.··.@new··t.com>,
666-Joseph I. Tsatskin wrote:
› Do you have trouble remembering 3-digit numbers?
› 
› Yes, I do. How many 3 digit numbers can most people remember?
 
› So you suggest that I code my paragraphs in alphabetic sequence and then 
› scroll all over the program listing trying to find the next line of code. 
› That's a pretty bizarre concept.
› 
Actually, I expect you to look through your deck of punched cards. If
you number your paragraphs, I would hope that they are already in
sequence.

›
› When I did some measurements last year, I found that there was a
› significant performance penalty when using external subroutines.
I don't know how much of a performance penalty you found. It
still is more important that your program works correctly.

Ron
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 6)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-10T12:35:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p23@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p20@usenetarchives.gap> <gap-ad2cc15b21-p23@usenetarchives.gap>`

```
On 10 Jan 1995 15:29:48 GMT, Ron Peterson (ro··.@sun··c.edu) wrote:
› In article <3eqocp$j.··.@new··t.com>,
› 666-Joseph I. Tsatskin  wrote:
›› Do you have trouble remembering 3-digit numbers?
› Yes, I do. How many 3 digit numbers can most people remember?

If you use similar numbering schemes in all your programs, you really don't
need to remember that many.

›› So you suggest that I code my paragraphs in alphabetic sequence and then 
›› scroll all over the program listing trying to find the next line of code. 
…[3 more quoted lines elided]…
› sequence.
 
› Buy a clue.
 
›› When I did some measurements last year, I found that there was a 
›› significant performance penalty when using external subroutines.
› I don't know how much of a performance penalty you found. It
› still is more important that your program works correctly.

Are you one of those people that find that getting a proram to work
correctly is so difficult, that taking performance into consideration is to
much of a mental strain?

This reminds me of one co-worker who produced a program that needed to run
weekly, but took 10-12 days (that's right, days) to complete. This of
course caused all kinds of havoc especially since the data center insisted
on weekly IPL and the program didn't have any sort of checkpointing in it.
But his program did exactly what was required, it just didn't do it within
the available resources. But as you say: "program works correctly".
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 7)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-12T02:34:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p24@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p20@usenetarchives.gap> <gap-ad2cc15b21-p23@usenetarchives.gap> <gap-ad2cc15b21-p24@usenetarchives.gap>`

```
On 11 Jan 1995 22:31:41 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› "But his program did exactly what was required, it just didn't do it within
› the available resources.  But as you say: "program works correctly"."
 
› Usually the specifications of a program include required performance
› characteristics, so I don't think anyone would say that a program was
› correct if it failed to meet deadline requirements. Of course one normally
› thinks of deadlines as something much shorter than a week, but the principle
› is the same.
 
› Of course a program must meet performance specs, but still, a lot of people
› worrying about a few microseconds extra overhead on CALL's compared to
…[3 more quoted lines elided]…
› language.

In this particular example, the problem extended well beyond using CALL
vs. PERFORM. It was actually a multitude of bad design decisions.

› Actually I must say that the quality of code from IBM mainframe compilers
› is pretty appalling, and it is interesting to note that at least one company
› that provided a much superior IBM mainframe product was quite unsuccessful.
› It seems that most COBOL programmers were more interested in perceived
› reliability than saving some CPU time!

Your derisive statement doesn't explain the success of STROBE and other
performance monitoring products.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-01-09T07:36:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap>`

```
ro··.@sun··c.edu (Ron Peterson) wrote:

› Callable subroutines have a minimal performance impact, but have
› the advantage of modular developement, resulting in higher quality
› programs.

Beg to differ -- modules, by themselves -- don't improve quality.
If you hack the monster into chunks and connect them with calls and
since you don't know which chunk uses what information you pass it
all... then you get what you deserve...

How about:

"Well designed modules result in higher quality programs"?

Seriously, it's not COBOL that makes for bad programs, it is bad
programming that makes for bad programs. You can creat good, well-
structured, maintainable programs that are efficient and clearly
understandable in COBOL. And you can create a monster in C. It is
not the tool itself that is inherently good or bad!

-----Burton
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-09T08:04:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap>`

```
In <3eqk1e$j.··.@daf··c.edu> ro··.@sun··c.edu (Ron Peterson) writes:
› Paragraph numbers are not necessary, require extra keying, and can
› not be easily remembered.
 
› All true.
 
› Regarding Christine's comment on paragraph order is that it is easier
› to find a paragraph in the source if the paragraphs are in alphabetical
› order. (The only reason for using a number prefix). If a program is 
› well structured there shouldn't be any drop thru's to the next paragraph.

But what's the greater evil, all those complaints about numbering, or
having your paragraphs scattered all over alphabetically without regard
to flow order? I'd find myself trying to name them so that common
functions were close together anyway, & would probably end up using some
kind of "prefix" anyway. I dunno. My complaints are not about fears of
"dropping thru" or anything about faulty execution; of course that won't
be affected if you are structured. It's about maintenance. Even iwth
the full 30 bytes afforded me to make a meaningful paragraph name, I'm
not going to know everything the paragraph does, & I'm going to have to
find it. I'm going to be jumping all over the place when I try to
understand a program for the first time, & probably again for the second,
third, etc time for a long time. & with mainframe response time, that is
going to be a pain.

But this is probably a matter of simple preference that I shouldn't argue
with. I agree I have trouble remembering my paragraph numbers.

I knew a guy who used to number each variable. Oy gevalt!
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "ro..." <ua-author-10957933@usenetarchives.gap>
- **Date:** 1995-01-10T10:45:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p27@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p27@usenetarchives.gap>`

```
In article <3erc9q$g.··.@pan··x.com>,
Christine Tiplady wrote:
› I'd find myself trying to name them so that common 
› functions were close together anyway, & would probably end up using some 
…[5 more quoted lines elided]…
› 
I think using a prefix is a good idea. And for small programs, it
probably isn't helpful to sort paragraphs. But, for large programs,
it becomes difficult to put paragraphs in execution order.

If a program is large, it is nice to have some supporting documentation
(please forgive my use of the "d" word). Although the program flow
chart is now frowned upon, a program structure chart can be quite
helpful in describing the logical flow of a program.

Ron
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-09T09:17:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap>`

```
Numbering paragraphs so they can be found seems an archaic hold over from
batch processing days when programs were generally read on paper. I realize
that there may still be some development environments where this is the
case, but surely this is an obsolete requirement for most devleopment
environments, where an editor can immediately find any routine you need
to look at.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-01-09T22:35:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p29@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p29@usenetarchives.gap>`

```
On 9 Jan 1995 09:17:02 -0500, Robert Dewar (de··.@cs.··u.edu) wrote:
› Numbering paragraphs so they can be found seems an archaic hold over from
› batch processing days when programs were generally read on paper. I realize
…[3 more quoted lines elided]…
› to look at.

Actually, I still look at the compiler listing of the program quiet
frequently, since it allows you to see a great deal more of the program at
once. Numbering paragraphs came in real handy when OS/VS COBOL produced
either sorted or unsorted cross reference listing (depending on the
selected option) and some poor souls didn't understand why sorted listing
was preferable. Of course, the current compilers (COBOL II and COBOL/370)
can only produce sorted cross reference, so this is no longer an issue.
But this is a fairly benign sort of habit, so I really don't care.
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 4)_

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1995-01-10T10:09:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p19@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap>`

```
ro··.@sun··c.edu (Ron Peterson) wrote:
› 
› In article <3ekphp$k.··.@new··t.com>,
…[10 more quoted lines elided]…
› 

I've gotta disagree with the notion that it's easier to locate para-
graphs by sorting them alphabetically, and with the corresponding
observation that this is "the only reason for using a number prefix."
In the shop where I used to work, we used the Murach/Noll structure
chart notation (well, I used Yourdon/Constantine, but everyone else
used Murach/Noll) for design, and we would assign number prefixes
to the paragraph modules on the chart -- numbers that indicated
the overall branching (initialize, process, report, etc.), and level
depth. Therefore, we knew that any paragraph having a 1xxxx- prefix
was related to initialization, any paragraph having a 3xxxx- prefix
was related to main processing, 5xxxx was reporting, etc. Also, the
prefix indicated whether it was a high-level paragraph (12000, 30000,
etc.) or a low-level (32150, 12210, 55215, etc). Frankly, how can
one track control flow when the paragraphs are (arbitrarily) sorted
alphabetically?

Curtis Bass
```

###### ↳ ↳ ↳ Re: I Need Professional Help!

_(reply depth: 5)_

- **From:** "ro..." <ua-author-10957933@usenetarchives.gap>
- **Date:** 1995-01-11T01:08:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p31@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p8@usenetarchives.gap> <gap-ad2cc15b21-p10@usenetarchives.gap> <gap-ad2cc15b21-p19@usenetarchives.gap> <gap-ad2cc15b21-p31@usenetarchives.gap>`

```
In article <3eu7uq$r.··.@atl··b.edu>,
Curtis Bass wrote:
› In the shop where I used to work, we used the Murach/Noll structure
› chart notation (well, I used Yourdon/Constantine, but everyone else
…[3 more quoted lines elided]…
› depth.

The use of structure chart coding is something that I haven't used, so
I can't comment on its effectiveness. But I think that those who are
using a simple paragraph numbering scheme haven't given enough thought
to how to design programs and make the program readable.

Ron
```

#### ↳ Re: I Need Professional Help!

- **From:** "curtis bass" <ua-author-9633319@usenetarchives.gap>
- **Date:** 1995-01-06T11:46:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p33@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
tip··.@pa··x.com (Christine Tiplady) wrote:
› 
› My stupid shop has this stupid standard [I'm in a foul mood]: all 
…[11 more quoted lines elided]…
› 

Ahhh, yes, I recall being forced to use this wretched "standard" in
the first shop I worked in. I tried to tell them that PERFORM THRU
was PATENTLY UNSTRUCTURED (it implies multiple entry/exit points),
and actively ENCOURAGED bad programming style (laziness & GOTO's),
but hey, standards are standards, and I was just a newbie, so what
did I know about "real life?". Anyway, I DID capitulate after much
hand waving & brow-beating, but the whole time I was there, I wrote
EVERY exit paragraph as ONE line:

10000-EXIT. EXIT.

This made it a little easier to bear, in that I was only writing ONE
line of superfluous tripe per paragraph, and not two:

10000-EXIT.
EXIT.

This makes my stomach turn to this day, because it looks as if part
of my paragraph's code has leaked out into the inter-paragraph abyss.
Why anyone would prefer this abomination is beyond my (above-average)
imagination.
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-06T17:44:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p33@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p33@usenetarchives.gap>`

```
In <3ejs5e$a.··.@atl··b.edu> Curtis Bass writes:
› hand waving & brow-beating, but the whole time I was there, I wrote
› EVERY exit paragraph as ONE line:
 
› 10000-EXIT.  EXIT.
 
› This made it a little easier to bear, in that I was only writing ONE
› line of superfluous tripe per paragraph, and not two:
 
› 10000-EXIT.
›     EXIT.

Thanx for this input, but somehow I don't think it's going to make me
feel better.

› This makes my stomach turn to this day, because it looks as if part
› of my paragraph's code has leaked out into the inter-paragraph abyss.
› Why anyone would prefer this abomination is beyond my (above-average)
› imagination.

Again, thank you, thank you all for your support.

:==8)
```

#### ↳ Re: I Need Professional Help!

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-06T17:38:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p35@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
In mal··.@wim··y.com (Murray Alexander) writes:

› Christine, you have my heart-felt sympathy and complete support. My shop does 
› permit GOTOs, but we certainly don't *encourage* the damned things. I used 
…[5 more quoted lines elided]…
› of experience has only reinforced this principle.

I am MASSIVELY grateful for your sympathy, & your cheer brought a tear to
my eye; but pray tell, if you do not GO TO, what does SECTION buy you?

I asked someone at work today, someone I THOUGHT was a fine upstanding
structured programmer, his opinion of these matters; & he was puzzled
about my own preferred style of using paragraphs, all paragraphs, &
nothing but paragraphs. It took a second for it to dawn on him that
Cobol considers the next paragraph name to signal the end of the previous
paragraph, & that EXITs, SECTIONs, etc are not necessary. How could
people not know this!? There is NO NEED for any of the following, which
could all be abolished from the Cobol language tomorrow as far as I care:
SECTION. THRU. EXIT. All they do is give you more room for error.
Misplaced or misspelled or forgotten exit paragraphs.

› Do you have the option of digging your heels in? How about tucking all your
› source code away in a private directory?

On this particular project, I'll obey my director. Everything else stays
the same, though. The powerful folx don't usually poke into source code.

› Let's hear it for Christine, folks! All together now...
 
› She's right, right, right!
› Let's fight, fight, fight!
› GO TO! PERFORM THRU!
› A blight, blight, blight!

You guys are the best.

:==8)
```

##### ↳ ↳ Re: I Need Professional Help!

- **From:** "bbr..." <ua-author-9420032@usenetarchives.gap>
- **Date:** 1995-01-07T15:27:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad2cc15b21-p35@usenetarchives.gap>`
- **References:** `<3ehu1i$rlr@panix3.panix.com> <gap-ad2cc15b21-p35@usenetarchives.gap>`

```
Christine Tiplady (tip··.@pa··x.com) wrote:
: [...] There is NO NEED for any of the following, which
: could all be abolished from the Cobol language tomorrow as far as I care:
: SECTION. THRU. EXIT. All they do is give you more room for error.

Right you are. The ONLY unit of modularity for a COBOL program should be
the paragraph. (Separately-compiled subroutines excepted, of course.)
These days you don't even need SECTIONs with the SORT verb. (Huzzah!)

I recommend trying to get the standard changed; don't give up... you're right!
```

#### ↳ Re: I Need Professional Help!

- **From:** "mud..." <ua-author-17032606@usenetarchives.gap>
- **Date:** 1995-01-06T22:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p37@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
Christine Tiplady (tip··.@pa··x.com) wrote:
: violated this horrible standard. I do not GO TO. I am allergic to it,
: it's against my religion, & I just wasn't raised that way. So I have no
: need of EXITs, nor of PERFORMing THRU, which is always a bad idea. Cobol
: is a structured language. i

COBOL *CAN* be a structured language or not. Funny thing, in my last job
I was required to use GO TO. IT was hard at first but I got used to it.
(IT was my first programming job and I had been taught to not use GO
TO). Now I have a new job where GO TO is absolutely forbidden. I have
adapted. I would suggest you read the book "Code Complete" by Steve
someboday ro other McConnell or something like that. It is a Microsoft
Press book. He makes some great points about GO TO. Using a GO TO
doesn't necessarily make something unstructured. He also says people
really misunderstand what structured program really is. I'd quote, but
the book is at the office.

If it kills you that much to use GO TO, I would suggest looking for a new
job.

Oh yeah, as an aside, when my previous boss found out one of his
ex-employees had used structured coding he was quite irate about it. HE
found it really hard to follow. :)
```

#### ↳ Re: I Need Professional Help!

- **From:** "dlpa..." <ua-author-6589473@usenetarchives.gap>
- **Date:** 1995-01-07T20:45:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad2cc15b21-p38@usenetarchives.gap>`
- **In-Reply-To:** `<3ehu1i$rlr@panix3.panix.com>`
- **References:** `<3ehu1i$rlr@panix3.panix.com>`

```
In article <3ehu1i$r.··.@pan··x.com> tip··.@pa··x.com (Christine Tiplady) writes:
› My stupid shop has this stupid standard [I'm in a foul mood]: all 
› paragraphs must be PERFORMed THRU an EXIT paragraph, to give lazy 
…[22 more quoted lines elided]…
› make it through this?  O unhappy day.

YOU DON'T HAVE TO SUFFER LIKE THIS!!! Take off that hair shirt, tell them
where to stick it, look for a nice refrigerator shipping carton, and set up
housekeeping there. Or you could do what I do - exude angst all the way to
the bank.
Dave Parker/PRI, Inc. - 303 N. Jeffreys - Pleasant Hill, MO 64080-1331 USA
dlp··.@dlp··0.com / dlp··.@dlp··t.net / dlp··.@tyr··l.net
dpa··.@big··i.edu        /         (816) 540-5167/5218 voice/fax
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
