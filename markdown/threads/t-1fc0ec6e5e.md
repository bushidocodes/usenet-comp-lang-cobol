[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Integer numeric

_9 messages · 8 participants · 1997-07 → 1997-08_

---

### Integer numeric

- **From:** "john" <ua-author-11681@usenetarchives.gap>
- **Date:** 1997-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`

```

if anyone knows how to validate a numeric field with integers only. an
decimal number in this field should be regarded as an error. thanks in
advance. john
zz··.@dru··o.edu
```

#### ↳ Re: Integer numeric

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-07-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`

```

"john" wrote:

› if anyone knows how to validate a numeric field with integers only. an
› decimal number in this field should be regarded as an error. thanks in
› advance. john
› -- 
› zz··.@dru··o.edu
If your PICTURE is 99999 then a numeric test will fail if a non
numeric is there. Whether it is a Q or $ or . it is not anticipated
as numeric.

JR
and stir with a Runcible spoon...
```

##### ↳ ↳ Re: Integer numeric

- **From:** "ejon" <ua-author-17071868@usenetarchives.gap>
- **Date:** 1997-08-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fc0ec6e5e-p2@usenetarchives.gap>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu> <gap-1fc0ec6e5e-p2@usenetarchives.gap>`

```

Jeff Raben wrote:
› 
› "john"  wrote:
…[8 more quoted lines elided]…
› as numeric.

It depends. Try this numeric test on a 360/370-compatible
system and you will be surprised:
01 wk-test-area.
05 wk-test-fld-char pic x(03) value "9 9".
05 wk-test-field redefines wk-test-fld-char
pic 999.


IF wk-test-field IS NUMERIC....


On some systems this will fly right on by.
Also if the field in the leading/trailing char has
"ABCDEFGHIJKLMNOPQR" or "{}", it will pass with
flying colors.
```

#### ↳ Re: Integer numeric

- **From:** "lindy mayfield" <ua-author-13980060@usenetarchives.gap>
- **Date:** 1997-07-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`

```

john wrote:
› 
› if anyone knows how to validate a numeric field with integers only. an
…[3 more quoted lines elided]…
› zz··.@dru··o.edu


I seem to remember having a lot of trouble with this in the past, and for my particular use I had to check each
digit of the string separately. Which wasn't really as difficult as it sounds.


The _COBOL MVS & VM V1R2 Programming Guide_ has this to say:

---

1.3.5.1 How to Do a Numeric Class Test

You can use the numeric class test to perform data validation. For example:

Linkage Section.
01 Count-x Pic 999.
.
.
.

Procedure Division Using Count-x.
If Count-x is numeric then display "Data is good"
.
.
.

The numeric class test checks the contents of a data item against a set of values that are valid for the
particular PICTURE and USAGE of the data item. For example, a packed decimal item would be
checked for hexadecimal values X'0' through X'9' in the digit positions and for a valid sign value
in the sign position (whether separate or non-separate).

---

In most instances doing a numeric check doesn't work very well. If you are checking data that doesn't always
conform to a COBOL pic clause, then you're in trouble.

As an example, if the data you expect is this:
001
102
BXX*
993
666
.11*
f89*

then those marked by an asterisk are invalid.

But if you are expecting this:

1112
92
1
91224

then anyone with a space in it is invalid, and you are going to have to parse each digit separately using
whatever rules are necessary.

Hope this helps. If you have a more specific question or problem then maybe I can help you with that.

Lindy
```

#### ↳ Re: Integer numeric

- **From:** "kiki" <ua-author-795227@usenetarchives.gap>
- **Date:** 1997-08-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu>`

```



john wrote in article
<01bc9dc3$50a363c0$420··.@myc··o.edu>...
› if anyone knows how to validate a numeric field with integers only. an
› decimal number in this field should be regarded as an error. thanks in
…[3 more quoted lines elided]…
› 
If you divide the number (rounded) by itself (unrounded) and use the
REMAINDER clause.
IF that value is greater or less than zero, you got a decimal.
There probablly is a better way.
```

##### ↳ ↳ Re: Integer numeric

- **From:** "joseph61.nospam" <ua-author-1167534@usenetarchives.gap>
- **Date:** 1997-08-01T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fc0ec6e5e-p5@usenetarchives.gap>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu> <gap-1fc0ec6e5e-p5@usenetarchives.gap>`

```

Startling the yaks "kiki" wrote:

}
}
}john wrote in article
}<01bc9dc3$50a363c0$420··.@myc··o.edu>...
}> if anyone knows how to validate a numeric field with integers only.
an
}> decimal number in this field should be regarded as an error. thanks
in
}> advance. john
}> --
}> zz··.@dru··o.edu
}>
}If you divide the number (rounded) by itself (unrounded) and use the
}REMAINDER clause.
}IF that value is greater or less than zero, you got a decimal.
}There probablly is a better way.

I think I'd try this first:

01 work-areas.
05 num-to-be-tested pic s9(9)v9(4).
05 integer-area pic s9(9).
05 test-results pic s9(9)v9(4).

move num-to-be-tested to integer-area
compute test-results = num-to-be-tested - integer-area
if test-results = 0
perform it-is-an-integer
else
perform not-an-integer
end-if.

Perhaps not the most efficient way to do it, but hopefully it's clear.



==============================================================
*** When tying shoes to the honeymooners' car, please be ***
*** sure that no one is still wearing them ***
************************ Joseph Cote *************************
****************** jos··.@ix.··m.com ********************
==============================================================
```

###### ↳ ↳ ↳ Re: Integer numeric

- **From:** "arn b" <ua-author-2587922@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fc0ec6e5e-p6@usenetarchives.gap>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu> <gap-1fc0ec6e5e-p5@usenetarchives.gap> <gap-1fc0ec6e5e-p6@usenetarchives.gap>`

```

Joseph Cote wrote:
› 
› Startling the yaks "kiki"  wrote:
…[35 more quoted lines elided]…
› ==============================================================
Ok forgive the last post. I could not cancel it(my anti spamming
confuses Netscape) and I did not understand the entire problem before
responding, but try this
01 work-areas.
05 num-to-be-tested pic s9(9)v9(4).
05 filler redefines num-to-be-tested.
07 filler pic x(9).
07 num-decimal pic 9(4).
if num-to-be-tested numeric and num-decimal = zero

***********************************************************
Please remove NOJUNK. from return address to respond
to AR··.@mys··f.com
***********************************************************
```

###### ↳ ↳ ↳ Re: Integer numeric

- **From:** "arn b" <ua-author-2587922@usenetarchives.gap>
- **Date:** 1997-08-02T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fc0ec6e5e-p6@usenetarchives.gap>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu> <gap-1fc0ec6e5e-p5@usenetarchives.gap> <gap-1fc0ec6e5e-p6@usenetarchives.gap>`

```

Joseph Cote wrote:
› 
› Startling the yaks "kiki"  wrote:
…[34 more quoted lines elided]…
› 
Ummmm....what about IF NUMERIC....
***********************************************************
Please remove NOJUNK. from return address to respond
to AR··.@mys··f.com
***********************************************************
```

##### ↳ ↳ Re: Integer numeric

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1fc0ec6e5e-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1fc0ec6e5e-p5@usenetarchives.gap>`
- **References:** `<01bc9dc3$50a363c0$420e8780@mycomputer.uchicago.edu> <gap-1fc0ec6e5e-p5@usenetarchives.gap>`

```

Maybe I don't understand the question...

A 'numeric' field is characterized by a string of numeric digits. The
'scale' of the number is indicated by the position of the 'V' in the
PIC.

For example, 12345 PIC 9(5) = 12345, while 12345 PIC 9(3)V99 is treated
as 123.45. The contents of the fields, viewed without the PIC in mind,
are the same - the PIC controls the scale.

So I don't quite get the question as to how a decimal in a numeric field
could be noticed. It would depend on the PIC.

If you mean that there would be a dot (.) in the field, then you could
use the IS NUMERIC (IS NOT NUMERIC) phrase in an IF statement. However,
this phrase, in older compilers, was not allowed vs. numeric PICs. Thus
you'd need to redefine the input field. In COBOL II you can use it on
PIC 9 fields also.

E.g., 05 WS-INFIELD-NUM PIC 9(5).
05 WS-INFIELD-ALPH REDEFINES WS-INFIELD-NUM PIC X(5).

IF WS-INFIELD-ALPH IS NOT NUMERIC....

John


kiki wrote:
› 
› john  wrote in article
…[10 more quoted lines elided]…
› There probablly is a better way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
