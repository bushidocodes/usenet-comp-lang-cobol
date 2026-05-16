[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MS/SQL weird input

_7 messages · 3 participants · 2008-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### MS/SQL weird input

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-07-21T17:35:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com>`

```
Hi,

It's been awhile that my Cobol program (that accesses MS SQL v8.0)
can't perfectly read the 'entire' records on selected range. The code
below

            EXEC SQL
             DECLARE CSR20 CURSOR FOR SELECT DISTINCT
                    A.RECCNT
                   ,A.TERMNO
                   ,A.OPERNO
                   ,A.TRANNO
                   ,A.PRODNO
                   ,A.ITEM_DESC
                   ,A.DEPT
                   ,A.VENDOR
                   ,A.RECCODE
                   ,A.QTY
                   ,A.DTE
                   ,A.PRICE
                   ,A.TAX
               FROM SL A
              WHERE ( A.DTE = :SL-DTE )
            END-EXEC

works sometime.... but on some instances, it is not reading "all" the
records, I mean it is reading 'partial' records. The volume of the
selected range option is about 350 records. Is anyone here experience
the MS/SQL server behaviour? I am using ODBC (User DSN) connection on
such application to connect to MS/Sql server.
```

#### ↳ Re: MS/SQL weird input

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-22T22:37:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6elrifF78kd7U1@mid.individual.net>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com>`

```


"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com...
> Hi,
>
…[27 more quoted lines elided]…
> such application to connect to MS/Sql server.

This code is syntactically fine.

How is the Host Variable SL-DTE defined? What value are you moving to it?

When you say "partial records" do you mean part of a row, with some columns 
not returned? Are these non returned columns contiguous or interspersed with 
returned columns? What SQLSTATE is returned when you get a "partial record"?

Depending on your answers to the above, I believe I can diagnose your 
problem.

Pete.
```

##### ↳ ↳ Re: MS/SQL weird input

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-07-22T06:54:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com> <6elrifF78kd7U1@mid.individual.net>`

```
SL-DTE is defined as 'char' that has a date (string date) value,
example '2008-06-01'. So basically my code is;

 MOVE "2008-06-01" TO SL-DTE

and the next thing is the EXEC SQL as defined earlier in my post. Not
using SQLSTATE though to monitor sql execution but SQLCODE that
returns a +0000 value, which actually a successful read. Following the
sql code above is below;

            EXEC SQL OPEN CSR20 END-EXEC
            PERFORM UNTIL (SQLCODE < 0) OR (SQLCODE = +100)
              EXEC SQL
              FETCH CSR20 INTO
                  :SL-RECCNT:SL-RECCNT-NULL
                 ,:SL-TERMNO:SL-TERMNO-NULL
                 ,:SL-OPERNO:SL-OPERNO-NULL
                 ,:SL-TRANNO:SL-TRANNO-NULL
                 ,:SL-PRODNO:SL-PRODNO-NULL
                 ,:SL-ITEM-DESC:SL-ITEM-DESC-NULL
                 ,:SL-DEPT:SL-DEPT-NULL
                 ,:SL-VENDOR:SL-VENDOR-NULL
                 ,:SL-RECCODE:SL-RECCODE-NULL
                 ,:SL-QTY:SL-QTY-NULL
                 ,:SL-DTE:SL-DTE-NULL
                 ,:SL-PRICE:SL-PRICE-NULL
                 ,:SL-TAX:SL-TAX-NULL
              END-EXEC
             *>
             *>sequel message(SQLCODE / SQLERRMC)
              IF SQLCODE = 0

                ...do process record...

              END-IF
            END-PERFORM
            EXEC SQL CLOSE CSR20 END-EXEC


What I'm looking at is the 'SELECT DISTINCT' phrase that I coded when
selecting the range of records (usually around 350 records). Could it
be possible to just use SELECT alone instead? The funny thing here is
that it is getting the 'entire' record or columns (sorry about the
partial word) per fetch.  Except that say, instead of getting the
350recs, it is fetching only 280recs.

The MS/SQL tables are not 'my' (design) table. Somebody else wrote the
front-end and I do the fetching in Cobol in PC-based platform for AS/
400 data migration at batch. When I tried to "re-run" my program
again, it is then that it is fetching 350recs. Big '????'

Tried checking 'DISPLAYING' the very last record that it fetched, so
far nothing wrong with it. Of course can't say actually what record it
did fail when the SQLCODE becomes not = 0.
```

###### ↳ ↳ ↳ Re: MS/SQL weird input

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-23T06:45:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6emo69F7v93sU1@mid.individual.net>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com> <6elrifF78kd7U1@mid.individual.net> <e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com>`

```


"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message
news:e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com...
> SL-DTE is defined as 'char' that has a date (string date) value,
> example '2008-06-01'.

So, PIC X(10).    then?

>So basically my code is;
>
…[24 more quoted lines elided]…
>              END-EXEC

If you never use the indicator variables or test them, might be better to
leave them out.
>             *>
>             *>sequel message(SQLCODE / SQLERRMC)
…[11 more quoted lines elided]…
> be possible to just use SELECT alone instead?

Yes, it is valid to do that, but duplicate rows will be returned if present.


>The funny thing here is
> that it is getting the 'entire' record or columns (sorry about the
> partial word) per fetch.  Except that say, instead of getting the
> 350recs, it is fetching only 280recs.

Ah, so the problem is not a partial row, it is a partial dataset...

Are you absolutely sure that the date you are using is not causing some rows
to be filtered?

ACCESS has some quirks when it comes to Date/Time.

Say, for example you want all the transaction for the 20th July, 2008...

Try this....

move "#2008-07-20x00:00:00#" to SL-DTE
move "#2008-07-20x23:59:59#" to SL-DTE1

... where the x in the above is a single blank.

Then...

            EXEC SQL
             DECLARE CSR20 CURSOR FOR SELECT DISTINCT
                    A.RECCNT
                   ,A.TERMNO
                   ,A.OPERNO
                   ,A.TRANNO
                   ,A.PRODNO
                   ,A.ITEM_DESC
                   ,A.DEPT
                   ,A.VENDOR
                   ,A.RECCODE
                   ,A.QTY
                   ,A.DTE
                   ,A.PRICE
                   ,A.TAX
               FROM SL A
              WHERE ( A.DTE  BETWEEN  :SL-DTE AND :SL-DTE1 )
            END-EXEC

You can test it by running it as a query in Access and substituting the
literals above for the host variable names.

(Cut and paste this code into Access query in SQL view...)

     SELECT DISTINCT
                    A.RECCNT
                   ,A.TERMNO
                   ,A.OPERNO
                   ,A.TRANNO
                   ,A.PRODNO
                   ,A.ITEM_DESC
                   ,A.DEPT
                   ,A.VENDOR
                   ,A.RECCODE
                   ,A.QTY
                   ,A.DTE
                   ,A.PRICE
                   ,A.TAX
               FROM SL A
              WHERE ( A.DTE  BETWEEN  "#2008-07-20 00:00:00#" AND
"#2008-07-20 23:59:59#")


I tried it on a database I have with a number of dates (and changing the
table name and fetched fields of course) and it worked correctly.

>
> The MS/SQL tables are not 'my' (design) table. Somebody else wrote the
> front-end and I do the fetching in Cobol in PC-based platform for AS/
> 400 data migration at batch. When I tried to "re-run" my program
> again, it is then that it is fetching 350recs. Big '????'

It is probably being caused by the Date formatting in Access. Different
times can cause problems. The above will establish whether that's it or not.

Other possibilities:

1. If you are sharing this database with an AS400 it is possible that the DB
is getting locked (or some pages of it are) at the time you go to access it.
Re-running works correctly because the locks have been released.

2. If you are doing  committed INSERT ,UPDATE, or DELETE on the SL table
during the "...do process record" in the above, you will lose the cursor
position and it will appear to have finished. (You neeed to HOLD the
cursor). If you use SQLSTATE instead of SQLCODE it will return a S1010
'function sequence error',  but I don't know what it does with SQLCODE.
Probably returns a negative, which gets treated as EOF in your code. If the
maintenance actions are based on a set of criteria they could occur anywhere
in your processing stream and so you would get a different number of records
being processed in your sequential FETCH cycle, which would look like it had
hit EOF.

3. If there are no maintenance actions going on during the sequential
process, the most likely cause will be the filter on date taking records out
because they don't match. The code above will determine this. If it
consistently returns the same number of records then that is the problem and
the code above fixes it.


>
> Tried checking 'DISPLAYING' the very last record that it fetched, so
> far nothing wrong with it. Of course can't say actually what record it
> did fail when the SQLCODE becomes not = 0.

Why not get a check on SQLSTATE as well? It tells more than SQLCODE. You
should get "00000" if it's OK, or "02000" if it is EOF (no data found on the
FETCH). If you are doing updates with an active cursor that isn't opened for
UPDATE or HOLD I reckon you'll get "S1010"... Any other code returned will
be more informative than SQLCODE.

Hope this helps,

Pete.
```

###### ↳ ↳ ↳ Re: MS/SQL weird input

_(reply depth: 4)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-07-23T23:57:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7642b98-0526-4a98-b6fa-327d907f7cfd@h1g2000prh.googlegroups.com>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com> <6elrifF78kd7U1@mid.individual.net> <e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com> <6emo69F7v93sU1@mid.individual.net>`

```
Thanks Pete.

That was a help. I will try to check SQLSTATE this time. As per MF
documentation though, the SQLCODE is used with SQLERRMC explaining the
sequel error if any. Haven't monitored SQLSTATE yet. This time around
I'm going to.

As for the behaviour though, I still need to verify exactly how MS/SQL
locked a datarow. It seems to me that in real scenario the SQL tables
are being used while the batch Cobol program is extracting/reading
(SELECT) records from it.

If it (MS/SQL) does lock records, how can it be retrieve/read by the
Cobol program? I guess even other VB/C# apps couldn't access locked
records from MS/SQL.
```

###### ↳ ↳ ↳ Re: MS/SQL weird input

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-25T00:30:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6eraujF8gpsbU1@mid.individual.net>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com> <6elrifF78kd7U1@mid.individual.net> <e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com> <6emo69F7v93sU1@mid.individual.net> <a7642b98-0526-4a98-b6fa-327d907f7cfd@h1g2000prh.googlegroups.com>`

```


"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:a7642b98-0526-4a98-b6fa-327d907f7cfd@h1g2000prh.googlegroups.com...
> Thanks Pete.
>
> That was a help.

Good... :-)

>I will try to check SQLSTATE this time. As per MF
> documentation though, the SQLCODE is used with SQLERRMC explaining the
> sequel error if any. Haven't monitored SQLSTATE yet. This time around
> I'm going to.

Check SQLMsg at the same time. It serves the same function as SQLERRMC.

>
> As for the behaviour though, I still need to verify exactly how MS/SQL
> locked a datarow.

It seems very unlikely to me that this is the problem. Even if rows are 
locked by the "other" system you should still be able to access them for 
reading. It could be that there are not enough connections available in the 
pool for both systems, but then youwould get a different SQLSTATE. If your 
connection succeeds (You DO check it, don't you... :-)?), your SELECTs 
should succeed.

I think it is likely to be the date field filtering stuff, that's why I 
suggested you use the BETWEEN. There are a lot of date functions available 
with MS ACCESS SQL and it gets pretty confusing. I've had all kinds of 
problems with dates in ACCESS but I've kind of got the hang of it now.

Today I've been working on an SQLSTATE 01S01 "Error on row". There is 
nothing wrong with the row that I can see, and I can run a query in Access 
and fetch it without problem. I pasted the same query into COBOL and it 
returns no data and 01S01...:--) The only difference is that COBOL reads the 
columns into host variables. I checked the size and type of every host 
variable and they are fine. I believe it may be because COBOL doesn't have a 
DATE type (as Robert pointed out earlier) and there are dates in the row. 
(I'm reading them into pic x(10) variables which SHOULD be OK... I can 
access the row into HVs in C# without problem but C# has a DATE type... 
Tomorrow I'll try commenting out rows and HVs and see if I can run it down. 
The point is that dates MAY be problematic when using ACCESS in COBOL.

> It seems to me that in real scenario the SQL tables
> are being used while the batch Cobol program is extracting/reading
> (SELECT) records from it.
>

That SHOULD be fine...

> If it (MS/SQL) does lock records, how can it be retrieve/read by the
> Cobol program? I guess even other VB/C# apps couldn't access locked
> records from MS/SQL.

Not if something has gone horribly wrong with the RDBMS. Might be time to 
run an ODBC trace and see what's going on...

Have you tried running your application when the other system is NOT active?

Good Luck!!

Pete.
```

###### ↳ ↳ ↳ Re: MS/SQL weird input

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-24T19:09:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nd6i845ghbma8066dm35jgktua406g3vf5@4ax.com>`
- **References:** `<01daf6e1-47d8-4a16-a2c3-a61febd1926d@i24g2000prf.googlegroups.com> <6elrifF78kd7U1@mid.individual.net> <e570df29-41bc-4474-83e4-24ab64e42d9c@l42g2000hsc.googlegroups.com> <6emo69F7v93sU1@mid.individual.net> <a7642b98-0526-4a98-b6fa-327d907f7cfd@h1g2000prh.googlegroups.com>`

```
On Wed, 23 Jul 2008 23:57:08 -0700 (PDT), Rene_Surop <infodynamics_ph@yahoo.com> wrote:

>Thanks Pete.
>
…[11 more quoted lines elided]…
>Cobol program?

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
