[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Get the @rowcount from SQL to Power

_4 messages · 2 participants · 2003-08_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Get the @rowcount from SQL to Power

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-08-07T17:26:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3213883.1060277215@dbforums.com>`

```

Hi. Now i have my system running with POWER x SQL
Works fines.
But to improve the systems a Need  some answers thar
i did not find anywhere, only here.

first : How to get the @ROWCOUNT from SQL to POWER
I Did this and doenst work

EXEC SQL BEGIN DECLARE  SECTION END-EXEC
01 sql-rowcount  pic s9(09)  comp-5
EXEC SQL END DECLARE SECTION   END-EXEC

IN PROCEDURE

EXEC SQL  SET :SQL-ROWCOUNT = @ROWCOUNT END-EXEC

i GET COMPILER ERROR

any idea ?
Tks
carlos Lages
```

#### ↳ Re: Get the @rowcount from SQL to Power

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-07T18:00:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308071700.598bba5a@posting.google.com>`
- **References:** `<3213883.1060277215@dbforums.com>`

```
Carlos lages <member129@dbforums.com> wrote

> EXEC SQL BEGIN DECLARE  SECTION END-EXEC
> 01 sql-rowcount  pic s9(09)  comp-5
…[6 more quoted lines elided]…
> i GET COMPILER ERROR

I think that you are very confused.

My guess is that you are trying to obtain the number of rows in a SQL
SELECT from a PowerCobol form table attribute using some invented
non-syntax.

If the SQL resulted in a table on the form then the EXEC SQL is not
required - use that table's RowCount attribute in a MOVE statement. 
If you are trying to get this from an SQL Cursor then @RowCount can't
be used and the SET syntax is nonsense anyway.
```

#### ↳ Re: Get the @rowcount from SQL to Power

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-08-08T16:07:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3218103.1060358855@dbforums.com>`
- **References:** `<3213883.1060277215@dbforums.com>`

```

I think you dont undstand me

If  i do that

selec  field1, field2  from tablex
where  codigo > 177

I want to know , how many rows  was selected.

Sql keeps  this information in @rowcount
I need to get  this .
How can i move @rowcount to a Cobol Host variable.

there is nothing about  Power cobol table Objetc.

Carlos Lages
```

##### ↳ ↳ Re: Get the @rowcount from SQL to Power

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-08-09T08:48:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh12df$td9$1@aklobs.kc.net.nz>`
- **References:** `<3213883.1060277215@dbforums.com> <3218103.1060358855@dbforums.com>`

```
Carlos lages wrote:

> I think you dont undstand me

I knew exactly what it is that you want, but you seemed to just make up 
what you thought may be code, but wasn't.
 
> If  i do that
> 
…[3 more quoted lines elided]…
> I want to know , how many rows  was selected.

Yes, I knew that.

> Sql keeps  this information in @rowcount

It may be that some specific versions of client interfaces for particular 
database systems maintain data items such as this. Which particular 
document did you read this in ?

For MS SQL Server (Sybase) the is an _extension_ that is 'SET ROWCOUNT ..' 
as you had but this is something _completely_ different:

"""SET ROWCOUNT limits the number of rows affected by all subsequent 
queries"""

This is not SQL, but is an extension.  Other databases do it with a LIMIT 
clause on the SELECT.  It is not the number of rows returned by a SELECT 
but is the maximum number that may be returned, if the select otherwise 
would return more then they are discarded.  There is also 'TOP n' in MS SQL 
(not ANSI) that is similar (but may result in different rows being 
returned).

> I need to get  this .
> How can i move @rowcount to a Cobol Host variable.

MS SQL Server (but not 'SQL') has a global variable @@rowcount. This is 
"The number of rows _affected_" and is not necessarily the number of rows 
found by a SELECT.  It _is_ the number of rows affected by a FETCH, UPDATE 
or INSERT.

It is probably what is returned in SQLERRD(3).
 
Remember - this is not 'MS SQL' that is running, it is Fujitsu client 
software, possibly using ODBC.

You could always do a 'pre select' of 

    SELECT COUNT(*) table WHERE ... INTO :myCount

or possibly write a database function to do it.

> there is nothing about  Power cobol table Objetc.

Power Cobol tables do define RowCount.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
