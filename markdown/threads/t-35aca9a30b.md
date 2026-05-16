[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Defensive programming

_18 messages · 12 participants · 1998-08 → 1998-09_

---

### Re: Defensive programming

- **From:** Lookin'@You.2 (WDS)
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35e5e47e.5284114@news1.frb.gov>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net>`

```
On Tue, 25 Aug 1998 15:12:15 GMT, stevewie@apk.net (SkippyPB) wrote:

>On Wed, 19 Aug 1998 21:45:25 +0100, "Simon Ward"
><tubby@toasts.force9.co.uk> enlightened us:
>
>>
>>I would be interested in what people think of the below idea.

[snip description of calling out-of-date routine]
>>
>>My idea is to use check field(s) in the linkage section which will
>>automatically detect (most of the time) whether past variable are out of
>>sync.
[...]
>>Now if program B called subroutine C, subroutine C would set a bad return
>>code and processing could be stopped indicating that there is a problem.
…[3 more quoted lines elided]…
>to compile and link all 3 programs when the copybook changed.

This idea could be extended to include a version number in your
linkage data and verify its consistency between routines.  Compare the
version number passed in the linkage data with one stored within each
routine (possibly from another copybook).

Of course, version management software could be used as well.
```

#### ↳ COMP-3, S9(8)

- **From:** Wei Lu <luw@me.udel.edu>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov>`

```
Could you please tell me that ?

PACK1        PIC            9(6)  COMP-3.
SIGN1         PIC           S9(6).
 A                PIC             9(6) .

Can I
1)   MOVE   PACK1    TO    A.
2)   MOVE       A         TO    PACK1.
3)   MOVE   SIGN1     TO     A.
4)    MOVE     A          TO     SIGN1.


What is the size of S9(8)  ?
What is the size of S9(8) COMP-3 ?

THANKS.
```

##### ↳ ↳ Re: COMP-3, S9(8)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s569k$f95$1@news.igs.net>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu>`

```

Wei Lu wrote in message ...
>Could you please tell me that ?
>
…[8 more quoted lines elided]…
>4)    MOVE     A          TO     SIGN1.

Yes to all.

>
>What is the size of S9(8)  ?
>What is the size of S9(8) COMP-3 ?


Both  sizes are platform dependant.  S9(8) will usually be 8 bytes,
but can be forced to nine by using a sign separate declaration. On
the odd platform, it will default to 9.  Comp-3 (I may be wrong here
because I do not usually use comp-3) is usually a word, so
in 32 bit platform, it will be four bytes, two's comp.

>
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

- **From:** Ibis redibis numquam peribis <rrg10300@dasb.fhda.edu>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.OSF.3.95q.980827202623.4498A-100000@octane.dasb.fhda.edu>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <6s569k$f95$1@news.igs.net>`

```


On Thu, 27 Aug 1998, Donald Tees wrote:

=> 
=> Wei Lu wrote in message ...
=> >Could you please tell me that ?
=> >
=> >PACK1        PIC            9(6)  COMP-3.
=> >SIGN1         PIC           S9(6).
=> > A                PIC             9(6) .
=> >
=> >Can I
=> >1)   MOVE   PACK1    TO    A.
=> >2)   MOVE       A         TO    PACK1.
=> >3)   MOVE   SIGN1     TO     A.
=> >4)    MOVE     A          TO     SIGN1.
=> 
=> Yes to all.
=> 
=> >
=> >What is the size of S9(8)  ?
=> >What is the size of S9(8) COMP-3 ?
=> 
=> 
=> Both  sizes are platform dependant.  S9(8) will usually be 8 bytes,
=> but can be forced to nine by using a sign separate declaration. On
=> the odd platform, it will default to 9.  Comp-3 (I may be wrong here
=> because I do not usually use comp-3) is usually a word, so
=> in 32 bit platform, it will be four bytes, two's comp.
=> 
=> 
=> 
On a dEC Alpha  S9(n) COMP-3  is allocated (n +1)/2 bytes, rounded UP, and
is Packed Decimal (of course, n <= 18). So, S9(8) COMP-3 is allocated 5
bytes in the alien dEC netherworld.
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35e7085e.0@news1.ibm.net>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <6s569k$f95$1@news.igs.net>`

```

Donald Tees wrote in message <6s569k$f95$1@news.igs.net>...
>
>Wei Lu wrote in message ...
…[23 more quoted lines elided]…
>in 32 bit platform, it will be four bytes, two's comp.


comp-3 is also platform dependent.
On IBM systems (and systems that emulate these) it
is 5 bytes (one half byte for each digit plus a half byte for the sign).
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NYIF1.3224$sG2.3107700@news3.mia.bellsouth.net>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <6s569k$f95$1@news.igs.net> <35e7085e.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
>
>comp-3 is also platform dependent.
>On IBM systems (and systems that emulate these) it
>is 5 bytes (one half byte for each digit plus a half byte for the sign).


Yes, and PIC 9(8) COMP-3 takes the same amount of space, because of a moronic
decision (by Amdahl?) to always allocate space for the sign, whether it is
wanted or not.  One's mind is boggled by the sheer number of wasted bytes
that decision has caused.
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298240.72395.29442@kcbbs.gen.nz>`
- **References:** `<NYIF1.3224$sG2.3107700@news3.mia.bellsouth.net>`

```
In message <<NYIF1.3224$sG2.3107700@news3.mia.bellsouth.net>> "Judson McClendon" <judmc123@bellsouth.net> writes:
> >
> >comp-3 is also platform dependent.
…[7 more quoted lines elided]…
> that decision has caused.

It may have wasted a few nybbles, but it peobably saved a few
bays full of electronics.

Put another way, to have instructions that operated on signed
or unsigned packed decimal would have required a bit somewhere
to indicate that it had the sign position or not.  This
either required a flag on the field (which took the same
space as the sign itself) or took a position in the
instruction - in ever instruction that worked on packed.

Having the flag in the field neither saves nor wastes space
which is thus indifferent as to whether it is signed or not.
Having the flag in the instruction set 'wastes' a bit in
every instruction.

The total number of wasted bits is either the even digit
unsigned packed values in memory (x4) or the number of
instructions in memory (all else being equal).
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_38G1.3571$_B3.4008867@news2.mia.bellsouth.net>`
- **References:** `<NYIF1.3224$sG2.3107700@news3.mia.bellsouth.net> <3298240.72395.29442@kcbbs.gen.nz>`

```
Richard Plinston wrote:
>Judson McClendon writes:
>> >
…[26 more quoted lines elided]…
>instructions in memory (all else being equal).


The instruction format already embodies the field type, or you
would have no way to handle packed BCD, signed and unsigned binary,
and signed and unsigned display numeric.  It would at most take only
one extra bit in the instruction, and that assumes the instruction
format already fully utilizes all the bits in the instruction.  Since
other architectures handle unsigned BCD quite easily, it is obvious
that it is no big deal to do so.
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298242.27509.4373@kcbbs.gen.nz>`
- **References:** `<_38G1.3571$_B3.4008867@news2.mia.bellsouth.net>`

```
In message <<_38G1.3571$_B3.4008867@news2.mia.bellsouth.net>> "Judson McClendon" <judmc123@bellsouth.net> writes:

> >The total number of wasted bits is either the even digit
> >unsigned packed values in memory (x4) or the number of
…[6 more quoted lines elided]…
> one extra bit in the instruction, and that assumes the instruction

So a 33 bit word ?

> format already fully utilizes all the bits in the instruction.  Since
> other architectures handle unsigned BCD quite easily, it is obvious
> that it is no big deal to do so.

Other architectures don't have the same instruction format
and layout (by definition).  Given that the BCD instructions
must have some refernce already to the number of bytes
involved, whereas the binary and floating only require a
single/double flag and a signed/unsigned flag, then the
number of bits required may already fill the 32 bit word.

'stealing' a bit from one of the fields will impose its
own constraints elsewhere, one that 'other architectures'
may lead to other wastages in other formats.

If you actually want to make a point then please do so by
indicating your own redesign of the instruction set to
show exactly where your bit will come from and also 
indicate the disadvantages that this redesign will
create so that a balanced view can be appreciated.
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 8)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EB0D31.B651C570@IMN.nl>`
- **References:** `<_38G1.3571$_B3.4008867@news2.mia.bellsouth.net> <3298242.27509.4373@kcbbs.gen.nz>`

```
Richard, Judson,

There is no bit needed at all to distinguish between short or lon, fixed or float, signed or unsigned or whatever
distinct type you may think of ...

The compiler knows the type from its definition. This definition is programmer-made by using the correct keywords in
the data declarations: float long fixed, comp-2 etc. etc. (keywords in C / C++ / COBOL / PL/1 / Pascal etc) or
(specific for COBOL and look-alikes) the picture symbols. The that compiler just generates the correct machine
instructions (m/i). This means that those m/i's do NOT look after the type, they are made for just one type. Except
... no even NOT conversion m/i's: even those are predefines to convert from GIVEN type x to type y and do not test if
var1 is indeed type x etc.

The machines that I know that are able to do mathematic with signed and unsigned packed (I mean REALY unsigned in
internal storage, not with a fake absolute sign like IBM) all had machine instructions for both types OR had
conversion instructions.

The COBOL Frog
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 9)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298243.25745.12538@kcbbs.gen.nz>`
- **References:** `<35EB0D31.B651C570@IMN.nl>`

```
In message <<35EB0D31.B651C570@IMN.nl>> "COBOL Frog  writes:
> 
> There is no bit needed at all to distinguish between short or lon, fixed or float, signed or unsigned or whatever
…[11 more quoted lines elided]…
> conversion instructions.

Silly boy, of course there is a need for 'a bit needed to
distinquish between short/long, ...'  The bits that are
needed, and do exist, are embedded in the instruction set
of the processor.  When the compiler outputs the object
code it is choosing the instructions appropriate for
the types: these instructions are appropriate because
they have the bit settings for the type and size of the
data.

If you analyse most CPU instruct sets you may notice
that many arithmetic instructions are just sets of
bits to work one way or another, single or double
word, signed or unsigned.
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 10)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EBB083.312211CE@IMN.nl>`
- **References:** `<35EB0D31.B651C570@IMN.nl> <3298243.25745.12538@kcbbs.gen.nz>`

```
Richard Plinston wrote:

> In message <<35EB0D31.B651C570@IMN.nl>> "COBOL Frog  writes:
> >
…[3 more quoted lines elided]…
> > The compiler knows the type from its definition.

8<

> Silly boy, of course there is a need for 'a bit needed to
> distinquish between short/long, ...'  The bits that are
> needed, and do exist, are embedded in the instruction set
> of the processor.

I just thought you were talking about extra bits in the data fields / operands. Now I understand you meant the bits in the
operation code.

>  When the compiler outputs the object
> code it is choosing the instructions appropriate for
> the types: these instructions are appropriate because
> they have the bit settings for the type and size of the
> data.

They need not to contain the size of the data. This size could be in the opcode and would need just one bit for simple
choices like short/long and signed/unsigned. But there are many m/i sets in the real world where the length is an operand
and not in the opcode. especially for string handling m/i's

>  If you analyse most CPU instruct sets you may notice
> that many arithmetic instructions are just sets of
> bits to work one way or another, single or double
> word, signed or unsigned.

May be so. I believe you. This is about the op.code of course

And BTW, I am not entirely silly.

The COBOL Frog
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

- **From:** bruce.chris@hyder.com
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s5kga$f0s$1@nnrp1.dejanews.com>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <6s569k$f95$1@news.igs.net>`

```
In article <6s569k$f95$1@news.igs.net>,
  "Donald Tees" <donald@willmack.com> wrote:
>
> Wei Lu wrote in message ...
…[23 more quoted lines elided]…
>

On an IBM mainframe (32 bit) a COMP-3 variable	is generally known as packed
decimal and is stored with each digit in the picture taking half a byte (a
nibble) and the sign taking half a byte. So in the example given the S9(8)
COMP-3 would be (according the above formula) four and half bytes - which is
rounded to five bytes. Hence its alsways a good idea to declare your COMP-3
variables with an odd number of 9s.

Internally it would be stored as 01,23,45,67,8S where S is C (+) D(-) F
(unsigned). Other values are permitted as the sign to but these are most
commonly seen. (Comma between each byte to illustrate!)

The digits are directly readable in a dump; there's no need to do any hex-dec
conversion to see what value the variable has.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: COMP-3, S9(8)

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E63459.EF060B28@att.net>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu>`

```
Wei Lu wrote:
> 
(snip)
> 
> What is the size of S9(8)  ?

With any IBM COBOL compiler I've ever seen (going back to D-level COBOL
in DOS) S9(8) will be 8 bytes (I assume the earlier reply was correct
concerning a separate sign).

> What is the size of S9(8) COMP-3 ?

Again, with any IBM COBOL compiler I've ever seen (going back to D-level
COBOL in DOS) S9(8) COMP-3 will be 5 bytes. COMP-3 is packed and a
packed field *always* has an odd number of bytes (in memory, not
according to COBOL), plus the sign. So your example will need 9 digits
plus the sign, divided by 2 to get the length in bytes. This has nothing
to do with words (the earlier reply was probably thinking of COMP, not
COMP-3, or some other platform), your field will be byte aligned,
nothing more.

If you're using a compiler other an IBM one, you need feedback from
someone else.

Bill Lynch
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

- **From:** "Erlend Moen" <emoen@hotmail.com>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s5p07$bug$1@o.online.no>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <35E63459.EF060B28@att.net>`

```
Bill Lynch skrev i meldingen <35E63459.EF060B28@att.net>...

>If you're using a compiler other an IBM one, you need feedback from
>someone else.


This goes for Microsoft/MicroFocus and Acucobol as well.

<-emo->
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 4)_

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E71D94.CEEA307B@IMN.nl>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <35E63459.EF060B28@att.net> <6s5p07$bug$1@o.online.no>`

```
Erlend Moen wrote:

> This goes for Microsoft/MicroFocus and Acucobol as well.

But not for Bull DPS machines.

PIC S9(n) will take (n+1)/2 bytes, rounded up.
So, when n is odd, bytes are fully filled, when n is even, a half byte
is added (at front and kept zero) to make up for whole bytes. So far it
is like IBM harware.

B U T when the picture has NO sign ... things are different:
IBM h/w always stores a sign, thats the "+1" in the above formula. But
Bull h/w/ does not store a sign when not present in the picture. So PIC
9(n) will take n/2 bytes. rounded up.
So when n is EVEN, bytes are fully filled, when n is ODD, a half byte is
added (at front and kept zero) to make up for whole bytes. That is NOT
like IBM harware.

The COBOL Frog
```

###### ↳ ↳ ↳ Re: COMP-3, S9(8)

_(reply depth: 5)_

- **From:** trblshtr@my-dejanews.com
- **Date:** 1998-08-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s7jac$sfg$1@nnrp1.dejanews.com>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu> <35E63459.EF060B28@att.net> <6s5p07$bug$1@o.online.no> <35E71D94.CEEA307B@IMN.nl>`

```
In article <35E71D94.CEEA307B@IMN.nl>,
  "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl> wrote:
> Erlend Moen wrote:
>
…[16 more quoted lines elided]…
>

I believe you will find it is compiler related, not h/w.  Acucobol, if i
recall, provides a COMP-6 usage clause which is, effectively, unsigned
COMP-3. COMP-3 on the other hand either implies, or requires, sign.
```

##### ↳ ↳ Re: COMP-3, S9(8)

- **From:** docdwarf@clark.net ()
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s6cde$6ua$1@callisto.clark.net>`
- **References:** `<6rf6sn$47a@news3.force9.net> <35e2cb3c.5343496@news.apk.net> <35e5e47e.5284114@news1.frb.gov> <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu>`

```
In article <Pine.SOL.3.95.980827222852.23903C-100000@me.udel.edu>,
Wei Lu  <luw@me.udel.edu> wrote:
>Could you please tell me that ?
>
…[12 more quoted lines elided]…
>What is the size of S9(8) COMP-3 ?

Can you do your own homework?

What is the due-date of this assignment?

(I think I called this'un right)

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
