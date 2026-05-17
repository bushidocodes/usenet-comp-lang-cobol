[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CLRSCRN from cobol on VAX VMS ?

_3 messages · 2 participants · 1995-03_

---

### CLRSCRN from cobol on VAX VMS ?

- **From:** "a.r...." <ua-author-17087529@usenetarchives.gap>
- **Date:** 1995-03-07T07:32:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-MwHO5DmHK_Y@usenetarchives.gap>`

```
Does anybody knoww how to clear the screen on a VAX terminal from within a
cobol program. (It's not a very good compiler, so something veeeery basic
is needed.

thanx

Arty.

"When should we evacuate ?"
```

#### ↳ Re: CLRSCRN from cobol on VAX VMS ?

- **From:** "cas..." <ua-author-15929350@usenetarchives.gap>
- **Date:** 1995-03-07T06:16:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fc440ad7b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-MwHO5DmHK_Y@usenetarchives.gap>`
- **References:** `<ua-fallback-MwHO5DmHK_Y@usenetarchives.gap>`

```
In article ,
A.R··.@sys··c.uk (Arthur Edwards) wrote:

› Does anybody knoww how to clear the screen on a VAX terminal from within a
› cobol program. (It's not a very good compiler, so something veeeery basic
› is needed.

in the interests of 'very basic' I tried:
DISPLAY "" ERASE END SCREEN
doesn't work

however, this does:
IDENTIFICATION DIVISION.
PROGRAM-ID. screen_tester.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 DELAY-VAL COMP-1 VALUE 3.000.
01 SMG-STUFF.
03 DISPLAY1 PIC 9(09) COMP.
03 PASTE1 PIC 9(09) COMP.
03 KEYBOARD1 PIC 9(09) COMP.
03 ROWS PIC S9(09) COMP VALUE 24.
03 COLUMNS PIC S9(09) COMP VALUE 80.
03 ROW PIC S9(09) COMP.
03 COL PIC S9(09) COMP.
/
PROCEDURE DIVISION.
0000-MAIN
.
* do the prep work; in the real world we would check condition value returned
* for each of these functions. Also, these routines do not always behave on
* emulated VT220 screens.
CALL "SMG$CREATE_VIRTUAL_DISPLAY"
USING BY REFERENCE ROWS
COLUMNS
DISPLAY1

CALL "SMG$CREATE_PASTEBOARD"
USING BY REFERENCE PASTE1

CALL "SMG$CREATE_VIRTUAL_KEYBOARD"
USING BY REFERENCE KEYBOARD1

MOVE 1 TO ROW
MOVE 1 TO COL
CALL "SMG$PASTE_VIRTUAL_DISPLAY"
USING BY REFERENCE DISPLAY1
PASTE1
ROW
COL

PERFORM 1000-DO-SOMETHING
* admire what we've done
CALL "LIB$WAIT"
USING BY REFERENCE DELAY-VAL
* tear it all down
CALL "SMG$DELETE_VIEWPORT"
USING BY REFERENCE DISPLAY1

CALL "SMG$DELETE_VIRTUAL_KEYBOARD"
USING BY REFERENCE KEYBOARD1

CALL "SMG$DELETE_PASTEBOARD"
USING BY REFERENCE PASTE1

CALL "SMG$DELETE_VIRTUAL_DISPLAY"
USING BY REFERENCE DISPLAY1

STOP RUN
.
/
1000-DO-SOMETHING
.

› 
› thanx
…[4 more quoted lines elided]…
› "When should we evacuate ?"
```

#### ↳ Re: CLRSCRN from cobol on VAX VMS ?

- **From:** "a.r...." <ua-author-17087529@usenetarchives.gap>
- **Date:** 1995-03-10T04:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5fc440ad7b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-MwHO5DmHK_Y@usenetarchives.gap>`
- **References:** `<ua-fallback-MwHO5DmHK_Y@usenetarchives.gap>`

```
In article <199··.@dct··c.uk>, mct··.@dct··c.uk wrote:
Using the VAX COBOL compiler it is:
*
* DISPLAY ""
* AT LINE NUMBER 1
* AT COLUMN NUMBER 1
* ERASE TO END OF SCREEN
* John

WONDERFUL ! THANKYOU THANKYOU ! I HAD TO SKIP THE COLUMN NUMBER 1 BIT TO
GET IT TO COMPILE, BUT IT WORKS !

ARTY.

"On a clear disk, you can seek for ever .."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
