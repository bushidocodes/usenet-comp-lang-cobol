[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Program abend with error message .

_2 messages · 2 participants · 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Program abend with error message .

- **From:** calvin5867705@yahoo.com (link)
- **Date:** 2002-11-18T11:50:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5d879bfe.0211181150.d5ef813@posting.google.com>`

```
While I am running the COBOL/CICS/IMS programs using the intertest, I
meet the error message below, does any guy have similar experience
before ? Your kind reply will be really appreciated.


  ,CA-InterTest for CICS 6.0 - PROTSYM FILE SOURCE LISTING BREAKPOINT 
   ,
COMMAND ===>,                                                         
        ,
Program=,RY3GC180,Option #,    , Stmt #,      ,             ,     
,Margin=,01,
,       ,                              ,Search=,                      
        ,
-------------------------------------------------------------------------------,
,_,RY3G-BODY                      ,|,,        ,        ,        |,,
---------+---------------------------------------------------------------------,
, ,02808****************************************************************
, ,02809
,A,  ==>     MOVE LOW-VALUES               TO RY3G-BODY.,
,    ==>
,    ==> an attempt to change an area that does not belong to this
task.
,    ==> Possible system damage has been prevented.
,    ==>
,    ==>      Press PF1 for a detailed description.
,    ==>
, ,02811
,_,02812     MOVE LOW-VALUES TO WS-ACCOUNT-KEY-HOLD,
,_,02813                        WS-REINS-KEY-HOLD,
,_,02814                        WS-CASH-KEY-HOLD.
, ,02815
,_,02816     SET CA2-PG-IND           TO CA2-DISP-PAGE-NO.
,_,02817     SET DTL-IND              TO 1.
, ,02818,
```

#### ↳ Re: Program abend with error message ..

- **From:** "Noel DeLeon" <ndeleon@snet.net>
- **Date:** 2002-11-19T03:40:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6piC9.6681$293.1229768758@newssvr10.news.prodigy.com>`
- **References:** `<5d879bfe.0211181150.d5ef813@posting.google.com>`

```
you do not have addresseability to the area you are moving into, or,
the area you are moving into is a separate csect, in which case, you have to
set it up in intertest as noprotect

"link" <calvin5867705@yahoo.com> wrote in message
news:5d879bfe.0211181150.d5ef813@posting.google.com...
> While I am running the COBOL/CICS/IMS programs using the intertest, I
> meet the error message below, does any guy have similar experience
…[11 more quoted lines elided]…
> --------------------------------------------------------------------------
-----,
> ,_,RY3G-BODY                      ,|,,        ,        ,        |,,
> ---------+----------------------------------------------------------------
-----,
> , ,02808****************************************************************
> , ,02809
…[15 more quoted lines elided]…
> , ,02818,
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
