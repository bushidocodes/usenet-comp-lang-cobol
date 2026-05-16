[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Several Homework Questions please

_13 messages · 9 participants · 2002-03 → 2002-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Several Homework Questions please

- **From:** rhamm90210@icqmail.com (Ryan Hamm)
- **Date:** 2002-03-27T14:09:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7dbb410.0203271409.4a2f358d@posting.google.com>`

```
I've searched every place I can find on the net (ZingCOBOL) and a
couple of books such as Structured COBOL Programming second edition,
Structured COBOL Programming Flowchart edition.  I've found answers to
most of the questions asked but a few aren't findable.  The teacher of
the class has said we probably won't find them all so I come here to
hope someone will be friendly enough to give me a couple of answers:

1.  In COBOL, the default storage for a numeric field is
________________
A.  zoned
B.  packed
C.  compressed
D.  computational

From two different sources it says that Display is the default usage
type but I can find nothing that says what the default storage type
is.

2.  A structure variable can not contain another structure variable. 
True or False

Since I can't find what a structure variable is I have no clue how to
answer this.  We had 45 questions and these are the two most stumping.
 Help would be appreciated on these two questions.
```

#### ↳ Re: Several Homework Questions please

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-03-27T17:27:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MGro8.5996$oz6.1720344@news20.bellglobal.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com>`

```
"Ryan Hamm" <rhamm90210@icqmail.com> wrote in message
news:b7dbb410.0203271409.4a2f358d@posting.google.com...
> I've searched every place I can find on the net (ZingCOBOL) and a
> couple of books such as Structured COBOL Programming second edition,
…[15 more quoted lines elided]…
>

None of the above.  Cobol cannot have a numeric field without a picture
clause, so there is no such thing as a default.  The storage MUST be
defined.

> 2.  A structure variable can not contain another structure variable.
> True or False
>

False, though I have never heard it called a structure variable in Cobol, I
am assuming you mean something like:

    01 this-is-a-record.
        02 this-is-a-group.
            04 this-is a-variable    picture x.

> Since I can't find what a structure variable is I have no clue how to
> answer this.  We had 45 questions and these are the two most stumping.
>  Help would be appreciated on these two questions.

Donald
```

##### ↳ ↳ Re: Several Homework Questions please

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-03-27T23:19:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vsso8.25433$n8.25381@nwrddc02.gnilink.net>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com>`

```
Donald Tees <donald_tees@sympatico.ca> wrote in message
news:MGro8.5996$oz6.1720344@news20.bellglobal.com...
> "Ryan Hamm" <rhamm90210@icqmail.com> wrote in message
> news:b7dbb410.0203271409.4a2f358d@posting.google.com...
…[21 more quoted lines elided]…
> defined.

The PICTURE clause does not define the USAGE. If no USAGE clause is present
for a numeric data item, and no group-level USAGE is in effect for that item
DISPLAY is assumed.

Therefore, the correct answer is what DISPLAY usage is :"zoned decimal"

BTW, USAGE COMP-1 or COMP-2  numeric data items do NOT use a PICTURE clause.
(Neither do pointers, but those are not really numeric fields).

MCM
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2002-03-27T17:14:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7tqqh$4lh$1@si05.rsvl.unisys.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <vsso8.25433$n8.25381@nwrddc02.gnilink.net>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:vsso8.25433$n8.25381@nwrddc02.gnilink.net...


> BTW, USAGE COMP-1 or COMP-2  numeric data items do NOT use a PICTURE
clause.

Ummm... As an advocate of portability, I must comment.

All of the COMP-n USAGEs are extensions to standard COBOL, be that standard
'68, '74, '85 or the upcoming 2002.   Some implementations of standard COBOL
have NO COMP-n extensions at all.

What one implementor chooses to mean by COMP-1 in an implementation as an
extension to standard COBOL on a certain machine has nothing to do with what
another implementor chooses to mean by it on another (or even the same)
machine.

I know of one implementation that, as you suggest, allows COMP-1 through
COMP-4, disallows PICTUREs on COMP-1 and COMP-2, and requires PICTUREs on
COMP-3 and COMP-4.  All four are marked as extensions to the standard (in
this case, ANSI X3.23-1968) in the documentation.

I know another implementation  that requires PICTUREs on COMP-1 and COMP-2,
doesn't allow them on COMP-4 and COMP-5, and doesn't allow COMP-3 at all.

COMP-2 in the second implementation is a whole lot like COMP-3 in the first;
COMP-4 and COMP-5 in the second are sort-of-similar-in-philosophy (though
not at all alike in internal structure) to COMP-1 and COMP-2 respectively in
the first, and COMP-1 in the second implementation has no parallel in the
first at all.

    -Chuck Stevens
```

##### ↳ ↳ Re: Several Homework Questions please

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-28T11:57:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA3052A.29F72201@Azonic.co.nz>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com>`

```
Donald Tees wrote:

> > 1.  In COBOL, the default storage for a numeric field is
> > ________________
…[7 more quoted lines elided]…
> defined.

Actually 'DISPLAY' is the default.
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-03-28T08:59:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0203280859.7e20c713@posting.google.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <3CA3052A.29F72201@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3CA3052A.29F72201@Azonic.co.nz>...
> Donald Tees wrote:
> 
…[11 more quoted lines elided]…
> Actually 'DISPLAY' is the default.

The original question is *very badly* written.

1. What does the standard say about how DISPLAY items are stored?

2. I've seen various methods of storing DISPLAY items on the PC
including:

                     (1)    (2)    (3)
 digit  ebcdic     ascii  ascii  ascii
          char      char   char   char
u  0-9     0-9       0-9    0-9    0-9 
+  0-9   {,A-I     {,A-I    0-9  @,A-I
-  0-9   },J-R     },J-R    p-y    P-Y

           hex       hex    hex    hex  
         f0-f9     30-39  30-39  30-39
         c0-c9  7b,41-49  30-39  40-49
         d0-d9  7d,4a-52  70-79  50-59

(1) ibm-pc cobol 1.00, cobol "6.50", ms-cobol 2.2
(2) ms-cobol 4.5 (mf)
(3) fujitsu 3.0 (win32)

Note that the signed digits in column (1) don't fit a simple bit field
scheme.

3. Other than to explain the history of computers, why do people use
the obsolete term "zoned decimal" anymore anyway, particularly when
teaching? It doesn't mean much to someone who has never seen a real
live punched card.

4. How about bit field or bitmapped or nibble or nybble or half byte,
etc.
(Please don't flame me about non eight bit bytes <g>.)
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-03-29T08:40:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA4286F.7FAED6D7@Azonic.co.nz>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <3CA3052A.29F72201@Azonic.co.nz> <7f64e2ff.0203280859.7e20c713@posting.google.com>`

```
E P Chandler wrote:
> > > > 1.  In COBOL, the default storage for a numeric field is
> > > > ________________
…[11 more quoted lines elided]…
> The original question is *very badly* written.

I suspect that the question is archaic and probably originated in the
60s or 70s.

> 1. What does the standard say about how DISPLAY items are stored?

No.  The question was asking how CLASS NUMERIC items are stored if the
method used to store them is not specified.  ie what is the default
_USAGE_.  That is reasonably clear because: 1) it is quite specific
about NUMERIC, which is a class, and 2) 3 of the answers are actual
USAGE options (as long as you recognise what zoned decimal is), the 4th
is spurious.


> 2. I've seen various methods of storing DISPLAY items on the PC
> including:
…[3 more quoted lines elided]…
>           char      char   char   char

What has the 'EDCDIC char' got to do with it on a PC ?

Regardless, you are simply indicating that it is 'zoned' with a
different bit used as the '-' zone, plus in (1) it also uses a 'signed'
zone.

> 3. Other than to explain the history of computers, why do people use
> the obsolete term "zoned decimal" anymore anyway, particularly when
> teaching? It doesn't mean much to someone who has never seen a real
> live punched card.

The EDCDIC character set is simply a zoned set of bits deriving directly
from punched card bit patterns which had been in use for decades
before.  The variations of decimal encoding you noticed derives from
several points: different companies used different encodings for '-';
emulating EBCDIC zonings in ASCII was done in different ways.  <shrung>
this is nothing to do with the question anyway.

> 4. How about bit field or bitmapped or nibble or nybble or half byte,
> etc.

Why ?, do you thing they may be a possibility for being the default for
a CLASS NUMERIC ?
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

_(reply depth: 5)_

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-03-28T21:06:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0203282106.389a12a0@posting.google.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <3CA3052A.29F72201@Azonic.co.nz> <7f64e2ff.0203280859.7e20c713@posting.google.com> <3CA4286F.7FAED6D7@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3CA4286F.7FAED6D7@Azonic.co.nz>...
> E P Chandler wrote:
> > 
> > The original question is *very badly* written.
 
> I suspect that the question is archaic and probably originated in the
> 60s or 70s.
 
> What has the 'EDCDIC char' got to do with it on a PC ?
 
One mapping uses the same characters except they are in ASCII. So the
relationship between digits and characters is more complex than simple
"zoning". Even if zones are used, the zoning scheme varies.

I'm trying to illustrate the variety in the representations using the
question as a foil for discussion.

I wonder what "zoned decimals" look like on pre 360 IBM systems,
Burroughs, Univac or a PDP-10? What do they look like in SIXBIT or
FIELDATA?
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

_(reply depth: 6)_

- **From:** Edward Reid <edward@paleo.org>
- **Date:** 2002-03-29T19:55:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B8CA771B0ACA16F70F75D0D0@news-east.usenetserver.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <3CA3052A.29F72201@Azonic.co.nz> <7f64e2ff.0203280859.7e20c713@posting.google.com> <3CA4286F.7FAED6D7@Azonic.co.nz> <7f64e2ff.0203282106.389a12a0@posting.google.com>`

```
On Fri, 29 Mar 2002 0:06:34 -0500, E P Chandler wrote
> I wonder what "zoned decimals" look like on pre 360 IBM systems,
> Burroughs, Univac or a PDP-10? What do they look like in SIXBIT or
> FIELDATA?

The current Unisys incarnations of the old Burroughs systems use 
EBCDIC, and the same zoned signs as the IBM 360 and its successors. 
There are two major Burroughs lines which are extinct; they used the 
same representation.

Packed decimal is a horse of a different color; though the digits are 
the same, just about everything else is different, and the usual rule 
is that for practical purposes they are incompatible.

The IBM 1401 used six-bit characters, so the internal representation is 
inherently incompatible with the 360. However, IIRC the punched card 
representation was the same -- just an overpunch in row 11 or 12 for 
negative or positive.

I note that the standard specifically leaves the representation of the 
sign up to the implementor when the SIGN clause is not specified. So as 
for the original question -- "In COBOL, the default storage for a 
numeric field is" -- the answer  "zoned" is just plain wrong. The 
standard allows implementation of the default sign as a separate 
character.

Edward Reid
Looking for work, will program 029 keypunch drums
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

_(reply depth: 7)_

- **From:** Edward Reid <edward@paleo.org>
- **Date:** 2002-04-03T14:40:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01HW.B8D0C4D00C4507890F751990@news-east.usenetserver.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com> <MGro8.5996$oz6.1720344@news20.bellglobal.com> <3CA3052A.29F72201@Azonic.co.nz> <7f64e2ff.0203280859.7e20c713@posting.google.com> <3CA4286F.7FAED6D7@Azonic.co.nz> <7f64e2ff.0203282106.389a12a0@posting.google.com> <01HW.B8CA771B0ACA16F70F75D0D0@news-east.usenetserver.com>`

```
On Fri, 29 Mar 2002 19:55:07 -0500, Edward Reid wrote
> The current Unisys incarnations of the old Burroughs systems use 
> EBCDIC, and the same zoned signs as the IBM 360 and its successors. 
> There are two major Burroughs lines which are extinct; they used the 
> same representation.

I lied. The V-Series (also known by various model numbers such as 
B2500, B3700, B4900) used a zone on the LEADING character for the sign. 
A standard transformation in converting COBOL from V-Series to 
A-Series/NX/LX (the surviving lines) was to add SIGN LEADING to all 
signed numeric items, to avoid data conversion. Which of course mucked 
up efficiency royally.

Edward Reid
```

#### ↳ Re: Several Homework Questions please

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-27T23:22:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8vso8.111218$Gf.10563152@bin2.nnrp.aus1.giganews.com>`
- **References:** `<b7dbb410.0203271409.4a2f358d@posting.google.com>`

```

"Ryan Hamm" <rhamm90210@icqmail.com> wrote in message
news:b7dbb410.0203271409.4a2f358d@posting.google.com...
> I've searched every place I can find on the net (ZingCOBOL) and a
> couple of books such as Structured COBOL Programming second edition,
…[14 more quoted lines elided]…
> is.

I assume you have a picture associated with each of these. While the storage
may depend on the picture (for example, the picture may contain editting
characters), I would have to pick "zoned" (although "zoned" is not a word
found in the COBOL community). The actual, common, and OFFICIAL answer is,
as you discovered, DISPLAY.

There is no such thing as "Compressed" storage. This is a trick answer.

>
> 2.  A structure variable can not contain another structure variable.
> True or False

I've been doing this for many decades and I have no idea what a COBOL
"Structure Variable" might be. It does not appear in any of the (many)
reference books I have, nor have I ever heard it used. Must be something
your instructor appropriated from C++ (which does have such a thing).

see: http://www.geocities.com/sstutor/structures.htm

Seems as if a structure variable (in C++) is a COBOL group item. If so, the
answer is TRUE.

>
> Since I can't find what a structure variable is I have no clue how to
> answer this.  We had 45 questions and these are the two most stumping.
>  Help would be appreciated on these two questions.
>
```

##### ↳ ↳ Re: Several Homework Questions please

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-03-28T06:04:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020328010410.22422.00000469@mb-fv.aol.com>`
- **References:** `<8vso8.111218$Gf.10563152@bin2.nnrp.aus1.giganews.com>`

```
Hi Jerry,

Are you sure want to ans TRUE. It seems your explaination indicates FALSE.
Maybe you missed the "not" in the ques?

Regards, Jack.
```

###### ↳ ↳ ↳ Re: Several Homework Questions please

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-28T15:45:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aUGo8.6202$VJ1.596799@bin3.nnrp.aus1.giganews.com>`
- **References:** `<8vso8.111218$Gf.10563152@bin2.nnrp.aus1.giganews.com> <20020328010410.22422.00000469@mb-fv.aol.com>`

```

"Jnjsle" <jnjsle@aol.com> wrote in message
news:20020328010410.22422.00000469@mb-fv.aol.com...
> Hi Jerry,
>
…[3 more quoted lines elided]…
> Regards, Jack.

Arghhh! You're right. To reiterate:

A GROUP item may contain another GROUP item.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
