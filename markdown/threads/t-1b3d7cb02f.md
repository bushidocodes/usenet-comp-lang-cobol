[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF SQL Question

_4 messages · 4 participants · 1998-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### MF SQL Question

- **From:** "george e. zielinski" <ua-author-6589581@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6iq83l$6rg$1@newshost.cyberramp.net>`

```

We would like to attempt building dynamic SQL statements in a MF COBOL
Program using Oracle. Does anyone have any experiences in this arena? For
example, is the following snippet of code possible (it's basic- but you can
get the idea)? I'd appreciate any help or guidance you can offer.

MOVE "SALES_CY" TO FIELD1.
PERFORM 500-SQL-SUM.
MOVE TEST-TOTALS TO CY-TOTALS.

MOVE "SALES_LY" TO FIELD-1.
PERFORM 500-SQL-SUM.
MOVE TEST-TOTALS TO LY-TOTALS.
.
.
.
STOP RUN.

500-SQL-SUM.
EXEC SQL
SELECT SUM(FIELD-1)
INTO :TEST-TOTALS
FROM SALES_TBL
END-EXEC.
```

#### ↳ Re: MF SQL Question

- **From:** "darius cooper" <ua-author-16041747@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b3d7cb02f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6iq83l$6rg$1@newshost.cyberramp.net>`
- **References:** `<6iq83l$6rg$1@newshost.cyberramp.net>`

```

George E. Zielinski wrote in message
› We would like to attempt building dynamic SQL statements... is the
› following snippet of code possible :
…[9 more quoted lines elided]…
› 


Yes, it's possible. The syntax is not exactly like you wrote it, but it's
possible. What you;ll need to do is to build the SQL statement into a string
and execute that: MOVE "SELECT SUM(SALES_LY) FROM SALES_TBL " TO
WS-SQL-STRING.

If the number of columns and data-type of each column are known beforehand,
the procedure is relatively straightforward. If the number of data-types of
the columns are not know until run-time, then things get a little more
involved. Check you ORACLE manuals for more details.

- Darius
```

#### ↳ Re: MF SQL Question

- **From:** "ed.s..." <ua-author-13502311@usenetarchives.gap>
- **Date:** 1998-05-08T09:15:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b3d7cb02f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6iq83l$6rg$1@newshost.cyberramp.net>`
- **References:** `<6iq83l$6rg$1@newshost.cyberramp.net>`

```

While I've never worked with Oracle and MF Cobol together, I have worked with
both products and am currently an Oracle DBA. I see nothing wrong with your
code. You will need to get Oracle's Pro*Cobol pre-compiler to translate the
EXEC SQL calls into native Oracle calls. This is no different from any other
RDBMS.

In article <6iq83l$6rg$1.··.@new··p.net>,
"George E. Zielinski" wrote:
› 
› We would like to attempt building dynamic SQL statements in a MF COBOL
…[27 more quoted lines elided]…
› 


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: MF SQL Question

- **From:** "jagannadham garimella" <ua-author-17075108@usenetarchives.gap>
- **Date:** 1998-05-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b3d7cb02f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b3d7cb02f-p3@usenetarchives.gap>`
- **References:** `<6iq83l$6rg$1@newshost.cyberramp.net> <gap-1b3d7cb02f-p3@usenetarchives.gap>`

```

Hi

I worked with dynamic SQLs in MF Cobol and DB2. There, the complete SQL statement
has to be a variable (say sql-stmt). Then you prepare the stmt and execute (or
execute immediate). I guess there are only four stmts that are allowed with
dynamic sqls (declare, prepare, execute and execute immediate). You cannot have
part of a SQL stmt substituted with variables.

In your case, you have to define a sql-stmt thus:

01 sql-stmt.
05 filler value 'select '
05 column1 pic x( ).
05 filler pic value 'into '
05 host-var1 pic x(d).
05 filler value 'from SALES_TBL'
etc.

Hope this is useful.

Jagan

exec sql prepare statement from :sql-stmt (to be defined just like a varchar).
exec sql execute statement..
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
