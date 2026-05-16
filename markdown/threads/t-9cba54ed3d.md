[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# QUESTION USING SCROLLABLE CURSORS IN EMBEDED SQL

_2 messages · 2 participants · 1999-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### QUESTION USING SCROLLABLE CURSORS IN EMBEDED SQL

- **From:** "Juan Rodriguez" <juanr@wilwel.com>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YBya3.1042$RL.27806@news.ntr.net>`

```

We are running into some obstacles when Using Cursors with Embeded SQL and
we are wondering if maybe you have some suggestions that may help us.
We are currently using Microfocus Netexpress 3.0 and Flexus SP2 for the GUI
front-end.
We are also accessing data from an MS SQL Database using Embeded SQL.

We have a situation where we have a Cursor tha retrieves 20,000 rows from a
database Table.  We have this SP2 GUI Window that displays 10 of those rows
at a time and allows the User to scroll forward(FETCH NEXT), scroll
back(FETCH PRIOR), reposition at the end(FETCH LAST), and reposition at the
beginning(FETCH FIRST).
 Because the number of rows is very large, we need to also allow the User to
randomly reposition within the Cursor.  At this time the User inputs an item
number and presses a fuction key that causes the program to performs
consecutive Fetches until it finds the item requested.   Then it displays 10
items from that point forward.

Is there a way to reposition within the Result set from a Cursor without
having to FETCH NEXT , FETCH NEXT, ...FETCH NEXT,
or FECTH PRIOR, FETCH PRIOR,....FETCH PRIOR  to get to the item desired.?

There exists a FETCH RELATIVE and a FETCH OBSOLUTE, but they are not
supported.

Any help from you is greatly appreciated.
Best Regards,
JCR
```

#### ↳ Re: QUESTION USING SCROLLABLE CURSORS IN EMBEDED SQL

- **From:** Jeen van der Meer <JMEER@t-online.de>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376BB884.FF6C4831@t-online.de>`
- **References:** `<YBya3.1042$RL.27806@news.ntr.net>`

```
Hi Juan,

If could show us the declaration of the cursor I or someone else, might
be able to show you how to solve your problem.
Without having seen the code, I could suggest an additional SQL
statement returning a single row. So you would have to have data from a
unique defined field in your table.
I hope this makes some sense to you.
If not you can always e-mail me.

Jeen


Juan Rodriguez schrieb:
> 
> We are running into some obstacles when Using Cursors with Embeded SQL and
…[25 more quoted lines elided]…
> JCR
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
