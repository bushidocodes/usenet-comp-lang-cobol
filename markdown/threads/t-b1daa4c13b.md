[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can I use SELECT * INTO <DB NAME>?

_14 messages · 8 participants · 2004-02_

---

### Can I use SELECT * INTO <DB NAME>?

- **From:** "Hilda Ng" <hilda@taifuji.com>
- **Date:** 2004-02-13T11:59:22+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<402c68e6@news02.imsbiz.com>`

```
Dear All,

Can I use

EXEC SQL
    SELECT * INTO <DB NAME>
END-EXEC

in cobol program?

IF yes, can I have some examples?

Thanks!
```

#### ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2004-02-13T01:35:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0402130135.31656f64@posting.google.com>`
- **References:** `<402c68e6@news02.imsbiz.com>`

```
"Hilda Ng" <hilda@taifuji.com> wrote in message news:<402c68e6@news02.imsbiz.com>...
> Dear All,
> 
…[10 more quoted lines elided]…
> Thanks!

Again!

Note: I have no experience with mainframes, so this post could be
totally out of target if that is your platform.

Depending on the RDBMS you are using it either illegal or the result
will by far away from what you want. It is allways good practice to
specify the source of data: "select * FROM TABLE_NAME into
TEMPORARY_TABLE" is a good example. If what you are trying to do is
replicate the contents of the entire database, then you should relly
on the mechanisms provided by the database, namely, downloading  all
data and uploading it to the next Database. If you are trying to
POPULATE one Table with the content of another, then "insert NEW_TABLE
select * from OLD_TABLE" will do the trick, provided the data
definitions are equivalent.

regards

Paulo Vieira, Emporsoft
```

##### ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** <hilda@taifuji.com>
- **Date:** 2004-02-13T18:26:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0i8p1$k8n4@imsp212.netvigator.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com>`

```

Thank You,

Let I explain this question more clearly,
I use the Micro-Focus Net Express 4.0,
Now I faced a probelm, for example

in the working storage section

    EXEC SQL
               INCLUDE DATABASE-TABLE-NAME
    END-EXEC

in the procedure section

    I want to use

      EXEC SQL
                 SELECT *
                 INTO DATABASE-TABLE-NAME
                 FROM DATABASE-TABLE
      END-EXEC

      but the compiler said compiler errors.

    If I use

       EXEC SQL
                  SELECT *
                  INTO  DATABASE-TABLE-NAME-filed-name1,
                              DATABASE-TABLE-NAME-field-name2,
                              DATABASE-TABLE-NAME-field-name3
                  FROM DATABASE-TABLE
        END-EXEC

      Then there is no compiler error.

      How can I use the

      EXEC SQL
                 SELECT *
                 INTO DATABASE-TABLE-NAME
                 FROM DATABASE-TABLE
      END-EXEC

      in Micro Focus  Next Express 4.0?

      Regards.




"Paulo Vieira" <pvieira@emporsoft.pt>
???????:b5b8d7c7.0402130135.31656f64@posting.google.com...
> "Hilda Ng" <hilda@taifuji.com> wrote in message
news:<402c68e6@news02.imsbiz.com>...
> > Dear All,
> >
…[30 more quoted lines elided]…
> Paulo Vieira, Emporsoft
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-02-13T12:11:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P93Xb.6589$PY.1696@newssvr26.news.prodigy.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com>`

```
Anything between EXEC SQL  and END-EXEC should be valid SQL, unless the
COBOL compiler publisher offers explicit extensions.

>       EXEC SQL
>                  SELECT *
>                  INTO DATABASE-TABLE-NAME
>                  FROM DATABASE-TABLE
>       END-EXEC

.. is not valid SQL, as SQL "SELECT * " creates multiple output columns and
rows and requires multiple destintion columns; further, SELECT INTO may be
used only for queries which return exactly one row.

The INSERT statement shown previously  (INSERT INTO destination_table SELECT
* from source_table) will copy the contents of the first table into the
second.

To handle multiple rows of data in your program, you probably want to look
at a CURSOR.
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-13T11:23:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402131123.476909e1@posting.google.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com>`

```
<hilda@taifuji.com> wrote 

> Let I explain this question more clearly,

That would be helpful, in your original 'SELECT * INTO <DB NAME>" I,
and maybe others took 'DB Name' as meaning 'the name of a database'. 
It appeared that you wanted to duplicate a database into a new one.

> I use the Micro-Focus Net Express 4.0,
> 
…[14 more quoted lines elided]…
>       END-EXEC

I always do it the other way around, and don't forget that you need to
identify host variables with a :

        SELECT * FROM table
            INTO :WS-Table-Row

But this would attempt to read the whole table into that WS area.  You
need to have a WHERE clause to limit it to just one row - or use a
cursor.

     EXEC-SQL SELECT * FROM table
               WHERE code = :code
                INTO :WS-Table-Row
     END-EXEC
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 4)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-02-13T19:01:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zzdXb.16537$sO4.1429476@news20.bellglobal.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <217e491a.0402131123.476909e1@posting.google.com>`

```
SELECT * is possible, but it is a poor coding practice.  If someone adds
some columns to the table, it can break your program.

Better to code something like:

EXEC SQL
     SELECT column_1
                   , column_2
                    etc
      INTO :dclgen-column-1
               ,:dclgen-column-2
               etc
      FROM table
     WHERE code= :code

It's a little more work, but it saves trouble in the long run.



"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0402131123.476909e1@posting.google.com...
> <hilda@taifuji.com> wrote
>
…[37 more quoted lines elided]…
>      END-EXEC
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-14T10:41:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402141041.281a3264@posting.google.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <217e491a.0402131123.476909e1@posting.google.com> <zzdXb.16537$sO4.1429476@news20.bellglobal.com>`

```
"Don Leahy" <leahydon@nospamplease.netscape.net> wrote 

> SELECT * is possible, but it is a poor coding practice.  If someone adds
> some columns to the table, it can break your program.
…[13 more quoted lines elided]…
> It's a little more work, but it saves trouble in the long run.

It seems to me that is why he used:

> > >     EXEC SQL
> > >                INCLUDE DATABASE-TABLE-NAME
> > >     END-EXEC

Which, I took it, was built from the layout of current table spec.  It
would require that the program be recompiled after each table change.

I must admit that I do more SQL with Python (and Perl recently) where
such concerns are unrequired.

In fact I use a Python program to create Cobol table host variables
and matching SELECTs because they are too boring to do manually.
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 6)_

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-02-14T15:44:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aNvXb.13035$lK.871233@news20.bellglobal.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <217e491a.0402131123.476909e1@posting.google.com> <zzdXb.16537$sO4.1429476@news20.bellglobal.com> <217e491a.0402141041.281a3264@posting.google.com>`

```
Not quite.  The INCLUDE statement only brings in the DCLGEN, which may or
may not match the real table.  (I am speaking of DB2 for z/OS...other
flavours may behave differently).

Whatever DB2 you use, I agree with you that coding host variables is boring.
I use a Rexx tool to generate my SQL statements.

Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0402141041.281a3264@posting.google.com...
>
> It seems to me that is why he used:
…[12 more quoted lines elided]…
> and matching SELECTs because they are too boring to do manually.
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-02-13T23:25:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<402D5DAE.C91CC21D@shaw.ca>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com>`

```


hilda@taifuji.com wrote:

> Thank You,
>
> Let I explain this question more clearly,
> I use the Micro-Focus Net Express 4.0,
> Now I faced a probelm, for example

Have you tried using the Open ESQL Assistant ?  You can select it from your
IDE.

- 1 - Create DB (I'm using MS Access)
- 2 - Register the ODBC Driver for the DB you are using
- 3 - Open the ESQL Assistant and select your particular DB from those
registered
        under the ODBC
- 4 - Query a particular DB Table and you can set up a series of SQL
statements,
         selecting ALL or "some" columns. (The resulting generated syntax is
'wordy'
         but comprehensive). For each statement created from the ESQL
         Assistant you can automatically copy/paste into your source program
-
         bullet proof , clean compile code !
- 5 - From the ESQL Assistant you generate the copybook (in three sections -

        (a) SQL 'fields', (b) 'record' format and (c) 'null' fields)) for
the particular table.

ESQL Assistant at first appears a little complicated - it's worth the effort
of  following the process through - it will make life so much easier. For
more details on the ESQL, refer to the on-line DB Manual for N/E 4.0.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-02-13T23:48:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<402D631D.83E04CA7@shaw.ca>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <402D5DAE.C91CC21D@shaw.ca>`

```


"James J. Gavan" wrote:

> hilda@taifuji.com wrote:
>
…[6 more quoted lines elided]…
> Have you tried using the Open ESQL Assistant ?  You can select it from your

Follow-up on my previous - most importantly I should have said that having
generated a query via the ESQL Assistant you can 'run' the query from the ESQL
to test its results against a test copy of your  DB without any compiling !
(That way you can find out what you can and can't leave out in your SELECT).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-02-15T13:28:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<102vhvrbelf8oc7@corp.supernews.com>`
- **In-Reply-To:** `<c0i8p1$k8n4@imsp212.netvigator.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com>`

```
hilda@taifuji.com wrote:
>     EXEC SQL
>                INCLUDE DATABASE-TABLE-NAME
…[12 more quoted lines elided]…
>       but the compiler said compiler errors.

Ah ha - I think I know what you're trying to do.  You're trying to make 
SELECT act like a READ statement... in other words, given

01  My-Rec.
     12  My-Field-1   Pic X(13).
     12  My-Field-2   Pic 9(04).
     12  My-Field-3   Pic X(45).

you're wanting to select the table and have it insert each column, in 
order, into the record "structure", right?

It's been my experience (and the documentation supports) that this isn't 
how it works.  You can use the *, but you still have to name each 
column.  So, you could say...

Exec SQL
     SELECT *
       INTO :My-Field-1,
            :My-Field-2,
            :My-Field-3
       FROM Table_Name
End-Exec

You also may want to look at null indicators, if any of the fields may 
be null.  These are specified after the field return variables, and are 
negative if the field you selected is null.

This type of select also only works if you're returning a maximum of 1 
row.  If you find nothing, SQLState or SQLCode (depending on your 
implementation) will be set (SQLState for "nothing found" is "02000"). 
If you're expecting more than 1 row, you'll have to use a cursor - check 
your documentation on that if you need it.

Hope that helps...
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-15T17:47:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402151747.1a1297bc@posting.google.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <102vhvrbelf8oc7@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote 

> >       EXEC SQL
> >                  SELECT *
…[27 more quoted lines elided]…
> End-Exec

That is most probably implementation dependent, but at least some
allow the use of a group host variable to mean all the elements as
host variables.  From MF for DB2:

""" --------------------------------------------------
In such an example, the procedural statement:

     exec sql fetch s3 into
         :host-structure:indic
     end-exec

is equivalent to:

     exec sql fetch s3 into
         :sumh:indic1, :avgh:indic2, :minh:indic3,
         :maxh:indic4, :varchar
     end-exec
----------------------------------- """

Similar for Fujitsu, or at least the most recent versions.  In early
versions each host variable _had_ to be an 01 level which precluded
any grouping.
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-02-16T10:18:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1031r66bhic4586@corp.supernews.com>`
- **In-Reply-To:** `<217e491a.0402151747.1a1297bc@posting.google.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com> <102vhvrbelf8oc7@corp.supernews.com> <217e491a.0402151747.1a1297bc@posting.google.com>`

```
Richard wrote:
> LX-i <lxi0007@netscape.net> wrote 
> 
…[31 more quoted lines elided]…
> any grouping.

Thanks for the info.  :)  I know our stuff is all 01-levels, which 
caused a significant learning curve for our folks who had never used 
non-record structures.  (The UNISYS DMS 2200 network database uses 
records that are actually records - the schema that's copied into the 
program is a named record with a 01-level, and all the data items are 
under that, just like a file would be with it's associated FD.)
```

###### ↳ ↳ ↳ Re: Can I use SELECT * INTO <DB NAME>?

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-02-15T20:21:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<54lv209gpl2ioug14i699hkqp33fc0n23i@4ax.com>`
- **References:** `<402c68e6@news02.imsbiz.com> <b5b8d7c7.0402130135.31656f64@posting.google.com> <c0i8p1$k8n4@imsp212.netvigator.com>`

```
On Fri, 13 Feb 2004 18:26:44 +0800, <hilda@taifuji.com> wrote:

>
>Thank You,
…[31 more quoted lines elided]…
>        END-EXEC

Maybe a 
exec sql
   insert into database-table-name (select * from database-table)
end-exec


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
