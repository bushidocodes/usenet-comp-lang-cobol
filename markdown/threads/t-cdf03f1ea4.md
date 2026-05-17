[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ASCII help

_8 messages · 6 participants · 1996-10_

---

### ASCII help

- **From:** "william black" <ua-author-22175@usenetarchives.gap>
- **Date:** 1996-10-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<325392AB.3C92@ihug.co.nz>`

```

I want to get a character from the user and then determene what charater
it is by the ascii code of the at character, can this be done in COBOL?
I want do this it enable the enter key as a character. Which I know has
an ascii code of 13 but I don't know how to encode this in COBOL.

William
wjc··.@ihu··o.nz
2nd Year Massey(Albany)Uni. Student
Bsc (Infomation systems, Computer Science)
```

#### ↳ Re: ASCII help

- **From:** "xyju..." <ua-author-13465596@usenetarchives.gap>
- **Date:** 1996-10-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<325392AB.3C92@ihug.co.nz>`
- **References:** `<325392AB.3C92@ihug.co.nz>`

```


In article <325··.@ihu··o.nz>
William Black wrote:

› I want to get a character from the user and then determene what charater
› it is by the ascii code of the at character, can this be done in COBOL? 
› I want do this it enable the enter key as a character. Which I know has
› an ascii code of 13 but I don't know how to encode this in COBOL.

You have to do something like:

05 INPUT-CHAR PIC X(01).
05 CHECK-CHAR REDEFINES INPUT-CHAR PIC 9(02) COMP.
88 ENTER-KEY VALUE 13.


IF ENTER-KEY
DO SOMETHING
END-IF.

Basically you have to redefine the char and check it's binary value. Make
sure the comp field is the same size as the char you are redefining.
```

##### ↳ ↳ Re: ASCII help

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-10-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p2@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap>`

```

XYj··.@g··.com wrote:
› 
›› I want to get a character from the user and then determene what charater
…[15 more quoted lines elided]…
› sure the comp field is the same size as the char you are redefining.

This method is not portable. What is portable is to use the intrinsic
function ORD. It will return the ordinal of the character in the
program's collating sequence. If you are using ASCII and are looking
for a code of 13, check for 14 (ordinal numbers start at 1, not 0).
If you have a small number of characters that you are looking for you
can define them with SYMBOLIC CHARACTERS in SPECIAL-NAMES and test
against those, probably by using EVALUATE. Actually, you could use
EVALUATE with ORD as well. No indication of what COBOL was being used
was given, so a specific method cannot be furnished.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: ASCII help

- **From:** "xyju..." <ua-author-13465596@usenetarchives.gap>
- **Date:** 1996-10-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p3@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap> <gap-cdf03f1ea4-p3@usenetarchives.gap>`

```


In article <325··.@tan··m.com>
Don Nelson wrote:

› This method is not portable.  What is portable is to use the intrinsic 
› function ORD.  It will return the ordinal of the character in the 
…[7 more quoted lines elided]…
› 

This is interesting. I have never heard of this intrisic ORD function and
none of our three compiler manuals make mention of it. In what COBOL
standard did this arrive?
```

###### ↳ ↳ ↳ Re: ASCII help

_(reply depth: 4)_

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p4@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap> <gap-cdf03f1ea4-p3@usenetarchives.gap> <gap-cdf03f1ea4-p4@usenetarchives.gap>`

```

XYj··.@g··.com () wrote:


› In article <325··.@tan··m.com>
› Don Nelson wrote:
 
›› This method is not portable.  What is portable is to use the intrinsic 
›› function ORD.  It will return the ordinal of the character in the 
…[7 more quoted lines elided]…
›› 
 
› This is interesting.  I have never heard of this intrisic ORD function and 
› none of our three compiler manuals make mention of it.  In what COBOL 
› standard did this arrive?


I guess the answer to the answer is even less portable.

JR

and stir with a Runcible spoon...
```

###### ↳ ↳ ↳ Re: ASCII help

_(reply depth: 4)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p4@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap> <gap-cdf03f1ea4-p3@usenetarchives.gap> <gap-cdf03f1ea4-p4@usenetarchives.gap>`

```

XYj··.@g··.com wrote:
› This is interesting. I have never heard of this intrisic ORD function and
› none of our three compiler manuals make mention of it. In what COBOL
› standard did this arrive?

This is part of the intrinsic function amendment to the 1985 COBOL
standard. The amendment was passed in 1989. COBOL II does not
include intrinsic functions, but almost every other major compiler in
use today does include them.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: ASCII help

_(reply depth: 4)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-10-08T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p4@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap> <gap-cdf03f1ea4-p3@usenetarchives.gap> <gap-cdf03f1ea4-p4@usenetarchives.gap>`

```

XYj··.@g··.com () wrote:

› This is interesting. I have never heard of this intrisic ORD function and
› none of our three compiler manuals make mention of it. In what COBOL
› standard did this arrive?

According to "Advanced ANSI COBOL With Structured Programming" by Gary
DeWard Brown (ISBN 0-471-54786-7):

"The intrinsic functions are a part of COBOL 85, as revised in 1989.
They are supported in Microsoft/Micro Focus COBOL, but as of this
writing have not yet been implememted in VS COBOL II."

Note: IBM now supports intrinsic functions in "COBOL/370" and "COBOL
for MVS & VM" compilers. Check your compiler for one of these types.

"Functions are written in the form:

FUNCTION function-name(arguments)

For example, the function named FACTORIAL computes the factorial of an
integer:

COMPUTE T-VAL = FUNCTION FACTORIAL(6)

The function computes the factorial of 6 and returns the value, 720,
which is then stored in T-VAL."

Hope this Helps
Boyce Williams
```

##### ↳ ↳ Re: ASCII help

- **From:** "jya..." <ua-author-17086590@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf03f1ea4-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cdf03f1ea4-p2@usenetarchives.gap>`
- **References:** `<325392AB.3C92@ihug.co.nz> <gap-cdf03f1ea4-p2@usenetarchives.gap>`

```

: >>William Black wrote:
: >>I want to get a character from the user and then determene what charater
: >>it is by the ascii code of the at character, can this be done in COBOL?
: >>I want do this it enable the enter key as a character. Which I know has
: >>an ascii code of 13 but I don't know how to encode this in COBOL.

: XYj··.@g··.com wrote:
: You have to do something like:

: 05 INPUT-CHAR PIC X(01).
: 05 CHECK-CHAR REDEFINES INPUT-CHAR PIC 9(02) COMP.
: 88 ENTER-KEY VALUE 13.

(snip)
---------------------------------------------------

Caution. The 'USAGE IS COMP' operand can cause problems unless you
are familiar with your compiler's generated number of bytes.
IBM compilers usually generate 2 bytes when 2 digits are
defined. In this case the example will be OK if the first
statement is defined as X(02) and CHECK-CHAR is defined
as 2 or 3 digits.

At least one other compiler doesn't even generate COMP
correctly. COBOL650 requires you to specify COMP-0 to gen-
erate pure binary (and in that case the maximum value in
the item is 32766). Using COMP-0 in this compiler should
work all right for this purpose.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
