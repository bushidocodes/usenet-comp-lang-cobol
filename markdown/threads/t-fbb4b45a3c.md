[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL DB2 PROBLEM

_4 messages · 3 participants · 1999-08_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL DB2 PROBLEM

- **From:** "Calatis" <nmourapires@mail.pt>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ptu8u$rnu$1@pthp35.telecom.pt>`

```
Hello,

How can i call, from a cobol program, an aplication that runs under DB2 to
execute my SQL statements. This aplication requires an input file (sql code)
and an output file (result of the sql).

It is possible to do this?

Thanks in advanced.
```

#### ↳ Re: COBOL DB2 PROBLEM

- **From:** Juergen@bop99.ping.de (Juergen Vetter)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7NUaV-mWOtB@bop99.ping.de>`
- **References:** `<7ptu8u$rnu$1@pthp35.telecom.pt>`

```
nmourapires@mail.pt meinte am 24.08.99
zum Thema "COBOL DB2 PROBLEM":

> Hello,
>
…[4 more quoted lines elided]…
> It is possible to do this?

sure!

Your compiler must have a preprocessor or must communicate with the  
preprocessor of your db-system.

We use today the Microfocus/Merant Cobol Workbench 4.0.26 with IBM DB2 2.1.2.
Merant NetExpress 3.0 with IBM UDB 5.x works also fine and we want to use it  
in the future because the old applications are no longer supported.

The sql-statements are in the cobol-sourcecode.

example
-------
"open a cursor with declare-statement"

002517 V05-OEFFNE-EG-CURSOR SECTION.
002518*    ***********************************************************
002519*    * OeFFNET EINEN CURSOR ZUR CROSSREF-TABELLE VKA14030      *
002520*    * ES WERDEN ALLE EG"S MIT VETRAGSNUMMER SELEKTIERT        *
002521*    ***********************************************************
002522 V05A.
002523D    DISPLAY K-PROG-NAME ": V05A"
002524     MOVE "V05A"                 TO  TXT-LABEL
002525*------------------------------------- SQL STARTEN
002526     EXEC SQL
002527
002528        DECLARE EG_CURSOR CURSOR FOR
002529
002530        SELECT
002531              RFRN_INZ_VER_ID
002532             ,NUM_PNR
002533             ,CHAR(DATE_EG_ENDE,EUR)
002534
002535        FROM
002536              VKA14030
002537        WHERE
002538              RFRN_INZ_ID_VTRG = :VKA14030-HS.RFRN-INZ-ID-VTRG
002539
002540     END-EXEC.
002541*------------------------------------- CURSOR OeFFNEN
002542     EXEC SQL
002543
002550        OPEN EG_CURSOR
002560
002570     END-EXEC.
        .....

Fetch the Cursor:
-----------------
028800 V10-FETCH-EG-CURSOR SECTION.
002890*    ***********************************************************
002900*    *   LIEST ZEILEN AUS DEM CURSOR ZUR EG-TABELLE            *
002910*    *   UND KOPIERT DIE ZEILEN IN DIE HOSTSTRUKTUR.           *
002920*    *                                                         *
002930*    ***********************************************************
002940 V10A.
002950D    DISPLAY K-PROG-NAME ": V10A"
002960     MOVE "V10A"                 TO  TXT-LABEL
002970
002980*------------------------------------- SQL STARTEN
002990     EXEC SQL
003000
003010         FETCH EG_CURSOR
003020
003030         INTO
003040              :VKA14030-HS.RFRN-INZ-VER-ID
003050             ,:VKA14030-HS.NUM-PNR
003051             ,:VKA14030-HS.DATE-EG-ENDE
003060
003070     END-EXEC

In this example the sqlcode is embedded in
EXEC SQL END-EXEC.

This is the same way as you do it in a mainframe environment.
The preprocessor now have to replace this statments.
The statements are replaced by api-calls.
You have to link a db2-library (for example IBM DB2 2.1.2 db2api.lib).
At compiletime you have to set som extra directives like SQL(COMMIT=1) or
DB2(COMMIT=1).

If you use the Cobol Workbench or NetExpress you have many howtos.

The result of a sql-statement is stored in host-variables like
vka14030-hs in the example. You can use this host-variables like other
cobol-variables (for example move-statement).

So you can move the informations to an output-structure and write this
into a file.

example:
--------
002091  MOVE NUM-PNR OF VKA14030-HS
002100    TO NUM-PNR OF REC-OUTPUT(NUM-ANZAHL OF REC-OUTPUT)

example host-variable Filename: VKA14150.CPY
---------------------------------------------------------------
EXEC SQL
    DECLARE VKA14150 TABLE
   (
    RFRN_OBJ_VER_ID     CHAR(38)         NOT NULL
   ,RFRN_MAND           CHAR(2)          NOT NULL
   ,NUM_VNR             INTEGER          NOT NULL
   )
END-EXEC.
01  VKA14150-HS.
  10  RFRN-OBJ-VER-ID          PIC  X(038).
  10  RFRN-MAND                PIC  X(002).
  10  NUM-VNR                  PIC S9(009) COMP.

source-code: working-storage implemetation:
-------------------------------------------
000880*    #=========================================================#
000890*    !   VKA14030 EINZELGESCH"FTSDATEN (EGST)                  !
000900*    #=========================================================#
000910
000920     EXEC SQL
000930         INCLUDE VKA14030
000940     END-EXEC.

           instead of

           COPY VKA14030
```

#### ↳ Re: COBOL DB2 PROBLEM

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824080852.06868.00003246@ng-cm1.aol.com>`
- **References:** `<7ptu8u$rnu$1@pthp35.telecom.pt>`

```
Calatis writes ...

>Hello,
>
…[5 more quoted lines elided]…
>

I'm having a little problem with your English here, so let me try to get a more
precise understanding of your question. What do you mean by "call an
application"? Normally we call a program. If that program requests DB2
services, you still simply call the program.

However, any program that uses DB2 services has to go through the DB2
preprocessor that converts "EXEC DB2..." statements to CALLs to various DB2
services; and, the original "EXEC DB2..." statements are extracted and
summarized into a DBRM (Data Base Request Module) that must be BOUND into,
ultimately, a DB2 plan.

At run time, this DB2 plan must be available along with the load module
produced from the original program. So for batch this typically means running
TSO in the batch by executing IKJEFT01 (or a variation of this) and passing
some TSO commands to setup the DB2 environment (DSN command) and then to
execute the program (RUN subcommand).

This being said, it is possible to call such a program, but the calling program
must also be run in the fashion described above.

On the other hand, if you are asking if you can call DB2 services from a COBOL
program, the answer is yes. And the program must be precompiled, compiled and
link; the output from the precopmpiler (the DBRM) must be bound; and the load
module must be run as mentioned above. Depending on other issues (such as
security / ownership) there may be other concerns to be addressed.


>Thanks in advanced.
>
>

You're welcome. Hope this helps.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: COBOL DB2 PROBLEM

- **From:** "Calatis" <nmourapires@mail.pt>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7q0dla$nf7$1@pthp35.telecom.pt>`
- **References:** `<7ptu8u$rnu$1@pthp35.telecom.pt>`

```

Thanks everyone!
You've been great help.

Nuno
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
