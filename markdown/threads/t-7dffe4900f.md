[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus XM over Windows NT server

_2 messages · 2 participants · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus XM over Windows NT server

- **From:** "Julia Sabater" <juli@infotelecom.es>
- **Date:** 1999-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01beb0df$20fe87e0$2443e0c2@tiago>`

```
Hi, group:

I have random problems when I execute the MicroFocus eXtended Memory
manager (XM) over a Windows NT server (in server computer). The most
frequent problem is if the COBOL application launched with XM calls the DOS
command (either command.com or cmd.com), the DOS session (or the complete
system) hangs. 

After trying many configuration combinations, it seems to me the cause is
the XM version, a bit old-fashioned.

My currently XM is:

XM V1.4.6 - The Micro Focus DOS Extender Copyright (c) 1987-1994 Micro
Focus Ltd
URN AXCPA/000074570    [Protocol: DPMI]                                 
Ref 009

NT version is 4.0, with Service Pack 4.

Anybody knows there is a newer version or workaround to fix that problem?

(Yes, I know, I shouldn't use the system console to run user applications,
but...)

Thanks a lot!

Julia Sabater.
juli@infotelecom.es
```

#### ↳ Re: Microfocus XM over Windows NT server

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#rBDwk6s#GA.323@nih2naae.prod2.compuserve.com>`
- **References:** `<01beb0df$20fe87e0$2443e0c2@tiago>`

```
Have you tried my method of using the X"91" function call?
See "Re" Call wordpad from mf cobol v3.2"
The exact wording can make a BIG difference.  It works on my NT just fine,
although I have not installed SP4 yet.

Note that this method does not mention command or cmd at all (unless you
want
a blank command prompt).

    Here is a sample program.  Note that when calling a dos program,
it pauses and does not continue until the external program has exited.
When I tried it with WORDPAD however, the calling program continued running.
I suppose that the easy solution would be an accept after the external call.
This would
also allow the user to see that an error other than program not found
existed.

    If you want a blank command prompt, you must specify "COMMAND".


000100 WORKING-STORAGE SECTION.
000200
000300 01  FUNCTION-X          PIC X VALUE X"91".
000400 01  RESULT              PIC 99 COMP         VALUE ZERO.
000500 01  CALL-PGM            PIC 99 COMP         VALUE 35.
000600 01  SET-CMD-LINE        PIC 99 COMP         VALUE 2.
000700 01  PARAMETER.
000800     05  PARM-SIZE       PIC 99 COMP.
000900     05  PARM            PIC X.
001000
001100 PROCEDURE DIVISION.
001200 0100-MENU.
001300     DISPLAY SPACES AT 0101.
001400     DISPLAY "CALL WORDPAD" AT 0101.
001500     DISPLAY "WORDPAD"   UPON COMMAND-LINE.
001600
001700     MOVE ZERO       TO PARM-SIZE.
001800     MOVE SPACES     TO PARM.
001900     CALL FUNCTION-X USING RESULT CALL-PGM PARAMETER.
002000     IF RESULT NOT = ZERO
002100       DISPLAY "ERROR CALLING EXTERNAL PGM" AT 1001.
002200     DISPLAY "ALL DONE"   AT 1501.
002300 THE-END.
002400     STOP RUN.





Thane Hubbell wrote in message ...
>On Tue, 8 Jun 1999 05:28:04, "Massimo Morgia"
><areasoftware@tiscalinet.it> wrote:
…[10 more quoted lines elided]…
>






Julia Sabater wrote in message <01beb0df$20fe87e0$2443e0c2@tiago>...
>Hi, group:
>
…[28 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
