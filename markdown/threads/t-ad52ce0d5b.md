[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# converting from cobol to other obdc database

_1 message · 1 participant · 2004-02_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases)

---

### Re: converting from cobol to other obdc database

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-02-24T13:27:49+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<pjI_b.17187$PY.4345@newssvr26.news.prodigy.com>`
- **References:** `<JUz_b.3586833$uj6.10411810@telenews.teleline.es>`

```
"Sam" <vermello@terra.es> wrote in message
news:JUz_b.3586833$uj6.10411810@telenews.teleline.es...
> I have a very old database in Cobol and now I need to convert to Obdc
> database format. I have no idea about Cobol, is there any program to do
it?
> Can I use other way to do it? Thanks.

Tutorial: Converting COBOL-created data for use with non-COBOL programs:
http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

FWIW, there is no such thing as "odbc format". Some DMBSs do, however,
support direct import  from fixed-field or comma-separated values files.

I believe someone has an ODBC driver for COBOL-created files.. meaning you
would not have to convert at all. (Can't recall clearly, but this may be a
driver for files created by a specific brand name COBOL compiler/runtime).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
