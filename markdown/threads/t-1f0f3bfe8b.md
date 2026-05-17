[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Win32 api call in acucobol 3.2 GT

_2 messages · 1 participant · 1997-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Win32 api call in acucobol 3.2 GT

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1997-12-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66sbul$ls8$1@node17.cwnet.frontiernet.net>`

```

For acucobol users only. Listed below is 3.2GT sample program for calling a
win32 api function. Hope it useful.

IDENTIFICATION DIVISION.
PROGRAM-ID. WEBROWSE.
AUTHOR. DAN MALTES.
DATE-WRITTEN. 12-12-97.
REMARKS. Connect to web url and send e-mail with default browser
via win32 api call to shell32.
****************************************************************
* Dan Maltes at Applied Systems Technology.
* e-mail: d.··.@ast··a.com
* www: http://www.frontiernet.net/â€¾dwm or http://www.astusa.com
****************************************************************
* Below is copy of the declare statment used in Visual Basic
* for the ShellExecute function.
* Declare Function ShellExecute Lib "shell32.dll"
* Alias "ShellExecuteA"
* (ByVal hwnd As Long, ByVal lpOperation As String,
* ByVal lpFile As String, ByVal lpParameters As String,
* ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
****************************************************************
* The key ingredient missing was the valid win32 handle for
* the runtime window. Acucobol now supplies this in working
* storage item h-acu-wnd. Pass this as the hwnd paramater and
* it works fine.
* Special Note: When passing strings there are 3 requirements:
* 1. Terminate each string with low-values or nulls.
* 2. You must setup pointers for each string and
* set the pointers to the address of each string.
* 3. Pass the pointer for each string to the function.
****************************************************************
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
*6 data items passed by value.
01 H-ACU-WND PIC 9(4) COMP-5 EXTERNAL.
01 WINDOW-HANDLE USAGE HANDLE OF WINDOW.
01 WS-OPERATION PIC X(255).
01 WS-FILE PIC X(255).
01 WS-PARAMATERS PIC X(255).
01 WS-DIRECTORY PIC X(255).
01 WS-SHOW-CMD USAGE UNSIGNED-LONG.
*Return value must be unsigned-long for win32.
01 RETURN-VALUE USAGE UNSIGNED-LONG.
*pointers for 4 strings to be passed.
01 PTR-WS-OPERATION USAGE POINTER.
01 PTR-WS-FILE USAGE POINTER.
01 PTR-WS-PARAMATERS USAGE POINTER.
01 PTR-WS-DIRECTORY USAGE POINTER.
*Browser functions.
01 BROWSER-FUNCTION PIC 9(4) VALUE 0.
88 BROWSE-WEBSITE VALUE 1.
88 SEND-EMAIL VALUE 2.
01 EXCEPTION-KEY PIC 9(4) VALUE 0.
* Screen section variables.
01 WS-URL PIC X(30) VALUE SPACES.
01 WS-EMAIL PIC X(30) VALUE SPACES.
LINKAGE SECTION.
SCREEN SECTION.
01 SCREEN-OPTIONS.
05 PUSH-BUTTON, TITLE "&Browse Website"
LINE 5 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 1.
05 LABEL, TITLE "URL: "
COL + 2, LABEL-OFFSET 10.
05 ENTRY-FIELD, VALUE WS-URL
COL + 2.
05 PUSH-BUTTON, TITLE "Send &E-mail"
LINE 8 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 2.
05 LABEL, TITLE "E-mail:"
COL + 2, LABEL-OFFSET 10.
05 ENTRY-FIELD, VALUE WS-EMAIL
COL + 2.
05 PUSH-BUTTON, TITLE "E&xit"
LINE 11 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 3.

PROCEDURE DIVISION.
MAIN-LOGIC SECTION.
*Set dll-connvetion to pascal calling convention.
*Win32 api requires pascal calling convention.
SET ENVIRONMENT "DLL-CONVENTION" TO 1.
*Load the dll so it's functions are available.
CALL "SHELL32.DLL".
DISPLAY FLOATING GRAPHICAL WINDOW
LINE 1 POS 1 SIZE 80 LINES 20
BOXED SYSTEM MENU HANDLE IN WINDOW-HANDLE.
*Choose a browser function.
MOVE "http://www.acucobol.com" TO WS-URL.
MOVE "mailto:d.··.@ast··a.com" TO WS-EMAIL.
DISPLAY SCREEN-OPTIONS.
PERFORM UNTIL EXCEPTION-KEY = 3
ACCEPT SCREEN-OPTIONS
ACCEPT EXCEPTION-KEY FROM ESCAPE KEY
MOVE EXCEPTION-KEY TO BROWSER-FUNCTION
EVALUATE TRUE
WHEN BROWSE-WEBSITE
MOVE WS-URL TO WS-FILE
PERFORM RUN-WEB-BROWSER
WHEN SEND-EMAIL
MOVE WS-EMAIL TO WS-FILE
PERFORM RUN-WEB-BROWSER
END-EVALUATE
END-PERFORM.
*Cancel dll to release memory.
CANCEL "SHELL32.DLL".
DESTROY ALL CONTROLS.
STOP RUN.
RUN-WEB-BROWSER SECTION.
*Set all string pointers initially to null.
SET PTR-WS-OPERATION TO NULL.
SET PTR-WS-FILE TO NULL.
SET PTR-WS-PARAMATERS TO NULL.
SET PTR-WS-DIRECTORY TO NULL.
MOVE SPACES TO WS-OPERATION.
INSPECT WS-OPERATION REPLACING
TRAILING SPACES BY NULLS.
SET PTR-WS-OPERATION TO ADDRESS OF WS-OPERATION.
* Set the web browser url command.
INSPECT WS-FILE REPLACING TRAILING SPACES BY NULLS.
SET PTR-WS-FILE TO ADDRESS OF WS-FILE.
MOVE SPACES TO WS-PARAMATERS.
INSPECT WS-PARAMATERS REPLACING
TRAILING SPACES BY NULLS.
SET PTR-WS-PARAMATERS TO ADDRESS OF WS-PARAMATERS.
MOVE SPACES TO WS-DIRECTORY.
INSPECT WS-DIRECTORY REPLACING TRAILING
SPACES BY NULLS.
SET PTR-WS-DIRECTORY TO ADDRESS OF WS-DIRECTORY.
* Use 1 for normal display of application window.
SET WS-SHOW-CMD TO 1.
* Must use the alias function name with correct case.
CALL "ShellExecuteA" USING BY VALUE
H-ACU-WND,
PTR-WS-OPERATION,
PTR-WS-FILE,
PTR-WS-PARAMATERS,
PTR-WS-DIRECTORY,
WS-SHOW-CMD,
RETURNING RETURN-VALUE
ON EXCEPTION
DISPLAY "Status: Can't run " WS-FILE
LINE 10 POS 1
DISPLAY "Return Value: " LINE 11 POS 1 RETURN-VALUE
ACCEPT OMITTED TAB
END-ACCEPT.
```

#### ↳ Re: Win32 api call in acucobol 3.2 GT

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f0f3bfe8b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<66sbul$ls8$1@node17.cwnet.frontiernet.net>`
- **References:** `<66sbul$ls8$1@node17.cwnet.frontiernet.net>`

```

Here's a more up to date version. I removed the extra string pointers
because passing strings by reference works fine:

IDENTIFICATION DIVISION.
PROGRAM-ID. WEBROWSE.
AUTHOR. DAN MALTES.
DATE-WRITTEN. 12-12-97.
REMARKS. Connect to web url or send e-mail with default browser
via win32 api call to shell32.
****************************************************************
* Dan Maltes at Applied Systems Technology.
* e-mail: d.··.@ast··a.com
* www: http://www.frontiernet.net/‾dwm or http://www.astusa.com
****************************************************************
* Below is copy of the declare statment used in Visual Basic
* for the ShellExecute function.
* Declare Function ShellExecute Lib "shell32.dll"
* Alias "ShellExecuteA"
* (ByVal hwnd As Long, ByVal lpOperation As String,
* ByVal lpFile As String, ByVal lpParameters As String,
* ByVal lpDirectory As String, ByVal nShowCmd As Long) As Long
****************************************************************
* The key ingredient missing was the valid win32 handle for
* the runtime window. Acucobol now supplies this in working
* storage item h-acu-wnd. Pass this as the hwnd paramater and
* it works fine.
* Strings can be passed by reference, but the strings must
* be null or low-value terminated.
****************************************************************
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
*6 data items passed by value.
01 H-ACU-WND PIC 9(4) COMP-5 EXTERNAL.
01 WINDOW-HANDLE USAGE HANDLE OF WINDOW.
01 WS-OPERATION PIC X(255).
01 WS-FILE PIC X(255).
01 WS-PARAMATERS PIC X(255).
01 WS-DIRECTORY PIC X(255).
01 WS-SHOW-CMD USAGE UNSIGNED-LONG.
*Return value must be unsigned-long for win32.
01 RETURN-VALUE USAGE UNSIGNED-LONG.
*Browser functions.
01 BROWSER-FUNCTION PIC 9(4) VALUE 0.
88 BROWSE-WEBSITE VALUE 1.
88 SEND-EMAIL VALUE 2.
01 EXCEPTION-KEY PIC 9(4) VALUE 0.
* Screen section variables.
01 WS-URL PIC X(30) VALUE SPACES.
01 WS-EMAIL PIC X(30) VALUE SPACES.
LINKAGE SECTION.
SCREEN SECTION.
01 SCREEN-OPTIONS.
05 PUSH-BUTTON, TITLE "&Browse Website"
LINE 5 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 1.
05 LABEL, TITLE "URL: "
COL + 2, LABEL-OFFSET 10.
05 ENTRY-FIELD, VALUE WS-URL
COL + 2.
05 PUSH-BUTTON, TITLE "Send &E-mail"
LINE 8 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 2.
05 LABEL, TITLE "E-mail:"
COL + 2, LABEL-OFFSET 10.
05 ENTRY-FIELD, VALUE WS-EMAIL
COL + 2.
05 PUSH-BUTTON, TITLE "E&xit"
LINE 11 COL 10 SIZE 15
SELF-ACT, EXCEPTION-VALUE 3.

PROCEDURE DIVISION.
MAIN-LOGIC SECTION.
*Set dll-convention to pascal calling convention.
*Win32 api requires pascal calling convention.
SET ENVIRONMENT "DLL-CONVENTION" TO 1.
*Load the dll so it's functions are available.
CALL "SHELL32.DLL".
DISPLAY FLOATING GRAPHICAL WINDOW
LINE 1 POS 1 SIZE 80 LINES 20
BOXED SYSTEM MENU HANDLE IN WINDOW-HANDLE.
*Choose a browser function.
MOVE "http://www.acucobol.com" TO WS-URL.
MOVE "mailto:d.··.@ast··a.com" TO WS-EMAIL.
DISPLAY SCREEN-OPTIONS.
PERFORM UNTIL EXCEPTION-KEY = 3
ACCEPT SCREEN-OPTIONS
ACCEPT EXCEPTION-KEY FROM ESCAPE KEY
MOVE EXCEPTION-KEY TO BROWSER-FUNCTION
EVALUATE TRUE
WHEN BROWSE-WEBSITE
MOVE WS-URL TO WS-FILE
PERFORM RUN-WEB-BROWSER
WHEN SEND-EMAIL
MOVE WS-EMAIL TO WS-FILE
PERFORM RUN-WEB-BROWSER
END-EVALUATE
END-PERFORM.
*Cancel dll to release memory.
CANCEL "SHELL32.DLL".
DESTROY ALL CONTROLS.
STOP RUN.
RUN-WEB-BROWSER SECTION.
MOVE SPACES TO WS-OPERATION.
INSPECT WS-OPERATION REPLACING
TRAILING SPACES BY NULLS.
* Set the web browser url command.
INSPECT WS-FILE REPLACING TRAILING SPACES BY NULLS.
MOVE SPACES TO WS-PARAMATERS.
INSPECT WS-PARAMATERS REPLACING
TRAILING SPACES BY NULLS.
MOVE SPACES TO WS-DIRECTORY.
INSPECT WS-DIRECTORY REPLACING TRAILING
SPACES BY NULLS.
* Use 1 for normal display of application window.
SET WS-SHOW-CMD TO 1.
* Must use the alias function name with correct case.
CALL "ShellExecuteA" USING BY VALUE
H-ACU-WND,
BY REFERENCE WS-OPERATION,
BY REFERENCE WS-FILE,
BY REFERENCE WS-PARAMATERS,
BY REFERENCE WS-DIRECTORY,
WS-SHOW-CMD,
RETURNING RETURN-VALUE
ON EXCEPTION
DISPLAY "Status: Can't run " WS-FILE
LINE 10 POS 1
DISPLAY "Return Value: " LINE 11 POS 1 RETURN-VALUE
ACCEPT OMITTED TAB
END-ACCEPT.

Daniel Maltes wrote in message
<66sbul$ls8$1.··.@nod··t.net>...
› For acucobol users only.  Listed below is 3.2GT sample program for calling
› a
…[149 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
