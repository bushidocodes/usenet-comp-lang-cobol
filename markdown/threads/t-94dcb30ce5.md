[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: Checking for lower and upper case data

_5 messages · 5 participants · 1996-08_

---

### Q: Checking for lower and upper case data

- **From:** "scott wilt" <ua-author-17086935@usenetarchives.gap>
- **Date:** 1996-08-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3224B691.3BBC@jcpenney.com>`

```

I am writing a COBOL 370 pgm that will do some edit checking on
an input string. In this case the string is a description that
will appear on an invoice for a particular item. I want to
ensure that the string has both upper and lower case as it comes
in - not all upper or all lower. If it is not mixed case I want
the string to error out.

Can you think of a way in COBOL to check for this? I am aware of
the islower() and isupper() functions in C. Is there anything
like this for COBOL?
```

#### ↳ Re: Q: Checking for lower and upper case data

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1996-08-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94dcb30ce5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3224B691.3BBC@jcpenney.com>`
- **References:** `<3224B691.3BBC@jcpenney.com>`

```

Scott Wilt (swi··.@jcp··y.com) wrote:

: I am writing a COBOL 370 pgm that will do some edit checking on
: an input string. In this case the string is a description that
: will appear on an invoice for a particular item. I want to
: ensure that the string has both upper and lower case as it comes
: in - not all upper or all lower. If it is not mixed case I want
: the string to error out.

: Can you think of a way in COBOL to check for this?

If execution time is a concern, you probably want to "roll your own"
using the class conditions ALPHABETIC-LOWER and ALPHABETIC-UPPER.
But for something quick and dirty, try the intrinsic functions.

Sample code follows. It's standard COBOL, but I don't know whether
your compiler implements the Intrinsic Function module. If not,
never mind.

Walter Murray
Hewlett-Packard
Support Technology Lab

----------------------------------------------------------------------
IDENTIFICATION DIVISION.
PROGRAM-ID. EXAMPLE.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 TEST-STRING PIC X(20).
PROCEDURE DIVISION.
BEGIN.
MOVE "ABC DEF*" TO TEST-STRING, PERFORM DO-TEST
MOVE "pqr stu+" TO TEST-STRING, PERFORM DO-TEST
MOVE "This OK?" TO TEST-STRING, PERFORM DO-TEST
STOP RUN.
DO-TEST.
*
* Make sure TEST-STRING contains at least one
* lowercase letter and at least one uppercase
* letter.
*
DISPLAY "TESTING """ TEST-STRING """ ... " NO ADVANCING
IF TEST-STRING NOT =
FUNCTION LOWER-CASE (TEST-STRING) AND
FUNCTION UPPER-CASE (TEST-STRING)
DISPLAY "OK"
ELSE
DISPLAY "*** BAD ***"
END-IF.
END PROGRAM EXAMPLE.
----------------------------------------------------------------------
```

#### ↳ Re: Q: Checking for lower and upper case data

- **From:** "glenn a. mitchell" <ua-author-17072865@usenetarchives.gap>
- **Date:** 1996-08-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94dcb30ce5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3224B691.3BBC@jcpenney.com>`
- **References:** `<3224B691.3BBC@jcpenney.com>`

```

Scott Wilt wrote:
› 
› I am writing a COBOL 370 pgm that will do some edit checking on
…[8 more quoted lines elided]…
› like this for COBOL?

I assume that the ALPHABETIC-UPPER and ALPHABETIC-LOWER class tests will
not do the trick because you expect something other than letters and the
space character (like punctuation!). An approach that will work (if
your COBOL is at the ANSI85 level with the intrinsic function module
approved in 1989) is to up-shift the input and compare it to the
original input. If it is the same, it obviously was all uppercase to
start with. Similarly, down-shift it to test for lower-case. The
intrinsic functions to use are UPPER-CASE and LOWER-CASE. If your COBOL
is not at that level, you could probably achieve the same result using
an INSPECT . . . CONVERTING to do the shifting.

Glenn A. Mitchell               mailto:mit··.@poa··c.org
Director, Computer Technology   http://www.mmc.org
Maine Medical Center            
Portland, ME  04101
```

##### ↳ ↳ Re: Q: Checking for lower and upper case data

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1996-08-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94dcb30ce5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-94dcb30ce5-p3@usenetarchives.gap>`
- **References:** `<3224B691.3BBC@jcpenney.com> <gap-94dcb30ce5-p3@usenetarchives.gap>`

```

› Scott Wilt wrote:
›› 
…[9 more quoted lines elided]…
›› like this for COBOL?

Here's another COBOL way to do it -- I'm assuming you want period,
comma, hyphen, space, and the alphabet.

identification division.
program-id. upcase.
environment division.
configuration section.
special-names.
class low-case is "a" thru "z" "." "," "-" " "
class up-case is "A" thru "Z" "." "," "-" " ".
data division.
working-storage section.
1 indata pic x(30).
procedure division.
begin.
accept indata
evaluate true
when indata low-case display "It's lower case"
when indata up-case display "It's upper case"
when other display "It's something else"
end-evaluate
stop run.

George Trudeau, Town of Falmouth
```

#### ↳ Re: Q: Checking for lower and upper case data

- **From:** "fr..." <ua-author-16633589@usenetarchives.gap>
- **Date:** 1996-08-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-94dcb30ce5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3224B691.3BBC@jcpenney.com>`
- **References:** `<3224B691.3BBC@jcpenney.com>`

```

In article <322··.@jcp··y.com>, Scott Wilt writes:
› I am writing a COBOL 370 pgm that will do some edit checking on 
› an input string.  In this case the string is a description that 
…[7 more quoted lines elided]…
› like this for COBOL?
IBM Cobol for MVS +VM (Release 2 of Cobol/370) has intrinsic upper-case and
lower case functions. So you could code:
IF Input-String equal Function Upper-Case(Input-String)
OR Input-String equal Function Lower-Case(Input-String)
Perform Error-Parargraph
END-IF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
