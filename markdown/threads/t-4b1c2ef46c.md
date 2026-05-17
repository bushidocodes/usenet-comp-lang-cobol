[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 85

_2 messages · 2 participants · 1995-01 → 1995-02_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Cobol 85

- **From:** "bhui..." <ua-author-17088046@usenetarchives.gap>
- **Date:** 1995-01-29T10:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-yNf_tWVSgrE@usenetarchives.gap>`

```
I am wodering about the efficiency of cobol 85. Like in condition code for
our cobol program, we have to use
IF .......
imperative sentence
END IF.
terminator end if, but in cobol 74 we don't have to use this delimitar. Can
anybody out there give me some more arguments about cobol 85.

Mushi Bhuiyan
e-mail: bhu··.@col··u.edu
```

#### ↳ Re: Cobol 85

- **From:** "st..." <ua-author-9304866@usenetarchives.gap>
- **Date:** 1995-02-04T15:45:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4b1c2ef46c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-yNf_tWVSgrE@usenetarchives.gap>`
- **References:** `<ua-fallback-yNf_tWVSgrE@usenetarchives.gap>`

```
In article bhu··.@col··u.edu (Mohammed Bhuiyan) writes:
› From: bhu··.@col··u.edu (Mohammed Bhuiyan)
› Subject: cobol 85
› Date: Sun, 29 Jan 1995 15:37:16
› Summary: advatage of cobol 85
 
› I am wodering about the efficiency of cobol 85.   Like in condition code for 
› our cobol program, we have to use 
…[4 more quoted lines elided]…
› anybody out there give me some  more arguments about cobol 85.
 
›   Mushi Bhuiyan
›   e-mail: bhu··.@col··u.edu

Contrary to all of your other responses, I am of the old school. I started
with COBOL 74 and don't have any problems using periods. I have taught COBOL
and I have found that students trying to use both periods and "END-?"
terminators get into problems. So my advice is to choose what you are
comfortable with (in my case, periods with a liberal use of PERFORMs - which
is good structured technique) and be consistant. I truly think that some
people over do the deep nesting of IFs and READs etc. (because they CAN
with "END-?") when they should be using PERFORMS. In that case, I think the
use of "END-?" terminators is detrimental to good and readable programming.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
