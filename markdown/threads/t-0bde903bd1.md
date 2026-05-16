[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Conversion of data & associated logic from ISAM to RDB

_64 messages · 11 participants · 2007-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Conversion of data & associated logic from ISAM to RDB

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-03T11:55:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com>`

```
We are using Micro Focus Net Express 4.0 and Microsoft SQL Server
2000.  The concepts/examples we are seeking however can be more
generic, i.e., not necessarily shown within COBOL source code per se.

Right now we have two realized problems, both of which appear to stem
from our mutual and still-thriving ignorance......

The first problem is as follows:  We are having surprising difficulty
in our attempts to find working examples of SQL-related code sequences
for handling low-volume user-entered updates vs large-volume batch
updates.  The working examples we need can be represented as pseudo-
code and/or actual code - we don't really care which - we just need
something representative to work from.  (See fictitious example
enclosed)

The second problem involves how to handle record locking issues among
multiple users.  The lead analyst wants us to code logic that requires
maintenance of a date-time field in every record - this date-time
stamp would then be used for determining the availability of a given
record such that unilaterally-applied changes are not given an
opportunity to sneak in while another user has said record in a state
of flux.  I'll spare you the further gory details of this terrifying
scheme for now, but suffice it to say we do not like it because it
seems that we would end up re-inventing the wheel, given that the rdb
is supposed to have various locking detection/tools already built into
it.

Here is a simple/fictitious representation of the type of code
sequence samples that we are looking for...

Typical LOW-VOLUME USER UPDATE module:
1.	Open rdb
2.	EXEC SQL WHENEVER SQLERROR DO sql_error;
3.	Accept record key from user
4.	Read matching record  w/ shared lock (presume REC-FOUND for this
example)
5.	Display fields on screen
6.	Accept field updates from user
7.	Edit field updates (presume EDIT-PASSED for this example)
8.	BEGIN TRANSACTION
9.	Read record from table with exclusive lock
10.	Move new field values to table
11.	Rewrite table record
12.	COMMIT
13.	END TRANSACTION
14.	Close rdb


Typical HIGH-VOLUME BATCH UPDATE module:
1.	Open rdb
2.	~?~?~
3.	~?~?~
4.	~?~?~


Perhaps there is a site somewhere that includes sql-related coding
examples?  I appreciate in advance any input that anyone may have
about how we should be approaching this data conversion effort.

Sincerely,
Dave Miner
```

#### ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-04T01:13:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<euuu4h$8a9$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com>`

```
In article <1175626528.510733.311750@n59g2000hsh.googlegroups.com>,
DaveM <renfrew76@xemaps.com> wrote:
>We are using Micro Focus Net Express 4.0 and Microsoft SQL Server
>2000.  The concepts/examples we are seeking however can be more
…[8 more quoted lines elided]…
>updates.

That's interesting... where have you looked for these, so that others here 
might not duplicate your efforts?

>The working examples we need can be represented as pseudo-
>code and/or actual code - we don't really care which - we just need
>something representative to work from.  (See fictitious example
>enclosed)

I'll do that.

>
>The second problem involves how to handle record locking issues among
…[5 more quoted lines elided]…
>of flux.

How interesting... this is a time-honored technique that I first heard 
described by someone who worked on one of the original airline reservation 
systems.

Things have changed a bit since then... your lead analyst seems to want to 
apply techniques for indexed files to a database; this has, in my 
experience, usually resulted in disappointment for the system's users and 
those who maintain the code.

>I'll spare you the further gory details of this terrifying
>scheme for now, but suffice it to say we do not like it because it
>seems that we would end up re-inventing the wheel, given that the rdb
>is supposed to have various locking detection/tools already built into
>it.

I am not sure about Microsoft SQL Server 2000 but I know that Oracle has 
some pretty good internals to avoid deadlocks; I suggest that someone dig 
into the appropriate manual and present the necessary pages to the lead 
analyst.

>
>Here is a simple/fictitious representation of the type of code
…[17 more quoted lines elided]…
>14.	Close rdb

Hmmmmm... is there anyone on this particular job who knows the difference 
between a 'record' and a 'row'?

>
>
…[4 more quoted lines elided]…
>4.	~?~?~

2. Do a bunch of stuff.
3. Close rdb
4. Get promoted before this comes back to fasten its teeth in one's 
gluteals.

>
>
>Perhaps there is a site somewhere that includes sql-related coding
>examples?  I appreciate in advance any input that anyone may have
>about how we should be approaching this data conversion effort.

My suggestion is that you find people who know what they are doing and pay 
them a lot of money to do it while you train the on-site staff to deal 
with the new technology.

DD
```

##### ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-04T12:00:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<euuu4h$8a9$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com>`

```
On Apr 3, 9:13 pm, docdw...@panix.com () wrote:
> In article <1175626528.510733.311...@n59g2000hsh.googlegroups.com>,
>
…[16 more quoted lines elided]…
>

If I'd kept a log of every single place I've been to while seeking
this information and then posted it here, as you seem to be kindly
requesting now, I am afraid that my inquiry would have become entirely
too enormous for most folks to bother with.  Lets just say that I have
looked everywhere, with the obvious exception of those places where
the answers I am looking for are actually being kept.

The gist of what I am currently seeking should exist mainly within the
minds of many of those who frequent this newsgroup, hence my inquiry.
Forgive me for not making it clearer, but I am not asking anyone to go
out on a google tour on my behalf; I am only asking for information
relevant to people's own real-world experiences such that we might
gain a better perspective about the options we are faced with.

> >The working examples we need can be represented as pseudo-
> >code and/or actual code - we don't really care which - we
…[22 more quoted lines elided]…
> for the system's users and those who maintain the code.


The handling of record (or I guess I should now say ROW) locking
conflicts, esp among multiple users, are supposed to be handled
primarily by functions that are internal to the rdb itself.
Regardless of how time-honored a given technique may be, it seems to
me that by going to the trouble of coding our own locking handler we
will only end up sidestepping what the rdb is designed to take care of
for us, and all in exchange for a manual (and inferior) version of
that capability.

This is rather like harnessing a team of mules up to a tractor to plow
the field.  Sure, its possible, but we'd be foolishly wasting the very
reasons that we'd paid extra money to buy the damn tractor in the
first place.


> >I'll spare you the further gory details of this terrifying
> >scheme for now, but suffice it to say we do not like it because
…[8 more quoted lines elided]…
>

Deadlocks per se are not of particular concern to us, as these are
supposed to be automatically handled by the rdb.  What we are trying
to learn about are the protocols of dealing with wait-locks, time-
outs, and prevention of unilateral changes etc.

>
>
…[23 more quoted lines elided]…
> the difference between a 'record' and a 'row'?

Yes, we do.  Pseudo-code, at least within our organization, is written
for the purpose of communicating ideas and logic flow.  Given that you
figured out that my usage of 'record' should have instead been
expressed as 'row', then this pseudo-code has apparently accomplished
its purpose.   :)

In any case, point taken.

>
> >Typical HIGH-VOLUME BATCH UPDATE module:
…[21 more quoted lines elided]…
> DD

Your final suggestion is excellent but I am afraid it is not
practicable because I do not control any of the purse strings.  We
have no choice but to work with this analyst, along with a rather
tight-fisted management team who is unwilling to spring for the cost
of formal training.  Complaints I have aplenty, of course, but that
won't resolve anything.  The only realistic and proactive plan we have
at this point is to continue doing what we are doing, namely, to
research usenet groups and knowledge bases, to ask questions, read
manuals, ask more questions, setup & run tests, analyze results,
borrow or buy additional manuals, and humbly beg somebody in the real
world to lead us to some working examples.

Thank you for your help.

Dave Miner
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "tleaders@gmail.com" <tleaders@gmail.com>
- **Date:** 2007-04-04T13:05:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1175717128.965681.301480@l77g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com>`

```
On Apr 4, 3:00 pm, "DaveM" <renfre...@xemaps.com> wrote:
> On Apr 3, 9:13 pm, docdw...@panix.com () wrote:
>
…[182 more quoted lines elided]…
> - Show quoted text -


Dave

First let me say that I have not used Net Express since I got a copy
of the beta release of 4.0 some years ago.  I have been using since
Fujitsu then. So the examples below are in Cobol.Net. The 1st program
is written in Cobol.net and the second is in VB.Net. Both programs do
roughly the same thing, they dump a sql table to a text file.


Depending on what your requirements are for the High Volume Batch
Update I would recommend that you read Microsoft's book-on-line (BOL)
the sections relating to Bulk Copy, Bulk Insert, DTS,  and odbc.

Good Luck
Tom



IDENTIFICATION DIVISION.
 PROGRAM-ID. Program1 AS "ADO_SQL_Generator.Program1".
 ENVIRONMENT DIVISION.

 CONFIGURATION SECTION.
 REPOSITORY.
     CLASS SQLCONNECTION AS "System.Data.SqlClient.SqlConnection"
     CLASS SQLDATAREADER AS "System.Data.SqlClient.SqlDataReader"
     CLASS SQLCOMMAND    AS "System.Data.SqlClient.SqlCommand"
     CLASS SQLDATETIME2  AS "System.Data.SqlTypes.SqlDateTime"
     CLASS SQLDATETIME   AS "System.DateTime".

 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
     SELECT SQL-OUT-FILE
     ASSIGN TO "c:\sqlinsrt.txt"
     ORGANIZATION IS LINE SEQUENTIAL.

 DATA DIVISION.
 FILE SECTION.
 FD  SQL-OUT-FILE
     RECORD IS VARYING IN SIZE FROM 10 TO 4000
     DEPENDING ON BSUB.
 01  SQL-OUT-REC.
     05 SOR-CHAR  PIC x
         OCCURS 10 TO 4000 TIMES DEPENDING ON BSUB.

 WORKING-STORAGE SECTION.
 01 CONNECTIONOBJ OBJECT REFERENCE SQLCONNECTION.
 01 DATAREADEROBJ OBJECT REFERENCE SQLDATAREADER.
 01 SQLCOMMANDOBJ OBJECT REFERENCE SQLCOMMAND.
 01 DATAREADEROBJ2 OBJECT REFERENCE SQLDATAREADER.
 01 SQLCOMMANDOBJ2 OBJECT REFERENCE SQLCOMMAND.
 01 MY-BOOLEAN   PIC 1 USAGE BIT VALUE B"1".
 01 MY-BOOLEAN2  PIC 1 USAGE BIT VALUE B"0".
 01 MY-STRING PIC X(455) VALUE SPACES.
*              111111111122222222223333333333444444444455555555556
*     123456789012345678901234567890123456789012345678901234567890
 01  SQL-COLUMNS.
     05 FILLER PIC X(41) VALUE
     "select A.NAME, B.NAME, C.NAME, B.LENGTH, ".
     05 FILLER PIC X(42) VALUE
     "B.PREC,B.SCALE,B.ISCOMPUTED, B.ISNULLABLE ".
     05 FILLER PIC X(18) VALUE
     "FROM SYSOBJECTS A ".
     05 FILLER PIC X(39) VALUE
     "INNER JOIN SYSCOLUMNS B ON A.ID = B.ID ".
     05 FILLER PIC X(43) VALUE
     "INNER JOIN SYSTYPES C ON B.XTYPE = C.XTYPE ".
     05 FILLER PIC X(20) VALUE
     "WHERE A.XTYPE = 'U' ".
     05 FILLER PIC X(24) VALUE
     "AND B.AUTOVAL IS NULL ".
     05 FILLER PIC X(14) VALUE
     "and a.nAME = '".
     05 SC-TABLE-NAME PIC X(30) VALUE spaces.
     05 FILLER PIC X(29) VALUE
     "' order bY A.NAME, B.COLID ".

 01  STV-SUB       PIC 9(4) VALUE 0.
 01  SYS-TABLE-VALUES.
     05 STV-OCC   OCCURS 1000 TIMES.
         10 STV-TABLE     PIC X(20).
         10 STV-COLUMN    PIC X(50).
         10 STV-DATA-TYPE PIC X(20).
         10 STV-LENGTH    PIC S9(4) USAGE COMP-5.
         10 STV-PREC      PIC S9(4) USAGE COMP-5.
         10 STV-SCALE     PIC S9(9) USAGE COMP-5.
         10 STV-ISCOMP    PIC S9(9) USAGE COMP-5.
         10 STV-ISNULL    PIC S9(9) USAGE COMP-5.

 01   BUILD-NEW-SELECT PIC X(5000) VALUE SPACES.
 01   BUILD-OUT-LINE   PIC X(5000) VALUE SPACES.
 01   CHAR-DATA        PIC X(5000) VALUE SPACES.
 01   ASUB             PIC 9(4) VALUE 0.
 01   BSUB             PIC 9(4) VALUE 0.
 01   XSUB             PIC 9(4) VALUE 0.
 01   SAVEB            PIC 9(4) VALUE 0.

 01  INT8-DATA          USAGE BINARY-CHAR UNSIGNED.
 01  INT8-FORMAT       PIC ----9.
 01  INT16-DATA        PIC S9(4) USAGE COMP-5.
 01  INT16-FORMAT      PIC -----9.
 01  INT32-DATA        PIC S9(9) USAGE COMP-5.
 01  INT32-FORMAT      PIC ---------9.
 01  DATE-DATA     OBJECT REFERENCE SQLDATETIME.
 01  DATE-DATA2    OBJECT REFERENCE SQLDATETIME2.
 01  DATE-FORMAT       PIC X(23).

 01  DEC0-DATA         PIC S9(18)      USAGE COMP-5.
 01  DEC0-FORMAT       PIC ------------------9.
 01  DEC1-DATA         PIC S9(17)V9(1) USAGE COMP-5.
 01  DEC1-FORMAT       PIC ------------------.9.
 01  DEC2-DATA         PIC S9(16)V9(2) USAGE COMP-5.
 01  DEC2-FORMAT       PIC -----------------.99.
 01  DEC3-DATA         PIC S9(15)V9(3) USAGE COMP-5.
 01  DEC3-FORMAT       PIC ----------------.999.
 01  DEC4-DATA         PIC S9(14)V9(4) USAGE COMP-5.
 01  DEC4-FORMAT       PIC ---------------.9999.
 01  DEC5-DATA         PIC S9(13)V9(5) USAGE COMP-5.
 01  DEC5-FORMAT       PIC --------------.99999.
 01  DEC6-DATA         PIC S9(12)V9(6) USAGE COMP-5.
 01  DEC6-FORMAT       PIC -------------.999999.

 01  LINE-CTR          PIC 99 VALUE 1.
 01  WRITE-COUNT       PIC 9(8)  VALUE 0.
 01  WRITE-COUNTD      PIC ZZ,ZZZ,ZZ9.
 01  WRITE-COUNT2      PIC 9(5)  VALUE 0.
 01  MY-COUNT          PIC 9(5)  VALUE 0.
 01  JUNK PIC X VALUE SPACE.
 01  SERVER-NAME   PIC X(30) VALUE SPACES.
 01  DATABASE-NAME PIC X(30) VALUE SPACES.
 PROCEDURE DIVISION.
 GET-SERVER-CONNECTION.
     DISPLAY "Enter Server Name or (LOCAL)".
     ACCEPT SERVER-NAME FROM CONSOLE.
     MOVE "SERVER=" TO BUILD-OUT-LINE
     MOVE 1 TO BSUB.
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES ADD 1 TO BSUB END-
PERFORM.
     MOVE SERVER-NAME TO BUILD-OUT-LINE(BSUB:)
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES ADD 1 TO BSUB END-
PERFORM.
     MOVE ";TRUSTED_CONNECTION=YES;DATABASE=" TO BUILD-OUT-LINE(BSUB:)
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES ADD 1 TO BSUB END-
PERFORM.
     DISPLAY "Enter DataBase Name ie 001".
     ACCEPT DATABASE-NAME FROM CONSOLE.
     MOVE DATABASE-NAME TO BUILD-OUT-LINE(BSUB:)
     INVOKE SQLCONNECTION "NEW" USING BUILD-OUT-LINE RETURNING
CONNECTIONOBJ.
     INVOKE CONNECTIONOBJ "Open".

     DISPLAY "Enter Table Name".
     ACCEPT SC-TABLE-NAME FROM CONSOLE.

     MOVE SQL-COLUMNS TO MY-STRING.
     INVOKE SQLCOMMAND "NEW" USING MY-STRING CONNECTIONOBJ
                             RETURNING
SQLCOMMANDOBJ.
     INVOKE SQLCOMMANDOBJ "ExecuteReader" RETURNING DATAREADEROBJ.
     MOVE B"1" TO MY-BOOLEAN.
     MOVE 0 TO MY-COUNT.

     MOVE 1 TO STV-SUB.
     MOVE SPACES TO SYS-TABLE-VALUES.

     INVOKE DATAREADEROBJ "Read" RETURNING MY-BOOLEAN.
     PERFORM WITH TEST BEFORE UNTIL MY-BOOLEAN NOT = B"1"
         INVOKE DATAREADEROBJ "GetString" USING 0 RETURNING STV-
TABLE(STV-SUB)
         INVOKE DATAREADEROBJ "GetString" USING 1 RETURNING STV-
COLUMN(STV-SUB)
         INVOKE DATAREADEROBJ "GetString" USING 2 RETURNING STV-DATA-
TYPE(STV-SUB)
         INVOKE DATAREADEROBJ "GetInt16" USING 3 RETURNING  STV-
LENGTH(STV-SUB)
         INVOKE DATAREADEROBJ "GetInt16"  USING 4 RETURNING STV-
PREC(STV-SUB)
         INVOKE DATAREADEROBJ "IsDBNull"  USING 5 RETURNING MY-
BOOLEAN2
         MOVE 0 TO STV-SCALE(STV-SUB)
         IF MY-BOOLEAN2 = B"0"
         INVOKE DATAREADEROBJ "GetInt32"  USING 5 RETURNING STV-
SCALE(STV-SUB)
         END-IF
         INVOKE DATAREADEROBJ "GetInt32"  USING 6 RETURNING STV-
ISCOMP(STV-SUB)
         INVOKE DATAREADEROBJ "GetInt32"  USING 7 RETURNING STV-
ISNULL(STV-SUB)
         ADD 1 TO STV-SUB
         ADD 1 TO MY-COUNT
         INVOKE DATAREADEROBJ "Read" RETURNING MY-BOOLEAN
     END-PERFORM.


     MOVE "Select " TO BUILD-NEW-SELECT.

     MOVE 1 TO STV-SUB.
     MOVE 8 TO ASUB.
 BUILD-SQL-LOOP.
     IF STV-COLUMN(STV-SUB) NOT = SPACES
       IF STV-SUB NOT = 1
          MOVE "," TO BUILD-NEW-SELECT(ASUB:)
          ADD 1 TO ASUB
       end-if
       MOVE STV-COLUMN(STV-SUB) TO BUILD-NEW-SELECT(ASUB:)
       PERFORM UNTIL BUILD-NEW-SELECT(ASUB:) = spaces
          ADD 1 TO ASUB
       END-PERFORM.
     ADD 1 TO STV-SUB.
     IF STV-SUB < 1000
         GO TO BUILD-SQL-LOOP.

     ADD 1 TO ASUB.
     MOVE 1 TO BSUB.
     MOVE "INSERT INTO" TO BUILD-OUT-LINE
     MOVE SC-TABLE-NAME TO BUILD-OUT-LINE(13:)
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
          ADD 1 TO BSUB
     END-PERFORM.
     MOVE "(" TO BUILD-OUT-LINE(BSUB:)
     ADD 1 TO BSUB.
     MOVE BUILD-NEW-SELECT(8:) TO BUILD-OUT-LINE(BSUB:)
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
          ADD 1 TO BSUB
     END-PERFORM.
     MOVE ") VALUES (" TO BUILD-OUT-LINE(BSUB:)
     PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
          ADD 1 TO BSUB
     END-PERFORM.
     MOVE BSUB TO SAVEB.
     MOVE "from" TO BUILD-NEW-SELECT(ASUB:)
     ADD 5 TO ASUB.
     MOVE SC-TABLE-NAME TO BUILD-NEW-SELECT(ASUB:)


     OPEN OUTPUT SQL-OUT-FILE.

     INVOKE DATAREADEROBJ "Close".
     INVOKE SQLCOMMAND "NEW" USING BUILD-NEW-SELECT CONNECTIONOBJ
                             RETURNING SQLCOMMANDOBJ2.
     INVOKE SQLCOMMANDOBJ2 "ExecuteReader" RETURNING DATAREADEROBJ2.
     MOVE B"1" TO MY-BOOLEAN.
     MOVE 0 TO MY-COUNT.
     INVOKE DATAREADEROBJ2 "Read" RETURNING MY-BOOLEAN.
     PERFORM WITH TEST BEFORE UNTIL MY-BOOLEAN NOT = B"1"
         PERFORM PROCESS-DATA-RECORD
         INVOKE DATAREADEROBJ2 "Read" RETURNING MY-BOOLEAN
     END-PERFORM.
     IF LINE-CTR NOT = 1
         MOVE 1 TO LINE-CTR
         MOVE "go" TO SQL-OUT-REC
         WRITE SQL-OUT-REC.
     INVOKE CONNECTIONOBJ "Close".
     DISPLAY "Hit Enter to Exit".
     ACCEPT JUNK FROM CONSOLE.
     CLOSE SQL-OUT-FILE.
     EXIT PROGRAM.


 PROCESS-DATA-RECORD.
     MOVE 1 TO STV-SUB
     MOVE SAVEB TO BSUB
     MOVE SPACES TO BUILD-OUT-LINE(BSUB:)
     PERFORM READ-VARIABLE-DATA
        UNTIL (STV-COLUMN(STV-SUB) = SPACES).

     MOVE ")" TO BUILD-OUT-LINE(BSUB:)
     MOVE BUILD-OUT-LINE TO SQL-OUT-REC.
     WRITE SQL-OUT-REC.
     ADD 1 TO LINE-CTR.
     IF LINE-CTR > 10
         MOVE 1 TO line-ctr
         MOVE "go" TO SQL-OUT-REC
         WRITE SQL-OUT-REC.
     ADD 1 TO WRITE-COUNT.
     ADD 1 TO WRITE-COUNT2.
     IF WRITE-COUNT2 > 199
         MOVE WRITE-COUNT TO WRITE-COUNTD
         DISPLAY "Write Record " WRITE-COUNTD
         MOVE 0 TO WRITE-COUNT2.

 READ-VARIABLE-DATA.
     MOVE B"0" TO MY-BOOLEAN2.
     COMPUTE ASUB = STV-SUB - 1
     MOVE 1 TO XSUB.
     INVOKE DATAREADEROBJ2 "IsDBNull"  USING ASUB RETURNING MY-
BOOLEAN2
     IF STV-COLUMN(STV-SUB) NOT = SPACES
       IF STV-SUB NOT = 1
         MOVE "," TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB.
     IF MY-BOOLEAN2 = B"1"
         MOVE "NULL" TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
     ELSE
       IF STV-DATA-TYPE(STV-SUB) = "char"
         INVOKE DATAREADEROBJ2 "GetString" USING ASUB  RETURNING CHAR-
DATA
         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB
         MOVE CHAR-DATA TO BUILD-OUT-LINE(BSUB:)
         IF CHAR-DATA = SPACES
             ADD 1 TO BSUB
         END-IF
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB
       ELSE
       IF STV-DATA-TYPE(STV-SUB) = "tinyint"
         MOVE 0 TO INT8-DATA
         INVOKE DATAREADEROBJ2 "GetByte" USING ASUB RETURNING INT8-
DATA
         MOVE INT8-DATA TO INT8-FORMAT
         MOVE INT8-FORMAT TO CHAR-DATA
         INSPECT CHAR-DATA TALLYING XSUB FOR LEADING " "
         MOVE CHAR-DATA(XSUB:) TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
       ELSE
       IF STV-DATA-TYPE(STV-SUB) = "smallint"
         MOVE 0 TO INT16-DATA
         INVOKE DATAREADEROBJ2 "GetInt16" USING ASUB RETURNING INT16-
DATA
         MOVE INT16-DATA TO INT16-FORMAT
         MOVE INT16-FORMAT TO CHAR-DATA
         INSPECT CHAR-DATA TALLYING XSUB FOR LEADING " "
         MOVE CHAR-DATA(XSUB:) TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
       ELSE
       IF STV-DATA-TYPE(STV-SUB) = "int"
         INVOKE DATAREADEROBJ2 "GetInt32" USING ASUB RETURNING INT32-
DATA
         MOVE INT32-DATA TO INT32-FORMAT
         MOVE INT32-FORMAT TO CHAR-DATA
         INSPECT CHAR-DATA TALLYING XSUB FOR LEADING " "
         MOVE CHAR-DATA(XSUB:) TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
       ELSE
       IF STV-DATA-TYPE(STV-SUB) = "datetime"
         INVOKE DATAREADEROBJ2 "GetDateTime" USING ASUB RETURNING DATE-
DATA
         INVOKE DATE-DATA "ToString" RETURNING DATE-FORMAT

         MOVE DATE-FORMAT TO CHAR-DATA
         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB
         INSPECT CHAR-DATA TALLYING XSUB FOR LEADING " "
         MOVE CHAR-DATA(XSUB:) TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB
       ELSE
       IF STV-DATA-TYPE(STV-SUB) = "decimal"
         IF STV-SCALE(STV-SUB) = 0
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC0-DATA
           MOVE DEC0-DATA TO DEC0-FORMAT
           MOVE DEC0-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 1
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC1-DATA
           MOVE DEC1-DATA TO DEC1-FORMAT
           MOVE DEC1-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 2
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC2-DATA
           MOVE DEC2-DATA TO DEC2-FORMAT
           MOVE DEC2-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 3
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC3-DATA
           MOVE DEC3-DATA TO DEC3-FORMAT
           MOVE DEC3-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 4
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC4-DATA
           MOVE DEC4-DATA TO DEC4-FORMAT
           MOVE DEC4-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 5
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC5-DATA
           MOVE DEC5-DATA TO DEC5-FORMAT
           MOVE DEC5-FORMAT TO CHAR-DATA
         END-IF
         IF STV-SCALE(STV-SUB) = 6
           INVOKE DATAREADEROBJ2 "GetDecimal" USING ASUB RETURNING
DEC6-DATA
           MOVE DEC6-DATA TO DEC6-FORMAT
           MOVE DEC6-FORMAT TO CHAR-DATA
         END-IF
         INSPECT CHAR-DATA TALLYING XSUB FOR LEADING " "
         MOVE CHAR-DATA(XSUB:) TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
       ELSE

         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB
         MOVE "data-type-not-processed" TO BUILD-OUT-LINE(BSUB:)
         PERFORM UNTIL BUILD-OUT-LINE(BSUB:) = SPACES
            ADD 1 TO BSUB
         END-PERFORM
         MOVE "'" TO BUILD-OUT-LINE(BSUB:)
         ADD 1 TO BSUB.
     ADD 1 TO STV-SUB.

 END PROGRAM PROGRAM1.






'= TABLE_EXPORT - This program will accept a SQL table name and export
the
'= information to a text file.

Module CreateInserts

    Sub Main()
        Dim oFile As System.IO.File
        Dim oWrite As System.IO.StreamWriter
        Dim sSql As String
        Dim sSqlNew As String
        Dim sSqlFrom As String
        Dim sSqlInsert As String
        Dim MyData As SqlClient.SqlDataReader
        Dim bReadFlag As Boolean
        Dim iCnt As Integer
        Dim iCntMax As Integer
        Dim sFileName(500) As String
        Dim sFieldName(500) As String
        Dim scharName(500) As String
        Dim iLength(500) As Integer
        Dim iPerc(500) As Integer
        Dim iScale(500) As Integer
        Dim iIsComputed(500) As Integer
        Dim iIsNullable(500) As Integer

        Console.WriteLine("Enter File Name")
        Dim InputName As String = Console.ReadLine
        '= The output file will be stored in "c:\labelprocess\" with
the prefix
        '= EXPORT and the suffix SQL.
        '=
        Dim OutputName As String = "c:\labelprocess\EXPORT "
        OutputName = OutputName + InputName + ".SQL"
        oWrite = oFile.CreateText(OutputName)


        sSql = "select A.NAME, B.NAME, C.NAME, B.LENGTH,
B.PREC,B.SCALE,B.AUTOVAL, B.ISNULLABLE " & _
                " FROM SYSOBJECTS A  " & _
                "  INNER JOIN SYSCOLUMNS B ON A.ID = B.ID  " & _
                "  INNER JOIN SYSTYPES C ON B.XTYPE = C.XTYPE  " & _
                "WHERE A.XTYPE = 'U' " & _
                "and a.nAME = '" + InputName + "'   " & _
                "and c.name <> 'sysname' " & _
                "order bY A.NAME, B.COLID "

        MyData = File_System.GetDataReader(sSql)
        iCnt = 0
        '= First the CREATE TABLE statements are written.
        If MyData.HasRows Then
            sSqlNew = "IF not exists (SELECT * FROM dbo.sysobjects
where id = object_id(N'[dbo].[" + InputName + "]') and
OBJECTPROPERTY(id, N'IsUserTable') = 1) "
            oWrite.WriteLine(sSqlNew)
            sSqlNew = "  CREATE TABLE [dbo].[" + InputName + "] ( "
            oWrite.WriteLine(sSqlNew)
            sSqlNew = " "
            bReadFlag = MyData.Read()
            Do While bReadFlag

                If MyData.IsDBNull(1) Then sSqlNew = " " Else sSqlNew
= sSqlNew + MyData.GetString(1) + "  " 'sFieldName(iCnt) =
MyData.GetString(1)
                If MyData.IsDBNull(2) Then sSqlNew = " " Else sSqlNew
= sSqlNew + MyData.GetString(2) + "  " 'scharName(iCnt) =
MyData.GetString(2)
                If MyData.GetString(2).ToLower = "char" _
                Or MyData.GetString(2).ToLower = "varchar" _
                Or MyData.GetString(2).ToLower = "nchar" _
                Or MyData.GetString(2).ToLower = "nvarchar" _
                Or MyData.GetString(2).ToLower = "text" _
                Or MyData.GetString(2).ToLower = "ntext" Then
                    If MyData.IsDBNull(3) Then sSqlNew = sSqlNew +
"( )" Else sSqlNew = sSqlNew + "(" + MyData.GetInt16(3).ToString + ")"
' iLength(iCnt) = MyData.GetInt16(3)
                ElseIf MyData.GetString(2).ToLower = "decimal" Or
MyData.GetString(2).ToLower = "numeric" Then
                    sSqlNew = sSqlNew + "("
                    If MyData.IsDBNull(4) Then sSqlNew = sSqlNew + "0"
Else sSqlNew = sSqlNew + MyData.GetInt16(4).ToString
                    sSqlNew = sSqlNew + ","
                    If MyData.IsDBNull(5) Then sSqlNew = sSqlNew + "0"
Else sSqlNew = sSqlNew + MyData.GetInt32(5).ToString
                    sSqlNew = sSqlNew + ") "
                End If
                If Not MyData.IsDBNull(6) Then sSqlNew = sSqlNew + "
Identity (1,1) "
                If Not MyData.IsDBNull(7) Then
                    If MyData.GetInt32(7) = 0 Then sSqlNew = sSqlNew +
" not null"
                Else
                    sSqlNew = sSqlNew + " null"
                End If
                oWrite.WriteLine(sSqlNew)
                sSqlNew = ","
                bReadFlag = MyData.Read()
            Loop
            oWrite.WriteLine(")")
            oWrite.WriteLine(" ")
            oWrite.WriteLine("GO")
            oWrite.WriteLine(" ")
            oWrite.WriteLine(" ")

        Else
            MsgBox("Invalid Table Name Entered - Program Ending")
            oWrite.WriteLine("Invalid Table Name Entered - Program
Ending")
            GoTo endsub
        End If
        MyData.Close()


        sSql = "select A.NAME, B.NAME, C.NAME, B.LENGTH,
B.PREC,B.SCALE,B.ISCOMPUTED, B.ISNULLABLE " & _
        " FROM SYSOBJECTS A  " & _
        "  INNER JOIN SYSCOLUMNS B ON A.ID = B.ID  " & _
        "  INNER JOIN SYSTYPES C ON B.XTYPE = C.XTYPE  " & _
        "WHERE A.XTYPE = 'U' AND B.AUTOVAL IS NULL    " & _
        "and a.nAME = '" + InputName + "'   " & _
        "and c.name <> 'sysname' " & _
        "order bY A.NAME, B.COLID "


        MyData = File_System.GetDataReader(sSql)
        iCnt = 0
        '= Then each data record from the table is read and the data
is used to create
        '= insert statements. The statements are in the form
        '= insert into <table name> (field names) values (data
values).
        sSqlNew = "Select "
        sSqlInsert = "insert into "
        If MyData.HasRows Then
            bReadFlag = MyData.Read()
            Do While bReadFlag And iCnt <= 500
                If MyData.IsDBNull(0) Then sFileName(iCnt) = " " Else
sFileName(iCnt) = MyData.GetString(0)
                If MyData.IsDBNull(1) Then sFieldName(iCnt) = " " Else
sFieldName(iCnt) = MyData.GetString(1)
                If MyData.IsDBNull(2) Then scharName(iCnt) = " " Else
scharName(iCnt) = MyData.GetString(2)
                If MyData.IsDBNull(3) Then iLength(iCnt) = 0 Else
iLength(iCnt) = MyData.GetInt16(3)
                If MyData.IsDBNull(4) Then iPerc(iCnt) = 0 Else
iPerc(iCnt) = MyData.GetInt16(4)
                If MyData.IsDBNull(5) Then iScale(iCnt) = 0 Else
iScale(iCnt) = MyData.GetInt32(5)
                If MyData.IsDBNull(6) Then iIsComputed(iCnt) = 0 Else
iIsComputed(iCnt) = MyData.GetInt32(6)
                If MyData.IsDBNull(7) Then iIsNullable(iCnt) = 0 Else
iIsNullable(iCnt) = MyData.GetInt32(7)
                If iCnt <> 0 Then
                    sSqlNew = sSqlNew + ", "
                    sSqlInsert = sSqlInsert + ", "
                Else
                    sSqlInsert = "Insert Into " + sFileName(iCnt) +
"("
                End If
                sSqlFrom = sFileName(iCnt)
                sSqlNew = sSqlNew + sFieldName(iCnt)
                sSqlInsert = sSqlInsert + sFieldName(iCnt)
                iCnt = iCnt + 1

                bReadFlag = MyData.Read()
            Loop
        Else
            MsgBox("Invalid Table Name Entered - Program Ending")
            oWrite.WriteLine("Invalid Table Name Entered - Program
Ending")
            GoTo endsub
        End If
        MyData.Close()


        sSqlNew = sSqlNew + " from " + sSqlFrom
        sSqlInsert = sSqlInsert + ") values ("


        MyData = File_System.GetDataReader(sSqlNew)
        iCntMax = iCnt - 1
        iCnt = 0
        sSqlNew = sSqlInsert

        If MyData.HasRows Then
            bReadFlag = MyData.Read()
            Do While bReadFlag
                sSqlNew = sSqlInsert
                For iCnt = 0 To iCntMax
                    If iCnt <> 0 Then
                        sSqlNew = sSqlNew + ", "
                    End If
                    If MyData.IsDBNull(iCnt) Then
                        If iIsNullable(iCnt) = 1 Then
                            sSqlNew = sSqlNew + "null"
                        Else
                            If MyData.GetDataTypeName(iCnt).ToLower =
"char" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"varchar" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"nchar" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"nvarchar" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"text" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"ntext" Then
                                sSqlNew = sSqlNew + " "
                            Else
                                sSqlNew = sSqlNew + "0"
                            End If
                        End If
                    Else
                        If MyData.GetDataTypeName(iCnt).ToLower =
"char" _
                        Or MyData.GetDataTypeName(iCnt).ToLower =
"varchar" _
                        Or MyData.GetDataTypeName(iCnt).ToLower =
"nchar" _
                        Or MyData.GetDataTypeName(iCnt).ToLower =
"nvarchar" _
                        Or MyData.GetDataTypeName(iCnt).ToLower =
"text" _
                        Or MyData.GetDataTypeName(iCnt).ToLower =
"ntext" Then
                            sSqlNew = sSqlNew + "'" +
MyData.GetString(iCnt).ToString.TrimEnd(" ")
                            If
MyData.GetString(iCnt).ToString.TrimEnd(" ") = "" Then
                                sSqlNew = sSqlNew + " '"
                            Else
                                sSqlNew = sSqlNew + "'"
                            End If
                        ElseIf MyData.GetDataTypeName(iCnt).ToLower =
"tinyint" Then
                            sSqlNew = sSqlNew +
MyData.GetByte(iCnt).ToString
                        ElseIf MyData.GetDataTypeName(iCnt).ToLower =
"smallint" Then
                            sSqlNew = sSqlNew +
MyData.GetInt16(iCnt).ToString
                        ElseIf MyData.GetDataTypeName(iCnt).ToLower =
"int" Then
                            sSqlNew = sSqlNew +
MyData.GetInt32(iCnt).ToString
                        ElseIf MyData.GetDataTypeName(iCnt).ToLower =
"datetime" Then
                            sSqlNew = sSqlNew + "'" +
MyData.GetDateTime(iCnt).ToString + "'"
                        ElseIf MyData.GetDataTypeName(iCnt).ToLower =
"decimal" _
                            Or MyData.GetDataTypeName(iCnt).ToLower =
"numeric" Then
                            sSqlNew = sSqlNew +
MyData.GetDecimal(iCnt).ToString
                        Else
                            sSqlNew = sSqlNew + " "
                        End If
                    End If
                Next iCnt
                sSqlNew = sSqlNew + ")"
                oWrite.WriteLine(sSqlNew)
                bReadFlag = MyData.Read()
            Loop
        End If
        MyData.Close()
        oWrite.WriteLine(" ")
        oWrite.WriteLine("GO")
        oWrite.WriteLine(" ")


        sSql = "select C.TEXT from sysobjects A " & _
            " INNER JOIN SYSOBJECTS B ON A.ID=B.PARENT_OBJ " & _
            " INNER JOIN SYSCOMMENTS C ON B.ID=C.ID" & _
            " where A.NAME = '" + InputName + "'"
        MyData = File_System.GetDataReader(sSql)
        If MyData.HasRows Then
            bReadFlag = MyData.Read()
            Do While bReadFlag
                sSqlNew = " "
                If MyData.IsDBNull(0) Then sSqlNew = " " Else sSqlNew
= MyData.GetString(0)
                oWrite.WriteLine(sSqlNew)
                oWrite.WriteLine(" ")
                oWrite.WriteLine("GO")
                oWrite.WriteLine(" ")
                bReadFlag = MyData.Read()
            Loop
        End If
        MyData.Close()

        '= Last the SQL statements to create the index keys are
created

        sSql = " select o.name,i.name, kn.name, " & _
                "  case " & _
                "    when i.indid = 1 then 'Clustered' " & _
                "    else ' ' " & _
                "  end, " & _
                " k.keyno " & _
                " from sysindexkeys k " & _
                "    inner join sysindexes I ON k.id = i.id and
k.indid=i.indid  " & _
                "    INNER JOIN syscolumns kn ON I.id = kn.id and
k.colid=kn.colid  " & _
                "    INNER JOIN sysobjects O ON I.id = o.id  " & _
                " where " & _
                "       o.name = '" + InputName + "'  and " & _
                "       I.indid > 0 and I.indid < 255 and  " & _
                "       (INDEXPROPERTY(I.id, i.name, N'IsStatistics')
<> 1) and " & _
                "       (INDEXPROPERTY(I.id, i.name,
N'IsAutoStatistics') <> 1) and " & _
                "       (INDEXPROPERTY(I.id, i.name,
N'IsHypothetical') <> 1) " & _
                "      and o.type = 'U' " & _
                " order  by i.name, k.keyno, k.colid "
        MyData = File_System.GetDataReader(sSql)
        Dim sLastKey As String = " "
        Dim sLastFileName As String = " "
        Dim sLastKeyName As String = " "
        Dim sLastFieldName As String = " "
        Dim sLastClustered As String = " "
        If MyData.HasRows Then
            bReadFlag = MyData.Read()
            Do While bReadFlag
                sSqlNew = " "

                If MyData.IsDBNull(0) Then sLastFileName = " " Else
sLastFileName = MyData.GetString(0)
                If MyData.IsDBNull(1) Then sLastKeyName = " " Else
sLastKeyName = MyData.GetString(1)
                If MyData.IsDBNull(2) Then sLastFieldName = " " Else
sLastFieldName = MyData.GetString(2)
                If MyData.IsDBNull(3) Then sLastClustered = " " Else
sLastClustered = MyData.GetString(3)
                If sLastKey = sLastKeyName Then
                    sSqlNew = ",[" + sLastFieldName + "]"
                    oWrite.WriteLine(sSqlNew)
                Else
                    If sLastKey <> " " Then
                        oWrite.WriteLine(")")
                        oWrite.WriteLine("GO")
                        oWrite.WriteLine(" ")
                    End If
                    sSqlNew = " CREATE UNIQUE " + sLastClustered + "
INDEX " + sLastKeyName + " ON " + sLastFileName
                    oWrite.WriteLine(sSqlNew)
                    oWrite.WriteLine("(")
                    sSqlNew = "[" + sLastFieldName + "]"
                    oWrite.WriteLine(sSqlNew)
                End If
                sLastKey = sLastKeyName
                bReadFlag = MyData.Read()
            Loop
            oWrite.WriteLine(")")
            oWrite.WriteLine("GO")
            oWrite.WriteLine(" ")
        End If
        MyData.Close()


EndSub:
        oWrite.Close()


    End Sub
    '=
End Module
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 4)_

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-10T09:44:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176223479.428972.39830@l77g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1175717128.965681.301480@l77g2000hsb.googlegroups.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com>`

```
Jimmy,

Thank you for your help.  Between yours and other responses I am now
aware of more specific terms that we should be using e.g.,
'embedded'), along with other fundamentally important pieces of
information.

Google/web search for 'sql-examples' found 43K hits, but most of these
were about structuring the sql query itself, as opposed to the kinds
of cobol-to-sql-database examples that I was looking for.  However, by
narrowing it down further with the added criteria "embedded" and
"cobol" it gave us a much more manageable/relevant 456 hits.  The
first page alone gives us more than enough useful links to keep us
constructively busy for a long while!

NE's Database Access online book was/is quite useful, but, of course,
did not contain the real-world examples we were looking for.  With
enlightenments since gleaned via this and other threads, I am happy to
say the this book is even MORE useful now because I have gained a
significantly better sense of  what many of the pieces really mean and
how they are applied.  (I still have a long way to go, obviously, but
it sure feels better to know I'm at least holding the manual right-
side up, so to speak.)

ESQL Assistant looks very useful, and I most certainly will also take
up your suggestion of signing up for MF forum per SQL.

According to one of the other writers I now owe you a consultant's
fee, along with a signed affadavit proving that I have already
achieved expert status in any given subject before having the audacity
to ask anyone else questions about it.   ;o)

Again, and in all seriousness, I thank you for your help.

Gratefully,
Dave Miner
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-10T17:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evgfql$it6$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com>`

```
In article <1176223479.428972.39830@l77g2000hsb.googlegroups.com>,
DaveM <renfrew76@xemaps.com> wrote:

[snip]

>According to one of the other writers I now owe you a consultant's
>fee, along with a signed affadavit proving that I have already
>achieved expert status in any given subject before having the audacity
>to ask anyone else questions about it.   ;o)

Mr Miner, the concept of 'owe' can carry with it both legal and moral 
obligations.  To the best of my knowledge there's no contractual agreement 
for payment between you and anyone offering responses here so - it might 
be concluded - that you owe twice as much as you've already been asked to 
pay.

On the other hand... you received information which, by your own 
admission, has saved you time; it can be argued that you owe a portion of 
your savings to one who assisted you in achieving them... and if 
Franklin's Equivalence ('Time is Money') is valid then you owe someone 
cash.

As for 'expert status'... that was never asked.  Just think of what you 
might have gotten were you to have respected the subject matter 
sufficiently to learn some basic terminology before trotting your requests 
out before the world, hat in your hand and spinach on your teeth, asking 
for folks to Do Their Jobs For You For Free.

It turns out that you got... something, sure.  How you evaluate whether 
what you got is of value or will send you and your team rushing pell-mell 
down a dead end is another matter... wouldn't want to find yourself on the 
carpet in front of the CFO saying 'But this... guy on the UseNet told me 
it'd work, how was *I* to know he was fulla hooey... I'm not Technical, 
you know!  To Julia... do it to Julia, not me!', would you?

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-11T00:16:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sNVSh.51648$6m4.42486@pd7urf1no>`
- **In-Reply-To:** `<1176223479.428972.39830@l77g2000hsb.googlegroups.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com>`

```
DaveM wrote:
> Jimmy,
> 
…[4 more quoted lines elided]…
> 
<SNIP>

Don't know how I dreamed up 58K hits - just re-did it and came up with
the same 43K hits that you did :-)

Doesn't give exactly what you were immediately after but check M/F site
for examples/samples - there are three 'general' SQL routines. Plus if
you get into your N/E sub-folders there are also some demos of 'general'
SQL solutions. Once into the M/F Forum you can search previous messages
with "Database", "ODBC" and "SQL" etc. You can't respond to the next -
but you can also look at old ARCHIVED messages. Like M/S, M/F under Net
Express also has a KnowledgeBase. But the whole bunch above tend to be
generalized.

Pete Dashwood's solution and ESQL Assistant. Pete reads your COBOL file
records and generates equivalent DB rows into a table. ESQL Assistant -
*YOU* design the DB Table and determine what type of SQL fields/columns
(Int, Char etc.), you want. Naturally the latter approach means you have
to get au fait with the particular DB package, (how numerics are stored)
- so it could take you a week or more to convert, depending upon the
number of tables you are going to generate.

There might be a nice solution using both Pete's package and ESQL
Assistant. Pete will read a whole bunch of COBOL files in mere minutes
and generate your DB Table formats. Now using ESQL Assistant, (the major
thing being you can generate your SQL statements knowing they will be
correct), when you test on a particular table the ESQL package will ask
you if you want to generate a copyfile - three parts :-

DB Table format
DB Table NULL columns
COBOL - a typical COBOL record

So Pete provides the initial definition of your DB Table and from that
ESQL using Pete's DB Table, generates the copyfile above which you can
test your individual queries with.

Obviously you are picking up stuff as you do more reading, but for a
quickie comparison, and don't take this as gospel :-

COBOL FILES             SQL
-----------             -------------

Open/Close          Connect/Disconnect (Note you connect/disconnect
                     to a specific Database which may contain 50 Tables,
                     (equivalent of 50 COBOL files, or perhaps 30 Files,
                     split into 50 tables)

Read using PrimeKey Select Distinct

Read Next           Select using Cursor - This uses a number for the
                     cursor. ESQL Assistant automatically generates the
                     next number, so there's no confusion between
                     different queries

Rewrite             Update

Write               Insert

Delete              Delete

The use of the various SQL "Verbs" becomes clearer if you use ESQL
Assistant to generate queries.

I think what you balked at in your original message was "How to..." do
equivalent of COBOL Write and Rewrite.

PROCEDURAL using an ISAM (my own style - so you adapt to your way)
------------------------

Display Screen-Record/GUI Dialog
Accept PrimeKey

if Blank - Quit

else set RecordNotFound, RecordNotChanged to true
          Read Record using PrimeKey (SQL - SELECT DISTINCT )
End-if

if RecordFound
    perform DISPLAY-RECORD
    perform ACCEPT-CHANGES
    for Changed-fields set RecordChanged to true

else (RecordNotFound)
      set RecordChanged to true
      perform ACCEPT-NEW-RECORD, (other than the PrimeKey)
      then perform ACCEPT-CHANGES (if you want to make corrections)
End-if

if  RecordChanged
     perform VALIDATION-CHECKS
     (errors - go back to perform ACCEPT-CHANGES)
End-if

if   ValidationOK (this is also a Level 88)

      if  RecordFound
          REWRITE COBOL-RECORD

      else WRITE COBOL-RECORD

End-if

PROCEDURAL using SQL
--------------------

The only real difference between this and COBOL file above is
substituting :-

SELECT DISTINCT       = READ FILE using PrimeKey
SQL-UPDATE            = REWRITE COBOL-RECORD
SQL-INSERT            = WRITE COBOL-RECORD.

REAL WORLD EXAMPLES
-------------------

I don't know that M/F have anything specific, but you could ask if you 
join the M/F Forum

I did post a message the latter part of last year - but can't locate it; 
e-mail me 'editing' my address above, so that I can confirm a link to 
you and in return I'll post the code I'm referring to. It's OO Classes 
but when looking at methods being invoked think of CALLING another 
program or performing a PARAGRAPH. I'm not recommending *mine* is the 
way to do it, but for a simple file it illustrates the program logic 
flow I illustrated above and gives you the COMPLETE SQL Statements for 
INSERT, UPDATE, CURSOR etc... for a specific table. (I don't mind if you 
call them records or rows :-) ).

If/when you get a paperback, or articles on design from the Web, 
concentrate on the term 'Normalization' so that you have a handle on it.

Jimmy
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-11T15:59:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5834o5F2ecb3nU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:sNVSh.51648$6m4.42486@pd7urf1no...
<snip>>
> Pete Dashwood's solution and ESQL Assistant. Pete reads your COBOL file
> records and generates equivalent DB rows into a table.

Not quite.

ISAM2RDB reads your COBOL source definitions and generates one or more 
TABLES into a designated DATABASE.

A single ISAM file definition COULD generate several tables. Ths is because 
the normalization process removes repeating groups (OCCURS in COBOL) to a 
separate linked table for each group. (One advantage of this is that every 
"table" in your COBOL system now has unlimited rows (no more maintaining 
OCCURS items) and will only take as much space as it actually needs...)

If your ISAM source definition has no OCCURS in it, then you should get a 
single table, with a correctly typed column for each of the fields defined 
in your ISAM definition. (Both groups and elements are defined, to assist 
with data loading and converting existing programs that may reference group 
fields. Unreferenced groups can be removed later.)

Certainly this tool gives you a structure that is useful while you are 
transitioning from ISAM to RDB. However, I would not suggest that this is 
how Relational Databases should be designed and built :-) It is a 
non-relational solution forced into a relational framework and, as such, it 
can never be as good as a Relational solution built from scratch. Sadly few 
of us have the time or funding to restart from scratch when moving to new 
technology, so ISAM2RDB provides a helpful bridge. (It also assists with the 
learning process; for example, you can look at the PICTURE of a given 
element in your COBOL code and see what type of Database definition for the 
corresponding column was generated on the RDB.)


ESQL Assistant -
> *YOU* design the DB Table and determine what type of SQL fields/columns
> (Int, Char etc.), you want. Naturally the latter approach means you have
…[17 more quoted lines elided]…
> test your individual queries with.

Yes, that could be viable. I guess it depends on how many tables are 
involved. If it is just a few, it is probably better to simply use ESQL and 
learn how to define tables. If there are many, it might be useful to use 
ISAM2RDB and pick up some pointers on how to define and normalize tables, in 
passing.
>
>
> If/when you get a paperback, or articles on design from the Web, 
> concentrate on the term 'Normalization' so that you have a handle on it.
>

A very important observation, Jimmy.

I have some stuff on this somewhere... I'll see if I can post it to a web 
server so people can access it.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 7)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-11T06:26:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4c%Sh.53345$6m4.32414@pd7urf1no>`
- **In-Reply-To:** `<5834o5F2ecb3nU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:sNVSh.51648$6m4.42486@pd7urf1no...
…[9 more quoted lines elided]…
> TABLES into a designated DATABASE.

Yes I can see I worded that badly - I really meant as you point out, 
that you generate the format for a Row in a particular table, or 
perhaps, like the reference to OCCURS below - you may generate 
definitions for one or more Tables. (I wonder if that's why the J4 gang 
are so keen on an 800 plus page document - so that you dot all the i's 
and cross all the t's :-) )

> 
> A single ISAM file definition COULD generate several tables. Ths is because 
…[22 more quoted lines elided]…
> 

If he should opt to go with ISAM2RDB to get his Table definitions - and 
it involves OCCURS - please make sure you spell out to him how to use 
the resulting 'inter-linking' tables. Aeons ago you produced similar for 
me - but without explanation how to use the 're-vamped OCCURS', I was
stumped on how to use them !

Just one other thought which you might comment on. When Dave has done 
his setup with tables and definitions, for his real-world COBOL files, I 
can't think of another solution, other than generating CSV files to 
import to the Database ??? (And given any OCCURS - he may have to 
generate more than one CSV from a given COBOL file).

Don't want to insult you Dave - but in case the term is new to you, 
'CSV' = Comma, Separated, Variables where records are written to a Line 
Sequential in the field/column sequence to make up a record being 
imported to a Table row, and usually with the file suffix .txt'.

No more below.

Jimmy

> ESQL Assistant -
> 
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-11T20:26:10+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<583kcsF2fnpmmU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net> <4c%Sh.53345$6m4.32414@pd7urf1no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:4c%Sh.53345$6m4.32414@pd7urf1no...
> Pete Dashwood wrote:
>> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
…[7 more quoted lines elided]…
>
What you got was a pre-release of the product.

You never asked for help.

Since then a number of customers have successfully used this tool. It comes 
with a comprehensive Help file that took almost as long to develop as the 
software did :-)  There are also various ancilliaries and "support" 
functions.

The concept of a secondary table linked to a primary one by a Foreign Key is 
not exactly rocket science. It's actually pretty fundamental to Relational 
Databases.

Obviously, if anyone had trouble using it I would gladly help, but I am no 
longer in the business of converting ISAM files (unless someone pays me a 
market rate to do so...:-)) and I'm not actually trying to sell this 
software...The tool is there and I'm happy to let people use it, but I'm not 
spending hours of time (which I simply don't have, at the moment) explaining 
fundamental concepts and providing free support.

> Just one other thought which you might comment on. When Dave has done his 
> setup with tables and definitions, for his real-world COBOL files, I can't 
…[3 more quoted lines elided]…
>

That would possibly work, but there is no need to do so. An approach I have 
used in the past, successfully, is to write a COBOL program that reads the 
ISAM file sequentially and simply transfers each record obtained, to the RDB 
interface generated by ISAM2RDB. As I mentioned elsewhere, the tool allows 
people with no RDB or SQL knowledge to access the RDB using COBOL records. 
The RDB maintenance module for the table being loaded will simply INSERT all 
the data. There is no need for intermediate processes or export/import; it 
is direct from ISAM to RDB.

The fundamental thing here is that a COBOL program can read ISAM and "write" 
RDB (within the same program). Once you write such a program you have a 
template that enables the loading of all future tables from their equivalent 
ISAM files.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 9)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-12T02:48:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6hTh.61601$aG1.7987@pd7urf3no>`
- **In-Reply-To:** `<583kcsF2fnpmmU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net> <4c%Sh.53345$6m4.32414@pd7urf1no> <583kcsF2fnpmmU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:4c%Sh.53345$6m4.32414@pd7urf1no...
…[16 more quoted lines elided]…
> You never asked for help.

True. But I didn't ask for the table definitions either, which you
returned to me having used, as yet another test set, my COBOL record
copyfiles. I was supposed to know what the Table definitions were ? You 
subsequently developed the Help File below which probably covered this
and other points.

I'm aware you do a good job on Help Files, so Dave shouldn't have a 
problem working his way through it. For me, just academic at this stage, 
as I wont be doing any more productive coding.

> 
> Since then a number of customers have successfully used this tool. It comes 
…[37 more quoted lines elided]…
> 
Again yes to the above. But from my experience, the quick transfer is
not necessarily the best for every situation :-

- Using any new tool, (Screen to GUIs, COBOL files to DBs etc., or as 
you have done, COBOL to Java, then moving on to C#),  should,
I believe, trigger in your mind what advantages the new tools give you.
So as part of the design planning inevitably you think of enhanced ways
of doing things - which can lead to a slightly different, or
considerably different database from the original.

- In my case the necessity of converting 700 data sets (different 
geographical locations), with some 7 files  each, accumulated over a 
twenty-year period, to fit a new design format. That meant in some 
stages of the transfer process the 'old' records just didn't have some 
fields needed in the "new" DB tables. So process in phases, having 
generated error reports where necessary, stop, do some manual editing 
and then move to the later phases.

- The best way of achieving this for me - Line Sequential - using a 
fixed record template. Given a value of 2.345 held in pic 9(03)v9(03) 
comp-3, the template outputs : ",002.345," - the result, all columns are 
aligned making it very easy to swiftly scroll through records, and make 
editing changes where necessary.

- Even with the above approach it is still a fiddly operation, i.e. 
checking the validity of the input data. You could of course take the 
'cleaned up' Line Sequential CSV and "write" to the DB as you suggest. 
However given the format is a CSV - just do the one import.

Different strokes for different folks.

Jimmy
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-12T16:33:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<585r42F2e105nU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net> <4c%Sh.53345$6m4.32414@pd7urf1no> <583kcsF2fnpmmU1@mid.individual.net> <g6hTh.61601$aG1.7987@pd7urf3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:g6hTh.61601$aG1.7987@pd7urf3no...
> Pete Dashwood wrote:
>> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
>> news:4c%Sh.53345$6m4.32414@pd7urf1no...
>>
<snip>>
> Again yes to the above. But from my experience, the quick transfer is
> not necessarily the best for every situation :-

It is if you're in a hurry... :-)

>
> - Using any new tool, (Screen to GUIs, COBOL files to DBs etc., or as you 
…[4 more quoted lines elided]…
> considerably different database from the original.

Sure. Growth occurs. And when it does, we see different, and often better, 
ways of doing things.

We are then faced with the dilemma of whether we should convert or scrap 
what we have and go back to square one, or continue with what we (now...) 
know is a sub-optimum solution. Usually a balance is struck between these 
two extremes... in this case it is a conversion from ISAM to RDB; probably 
the best that can done under the circumstances.

A "Relational purist" will be unhappy because the RDB is being constrained 
by the original ISAM DB design (which may have also "evolved" over time),, 
and therefore doesn't realise all the true benefits of RDB; someone who 
LOVES ISAM and flat files will be unhappy about why something that works 
fine, is being moved to a "new fangled technology" (even if it is nearly 25 
years old... some people are suspicious of anything less than two decades 
old...)...no-one is ever completely happy.

Given all these conflicts of perspective and interest, it is a miracle there 
are any functioniong systems in the world at all...:-)

My experience is that people do the best they can; (no-one gets out of bed 
in the morning and decides: "I think I'll go into work today and really 
screw up everything I do...yeah, that'll make me feel better...")... 
sometimes they get it wrong, sometimes they get it right, sometimes they are 
constrained by other factors into compromises which are not optimal. Only 
very rarely (and it is more likely if you work for yourself, and can 
therefore decide what you will or will not go with) does the opportunity to 
do something from scratch, using the best technology arise. (Even then, in 5 
years you will realise it could have been better... :-))
>
> - In my case the necessity of converting 700 data sets (different 
…[6 more quoted lines elided]…
>
Sounds pretty drastic...

One advantage of RDB of course, is that it is very easy to "expand the 
design" and tolerate missing data as well.

> - The best way of achieving this for me - Line Sequential - using a fixed 
> record template. Given a value of 2.345 held in pic 9(03)v9(03) comp-3, 
> the template outputs : ",002.345," - the result, all columns are aligned 
> making it very easy to swiftly scroll through records, and make editing 
> changes where necessary.

This is one step away from what I suggested. Only difference, I'd have the 
template write the data directly to the RDB and do the "cleanup" on the RDB, 
where there are better tools available for identifying and correcting data 
anomalies.

However, ANY solution that works, is a GOOD solution... :-}

(I was embarrassed when, as a student pilot, I made a pretty heavy landing 
and apologised to my instructor. He was a Texan who was rarely phased by 
anything, and he just drawled: "Son, any landing you walk away from is a 
GOOD landing...")
>
> - Even with the above approach it is still a fiddly operation, i.e. 
…[4 more quoted lines elided]…
> Different strokes for different folks.

Absolutely.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-12T08:56:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131sb8b2f0atpc7@corp.supernews.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net> <4c%Sh.53345$6m4.32414@pd7urf1no> <583kcsF2fnpmmU1@mid.individual.net> <g6hTh.61601$aG1.7987@pd7urf3no> <585r42F2e105nU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:585r42F2e105nU1@mid.individual.net...
[snip]
> We are then faced with the dilemma of whether we should convert or scrap
> what we have and go back to square one, or continue with what we (now...)
> know is a sub-optimum solution. Usually a balance is struck between these
> two extremes... in this case it is a conversion from ISAM to RDB; probably
> the best that can done under the circumstances.

< http://www.microfocusworld.com/track_page.php?id=5 >
"A partner will present a session that shows how a relational
database can be used with a COBOL application using
standard COBOL I/O statements, WITHOUT any changes
to the code!"

Perhaps the best is no conversion, at all! Just upgrade to the
latest technology.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-12T14:13:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evleq8$o9j$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <g6hTh.61601$aG1.7987@pd7urf3no> <585r42F2e105nU1@mid.individual.net> <131sb8b2f0atpc7@corp.supernews.com>`

```
In article <131sb8b2f0atpc7@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[15 more quoted lines elided]…
>latest technology.

Mr Smith, come now... an organisation where the analyst recommends 
timestamping records... errrr, rows in a database and the manager has to 
turn to the UseNet for help will not, in my experience, embrace a solution 
which requires Spending Money to upgrade technology or sending someone of 
sufficient technical competence to benefit from the experience - as 
opposed to, say, a Corner-Office Idiot - to the Royal Pacific Resort in 
Orlando, FL, USA for three days.

(oh... and a rather common mis-spelling in the paragraph you quoted might 
be seen, by some, as casting aspersions on the relibility of the claims)

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-12T12:19:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176405559.394072.299600@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<evleq8$o9j$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <g6hTh.61601$aG1.7987@pd7urf3no> <585r42F2e105nU1@mid.individual.net> <131sb8b2f0atpc7@corp.supernews.com> <evleq8$o9j$1@reader2.panix.com>`

```
On 12 Apr, 15:13, docdw...@panix.com () wrote:
> In article <131sb8b2f0at...@corp.supernews.com>,
>
…[35 more quoted lines elided]…
> DD

I presume that you mean me and the sleight of hand. I believe slight
of hand is only relevant in BDSM circles.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-12T21:10:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evm78h$ch4$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <131sb8b2f0atpc7@corp.supernews.com> <evleq8$o9j$1@reader2.panix.com> <1176405559.394072.299600@o5g2000hsb.googlegroups.com>`

```
In article <1176405559.394072.299600@o5g2000hsb.googlegroups.com>,
Alistair <alistair@ld50macca.demon.co.uk> wrote:
>On 12 Apr, 15:13, docdw...@panix.com () wrote:

[snip]

>> (oh... and a rather common mis-spelling in the paragraph you quoted might
>> be seen, by some, as casting aspersions on the relibility of the claims)
>
>I presume that you mean me and the sleight of hand. I believe slight
>of hand is only relevant in BDSM circles.

It may have been done with craftiness, Mr Maclean, but I am unsure whether 
it was done in order to deceive... so if it offended perhaps it was a 
sleightless slight.

(wonderful language, this English... how *does* anyone learn it?)

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-13T06:58:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131uoo31usaadf7@corp.supernews.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <g6hTh.61601$aG1.7987@pd7urf3no> <585r42F2e105nU1@mid.individual.net> <131sb8b2f0atpc7@corp.supernews.com> <evleq8$o9j$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:evleq8$o9j$1@reader2.panix.com...
> In article <131sb8b2f0atpc7@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
…[4 more quoted lines elided]…
> >> We are then faced with the dilemma of whether we should convert or
scrap
> >> what we have and go back to square one, or continue with what we
(now...)
> >> know is a sub-optimum solution. Usually a balance is struck between
these
> >> two extremes... in this case it is a conversion from ISAM to RDB;
probably
> >> the best that can done under the circumstances.
> >
…[15 more quoted lines elided]…
> Orlando, FL, USA for three days.

Apart from your alleged experience, this latest
technology would reasonably permit one to identify
"rows in a database" as records since there would
be no difference with respect to a COBOL program,
where the concept "records in a file" is common.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-13T14:17:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evo3dn$o4d$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <131sb8b2f0atpc7@corp.supernews.com> <evleq8$o9j$1@reader2.panix.com> <131uoo31usaadf7@corp.supernews.com>`

```
In article <131uoo31usaadf7@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:evleq8$o9j$1@reader2.panix.com...
>> In article <131sb8b2f0atpc7@corp.supernews.com>,
>> Rick Smith <ricksmith@mfi.net> wrote:

[snip]

>> >< http://www.microfocusworld.com/track_page.php?id=5 >
>> >"A partner will present a session that shows how a relational
…[19 more quoted lines elided]…
>where the concept "records in a file" is common.

Mr Smith, I am not sure what you are calling 'a COBOL program' here.  
According to the last version of the COBOL Language Reference I consulted 
(<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/IGY3LR10/CCONTENTS?DT=20020920180651> 
or thereabouts) there are Reserved Words for file and record access; where 
are you finding the ones which allow 'a COBOL program' to address a 
database?

('Reasonable' might be in the mind of the beholder, of course; a fuel 
injector might be the same with respect to an automobile as a 
carburetor... errr, carburettor... oh, such things make me tyred... 
anyhow, the two devices might be the same in that they both assist in 
supplying the engine with air/fuel mixtures; it may be that 'a rose, by 
any other name', has a different place in poetry than it could in a 
technically-oriented workplace.)

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-13T13:03:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131ve6adqohilc0@corp.supernews.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <131sb8b2f0atpc7@corp.supernews.com> <evleq8$o9j$1@reader2.panix.com> <131uoo31usaadf7@corp.supernews.com> <evo3dn$o4d$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:evo3dn$o4d$1@reader2.panix.com...
> In article <131uoo31usaadf7@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:evleq8$o9j$1@reader2.panix.com...
> >> In article <131sb8b2f0atpc7@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[13 more quoted lines elided]…
> >> timestamping records... errrr, rows in a database and the manager has
to
> >> turn to the UseNet for help will not, in my experience, embrace a
solution
> >> which requires Spending Money to upgrade technology or sending someone
of
> >> sufficient technical competence to benefit from the experience - as
> >> opposed to, say, a Corner-Office Idiot - to the Royal Pacific Resort in
…[10 more quoted lines elided]…
>
(<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/IGY3LR10/CCO
NTENTS?DT=20020920180651>
> or thereabouts) there are Reserved Words for file and record access; where
> are you finding the ones which allow 'a COBOL program' to address a
> database?

The claim was with respect to "using standard COBOL
I/O statements". There was no claim respecting 'physical
files' nor 'physical records' as defined by standard COBOL.

Page 146, FDIS ISO/IEC 1989:2002, 9.1.1 Physical and
logical files, "... In this document, references to records mean
to logical records, unless the term 'physical record' is specifically
used. Similarly, references to files mean to the logical
characteristics of a file, unless 'physical file' is used."

Page 4, FDIS ISO/IEC 1989:2002, 3.1.8 Nonstandard extensions,
"Nonstandard extensions are language elements or functionality
in an implementation that consist of any of the following:
...
3) language elements defined in this International Standard
for which different functionality is implemented, where that
language element is required for conformance to this
International Standard, provided that standard-conforming
behavior is also implemented and that an implementor-defined
mechanism exists for selection of the nonstandard behavior."

Thus, "an implementor-defined mechanism" for selectively
replacing the standard COBOL "file connector" with, say, a
"database connector" would permit "using standard COBOL
I/O statements" to access a database and without
contradicting standard COBOL.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-13T17:16:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evodsg$4ev$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <131uoo31usaadf7@corp.supernews.com> <evo3dn$o4d$1@reader2.panix.com> <131ve6adqohilc0@corp.supernews.com>`

```
In article <131ve6adqohilc0@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:evo3dn$o4d$1@reader2.panix.com...
…[44 more quoted lines elided]…
>files' nor 'physical records' as defined by standard COBOL.

This might be, Mr Smith, a reason for my having mentioned neither 
'physical files' nor 'physical records'.  What implementors may wish to 
do with access-methods are their own concerns.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-14T00:04:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5899tkF2fm85tU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <1175717128.965681.301480@l77g2000hsb.googlegroups.com> <1176223479.428972.39830@l77g2000hsb.googlegroups.com> <sNVSh.51648$6m4.42486@pd7urf1no> <5834o5F2ecb3nU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5834o5F2ecb3nU1@mid.individual.net...
>
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:sNVSh.51648$6m4.42486@pd7urf1no...
> <snip>>
<snip>>>

>> If/when you get a paperback, or articles on design from the Web, 
>> concentrate on the term 'Normalization' so that you have a handle on it.
…[8 more quoted lines elided]…
>
This has now been posted... Accessing the following link will reveal 3 
documents that are worth reading if you are considering migrating ISAM to 
RDB....

http://homepages.ihug.co.nz/~dashwood/dashwood/RDBStuff/

Any or all feedback appreciated.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-04-04T20:38:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y1UQh.26894$6m4.24989@pd7urf1no>`
- **In-Reply-To:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com>`

```
DaveM wrote:
> On Apr 3, 9:13 pm, docdw...@panix.com () wrote:
> 
…[34 more quoted lines elided]…
> gain a better perspective about the options we are faced with.

<snip>

So you have gone searching David, but did your search take the following 
into account  :-

- Google Search, enter with the hyphen, "SQL-Examples" - will give you 
54K hits

- The N/E V4.0 on-line book regarding SQL - Database Access 
http://supportline.microfocus.com/supportline/documentation/books/nx40/nx40indx.htm 


- From the IDE top Menu Bar ----> Tools ----> Open ESQL Assistant, 
which lets you model SQL queries and run them, and get results, WITHOUT 
compiling. Once your test works, then you can copy/paste the proven SQL 
statement into a COBOL program and compile. (At first sight this tool 
looks complicated, but it isn't. Having set up a dummy DB table, have 
the patience to read through the text and then start experimenting with 
ESQL Assistant - you will be pleasantly surprised).

- Last and by no means least - sign up for the free Micro Focus Forum. 
Post under Net Express, ensuring "SQL" appears in your message title - 
and you should get help from an M/F lady specializing in DB support.

Regardless of the above, it will be worth your while to get a paperback 
'How to ...." on DBs and SQL.

Jimmy
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 4)_

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-10T09:52:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176223974.296394.233090@d57g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<y1UQh.26894$6m4.24989@pd7urf1no>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <y1UQh.26894$6m4.24989@pd7urf1no>`

```
Oops.  Instead of posting my response to you under your recent
message, I mistakenly posted it under TLEADERS's message.  Sorry about
that!  -Dave
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-05T09:44:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ev2gd1$ov7$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com>`

```
In article <1175713257.593859.110760@n59g2000hsh.googlegroups.com>,
DaveM <renfrew76@xemaps.com> wrote:
>On Apr 3, 9:13 pm, docdw...@panix.com () wrote:
>> In article <1175626528.510733.311...@n59g2000hsh.googlegroups.com>,
…[24 more quoted lines elided]…
>the answers I am looking for are actually being kept.

Let's just say that when asked for any sort of evidence of your work you 
presented none, Mr Minor... there's a bit more data available in this 
newsgroup to indicate that than your having 'looked everywhere'.

>
>The gist of what I am currently seeking should exist mainly within the
>minds of many of those who frequent this newsgroup, hence my inquiry.

That may well be... you are asking a group of what have been called 
'knowledge workers'.

>Forgive me for not making it clearer, but I am not asking anyone to go
>out on a google tour on my behalf; I am only asking for information
>relevant to people's own real-world experiences such that we might
>gain a better perspective about the options we are faced with.

This is called 'a consultation', Mr Minor... and a few people here are 
accustomed to a phenomenon of which you may not be aware:  they use their 
brains on the behalf of someone's data-processing project and they get 
paid for it.

[snip]

>> >The second problem involves how to handle record locking issues
>> >among multiple users.  The lead analyst wants us to code logic
…[18 more quoted lines elided]…
>primarily by functions that are internal to the rdb itself.

'Supposed to be', Mr Minor?  What caused anyone to come to that 
conclusion... something they overheard in a pub or read in an article in 
an airline magazine?

>Regardless of how time-honored a given technique may be, it seems to
>me that by going to the trouble of coding our own locking handler we
>will only end up sidestepping what the rdb is designed to take care of
>for us, and all in exchange for a manual (and inferior) version of
>that capability.

What 'seems to you', Mr Minor, might be different than what is stated in 
the product's documentation or in the product's actual functioning... if 
someone has made assertions about the product's capabilities then those 
assertions might need to be verified.

>
>This is rather like harnessing a team of mules up to a tractor to plow
>the field.  Sure, its possible, but we'd be foolishly wasting the very
>reasons that we'd paid extra money to buy the damn tractor in the
>first place.

I was taught, Mr Minor, that 'The responsibility for the allocation, 
co-ordination and motivation of personnel and resources towards the 
accomplishment of a stated Executive goal is that of Management'... if you 
have Managers who purchase tractors in order to harness programmers to 
pull them then the Executives deserve what results.

>
>
…[13 more quoted lines elided]…
>supposed to be automatically handled by the rdb.

Another 'supposed'... building a product based on suppositions might 
result in disappointment.

>What we are trying
>to learn about are the protocols of dealing with wait-locks, time-
>outs, and prevention of unilateral changes etc.

Those should be mentioned in the Product Documentation, along with where 
it talks about how 'the Product is supposed to automatically handle 
deadlocks'... wonderful things, those 'supposeds' and 'should bes'.

>>
>> >Here is a simple/fictitious representation of the type of code
…[26 more quoted lines elided]…
>its purpose.   :)

It seems to have done that, and more.

>
>In any case, point taken.

How pleasant... when one is out scouring the UseNet for free advice it 
might be best to do so without the equivalent of 'spinach on one's teeth'.

>
>>
…[26 more quoted lines elided]…
>of formal training.

Your management will get what they pay for; try to remind them about the 
difference in using an architect who has AIA certification and one who 
built a dog-house or two.

>Complaints I have aplenty, of course, but that
>won't resolve anything.

Complaints are not nearly as valid as plans, with cause-and-effect clearly 
laid out.  Implement a new technology without insuring a trained support 
base and it is likely that support will be... less than stellar.

>The only realistic and proactive plan we have
>at this point is to continue doing what we are doing, namely, to
…[3 more quoted lines elided]…
>world to lead us to some working examples.

Hmmmmm... Read Admiral Grace W Hopper once said something along the lines 
of ''But we've *always* done it this way'' is the most dangerous phrase in 
the language.'  Your approach reminds me of a USSR-era joke from decades 
on back:

What is Marxist philosophy?  Marxist philosophy is a black cat in a black 
room.

What is Marxist-Leninist philosophy?  Marxist-Leninist philosophy is 
looking for a black cat in a black room.

What is Marxist-Leninist-Stalinist philosophy?  Marxist-Leninist-Stalinist 
philosophy is looking for a black cat in a black room and, every so often, 
shouting out 'I've got it!  I've got it!'

There used to be a bit of Workplace Humor about beating a dead horse... 
but what I know is that if you go into a bar frequented by longshoremen 
and say 'Hey, fellows, we're going to be doing some packing and lifting at 
our place... who'd like to give us a free bit of work?' you may find 
yourself disappointed with the results.

>
>Thank you for your help.

A pleasure.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 4)_

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-09T10:00:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176138034.214060.257610@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<ev2gd1$ov7$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <euuu4h$8a9$1@reader2.panix.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com>`

```
Mr Dworf,

Hindsight being 20-20, our archival research would have yielded much
better results had we known to search for the term "embedded sql".
Had you bothered to heed my earlier mention about our admitted
starting place of ignorance then you would have already figured out
that it can be quite difficult to ask for something when you don't
even know what it is really supposed to be called in the first
place.

Speaking of my own ignorance, I really should have thought to check
your track record before I responded to you the first time.  Having
read a sampling of your archived postings since then I have largely
found that your 'input' and 'help' are much more aptly labeled
'heckling' and 'belittlement'.  A large part of your responses seem to
be the result of your purposefully reading between lines that aren't
there, and twisting the ones that are, just to stir up reactions from
people for your subsequent entertainment.

You could learn a lot from the other three respondents to this
inquiry.  Without demanding research evidence nor accusing people of
trying to pilfer other's professional thoughts, these individuals have
graciously given me the working examples I was looking for, along with
suggestions of books/resources and pointers to better search criteria
(e.g., Embedded Sql).

Given your track record, Mr Dworf, I believe that there are two things
forthcoming from you that are practically inevitable:    1) You are
absolutely going to have to have the last word in this thread,  and,
2) You are going to continue to 'help' other requestors in this same
fashion until either death or getting a life.

You are not worth any more of my time.  May you savor the distance and
enjoy your freedom.

Dave
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-09T18:25:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eve0f5$lsf$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com>`

```
In article <1176138034.214060.257610@q75g2000hsh.googlegroups.com>,
DaveM <renfrew76@xemaps.com> wrote:
>Mr Dworf,

Please... jes' ol' Doc, if you can manage to spell that correctly.

>
>Hindsight being 20-20, our archival research would have yielded much
…[5 more quoted lines elided]…
>place.

The responsibility for knowing where one is going and how to request such
a thing is that of the traveller... knowing neither where one wishes to
end up nor how to request information about it may, indeed, result in
one's getting lost.

>
>Speaking of my own ignorance, I really should have thought to check
>your track record before I responded to you the first time.

You might have checked other things as well... there's an Olde Joke you 
might have stumbled across, say, at 
http://www.dotnetspider.com/fun/Computer-Joke-838.aspx .

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-09T12:59:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h83l135hg4pgs80td2kqima848pka3edtm@4ax.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com>`

```
On Mon, 9 Apr 2007 18:25:41 +0000 (UTC), docdwarf@panix.com () wrote:

>You might have checked other things as well... there's an Olde Joke you 
>might have stumbled across, say, at 
>http://www.dotnetspider.com/fun/Computer-Joke-838.aspx .

Although looking up the longitude and latitude mentioned in that joke
leaves me scratching my head.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-09T19:02:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eve2jj$ns9$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <h83l135hg4pgs80td2kqima848pka3edtm@4ax.com>`

```
In article <h83l135hg4pgs80td2kqima848pka3edtm@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 9 Apr 2007 18:25:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>leaves me scratching my head.

Don't worry, Mr Brazee... somehow that will be the programmer's fault, as 
well.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-04-09T16:45:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<131lcvm34r0b3ba@news.supernews.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <h83l135hg4pgs80td2kqima848pka3edtm@4ax.com> <eve2jj$ns9$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <h83l135hg4pgs80td2kqima848pka3edtm@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[10 more quoted lines elided]…
> fault, as well.

Evidently as the location is about 500 miles east of New York City, in the 
Atlantic.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-10T11:39:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58014tF2f874sU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:eve0f5$lsf$1@reader2.panix.com...
> In article <1176138034.214060.257610@q75g2000hsh.googlegroups.com>,
> DaveM <renfrew76@xemaps.com> wrote:
…[16 more quoted lines elided]…
> one's getting lost.

It certainly does if one only encounters unhelpful people.

People of goodwill can assist the traveller to more clearly define the goals 
and the road, even if these are fuzzy at the start.

Sometimes the actual destination is not the one that was originally 
envisioned, but as always, the action of getting there is an opportunity for 
growth.


>
>>
…[6 more quoted lines elided]…
>

Not sure what the point is here... we have a patently incompetent 
programmer, and a patently stupid Project Manager, neither of whom have any 
responsibility for their actions.

As they are both idiots, whatever their interaction is, it is of little 
consequence. For this joke to work, it would be necessary to identify with 
one or other of the parties.  This requires us to assume the same mantle of 
idiocy that they both display.

Ah, now I see why SOME might find it amusing... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-10T00:41:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evemfl$s5c$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net>`

```
In article <58014tF2f874sU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:eve0f5$lsf$1@reader2.panix.com...
…[20 more quoted lines elided]…
>It certainly does if one only encounters unhelpful people.

'Helpful', Mr Dashwood, might be in the mind of the beholder... assisting 
someone in learning that it is best to swallow before speaking can not 
only assist in clarity of communication, it may decrease someone's chance 
of aspirating food.

>
>People of goodwill can assist the traveller to more clearly define the goals 
…[4 more quoted lines elided]…
>growth.

Being taught that saying 'row' and when to say 'record' when one seeks 
free advice from professionals about a business-related matter might cause 
one to be taken... a bit less seriously that one desires could well be an 
'opportunity for growth' that comes about completely serendipitously, 
sure!

>>>
>>>Speaking of my own ignorance, I really should have thought to check
…[12 more quoted lines elided]…
>consequence. For this joke to work, it would be necessary to identify with 

Leaving aside that the text in the URL given might be seen as showing as 
much about programming comptence as it does about managerial stupidity 
(but it might be seen as... significant how someone might leave a 
reference to a programmer in lower case while Project Manager gets 
Capitalised) it might be wise to recall an interchange from that Classic 
of Anciente Philosophie, 'The Day the Earth Stood Still' (as quoted on 
http://imdb.com/title/tt0043456/quotes ):

--begin quoted text:

Mr. Harley: Your impatience is quite understandable.
Klaatu: I'm impatient with stupidity. My people have learned to live 
without it.
Mr. Harley: I'm afraid my people haven't. I'm very sorry... I wish it were 
otherwise. 

--end quoted text

[snip]

>Ah, now I see why SOME might find it amusing... :-)

To the best of my knowledge, Mr Dashwood, no-one has posted to this forum 
calling it such.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 7)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-12T12:14:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176405267.687547.144160@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<58014tF2f874sU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net>`

```
On 10 Apr, 00:39, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:
> > You might have checked other things as well... there's an Olde Joke you
…[14 more quoted lines elided]…
> Pete

I have to take issue with your description of the Programmer as being
incompetent; he clearly answered the question posed in the most
accurate fashion possible, volunteering more information than is
strictly necessary. I wonder if there is a certain note of
defensiveness in your response?

I do, however, agree that the project manager is clearly incompetent
(at ballooning, at boy-scout preparation, at map-reading, at eliciting
information?).

;-)
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-13T22:58:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58961sF2ftvphU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1176405267.687547.144160@q75g2000hsh.googlegroups.com...
> On 10 Apr, 00:39, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[24 more quoted lines elided]…
> strictly necessary.

Really? By what strange definition of  "competence" does a person standing 
in a field, decide that his current location is at co-ordinates that are 
several hundred miles off-shore in the Atlantic Ocean?

If this is your idea of the "most accurate fashion possible" I can 
understand how getting a job may be ..... difficult.


> I wonder if there is a certain note of
> defensiveness in your response?


I wonder if there is a certain note of attempting to stir things in yours?


> I do, however, agree that the project manager is clearly incompetent
> (at ballooning, at boy-scout preparation, at map-reading, at eliciting
> information?).
>

Yes, on that we can agree.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-13T08:20:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nb4v13hdjpic5jlmqkunkobe5qdt99nc33@4ax.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net>`

```
On Fri, 13 Apr 2007 22:58:13 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Really? By what strange definition of  "competence" does a person standing 
>in a field, decide that his current location is at co-ordinates that are 
>several hundred miles off-shore in the Atlantic Ocean?

Standing in a field is one thing.   Outstanding in a field is
something else.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-14T11:38:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58aijvF2gcvk9U1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <nb4v13hdjpic5jlmqkunkobe5qdt99nc33@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:nb4v13hdjpic5jlmqkunkobe5qdt99nc33@4ax.com...
> On Fri, 13 Apr 2007 22:58:13 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> something else.

ROFL!

(Of course, I wouldn't know, having striven for mediocrity throughout ost of 
my life... :-))

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-13T09:00:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176480052.803028.87680@p77g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<58961sF2ftvphU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net>`

```
On 13 Apr, 11:58, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[52 more quoted lines elided]…
> Pete

According to my map reading skills he would have been standing on the
Sohm Plain, probably at a depth of around 1000 feet. I give you that
his GPS (if he had one) was somewhat out of true but then there is no
field at that location so the joke needs to be updated. So that still
leaves the PM at 300% more incompetent than the Programmer.

And YES, I was stirring it a bit, but I have noticed a certain
tendency on your part to blame programmers before managers for project
ills and skills shortages.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-14T12:46:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58amj3F2fva6gU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1176480052.803028.87680@p77g2000hsh.googlegroups.com...
> On 13 Apr, 11:58, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
>> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>>
<snip>
> So that still
> leaves the PM at 300% more incompetent than the Programmer.

Just like someone being 300% more dead than another...

>
> And YES, I was stirring it a bit, but I have noticed a certain
> tendency on your part to blame programmers before managers for project
> ills and skills shortages.
>
OK, let's finish this right here, once and for all.

I have been a programmer since 1965. I'm still a programmer. I posted 
program code to this very forum yesterday (when was the last time you did, 
Alistair?) and I am taking a break from writing more program code (on a 
Saturday) to write this response. I intend to be a programmer as long as I 
can see and use my fingers.

However, although programming is a passion for me, it is not the only "hat" 
I wear. For almost two decades  now I have been making a living out of 
managing programmers and providing consultancy to corporations. So amongst 
my other "hats"... manager, consultant, negotiator, mediator, conflict 
resolver, trouble shooter, and project manager.

I am getting a bit tired of certain people here ALWAYS seeing the trouble as 
being caused by management so, if I defend that point of view, it  is 
because of that. I don't like unbalanced assessments.

There ARE bad managers, just as there are crap programmers. Both varieties 
make life tiresome for those of us who just want to do a job as well as we 
know how, and get some satisfaction from it.

As for blaming either programmers or managers for the ills of a project, I 
never do that. I don't blame anyone for anything. Ever.

I see no point in blame (by the same token, I see rehabilitation as 
preferable to punishment... guess I'm a pinko Liberal :-)), and every 
project or team I manage promotes a blame-free culture.  I encourage 
personal responsibility and try to see that people have enough empowerment 
to exercise their discretion and take responsibility. Someone makes a bad 
decision, they learn from it and move on. There can be no growth if all we 
ever do is stay comfortable and do as we are told, without thought or 
question, then gleefully point the finger at others when things go pear 
shaped. (I have fired people for doing this, even though they were 
technically "right" and quite convinced they could not be touched because 
they had simply done as they were told, knowing full well the consequences 
of doing so...). People screw up, they fix it.(Sometimes the rest of the 
team help them fix it; I have never abandoned anyone on my team because they 
screwed up. I have defended them (even when they were patently wrong, 
sometimes) and ensured that whatever was made wrong was made right.). This 
applies equally to managers and programmers.

NO-ONE works alone on my watch, including me. I keep the team informed of 
what is going on politically and explain what I am doing about it. I listen 
to suggestions and considerations and apply them if they make sense....I 
work very hard to keep politics and paperwork off their backs so they can do 
their job. (Funny thing, I never have trouble getting tech people to work 
with me again, once they have done so... can't say the same about certain 
managers.)

I've fought battles at senior management level and right through the gamut 
of management. I know that Doc's "Corner Office Idiot" (actually, I love 
that... :-)) is a reality, and I've dealt with them too. But, and this is 
the important point, there are also people in corner offices who are doing 
the very best they can. There are people who are the first to arrive and the 
last to leave, dedicated company people who put heart and soul into their 
jobs and are defined by the work they do. (No, I don't think this is 
healthy, but I'm certainly not going to denigrate these people or tar them 
with the same brush as COIs.)

When every programmer and staff member in the company is saintly and without 
fault, when these perfect superior people are NEVER wrong and ALWAYS right, 
THEN, I might agree they have the right to denigrate the people who manage 
them (be they idiots or saints). In the meantime, criticism is fine and 
natural but it should be fair and true, and preferably from a position of 
seeking to improve, not seeking to destroy, humiliate, or belittle, for the 
sake of destruction or to boost one's own ego. There is enough negativity 
and frustration in everyday work without seizing on the opportunity to 
generate more because some COI screwed up again.

All of us every day have to deal with management decisions that are not 
perfect, sometimes downright stupid. It goes with the territory. You pick 
your battles and win the ones you can; get stupid policies changed, don't 
sit back and pontificate on how stupid THEY are and how clever WE are...

In the final analysis, I guess it is this US and THEM perception that really 
irritates me. Especially when I can find myself in both camps...:-)

OK, that's all I really want to say on this... back to work. (I'm working 
for this really hard bastard who sets me impossible goals and makes me work 
weekends if I don't achieve them... soon as I can, I'm going to quit working 
for him and get a job with some much more understanding management...:-))

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 11)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-14T13:42:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176583356.665549.161780@p77g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<58amj3F2fva6gU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net>`

```
On 14 Apr, 01:46, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[61 more quoted lines elided]…
> what is going on politically and explain what I am doing about it.

Doesn't that get you into trouble with your managers?


 I listen
> to suggestions and considerations and apply them if they make sense....I
> work very hard to keep politics and paperwork off their backs so they can do
…[37 more quoted lines elided]…
> Pete.


Thanks Pete, a good response. I think that a problem with management
is that we all think that we can do better if only we were in their
shoes. The reality is that we would probably be worse at management
than those we criticise. I know from having had disagreements with
managers in the past that there often is much that they see that we do
not know of, at the coalface, and I have certainly been grateful for
their shields from time to time.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-15T13:02:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58dbscF2gah4lU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1176583356.665549.161780@p77g2000hsh.googlegroups.com...
> On 14 Apr, 01:46, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[78 more quoted lines elided]…
> Doesn't that get you into trouble with your managers?

Yes, of course it does... :-)

(I don't reveal things I have been told in confidence by managers or team 
members, but if there is information that affects our project and I can't 
tell them, I may say that. As soon as it is clear to tell them, I do so.)

Fortunately, these days having a certain track record, I tend to report to 
very senior people and they like having an independent view which is not 
trying to further a career by arse-licking, but is honestly trying to make 
things better and get things done. One advantage of being an independent 
consultant is that you don't need to worry about career advancement, and can 
call things as you see them. I can think immediately of several occasions 
where I stated opinions at Board level which caused a shocked hush :-) But, 
further down the track I was thanked for speaking out, and the result was 
change in the Organization which was better for all concerned.

The point is you don't go looking for confrontation and you work with 
people, understanding their problems and helping to look at/for solutions, 
but occasionally, you will encounter a COI who believes that the power of 
the corner is the only way to do things and that any suggestion for change 
is simply disruptive and stirring rebellion in the ranks. (These people are 
invariably the ones who have acquired power through longevity rather than 
ability, and the power they enjoy at work is usually the only part of their 
life that is empowered. As a result, they misuse the power they have.)

I have encountered a number of these and I have never stabbed any of them in 
the back or gone "over their heads" without upfront notification. After 
realizing that there will be no progress, it comes to a point of 
acknowledging that to be the case, and stating that both cases (his and 
mine) must now be escalated to the next level of management. (Sometimes this 
will be IT Director or Board). I make sure that it doesn't become personal 
(at least as far as I'm concerned; some COIs are actually very vindictive 
when "threatened").

Maybe I do more entertaining presentations, maybe it's because my case is 
better, but I don't recall ever losing one of these impasses :-) Then it 
comes down to damage control and trying to make sure the sullen resentment 
engendered in the COI by being publicly thwarted, is discharged, by 
participation in something successful. (I always make sure the local 
management get credit for all success; and the team (who really did the 
work) are treated to a lavish party at my expense, if the company won't 
stump for it.. (It never ceases to amaze me the number of corporations who 
don't acknowledge outstanding work from their employees..."It's not our 
policy" ... "Well, it bloody well should be, and if you won't do it, I'll do 
it myself...") Especially true in the U.K. for some reason...)

I hasten to add that I have also worked for some corporations who DO gladly 
acknowledge their staff. On at least two occasions I can remember being 
surprised at how generous the Company was, once it was pointed out that some 
of the people in the trenches were going the extra mile...

So, yes, it isn't always plain sailing and sometimes managers are left 
feeling bad. I'm always sorry about that, but how they feel is their 
problem... I'm not paid to win popularity contests...and I'm not so insecure 
as a person that I need the approval of COIs :-)

>
>
…[62 more quoted lines elided]…
>

Thanks Alistair; I appreciate you saying that.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-15T07:46:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176648406.952042.96450@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<58dbscF2gah4lU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <58dbscF2gah4lU1@mid.individual.net>`

```
On 15 Apr, 02:02, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[204 more quoted lines elided]…
> Pete.

BTW, I don't post code (as you correctly observed) as there are others
who can do better than myself and my ego is fragile enough that it
wouldn't stand the horse-whipping I would get. I have, however, passed
code to others via email who I felt would benefit from it and I have
posted code, for comment, on other newsgroups (Assembler) and that got
justly critiqued. I would also admit that I feel that I don't have the
time to post wads of code, as others do. I have work that I have to do
for others that should take priority but sloth wins out.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-16T11:16:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58fq1jF2gql85U1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <58dbscF2gah4lU1@mid.individual.net> <1176648406.952042.96450@o5g2000hsb.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1176648406.952042.96450@o5g2000hsb.googlegroups.com...
> On 15 Apr, 02:02, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
<snip>>
> BTW, I don't post code (as you correctly observed) as there are others
> who can do better than myself and my ego is fragile enough that it
…[6 more quoted lines elided]…
>
Fair enough. My comment wasn't meant to wound, just to point out that 
programmers write programs and that means producing code.

I was being criticized for appearing not to support programmers when I have 
been one all my working life and intend to go on being one.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-16T13:00:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com>`

```
On 14 Apr 2007 13:42:36 -0700, "Alistair"
<alistair@ld50macca.demon.co.uk> wrote:

>Thanks Pete, a good response. I think that a problem with management
>is that we all think that we can do better if only we were in their
>shoes. 

I doubt it.    Think of sports stars.   The stands are full of people
criticizing the quarterback - people who know that there's no way they
would survive on the field.

>The reality is that we would probably be worse at management
>than those we criticise. I know from having had disagreements with
>managers in the past that there often is much that they see that we do
>not know of, at the coalface, and I have certainly been grateful for
>their shields from time to time.

Even if I had the competence (which I don't) - I once had to fire
somebody.   That was once too often, I won't be in that position
again.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-04-16T19:26:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j5QUh.17102$Um6.3678@newssvr12.news.prodigy.net>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`

```
> Even if I had the competence (which I don't) - I once had to fire
> somebody.   That was once too often, I won't be in that position
> again.

In my experience a common mistake is making the best <anything> the 
<anything> manager.

Far too often this does nothing more than subtract a quality <anything> 
while adding a crummy manager; a bad deal no matter how you do the math..

MCM
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-17T12:44:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58ijipF2h99p3U1@mid.individual.net>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com> <j5QUh.17102$Um6.3678@newssvr12.news.prodigy.net>`

```

"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:j5QUh.17102$Um6.3678@newssvr12.news.prodigy.net...
>> Even if I had the competence (which I don't) - I once had to fire
>> somebody.   That was once too often, I won't be in that position
…[7 more quoted lines elided]…
>
Absolutely.

Many organizations (and people) seem to fail to realize that there is a 
specific skill set required to manage, and it is not in our genes...

It can be acquired painfully over time; training is a much more effective 
route.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-16T22:54:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f00urm$jjt$1@reader2.panix.com>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`

```
In article <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On 14 Apr 2007 13:42:36 -0700, "Alistair"
><alistair@ld50macca.demon.co.uk> wrote:

[snip]

>>The reality is that we would probably be worse at management
>>than those we criticise. I know from having had disagreements with
…[6 more quoted lines elided]…
>again.

I am reminded of a tale, perhaps apochryphal: in a class at Harvard a 
professor gave an example to a roomful of MBA candidates, a conflict 
between a line-worker and a supervisor.  One student said that the 
line-worker should be fired... after all, anyone can work an 
assembley-line but a good supervisor is hard to find.

The professor left the lectern, stood in front of the student and declaime 
that this was the *stupidest* thing he'd heard in all his years of 
teaching and that he would not tolerate someone capable of generating this 
kind of nonsense in his class... and the student was to get out, *now*.

The student (and the rest of the class) sat, dumbfounded... and the 
professor then swept the books and papers (this was in the Oldene Dayse, 
before students had computers) on to the floor and shouted 'GET OUT OF MY 
CLASS, *NOW*!!!'

The student gathered his stuff and left the room... and then, when the 
professor had returned to the lectern and resumed the class, crept back in 
the door and sat in the last row.

The professor then stopped the discussion and called out 'So, Mr Jones... 
tell us all what it is like to be fired.'

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-17T13:04:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58ikp5F2gthmlU1@mid.individual.net>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com> <f00urm$jjt$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f00urm$jjt$1@reader2.panix.com...
> In article <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[39 more quoted lines elided]…
>
One week, in 1969, I was fired from my programming job (I had, in all 
innocence, done something that caused my manager to lose his annual 
increment :-) It was political, not technical, but being young at the time I 
did not have the broader vision I now enjoy. I can say that had he not lied 
and prevaricated in the first place, the situation could not have arisen.)

Not only did he fire me, he promised I would never work again. "Your 
programming career is over."

(In those days the City of Auckland had less than half a million people and 
there were no more than 20 IBM mainframe sites within a 15 mile radius of 
the city centre.  It was a small IT community. He went to the IBM User Group 
and told those there assembled that he had fired me for disgraceful and 
unethical conduct and would strongly recommend no-one else ever employ me.)

 To say that this guy was a vindictive tyrant might be construed as sour 
grapes on my part, so I won't say that... :-)

I remember how it felt. I went home to find my wife packing; she had decided 
to leave me. (In retrospect, I don't really blame her, but that's another 
story... :-) Obviously, she didn't know I had been fired so that didn't 
figure in her decision. Because we both worked she owned half of the car and 
I couldn't afford to stay in our flat without her contribution, so within a 
couple of days of finding myself alone and unemployable, I also had no 
transport and nowhere to live... :-)  (Yeah, I can laugh now, but it wasn't 
funny then.... :-))

The point is, I have never forgotten how that felt, and would think long and 
carefully before imposing it on someone else. (And then it would never be 
with spite or vindictiveness, only because it was necessary.)

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-17T01:27:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f017qk$nvk$1@reader2.panix.com>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com> <f00urm$jjt$1@reader2.panix.com> <58ikp5F2gthmlU1@mid.individual.net>`

```
In article <58ikp5F2gthmlU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f00urm$jjt$1@reader2.panix.com...

[snip]

>> The professor then stopped the discussion and called out 'So, Mr Jones...
>> tell us all what it is like to be fired.'

[snip]

>The point is, I have never forgotten how that felt, and would think long and 
>carefully before imposing it on someone else.

I believe it was Aeschylus who said 'Great hardships make for later 
entertainments'... and perhaps that leads well into The Other Side of the 
Coin.

Aeschylus is remembered by many as being a playwright... but he was also a 
'general' (Gr. 'strategos') and it was reported that this rank was what he 
had inscribed on his tombstone and nothing about his dramatic victories.

I've found sports metaphors abound in the workplace - 'The football is in 
your court' is one that I've heard - and these are nuisances to me for two 
reasons.  First, I don't play or follow sports and second my training as a 
Classicist causes me to try to go to the source for things... and sports 
are, rather often, a kind of ritualised combat.

(this can make for Big Laffs when someone will say 'We need someone to 
throw a real Hail Mary now'... and into the silence I'll pour 'Well, if 
you think it'll do any good, why not?  Ave Maria, gratia plena, Dominus 
tecum, Benedicta tu in mulieribus...')

Anyhow... any kind of soldier, at any time, may be called upon to make 
decisions which can cause death for himself, his comrades-in-arms 
(literally) or his subordinates.  Don't like the possibility?  Don't 
enlist, don't accept the promotion or (in times of conscription) don't 
stay in a country with an extradition treaty... or as it has been said 
before:

Lead, Follow or Get Out Of The Way

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 15)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T06:11:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176901909.853485.183270@d57g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<58ikp5F2gthmlU1@mid.individual.net>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com> <f00urm$jjt$1@reader2.panix.com> <58ikp5F2gthmlU1@mid.individual.net>`

```
On 17 Apr, 02:04, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:f00urm$jjt$1@reader2.panix.com...
> > In article <2qh7231fi9tlotbqmdi3afv7ue7fsn2...@4ax.com>,
…[74 more quoted lines elided]…
> - Show quoted text -

In this pygmies' defense I would like to point out that the guy that I
fired was totally incompetent (however, he did pass the interview and
that makes me doubt my ability to gauge how good a candidate is) and
he was about to blast his large redundancy package (from another firm)
on a flash motor so I started the inevitable process so that he
wouldn't be entirely lacking in monetary resources when he hit the
street.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-17T12:41:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58ijdiF2gr0i0U1@mid.individual.net>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com...
> On 14 Apr 2007 13:42:36 -0700, "Alistair"
> <alistair@ld50macca.demon.co.uk> wrote:
…[17 more quoted lines elided]…
> again.

That you would feel this way, shows you were probably a good manager, 
Howard.

I have fired less than half a dozen people in 20 years and every time I 
looked on it as a failure on my part as well as theirs. It is never easy, 
and it is always a last resort after warnings and attempts to redirect, or 
because they have done something so outrageous and beyond the pale that it 
is just unacceptable.

It is the horrible little weak pygmies of managers who actually enjoy firing 
people. Fortunately, these guys don't usually last too long...

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T06:04:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176901445.601955.270330@b75g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`
- **References:** `<1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176583356.665549.161780@p77g2000hsh.googlegroups.com> <2qh7231fi9tlotbqmdi3afv7ue7fsn2ijj@4ax.com>`

```
On 16 Apr, 20:00, Howard Brazee <how...@brazee.net> wrote:
> On 14 Apr 2007 13:42:36 -0700, "Alistair"
>
…[17 more quoted lines elided]…
> again.

I was once instrumental in initiating the process by which someone I
worked with got fired (and I had the final decision). I don't regret
it, but I do regret being the corner office idiot who hired the chump
in the first place!
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 11)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2007-04-14T16:43:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176594225.920162.13260@w1g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<58amj3F2fva6gU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net>`

```
On Apr 14, 1:46 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[101 more quoted lines elided]…
> Pete.

I agree with you and with Alistair's response, though think that such
issues are often basically a system problem, for exmaple, take the
following items and stir them with a wooden spoon over a hot stove.

Customers always want/buy/can afford/justify to their shareholders
items/services that are the cheapest, most effective and speedily
available.

Employees want as much money as possible for as little effort as
possible in congenial surroundings.

Employers want as much work as possible for as little money as
possible in the cheapest facilities practical.

If you pay peanuts you get monkeys

If a million monkeys spent a thousand years bashing away on
typewriters, one might write the works of Shakespeare (some might say
that one did, only he didn't use a typewriter, I don't know what his
handwriting was like, but I work in the NHS).

Many programmers and probably analysts wrote most of their programs
online with two fingers.  Managers paid them to do it like that.  I
wrote much of mine like that too.

Employers and employees are often unwilling (can not afford) to invest
time and money in training to use software and equipment to best
advantage.

No one gets a job for life anymore and many didn't anyway.

Employers are mostly in no position to promise a job for life.

Restrictive practices and agreeing to inappropriate contract terms.

The need for employers and employees to protect and invest in
intellectual property and rights while still managing to do their jobs
effectively with several employees and employers.

Most software written on behalf of employers was not reviewed for a
possible conflict with software patents, which were in any case
legally disallowed for much of my career.  Certainly not in my
personal experience in a variety of companies and government
organisations.  When I have had to specify, write or amend a program
to provide some funtionality, I have never had to check if someone
else from another organisation had done something similar and patented
it, so that my work was in contravention.  I can not begin to imagine
how much extra overhead and delay there would be if all organisations
had to make such checks.

Twiddling thumbs furiously.

Some of the programming and design standards I have seen.

Drinking at lunchtime.

Some of the progams and specifications that I have seen.

I have also seen some very well written specifications, programs and
user documentation.

Cultures of working long hours.

Getting a life

Office parties.

Perennial legislative changes necessitating software amendment.

Tax structures.

Political planning generally being subject to general election and
short-term public opinion constraints.

Alternatives to democracy have generally been much worse.

Voter apathy and political skulduggery.

Investing for the future in child and adult education.

That's probably enough of this rant, I am certainly not perfect myself
either.  I have just enjoyed a very pleasant ride on my motorbike to
Symonds Yat in Gloucestershire, in fine good and warm weather.  I
stopped on the way back to listen to the nightingales in a local
nature reserve.

(I tried posting this earlier but lost my connection, though it said
it was sent, but now can't see it in the list, though it might turn up
later. I have lately taken to saving posts separately while writing
them to protect myself from such problems and this one is very similar
to the other, though I think it is better for having had a little more
time spent on it.)

Robert
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-15T13:55:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58df0rF2gb7u1U1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176594225.920162.13260@w1g2000hsg.googlegroups.com>`

```

"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1176594225.920162.13260@w1g2000hsg.googlegroups.com...
> On Apr 14, 1:46 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[134 more quoted lines elided]…
>

I actualy enjoyed this, Robert... it is almost surreal :-)

All of these factors are part of what we do and we have to deal with them.

(Please excuse the use of "you" in the rest of this document; it is NOT 
targeted at you personally, it's just that I find the impersonal "one" 
sounds pretentious, and I'm not comfoprtable with using it any more than 
absolutely necessary...)

Attitude can sometimes be a decisive factor; if you really can't change 
something, you may be able to change your mind about it, decide it is not so 
important, and get on with what you're really trying to achieve. Of course, 
if you go to work without really trying to achieve anything, other than pay 
the rent, then you can't be surprised if the workplace is not an enjoyable 
environment :-)


> Customers always want/buy/can afford/justify to their shareholders
> items/services that are the cheapest, most effective and speedily
> available.
>
I think that is a worthwhile goal. (Whether it is actually achievable or not 
is quite another matter :-))

> Employees want as much money as possible for as little effort as
> possible in congenial surroundings.

Some certainly do... others are more realistic... others again are actually 
happy to work and find making an effort brings rewards of a different 
nature. Not everyone is as shallow as you suggest.

>
> Employers want as much work as possible for as little money as
> possible in the cheapest facilities practical.
>

See response immediately above. There are good and bad employers.

> If you pay peanuts you get monkeys
>
Not necessarily; I have worked with some very bright people who were paid 
peanuts. They may have motivations other than money for working where they 
do.

> If a million monkeys spent a thousand years bashing away on
> typewriters, one might write the works of Shakespeare (some might say
> that one did, only he didn't use a typewriter, I don't know what his
> handwriting was like, but I work in the NHS).

It might take more than a million and longer than the age of the Universe... 
probably better to leave it to Will... :-)
>
> Many programmers and probably analysts wrote most of their programs
> online with two fingers.  Managers paid them to do it like that.  I
> wrote much of mine like that too.

I cannot recall ever being told to type with two fingers as a requirement 
for receiving a paycheck.... :-)

Our experience differs here, apparently.
>
> Employers and employees are often unwilling (can not afford) to invest
> time and money in training to use software and equipment to best
> advantage.

Employers should allocate a percentage fo profit for re0investment in 
training (wise ones do...)

Employees should not let anything as important as the skill sets with which 
they will earn a living, be dependent on someone paying for their training. 
In other words, if you lose the yearning for learning and justify this with 
"Well, they won't pay for my training..." you deserve whatever you get. 
These days you can acquire VERY valuable skills for free; all it takes is 
time and effort. Attitude again.

Have a look at: http://www.w3schools.com/

A very large amount of the stuff I use every day, I acquired from this site. 
Java... I bought a couple of books, C#... free video tutorials online... 
There is really no excuse for people not to have marketable skills these 
days. (But there are a thousand reasons you can justify not doing so :-))
>
> No one gets a job for life anymore and many didn't anyway.

Interesting you should say that. I came to this conclusion in 1975 and have 
worked as a freelance ever since then.Many of my friends thought I was crazy 
to give up the "security" of full time employment. (I came to the conclusion 
this was always an illusion when I saw good people getting fired when it 
suited the company, even after twenty years of faithful service... Sometimes 
this was not malevolence on the part of the company, just simple economics 
and survival.)  I endorse your statement 100%. Time has shown it to be true.
>
> Employers are mostly in no position to promise a job for life.

Yep, neither should they. If we all took a bit more responsibility for 
ourselves we wouldn't need "Nanny" employers or Governments to wipe our 
noses for us...


>
> Restrictive practices and agreeing to inappropriate contract terms.

Don't do it. I cross out the ridiculous clauses in the contract before 
signing it. If they don't like it (and usually they don't) I just say, 
"Sorry, I can't agree to that." By this time I've had the interview and the 
employer is waiting for me to start Monday. I've never had a pimp yet, who 
wouldn't buckle... they don't relish explaining to their customer that I 
dropped out because of unfair and restrictive practises in their contract. 
Even if they didn't cave, I wouldn't go to a place where I had signed a 
restrictive contract. The answer to getting these practises changed, is for 
more of us to resist them.

>
> The need for employers and employees to protect and invest in
> intellectual property and rights while still managing to do their jobs
> effectively with several employees and employers.

My approach to this is that they have the full rights to anything I do or 
produce for them while they are paying me, and can use it any way they see 
fit. BUT, this is a non-exclusive right. I NEVER waive my own right to my 
own IP. As for going down the road to their competitors and doing the same 
solution, that's something they just have to suck on. Maybe there's an 
incentive there for them to keep me... :-)

(If it was really critical to their competitive advantage, I'd negotiate and 
point out that not allowing me to sell my skill causes me financial 
disadvantage... Hopefully they'd take the hint. I would NOT blackmail them 
or do anything unethical that could jeopardise their position with a 
competitor, but I would certainly work for a competitor (and have done). 
Never had a problem with this, but it is certainly a grey area. These "grey 
areas" again come down to attitude. If you negotiate openly and fairly most 
issues can be resolved.)
>
> Most software written on behalf of employers was not reviewed for a
…[8 more quoted lines elided]…
> had to make such checks.

And the reason they don't is because they don't have to. If you build 
something yourself, from scratch, you are not violating anyone's software 
patent. The code you write is patently not a duplicate of their solution. 
Algorithms cannot be patented as far as I know, and even if they could, a 
simple addition of a step or modification of an existing one probably covers 
it.

>
> Twiddling thumbs furiously.
>

Never had time to do that... :-) It's like beng bored; I don't recall ever 
experiencing that either. Always something going on in my head...:-)

> Some of the programming and design standards I have seen.
>
Amen.

> Drinking at lunchtime.
>
Can be very useful...:-)

> Some of the progams and specifications that I have seen.
>
Amen.

> I have also seen some very well written specifications, programs and
> user documentation.
>
Amen.
> Cultures of working long hours.
>
…[21 more quoted lines elided]…
> nature reserve.

Ah, now THAT is time well spent... :-) I used to spend quite a bit of time 
in the Wye Valey and had friends in both Hereford and Gloucester. It is 
beautiful country and good for the soul... :-)
>
> (I tried posting this earlier but lost my connection, though it said
…[5 more quoted lines elided]…
>

Funny how time often improves things :-) (He reaches for a bottle of NZ 
Cabernet Sauvignon (2002)...there is a satisfying popping sound (Damnation 
on all screw tops)... End of message.

Pete.
> Robert
>
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-15T08:14:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176650053.507172.150730@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<58df0rF2gb7u1U1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <1176594225.920162.13260@w1g2000hsg.googlegroups.com> <58df0rF2gb7u1U1@mid.individual.net>`

```
On 15 Apr, 02:55, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
>
> > If you pay peanuts you get monkeys
…[3 more quoted lines elided]…
> do.

I always think that if you pay peanuts then you get monkeys working
for you. The more peanuts you poay then the bigger the monkey.

>
> > The need for employers and employees to protect and invest in
…[9 more quoted lines elided]…
>

You should be aware that in the UK the intellectual property rights
exist with the author unless a waiver has been signed. I have
previously recounted an incident where a contractor refused his
employer the right to amend code that he had written (and he got a
handsome pay cheque for the IP rights). I doubt that many employers
realise the potential problems they face if coders get officious.

I have heard of cases where companies have infringed copyright and/or
IP rights by employing people/teams to write code with matching
functionality to a competitor. Usually this appears to be a case of
using code filched from the competitors' application but it can also
be where the employer has seen the competitors' code and
unintentionally writes the same code in subroutines. To avoid that
particular problem, companies often specifically employ people/teams
that have not had sight of the competitors' code.

I have signed a waiver to IP rights before now simply on the principle
that I doubted that I would ever want to be associated with the
application. Strangely, it is the only system upon which I have worked
that I know is still running.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-15T01:30:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<evrv6s$na5$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net>`

```
In article <58amj3F2fva6gU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>But, and this is 
>the important point, there are also people in corner offices who are doing 
…[4 more quoted lines elided]…
>with the same brush as COIs.)

Mr Dashwood, I waited a bit to respond to this... and I'll try to be as 
plain as possible about it.

My views may be tainted by my position, after putting in my mandatory 'two 
years' I fell/lied my way into a consulting/contracting/hired gun job... 
and I've held those for the decades since.  I'm hired - usually - to do a 
job and not much else.

Likewise... if the precept is, almost Hippocratically, 'First, Do Your 
Job' then it doesn't matter if the people are 'doing the very best they 
can' or 'first to arrive and the last to leave, dedicated company people 
who put their heart and soul into their jobs'; what matters is, quite 
simply, Can They Do Their Jobs?

If they cannot then there might be many reasons for this... one is 'they 
are incapable of doing their jobs'.  If that is the case then to present 
themselves as capable and to collect a salary for a job they cannot do is, 
to my eyes, fraud and theft... in the same way as if I were to represent 
myself as skilled in Java and .NET and other stuff I don't know.  

Yes, I exaggerated my skills for a short while a few decades back... and I 
got away with it and the statute of limitations for such has, I believe, 
expired.  A difference in quantity, however, may make for a difference in 
quality - drop a pennyweight from waist-height onto someone's foot and 
things more-or-less keep going on as they did, drop a rock weighing a few 
stone in a similar manner and someone might be crippled for life - and for 
someone to go to work year after year, decade after decade, being able 
only to 'do their best' or 'show up first/leave last' when their job is 
the allocation, co-ordination and motivation of personnel and resources 
towards the accomplishment of a stated Executive goal means that (by this 
definition) they are not capable of doing a Manager's job.

To expect consistent and repetitive fraud and theft to be met with the 
kind of tolerance, generosity and openness-of-spirit you seem to be 
espousing just might be, perhaps, beyond the capabilities of many folks... 
myself, maybe, included.

Can you Do Your Job?  Good... then do it.  Are you incapable of Doing The 
Job that you have been assigned?  Do not accept the assignment... I've 
turned down contracts many times with 'Sorry, my skill-set doesn't include 
that', no shame involved.  If you must accept the assignment - and I don't 
know of too many folks who get told 'be a manager or you'll be fired' then 
let it be known, loud and clear, in writing that your skill-set does not 
include what is needed to accomplish the task.

Of course... in my experience it doesn't work that way.  The variant of 
Sturgeon's Law that I apply to folks in *any* job - butcher, baker, 
candlestick-maker, doctor, lawyer, cook from New Dehli - is that 10% of 
the folks doing that job have what I call 'the touch'... an instinctive, 
intuitive grasp of what needs to be done and a delight in Doing It 
Right... and the other 90% are busy praying '*Please* don't let me get 
found out'... and, at times, busy making sure that nobody around them is 
competent enough to see what frauds they are; I believe I've mentioned a 
sort of 'Gresham's Law of Management' previously.

I'm not really sure how to wind this up in a memorable fashion... decades 
on back I did my Basic Training for the United States Air Force Reserves 
in the 3701st Basic Military Training Squadron at Lackland Air Force Base 
in San Antonio, Texas, USA... got a tattoo on the one day they allowed us 
a Town Pass, but that's another story... anyhow, the motto of our squadron 
was a simple 'Lead, Follow or Get Out Of The Way'.

Can one allocate, co-ordinate and motivate (etc, see above)?  Good, then 
be a Manager.

Can't do that?  Stand back, then, and be allocated and co-ordinated... 
motivate yourself by the quality of your work.

Can't do either?  Don't hinder folks who are just trying to Do Their Jobs.

Lead, Follow or Get Out Of The Way.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-15T14:44:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58dhrlF2fvfrkU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <evrv6s$na5$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:evrv6s$na5$1@reader2.panix.com...
> In article <58amj3F2fva6gU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[82 more quoted lines elided]…
> Lead, Follow or Get Out Of The Way.

It's a good motto.

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-16T12:57:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net>`

```
On Sat, 14 Apr 2007 12:46:46 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I am getting a bit tired of certain people here ALWAYS seeing the trouble as 
>being caused by management so, if I defend that point of view, it  is 
>because of that. I don't like unbalanced assessments.

Management is the easy target - it's either them or us, and they get
paid much more, and have the power to fire us.  8^)

>There ARE bad managers, just as there are crap programmers. Both varieties 
>make life tiresome for those of us who just want to do a job as well as we 
>know how, and get some satisfaction from it.

Ane *everybody* screws up, often without anything they can do about
it.   (Which is why crime doesn't pay - eventually a screw up will
happen, and that's when criminals will pay).

I like the purpose of the design of sidewalks - with built in places
where they're supposed to fail.    Good design doesn't assume
perfection - good design minimizes the effects of mistakes.

A bad design is our current password system that assumes people won't
act like people.

My wife was complaining about some minimum wage workers who were
incompetent for their jobs.   I asked her - what should these people
be doing?    We can't force competency.   We could bribe them to stay
out of the workforce with more taxes to pay for more welfare - but
then we would have to pay much more to keep the competent people
serving burgers.

>When every programmer and staff member in the company is saintly and without 
>fault, when these perfect superior people are NEVER wrong and ALWAYS right, 
>THEN, I might agree they have the right to denigrate the people who manage 
>them (be they idiots or saints). 

We can't wait for a perfect citizen to vote out incompetent leaders,
and they can't wait until they are perfect to get rid of incompetent
workers.    (I'm more afraid of the Righteous than of those who
recognize their limits).

We can be considerate and understanding though.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-16T23:02:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f00v9i$6fl$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com>`

```
In article <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>My wife was complaining about some minimum wage workers who were
>incompetent for their jobs.   I asked her - what should these people
>be doing?    We can't force competency.

Leaving aside the question of 'who hired the incompetents?' - which, of 
course, places the blame on Management - I would ask 'what is there that 
encourages/rewards anything other than the 'some pretend to work while 
others pretend to pay them' mentality?'... which brings into question the 
entire Corporate Structure of Labor, Management and Executive groups.

(my Sainted Paternal Grandfather - may he sleep with the angels! - used to 
say, long before things like Career Ladders and Empowerment were ever 
buzzwords, 'you can tell who gets a piece of the till by the way they 
move')

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-17T13:15:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58ileeF2h630jU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com> <f00v9i$6fl$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f00v9i$6fl$1@reader2.panix.com...
> In article <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[19 more quoted lines elided]…
>

I don't see "Empowerment" as a buzzword (but that might be because I'm 
wearing my Manager hat as I write this:-)). I think it is really important 
to give people the "space" to make decisions and accept responsibility, 
always providing support for that process, and guidance if they ask for it. 
My experience has been that people grow when this happens and can then take 
more responsibility, and so on. (Ultimately, I'd like to get everybody doing 
my job for me, so I can just collect my cheque and say hello occasionally... 
:-) Hasn't happened yet, but I live in hope...)

I think your Grandaddy was right about the change in walk of those who have 
a piece of the till; I know I walk differently when a dividend cheque or 
Bond payment arrives :-) The spring in my step soon dissipates when the 
bills come in... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-04-17T09:18:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f023cb$l1e$1@reader2.panix.com>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com> <f00v9i$6fl$1@reader2.panix.com> <58ileeF2h630jU1@mid.individual.net>`

```
In article <58ileeF2h630jU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f00v9i$6fl$1@reader2.panix.com...

[snip]

>> (my Sainted Paternal Grandfather - may he sleep with the angels! - used to
>> say, long before things like Career Ladders and Empowerment were ever
…[6 more quoted lines elided]…
>always providing support for that process, and guidance if they ask for it. 

Any job requires both responsibility and authority to accomplish... if you 
want the floors swept the sweeper needs enough authority (in terms, say, 
of a key to the door-lock) to get the broom out of the closet.

Archimedes said 'Give me a lever long enough and a place to stand and I 
will move the world'... likewise, give someone the tools and support and 
let the do their jobs.

[snip]

>I think your Grandaddy was right about the change in walk of those who have 
>a piece of the till; I know I walk differently when a dividend cheque or 
>Bond payment arrives :-) The spring in my step soon dissipates when the 
>bills come in... :-)

It is not only when the payment comes in... someone who has a piece of the 
till learns that what they do affects what winds up in their pocket.  They 
look for things, they tend to things in a way that someone whose paycheck 
is the same 'no matter what' usually does not.

DD
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 14)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T06:13:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176901981.503200.294630@b75g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<58ileeF2h630jU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com> <f00v9i$6fl$1@reader2.panix.com> <58ileeF2h630jU1@mid.individual.net>`

```
On 17 Apr, 02:15, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:f00v9i$6fl$1@reader2.panix.com...
> > In article <37h7235mfp72i68g1vc2dv7hatkjh56...@4ax.com>,
…[29 more quoted lines elided]…
>

Yea Gods! We agree on something!

>
> Pete.- Hide quoted text -
>
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-17T13:06:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58ikslF2govvaU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <1175713257.593859.110760@n59g2000hsh.googlegroups.com> <ev2gd1$ov7$1@reader2.panix.com> <1176138034.214060.257610@q75g2000hsh.googlegroups.com> <eve0f5$lsf$1@reader2.panix.com> <58014tF2f874sU1@mid.individual.net> <1176405267.687547.144160@q75g2000hsh.googlegroups.com> <58961sF2ftvphU1@mid.individual.net> <1176480052.803028.87680@p77g2000hsh.googlegroups.com> <58amj3F2fva6gU1@mid.individual.net> <37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:37h7235mfp72i68g1vc2dv7hatkjh56ukf@4ax.com...
> On Sat, 14 Apr 2007 12:46:46 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[43 more quoted lines elided]…
> We can be considerate and understanding though.

Fair comment. I have nothing more to add :-)

Pete.
```

#### ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-04T16:13:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57gmudF2cqvorU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com>`

```

"DaveM" <renfrew76@xemaps.com> wrote in message 
news:1175626528.510733.311750@n59g2000hsh.googlegroups.com...
> We are using Micro Focus Net Express 4.0 and Microsoft SQL Server
> 2000.  The concepts/examples we are seeking however can be more
…[12 more quoted lines elided]…
>
Fair enough.

> The second problem involves how to handle record locking issues among
> multiple users.  The lead analyst wants us to code logic that requires
…[8 more quoted lines elided]…
> it.

Yes, this was fairly normally practice once upon a time. I remember using it 
in 1978 on the first IBM 3790 deployment in the UK. This was to be a 
"distributed application" that was to be "Networked" (Cutting edge stuff at 
the time... We were given a very thick Assembler manual and told to learn 
it. A week later we were writing applications, which had to be Assembled and 
run on a mainframe because there was no hardware available yet :-)). There's 
nothing wrong with date/timestamping rows on an RDB, even today, but not for 
the reasons your Lead Analyst wants to do so. Nowadays it serves as an audit 
trail, rather than a locking or rollback/recovery device.

You are absolutely correct in that your DBMS (SQL Server) can manage its own 
transaction isolation, rollback and recovery. Perhaps the Lead Analyst needs 
to do a quick course on modern Database Management?

>
> Here is a simple/fictitious representation of the type of code
…[3 more quoted lines elided]…
> 1. Open rdb

That would be a CONNECT...

> 2. EXEC SQL WHENEVER SQLERROR DO sql_error;
> 3. Accept record key from user
> 4. Read matching record  w/ shared lock (presume REC-FOUND for this
> example)

Despite the ISAM terminology, you are simply requesting a row. Don't worry 
too much about the locking; the advantage of a DBMS is that it takes much of 
this concern off you, and, at this point it doesn't matter anyway.

> 5. Display fields on screen
> 6. Accept field updates from user
…[3 more quoted lines elided]…
> 9. Read record from table with exclusive lock

Get a row, with update intent.

> 10. Move new field values to table
> 11. Rewrite table record

That would be an UPDATE... :-)

> 12. COMMIT
> 13. END TRANSACTION (ONLY if it is a distributed transaction and will use 
> MS Transact-SQL to access distributed servers)
> 14. Close rdb

No, we don't close the database; other people are using it... :-) Instead we 
might DISCONNECT from it.
>
>
…[5 more quoted lines elided]…
>

In fact, you could use almost exactly the same algorithm you did above for 
the transaction bit, but without the connection and disconnection, so....

1. establish a connection.
2. start a transaction. (ONLY if it is a distributed transaction and will 
use MS Transact-SQL to access distributed servers)
3. read your batch input and get a key and data for the update.
    These must be loaded into Host Variables in your WORKING-STORAGE SECTION 
(See DECLARE in your SQL manual)
    Set a count somewhere of the records you have read. You will use this to 
issue a COMMIT after say, 500 updates.

4. issue an UPDATE something like this:

(Sample of COBOL with embedded SQL...)

PROCEDURE DIVISION.
...
EXEC SQL
     UPDATE ourTable
          SET dataColumn1 =  :field-1 (from the batch record. Note that Host 
Variables start with a special character which can
                                                        vary across 
environments. Try using a colon...)
                  dataColumn2 =  :field-2
                  dataColumn3 =  :field-3
                  dataColumnN = :field-N
                  ...
         WHERE ourTableKey =  :Batch-record-key

END-EXEC

if function REM (input-rec-count  500) = zero
       EXEC SQL
            COMMIT WORK (OR COMMIT TRANSACTION if you are running 
distributed servers using Transact-SQL)
       END-EXEC
       (Start a new transaction at this point if you are accessing 
distributed servers. If you are not, SQL Server automatically 
assigns a transaction where one is needed and you don't need to worry about 
it.)
end-if

...

5. When you have hit EOF on your batch file, do the final COMMIT and then 
DISCONNECT.

>
> Perhaps there is a site somewhere that includes sql-related coding
> examples?

Most people are a bit cagey about publicising their code :-)

Try the following:

http://developer.mimer.com/interfaces/interface_5.htm
http://www.pdc.kth.se/doc/SP/manuals/db2-5.0/html/db2a0/db2a002.htm

> I appreciate in advance any input that anyone may have
> about how we should be approaching this data conversion effort.

Now THAT's an entirely different matter...   If you are looking for free 
strategic advice, what you get is probably worth the price...:-)

Having done a number of successful conversions from COBOL file system to 
RDBMS, built tools to automatically analyse COBOL File Definitions and 
generate RDB equivalents in third normal form with all repeating groups, 
foreign keys, constraints and indexes carried over, and having worked with 
RDB since the second IBM course on them in Reading, England, in 1983, I have 
a nodding acquaintance with the problems you are facing.

(However, I have never loaded 60 million records to a database so I must 
state that caveat up front...)

If you were to ask for my advice (and pay for it) I can tell you that I 
could not, in all conscience, recommend what you are doing.

Given the stated environment (SQL Server) you are utilising a tiny fraction 
of what is available to you. It's a bit like buying a Ferrari and never 
getting out of first gear...

Embedded SQL is not the way to go.

Have a look at ADO.Net (this is not the same as ADO; it is light years 
ahead). You would do much better embedding ADO.Net calls against your SQL 
Server DB. This allows data and table adapters, automatic binding to 
datasources, processing result sets with a single command, and manipulating 
SETS of data rather than a row at a time.It is also makes MUCH less 
connection demand on the server, so overall throughput is improved.)

Here's an overview:
http://www.developer.com/net/vb/article.php/10926_1540311_1

(Ironically, because it can employ Reader objects, this approach MAY use 
OPEN, BEGIN... and CLOSE... :-))

I have not used it from COBOL (I use C#), but I see no reason why it 
couldn't be called from COBOL as a normal COM server. I must have a go at 
this when I get some time...:-)

However, given the realities of your current situation, embedded SQL is 
probably what will happen.

If you need help with it, post here.

Good luck.

Pete.
```

##### ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "DaveM" <renfrew76@xemaps.com>
- **Date:** 2007-04-04T11:45:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1175712344.282357.44480@w1g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<57gmudF2cqvorU1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <57gmudF2cqvorU1@mid.individual.net>`

```
Pete,

Your response was VERY helpful, and I am grateful to you for taking
the time and patience to put it together.  We will check out the sites
you recommend, and I will pass along all of your suggestions and
examples to my team as well as management.

Also, please forgive me if I misspoke in my final para, as I would
never presume the right to ask anyone for the favor of writing me up
an entire detailed game plan on how we should carry out the whole
conversion project.  The kind of information that I meant to ask for
is what you have indeed since given me, and I thank you!

Dave Miner
```

###### ↳ ↳ ↳ Re: Conversion of data & associated logic from ISAM to RDB

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-05T11:59:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57isfjF2d4i06U1@mid.individual.net>`
- **References:** `<1175626528.510733.311750@n59g2000hsh.googlegroups.com> <57gmudF2cqvorU1@mid.individual.net> <1175712344.282357.44480@w1g2000hsg.googlegroups.com>`

```

"DaveM" <renfrew76@xemaps.com> wrote in message 
news:1175712344.282357.44480@w1g2000hsg.googlegroups.com...
> Pete,
>
…[8 more quoted lines elided]…
> conversion project.

Nothing to forgive... :-) I understood what you were requesting. You just 
gave me an opportunity to point out that the conventional wisdom to use 
embedded SQL is not necessarily the best solution. A whole raft of new 
techniques for data access and manipulation are starting to filter through 
to the mainstream and the next couple of years will see some major changes 
in the way we access data, particularly on PC platforms. By advising the use 
of ADO.Net I am ensuring you at least are on the playing field for this 
stuff.

SQL Server is a good choice, although I don't know of any current RDBMS that 
are actually "bad". DB2, Ingres, Oracle, and even MySQL (which is free; your 
management should love that :-)) I have found to be completely adequate 
systems. I have one system that uses MySQL and SQLServer together and it all 
works fine. (It evolved that way... when I first started building it I 
couldn't afford SQL Server :-) Later, I added some components that used SQL 
Server and thought... I'll get round to "unifying" it some time... That was 
four years ago... :-))

The kind of information that I meant to ask for
> is what you have indeed since given me, and I thank you!
>
> Dave Miner
>
Thanks for the acknowledgement (You'd be surprised how many people here 
never even reply or let us know whether what was posted was useful...).

I imagine you have completed the conversion of your ISAM data structures to 
Databases, and are now seeking to load them. In case you haven't, I have a 
tool I wrote some years back that can automate that process. (ISAM2RDB). You 
feed it your ISAM COBOL definition (Source code) and it creates a Relational 
Database in third normal form.  It builds linked tables for repeating groups 
(COBOL OCCURS) and also copes with REDEFINES in the COBOL source.

I also have a Declaration Generator tool I wrote that will analyse a table 
on a RDB and generate a COBOL record definition for interfacing to it. This 
is the same facility provided by DECLGEN in IBM mainframe environments. It 
actually can go one step further than generating a COPY book to include in 
your COBOL, by also generating a COBOL access module that can mainatain the 
table (INSERT, UPDATE,  SELECT *, and DELETE) so that programmers with no 
knowledge of SQL can still access and update the database, but are shielded 
from the details. The source code generated is COBOL with embedded SQL, and 
can be useful as a learning aid while people are learning SQL.

Given that your management are not prepared to spend money on training 
(which SHOULD be their top priority), it is highly unlikely they'll spend 
any on tools :-), however, as I wrote these things many years ago when first 
looking at converting to RDBMS, and as I am moving away from Embedded SQL 
(ESQL)   the value of these tools to me now is pretty low. If you are 
interested, I can let you have a free demo... send me some COBOL ISAM 
definitions and I'll return you an ACCESS DB generated by the tools (this is 
easily exportable to SQL Server, but takes less space for mailing.)

I have some stuff going on at the moment that is occupying my time and 
effort but I hope within the next month or so to have a Web site up that 
will offer certain facilities as a Web Service. (Now that I've cracked 
getting COBOL COM and DCOM+ components to run as a Web Service... :-)). I 
guess I could put these tools up there too, and people could then use them 
remotely on an "as needed" basis... or maybe I'll just take a break :-)


Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
