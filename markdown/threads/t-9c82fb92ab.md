[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# winhelp in MF cobol

_1 message · 1 participant · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### winhelp in MF cobol

- **From:** "WerewolF" <werewolf@anti-social.com>
- **Date:** 1999-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<780f7j$3gh$1@duke.telepac.pt>`

```
Does anyone know how can I call winhelp in MF cobol but executing the entry
in the topic I want?

A solution for this would be much appreciated.

Here is the program.
Thank you

       SPECIAL-NAMES.
           call-convention 11 is winapi.
       DATA DIVISION.
       Working-Storage Section.

       01 WS-WinExec-Parameters.
          03 WS-WinExec-Command-Line         pic x(128).
          03 WS-WinExec-Window-State         pic 9(004) comp-5.
          03 WS-WinExec-Return-Code          pic 9(004) comp-5.
       01 WS-PTR                             PROCEDURE-POINTER.
       01 WS-COUNTER                         PIC 9(3).
******************************************************
       LINKAGE SECTION.
       COPY FSTLINK.CBL.
      *--------------------------------------------------
       PROCEDURE DIVISION USING COM-AREA COM-AREA-S COM-AREA-T.
      *--------------------------------------------------
           SET WS-PTR TO ENTRY"KERNEL".
           initialize WS-WinExec-Parameters.
           MOVE 1    TO WS-WINEXEC-WINDOW-STATE.
           STRING "WINHELP.EXE"
                            DELIMITED BY SIZE
                  " "         DELIMITED BY SIZE
                   "praia.hlp "   DELIMITED BY SPACES
****************  " 4125 "         DELIMITED BY SIZE
                 X"00"        DELIMITED BY SIZE
                 INTO WS-WINEXEC-COMMAND-LINE
           END-STRING.
***********DISPLAY WS-WINEXEC-COMMAND-LINE
           CALL Winapi "WINEXEC"
                    USING BY REFERENCE WS-WINEXEC-COMMAND-LINE
                          BY VALUE WS-WINEXEC-WINDOW-STATE
                      RETURNING   WS-WINEXEC-RETURN-CODE
           END-CALL.
       R-FIM.
            EXIT PROGRAM.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
