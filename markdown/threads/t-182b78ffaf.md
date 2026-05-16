[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ChangeMan Package Error

_1 message · 1 participant · 2005-04_

---

### ChangeMan Package Error

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-04-17T16:39:37+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3t5ko$bq2$1@mawar.singnet.com.sg>`

```
Hi,
Just need some advise on CHGMAN package.
Basically how to get the amended "cobol pgm" to use the updated
"copybook" that are raised in another package. If not,
pgm compiliation will hit error as "field not found".
Tks in advance.

Assume raised a chgmane package called package A
=====================================
I had raised a CHGMAN package to make some amendment to
"copybook" (add another 01 level with new fields specified).

Assume raised another changeman package call package B
=========================================
I had raised another CHGMAN package to make some amendment to
"cobol pgm" to reference to those new fields in package A of the copybook.

(1)  When I compiled the "cobol pgm", it will hit error as it cannot find
the new fields which I state in the "copybook". I know it's because of the 
package
type. I raised both package as "simple" .
Kindly advise what should I changed for both packages above ( participating, 
super etc )

(2)   In addition, I had also some other cobol pgms included inside package
B as well .(those other cobol pgms don't reference the copybook in packageA)
Kindly advise what will happen to those other cobol pgm assuming
if there were suggestion to change the package type for B or there
is no issue at all


** Kindly note that the "copybook" (in package A) is used and reference by
other system as well and that the "cobol pgm" is used by our system ONLY.

** Kindly note that cannot checkout both in one package as the "copybook"
and "cobol pgm" are residing in different lib.

(P/s : I did change both package to "participating" type but compiling of
the cobol pgm still give error as it cannot link to the copybook in package 
B to
reference the new fields there)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
