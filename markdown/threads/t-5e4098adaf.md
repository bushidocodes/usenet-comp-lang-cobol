[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Runtime error

_4 messages · 4 participants · 2009-03_

---

### Runtime error

- **From:** Anna <colleen1980@gmail.com>
- **Date:** 2009-03-27T22:43:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<caeb4390-2b0b-415d-94af-bdaab2158839@w34g2000yqm.googlegroups.com>`

```
Hi guys: Can any one please tell me why it gives run time error in the
main program. I write two files. First one i create a blank data file.
When i run the second file it gives a runtime error needs help.

Thanks.


 IDENTIFICATION DIVISION.
 PROGRAM-ID. VNDBLD01.
*------------------------------------------------
* Create an Empty Vendor File.
*------------------------------------------------
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.

     SELECT VENDOR-FILE
         ASSIGN TO "vendor"
         ORGANIZATION IS INDEXED
         RECORD KEY IS VENDOR-NUMBER
         ACCESS MODE IS DYNAMIC.

 DATA DIVISION.
 FILE SECTION.

 FD  VENDOR-FILE
     LABEL RECORDS ARE STANDARD.
 01  VENDOR-RECORD.
     05  VENDOR-NUMBER                    PIC 9(5).
     05  VENDOR-NAME                      PIC X(30).
     05  VENDOR-ADDRESS-1                 PIC X(30).
     05  VENDOR-ADDRESS-2                 PIC X(30).
     05  VENDOR-CITY                      PIC X(20).
     05  VENDOR-STATE                     PIC X(2).
     05  VENDOR-ZIP                       PIC X(10).
     05  VENDOR-CONTACT                   PIC X(30).
     05  VENDOR-PHONE                     PIC X(15).

 WORKING-STORAGE SECTION.

 PROCEDURE DIVISION.
 PROGRAM-BEGIN.
     OPEN OUTPUT VENDOR-FILE.
     CLOSE VENDOR-FILE.

 PROGRAM-DONE.
     STOP RUN.
================================================================
 IDENTIFICATION DIVISION.
 PROGRAM-ID. VNDMNT01.
*---------------------------------
* Add, Change, Inquire and Delete
* for the Vendor File.
*---------------------------------
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
		SELECT VENDOR-FILE ASSIGN TO "vendor"
			ORGANIZATION IS INDEXED
			RECORD KEY IS VENDOR-NUMBER
			ACCESS MODE IS DYNAMIC.
 DATA DIVISION.
 FILE SECTION.
	FD VENDOR-FILE
		LABEL RECORDS ARE STANDARD.
	01 VENDOR-RECORD.
		05 VENDOR-NUMBER 	PIC 9(5).
		05 VENDOR-NAME 		PIC X(30).
		05 VENDOR-ADDRESS-1 PIC X(30).
		05 VENDOR-ADDRESS-2 PIC X(30).
		05 VENDOR-CITY 		PIC X(20).
		05 VENDOR-STATE 	PIC X(30).
		05 VENDOR-ZIP 		PIC X(10).
		05 VENDOR-CONTACT PIC X(30).
		05 VENDOR-PHONE PIC X(15).
 WORKING-STORAGE SECTION.

 77  MENU-PICK                    PIC 9.
     88  MENU-PICK-IS-VALID       VALUES 0 THRU 4.

 77  THE-MODE                     PIC X(7).
 77  WHICH-FIELD                  PIC 9.
 77  OK-TO-DELETE                 PIC X.
 77  RECORD-FOUND                 PIC X.
 77  VENDOR-NUMBER-FIELD          PIC 99999.

 PROCEDURE DIVISION.
 PROGRAM-BEGIN.
     PERFORM OPENING-PROCEDURE.
     PERFORM MAIN-PROCESS.
     PERFORM CLOSING-PROCEDURE.

 PROGRAM-DONE.
     STOP RUN.

 OPENING-PROCEDURE.
     OPEN I-O VENDOR-FILE.

 CLOSING-PROCEDURE.
     CLOSE VENDOR-FILE.


 MAIN-PROCESS.
     PERFORM GET-MENU-PICK.
     PERFORM MAINTAIN-THE-FILE
         UNTIL MENU-PICK = 0.

*---------------------------------
* MENU
*---------------------------------
 GET-MENU-PICK.
     PERFORM DISPLAY-THE-MENU.
     PERFORM GET-THE-PICK.
     PERFORM MENU-RETRY
         UNTIL MENU-PICK-IS-VALID.

 DISPLAY-THE-MENU.
     PERFORM CLEAR-SCREEN.
     DISPLAY "    PLEASE SELECT:".
     DISPLAY " ".
     DISPLAY "          1.  ADD RECORDS".
     DISPLAY "          2.  CHANGE A RECORD".
     DISPLAY "          3.  LOOK UP A RECORD".
     DISPLAY "          4.  DELETE A RECORD".
     DISPLAY " ".
     DISPLAY "          0.  EXIT".
     PERFORM SCROLL-LINE 8 TIMES.

 GET-THE-PICK.
     DISPLAY "YOUR CHOICE (0-4)?".
     ACCEPT MENU-PICK.
 MENU-RETRY.
     DISPLAY "INVALID SELECTION - PLEASE RE-TRY.".
     PERFORM GET-THE-PICK.
 CLEAR-SCREEN.
     PERFORM SCROLL-LINE 25 TIMES.

 SCROLL-LINE.
     DISPLAY " ".

 MAINTAIN-THE-FILE.
     PERFORM DO-THE-PICK.
     PERFORM GET-MENU-PICK.

 DO-THE-PICK.
     IF MENU-PICK = 1
         PERFORM ADD-MODE
     ELSE
     IF MENU-PICK = 2
         PERFORM CHANGE-MODE
     ELSE
     IF MENU-PICK = 3
         PERFORM INQUIRE-MODE
     ELSE
     IF MENU-PICK = 4
         PERFORM DELETE-MODE.

*---------------------------------
* ADD
*---------------------------------
 ADD-MODE.
     MOVE "ADD" TO THE-MODE.
     PERFORM GET-NEW-VENDOR-NUMBER.
     PERFORM ADD-RECORDS
        UNTIL VENDOR-NUMBER = ZEROES.

 GET-NEW-VENDOR-NUMBER.
     PERFORM INIT-VENDOR-RECORD.
     PERFORM ENTER-VENDOR-NUMBER.
     MOVE "Y" TO RECORD-FOUND.
     PERFORM FIND-NEW-VENDOR-RECORD
         UNTIL RECORD-FOUND = "N" OR
               VENDOR-NUMBER = ZEROES.

 FIND-NEW-VENDOR-RECORD.
     PERFORM READ-VENDOR-RECORD.
     IF RECORD-FOUND = "Y"
         DISPLAY "RECORD ALREADY ON FILE"
         PERFORM ENTER-VENDOR-NUMBER.

 ADD-RECORDS.
     PERFORM ENTER-REMAINING-FIELDS.
     PERFORM WRITE-VENDOR-RECORD.
     PERFORM GET-NEW-VENDOR-NUMBER.

 ENTER-REMAINING-FIELDS.
     PERFORM ENTER-VENDOR-NAME.
     PERFORM ENTER-VENDOR-ADDRESS-1.
     PERFORM ENTER-VENDOR-ADDRESS-2.
     PERFORM ENTER-VENDOR-CITY.
     PERFORM ENTER-VENDOR-STATE.
     PERFORM ENTER-VENDOR-ZIP.
     PERFORM ENTER-VENDOR-CONTACT.
     PERFORM ENTER-VENDOR-PHONE.

*---------------------------------
* CHANGE
*---------------------------------
 CHANGE-MODE.
     MOVE "CHANGE" TO THE-MODE.
     PERFORM GET-VENDOR-RECORD.
     PERFORM CHANGE-RECORDS
        UNTIL VENDOR-NUMBER = ZEROES.

 CHANGE-RECORDS.
     PERFORM GET-FIELD-TO-CHANGE.
     PERFORM CHANGE-ONE-FIELD
         UNTIL WHICH-FIELD = ZERO.
     PERFORM GET-VENDOR-RECORD.

 GET-FIELD-TO-CHANGE.
     PERFORM DISPLAY-ALL-FIELDS.
     PERFORM ASK-WHICH-FIELD.

 ASK-WHICH-FIELD.
     DISPLAY "ENTER THE NUMBER OF THE FIELD".
     DISPLAY "TO CHANGE (1-8) OR 0 TO EXIT".
     ACCEPT WHICH-FIELD.
     IF WHICH-FIELD > 8
         DISPLAY "INVALID ENTRY".

 CHANGE-ONE-FIELD.
     PERFORM CHANGE-THIS-FIELD.
     PERFORM GET-FIELD-TO-CHANGE.

 CHANGE-THIS-FIELD.
     IF WHICH-FIELD = 1
         PERFORM ENTER-VENDOR-NAME.
     IF WHICH-FIELD = 2
         PERFORM ENTER-VENDOR-ADDRESS-1.
     IF WHICH-FIELD = 3
         PERFORM ENTER-VENDOR-ADDRESS-2.
     IF WHICH-FIELD = 4
         PERFORM ENTER-VENDOR-CITY.
     IF WHICH-FIELD = 5
         PERFORM ENTER-VENDOR-STATE.
     IF WHICH-FIELD = 6
         PERFORM ENTER-VENDOR-ZIP.
     IF WHICH-FIELD = 7
         PERFORM ENTER-VENDOR-CONTACT.
     IF WHICH-FIELD = 8
         PERFORM ENTER-VENDOR-PHONE.

     PERFORM REWRITE-VENDOR-RECORD.

*---------------------------------
* INQUIRE
*---------------------------------
 INQUIRE-MODE.
     MOVE "DISPLAY" TO THE-MODE.
     PERFORM GET-VENDOR-RECORD.
     PERFORM INQUIRE-RECORDS
        UNTIL VENDOR-NUMBER = ZEROES.

 INQUIRE-RECORDS.
     PERFORM DISPLAY-ALL-FIELDS.
     PERFORM GET-VENDOR-RECORD.

*---------------------------------
* DELETE
*---------------------------------
 DELETE-MODE.
     MOVE "DELETE" TO THE-MODE.
     PERFORM GET-VENDOR-RECORD.
     PERFORM DELETE-RECORDS
        UNTIL VENDOR-NUMBER = ZEROES.

 DELETE-RECORDS.
     PERFORM DISPLAY-ALL-FIELDS.
     MOVE "X" TO OK-TO-DELETE.

     PERFORM ASK-TO-DELETE
        UNTIL OK-TO-DELETE = "Y" OR "N".

     IF OK-TO-DELETE = "Y"
         PERFORM DELETE-VENDOR-RECORD.

     PERFORM GET-VENDOR-RECORD.

 ASK-TO-DELETE.
     DISPLAY "DELETE THIS RECORD (Y/N)?".
     ACCEPT OK-TO-DELETE.
     IF OK-TO-DELETE = "y"
         MOVE "Y" TO OK-TO-DELETE.
     IF OK-TO-DELETE = "n"
         MOVE "N" TO OK-TO-DELETE.
     IF OK-TO-DELETE NOT = "Y" AND
        OK-TO-DELETE NOT = "N"
         DISPLAY "YOU MUST ENTER YES OR NO".

*---------------------------------
* Routines shared by all modes
*---------------------------------
 INIT-VENDOR-RECORD.
     MOVE SPACE TO VENDOR-RECORD.
     MOVE ZEROES TO VENDOR-NUMBER.

 ENTER-VENDOR-NUMBER.
     DISPLAY " ".
     DISPLAY "ENTER VENDOR NUMBER OF THE VENDOR" .
     DISPLAY "TO " THE-MODE " (1-99999)".
     DISPLAY "ENTER 0 TO STOP ENTRY".
     ACCEPT VENDOR-NUMBER-FIELD FROM CONSOLE.
*OR  ACCEPT VENDOR-NUMBER-FIELD WITH CONVERSION.

     MOVE VENDOR-NUMBER-FIELD TO VENDOR-NUMBER.

 GET-VENDOR-RECORD.
     PERFORM INIT-VENDOR-RECORD.
     PERFORM ENTER-VENDOR-NUMBER.
     MOVE "N" TO RECORD-FOUND.
     PERFORM FIND-VENDOR-RECORD
         UNTIL RECORD-FOUND = "Y" OR
               VENDOR-NUMBER = ZEROES.

*---------------------------------
* Routines shared Add and Change
*---------------------------------
 FIND-VENDOR-RECORD.
     PERFORM READ-VENDOR-RECORD.
     IF RECORD-FOUND = "N"
         DISPLAY "RECORD NOT FOUND"
         PERFORM ENTER-VENDOR-NUMBER.

 ENTER-VENDOR-NAME.
     DISPLAY "ENTER VENDOR NAME".
     ACCEPT VENDOR-NAME FROM CONSOLE.

 ENTER-VENDOR-ADDRESS-1.
     DISPLAY "ENTER VENDOR ADDRESS-1".
     ACCEPT VENDOR-ADDRESS-1 FROM CONSOLE.

 ENTER-VENDOR-ADDRESS-2.
     DISPLAY "ENTER VENDOR ADDRESS-2".
     ACCEPT VENDOR-ADDRESS-2 FROM CONSOLE.

 ENTER-VENDOR-CITY.
     DISPLAY "ENTER VENDOR CITY".
     ACCEPT VENDOR-CITY FROM CONSOLE.

 ENTER-VENDOR-STATE.
     DISPLAY "ENTER VENDOR STATE".
     ACCEPT VENDOR-STATE FROM CONSOLE.

 ENTER-VENDOR-ZIP.
     DISPLAY "ENTER VENDOR ZIP".
     ACCEPT VENDOR-ZIP FROM CONSOLE.

 ENTER-VENDOR-CONTACT.
     DISPLAY "ENTER VENDOR CONTACT".
     ACCEPT VENDOR-CONTACT FROM CONSOLE.

 ENTER-VENDOR-PHONE.
     DISPLAY "ENTER VENDOR PHONE".
     ACCEPT VENDOR-PHONE FROM CONSOLE.

*---------------------------------
* Routines shared by Change,
* Inquire and Delete
*---------------------------------
 DISPLAY-ALL-FIELDS.
     DISPLAY " ".
     PERFORM DISPLAY-VENDOR-NUMBER.
     PERFORM DISPLAY-VENDOR-NAME.
     PERFORM DISPLAY-VENDOR-ADDRESS-1.
     PERFORM DISPLAY-VENDOR-ADDRESS-2.
     PERFORM DISPLAY-VENDOR-CITY.
     PERFORM DISPLAY-VENDOR-STATE.
     PERFORM DISPLAY-VENDOR-ZIP.
     PERFORM DISPLAY-VENDOR-CONTACT.
     PERFORM DISPLAY-VENDOR-PHONE.
     DISPLAY " ".

 DISPLAY-VENDOR-NUMBER.
     DISPLAY "   VENDOR NUMBER: " VENDOR-NUMBER.

 DISPLAY-VENDOR-NAME.
     DISPLAY "1. VENDOR NAME: " VENDOR-NAME.

 DISPLAY-VENDOR-ADDRESS-1.
     DISPLAY "2. VENDOR ADDRESS-1: " VENDOR-ADDRESS-1.

 DISPLAY-VENDOR-ADDRESS-2.
     DISPLAY "3. VENDOR ADDRESS-2: " VENDOR-ADDRESS-2.

 DISPLAY-VENDOR-CITY.
     DISPLAY "4. VENDOR CITY: " VENDOR-CITY.

 DISPLAY-VENDOR-STATE.
     DISPLAY "5. VENDOR STATE: " VENDOR-STATE.

 DISPLAY-VENDOR-ZIP.
     DISPLAY "6. VENDOR ZIP: " VENDOR-ZIP.

 DISPLAY-VENDOR-CONTACT.
     DISPLAY "7. VENDOR CONTACT: " VENDOR-CONTACT.

 DISPLAY-VENDOR-PHONE.
     DISPLAY "8. VENDOR PHONE: " VENDOR-PHONE.

*---------------------------------
* File I-O Routines
*---------------------------------
 READ-VENDOR-RECORD.
     MOVE "Y" TO RECORD-FOUND.
     READ VENDOR-FILE RECORD
       INVALID KEY
          MOVE "N" TO RECORD-FOUND.

*or  READ VENDOR-FILE RECORD WITH LOCK
*      INVALID KEY
*         MOVE "N" TO RECORD-FOUND.

*or  READ VENDOR-FILE RECORD WITH HOLD
*      INVALID KEY
*         MOVE "N" TO RECORD-FOUND.

 WRITE-VENDOR-RECORD.
     WRITE VENDOR-RECORD
         INVALID KEY
         DISPLAY "RECORD ALREADY ON FILE".

 REWRITE-VENDOR-RECORD.
     REWRITE VENDOR-RECORD
         INVALID KEY
         DISPLAY "ERROR REWRITING VENDOR RECORD".

 DELETE-VENDOR-RECORD.
     DELETE VENDOR-FILE RECORD
         INVALID KEY
         DISPLAY "ERROR DELETING VENDOR RECORD".
---------------------------------------------------------------------------------------
RUN TIME ERROR
NetCOBOL COBOL ERROR REPORT

<<Summary>>
 The COBOL run-time message occurred:
  Application       : C:\Documents and Settings\Kathy\My Documents
\NetCOBOL Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe(PID=00000860)
  Exception Number  : JMP0310I-U [PID:00000860 TID:00000114] OPEN
ERROR. FILE=vendor. 'INV-LRECL '. PGM=VNDMNT01 LINE=49.1
  Generation Time   : 03/28/2009(0:31:47)
  Generation Module : C:\Documents and Settings\Kathy\My Documents
\NetCOBOL Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
  Time Stamp        : 03/28/2009(0:31:28)
  File Size         : 75804bytes

<<Detail>>
  Thread ID    : 00000114
  Register     : EAX=0012BF8C  EBX=00000065  ECX=E9999999
EDX=00050001  ESI=00000000
               : EDI=00156DBC  EIP=7C812A5B  ESP=0012BF88
EBP=0012BFDC  EFL=00000246
               : CS=001B  SS=0023  DS=0023  ES=0023  FS=003B  GS=0000
  Stack Commit : 0000A000 (Top:00130000, Base:00126000)
  Instruction  : Address  +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +a +b +c +d +e
+f
                 7C812A4B 8D 7D C4 F3 A5 5F 8D 45 B0 50 FF 15 08 15 80
7C
         FAULT ->7C812A5B 5E C9 C2 10 00 85 FF 0F 8E 36 93 FF FF 8B 55
FC

  Module File : C:\Documents and Settings\Kathy\My Documents\NetCOBOL
Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
  Section Relative Position : .text+000002FE
  Symbol Relative Position : VNDMNT01+000002FE
  Compilation Information : ASCII, SINGLE THREAD, NOOPTIMIZE
  External Program/Class : VNDMNT01
  Source File : Vndmnt01.cob
  Source Line : 49

 <Call Stack>
[  1]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BKATCH.dll
  Section Relative Position : .text+00002DE9
  Export Relative Position : NotifyExecErrorInfo+00000169
[  2]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIPRCT.dll
  Section Relative Position : .text+00025AA2
  Export Relative Position : JMP1MESM+00002252
[  3]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIPRCT.dll
  Section Relative Position : .text+00023ADF
  Export Relative Position : JMP1MESM+0000028F
[  4]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIPRCT.dll
  Section Relative Position : .text+00046A6E
  Export Relative Position : JMP5IOER+0000120E
[  5]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIIO.dll
  Section Relative Position : .text+00010935
  Export Relative Position : JMP5VIXD+00003FF5
[  6]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIIO.dll
  Section Relative Position : .text+0000CFB5
  Export Relative Position : JMP5VIXD+00000675
[  7]---------------------------------------------------------------------------------
  Module File : C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIIO.dll
  Section Relative Position : .text+0000CB75
  Export Relative Position : JMP5VIXD+00000235
[  8]---------------------------------------------------------------------------------
  Module File : C:\Documents and Settings\Kathy\My Documents\NetCOBOL
Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
  Section Relative Position : .text+00000302
  Symbol Relative Position : VNDMNT01+00000302
  Compilation Information : ASCII, SINGLE THREAD, NOOPTIMIZE
  External Program/Class : VNDMNT01
  Source File : Vndmnt01.cob
  Source Line : 49
[  9]---------------------------------------------------------------------------------
  Module File : C:\Documents and Settings\Kathy\My Documents\NetCOBOL
Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
  Section Relative Position : .text+0000000A
  Symbol Relative Position : VNDMNT01+0000000A
[ 10]---------------------------------------------------------------------------------
  Module File : C:\Documents and Settings\Kathy\My Documents\NetCOBOL
Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
  Section Relative Position : .text+00005E64
  Export Relative Position : VNDNEW01+00001B3C
  Symbol Relative Position : _WinMainCRTStartup+000000CE
[ 11]---------------------------------------------------------------------------------
  Module File : C:\WINDOWS\system32\KERNEL32.dll
  Section Relative Position : .text+00015FD7
  Export Relative Position : RegisterWaitForInputIdle+00000049

<<System Information>>
  Computer Name   : PC
  User Name       : Kathy
  Windows Version : Microsoft Windows XP
  Version Number  : 5.01.2600
  Service Pack    : Service Pack 2

<<Command Line>>
  "C:\Documents and Settings\Kathy\My Documents\NetCOBOL Studio
V10.0.0\workspace\DATAPROJ\DATAPROJ.exe"

<<Environment Variable>>
  =::=::\
  ALLUSERSPROFILE=C:\Documents and Settings\All Users
  APPDATA=C:\Documents and Settings\Kathy\Application Data
  CommonProgramFiles=C:\Program Files\Common Files
  COMPUTERNAME=PC
  ComSpec=C:\WINDOWS\system32\cmd.exe
  FP_NO_HOST_CHECK=NO
  GETMODEL=Satellite M35X
  HOMEDRIVE=C:
  HOMEPATH=\Documents and Settings\Kathy
  LIB=C:\Program Files\Fujitsu NetCOBOL for Windows\
  LOGONSERVER=\\PC
  MEFTLOGROOT=C:\MEFTLOGROOT
  NUMBER_OF_PROCESSORS=1
  OS=Windows_NT
  Path=C:\Program Files\Fujitsu NetCOBOL for Windows\;C:\WINDOWS
\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\Program Files\ATI
Technologies\ATI Control Panel;C:\Program Files\IDM Computer Solutions
\UltraEdit\
  PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH
  PROCESSOR_ARCHITECTURE=x86
  PROCESSOR_IDENTIFIER=x86 Family 6 Model 9 Stepping 5, GenuineIntel
  PROCESSOR_LEVEL=6
  PROCESSOR_REVISION=0905
  ProgramFiles=C:\Program Files
  SESSIONNAME=Console
  SystemDrive=C:
  SystemRoot=C:\WINDOWS
  TEMP=C:\DOCUME~1\Kathy\LOCALS~1\Temp
  TMP=C:\DOCUME~1\Kathy\LOCALS~1\Temp
  USERDOMAIN=PC
  USERNAME=Kathy
  USERPROFILE=C:\Documents and Settings\Kathy
  VERNUM=PSA72U-00T00U
  windir=C:\WINDOWS

<<Execution Environment Information>>
  Run-time System : V10.0.0
  Run-time Mode   : ASCII, SINGLE THREAD
  Program Name    : VNDMNT01
  .CBR File       : C:\Documents and Settings\Kathy\My Documents
\NetCOBOL Studio V10.0.0\workspace\DATAPROJ\COBOL85.CBR
    [EOF]

<<STACK/HEAP Information>>
  Stack : 00100000
  Heap  : 00100000

<<Task List>>
         0 [System Process]
         4 System
       1D8 smss.exe
       22C csrss.exe
       244 winlogon.exe
       270 services.exe
       27C lsass.exe
       33C svchost.exe
       378 svchost.exe
       3A0 svchost.exe
       3C8 svchost.exe
       420 svchost.exe
       440 svchost.exe
       4A8 ccSetMgr.exe
       51C ccEvtMgr.exe
       5B4 spoolsv.exe
       61C CeEPwrSvc.exe
       628 CFSvcs.exe
       640 COBATSVC.exe
       650 Crypserv.exe
       69C lxddcoms.exe
       6E4 navapsvc.exe
       700 SAVScan.exe
       734 svchost.exe
       740 swupdtmr.exe
       7B0 symwsc.exe
       7E8 fxssvc.exe
       694 alg.exe
       8EC explorer.exe
       9D4 wuauclt.exe
       A98 tfswctrl.exe
       AC0 ltmoh.exe
       AE8 agrsmmsg.exe
       AFC NDSTray.exe
       B04 CeEKey.exe
       B10 PadExe.exe
       B38 SmoothView.exe
       B48 ZoomingHook.exe
       B50 TPTray.exe
       B6C ccApp.exe
       B7C igfxtray.exe
       B8C hkcmd.exe
       C04 lxddmon.exe
       C10 lxddamon.exe
       C24 ctfmon.exe
       C34 msnmsgr.exe
       C40 GoogleToolbarNotifier.exe
       C50 wcescomm.exe
       CAC rapimgr.exe
       CF4 WG111v2.exe
       DBC MEMonitor.exe
       D98 VZAccess Manager.exe
       FFC emule.exe
       D14 Ivpsvmgr.exe
       D00 cbdt.exe
       A28 crp32002.ngn
       ED8 javaw.exe
       CFC iexplore.exe
       E28 WLLoginProxy.exe
       860 DATAPROJ.exe
       ED0 F3BKDSNP.exe

<<Module List>>
  00400000 - 0040F000  C:\Documents and Settings\Kathy\My Documents
\NetCOBOL Studio V10.0.0\workspace\DATAPROJ\DATAPROJ.exe
                         03/28/2009(0:31:28)
  7C900000 - 7C9B0000  C:\WINDOWS\system32\ntdll.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  7C800000 - 7C8F5000  C:\WINDOWS\system32\KERNEL32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.3119
                         04/16/2007(8:52:53)
  10000000 - 1006A000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIPRCT.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         07/18/2008(12:46:12)
  00320000 - 00364000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIIO.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         03/12/2008(13:36:20)
  00370000 - 003AF000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIFRM.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:45:58)
  7E410000 - 7E4A0000  C:\WINDOWS\system32\USER32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.3099
                         03/08/2007(8:36:28)
  77F10000 - 77F58000  C:\WINDOWS\system32\GDI32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.3466
                         10/23/2008(6:01:36)
  77DD0000 - 77E6B000  C:\WINDOWS\system32\ADVAPI32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  77E70000 - 77F02000  C:\WINDOWS\system32\RPCRT4.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.3173
                         07/09/2007(6:09:42)
  77FE0000 - 77FF1000  C:\WINDOWS\system32\Secur32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  003B0000 - 003FA000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIDBG.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         03/12/2008(13:36:20)
  00410000 - 0044A000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIOLER.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         06/03/2008(12:45:34)
  774E0000 - 7761D000  C:\WINDOWS\system32\ole32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2726
                         07/25/2005(21:39:48)
  77C10000 - 77C68000  C:\WINDOWS\system32\msvcrt.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 7.0.2600.2180
                         08/04/2004(5:00:00)
  77120000 - 771AB000  C:\WINDOWS\system32\OLEAUT32.dll
  00450000 - 00465000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIOLES.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  00470000 - 004B2000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BISCRN.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         08/20/2008(9:35:02)
  004C0000 - 00518000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BILPIO.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         03/12/2008(13:36:20)
  00530000 - 00535000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIOVLD.dll
                         FUJITSU LIMITED, NetCOBOL, 90.20.0.0
                         03/19/2007(11:21:28)
  73000000 - 73026000  C:\WINDOWS\system32\WINSPOOL.DRV
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  00540000 - 0054E000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BISQL.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  00550000 - 0056F000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIPRIO.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  00570000 - 00581000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BISCLS.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  00590000 - 0059E000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BILANP.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  005A0000 - 005BB000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIZCOM.DLL
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         01/16/2009(10:41:14)
  7C9C0000 - 7D1D6000  C:\WINDOWS\system32\SHELL32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.3402
                         07/03/2008(6:16:57)
  77F60000 - 77FD6000  C:\WINDOWS\system32\SHLWAPI.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.2995
                         09/23/2006(13:12:50)
  78130000 - 781CB000  C:\WINDOWS\WinSxS
\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-
ww_6b128700\MSVCR80.dll
                         Microsoft Corporation, Microsoft® Visual
Studio® 2005, 8.00.50727.762
                         12/01/2006(23:54:32)
  005D0000 - 005DE000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIAESV.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:45:58)
  005E0000 - 0060C000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BKATCH.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         05/30/2008(11:40:40)
  00610000 - 00621000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIEFNC.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:45:58)
  00630000 - 00666000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIEXFH.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         07/18/2008(12:46:12)
  00670000 - 00695000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BICICL.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         04/16/2008(16:59:10)
  71AD0000 - 71AD9000  C:\WINDOWS\system32\WSOCK32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  71AB0000 - 71AC7000  C:\WINDOWS\system32\WS2_32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  71AA0000 - 71AA8000  C:\WINDOWS\system32\WS2HELP.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  006A0000 - 006AF000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BINDBC.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(11:46:00)
  77C00000 - 77C08000  C:\WINDOWS\system32\VERSION.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  763B0000 - 763F9000  C:\WINDOWS\system32\comdlg32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.2180
                         08/04/2004(5:00:00)
  5D090000 - 5D12A000  C:\WINDOWS\system32\COMCTL32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.2982
                         08/25/2006(8:45:58)
  006B0000 - 006CF000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIIFNC.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         03/12/2008(13:36:20)
  006D0000 - 006E9000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIFLTE.dll
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         04/21/2008(17:28:04)
  76390000 - 763AD000  C:\WINDOWS\system32\IMM32.DLL
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  629C0000 - 629C9000  C:\WINDOWS\system32\LPK.DLL
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)
  74D90000 - 74DFB000  C:\WINDOWS\system32\USP10.dll
                         Microsoft Corporation, Microsoft(R) Uniscribe
Unicode script processor, 1.0420.2600.2180
                         08/04/2004(5:00:00)
  773D0000 - 774D3000  C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-
Controls_6595b64144ccf1df_6.0.2600.2982_x-ww_ac3f9c03\comctl32.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.2982
                         08/25/2006(8:45:55)
  00EA0000 - 00EB2000  C:\Program Files\Fujitsu NetCOBOL for Windows
\F3BIFUNC.DLL
                         FUJITSU LIMITED, NetCOBOL, V10.0.0
                         02/29/2008(18:30:00)
  5AD70000 - 5ADA8000  C:\WINDOWS\system32\uxtheme.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 6.00.2900.2180
                         08/04/2004(5:00:00)
  74720000 - 7476B000  C:\WINDOWS\system32\MSCTF.dll
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.3319
                         02/26/2008(4:59:50)
  755C0000 - 755EE000  C:\WINDOWS\system32\msctfime.ime
                         Microsoft Corporation, Microsoft® Windows®
Operating System, 5.1.2600.2180
                         08/04/2004(5:00:00)

<<Stack Summary>>
  FramePtr RetAddr  Param-01 Param-02 Param-03 Param-04 Param-05
Param-06 Param-07 Param-08 Module:Program
  0012BFDC 005E3DE9 E9999999 00000000 00000000 00000000 00156DBC
10060D30 00000000 00000000 KERNEL32.dll:RaiseException
  0012CA5C 10026AA2 004012FE 00000010 00156DBC 00000136 00000000
00000004 10060D30 00000004 F3BKATCH.dll:NotifyExecErrorInfo
  0012DF44 10024ADF 10060D30 00000136 00000000 00000004 0012DFC8
00000002 00000008 0040B27C F3BIPRCT.dll:JMP1MESM
  0012E098 10047A6E 10060D30 00000136 00000000 00000004 0012E0DC
0012FD70 0012F96C 0012F0F8 F3BIPRCT.dll:JMP1MESM
  0012FD7C 00331935 0040B27C 00000100 0040B344 01050694 00000020
0118334C 00000004 01050694 F3BIPRCT.dll:JMP5IOER
  0012FDB8 0032DFB5 0040B27C 0040B344 0040D11C 00000000 0040B344
01050694 00000001 FFFFFFFF F3BIIO.dll:JMP5VIXD
  0012FDE8 0032DB75 0040B27C 0012FE38 00000000 00000000 0040B344
0040B27C 0040D60C 01050694 F3BIIO.dll:JMP5VIXD
  0012FE24 00401302 0040B27C 00000001 0012FE38 00000001 0040B344
00F44908 00000001 0012FF1C F3BIIO.dll:JMP5VIXD
  0012FF28 0040100A 00000000 0012FFC0 00406E64 00400000 00000000
00142456 0000000A 03A5ED08 DATAPROJ.exe:VNDMNT01
  0012FF34 00406E64 00400000 00000000 00142456 0000000A 03A5ED08
00000000 7FFDF000 00000000 DATAPROJ.exe:VNDMNT01
  0012FFC0 7C816FD7 03A5ED08 00000000 7FFDF000 8054ABB8 0012FFC8
FE235020 FFFFFFFF 7C839AA8 DATAPROJ.exe:_WinMainCRTStartup
  0012FFF0 00000000 00406D96 00000000 78746341 00000020 00000001
00002498 000000C4 00000000 KERNEL32.dll:RegisterWaitForInputIdle

<<Stack Dump>>
  0012BF80  5B 2A 81 7C 8C BF 12 00 - 30 0D 06 10 99 99 99 E9  [*.|....
0.......
  0012BF90  00 00 00 00 00 00 00 00 - 5B 2A 81 7C 00 00 00 00  ........
[*.|....
  0012BFA0  98 23 15 00 B4 BF 12 00 - 92 09 91 7C 98 23 15
00  .#.........|.#..
  0012BFB0  24 99 5F 00 D8 BF 12 00 - F7 76 DD 77 CC BF 12 00
$._......v.w....
  0012BFC0  BC 6D 15 00 30 0D 06 10 - 65 00 00 00 00 00 00 00  .m..
0...e.......
  0012BFD0  00 00 00 00 00 00 00 00 - 5C CA 12 00 5C CA 12 00  ........
\...\...
  0012BFE0  E9 3D 5E 00 99 99 99 E9 - 00 00 00 00 00 00 00
00  .=^.............
  0012BFF0  00 00 00 00 BC 6D 15 00 - 30 0D 06 10 00 00 00 00  .....m..
0.......
  0012C000  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C010  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C020  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C030  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C040  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C050  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C060  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C070  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C080  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C090  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0A0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C0F0  00 00 00 00 00 00 00 00 - 00 00 00 00 0C C1 12
00  ................
  0012C100  21 C2 91 7C 31 00 00 00 - B0 C5 12 00 20 C1 12 00  !..|
1....... ...
  0012C110  F6 C1 91 7C 31 00 00 00 - 02 00 00 00 E9 FF FF FF  ...|
1...........
  0012C120  98 C5 12 00 14 C3 91 7C - 00 00 00 00 00 00 00
00  .......|........
  0012C130  9A 00 3C 01 64 BA 91 7C - 00 00 00 00 00 00 00
00  ..<.d..|........
  0012C140  00 00 00 00 00 00 00 00 - 07 00 00 00 00 00 00
00  ................
  0012C150  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C160  00 00 00 00 B0 C5 12 00 - 00 00 00 00 00 00 00
00  ................
  0012C170  01 00 00 00 50 C9 12 00 - 00 00 00 00 17 00 00
00  ....P...........
  0012C180  40 CB 12 00 17 00 00 00 - FF FF FF FF E8 C5 12 00
@...............
  0012C190  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1A0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C1F0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C200  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C210  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C220  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C230  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C240  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C250  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C260  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C270  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C280  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C290  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2A0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C2F0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C300  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C310  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C320  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C330  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C340  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C350  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C360  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C370  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C380  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C390  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3A0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C3F0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C400  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C410  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C420  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C430  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C440  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C450  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C460  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C470  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C480  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C490  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4A0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C4F0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C500  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C510  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C520  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C530  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C540  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C550  EA D4 90 7C FF 80 91 7C - FF FF FF FF 90 C5 12
00  ...|...|........
  0012C560  6A 12 00 00 88 C5 12 00 - FF 1B 91 7C 00 00 14 00
j..........|....
  0012C570  B0 4C 15 00 00 00 14 00 - B0 4C 15 00 01 09 00
00  .L.......L......
  0012C580  40 06 14 00 6A 08 00 00 - BC C5 12 00 5D 82 91 7C
@...j.......]..|
  0012C590  6A 12 00 00 03 92 00 00 - D0 C5 12 00 D2 C2 91 7C
j..............|
  0012C5A0  B0 C5 12 00 4C C9 12 00 - E4 C5 12 00 9A 00 3C
01  ....L.........<.
  0012C5B0  C9 00 3C 01 36 FF 00 00 - 9A 00 3C 01 42 00 00 00  ..<.
6.....<.B...
  0012C5C0  E8 C7 12 00 F4 B5 91 7C - 86 B6 91 7C 00 00 00
00  .......|...|....
  0012C5D0  90 C9 12 00 C8 99 92 7C - 9A 00 3C 01 B3 7F 00
00  .......|..<.....
  0012C5E0  4C C9 12 00 40 CB 12 00 - 00 00 00 00 02 00 00 00
L...@...........
  0012C5F0  00 28 00 00 00 00 00 00 - C9 98 92 7C 38 4C 15 00  .
(.........|8L..
  0012C600  50 4C 15 00 70 4C 15 00 - 90 4C 15 00 F0 DD 12 00
PL..pL...L......
  0012C610  40 CB 12 00 00 00 00 00 - 00 00 00 00 00 00 00 00
@...............
  0012C620  00 00 00 00 00 00 00 00 - 40 06 14 00 00 00 00
00  ........@.......
  0012C630  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C640  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C650  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C660  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C670  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C680  00 00 00 00 78 01 14 00 - 00 00 00 00 00 00 00
00  ....x...........
  0012C690  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C6A0  78 01 14 00 90 99 15 00 - 00 00 00 00 00 00 00 00
x...............
  0012C6B0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C6C0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C6D0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C6E0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C6F0  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C700  00 00 00 00 00 00 00 00 - 00 00 00 00 00 00 00
00  ................
  0012C710  00 00 00 00 96 00 00 00 - 00 00 00 00 50 C7 12
00  ............P...
  0012C720  00 00 14 00 32 07 91 7C - 0C 00 00 00 C8 08 14 00  ....
2..|........
  0012C730  00 00 14 00 E8 30 15 00 - 28 C7 12 00 00 00 00 00  .....0..
(.......
  0012C740  6C C9 12 00 18 EE 90 7C - 38 07 91 7C FF FF FF FF  l......|
8..|....
  0012C750  32 07 91 7C AB 06 91 7C - EB 06 91 7C D4 C9 12 00
2..|...|...|....
  0012C760  DC C9 12 00 00 00 00 00 - 00 00 14 00 32 07 91
7C  ............2..|
  0012C770  38 C9 12 00 B0 2F 14 00 - 38 C8 12 00 C0 1D 15 00
8..../..8.......
```

#### ↳ Re: Runtime error

- **From:** Louis Krupp <lkrupp_nospam@pssw.com.invalid>
- **Date:** 2009-03-28T00:58:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49cdcab0$1@news.x-privat.org>`
- **In-Reply-To:** `<caeb4390-2b0b-415d-94af-bdaab2158839@w34g2000yqm.googlegroups.com>`
- **References:** `<caeb4390-2b0b-415d-94af-bdaab2158839@w34g2000yqm.googlegroups.com>`

```
Anna wrote:
> Hi guys: Can any one please tell me why it gives run time error in the
> main program. I write two files. First one i create a blank data file.
…[72 more quoted lines elided]…
> 		05 VENDOR-PHONE PIC X(15).
<snip>
> ---------------------------------------------------------------------------------------
> RUN TIME ERROR
…[7 more quoted lines elided]…
> ERROR. FILE=vendor. 'INV-LRECL '. PGM=VNDMNT01 LINE=49.1
<snip>

Wild guess:

INV-LRECL means "invalid logical record length."  You create the file 
with one record layout and try to reopen it with another record layout, 
and the two have different sizes.

In this case, VENDOR-STATE is defined as PIC X(30) in one program and 
PIC X(2) in the other.

You might want to use a copybook so you only have to define the record 
layout in one file.

Louis
```

#### ↳ Re: Runtime error

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-03-28T11:33:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<actzl.49553$3S3.46351@newsfe22.iad>`
- **References:** `<caeb4390-2b0b-415d-94af-bdaab2158839@w34g2000yqm.googlegroups.com>`

```
You might try varying the ACCESS MODE in the First program ...

PL



Hi guys: Can any one please tell me why it gives run time error in the
main program. I write two files. First one i create a blank data file.
When i run the second file it gives a runtime error needs help.

Thanks.


 IDENTIFICATION DIVISION.
 PROGRAM-ID. VNDBLD01.
*------------------------------------------------
* Create an Empty Vendor File.
*------------------------------------------------
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.

     SELECT VENDOR-FILE
         ASSIGN TO "vendor"
         ORGANIZATION IS INDEXED
         RECORD KEY IS VENDOR-NUMBER
         ACCESS MODE IS DYNAMIC.

 DATA DIVISION.
 FILE SECTION.

 FD  VENDOR-FILE
     LABEL RECORDS ARE STANDARD.
```

#### ↳ Re: Runtime error

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-03-28T15:20:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TvSdnavR2coeG1PUnZ2dnUVZ_oednZ2d@earthlink.com>`
- **References:** `<caeb4390-2b0b-415d-94af-bdaab2158839@w34g2000yqm.googlegroups.com>`

```
Anna wrote:
> Hi guys: Can any one please tell me why it gives run time error in the
> main program. I write two files. First one i create a blank data file.
> When i run the second file it gives a runtime error needs help.
>

The records in the two programs are of different lengths. It IS possible to 
have variable length records in an ISAM file, but not the way you've set it 
up.

It's not necessary to have a stand-alone program to create the file. You can 
create the file in your main program viz.:

OPENING-PROCEDURE.
   OPEN OUTPUT VENDOR-FILE.
   CLOSE VENDOR-FILE.
   OPEN I-O VENDOR-FILE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
