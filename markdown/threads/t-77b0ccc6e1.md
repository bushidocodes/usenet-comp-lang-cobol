[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Doubt on Relativity performance-Record Types

_2 messages · 2 participants · 2001-02_

---

### Doubt on Relativity performance-Record Types

- **From:** Rech Informatica Ltda/Brazil <rovani@rech.com.br>
- **Date:** 2001-02-02T15:16:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95eiva$1d0$1@nnrp1.deja.com>`

```
Dear Friends,

   I am projecting a new system of revenue and I have some doubts on
how to project it to have the best possible performance with Relativity.

   Would I like to know if the primary key and the alternate keys are
used in the filters of record types?

   I have 1 file that has several record types, that are defined for
the second field of the primary key. In an alternate key this field is
defined as the first field of the alternate key. In case the keys are
used as filter of record types, I would like to know Relativity is "
intelligent " enough to use the alternate key to activate the filter of
a record type.

For instance:


           SELECT  NOBPED         ASSIGN       TO NW-DRIOBP,
                                  ORGANIZATION IS INDEXED,
                                  ACCESS MODE  IS DYNAMIC,
      *--> CHAve principal           (Ped+Tip.Regis+N.Item+Seq)-10 Bytes
                                  RECORD KEY   IS NC-CHA,
      *--> Chave Tipo reg/ped/it/seq (Tip.Regis+Ped+N.Item+Seq)-10 Bytes
                                  ALTERNATE RECORD KEY IS NC-CTP =
                                  NC-REX, NC-PEX, NC-NIS,
      *--> Chave tipo Reg/it/seq/ped (Tip.Regis+N.Item+Seq+Ped)-10 Bytes
                                  ALTERNATE RECORD KEY IS NC-CRI =
                                  NC-REX, NC-NIS, NC-PEX,
                                  LOCK MODE    IS MANUAL
                                  WITH LOCK    ON RECORD,
                                  FILE STATUS  IS FS-OBP.

       FD          NOBPED         RECORD CONTAINS 142 CHARACTERS,
                                  RECORDING MODE IS VARIABLE.
      *--> REGistro de OBservacoes de Pedidos
       01  NREG-OBP.
      *--> CHAve das observacoes do pedido - 10 Bytes
           05 NC-CHA.
      *--> numero do PEdido alfanumerico - X - 3 Bytes
              10 NC-PEX.
      *--> numero do PEDido
                 15 NC-PED        PIC IS 9(07)                   COMP-X.
      *--> tipo de REgistro alfanumerico - X - 1 Byte
              10 NC-REX.
      *--> tipo de REGistro de observacoes
                 15 NC-REG        PIC IS 9(02)                   COMP-X.
      *--> tipo de REGistro - OK/validos
                    88 NC-REGOK                   VALUES ARE 01 THRU 03.
      *--> tipo de REGistro - OBserv.do Pedido/nota
                    88 NC-REGOBP                  VALUE IS 01.
      *--> tipo de REGistro - GRaDes de quantidade
                    88 NC-REGGRD                  VALUE IS 02.
      *--> tipo de REGistro - VOLumes
                    88 NC-REGVOL                  VALUE IS 03.
      * -------------------------------------------------------------- *
      *--> Numero do Item/Sequencial - X - 6 Bytes
              10 NC-NIS.
      *--> Numero do ITem
                 15 NC-NIT        PIC IS 9(03)                   COMP-X.
      * -------------------------------------------------------------- *
      *--> SEQuencial
                 15 NC-SEQ        PIC IS 9(09)                   COMP-X.
      *--> Tabela de DEscricoes das observacoes - 132 Bytes
           05 NC-TDE.
      * -------------------------------------------------------------- *
      *--> DEScricao da observacao
              10 NC-DES           PIC IS X(132).
      * -------------------------------------------------------------- *
      *--> Tipo de Registro: 06 NC-REGCVC - Cliente Venda a Consumidor
      *--> Redefinicao p/tipo de registro: 06 - NC-REGCVC
           05 NC-R06    REDEFINES NC-TDE.
      * -------------------------------------------------------------- *
      *--> redefinicao p/Dados do COnsumidor - 107 Bytes
              10 NC-DCO.
      *--> DEscricao do Consumidor
                 15 NC-DEC        PIC IS X(32).
      *--> Inscricao EStadual da empresa/cart.identidade (pessoa fisica)
                 15 NC-IES        PIC IS X(15).
      *--> CIDade
                 15 NC-CID        PIC IS X(20).
      *--> ESTado
                 15 NC-EST        PIC IS X(02).
      *--> ENDereco
                 15 NC-END        PIC IS X(34).
      *--> CEP consumidor
                 15 NC-CEP        PIC IS 9(08)                   COMP-X.
      * -------------------------------------------------------------- *
      *--> Filler Cliente venda a Consumidor (low-values)
              10 NC-FCC           PIC IS X(25).
...
...
...

Good Bye,

---------------------------------------------------
  Rovani Marcelo Rech
  Rech Informatica Ltda - Novo Hamburgo/RS - Brazil
  www.rech.com.br - rovani@rech.com.br

Portuguese:

D�vida sobre Relativity performance.

Eu estou projetando um novo sistema de faturamento e tenho algumas
d�vidas sobre como projet�-lo para ter a melhor performance poss�vel
com o Relativity.

Eu gostaria de saber se a chave principal e as chaves alternativas s�o
utilizadas nos filtros de tipos de registros?

Eu tenho 1 arquivo que tem diversos tipos de registros, que s�o
definidos pelo segundo campo da chave principal. Em uma chave
alternativa este campo est� definido como o primeiro campo da chave
alternativa. Caso as chaves sejam utilizadas como filtro de tipos de
registros, eu gostaria de saber se o Relativity � "inteligente" o
suficiente para utilizar a chave alternativa para agilizar o filtro de
tipo de registro.



Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Doubt on Relativity performance-Record Types

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2001-02-02T13:15:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kUDe6.29$lA2.797@client>`
- **References:** `<95eiva$1d0$1@nnrp1.deja.com>`

```
Dear Rovani Marcelo Rech:

Rech Informatica Ltda/Brazil <rovani@rech.com.br> wrote in message
news:95eiva$1d0$1@nnrp1.deja.com...
> Dear Friends,
>
…[4 more quoted lines elided]…
> used in the filters of record types?

It is typical, but not necessary, that the record type field is contained in
the primary key, as well as most/all of the alternate keys.  Relativity can
work with the record type field (or fields - there can be any number of
fields used to define the record type) anywhere in the portion of the record
area shared by the various record types.


>
>    I have 1 file that has several record types, that are defined for
…[4 more quoted lines elided]…
> a record type.

The example file (which I have deleted) should work very nicely.  After
importing the file definition, define the record types using NC-REGOBP,
NC-REGGRD, and NC-REGVOL, then define the tables.  It is not necessary, or
even desirable, to include a column for NC-REG (or NC-REX) in your tables,
since the value is implied by the record type used to define the table.
Relativity will choose the best key depending on the SQL statement (usually
based upon the WHERE clause, the JOIN conditions, and the ORDER BY clause),
automatically supplying the value for NC-REG based upon the record type used
for the table.

>
> For instance:
>
>
>            SELECT  NOBPED         ASSIGN       TO NW-DRIOBP,
[snip]

Best regards,
Tom Morrison               www.liant.com
Liant Software Corporation
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
