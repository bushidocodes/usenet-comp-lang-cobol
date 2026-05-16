[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMPUTE with negative value and unsigned destination

_4 messages · 4 participants · 2005-02_

---

### COMPUTE with negative value and unsigned destination

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2005-02-09T23:16:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<420b0adc$1_1@127.0.0.1>`

```
2005-02-09T23:06-08:00

What does COBOL 85 (or COBOL 2002 for that matter) say about the behavior of
this program?

-----cut here-----
 IDENTIFICATION DIVISION.
 PROGRAM-ID. COBTEST.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01  A   PIC 99      VALUE 23.
 01  B   PIC S99     VALUE -7.
 PROCEDURE DIVISION.
 BEGIN.
     COMPUTE A = B
         ON SIZE ERROR     DISPLAY "SIZE ERROR"
         NOT ON SIZE ERROR DISPLAY "NOT SIZE ERROR"
     END-COMPUTE
     DISPLAY "A = " A
     STOP RUN.
 END PROGRAM COBTEST.
-----cut here-----

As I read the standard, a size error condition does not exist.  However, I
can't find anything that says what happens when a negative value is assigned
to an unsigned numeric data item.  With a MOVE statement, it's very clear
that the absolute value is stored.  I can't find where it says that for
COMPUTE.

The compiler I use displays "NOT SIZE ERROR" and "A = 07".  Does the
standard actually require that?  Where?

Walter



----== Posted via Newsfeeds.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

#### ↳ Re: COMPUTE with negative value and unsigned destination

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-10T16:32:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B0MOd.1447379$B07.212035@news.easynews.com>`
- **References:** `<420b0adc$1_1@127.0.0.1>`

```
For the '02 Standard, check out

A) Rule 4b on page 402
       and
B) GR(1) on page 431

To me, these mean that one does a "store" (move) and just use the absolute 
value.  However, I won't swear to this - and certainly won't swear it works this 
way in the '85 Standard.
```

#### ↳ Re: COMPUTE with negative value and unsigned destination

- **From:** "Ron" <NoSpam@SpamStopper.Org>
- **Date:** 2005-02-10T21:17:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lrqdnVsaWvFVvpHfRVn_vA@giganews.com>`
- **References:** `<420b0adc$1_1@127.0.0.1>`

```
> What does COBOL 85 (or COBOL 2002 for that matter) say about the behavior of
> this program?
>
> -----cut here-----

Since programming in the 70's I've always understood that data is stored
according to the format of the receiving field. Since A is PIC 99 no sign can
be stored therefore A will = 07. This is a very common defect in many programs
that I've repaired innumerable times when users have complained that their reports
"don't add up".

Editorial Comment: Always, always, always use S on the picture clause of every
numeric field that can possibly be used in a calculation or that represents a numeric
quantity. Always, have a sign on the picture clause of every numeric field that prints.
Never mind that you're told the field "won't be negative". Someday it will be negative,
and you'll save yourself hours of headaches trying to find the lone negative quantity
that's screwing up your report or file. The only exception should be data elements that
logically cannot be negative, like a phone number or a date.
```

##### ↳ ↳ Re: COMPUTE with negative value and unsigned destination

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2005-02-11T13:03:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1108155807.326596.201990@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<lrqdnVsaWvFVvpHfRVn_vA@giganews.com>`
- **References:** `<420b0adc$1_1@127.0.0.1> <lrqdnVsaWvFVvpHfRVn_vA@giganews.com>`

```

Ron wrote:
> > What does COBOL 85 (or COBOL 2002 for that matter) say about the
behavior of
> > this program?
> >
> > -----cut here-----
>
> Since programming in the 70's I've always understood that data is
stored
> according to the format of the receiving field. Since A is PIC 99 no
sign can
> be stored therefore A will = 07. This is a very common defect in many
programs
> that I've repaired innumerable times when users have complained that
their reports
> "don't add up".
>
> Editorial Comment: Always, always, always use S on the picture clause
of every
> numeric field that can possibly be used in a calculation or that
represents a numeric
> quantity. Always, have a sign on the picture clause of every numeric
field that prints.
> Never mind that you're told the field "won't be negative". Someday it
will be negative,
> and you'll save yourself hours of headaches trying to find the lone
negative quantity
> that's screwing up your report or file. The only exception should be
data elements that
> logically cannot be negative, like a phone number or a date.


I fully agree

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
