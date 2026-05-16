[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Powercobol and sql

_2 messages · 2 participants · 2004-01_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Powercobol and sql

- **From:** "Dionisis Vrionis" <diovr@dksoft.gr>
- **Date:** 2004-01-20T14:38:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<buj7g7$1a5f$1@ulysses.noc.ntua.gr>`

```
I Want to create a database from database using powercobol and i don't know
how???

Example.

I have a database in access named a-data with a-table b-table c-table (table
names) and i want to create another database named b-data with a1-table from
a-table of a-data database.
```

#### ↳ Re: Powercobol and sql

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-21T02:20:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<400d2bb6_7@news.athenanews.com>`
- **References:** `<buj7g7$1a5f$1@ulysses.noc.ntua.gr>`

```

"Dionisis Vrionis" <diovr@dksoft.gr> wrote in message
news:buj7g7$1a5f$1@ulysses.noc.ntua.gr...
> I Want to create a database from database using powercobol and i don't
know
> how???
>
> Example.
>
> I have a database in access named a-data with a-table b-table c-table
(table
> names) and i want to create another database named b-data with a1-table
from
> a-table of a-data database.
>
>
Create an empty b-data database in Access. Make sure you have defined an
empty a1-table on it.

Make sure you have an @ODBC_inf entry in your COBOL85.CBR file (Let's say
this entry points to "odbc.inf")

In the odbc.inf file create entries for BOTH databases, naming them a-data
and b-data.

Make sure you have set up ODBC32 in Control Panel to recognise both these
DBs.

Use the SQL CONNECT statement to connect to a-data.

get a row of a-table

use the SQL USE statement to connect to b-data.

insert a row on a1-table.

If b-data is a temporary database you can create it dynamically through SQL,
but you will lose it at the end of the session. There may be a way to save
it; I've never looked.

The approach you are proposing may not be the best one. It might be better
to run a separate process to populate b-data, after you have finished with
a-data.

HTH

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
