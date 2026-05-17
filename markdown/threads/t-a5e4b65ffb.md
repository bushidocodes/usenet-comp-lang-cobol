[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ERROR Again: Error 173 with DLLs

_5 messages · 3 participants · 1997-04_

---

### ERROR Again: Error 173 with DLLs

- **From:** "stefan schreyer" <ua-author-16657536@usenetarchives.gap>
- **Date:** 1997-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE>`

```

I'm porting a big COBOL application (300 Files) with access to
MS-SQL-Server to NT. I use one EXE file 'MENUE.EXE' that calls
different DLL files, but on exiting the EXE file with STOP RUN I get
an error so that an application which calls the EXE file crashes!!!
:-(

I get error 173 (called program-file not found), the required function
is '__SQLESTPD'. In which lib is this function and how do I solve the
problem?

If I do the same with one big EXE file (instead of using DLLs) there
is no error, but this workaround is not acceptable, too big!!!
When using GNT-Files or even in the animator there is no error, too.

I use (MF=MicroFocus):
SQL Server 6.00.121
MF Object COBOL 4.0.16
MF ESQL-Toolkit for MS SQL-Server, version 2.1

Stefan Schreyer, Oldenburg, Germany, Planet Earth
E-Mail: mailto:Ste··.@Inf··g.DE
WWW : http://www.informatik.uni-oldenburg.de/~shumway
```

#### ↳ Re: ERROR Again: Error 173 with DLLs

- **From:** "dt..." <ua-author-7376421@usenetarchives.gap>
- **Date:** 1997-04-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a5e4b65ffb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE>`
- **References:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE>`

```

"Stefan Schreyer" wrote:

Stefan -

It almost sounds like your application "thinks" that _SQLESTPD is a
PROGRAM (.EXE) verse a .DLL. In other words, it's being called
incorrectly (just a guess).

D.


› I'm porting a big COBOL application (300 Files) with access to
› MS-SQL-Server to NT. I use one EXE file 'MENUE.EXE' that calls
› different DLL files, but on exiting the EXE file with STOP RUN I get
› an error so that an application which calls the EXE file crashes!!!
› :-(
 
› I get error 173 (called program-file not found), the required function
› is '__SQLESTPD'. In which lib is this function and how do I solve the
› problem?
 
› If I do the same with one big EXE file (instead of using DLLs) there
› is no error, but this workaround is not acceptable, too big!!!
› When using GNT-Files or even in the animator there is no error, too.
 
› I use  (MF=MicroFocus):
› SQL Server 6.00.121
› MF Object COBOL 4.0.16
› MF ESQL-Toolkit for MS SQL-Server, version 2.1
 
› Stefan Schreyer, Oldenburg, Germany, Planet Earth
› E-Mail: mailto:Ste··.@Inf··g.DE
› WWW   : http://www.informatik.uni-oldenburg.de/~shumway
```

##### ↳ ↳ Re: ERROR Again: Error 173 with DLLs

- **From:** "stefan schreyer" <ua-author-16657536@usenetarchives.gap>
- **Date:** 1997-04-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a5e4b65ffb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a5e4b65ffb-p2@usenetarchives.gap>`
- **References:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE> <gap-a5e4b65ffb-p2@usenetarchives.gap>`

```

On Wed, 23 Apr 1997 16:43:12 GMT, dt··.@drs··e.com (Douglas Troy)
wrote:

› It almost sounds like your application "thinks" that _SQLESTPD is a
› PROGRAM (.EXE) verse a .DLL.  In other words, it's being called
› incorrectly (just a guess).
› 
› D.
THNX for your advice/guess. Here are further explanation for
understanding the problem:

I load my DLL with database functions (e.g. MYDB.DLL) like this:

in my COBOL EXE:
...
13 ENVIRONMENT DIVISION.
14 CONFIGURATION SECTION.
15 SOURCE-COMPUTER. SIEMENS.
16 OBJECT-COMPUTER. SIEMENS.

17******************************************************************
18 SPECIAL-NAMES.
19 CALL-CONVENTION 8 LITLINK.

20******************************************************************
21 INPUT-OUTPUT SECTION.

22 FILE-CONTROL.

23 DATA DIVISION.

24 FILE SECTION.


25******************************************************************

26 WORKING-STORAGE SECTION.


27******************************************************************

01 RC PIC S9(9) COMP-5.

28 01 LOADDLL PROCEDURE-POINTER.

29 77 KZ-LOAD PIC 9 VALUE 0.


30******************************************************************

31 LINKAGE SECTION.


32******************************************************************

33 01 PARAM1 PIC X.


34******************************************************************

35 PROCEDURE DIVISION USING PARAM1.


36******************************************************************

37 IF KZ-LOAD EQUAL 0

38 SET LOADDLL TO ENTRY "MYDB.DLL"

39 MOVE 1 TO KZ-LOAD.

40

41 CALL LITLINK "MYFUNC" USING PARAM1 RETURNING RC

42

43 EXIT PROGRAM.

44 STOP RUN.

45 END-OF-JOB.


In row 38 MYDB.DLL is loaded, in row 41 the function MYFUNC in the dll
is called. In the function MYFUNC I use calls to the MS-SQL-Server for
connecting, selecting and other stuff and these calls work!!!
AFTER the COBOL EXE terminates I get the above error!

With INT or GNT there is NO ERROR!
Funny, isn't it?

CU,
Kiwi

Stefan Schreyer, Oldenburg, Germany, Planet Earth
E-Mail: mailto:Ste··.@Inf··g.DE
WWW : http://www.informatik.uni-oldenburg.de/~shumway
```

###### ↳ ↳ ↳ Re: ERROR Again: Error 173 with DLLs

- **From:** "dt..." <ua-author-7376421@usenetarchives.gap>
- **Date:** 1997-04-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a5e4b65ffb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a5e4b65ffb-p3@usenetarchives.gap>`
- **References:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE> <gap-a5e4b65ffb-p2@usenetarchives.gap> <gap-a5e4b65ffb-p3@usenetarchives.gap>`

```

"Stefan Schreyer" wrote:

› On Wed, 23 Apr 1997 16:43:12 GMT, dt··.@drs··e.com (Douglas Troy)
› wrote:
 
›› It almost sounds like your application "thinks" that _SQLESTPD is a
›› PROGRAM (.EXE) verse a .DLL.  In other words, it's being called
…[4 more quoted lines elided]…
› understanding the problem:
 
› I load my DLL with database functions (e.g. MYDB.DLL) like this:
 
› in my COBOL EXE:
› ...
…[3 more quoted lines elided]…
›    16 OBJECT-COMPUTER.  SIEMENS.
 
› 17******************************************************************
›    18 SPECIAL-NAMES.
›    19     CALL-CONVENTION 8 LITLINK.
 
› 20******************************************************************
›    21 INPUT-OUTPUT SECTION.
 
›    22 FILE-CONTROL.
 
›    23 DATA DIVISION.
 
›    24 FILE SECTION.
 
 
› 25******************************************************************
 
›    26 WORKING-STORAGE SECTION.
 
 
› 27******************************************************************
 
›       01   RC  PIC S9(9) COMP-5.
 
›    28 01 LOADDLL PROCEDURE-POINTER.
 
›    29 77 KZ-LOAD PIC 9 VALUE 0.
 
 
› 30******************************************************************
 
›    31 LINKAGE SECTION.
 
 
› 32******************************************************************
 
›    33 01 PARAM1 PIC X.
 
 
› 34******************************************************************
 
›    35 PROCEDURE DIVISION USING PARAM1.
 
 
› 36******************************************************************
 
›    37     IF      KZ-LOAD         EQUAL     0
 
›    38        SET  LOADDLL         TO        ENTRY "MYDB.DLL"
 
›    39        MOVE 1               TO        KZ-LOAD.
 
›    40
 
›    41     CALL LITLINK "MYFUNC" USING PARAM1 RETURNING RC
 
›    42
 
›    43     EXIT PROGRAM.
 
›    44     STOP RUN.
 
›    45 END-OF-JOB.
 
 
› In row 38 MYDB.DLL is loaded, in row 41 the function MYFUNC in the dll
› is called. In the function MYFUNC I use calls to the MS-SQL-Server for
› connecting, selecting and other stuff and these calls work!!!
› AFTER the COBOL EXE terminates I get the above error!
 
› With INT or GNT there is NO ERROR!
› Funny, isn't it?
 
› CU,
› Kiwi
 
› Stefan Schreyer, Oldenburg, Germany, Planet Earth
› E-Mail: mailto:Ste··.@Inf··g.DE
› WWW   : http://www.informatik.uni-oldenburg.de/â€¾shumway

Stefan:

In your example, you had both an EXIT PROGRAM and a STOP RUN. I
don't believe it is necessary to have both (unless the EXIT PROGRAM
releases the .DLL core from memory????). Perhaps that's a problem?

Also, if you put, say a DISPLAY statement in after the CALL to the
DLL, do you still get that error?

Again, I'm guessing.
D.
```

##### ↳ ↳ Re: ERROR Again: Error 173 with DLLs

- **From:** "user..." <ua-author-1142773@usenetarchives.gap>
- **Date:** 1997-04-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a5e4b65ffb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a5e4b65ffb-p2@usenetarchives.gap>`
- **References:** `<5jih2n$pqj@news.Informatik.Uni-Oldenburg.DE> <gap-a5e4b65ffb-p2@usenetarchives.gap>`

```


Try to use Exit Program , instead Stop Run.

Regards ,

J Monteiro
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
