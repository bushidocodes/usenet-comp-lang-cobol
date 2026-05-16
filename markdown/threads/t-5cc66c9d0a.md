[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Giving empty files

_1 message · 1 participant · 2004-04_

---

### Giving empty files

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-04-27T15:06:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6lst8$l20$1@peabody.colorado.edu>`

```
Has anybody ever had occasional problems in an IBM mainframe environment reading
empty files created by a COBOL GIVING statement?

I've been running a test job over and over again (that deletes the file, creates
it with a CoBOL sort program, and then reads it with another CoBOL program).  
Sometimes the return status is '10' when I read the file.   Sometimes it is a
'00' with garbage read (I could gener this empty file to a new file and it found
data that I couldn't see by browsing it), and sometimes it aborts with a '30'
error status when reading.

No consistency.


One time I edited this empty file copied in data.   The abend was because it
read this old record despite the file being deleted with the IEFBR14 below.:

Step #01 deletes this file.
Step #02 is a CoBOL sort that is creating an empty file using a GIVING file but
no data found.  It does check for sort status.
Step #04 is a CoBOL program that opens and reads this empty file, sometimes
giving '00' return code (and data that should be deleted), sometimes '10', and
sometimes aborting with '30'.


//MPCM$#01   EXEC PGM=IEFBR14 ************ CLEAN-UP FILES
//FINDFILE   DD DSN=&SYSTEM..MPCMTMP1.&APP.&CAMPUS..FINDER,
//             DISP=(MOD,DELETE),SPACE=(TRK,0)
//MPCM$#02   EXEC PGM=SIPR856
//***********************************************
//*  EXTRACT STUDENTS WITH DEBIT BALANCE        *
//***********************************************
//STEPLIB    DD DSN=UMS.PROD.LOAD,DISP=SHR
//           DD DSN=CEE.SCEERUN,DISP=SHR
//           DD DSN=IDMS.SYSTEM&SYSNUM..LOADLIB,DISP=SHR
//           DD DSN=IDMS.&VER..LOADLIB,DISP=SHR
//SYSIDMS    DD DSN=UMS.PROD.DATA(SI&SYSNUM.&MODE),DISP=SHR
//SORTWK01   DD UNIT=SYSDA,SPACE=(CYL,15,,CONTIG)
//SORTWK02   DD UNIT=SYSDA,SPACE=(CYL,15,,CONTIG)
//SORTWK03   DD UNIT=SYSDA,SPACE=(CYL,15,,CONTIG)
//SYSOUX     DD SYSOUT=&PRTB2
//PARMFL     DD DSN=&USER1,
//             DISP=SHR
//FINDOUT    DD DSN=&SYSTEM..MPCMTMP1.&APP.&CAMPUS..FINDER,
//             DISP=(NEW,CATLG,CATLG),
//             UNIT=&UNIT,
//             SPACE=(CYL,(24,12),RLSE),
//             DCB=(RECFM=FB,LRECL=80,DSORG=PS)
//SYSDBOUT   DD SYSOUT=&PRTB1
//SYSOUT     DD SYSOUT=&PRTB2
//MPCM$#03   EXEC PGM=IEFBR14 ************ CLEAN-UP FILES
//FINDFILE   DD DSN=&SYSTEM..MPCMTMP2.&APP.&CAMPUS..FINDER,
//             DISP=(MOD,DELETE),SPACE=(TRK,0)
//MPCM$#04   EXEC PGM=SIPR857
//***********************************************
//*  EXTRACT STUDENTS WITH DEBIT BALANCE        *
//***********************************************
//STEPLIB    DD DSN=UMS.PROD.LOAD,DISP=SHR
//           DD DSN=CEE.SCEERUN,DISP=SHR
//           DD DSN=IDMS.SYSTEM&SYSNUM..LOADLIB,DISP=SHR
//           DD DSN=IDMS.&VER..LOADLIB,DISP=SHR
//SYSIDMS    DD DSN=UMS.PROD.DATA(SI&SYSNUM.&MODE),DISP=SHR
//SYSOUX     DD SYSOUT=&PRTB2
//PARMFL     DD DSN=&USER1,
//             DISP=SHR
//FINDIN     DD DSN=&SYSTEM..MPCMTMP1.&APP.&CAMPUS..FINDER,
//             DCB=(RECFM=FB,LRECL=80,DSORG=PS),
//             DISP=(OLD,KEEP,DELETE)
//FINDOUT    DD DSN=&SYSTEM..MPCMTMP2.&APP.&CAMPUS..FINDER,
//             DISP=(NEW,CATLG,CATLG),
//             UNIT=&UNIT,
//             SPACE=(CYL,(24,12),RLSE),
//             DCB=(RECFM=FB,LRECL=80,DSORG=PS)
//SYSDBOUT   DD SYSOUT=&PRTB2
//SYSOUT     DD SYSOUT=&PRTB2
//EXCEPT     DD SYSOUT=&PRTE1
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
