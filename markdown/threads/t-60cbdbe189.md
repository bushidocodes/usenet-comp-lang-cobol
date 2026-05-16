[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INVOKE IN COBOL

_5 messages · 4 participants · 2001-05_

---

### INVOKE IN COBOL

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2001-05-02T22:00:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cpsfr$5vg$1@venus.telepac.pt>`

```
Does somebody know where i can look for books or articles about the
instruction "Invoke" clalling class of Excel or Word with the goal of using
the Excel or Word to make list to the printer for example.

Thank you

Raimundo Carvalho
```

#### ↳ Re: INVOKE IN COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-05-03T01:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF0AF37.E14B6CD8@home.com>`
- **References:** `<9cpsfr$5vg$1@venus.telepac.pt>`

```


Raimundo Carvalho wrote:

> Does somebody know where i can look for books or articles about the
> instruction "Invoke" clalling class of Excel or Word with the goal of using
> the Excel or Word to make list to the printer for example.
>

Although the word INVOKE is used loosely in this NewsGroup by some, implying
'calling',  INVOKE is one of the new RESERVED WORDS associated with OO for :-

    invoking classes
    invoking methods

PC-wise only currently available with Fujitsu and Merant (Net Express) OO
compilers, where the OO syntax is currently 'an extension' to COBOL prior to
COBOL 2002 being released.

Meanwhile, depending upon your PC compiler you can 'call' Excel or Word using
Windows API calls if your compiler has them, or even using COBOL 'support'
products such as Flexus SP2 or Norcom Screen IO.

Check out cobolreport.com, "Gene Webb's OO Tutorial"..

Jimmy
```

##### ↳ ↳ Re: INVOKE IN COBOL

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-02T22:28:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cqj97$lap$1@nntp9.atl.mindspring.net>`
- **References:** `<9cpsfr$5vg$1@venus.telepac.pt> <3AF0AF37.E14B6CD8@home.com>`

```
Also INVOKE (and OO) is available (currently) with IBM VisualAge COBOL
```

##### ↳ ↳ Re: INVOKE IN COBOL

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-05-03T04:12:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-1xd6Qgl9cEoD@24-108-102-82.ivideon.com>`
- **References:** `<9cpsfr$5vg$1@venus.telepac.pt> <3AF0AF37.E14B6CD8@home.com>`

```
On Thu, 3 May 2001 01:06:09, "James J. Gavan" <jjgavan@home.com> 
wrote:

> 
> 
…[16 more quoted lines elided]…
> 

The IBM Visualage COBOL version 2.2 for OS/2 and Windows NT and the 
version
3.0 for NT also support all the OO syntax (or a large portion)
```

#### ↳ Re: INVOKE IN COBOL

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2001-05-03T23:29:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9csm3r$b7c$1@venus.telepac.pt>`
- **References:** `<9cpsfr$5vg$1@venus.telepac.pt>`

```
What i want is to make call to excel using vba and i have to know all kinds
of invoke of class and methods of excel to make a sucessful call to many
possibilities of excel.

For example if i want to make a copy of one sheet to another how can i do
that using invoke in NEtexpress.


Example:

           invoke excelserver "GetActiveWorkbook" returning theworkbook.
************ PARA NAO SALVAR
           if   COM-G-ARQUIVO-DISCO = 1
                invoke theWorkbook "Save"
           else invoke theWorkbook "Setsaved" using by value -1.
           invoke theWorkbook "close".
           invoke theWorkbook "finalize" returning theworkbook.

Thank you

Raimundo Carvalho


Raimundo Carvalho <ray@mail.telepac.pt> escreveu na mensagem
news:9cpsfr$5vg$1@venus.telepac.pt...
> Does somebody know where i can look for books or articles about the
> instruction "Invoke" clalling class of Excel or Word with the goal of
using
> the Excel or Word to make list to the printer for example.
>
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
