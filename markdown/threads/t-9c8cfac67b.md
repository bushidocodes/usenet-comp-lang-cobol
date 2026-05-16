[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Generating Random Numbers

_3 messages · 3 participants · 1998-12_

---

### Generating Random Numbers

- **From:** "Dennis Fyke" <DEFyke@aol.com>
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be2612$2b5dffc0$2c198318@default.mw.mediaone.net>`

```
Fujitsu Cobol has a Random function but I can't seem to get it to compile, 
does anyone know of a good method of generating random numbers?
```

#### ↳ Re: Generating Random Numbers

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3672e62f.0@news1.ibm.net>`
- **References:** `<01be2612$2b5dffc0$2c198318@default.mw.mediaone.net>`

```

Dennis Fyke wrote in message
<01be2612$2b5dffc0$2c198318@default.mw.mediaone.net>...
>Fujitsu Cobol has a Random function but I can't seem to get it to compile,
>does anyone know of a good method of generating random numbers?


go to http://www.etk.com then downloads, then ETKPAK, the
MATHPK routine generates random numbers. It is amazing how
often this question crops up.


To give you a feeling of what is involved, here is an excerpt:

017300 01  RANDOM-VARIABLES.
017400     02  RANDOM-PRECISION        PIC S9(7)  COMP  VALUE +9999999.
017500     02  RANDOM-INTEGER          PIC S9(7)  COMP  VALUE   ZERO.
017600     02  RANDOM-MODULUS          PIC S9(7)  COMP  VALUE +2099863.
017700     02  RANDOM-MULTIPLIER       PIC S9(7)  COMP  VALUE +1005973.
017800     02  RANDOM-INCREMENT        PIC S9(7)  COMP  VALUE  +443771.
017900     02  RANDOM-QUOTIENT         PIC S9(7)  COMP  VALUE   ZERO.
018000     02  RANDOM-PRODUCT          PIC S9(15) COMP  VALUE   ZERO.
018100     02  RANDOM-ADJUST           PIC S9(9)  COMP  VALUE +2099863.
018200
070800
070900**********************   RANDOM FUNCTION    **********************
071000*
071100*            COMPUTES RESULT = RANDOM FRACTION IN (0:1)
071200*
071300*----------------------------------------------------------------
071400
071500 RANDOM-FUNCTION.
071600     MOVE MATHPK-ARGUMENT-1 TO RANDOM-INTEGER
071700
071800     COMPUTE RANDOM-PRODUCT  = RANDOM-INCREMENT
071900                             + RANDOM-MULTIPLIER * RANDOM-INTEGER
072000     COMPUTE RANDOM-QUOTIENT = RANDOM-PRODUCT    / RANDOM-MODULUS
072100     COMPUTE RANDOM-INTEGER  = RANDOM-PRODUCT
072200                             - RANDOM-QUOTIENT   * RANDOM-MODULUS
072300     COMPUTE MATHPK-RESULT   = RANDOM-INTEGER    / RANDOM-ADJUST
072400
072500     MOVE RANDOM-INTEGER TO MATHPK-ARGUMENT-1
072600     .
072700
072800*******************    SEED RANDOM FUNCTION    *******************
072900*
073000*            SEEDS THE RANDOM NUMBER GENERATOR WITH THE
073100*            NUMBER IN ARGUMENT-1, WHICH MUST BE WITHIN
073200*                       THE INTERVAL (0:1)
073300*
073400*----------------------------------------------------------------
073500
073600 SEED-RANDOM-FUNCTION.
073700     MOVE MATHPK-ARGUMENT-1 TO ARG-X
073800     IF ZERO < ARG-X
073900        AND    ARG-X < VALUE-ONE
074000         COMPUTE RANDOM-INTEGER = ARG-X * RANDOM-PRECISION
074100         MOVE RANDOM-INTEGER TO MATHPK-ARGUMENT-1
074200     ELSE
074300         PERFORM SET-DOMAIN-ERROR
074400     .
```

#### ↳ Re: Generating Random Numbers

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36730727.240357659@news1.ibm.net>`
- **References:** `<01be2612$2b5dffc0$2c198318@default.mw.mediaone.net>`

```
On 12 Dec 1998 20:58:24 GMT, "Dennis Fyke" <DEFyke@aol.com> wrote:

>Fujitsu Cobol has a Random function but I can't seem to get it to compile, 
>does anyone know of a good method of generating random numbers?
>
>

I demonstrate this function using Fujitsu COBOL in my book.  Can you
post your code, and we'll see what we can do to get it to work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
