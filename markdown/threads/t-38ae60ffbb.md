[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with Easytrieve

_8 messages · 7 participants · 1999-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help with Easytrieve

- **From:** "gee" <grant_englebrecht@nospam.compuware.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371ad5a7@199.186.16.51>`

```
I realise that this may not be the right forum for this question, but I have
noticed quite a few people exhibiting MVS knowledge.

My question is this;
I have an input file that is defined as follows
   dcb=(recfm=vb,lrecl=363)
my output file is defined as follows
   dcb=(recfm=vb,lrecl=377)

I want to read in the file and only select certain fields to output.

Easytrieve Plus lets me read it in fine but the output seems to contain part
of the next record ??

I have included the jcl used.

where am I going wrong.

yes I do know I can use cobol but the stipulation for this project is to use
easytrieve plus.

Thanks in advance
G


source follows

//EZY      JOB (22YR0T,CP03),'EZY',MSGCLASS=X,
//      CLASS=C,NOTIFY=EHTGTQ,RESTART=REPORT00
//*
/*JOBPARM  SYSAFF=ANY
//***************>>>>>>> START OF JOB <<<<<<<<<**************
//DELETE    EXEC PGM=IEFBR14
//DD01       DD  DSN=YRTEST.COMPUWRE.NBSUBSET.XTRNEW2.D,
//     DISP=(MOD,DELETE,DELETE),SPACE=(TRK,1),UNIT=SYSDA
//DD02       DD  DSN=YRTEST.COMPUWRE.NBSUBSET.XTROLD2.D,
//     DISP=(MOD,DELETE,DELETE),SPACE=(TRK,1),UNIT=SYSDA
//*
//DEFINE    EXEC PGM=IEFBR14
//DD01       DD  DSN=YRTEST.COMPUWRE.NBSUBSET.XTRNEW2.D,
//     DISP=(,CATLG,DELETE),SPACE=(TRK,(100,10),RLSE),UNIT=SYSDA,
//     DCB=(RECFM=VB,LRECL=377)
//DD02       DD  DSN=YRTEST.COMPUWRE.NBSUBSET.XTROLD2.D,
//     DISP=(,CATLG,DELETE),SPACE=(TRK,(100,10),RLSE),UNIT=SYSDA,
//     DCB=(RECFM=VB,LRECL=377)
//*
//***************>>>>>>> START OF JOB <<<<<<<<<**************
//REPORT00  EXEC PGM=EZTPA00
//STEPLIB    DD  DISP=SHR,DSN=AMPS.SW.EASYPLUS.LOAD
//*
//MACROS     DD   DSN=YRTEST.P.CCPROD.EASYMAC,DISP=SHR
//SYSPRINT   DD   SYSOUT=*
//SYSUDUMP   DD   SYSOUT=*
//SYSOUT     DD   SYSOUT=*
//NBOLD2     DD   DUMMY,DISP=SHR,DSN=YRTEST.COMPUWRE.NBSUBSET.XTROLD2
//NBOLD2D    DD   DUMMY,DISP=SHR,DSN=YRTEST.COMPUWRE.NBSUBSET.XTROLD2.D
//NBNEW2     DD   DISP=SHR,DSN=YRTEST.COMPUWRE.NBSUBSET.XTRNEW2
//NBNEW2D    DD   DISP=SHR,DSN=YRTEST.COMPUWRE.NBSUBSET.XTRNEW2.D
//SYSIN      DD   *
*
LIST ON
*
FILE NBNEW2  VB (0 0)
   NEW-TYPE         1     1 A
   NEW-NUM          2     3 N, 0
   NEW-TABLE       33    18 A
   NEW-DATA         5   219 A
*

FILE NBNEW2D VB (0 0)
   NEW2D-TABLE      1    18  A
   NEW2D-DATA      19   359  A
*

FILE NBOLD2 VB (0 0)
   OLD-TYPE         1     1 A
   OLD-NUM          2     3 N, 0
   OLD-TABLE       33    18 A
   OLD-DATA         5   359 A
*
FILE NBOLD2D VB (0 0)
*  OLD2D-REC        1   377  A
   OLD2D-TABLE      1    18  A
   OLD2D-DATA      19   359  A

*
   WS-NEW-TBL W 18   A  OCCURS 20
   WS-OLD-TBL W 18   A  OCCURS 20

   WS-COUNT   W  3   N

JOB INPUT NBNEW2
*
    IF NEW-TYPE = 'H'
        DISPLAY NEW-NUM NEW-TABLE
        WS-NEW-TBL(NEW-NUM) = NEW-TABLE
    ELSE
      IF NEW-TYPE = 'T'
         STOP
      ELSE
          IF NEW-TYPE = 'D'
            WS-COUNT = WS-COUNT + 1
            IF WS-COUNT > 10
               STOP
            END-IF
            NEW2D-TABLE = WS-NEW-TBL(NEW-NUM)
            NEW2D-DATA  = NEW-DATA
            PUT NBNEW2D
          END-IF
      END-IF
    END-IF
```

#### ↳ Re: Help with Easytrieve

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XINS2.5191$qx1.115795@storm.twcol.com>`
- **References:** `<371ad5a7@199.186.16.51>`

```
From the code below it doesn't seem like your output file needs to be 4
bytes longer. Shorten it.

Geussing at how EZ stores blocked files, It is probably blocking up the
input records in sequential storage, then moving the input record for the
length of the output record to the output record area. Thus grabbing the
first few bytes of the next record. Sort of a table overflow problem.

>*
>LIST ON
…[52 more quoted lines elided]…
>
```

#### ↳ Re: Help with Easytrieve

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371BB798.4ADF@saif.com>`
- **References:** `<371ad5a7@199.186.16.51>`

```
I think you have things set up just fine, but with one minor problem; 
how does your EZPLUS program behave when the incoming record is shorter
than its maximum possible length?

The answer to this is that if your incoming record is physically shorter
than max and you don't code for this condition, then the remaining area
is actually looking forward in the buffer and gives you the header
section of the next record.

I have used two different solutions:
====================================
1) Use the WORKAREA parameter on the input file.  However, this requires
you to "blank out" this workarea before each read, or EZPLUS leaves data
from previous reads in the right-most area.

2) Re-compute the correct LRECL for the output file right before writing
the record.
In this case, I think the instruction would something like this:
	RECORD-LENGTH(OUTFILE) = RECORD-LENGTH(INFILE) + 14
	PUT OUTFILE

Let me know if this works.
mailto:petwir@saif.com



gee wrote:
> 
> I realise that this may not be the right forum for this question, but I have
…[108 more quoted lines elided]…
>     END-IF
```

#### ↳ Re: Help with Easytrieve

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990419084543.20551.00004038@ng-fi1.aol.com>`
- **References:** `<371ad5a7@199.186.16.51>`

```
you need to specify the length of the record being output based on the length
of the input record.  You may want to intialize the output record everytime you
read in a new record.  EZtrieve does not do this for you.
```

#### ↳ Re: Help with Easytrieve

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ffih8$egm$1@nnrp1.dejanews.com>`
- **References:** `<371ad5a7@199.186.16.51>`

```
In article <371ad5a7@199.186.16.51>,
  "gee" <grant_englebrecht@nospam.compuware.com> wrote:
> I realise that this may not be the right forum for this question, but I have
> noticed quite a few people exhibiting MVS knowledge.
…[12 more quoted lines elided]…
> I have included the jcl used.

<snip the remainder>

Easy holds the 'System-Defined File Fields' RECORD-LENGTH, RECORD-COUNT and
FILE-STATUS. These are somehow similar to the COBOL special registers.

In the Reference Guide of the release 6.2, you can read at page 11-4:
'RCORD-LENGTH is a two-byte binary field used for all file types to determine
or establish the length of the current data record....<snip>... For
variable-length files, assign the length fo the record to the RECORD-LENGTH
field before the PUT or WRIE statement is executed.'

So do the following:

MOVE 363 to RECORD-LENGTH
WRITE myoutputfile

Or even better, move the input lenght to the output length:

FILE INFILE
INFIELD 1 100 A
FILE OUTFILE
OUTFIELD 1 200 A
JOB INPUT INFILE
 MOVE INFILE:RECORD-LENGTH TO OUTFILE:RECORD-LENGTH
 PUT OUTFILE FROM INFILE

Daniel

------------------------------------------------------------------------
visit us at http://www.winterthur.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Help with Easytrieve

- **From:** "gee" <grant_englebrecht@nospam.compuware.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371bb81b@199.186.16.51>`
- **References:** `<371ad5a7@199.186.16.51> <7ffih8$egm$1@nnrp1.dejanews.com>`

```
thanks for that.  It worked a treat.
what whould I do without this newsgroup.

G
```

#### ↳ Re: Help with Easytrieve

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vHS2.4744$s_5.219452@dfiatx1-snr1>`
- **References:** `<371ad5a7@199.186.16.51>`

```
There is an MVS-Specific web-based message board at http://www.mvshelp.com

Oh, your specific problem? Well, I don't know EZTrieve, but with both
SyncSort and QuickJob I *often* forget to account for the four-byte length
word at the start of each variable-length record (i.e., the data starts at
position 5, not position 1). Maybe you have a similar situation?

MCM

gee wrote in message <371ad5a7@199.186.16.51>...
>I realise that this may not be the right forum for this question, but I
have
>noticed quite a few people exhibiting MVS knowledge.
>
…[4 more quoted lines elided]…
>   dcb=(recfm=vb,lrecl=377)
```

#### ↳ Re: Help with Easytrieve

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990419214930.29557.00002958@ng06.aol.com>`
- **References:** `<371ad5a7@199.186.16.51>`

```
if you output:VB and reclen=377, did you include 4 bytes in this layout?
if it is 377 EZTR layout must be 373
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
