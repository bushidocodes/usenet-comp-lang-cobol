[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migrating MF Indexed files to SQL Warehouse

_3 messages · 3 participants · 1999-07_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases) · [`VSAM, files, sorting`](../topics.md#files)

---

### Migrating MF Indexed files to SQL Warehouse

- **From:** "Jason Bailey" <jbailey5@earthlink.net>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n2hgu$kv2$1@holly.prod.itd.earthlink.net>`

```
Our insurance company is at a cross-roads where we are about to start
underwriting a large amount of new policies per month.  Our current system
was written in the 80's and we have a need to facilitate large data files.

Because I worry about indexed files become too bloated (and performance
degradation) I am looking at migrating the files to SQL Server 7.  This
would not only help with the performance issue, it would also allow us to
dynamically create reports from custom-made queries.

My question is:  Has anyone had experience with migrating from MF files to
SQL?  We'll be using AcuCobol 4.2 with Acu4GL for MS SQL Server.

Jason Bailey
Lead Programmer/Project Lead
```

#### ↳ Re: Migrating MF Indexed files to SQL Warehouse

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yX9l3.1577$cd5.116743@typ42b.nn.bcandid.com>`
- **References:** `<7n2hgu$kv2$1@holly.prod.itd.earthlink.net>`

```

Jason Bailey wrote in message <7n2hgu$kv2$1@holly.prod.itd.earthlink.net>...
>Our insurance company ... current system
>was written in the 80's and we have a need to facilitate large data files.
…[4 more quoted lines elided]…
>SQL?  We'll be using AcuCobol 4.2 with Acu4GL for MS SQL Server.


If you want to reengineer a large suite of applications, rather than doing
it manually,
you might consider using a reengineering tool such as the DMS Reengineering
Toolkit.
(http://www.semdesigns.com/Products/DMS/DMSToolkit.html).  Such tools
can be used to define a translation for the data, and to drive corresponding
changes to the code.
```

#### ↳ Re: Migrating MF Indexed files to SQL Warehouse

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9H5l3.147$ZU.17939@typhoon01.swbell.net>`
- **References:** `<7n2hgu$kv2$1@holly.prod.itd.earthlink.net>`

```

Jason Bailey <jbailey5@earthlink.net> wrote in message news:7n2hgu$kv2$

IMHO it would be far, far cheaper to buy faster computers than to rewrite a
database server.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
