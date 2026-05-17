[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL vs COBOL II

_3 messages · 3 participants · 1997-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL vs COBOL II

- **From:** "myron coulson" <ua-author-17071895@usenetarchives.gap>
- **Date:** 1997-10-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3453F92A.1DFF1C1D@ibm.net>`

```

Can someone briefly explain the diferences between COBOL and COBOL
II? Is it just COBOL 74 and 85, or old and new? Thanks.
```

#### ↳ Re: COBOL vs COBOL II

- **From:** "rkra..." <ua-author-13871254@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc47b38b4b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3453F92A.1DFF1C1D@ibm.net>`
- **References:** `<3453F92A.1DFF1C1D@ibm.net>`

```


I can answer part of this. 'COBOL II' is an IBM mainframe product name. It
compiled COBOL 74 syntax through Release 2. Subsequent releases compile COBOL
85 syntax, with an optional feature known as CMPR2 (compile release 2) to
regress the front-end back to COBOL 74 syntax.

Newer releases of the product go by the name of COBOL for MVS (still COBOL 85
syntax). There are a number of features in these later releases that help
identify code needing change for a migration, and a number of independently
controlled compiler back-end controls (such as preferred sign and binary data
item semantics). This is an extremely good product, it is very flexible.
It is a remarkable reflection of IBM's wide diversity of customers.

If you take COBOL 85 as the current standard, then any compiler or standing
code that involves COBOL 74 syntax might be called 'old COBOL'.

There is yet another IBM product, sometimes known as COBOL 370, that compiles
with language bindings to the LE 370 executable environment. LE 370 is the
doorway to the happy hunting ground of object oriented programming. This type
of compile is known at the street level as 'COBOL THREE'. If it is possible to
build the Tower of Babel in cyberspace, the mason's mark on the foundation
stones will surely be 'LE'.









Robert Rayhawk
RKR··.@a··.com
```

##### ↳ ↳ Re: COBOL vs COBOL II

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-10-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc47b38b4b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dc47b38b4b-p2@usenetarchives.gap>`
- **References:** `<3453F92A.1DFF1C1D@ibm.net> <gap-dc47b38b4b-p2@usenetarchives.gap>`

```

RKRayhawk wrote:
...
› Newer releases of the product go by the name of COBOL for MVS (still COBOL 85
› ...
› There is yet another IBM product, sometimes known as COBOL 370, that compiles
›  with language bindings to the LE 370 executable environment. LE 370 is the
...
COBOL 370, COBOL for MVS, and its latest re-incarnation COBOL for OS/390
are all basically different releases of the same compiler concept, all
dependent on LE runtime, which has gone through a similar naming/release
evolution. The names were changed after S/390 made S/370 obsolete, and
then they had to change again when MVS became OS/390.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
