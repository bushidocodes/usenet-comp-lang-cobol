[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A cobol question

_6 messages · 6 participants · 1995-03_

---

### A cobol question

- **From:** "mayer goldberg" <ua-author-4361383@usenetarchives.gap>
- **Date:** 1995-03-06T23:25:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
I have a rather elementary question in COBOL; please forgive me, I'm
still picking up the language.

How do I refer to the n'th ascii or ebcdic character? The problem
came up while learning about sequential files, and creating some
simple ones, and wanting to put the newline char as the last field in
a record, so that I would get each record on a separate line ... But
in general, I would like to have access to the entire ascii char set.

Thanks,

Mayer
Mayer Goldberg

Email:	ma··.@cs.··a.edu
	ma··.@ucs··a.edu

URL: http://www.cs.indiana.edu/hyplan/mayer.html

Department of Computer Science,
Indiana University
Bloomington, Indiana 47405
U.  S.  A.
```

#### ↳ Re: A cobol question

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-03-07T09:39:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d35b76d8af-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`
- **References:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
Mayer Goldberg (ma··.@cs.··a.edu) wrote:
: I have a rather elementary question in COBOL; please forgive me, I'm
: still picking up the language.

: How do I refer to the n'th ascii or ebcdic character? The problem
: came up while learning about sequential files, and creating some
: simple ones, and wanting to put the newline char as the last field in
: a record, so that I would get each record on a separate line ... But
: in general, I would like to have access to the entire ascii char set.

: Thanks,

: Mayer
: --
: Mayer Goldberg

Use the CHAR function.

Example:

move function char(10) to outrec(80,1).

This moves a binary byte value of 10 to position 80 of outrec.
(this is an ANSI 85 addition)
```

#### ↳ Re: A cobol question

- **From:** "richard_..." <ua-author-17073823@usenetarchives.gap>
- **Date:** 1995-03-07T14:28:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d35b76d8af-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`
- **References:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
In message <<199··.@new··a.edu>> "Mayer Goldberg" writes:
› still picking up the language. 
› 
…[5 more quoted lines elided]…
› 
If you use LINE SEQUENTIAL the file will be variable length wil
with line terminators of CR-LF or LF depending on environment
and/or setting of a switch (with MF).

MF and MS allow use of hex characters as x"0D", x"0A" or even
x"0D0A".

There is a SPECIAL-NAMES entry which allows one to set up
symbolic names for particular character values which can
then be used in a similar way to SPACES, QUOTES, etc.

You can use COMPUTATIONAL fields to create a group field with
any character values required such as:

01 CR-LF.
03 FILLER PIC 99 COMP VALUE 13.
03 FILLER PIC 99 COMP VALUE 10.
```

#### ↳ Re: A cobol question

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-03-07T15:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d35b76d8af-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`
- **References:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
In article <199··.@new··a.edu>
"Mayer Goldberg" writes:

›
› I have a rather elementary question in COBOL; please forgive me, I'm
› still picking up the language.
›
› How do I refer to the n'th ascii or ebcdic character? The problem

Hi: I would use the special-names in the environment division.
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. ITSY-BITSY-MACHINE.
OBJECT-COMPUTER. I-OBJECT.
SPECIAL-NAMES.
ALPHABET COB-EBCDIC IS EBCDIC
ALPHABET COB-ASCII IS ASCII
SYMBOLIC CHARACTERS ASCII-LINE-FEED IS 11 IN COB-ASCII.

Later in the program....
MOVE ASCII-LINE-FEED TO WS-END-OF-REC.
MOVE WS-REC TO FD-REC-OUT.
WRITE FD-REC-OUT.
In the good old days, before I had the above to work with,
I would code a comp field and put the numeric value in it, and
then do a redefine:
01 WS-UGLY-CONSTANTS.
05 WS-ASCII-LINE-FEED-COMP PIC S9(04) VALUE 10.
05 WS-ASCII-LINE-FEED-REDEF REDEFINES WS-ASCII-LINE-FEED-COMP.
10 FILLER PIC X.
10 WS-ASCII-LINE-FEED PIC X.

Move Ws-ascii-line-feed to whatever...

Gross, No?


Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

#### ↳ Re: A cobol question

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-03-07T18:56:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d35b76d8af-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`
- **References:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
Mayer Goldberg (ma··.@cs.··a.edu) wrote:
: I have a rather elementary question in COBOL; please forgive me, I'm
: still picking up the language.

: How do I refer to the n'th ascii or ebcdic character? The problem
: came up while learning about sequential files, and creating some
: simple ones, and wanting to put the newline char as the last field in
: a record, so that I would get each record on a separate line ... But
: in general, I would like to have access to the entire ascii char set.

: Thanks,

: Mayer
: --
: Mayer Goldberg

: Email: ma··.@cs.··a.edu
: ma··.@ucs··a.edu

: URL: http://www.cs.indiana.edu/hyplan/mayer.html

: Department of Computer Science,
: Indiana University
: Bloomington, Indiana 47405
: U. S. A.

01 Char-String.
02 CS-Char PIC X OCCURS ### TIMES.

Any character in Char-String can be individually referenced as
CS-Char(number)

If you wish to refer to its numeric value, try the following.

01 NUM-VAL PIC S9(5) COMP-1.
01 NV REDEFINES NUM-VAL.
02 FILLER PIC X.
02 NV-CHAR PIC X.

Move 0 into NUM-VAL, move the character into NV-CHAR, refer to numeric
value in NUM-VAL.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

#### ↳ Re: A cobol question

- **From:** "t..." <ua-author-15731627@usenetarchives.gap>
- **Date:** 1995-03-07T21:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d35b76d8af-p6@usenetarchives.gap>`
- **In-Reply-To:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`
- **References:** `<1995Mar7.042516.15255@news.cs.indiana.edu>`

```
In article <199··.@new··a.edu>,
"Mayer Goldberg" wrote:
› I have a rather elementary question in COBOL; please forgive me, 
› I'm
…[13 more quoted lines elided]…
› Mayer

You could simply move the hex value (0A in your case) to whatever
PIC X variable - MOVE X"0A" TO pic-x-var.

Tim Mitchell
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
