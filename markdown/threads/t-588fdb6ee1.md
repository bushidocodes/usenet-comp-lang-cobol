[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is there a "while statement " in Cobol?

_2 messages · 2 participants · 2001-02_

---

### Re: Is there a "while statement " in Cobol?

- **From:** "pwmeister" <peter.meister@tietoenator-nospam.com>
- **Date:** 2001-02-08T12:56:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95u1d2$kma$1@news1.enator.se>`
- **References:** `<8RZf6.25$D13.51393@nnrp2.sbc.net>`

```
yes!

004958
004959 D-BEHANDLA-FEL-TTYP SECTION.
004960
004961     MOVE 'X'    TO FELPOSTER
004962
004963     MOVE C35R010-TTYP TO FEL-TTYP
004964
004965     DOWHILE IN1-POSTER-KVAR
004966       AND C35R010-FORVNR   = FORVNR IN C35CFORV
004967       AND C35R010-RSKPAR   = AKT-RSKPAR
004968       AND C35R010-REDOVDAT =  AKT-REDOVDAT
004969       AND C35R010-TTYP     = FEL-TTYP
004970           PERFORM XB-SKRIV-FELPOST
004971           PERFORM XA-NESTA-INPOST
004972     DOEND
004973
004974
004975 D-END.
004976/PAGE

that is, if you the PRECOSP precompiler.


Meesha wrote in message <8RZf6.25$D13.51393@nnrp2.sbc.net>...
>For a project in school I need to construct a grammar for while statements
>for several languages, one of them is COBOL.I couldn't come up with
anything
>conclusive on that.I would appreciate some help.
>Thanks
>Meesha
>
>
```

#### ↳ Re: Is there a "while statement " in Cobol?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-02-11T16:47:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a86c20f.4822007@news1.attglobal.net>`
- **References:** `<8RZf6.25$D13.51393@nnrp2.sbc.net> <95u1d2$kma$1@news1.enator.se>`

```
Which COBOL vendor has this construct?

On Thu, 8 Feb 2001 12:56:53 +0100, "pwmeister"
<peter.meister@tietoenator-nospam.com> wrote:

>yes!
>
…[33 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
