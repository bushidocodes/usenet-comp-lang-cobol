[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress OPENESQL and comp-3.

_2 messages · 2 participants · 1998-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### NetExpress OPENESQL and comp-3.

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34D1A75B.3A9405D8@yahoo.com>`

```

Hi,

Is there a way to get OPENESQL to accept comp-3 fields in the FETCH -
statement ??
It accepts comp-5, but not comp-3.

Compiler-directive ?????

Tommy Nilsen
tom··.@NOS··o.com
(Remove the NOSPAM)
```

#### ↳ Re: NetExpress OPENESQL and comp-3.

- **From:** "ed" <ua-author-25747@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f841c7ccc2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34D1A75B.3A9405D8@yahoo.com>`
- **References:** `<34D1A75B.3A9405D8@yahoo.com>`

```

I just wondered if you were using the right data type for the comp-3 field.
Here's a bit from the solutions guide online book, chapter 4.

Use the ANSI data type code (shown in the second column of the table above)
to determine which COBOL data type to use. The table below shows the
relationship between the two.

Data type Usual name Equivalent COBOL pictures
------------------------------------------------------------------------
2 numeric pic s9(a)v9(b)usage comp-3.
where a + b is less than or equal to 18
3 decimal pic s9(a)v9(b)usage comp-3.
where a + b is less than or equal to 18
4 integer pic s9(9) comp.
pic s9(9) comp-5.
pic x(4) comp-5.
pic x(4) comp-x.
pic 9(9) usage display. .....etc.

tommy nilsen wrote in article
<34D··.@ya··o.com>...
› Hi,
› 
…[10 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
