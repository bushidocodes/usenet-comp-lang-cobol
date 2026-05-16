[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC and Cobol

_2 messages · 2 participants · 2002-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC and Cobol

- **From:** "Adi" <w_kusch@t-online.de>
- **Date:** 2002-09-08T00:00:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aldt0f$il7$07$1@news.t-online.com>`

```
Hello!
I am a newbie ;). I try to coonect with a MS-Access-DB via COBOL (NetCobol,
ConsoleApplication), but I get a error massage:
 *** Error: 'Fujitsu.COBOL.COBOLRuntimeException' in
fujitsu.cobol.runtime.programcontrol.netmodule.
        JMP0371I-U [PID:00000da0 TID:00000f24]  ENVIRONMENT INFORMATION FILE
ERROR TO PERFORM SQL. '@ODBC_Inf'.         PGM=CobolTestApp.Program1***

My code:

WORKING-STORAGE SECTION.
.....
EXEC SQL BEGIN DECLARE SECTION END-EXEC.
01 SQLSTATE PIC X(5).
EXEC SQL END DECLARE SECTION END-EXEC.

PROCEDURE DIVISION.
EXEC SQL CONNECT TO 'WEBGINE' END-EXEC.
EXEC SQL DISCONNECT ALL END-EXEC
....


In file "cobol85.cbr":

[CobolTestApp.Program1]
@ODBC_Inf=C:\.............\Cobol\CobolTestApp\OdbcInfo.inf





In file "OdbcInfo.inf":

[SERVER LIST]
WEBGINE=WEBGINE
[WEBGINE]
@SQL_DATASRC=OfficeControl
@SQL_USERID=
@SQL_PASSWORD=
@SQL_ACCESS_MODE=READ_ONLY
@SQL_COMMIT_MODE=MANUAL
@SQL_CONCURRENCY=READ_ONLY
@SQL_ODBC_CURSORS=USE_DRIVER
@SQL_QUERY_TIMEOUT=0


How I can create a connection without an error?
Many thanks .
Regards,
Adi
```

#### ↳ Re: ODBC and Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-09-09T13:38:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0209091238.4892ffd2@posting.google.com>`
- **References:** `<aldt0f$il7$07$1@news.t-online.com>`

```
"Adi" <w_kusch@t-online.de> wrote 

> In file "cobol85.cbr":
> 
> [CobolTestApp.Program1]
> @ODBC_Inf=C:\.............\Cobol\CobolTestApp\OdbcInfo.inf

I found that it needed this to be in the environment rather than in
the run time settings file:

SET @ODBC_INF=C:\...\ODBCInfo.inf
run program

You may need to add this to autoexec.bat to reserve environment space.
 I usually have a space holder in autoexec.bat that does:

SET ZZZ1=ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
SET ZZZ2=ZZZZZZZZZZZZZZZZZZZ ..

Then later do: 

SET ZZZ1=
SET ZZZ2=

which then leaves unused and reusable space for new settings.

Also, use program SQLODBCS to set the inf file, especially an encoded
password.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
