[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBMCOBOL and LE ABEND

_12 messages · 4 participants · 2000-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBMCOBOL and LE ABEND

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E48387.2EE194F4@generali.it>`

```
Does anybody know if there is some documented procedure to understand
what is the COBOL program or COBOL CSECT that damage heap memory and
cause ABEND U4038 with message
"CEE0802C: Heap storage control information was damaged."?

Thanx.
Max
```

#### ↳ Re: IBMCOBOL and LE ABEND

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001011120906.11284.00000342@ng-ca1.aol.com>`
- **References:** `<39E48387.2EE194F4@generali.it>`

```
What is the setting of your TERMTHDACT runtime option? It should be one of:
TRACE, DUMP, UADUMP or UATRACE. If not, try rerunning with one of those options
and tell us what you get.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: IBMCOBOL and LE ABEND

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E569E3.3336866C@generali.it>`
- **References:** `<39E48387.2EE194F4@generali.it> <20001011120906.11284.00000342@ng-ca1.aol.com>`

```
I have TERMTHDACT(UADUMP) active.
Thanx

S Comstock wrote:

> What is the setting of your TERMTHDACT runtime option? It should be one of:
> TRACE, DUMP, UADUMP or UATRACE. If not, try rerunning with one of those options
…[10 more quoted lines elided]…
> USA
```

#### ↳ Re: IBMCOBOL and LE ABEND

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s2leh$1ec9$1@wrath.news.nacamar.de>`
- **References:** `<39E48387.2EE194F4@generali.it>`

```
I'm not sure about your environment (CICS/Batch/CBLOPTS-settings,LE-version)

You may turn on the HeapCheck-Option for this program via PARM
/HEAPCHK=(ON)

Roland


"Massimo Petten�" <Petteno.Massimo@generali.it> schrieb im Newsbeitrag
news:39E48387.2EE194F4@generali.it...
> Does anybody know if there is some documented procedure to understand
> what is the COBOL program or COBOL CSECT that damage heap memory and
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBMCOBOL and LE ABEND

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5671F.B877182B@generali.it>`
- **References:** `<39E48387.2EE194F4@generali.it> <8s2leh$1ec9$1@wrath.news.nacamar.de>`

```
My Environment is IMS. I tryed to set HEAPCHK(ON) using "STEPLIB"
but I still have no differences (DUMP information are the same).
I'm not able to read the dump information.
Thanx.
Max

Roland Schiradin wrote:

> I'm not sure about your environment (CICS/Batch/CBLOPTS-settings,LE-version)
>
…[17 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: IBMCOBOL and LE ABEND

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2000-10-13T00:45:09+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s5es1$28i4$1@wrath.news.nacamar.de>`
- **References:** `<39E48387.2EE194F4@generali.it> <8s2leh$1ec9$1@wrath.news.nacamar.de> <39E5671F.B877182B@generali.it>`

```
I'm not an IMS-specalist.

I would guess your HEAPCHK setting was not in use. To make
sure just add RPTOPT(ON) to your CEEUOPT/CEEROPT
This will tell which options in effect but I don't know where (no IMS
know-how)

Roland


"Massimo Petten�" <Petteno.Massimo@generali.it> schrieb im Newsbeitrag
news:39E5671F.B877182B@generali.it...
> My Environment is IMS. I tryed to set HEAPCHK(ON) using "STEPLIB"
> but I still have no differences (DUMP information are the same).
…[6 more quoted lines elided]…
> > I'm not sure about your environment
(CICS/Batch/CBLOPTS-settings,LE-version)
> >
> > You may turn on the HeapCheck-Option for this program via PARM
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBMCOBOL and LE ABEND

_(reply depth: 4)_

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E6B40D.74C01B53@generali.it>`
- **References:** `<39E48387.2EE194F4@generali.it> <8s2leh$1ec9$1@wrath.news.nacamar.de> <39E5671F.B877182B@generali.it> <8s5es1$28i4$1@wrath.news.nacamar.de>`

```
I tryed with HEAPCHK(ON) but I had the same information
on dump as before. HEAPCHK seems do not help me.

Max


Roland Schiradin wrote:

> I'm not an IMS-specalist.
>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: IBMCOBOL and LE ABEND

_(reply depth: 5)_

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2000-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8safnd$r6b$1@wrath.news.nacamar.de>`
- **References:** `<39E48387.2EE194F4@generali.it> <8s2leh$1ec9$1@wrath.news.nacamar.de> <39E5671F.B877182B@generali.it> <8s5es1$28i4$1@wrath.news.nacamar.de> <39E6B40D.74C01B53@generali.it>`

```
In this case try to get a SYSUDUMP and use the IPCS LEDATA to check
which HEAP is corrupted. Maybe the data in the corrupted data will help

Roland

"Massimo Petten�" <Petteno.Massimo@generali.it> schrieb im Newsbeitrag
news:39E6B40D.74C01B53@generali.it...
> I tryed with HEAPCHK(ON) but I had the same information
> on dump as before. HEAPCHK seems do not help me.
…[15 more quoted lines elided]…
>
```

#### ↳ Re: IBMCOBOL and LE ABEND

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-10-12T03:19:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001011231948.03174.00002184@ng-fh1.aol.com>`
- **References:** `<39E48387.2EE194F4@generali.it>`

```
>From: Massimo =?iso-8859-1?Q?Petten=F2?= Petteno.Massimo@generali.it 
>Date: 10/11/00 11:13 AM Eastern Daylight Time

I may be going brain dead but doesn't a U4038 mean that the FD in a program
doesn't match the DCB LRECL in a file? Or you're missing a DD statement (which
of course it won't match the DCB because there isn't any) - or is that a U4035?
 Don't remember anything about heap.

(I know - that helps a heap).

Eileen

>Does anybody know if there is some documented procedure to understand
>what is the COBOL program or COBOL CSECT that damage heap memory and
…[4 more quoted lines elided]…
>Max
```

##### ↳ ↳ Re: IBMCOBOL and LE ABEND

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5A76E.5C26915D@generali.it>`
- **References:** `<39E48387.2EE194F4@generali.it> <20001011231948.03174.00002184@ng-fh1.aol.com>`

```
I'm sorry it was an LE ABEND U4039.
Max

YukonMama wrote:

> >From: Massimo =?iso-8859-1?Q?Petten=F2?= Petteno.Massimo@generali.it
> >Date: 10/11/00 11:13 AM Eastern Daylight Time
…[16 more quoted lines elided]…
> >Max
```

###### ↳ ↳ ↳ Re: IBMCOBOL and LE ABEND

- **From:** Simon Elliott <"Simon.L.Elliott[Delete.Me]"@CapGemini.Co.UK>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5B082.9B4F7220@CapGemini.Co.UK>`
- **References:** `<39E48387.2EE194F4@generali.it> <20001011231948.03174.00002184@ng-fh1.aol.com> <39E5A76E.5C26915D@generali.it>`

```
Massimo Pettenï¿½ wrote:

> I'm sorry it was an LE ABEND U4039.
> Max

The Language Environment for MVS and VM V1R5 bookshelf at
http://www.s390.ibm.com:80/bookmgr-cgi/bookmgr.cmd/Shelves/CEE5S004

gives

"The default abnormal termination exits, CEEBDATX (for batch) and CEECDATX (for
CICS), are now automatically linked in at install time. These exits issue abend 4039
when an unhandled condition of severity 2 or greater occurs."

Does this help?
```

###### ↳ ↳ ↳ Re: IBMCOBOL and LE ABEND

_(reply depth: 4)_

- **From:** Massimo Pettenò <Petteno.Massimo@generali.it>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5BB84.D0AB45BD@generali.it>`
- **References:** `<39E48387.2EE194F4@generali.it> <20001011231948.03174.00002184@ng-fh1.aol.com> <39E5A76E.5C26915D@generali.it> <39E5B082.9B4F7220@CapGemini.Co.UK>`

```
Actually I don't know, or better I don't thoink so.
Thanx the same.
Max

Simon Elliott wrote:

> Massimo Pettenï¿½ wrote:
>
…[24 more quoted lines elided]…
> Please delete "Delete.Me" to reply.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
