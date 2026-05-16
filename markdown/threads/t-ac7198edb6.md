[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing multiple databases in Net Express V3.0

_5 messages · 3 participants · 2002-06 → 2002-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Accessing multiple databases in Net Express V3.0

- **From:** "Bill Gentry" <billgentry2@comcast.net>
- **Date:** 2002-06-30T21:33:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com>`

```
Hello all,

I've been working up an app that needs to process 2 MS Access databases
concurrently.   It will connect to both DB's via ODBC "connect" statements,
issue SQL's against both of them, then disconnect.

First off, I'm not sure if this will even work or not, at least with the IDE
I'm using.  I've been into MicroFocus' Knowledge base, and All I saw was one
program sample where you could setup multiple connections, but you had to
"swap" the connections, similar to closing one file before opening another.

In any case, here's a couple of code snippets.  I'm not posting the whole
program for the sake of brevity... if anyone wants to see the whole thing,
I'll post it.

First, I declare my two databases like this:
       110-DECLARATIVES.

           EXEC SQL
               DECLARE KCONN DATABASE
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.
           EXEC SQL
               DECLARE TCONN DATABASE
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.

       120-CONNECTIONS.
           MOVE 'KSYS'           TO KSERVER.
           MOVE ' '              TO KUSER.
           EXEC SQL
               CONNECT TO :KSERVER
                       AS KCONN
                     USER :KUSER
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.

           MOVE 'TRANS1'       TO TSERVER.
           MOVE ' '            TO TUSER.
           EXEC SQL
              CONNECT TO :TSERVER
                      AS TCONN
                    USER :TUSER
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.

Then, later in the program, I attempt to fetch some data from the database
I'd declared as "KCONN"

           EXEC SQL
              AT KCONN
               DECLARE SUBMCURS CURSOR
                  FOR
                     SELECT TranFile FROM Submitted
                     Where ExtractID = 'ZZ'
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.
           EXEC SQL
               OPEN SUBMCURS
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.
           EXEC SQL
               FETCH SUBMCURS INTO :TRAN-FILE-NAME
           END-EXEC.
           PERFORM 950-CHECK-SQLCODE.

The last SQL statement is giving me an SQLCODE of -0000019514 "cursor is not
prepared".   The netexpress documentation lists the "AS" as valid code in
the declare cursor, if you have a "db_name" in use, as I do in this program.
It's not listed as valid code for the "OPEN" or the "FETCH" commands.

Anyway, if anyone has had any luck with this, I'd appreciate the input.  I'm
going to keep working on it and I'll post the "fix" if I ever find one.   I
may have to re-think the app, though:  Dump the contents of the first
database to text files, then connect to the second database for processing.

Thanks,
Bill
```

#### ↳ Re: Accessing multiple databases in Net Express V3.0

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-30T23:08:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D1F903E.406C4E58@shaw.ca>`
- **References:** `<yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com>`

```


Bill Gentry wrote:

> Hello all,
>
…[75 more quoted lines elided]…
> Bill

I'm a real 'newbie' at SQL so I'm using the ESQL Assistant to generate my
'basic' queries. The following is OO but see if it ties in similar to what you
are doing. The only change I have made is to substitute SQLTATE for SQL:CODE :-

$set sql (ansi92entry) sql (dbman=ODBC)

 *>-----------------sqlconct.cbl----------------------------------

 Class-id.          SQLConnection
                    inherits from SQLErrors.

 Class-control.     SQLConnection         is class "sqlconct"
                    SQLErrors             is class "sqlerror"
                    .
*>---------------------------------------------------------------
 FACTORY.
 *>--------------------------------------------------------------
 Method-id. "new".
 *>--------------------------------------------------------------
 Linkage section.
 01 lnk-self                         object reference.
 Procedure Division returning lnk-self.
   invoke super "new" returning lnk-self
 End Method "new".
 *>--------------------------------------------------------------
 END FACTORY.
 *>--------------------------------------------------------------
 OBJECT.
 *>--------------------------------------------------------------
 OBJECT-STORAGE SECTION.
 *>--------------------------------------------------------------
 copy "sqlerror.cpy" replacing ==(tag)== by ==ws==.
 01 os-Parent                            object reference.

 *> DB IDs

 01 ws-dbID              pic 9 value 0.
    88 NoID              value 0.
    88 GeneralID         value 1.          *> Server1
    88 FacilityID        value 2.          *> Server2

 *> DB Names

 01 ws-CurrentName       pic x(10) value spaces.
 01 ws-DbName occurs 2.
    05 pic x(10)         value "Corrosion".
    05 pic x(10)         value "Facility".

 EXEC SQL BEGIN DECLARE SECTION END-EXEC.
 01  SQLSTATE    PIC X(5).
 EXEC SQL END DECLARE SECTION END-EXEC.

 01 charx                    pic x.

 *>--------------------------------------------------------------
 Method-id. "DBConnect".
 *>--------------------------------------------------------------
 Linkage section.
 01 lnk-id                              pic 9.
 01 lnk-result                          pic 9(03).

 Procedure Division using     lnk-id
                    returning lnk-result.

   Move zeroes to lnk-result

   Evaluate true
     when lnk-id = ws-dbID
          EXIT METHOD
     when lnk-id = 1
           move lnk-ID to ws-dbID
           move ws-DbName(ws-dbID) to ws-CurrentName
           EXEC SQL SET CONNECTION Server1 END-EXEC
     when other
           move lnk-ID to ws-dbID
           move ws-DbName(ws-dbID) to ws-CurrentName
           EXEC SQL SET CONNECTION Server2 END-EXEC
   End-evaluate

   if    SQLSTATE <> '00000'
         invoke super "sqlstateMessage"
           using ws-dbID, SQLSTATE, ws-CurrentName
         move 99 to lnk-result
   End-if

 End Method "DBConnect".
 *>--------------------------------------------------------------
 Method-id. "DBDisconnect".
 *>--------------------------------------------------------------
 Procedure Division.

   EXEC SQL DISCONNECT Server1 END-EXEC
   EXEC SQL DISCONNECT Server1 END-EXEC

 End Method "DBDisconnect".
 *>--------------------------------------------------------------
 Method-id. "setDBs".
 *>--------------------------------------------------------------
 Linkage section.
 01 lnk-result                              pic 9(03).
 Procedure Division returning lnk-result.

  move zeroes to lnk-result

  set GeneralID to true
  EXEC SQL CONNECT TO "Corrosion" as Server1 END-EXEC

   if   SqlState <> "00000"
        perform ERROR-MESSAGE
   End-if

  set FacilityID to true
  EXEC SQL CONNECT TO "Facility"  as Server2 END-EXEC

   if   SqlState <> "00000"
        perform ERROR-MESSAGE
   End-if

 EXIT METHOD.

 ERROR-MESSAGE.

  invoke super "sqlstateMessage"
  using ws-ErrorID, SqlState, ws-CurrentName
  move 99 to lnk-result
  .

 End Method "setDBs".
 *>--------------------------------------------------------------
 End OBJECT.
 End CLASS SQLConnection.
 *>---------------------------------------------------------------

From my Business Logic Class 'EditClients' I  invoke the Client Table :-

$set sql (ansi92entry) sql (dbman=ODBC)

 *>-----------------clitable.cbl---------------------------------

 Class-id.          ClientsTable
                    inherits from SqlErrors.

 Class-control.     ClientsTable            is class "clitable"
                    SqlErrors               is class "sqlerror"
                    .
 *>--------------------------------------------------------------
 FACTORY.
 *>--------------------------------------------------------------
 End FACTORY.
 *>------------------------------------------------------------
 OBJECT.
 *>----------------------------------------------------------
 OBJECT-STORAGE SECTION.
 EXEC SQL BEGIN DECLARE SECTION END-EXEC.
 01  SQLSTATE                    pic x(5).
 EXEC SQL END DECLARE SECTION END-EXEC.

 copy "clients.cpy".
 copy "CliRecrd.cpy" replacing ==(tag1)== by ==01 ClientsRecord==
                               ==(tag)==  by ==Clients==.
 copy "sqlerror.cpy" replacing ==(tag)==  by ==ws==.

 01 ws-dbID              pic 9 value 1. *> General
 01 os-DBI               object reference.
 01 os-SqlConnection     object reference.
 *>--------------------------------------------------------------

I *think* you only need the cursor where you are going to FETCH more than one,
so I''ve included methods for 'one' and 'cursor'. BTW if you are *new* to DB, it
might pay to try using the ESQ: Assistant to ensure 100% syntax :-

*>---------------------------------------------------------
Method-id. "getClientDefaults".
*>---------------------------------------------------------
Linkage section.
01 lnk-key                       pic x(03).
01 lnk-record.
copy "sqlreslt.cpy" replacing ==(tag)== by ==05 lnk==.
copy "clideflt.cpy" replacing ==(tag)== by ==lnk==.

Procedure Division using     lnk-Key
                   returning lnk-record.

set ResultOK to true
invoke os-SqlConnection "DBconnect"
       using ws-dbID returning lnk-SqlResult

if TableError
   EXIT METHOD
End-if

move lnk-key to Clients-cliID, ws-ErrorID(1:3)
move "00"    to Clients-FacID, ws-ErrorID(4:2)

     EXEC SQL
      SELECT DISTINCT
            ,`A`.`LifeYears`
            ,`A`.`Percent1`
            ,`A`.`Percent2`
            ,`A`.`Range1`
            ,`A`.`Range2`
            ,`A`.`Range3`
            ,`A`.`Range4`
      INTO
           :Clients-LifeYears:Clients-LifeYears-NULL
          ,:Clients-Percent1:Clients-Percent1-NULL
          ,:Clients-Percent2:Clients-Percent2-NULL
          ,:Clients-Range1:Clients-Range1-NULL
          ,:Clients-Range2:Clients-Range2-NULL
          ,:Clients-Range3:Clients-Range3-NULL
          ,:Clients-Range4:Clients-Range4-NULL
        FROM `Clients` A
       WHERE ( `A`.`CliId` = :Clients-CliId )
        AND  ( `A`.`FacId` = :Clients-FacId )
     END-EXEC

Evaluate true
    when SQLSTATE = "00000"
     move Clients-ClientSubData to lnk-ClientSubData
    when SQLSTATE = "02000"              *> No more rows
         set RecNotFound to true
    when other
         invoke self "setErrorMessage"
         set TableError to true
End-Evaluate

End Method "getClientDefaults".
*>---------------------------------------------------------

And for more than "one" -  Note that ESQL Assistant generates the next cursor
number that you need for each query, plus each of my queries invokes "DBConnect"
to check I'm accessing the correct database:-

*>--------------------------------------------------------------
Method-id. "makeClientCollection".
*>--------------------------------------------------------------
Local-storage section.
copy "clilistrec.cpy" replacing ==(tag)== by ==ls==.
Linkage section.
01 lnk-PrimeKey.
   05 lnk-ClientNumber               pic x(03).
   05 lnk-FacilityNumber             pic x(02).
copy "sqlreslt.cpy" replacing ==(tag)== by ==01 lnk==.

Procedure Division using     lnk-PrimeKey
                   returning lnk-SqlResult.

set ResultOK to true
initialize ls-CliListrecord
invoke os-SqlConnection "DBconnect"
       using ws-dbID returning lnk-SqlResult

if TableError
   EXIT METHOD
End-if

EXEC SQL
 DECLARE CSR29 CURSOR FOR SELECT
        `A`.`CliId`
       ,`A`.`FacId`
       ,`A`.`Shortname`
   FROM `Clients` A
  WHERE ( `A`.`FacId` = '00' )
END-EXEC
EXEC SQL OPEN CSR29 END-EXEC

PERFORM UNTIL SQLSTATE <> '00000'
  EXEC SQL
  FETCH CSR29 INTO
      :Clients-CliId:Clients-CliId-NULL
     ,:Clients-FacId:Clients-FacId-NULL
     ,:Clients-Shortname:Clients-Shortname-NULL
  END-EXEC

   Evaluate true

      when SQLSTATE = "00000"
        initialize ls-CliListRecord
        move Clients-CliID     to Cli-ID
        move Clients-FacID     to Fac-ID
        move Clients-shortname to Cli-ShortName
        invoke os-DBI "newListRecord" using ls-CliListRecord

        *> Note : above data is returned to os-DBI to add
        *> to the appropriate collection/dictionary entry

     when SQLSTATE = "02000"               *> no more rows
          EXIT PERFORM
     when other
          move Clients-CliID to ws-ErrorID(1:3)
          move Clients-FacID to ws-ErrorID(4:2)
          invoke self "setErrorMessage"
          set TableError to true
          EXIT METHOD
   End-evaluate
END-PERFORM
EXEC SQL CLOSE CSR29 END-EXEC

End Method "makeClientCollection".
*>--------------------------------------------------------------

HTH

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Accessing multiple databases in Net Express V3.0

- **From:** "Bill Gentry" <billgentry2@comcast.net>
- **Date:** 2002-07-01T13:52:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8ZT8.487169$Gs.34056508@bin5.nnrp.aus1.giganews.com>`
- **References:** `<yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com> <3D1F903E.406C4E58@shaw.ca>`

```
Hi Jimmy,

As always, thanks for the input!  I'm somewhat of a newbie at SQL myself
.... maybe "experienced beginner" or "light intermediate" would describe me
best.   Anyway, I'm going to take a closer look at your code to see if it
applies to what I'm doing.  Basically, my app is going to query DB1 and
"post" the results to DB2.   I've already found a work-around to my problem,
but it would be "neat" to not have to disconnect from DB1 before posting to
DB2.  I guess I'm a bit a###-retentive.

I'll keep the NG posted on my progress.

Thanks again,
Bill


"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D1F903E.406C4E58@shaw.ca...
>
>
…[5 more quoted lines elided]…
> > concurrently.   It will connect to both DB's via ODBC "connect"
statements,
> > issue SQL's against both of them, then disconnect.
> >
> > First off, I'm not sure if this will even work or not, at least with the
IDE
> > I'm using.  I've been into MicroFocus' Knowledge base, and All I saw was
one
> > program sample where you could setup multiple connections, but you had
to
> > "swap" the connections, similar to closing one file before opening
another.
> >
> > In any case, here's a couple of code snippets.  I'm not posting the
whole
> > program for the sake of brevity... if anyone wants to see the whole
thing,
> > I'll post it.
> >
…[31 more quoted lines elided]…
> > Then, later in the program, I attempt to fetch some data from the
database
> > I'd declared as "KCONN"
> >
…[17 more quoted lines elided]…
> > The last SQL statement is giving me an SQLCODE of -0000019514 "cursor is
not
> > prepared".   The netexpress documentation lists the "AS" as valid code
in
> > the declare cursor, if you have a "db_name" in use, as I do in this
program.
> > It's not listed as valid code for the "OPEN" or the "FETCH" commands.
> >
> > Anyway, if anyone has had any luck with this, I'd appreciate the input.
I'm
> > going to keep working on it and I'll post the "fix" if I ever find one.
I
> > may have to re-think the app, though:  Dump the contents of the first
> > database to text files, then connect to the second database for
processing.
> >
> > Thanks,
…[3 more quoted lines elided]…
> 'basic' queries. The following is OO but see if it ties in similar to what
you
> are doing. The only change I have made is to substitute SQLTATE for
SQL:CODE :-
>
> $set sql (ansi92entry) sql (dbman=ODBC)
…[162 more quoted lines elided]…
> I *think* you only need the cursor where you are going to FETCH more than
one,
> so I''ve included methods for 'one' and 'cursor'. BTW if you are *new* to
DB, it
> might pay to try using the ESQ: Assistant to ensure 100% syntax :-
>
…[58 more quoted lines elided]…
> And for more than "one" -  Note that ESQL Assistant generates the next
cursor
> number that you need for each query, plus each of my queries invokes
"DBConnect"
> to check I'm accessing the correct database:-
>
…[72 more quoted lines elided]…
>
```

#### ↳ Re: Accessing multiple databases in Net Express V3.0

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-07-01T11:07:16+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d216290_4@Usenet.com>`
- **References:** `<yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com>`

```
Bill,

I don't use NetExpress, but you might check out the use of the SQL "USE"
statement. You have "CONNECT" covered OK.

Pete.

Bill Gentry <billgentry2@comcast.net> wrote in message
news:yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com...
> Hello all,
>
> I've been working up an app that needs to process 2 MS Access databases
> concurrently.   It will connect to both DB's via ODBC "connect"
statements,
> issue SQL's against both of them, then disconnect.
>
> First off, I'm not sure if this will even work or not, at least with the
IDE
> I'm using.  I've been into MicroFocus' Knowledge base, and All I saw was
one
> program sample where you could setup multiple connections, but you had to
> "swap" the connections, similar to closing one file before opening
another.
>
> In any case, here's a couple of code snippets.  I'm not posting the whole
…[54 more quoted lines elided]…
> The last SQL statement is giving me an SQLCODE of -0000019514 "cursor is
not
> prepared".   The netexpress documentation lists the "AS" as valid code in
> the declare cursor, if you have a "db_name" in use, as I do in this
program.
> It's not listed as valid code for the "OPEN" or the "FETCH" commands.
>
> Anyway, if anyone has had any luck with this, I'd appreciate the input.
I'm
> going to keep working on it and I'll post the "fix" if I ever find one.
I
> may have to re-think the app, though:  Dump the contents of the first
> database to text files, then connect to the second database for
processing.
>
> Thanks,
> Bill
>
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Accessing multiple databases in Net Express V3.0

- **From:** "Bill Gentry" <billgentry2@comcast.net>
- **Date:** 2002-07-03T17:22:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tpGU8.19714$vq.745285@bin6.nnrp.aus1.giganews.com>`
- **References:** `<yOKT8.471307$Gs.33516106@bin5.nnrp.aus1.giganews.com> <3d216290_4@Usenet.com>`

```
Hi Pete,

Thanks, I'll take a look at that.

Also, I dug a little deeper into my "problem":  The MS Access driver was
returning an SQLSTATE of "IM001" which means "Driver does not suppor this
function".   I figure that this means either 1) MS Acess does not support
this AT ALL, or 2) (hopefully) MS Access does not support this the way I'm
doing it ( maybe the USE statement will do what I need )   Again, I'll keep
the NG posted.

Thx,
Bill


"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3d216290_4@Usenet.com...
> Bill,
>
…[18 more quoted lines elided]…
> > program sample where you could setup multiple connections, but you had
to
> > "swap" the connections, similar to closing one file before opening
> another.
> >
> > In any case, here's a couple of code snippets.  I'm not posting the
whole
> > program for the sake of brevity... if anyone wants to see the whole
thing,
> > I'll post it.
> >
…[31 more quoted lines elided]…
> > Then, later in the program, I attempt to fetch some data from the
database
> > I'd declared as "KCONN"
> >
…[19 more quoted lines elided]…
> > prepared".   The netexpress documentation lists the "AS" as valid code
in
> > the declare cursor, if you have a "db_name" in use, as I do in this
> program.
…[21 more quoted lines elided]…
>                 http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
