[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress OpenSQL SCROLLOPTION

_2 messages · 2 participants · 2000-01 → 2000-02_

---

### NetExpress OpenSQL SCROLLOPTION

- **From:** fabiochi <fabiochi@hotmail.com>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<164c000c.d6e042df@usw-ex0102-014.remarq.com>`

```
Hi,
I have some cobol programs that use cursor to fetch and update tables
on DB2 via odbc. I open a cursor for update, i fetch to the first
record and when I do the update statement (UPDATE xxxx SET xxxxx WHERE
CURRENT OF cur1) all the tables records are updated not the only
pointed by the fetch statement.

Do you have any idea about that ?

I found the SET SCROLLOPTION statement in the Microfocus docs but I
didn't find how I can use it.

Does anybody know it ?

Thanks in advance
Fabio


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: NetExpress OpenSQL SCROLLOPTION

- **From:** "Randy & Chris Zimmerman" <rwzcez91@execpc.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389749c2$0$1400@news.execpc.com>`
- **References:** `<164c000c.d6e042df@usw-ex0102-014.remarq.com>`

```
Positioned updates are possible if you use the directive SQL(USECURLIB=YES).
This will cause OESQL to use the ODBC Cursor Library.  You should make sure
that you have applied the latest OESQL web-sync fixpack to have this
functionality.

Because all SQL statement functionality doesn't translate to ODBC calls, you
can also use the DB2 ESQL preprocessor which is invoked via the DB2
directive.  See the Data Access on-line docs for more details.



fabiochi <fabiochi@hotmail.com> wrote in message
news:164c000c.d6e042df@usw-ex0102-014.remarq.com...
> Hi,
> I have some cobol programs that use cursor to fetch and update tables
…[16 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
