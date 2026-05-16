[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress GUI screens on win-95

_2 messages · 2 participants · 1998-12_

---

### NetExpress GUI screens on win-95

- **From:** vgibson@westga.edu (Vince Gibson)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366d546e.11310964@news.westga.edu>`

```
I am using NetExpress 2.0 on a NT v4 machine. I am developing  GUI
programs using the dialog system. The problem is when I run the
programs on win-95 machines, the screens appearance is all messed up.
The entry fields are shown very small which chops off the information
inside. When you resize the window to make the fields taller, the test
labels repeat across the screen making it a bloody mess.

What can I do to make the appearance of the GUI windows on the win-95
appear the same as it does in the dialog system development.
```

#### ↳ Re: NetExpress GUI screens on win-95

- **From:** hippy@ndirect.co.uk (Guy C. Fountain)
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366ef10c.15272220@news.netdirect.net.uk>`
- **References:** `<366d546e.11310964@news.westga.edu>`

```
On Tue, 08 Dec 1998 16:40:35 GMT, vgibson@westga.edu (Vince Gibson)
wrote:

>I am using NetExpress 2.0 on a NT v4 machine. I am developing  GUI
>programs using the dialog system. The problem is when I run the
…[6 more quoted lines elided]…
>appear the same as it does in the dialog system development.

Vince,

Dialog has dynamic window sizing.
Example below of global dialog, object dialog and data block that uses
this.


***Global Dialog***

 SCREENSET-INITIALIZED
*
* This CALLOUT loads the NetExpress API Class Library
* NOTE this must always occur before any function which
* causes the creation of a window.
     CALLOUT-PARAMETER 1 CONFIG-FLAG $NULL
     CALLOUT-PARAMETER 2 CONFIG-VALUE $NULL
     MOVE 15 CONFIG-FLAG
     MOVE 1 CONFIG-VALUE
     CALLOUT "dsrtcfg" 3 $PARMLIST
*
* This CALLOUT enables Default push button tracking
     CALLOUT-PARAMETER 1 CONFIG-FLAG $NULL
     CALLOUT-PARAMETER 2 CONFIG-VALUE $NULL
     MOVE 8 CONFIG-FLAG
     MOVE 1 CONFIG-VALUE
     CALLOUT "dsrtcfg" 3 $PARMLIST
*
* This CALLOUT enables Dynamic Window Sizing
* and multiple resolution support
     CALLOUT-PARAMETER 1 CONFIG-FLAG $NULL
     CALLOUT-PARAMETER 2 CONFIG-VALUE $NULL
     MOVE 9 CONFIG-FLAG
     MOVE 2 CONFIG-VALUE
     CALLOUT "dsrtcfg" 3 $PARMLIST
*
* This CALLOUT sets correct background color on Dialog Box text
     CALLOUT-PARAMETER 1 CONFIG-FLAG $NULL
     CALLOUT-PARAMETER 2 CONFIG-VALUE $NULL
     MOVE 10 CONFIG-FLAG
     MOVE 1 CONFIG-VALUE
     CALLOUT "dsrtcfg" 3 $PARMLIST
*
* This procedure does a callout to handle your statusbar resize events
   RESIZE-PROCEDURE
     MOVE "RESIZE" CALL-FUNCTION(1)
     CALLOUT "SBAR" 0 FUNCTION-DATA
*
* This procedure does a callout to handle your statusbar refresh
   REFRESH-STATUS-BAR
     SET OBJECT-REFERENCE(1) CURRENT-WINDOW-SBAR
     MOVE "REFRESH-OBJECT" CALL-FUNCTION(1)
     CALLOUT "SBAR" 0 FUNCTION-DATA


***Primary window dialog***

 WINDOW-CREATED
*
* Status bar processing
     SET CURRENT-WINDOW-SBAR MAIN-WIND-SBAR-OBJREF
     TIMEOUT 25 REFRESH-STATUS-BAR
*
 GAINED-FOCUS
     SET CURRENT-WINDOW-SBAR MAIN-WIND-SBAR-OBJREF
 WINDOW-SIZED
     SET OBJECT-REFERENCE(1) MAIN-WIND-SBAR-OBJREF
     BRANCH-TO-PROCEDURE RESIZE-PROCEDURE
 WINDOW-RESTORED
     SET OBJECT-REFERENCE(1) MAIN-WIND-SBAR-OBJREF
     BRANCH-TO-PROCEDURE RESIZE-PROCEDURE
 WINDOW-MAXIMIZED
     SET OBJECT-REFERENCE(1) MAIN-WIND-SBAR-OBJREF
     BRANCH-TO-PROCEDURE RESIZE-PROCEDURE
   @EXIT
     BRANCH-TO-PROCEDURE EXIT-MAIN-WIND


***Data Block***

EXIT-FLAG                        9      1.0           
CONFIG-FLAG                      C5     4.0           
CONFIG-VALUE                     C5     4.0           
FUNCTION-DATA                          1              
  WINDOW-HANDLE                  C5     4.0           
  OBJECT-REFERENCE               OBJ-REF              
  CALL-FUNCTION                  X     30.0           
  NUMERIC-VALUE                  C5     4.0           
  NUMERIC-VALUE2                 C5     4.0           
  SIZE-WIDTH                     C5     4.0           
  SIZE-HEIGHT                    C5     4.0           
  POSITION-X                     C5     4.0           
  POSITION-Y                     C5     4.0           
  IO-TEXT-BUFFER                 X    256.0           
  IO-TEXT-BUFFER2                X    256.0           
CURRENT-WINDOW-SBAR              OBJ-REF              
MAIN-WIND-SBAR-OBJREF            OBJ-REF              
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
