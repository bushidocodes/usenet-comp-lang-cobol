[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol embedded sql source example

_1 message · 1 participant · 2006-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Re: cobol embedded sql source example

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-03T21:03:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zU86g.11321$Lm5.4638@newssvr12.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:...
> "Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
> news:0bmh52hnrqjpkdkv9icdcodpge1le2ff51@4ax.com...
…[14 more quoted lines elided]…
> long-standing problem I have had...
...
> But, following your lead, it looks like.........
>
…[4 more quoted lines elided]…
> Sheesh, I can hardly wait to test this now!

OK, I tested. I was close.  The sequence which works is

SqlPrepare   "SELECT * from empty_table"
SqlNumResultCols  ==>. returns number of columns
SqlDescribeCol     ==>    returns full info on each returned column

But, SQLExecDirect does the same thing - at least ODBC-2 with MS-Jet
(Access) Driver it does.

However, saving the actual execution is worth something if all I need at the
time is the ordered list of columns.. since there is no actual data
retrieval and building of a result set for the DBMS to do.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
