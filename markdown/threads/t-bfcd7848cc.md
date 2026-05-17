[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Date standardizing or patching?

_35 messages · 25 participants · 1997-04 → 1997-05_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Date standardizing or patching?

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ig6lm$133$1@news1.i1.net>`

```



Every problem to be fixed creates an opportunity to make your programs
and system better, or much, much worse.

With the Y2K problem and the time pressure to fix the problems, what
has been your shop or clients approach to fixing the dates?

I've seen many shops with as many as 4 or 5 different formats, YYMMDD,
MMDDYY, YYDDD, some are packed, some are unpacked. I've pulled my
hair out writing aging or tracking reports and routines that need to
interface dates with different formats. Different formats add time to
program and complexity.

Has your shop decided to standardize all date fields to one format?
Have they decided to add separate century fields to correspond with
existing date fields? Or something in between?

Thoughts?

Tim Oxler

TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

#### ↳ Re: Date standardizing or patching?

- **From:** "mbr..." <ua-author-17072189@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5ig6lm$133$1@news1.i1.net>`
- **References:** `<5ig6lm$133$1@news1.i1.net>`

```

Tim Oxler (tro··.@i··.net) wrote:
› Every problem to be fixed creates an opportunity to make your programs
› and system better, or much, much worse.
 
› With the Y2K problem and the time pressure to fix the problems, what
› has been your shop or clients approach to fixing the dates?
 
› I've seen many shops with as many as 4 or 5 different formats, YYMMDD,
› MMDDYY, YYDDD, some are packed, some are unpacked.  I've pulled my
› hair out writing aging or tracking reports and routines that need to
› interface dates with different formats.  Different formats add time to
› program and complexity.
 
› Has your shop decided to standardize all date fields to one format?
› Have they decided to add separate century fields to correspond with
› existing date fields?  Or something in between?
 
› Thoughts?
 
› Tim Oxler
 
› TEO Computer Technologies Inc.
› tro··.@i··.net
› http://www.i1.net/~troxler
› http://users.aol.com/TEOcorp

Two words:

### ##### ####### ##### ##### ### #
# # # # # # # # # # # ##
# # # # # # # # # # #
# ##### # # ##### ###### # # #
# # # # # # # # # # #
# # # # # # # # # # # #
### ##### ####### ##### ##### ### #####

Read about it in:

http://www.ft.uni-erlangen.de/~mskuhn/iso-time.html
```

##### ↳ ↳ Re: Date standardizing or patching?

- **From:** "chile" <ua-author-39481769@usenetarchives.gap>
- **Date:** 1997-05-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p2@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap>`

```

The way I see it ( whatever thats worth ) is that for existing programs.

1 if dates are unpacked pack them and ad CC to the begining of the field
this expands the 6 byte field to 11 bytes and does not upset the rest of
the rest of the record.
2 if the dates are already packed add C to the begining of the field as
there are 7 digits available in the field.
These changed will affect the system as little as possible.

But for new applications the imput and reporting format should be
MM/DD/CCYY the file format should be CCYYMMDD as it will then sort
correctly without any "complex" sorting.


On 9 Apr 1997, Marc Brett wrote:

› Tim Oxler (tro··r@i··.net) wrote:
›› Every problem to be fixed creates an opportunity to make your programs
…[42 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Date standardizing or patching?

- **From:** "g..." <ua-author-1935339@usenetarchives.gap>
- **Date:** 1997-05-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p2@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap>`

```

Certified Chilehead (ch··.@jos··t.com) wrote:

: The way I see it ( whatever thats worth ) is that for existing programs.

: 1 if dates are unpacked pack them and ad CC to the begining of the field
: this expands the 6 byte field to 11 bytes and does not upset the rest of
: the rest of the record.
: 2 if the dates are already packed add C to the begining of the field as
: there are 7 digits available in the field.
: These changed will affect the system as little as possible.

Believe me, it's not that simple. Some languages don't handle packed
decimal easily. Even for those which do, conversion of the data may well
be a formidable task. Consider a store of two billion records, each
containing three dates. How long will it take to convert, and how will
you handle processing while the conversion is going on and both old and
new formats are present? What do you suggest for dates which are packed
into _three_ bytes.

: But for new applications the imput and reporting format should be
: MM/DD/CCYY the file format should be CCYYMMDD as it will then sort
: correctly without any "complex" sorting.

Actually, given the current emphasis on international operations, the
MM/DD/CCYY format is seriously defective, even for human interaction.
The unambiguous CCYY-MM-DD format should be used, with whatever choice of
punctuation suits your organization.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "chile" <ua-author-39481769@usenetarchives.gap>
- **Date:** 1997-05-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```



On 5 May 1997, Gary L. Smith wrote:

› Certified Chilehead (ch··e@jos··t.com) wrote:
› 
…[7 more quoted lines elided]…
› : These changed will affect the system as little as possible.
 
› 
› Believe me, it's not that simple.  Some languages 

The discussion was to RPG and COBOL which do convert easily

don't handle packed
› decimal easily.  Even for those which do, conversion of the data may well 
› be a formidable task.  Consider a store of two billion records, each 
› containing three dates.  How long will it take to convert, and how will 
› you handle processing while the conversion is going on and both old and 
› new formats are present?
Shouldnt take any longer than a backup and a restore.

What do you suggest for dates which are packed
› into _three_ bytes.

Never heard of any such way to pack a date. MMDDYY packs into 0MDY
MDY+
and thats 4 bytes leaving 1 nibble for the C.
you of cource have to assume the second C

› 
› : But for new applications the imput and reporting format should be
…[6 more quoted lines elided]…
› punctuation suits your organization.

As programmers we will have to see how managment will react to this it is
preferable but I dont think it will fly with the powers that be

› --
›
…[3 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "dr john stockton" <ua-author-517039@usenetarchives.gap>
- **Date:** 1997-05-04T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```

In article <5kjrnt$c.··.@new··t.com> of Mon, 5 May 1997 05:38:05 in
comp.software.year-2000, "Gary L. Smith" wrote:
› Actually, given the current emphasis on international operations, the 
› MM/DD/CCYY format is seriously defective, even for human interaction.
 
› Yes.
 
› The unambiguous CCYY-MM-DD format should be used, with whatever choice of 
› punctuation suits your organization.

No. The format is ambiguous. CC can be, and has been (in the USA, by
some State body's staff), interpreted as the Century, currently the
20th.

Use YYYY/MM/DD to indicate what you undoubtedly actually mean.

John Stockton, Surrey, UK.    j.··.@mer··o.uk    Turnpike v1.12    MIME.
  Web URL: http://www.merlyn.demon.co.uk/ -- includes FAQqish topics and links.
  Correct 4-line sig separator is as above, a line comprising "-- " (SoRFC1036)
  Before a reply, quote with ">" / "> ", known to good news readers (SoRFC1036)
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "g..." <ua-author-1935339@usenetarchives.gap>
- **Date:** 1997-05-04T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p6@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p6@usenetarchives.gap>`

```

Dr John Stockton (j.··.@mer··o.uk) wrote:

: >The unambiguous CCYY-MM-DD format should be used, with whatever choice of
: >punctuation suits your organization.

: No. The format is ambiguous. CC can be, and has been (in the USA, by
: some State body's staff), interpreted as the Century, currently the
: 20th.

: Use YYYY/MM/DD to indicate what you undoubtedly actually mean.

That was perhaps clumsy terminology on my part. Of course I meant YYYY,
as you suggest.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```

Gary L. Smith wrote:
› 
› Believe me, it's not that simple.  Some languages don't handle packed
…[6 more quoted lines elided]…
› 
This struck me as an interesting challenge: a date packed into 3 bytes?
I'll assume you're talking about a 'Julian' date (YYDDD) stored as a
COBOL usage COMP-3 data element ('yydddS'x). Actually, you could
(somewhat) easily convert this date field to include the century, er,
4-digit year, by storing it as Binary (usage COMP) and truncating the
high-order byte (via redefines), and moving the remaining 3 bytes to a
PIC X(3) field (and visa-versa).
I know this wasn't the point, but it seemed worth exploring in case
anyone else out there had run into this before.
Cheers :-)
Jim Van Sickle   
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p8@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap>`

```



Jim Van Sickle wrote in article <336··.@i··.net>...
› This struck me as an interesting challenge: a date packed into 3 bytes? 
› I'll assume you're talking about a 'Julian' date (YYDDD) stored as a
…[7 more quoted lines elided]…
› Cheers :-)
01 DATE-WORK.
05 DATE-FULL PIC S9(7) COMP-3.
05 FILLER REDEFINES DATE-FULL.
07 DATE-MOVE PIC X(03).

COMPUTE DATE-FULL = * 100.
MOVE DATE-MOVE TO

I've seen code like this in an IBM mainframe COBOL environment used to pack
a six position date into three bytes ... The same could be done if you
cared to use a four position date ... Interesting enough, this stripping
technique does result in a field that can be interrogate via a SORT
include/omit and other utilities, i.e. the fields are in byte-to-byte
accordingly to CC, YY, MM, DD order ... A little clever programming can
make this field more useful than leaving the components float across byte
positions ... Anyway, I said I've seen it done ... I don't however
recommend its use.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p9@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap>`

```

In article <01bc5a65$1a0d3080$95609fcf@corkery1>,
"Kevin P Corkery" wrote:
› 
› 
…[16 more quoted lines elided]…
› COMPUTE DATE-FULL =  * 100.

You have an error here; I think you want to multiply by 10 NOT 100. Or maybe
you were trying to demostrate why this is a "bad" idea B]

› MOVE DATE-MOVE TO 
› 
…[9 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p9@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap>`

```

Kevin P Corkery wrote:
› 
› Jim Van Sickle  wrote in article <336··.@i··.net>...
…[23 more quoted lines elided]…
› recommend its use.

We are still left with the challenge of including a 4-digit year (in the
interest of Y2K compliance--I forget but I think this was the original
issue), and, for argument's sake, storing it in a 3-byte field. My
suggestion, using Julian rather than Gregorian format, would look
something like:

01 DATE-COMP PIC S9(9) USAGE COMP.
01 FILLER REDEFINES DATE-COMP.
05 FILLER PIC X.
05 DATE-BIN PIC X(3).

01 DATE-DISPLAY PIC 9(7) .
01 FILLER REDEFINDS DATE-DISPLAY.
05 DATE-YYYY PIC 9(4).
05 DATE-DDD PIC 9(3).

MOVE 1997 TO DATE-YYYY.
MOVE 127 TO DATE-DDD.
MOVE DATE-DISPLAY TO DATE-COMP.
MOVE DATE-BIN TO .

(Disclaimer: I didn't test this but it should work)

To convert back, simply reverse the process (make sure DATE-COMP is
initialized to zero first). If you're only interested in a 2-digit year,
the first method mentioned will work, but the maximum *binary* value
that can fit in 3-bytes, x'FFFFFF', has a decimal equivalent of
16777215--not big enough for YYYYMMDD (well, not after the late 17th
century, anyway :-). If you're stuck with Gregorian, you could also
store the year as 3 digits, with the first digit being a century
indicator (0=19, 1-20). This will also facilitate sorting and comparing,
etc.

Most importantly, any of these methods also avoids the packed decimal
format that nobody but COBOL understands!

Jim Van Sickle   
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p11@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap> <gap-bfcd7848cc-p11@usenetarchives.gap>`

```

Jim Van Sickle wrote:

› 
› Most importantly, any of these methods also avoids the packed decimal
…[6 more quoted lines elided]…
› Rochelle Park, NJ

Jim,

PL/I, SAS and Assembler have no problems with packed decimal data.
---
Wayne L. Beavers        mailto:way··.@bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"The Mainframe/Internet Company"
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "trevor batley" <ua-author-17071973@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p11@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap> <gap-bfcd7848cc-p11@usenetarchives.gap>`

```

Or,

if you ask any of your Assembler colleagues you could store your Gregorian
dates in 2 or 3 bytes using the following bitmap
(YYYYYYYYYYYYYYYMMMMDDDDD).

To use it in COBOL:

01 DATE-COMP PIC S9(9) USAGE COMP.
01 FILLER REDEFINES DATE-COMP.
05 FILLER PIC X.
05 DATE-BIN PIC X(3).
or
05 FILLER PIC X(2).
05 DATE-BIN PIC X(2).

COMPUTE DATE-COMP = (YYYY*512) + (MM*32) + (DD)

Unstringing can be done via:

DIVIDE DATE-COMP BY 512 GIVING YYYY REMAINDER MONTHS-DAYS.
DIVIDE MONTHS-DAYS BY 32 GIVING MONTHS REMAINDER DAYS.

If you are only using 2 bytes the maximum value is 127 which can be
converted by:

ADD 1900 TO YYYY.

Depends on the site standards being applied.

Jim Van Sickle wrote in article <337··.@i··.net>...
› Kevin P Corkery wrote:
› stuff deleted...
…[42 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "ken winters" <ua-author-4863506@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p11@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap> <gap-bfcd7848cc-p11@usenetarchives.gap>`

```

Jim Van Sickle wrote:
› 
 
› 
› We are still left with the challenge of including a 4-digit year (in the
…[9 more quoted lines elided]…
› 
 
 
› --
› Jim Van Sickle   
› Manager, Operations and Tech Support
› United Retail Group. Inc.
› Rochelle Park, NJ

I agree that that would work, on a machine with 4-byte words. I used
something very similar, but trickier, to get a binary date field out of
the middle of a word about 20 years ago. That machine was a Burroughs
6500, which has a six byte word, if you're using EBCDIC, or an eight
byte
word, using BDC. (6 bytes times 8 bits = 8 bytes times 6 bits = 48 bits
to a word.)

This illustrates a hidden danger in y2k solutions: Fixing the y2k
problem,
within constraints needed to keep the project feasible, by creating non-
portable code. This in spite of the fact that COBOL was designed to
hide
low-level details and make programs _more_ portable.

Now I wonder: How many of those 48-bit word Burroughs machines are still
out there?

------------------------------------------------------------------------
 Ken Winters  kwi··.@fo··d.com   Auto/Quantum Mechanic (amateur status)
 CAD/CAM/PIM Systems Department     Phone (work)  (313) 59-43074
 PIM Architecture and Interfaces          (home)  (810) 546-1070
------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 7)_

- **From:** "myaddress..." <ua-author-17071638@usenetarchives.gap>
- **Date:** 1997-05-08T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p14@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap> <gap-bfcd7848cc-p11@usenetarchives.gap> <gap-bfcd7848cc-p14@usenetarchives.gap>`

```

On Wed, 07 May 1997 19:20:58 -0400, Ken Winters
wrote:



› That machine was a Burroughs
› 6500, which has a six byte word, if you're using EBCDIC, or an eight
› byte
› word, using BDC.  (6 bytes times 8 bits = 8 bytes times 6 bits = 48 bits
› to a word.)




› Now I wonder: How many of those 48-bit word Burroughs machines are still
› out there?



Haven't seen a 6500 since I saw one roll out the door and a 7800 roll
in over 10 years ago.

Boris
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p9@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap>`

```

In <01bc5a65$1a0d3080$95609fcf@corkery1>, "Kevin P Corkery" writes:
› 
› 
…[28 more quoted lines elided]…
› 

The Federal government is full of data like this. Signless,
packed decimal coded dates. There are millions of *reels* of
tape with this format data on it all around Washington DC.

It fills warehouses, storage bunkers, maybe even the hollowed
out mountain they show on the X-Files, not just a few
tens of thousand slots in a couple dozen robot tape libraries.

I'm saving your code fragments, when the real screaming starts in
a few hundred days, I'll be able to charge a fortune for those
few lines.

Cory Hamasaki http://www.kiyoinc.com
HHResearch Co. OS/2 Webstore & Newsletter
REDWOOD
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "g..." <ua-author-1935339@usenetarchives.gap>
- **Date:** 1997-05-10T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p16@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap> <gap-bfcd7848cc-p16@usenetarchives.gap>`

```

cory hamasaki (kiy··.@i··.net) wrote:

: The Federal government is full of data like this. Signless,
: packed decimal coded dates. There are millions of *reels* of
: tape with this format data on it all around Washington DC.

It doesn't surprise me a bit. After all, the Federal government's use of
computers predates the IBM-360, which intoduced the packed decimal format
as we know and it today. The kids of today
who think the computing world began with the PC call the format "BCD",
but there are a few of us left who know what BCD really is, and possibly
one or two who might recognize BCL.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-05-09T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p9@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p9@usenetarchives.gap>`

```

In article <01bc5a65$1a0d3080$95609fcf@corkery1>,
"Kevin P Corkery" wrote:
› 
› 01  DATE-WORK.
…[5 more quoted lines elided]…
› MOVE DATE-MOVE TO 

I don't think you tested this before posting it. To shift left one,
multiply by ten, not by a hundred.

However, one of the great advantages of CoBOL is that unlike other
languages you don't have to multiply to get a decimal shift.

05 WS-DATE-9 PIC 9(7).
05 FILLER REDEFINES WS-DATE-9.
10 WS-DATE-X.
15 WS-DATE-9-YY PIC 9(2).
15 WS-DATE-9-MM PIC 9(2).
15 WS-DATE-9-DD PIC 9(2).
10 FILLER PIC 9(1) VALUE ZERO.

MOVE WS-DATE-9 TO DATE-FULL.

This compiles to a single pack instruction or the platform equivalent.
Note that if your entire sort key is numeric, as many are even today, you
can line up your sort key fields in display and pack them all with a
single instruction -- up to 17 characters in CoBOL and up to 30
characters in assembler.

If your sort key is longer than that, pack from left to right in the
field. The extra byte from the first pack does no harm because it is
immediately overlaid by the second pack, and so on. Which leads to the
second insight, that it is not necessary to pack in working storage and
then move the results to the buffer. You can pack directly into the
buffer, as long as you do it before loading the field that follows.

At a bank or insurance company you can knock one or two hours off the
wallclock time of every sort with simple techniques like this.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambride, MA 02138
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "g..." <ua-author-1935339@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p8@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap>`

```

Jim Van Sickle (ji··.@i··.net) wrote:
: This struck me as an interesting challenge: a date packed into 3 bytes?
: I'll assume you're talking about a 'Julian' date (YYDDD) stored as a
: COBOL usage COMP-3 data element ('yydddS'x). Actually, you could
: (somewhat) easily convert this date field to include the century, er,
: 4-digit year, by storing it as Binary (usage COMP) and truncating the
: high-order byte (via redefines), and moving the remaining 3 bytes to a
: PIC X(3) field (and visa-versa).

Nope, in this case it was (is, actually) six digits packed into three
bytes: X'YYMMDD'. No sign, no zone, no overhead. The original
application was written in assembly and its successor in C, but we do
have the need to process the data through some COBOL applications. As
someone else suggested, it's typically done with redefined work areas
containing the date multiplied by 10. Some programs just need to compare
dates, though, and that works just fine by declaring them PIC X(3).
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "mike rochford" <ua-author-959623@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p19@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p19@usenetarchives.gap>`

```

Gary L. Smith wrote:
› 
› Jim Van Sickle (ji··.@i··.net) wrote:
› : This struck me as an interesting challenge: a date packed into 3 bytes?
 
› 
› Nope, in this case it was (is, actually) six digits packed into three
…[10 more quoted lines elided]…
› Columbus, Ohio                 Gar··.@oc··c.org

Having read through all the crap on this page, I can only assume that
you are all working with compilers that do not support the COMP-6 usage
on a packed data field.

Quoting from the AcuCobol manual - The format of a comp-6 item is
identical to a comp-3 item except that it is unsigned and no space is
allocated for the sign. Thus there are two decimal digits per byte, and
the actual size of the item is arrived at by dividing its PICTURE size
by two and rounding up.

ie - a date of YYMMDD could be stored using a PIC 9(6) COMP-6 clause in
three bytes.

RM/Cobol and Micro Focus also allow support for COMP-6 data items.

MIKE.
Mike Rochford
-------------
EasiRun International
      
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
|  18 Lakeside Place                   PO Box 13226 | 
|  Benoni                              Northmead    |
…[3 more quoted lines elided]…
|  URL: http://www.easirun.co.za                    |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-07T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p20@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap> <gap-bfcd7848cc-p19@usenetarchives.gap> <gap-bfcd7848cc-p20@usenetarchives.gap>`

```

Mike Rochford wrote:
› 
› (clip clip clip)
…[6 more quoted lines elided]…
› 
Please please please forgive me for not stating this up-front, but for
the record, my point of reference is IBM MF COBOL. Furthermore, per IBM,
as of the current releases of IBM COBOL for MVS & VM Release 2 (Program
Number 5688-197), IBM VisualAge for COBOL for OS/2 Release 2 (Program
Number 5622-793), and IBM COBOL Set for AIX Release 1 (Program Number
5765-548), COMP-6 is recognized but is 'reserved for future
development'.

The horse is dead...I shall discontinue beating it :-)

Jim Van Sickle   
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "j. robert jones" <ua-author-17072955@usenetarchives.gap>
- **Date:** 1997-05-12T20:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p8@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p8@usenetarchives.gap>`

```

I have seen a lot of 3-byte dates used in HBO and Company's IBM
mainframe software.
The way they do it is that they use January 1, 1900 as the base, and
count the number of days before or after this date and store it in a 3
byte COMP-3 field. Most dates in master files are stored in this
manner. The sceme will work well into the 22nd century.
The downside is that these dates look really ugly in master files if you
are looking for a record in a file dump.
The upside is that it is really easy to determine number of days between
2 dates in different years.
Assembler subroutines are used to convert these types of dates to and
from many different formats.
They borrowed this concept of date storage from an ancient IBM system
called SHAS (Shared Hospital Accounting System). They packed dates into
2 bytes by using a binary field. This system broke down on September
19, 1989. A few software companies got caught by this one.

Jim Van Sickle wrote:
› 
› Gary L. Smith wrote:
…[23 more quoted lines elided]…
› Rochelle Park, NJ
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "ptrclark" <ua-author-621340@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```

In article Certified Chilehead writes:

› On 5 May 1997, Gary L. Smith wrote:
 
›› Certified Chilehead (ch··e@jos··t.com) wrote:
 
› [snip]
 
›  What do you suggest for dates which are packed 
›› into _three_ bytes.
 
› Never heard of any such way to pack a date. MMDDYY packs into  0MDY
›                                                               MDY+
› and thats 4 bytes leaving 1 nibble for the C.
› you of cource have to assume the second C

Just because you haven't heard of it doesn't mean it doesn't exist. Packing 6
digit dates into 3 bytes is very common in code that I have been exposed to.
Unsigned packed data types are very common in the non-IBM world.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "g..." <ua-author-1935339@usenetarchives.gap>
- **Date:** 1997-05-06T20:00:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```

Certified Chilehead (ch··.@jos··t.com) wrote:

: On 5 May 1997, Gary L. Smith wrote:

: > Believe me, it's not that simple. Some languages don't handle packed
: > decimal easily.

: The discussion was to RPG and COBOL which do convert easily

I didn't see anything indicating that the discussion was to be restricted
to those languages. Why should it be? Software is also written in PL/I
and C and FORTRAN, and is likely to use dates in any of those.

: > Even for those which do, conversion of the data may well
: > be a formidable task. Consider a store of two billion records, each
: > containing three dates. How long will it take to convert, and how will
: > you handle processing while the conversion is going on and both old and
: > new formats are present?
: Shouldnt take any longer than a backup and a restore.

We're talking many hundreds of reels of tape here, possibly many
thousands. Only a small part of the data store is disk-resident. Some
of it is stored off-site. The part that's disk-resident is online 7
days a week, 24 hours a day, with the exception of one half-hour of
system down-time.

: What do you suggest for dates which are packed
: > into _three_ bytes.

: Never heard of any such way to pack a date. MMDDYY packs into 0MDY
: MDY+
: and thats 4 bytes leaving 1 nibble for the C.
: you of cource have to assume the second C

There are possibly many things you haven't heard of. That doesn't stop
them from existing. Three bytes hold six digits very nicely -- today is
X'970507'. The application was designed for a system which had no
knowledge of IBM's packed decimal format.

: > Actually, given the current emphasis on international operations, the
: > MM/DD/CCYY format is seriously defective, even for human interaction.
: > The unambiguous CCYY-MM-DD format should be used, with whatever choice of
: > punctuation suits your organization.

: As programmers we will have to see how managment will react to this it is
: preferable but I dont think it will fly with the powers that be

Perhaps not. There are an awful lot of short-sighted managers who have no
awareness of the importance of international considerations in business.
Ten years from now, there will be a lot fewer of them, and of the
businesses they're now managing.
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "jce..." <ua-author-17072007@usenetarchives.gap>
- **Date:** 1997-05-13T20:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p4@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap>`

```

Peter Clark wrote:
› 
› In article  Certified Chilehead  writes:
…[17 more quoted lines elided]…
› Unsigned packed data types are very common in the non-IBM world.

And not that uncommon in the IBM-world either. All it takes is to scale
a COMP-3 value by a factor of 10 giving MM DD YY 0C, use REDEFINES to
overlay first 3 bytes with a 3-char field and move your three bytes as a
character field to destination field in a record. Reverse the process
if processing must be done on the date. Not as elegant as direct
support for unsigned packed data, but effective and actually used in
real production programs where external file space saving warranted the
extra complexity.

Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-05-16T20:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p25@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p2@usenetarchives.gap> <gap-bfcd7848cc-p4@usenetarchives.gap> <gap-bfcd7848cc-p25@usenetarchives.gap>`

```

jce··.@a··.org wrote in article <337··.@a··.org>...
› Peter Clark wrote:
›› In article
 
›› Certified Chilehead  writes:
››› On 5 May 1997, Gary L. Smith wrote:
…[25 more quoted lines elided]…
› extra complexity.

Another practice that I have seen in various forms is to store the Julian
date in a YYYDDD format where the YYY assumes a base year. For instance,
an insurance company that I worked for back in the early 70's (or should I
say 1970's for Y2K correctness?) used 1800 as their base year. Thus the
date 197120 would translate as 30 April 1997. On non-IBM mainframes this
can be saved in a 3-byte field where packing can be effected without saving
the sign. I have seen it saved as as pair of 2-byte fields as +YYY+DDD but
then we're back to four bytes again - still, it is shorter than YYYYMMDD.

On querying the use of a two-digit year on a client site back in around
1976, the response was "And what makes you think that the load of crap
you're writing will still be around in five years time, let alone
twenty-five?". I happen to know that it still is around... and it still is
a load of crap, not by programming but by specification.


Charles F Hankel, Freedom Bird Ltd

An opinion is only an opinion
and this opinion is mine.
```

#### ↳ Re: Date standardizing or patching?

- **From:** "paul" <ua-author-17071285@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p27@usenetarchives.gap>`
- **In-Reply-To:** `<5ig6lm$133$1@news1.i1.net>`
- **References:** `<5ig6lm$133$1@news1.i1.net>`

```

On Wed, 09 Apr 1997 13:44:28 GMT, tro··.@i··.net (Tim Oxler) growled:

› With the Y2K problem and the time pressure to fix the problems, what
› has been your shop or clients approach to fixing the dates?
…[9 more quoted lines elided]…
› existing date fields?  Or something in between?

Well, in the UK we never went on the MMDDYY thang in real life so it
never appeared in our code. And our company never used YYDDD so we've
only had MMDDYY and DDMMYY to worry about. Phew!

We're standardising on CCYYMMDD unpacked everywhere. We switched to
that standard for new code a year ago and we're slowly converting all
our code to match. The task of tracking date fields down has been made
simpler because all date fields historically contained "DAT" in their
name and any created in the last five years contain *YY *MM and *DD
sub-fields.

We've also standardised the definition of all date fields as follows:

02 xxx-CDATE PIC 9(8).
02 FILLER REDEFINES xxx-CDATE.
03 xxx-CC PIC 99.
03 xxx-DATE PIC 9(6).
03 FILLER REDEFINES xxx-DATE.
04 xxx-YY PIC 99.
04 xxx-MM PIC 99.
04 xxx-DD PIC 99.

This should stand us in good stead when we next convert to ten digit
dates in 9999AD ... although I hope to have retired by then.
```

##### ↳ ↳ Re: Date standardizing or patching?

- **From:** "xf..." <ua-author-3866152@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p27@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap>`

```

pa··l@the··o.ukx (Paul Oldham) wrote:

› Well, in the UK we never went on the MMDDYY thang in real life so it
› never appeared in our code. And our company never used YYDDD so we've
› only had MMDDYY and DDMMYY to worry about. Phew!
 
› We're standardising on CCYYMMDD unpacked everywhere. We switched to
› that standard for new code a year ago and we're slowly converting all
…[3 more quoted lines elided]…
› sub-fields.

As Paul rightly points out in the UK we use DDMMYY or even ( if we
planned ahead ) DDMMCCYY.

In term of usage on a file though , it all stems back to the days when
programmers used the shortest methods to achieve results rather than
the clearest.

CCYYMMDD should be the standard date because (a) is the only variety
that when sorted comes out in the correct order and (b) is readable
without any conversion.

Id be interested to hear why the US uses the format MMDDYY , I cant be
from an IT point of view as its pretty useless for sorting ( unless
you split the sort ).

Generally dates on files DDMMCCYY ( or the US equivelant MMDDYY ) are
there when the date is to be used for printing purposes rather than
used in any calculation. Its easier to move the field direct rather
than re-arrange it for printing.

Generally dates on files CCYYDDD are there when the date is to be used
in calculations rather than for printing. Its a damn sight easier to
work out the number of days between two dates using this method.

Of course , this doesnt hold true all the time. Inevitably you need to
use these dates for something other than their origional use , so you
get to see all sorts of routines that convert dates from one format to
the other.

As for tracking down dates , I know of one site in the UK who would
make you cry. The IT manager at this site thought of himself as a bit
of a programmer so did his own amendments. Bad enough I hear you cry?
Well it gets worse , this bloke was a lazy s-o-b and when he wanted to
add a field to a file , instead of doing it the usual way ( finding a
spare field or redundant one and renaming it , or increasing the file
size ) hed would take pot luck and pick out what was in his own
opinion the least used field on the file ( no checking , just a guess
that its not used ). He would then stick his own field in their
WITHOUT renaming the field. If you were lucky he would move it to WS
and have the real field name there , but most of the time he just used
the origional fieldname. Try amending code where you see a field name
INVOICE-NUMBER but in reality could contain a date , a surname , even
an amount!

All the best.
Kevin White

Email : kev··.@dia··x.com
Day Phone : 01536-402551 ext 3209
Phone/Fax : 01933-270322
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "mario alvarez" <ua-author-17072425@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p28@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap>`

```

Kevin White wrote:
› 
› pa··l@the··o.ukx (Paul Oldham) wrote:
…[12 more quoted lines elided]…
› an amount!

Shoot the bastard,,,,NOW!!!!!!!!!!!!!

Mario L. Alvarez           *****  	ANTI-SPAM notice  ***********
Systems Analyst            * remove ANTISPAM when replying          *
S.C. Department of Revenue *                                        * 
Columbia, S.C.             *  alv··.@app··c.us *
                           ******************************************
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "kk..." <ua-author-3129200@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p28@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap>`

```

On Wed, 09 Apr 1997 18:29:33 GMT, xf··.@dia··x.com (Kevin White)
wrote:

(snip the good stuff)

› CCYYMMDD should be the standard date because (a) is the only variety
› that when sorted comes out in the correct order and (b) is readable
…[5 more quoted lines elided]…
› 

Kev,
>From day one in school, we were taught to date our papers as
MM/DD/YY. My son is in first grade and they still teach it. Later
on, they'll teach them about gallons, inches, and yards! Possibly,
they'll discuss metrics for a day or so. There was something in the
local paper lately about how converting to the rest of the world would
help businesses but it was slammed as usual.

Cheers,
Kevin
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

- **From:** "ter..." <ua-author-3254988@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p28@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap>`

```

In <5ignd7$b.··.@soa··x.com>
xf··.@dia··x.com (Kevin White) wrote:



› Id be interested to hear why the US uses the format MMDDYY , I cant be
› from an IT point of view as its pretty useless for sorting ( unless
› you split the sort ).

My guess would be that in the US when we write a date in long form we
write in month day, year order (e.g. April 9, 1997). The mm/dd/yy form
(e.g. 04/09/97) is just a short form of that. How are dates writen in
long form in the UK?

I just looked at a picture of the original US Declaration of
Independence and the date on it is written "July 4, 1776" so we've
been writing dates in that order for over 220 years.

› Generally dates on files DDMMCCYY ( or the US equivelant MMDDYY ) are
› there when the date is to be used for printing purposes rather than
› used in any calculation. Its easier to move the field direct rather
› than re-arrange it for printing.

Actually, most systems I've worked kept the date in YYMMDD order
internally and reformatted the date for output to the user. One place
I worked went so far as to make it a company wide policy to put all
dates in YYMMDD format, even in hardcopy documents.

› Generally dates on files CCYYDDD are there when the date is to be used
› in calculations rather than for printing. Its a damn sight easier to
› work out the number of days between two dates using this method.

One system I've encounted used epoch dates internally. Dates were
recorded as a 32 bit signed binary number and was a count of days
since Jan. 1, 1901. Days between dates and day of the week
calculations were a snap.

› Of course , this doesnt hold true all the time. Inevitably you need to
› use these dates for something other than their origional use , so you
› get to see all sorts of routines that convert dates from one format to
› the other. 



› All the best.
› Kevin White

B&R
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 4)_

- **From:** "paul" <ua-author-17071285@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p31@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap> <gap-bfcd7848cc-p31@usenetarchives.gap>`

```

On Thu, 10 Apr 1997 02:05:44 GMT, ter··.@nig··l.net (Batz) growled:

› In <5ignd7$b.··.@soa··x.com> 
› xf··.@dia··x.com (Kevin White) wrote:
…[10 more quoted lines elided]…
› long form in the UK?

In my experience "9th April 1997" would be more normal when writing it
down, but you see it the other way too and both forms are used in
spoken english. I will certainly use "9th of April" and "April the
9th" interchangeably when speaking... although I wouldn't use "April
9th" or "April 9".
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 5)_

- **From:** "ter..." <ua-author-3254988@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p32@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap> <gap-bfcd7848cc-p31@usenetarchives.gap> <gap-bfcd7848cc-p32@usenetarchives.gap>`

```

In <334··.@new··o.uk>
pa··l@the··o.ukx (Paul Oldham) wrote:

› On Thu, 10 Apr 1997 02:05:44 GMT, ter··.@nig··l.net (Batz) growled:
 
›› In <5ignd7$b.··.@soa··x.com> 
›› xf··.@dia··x.com (Kevin White) wrote:
…[10 more quoted lines elided]…
›› long form in the UK?
 
› In my experience "9th April 1997" would be more normal when writing it
› down, but you see it the other way too and both forms are used in
› spoken english. I will certainly use "9th of April" and "April the
› 9th" interchangeably when speaking... although I wouldn't use "April
› 9th" or "April 9".

I wonder when and why the divergence occurred. Did we change, you
change or both?

As far as spoken dates go, just about every form is used, though the
the "April 9th" form is most common when reading a written date. When
not reading it from written text all forms seem to be used equally,
but there are certain to be regional diffeences.

B&R
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p33@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap> <gap-bfcd7848cc-p31@usenetarchives.gap> <gap-bfcd7848cc-p32@usenetarchives.gap> <gap-bfcd7848cc-p33@usenetarchives.gap>`

```

Batz wrote:
› 
› In <334··.@new··o.uk>
…[33 more quoted lines elided]…
› 
I prefer to hear people say April 9th. Because I find that I immediately
begin visualizing the callendar as soon as I hear the word April. Then I
zoom in on the 9th. The 9th of April causes a delay in visualization,
since there are 12 9ths per year.

I guess I have written too much assembler code over the years and just
can't help but save nanoseconds.
---
Wayne L. Beavers        mailto:way··.@bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"The Mainframe/Internet Company"
```

###### ↳ ↳ ↳ Re: Date standardizing or patching?

_(reply depth: 6)_

- **From:** "2nd bow" <ua-author-17073700@usenetarchives.gap>
- **Date:** 1997-04-15T20:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bfcd7848cc-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bfcd7848cc-p33@usenetarchives.gap>`
- **References:** `<5ig6lm$133$1@news1.i1.net> <gap-bfcd7848cc-p27@usenetarchives.gap> <gap-bfcd7848cc-p28@usenetarchives.gap> <gap-bfcd7848cc-p31@usenetarchives.gap> <gap-bfcd7848cc-p32@usenetarchives.gap> <gap-bfcd7848cc-p33@usenetarchives.gap>`

```



Batz wrote in article <5ij0bf$met$1.··.@new··1.net>...
››› 
›››› Id be interested to hear why the US uses the format MMDDYY , I cant be
…[23 more quoted lines elided]…
›  

The US changed (were they isolated from the rest of the world a couple of
hundred years ago?) the way they used dates probably about the same time
they changed the way they spelt, gaol (jail) and colour (color) and many
other things. ( I believe the Brits were around first kids)

This adds up to much fun for us in Australia, we of course have always
adopted the UK usage, being a member of the commonwealth and speaking
"English", but because of the huge influence the US has over TV and
therefore communication in this country we notice people picking up nasty
language usage habits (especially in pronounciation).

Language of course changes over time and any place that's separated will
develope differently. I've travelled to most states in Australia (six of
them) and do you think any state used the same language for a glass of
beer? I got middies, pots, schooners, pints, half pints, and a couple more,
and that was in Queensland and NSW only. I speak to my old man about
getting a case of beer (box of 24) and he doesn't know what I'm talking
about, their generation call it a carton of beer. What's this got to do
with COBOL I don't know, but I suddenly feel like a beer, excuse me people.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
