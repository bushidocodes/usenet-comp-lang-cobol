[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL typedef keyword

_6 messages · 6 participants · 1996-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL typedef keyword

- **From:** "avital nahon" <ua-author-17086557@usenetarchives.gap>
- **Date:** 1996-06-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```


Hi

If I use MF COBOL's typedef keyword (oocobol version 3.3) The compiler
complains that the item is not unique:

***************************************
DATA DIVISION.

01 TYPE1 TYPEDEF.
02 ITEM1 PIC X(10).
02 ITEM2 PIC X(10).

01 VAR1 TYPE1.

PROCEDURE DIVISION.

DISPLAY ITEM1.

EXIT.
***************************************

Is it a bug or it meant to function this way ?

Avital
```

#### ↳ Re: MF COBOL typedef keyword

- **From:** "joan colley" <ua-author-15559010@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdb2b6f202-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`
- **References:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```

Avital Nahon wrote:
› 
› Hi
…[22 more quoted lines elided]…
› Avital


Hi there,

If you use the h2cpy program to convert a c include file (say type.h) to
a cobol file you will see the syntax for typedef.

Joan.
```

#### ↳ Re: MF COBOL typedef keyword

- **From:** "strl" <ua-author-2334088@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdb2b6f202-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`
- **References:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```

It is a bug. The program should compile without any errors.
There is a workaround however. You can do

DISPLAY ITEM1 OF VAR1.

When you define more groups of USAGE TYPE1, then you will have to
use qualification anyway.

I thought we fixed this problem in our v4.0 product for the latest
update disc. I've descovered MOVE ITEM1 TO SOMETHING-ELSE now works
but not DISPLAY ITEM1. Weird! Consider it passed on to the compiler
bods.

Regards,
Steve.
```

#### ↳ Re: MF COBOL typedef keyword

- **From:** "h..." <ua-author-509909@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdb2b6f202-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`
- **References:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```

Assuming that typedef stands for "type definition" (that is,
assuming that it's basically borrowed from C), it is probably meant
to work this way. You should be allowed to declare and use several
variables of any one type you declared, so you probably should tell
the compiler which one's ITEM1 you are talking about. The required
syntax might read something like DISPLAY ITEM1 OF VAR1, although I
don't know for sure as I haven't seen type definitions in Cobol
yet.

(When I want to save the labor of typing in identical sub-items of
several variables, I currently have to resort to macros that mimic
type definitions, as in:

replace ==TDate.== by ==.
05 Year pic 9(4).
05 Month pic 9(2).
05 TheDay pic 9(2).==.

01 OrderDate TDate.
01 ShippingDate TDate.
01 BillingDate TDate.

Typedef's should allow you to do the same thing more cleanly.)

In article <01bb5054.8a571b60$926ccbc7@nt-avital>, "Avital Nahon"
(avi··.@adp··o.il) writes: >
› If I use MF COBOL's typedef keyword (oocobol version 3.3) The compiler
› complains that the item is not unique:
…[17 more quoted lines elided]…
› Is it a bug or it meant to function this way ?
```

#### ↳ Re: MF COBOL typedef keyword

- **From:** "skyw..." <ua-author-17071604@usenetarchives.gap>
- **Date:** 1996-06-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdb2b6f202-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`
- **References:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```

"Avital Nahon" wrote:

You have to qualify just like what we do in languages like "C".
Because typedef is just a template and there is no real memory
associated with that.
Hope it helps.



› Hi
 
› If I use MF COBOL's typedef keyword (oocobol version 3.3) The compiler
› complains that the item is not unique:
 
› ***************************************
›       DATA DIVISION.
 
›       01 TYPE1 TYPEDEF.
›        02 ITEM1 PIC X(10).
›        02 ITEM2 PIC X(10).
 
›       01 VAR1 TYPE1.
 
›       PROCEDURE DIVISION.
 
›       DISPLAY ITEM1.
 
›       EXIT.
› ***************************************
 
› Is it a bug or it meant to function this way ?
 
› Avital

Disclaimer : If my employer shares my views,
I will be surprised
```

#### ↳ Re: MF COBOL typedef keyword

- **From:** "mike.r..." <ua-author-17086912@usenetarchives.gap>
- **Date:** 1996-06-05T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdb2b6f202-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`
- **References:** `<01bb5054.8a571b60$926ccbc7@nt-avital>`

```





AN>Hi

AN>If I use MF COBOL's typedef keyword (oocobol version 3.3) The
AN>compiler complains that the item is not unique:

AN>***************************************
AN> DATA DIVISION.

AN> 01 TYPE1 TYPEDEF.
AN> 02 ITEM1 PIC X(10).
AN> 02 ITEM2 PIC X(10).

AN> 01 VAR1 TYPE1.

AN> PROCEDURE DIVISION.

AN> DISPLAY ITEM1.

AN> EXIT.
AN>***************************************

AN>Is it a bug or it meant to function this way ?

AN>Avital



Shalom Avital...

In this case you defined 'TYPE1' twice. Each data-name in DATA DIVISION
MUST be unique or else...flaged. It has been some years since I used MF
COBOL compiler, but I believe that any compiler of good nature will flag
it.

take care..Mike..
---
魹ｽ CMPQwk #1.42魹ｽ UNREGISTERED EVALUATION COPY
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
