[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# reading COBOL Sequential output file (Easy Question)---Help

_7 messages · 5 participants · 2003-11 → 2003-12_

---

### reading COBOL Sequential output file (Easy Question)---Help

- **From:** fisherj12@hotmail.com (Fisher)
- **Date:** 2003-11-25T08:55:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<147ccfbd.0311250855.473d10b9@posting.google.com>`

```
I am reading a sequential file using a Visual Basic 6.0 Type Array. As
I read each record from the cobol output Sequential file (put into vb

strings--then the array)---- the VB Sub will then insert a record into
the db as I have the data put into the array with the correct space

allocated from the cobol output file.


I am given the cobol sequential file layout.

I know how many characters to allow a 
ID pic X(02)'''''2 right?
CATEGOREY pic X(01) etc''''1 right?

but what do I do with a 
FLOORPLAN pic s99v99
and 
FLOOR B pic s99v99 occurs 8
and 
FLOOR C pic s(9) occurs 4
????


the type array goes like this
Private Type dataInfo
  ID As String * 2
  CATEGOREY As String * ????????????????
  FLOORPLAN As String * ????????????????
  FLOORB As String * ???????????????????
  FLOORC As String * ?????????????????
End Type

Private Whatever As dataInfo



These are really confusing me and I cannot find that much research on
it.

Thanks for any of your help 
email me if my question is unclear or you want to talk further about
the question.
Thanks in advance.

Jeff Fisher
Systems Engineering, Inc.
```

#### ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-25T12:42:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031125134308.566$Fp@news.newsreader.com>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com>`

```
"Fisher" <fisherj12@hotmail.com> wrote:
>
> I am given the cobol sequential file layout.
>
> I know how many characters to allow a
> ID pic X(02)'''''2 right?

Pic X(02) represents a 2 character alphanumeric field, equivalent to
DIM ID AS STRING * 2

> CATEGOREY pic X(01) etc''''1 right?

Pic X(01) represents a 1 character alphanumeric field, equivalent to
DIM CATEGOREY AS STRING * 1

> but what do I do with a
> FLOORPLAN pic s99v99

The field is exactly 4 characters. The rightmost character is both
the low-order digit and the sign. Here are the possible values for
the rightmost character:

   Digit value:  0 1 2 3 4 5 6 7 8 9
                 - - - - - - - - - -
Field Negative:  p q r s t u v w x y
Field Positive:  0 1 2 3 4 5 6 7 8 9

There is an *assumed* decimal place between the second and third
character positions. In other words, the value "1234" would
represent the number 12.34, and the value "123t" would represent
the number -12.34

> and
> FLOOR B pic s99v99 occurs 8

The format is the same as above, but there are 8 fields, one right
after the other, left to right (ie. #1 is leftmost, #8 is rightmost).

> and
> FLOOR C pic s(9) occurs 4
> ????

This is an integer field 9 positions long, with the rightmost
character representing the sign, exactly as above. There are
four of them, left to right as above.

Knowing the representation, you should be able to decode and store
them as you like.
```

##### ↳ ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-27T07:16:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311270716.383e1853@posting.google.com>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com> <20031125134308.566$Fp@news.newsreader.com>`

```
One caution below...

"Judson McClendon" <judmc@sunvaley0.com> wrote in message news:<20031125134308.566$Fp@news.newsreader.com>...

> > but what do I do with a
> > FLOORPLAN pic s99v99
…[9 more quoted lines elided]…
> 

The sign representation is implimentor defined - and differs between
COBOL compilers.
```

###### ↳ ↳ ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-28T06:48:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031128074852.265$sv@news.newsreader.com>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com> <20031125134308.566$Fp@news.newsreader.com> <bfdfc3e8.0311270716.383e1853@posting.google.com>`

```
"Thane Hubbell" <thaneh@softwaresimple.com> wrote:
> One caution below...
>
…[16 more quoted lines elided]…
> COBOL compilers.

Oops! You're right, Thane. :-)
```

###### ↳ ↳ ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-11-28T13:15:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9UHxb.6113$aw2.2647823@newssrv26.news.prodigy.com>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com> <20031125134308.566$Fp@news.newsreader.com> <bfdfc3e8.0311270716.383e1853@posting.google.com> <20031128074852.265$sv@news.newsreader.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031128074852.265$sv@news.newsreader.com...
> "Thane Hubbell" <thaneh@softwaresimple.com> wrote:
> > One caution below...
…[19 more quoted lines elided]…
> Oops! You're right, Thane. :-)


My MF manual contains this:
"The USAGE IS DISPLAY clause (whether specified explicitly or implicitly)
specifies that a standard data format is used to represent a data item in
the storage of the computer, and that the data item is aligned on a
character boundary".

This does NOT contain one of the "MF" or "VSC2" 'circles' indicating a
implementor extension; nor does the description of the sign encoding for
USAGE IS DISPLAY for not-separately signed numeric data. In this latter
section the manual indicates negative signing is accomplished by setting bit
6 of the character on (i.e., add x'40') ; this will, of course, result in a
different display character depending on the character-set in use.

So, are you guys really sure that the sign encoding is implementor-defined?
Above seems to indicate it's standard.

MCM
```

###### ↳ ↳ ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-28T10:48:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031128114911.631$t2@news.newsreader.com>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com> <20031125134308.566$Fp@news.newsreader.com> <bfdfc3e8.0311270716.383e1853@posting.google.com> <20031128074852.265$sv@news.newsreader.com> <9UHxb.6113$aw2.2647823@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > "Thane Hubbell" <thaneh@softwaresimple.com> wrote:
…[36 more quoted lines elided]…
> Above seems to indicate it's standard.


In COBOL 85, yep. Paragraph 3.17.4(1) says the 'S' character specifies
that the field is signed, but neither the position or the representation of the
sign. Paragraph 3.17.4(3)c declares that if you specify the 'SIGN is
SEPARATE' clause, the representation must be "the standard data format
characters '+' and '-'." I knew this, but much of my experience is on EBCDIC
mainframes, where there is considerable consistency in display sign
representation (upper 4 bits almost always hex C for pos, D for neg), and it
just slipped my mind when I made my post.
```

###### ↳ ↳ ↳ Re: reading COBOL Sequential output file (Easy Question)---Help

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-03T20:03:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bkrzb.26607$sb4.23581@newsread2.news.pas.earthlink.net>`
- **References:** `<147ccfbd.0311250855.473d10b9@posting.google.com> <20031125134308.566$Fp@news.newsreader.com> <bfdfc3e8.0311270716.383e1853@posting.google.com> <20031128074852.265$sv@news.newsreader.com> <9UHxb.6113$aw2.2647823@newssrv26.news.prodigy.com> <20031128114911.631$t2@news.newsreader.com>`

```
For "portable" numeric fields define them as

   Usage Display (default)
   Sign is leading separate

Otherwise, one "may" find the sign indicator at the beginning, end (or
theoretically - middle) of the field.

Using "leading separate" ALSO makes "conversion" (e.g. ASCII/EBCDIC) a WHOLE lot
easier.  Obviously, it DOES take more storage and is probably NOT a great choice
for "arithmetic performance" numeric items.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
