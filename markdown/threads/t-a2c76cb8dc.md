[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# line feed

_8 messages · 8 participants · 2000-12_

---

### line feed

- **From:** sdeblanc@my-deja.com
- **Date:** 2000-12-13T17:08:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<918aef$rp3$1@nnrp1.deja.com>`

```
Ok, please don't laugh at this novice. I am
looking for the character combination that will
allow me to advance to the same column on the
next line.  If I am on column 55 on line 3 in my
output, I need to advance to column 55 on line
4.  I have tried the X'OA' and the X'OD'
characters, singly and in combination and have
dealt with the line sequential info.  However,
nothing I have done to date achieves this.  It
always takes it to column 1 on the next line.I
use NetExpress 3.0 run on Windows NT and draw
info from SQL Server 7.0 setup.  PLEASE, if
anyone has a suggestion, I would truly appreciate
your advice.  TIA--


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: line feed

- **From:** Terry Winchester <terrywin.nospam@pronetisp.net>
- **Date:** 2000-12-13T16:24:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jfpf3tcucg2knqp1mkb8bl7qpvhofv55ic@4ax.com>`
- **References:** `<918aef$rp3$1@nnrp1.deja.com>`

```
On Wed, 13 Dec 2000 17:08:38 GMT, sdeblanc@my-deja.com wrote:

>Ok, please don't laugh at this novice. I am
>looking for the character combination that will
…[12 more quoted lines elided]…
>

You will probably need to use embedded tab characters
(X'09') to get near your column. Most tabs expand to 8
spaces - you need 6, plus 5 spaces (X'20').  Not all 
printers support this method though.

HTH
Good Luck
Terry
```

#### ↳ Re: line feed

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-12-14T08:16:16
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<919vjf$3gjvt$1@ID-39799.news.dfncis.de>`
- **References:** `<918aef$rp3$1@nnrp1.deja.com>`

```
line feed, carriage return (X'0A0D'), and 54 spaces.

I assume you are talking about a print.

<sdeblanc@my-deja.com> wrote in message news:918aef$rp3$1@nnrp1.deja.com...
> Ok, please don't laugh at this novice. I am
> looking for the character combination that will
…[15 more quoted lines elided]…
> http://www.deja.com/
```

##### ↳ ↳ Re: line feed

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2000-12-14T22:42:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D1c_5.5940$7I.510706@typhoon.nyroc.rr.com>`
- **References:** `<918aef$rp3$1@nnrp1.deja.com> <919vjf$3gjvt$1@ID-39799.news.dfncis.de>`

```
From his post, it appears he wants to do a LF *without* a CR. I'm assuming
most printers won't support that. He may need to keep track of  how many
characters have been printed, then do a CR/LF, then space out that many
characters before printing.
Rick: sdeblanc said "*if* I am on column 55."  I suppose he means "...and if
I am on column 17 of line 3, I need to advance to col 17 of line 4."

Rick Price <rick@hpd.co.uk> wrote in message
news:919vjf$3gjvt$1@ID-39799.news.dfncis.de...
> line feed, carriage return (X'0A0D'), and 54 spaces.
>
> I assume you are talking about a print.
>
> <sdeblanc@my-deja.com> wrote in message
news:918aef$rp3$1@nnrp1.deja.com...
> > Ok, please don't laugh at this novice. I am
> > looking for the character combination that will
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: line feed

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-12-15T03:45:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001214224513.12660.00002589@nso-cd.aol.com>`
- **References:** `<D1c_5.5940$7I.510706@typhoon.nyroc.rr.com>`

```
In article <D1c_5.5940$7I.510706@typhoon.nyroc.rr.com>, "William Bub"
<fathafluff@hotmail.com> writes:

>
>From his post, it appears he wants to do a LF *without* a CR. I'm assuming
…[5 more quoted lines elided]…
>

Long Long ago there was a VT (Vertical Tab) character used for 
screen positioning and on several dot-matrix type printers.
I don't suppose that there are any PCL language gurus out there 
that might know if such a thing exists for InkJet/LaserJet printers.
```

###### ↳ ↳ ↳ Re: line feed

_(reply depth: 4)_

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-12-15T09:04:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6smj3t87360lljftibcijftm138dai7tqi@4ax.com>`
- **References:** `<D1c_5.5940$7I.510706@typhoon.nyroc.rr.com> <20001214224513.12660.00002589@nso-cd.aol.com>`

```
I have this in my notes.

I have never tried this though

Vertical and Horizontal cursor motion
Operation  === Type of motion === Ascii sequence === Decimal === Hexa
Vertical Position === # of Rows === Ec&a#R (r) === 027 038 097 #...#
082 (114) === 1B 26 61 #...# 52 (72)
 === # of Dots === Ec*p#Y(y) === 027 042 112 #...# 089(121) === 1B 2A
70 #...# 59 (79) === # of Decipoints === Ec&a#V (v) === 027 038 097
#...# 086(118) === 1B 26 61 #...# 56 (76)
Horizontal Position === # of Columns === Ec&a#C (c) === 027 038 097
#...# 067(99) === 1B 26 61 #...# 43 (63) === # of Dots === Ec*p#X (x)
=== 027 042 112 #...# 088  (120) === 1B 2A 70 #...# 58 (78)
 === # of Decipoints === Ec&a#H (h) === 027 038 097 #...# 072 (104)
=== 1B 26 61 #...# 48 (68)
Half Line Feed ===  === Ec= === 027 061	1B 3D

Put the text in a Excel spreadsheet bearing in mind that the column 
separator is " === ".

FF

On 15 Dec 2000 03:45:13 GMT, sff5ky@aol.comxxx123 (Sff5ky) wrote:

>In article <D1c_5.5940$7I.510706@typhoon.nyroc.rr.com>, "William Bub"
><fathafluff@hotmail.com> writes:
…[13 more quoted lines elided]…
>that might know if such a thing exists for InkJet/LaserJet printers.
```

#### ↳ Re: line feed

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-12-19T10:58:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91o0eu$dic$1@news.igs.net>`
- **References:** `<918aef$rp3$1@nnrp1.deja.com>`

```
Write the leading characters as part of the record.
(Hint: to get to column 53, write 52 spaces).

sdeblanc@my-deja.com wrote in message <918aef$rp3$1@nnrp1.deja.com>...
>Ok, please don't laugh at this novice. I am
>looking for the character combination that will
…[15 more quoted lines elided]…
>http://www.deja.com/
```

##### ↳ ↳ Re: line feed

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-12-19T20:42:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91p2r90iv8@enews4.newsguy.com>`
- **References:** `<918aef$rp3$1@nnrp1.deja.com> <91o0eu$dic$1@news.igs.net>`

```
Now you're thinking!  You're like me; it's quicker to think up a neat, 
unique method than to look up something in a book.  I would imagine that
you're code is also somewhat 'non-standard' in general.

Jeff

----------
In article <91o0eu$dic$1@news.igs.net>, "donald tees" <donald@willmack.com>
wrote:


> Write the leading characters as part of the record.
> (Hint: to get to column 53, write 52 spaces).
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
