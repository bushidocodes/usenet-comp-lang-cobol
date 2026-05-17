[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Net Express ODBC

_2 messages · 2 participants · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Microfocus Net Express ODBC

- **From:** "danfan" <ua-author-6722460@usenetarchives.gap>
- **Date:** 1998-06-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ljt82$e96$1@cubacola.tninet.se>`

```

I've been trying to run a Micro Focus NETEXPRESS COBOL
using embedded sql against an ODBC data source
(Teradata ODBC). It doesn't work properly, and even
causes the DB to crash.

Does anyone use NETEXPRESS against ODBC?
Even Teradata?

What are your compiler options?

/DG
```

#### ↳ Re: Microfocus Net Express ODBC

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-06-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d2d59eaa9f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6ljt82$e96$1@cubacola.tninet.se>`
- **References:** `<6ljt82$e96$1@cubacola.tninet.se>`

```

Danfan?

We have lots of Customers who are using the OpenESQL
pre-compiler successfully. I must admit I have not talked to
anyone using Teradata before. I would suggest you test
your program against another ODBC driver to see if the
problem lies in our code or the Teradata ODBC driver.

These sort of problems normally turn out to be an ODBC
issue but there is always a first time! Also check to see
if that you are using the latest Teradata ODBC driver.

Another thing to try; use a different tool (Access, VB,
Excel etc) to access the Teradata data source. Do
you get similar problems.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

danfan wrote in message <6ljt82$e96$1.··.@cub··t.se>...
› I've been trying to run a Micro Focus NETEXPRESS COBOL
› using embedded sql against an ODBC data source
…[12 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
