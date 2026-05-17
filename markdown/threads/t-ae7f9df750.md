[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ALPHABETIC TO NUMERIC CONVERSION

_5 messages · 4 participants · 1998-06_

---

### ALPHABETIC TO NUMERIC CONVERSION

- **From:** "logana..." <ua-author-17075089@usenetarchives.gap>
- **Date:** 1998-06-09T06:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6lj1sd$3c7$1@nnrp1.dejanews.com>`

```

I am fairly new to COBOL programming ( i'm learning through a corespondence
course) and have a problem. Is there any way to easily convert alphabetic
charachters to numeric values (possibly on the basic of the ASCII value) The
only way i can think of doing this is to use something along the lines of a
long winded evaluate statement or possibly searching a table with all the
charachters and equivilant values? Alex Logan LOG··.@my-··s.com

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: ALPHABETIC TO NUMERIC CONVERSION

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-06-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ae7f9df750-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6lj1sd$3c7$1@nnrp1.dejanews.com>`
- **References:** `<6lj1sd$3c7$1@nnrp1.dejanews.com>`

```

The easiest way is to redefine them, but the code will be computer/OS
dependant. For example, find the usage COMP-1 is a 16 bit twos
compliment number on a PC. So the following will work fine.

01 THIS-IS-ASCII.
02 THIS-IS-ZERO PICTURE X.
02 CHARACTER-DATA PICTURE X.
01 THIS-IS-BINARY redefines THIS-IS-ASCII.
02 THIS-IS-16-BITS PICTURE 99 USAGE COMP-1.
01 THIS-IS-NUMERIC-ASCII-VALUE picture 99.

move zero to this-is-binary. (to set high order to zero).
move "A" to character-data. (to set low order in binary).
move this-is-16-bits to this-is-numeric-ascii-value. (convert
binary to ASCII)
```

##### ↳ ↳ Re: ALPHABETIC TO NUMERIC CONVERSION

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1998-06-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ae7f9df750-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ae7f9df750-p2@usenetarchives.gap>`
- **References:** `<6lj1sd$3c7$1@nnrp1.dejanews.com> <gap-ae7f9df750-p2@usenetarchives.gap>`

```

Donald Tees wrote:
› 
› The easiest way is to redefine them, but the code will be computer/OS
…[13 more quoted lines elided]…
› binary to ASCII)

Surely this presupposes that the operating platform is ASCII-oriented
because you would get different results on an EBCDIC system such as most
mainframes? The use of intrinsic functions seems to be the better
option but, that said, they are not necessarily available on all
compilers that are in use out there.

Charles F Hankel, Wirral, UK
Freelance Systems Professional
Surfing through this life on the Y2K wave
-----------------------------------------
Antispam: take away my breakfast to reply
```

###### ↳ ↳ ↳ Re: ALPHABETIC TO NUMERIC CONVERSION

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-06-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ae7f9df750-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ae7f9df750-p3@usenetarchives.gap>`
- **References:** `<6lj1sd$3c7$1@nnrp1.dejanews.com> <gap-ae7f9df750-p2@usenetarchives.gap> <gap-ae7f9df750-p3@usenetarchives.gap>`

```

› Surely this presupposes that the operating platform is ASCII-oriented

The question was "how do you get the ASCII value ...", so yes I made the
supposition that it was an ASCII computer. I also stated that it was
platform
specific.
```

#### ↳ Re: ALPHABETIC TO NUMERIC CONVERSION

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-06-08T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ae7f9df750-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6lj1sd$3c7$1@nnrp1.dejanews.com>`
- **References:** `<6lj1sd$3c7$1@nnrp1.dejanews.com>`

```

› I am fairly new to COBOL programming ( i'm learning through a corespondence
› course) and have a problem. Is there any way to easily convert alphabetic
› charachters to numeric values (possibly on the basic of the ASCII value)

The following method will work (but is slightly non-portable, i.e. may have
to
be adjusted depending on the compiler):

01 CHAR-CONVERSION.
02 THE-CHAR-VALUE PIC S9(4) COMP-4 VALUE ZERO.
02 FILLER REDEFINES THE-CHAR-VALUE.
03 FILLER PIC X.
03 THE-CHAR PIC X.


To use it:

MOVE "A" TO THE-CHAR
DISPLAY THE-CHAR-VALUE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
