[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS VERIFY PASSWORD command issue.

_4 messages · 3 participants · 2008-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS VERIFY PASSWORD command issue.

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2008-05-02T19:00:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iklm14pfhmhshllio7drtni6ki7ssv1h9v@4ax.com>`

```
Hi all,

I'm having a bit of a problem with checking the return codes from a
EXEC CICS VERIFY PASSWORD command.

Code as follows
CODE
WORKING-STORAGE SECTION.
 01  WSBB-PASSWORD        PIC X(8) VALUE SPACES.
 01  WSBB-USERID          PIC X(8) VALUE SPACES.
 01  WSBB-RESP-CODE       PIC S9(8) COMP VALUE ZEROS.
 01  WSBB-RESP-CODE1      PIC S9(8) COMP VALUE ZEROS.
 01  WSBB-RESP-CODE2      PIC S9(8) COMP VALUE ZEROS.
 01  WSBB-RETURN-CODE     PIC S9(8) COMP VALUE ZEROS.
 01  WSBB-DAYS-LEFT       PIC S9(4) COMP VALUE ZEROS.
 01  WSBB-RET-CODE        PIC -9(10).
 01  WSBB-CHANGETIME      PIC S9(15) COMP-3.
 01  WSBB-INVALIDCOUNT    PIC S9(4) COMP VALUE ZEROS.
 01  WSBB-LASTUSETIME     PIC S9(15) COMP-3.
 01  WSBB-EXPIRYTIME      PIC S9(15) COMP-3.
 01  WSBB-TIME            PIC X(64) VALUE SPACES.
 PROCEDURE DIVISION.
*
 100-MAINLINE SECTION.
**********************
*
 101-PARA.
     MOVE 'usernam' to WSBB-USERID.
     MOVE 'PASSWOR' to WSBB-PASSWORD.
     EXEC CICS VERIFY PASSWORD(WSBB-PASSWORD) USERID(WSBB-USERID)
          DAYSLEFT(WSBB-DAYS-LEFT)
          EMSRESP(WSBB-RESP-CODE1)
          EMSREASON(WSBB-RESP-CODE2)
          CHANGETIME(WSBB-CHANGETIME)
          INVALIDCOUNT(WSBB-INVALIDCOUNT)
          LASTUSETIME(WSBB-LASTUSETIME)
          EXPIRYTIME(WSBB-EXPIRYTIME)
          RESP(WSBB-RESP-CODE)
          RESP2(WSBB-RETURN-CODE)
     END-EXEC.

All done according to the manuals.
Command works fine, but the values of RESP AND RESP2 are always
invalid values. This is still the case if I use the cics precompiler
eibresp and eibresp2 fields.

In all cases the values returned on these 2 fields are
RESP= -0268166945
RESP2= 1342181408
even if the command was sucessefull, on which case RESP should be
equal zero.

All other return fields are correct upon execution.

This is Z/OS 1.07
CICS/ESA V6.2.0
CICS Transaction Server Version 2.2.0
ENTERPRISE COBOL FOR Z/OS  3.4.1 0402

compile options in place
ADV,NOAWO,BUFSIZE(22528),NOCOMPILE(S),DATA(31)     
NODBCS,NODECK,NODUMP,NODYNAM,FASTSRT               
FLAG(I),NOFLAGSTD                                  
LANGUAGE(UE),LIB,LINECOUNT(60),LIST,MAP,NONAME     
NONUMBER,NUMPROC(NOPFD),OBJECT,NOOFFSET,OPTIMIZE   
OUTDD(SYSOUT),RENT,NOSEQUENCE,SIZE(MAX)            
SOURCE,SPACE(1),NOSSRANGE,NOTERM,NOTEST,TRUNC(STD)
NOVBREF,NOWORD,XREF(FULL),NOZWB,APOST              

Already tried with different TRUNC(xxx) with no luck.

Any ideas/suggestions welcome
 

Regards


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: CICS VERIFY PASSWORD command issue.

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2008-05-03T07:37:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wCUSj.153685$D_3.30130@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<iklm14pfhmhshllio7drtni6ki7ssv1h9v@4ax.com>`
- **References:** `<iklm14pfhmhshllio7drtni6ki7ssv1h9v@4ax.com>`

```
Frederico Fonseca wrote:
> Hi all,
> 
…[76 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com

I think you need help from your CICS technical services department or 
your systems programmers.  The fact that your EIBRESP (WSBB-RESP-CODE) 
is way out of range suggests that something is not configured 
correctly in your CICS region.  You might be missing a library for 
RACF in your DFHRPL list.  Or perhaps you're missing a critical 
startup program at region initialization, or the CICS region has 
incorrect SIT parms (System Initialization Table) related to RACF 
processing.

I don't think there is anything in your compile options that should 
cause a problem.  NODYNAM is critical for the EIB interface, but you 
already have that correctly specified.
```

##### ↳ ↳ Re: CICS VERIFY PASSWORD command issue.

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2008-05-07T18:19:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05p3245r247b04u3ppnja7nalpqj6lrm9h@4ax.com>`
- **References:** `<iklm14pfhmhshllio7drtni6ki7ssv1h9v@4ax.com> <wCUSj.153685$D_3.30130@bgtnsc05-news.ops.worldnet.att.net>`

```
On Sat, 03 May 2008 07:37:00 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>Frederico Fonseca wrote:
>> Hi all,
…[90 more quoted lines elided]…
>already have that correctly specified.
Found the problem.

Code above is perfectly correct. problem was on one of the programs
higher on the calling stack that was not passing down the correct
linkage dfheiblk, so when my program tries to reference it, it gives
invalid results.

For others info, CICS precompiler programs will replace
          RESP(WSBB-RESP-CODE)
with
"Move eibresp to WSBB-RESP-CODE" where eibresp is supplied on the
linkage.   

Thanks both you and Bill for the replies.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: CICS VERIFY PASSWORD command issue.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-03T18:01:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AL1Tj.54105$qg2.52802@fe08.news.easynews.com>`
- **References:** `<iklm14pfhmhshllio7drtni6ki7ssv1h9v@4ax.com>`

```
Frederico,
  I am a little confused by where you have:

> CICS/ESA V6.2.0
> CICS Transaction Server Version 2.2.0

Does this mean you have tried it with both?

Anyway, have you seen the NEWER migration guide information at:

  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfhefc00/1.5.7

That does mention changes to the EIBRESP code (with CICS TS 3.x).  Therefore, 
there may be changes (with or without PTFs) at lower levels.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
