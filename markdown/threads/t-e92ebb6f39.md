[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# indicator field

_1 message · 1 participant · 1999-01_

---

### Re: indicator field

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-10T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<77bspt$akc@sjx-ixn6.ix.netcom.com>`
- **References:** `<36942eec.748517@netnews> <19990107030534.17758.00002763@ngol08.aol.com> <36948067.21564378@netnews>`

```

Randall Bart wrote in message <36948067.21564378@netnews>...
>'Twas 07 Jan 1999 08:05:34 GMT, when mark0young@aol.com (Mark0Young)
>illuminated alt.cobol thusly:
…[7 more quoted lines elided]…
>>I'll have to look that up the next time I go to work--one problem of
having
>>worked in IT for 22 years is that sometimes one remembers restrictions
that
>>existed at one time or were shop standards but have since been relaxed.
>
…[11 more quoted lines elided]…
>R B |\  Randall Bart



Randall is correct that continuation of COBOL words (rather than
alphanumeric literals) is on the way out.

My favorite "obscure" test is something like this:

    05  Num    Pic  S9(03)v99.
            ...
     Move     -
-      123.
-      45  to Num.

(you should see all the compilers that get sick on that perfectly legal
code.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
