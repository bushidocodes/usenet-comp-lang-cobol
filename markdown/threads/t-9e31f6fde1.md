[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Connecting to SQL Server w/ NT authentication

_1 message · 1 participant · 2005-02_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Connecting to SQL Server w/ NT authentication

- **From:** "joshsackett" <joshsackett@gmail.com>
- **Date:** 2005-02-04T11:32:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107545536.180798.93630@c13g2000cwb.googlegroups.com>`

```
Hi,
I have an old old old version of MicroFocus COBOL that uses ESQL and
DB-LIB to connect to SQL Server. Currently the username and password is
hard-coded in each  .CBL build file and I want to change to NT
authentication.

This version cannot point to an ODBC or else I would do it that way. I
tried stripping out the username parameter and nothing was passed
through - SQL error:
"Login failed for user '(null)'. Reason: Not associated with a trusted
SQL Server connection."

Is there a switch to use within the COBOL program to tell it to pick up
the current user's NT information or am I stuck w/ SQL authentication
only?

Thanks,
Josh
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
