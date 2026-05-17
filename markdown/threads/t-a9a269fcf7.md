[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking modem status with Cobol?

_1 message · 1 participant · 1996-04_

---

### Checking modem status with Cobol?

- **From:** "guyf..." <ua-author-17086728@usenetarchives.gap>
- **Date:** 1996-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kost9$gvb@ns.eirenet.net>`

```
Does anyone know how to check the modem status after dialing a number?
What follows is a Class I wrote with two methods. One is to dial a number
passed to it and the other is to reset the modem. My problem is I have to
reset the modem by clicking on a button on the GUI interface to reset the
modem. Basically I need to check for a "busy" status, "connected" status
or count the number of times the dialed number rings and reset the modem
after a predetermined number of rings.

I am using MF Workbench 4.0 and Dialog System with Windows 95.

Any help in the way of code fragments demonstrating a solution or
suggestions on how to do this would be greatly appreciated.

Anyone who wishes to adapt the code for use with a non OO Cobol are quite
welcome to do so.


$SET MFOO LINKCOUNT"160"

******************************************************************
******************************************************************
******************************************************************
** TELEPHONE - METHODS USED IN DIALING, RESETTING THE MODEM AND
** CHECKING RETURN CODES FROM THE MODEM.
******************************************************************
******************************************************************
CLASS-ID. TELEPHONE
DATA IS PROTECTED
INHERITS FROM Base.

*AUTHOR. G FOUNTAIN.
* ARRAY SYSTEMS.
* RATHCALLAN.
* LADYSBRIDGE.
* CO. CORK.
* PHONE/FAX - + 353 (0)21 667203.
* INTERNET - GUY··.@EIR··T.NET.
*REVIEWED BY. REVIEWER'S NAME.
DATE-WRITTEN. * DATE CODING STARTED.
*DATE-REVISED. * DATE OF REVISION.
* * INSERT LATEST DATE AT TOP.
DATE-COMPILED.
*PROGRAM-STATUS. M.
* U = UNMODIFIED SKELETON M = MODIFIED SKELETON
* C = CODED T = TESTED
* P = PRODUCTION R = UNDER REVISION

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
******************************************************************
******************************************************************
** ALL SELECT STATEMENTS FOR ALL FILES USED BY THE SYSTEM,
** OTHER THAN THE PRINT FILE, WILL BE MAINTAINED IN A COPY
** LIBRARY. THE FORMAT OF THE COPY FILE NAMES WILL BE
** "D:SLCTXXXX.CPY". THE "D" WILL SPECIFIY THE DRIVE AND THE
** "XXXX" WILL BE THE FIRST FOUR POSITIONS OF THE FILENAME TO
** BE SELECTED.
******************************************************************
******************************************************************
000100 SELECT DIALFILE
000110 ASSIGN TO COMM-PORT;
000120 ORGANIZATION IS LINE SEQUENTIAL;
FILE STATUS DIAL-STAT.

OBJECT SECTION.
******************************************************************
******************************************************************
** Insert names of other classes used here
******************************************************************
******************************************************************
CLASS-CONTROL.
DATEANDTIME IS CLASS "dateandtime"
PRACTICE IS CLASS "practice"
TELEPHONE IS CLASS "telephone"
Base IS CLASS "base".

DATA DIVISION.
FILE SECTION.
******************************************************************
******************************************************************
** ALL FD'S FOR ALL FILES USED BY THE SYSTEM, OTHER THAN THE
** PRINT FILE, WILL BE MAINTAINED IN A COPY LIBRARY. THE
** FORMAT OF THE COPY FILE NAMES WILL BE "D:XXXXFD.CPY". THE
** "D" WILL SPECIFY THE THE DRIVE AND THE "XXXX" WILL BE A
** MEANINGFUL ABBREVIATION OR EXPANSION OF THE TYPE/PURPOSE OF
** THE FILE.
******************************************************************
******************************************************************
000100 FD DIALFILE
RECORD IS VARYING IN SIZE
FROM 1 TO 40 CHARACTERS
DEPENDING ON DIAL-LGTH
DATA RECORD IS DIALRECD.
000140 01 DIALRECD.
000150 03 DIAL-RECD PIC X
OCCURS 1 TO 40 DEPENDING ON DIAL-LGTH.

WORKING-STORAGE SECTION.
******************************************************************
******************************************************************
** THE FOLLOWING ENTRIES WILL BE STANDARD IN THE WORKING-
** STORAGE SECTION FOR ALL SYSTEMS DEVELOPED BY ARRAY SYSTEMS.
** ALL SECTIONS MAY BE ADDED TO IF REQUIRED.
******************************************************************
** ALL LEVEL NUMBERS WILL BE IN INCREMENTS OF 2.
** THERE WILL BE 2 POSITIONS BETWEEN THE LEVEL & DATA NAME.
** ALL INDENTATION WILL BE IN INCREMENTS OF 4.
** ALL PICTURE CLAUSES WILL BEGIN IN POSITION 40.
** THE VALUE OR OCCURS CLAUSE WILL BEGIN IN POSITION 56.
******************************************************************
******************************************************************
01 FILLER PIC X.

OBJECT-STORAGE SECTION.
******************************************************************
******************************************************************
** Insert your class data declarations here
******************************************************************
******************************************************************
77 DIAL-LGTH PIC 99 VALUE 1.
77 DIAL-STAT PIC XX.
77 DLAY-TIME PIC 9(8).
77 ONE PIC 9 VALUE 1.

01 COMM-DIAL.
03 FILLER PIC X(4) VALUE
"ATDT".
03 DIAL-NMBR PIC X(15).
01 COMM-HANG PIC X(4) VALUE "ATH0".
*01 COMM-INIT PIC X(16) VALUE
* "AT&FL3X4V0&C1&D2".
01 COMM-INIT PIC X(04) VALUE
"ATL3".
01 COMM-PORT.
03 FILLER PIC XXX VALUE "COM".
03 MODM-PORT-NMBR PIC 9.
03 FILLER PIC X VALUE ":".
01 COMM-RSET PIC XXX VALUE "ATZ".

******************************************************************
******************************************************************
** INITIALIZES MODEM AND DIALS NUMBER PASSED TO METHOD
******************************************************************
******************************************************************
METHOD-ID. "dialphone".

LOCAL-STORAGE SECTION.
******************************************************************
******************************************************************
** Insert your method local data declarations here
******************************************************************
******************************************************************
77 FILLER PIC X.

LINKAGE SECTION.
******************************************************************
******************************************************************
** Insert your linkage data declarations here
******************************************************************
******************************************************************
77 PHON-NMBR PIC X(15).
77 MODM-STAT PIC XX.

******************************************************************
******************************************************************
** Insert your procedure specification here
******************************************************************
******************************************************************
PROCEDURE DIVISION
USING PHON-NMBR
RETURNING MODM-STAT.
******************************************************************
******************************************************************
** Insert your procedure code here
******************************************************************
******************************************************************

0000-MAIN-PROC.
INVOKE PRACTICE "getmodemport"
RETURNING MODM-PORT-NMBR.
MOVE PHON-NMBR TO DIAL-NMBR.
OPEN OUTPUT DIALFILE.
MOVE 4 TO DIAL-LGTH
MOVE COMM-INIT TO DIALRECD.
WRITE DIALRECD.
MOVE 50 TO DLAY-TIME.
INVOKE DATEANDTIME "delayloop"
USING DLAY-TIME.
MOVE 19 TO DIAL-LGTH
MOVE COMM-DIAL TO DIALRECD.
WRITE DIALRECD.
CLOSE DIALFILE.

EXIT METHOD.

END METHOD "dialphone".

******************************************************************
******************************************************************
** RESET MODEM
******************************************************************
******************************************************************
METHOD-ID. "resetmodem".

LOCAL-STORAGE SECTION.
******************************************************************
******************************************************************
** Insert your method local data declarations here
******************************************************************
******************************************************************
77 FILLER PIC X.

LINKAGE SECTION.
******************************************************************
******************************************************************
** Insert your linkage data declarations here
******************************************************************
******************************************************************
77 FILLER PIC X.

******************************************************************
******************************************************************
** Insert your procedure specification here
******************************************************************
******************************************************************
PROCEDURE DIVISION.

******************************************************************
******************************************************************
** Insert your procedure code here
******************************************************************
******************************************************************

0000-MAIN-PROC.

OPEN OUTPUT DIALFILE.
MOVE 4 TO DIAL-LGTH.
MOVE COMM-HANG TO DIALRECD.
WRITE DIALRECD.
CLOSE DIALFILE.

EXIT METHOD.

END METHOD "resetmodem".

OBJECT.

OBJECT-STORAGE SECTION.

01 FILLER PIC X.

END OBJECT.

END CLASS TELEPHONE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
