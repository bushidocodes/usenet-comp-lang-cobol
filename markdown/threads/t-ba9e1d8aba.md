[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# STDIN and CALL "SYSTEM" questions

_6 messages · 3 participants · 1999-10_

---

### STDIN and CALL "SYSTEM" questions

- **From:** semiel@my-deja.com
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7thktk$9rj$1@nnrp1.deja.com>`

```
-I would like to read from STDIN using ONLY ANS85 Cobol
-I need to do a CALL "SYSTEM" on WinNT without opening a DOS box at all

Thanks for your help,
Alain.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: STDIN and CALL "SYSTEM" questions

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tiel8$9pb$1@news.cerf.net>`
- **References:** `<7thktk$9rj$1@nnrp1.deja.com>`

```
semiel@my-deja.com wrote in message <7thktk$9rj$1@nnrp1.deja.com>...
>-I would like to read from STDIN using ONLY ANS85 Cobol

I would assume a standard ACCEPT statement uses STDIN.

>-I need to do a CALL "SYSTEM" on WinNT without opening a DOS box at all

This cannot be accomplished using standard ANS85 Cobol, but here is a
solution using Acucobol and the Windows API:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. SHELLAPI.
       AUTHOR.     (c) 1999, Cheesle.
       REMARKS.
      *This program demonstrates how to perform a shell execute of a program
      *or a document that has an association set up in the windows command
      *shell.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01 SHOW-OPTION         UNSIGNED-INT.
       01 H-ACU-WND           SIGNED-INT IS EXTERNAL.
       01 EXEC-RESULT       SIGNED-INT.

       01 ERROR-STR.
          03 FILLER           PIC X(18) VALUE "An error occured: ".
          03 EXEC-ERR         PIC S9(02).
       01 ERROR-STRING REDEFINES ERROR-STR PIC X(21).

       01 PARAMS.
          03 TASK             PIC X(30).
          03 APP              PIC X(30).
          03 APP-PARAMS       PIC X(30).
          03 DIRECTORY        PIC X(30).

       SCREEN SECTION.

       PROCEDURE DIVISION.
       MAIN SECTION.
       MAIN-001.

           SET     ENVIRONMENT      "DLL-CONVENTION" TO 1.
      *We want the application minimized, and our current window to stay
active
      *we do so by setting SHOW-OPTION to 7.
    DISPLAY INITIAL          WINDOW
            TITLE-BAR        WITH SYSTEM MENU
            AUTO-MINIMIZE
            SIZE             40
            LINES     20
            TITLE            "Demo of ShellExecute".
    STRING  "TEST.TXT"       LOW-VALUES DELIMITED BY SIZE
            INTO             APP.
    STRING  "open"           LOW-VALUES DELIMITED BY SIZE
            INTO             TASK.
    STRING  LOW-VALUES       DELIMITED BY SIZE INTO APP-PARAMS.
    STRING  LOW-VALUES       DELIMITED BY SIZE INTO DIRECTORY.
           MOVE    7                TO SHOW-OPTION.

    CALL    "SHELL32.DLL"    ON EXCEPTION GO TO MAIN-900.
      *Important note: All use of NULL is to terminate strings.
    CALL    "ShellExecuteA"  USING
            BY               VALUE H-ACU-WND
      *The following command instructs the function to open the application,
      *other options are: "print", "edit", "explore", "properties"
      *You may sett this one to NULL, the default action then is"open"
            BY REFERENCE     TASK
      *The file to open
            BY REFERENCE     APP
      *If we were to open an executable, any parameters may be sent here, if
      *the file is a document, we may not send parameters, thus setting to
      *NULL.
            BY REFERENCE     APP-PARAMS
      *Here we specify the directory of the application / document
      *NULL makes use of the current directory
                   BY REFERENCE     DIRECTORY
      *Finally we decide how we would like to application to launch,
      *See below for a list of possible options here
                   BY               VALUE SHOW-OPTION
                   GIVING     EXEC-RESULT
            ON               EXCEPTION GO TO MAIN-900.

           IF      EXEC-RESULT      < 33
               MOVE             EXEC-RESULT TO EXEC-ERR
                   DISPLAY          MESSAGE BOX
                                    ERROR-STRING
                                    TITLE "Error"
                                    TYPE 1
        ICON 3
    ELSE
            DISPLAY          "Done..."
            ACCEPT           OMITTED.

           CANCEL  "SHELL32.DLL".
           SET     ENVIRONMENT      "DLL-CONVENTION" TO 0.

       MAIN-900.
       MAIN-EXIT.
           GOBACK.

      *Possible show options:
      *SW_SHOWNORMAL       1 Launches, displays in standard mode and
activates
      *SW_SHOWMINIMIZED    2 Launches, minimizes and activates
      *SW_SHOWMAXIMIZED    3 Launches, displays maximized and activates.
      *SW_SHOWNOACTIVATE   4 Launches, displays and keep you window active.
      *SW_SHOW             5 Launches, activates and show it 'as is'.
      *SW_SHOWMINNOACTIVE  7 Launches, minimizes and keep your window
active.
      *SW_SHOWNA           8 Launches, displays, but keep your window
active.
      *SW_SHOWDEFAULT      10 Launches, activates and show window as it is
      *         programmatically set do to.

      * There are more options as well, these are however the most common
ones.

      *Error messages
      *                        0       System out of memory or resources
      *SE_ERR_FNF              2       file not found
      *SE_ERR_PNF              3       path not found
      *SE_ERR_ACCESSDENIED     5       access denied
      *SE_ERR_OOM              8       out of memory
      *SE_ERR_DLLNOTFOUND      32      Did not find the DLL (SHELL32.DLL)
      *SE_ERR_SHARE            26      Sharing violation (some other use the
      *                                file)
      *SE_ERR_ASSOCINCOMPLETE  27      Incomplete association of the
document
      *                                Control the association.
      *SE_ERR_DDETIMEOUT       28      Dynamic Data Exchange time out. Your
      *                                computer is either overloaded or your
      *                                network has a problem
      *SE_ERR_DDEFAIL          29      Could no complete DDE services
      *SE_ERR_DDEBUSY          30      Dynamic Data Exchange conquestion,
wait
      *                                and try again
      *SE_ERR_NOASSOC          31      There is no association defined for
this
      *                                file.

      * There are more errors as well, these are however the most common
ones.

Note that this example assumes that you have notepad.exe on your computer
and that TXT files are associated with notepad.exe.

Hope it helps.

Cheesle
```

##### ↳ ↳ Re: STDIN and CALL "SYSTEM" questions

- **From:** semiel@my-deja.com
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tl5m7$q4l$1@nnrp1.deja.com>`
- **References:** `<7thktk$9rj$1@nnrp1.deja.com> <7tiel8$9pb$1@news.cerf.net>`

```

> >-I would like to read from STDIN using ONLY ANS85 Cobol
>
> I would assume a standard ACCEPT statement uses STDIN.

As far as i know the normal ANS85 ACCEPT reads from console (Bios or
something...). It reads stuff send through the keyboard.
What im sure of, is that it doesnt read from STDIN.
No one i have asked could respond to this question.

Thanks,
Alain.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Repost: STDIN question!

- **From:** semiel@my-deja.com
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tsof3$q1g$1@nnrp1.deja.com>`
- **References:** `<7thktk$9rj$1@nnrp1.deja.com> <7tiel8$9pb$1@news.cerf.net> <7tl5m7$q4l$1@nnrp1.deja.com>`

```

> >-I would like to read from STDIN using ONLY ANS85 Cobol
>
> I would assume a standard ACCEPT statement uses STDIN.

As far as i know the normal ANS85 ACCEPT reads from console (Bios or
something...). It reads stuff send through the keyboard.
What im sure of, is that it doesnt read from STDIN.
No one i have asked could respond to this question.

Thanks,
Alain.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Repost: STDIN question!

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tt0in$st3$1@news.cerf.net>`
- **References:** `<7thktk$9rj$1@nnrp1.deja.com> <7tiel8$9pb$1@news.cerf.net> <7tl5m7$q4l$1@nnrp1.deja.com> <7tsof3$q1g$1@nnrp1.deja.com>`

```
semiel@my-deja.com wrote in message <7tsof3$q1g$1@nnrp1.deja.com>...
>
>> >-I would like to read from STDIN using ONLY ANS85 Cobol
…[6 more quoted lines elided]…
>No one i have asked could respond to this question.

Well, that's interesting, consider the following:

MyApp <info.txt

This is typed on the console, and what happens is that MyApp will read this,
if it reads from STDIN. Hence, I may dare to say that STDIN is by default
from console.

This does however not conflict with your final statement, that the ANS85
ACCEPT does not read from STDIN, but, in that case, nor does it read from
the console.

Cheesle
```

###### ↳ ↳ ↳ Re: Repost: STDIN question!

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICoM3.2354$Ck.2642@news1.mia>`
- **References:** `<7thktk$9rj$1@nnrp1.deja.com> <7tiel8$9pb$1@news.cerf.net> <7tl5m7$q4l$1@nnrp1.deja.com> <7tsof3$q1g$1@nnrp1.deja.com> <7tt0in$st3$1@news.cerf.net>`

```
Cheesle wrote:
>semiel@my-deja.com wrote:
>>
…[19 more quoted lines elided]…
>the console.

Stdin is a C concept, console is a DOS concept (CON:).  In the majority
of DOS C compilers I have seen, stdin+stdout = console.  Whether or not
a COBOL program can use stdin for simple ACCEPT statements is entirely
a function of the particular compiler, and how it does I/O.

For example, with MF COBOL 3.2, a simple:  ACCEPT data-name
does take redirected data, and echoes the data to the screen on input.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
