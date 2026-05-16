[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating tables

_11 messages · 4 participants · 2004-10_

---

### Creating tables

- **From:** "Dionisis Vrionis" <diovr@dksoft.gr>
- **Date:** 2004-10-12T11:56:51+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```
I Have a database named test.mdb without tables.
How can i create a table in a database from netcobol.
```

#### ↳ Re: Creating tables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-12T18:49:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c46om0tkmbivehcgdhr7olf558gd4ksss8@4ax.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```
On Tue, 12 Oct 2004 11:56:51 +0300, "Dionisis Vrionis"
<diovr@dksoft.gr> wrote:

>I Have a database named test.mdb without tables.
>How can i create a table in a database from netcobol.
>

From MS Acess help

CREATE [TEMPORARY] TABLE table (field1 type [(size)] [NOT NULL] [WITH
COMPRESSION | WITH COMP] [index1] [, field2 type [(size)] [NOT NULL]
[index2] [, ...]] [, CONSTRAINT multifieldindex [, ...]])

The CREATE TABLE statement has these parts:

Part Description 
table The name of the table to be created. 
field1, field2 The name of field or fields to be created in the new
table. You must create at least one field. 
type The data type of field in the new table. 
size The field size in characters (Text and Binary fields only). 
index1, index2 A CONSTRAINT clause defining a single-field index.  
multifieldindex A CONSTRAINT clause defining a multiple-field index.  


You just issue the correct table statement on a SQL connection and it
will create the table.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Creating tables

- **From:** "Peter E.C Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-10-16T02:28:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1097846885.h+JxAdvYkvHzg0qy7ADzVw@teranews>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr> <c46om0tkmbivehcgdhr7olf558gd4ksss8@4ax.com>`

```
Frederico,

As far as I can tell, it won't do that if you are not using ODBC. (The ODBC
connection decides what SQL is supported...)

See Richard's post in this thread.  I believe he is right, but if you have
actually done it, then your straight flush beats our four aces <G>.

My post outlines a way it can be done using DAO and COM/OLE.

Regards,

Pete.


"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:c46om0tkmbivehcgdhr7olf558gd4ksss8@4ax.com...
> On Tue, 12 Oct 2004 11:56:51 +0300, "Dionisis Vrionis"
> <diovr@dksoft.gr> wrote:
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Creating tables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-15T18:23:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jk10n09v3rmvje7dpopjenj8f3tmq828qd@4ax.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr> <c46om0tkmbivehcgdhr7olf558gd4ksss8@4ax.com> <1097846885.h+JxAdvYkvHzg0qy7ADzVw@teranews>`

```
On Sat, 16 Oct 2004 02:28:01 +1300, "Peter E.C Dashwood"
<dashwood@enternet.co.nz> wrote:
Top posting corrected.

>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
>news:c46om0tkmbivehcgdhr7olf558gd4ksss8@4ax.com...
…[37 more quoted lines elided]…
>connection decides what SQL is supported...)

You are correct. using the precompiler supplied with NetCobol it is
impossible to do it using ESQL.

I have done it in ESQL using the Oracle Precompiler.
And it is also possible to do it using ADO (or DAO as you have) with
either ODBC or OLEDB.



>
>See Richard's post in this thread.  I believe he is right, but if you have
…[8 more quoted lines elided]…
>



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Creating tables

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-10-12T20:26:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0410121926.74478c59@posting.google.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```
"Dionisis Vrionis" <diovr@dksoft.gr> wrote 

> I Have a database named test.mdb without tables.
> How can i create a table in a database from netcobol.

I will assume that your problem is not so much "create a table" but is
"from netcobol".

Fujitsu NetCobol SQL is implemented to not include such things as
CREATE TABLE.  ie it allows all the SQL that is in the manual, and
only that SQL. You probably should create the table externally using,
for example, a command line client, or a graphics administration
client.
```

#### ↳ Re: Creating tables

- **From:** "Peter E.C Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-10-14T01:20:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```

"Dionisis Vrionis" <diovr@dksoft.gr> wrote in message
news:ckg68k$1km9$1@ulysses.noc.ntua.gr...
> I Have a database named test.mdb without tables.
> How can i create a table in a database from netcobol.
>
What Richard wrote is true, however, there is more than one way to skin a
cat, and tables can be created by more than just embedded SQL.

With a little imagination, some knowledge if the DB object model, and an OO
COBOL compiler (like NetCOBOL), you can certainly create tables "on the
fly".

Here's how....

 ENVIRONMENT     DIVISION.
 REPOSITORY.
     CLASS COM-EXCEPTION AS "*COM-EXCEPTION"
     CLASS COM AS "*COM".
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01  DAO-connection pic x(8192) value "DAO.DBEngine.36".  *> Make sure this
is the COM ProgID of the

*> the version of ACCESS or DAO you have on

*> your system. Search the registry for DAO...

*> (Data Access Objects)
 01  OBJ-DBEngine              OBJECT REFERENCE COM.
 01  OBJ-DAOCONNECTION  OBJECT REFERENCE COM.
 01  OBJ-Database              OBJECT REFERENCE COM.
 01  NAME-DB PIC X(whatever) value "Name of the DB you want to access (can
be ODBC DSN)".
* [You might want to pass this through Linkage...]

 01  create-stuff pic x( whatever) value "CREATE TABLE tablename (field,
field, ...) CONSTRAINTS etc".

========================  Examples of valid CREATE entry  (valid for SQL
Server and ACCESS 2003)=============
You could set up  "create-stuff" to contain the following...

CREATE TABLE jobs
(
   job_id  smallint
      IDENTITY(1,1)
      PRIMARY KEY CLUSTERED,
   job_desc        varchar(50)     NOT NULL
      DEFAULT 'New Position - title not formalized yet',
   min_lvl tinyint NOT NULL
      CHECK (min_lvl >= 10),
   max_lvl tinyint NOT NULL
      CHECK (max_lvl <= 250)
)

It will create the table as described.

If you want a temporary table try...

CREATE TABLE  #tempTable (tempField int... etc)

Here's the offical story on temporary tables...

Temporary Tables
You can create local and global temporary tables. Local temporary tables are
visible only in the current session; global temporary tables are visible to
all sessions.

Prefix local temporary table names with single number sign (#table_name),
and prefix global temporary table names with a double number sign
(##table_name).

SQL statements reference the temporary table using the value specified for
table_name in the CREATE TABLE statement:

CREATE TABLE #MyTempTable (cola INT PRIMARY KEY)  (this would be one EXECUTE
statement)
INSERT INTO #MyTempTable VALUES (1) (This would be another EXECUTE
statement)
============================================================================
=================================

 01  Temp-text pic x(50).
 01  connection-flag pic x value '1'.
     88 no-connection value zero.
     88 connected     value '1'.
 PROCEDURE       DIVISION. [using databaseName, TableName perhaps...]
 DECLARATIVES.
 ERR SECTION.
     USE AFTER EXCEPTION OLE-EXCEPTION
     move spaces to DB-path
     set no-connection to TRUE
     .
 END DECLARATIVES.
 main section.
     set connected to TRUE
     perform a-section
     .
 return-to-caller.
     exit program.
*==============================================================
 a-section section.
 a000.
*
* Establish COM Object references to the specified
* ACCESS Database using DAO.
*
     invoke COM "CREATE-OBJECT"
                using DAO-connection
          returning OBJ-DBEngine
     end-invoke

     invoke OBJ-DBEngine "OpenDatabase"
                 using NAME-DB
          returning OBJ-Database
     end-invoke
*
* Check we got to the DB OK...
     if no-connection
         yada-yada-yada...

* Now you can use the EXECUTE method of the Database to create your new
table...

       invoke OBJ-Database "Execute"
                  using create-stuff
       end-invoke
....
a999.
    exit.

The above is not definitive, but it has been put together from currently
working code. Hopefully there's enough here to get you going.

Pete.
```

##### ↳ ↳ Re: Creating tables

- **From:** "Dionisis Vrionis" <diovr@dksoft.gr>
- **Date:** 2004-10-15T19:20:48+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckotcq$130t$1@ulysses.noc.ntua.gr>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr> <1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews>`

```
Your sample it works fine.
Thanks all (specially you Peter) for help.

"Peter E.C Dashwood" <dashwood@enternet.co.nz> wrote in message
news:1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews...
>
> "Dionisis Vrionis" <diovr@dksoft.gr> wrote in message
…[7 more quoted lines elided]…
> With a little imagination, some knowledge if the DB object model, and an
OO
> COBOL compiler (like NetCOBOL), you can certainly create tables "on the
> fly".
…[9 more quoted lines elided]…
>  01  DAO-connection pic x(8192) value "DAO.DBEngine.36".  *> Make sure
this
> is the COM ProgID of the
>
…[41 more quoted lines elided]…
> You can create local and global temporary tables. Local temporary tables
are
> visible only in the current session; global temporary tables are visible
to
> all sessions.
>
…[7 more quoted lines elided]…
> CREATE TABLE #MyTempTable (cola INT PRIMARY KEY)  (this would be one
EXECUTE
> statement)
> INSERT INTO #MyTempTable VALUES (1) (This would be another EXECUTE
> statement)
>
============================================================================
> =================================
>
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Creating tables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-16T01:01:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6p0n0h8fpa6j5c2h7r627bkalof1cbf36@4ax.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr> <1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews> <ckotcq$130t$1@ulysses.noc.ntua.gr>`

```
On Fri, 15 Oct 2004 19:20:48 +0300, "Dionisis Vrionis"
<diovr@dksoft.gr> wrote:

>Your sample it works fine.
>Thanks all (specially you Peter) for help.
Though this sample works fine I would advise you to try and adapt it
to use ADO instead as it is better.


>
>"Peter E.C Dashwood" <dashwood@enternet.co.nz> wrote in message
…[146 more quoted lines elided]…
>



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Creating tables

- **From:** "Peter E.C Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-10-16T15:07:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1097892454.EXtmP+zr+2Rt/9plGPuDjQ@teranews>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr> <1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews> <ckotcq$130t$1@ulysses.noc.ntua.gr>`

```

"Dionisis Vrionis" <diovr@dksoft.gr> wrote in message
news:ckotcq$130t$1@ulysses.noc.ntua.gr...
> Your sample it works fine.
> Thanks all (specially you Peter) for help.
>

Excellent! Glad it was of use.

Frederico has recommended you to replace the solution with an ADO one.

I neither agree nor disagree with this.

Here's some quick thoughts on the matter...

1. ADO is ActiveX Data Objects and is MicroSoft's stated "direction" for
database access. It is component based and is more flexible and intended to
handle more data sources than even ODBC.  Three years ago they were telling
everybody to go this way and they still are.

2. DAO is "Data Access Objects". It utilises a model which is based on
direct interface to the database engine and it is being implemented in open
software, outside MicroSoft. (of course, MS have their own DAO also). The
ADO model is simpler and less hierachic because it is component based,  but
I have found the DAO model to be excellent when using ACCESS.

3. A quick web search reveals current posts on DAO so, despite
recommendations from MS, it is still being used. You should do a few
searches of your own on these two technologies and make your own mind up. I
think they both have merit and I use them both.

Fujitsu PowerCOBOL provides an ADO based control for connection to databases
and it works pretty well. (I don't use it, although I tried it once. I have
a slightly different philosophy about databases and believe they should be
used solely as repositories (no database dependent SQL and I'm still making
my mind up about stored procedures), I also believe in separation layers
(multi-tier model), so I like ODBC and COBOL or Java.

Around two years ago, I was managing the Legacy systems for a major UK
utility and most of my team were ex-COMPAQ guys who were born and bred into
Client/Server. (All of the Legacy was on Client/Server,  so it is not only
mainframes that are being replaced by "new technology"; in this case the
Siebel Solution (�30,000,000 over three years...)). Many of our team used
SQL Server with stored procedures and triggers, and they explained to me
their reasons for doing so. I explained why I don't, and we had some really
interesting discussions. On balance, I think they were right and I probably
would use stored procedures now, but ONLY if I was totally persuaded there
was not going to be a change of DB technology or vendor any time soon...

4. It would be a fairly simple change to "convert" the DAO solution to ADO
(I'm surprised Frederico didn't provide some code, rather than just a
personal opinion); You can use ADO at different levels of the model,
directly.

5. One always needs to think carefully before replacing a working solution
with one that is based on intangibles ("It's more efficient" (How much and
does it matter?), "we're phasing out the old way" (When?), "Everybody's
doing it this way..." (Sure, Doc's favourite: "Brooklyn Bridge"). There may
be benefits with an ADO approach but how quantifiable are they? This is
something you need to decide for yourself.

Regards,

Pete.

(Top post, nothing more below.)

> "Peter E.C Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:1097670067.BM6bnx51U2GOAH7FlW/9Hg@teranews...
…[6 more quoted lines elided]…
> > What Richard wrote is true, however, there is more than one way to skin
a
> > cat, and tables can be created by more than just embedded SQL.
> >
…[25 more quoted lines elided]…
> >  01  NAME-DB PIC X(whatever) value "Name of the DB you want to access
(can
> > be ODBC DSN)".
> > * [You might want to pass this through Linkage...]
…[36 more quoted lines elided]…
> > Prefix local temporary table names with single number sign
(#table_name),
> > and prefix global temporary table names with a double number sign
> > (##table_name).
> >
> > SQL statements reference the temporary table using the value specified
for
> > table_name in the CREATE TABLE statement:
> >
…[6 more quoted lines elided]…
>
============================================================================
> > =================================
> >
…[58 more quoted lines elided]…
>
```

#### ↳ Re: Creating tables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-16T17:46:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qtj2n0hfvfvi3gp0hjf7rop696v4555ssj@4ax.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```
On Tue, 12 Oct 2004 11:56:51 +0300, "Dionisis Vrionis"
<diovr@dksoft.gr> wrote:

>I Have a database named test.mdb without tables.
>How can i create a table in a database from netcobol.
>

And to be absolutelly clear on how to use ADO

fully working code.
 IDENTIFICATION DIVISION.
 PROGRAM-ID. "ADODEMO".
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 REPOSITORY.
     CLASS COM-EXCEPTION AS "*COM-EXCEPTION"
     CLASS COM AS "*COM".
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01  VARIABLES.
     05  ADO-CONNECTION-TYPE   PIC X(8192) VALUE "ADODB.Connection".  
     05  ADO-RECORDSET-TYPE   PIC X(8192) VALUE "ADODB.Recordset".  
     05  ADO-COMMAND-TYPE   PIC X(8192) VALUE "ADODB.Command".  
     05  OBJ-CONNECTION  OBJECT REFERENCE COM .
     05  OBJ-RECORDSET   OBJECT REFERENCE COM.
     05  OBJ-COMMAND   OBJECT REFERENCE COM.

     05  OBJ-FIELD   OBJECT REFERENCE COM OCCURS 10.
     05  OBJ-FIELDS   OBJECT REFERENCE COM.
     05  OBJ-FIELDS-COUNT  PIC S9(9) COMP-5 VALUE 0.
     05  RECORDCOUNT  PIC S9(9) COMP-5 VALUE 0.
     05  NUMBER-FIELD PIC S9(9)V9(9)  VALUE 0.
     05  NUMBER-FIELD-EDT PIC -(10).9(9).
     05  ALPHA-FIELD PIC X(200).
     05  RETURN-ERROR   PIC 9(9) COMP-5.
     05  WLOCK PIC S9(9) COMP-5 VALUE 1.
     05  WCURSOR PIC S9(9) COMP-5 VALUE 1.
     05  WOPTION PIC S9(9) COMP-5 VALUE -1.
     05  W-INDEX            PIC 99.
     05  W-INDEX-1          PIC 99.
     05  EOF PIC S9(9) COMP-5.
     05  BOF PIC S9(9) COMP-5.

     05  FIELD-NAME                 PIC X(25).
     05  FIELD-TYPE                 PIC 9(9) OCCURS 10.

     05  ADO-STRING.
         10              PIC X(30) VALUE
*       123456789    0523456789    05234567890
      "DSN=LOCALSERVER;UID=FREDERICO;".
         10              PIC X(30) VALUE
      "PWD=FREDE1;DATABASE=FACTUCLI;".
     05  ADO-CONNECT-STRING REDEFINES ADO-STRING PIC X(60).
     05  ADO-SQL-STRING PIC X(500).

 PROCEDURE DIVISION.
 MAIN SECTION.
     *> CREATE MAIN OBJECTS. 
     INVOKE COM "CREATE-OBJECT" 
            USING ADO-CONNECTION-TYPE
            RETURNING OBJ-CONNECTION.
     INVOKE COM "CREATE-OBJECT" 
            USING ADO-RECORDSET-TYPE
            RETURNING OBJ-RECORDSET.
     *> DEFINE AND OPEN CONNECTION
     INVOKE OBJ-CONNECTION "SET-CONNECTIONSTRING"
            USING ADO-CONNECT-STRING 
            RETURNING RETURN-ERROR.

     INVOKE OBJ-CONNECTION "OPEN" 
            RETURNING RETURN-ERROR.
     *> DEFINE SQL AND EXECUTE IT
     STRING "SELECT * FROM PAISES ORDER BY PAIS;" 
            LOW-VALUE DELIMITED BY SIZE
       INTO ADO-SQL-STRING.
     INVOKE OBJ-RECORDSET "OPEN" 
            USING ADO-SQL-STRING
                  OBJ-CONNECTION 
                  WLOCK 
                  WCURSOR 
            RETURNING RETURN-ERROR.
     *> ASSUMING THE SQL WORKED WE WILL HAVE A FIELDS COLLECTION. GET
IT'S OBJECT AND THE COUNT OF ITEMS.

     INVOKE OBJ-RECORDSET "GET-FIELDS" 
            RETURNING OBJ-FIELDS.
     INVOKE OBJ-FIELDS "GET-COUNT" 
            RETURNING OBJ-FIELDS-COUNT.
     *> NOW LOAD EACH FIELD OBJECT AND IT'S TYPE.
     *> ON REAL LIFE WE CAN BYPASS THE TYPE AS WE WILL NORMALLY NOW
THAT. EXCEPTIONS ARE ON DYNAMIC SQL SOLUTIONS.
     PERFORM VARYING W-INDEX
             FROM 0 BY 1 
             UNTIL W-INDEX > (OBJ-FIELDS-COUNT - 1)
        INVOKE OBJ-FIELDS "GET-ITEM" USING W-INDEX RETURNING
OBJ-FIELD(W-INDEX + 1)
        MOVE SPACES TO FIELD-NAME
        MOVE ZEROS TO FIELD-TYPE(W-INDEX + 1)
        INVOKE OBJ-FIELD(W-INDEX + 1) "GET-NAME"
               RETURNING FIELD-NAME
        INVOKE OBJ-FIELD(W-INDEX + 1) "GET-TYPE" 
               RETURNING FIELD-TYPE(W-INDEX + 1)
        DISPLAY "FIELD N. " W-INDEX " NAME=" FIELD-NAME " FIELD TYPE="
FIELD-TYPE (W-INDEX + 1)
     END-PERFORM.

     INVOKE OBJ-RECORDSET "GET-RECORDCOUNT" RETURNING RECORDCOUNT.
    *> AS THE RECORD COUNT PROPERTY ONLY WORKS WITH CERTAIN TYPES OF
CURSORS WE RETRIEVE
    *> THE EOF/BOF VALUES ALSO TO DETERMINE IF WE HAVE RECORDS.
     INVOKE OBJ-RECORDSET "GET-EOF" RETURNING EOF.
     INVOKE OBJ-RECORDSET "GET-BOF" RETURNING BOF.


    *> NOW LOAD THE RECORDS UNTIL END OF FILE. DISPLAY ON THIS CASE.
     IF RECORDCOUNT NOT < 0
     OR (NOT BOF = 0 AND EOF = 0)
        PERFORM UNTIL EOF = 1
            INVOKE OBJ-RECORDSET "GET-EOF" RETURNING EOF
            IF EOF = 0
               PERFORM VARYING W-INDEX
                       FROM 1 BY 1
                       UNTIL W-INDEX > OBJ-FIELDS-COUNT
                     EVALUATE FIELD-TYPE(W-INDEX)
                     WHEN 131 *> Numeric
                             INVOKE OBJ-FIELD(W-INDEX) "GET-VALUE"
                                 RETURNING NUMBER-FIELD
                          MOVE NUMBER-FIELD TO NUMBER-FIELD-EDT
                          DISPLAY "FIELD " W-INDEX " VALUE = "
NUMBER-FIELD-EDT
                     WHEN 129 *> CHAR
                          INVOKE OBJ-FIELD(W-INDEX) "GET-VALUE"
                                 RETURNING ALPHA-FIELD
                          DISPLAY "FIELD " W-INDEX " VALUE = "
ALPHA-FIELD (1:50)
                     END-EVALUATE
               END-PERFORM
               INVOKE OBJ-RECORDSET "MOVENEXT" RETURNING RETURN-ERROR
            END-IF
        END-PERFORM
     END-IF.
     





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Creating tables

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-17T00:38:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67c3n0d7sbvgjgt43kscb5kipcec0lquf7@4ax.com>`
- **References:** `<ckg68k$1km9$1@ulysses.noc.ntua.gr>`

```
On Tue, 12 Oct 2004 11:56:51 +0300, "Dionisis Vrionis"
<diovr@dksoft.gr> wrote:

>I Have a database named test.mdb without tables.
>How can i create a table in a database from netcobol.
>
And now an example in ADO to create tables
Uses the command and the connection object to create two tables.


 IDENTIFICATION DIVISION.
 PROGRAM-ID. "ADODEMO1".
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 REPOSITORY.
     CLASS COM-EXCEPTION AS "*COM-EXCEPTION"
     CLASS COM AS "*COM".
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01  VARIABLES.
     05  ADO-CONNECTION-TYPE   PIC X(8192) VALUE "ADODB.Connection".  
     05  ADO-COMMAND-TYPE   PIC X(8192) VALUE "ADODB.COMMAND".  
     05  OBJ-CONNECTION  OBJECT REFERENCE COM .
     05  OBJ-COMMAND   OBJECT REFERENCE COM.

     05  RETURN-ERROR   PIC 9(9) COMP-5.
     05  ZERO-RECORDS   PIC 9(9) COMP-5.
     05  ADO-SQL-CMDTEXT   PIC 9(9) COMP-5 VALUE 1.
     05  ADO-STRING.
         10              PIC X(30) VALUE
      "DSN=LOCALSERVER;UID=FREDERICO;".
         10              PIC X(30) VALUE
      "PWD=FREDE1;DATABASE=FACTUCLI;".
     05  ADO-CONNECT-STRING REDEFINES ADO-STRING PIC X(60).
     05  ADO-SQL-STRING PIC X(500).

 PROCEDURE DIVISION.
 MAIN SECTION.
     *> CREATE MAIN OBJECTS. 
     INVOKE COM "CREATE-OBJECT" 
            USING ADO-CONNECTION-TYPE
            RETURNING OBJ-CONNECTION.
     INVOKE COM "CREATE-OBJECT" 
            USING ADO-COMMAND-TYPE
            RETURNING OBJ-COMMAND.
     *> DEFINE AND OPEN CONNECTION
     INVOKE OBJ-CONNECTION "SET-CONNECTIONSTRING"
            USING ADO-CONNECT-STRING 
            RETURNING RETURN-ERROR.

     INVOKE OBJ-CONNECTION "OPEN"
            RETURNING RETURN-ERROR.

     *> Create a table using the connection object
     STRING "CREATE TABLE DEMO2 (DEMO CHAR)" 
            LOW-VALUE DELIMITED BY SIZE
       INTO ADO-SQL-STRING.
     INVOKE OBJ-CONNECTION "EXECUTE"
            USING ADO-SQL-STRING
                  ZERO-RECORDS

     *> Create a table using the command object
     STRING "CREATE TABLE DEMO3 (DEMO CHAR)" 
            LOW-VALUE DELIMITED BY SIZE
       INTO ADO-SQL-STRING.
     INVOKE OBJ-COMMAND "SET-ACTIVECONNECTION" 
            USING OBJ-CONNECTION
     INVOKE OBJ-COMMAND "SET-COMMANDTYPE"
            USING ADO-SQL-CMDTEXT
     INVOKE OBJ-COMMAND "SET-COMMANDTEXT"
            USING ADO-SQL-STRING
     INVOKE OBJ-COMMAND "EXECUTE"
            USING ZERO-RECORDS.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
