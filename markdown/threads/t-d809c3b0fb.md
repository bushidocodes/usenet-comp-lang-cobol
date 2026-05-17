[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sample cobol programs

_18 messages · 11 participants · 1996-06 → 1996-07_

---

### Sample cobol programs

- **From:** "jack..." <ua-author-10465762@usenetarchives.gap>
- **Date:** 1996-06-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4qcldh$lf3@news-e2c.gnn.com>`

```

Does anyone know where I can acquire some ready to
compile cobol sample programs(for a beginner).
Thanks,
Chris Newton
```

#### ↳ Re: Sample cobol programs

- **From:** "juan manuel urraburu" <ua-author-17084485@usenetarchives.gap>
- **Date:** 1996-06-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4qcldh$lf3@news-e2c.gnn.com>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com>`

```

Take a look at
http://ourworld.compuserve.com/homepages/Juan_Urraburu_2/archs.htm

Regards,

Juan Manuel Urraburu
pro··.@adi··m.uy
```

#### ↳ Re: Sample cobol programs

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1996-07-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4qcldh$lf3@news-e2c.gnn.com>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com>`

```

jac··.@g··.com (Christopher J Newton) wrote:

› Does anyone know where I can acquire some ready to
› compile cobol sample programs(for a beginner).
› Thanks,
› Chris Newton

More than slightly tongue in cheek, but yet a program that will
compile -- see http://www.ccsnet.com/falmouth/ and find the sample
program posted by a somewhat twisted (from too much COBOL) individual.

It's in the data processing department which is linked off the main
page right after the e-mail address.

George Trudeau, Systems Analyst (COBOL!), Town of Falmouth

"E-Mail so interesting, it doesn't need a tag line."
```

##### ↳ ↳ Re: Sample cobol programs

- **From:** "rayg..." <ua-author-1603681@usenetarchives.gap>
- **Date:** 1996-07-03T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p3@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap>`

```

gtr··.@ca··e.com (George Trudeau) wrote:


› More than slightly tongue in cheek, but yet a program that will
› compile -- see http://www.ccsnet.com/falmouth/ and find the sample
› program posted by a somewhat twisted (from too much COBOL) individual.
 
› It's in the data processing department which is linked off the main
› page right after the e-mail address.
 
› George Trudeau, Systems Analyst (COBOL!), Town of Falmouth

That program is missing the Environment and Data Divisions.

(Unless COBOL on PCs doesn't need them? I'm a Mainframe guy myself.)


Curly: "Gimme some burnt toast and a rotten egg!"
Larry: "Burnt toast and a rotten egg?!"
Curly: "Yeah, I got a tapeworm and that's good enough for 'im!!"
-------------------------------------
Raymond F. Greenberg
```

###### ↳ ↳ ↳ Re: Sample cobol programs

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p4@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap>`

```

ray··.@po··d.com (Raymond F. Greenberg) wrote:


› That program is missing the Environment and Data Divisions.
 
› (Unless COBOL on PCs doesn't need them? I'm a Mainframe guy myself.)

Raymond, as far as I know that program is legal COBOL. I think that
some of IBM's older compilers will choke on it, but I put all the
warnings and standards flaggers on high with Digital's OpenVMS COBOL
compiler and it came up clean.

Perhaps someone with a copy of the standard can tell us if the
Environment and Data Divisions are required if null.

George Trudeau
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 4)_

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-07-11T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p5@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap>`

```

gtr··.@ca··e.com (George Trudeau) wrote:
› ray··.@po··d.com (Raymond F. Greenberg) wrote:
› 
…[14 more quoted lines elided]…
› 
I believe that the headers must be there, but the divisions may be empty.
Am I right, Don?

Doug Miller
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 5)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-07-11T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p6@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap>`

```

Doug Miller wrote:
›› I believe that the headers must be there, but the divisions may be empty.
› Am I right, Don?

Nope. You can write a program with nothing but the following
according to the current standard (1985 with addenda):

IDENTIFICATION DIVISION.
PROGRAM-ID. whatever.
PROCEDURE DIVISION.
paragraph-name.
DISPLAY "small program"
.

Actually, you can leave out the procedure division, but it makes no
sense.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 6)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-14T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p7@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap>`

```

Don Nelson wrote:

› Nope.  You can write a program with nothing but the following 
› according to the current standard (1985 with addenda):
 
› IDENTIFICATION DIVISION.
› PROGRAM-ID.  whatever.
…[3 more quoted lines elided]…
›    .
 
› Actually, you can leave out the procedure division, but it makes no 
› sense.

It's more like "paragraph-name." can be left out, but PROCEDURE
DIVISION is required.

I maybe wrong
Boyce
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 7)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-07-14T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p8@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
›› Actually, you can leave out the procedure division, but it makes no
…[5 more quoted lines elided]…
› I maybe wrong

Sorry, Boyce, but you are wrong. The entire Procedure Division is
optional. If you do specify the PROCEDURE DIVISION header, you must
specify a paragraph-name (or section-name).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 8)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-15T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p9@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap>`

```

I compiled and ran the following program on COBOL/370 to test the need
for a paragraph-name within the PROCEDURE DIVISION. It worked OK.

000100 IDENTIFICATION DIVISION.

000200 PROGRAM-ID. CBL0085.

000300 ENVIRONMENT DIVISION.

000400 CONFIGURATION SECTION.

000500 SOURCE-COMPUTER. IBM-370.

000600 OBJECT-COMPUTER. IBM-370.

000700 PROCEDURE DIVISION.

000800 DISPLAY 'HELLO WORLD'

000900 STOP RUN

001000 .


Boyce Williams
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 9)_

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1996-07-15T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p10@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap>`

```

Boyce G. Williams, Jr. (bow··.@gem··u.edu) wrote:
: I compiled and ran the following program on COBOL/370 to test the need
: for a paragraph-name within the PROCEDURE DIVISION. It worked OK.

: 000100 IDENTIFICATION DIVISION.
: 000200 PROGRAM-ID. CBL0085.
: 000300 ENVIRONMENT DIVISION.
: 000400 CONFIGURATION SECTION.
: 000500 SOURCE-COMPUTER. IBM-370.
: 000600 OBJECT-COMPUTER. IBM-370.
: 000700 PROCEDURE DIVISION.
: 000800 DISPLAY 'HELLO WORLD'
: 000900 STOP RUN
: 001000 .

This program does not conform to the COBOL standard. Boyce has
demonstrated that a particular release of a particular compiler,
invoked in a particular way, accepted a particular non-conforming
program, and that it appeared to work as he expected it to. This
is one data point. There are other compilers that will reject
this program.

It is common for compilers to have quirks like this. The more
a programmer takes advantage of such quirks, the more difficult
it will be to port the code to a different compiler, or even,
sometimes, to a future release of the same compiler.

Walter Murray
Hewlett-Packard
Support Technology Lab
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 10)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-16T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p11@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap> <gap-d809c3b0fb-p11@usenetarchives.gap>`

```

wal··.@hpr··p.com (Walter Murray) wrote:

› Boyce G. Williams, Jr. (bow··.@gem··u.edu) wrote:
› : I compiled and ran the following program on COBOL/370 to test the need
› : for a paragraph-name within the PROCEDURE DIVISION.  It worked OK.
 
› : 000100 IDENTIFICATION DIVISION.
› : 000200 PROGRAM-ID.    CBL0085.
…[7 more quoted lines elided]…
› : 001000         .
 
› This program does not conform to the COBOL standard.  Boyce has
› demonstrated that a particular release of a particular compiler,
…[3 more quoted lines elided]…
› this program.
 
› It is common for compilers to have quirks like this.  The more
› a programmer takes advantage of such quirks, the more difficult
› it will be to port the code to a different compiler, or even,
› sometimes, to a future release of the same compiler.

What's not conforming?

Boyce Williams
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 11)_

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1996-07-17T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p12@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap> <gap-d809c3b0fb-p11@usenetarchives.gap> <gap-d809c3b0fb-p12@usenetarchives.gap>`

```

Boyce G. Williams, Jr. (bow··.@gem··u.edu) wrote:

: wal··.@hpr··p.com (Walter Murray) wrote:

: >Boyce G. Williams, Jr. (bow··.@gem··u.edu) wrote:

: >: I compiled and ran the following program on COBOL/370 to test the need
: >: for a paragraph-name within the PROCEDURE DIVISION. It worked OK.

: >: [a program with a Procedure Division but no paragraph-name]

: >This program does not conform to the COBOL standard.
: >[snip]

: What's not conforming?

The fact that there's no paragraph-name in the Procedure Division.

As I recall, the question was whether the paragraph-name could
be omitted. Don Nelson pointed out, correctly, that it was
required. You pointed out that COBOL/370 would accept a program
without one. My point was that, regardless of whether COBOL/370
accepts it, the COBOL standard says that your sample program is
illegal, and you should not expect it to work with other compilers.

If you want chapter and verse from the standard, it's in X3.23-1985,
page IV-36, paragraph 6.4.1.4.2.

Walter Murray
Hewlett-Packard
Support Technology Lab
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 12)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-18T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p13@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap> <gap-d809c3b0fb-p11@usenetarchives.gap> <gap-d809c3b0fb-p12@usenetarchives.gap> <gap-d809c3b0fb-p13@usenetarchives.gap>`

```

wal··.@hpr··p.com (Walter Murray) wrote:


› The fact that there's no paragraph-name in the Procedure Division.
 
› As I recall, the question was whether the paragraph-name could
› be omitted.  Don Nelson pointed out, correctly, that it was
…[3 more quoted lines elided]…
› illegal, and you should not expect it to work with other compilers.
 
› If you want chapter and verse from the standard, it's in X3.23-1985,
› page IV-36, paragraph 6.4.1.4.2.
 
› Walter Murray
› Hewlett-Packard
› Support Technology Lab

Does IBM know about this?
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 13)_

- **From:** "joe kline" <ua-author-8716933@usenetarchives.gap>
- **Date:** 1996-07-22T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p14@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap> <gap-d809c3b0fb-p11@usenetarchives.gap> <gap-d809c3b0fb-p12@usenetarchives.gap> <gap-d809c3b0fb-p13@usenetarchives.gap> <gap-d809c3b0fb-p14@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:

›› If you want chapter and verse from the standard, it's in X3.23-1985,
›› page IV-36, paragraph 6.4.1.4.2.
…[3 more quoted lines elided]…
› Does IBM know about this?

Probably not! but if they did I'm sure they'd drop
everything...including the 'big fix' currently going on in Atlanta
(Olympics)... to address this egregious violation. Walt I think a Noble
Prize is in order.
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 11)_

- **From:** "alain chappuis" <ua-author-17072993@usenetarchives.gap>
- **Date:** 1996-07-17T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p12@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p10@usenetarchives.gap> <gap-d809c3b0fb-p11@usenetarchives.gap> <gap-d809c3b0fb-p12@usenetarchives.gap>`

```

Boyce G. Williams, Jr. wrote:
› 
› wal··.@hpr··p.com (Walter Murray) wrote:
…[4 more quoted lines elided]…
› 

Mieux, in my example i have only 6 lines:

Identification Division.
Program-id. Petit.
Procedure Division.
Begin.
Display "Hello world"
Stop run.
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 8)_

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-15T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p9@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap>`

```

Don Nelson wrote:

› Boyce G. Williams, Jr. wrote:
›› 
…[6 more quoted lines elided]…
›› I maybe wrong
 
› Sorry, Boyce, but you are wrong.  The entire Procedure Division is 
› optional.  If you do specify the PROCEDURE DIVISION header, you must 
› specify a paragraph-name (or section-name).

Hmm, I compiled and ran a program with no paragraph-names in it and it
ran OK like the following seqment:

PROCEDURE DIVISION.
DISPLAY 'HELLO WORLD'
STOP RUN
.

Of course, it was on an IBM MVS mainframe with OS/VS COBOL. I'll
double check this with the new COBOL/370 we just got.

I have an idea. Since so many folks (mostly C programmers) complain
about the verbose nature of COBOL, let's see who can write the
shortest operational COBOL program. Mind you, it must compile cleanly
and run cleanly. Producing something is not an requirement.

Have a bandit day,
Boyce Williams
```

###### ↳ ↳ ↳ Re: Sample cobol programs

_(reply depth: 9)_

- **From:** "mor..." <ua-author-4892761@usenetarchives.gap>
- **Date:** 1996-07-15T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d809c3b0fb-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d809c3b0fb-p17@usenetarchives.gap>`
- **References:** `<4qcldh$lf3@news-e2c.gnn.com> <gap-d809c3b0fb-p3@usenetarchives.gap> <gap-d809c3b0fb-p4@usenetarchives.gap> <gap-d809c3b0fb-p5@usenetarchives.gap> <gap-d809c3b0fb-p6@usenetarchives.gap> <gap-d809c3b0fb-p7@usenetarchives.gap> <gap-d809c3b0fb-p8@usenetarchives.gap> <gap-d809c3b0fb-p9@usenetarchives.gap> <gap-d809c3b0fb-p17@usenetarchives.gap>`

```

At least on any of the IBM 360/390 class compilers and those that support
the dialect you should be able to get away with:
ID DIVISION.
Program-id. S.
Procedure Division.
DISPLAY 'HELLO WORLD'

The STOP RUN is optional. The IBM compiler I use (VS COBOL II) just
issues a warning message regarding the lack of paragraph name.

› PROCEDURE DIVISION.
› DISPLAY 'HELLO WORLD'
…[12 more quoted lines elided]…
› Boyce Williams 


Clark F. Morris, Jr.
on assignment in St. John, New Brunswick, Canada - mor··.@nbn··b.ca
506-657-9331
at home in Bridgetown, Nova Scotia, Canada - cmo··.@fox··n.ca
902-665-4006
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
