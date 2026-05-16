[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Coding an ODBC statement

_2 messages · 2 participants · 2001-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Coding an ODBC statement

- **From:** "Stephen Plotnick" <thepla@attglobal.net>
- **Date:** 2001-05-14T18:10:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b006832_4@news1.prserv.net>`

```
I have been able to create an SQL statement directly into Access to get a
desired result. I am now trying to create this statement into my Realia 3.1
ODBC and I am not being successful. Does anybody know the correct syntax for
the following statement?

SELECT *
FROM LongDesc
WHERE (LongDesc_Description LIKE 'drill*' or LongDesc_Description LIKE '*
drill*') and (LongDesc_Description LIKE 'master*' or LongDesc_Description
LIKE '* master*');

I am successful with single entry exact matches and starting with matches, I
need to substitute a "%" for the "*" for the starting with scenario.

Thanks.
```

#### ↳ Re: Coding an ODBC statement

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-15T19:01:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b00d8e5_4@Usenet.com>`
- **References:** `<3b006832_4@news1.prserv.net>`

```
Stephen,

What you are doing is excellent and I recommend people to "try" their SQL in
ACCESS Query mode, then cut and paste it into COBOL. (I do this myself,
especially where complex joins are involved, and it has saved me hours of
sweat.)

There are a couple of pitfalls though...

1.The syntax through ODBC may not be EXACTLY the same as that used in ACCESS
SQL Query (although it is usually very close...)

2. You must NOT specify the semi-colon terminator used in ACCESS, when using
COBOL.

You don't say whether the "failure" is due to a syntax error or whatever.
Please give the SQLSTATE when requesting assistance.

Here's a stab at what you requested, but without the SQLSTATE I can't be
sure...

EXEC SQL
   SELECT *
   FROM LongDesc
   WHERE ((LongDesc_Description LIKE 'drill*') OR
                   (LongDesc_Description LIKE '*drill*'))
                                                 AND
                  ((LongDesc_Description LIKE 'master*') OR
                  (LongDesc_Description LIKE '* master*'))
END-EXEC

Although it is syntactically correct, it is logically invalid and will
always return SQLSTATE 02000.

Cut and paste it into your program and you'll see what I mean.

Furthermore, ACCESS (used from COBOL) may grizzle at the underlines.  If so,
try removing them from the column names.

Hope this helps,

Pete.

"Stephen Plotnick" <thepla@attglobal.net> wrote in message
news:3b006832_4@news1.prserv.net...
> I have been able to create an SQL statement directly into Access to get a
> desired result. I am now trying to create this statement into my Realia
3.1
> ODBC and I am not being successful. Does anybody know the correct syntax
for
> the following statement?
>
…[6 more quoted lines elided]…
> I am successful with single entry exact matches and starting with matches,
I
> need to substitute a "%" for the "*" for the starting with scenario.
>
> Thanks.
>
>



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
