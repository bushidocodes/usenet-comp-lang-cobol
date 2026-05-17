[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Standard - Qualification of names

_11 messages · 6 participants · 1995-06_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL Standard - Qualification of names

- **From:** "mor..." <ua-author-4892761@usenetarchives.gap>
- **Date:** 1995-06-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`

```
The following has been sent as a comment to Ann Wallace - Convenor
ISO/IES JTC 1/Sc22/WG4 and Don Schricker, Chairman, TC X3J4 U.S. TAG
to SC22/WG4. This is being posted to comp.lang.cobol and
bit.listserv.ibm-main. Especially in the latter group, if you have
people who work with COBOL pass it on to them. If either you or they
wish to concur or disagree please email Ann··.@vne··m.com and
d.··.@mfl··o.uk by June 30, 1995. They prefer getting the first round
of comments on the proposed 1997 standard by email. Also comment on
this and things that are in the proposed standard such as bit
manipulation and objected oriented code both to them and to
comp.lang.cobol.

There is a major oversight in the proposed 1997 standard. There is no
proposal to simplify the specification of qualified data-names. Reuse of data
descriptions within a program is a powerful tool and concept. It allows a
description to be coded once and then used everywhere the data area is needed.
The concept makes programs more reliable and reduces maintenance costs. In
1963 (or earlier), the designers of COBOL invented the idea of qualified data
names that allowed reuse of data descriptions within a program. They then
made it awkward to use. I have seen little use of it qualification in the
two organizations I worked for and in the packaged software that I dealt with.
I suspect the same is true of most COBOL using organizations. Identifer-1 OF
identifier-2 OF identifier-n is awkward. It is not normal English
construction because we normally say the dog's bone not the bone of the dog.
It takes four character positions instead of the one used by most computer
languages that have identifier-n.indentifier-2.identifier-1 as the means of
implementing qualification. I know that I have had complaints about the
readability of COBOL programs that I have written that use qualification.
With only 61 characters in the COBOL line, this is a noticeable limitation
because it increases the likelihood of a single statement requiring more than
one line. The proposal for a variable length line probably will not help that
much. Even today most computer screens display comfortably only about 80
characters. I use 132 wide for Word-Perfect but my wife prefers the larger
letters of 80 wide on a 14 inch screen. The time is long overdue for COBOL to
allow qualification in the same manner as SQL, C, Natural from Software AG,
DYL280 from Sterling Software, High-Level Assembler from IBM (370 class
systems) and other languages have implemented it. Many COBOL bugs would never
have existed if qualification had been implemented so that it was simple to
use and perceived as easy to read.

The period should be the connective character used to join the file-
name/group-name(s) to the field-name/condition-name. This is to cut down on
the confusion for programmers who use multiple languages. Implementing this
change to COBOL will bring more benefit to more organizations than
improvements to the report writer or introduction of the validation facility.
Our legacy of 30+ years of lacking a means of qualification viewed as simple
and straight forward means that the COPY library-name REPLACING LEADING
==string-1== BY ==string-2== is still very much needed. However there are
many record descriptions used today that do not lend themselves to this
facility. This comment is being sent to various Internet news groups in hopes
of generating discussion and hopefully support for this change.

Clark Morris CFM Technical Programming Services - cmo··.@fox··n.ca
on assignment in New Brunswick, Canada - mor··.@nbn··b.ca
```

#### ↳ Re: COBOL Standard - Qualification of names

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1995-06-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`

```
In article mrw@trophy "Mike Wilson" writes:
› I would..like..something along the lines of the Pascal 'with'...
›     with customer-record
…[5 more quoted lines elided]…
›     end-with.

Hmmm. It's a good idea heading in the right direction, but it
only allows for one qualification. In your example you need two.
How about using
(1) a local macro facility, and
(2) "=>" instead of "." as a qualification pointer
example:
WITH (aa AS customer-record) AND (bb AS print-record)
MOVE aa=>account-number TO bb=>account-number
...
END-WITH.

Richard Ross-Langley  +44(0)1727 852801
Mine of Information Ltd,  PO BOX 1000,  St Albans AL3 5NY,  GB
=== Independent Computer Consultancy * Established in 1977 ===
```

##### ↳ ↳ Re: COBOL Standard - Qualification of names

- **From:** "charles godwin" <ua-author-2829225@usenetarchives.gap>
- **Date:** 1995-06-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p2@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p2@usenetarchives.gap>`

```
R Ross-Langley wrote:
› In article  mrw@trophy "Mike Wilson" writes:
› 
…[11 more quoted lines elided]…
› -

This is going to far!

I oppose the with syntax as it is a partial band-aid and does nothing for
the situation of referencing several items on two idential structures.
The second solution is just a scheme to reduce key-strokes. It could be
achieved today by using REPLACE


REPLACE AA by customer-record bb bt print-record
MOVE account-number of aa TO account-number of bb
REPLACE OFF


Charles Godwin

(613)761-1430 Work
(613)761-1422 Fax
```

#### ↳ Re: COBOL Standard - Qualification of names

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-22T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`

```
In article <3sd4g4$c.··.@dar··b.ca> , mor··.@nbn··b.ca writes:
›
› lots of stuff about using periods for qualification
›
This has been discussed many times for many years. However, because the
period has a significant meaning in COBOL and does not in other languages
it
has never been accepted. In fact, some compilers do not enforce the rule
that a period must be followed by a space and let one sentence run into
another. This could cause problems. Also note that the other languages
require that you qualify every level. COBOL does not. You only need to
qualify enough to make the item unique. Following other language rules
(as
was suggested), you actually end up with names much longer than you would
using the current COBOL qualification rules.

By the way, I see qualification used all over the place. I suppose this
is
because I have seen thousands of COBOL programs that are written by
thousands of programmers from a large number of different installations.
The complaints about COBOL qualification are few. In my 24 years of
being
involved with COBOL standardization I have only heard a handful of people
complain.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

##### ↳ ↳ Re: COBOL Standard - Qualification of names

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-06-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p4@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap>`

```
Don Nelson (nel··.@tan··m.com) wrote:
: In article <3sd4g4$c.··.@dar··b.ca> , mor··.@nbn··b.ca writes:
: >
: > lots of stuff about using periods for qualification
: >
: This has been discussed many times for many years. However, because the
: period has a significant meaning in COBOL and does not in other languages
: it
: has never been accepted. In fact, some compilers do not enforce the rule
: that a period must be followed by a space and let one sentence run into
: another. This could cause problems. Also note that the other languages
: require that you qualify every level. COBOL does not. You only need to
: qualify enough to make the item unique. Following other language rules
: (as
: was suggested), you actually end up with names much longer than you would
: using the current COBOL qualification rules.

: By the way, I see qualification used all over the place. I suppose this
: is
: because I have seen thousands of COBOL programs that are written by
: thousands of programmers from a large number of different installations.
: The complaints about COBOL qualification are few. In my 24 years of
: being
: involved with COBOL standardization I have only heard a handful of people
: complain.

: Don Nelson
: COBOL Development, Tandem Computers, Inc.

I respect your opinion and your years of hard work in the COBOL standard
area, but this seems a bit like "throwing the baby out with the bathwater".
If '.' is a bad symbol then another can be used (':' perhaps, I believe
this is only used for ref mod). However, your point is well taken as
to the current nature of COBOL qualification rules.

A way to create and use a type (as in PASCAL's TYPE or C's typedef) along
with a shorthand for name qualification would be a greate asset in COBOL.
The question isn't if it's needed, it's when will it become part of the
language. I'd rather see free form source and dynamic arrays than the
above ... on the other had I'd rather see the above than the new
invoke verb (however I'm not daff and realize that invoke is far too
chic not to be added ... don't get me wrong I think OO is good and that
invoke is well thought out, but adding it before a simple type definition
system doesn't seem overly wise.). In any case a way to define and use
types as well as a shorthand would be very useful and not too difficult
to add to existing compilers (as these could be implemented now via a
rather simple preprocessor which as we all know is an ugly-evil-non-standard
method :-) ) Generally, people don't complain about something they've
never had ... unless they think their boss wants it ;-)

Ok, Ok, I heard you saying "... but you can do the same thing with the
'COPY ... REPLACING ...' and the '... OF ...'. True, but COPY ...
REPLACING ... leads to it's own form of errors and is less clear than
the above. It also leads to a record being defined several times
instead of once with several occurances.

There is also something wonderfully that might be added beyond the
97 standard ... :-) ... having the record type embedded into the
database it describes ... yep, lots of problems to over come on
this ... but it would be nice.
```

###### ↳ ↳ ↳ Re: COBOL Standard - Qualification of names

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-25T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p5@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap> <gap-d1eed5ac9c-p5@usenetarchives.gap>`

```
In article <3sicuc$k.··.@new··s.net> Greg Granger,
ggr··.@cyb··s.net writes:
› Don Nelson (nel··.@tan··m.com) wrote:
› : In article <3sd4g4$c.··.@dar··b.ca> , mor··.@nbn··b.ca
› writes:
› :
 
› Some stuff I said
 
› I respect your opinion and your years of hard work in the COBOL standard
› area, but this seems a bit like "throwing the baby out with the
…[3 more quoted lines elided]…
› to the current nature of COBOL qualification rules.

When we suggested using something other than the period to the ones who
wanted this, they said the period or nothing.

› A way to create and use a type (as in PASCAL's TYPE or C's typedef) along
› with a shorthand for name qualification would be a greate asset in COBOL.

A type definition something like you describe has been added (it was
approved at the last meeting).

› The question isn't if it's needed, it's when will it become part of the 
› language.  I'd rather see free form source and dynamic arrays than the
› above 
 
› Both have been added.
 
› ... on the other had I'd rather see the above than the new 
› invoke verb (however I'm not daff and realize that invoke is far too
› chic not to be added ... don't get me wrong I think OO is good and that
› invoke is well thought out, but adding it before a simple type definition
› system doesn't seem overly wise.).

It wasn't. It was added more or less in parallel. Also, OO is lots more
than INVOKE. The proposal was around 70 pages long.

› In any case a way to define and use 
› types as well as a shorthand would be very useful and not too difficult
…[16 more quoted lines elided]…
› 

I don't understand this. And, nobody has proposed anything that sounds
like it.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: COBOL Standard - Qualification of names

_(reply depth: 4)_

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-06-25T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p6@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap> <gap-d1eed5ac9c-p5@usenetarchives.gap> <gap-d1eed5ac9c-p6@usenetarchives.gap>`

```
Don Nelson (nel··.@tan··m.com) wrote:
: In article <3sicuc$k.··.@new··s.net> Greg Granger,
: ggr··.@cyb··s.net writes:
: >Don Nelson (nel··.@tan··m.com) wrote:
: >: In article <3sd4g4$c.··.@dar··b.ca> , mor··.@nbn··b.ca
:...
: >If '.' is a bad symbol then another can be used (':' perhaps, I believe
: >this is only used for ref mod). However, your point is well taken as
: >to the current nature of COBOL qualification rules.

: When we suggested using something other than the period to the ones who
: wanted this, they said the period or nothing.
Hmm, that's odd, I don't see anything that special about '.' ... maybe
someone should have whacked 'em on the head once or twice ;-)


: >A way to create and use a type (as in PASCAL's TYPE or C's typedef) along
: >with a shorthand for name qualification would be a greate asset in COBOL.

: A type definition something like you describe has been added (it was
: approved at the last meeting).
Wonderful, this will be quite useful. (sorry I didn't realize it was
already being considered)
:...
: Don Nelson
: COBOL Development, Tandem Computers, Inc.
: Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
: Project Editor, 1997 ISO COBOL Standard


As always thanks for the info.
```

###### ↳ ↳ ↳ Re: COBOL Standard - Qualification of names

_(reply depth: 5)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-25T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p7@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap> <gap-d1eed5ac9c-p5@usenetarchives.gap> <gap-d1eed5ac9c-p6@usenetarchives.gap> <gap-d1eed5ac9c-p7@usenetarchives.gap>`

```
In article <3sn6sp$s.··.@pin··g.be> Gordon Degrandis,
Gor··.@pi··g.be writes:
› 
› My suggestion for the seperator for COBOL qualification is the use of
…[7 more quoted lines elided]…
› 
We have had numerous suggestions to make the underscore work exactly
like the hyphen for names. Since people are used to using hyphens in
names in other languages, it probably would be even more confusing.
Like "group_item" would seem just like "group-item".

If we were going to have some special character, we would have to stick
to the ISO character set, so real oddball characters like apl uses are
out. As I recall, the exclamation point (!), the pound sign (#), the
percent (%), the question mark (?), the commercial at (@), the
circumflex accent (^), the grave accent (`), the tilde (~), vertical
line (|), reverse solidus (\), and the square and curly brackets ([]
{}) are not yet used for anything. Of course, if you branch into the
extended supplements you have lots of neat stuff, but that requires
16-bit characters and the like. At one time or another some of these
have been suggested, but there never was any agreement.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: COBOL Standard - Qualification of names

_(reply depth: 6)_

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1995-06-26T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p8@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap> <gap-d1eed5ac9c-p5@usenetarchives.gap> <gap-d1eed5ac9c-p6@usenetarchives.gap> <gap-d1eed5ac9c-p7@usenetarchives.gap> <gap-d1eed5ac9c-p8@usenetarchives.gap>`

```
In article <3snerh$b.··.@gaz··m.com>
nel··.@tan··m.com "Don Nelson" writes:
› We have had numerous suggestions to make the underscore work exactly 
› like the hyphen for names.  Since people are used to using hyphens in 
› names in other languages, it probably would  be even more confusing.   
 
› Agreed.  (And extra periods seem a bit dangerous in COBOL).
 
› If we were going to have some special character, we would have
› to stick to the ISO character set... Of course, if you branch
› into the extended supplements you have lots of neat stuff...

What about character pairs? (Cf ":=" in Algol, ">=" in COBOL).

How about "->" as a structure member pointer, as used in C, eg:
ADD INPUT-REC -> BALANCE TO WS-INVOICE-TOTAL
which points from the 01 record level to the item contained in it?

Richard Ross-Langley
```

###### ↳ ↳ ↳ Re: COBOL Standard - Qualification of names

_(reply depth: 7)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-26T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d1eed5ac9c-p9@usenetarchives.gap>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca> <gap-d1eed5ac9c-p4@usenetarchives.gap> <gap-d1eed5ac9c-p5@usenetarchives.gap> <gap-d1eed5ac9c-p6@usenetarchives.gap> <gap-d1eed5ac9c-p7@usenetarchives.gap> <gap-d1eed5ac9c-p8@usenetarchives.gap> <gap-d1eed5ac9c-p9@usenetarchives.gap>`

```
In article <804··.@min··o.uk> R Ross-Langley,
r.··.@min··o.uk writes:
› In article <3snerh$b.··.@gaz··m.com>
›   nel··.@tan··m.com "Don Nelson" writes:
…[4 more quoted lines elided]…
› Agreed.  (And extra periods seem a bit dangerous in COBOL).

Periods as they are now are dangerous (ask any maintenance
programmer who has goofed and put one in an unterminated IF).

› 
›› If we were going to have some special character, we would have
…[8 more quoted lines elided]…
› 
Not a bad idea. We are using pairs in the new standard for other
things. For example, *> is used to signal an in-line comment. We
are using !! for in-line invocation. Of course, the purists will
say that you are using four characters (two spaces and the two
symbols) where one would do.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

#### ↳ Re: COBOL Standard - Qualification of names

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-06-25T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1eed5ac9c-p11@usenetarchives.gap>`
- **In-Reply-To:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`
- **References:** `<3sd4g4$cni@darwin.nbnet.nb.ca>`

```
cou··.@c··.com (Jitze Couperus) wrote:

› In article , mrw@trophy (Mike Wilson) wrote:
 
›› I would also like to see something along the lines of the Pascal
›› 'with'. For those who don't know Pascal (and that includes me), I think
…[6 more quoted lines elided]…
› with matching datanames is going to save coding effort.
 
› Jitze Couperus

I do not agree.
We have written an application recently that uses over 1000 program
modules that are eventually linked together to make a server program.
These program modules use the data definitions that are stored in a data
dictionary system. We use the MOVE CORR statement to move data from the
database to the module parameters. The original data names came from the
database description and ALL the working-storage data names use the same
data names as the database. So in our case the MOVE CORR works, since
the developer IS NOT responsible for defining the modules working
storage. In our development, we have developed 4 new application systems
using our data dictionary and we have never had any problems with data
definition, maintenance and the use of the COBOL MOVE CORR statement.

My suggestion for the seperator for COBOL qualification is the use of
the underscore "_". This character has no use in COBOL and can be used
quite eaisly to represent the qualification character. So your move
would look like:

MOVE group_item1 TO group1_item2.

Looks good for me.



------------------------------------------------------
Internet: Gor··.@pi··g.be
Compuserve: 100273,1562
Currently on location in Belgium!
Snappy quote for this week:
A gleekzorp without a tornpee is like a quop without a fertsneet (sort of).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
