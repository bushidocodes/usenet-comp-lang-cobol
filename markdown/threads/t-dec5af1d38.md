[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cob compile error with EXEC SQL INCLUDE SQLCA

_10 messages · 6 participants · 2003-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** guyanglucky@hotmail.com (HG)
- **Date:** 2003-10-11T19:55:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e6bdf0.0310111855.67bad23d@posting.google.com>`

```
I have a simple cobol program using EXEC SQL, say hello.cbl

       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       DATA DIVISION.
       FILE SECTION.

       WORKING-STORAGE SECTION.

       01  TABLE-ELEMENTS.

           05  COL1 PIC X(10).
	   05  COL2 PIC X(10).
	    
           EXEC SQL 
      		INCLUDE SQLCA 
      	   END-EXEC.


       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           
	   EXEC SQL
		WHENEVER SQLERROR GOTO PROGRAM-DONE
	   END-EXEC.

	   EXEC SQL
		SELECT C1, C2 INTO :COL1, :COL2 FROM USER.TEST
 	   END-EXEC.

	   DISPLAY "Col1 = " COL1.
	   DISPLAY "Col2 = " COL2.

       PROGRAM-DONE.
           STOP RUN.

When I compile with following MF cobol command: 

cob -P -a -C "sqldb(DBNAME) sqlaccess() sqlbind() sqlformat(usa)
xopen(4) flag(vsc2)" hello.cbl

I got error message:
--------------------------------------
*  19     END-EXEC.                (0)**
*  8-S****************
*     Unknown COPY file sqlca specified
*  71-S***************             (2)**
**    PROCEDURE DIVISION missing or unknow statement
cob: error(s) in compilation: hello.cbl
---------------------------------------

---------------------------------------

Is there any place to setup enviroment to INCLUDE SQLCA so that
compiler will know? or something missing for the code.

Thanks in advance.

Hansen
```

#### ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2003-10-12T05:32:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmap15$m3q$1@titan.btinternet.com>`
- **In-Reply-To:** `<9e6bdf0.0310111855.67bad23d@posting.google.com>`
- **References:** `<9e6bdf0.0310111855.67bad23d@posting.google.com>`

```
Hi Hansen.

You need to set the COBCPY variable to the directory containing 
sqlca.cpy/sqlca.cbl .

Wiggy.
```

#### ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-12T10:53:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310120953.1530bf17@posting.google.com>`
- **References:** `<9e6bdf0.0310111855.67bad23d@posting.google.com>`

```
guyanglucky@hotmail.com (HG) wrote 

>        WORKING-STORAGE SECTION.
>        01  TABLE-ELEMENTS.
…[5 more quoted lines elided]…
>  	   END-EXEC.

You will also need the host variables in a declaration section:

         EXEC SQL BEGIN DECLARE SECTION END-EXEC.
>        01  TABLE-ELEMENTS.
>            05  COL1 PIC X(10).
> 	     05  COL2 PIC X(10).
         EXEC SQL END DECLARE SECTION END-EXEC.
```

##### ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-10-13T02:06:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031012220600.24881.00000212@mb-m17.aol.com>`
- **References:** `<217e491a.0310120953.1530bf17@posting.google.com>`

```
>From: riplin@Azonic.co.nz  (Richard)
>Date: 10/12/03 1:53 PM Eastern Daylight Time

>You will also need the host variables in a declaration section:
>
…[6 more quoted lines elided]…
>

Doesn't he have to give the table?

EXEC SQL
     the table declgen
END-EXEC

Host variables C01 and C02 are ok as he had them (unless there is something
different in the PC world from the mainframe in this respect).

One declares cursors...

EXEC SQL
   DECLARE COLCSR CURSOR FOR
        SELECT C1,
                     C2
        FROM USER.TEST
        Where statements if needed
END-EXEC

This is if there would be more than one row that can fullfill his SELECT.

Then he'd have the FETCH the cursor.

EXEC SQL
   FETCH COLCSR
   INTO :COL1,
           :COL2
END-EXEC

Eileen
(who has been cursing cursors for the last week)
```

###### ↳ ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-10-13T03:51:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ejpib.42748$Pd.881124@twister.tampabay.rr.com>`
- **References:** `<217e491a.0310120953.1530bf17@posting.google.com> <20031012220600.24881.00000212@mb-m17.aol.com>`

```

"YukonMama" <yukonmama@aol.com> wrote in message
news:20031012220600.24881.00000212@mb-m17.aol.com...
> >From: riplin@Azonic.co.nz  (Richard)
> >Date: 10/12/03 1:53 PM Eastern Daylight Time
…[15 more quoted lines elided]…
> END-EXEC

Depends how strict you are on compiling.  If you don't declare the table you
don't get a RC=0 but rather a RC=4 (on MVS w/DB2 anyhow).
If you have code reviews I always think you should "justify" or "explain"
warnings.  In other words, I always recommend declaring the table and using
them for host variables accessing the data.

JCE
```

###### ↳ ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA [OS390 / DB2]

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-10-13T13:00:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Olxib.43058$Pd.915977@twister.tampabay.rr.com>`
- **References:** `<217e491a.0310120953.1530bf17@posting.google.com> <20031012220600.24881.00000212@mb-m17.aol.com> <ejpib.42748$Pd.881124@twister.tampabay.rr.com>`

```
Sometimes my lack of clarity astounds me...

If you use a DCLGEN, it includes a Table declaration and the host variable
structure

******************************************************************
* DCLGEN TABLE(dbsys.TABLEV)
*        LIBRARY(yourlib.DCLGEN(TABLEC))
*        ACTION(REPLACE)
*        LANGUAGE(COBOL)
*        QUOTE
* ... IS THE DCLGEN COMMAND THAT MADE THE FOLLOWING STATEMENTS
******************************************************************
     EXEC SQL DECLARE TABLEV TABLE
     (
       TABLE_NAME                   CHAR(20) NOT NULL,
     ) END-EXEC.
******************************************************************
* COBOL DECLARATION FOR TABLE D2.CTLPGMV                         *
******************************************************************
 01  DCLTABLEV.
     10 TABLE  PIC X(20).

If you do no use the declare table and have just host variables for your
COBOL program you get a precompile **warning.**

DSNH206I W     DSNHANAL LINE 966 COL 14  STATEMENT REFERENCES COLUMN "TABLE"
DECLARE TABLE_CURSOR CURSOR FOR SELECT TABLE FROM TABLE A

I don't know what happens that is bad to warrant a warning - so I declare it
and get RC=0 :-)

With regards to  EXEC SQL dclgen END-EXEC

You don't need it.  It's often advised as it can be recreated with table
changes.  It doesn't matter as long as you have the correct data types for
the sql statements declared.
01 DCLTABLEV
     05 TABLE PIC X(20).

Is not necessary if you choose to use:
01 MY-OWN-HOST-VAR  PIC X(20).

JCE

"jce" <defaultuser@hotmail.com> wrote in message
news:ejpib.42748$Pd.881124@twister.tampabay.rr.com...
>
> "YukonMama" <yukonmama@aol.com> wrote in message
…[20 more quoted lines elided]…
> Depends how strict you are on compiling.  If you don't declare the table
you
> don't get a RC=0 but rather a RC=4 (on MVS w/DB2 anyhow).
> If you have code reviews I always think you should "justify" or "explain"
> warnings.  In other words, I always recommend declaring the table and
using
> them for host variables accessing the data.
>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA [OS390 / DB2]

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-13T11:47:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310131047.2457ddbc@posting.google.com>`
- **References:** `<217e491a.0310120953.1530bf17@posting.google.com> <20031012220600.24881.00000212@mb-m17.aol.com> <ejpib.42748$Pd.881124@twister.tampabay.rr.com> <Olxib.43058$Pd.915977@twister.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote

> If you use a DCLGEN, it includes a Table declaration and the host variable
> structure
…[7 more quoted lines elided]…
> COBOL program you get a precompile **warning.**

This seems to be specific to particular databases and precompilers
rather than being standard SQL.  In fact it seems to be mostly
redundant and used only for checking purposes within the precompiler.
My embedded SQL(s) don't allow it.

> You don't need it.  It's often advised as it can be recreated with table
> changes.  It doesn't matter as long as you have the correct data types for
> the sql statements declared.

Certainly there may be a problem if the FETCH is into a record and the
table has been changed.  I usually specify the table fields and the
host variables specifically rather than use a group variable, but this
is just as much a problem.

For PostgreSQL I can generate Cobol record areas from the table using
a simple Python program which is roughly what DCLGEN does.
```

###### ↳ ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA [OS390 / DB2]

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-10-16T03:14:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031015231429.23480.00000249@mb-m16.aol.com>`
- **References:** `<Olxib.43058$Pd.915977@twister.tampabay.rr.com>`

```
>From: "jce" defaultuser@hotmail.com 
>Date: 10/13/03 9:00 AM Eastern Daylight Time

>
>With regards to  EXEC SQL dclgen END-EXEC
>
>You don't need it. 


These are always included in our programs with the statements in a copybook.  I
can't remember every coding a DB2 program without this. In this shop or
previous ones.

I may try it just to see what kind of errors I get.  I will put in the host
variables though :)
```

###### ↳ ↳ ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-12T22:24:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310122124.7bb901f4@posting.google.com>`
- **References:** `<217e491a.0310120953.1530bf17@posting.google.com> <20031012220600.24881.00000212@mb-m17.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote 

> Doesn't he have to give the table?

The table is specified in the SELECT.
 
> EXEC SQL
>      the table declgen
> END-EXEC

It is probably most useful to have a COPY for the table, I generate
these from the table itself using a Python program because this can
introspect the table.
 
> Host variables C01 and C02 are ok as he had them (unless there is something
> different in the PC world from the mainframe in this respect).

They _might_ be OK, it depends on what the table has been created as. 
It also depends on the version of Cobol and/or pre-processor.  eg
Fujitsu 4 insists on having each host variable as 01 or 77 level and
varchar as having two 49 levels for the size and text.

> One declares cursors...
> [...]
> This is if there would be more than one row that can fullfill his SELECT.

As you say, if there is more than one row then a cursor is likely to
be required. It also needs a CONNECT and a DISCONNECT.  He has some
way to go.
```

#### ↳ Re: cob compile error with EXEC SQL INCLUDE SQLCA

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-10-15T08:32:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3483901.1066221172@dbforums.com>`
- **References:** `<9e6bdf0.0310111855.67bad23d@posting.google.com>`

```

SQLCA  means  Comunication Area



some cobol vendors  like Fujtisu doesnt implemment  this SQLCA, the  you
must  Declare  SQLSTATE  pic x(05)  to

check Status from SQL operation.



Carlos Lages



http://docs.hp.com/hpux/onlinedocs/36217-90161/36217-90161.html



this site  you have  nore information how  to use SQLCA, if and  only if
you cobol  has this feature
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
