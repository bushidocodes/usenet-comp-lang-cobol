[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MySQL access from COBOL

_5 messages · 3 participants · 2005-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### MySQL access from COBOL

- **From:** anguel@web.de (Anguel de Quevedo Garcia)
- **Date:** 2005-04-13T07:09:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97e9eb99.0504130609.2dcd728d@posting.google.com>`

```
Does any of you know a way to access mysql databases from Compaq
Cobol? Or the other way 'round: Does someone know about another cobol
compiler running on Unix or VMS that's able to do that job?
```

#### ↳ Re: MySQL access from COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-13T11:20:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113416415.308428.147260@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<97e9eb99.0504130609.2dcd728d@posting.google.com>`
- **References:** `<97e9eb99.0504130609.2dcd728d@posting.google.com>`

```
> Does any of you know a way to access mysql databases from
> Compaq Cobol? Or the other way 'round: Does someone know
> about another cobol compiler running on Unix or VMS that's able
> to  do that job?

MySQL can be accessed using ODBC or unixODBC and so any Cobol that can
use this can access it.  eg Fujitsu Cobol for Linux.

In my experience the MySQL should be running with transactions enabled.
This required very late version 3 or version 4 and InnoDB tables. Later
versions of MySQL have probably changed again.
```

##### ↳ ↳ Re: MySQL access from COBOL

- **From:** anguel@web.de (Anguel de Quevedo Garcia)
- **Date:** 2005-04-15T03:12:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97e9eb99.0504150212.38ddda55@posting.google.com>`
- **References:** `<97e9eb99.0504130609.2dcd728d@posting.google.com> <1113416415.308428.147260@f14g2000cwb.googlegroups.com>`

```
Richard wrote:

>> Does any of you know a way to access mysql databases from
>> Compaq Cobol? Or the other way 'round: Does someone know
…[4 more quoted lines elided]…
> use this can access it.  eg Fujitsu Cobol for Linux.

Thank you so far. But I must admit that I don't have any clue how to
set up ODBC on a unix machine (on the same as the mysql server is running
on) and how to code that access on VMS Cobol. Is there any tutorial out
there? I did not found any on the web.

Thank you
-=* Anguel *=-
```

###### ↳ ↳ ↳ Re: MySQL access from COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-15T12:50:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113594607.660495.52750@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<97e9eb99.0504150212.38ddda55@posting.google.com>`
- **References:** `<97e9eb99.0504130609.2dcd728d@posting.google.com> <1113416415.308428.147260@f14g2000cwb.googlegroups.com> <97e9eb99.0504150212.38ddda55@posting.google.com>`

```
> I don't have any clue how to set up ODBC on a unix machine

Start by getting unixODBC form unixodbc.org and read the documentation
that comes with it.

> how to code that access on VMS Cobol

I have no idea, nor even that anything on VMS could access ODBC or any
version of MySQL.

You may even have to tier your program so that there is a MySQL
accessing program running on the MySQL server that sends data back to
your program.
```

###### ↳ ↳ ↳ Re: MySQL access from COBOL

_(reply depth: 4)_

- **From:** "Don Braffitt" <don.braffitt@hp.com>
- **Date:** 2005-04-24T18:18:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1114391921.123374.26090@l41g2000cwc.googlegroups.com>`
- **References:** `<97e9eb99.0504130609.2dcd728d@posting.google.com> <1113416415.308428.147260@f14g2000cwb.googlegroups.com> <97e9eb99.0504150212.38ddda55@posting.google.com> <1113594607.660495.52750@l41g2000cwc.googlegroups.com>`

```
> I have no idea, nor even that anything on VMS could access ODBC or
> any version of MySQL.

One way to do ODBC access on OpenVMS is with CONNX

  http://www.connx.com/products/rms.html

- Don Braffitt
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
