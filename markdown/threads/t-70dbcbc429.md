[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to Handle an Unhandled Condition?

_5 messages · 5 participants · 1999-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to Handle an Unhandled Condition?

- **From:** Bill Thompson <wthompson@my-deja.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80c3gc$vqh$1@nnrp1.deja.com>`

```
Can somebody point me to the documentation that will tell me how to
catch and process what is now a "CEE3DMP V1 R6.0: Condition processing
resulted in the unhandled condition." as a result of "IGZ0097S Argument-
1 for function NUMVAL in program ... contained no digits."

TIA, Bill
```

#### ↳ Re: How to Handle an Unhandled Condition?

- **From:** docdwarf@clark.net ()
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gdhW3.35831$oa2.130088@iad-read.news.verio.net>`
- **References:** `<80c3gc$vqh$1@nnrp1.deja.com>`

```
In article <80c3gc$vqh$1@nnrp1.deja.com>,
Bill Thompson  <wthompson@my-deja.com> wrote:
>Can somebody point me to the documentation that will tell me how to
>catch and process what is now a "CEE3DMP V1 R6.0: Condition processing
>resulted in the unhandled condition." as a result of "IGZ0097S Argument-
>1 for function NUMVAL in program ... contained no digits."

Warning - I am not, nor do I claim to be, conversant with the
peculiarities of NUMVAL.  Please keep this in mind.

Given:

01  BUNCHA-STUFF.
    05  CHARFLD PIC X(09).
    05  NUMFLD  PIC 9(09).

... and a value in CHARFLD of, say, 'KERFLOOIE' then I would expect a
statement such as:

COMPUTE NUMFLD = FUNCTION NUMVAL(CHARFLD)

... to cause the error in question.  Off the top of my pointy little head
all I can suggest is:

PERFORM VARYING SUB1 FROM 1 BY 1 UNTIL SUB1 > (LENGTH OF CHARFLD)
    IF CHARFLD(SUB1:1) NUMERIC
        COMPUTE NUMFLD = FUNCTION NUMVAL(CHARFLD)
        ADD (LENGTH OF CHARFLD) TO SUB1
    END-IF
END-PERFORM (.) <==(placement of period to be debated at length)

DD
```

#### ↳ Re: How to Handle an Unhandled Condition?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991110133236.23576.00000430@ngol02.aol.com>`
- **References:** `<80c3gc$vqh$1@nnrp1.deja.com>`

```
In article <80c3gc$vqh$1@nnrp1.deja.com>, Bill Thompson <wthompson@my-deja.com>
writes:

>resulted in the unhandled condition." as a result of "IGZ0097S Argument-
>1 for function NUMVAL in program ... contained no digits."
>

I kinda got bit by this myself a time or two.
Since then any NUMVAL functions are covered by an
IF <field> Greater than Spaces
```

#### ↳ Re: How to Handle an Unhandled Condition?

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991111162725.07218.00000149@ng-cl1.aol.com>`
- **References:** `<80c3gc$vqh$1@nnrp1.deja.com>`

```
Bill Thompson writes...

>Can somebody point me to the documentation that will tell me how to
>catch and process what is now a "CEE3DMP V1 R6.0: Condition processing
>resulted in the unhandled condition." as a result of "IGZ0097S Argument-
>1 for function NUMVAL in program ... contained no digits."

As someone suggested, you can check your input field before invoking the NUMVAL
function.

However, I read your request differently. If you really want to know about "how
to
catch and process" the unhandled condition, then jump into the LE pubs on
condition handling. There is a lot of background to get first, but you can
figure it out.

If you want to save yourself a lot of time, bring us in for a class on LE and
we'll run through all you need to know about LE from an application programmers
perspective, including how to code LE condition handlers in COBOL (or C or PL/I
or Assembler). Check the website in my signature for details.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: How to Handle an Unhandled Condition?

- **From:** "The COBOL Frog" <H.Klink@IMN.nl>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80khij$iev$1@porthos.nl.uu.net>`
- **References:** `<80c3gc$vqh$1@nnrp1.deja.com>`

```
Bill,

I.s.o.

...  SOMEFLD PIC X(n).
...
     MOVE / COMPUTE ... FUNCTION NUMVAL(SOMEFLD) ...

use

...  SOMEFLD PIC X(n).
     EXTRAFIELD PIC X(n+1) VALUE "0".
...
     MOVE SOMEFLD TO EXTRAFIELD(2:)
     MOVE / COMPUTE ... FUNCTION NUMVAL(EXTRAFIELD) ...

The leading zero in the EXTRAFIELD will ensure at least one digit is present without influencing the arithmatec value of the result.

Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
