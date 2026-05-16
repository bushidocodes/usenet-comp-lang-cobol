[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# extract words from line

_5 messages · 5 participants · 2003-02_

---

### extract words from line

- **From:** tejaspandya@hotmail.com (Tejas Pandya)
- **Date:** 2003-02-12T02:44:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4bf88f51.0302120244.57a99d46@posting.google.com>`

```
Hi, I need hlep with extracting words. What I want to do is, read a
sentence and extract each word that I read. The line contains no
special characters etc just plain text with spaces, as if it contains,
I replace all characters by space. I need to store each extracted word
in a file and sort them. Can anyone hlep please. I cannot get to
extract the second word after I unstring delimit by space to a
temp-word. Can someone help please. Thanks
```

#### ↳ Re: extract words from line

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2003-02-12T10:40:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fkiK4b9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<4bf88f51.0302120244.57a99d46@posting.google.com>`

```
     Am  12.02.03
schrieb  tejaspandya@hotmail.com (Tejas Pandya)
    auf  /COMP/LANG/COBOL
     in  4bf88f51.0302120244.57a99d46@posting.google.com
  ueber  extract words from line

TP> Hi, I need hlep with extracting words. What I want to do is, read a
TP> sentence and extract each word that I read. The line contains no
TP> special characters etc just plain text with spaces, as if it
TP> contains, I replace all characters by space. I need to store each
TP> extracted word in a file and sort them. Can anyone hlep please. I
TP> cannot get to extract the second word after I unstring delimit by
TP> space to a temp-word.

   There is more than one way to do it...

   You can specify the starting position of the UNSTRING by the "WITH  
POINTER identifier-7" clause, and count the number of characters found  
by the "COUNT IN identifier-6", and then repeat that in a loop by  
setting the POINTER from the characters in COUNT;

   You can specify more than one "INTO  identifier-4" (and count the  
number of words found by the "TALLYING IN ... " clause.

   I don't know in how far a dynamic allocation of receiving areas as  
part of an array would be possible, with the subscript of the array  
being calculated dynamically e.g. by the TALLYING IN phrase.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Die Interessen der Nation lassen sich nicht anders formulieren als unter
dem Gesichtspunkt der herrschenden Klasse oder der Klasse, die die
Herrschaft anstrebt."            - Leo Trotzki         (27. Januar 1932)
```

#### ↳ Re: extract words from line

- **From:** docdwarf@panix.com
- **Date:** 2003-02-12T05:50:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2d8u0$2u6$1@panix1.panix.com>`
- **References:** `<4bf88f51.0302120244.57a99d46@posting.google.com>`

```
In article <4bf88f51.0302120244.57a99d46@posting.google.com>,
Tejas Pandya <tejaspandya@hotmail.com> wrote:
>Hi, I need hlep with extracting words.

Please do your own homework.

DD
```

##### ↳ ↳ Re: extract words from line

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-02-12T22:55:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4AD0D8.3050605@optonline.NOSPAM.net>`
- **References:** `<4bf88f51.0302120244.57a99d46@posting.google.com> <b2d8u0$2u6$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <4bf88f51.0302120244.57a99d46@posting.google.com>,
> Tejas Pandya <tejaspandya@hotmail.com> wrote:
…[3 more quoted lines elided]…
> Please do your own homework.

It does smell like homework.
```

#### ↳ Re: extract words from line

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-12T07:03:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dP6cndGslsdE2dejXTWciA@giganews.com>`
- **References:** `<4bf88f51.0302120244.57a99d46@posting.google.com>`

```

"Tejas Pandya" <tejaspandya@hotmail.com> wrote in message
news:4bf88f51.0302120244.57a99d46@posting.google.com...
> Hi, I need hlep with extracting words. What I want to do is, read a
> sentence and extract each word that I read. The line contains no
…[4 more quoted lines elided]…
> temp-word. Can someone help please. Thanks

Move SPACE to WORD-ARRAY
Move 1 to U-POINT.
Perform varying INDX from 1 by 1 until INDX > MAXWORDS
   Unstring MYTEXT delimited by ALL SPACE into WORD(INDX)
       with pointer U-POINT
   If WORD(INDX) not equal SPACE
      Move INDX to NUM-WORDS
      End-if
End-Perform.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
