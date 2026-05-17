[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol problem!

_7 messages · 7 participants · 1997-02 → 1997-03_

---

### Cobol problem!

- **From:** "calvin yiu" <ua-author-17072434@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`

```

Hi all,

Is there any function used to change the case of characters in COBOL/85?

Calvin
```

#### ↳ Re: Cobol problem!

- **From:** "chai..." <ua-author-2228828@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`

```

Try:

MOVE FUNCTION UPPER-CASE (field-name) TO field-name
```

#### ↳ Re: Cobol problem!

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-02-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`

```

The example in the book is:

INSPECT variable CONVERTING "abcdefghijklmnopqrstuvwxyz" TO
"ABCDEFGHIJKLMNOPQRSTUVWXYZ" .

Calvin Yiu wrote in article
<01bc24b7$23fc8ca0$d5e··.@cal··u.hk>...
› Hi all,
›
…[4 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Cobol problem!

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-03-02T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3a6ae90fb-p3@usenetarchives.gap>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk> <gap-a3a6ae90fb-p3@usenetarchives.gap>`

```

"John McKown" wrote:

› The example in the book is:
 
› INSPECT variable CONVERTING "abcdefghijklmnopqrstuvwxyz" TO
› "ABCDEFGHIJKLMNOPQRSTUVWXYZ" .
 
› Calvin Yiu  wrote in article
› <01bc24b7$23fc8ca0$d5e··.@cal··u.hk>...
…[6 more quoted lines elided]…
›› 

Also FUNCTION LOWER-CASE(field-name) and FUNCTION
UPPER-CASE(field-name) for IBM COBOL for MVS & VM.

Just my two cents worth, adjusted for inflation,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

#### ↳ Re: Cobol problem!

- **From:** "jhbuhhh" <ua-author-6256507@usenetarchives.gap>
- **Date:** 1997-02-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`

```

What I have uusually done is set a an array with all the lower upper/
case characters in it, in a three trier arch. I would make this routine a
process layer and just pass my data 2 and from, although a copy code
procedure that is executed works just as well and a bit more efficent

best of luck

› "Calvin Yiu"  wrote in article
› <01bc24b7$23fc8ca0$d5e··.@cal··u.hk>...
…[7 more quoted lines elided]…
›
```

#### ↳ Re: Cobol problem!

- **From:** "stevenc" <ua-author-1500476@usenetarchives.gap>
- **Date:** 1997-03-04T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk>`

```

Calvin Yiu wrote:
›
› Hi all,
…[3 more quoted lines elided]…
› Calvin

In COBOL/370, I know there is such a function used to convert characters
from lower case to upper case and vice versa and it is called
FUNCTION UPPER-CASE and FUNCTION LOWER-CASE.
ex. move FUNCTION UPPER-CASE(abc) to ws-upper-case.
ws-upper-case would contain the characters "ABC" in upper-case after the
move is done.
```

##### ↳ ↳ Re: Cobol problem!

- **From:** "information services" <ua-author-734034@usenetarchives.gap>
- **Date:** 1997-03-05T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3a6ae90fb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3a6ae90fb-p6@usenetarchives.gap>`
- **References:** `<01bc24b7$23fc8ca0$d5e4598f@calvin.cityu.edu.hk> <gap-a3a6ae90fb-p6@usenetarchives.gap>`

```

on the AS400, I use the INSPECT CONVERTING statement, this is COBOL/400
version 3.

StevenC wrote in article <331··.@dsu··r.net>...
› Calvin Yiu wrote:
›› 
…[13 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
