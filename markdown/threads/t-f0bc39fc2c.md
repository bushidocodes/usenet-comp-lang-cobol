[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Old COBOL question - forwarded

_9 messages · 8 participants · 1997-06_

---

### Old COBOL question - forwarded

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5n6puq$2joq@mercury.vcu.edu>`

```

I'm forwarding this post in the interest of furthering discussion:

We are attempting to get everyone to move to COBOL/370 (AD/CYCLE,
whatever you
want to call it). We currently have 3 versions of COBOL available to
everyone
(VS-COBOL, COBOL-II and COBOL/370).

A user trying to recompile his program under COBOL/370 can't get the
following
statement to compile:

05 WS-PCT-CK PIC 99.99.
88 VALID-X-PCT VALUES 03.00 THRU 06.50.
88 VALID-E-PCT VALUES 01.50 THRU 04.50.
88 VALID-M-PCT VALUES 00.00 THRU 03.00.

Of all the text I have searched, never had I seen an example of a
decimal in the
PICTURE clause itself, just the VALUE. A "V" was always used to
denote the
"assumed decimal position".

The error he gets is "VALUE CLAUSE LITERAL DOES NOT CONFORM TO
PICTURE. CLAUSE
IGNORED" on the 88 statements.

Did I miss something or am I right that this statement is invalid and
should be
PIC 99V99 and he has simply slipped through a "bug" ???



Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

#### ↳ Re: Old COBOL question - forwarded

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5n6puq$2joq@mercury.vcu.edu>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu>`

```



Boyce G. Williams, Jr. wrote in article
<5n6puq$2j··.@mer··u.edu>...
› I'm forwarding this post in the interest of furthering discussion:
› 
…[14 more quoted lines elided]…
› 


I'm taking a stab in the dark here, but try changing the 99.99 to 99V99 and
see what happens.

I've never seen the "thru" values used in the 88 levels before, that too
could cause a problem if it is an extension that is no longer supported.
Anyone else use/see these thru values on 88 levels before?
```

##### ↳ ↳ Re: Old COBOL question - forwarded

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0bc39fc2c-p2@usenetarchives.gap>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu> <gap-f0bc39fc2c-p2@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› 
…[11 more quoted lines elided]…
› see what happens.

The statement is illegal. To be legal the values would have to be
nonnumeric literals or the 99.99 would have to be 99V99. I'm amazed
that it compiled correctly on any implementation.

› I've never seen the "thru" values used in the 88 levels before, that too
› could cause a problem if it is an extension that is no longer supported.
› Anyone else use/see these thru values on 88 levels before?

THRU is part of the standard and is supported in every compiler I have
ever heard of. It can be very handy (and very confusing when there
are overlapping ranges).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Old COBOL question - forwarded

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5n6puq$2joq@mercury.vcu.edu>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu>`

```

This is being forward in the interest of furthering discussion:

Return-path:
Date: Thu, 05 Jun 1997 14:17:09 -0400
From: Thane Hubbell
Subject: Re: Old COBOL question - forwarded
To: bow··.@Gem··U.EDU
Reply-to: red··.@i··.net
X-MSMail-Priority: Normal



Boyce G. Williams, Jr. wrote in article
<5n6puq$2j··.@mer··u.edu>...
› I'm forwarding this post in the interest of furthering discussion:
› 
…[14 more quoted lines elided]…
› 


I'm taking a stab in the dark here, but try changing the 99.99 to
99V99 and
see what happens.

I've never seen the "thru" values used in the 88 levels before, that
too
could cause a problem if it is an extension that is no longer
supported.
Anyone else use/see these thru values on 88 levels before?


Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

##### ↳ ↳ Re: Old COBOL question - forwarded

- **From:** "bill wagner" <ua-author-1833025@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0bc39fc2c-p4@usenetarchives.gap>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu> <gap-f0bc39fc2c-p4@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
› This is being forward in the interest of furthering discussion:
…[40 more quoted lines elided]…
› 
I've used thru values on 88 levels on different versions of IBM Cobol
for 20 years. They even work with PIC X fields. I am unable to check,
but I expect (hope?) that they'll work when we move onto Cobol/VSE later
this year.
Thanks, Bill Wagner.

Bill Wagner
wcw··.@ui··c.edu
University of Illinois  These are my opinions and my opinions only!!!!!!
```

##### ↳ ↳ Re: Old COBOL question - forwarded

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0bc39fc2c-p4@usenetarchives.gap>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu> <gap-f0bc39fc2c-p4@usenetarchives.gap>`

```



Boyce G. Williams, Jr. wrote in article
<5n78kr$2r··.@mer··u.edu>...
› This is being forward in the interest of furthering discussion:
› I've never seen the "thru" values used in the 88 levels before, that
…[7 more quoted lines elided]…
› 
Yep ... use them all the time (at least on COB74 based compilers) ... but
you need to be careful on how you use them on alphanumeric items 'cause you
can get things responding "true" when they shouldn't, remember all items in
the collating sequence between your range are considered true ... If you
look at the IBM S/390 EBCDIC collating sequence you'll see that 'A' THRU
'Z' can include some unwanted hex values.
```

##### ↳ ↳ Re: Old COBOL question - forwarded

- **From:** "charles goodman" <ua-author-901347@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f0bc39fc2c-p4@usenetarchives.gap>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu> <gap-f0bc39fc2c-p4@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:

›› 
››     05  WS-PCT-CK                 PIC 99.99.
…[8 more quoted lines elided]…
› 

Changing the picture clause will change how the program works. Since
the picture 99.99 is numeric edited, I would try changing the 88 values
making them non-numeric:

05 WS-PCT-CK PIC 99.99.
88 VALID-X-PCT VALUES "03.00" THRU "06.50".
88 VALID-E-PCT VALUES "01.50" THRU "04.50".
88 VALID-M-PCT VALUES "00.00" THRU "03.00".

Charlie Goodman
```

#### ↳ Re: Old COBOL question - forwarded

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-06-04T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5n6puq$2joq@mercury.vcu.edu>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu>`

```

The value clause on an 88 level must conform to the same rules as the value
clause associated with a PICture'd element. Thus, if the PIC is 99V99,
then the value clause should be a numeric field such as 03.50. But if the
PIC is 99.99 then this is a numeric editted field which has many of the
same attributes as an alphanumeric field, so a value of "03.50" is
acceptable [note this is a 5 position field, not four positions]. Since
03.50 is a numeric value, it can only be used as a value with a numeric
field, not an alphanumeric or numeric-editted field.
```

#### ↳ Re: Old COBOL question - forwarded

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f0bc39fc2c-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5n6puq$2joq@mercury.vcu.edu>`
- **References:** `<5n6puq$2joq@mercury.vcu.edu>`

```

In article <5n6puq$2j··.@mer··u.edu>,
bow··.@gem··u.edu (Boyce G. Williams, Jr.) wrote:
› 
› A user trying to recompile his program under COBOL/370 can't get the
…[8 more quoted lines elided]…
› CLAUSE IGNORED" on the 88 statements.

When the VALUE clause literal does not conform to the PICTURE, you can
change the VALUE clause literal to match the PICTURE, like this:

05 WS-PCT-CK PIC 99.99.
88 VALID-X-PCT VALUES "03.00" THRU "06.50".
88 VALID-E-PCT VALUES "01.50" THRU "04.50".
88 VALID-M-PCT VALUES "00.00" THRU "03.00".

or you can change the PICTURE to match the VALUE clause literal, like
this:

05 WS-PCT-CK PIC 99V99.
88 VALID-X-PCT VALUES 03.00 THRU 06.50.
88 VALID-E-PCT VALUES 01.50 THRU 04.50.
88 VALID-M-PCT VALUES 00.00 THRU 03.00.

The PICTURE determines whether the elementary item is numeric or numeric
edited, which in turn determines what kind of comparison the compiler
will emit. If you change the VALUE clause literal to match the PICTURE,
the item is five bytes numeric edited, and you are requesting the
compiler to emit a character comparison such as CLC. If you change the
PICTURE to match the VALUE clause literal, the item is four bytes numeric
and you are requesting the compiler to emit a numeric comparison such as
PACK, CP.

In general, a numeric comparison is more expensive than a character
comparison, because it does more. However, if this variable is the
result of a computation as the name implies, it should not have USAGE
DISPLAY, and if it is used for percentages as the name implies, it should
have room enough for 100.00% just in case. One of the following would be
preferable, depending on the platform and on the rest of the program: PIC
99V99 COMP; COMP-1; COMP-2; PIC 999V99 COMP-3; or PIC 99V99 COMP-5. (PIC
999V99 COMP or PIC 999V99 COMP-5 would probably not be an improvement.)


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
