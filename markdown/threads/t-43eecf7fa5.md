[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I'm confused about USAGE and internal storage

_9 messages · 9 participants · 1997-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### I'm confused about USAGE and internal storage

- **From:** "tzadik vanderhoof" <ua-author-27911@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

I'm a bit confused about a few things in COBOL...

1) What are all these USAGEs? I know COMP-3 is packed decimal (BCD) and
DISPLAY is character (EBCDIC) form but what is COMP, COMP-1, and COMP-2
(COMP-4?) ? Are any of these floating point or binary?

2) Where is the sign stored in a USAGE IS DISPLAY data? There seems to be
no place for it, if, as my book says, PIC S999 uses 3 characters.

3) How do you read in a signed number from a file? Again, a similar
problem to the above question...there's no room for it. If you're reading
into a field that is PIC S999, then you will only read 3 characters, all
numeric...no room for a minus sign.

Sorry if my questions are too basic...but my book is quite unclear about
the finer points of how the data is actually stored in the computer. Some
programmers may claim that you don't have to know that, but I disagree...I
think much more clearly when I can picture in my mind exactly what is going
on in memory...I've always claimed that every programmer should have some
assembler experience for just that reason.
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

Tzadik Vanderhoof wrote:
› 
› I'm a bit confused about a few things in COBOL...
…[3 more quoted lines elided]…
› (COMP-4?) ?  Are any of these floating point or binary?

IBM packed decimal is not the same as true BCD. A true BCD number would
always have one decimal digit in each nybble (4 bits), and IBM packed decimal
always uses the rightmost nybble for sign (F is unsigned postive, C is signed
positive, and D is negative). Therefore a string of bytes containing an IBM
packed decimal number always has an odd number of decimal digits, and the
same string of bytes containing a true BCD number would always have an even
number of decimal digits.

IBM COMP or COMPUTATIONAL USAGE is fixed-point binary. Apparently COMP-4 is
also binary.

COMP-1 should be single-precision floating point. COMP-2 should be
double-precision floating point. I had it in school 17 years ago, but never
used it in the business world. I can't remember if the mantissa is binary
or BCD, but I'm pretty sure the exponent is binary.

›
› 2) Where is the sign stored in a USAGE IS DISPLAY data? There seems to be
› no place for it, if, as my book says, PIC S999 uses 3 characters.

The sign (F, C, or D) is stored in the left nybble of the rightmost byte:

Unsigned 123 = X'F1F2F3' or C'123'
Signed +123 = X'F1F2C3' or C'12C'
Signed -123 = X'F1F2D3' or C'12L'

› 
› 3) How do you read in a signed number from a file?  Again, a similar
› problem to the above question...there's no room for it.  If you're reading
› into a field that is PIC S999, then you will only read 3 characters, all
› numeric...no room for a minus sign.

Generally, it's not a problem. The sign is encoded in the rightmost byte.
If the data item was created by an IBM COBOL compiler, it followed the sign
rules when it was written, and will be understood when it is read. But if
you are importing/exporting data between different environments, you may have
some conversion to do. Obviously, you need to know how data is stored in
both environments.

› 
› Sorry if my questions are too basic...but my book is quite unclear about
…[4 more quoted lines elided]…
› assembler experience for just that reason.

You're absolutely right, you do need to know how the data is stored in order
to convert from one coding system to another. And some experience with
assembler could help the programmer to be aware of those underlying details.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

Your question is meaningless until you mention the platform and compiler
which you are referencing.

COMP- anything is implemetor defined, some standardization, but not a lot.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

"Tzadik Vanderhoof" wrote:

› I'm a bit confused about a few things in COBOL...
› 
…[4 more quoted lines elided]…
>From "IBM COBOL for MVS & VM Programming Guide", page 63:

PICTURE, USAGE and Internal hex
Optional SIGN clause value Representation

External Decimal:
PIC S9999 DISPLAY +1234 F1F2F3C4
-1234 F1F2F3D4
1234 F1F2F3C4

PIC 9999 DISPLAY 1234 F1F2F3F4

PIC S9999 DISPLAY SIGN LEADING +1234 C1F2F3F4
-1234 D1F2F3F4

PIC S9999 DISPLAY SIGN LEADING SEPERATE
+1234 4EF1F2F3F4
-1234 60F1F2F3F4

PIC S9999 DISPLAY SIGN TRAILING SEPERATE
+1234 F1F2F3F44E
-1234 F1F2F3F460

Binary:
PIC S9999 BINARY +1234 04D2
COMP -1234 FB2E
COMP-4

PIC 9999 BINARY +1234 04D2
COMP -1234 04D2
COMP-4

Internal decimal:
PIC S9999 PACKED-DECIMAL +1234 01124C
COMP-3 -1234 01124D

PIC 9999 PACKED-DECIMAL +1234 01124C
COMP-3 -1234 01124D

Internal floating point:
COMP-1 +1234 434D2000
-1234 C34D2000

COMP-2 +1234 434D200000000000
-1234 C34D200000000000

External floating point:
PIC +9(2)9(2)E+99 DISPLAY +1234 43F1F24BF3F4C54EF0F2
-1234 60F1F24BF3F4C54EF0F2

All internal representations are in EBCDIC.

› 2) Where is the sign stored in a USAGE IS DISPLAY data? There seems to be
› no place for it, if, as my book says, PIC S999 uses 3 characters.
›
The sign is stored in the last byte of the field as follows:

+1 thru +9 is: A thru I or hex "C1" thru "C9"
-1 thru -9 is: J thru R or hex "D1" thru "D9"
+0 is: {
-0 is: }

Example: when viewing a field directly without hex representation the
value "+1234" for field "PIC S9999 DISPLAY" appears as "123D". This
is a holdover from the cardpunch days when one must pack as much
infomation onto a 80-character card as possible.

› 3) How do you read in a signed number from a file?  Again, a similar
› problem to the above question...there's no room for it.  If you're reading
…[3 more quoted lines elided]…
› See the answers to the above questions.
 
› Sorry if my questions are too basic...but my book is quite unclear about
› the finer points of how the data is actually stored in the computer.  Some
…[4 more quoted lines elided]…
› 

You'll encounter this in all operating systems and with older
programs. Most programmers will either use the imbedded sign with
implied DISPLAY's or use packed-decimal. It's out of habit. It's a
real nightmare for C programmers trying to read in ;)

I think for max portability one should use SIGN TRAILING SEPERATE. I
beleive I read that as an international standard somewhere. Please
correct me if I'm wrong on this.

Just my two cents worth; adjusted for inflation,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "nospam..." <ua-author-565979@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

On 25 Jun 1997 21:47:51 GMT, "Tzadik Vanderhoof"
wrote:

In addition to the other responses, and to add to the confusion.



› 2) Where is the sign stored in a USAGE IS DISPLAY data? There seems to be
› no place for it, if, as my book says, PIC S999 uses 3 characters.



You also may have the choice of SIGN LEADING, SIGN TRAILING and SIGN
SEPERATE; depending on which flavor of COBOL you are using. If memory
serves, these affect USAGE DISPLAY numeric fields by controlling how
the sign is maintained and may effect the number of bytes a data item
will take up.

Maybe someone who is using these constructs currently can shed some
light here, if you need.
```

##### ↳ ↳ Re: I'm confused about USAGE and internal storage

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-06-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43eecf7fa5-p5@usenetarchives.gap>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il> <gap-43eecf7fa5-p5@usenetarchives.gap>`

```

nos··.@er··s.com wrote:
:>
:> On 25 Jun 1997 21:47:51 GMT, "Tzadik Vanderhoof"
:> wrote:
:>
:> In addition to the other responses, and to add to the confusion.
:>
:>
:>
:> >2) Where is the sign stored in a USAGE IS DISPLAY data? There seems
to be
:>
:>
:>
:> You also may have the choice of SIGN LEADING, SIGN TRAILING and SIGN
:> SEPERATE; depending on which flavor of COBOL you are using. If
memory
:> serves, these affect USAGE DISPLAY numeric fields by controlling how
:> the sign is maintained and may effect the number of bytes a data item
:> will take up.
:>
:> Maybe someone who is using these constructs currently can shed some
:> light here, if you need.

I guess I should have posted a response sooner, but I E-mailed
Tzadik a detailed 4 page copy of USAGE and various COMP fields
and MOVEs to Edited PICs with samples from one of my manuals.
If any one else needs it, just ask, but it is for PCs.

Bill H.
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "hbu..." <ua-author-14991407@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p7@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

"Tzadik Vanderhoof" wrote:

› 3) How do you read in a signed number from a file?  Again, a similar
› problem to the above question...there's no room for it.  If you're reading
› into a field that is PIC S999, then you will only read 3 characters, all
› numeric...no room for a minus sign.

The sign is stored in the first 4 bits of the last character. In a
signed number only the last 4 bits of every character are used to
represent the digit. I forget what the 4-bit value for negative is (C
or D??).

----------------------------------------------
Herb Bujak
Mobile Data Solutions, Inc.
Work: hbu··.@mds··c.ca
Home: her··.@geo··s.com
http://www.geocities.com/SiliconValley/Pines/9037/
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "priyamvadha v. j." <ua-author-17071621@usenetarchives.gap>
- **Date:** 1997-06-27T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p8@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```


USAGE IS DISPLAY , is used purely for display purposes, where data is
stored in the character format,
where as, USAGE IS COMPUTATIONAL is used for computational purposes, where
the data is stored
in the binary form ready to be put into registers and operations performed
on it.There is no need that
any field used for computational purposes be always declared with usage is
computational.Even if
it is not defined as such, it is taken care that during execution ,all
fields used for computation
are converted to their binary forms. By declaring the field as usage
computational,beforehand, you
are improving the performance by eliminating the need for computational
feilds to be converted to
binary.I dont know exactly, but declaring the fields as computational may
cause some porting
problems.

As I understand, there is no need for a signed display field to
have a PIC of S999. If you find
a need to display signed data you need to use an editing character which is
+ or -. If - is
used all those which are negative, are represented in storage with a sign(
ie., negative field takes
up one character position, where as a positive field does not).

The ' -' picture insertion character differs from S character in that the
use of S character
identifies a field as a signed one for computational purposes but the sign
does not occupy a
position as such . Use of '-' picture character leads to a field in which
sign occupies a character
position. This is used for display purposes. Similar is the case with V
which declares a computational
field as having a decimal point which is assumed which should be used for
display purposes with an
editing character ' . '.
for example computational field ------------- FELD-1 PIC
99V99
for display purposes ------------- FELD-2
PIC 99.99 USAGE DISPLAY.

PROCEDURE DIVISION.
...
MOVE FELD-1 TO FELD-2.
DISPLAY FELD-2.

now coming to the how the signed feild is keyed in , and how it is read
from the feild on a file

consider a record with the followng format
FILENAME ----------EXAMPLE-FILE
01 EXAMPLE-REC
02 FELD1 PIC 99V999.
02 FELD2 PIC S99.
02 FELD3 PIC XXXX.

FELD1 is keyed in as ------- 24299 ( to mean 24.299)
FELD2 is keyed in as ------- 22 and then '-' on the numeric key pad(
to mean -22)
FELD3 is keyed in as ------- cc2c

EXAMPLE-FILE would look as
242992Lcc2c
------------------
assuming that A-J stand for +1 to +9.(a=+1, b=+2.......j=+9)
assuming that K-T stand for -1 to -9(k=-1,L=-2,.........t=-9)
I learn that a similar method was used in one of the implementations to
store -ve numbers.It
may differ from one implementation to other.But a similar method can be
used.

Since the system has already been given the record format, seeing the file,
the system interprets
which feild is +ve and -ve, and about the decimal point positions.


Priyamvadha v j



Tzadik Vanderhoof wrote in article
<01bc81b1$646b9d60$7cf··.@dia··t.il>...
› I'm a bit confused about a few things in COBOL...
› 
…[24 more quoted lines elided]…
›
```

#### ↳ Re: I'm confused about USAGE and internal storage

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-28T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43eecf7fa5-p9@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`
- **References:** `<01bc81b1$646b9d60$7cf8cbc7@dialup.netvision.net.il>`

```

In article <01bc81b1$646b9d60$7cf··.@dia··t.il>,
"Tzadik Vanderhoof" wrote:
› 
› I'm a bit confused about a few things in COBOL...
…[7 more quoted lines elided]…
› computer.

Although your book ought to explain all of the significant data formats,
it can't explain which format goes with which USAGE because that differs
from vendor to vendor. Since you mention EBCDIC in your article, the
following is probably applicable, but to find out for sure, you must
consult the manual for your compiler:

COMP - two's complement binary 1 thru 4 digits, two bytes
5 thru 9 digits, four bytes
10 thru 18 digits, eight bytes

COMP-1 - Single-precision floating-point binary (four bytes)
COMP-2 - Double-precision floating-point binary (eight bytes)

COMP-3 - Packed decimal (n+2)/2 bytes, up to a maximum of 10 bytes

I should point out that, again since you mention EBCDIC, the
floating-point binary in question is probably not IEEE format but IBM
hexadecimal normalized format. This one deficiency in the IBM 360
instruction set sold more UNIVAC 1108s, GE 6000s, etc., than anything
else.

Beyond this, the extension I find most useful is COMP-5 (Native Binary).
As you may know, the PICTURE clause is decimal and therefore if the USAGE
is binary there is a conflict. The default TRUNC(STD) compiler option
tells the compiler to use the PICTURE, which is expensive, while
TRUNC(BIN) tells the compiler to use the USAGE, which is not always safe.
Unfortunately, since TRUNC is a compiler option, you make this choice
only once for every variable in the entire compilation.

COMP-5 was introduced to allow you to specify truncation on a variable-by
variable basis. COMP-5 variables are always TRUNC(BIN), regardless of
the compiler option. Therefore, if you let the TRUNC option default to
TRUNC(STD), COMP variables will always be truncated and COMP-5 variables
will never be truncated. COMP-5 is also useful in dealing with
endianness. I would like to be able to use COMP-5 on MVS, but I am not
holding my breath.

MicroFocus has an interesting extension called COMP-X, in which the
number of Xs in the PICTURE directly represents the number of bytes in
the variable.

Even though our field is overfull of jargon, the name "COMP-3" has to set
some kind of world record for obscurity. The kind folks at the standards
committee tried to remedy this by introducing the plain names BINARY and
PACKED-DECIMAL. Not only is BINARY clearer than COMP, it will also be
the same in all compilers that meet the standard, whereas COMP is not
necessarily what you expect (c.f. UNISYS A series).

Unfortunately, they neglected to provide abbreviations, and CoBOL
programers are always short of columns. If I could change COMP-3 to
PACKED, I would immediately do so, because it still lines up. But if I
tried to change COMP-3 to PACKED-DECIMAL with an editor, hundreds of
thousands of lines of code would push past column 72. Consequently, I
have yet to see BINARY or PACKED-DECIMAL used in a production program at
a bank or insurance company. However, this should not stop you from
using them in your personal code, if your compiler supports them.

I snipped the rest of your questions because if your book doesn't explain
overpunched signs, you need another book. Usenet is OK for chatting but
it can't come near a book when it comes to conveying information, and you
need the manual for your compiler anyway.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
