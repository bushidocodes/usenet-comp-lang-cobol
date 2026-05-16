[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Netexpress 3.0 and Oracle 8.0 - Cursors

_4 messages · 3 participants · 1999-03_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Netexpress 3.0 and Oracle 8.0 - Cursors

- **From:** "tommy" <tommynilsen@yahoo.ocm>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a45M2.176$gH6.887@news1.online.no>`

```

Hi.

Could anyone please tell me how to use a cursor to retrieve
first,previous,next and last record using a cursor ??

Or could anyone please tell me where to find information about it.........

Thanks

Tommy
```

#### ↳ Re: Netexpress 3.0 and Oracle 8.0 - Cursors

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dr6ai$6fv@dfw-ixnews11.ix.netcom.com>`
- **References:** `<a45M2.176$gH6.887@news1.online.no>`

```
Tommy,
  Are you talking about a SQL cursor - or a screen cursor?  My guess is the
the former, but you will get VERY different answers depending on what you
want.
```

##### ↳ ↳ Re: Netexpress 3.0 and Oracle 8.0 - Cursors

- **From:** "tommy" <tommynilsen@yahoo.ocm>
- **Date:** 1999-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g_kM2.48$Te3.67@news1.online.no>`
- **References:** `<a45M2.176$gH6.887@news1.online.no> <7dr6ai$6fv@dfw-ixnews11.ix.netcom.com>`

```
Yes, I'm talking about a SQL cursor.

Tommy


William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7dr6ai$6fv@dfw-ixnews11.ix.netcom.com...
> Tommy,
>   Are you talking about a SQL cursor - or a screen cursor?  My guess is
the
> the former, but you will get VERY different answers depending on what you
> want.
…[11 more quoted lines elided]…
> >Or could anyone please tell me where to find information about
it.........
> >
> >Thanks
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Netexpress 3.0 and Oracle 8.0 - Cursors

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-uFk1efeRjncd@Dwight_Miller.iix.com>`
- **References:** `<a45M2.176$gH6.887@news1.online.no>`

```
On Tue, 30 Mar 1999 14:20:09, "tommy" <tommynilsen@yahoo.ocm> wrote:

> 
> Hi.
…[4 more quoted lines elided]…
> Or could anyone please tell me where to find information about it.........

COBOL Unleashed has most of what you need.

You can't go forward and backward in the cursor, but you can setup 
multiple cursors, and order the rows differently. 

The Oracle manual really sucks on this issue, wanting instead to teach
you PL-SQL and stored procedures.  I got my answers from COBOL 
Unleashed using what is in the Oracle chapter in conjunction with what
is in the DB2 chapter.

You need to define your cursor.   This will end up creating no 
generated code.  If you perform it, like I do, and your compiler does 
not like empty paragraphs, you need to code a continue after the 
end-exec of the SQL.

Next you need to OPEN your cursor.

Then you execute consecutive FETCH's of the cursor until you have all 
the data, then CLOSE the cursor (to be nice).

If you want to update from said cursor, you can do that too using 
CURRENT OF cursorname in your WHERE clause of an UPDATE statement.

Does that give you enough to go on?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
