[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help- Visual Basic

_2 messages · 2 participants · 2000-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help- Visual Basic

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-08-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mpkjn$oi6$1@venus.telepac.pt>`

```
I am calling from Visual Basic a program linked with a dll extension and
with an entry point like says the book "Microfocus Cobol- Colbol users
guide". But i have a return error 458 yhat does know thr entry point .
Can abyone hepls me.
I build de program ddl with netexpress.
Thanks
Raimundo Carvalho


       IDENTIFICATION DIVISION.
       PROGRAM-ID. PRA00W.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           CALL-CONVENTION 3 IS WINAPI.
       input-output section.

       DATA DIVISION.
       FILE SECTION.

       working-storage section.
           copy "dssysinf.cpy".
           copy "ds-cntrl.mf".
           copy "pRA00w.cpb".
       01 STR PIC X(10).
       01 dsgrun pic x(6) value "DSGRUN".
       01 action-code                  pic 999.
           78 accao-fim                      value 1.
       01 CORRENTE-DATA.
          05 CORRENTE-DATA-AMD             pic X(08) VALUE SPACES.
          05 FILLER                        pic X(13) VALUE SPACES.

       01 end-of-file-flag              pic 9.
           88 end-of-file                      value 1.

       01 end-of-actions-flag           pic 9.
           88 end-of-actions                   value 1.
****************************
       COPY FSTLINK.CBL.
*************************************
       procedure division WINAPI.
*************************************
           ENTRY "cobstring" USING STR.
       R-APRES-1.
           MOVE STR TO PRA00W-STRING.
********************** comeca aqui ****************************
           initialize ds-control-block
           initialize PRA00W-data-block
           move "pra00w" to ds-set-name
           move ds-new-set to ds-control
           move PRA00W-data-block-version-no to
                 ds-data-block-version-no
           move PRA00W-version-no to ds-version-no
           move SPACES TO COM-PGM
           move zero to end-of-actions-flag.
************************
       R-CALL.
           MOVE SPACES TO PRA00W-TESTE
           call DSGRUN using ds-control-block,
                              PRA00W-data-block.
           move ds-continue      to ds-control
********************************
           IF   PRA00W-TESTE    = "sa"
                GO TO R-EXIT.
           GO TO R-CALL.
******************************************************************
       R-EXIT.
           move PRA00W-data-block-version-no to
                 ds-data-block-version-no
           move PRA00W-version-no to ds-version-no
           move "pst00w" to ds-set-name
           move ds-quit-set      to ds-control
           call DSGRUN using ds-control-block,
                              PRA00W-data-block.
                EXIT PROGRAM.
```

#### ↳ Re: Help- Visual Basic

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mrbcg$c6$1@hyperion.mfltd.co.uk>`
- **References:** `<8mpkjn$oi6$1@venus.telepac.pt>`

```
Raimundo,

The DLLs that 32 bit Visual BASIC creates are OLE servers and not
standard Windows DLLs.  You have to access these DLLs via OLE
and Object COBOL i.e. a CALL can no longer be used.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

Raimundo Carvalho <ray@mail.telepac.pt> wrote in message
news:8mpkjn$oi6$1@venus.telepac.pt...
> I am calling from Visual Basic a program linked with a dll extension and
> with an entry point like says the book "Microfocus Cobol- Colbol users
…[76 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
