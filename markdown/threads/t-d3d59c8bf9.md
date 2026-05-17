[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How is cobol binary data stored?

_7 messages · 5 participants · 1997-12_

---

### How is cobol binary data stored?

- **From:** "g..." <ua-author-17071301@usenetarchives.gap>
- **Date:** 1997-12-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`

```

Hi, cobol gurus,
I need to exchange data between DEC digital UNIX cobol and DEC fortran77.
I know i can always use ascii/text file to build the bridge, but that
will lose precision and take more disk space. I have tried usage
(binary, computational) and then write this field to a file, but fortran
wouldn't read it. on the other hand, the unformatted (binary) fortran
output doesn't suit cobol(usage is binary) either.
I am more familiar with fortran and I know the fortran binary output
is quite portable across platforms, except for big_endian/little_endian
problem. I wish someone could tell me how cobol stores its binary
data.
guoqing
```

#### ↳ Re: How is cobol binary data stored?

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`

```

In article <66clfd$ecq$1.··.@cor··n.ca>,
g.··.@mor··n.ca (Guoqing Li) wrote:
› 
› I need to exchange data between DEC digital UNIX cobol and DEC
…[8 more quoted lines elided]…
› problem.  I wish someone could tell me how cobol stores its binary data.

ForTran CoBOL

INTEGER*1, LOGICAL*1 PIC X(1)
INTEGER*2, LOGICAL*2 PIC S9(4) COMP
INTEGER*4, LOGICAL*4 PIC S9(9) COMP
REAL*4 COMP-1
REAL*8 COMP-2

NB: For REAL*8 and COMP-2 you use compiler options to choose D_FLOATING
or G_FLOATING. Be sure to use the _same_ compiler option on the CoBOL
program and the ForTran program!

It may be you are having trouble with the ForTran unformatted file rather
than with the data itself. See Appendix C of the ForTran user manual for
help on how to use a ForTran unformatted file with other languages.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: How is cobol binary data stored?

- **From:** "g..." <ua-author-17071301@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3d59c8bf9-p2@usenetarchives.gap>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca> <gap-d3d59c8bf9-p2@usenetarchives.gap>`

```

Chris Westbury (cwe··.@gia··t.com) wrote:
: In article <66clfd$ecq$1.··.@cor··n.ca>,
: g.··.@mor··n.ca (Guoqing Li) wrote:
: >
: > I need to exchange data between DEC digital UNIX cobol and DEC
: > fortran77. I know i can always use ascii/text file to build the
: > bridge, but that will lose precision and take more disk space. I have
: > tried usage (binary, computational) and then write this field to a
: > file, but fortran wouldn't read it. on the other hand, the unformatted
: > (binary) fortran output doesn't suit cobol (usage is binary) either.
: >
: > I am more familiar with fortran and I know the fortran binary output is
: > quite portable across platforms, except for big_endian/little_endian
: > problem. I wish someone could tell me how cobol stores its binary data.

: ForTran CoBOL

: INTEGER*1, LOGICAL*1 PIC X(1)
: INTEGER*2, LOGICAL*2 PIC S9(4) COMP
: INTEGER*4, LOGICAL*4 PIC S9(9) COMP
: REAL*4 COMP-1
: REAL*8 COMP-2

: NB: For REAL*8 and COMP-2 you use compiler options to choose D_FLOATING
: or G_FLOATING. Be sure to use the _same_ compiler option on the CoBOL
: program and the ForTran program!

: It may be you are having trouble with the ForTran unformatted file rather
: than with the data itself. See Appendix C of the ForTran user manual for
: help on how to use a ForTran unformatted file with other languages.


: --
: Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138

Thanks a lot. it works! I have tried for the integer cases. it works
fine, except for I have to put filler at the beginning and the end of
the record for fortran unformatted file to by-pass the bytecounts.
cobol binary file is more straightforward, like C.
guoqing
====================================================================
Guoqing Li, Department of Physics and Physical Oceanography
Memorial University of Newfoundland, St. John's, NF, A1B 3X7, Canada
Tel:(709)737-8888 Fax:(709)737-8739 ema··.@mor··n.ca
```

#### ↳ Re: How is cobol binary data stored?

- **From:** "george ewins" <ua-author-6589024@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`

```

For any interchange between systems don't try to cut corners you will screw
yourself or your employer in the long run. Use ASCII and make the sign
separate characters. Binary representation is up to the implementor (as are
embedded signs).

Guoqing Li wrote:
› 
› Hi, cobol gurus,
…[12 more quoted lines elided]…
› 

George Ewins
gew··.@u··.net
```

##### ↳ ↳ Re: How is cobol binary data stored?

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3d59c8bf9-p4@usenetarchives.gap>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca> <gap-d3d59c8bf9-p4@usenetarchives.gap>`

```

Just a tiny quibble, George, because I completely agree with you. Instead of
"Use ASCII", make that "Use DISPLAY". I suspect that was what you really
meant. Many mainframes use EBCDIC instead of ASCII.

George Ewins wrote in article <348··.@u··.net>...
› For any interchange between systems don't try to cut corners you will screw
› yourself or your employer in the long run.  Use ASCII and make the sign
…[15 more quoted lines elided]…
›› data.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: How is cobol binary data stored?

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-12-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca>`

```

Guoqing Li wrote in article
<66clfd$ecq$1.··.@cor··n.ca>...
› Hi, cobol gurus,
› I need to exchange data between DEC digital UNIX cobol and DEC fortran77.
…[9 more quoted lines elided]…
› guoqing
Sorry, but it depends on the platform. Most COBOL implementations try to
use what is native to the platform. Some even change this depending on
what compile options you select (compatibility with other platforms, etc.),
and which of the binary usages you select (e.g. COMP, COMP-4) which can
adjust size (2, 4 or 8 bytes), endian, etc. In general most COBOLs when
doing COMP binary fields will use a twos-complement with 2, 4 or 8 bytes
(small, medium or large...?), depending on the number of siginificant
digits. Example, PIC S9(04) COMP on IBM will be two-bytes, PIC S9(8) COMP
will be four-bytes, and PIC S9(15) COMP-4 will be eight-bytes.

However, your COBOL documentation should get *very* specific about this
stuff (like several pages with hex examples of each COMP usage variant).
If you don't have that documentation then you need to get it. And if you
want a better answer to this question then you will have to be a great deal
more specific in how you ask it. Tell us platform, compiler publisher and
version, and include the hex of what your FORTRAN compiler is expecting,
and someone can probably tell ou exactly what you want to know (presuming
you haven't, by then, already found it in the documentation...).
"There's a big difference between mostly dead, and all dead.  Please, open
his mouth."
    Miracle Max, "The Princess Bride"
```

##### ↳ ↳ Re: How is cobol binary data stored?

- **From:** "g..." <ua-author-17071301@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3d59c8bf9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3d59c8bf9-p6@usenetarchives.gap>`
- **References:** `<66clfd$ecq$1@coranto.ucs.mun.ca> <gap-d3d59c8bf9-p6@usenetarchives.gap>`

```

Gary Lee (nsp··.@nsp··p.com) wrote:
: Guoqing Li wrote in article
: <66clfd$ecq$1.··.@cor··n.ca>...
: > Hi, cobol gurus,
: > I need to exchange data between DEC digital UNIX cobol and DEC fortran77.
: > I know i can always use ascii/text file to build the bridge, but that
: > will lose precision and take more disk space. I have tried usage
: > (binary, computational) and then write this field to a file, but fortran
: > wouldn't read it. on the other hand, the unformatted (binary) fortran
: > output doesn't suit cobol(usage is binary) either.
: > I am more familiar with fortran and I know the fortran binary output
: > is quite portable across platforms, except for big_endian/little_endian
: > problem. I wish someone could tell me how cobol stores its binary
: > data.
: > guoqing
: Sorry, but it depends on the platform. Most COBOL implementations try to
: use what is native to the platform. Some even change this depending on
: what compile options you select (compatibility with other platforms, etc.),
: and which of the binary usages you select (e.g. COMP, COMP-4) which can
: adjust size (2, 4 or 8 bytes), endian, etc. In general most COBOLs when
: doing COMP binary fields will use a twos-complement with 2, 4 or 8 bytes
: (small, medium or large...?), depending on the number of siginificant
: digits. Example, PIC S9(04) COMP on IBM will be two-bytes, PIC S9(8) COMP
: will be four-bytes, and PIC S9(15) COMP-4 will be eight-bytes.

: However, your COBOL documentation should get *very* specific about this
: stuff (like several pages with hex examples of each COMP usage variant).
: If you don't have that documentation then you need to get it. And if you
: want a better answer to this question then you will have to be a great deal
: more specific in how you ask it. Tell us platform, compiler publisher and
: version, and include the hex of what your FORTRAN compiler is expecting,
: and someone can probably tell ou exactly what you want to know (presuming
: you haven't, by then, already found it in the documentation...).
: --
: "There's a big difference between mostly dead, and all dead. Please, open
: his mouth."
: Miracle Max, "The Princess Bride"

Thanks for the advice, unfortunately we don't have any cobol manual
and the supporting staff can not be of much help either. My compiler
is DEC COBOL V2.4 under digital UNIX(used to be OSF1) V4.0.
I will narrow my question to this: how does cobel read a binary file
created by fortran's open (unformatted) statement?
When fortran opens a file as unformatted, it assumes that records
are delimited at both ends by an integer bytecount. the first
bytecount is used to determine the number of bytes to read and the last
then becomes a simple data integrity check.
for instance, suppose a fortran unformatted file contains only an
integer 3.
"od" (octal dump, digital UNIX command) displays the file as
32-bit words 4 3 4 ( when declared as integer*4).
Now what cobol USAGE would read in this "3"?

-----------
"My Wesley will come to me."
Buttercup, "The Prince's Bride"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
