[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# data reference error 104

_3 messages · 2 participants · 2001-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### data reference error 104

- **From:** "MadG" <patrick4133@hotmail.com>
- **Date:** 2001-03-11T18:21:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<omPq6.14150$p66.5009066@news3.rdc1.on.home.com>`

```
I don't understand the descriptions that I have found of this error.
It appears in the following code when I divide in 110-CALCULATE-REG-PAY

Do I need to post the calling code as well?

Pat.


 01 JOB-VARIABLES.
   05 BI-MONTH  PIC 99 VALUE 26.

 LINKAGE SECTION.
        01 LS-ANNUAL-SALARY PIC 9(6)V99.
 01 LS-REG-PAY  PIC 9(5)V99.

 PROCEDURE DIVISION USING LS-ANNUAL-SALARY LS-REG-PAY.

 000-PRODUCE-REG-PAY-SALARY.
  PERFORM 110-CALCULATE-REG-PAY
  PERFORM 120-WRAP-UP.

 110-CALCULATE-REG-PAY.
  DIVIDE LS-ANNUAL-SALARY BY
  BI-MONTH GIVING LS-REG-PAY.
```

#### ↳ Re: data reference error 104

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-03-12T08:32:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AAC89AD.52F1508D@Azonic.co.nz>`
- **References:** `<omPq6.14150$p66.5009066@news3.rdc1.on.home.com>`

```
MadG wrote:
> 
> I don't understand the descriptions that I have found of this error.
> It appears in the following code when I divide in 110-CALCULATE-REG-PAY

>  PROCEDURE DIVISION USING LS-ANNUAL-SALARY LS-REG-PAY.
> 
…[6 more quoted lines elided]…
>   BI-MONTH GIVING LS-REG-PAY.

You haven't indicated what 120-Wrap-Up does.  Assuming that it does not
much then the code starts executing at PROCEDURE DIVISION, does the
perform 110-.. (and the code therein) does the perform 120- (and the
code therein) and then the next staement executed is ?

You would probably like to say 'it returns because that it what I want
it to do'.  But you haven't told it to do that so it executes the next
available statement (DIVIDE) and then whatever follows until end of
source code.

The 104 error is most likely a completely spurious one caused by
overwriting data.  You probably don't have matching sizes for the passed
parameters of the calling program may have these in LINKAGE (which is
probably wrong).
```

##### ↳ ↳ Re: data reference error 104

- **From:** "MadG" <patrick4133@hotmail.com>
- **Date:** 2001-03-11T19:34:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lrQq6.14349$p66.5153958@news3.rdc1.on.home.com>`
- **References:** `<omPq6.14150$p66.5009066@news3.rdc1.on.home.com> <3AAC89AD.52F1508D@Azonic.co.nz>`

```
YEP, IT WAS THE SIZE.

I caught it a minute before I checked back here.

Thanks Richard!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
