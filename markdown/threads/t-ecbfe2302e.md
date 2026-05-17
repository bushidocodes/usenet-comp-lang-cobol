[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question of MF, please readme

_7 messages · 7 participants · 1997-01_

---

### Question of MF, please readme

- **From:** "marcela godoy" <ua-author-17071734@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32D2BFDE.158D@tandem.cl>`

```

I am using MF COBOL V.3.2., how to obtain the true long of a string?
for example :

WORKING . . .
01 WS-FILLER PIC X(10).
.
.
.
PROCEDURE DIVISION
.
.
.
MOVE 'XXXX' TO WS-FILLER.
.
.
.


then, for that example the true long of "ws-filler" is 4. How to obtain that?
```

#### ↳ Re: Question of MF, please readme

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32D2BFDE.158D@tandem.cl>`
- **References:** `<32D2BFDE.158D@tandem.cl>`

```

Marcela Godoy wrote:
› 
› I am using MF COBOL V.3.2., how to obtain the true long of a string?
…[7 more quoted lines elided]…
› then, for that example the true long of "ws-filler" is 4. How to obtain that?

I don't have experience with MicroFocus COBOL compilers, but I can think of
a couple of ways to obtain the true length of the data.

01 WS-FILLER-LENGTH PIC 9(4) USAGE [any numeric type].
INSPECT WS-FILLER TALLYING WS-FILLER-LENGTH FOR CHARACTERS BEFORE SPACE.

The above example should work with IBM COBOL II or COBOL/370.

You could also redefine WS-FILLER as an array of bytes and count
characters until you encounter a SPACE or LOW-VALUE.

Don't try MOVE LENGTH OF WS-FILLER TO WS-FILLER-LENGTH, because that
returns the defined length of WS-FILLER (10 bytes) rather than the length
the meaningful contents.

I hope that helps!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Question of MF, please readme

- **From:** "tony heffner" <ua-author-6589464@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32D2BFDE.158D@tandem.cl>`
- **References:** `<32D2BFDE.158D@tandem.cl>`

```

Marcela Godoy wrote:
› 
› I am using MF COBOL V.3.2., how to obtain the true long of a string?
…[16 more quoted lines elided]…
› then, for that example the true long of "ws-filler" is 4. How to obtain that?

data division.
working-storage section.
01 counter pic 9(2) value zero.
01 ws-string pic x(10).

procedure division.
move "xxxx" to ws-string.
inspect ws-string tallying counter for characters.
display counter.
move zero to counter.
inspect ws-string tallying counter for characters
before initial space.
display counter.

This should work for ya. First inspect, entire length (you could get
this
through use of intrinsic function "length of"), second inspect what your
looking for.

Tony Heffner
ag··.@atl··p.com
```

#### ↳ Re: Question of MF, please readme

- **From:** "hans chr. enevoldsen" <ua-author-6589041@usenetarchives.gap>
- **Date:** 1997-01-10T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32D2BFDE.158D@tandem.cl>`
- **References:** `<32D2BFDE.158D@tandem.cl>`

```

Marcela Godoy wrote:
› 
› I am using MF COBOL V.3.2., how to obtain the true long of a string?
…[16 more quoted lines elided]…
› then, for that example the true long of "ws-filler" is 4. How to obtain that?
Here's a third version:

data division.
working-storage section.
01 counter pic 9(2) value zero.
01 ws-string pic x(10) value spaces.

procedure division.

move "xxxx" to ws-string
perform varying counter from 10 to 1 by -1
until ws-string(counter:1) > space
end-perform

The loop will examine from right to left and be terminated when the
rightmost 'x' is encountered, and counter will then contain the digit 4.
The implicit test is 'WITH TEST BEFORE', so Cobol evaluates the 'until'
condition before varying counter.

Best regards

Hans Chr. Enevoldsen
```

##### ↳ ↳ Re: Question of MF, please readme

- **From:** "virtua..." <ua-author-649846@usenetarchives.gap>
- **Date:** 1997-01-10T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ecbfe2302e-p4@usenetarchives.gap>`
- **References:** `<32D2BFDE.158D@tandem.cl> <gap-ecbfe2302e-p4@usenetarchives.gap>`

```

gee guys.
i know you like performs, and loops.
but cobol is over 30 years old.
dont you think they have figured out a better way?

try your cobol manual.
look up the word INSPECT



"Hans Chr. Enevoldsen" wrote:

› Marcela Godoy wrote:
›› 
…[18 more quoted lines elided]…
› Here's a third version:
 
›       data division.
›       working-storage section.
›       01  counter             pic  9(2)  value zero.
›       01  ws-string           pic  x(10) value spaces.
 
›       procedure division.
 
›           move "xxxx" to ws-string 
›           perform varying counter from 10 to 1 by -1
…[6 more quoted lines elided]…
› condition before varying counter.
 
› Best regards
 
› Hans Chr. Enevoldsen

*************************************************************************
Visit my webpage at (new address, please bookmark)
http://www.front.net/virtual.virgin/virtual.html-ssi
*************************************************************************
```

#### ↳ Re: Question of MF, please readme

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<32D2BFDE.158D@tandem.cl>`
- **References:** `<32D2BFDE.158D@tandem.cl>`

```

In message <<32D··.@tan··m.cl>> Marcela Godoy writes:
›
› then, for that example the true long of "ws-filler" is 4. How to obtain that?

MOVE "XYZ 123" TO Text-String
MOVE ZERO TO Trailing-Spaces
INSPECT FUNCTION REVERSE(Text-String)
TALLYING Trailing-Spaces FOR LEADING SPACES
COMPUTE String-Len = LENGTH OF Text-String - Trailing-Spaces


This does calculate 7 for the example, but if it takes more than
a few seconds to work out what it does and how then don't use it
but do something like:

PERFORM
VARYING String-Len FROM LENGTH OF Text-String BY -1
UNTIL String-Len < 1
OR Text-String(String-Len:1) NOT = SPACE

END-PERFORM
```

#### ↳ Re: Question of MF, please readme

- **From:** "dbma..." <ua-author-1810562@usenetarchives.gap>
- **Date:** 1997-01-16T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecbfe2302e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<32D2BFDE.158D@tandem.cl>`
- **References:** `<32D2BFDE.158D@tandem.cl>`

```

Marcela Godoy wrote:

› I am using MF COBOL V.3.2., how to obtain the true long of a string?
› for example :
› 
› WORKING . . .
› 01 WS-FILLER     PIC X(10).

I assume that you mean length. It depends on the version of Cobol
used. The generic ways is to write a routine that will search the
string backwards, eg. from the n'th to the 1'st char, and find the
first non-blank character. This would give you the length. Not the
best solution, but it works!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
