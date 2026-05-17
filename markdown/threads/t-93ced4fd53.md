[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Object Oriented?

_6 messages · 5 participants · 1997-02 → 1997-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Object Oriented?

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-02-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc17fe$556a67a0$2710edcc@743441631>`

```

This is more a curiousity type question. In IBM's COBOL, it is now possible
to create object-oriented programs. Other than some sort of "framework"
(maybe like a CICS interface), can anybody give me some idea why I would
use this facility in my own programs? IOW - why would I create my own class
hierarchy from scratch? Just wondering.
John McKown
```

#### ↳ Re: Object Oriented?

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1997-02-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-93ced4fd53-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc17fe$556a67a0$2710edcc@743441631>`
- **References:** `<01bc17fe$556a67a0$2710edcc@743441631>`

```

In <01bc17fe$556a67a0$2710edcc@743441631>, "John McKown" writes:
› This is more a curiousity type question. In IBM's COBOL, it is now possible
› to create object-oriented programs. Other than some sort of "framework"
…[3 more quoted lines elided]…
› John McKown

So you can codify your critical business logic. If you were doing
banking work, you might have a collection of "loan-payoff" objects, and
a hierarchy of "convert-account-to-preferred-customer",
"calculate-holiday-interest", "apply-current-interest",
"get-date-range", etc.

Yes, these are just subroutines but it's so much more high-tech to call
them objects.

In theory, once you build up this universe, you've got something easy to
maintain... ...at least that's what the academics, who've never seen
how large production systems can get, think.

Cory Hamasaki "I have JCL Objects and IEBGENER Objects too."
```

##### ↳ ↳ Re: Object Oriented?

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-93ced4fd53-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-93ced4fd53-p2@usenetarchives.gap>`
- **References:** `<01bc17fe$556a67a0$2710edcc@743441631> <gap-93ced4fd53-p2@usenetarchives.gap>`

```

kiy··.@i··.net wrote:
› 
› John McKown writes:
…[14 more quoted lines elided]…
› them objects.
 
› Interesting definition of object.
 
› In theory, once you build up this universe, you've got something easy to
› maintain... ...at least that's what the academics, who've never seen
› how large production systems can get, think.

I think you are being very unfair to those who have contributed greatly to the
advance of computer science. Are you suggesting that organizations such as
AT&T do not have large production systems?

Del.
```

###### ↳ ↳ ↳ Re: Object Oriented?

- **From:** "luis a. espinal" <ua-author-12404825@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-93ced4fd53-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-93ced4fd53-p3@usenetarchives.gap>`
- **References:** `<01bc17fe$556a67a0$2710edcc@743441631> <gap-93ced4fd53-p2@usenetarchives.gap> <gap-93ced4fd53-p3@usenetarchives.gap>`

```

›› In theory, once you build up this universe, you've got something easy to
›› maintain... ...at least that's what the academics, who've never seen
…[6 more quoted lines elided]…
› Del.
I agree with you, Del. I've seen far too often that kind of remark about
academics. It is so biased, iliterate, insulting and unfair. I've known
academics who HAVE work in large scale systems either in D.o.D. or in
commercial apps. in a variety of languages from Cobol, Fortran down to
C/C++, and they have been able to deploy object-orientation
successfully. Even myself have found oop an usefull tool in my job. Of
course, if someone does not know how to use oop concepts, she would
end-up having a mess. It's posible to have object-oriented spagetti
code, but that is not object-orientation or academics fault but the
implementor. In any case, if someone says that academics do not have
working experience outside the classroom is because he/she has never had
the privilege of meeting one. And this kind of remarks are always found
when new ideas are introduced ( oop is not a new idea, though. ) Remeber
when procedural programming and relational-databases were introduced?
Interesting in theory, yet academics then did not have an idea of
complicated large-scales apps could be. It is like the 70's; it always
comes back.
Luis++ = ( les··.@sol··u.edu XOR 
	   lui··.@arm··e.com );
What does not kill us makes us stronger
...abort, retry, ignore ?
```

###### ↳ ↳ ↳ Re: Object Oriented?

_(reply depth: 4)_

- **From:** "cad..." <ua-author-17071389@usenetarchives.gap>
- **Date:** 1997-03-03T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-93ced4fd53-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-93ced4fd53-p4@usenetarchives.gap>`
- **References:** `<01bc17fe$556a67a0$2710edcc@743441631> <gap-93ced4fd53-p2@usenetarchives.gap> <gap-93ced4fd53-p3@usenetarchives.gap> <gap-93ced4fd53-p4@usenetarchives.gap>`

```

On Fri, 28 Feb 1997 05:48:24 -0500, Luis A. Espinal wrote:
››› maintain... ...at least that's what the academics, who've never seen
››› how large production systems can get, think.
›› I think you are being very unfair to those who have contributed greatly to the
› academics. It is so biased, iliterate, insulting and unfair. I've known
› academics who HAVE work in large scale systems either in D.o.D. or in

It would be more accurate just to state that shortsighted, poor design can
be practiced anywhere. Business tends to suffer financially, so it's more
of a priority than in academia but I'm sure the readers of this group are
familar with business systems that have been implemented poorly and
academic/experimental systems that have been done beautifully. This isn't
caused by a language, platform or environment but by the programmer(s).
Some languages do give you more rope but there's usually a very good reason
for it.
```

#### ↳ Re: Object Oriented?

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-11T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-93ced4fd53-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bc17fe$556a67a0$2710edcc@743441631>`
- **References:** `<01bc17fe$556a67a0$2710edcc@743441631>`

```

John McKown wrote:
› 
› This is more a curiousity type question. In IBM's COBOL, it is now possible
…[3 more quoted lines elided]…
› hierarchy from scratch? Just wondering.

Yours is an excellent question. Why indeed would you go to the expense of creating
a set of classes in OOCOBOL? You wouldn't if you were not convinced there was some
benefit in the end. More to the point, OOCOBOL is only worth using if it reduces
the cost of producing software. Does it? Maybe.

I say, "maybe", because a methodology or programming language is only a tool for
programmers. Neither will turn poor programmers into good programmers. Good
programmers follow good programming practices no matter which methodology they are
using or which language they implement their designs in. However, I have found
that OO languages make following good practices easier.

So what are the [claimed] benefits of OO programming (NB: Doug Miller posted an
interesting paper sometime back, debating the validity of these claims).


CODE REUSE:

This is the claim I see more than any other: OO programming promotes reuse. This
is easy to believe because it seems obvious. If, for example, I have an object
that encapsulates a "customer" on my system, I could reuse it in several places.
Maybe. What most people do not realize is that reuse requires work; it doesn't
come for free.

Additionally, do I need to use OO programming to achieve reuse? Definitely not.
One method of reuse is to simply copy existing code into a new program and modify
it. Crude? Yes, but it still qualifies as reuse. COBOL programmers can also
employ copy books to share code amoung different programs, maintaining a single
source base. My company ("http://www.netron.com") specializes in COBOL reuse using
frame technology. This is a more sophisticated form of reuse and yields
substantial benefits ("http://www.netron.com/about.htm#study"). My point, however,
is that there are many ways to achieve reuse. But, no matter how you achieve it,
the more you can reuse existing code, the more you lower the cost of producing
software.


DESIGN REUSE:

This is another level of reuse and, IMHO, the most important type of reuse. Design
level reuse comes from the reuse of frameworks and patterns, and may or may not
include code reuse. I think many programmers use design level reuse without even
knowing it; however, what they are reusing is their own past designs - solutions to
previous, similar problems. Formal design reuse promotes the use of the best
designs. In addition, it should be easier for others to understand the program if
the solutions to various problems are the same as those found in other programs.

Currently, the best known examples of design level reuse are the popular Windows
frameworks: OWL and MFC (both are C++ frameworks). Anyone who remembers writing
Windows programs in C knows that these frameworks make it alot easier to create
Windows applications. I am not aware of any frameworks for OOCOBOL, but Netron
does supply frameworks for COBOL.


MORE MAINTAINABLE:

OO programs are more maintainable than their 3GL equivalents. Again, maybe. They
should; this is one of the benefits that I believe should be realized, but it comes
down to this: the language doesn't make the programmers any better. A poor
programmer can do just as poor a job design and implementing an OO program as a 3GL
program. Plus, in my experience, good programmers often do not improve their
product when moving from 3GL to OO programming. The latter is not because there is
no room for improvement, there always is.

The good programmer continues with good programming practices in the OO world,
lowering coupling, increasing cohesion. The new language has natural support for
this, meaning the good programmer finds it easier to do these things (after the
initial cost of learning the new technology). So, the OO program is not
necessarily more maintainable than the 3GL equivalent.

However, there are software engineering principles that apply to OO design that
should make the resulting software easier to maintain. IMHO, the most important of
these is the open/close principle (Bertrand Meyer). Essentially, it means that the
program is open to new features but existing code is closed (i.e., the new features
do not affect existing code). This is not an easy principle to follow and requires
careful design.

Open/close is not limited to traditionaly OO languages either. Again, I would
point to Netron's frame technology as an example.


These are my top three benefits of OO programming. There are others, and I'm sure
some other programmers would have a different top three. But, I hope I've made two
points clear:

(1) OO programming guarantees nothing; you still need exceptional people to achieve
exceptional results.
(2) it is not the only way to achieve the claimed benefits


Del.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
