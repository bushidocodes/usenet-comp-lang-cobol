[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 88 Definitions and Data Validation

_1 message · 1 participant · 1999-02_

---

### Re: 88 Definitions and Data Validation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79fo5i$bag@dfw-ixnews4.ix.netcom.com>`
- **References:** `<xqau2.1739$ob2.4260@news.flash.net> <1999Feb4.132809.19503@giant> <6%Bu2.42$j3.54@testbox>`

```

Tom Eisenman wrote in message <6%Bu2.42$j3.54@testbox>...
>But in many systems the example you have given below will cause the program
>to abend (crash) the first time one of the customer fields is non-numeric.
…[4 more quoted lines elided]…
>


Not true, (either part)
   The ANSI/ISO Standard explicitly says that you do NOT get an
"incompatible data" condition when doing a class test - and I know of no
compiler that does so.   You can do a  NUMERIC (or NOT NUMERIC) test against
a USAGE DISPLAY elementary numeric field.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
