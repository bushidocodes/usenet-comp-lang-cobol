[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCUM/PAGING overflow is not being set to TRUE

_5 messages · 4 participants · 1999-05_

---

### ACCUM/PAGING overflow is not being set to TRUE

- **From:** rltuset@yahoo.com
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7iejfd$30n$1@nnrp1.deja.com>`

```
I am using the ACCUM/PAGING options in CICS to build my pages with the
SEND MAP command.  Below is a portion of my code.  The RESPONSE-CODE in
paragraph 2230-SEND-DETAIL-MAP is not being set to overflow when it
should.  I have used the ACCUM/PAGING options before with the SEND TEXT
command with no problems.

What's wrong and how can I fix it?

 003800  1000-DISPLAY-SELECTED-LEA.
 003810 *
 003820      MOVE '1000' TO ERR-PARA.
 003830      PERFORM 1100-START-JHACSRPD-BROWSE THRU 1100-EXIT
 003840      PERFORM 2260-SEND-HEADER-MAP       THRU 2260-EXIT
 003850      PERFORM 2000-PRODUCE-PRC-LINE      THRU 2000-EXIT
 003860          UNTIL END-OF-BROWSE.
 003870      PERFORM 3000-SEND-TOTAL-MAP        THRU 3000-EXIT
 003880      IF SCS-PAGEO > 1
 003890          PERFORM 2240-SEND-TRAILER-MAP1 THRU 2250-EXIT
 003900      ELSE
 003910          PERFORM 2250-SEND-TRAILER-MAP2 THRU 2250-EXIT
 003920      END-IF.
 003930      EXEC CICS
 003940          SEND PAGE
 003950               RELEASE TRANSID('DEUN')
 003960      END-EXEC.
 003970 *
 003980  1000-EXIT.
 003990 *
 004000      EXIT.
             .
             .
             .
 004710  2200-SEND-PRC-LINE.
 004720 *
 004730      MOVE '2200' TO ERR-PARA.
 004740      MOVE JHA-PRC TO SCS-PRC-CODEO
 004750      MOVE JHA-PRC(2:2) TO WS-TM700-PRC
 004760      PERFORM 2210-READ-TM700 THRU 2210-EXIT.
 004770      IF PRC-FOUND
 004780          IF STATE-PRC
 004790              MOVE WS-TM700-PRC-DESC(1:30) TO SCS-PRC-DESCO
 004800          ELSE
 004810              MOVE ATTR-PROT-BRT TO SCS-PRC-DESCA SCS-PRC-CODEA
 004820              MOVE 'INVALID CHARTER SCH PRC CODE' TO
SCS-PRC-DESCO
 004830          END-IF
 004840      ELSE
 004850          MOVE ATTR-PROT-BRT TO SCS-PRC-DESCA SCS-PRC-CODEA
 004860          MOVE 'PRC CODE NOT FOUND IN TM700' TO SCS-PRC-DESCO
 004870      END-IF.
 004880 *
 004890      PERFORM 2220-DISPLAY-APPROVED-AMOUNTS
 004900          THRU 2220-EXIT
 004910 *
 004920      PERFORM 2230-SEND-DETAIL-MAP THRU 2230-EXIT
 004930      IF PAGE-OVERFLOW
 004940          PERFORM 2240-SEND-TRAILER-MAP1 THRU 2240-EXIT
 004950          PERFORM 2260-SEND-HEADER-MAP   THRU 2260-EXIT
 004960          PERFORM 2230-SEND-DETAIL-MAP   THRU 2230-EXIT
 004970          MOVE 'N' TO PAGE-OVERFLOW-SW
 004980      END-IF.
 004990 *
 005000  2200-EXIT.
 005010 *
 005020      EXIT.
             .
             .
             .
 005690  2230-SEND-DETAIL-MAP.
 005700 *
 005710      MOVE '2230' TO ERR-PARA.
 005720      EXEC CICS
 005730          SEND MAP('JHA189B')
 005740               MAPSET('JHA189T')
 005750               FROM(JHA189BO)
 005760               ACCUM
 005770               PAGING
 005780               ERASE
 005790               RESP(RESPONSE-CODE)
 005800      END-EXEC.
 005810      EVALUATE TRUE
 005820          WHEN RESPONSE-CODE = DFHRESP(OVERFLOW)
 005830              MOVE 'Y' TO PAGE-OVERFLOW-SW
 005840          WHEN RESPONSE-CODE NOT = DFHRESP(NORMAL)
 005850              GO TO 9999-TERMINATE-PROGRAM
 005860      END-EVALUATE.
 005870 *
 005880  2230-EXIT.
 005890 *


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

#### ↳ Re: ACCUM/PAGING overflow is not being set to TRUE

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7ien84$f7q$1@server.cntfl.com>`
- **References:** `<7iejfd$30n$1@nnrp1.deja.com>`

```

rltuset@yahoo.com wrote in message <7iejfd$30n$1@nnrp1.deja.com>...
>I am using the ACCUM/PAGING options in CICS to build my pages with the
>SEND MAP command.  Below is a portion of my code.  The RESPONSE-CODE in
…[5 more quoted lines elided]…
>
[...]
> 003880      IF SCS-PAGEO > 1
> 003890          PERFORM 2240-SEND-TRAILER-MAP1 THRU 2250-EXIT

I would assume this should be THRU 2240-EXIT.
------------------
Rick Smith
```

##### ↳ ↳ Re: ACCUM/PAGING overflow is not being set to TRUE

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<374AE77D.D610FA10@NOSPAMhome.com>`
- **References:** `<7iejfd$30n$1@nnrp1.deja.com> <7ien84$f7q$1@server.cntfl.com>`

```
> [...]
> > 003880      IF SCS-PAGEO > 1
…[4 more quoted lines elided]…
> Rick Smith

That's why I hate sections and PERFORM THRUs.
```

###### ↳ ↳ ↳ Re: ACCUM/PAGING overflow is not being set to TRUE

- **From:** rltuset@yahoo.com
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7if481$gcm$1@nnrp1.deja.com>`
- **References:** `<7iejfd$30n$1@nnrp1.deja.com> <7ien84$f7q$1@server.cntfl.com> <374AE77D.D610FA10@NOSPAMhome.com>`

```
In article <374AE77D.D610FA10@NOSPAMhome.com>,
  Howard Brazee <brazee@NOSPAMhome.com> wrote:
> > [...]
> > > 003880      IF SCS-PAGEO > 1
…[7 more quoted lines elided]…
>

You guys are missing the forest for the trees, BUT thanks for catching
the typo.  The winner is...

From:    vbandke@ibm.net (Volker Bandke)
To:      rltuset@yahoo.com
Subject: Re: ACCUM/PAGING overflow is not being set to TRUE
Date:    Tue, 25 May 1999 20:22:22 GMT
Organisation: BSP Beratung, Schulung, Projekte GmbH
Reply-to:  vbandke@bsp-gmbh.com


On Tue, 25 May 1999 16:34:53 GMT, rltuset@yahoo.com wrote:

>I am using the ACCUM/PAGING options in CICS to build my pages with the
>SEND MAP command.  Below is a portion of my code.  The RESPONSE-CODE
in
>paragraph

<<snipped>>             .
>             .
>             .
…[11 more quoted lines elided]…
> 005800      END-EXEC.
<<more snipped>>
You forgot to code the NOFLUSH option on the SEND MAP command

with kind regards

Volker Bandke
(BSP GmbH)

THANKS A HEAP, Volker.


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

#### ↳ Re: ACCUM/PAGING overflow is not being set to TRUE

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<374b044e.4838066@news3.ibm.net>`
- **References:** `<7iejfd$30n$1@nnrp1.deja.com>`

```
On Tue, 25 May 1999 16:34:53 GMT, rltuset@yahoo.com wrote:

>I am using the ACCUM/PAGING options in CICS to build my pages with the
>SEND MAP command.  Below is a portion of my code.  The RESPONSE-CODE in
>paragraph 

<<snipped>>             .
>             .
>             .
…[11 more quoted lines elided]…
> 005800      END-EXEC.
<<more snipped>>
You forgot to code the NOFLUSH option on the SEND MAP command

with kind regards

Volker Bandke
(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
