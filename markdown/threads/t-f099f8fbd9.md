[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/IMS question

_4 messages · 4 participants · 2002-10 → 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL/IMS question

- **From:** calvin5867705@yahoo.com (link)
- **Date:** 2002-10-29T12:09:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5d879bfe.0210291209.660ca5fa@posting.google.com>`

```
Hi,

I am a new comer COBOL/CICS/IMS programs. I have a few questions about
that.

I just finished coding COBOL/CICS/IMS programs. While I am doing the
test, I meet the error message
"E042 - PSB SCHEDULE ERROR. CODE: 0813UI,E124". When I asked my
friend, he just told me that "You need to set up a PSB.
The CICS group needs to define this PSB to the CICS tables. "

Does anybody know what's procedure for COBOL/IMS setting (ie: PSB)
after coding ? Beside this, anything else that I need to do  which
insure the testing ? ANy utility that will help me to do that ?

Thanks a lot for your assistance.
```

#### ↳ Re: COBOL/IMS question

- **From:** corek@nospam.hotmail.com
- **Date:** 2002-10-29T23:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b6uru0qfid5n4hgtiudlv1f7spkr7fasi@4ax.com>`
- **References:** `<5d879bfe.0210291209.660ca5fa@posting.google.com>`

```
On 29 Oct 2002 12:09:53 -0800, calvin5867705@yahoo.com (link) wrote:
Is it the PSB construction you don't know?
(Example
         PCB   TYPE=DB,DBDNAME=databasename,PROCOPT=GIR,KEYLEN=100
         SENSEG NAME=tablename,PARENT=0
         SENSEG NAME=tablename2,PARENT=tablename
         PSBGEN LANG=COBOL,PSBNAME=PC20PSB
         END
)
or is it putting into the CICS tables - which is the Database Admins
job?

>Hi,
>
…[13 more quoted lines elided]…
>Thanks a lot for your assistance.
```

#### ↳ Re: COBOL/IMS question

- **From:** jimferg <member@mainframeforum.com>
- **Date:** 2002-10-30T18:00:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dc0648d$1_2@news.onlynews.com>`
- **References:** `<5d879bfe.0210291209.660ca5fa@posting.google.com>`

```
You need schedule your PSB with CICS by using an CBLTDLI call w/ a
function of "PCB". You should also terminate your PSB at teh end of your
processing.

The relevent pieces of code are below.

01 WS-IMS-SCHED. 05 CICS-PGM-NAME PIC X(08) VALUE 'AISA01# '. 05
PCB-FUNC PIC X(04) VALUE 'PCB '. 05 TERM-FUNC PIC X(04) VALUE 'TERM'.

 LINKAGE SECTION. COPY DLIUIB. 01 OVERLAY-DLIUIB REDEFINES DLIUIB. 05
 PCBADDR USAGE IS POINTER. 05 FILLER PIC XX.

 01 PCB-ADDRESS-LIST. 05 BTSPCB-ADDR USAGE IS POINTER.

 01 BTS-CUST-PCB. COPY PCBDEF.

******************************************************************
* SCHEDULE PSB FOR DPS CALL
******************************************************************
 9600-SCHEDULE-PSB. CALL 'CBLTDLI' USING PCB-FUNC CICS-PGM-NAME ADDRESS
 OF DLIUIB. SET ADDRESS OF PCB-ADDRESS-LIST TO PCBADDR. SET ADDRESS OF
 BTS-CUST-PCB TO BTSPCB-ADDR. 9600-EXIT. EXIT.

 ******************************************************************
 * TERMINATE PSB
 ******************************************************************
  9700-TERMINATE-PSB. CALL 'CBLTDLI' USING TERM-FUNC. 9700-EXIT. EXIT.
















:) :) :)
```

##### ↳ ↳ Re: COBOL/IMS question

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2002-11-02T19:20:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DC487E2.A0C6907B@sprynet.com>`
- **References:** `<5d879bfe.0210291209.660ca5fa@posting.google.com> <3dc0648d$1_2@news.onlynews.com>`

```
jimferg wrote:
> 
> You need schedule your PSB with CICS by using an CBLTDLI call w/ a
…[27 more quoted lines elided]…
> :) :) :)

I sure hope these smileys are there because of the amusing way that code
is constructed!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
