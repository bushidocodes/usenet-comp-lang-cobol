[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Illegal File name Problem

_1 message · 1 participant · 1999-03_

---

### Illegal File name Problem

- **From:** charlie.smith@sdpsbbs.sdps-bbs.com
- **Date:** 1999-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<920270346.1@sdpsbbs.sdps-bbs.com>`

```
 "<> From: "Jim" <jimyt@REMOVEMEyahoo.com>

 "<> OS: MS Windows 98
 "<> Compiler: Microfocus Animator 2

 "<> Dear Group,

 "<> I am having problems with a file in the following program, the
 error I
 "<> am getting suggests that I have illegal characters in the file
 name
 "<> "CUSTMAST.MF". I have tried renaming the file, rewriting the
 code,
 "<> changing case etc but an unable to find an answer, please help.

 "<> Error: illegal character in filename (004)

 "<> Relevant sections of code:

 "<>
 ---------------------------------------------------------------------
-
 "<> ----- --------------
 "<> 000050 FILE-CONTROL.
 "<> 000060     SELECT SORTED-FILE ASSIGN TO "MT25SD.DAT"
 "<> 000070         ORGANIZATION IS LINE SEQUENTIAL.
 "<> 000090     SELECT CUSTOMER-MASTER ASSIGN TO "CUSTMAST.MF"
 "<> 000100         ORGANIZATION IS LINE SEQUENTIAL.
 "<> 000090     SELECT NEW-CUST-MASTER ASSIGN TO "MT25NF.DAT"
 "<> 000100         ORGANIZATION IS LINE SEQUENTIAL.
 "<> SELECT STOCK-MASTER-FILE ASSIGN TO "STCKMAST.IDX"
 "<> ORGANIZATION IS INDEXED
 "<> ACCESS MODE RANDOM
 "<> RECORD KEY IS  S-PART-NUM.
 "<> 000080    SELECT PRINT-FILE ASSIGN TO PRINTER.
 "<>
 ---------------------------------------------------------------------
-
 "<> ----- ----------------
 "<> 001551 INITIAL-ROUTINE.
 "<> 001560     OPEN INPUT  CUSTOMER-MASTER    *error reported here*
 "<>                        SORTED-FILE
 "<>                        STOCK-MASTER-FILE
 "<> 001570     OUTPUT NEW-CUST-MASTER
 "<> 001580                 PRINT-FILE
 "<> 001590     PERFORM PRINT-REPORT-HDGS
 "<> 001621     PERFORM READ-SORTED-FILE
 "<> PERFORM READ-MASTER-FILE.

I believe you actually reading the error incorrectly.

The error message is really saying that you have an illegal filename
in file number 004.  I translate that to be the STOCK-MASTER-FILE.

Since it is defined as an INDEXED fle, MF COBOL reserves the .IDX
 file
extension.  You can NOT use that extension youself.  You should
probably call the file STCKMAST.DAT and let MF automatically use the
IDX extension.

Sorry for the way the lines wrapped when my reader quoted the
 original
message.

Also, if my analysis is wrong, I hope some of the other folks will
chime in.

Charlie Smith

-----------------------------------------------------------------
Charlie Smith                      Smith Data Processing Services
csmit002@sdpsbbs.sdps-bbs.com      The CyberSpace BBS - 1:231/992
Decatur Township Info Network      BBS/PPP/FAX --- 1 317 856 9020
-----------------------------------------------------------------

... Backup not found: (A)bort (R)etry (S)lap nearest innocent
 bystander.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
