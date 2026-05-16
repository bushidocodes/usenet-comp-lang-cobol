[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/COBOL vs. 6.5 prob. - retn code

_4 messages · 3 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM/COBOL vs. 6.5 prob. - retn code

- **From:** Erie <73042.311@CompuServe.COM>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uQyQZzid#GA.96@nih2naaf.prod2.compuserve.com>`

```
I am writing a windows 95 (DOS) batch file which will call several 
COBOL programs.  I know that RM/COBOL gives you a return code in 
the program during an error.  The question I have is how can I use 
this return code code to determine if the program has an error?  
It appears that this return code must not be automatically 
returned to the operating system because the batch ERRORLEVEL test 
does not catch the return code.  Doe anyone have any experience 
doing anything like this?  Let me know.  Any help would be greatly 
appreciated.  Thanks in advance.
```

#### ↳ Re: RM/COBOL vs. 6.5 prob. - retn code

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dbpmp$jgb$3@news.igs.net>`
- **References:** `<uQyQZzid#GA.96@nih2naaf.prod2.compuserve.com>`

```
You may be running into the the old problem of the dos IF statement.  It is
not an equality check, it is a less than check. You have to start with the
highest level first.
IE
if errorlevel 1 goto
if errorlevel 2 goto
will not work.
but
if errorlevel 2 goto
if errorlevel 1 goto
will
Erie <73042.311@CompuServe.COM> wrote in message ...
>I am writing a windows 95 (DOS) batch file which will call several
>COBOL programs.  I know that RM/COBOL gives you a return code in
…[6 more quoted lines elided]…
>appreciated.  Thanks in advance.
```

##### ↳ ↳ Re: RM/COBOL vs. 6.5 prob. - retn code

- **From:** Erie <73042.311@CompuServe.COM>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eUJ89bsd#GA.255@nih2naad.prod2.compuserve.com>`
- **References:** `<7dbpmp$jgb$3@news.igs.net>`

```
Thanks, but I don't think this is the problem because I was just 
using NOT ERRORLEVEL to test if the value was not 0.  So, I don't 
believe RMCOBOL is really returning any value back to the 
operating system.  But, thanks for trying to help.
```

#### ↳ Re: RM/COBOL vs. 6.5 prob. - retn code

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vXsK2.64216$rs2.18430163@client.news.psi.net>`
- **References:** `<uQyQZzid#GA.96@nih2naaf.prod2.compuserve.com>`

```
Erie,

This works for me.


ID DIVISION.
PROGRAM-ID.  A.
REMARKS.   Returns a return-code of 2.
PROCEDURE DIVISION.
A.
      MOVE 2 TO RETURN-CODE.
      STOP RUN.
END PROGRAM A.


START /W RUNCOBOL  A.COB  K
IF ERRORLEVEL 252 GOTO LEVEL252
IF ERRORLEVEL 2   GOTO LEVEL2
IF ERRORLEVEL 1   GOTO LEVEL1
ECHO  Error level 1  2 or 252 not returned
PAUSE
GOTO ENDIT

:LEVEL252
CLS
ECHO   Program not Found ERROR LEVEL 252
PAUSE
GOTO ENDIT

:LEVEL2
CLS
ECHO   Test PASSED  ERROR LEVEL 2
PAUSE
GOTO ENDIT

:LEVEL1
CLS
ECHO   Test FAILED ERROR LEVEL 1
PAUSE
:ENDIT

==============================================
Robert A. Heady                                   r.heady@liant.com

Liant Software Corp.
8911 Capital of Texas Hwy.
Austin, TX  78759
Phone:   (512) 343-1010
Fax:       (800) 835-0301
Home Page:  www.liant.com                                     VRWC
==============================================
Erie <73042.311@CompuServe.COM> wrote in message ...
>I am writing a windows 95 (DOS) batch file which will call several
>COBOL programs.  I know that RM/COBOL gives you a return code in
…[6 more quoted lines elided]…
>appreciated.  Thanks in advance.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
