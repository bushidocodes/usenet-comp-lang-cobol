[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# status 46 abend --- help!

_10 messages · 7 participants · 2000-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### status 46 abend --- help!

- **From:** "Seekermike" <seeker@dwx.com>
- **Date:** 2000-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e12ff3@news.dwx.com>`

```
I program in mainframe COBOL for MVS/VM.  Last week a nightly batch program
that had been running fine for 6 weeks started giving me problems.  The
program reads a sequential DASD file, GS.MA.SRTD.AUDIT.AGTMF.UPDT(+1), and
keeps abending for status code 46, trying to do a READ NEXT but there is no
next record.  The odd thing is, the job runs fine when I run it the next
morning!  I copy the production input files to test, so as far as I can
tell, everything is exactly the same.  I even copied the production JCL
(which abends at night) to test and ran with it.....and it runs fine!
Something is different at night that makes the job abend, but I can't figure
out what.  Can anyone help me?  My home e-mail is seeker@dwx.com.

Here is the program code and JCL I'm using.


        SELECT AUDIT-FILE
            ASSIGN TO UT-S-AG232S1.
::
::
::

 FD   AUDIT-FILE
      RECORDING MODE IS F.
      COPY AGWIQO10.
::
::
::

 000100*W AGWIQO10  AGENT MASTER AUDIT TRAIL RECORD
 000200****************************************************************
 000300**   THIS RECORD LAYOUT IS FOR THE SEQUENTIAL AUDIT TRAIL FILE
 000400**   THAT IS WRITTEN TO AS CICS TD QUEUE 'AGPR'.
 000500****************************************************************
 000600 01  AGWIQO10.
 000700     05  AGWIQO10-KEY.
 000800         10  AGWIQO10-PROC-GRP        PIC XX.
 000900         10  AGWIQO10-REC-TYPE        PIC XX.
 001000         10  AGWIQO10-AGENT           PIC X(18).
 001100         10  AGWIQO10-COMP            PIC XX.
 001200         10  AGWIQO10-LINE            PIC XX.
 001300     05  AGWIQO10-SUB-KEY.
 001400         10  AGWIQO10-DATE            PIC S9(7) COMP-3.
 001500         10  AGWIQO10-TIME            PIC S9(7) COMP-3.
 001600         10  AGWIQO10-UPDT-CODE       PIC 9.
 001700         10  AGWIQO10-OPER-ID         PIC XXXX.
 001800     05  AGWIQO10-DATA                PIC X(1674).



  3450-READ-AUDIT.
      INITIALIZE AGWIQO10-KEY.
      MOVE '01' TO AGWIQO10-PROC-GRP.
      MOVE 'AA' TO AGWIQO10-REC-TYPE.
      MOVE AAF-AGENT-KEY TO AGWIQO10-AGENT.
      READ AUDIT-FILE NEXT
        AT END
          MOVE 'Y' TO AUDIT-EOF.
      MOVE AGWIQO10 TO WS-AGWIQO10.
 ****
 **** THIS MAKES SURE THE RECORD WE JUST READ FROM THE AUDIT FIL
 **** MATCHES THE RECORD WE READ ON THE TFG AGENT MASTER FILE
 **** (BOTH FIELDS ARE 18 BYTES LONG)
      IF (AGWIQO10-AGENT = AAF-AGENT-KEY)
            MOVE 'Y' TO AUDIT-EOF.
  3450-READ-EXIT.
      EXIT.

::
::
::

//STEP0080 EXEC PGM=AGB0170,COND=(0,NE)
//NA100I1  DD  DSN=GS.NA.MASTER,DISP=SHR                     *READ*
//NA100I2  DD  DSN=GS.NA.INDEX,DISP=SHR                      *READ*
//NA100I4  DD  DSN=GS.NA.HISTORY,DISP=SHR                    *READ*
//NA100I5  DD  DSN=GS.NA.CLIENT,DISP=SHR                     *READ*
//TALIVLB  DD  DSN=GS.TA.LIVE.TABLES,DISP=SHR                *READ*
//AGSI010  DD  DSN=GS.MA.AGENTS.MASTER.AA.DASD,DISP=SHR      *READ*
//AG232S1  DD  DSN=GS.MA.SRTD.AUDIT.AGTMF.UPDT(+1),DISP=SHR  *READ*
//AGMISC   DD  DSN=GS.MA.AGENTS.MISC,DISP=SHR,               *READ*
//             AMP=('BUFND=8,BUFNI=8')
//AMVU020  DD  DSN=AM.P.XX.P.AGTMF,DISP=SHR                  *UPDATE*
//AMVU030  DD  DUMMY    *,DSN=AM.P.XX.P.AGTRANS,DISP=SHR     *UPDATE*
//AMRO040  DD  SYSOUT=3,FLASH=SL3Y             *TFG RECS*
//AMRO050  DD  SYSOUT=3,FLASH=SL3Y             *IMT AGTMF UPDATED*
//AMRO060  DD  DUMMY                           *IMT TRANS UPDATED*
//AMRO070  DD  SYSOUT=3,FLASH=SL3Y             *IMT AGTMF NOT FOUND*
//AMRO080  DD  DUMMY                           *IMT TRANS NOT FOUND*
//MIN9001  DD  DSN=AM.P.XX.P.AMDATE,DISP=OLD   *DATE OF LAST RUN*
//SYSUDUMP DD  SYSOUT=D
//SYSDBOUT DD  SYSOUT=D
//SYSOUT   DD  SYSOUT=*
```

#### ↳ Re: status 46 abend --- help!

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E1E50F.22EC87FA@brazee.net>`
- **References:** `<39e12ff3@news.dwx.com>`

```


Seekermike wrote:
> 
> The odd thing is, the job runs fine when I run it the next
> morning!  I copy the production input files to test, so as far as I can
> tell, everything is exactly the same.  I even copied the production JCL
> (which abends at night) to test and ran with it.....and it runs fine!


When I get something like that, I ask myself the following:

Do you have the same compiler options for test and production?

Do you have same security options for the test and production files?

Are you running the same version of the program?

Are the files what I think they are?
```

##### ↳ ↳ Re: status 46 abend --- help!

- **From:** "Seekermike" <seeker@dwx.com>
- **Date:** 2000-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e24294$1@news.dwx.com>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net>`

```
As it turned out, one of the files was NOT what I thought it was.   I have a
date input dataset that was set to 20001003 instead of 2001004, so the
program was searching for data from more than one date, then looking for its
counterpart in the audit file.  When it couldn't find the record it was
looking for, it abended for status code 46.  Thanks!


Howard Brazee <howard@brazee.net> wrote in message
news:39E1E50F.22EC87FA@brazee.net...
>
>
…[16 more quoted lines elided]…
> Are the files what I think they are?
```

##### ↳ ↳ Re: status 46 abend --- help!

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-10T15:01:33+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E2949D.FEC39563@zip.com.au>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net>`

```
Howard Brazee wrote:

> Seekermike wrote:
> >
…[13 more quoted lines elided]…
> Are the files what I think they are?

SSRANGE compiler option will tell you whether you have a memory overwrite
problem.   This causes strange results like think to happen, optimise
reorganises the working storage.

Ken
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FsDE5.347$tC5.17529@paloalto-snr1.gtei.net>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au>`

```
I have seen this a number of times. Last time it happened it was on an IBM
mainframe on a VSAM file which had not been re-org'd
(REPRO/DELETE/DEFINE/REPRO) for while and all the CI's were full.

Time before that it was when the OPEN failed, but never interrogated, and
the FILE STATUS variable was shared across files, as in:

OPEN INPUT
          FILE-1    << Open fails, FILE STATUS not '00'
          FILE-2    << open succeeds, file status is '00'
          FILE-3.
IF File-status NOT = '00'
  (error procedure)...

This code will only trigger an error if the OPEN of FILE-3 fails.

Just some things to keep in mind....
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E31CF7.92603079@brazee.net>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au> <FsDE5.347$tC5.17529@paloalto-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> Time before that it was when the OPEN failed, but never interrogated, and
> the FILE STATUS variable was shared across files, as in:

I like having a company standard stating that all FILE STATUS variables
are unique to particular files, with names which make it obvious which
files they refer to.
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VZFE5.6614$Ri3.28217@news2.atl>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au> <FsDE5.347$tC5.17529@paloalto-snr1.gtei.net> <39E31CF7.92603079@brazee.net>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> I like having a company standard stating that all FILE STATUS variables
> are unique to particular files, with names which make it obvious which
> files they refer to.

What puzzles me is why in the world would anyone conceive of doing
it any other way?  Saving a couple of bytes of RAM?
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

_(reply depth: 6)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E341B2.6BBC3653@dced.state.ak.us>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au> <FsDE5.347$tC5.17529@paloalto-snr1.gtei.net> <39E31CF7.92603079@brazee.net> <VZFE5.6614$Ri3.28217@news2.atl>`

```
Judson McClendon wrote:

> "Howard Brazee" <howard@brazee.net> wrote:
> >
…[5 more quoted lines elided]…
> it any other way?  Saving a couple of bytes of RAM?

Local situation was due to copybooks for files not normally used together.
Worked fine for a while, then a special program used both files & oh, God,
they used the same FILE STATUS variable. Now changed.
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-10-11T00:09:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NcOE5.1376$9n6.249446@dfiatx1-snr1.gtei.net>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au> <FsDE5.347$tC5.17529@paloalto-snr1.gtei.net> <39E31CF7.92603079@brazee.net> <VZFE5.6614$Ri3.28217@news2.atl>`

```
Can you spell, "L-A-Z-Y?"

MCM

Judson McClendon <judmc@bellsouth.net> wrote in message
news:VZFE5.6614$Ri3.28217@news2.atl...
> "Howard Brazee" <howard@brazee.net> wrote:
> >
…[6 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: status 46 abend --- help!

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8rvqth$ich$1@slb7.atl.mindspring.net>`
- **References:** `<39e12ff3@news.dwx.com> <39E1E50F.22EC87FA@brazee.net> <39E2949D.FEC39563@zip.com.au> <FsDE5.347$tC5.17529@paloalto-snr1.gtei.net>`

```
I suspect that Michael understands this, but others may not.  Including
multiple files in the same OPEN statement is NOT the problem with the
"attached" example.  The problem is that the different files all use the
same field to store the file status-code.  If each of the files DID have a
different file-status field and all 3 fields were queried after the OPEN,
then this would be "OK" code. (Although, you would need to think about the
question of whether or not you really WANT to open the 2nd and 3rd files -
if the 1st file's open failed.  Sometimes you do - sometimes you don't)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
