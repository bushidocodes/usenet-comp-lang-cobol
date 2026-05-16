[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS Packed Decimal with no sign nibble?

_49 messages · 15 participants · 2003-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: MVS Packed Decimal with no sign nibble?

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-05T16:43:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031205174458.964$v0@news.newsreader.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[6 more quoted lines elided]…
> point, or external decimal (which was converted to binary for calculations).

Peter, I am looking at a book titled "Logical Programming with System/360"
by Don H. Stabley, copyright 1970, John Wiley publisher. On page 60, is a
paragraph with the heading "2. Packed Decimal Data", and on the opposite
page (61) is a chart showing how various packed decimal values would be
stored, dutifully showing the (IBM required) sign nibble. How can you say
that the System/360 did not require a sign on packed decimal fields? We are
discussing packed decimal fields, no? Any packed decimal field on an IBM
System/360 or descendant requires a sign nibble. That's what I said, and it's
true.

> > Perhaps to sell more memory?
>
> Nope. Not at all. Memory (being hand made) was certainly expensive but one
> of the reasons for implementing packed in the first place was to SAVE
> memory.

Saving memory with packed decimal, yes. Saving memory by adding a
redundant mandatory sign to 'unsigned' fields, no. :-)

Don't reject that idea so casually. When it comes to using every possible
angle to sell more hardware, IBM was second to none in those days. Bill
Gates probably learned much of what he knows about that from watching
IBM. Gates did say he wanted to be "the IBM of software," remember?
```

#### ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2003-12-06T11:41:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com>`

```
On Fri, 5 Dec 2003 16:43:58 -0600, "Judson McClendon"
<judmc@sunvaley0.com> enlightened us:

>"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>>
…[18 more quoted lines elided]…
>

Let's clarify here.  IBM required the sign nibble on a Packed Decimal
field if you wanted to perform arithmetic operations on it or move it
to an unpacked field.  However, you could certainly store packed
decimal numbers on disk or tape without the sign nibble.  I wrote many
an Assembler conversion program for some of the old banking systems
(including IBM's own PAL package) that stored data in this way.  When
converting the data, we had to shift the data a half byte and insert a
sign so that the data could be used in Cobol in a Comp-3 data field.


>> > Perhaps to sell more memory?
>>
…[10 more quoted lines elided]…
>IBM. Gates did say he wanted to be "the IBM of software," remember?

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


Real Tombstone Epitaphs:

In a Thurmont, Maryland, cemetery:
Here lies an Atheist
All dressed up And no place to go.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-07T13:08:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd26fb1_8@news.athenanews.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com>`

```
Thanks Steve.

I read this after I formulated my response to Judson, but it endorses my own
position on this.

I think that because this is a COBOL forum, many people (in particular,
Judson) just aren't aware that Packed can be used in this way.

It is ironic that he has convinced himself  that  the sign is a ploy by IBM
to sell more memory <G>.

Pete.

"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
news:nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com...
> On Fri, 5 Dec 2003 16:43:58 -0600, "Judson McClendon"
> <judmc@sunvaley0.com> enlightened us:
…[7 more quoted lines elided]…
> >> It wasn't. The original System 360, designed by Gene Amdahl, had no
packed
> >> decimal. It was a pure binary machine, intended for (mainly) scientific
> >> applications. It utilised up to 64 bit (doubleword) binary, or floating
> >> point, or external decimal (which was converted to binary for
calculations).
> >
> >Peter, I am looking at a book titled "Logical Programming with
System/360"
> >by Don H. Stabley, copyright 1970, John Wiley publisher. On page 60, is a
> >paragraph with the heading "2. Packed Decimal Data", and on the opposite
> >page (61) is a chart showing how various packed decimal values would be
> >stored, dutifully showing the (IBM required) sign nibble. How can you say
> >that the System/360 did not require a sign on packed decimal fields? We
are
> >discussing packed decimal fields, no? Any packed decimal field on an IBM
> >System/360 or descendant requires a sign nibble. That's what I said, and
it's
> >true.
> >
…[13 more quoted lines elided]…
> >> Nope. Not at all. Memory (being hand made) was certainly expensive but
one
> >> of the reasons for implementing packed in the first place was to SAVE
> >> memory.
…[25 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-07T06:27:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xLzAb.3363$rP6.2479@newsread2.news.pas.earthlink.net>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com> <3fd26fb1_8@news.athenanews.com>`

```
Pete and Steve, (Judson and others)
   I guess I am confused about exactly whether this is an argument about
terminology or history or what.

There SEEMS to be agreement that on S/360 and subsequent IBM "mainframe"
machines, one must have a "valid" sign-nibble in a packed-decimal field in order
to do arithmetic on it.

Furthermore, I think we all agree that all such machines support UNSIGNED
"zoned-decimal" numeric items (that one can do arithmetic on).

The question (seems to me) to come down to whether you can "pack" an unsigned
numeric value into a "valid" packed field that you will NOT be doing arithmetic
on.

Here I think the "terminology" problem arises.  Yes, you certainly can put the
"bit-patterns" representing the digits from 0-9 in each nibble of a field and
that is a "valid" storage of something in S/360 and following.  HOWEVER, in
IBM's terminology this is NOT (and as far as I know, never has been) a "valid
packed field".  For the most current definition, see:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dz9zr002/8.1.2

which is the definition of "Packed Format" and which says (in part),

"  In  the  packed  format, each byte contains two decimal digits (D), except
for the rightmost byte, which contains a sign to the right  of  a  decimal
digit."

which (seems to me) to indicate that if the last nibble isn't a sign, it isn't
in "packed format".

Concerning the "question" of whether you can "pack" data that does NOT include a
sign nibble in the penultimate nibble of a zoned decimal sending item,

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dz9zr002/7.5.98

implies (or I infer) that you may - but are "minimally" supported - as it says,

"The second operand is treated as having the zoned format. The numeric bits of
each byte are treated as a digit. The zone bits are ignored, except the zone
bits in the rightmost byte, which are treated as a sign."

It even addresses what I think started this conversation when it says,

 "3. To remove the zone bits of all bytes of a field, including the rightmost
byte, both operands should be extended on the right with a dummy byte, which
subsequently should be ignored in the result field."

So you probably (and I suspect some mainframe assembler programmers DO) "pack"
fields where the sending field's sign-nibble is not A-F.  As Pete and Steve
indicated, you will be in "trouble" if you then try to use this in arithmetic -
furthermore, you can, however, even use the UNPACK instruction - as
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dz9zr002/7.5.141

says,

 "The sign and digits are not checked for valid codes."

So if your sending field were X"ABCDE1" - when you unpack it you will get (I
think)
    X"FAFBFCFD1E"

which must be useful <G> for something.

For further information on
  "Decimal-Operand Data Exception"
(known and loved by IBM mainframe COBOL programmers as S0C7), see:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dz9zr002/8.2.5

    ***

Does this put us all back talking about the same things????
```

###### ↳ ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-07T11:16:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031207121721.593$2d@news.newsreader.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com> <3fd26fb1_8@news.athenanews.com> <xLzAb.3363$rP6.2479@newsread2.news.pas.earthlink.net>`

```
Bill, thanks for the post. What you say below is precisely as I have known
it to be all along. What I have been trying to say can be expressed succinctly
this way:

"On most non-IBM hardware, you can create a field PIC 9999 (with some
COMP-? usage) that will be stored as packed decimal into two bytes, with
all four half-bytes representing decimal values, and no sign. This field can
then be used in any arithmetic operation as any other numeric field, and it
will always be considered positive for this purpose. IBM mainframe
hardware (System/360 & descendents) does not support this use."

I'm surprised anyone thought I was trying to say that you could not stuff
four decimal digits into two bytes with no sign using assembly language
or even cleverly written COBOL. As an old time assembly programmer
I considered this a no-brainer non-issue. Wow, I must come across as
pretty dumb. :-)
```

###### ↳ ↳ ↳ How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 5)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-12-08T04:28:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031207232844.03883.00000415@mb-m07.aol.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com>`

```
Judson McClendon writes ...

[snip]

>"On most non-IBM hardware, you can create a field PIC 9999 (with some
>COMP-? usage) that will be stored as packed decimal into two bytes, with
…[4 more quoted lines elided]…
>

Just out of curiosity, as a lifelong IBM mainframe bigot, can you tell me how
such numbers convey sign when necessary? It seems they can't. So when you need
a sign, you have to waste a whole byte on it? Is that how they do it on non-IBM
iron?

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-08T06:45:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031208074645.970$P6@news.newsreader.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com>`

```
"S Comstock" <scomstock@aol.com> wrote:
> Judson McClendon writes ...
>
…[11 more quoted lines elided]…
> iron?

Steve, you have it almost reversed. 'Unsigned' numbers have always
been considered positive in mathematics. None of us were ever taught
in math class that we absolutely must write explicit '+' signs by every
single positive number. A computer should consider any numeric field
without an explicit sign as positive, just as we would do if the same
number were written or printed that way. Virtually all non-IBM CPUs
are designed to function this way. AFAIK it is only IBM System/360
and descendents that require a redundant, explicit '+' sign to be present
on unsigned packed BCD fields. All other hardware I know of that does
support packed BCD supports both signed and unsigned formats. If you
do math on the unsigned BCD fields, they are treated as implicitly
positive, in line with ubiquitous mathematical convention, the very same
convention you yourself undoubtedly use in writing numbers. There is
simply no justification for a computer to require an extra 4 bits to be
appended to every single packed BCD number that is either never used
in math to begin with, or those that can never be negative. Even a six
year old school child knows a number without a sign written by it is to
be considered positive. :-)

Did you ever see a problem like this in any textbook?

   +123
   +456
+ +789
--------

I haven't. ;-)
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-08T16:34:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br2974$ke6$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com>`

```

On  8-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Steve, you have it almost reversed. 'Unsigned' numbers have always
> been considered positive in mathematics. None of us were ever taught
…[3 more quoted lines elided]…
> number were written or printed that way.

A non-signed number requires extra processing to check to see if an arithmetic
operation would create a negative - and then must decide what to do about it.
A signed number simply gets processed.

I imagine the sign nibble is in unsigned IBM packed-decimal for hardware
purposes - the microcode is simpler if all packed numbers have their significant
digits the same - then it checks sign and does whatever processing (positive,
negative, or unsigned) warrants.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-08T11:12:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br2ifm$26l4$1@si05.rsvl.unisys.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:br2974$ke6$1@peabody.colorado.edu...

> A non-signed number requires extra processing to check to see if an
arithmetic
> operation would create a negative - and then must decide what to do about
it.
> A signed number simply gets processed.

Why?  Seems to me it's the *sign* that requires the extra processing to
determine whether it's positive or negative; the hardware already knows (or
should know!) that an item *without* a sign is always positive!

> I imagine the sign nibble is in unsigned IBM packed-decimal for hardware
> purposes - the microcode is simpler if all packed numbers have their
significant
> digits the same - then it checks sign and does whatever processing
(positive,
> negative, or unsigned) warrants.

Since when is "It's easier for IBM to write their microcode that way"
sufficient justification for a "everybody knows that all unsigned packed
items have to be signed"?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 9)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-12-08T21:33:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ttj9tvshau1pnupv5glqip5uu56ubbvfh4@4ax.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com>`

```
On Mon, 8 Dec 2003 11:12:53 -0800 "Chuck Stevens" <charles.stevens@unisys.com>
wrote:

:>"Howard Brazee" <howard@brazee.net> wrote in message
:>news:br2974$ke6$1@peabody.colorado.edu...

:>> A non-signed number requires extra processing to check to see if an
:>arithmetic
:>> operation would create a negative - and then must decide what to do about
:>it.
:>> A signed number simply gets processed.

:>Why?  Seems to me it's the *sign* that requires the extra processing to
:>determine whether it's positive or negative; the hardware already knows (or
:>should know!) that an item *without* a sign is always positive!

That either requires:

1. separate machine instructions for signed and unsigned fields  or 

2. checking the number for one of three states: positive, negative and
unsigned - and a greater possibility of error because if a value is expected
to be signed but has garbage it may match the unsigned format.

:>> I imagine the sign nibble is in unsigned IBM packed-decimal for hardware
:>> purposes - the microcode is simpler if all packed numbers have their
:>significant
:>> digits the same - then it checks sign and does whatever processing
:>(positive,
:>> negative, or unsigned) warrants.

:>Since when is "It's easier for IBM to write their microcode that way"
:>sufficient justification for a "everybody knows that all unsigned packed
:>items have to be signed"?

It isn't.

The S/360+ have machine instructions that work directly on packed fields in
memory without requiring adjustment.

The 80286 (and I presume the Pentium(TM?)) process for BCD required machine
instructions for byte by byte processing of BCD fields and adjusting the
results for each byte.

How does the Unisys MCP hardware process packed fields?
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-08T12:45:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br2ntl$2akn$1@si05.rsvl.unisys.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <ttj9tvshau1pnupv5glqip5uu56ubbvfh4@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
news:ttj9tvshau1pnupv5glqip5uu56ubbvfh4@4ax.com...

> That either requires:
>
> 1. separate machine instructions for signed and unsigned fields  or

Depends on what you mean by "machine instructions".  Arithmetic on Unisys
MCP systems is done entirely in binary.   Our experiments with building
decimal-*arithmetic* hardware led us to the conclusion that our efforts in
improving performance were much better expended elsewhere -- with very fast
arithmetic hardware, improving the decimal-to-binary and binary-to-decimal
hardware was both simpler and more effective.   We do have separate machine
instructions for signed and unsigned fields.

> 2. checking the number for one of three states: positive, negative and
> unsigned -

No.   There's a sign in all the formats on which all arithmetic operators
perform; it's up to the conversion operators, coming in and coming out of
the operations, to ensure the validity of the sign.

> How does the Unisys MCP hardware process packed fields?

In various ways.

For arithmetic retrieval, most often it does an ICLD (for left-signed), ICRD
(for right-signed) or ICUD operator against the indexed data descriptor
pointing to the data that's to be converted to internal binary.  For ICLD
and ICRD, the sign position is examined for the presence of @D@ to indicate
a negative result; anything else in the sign indicates positive.

For storing of arithmetic results, ordinarily it converts the internal
binary to an internal packed operand-on-stack format using the BCD operator,
recording the sign in an external register, then transfers that using UPLD,
UPRD or UPUD into the area pointed to by the destination descriptor, the
first two of these setting the sign according to the register, and the third
ignoring it.   The same operators are used for both DISPLAY and PACKED
destinations, the sign position (zone vs. digit) distinction being handled
by the hardware.

For example, given
        01  A-RECORD.
            03  FIELD-1 PIC S9(5) COMP. *> or PACKED-DECIMAL
            03  FIELD-2 PIC 9(3)V99 COMP.
the code generated for
        COMPUTE FIELD-2 = FIELD-1 / 100.
looks like
    LT <hex offset of FIELD-2 = 6>, NAMC (A-record), INDX
    LT <hex offset of FIELD-1 = 0>, NAMC (A-Record), INDX
    LT (digit length of field-1 = 5), ICLD
    BCD (digit length of field-1 = 5)
    LT (digit length of field-2 = 5), UPUD
Note that the compiler recognizes that it doesn't have to do the division.
If you change the formula to
        COMPUTE FIELD-2 = FIELD-1 / 10000.
then a LT (100), IDIV gets added right after the ICLD (truncating the
rightmost two digits of the source).

The need for fast decimal arithmetic does not necessarily imply the need for
fast decimal *arithmetic* hardware.  The engineers seriously considered
providing decimal hardware on the A Series some twenty years ago, and they
concluded that improving the ICxD, BCD and UPxD operators within the
existing stack architecture of the system would do far more toward improving
overall decimal performance than tacking a fast decimal "box" on the side of
that architecture could ever hope to achieve.  I believe history has borne
out that conclusion; we have had no reason to revisit it.

Fast decimal arithmetic hardware is NOT a prerequisite to fast arithmetic on
decimal items.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-09T15:26:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br4pju$68k$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com>`

```

On  8-Dec-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> > A non-signed number requires extra processing to check to see if an
> arithmetic
…[6 more quoted lines elided]…
> should know!) that an item *without* a sign is always positive!

So what is the compiler supposed to do when you subtract a larger number from a
smaller one?   If the smaller number is signed - it subtracts them.  If the
smaller one is unsigned, it does error processing.   It can't treat them the
same.


> > I imagine the sign nibble is in unsigned IBM packed-decimal for hardware
> > purposes - the microcode is simpler if all packed numbers have their
…[7 more quoted lines elided]…
> items have to be signed"?

There is only one reason for packed decimal numbers - it works better in
hardware.   This isn't a business rules issue - it is a hardware issue.  We want
hardware efficiency with fast processing and small size.   The computer
designers pick the best way to do hardware efficiency.   If you don't care about
such, just always use Usage Display.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-09T16:07:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_qmBb.5311$_r6.2943@newsread1.news.pas.earthlink.net>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu>`

```
Howard,
  Re:

"Howard Brazee" <howard@brazee.net> wrote in message
news:br4pju$68k$1@peabody.colorado.edu...
<snip>
> > Why?  Seems to me it's the *sign* that requires the extra processing to
> > determine whether it's positive or negative; the hardware already knows (or
> > should know!) that an item *without* a sign is always positive!
>
> So what is the compiler supposed to do when you subtract a larger number from
a
> smaller one?   If the smaller number is signed - it subtracts them.  If the
> smaller one is unsigned, it does error processing.   It can't treat them the
> same.
>
>

   ***

I don't understand this statement.  Regardless of what happens (on any specific
hardware) with Packed numeric fields, try the following (with Usage Display
data).

    01 NumFields.
            05  Larger-NF         Pic   S999  Value +999.
            05  Smaller-NF       Pic       99   Value 99.
            05 Recv-Signed       Pic   S9999.
            05 Recv-Unsigned   Pic     9999.
               ...
            Subtract Larger-NF from Smaller-NF Giving Recv-Signed
                 On Size Error
                        Display "Will never happen"
             End-Subtract
       *
            Subtract Larger-NF from Smaller-NF Giving Recv-Unsigned
                 On Size Error
                        Display "Will still never happen"
            End-Subtract

  ***

   As both of those subtract's will work (and would ALSO work withOUT any "on
size error" phrase), I don't understand why you think the results would/should
be any different with Packed-Decimal fields (for any or all of the fields).

Note:
  I have raised a question among the J4 and WG4 members as to whether it might
be a "nice" enhancement to provide a (new) non-fatal exception condition when a
negative value is "attempted" to be stored in an unsigned receiving item of an
arithmetic expression.  Currently (and in past Standards) the ON SIZE ERROR only
checks the "absolute value" of the results of arithmetic.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-09T18:28:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br5481$ijc$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <_qmBb.5311$_r6.2943@newsread1.news.pas.earthlink.net>`

```

On  9-Dec-2003, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>    As both of those subtract's will work (and would ALSO work withOUT any "on
> size error" phrase), I don't understand why you think the results would/should
…[9 more quoted lines elided]…
> checks the "absolute value" of the results of arithmetic.

I didn't know that.   Interesting.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-10T13:51:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd66e52_1@news.athenanews.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <_qmBb.5311$_r6.2943@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:_qmBb.5311$_r6.2943@newsread1.news.pas.earthlink.net...
> Howard,
>   Re:
…[4 more quoted lines elided]…
> > > Why?  Seems to me it's the *sign* that requires the extra processing
to
> > > determine whether it's positive or negative; the hardware already
knows (or
> > > should know!) that an item *without* a sign is always positive!
> >
> > So what is the compiler supposed to do when you subtract a larger number
from
> a
> > smaller one?   If the smaller number is signed - it subtracts them.  If
the
> > smaller one is unsigned, it does error processing.   It can't treat them
the
> > same.
> >
…[4 more quoted lines elided]…
> I don't understand this statement.  Regardless of what happens (on any
specific
> hardware) with Packed numeric fields, try the following (with Usage
Display
> data).
>
…[18 more quoted lines elided]…
>    As both of those subtract's will work (and would ALSO work withOUT any
"on
> size error" phrase), I don't understand why you think the results
would/should
> be any different with Packed-Decimal fields (for any or all of the
fields).
>
> Note:
>   I have raised a question among the J4 and WG4 members as to whether it
might
> be a "nice" enhancement to provide a (new) non-fatal exception condition
when a
> negative value is "attempted" to be stored in an unsigned receiving item
of an
> arithmetic expression.  Currently (and in past Standards) the ON SIZE
ERROR only
> checks the "absolute value" of the results of arithmetic.
>

That sounds like good sense to me, Bill.

Shall we look for it this century...<G>?

Pete.

>
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-09T08:29:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br4ta7$r43$1@si05.rsvl.unisys.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message

> So what is the compiler supposed to do when you subtract a larger number
from a
> smaller one?   If the smaller number is signed - it subtracts them.  If
the
> smaller one is unsigned, it does error processing.   It can't treat them
the
> same.

I think you are presuming that all implementations actually do the
arithmetic directly on the decimal data.  The standards only require that
the system "act as if" they had done so.  In our case, the source fields
(signed or unsigned, of whatever usage) are translated to one of two
standard intermediate forms with the proper signs (negative for negative,
positive for unsigned, zero value and positive), and the arithmetic done on
those.  If the destination is unsigned, it is the absolute value of the
result that gets stored.

> There is only one reason for packed decimal numbers - it works better in
> hardware.   This isn't a business rules issue - it is a hardware issue.
We want
> hardware efficiency with fast processing and small size.   The computer
> designers pick the best way to do hardware efficiency.   If you don't care
about
> such, just always use Usage Display.

I don't disagree that on our systems the difference in processor resource
consumption between PACKED-DECIMAL and DISPLAY for numeric items is small.
But "hardware efficiency" is not simply about *processor* resource
consumption, it is also about *storage* resource consumption and
*inter-device communication* resource consumption.   In all implementations
I'm aware of, PACKED-DECIMAL is a compromise between resource consumption
and legibility, and while (as has been discussed recently!) it isn't
*entirely* portable from one implementation to another, the information
stored in this format is almost always *legible* on just about any platform,
even if that legibility requires some adjustments to the data declarations.
As I see it, the ultimate in portability for numeric items is given by
DISPLAY with an explicit separate sign, but such items occupy twice (more or
less) the storage resources as the packed decimal equivalents, and require
twice the resources to be transferred from one place or device to another.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-09T19:10:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br56nn$ir$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com>`

```

On  9-Dec-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> I don't disagree that on our systems the difference in processor resource
> consumption between PACKED-DECIMAL and DISPLAY for numeric items is small.
> But "hardware efficiency" is not simply about *processor* resource
> consumption, it is also about *storage* resource consumption and
> *inter-device communication* resource consumption.

Agreed.

> In all implementations
> I'm aware of, PACKED-DECIMAL is a compromise between resource consumption
…[7 more quoted lines elided]…
> twice the resources to be transferred from one place or device to another.

Agreed again.    Any argument about whether packed decimal should be signed that
says that ignores hardware efficiency though is flawed.   Packed decimal is
about hardware.   Nowadays portability across platforms is more and more
important, making such decisions less important.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-10T14:33:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd67828_5@news.athenanews.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:br56nn$ir$1@peabody.colorado.edu...
<snip>>


>  Any argument about whether packed decimal should be signed that
> says that ignores hardware efficiency though is flawed.   Packed decimal
is
> about hardware.

NO, it ISN'T!!!!

It is about decimal accuracy on a system that was inherently floating point,
and about saving storage that was relatively "priceless" by today's
standards.

Packed decimal was NEVER implemented as hardware on IBM system 360. The
"decimal instruction set" was possible because of Amdahl's innovative
thinking in providing a "soft" set of control logic for his system. It was
an OPTION on early 360s. (If it had been an inherent part of hardware it
would've been much more difficult NOT to offer it...)

I don't know whether S390 implements packed hardware or not, but if it does,
it will be because the format established itself over years and it would
make sense to move it into hardware.

Hardware considerations were NOT a factor in the development of Packed
Decimal; it was purely a MARKETING consideration, to make a system that had
been designed primarily as a scientific computer  into a general purpose
system that could be used for commercial applications. Commerce had
fundamental requirements for decimal accuracy (you don't want paychecks
calculated as $99.999999999999, or have an inventory receipt for 1 item,
added to the one already in stock and see that you now have
1.99999999999999999 of them <G>), and manipulation of large quantities of
data (in fact we called it "Electronic Data Processing" to distinguish it
from Scientific computing...As all forms of storage were expensive, anything
that could halve that requirement was very desirable from a marketing point
of view.).

The commercial success of System 360 was a surprise, even to IBM. Once the
dam broke, everyone scrambled to get on board and say "I knew it all
along...". At that point, no expense was spared to do whatever was necessary
to enhance the further marketing of it. Apparently, Gene Amdahl himself
never actually liked the idea of a decimal instruction set, seeing it as
degrading the purity of his creation. (My source for this is hearsay, from
an IBM marketing man who had had conversations with Amdahl in the early
1960s, so it may not be true, but I believe it to be so.)

The sad thing (in the big picture) is that while S360 grabbed the limelight
with its "new" packed decimal commercial capabilities, other systems
(arguably, better...) from other manufacturers, were pushed onto the back
foot.

For example, I can remember IBM sales people claiming that "Thanks to our
soft control logic, implemented in Read Only Storage (ROS), our machine can
do in ONE instruction what our competitors take many to do".  Much was made
of the fact that each mylar card in ROS was like a miniature program,
thereby increasing the power of each "instruction".

Yet I also remember writing a benchmark for ICL 1900 and IBM 360 where the
1900 creamed it, despite taking more instructions...

The fact was, that by the time the 360 had gone stepping through ROS to
determine what to do, the 1900 had already  completed, using its very fast
Load and Store type instruction set. (On thinking about it, I guess it was a
bit like RISC vs CISC).

BOTTOM LINE:  Packed Decimal was a marketing requirement, not driven by
hardware at all.

Pete. ("I was that soldier...").
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-10T15:47:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br7f5v$e1$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com>`

```

On  9-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> >  Any argument about whether packed decimal should be signed that
> > says that ignores hardware efficiency though is flawed.   Packed decimal
…[5 more quoted lines elided]…
> It is about decimal accuracy on a system that was inherently floating point,

That's hardware.

> and about saving storage that was relatively "priceless" by today's
> standards.

That's hardware.


> BOTTOM LINE:  Packed Decimal was a marketing requirement, not driven by
> hardware at all.

Well, everything's marketing.   But packed-decimal is about the costs and
benefits of the way the hardware is designed and costed.    It has nothing to do
with the business logic being processed.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 14)_

- **From:** "Francis ANDRE" <francis.andre@easynet.fr>
- **Date:** 2003-12-18T01:43:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe0f81a$0$400$afc38c87@news.easynet.fr>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com> <br7f5v$e1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> a �crit dans le message de news:
br7f5v$e1$1@peabody.colorado.edu...
> Well, everything's marketing.   But packed-decimal is about the costs and
> benefits of the way the hardware is designed and costed.    It has nothing
to do
> with the business logic being processed.

Wrong......As explained very clearly by Peter, Packed Decimal data type it
is about DECIMAL computation and as a consequence of BUSINESS computation
(yes, the $1.999.999.999.999 error!!) packed decimal is about doing
computation on BIG NUMBERs that cannot be represented within the
"traditional 4 bytes integer" and WITH (*more or less*) the equivalent
efficienty in time and space.....

DECIMAL computation has its own set of rules for ROUNDING, TRUNCATING, ERROR
REPORTING that have nothing to do with hardware. Moreover, these rules of
truncation/rounding and division by zero are quite different from those of
FIXED POINT BINARY and thoses of FLOATING POINT BINARY!!!

From a pure language point of view, A COBOL compiler could perfectly do
DECIMAL computations without support of underlying hardware if the semantic
is respected.....If the underlying hardware support the BCD operations, it
will go faster, that's all...but it is not a primary requirement for
using/implementing packed decimal data, even is most of hardware have
implemented BCD instructions (Intel, PA-RISC and so on...by the way, did you
wonder why they did it???)


Just for a contribution, have a look to the Hursley CICS labs page on
decimal computation semantic  (packed or not :)) with a specific attention
to the truncation/rounding and other rules

http://www2.hursley.ibm.com/decimal/


Regards

FA






"Howard Brazee" <howard@brazee.net> a �crit dans le message de news:
br7f5v$e1$1@peabody.colorado.edu...
>
> On  9-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > >  Any argument about whether packed decimal should be signed that
> > > says that ignores hardware efficiency though is flawed.   Packed
decimal
> > is
> > > about hardware.
…[3 more quoted lines elided]…
> > It is about decimal accuracy on a system that was inherently floating
point,
>
> That's hardware.
…[11 more quoted lines elided]…
> benefits of the way the hardware is designed and costed.    It has nothing
to do
> with the business logic being processed.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-18T09:08:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<brsmva$2s0k$1@si05.rsvl.unisys.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com> <br7f5v$e1$1@peabody.colorado.edu> <3fe0f81a$0$400$afc38c87@news.easynet.fr>`

```

"Francis ANDRE" <francis.andre@easynet.fr> wrote in message
news:3fe0f81a$0$400$afc38c87@news.easynet.fr...

> Wrong......As explained very clearly by Peter, Packed Decimal data type it
> is about DECIMAL computation and as a consequence of BUSINESS computation
…[3 more quoted lines elided]…
> efficienty in time and space.....

Not entirely accurate.  There is not now, nor has there ever been, a
requirement in the standard that the underlying hardware support
packed-decimal arithmetic operations.

> DECIMAL computation has its own set of rules for ROUNDING, TRUNCATING,
ERROR
> REPORTING that have nothing to do with hardware.

To large degree, the prior standards for COBOL left much of this up to the
implementor.  Precise rules for arithmetic were introduced with the
"standard arithmetic" feature of 2002 COBOL.

> Moreover, these rules of
> truncation/rounding and division by zero are quite different from those of
> FIXED POINT BINARY

I don't see that being the case.  Can you clarify?

> and thoses of FLOATING POINT BINARY!!!

That I'll agree with.

> From a pure language point of view, A COBOL compiler could perfectly do
> DECIMAL computations without support of underlying hardware if the
semantic
> is respected.....

Absolutely.  We've been doing it for nigh onto forty years.

> If the underlying hardware support the BCD operations, it
> will go faster, that's all...

That's not at all clear!   Perhaps on some machines.  We found better
performance at less cost (to us and to our customers) by optimizing the
hardware for conversion to and from binary representation than by adding
hardware for the direct arithmetic processing of strings.

> but it is not a primary requirement for
> using/implementing packed decimal data,

If the machine processes BCD fast enough, why would the end user care if the
hardware supports decimal arithmetic?

> even is most of hardware have
> implemented BCD instructions

Not sure what this means ...

> (Intel, PA-RISC and so on...by the way, did you
> wonder why they did it???)

No, as it happens;

> Just for a contribution, have a look to the Hursley CICS labs page on
> decimal computation semantic  (packed or not :)) with a specific attention
> to the truncation/rounding and other rules
>
> http://www2.hursley.ibm.com/decimal/

I agree with the assertion that binary *floating-point* is generally
unsuitable for business computations, but I remain unconvinced that binary
*fixed-point* shares that unsuitability.  In our implementation USAGE BINARY
items obey exactly the same truncation and rounding rules that USAGE
COMPUTATIONAL, USAGE PACKED-DECIMAL and USAGE DISPLAY items obey, and that's
what our reading of the standard says they should do.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-22T17:01:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bs780e$rkg$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com> <br7f5v$e1$1@peabody.colorado.edu> <3fe0f81a$0$400$afc38c87@news.easynet.fr>`

```

On 17-Dec-2003, "Francis ANDRE" <francis.andre@easynet.fr> wrote:

> > Well, everything's marketing.   But packed-decimal is about the costs and
> > benefits of the way the hardware is designed and costed.    It has nothing
…[8 more quoted lines elided]…
> efficienty in time and space.....

No, decimal is about decimal.   Packed decimal is about decimal in less bytes.
Machines can be designed to do decimal arithmetic without packing the numbers.
The decision to pack them is about hardware and efficiency.

Time and space efficiency are not about business rules and logic, they are about
computer design.


> If the underlying hardware support the BCD operations, it
> will go faster, that's all...but it is not a primary requirement for
> using/implementing packed decimal data, even is most of hardware have
> implemented BCD instructions (Intel, PA-RISC and so on...by the way, did you
> wonder why they did it???)

No, I did not wonder about the obvious.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-12-13T09:42:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-3FF7AD.09423513122003@corp.supernews.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com>`

```
In article <3fd67828_5@news.athenanews.com>,
 "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> "Howard Brazee" <howard@brazee.net> wrote in message
> news:br56nn$ir$1@peabody.colorado.edu...
…[11 more quoted lines elided]…
> standards.

Well, no, it isn't that either.

All of those machines had fixed-point binary (aka integer) instructions 
that were more efficient at saving space than packed decimal and did not 
have the problems of floating point.

If they were so concerned about storage they would not have wasted 4 
bytes to store a number in the range -9,999,999..+9,999,999 when fixed 
point binary would allow them (+2^23)-1..-2^32.

Packed decimal gave some data validation.  If somebody crashed your 
integer you just had a different integer -- if somebody crashed your 
packed decimal field you got a machine exception and someone knew about  
it.  Though there are other validation types that could have been 
applided to fixed-point binary without giving up as much range.

But mostly I think it had to do with having a "human readable" format 
for human programmers to lazy to learn another base notation.  Why else, 
in those days of glacial CPU speeds and severly constrained storage 
would anyone choose a format that was slower than native binary AND took 
more storage?
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-13T11:56:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312131156.42caf019@posting.google.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com> <br56nn$ir$1@peabody.colorado.edu> <3fd67828_5@news.athenanews.com> <joe_zitzelberger-3FF7AD.09423513122003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 

> > > Packed decimal is about hardware.
> > NO, it ISN'T!!!!
…[3 more quoted lines elided]…
> Well, no, it isn't that either.

> Packed decimal gave some data validation.  If somebody crashed your 
> integer you just had a different integer -- if somebody crashed your 
> packed decimal field you got a machine exception and someone knew about 

 ... sometimes, depending on what value was crashed into it.

> But mostly I think it had to do with having a "human readable" format 
> for human programmers to lazy to learn another base notation.  Why else, 
> in those days of glacial CPU speeds and severly constrained storage 
> would anyone choose a format that was slower than native binary AND took 
> more storage?

Having done some rather different performance testing than others seem
to have, my view is that BCD is about having the best performance and
space saving in a business environment when there is only small
amounts of computation and large amounts of 'display' formatting.

The cost of display decimal computation is large, the cost of
converting from display decimal to binary is large.  So if one used
binary for calculations and all the data was comming in in display
format (cards) and was producing display format (invoices, customer
lists, cards) then the most efficient overall was to use BCD for
computations.  While splower than binary the conversion from decimal
to BCD and back was _much_ faster.

It's about business _system_ performance, not CPU or individual
instructions.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-10T13:55:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd66f5a_6@news.athenanews.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <br4ta7$r43$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:br4ta7$r43$1@si05.rsvl.unisys.com...
>
<snip>

> As I see it, the ultimate in portability for numeric items is given by
> DISPLAY with an explicit separate sign, but such items occupy twice (more
or
> less) the storage resources as the packed decimal equivalents, and require
> twice the resources to be transferred from one place or device to another.
>

So it's just as well that today's systems are MORE than twice (actually,
hundreds of times) more powerful than the systems that required the Packed
format to be developed, isn't it G>?

I agree with you regarding portability; I just don't see the "efficiency" or
"overheads" as a problem on modern hardware.

Pete.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-10T13:48:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd66dbc_1@news.athenanews.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:br4pju$68k$1@peabody.colorado.edu...
>
>
> There is only one reason for packed decimal numbers - it works better in
> hardware.

No, Howard, that is simply not true.

There are a number of reasons why Packed was introduced to System 360 and I
covered all of them elsewhere in this thread.

Pete.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-10T15:48:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br7f7r$l7$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <3fd66dbc_1@news.athenanews.com>`

```

On  9-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > There is only one reason for packed decimal numbers - it works better in
> > hardware.
…[4 more quoted lines elided]…
> covered all of them elsewhere in this thread.

Which I replied to.  (unconvinced)
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-10T07:24:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031210082554.203$pR@news.newsreader.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> So what is the compiler supposed to do when you subtract a larger number
> from a smaller one?   If the smaller number is signed - it subtracts them.  If the
> smaller one is unsigned, it does error processing.   It can't treat them the
> same.

Wow, Howard. I am constantly amazed at the efficiency of the IBM
propaganda machine. It's as if many of you can only view things through
the 'IBM filter'. :-)

Let me give you a real world counter-example. The Burroughs/Unisys
V Series hardware instruction format supported, for each instruction
address (you could have up to three addresses in one instruction), two
bits to specify indexing and two bits to specify unsigned, signed, alpha-
numeric and indirect. 'Numeric' on the V meant packed decimal, since
ALL math on the V was in decimal, even machine addresses. The V
was designed from the ground up as a COBOL machine. You could
add/subtract a signed/unsigned field to/from a signed/unsigned field,
in any combination. Or you could add/subtract/multiply/divide a
signed/unsigned field with a signed/unsigned field giving a
signed/unsigned result, in any combination. You could subtract a 10
digit signed field from a 4 digit unsigned field with a 10 digit signed
(or unsigned, you could test less/greater/equal afterward to determine
if the result was neg/pos/zero) field as result. No sweat. Remember,
an unsigned numeric field is a positive field. There is no mathematical
ambiguity. Or should I say 'IBMbiguity'? ;-) Learn to think outside the
'IBM box'. :-)

As an aside: the Burroughs/Unisys V series systems and assembly
language were the friendliest, easiest to work with, that I have ever
seen. Reading a memory dump was a piece of cake, since all numbers
and addresses were in decimal. You could do a table search in two
instructions (search/test), test for alpha, numeric or any arbitrary
combination of characters in two instructions (scan/test), or sort an
array with seven instructions. Sweet. IMO, it's only real CPU design
defect was the 5 digit machine address size. It eventually became an
impediment to growth, analogous to the Intel 80x86 64k limit.
```

###### ↳ ↳ ↳ The IBM box (was: Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-12-10T16:36:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031210113659.10830.00000452@mb-m24.aol.com>`
- **References:** `<20031210082554.203$pR@news.newsreader.com>`

```
Judson McClendon writes ...

[snip]

> Learn to think outside the
>'IBM box'. :-)

And his motivation to do that is?

Those of us with long careers in IBM mainframes may well be brainwashed. But
ya' know, it's paid the bills and kept life interesting. With z/Architecture,
z/OS UNIX, and a host of other new technologies springing up on the manframe
base it makes a lot more sense to learn that real well than to spend the effort
on learning an architecture he (or I) will likely never need to know. There's
just so many hours in the day, so many brain cells surviving this long, so much
work that has to get done, that there's simply no payback in sight for the
effort. Some do that for a hobby, but my hobby's include a lot of non-IS stuff
and so there it's also a matter of priorities.

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-11T07:18:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031211081959.778$lR@news.newsreader.com>`
- **References:** `<20031210082554.203$pR@news.newsreader.com> <20031210113659.10830.00000452@mb-m24.aol.com>`

```
"S Comstock" <scomstock@aol.com> wrote:
> Judson McClendon writes ...
> >
…[12 more quoted lines elided]…
> and so there it's also a matter of priorities.

One motivation is that you should always know *why* you do or believe
what you do. There may be good reasons to do/believe as you do, but you
should know what they are, so you won't make tunnel-vision assumptions
such as we have seen in this thread. Anyone who suggested never learning
a language other than COBOL would get a firestorm of protests, and rightly
so. But you are suggesting the vendor equivalent. :-)  Do not limit yourself
unnecessarily. You may never know when you will need to pay your bills
programming with someone else's hardware/software. Learn well the
platform you use, surely. But also learn what part of that knowledge is
'local', and what part is 'global'. :-)
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 13)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-12-12T14:29:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031212092905.04179.00000722@mb-m29.aol.com>`
- **References:** `<20031211081959.778$lR@news.newsreader.com>`

```
Judson McClendon writes ...

[snip]

>One motivation is that you should always know *why* you do or believe
>what you do. There may be good reasons to do/believe as you do, but you
…[7 more quoted lines elided]…
>'local', and what part is 'global'. :-)

Interesting, considering your signature tag line.

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-12T09:55:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031212105647.284$vU@news.newsreader.com>`
- **References:** `<20031211081959.778$lR@news.newsreader.com> <20031212092905.04179.00000722@mb-m29.aol.com>`

```
"S Comstock" <scomstock@aol.com> wrote:
>
> Interesting, considering your signature tag line.

I view my tagline more in terms of how 'true' it is. If 'true', then it must
be 'global' (based on content), but if 'not true', then it is 'irrelevant', not
'local'. My belief is that it is 'true', therefore 'global', therefore vastly
important, even vital. :-)
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 14)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-13T16:14:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vtn3p9nrd7ijb9@corp.supernews.com>`
- **In-Reply-To:** `<20031212092905.04179.00000722@mb-m29.aol.com>`
- **References:** `<20031211081959.778$lR@news.newsreader.com> <20031212092905.04179.00000722@mb-m29.aol.com>`

```
S Comstock wrote:
> Judson McClendon writes ...
> 
…[15 more quoted lines elided]…
> Interesting, considering your signature tag line.

In what way does signing his messages with John 3:16 violate what he's 
said above?
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 15)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-12-14T03:55:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031213225511.01603.00000533@mb-m20.aol.com>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com>`

```
LX-i writes ...

>S Comstock wrote:
>> Judson McClendon writes ...
…[21 more quoted lines elided]…
>

One could paraphrase ...

"Anyone who suggested never learning a religion other than Christianity
would get a firestorm of protests, and rightly so. ... Do not limit yourself
unnecessarily. You may never know when you will need to pay your
[salvation] bills with someone else's religion."

This is an international, multi-religious, technical forum. I find prosletyzing
inappropriate here, not to mention offensive to those of us who don't
have the same beliefs. Believe what you want, but stay on topic to the
group and respect others beliefs. That being said, I will say no more on
this topic.

Kind regards (I mean that sincerely),



-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 16)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-12-14T17:03:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BUclcaCtfJ3$EwN5@ld50macca.demon.co.uk>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com> <20031213225511.01603.00000533@mb-m20.aol.com>`

```
I've said it before and I'll say it again: I defend Judson's right to 
express publicly his religious beliefs. For the record, I am a staunch 
atheist and consider all religions flawed. Despite that, I support 
Judson's action, in expressing his belief, if not his expressed belief.

PLEASE don't start another religious pogrom on this newsgroup.
Thanks.

In message <20031213225511.01603.00000533@mb-m20.aol.com>, S Comstock 
<scomstock@aol.com> writes
>LX-i writes ...
>
…[49 more quoted lines elided]…
>USA
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-15T12:34:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031215133540.249$Pi@news.newsreader.com>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com> <20031213225511.01603.00000533@mb-m20.aol.com> <BUclcaCtfJ3$EwN5@ld50macca.demon.co.uk>`

```
Thank you, Alistair. Other than my tagline, I try not to proselytize here,
and when I do make comments about religious topics, I try to be even
handed. My intent is not to offend. :-)
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-15T10:39:13+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fdcd8d4_4@news.athenanews.com>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com> <20031213225511.01603.00000533@mb-m20.aol.com>`

```
Ah, Religion and/or Politics... you can bet on them every time to provoke a
reaction...<G>

Comments below...

"S Comstock" <scomstock@aol.com> wrote in message
news:20031213225511.01603.00000533@mb-m20.aol.com...
> LX-i writes ...
>
>
> "Anyone who suggested never learning a religion other than Christianity
> would get a firestorm of protests, and rightly so. ... Do not limit
yourself
> unnecessarily. You may never know when you will need to pay your
> [salvation] bills with someone else's religion."
>
> This is an international, multi-religious, technical forum. I find
prosletyzing
> inappropriate here, not to mention offensive to those of us who don't
> have the same beliefs. Believe what you want, but stay on topic to the
> group and respect others beliefs. That being said, I will say no more on
> this topic.
>
I am surprised by your sensitivity, Steve, but you make a good case, and it
is well expressed.

The thing to consider here is whether Judson is actually proselytizing by
use of his tag line.

You consider he is and are offended by it; I don't think he is and am not
offended by it.

I don't share Judson's beliefs, but knowing that HE holds them, helps me to
understand his approach and position on many things. His tag line certainly
wouldn't persuade me to re-evaluate or change my own religious views.

The most important point you made was respect for others' beliefs.

There has never been any indication that Judson is disrespecting other
Religions by using his tag line.
(The fact is that his religious belief may REQUIRE him to publicly state his
position...this is not through lack of tolerance or respect for other
opposing beliefs.)

I guess overall, you are correct that it is a technical forum and Religious
or Political banner waving is therefore inappropiate.

It probably would be "better" if he didn't use that particular tag line when
posting here, but this is a free, unmoderated, forum where people can say
anything they like (I just hope we manage to keep it that way), and that is
part of the deal when you come here... if you are likely to be offended,
then unmoderated forums are "best avoided".

I see tag lines as an expression of an individual's personality and for the
most part they are amusing and harmless. (The ones that are vicious or mean
get jumped on fairly quickly.)

BOTTOM LINE:

1. You have a right to say what you want about Judson's tag line.

2. Judson has a right to say what he wants in his tag line.

3. The rest of us have a right to accept or discard either of the above
positions.

Call it a draw <G>?

Pete.
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-15T12:50:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031215135209.757$Rn@news.newsreader.com>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com> <20031213225511.01603.00000533@mb-m20.aol.com> <3fdcd8d4_4@news.athenanews.com>`

```
Thanks Peter. I really do wish not to offend. I see taglines as simply a
place for people to say something personal. Many are humorous, and I
have seen a few that were pretty provocative, even hostile. To me, this
is a good example of free speech. It is a place to say what you want
without stuffing it down people's throats. I am not offended by those
who have different beliefs, or by Steve's comments, though I regret my
tagline bothers him. I don't recall ever protesting a tagline, even ones
containing what I would call profanity or blasphemy. The way I see it,
if God gives us free will to believe as we wish, who am I to question
that? :-)
```

###### ↳ ↳ ↳ Re: The IBM box (was: Re: How do they do it? (was" Re: MVS Packed

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-15T20:59:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vtst98thl996fe@corp.supernews.com>`
- **In-Reply-To:** `<20031215135209.757$Rn@news.newsreader.com>`
- **References:** `<vtn3p9nrd7ijb9@corp.supernews.com> <20031213225511.01603.00000533@mb-m20.aol.com> <3fdcd8d4_4@news.athenanews.com> <20031215135209.757$Rn@news.newsreader.com>`

```
Judson McClendon wrote:
> Thanks Peter. I really do wish not to offend. I see taglines as simply a
> place for people to say something personal. Many are humorous, and I
> have seen a few that were pretty provocative, even hostile. To me, this
> is a good example of free speech. It is a place to say what you want
> without stuffing it down people's throats.

My favorite one is Ubiquitous's...

ISLAM - Winning the hearts and minds of the world, one bomb at a time.

:)  (brevity truly is the essence of wit...)
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-10T21:39:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br83qi$7t7$1@peabody.colorado.edu>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <20031210082554.203$pR@news.newsreader.com>`

```

On 10-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Wow, Howard. I am constantly amazed at the efficiency of the IBM
> propaganda machine. It's as if many of you can only view things through
> the 'IBM filter'. :-)

I have spent almost half of my career using IBM mainframes.   But I have spent
over a decade on Univac, and have used Burroughs, Honeywell, and Vax.

I laughed as much as anybody when IBM "invented" virtual memory.
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 12)_

- **From:** atmbelg@yahoo.co.uk (AM)
- **Date:** 2003-12-15T05:17:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cc6bb282.0312150517.578b29b5@posting.google.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com> <20031208074645.970$P6@news.newsreader.com> <br2974$ke6$1@peabody.colorado.edu> <br2ifm$26l4$1@si05.rsvl.unisys.com> <br4pju$68k$1@peabody.colorado.edu> <20031210082554.203$pR@news.newsreader.com> <br83qi$7t7$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<br83qi$7t7$1@peabody.colorado.edu>...
> On 10-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:
> 
…[7 more quoted lines elided]…
> I laughed as much as anybody when IBM "invented" virtual memory.

Yup. While I was still in High School in 1964, the ATLAS computer at
the University of London (England) had virtual memory. And the 360/67
never worked, but the Univac 1108 did real time, remote batch and
denmand mode processing simultaneously; none of the crap IBM "3 OS on
1 machine" stuff they had on the 370s....

ATLAS project also developed 
Multiprogramming 
Job scheduling, 
Spooling 
Interrupts 
Pipelining 
Interleaved Storage 
Autonomous transfer units 
Virtual Storage 
Paging 
and probably more. It's all here
http://www.computer50.org/kgill/atlas/atlas.html
```

###### ↳ ↳ ↳ Re: How do they do it? (was" Re: MVS Packed Decimal with no sign nibble?)

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-08T10:58:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br2hkk$25r5$1@si05.rsvl.unisys.com>`
- **References:** `<20031207121721.593$2d@news.newsreader.com> <20031207232844.03883.00000415@mb-m07.aol.com>`

```

"S Comstock" <scomstock@aol.com> wrote in message
news:20031207232844.03883.00000415@mb-m07.aol.com...

> Just out of curiosity, as a lifelong IBM mainframe bigot, can you tell me
how
> such numbers convey sign when necessary? It seems they can't. So when you
need
> a sign, you have to waste a whole byte on it? Is that how they do it on
non-IBM
> iron?

When is it necessary for a PIC 9999 item to convey a sign if the arithmetic
and/or conversion hardware correctly determines that such an item is always
positive and treats it accordingly?

On Unisys MCP systems, given the following description:
    01  A-RECORD.
          03  FIELD-1 PIC 9999 PACKED-DECIMAL.
          03  FIELD-2 PIC 99999 PACKED-DECIMAL.
          03  FIELD-3 PIC X.
there are four "slack bits" between Field-2 and FIELD-3, and A-RECORD is 6
bytes long.  Given
    01  ANOTHER-RECORD.
          03  FIELD-4 PIC 999 PACKED-DECIMAL.
          03  FIELD-5 PIC 9 PACKED-DECIMAL.
there are NO slack bytes, and ANOTHER-RECORD is two bytes long.

If any of these four numeric fields is retrieved numerically, the hardware
instruction set is sufficiently powerful to take into account the fact that
the item is unsigned and thus positive, and if it is used as a destination
it is sufficiently powerful to know that no sign should be stored because
the item declaration has no sign, and its absolute value is then stored.

Why should it not be otherwise?

    -Chuck Stevens
```

##### ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "James" <magogrwr@bellsouth.net>
- **Date:** 2003-12-23T21:57:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Nc7Gb.15022$n01.10639@bignews5.bellsouth.net>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com>`

```
We used that technique last year in a system where we needed an internal
counter and couldn't expand
the data anymore and only had 1 byte left!

"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
news:nc14tv0c1g1r9u8cq7aa991gr002np2ve8@4ax.com...
> On Fri, 5 Dec 2003 16:43:58 -0600, "Judson McClendon"
> <judmc@sunvaley0.com> enlightened us:
…[7 more quoted lines elided]…
> >> It wasn't. The original System 360, designed by Gene Amdahl, had no
packed
> >> decimal. It was a pure binary machine, intended for (mainly) scientific
> >> applications. It utilised up to 64 bit (doubleword) binary, or floating
> >> point, or external decimal (which was converted to binary for
calculations).
> >
> >Peter, I am looking at a book titled "Logical Programming with
System/360"
> >by Don H. Stabley, copyright 1970, John Wiley publisher. On page 60, is a
> >paragraph with the heading "2. Packed Decimal Data", and on the opposite
> >page (61) is a chart showing how various packed decimal values would be
> >stored, dutifully showing the (IBM required) sign nibble. How can you say
> >that the System/360 did not require a sign on packed decimal fields? We
are
> >discussing packed decimal fields, no? Any packed decimal field on an IBM
> >System/360 or descendant requires a sign nibble. That's what I said, and
it's
> >true.
> >
…[13 more quoted lines elided]…
> >> Nope. Not at all. Memory (being hand made) was certainly expensive but
one
> >> of the reasons for implementing packed in the first place was to SAVE
> >> memory.
…[25 more quoted lines elided]…
> Steve
```

#### ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-06T14:44:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312061444.7463ee99@posting.google.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote

> Saving memory with packed decimal, yes. Saving memory by adding a
> redundant mandatory sign to 'unsigned' fields, no. :-)
> 
> Don't reject that idea so casually. When it comes to using every possible
> angle to sell more hardware, IBM was second to none in those days. 

There was proably _less_ hardware used because the design could be
simplified by not having to have options for signed and unsigned.

In any case leaving the sign nibble off only saves memory half the
time as the number is byte aligned.

You are also wrong that IBM wanted to sell more hardware, what it
wanted to do was get more money.  If it could do this with _less_
hardware then it would.  Leaving off the hardware to support two types
of packed decimal achieved this.
```

#### ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-07T13:01:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd26e27_6@news.athenanews.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031205174458.964$v0@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
…[4 more quoted lines elided]…
> > It wasn't. The original System 360, designed by Gene Amdahl, had no
packed
> > decimal. It was a pure binary machine, intended for (mainly) scientific
> > applications. It utilised up to 64 bit (doubleword) binary, or floating
> > point, or external decimal (which was converted to binary for
calculations).
>
> Peter, I am looking at a book titled "Logical Programming with System/360"
…[3 more quoted lines elided]…
> stored, dutifully showing the (IBM required) sign nibble.

Thank you for quoting your reference. I have no quibble with that particular
"Authority",  but I certainly take issue with the way you have interpreted
it.


> How can you say
> that the System/360 did not require a sign on packed decimal fields?

I didn't say that. (But I'm going to now <G>...see below).

(Although in the early days using BAL (System 360 Assembler), we routinely
packed data without storing a sign in it... It is an ARITHMETIC requirement,
NOT a storage requirement. It certainly requires a sign for COBOL.)

I said S360 users have a CHOICE of arithmetic formats, and at least one of
these supports unsigned decimal fields, even for arithmetic.

YOU said the S360 "was designed to always require a sign" (you can see the
quote above; I'm not making it up...<G>) and I corrected you on this.

> We are
> discussing packed decimal fields, no?

Now, that is a fair point, given the topic. However, like the majority of
posts in CLC, this one drifts on and off topic.

I would agree with you that we are "discussing packed fields" at least some
of the time. In my own posts I was very clear about what applied to packed
and what didn't, but I did not always stay exactly on topic.

> Any packed decimal field on an IBM
> System/360 or descendant requires a sign nibble. That's what I said, and
it's
> true.
>

No, it isn't.

Sadly, restating it confidently and emphatically just makes you more
emphatically wrong.

A sign nibble is required for ARITHMETIC fields (fields which we intend to
use in calculation). There is NO intrinsic requirement for packed fields to
use the last nibble as a sign. You can PACK anything; only when you try to
do arithmetic on it will you get a S0c7, if it doesn't contain a valid
arithmetic sign. (As many Assembler programmers found to our cost...and many
COBOL programmers have found to their cost, right up to the present time,
when they move spaces to a group level containing packed fields, thereby
"packing a blank". Note the system does NOT crash on the MOVE; it crashes as
soon as you use one of the packed fields for ARITHMETIC.)


> > > Perhaps to sell more memory?
> >
> > Nope. Not at all. Memory (being hand made) was certainly expensive but
one
> > of the reasons for implementing packed in the first place was to SAVE
> > memory.
…[3 more quoted lines elided]…
>

And you have no problem reconciling these two conflicting ideas in your
mind? (It must be Hell in there...<G>)

> Don't reject that idea so casually.

When an idea is blatantly stupid I do tend to dismiss it.

Do you have any other evidence for your axiomatically unsound, unsupported,
assertion, that would warrant my expending  brain cells on re-evaluating it?

I think not.

> When it comes to using every possible
> angle to sell more hardware, IBM was second to none in those days.

That is certainly true, but they never descended to the obviously absurd.

> Bill
> Gates probably learned much of what he knows about that from watching
> IBM. Gates did say he wanted to be "the IBM of software," remember?

Switching your losing argument to enlist the anti-Bill Gates camp cuts no
ice with me <G> .
(Either as a rhetorical device or as support for your case. What Bill Gates
did or did not say has as much relevance to this discussion as General
Relativity does to an archer fish contemplating a fly. (Figure that one out
for yourself...<G>))

Who's off-topic now <G>?

Pete.
```

##### ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-07T10:56:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031207115744.182$wy@news.newsreader.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <3fd26e27_6@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> (Although in the early days using BAL (System 360 Assembler), we routinely
> packed data without storing a sign in it... It is an ARITHMETIC requirement,
> NOT a storage requirement. It certainly requires a sign for COBOL.)

I never intended to question that data could be packed like that in assembly,
or even cleverly written COBOL. What I have been trying to express is that
it is not supported as a data type by the hardware, and that you could not do
arithmetic using an unsigned packed decimal field without having a sign,
both of which are supported by all the non-IBM hardware I am currently
familiar with. Your post above seems to say you agree with me. :-)

Anyway, I think we've rode this horse to death. :-)
```

###### ↳ ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-08T11:15:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd3a6bb_3@news.athenanews.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <3fd26e27_6@news.athenanews.com> <20031207115744.182$wy@news.newsreader.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031207115744.182$wy@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > (Although in the early days using BAL (System 360 Assembler), we
routinely
> > packed data without storing a sign in it... It is an ARITHMETIC
requirement,
> > NOT a storage requirement. It certainly requires a sign for COBOL.)
>
> I never intended to question that data could be packed like that in
assembly,
> or even cleverly written COBOL. What I have been trying to express is that
> it is not supported as a data type by the hardware, and that you could not
do
> arithmetic using an unsigned packed decimal field without having a sign,
> both of which are supported by all the non-IBM hardware I am currently
> familiar with. Your post above seems to say you agree with me. :-)
>
> Anyway, I think we've rode this horse to death. :-)

Yes, I agree.

The only issue (now) is your stated belief that the sign nibble was/is a
ploy by IBM to sell more memory.

Withdraw that, and we can close this argument like the gentlemen we are <G>.

Pete.


> -- 
> Judson McClendon      judmc@sunvaley0.com (remove zero)
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-08T06:50:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031208075121.063$DI@news.newsreader.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <3fd26e27_6@news.athenanews.com> <20031207115744.182$wy@news.newsreader.com> <3fd3a6bb_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>
…[3 more quoted lines elided]…
> Withdraw that, and we can close this argument like the gentlemen we are <G>.


I only suggested that as a conceivable possibility, somewhat tongue-in-
cheek at that. I actually believe it was originally done simply to make the
CPU design simpler. Fair enough?  :-)
```

###### ↳ ↳ ↳ Re: MVS Packed Decimal with no sign nibble?

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-09T11:55:33+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd501ac_8@news.athenanews.com>`
- **References:** `<8YudnQLu9tKopFaiRVn-uw@comcast.com> <xWcJcSB6d7y$EwDF@ld50macca.demon.co.uk> <QEYyb.36180$aT.34342@news-server.bigpond.net.au> <20031202074525.298$YC@news.newsreader.com> <3fccadee_2@news.athenanews.com> <20031205174458.964$v0@news.newsreader.com> <3fd26e27_6@news.athenanews.com> <20031207115744.182$wy@news.newsreader.com> <3fd3a6bb_3@news.athenanews.com> <20031208075121.063$DI@news.newsreader.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031208075121.063$DI@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[4 more quoted lines elided]…
> > Withdraw that, and we can close this argument like the gentlemen we are
<G>.
>
>
> I only suggested that as a conceivable possibility, somewhat tongue-in-
> cheek at that. I actually believe it was originally done simply to make
the
> CPU design simpler. Fair enough?  :-)

OK, that's fine <G>.

I hope you are now better informed and realise that packed processing on IBM
systems has nothing to do with CPU design.

It was originally implemented in firmware, as an optional extra, to a
machine that already had a highly efficient CPU <G>.

I have been interested to read Chuck's posts as to how the same
functionality is implemented on Unisys equipment.

No further posts from me on this, except in response to specific questions,
if any.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
