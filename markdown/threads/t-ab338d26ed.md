[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trig Function in Cobol

_5 messages · 4 participants · 1996-07_

---

### Trig Function in Cobol

- **From:** "all-tis" <ua-author-17086390@usenetarchives.gap>
- **Date:** 1996-07-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31E3DE98.4F8F@tandy.com>`

```

Does anyone have any source code to perform trig functions in COBOL II on
an Amdahl ?

thanks,
chad
```

#### ↳ Re: Trig Function in Cobol

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab338d26ed-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31E3DE98.4F8F@tandy.com>`
- **References:** `<31E3DE98.4F8F@tandy.com>`

```

In <31E··.@ta··y.com>, All-TIS writes:
› Does anyone have any source code to perform trig functions in COBOL II on 
› an Amdahl ?
› 
› thanks,
› chad

The ETK portable subroutine library contains MATHPK which does
trig functions (and other stuff, such as calendar routines).
You can download a copy from http://www.toscintl
click on ETK to get to the page where the subroutine library is.
```

##### ↳ ↳ Re: Trig Function in Cobol

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab338d26ed-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ab338d26ed-p2@usenetarchives.gap>`
- **References:** `<31E3DE98.4F8F@tandy.com> <gap-ab338d26ed-p2@usenetarchives.gap>`

```

In <4s2tvm$3b··.@new··m.net>, lsv··.@i··.net writes:
› In <31E··.@ta··y.com>, All-TIS  writes:
›› Does anyone have any source code to perform trig functions in COBOL II on 
…[9 more quoted lines elided]…
› 
should be http://www.toscintl.com
Leif Svalgaard
```

#### ↳ Re: Trig Function in Cobol

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab338d26ed-p4@usenetarchives.gap>`
- **In-Reply-To:** `<31E3DE98.4F8F@tandy.com>`
- **References:** `<31E3DE98.4F8F@tandy.com>`

```

There are two approaches to this problem.

First, get to the more current COBOL/370 or COBOL for MVS and VM products.
They have the intrinsics built in - most trig functions included (sorry
no hyperbolics).

Second, back in the days before COBOL/370 was available, I wrote some of
the functions in VS COBOL II, using only add substract multiply and
divide. These implemented the functions via McLauren or Taylor series
expansions. About 6 terms provided single precision accuracy (COIMP-1).

My ancient and honorable (not to mention well worn) Calculus and Analytic
Geometry textbook from the Missouri School of Mines and Missery had
excellent examples of all of these functions just waiting to be converted
to a COMPUTE statement. It also seems to me that one did not have to
implement all of the functions, with only a limited set, you could
synthesize the rest - shows you how long ago that I took the Math 8, 21,
22 series of courses.

Accuracy was tested by comparing the calculated (in COBOL) values to those
calculated by FORTRAN built-in functions.

IBM used publish (may still) a manual on their implementation of the
various numeric functions in their FORTRAN library. Funny thing, they
used Taylor series for the functions.

I can probably find the source for these functions on the mainframe system
where I built them if you still need them.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Trig Function in Cobol

- **From:** "fim w������stberg" <ua-author-6589423@usenetarchives.gap>
- **Date:** 1996-07-10T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab338d26ed-p5@usenetarchives.gap>`
- **In-Reply-To:** `<31E3DE98.4F8F@tandy.com>`
- **References:** `<31E3DE98.4F8F@tandy.com>`

```

All-TIS wrote:
› Does anyone have any source code to perform trig functions in COBOL II on 
› an Amdahl ?
› 
› thanks,
› chad

Hi chad,

All you need is the ETKPAK, look at http://www.toscintl.com
Regards
Fim W
------------------------------------
Fim Wastberg
Travarvagen 5
175 39 JARFALLA
SWEDEN
Phone home: +46 8 580 333 91
Phone off: +46 8 580 277 00
Fax: +46 8 580 250 72
mailto:f.··.@dat··e.se
------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
