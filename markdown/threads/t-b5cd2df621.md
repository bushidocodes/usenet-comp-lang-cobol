[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC using Excel

_3 messages · 3 participants · 2001-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC using Excel

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2001-04-19T21:35:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bnln0$jp2$1@ins21.netins.net>`

```
I would like to use ODBC with MS Excel.  I understand how to create the
ODBC data source using ODBC, but I am not clear about how to access the
data.  Has anybody tried this using Fujitsu COBOL?  I would like to
present it as a project in my classes next semester.  I could use MS
Sequel Server or Access, but these are presented later as part of our 
Database course.  

The concept seems possible - now if I can figure it out.  I will
experiment during the summer - but any hints or roadblocks would be
appreciated.

Thanks,

Floyd Johnson
```

#### ↳ Re: ODBC using Excel

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2001-04-24T20:02:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AE5DBE8.3AE69A58@boeing.com>`
- **References:** `<9bnln0$jp2$1@ins21.netins.net>`

```
Floyd Johnson wrote:
> 
> I would like to use ODBC with MS Excel.  I understand how to create the
…[9 more quoted lines elided]…
> 

I have not done this (I am a mainframe fossil), but my DB2 database does
download into MS Excel spreadsheets or rather Cold Fusion interacts with
the proper API (?) to load the extracted query into an Excel spreadsheet
- performance is horrid when anything more then around 2K rows are
requested.

I bet you can tell I have a ColdFusion Programmer helping me with my
application.

	Susan A
```

##### ↳ ↳ Re: ODBC using Excel

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2001-04-24T16:27:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AE5E1AB.11295DE9@yahoo.com>`
- **References:** `<9bnln0$jp2$1@ins21.netins.net> <3AE5DBE8.3AE69A58@boeing.com>`

```
Susan Allen wrote:
> 
> Floyd Johnson wrote:
…[22 more quoted lines elided]…
>         Susan A

You can try using Q + E database editor.  It allows a macro to make an
ODC connection to run an SQL statement.  This may be very slow, however
but it does work.  Advantage software makes it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
