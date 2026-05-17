[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pic s9(7)v99...please explain...I'm just a little windows programmer!

_17 messages · 11 participants · 1998-05_

---

### Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "bi..." <ua-author-16025780@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net>`

```

I am writing a program for someone that exports files to be used by a
Cobol program. I have been told that the format must be pic s9(7)v99.
The programmer who sent the info said that both negative and positive
numbers must be indicated in the last byte of the data.

In some of the code I inherited it seems that negative numbers are
being shown like this:

-0.01 = 00000000J
-0.02 = 00000000K
-0.11 = 00000001J
-2.12 = 00000021K

but the code puts positive numbers like this:

0.01 = 000000001
0.02 = 000000002
2.12 = 000000212

The programmer who received this output said that positive numbers
should also be "signed" and gave only one example:

"a value of 0 should be shown as 00000000{ and not 000000000"

Okay, what about the other positive values?

Could someone please explain this to me or point in the right
direction?
```

#### ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net>`

```

Bill Strahan wrote:
› 
› I am writing a program for someone that exports files to be used by a
…[26 more quoted lines elided]…
› direction?

It looks like your data needs to be in IBM zoned decimal format. Digits
are represented by hex values F0 thru F9.

The rightmost digit contains the sign in the lefthand nybble. X'F' is
unsigned positive, X'C' is signed positive, and X'D' is signed negative.

F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 are the unsigned positive digits

C0 C1 C2 C3 C4 C5 C6 C7 C8 C9 are the signed positive digits

D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 are the signed negative digits

In the EBCDIC character set, C0 thru C9 will display as "{ABCDEFGHI".

D1 thru D9 will display as "JKLMNOPQR" (digits with negative sign). I
don't remember if there is a printable graphic for X'D0' in the EBCDIC
character set.

I hope that helps.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
Y2K Time Machine reports at http://home.att.net/~arnold.trembley/
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p2@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap>`

```

Woah! Remember, if Bill is creating this file in Windows, he is creating
an ASCII file, not an EBCDIC file! What Bill must to do is use the ASCII
character which will translate into the EBCDIC character that is desired.
He is going to need an EBCDIC-ASCII equivalence table in addition to the
information you gave.
```

###### ↳ ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "john calahan" <ua-author-8533050@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p3@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap> <gap-0da4b8aebd-p3@usenetarchives.gap>`

```

This is just a side note, but the tone of Bill's message gave me the
impression he was looking at data on the mainframe side. I've dealt with
numerous host-to-PC file transfer packages over the years, and virtually
all of them had some sort of EBCDIC-to-ASCII translation feature built
into them. I don't know if that's the route Bill will go, but if so he
should look into that.

John Calahan

On Wed, 20 May 1998, Judson McClendon wrote:

› Woah!  Remember, if Bill is creating this file in Windows, he is creating
› an ASCII file, not an EBCDIC file!  What Bill must to do is use the ASCII
…[68 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

_(reply depth: 4)_

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p4@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap> <gap-0da4b8aebd-p3@usenetarchives.gap> <gap-0da4b8aebd-p4@usenetarchives.gap>`

```

what i hear him saying is that he is a windows programmer
and is trying to look at mainframe data.

now, since he did not give us his source language,
we can assume its not COBOL.

what we also need is to know if you are using
data connected to a mainframe, or is the
data on the local PC. if its on the mainframe
you might have to convert to little endian format as well.



gvw··.@ix.··m.com to reply remove the spam
```

###### ↳ ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "wouter wijker" <ua-author-6588841@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p3@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap> <gap-0da4b8aebd-p3@usenetarchives.gap>`

```

The behaviour is a bit compiler dependent. MF-Cobol offers the option to
run with the SIGN=EBCDIC or SIGN=ASCII compiler directive.
This will most certainly help in a quick and dirty EBCDIC to ASCII
translation.

The ASCII convention is:

0 1 2 3 4 5 6 7 8 9 (Unsigned/ Positive)
p q r s t u v w x y (Negative)

The EBCDIC convention is:
0 1 2 3 4 5 6 7 8 9 (Unsigned)
} J K L M N O P Q R (NEGATIVE)
{ A B C D E F G H I (Positive)

Do not translate an EBCDIC value of -123 (F1F2D3 == 12L) to
Ascii by simply translating the characters , in this cas the sign
charater 'L' is translated to its equivalent in ascii.

It has to translate to -123 (313273 == 12s).
Hope it helps,
Kind regards,
W Wijker.
```

###### ↳ ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "rick smith" <ua-author-44949@usenetarchives.gap>
- **Date:** 1998-05-20T06:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p3@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap> <gap-0da4b8aebd-p3@usenetarchives.gap>`

```

You might try the following.

Converting signed ASCII to EBCIDIC.

Move the numeric field (pic 9) to an alphanumeric field (pic X)
in the output record then convert the sign. Using the CALL
on the numeric field will result in invalid data.

In your program, insert the following code for each data-name
to be converted:

CALL "CONVSIGN" USING
data-name (FUNCTION LENGTH(data-name):1).
*> POINT TO THE LAST CHARACTER IN THE FIELD

where CONVSIGN contains:

...
LINKAGE SECTION.
01 CONV-CHAR PIC X.
PROCEDURE DIVISION USING CONV-CHAR.
INSPECT CONV-CHAR
CONVERTING "0123456789pqrstuvwxy" *> SIGNED ASCII
TO "{ABCDEFGHI}JKLMNOPQR". *> SIGNED EBCIDIC
EXIT PROGRAM.

Disclaimer: Although I did reference some existing working code to produce
this snippet, I did NOT test this particular code. Use at your own risk!

Judson McClendon wrote in message <6ju5gj$bev$1.··.@cam··g.com>...
› Woah!  Remember, if Bill is creating this file in Windows, he is creating
› an ASCII file, not an EBCDIC file!  What Bill must to do is use the ASCII
…[66 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "danie..." <ua-author-6589640@usenetarchives.gap>
- **Date:** 1998-05-20T07:54:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p2@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p2@usenetarchives.gap>`

```

In article <6jtvag$7.··.@bgt··t.net>,
arn··.@wor··t.net wrote:
› 
› Bill Strahan wrote:
…[3 more quoted lines elided]…
›› Cobol program.  I have been told that the
format must be pic s9(7)v99.

snip

› It looks like your data needs to be in IBM zoned
› decimal format.  Digits
› are represented by hex values F0 thru F9.
 
› snip
 
› F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 are the unsigned
› positive digits
…[6 more quoted lines elided]…
› 
 
› snip
 
 
› Arnold Trembley
› Software Engineer I (just a job title, still a
› programmer)
› MasterCard International

Hi,

Your zoned decimal explications are not in all
points correctly:

+12345 is in EBCDIC hex F1 F2 F3 F4 F5
or F1 F2 F3 F4 C5 (signed)
-12345 is F1 F2 F3 F4 D5

Character equvalents in EBCDIC are the following:

F0 to F9 = zero to nine
C0 = '{', C1 to C9 = 'A' to 'I'
D0 = '}', D1 to D9 = 'J' to 'R'

The declaration in COBOL as S9(7)V9(2) means that
the numbes has to be signed (the 'S' at the
beginning) and that it has to have nine (seven plus
two) numbers (the nines), from which seven are
before and two after the decimal point. The 'V'
indicates the decimal point which is held
internally and not shown in the field itself.

Cheers

Daniel

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "min..." <ua-author-793677@usenetarchives.gap>
- **Date:** 1998-05-20T21:28:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **In-Reply-To:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net>`

```

bi··.@ttg··e.com (Bill Strahan) wrote:
› 
› I am writing a program for someone that exports files to be used by a
› Cobol program.  I have been told that the format must be pic s9(7)v99.
› The programmer who sent the info said that both negative and positive
› numbers must be indicated in the last byte of the data.

Hi Bill - here's some info. Some of this is slangish, not IBMese, in hopes
that it will stay easier to comprehend.
pic s9(7)v99 means the field contains 9 digits altogether. When it is stored,
it is simply 9 bytes representing numbers. When it is read into a COBOL
program, it is 'scaled' to make it represent 7 digits on the 'whole number'
side and 2 digits on the 'decimal side'.

The 's' means it is a 'signed' field. In IBM COBOL, this forces the sign
into the 'top half' of the last byte.

Now, in IBM COBOL, the representation of numbers in single bytes is such that
the first four bits (let's call it the 'top' four bits) contains the 'sign'
and the 'bottom' four bits contain the numeric value.

For a multi-byte number, the actual sign is only stored in the top half of
the last (rightmost) byte. The rest of the bytes have a neutral sign.
The signs are represented by hex combos of 1's and 0's in the top half, but
for discussion purposes, let's say they are 'C' (+), 'D' (-), and 'F' for
neutral. (This is what shows up in an interpretation of a 'core dump'.)

So +1234567.89 would be stored with 'top' halfs of FFFFFFFFC and 'bottom
halfs as 123456789. -1234567.89 would be the same except that the last top
half would be a 'D' instead of a 'C'.


› In some of the code I inherited it seems that negative numbers are
› being shown like this:
…[15 more quoted lines elided]…
› "a value of 0 should be shown as 00000000{ and not 000000000"

All the above are what the programmer sees in an attempt to print his
storage. The printing software makes assumptions about things with 'C', 'D',
and 'F' in the top halfs of bytes. For instance, the -0.01 example is not
really stored with the intent of being a 'J', the printing software is making
a guess.
The stipulation about '{' is an interpretation of 'C0'. I.e., he wants 0 to
be stored as +0.
He also expects +0.01 to appear as 00000000A to him. What happened in your
example of 'the positive numbers' is that they were neutral (had 'F' in the
top halfs of the last byte.

The deal is that in EBCDID, C1 (top/bottom) is interpreted as an 'A', C2 as
'B', ...l, D1 = J, etc. Again, this is just a printing interpretation, not
exactrly what the storage contains.
›

Abyway, the language you're using will need to create the EBCDIC counterparts
of your numbers. There are converters that will do it for you on the FTP.
Sorry but I don't know any offhand.

Java may have a class that does it.

Hope this helps. You may e-mail me for more info. But this is from home, so I
only get to it once a night.

Hi to the rest of you 'regulars'. This once-in-a-while contributor is here in
Tucson now - new job. But not allowed to use the internet from work.

John Mindock



-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

› Hi to the rest of you 'regulars'. This once-in-a-while contributor is here
› in
› Tucson now - new job. But not allowed to use the internet from work.

Thats crazy. This is a great place to see what is happening across
the industry. That sort of thing is a must for any kind of professional
awareness.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

##### ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p9@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap>`

```

P.S. To that last, your explanation of that last post was as interesting
as hell, but I got real confused for a moment. I realised in a flash that
in thirty years of Cobol programming, I had never used ECIDIC, and it
was a whole other world. In the DOS (Ascii) world, it is much simpler.

Each X,9 or whatever is a single ASCII character. The *SIGN* however
is imbedded in the last ASCII character. It is a single bit, bit 6, ored
with the ASCII value as a number. So, in a PICTURE S9(5)V9(5) field,
there would be ten ASCII characters, and the number 1.5 would be
stored as the ASCII characters "0000150000". The number -1.5 would
be stored as the same characters, but with bit six in the last zero as
a 1. That is hex 30 ored with hex 40 = hex 70 = ASCII "p". So the
number would be "000015000p". (Don't have an ASCII table handy,
is that right?).

Anyway, that did not quite jive with the example ... so I did not respond.
```

###### ↳ ↳ ↳ Re: Pic s9(7)v99...please explain...I'm just a little windows programmer!

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0da4b8aebd-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0da4b8aebd-p16@usenetarchives.gap>`
- **References:** `<80656230B5131C76.6B26D857099A706D.00463B0E497F52A3@library-proxy.airnews.net> <gap-0da4b8aebd-p9@usenetarchives.gap> <gap-0da4b8aebd-p16@usenetarchives.gap>`

```

In article <6k16l1$h4f$1.··.@new··s.net>,
"Donald Tees" wrote:
›
› The *SIGN* however is imbedded in the last ASCII character. It is a
› single bit, bit 6, ored with the ASCII value as a number.

The system of overpunched signs implemented in IBM hardware in 1964 is
actually quite clever, being the culmination of many years of real-world
experience. It has been so successful that many manufacturers such as
DEC in turn implemented it in hardware, and many more implemented it in
software. Still more implemented it merely to be able to offer mainframe
compatability.

All of the overpunched signs in this system are what they are because of
the bit patterns. It's so simple you don't even have to remember them.
Just interchange the nibbles: X'1D' -> X'D1'.

Pretty much the only problem with this system is that after you translate
it to ASCII, it doesn't make sense any more. There's no way to figure
out why X'1D' goes to X'4A' from the bit patterns; X'4A' is simply the
ASCII equivalent of X'D1'.

The IBM system is not the only system in the world, of course. Univac
went its own way, as always. Then there are the newer systems such as
the one described by Mr. Tees, which is making headway where mainframe
compatibility is not a priority, such as AIX on the RS/6000. In this
system, there is no equivalent to positive. Numbers are either unsigned
or negative:

OVERPUNCHED EMBEDDED
Unsigned Positive Negative Unsigned Negative

0 { } 0 p
1 A J 1 q
2 B K 2 r
3 C L 3 s
4 D M 4 t
5 E N 5 u
6 F O 6 v
7 G P 7 w
8 H Q 8 x
9 I R 9 y

In short, something you read in a newsgroup might well be true of the
poster's platform, but it isn't necessarily true of yours.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
