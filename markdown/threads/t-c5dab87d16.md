[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wrong calculation in NetExpress v3.0

_25 messages · 9 participants · 2001-01 → 2001-02_

---

### Wrong calculation in NetExpress v3.0

- **From:** Rech Informatica Ltda/Brazil <rovani@rech.com.br>
- **Date:** 2001-01-26T13:41:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94ruqp$kq2$1@nnrp1.deja.com>`

```
Dear Friends,

   I am sending this message to this forum, because I await return of
the support MicroFocus of the distributor in Brazil since November 24,
1999. I believe that Merant was never knowing about the mistake,
because it was never corrected. As it exists in this forum members with
direct access to Merant, I have hopes to be corrected. In Brazil, we
don't have direct access to Merant, and the local support is very weak.

   The problem is the following: When variables of the type are used V9
(02) COMP, results in wrong values. Besides, the result is different
in.INT and in.GNT, in MF-COBOL 3.2.50 (16 bits) and in the NetExpress
v3.0 (32 bits).

   Below follows the program demonstrating the mistake. It is enough to
generate it in the NetExpress v3.0 in .Int and in .Gnt.

   I apologize for my bad English.

Portuguese:
C�lculo errado no NetExpressv3.0

   Eu estou mandando esta mensagem para este f�rum, pois aguardo
retorno do suporte MicroFocus do distribuidor no Brasil desde 24 de
novembro de 1999. Eu acredito que a Merant nunca ficou sabendo do erro,
pois ele nunca foi corrigido. Como existe neste f�rum membros com
acesso direto � Merant, tenho esperan�as que o erro seja corrigido. No
Brasil, n�s n�o temos acesso direto � Merant, e o suporte local � muito
fraco.

   O problema � o seguinte: Quando s�o utilizadas vari�veis do tipo V9
(02) COMP, resulta em valores errados. Al�m disto, o resultado �
diferente em .INT e em .GNT, no MF-COBOL 3.2.50 (16 Bits) e no
NetExpress v3.0 (32 bits).

   Abaixo segue o programa demonstrando o erro. Basta ger�-lo no
NetExpress v3.0 em .Int e em .Gnt.

Pe�o desculpas pelo meu Ingl�s ruim.

---------------------------------------------------

      * -------------------------------------------------------------- *
      *                Programa de TESTE de calculo                    *
      * -------------------------------------------------------------- *
       IDENTIFICATION             DIVISION.
       PROGRAM-ID.                DECIMAL.
       ENVIRONMENT                DIVISION.
       CONFIGURATION              SECTION.
       SPECIAL-NAMES.
           DECIMAL-POINT     IS   COMMA.
       DATA                       DIVISION.
       WORKING-STORAGE            SECTION.
       01  WRK-CAMPOS.
      *--> Dia de FErias
           05 WFPF-DFE            PIC IS 9(02)    VALUE IS 1     COMP-X.
      *--> Guarda a parte decimal do calculo - formato DISPLAY
           05 W-RESTO-DISPLAY     PIC IS V9(02)   VALUE IS ZEROS.
      *--> Guarda a parte decimal do calculo - formato COMP
           05 W-RESTO-COMP        PIC IS V9(02)   VALUE IS ZEROS COMP.
      *--> Variavel para guardar o valor 30
           05 W-TRINTA            PIC IS 9(02)    VALUE IS ZEROS.
      *--> Variavel para guardar o valor 2,5
           05 W-DOISV5            PIC IS 9V9      VALUE IS ZEROS.
           05 W-MASC              PIC IS 999,99   VALUE IS ZEROS.
      * -------------------------------------------------------------- *
       PROCEDURE                  DIVISION.
      *--> Teste de calculo.............................................
       001-CALCULO.
           DISPLAY                                       SPACES AT 0101,
                                  "Calculos usando var.Display" at 0606.
      *--> Calculo com COMPUTE:
           MOVE    1         TO   WFPF-DFE.
           COMPUTE       W-RESTO-DISPLAY = 30 / 2,5.
           COMPUTE     WFPF-DFE = (W-RESTO-DISPLAY * 30) + WFPF-DFE - 1.
           MOVE    WFPF-DFE  TO   W-MASC.
           DISPLAY                "1. Calculo: " AT 0806, W-MASC.

      *--> Calculo com COMPUTE e constantes:
           MOVE    1         TO   WFPF-DFE.
           MOVE    30        TO   W-TRINTA.
           MOVE    2,5       TO   W-DOISV5.
           COMPUTE W-RESTO-DISPLAY = W-TRINTA / W-DOISV5.
           COMPUTE     WFPF-DFE = (W-RESTO-DISPLAY * 30) + WFPF-DFE - 1.
           MOVE    WFPF-DFE  TO   W-MASC.
           DISPLAY                "2. Calculo: " AT 1006, W-MASC.

      *--> Calculo com constantes.......................................
           COMPUTE W-RESTO-DISPLAY = 30 / 2,5.
           MOVE    W-RESTO-DISPLAY TO W-MASC.
           DISPLAY                "3. Calculo: " AT 1206, W-MASC.

      *--> Calculo com variaveis........................................
           MOVE    30        TO   W-TRINTA.
           MOVE    2,5       TO   W-DOISV5.
           COMPUTE W-RESTO-DISPLAY = W-TRINTA / W-DOISV5.
           MOVE    W-RESTO-DISPLAY TO W-MASC.
           DISPLAY                "4. Calculo: " AT 1406, W-MASC.
      *================================================================*
           DISPLAY                "Calculos usando var.Comp" at 0650.
      *--> Calculo com COMPUTE:
           MOVE    1         TO   WFPF-DFE.
           COMPUTE       W-RESTO-COMP = 30 / 2,5.
           COMPUTE WFPF-DFE = (W-RESTO-COMP * 30) + WFPF-DFE - 1.
           MOVE    WFPF-DFE  TO   W-MASC.
           DISPLAY                "5. Calculo: " AT 0850, W-MASC.

      *--> Calculo com COMPUTE e constantes:
           MOVE    1         TO   WFPF-DFE.
           MOVE    30        TO   W-TRINTA.
           MOVE    2,5       TO   W-DOISV5.
           COMPUTE W-RESTO-COMP = W-TRINTA / W-DOISV5.
           COMPUTE WFPF-DFE = (W-RESTO-COMP * 30) + WFPF-DFE - 1.
           MOVE    WFPF-DFE  TO   W-MASC.
           DISPLAY                "6. Calculo: " AT 1050, W-MASC.

      *--> Calculo com constantes.......................................
           COMPUTE W-RESTO-COMP = 30 / 2,5.
           MOVE    W-RESTO-COMP TO W-MASC.
           DISPLAY                "7. Calculo: " AT 1250, W-MASC.

      *--> Calculo com variaveis........................................
           MOVE    30        TO   W-TRINTA.
           MOVE    2,5       TO   W-DOISV5.
           COMPUTE W-RESTO-COMP = W-TRINTA / W-DOISV5.
           MOVE    W-RESTO-COMP TO W-MASC.
           DISPLAY                "8. Calculo: " AT 1450, W-MASC.

      *--> Encerra o programa exemplo...................................
           STOP                   RUN.
      * ------------------------- DECIMAL.CBL ------------------------ *
       END PROGRAM                DECIMAL.



---------------------------------------------------
  Rovani Marcelo Rech
  Rech Informatica Ltda - Novo Hamburgo/RS - Brazil
  www.rech.com.br - rovani@rech.com.br


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** riplin@kcbbs.gen.nz
- **Date:** 2001-01-28T02:53:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9501j0$rub$1@nnrp1.deja.com>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com>`

```


  Rech Informatica Ltda/Brazil <rovani@rech.com.br> wrote:

>    The problem is the following: When variables of the type are used
V9
> (02) COMP, results in wrong values. Besides, the result is different
> in.INT and in.GNT, in MF-COBOL 3.2.50 (16 bits) and in the NetExpress
> v3.0 (32 bits).


>            05 WFPF-DFE            PIC IS 9(02)    VALUE IS 1
COMP-X.

COMP-X is invalid for a PIC 9(2) picture.

Use 'PIC X COMP-X' or 'PIC 9(2) COMP' (or COMP-5).



Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-28T15:50:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9524e8$6r9$1@slb0.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <9501j0$rub$1@nnrp1.deja.com>`

```
Just in case someone sees this and "believes" it.  You *may* use PIC 9(n)
values with COMP-X fields (or at least you could in every Micro Focus/MERANT
version that I know of).
```

##### ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-28T15:53:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9524e9$6r9$2@slb0.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <9501j0$rub$1@nnrp1.deja.com>`

```
Just in case someone sees this and "believes" it.  You *may* use PIC 9(n)
values with COMP-X fields (or at least you could in every Micro Focus/MERANT
version that I know of).
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** keldin@earthlink.not (TJ Dombrowski)
- **Date:** 2001-01-29T03:19:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns9037E402AC020keldinearthlink@207.217.77.22>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <9501j0$rub$1@nnrp1.deja.com> <9524e9$6r9$2@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in
<9524e9$6r9$2@slb0.atl.mindspring.net>: 

>Just in case someone sees this and "believes" it.  You *may* use PIC
>9(n) values with COMP-X fields (or at least you could in every Micro
…[4 more quoted lines elided]…
> wmklein <at> ix.netcom.com

Whats COMP-X?

Coming from a person that only uses IBM VS Cobol II

TJ
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-28T22:11:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<952qlq$5ks$2@nntp9.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <9501j0$rub$1@nnrp1.deja.com> <9524e9$6r9$2@slb0.atl.mindspring.net> <Xns9037E402AC020keldinearthlink@207.217.77.22>`

```
COMP-X is a USAGE for binary items.  It is available in several PC/Unix
compilers and allows you to define binary items via the "storage" to be
allocated.  As you know IBM's mainframe compiler, consider

   05  NumField Pic S9  Comp  (or COMP-4 or Binary).

This will allocate a half-word of storage for the binary field - even though
you (theoretically) cannot have a value in it greater than +9.  Depending on
what your TRUNC compiler option is, such items may or may not actually
"allow" values up to (approximately) 32k.

In Micro Focus COBOL (for example)

  05 NumField2  Pic X  Comp-5.

allows for one byte of storage for binary use.  This allows for "legitimate"
values up to 256.

There are a "bunch" of complications for both types of fields (including
sign implications and what happens with "implicit" decimal points)  but this
should give you the BASIC idea.

P.S.  IBM COBOL for OS/390 & VM V2R2 includes support for COMP-5 which
allows for NOTRUNC (or TRUNC(BIN)) behavior even when you compile with
another TRUNC option.  However, IBM still provides NO support for 1 or 3 or
5 byte binary fields.
```

#### ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-28T13:51:23
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<951cp1$3pr$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com>`

```

    05 W-RESTO-DISPLAY     PIC IS V9(02)   VALUE IS ZEROS.
    COMPUTE       W-RESTO-DISPLAY = 30 / 2,5.
    COMPUTE W-RESTO-DISPLAY = W-TRINTA / W-DOISV5.

Unfortunately what is happening here, is each of the COMPUTE statements
which involve 30 / 2.5 (=12.0) whether in literals or data items is causing
an ON SIZE condition. Looking at the MF LRM, the rules are that when such a
condition happens and there is no ON SIZE clause, the results are undefined.

As it sometime happens in these cases, the undefined result looks like what
you want. But as it can be seen when running in .gnt (16 bit), and int (32
bit) the results are undefined, even more evident for COMP items. One can
see in 32 bit gnt code the first COMPUTE statement with a resultant DISPLAY
item giving an undefined result.

The reason there is a difference between int and gnt, 16 and 32 bit is in
the difference of the alogrithms used. Designed to give the same results
when the answer is defined, but because of different optimizations, they
don't give the same answer when the results are not defined.

I can't think of anything immdediately useful to do which would according to
any rules always give defined results (appart from putting ON SIZE ERROR
clause on your COMPUTE statements).

Regards,
Steve.

My 3.2.46 16 bit product, int code:
  Calculos usando var.Display                 Calculos usando var.Comp
  1. Calculo: 000,00                          5. Calculo: 000,00
  2. Calculo: 000,00                          6. Calculo: 000,00
  3. Calculo: 000,00                          7. Calculo: 000,00
  4. Calculo: 000,00                          8. Calculo: 000,00

My 3.2.46 16 bit product gnt code:
 Calculos usando var.Display                 Calculos usando var.Comp
 1. Calculo: 000,00                          5. Calculo: 052,00
 2. Calculo: 000,00                          6. Calculo: 052,00
 3. Calculo: 000,00                          7. Calculo: 001,76
 4. Calculo: 000,00                          8. Calculo: 001,76

My 3.1.11 NX product int code:
 Calculos usando var.Display                 Calculos usando var.Comp
 1. Calculo: 000,00                          5. Calculo: 052,00
 2. Calculo: 000,00                          6. Calculo: 052,00
 3. Calculo: 000,00                          7. Calculo: 001,76
 4. Calculo: 000,00                          8. Calculo: 001,76

My 3.1.11 NX product gnt code:
 Calculos usando var.Display                 Calculos usando var.Comp
 1. Calculo: 104,00                          5. Calculo: 104,00
 2. Calculo: 000,00                          6. Calculo: 052,00
 3. Calculo: 000,00                          7. Calculo: 012,00
 4. Calculo: 000,00                          8. Calculo: 001,76

Rech Informatica Ltda/Brazil wrote in message
<94ruqp$kq2$1@nnrp1.deja.com>...
>Dear Friends,
>
…[18 more quoted lines elided]…
>C�lculo errado no NetExpressv3.0
...
```

##### ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** Rech Informatica Ltda/Brazil <rovani@rech.com.br>
- **Date:** 2001-01-29T12:24:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<953nd0$jo6$1@nnrp1.deja.com>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk>`

```
Dear Mr.Steven,

   Thank you very much for their explanations. Even so, in the example
that I gave, I am not concerned value will be exceeded. I hoped the
result of the calculation was simply truncated, therefore for me it
only interests the decimal part. For this, the result variable is
declared like V9(02) COMP.

   I thought that should declare ON_SIZE_ERROR only if I wanted to test
a blowout of value, and no when I wanted to truncate it.

Thank's.

Portuguese:
   Muito obrigado pelas suas explica��es. Mesmo assim, no exemplo que
eu dei, n�o me interessa se o valor ser� excedido. Eu esperava que o
resultado do c�lculo fosse simplesmente truncado, pois para mim s�
interessa a parte decimal. Por isto, a vari�vel de resultado est�
declarada como V9(02) COMP.
   Eu pensava que devia declarar ON_SIZE_ERROR somente se eu quisesse
testar um estouro de valor, e n�o quando eu quisesse trunc�-lo.

Obrigado.

-----------------------------------------------
In article <951cp1$3pr$1@hyperion.mfltd.co.uk>,
  "Steven Lalewicz" <strl@mfltd.co.uk> wrote:
>
>     05 W-RESTO-DISPLAY     PIC IS V9(02)   VALUE IS ZEROS.
…[3 more quoted lines elided]…
> Unfortunately what is happening here, is each of the COMPUTE
statements
> which involve 30 / 2.5 (=12.0) whether in literals or data items is
causing
> an ON SIZE condition. Looking at the MF LRM, the rules are that when
such a
> condition happens and there is no ON SIZE clause, the results are
undefined.
>
> As it sometime happens in these cases, the undefined result looks
like what
> you want. But as it can be seen when running in .gnt (16 bit), and
int (32
> bit) the results are undefined, even more evident for COMP items. One
can
> see in 32 bit gnt code the first COMPUTE statement with a resultant
DISPLAY
> item giving an undefined result.
>
> The reason there is a difference between int and gnt, 16 and 32 bit
is in
> the difference of the alogrithms used. Designed to give the same
results
> when the answer is defined, but because of different optimizations,
they
> don't give the same answer when the results are not defined.
>
> I can't think of anything immdediately useful to do which would
according to
> any rules always give defined results (appart from putting ON SIZE
ERROR
> clause on your COMPUTE statements).
>
…[36 more quoted lines elided]…
> >the support MicroFocus of the distributor in Brazil since November
24,
> >1999. I believe that Merant was never knowing about the mistake,
> >because it was never corrected. As it exists in this forum members
with
> >direct access to Merant, I have hopes to be corrected. In Brazil, we
> >don't have direct access to Merant, and the local support is very
weak.
> >
> >   The problem is the following: When variables of the type are used
V9
> >(02) COMP, results in wrong values. Besides, the result is different
> >in.INT and in.GNT, in MF-COBOL 3.2.50 (16 bits) and in the NetExpress
> >v3.0 (32 bits).
> >
> >   Below follows the program demonstrating the mistake. It is enough
to
> >generate it in the NetExpress v3.0 in .Int and in .Gnt.
> >
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-29T15:49:45
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<954841$dg7$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com>`

```
Rech Informatica Ltda/Brazil wrote in message
<953nd0$jo6$1@nnrp1.deja.com>...
>Dear Mr.Steven,
>
…[9 more quoted lines elided]…
>Thank's.

Does not look like there is direct way of doing this. Truncation only
occurs if the target item can't hold all the positions after the decimal
point. Say in a COMPUTE PIC-99V99 = PIC-99V9999

With COMPUTE .. ON SIZE ERROR, if the ON SIZE ERROR is executed, then the
rules are the resultant data item is untouched. So one can't achieve the
truncation you wish this way either.

One way to achieve what you what might be:

05 BIG-ITEM            PIC 9(9)V9(9).
05 W-RESTO-DISPLAY     PIC IS V9(02)   VALUE IS ZEROS.
COMPUTE BIG-ITEM = 30 / 2.5
MOVE BIG-ITEM TO W-RESTO-DISPLAY

For more information on this issue, you may wish to consult the LRM
Chapter 4 looking at the paragraphs, The ROUNDED Phrase, and ON SIZE
ERROR Phrase.

Regards,
Steve.
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-09T07:40:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A839EEA.CD2D3257@Azonic.co.nz>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <954841$dg7$1@hyperion.mfltd.co.uk>`

```
Steven Lalewicz wrote:
> 
> One way to achieve what you what might be:
…[4 more quoted lines elided]…
> MOVE BIG-ITEM TO W-RESTO-DISPLAY


Or redefine Big-Item as:

   05  Big-Split REDEFINES Big-Item.
       07  Big-Integer    PIC 9(9).
       07  Big-Fraction   PIC V99.
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-29T11:08:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95483a$cd3$1@nntp9.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com>`

```
TRUNCATION is by definition a case of "ON SIZE ERROR" - and hence falls into
its rules.  If specified, the ON SIZE ERROR statement will be reached - if
not specified "results are semi-unpredictable".

If what you really want is TRUNCATION, then do the arithmetic into a field
"large enough" to hold the full value - then MOVE it to the field where you
want truncation.  (MOVE "defines" truncation - arithmetic does NOT)
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-01-29T13:20:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<954caf$2s82$1@news.hitter.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net>`

```
The TRUNC compiler directive changes ANSI behavior for
truncation of arithmetic results.

Using 3.2.24, with TRUNC"ANSI", running an INT showed 000,00
for all results. Running a GNT showed some non-zero values.

With TRUNC, running the INT still showed 000,00; but the GNT
also showed 000,00 for all calculations.

I do not have Net Express and cannot test the behavior of TRUNC
in that product.
------------------
Rick Smith

William M. Klein wrote in message <95483a$cd3$1@nntp9.atl.mindspring.net>...
>TRUNCATION is by definition a case of "ON SIZE ERROR" - and hence falls
into
>its rules.  If specified, the ON SIZE ERROR statement will be reached - if
>not specified "results are semi-unpredictable".
…[90 more quoted lines elided]…
>> >  4. Calculo: 000,00                          8. Calculo: 001,76
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-29T14:43:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<954kla$udu$1@slb7.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net>`

```
This is why I say that "truncation" with arithmetic expression is
"semi-undefined" - because what you REALLY have is an ON SIZE ERROR
condition (whether or not you actually test for it).

As I stated earlier, if what you WANT is truncation "from" an arithmetic
expression - then you need to store the resultant value (from the arithmetic
operation) in a "large enough" field and then MOVE it to the field to do
truncation.
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-01-29T19:21:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9551h9$j9r$1@news.hitter.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net>`

```
Bill, we are not on the same page yet.

The TRUNC directive affects truncation when storing the
results of arithmetic statements into binary fields that have
a numeric picture.

TRUNC"ANSI" causes truncation of values moved to the
destination. On arithmetic statements where a size error
condition exists, the result is undefined.

TRUNC"ANSI" is the default behavior and, to acheive the
desired truncation of arithmetic statements, a "large enough"
programmer-defined intermediate field must be used to
prevent an undefined result from the arithmetic statement,
then the value of that field must be moved to the destination.

What I am saying is; that when TRUNC is specified, the result
of an arithmetic statement is truncated to the picture before
storing the result. There is no need for a programmer-defined
field "large enough" to hold the untruncated value and no need
to MOVE the result to the destination.

I am also saying: Using the directive

      $SET TRUNC

will likely give "Rech Informatica Ltda/Brazil"
<rovani@rech.com.br> the desired result with no other
changes. This is what my tests with MF WB 3.2.24 showed.

Whether it is wise to use the TRUNC directive, is different
question.
------------------
Rick Smith

William M. Klein wrote in message <954kla$udu$1@slb7.atl.mindspring.net>...
>This is why I say that "truncation" with arithmetic expression is
>"semi-undefined" - because what you REALLY have is an ON SIZE ERROR
…[3 more quoted lines elided]…
>expression - then you need to store the resultant value (from the
arithmetic
>operation) in a "large enough" field and then MOVE it to the field to do
>truncation.
…[19 more quoted lines elided]…
>> Rick Smith
[...]
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-30T07:13:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A76CC0D.37C5D3F1@brazee.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net> <9551h9$j9r$1@news.hitter.net>`

```


Rick Smith wrote:

> Bill, we are not on the same page yet.
>
…[22 more quoted lines elided]…
>       $SET TRUNC

I try to avoid compiler directive dependent code.  While it is somewhat
acceptable if the compiler directives can be placed in the code (won't work
here, as Endevor is set up to fail with them), compiler dependent code is
vulnerable when maintenance is done with a different compiler switch.   So I
have a called program to pull out an IDMS db-key out of a field which has a
CoBOL picture which is too small for it.   If there is a way to do it with
standard CoBOL code, I prefer that method.
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-01-30T11:43:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<956rdp$2leb$1@news.hitter.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net> <9551h9$j9r$1@news.hitter.net> <3A76CC0D.37C5D3F1@brazee.net>`

```

Howard Brazee wrote in message <3A76CC0D.37C5D3F1@brazee.net>...
>
>Rick Smith wrote:
[...]
>> I am also saying: Using the directive
>>
…[6 more quoted lines elided]…
>standard CoBOL code, I prefer that method.

I agree. Having considered the subject "Wrong calculation"
problem, in depth, I would prefer FUNCTION REM for COBOL 85
(or FRACTION-PART for the draft COBOL standard) to correct for
the undefined result. The use of these intrinsic functions makes it
more clear that only the portion to the right of the decimal point is
significant.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 7)_

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-30T15:36:17
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<956rnk$n52$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net> <9551h9$j9r$1@news.hitter.net>`

```
I'm not sure putting a $SET TRUNC at the top of the program
is the complete answer to this.

There is a little clause in the LRM (in the section of COMP data
items):

'Regardless of the setting of any directive, an arithmetic statement
gives the size error condition if the result has more decimal digits
than specified in the PICTURE clause of a receiving item.'

I created two versions of the program, one which has
ON SIZE ERROR DISPLAY "EOS" AT .... on each COMPUTE. With $SET TRUNC
all the COMPUTE W-RESTO-DISPLAY and COMPUTE W-RESTO-COMP still
give the ON SIZE ERROR condition.

The other version, I changed all the 2.5 to 2.8 just to see the
fraction part was being evaluated correctly, since I think one needs
to do a bit more testing to show predictable results are happening.

Certainly running this does appear to give the correct results, but
speaking to the developer who works on the code generation part
(create the .gnt files), he says the generator assumes that the
results can be undefined if an on size condition happens and there
is NO SIZE ERROR clause.

It is pretty obvious the TRUNC directive has effected the results
(seemingly for the better). I'm currently trying to produce an
example which shows unpredictable results, but failed so far!

I would suggest the code be changed as Bill (and myself also)
suggested, by doing the COMPUTE in a data item which can hold the
result and then do the truncation via a MOVE statement.

When I've figured out the ins and out of what is happening with
the TRUNC directive, I'll drop another post.

Regards,
Steve.

Rick Smith wrote in message <9551h9$j9r$1@news.hitter.net>...
>Bill, we are not on the same page yet.
>
…[66 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-31T08:07:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<959673$fk3$1@slb7.atl.mindspring.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net> <9551h9$j9r$1@news.hitter.net> <956rnk$n52$1@hyperion.mfltd.co.uk>`

```
The thing about "undefined results" (in general) is that they MAY produce
the correct results (sometimes).  HOWEVER, (and I am *not* saying that Micro
Focus/MERANT has done this often - but other vendors certainly have), even
if something works "today" - it may not in a future maintenance or release
level.

Therefore, I would still say to Rick (and Steven) that even if you could
test every POSSIBLE variation today and get the "desired" results, that this
is still "undefined" behavior and applications should not be coded to "rely"
on it.  I think that Steven and I are in agreement on this - and even Rick
indicated that he didn't like "relying" on compiler directive behavior - if
there were other ways of accomplishing the same thing.
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 9)_

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-31T18:04:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<959oov$191$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <954caf$2s82$1@news.hitter.net> <954kla$udu$1@slb7.atl.mindspring.net> <9551h9$j9r$1@news.hitter.net> <956rnk$n52$1@hyperion.mfltd.co.uk> <959673$fk3$1@slb7.atl.mindspring.net>`

```
William M. Klein wrote in message <959673$fk3$1@slb7.atl.mindspring.net>...
>The thing about "undefined results" (in general) is that they MAY produce
>the correct results (sometimes).  HOWEVER, (and I am *not* saying that
Micro
>Focus/MERANT has done this often - but other vendors certainly have), even
>if something works "today" - it may not in a future maintenance or release
…[3 more quoted lines elided]…
>test every POSSIBLE variation today and get the "desired" results, that
this
>is still "undefined" behavior and applications should not be coded to
"rely"
>on it.  I think that Steven and I are in agreement on this - and even Rick
>indicated that he didn't like "relying" on compiler directive behavior - if
>there were other ways of accomplishing the same thing.
>

Bill,

I was surprised the TRUNC directive did change the results, as I was
assuming it was not going to affect COMPUTE statement. I like to try
and prove theory with practice and if they don't match try and work
out why (in this case cause my theory was wrong :-( ).

I've had another chat with the generator developers and they now
 confirm that the TRUNC directive ($SET TRUNC) does effect not just MOVE
statements, but COMPUTE, ADD etc (only for COMP, BINARY and COMP-4) items.
Just like it says in the manuals.

The purpose of the TRUNC ($SET TRUNC) directive they say is to give
defined results when a ON SIZE condition happens. Which is truncation
to the size given by the item's PICTURE clause. So one can use the TRUNC
directive to give predicted results here.

However TRUNC does not effect DISPLAY data items. So in theory the
behaviour can still be undefined when an ON SIZE condition happens.

Also one has to be careful with the demo supplied because some of the
COMPUTES use COMP-X items and they are another law onto their own...

Regards,
Steve.


>--
>Bill Klein
…[84 more quoted lines elided]…
>> >>As I stated earlier, if what you WANT is truncation "from" an
arithmetic
>> >>expression - then you need to store the resultant value (from the
>> >arithmetic
>> >>operation) in a "large enough" field and then MOVE it to the field to
do
>> >>truncation.
>> >>
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Wrong calculation in NetExpress v3.0

_(reply depth: 4)_

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-01-29T18:24:53
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<954h77$eh9$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net>`

```

William M. Klein wrote in message <95483a$cd3$1@nntp9.atl.mindspring.net>...
>TRUNCATION is by definition a case of "ON SIZE ERROR" - and hence falls
into
>its rules.  If specified, the ON SIZE ERROR statement will be reached - if
>not specified "results are semi-unpredictable".
…[4 more quoted lines elided]…
>

Ah, that would be the 'Standard Alignment Rules'.

I was looking at these rules, but being no where near the MOVE verb or the
section on ON SIZE ERROR, I was uncertain if it was really talking about the
MOVE statement so I was reluctant to mention them in my second response.
Page
2-34 V4.0 LRM or page IV-16 in my copy of the ANS 85 Standard. Reading them
again, what else could it be refering to.

Regards,
Steve.
```

###### ↳ ↳ ↳ Using MOVE to Truncate is Counter-Intuitive (was: Re: Wrong calculation in NetExpress v3.0)

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-02-03T21:33:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95if88$rl3$1@news.hitter.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net>`

```
Bill, I was stunned by your comment! I have never seen or
heard anyone mention anything like it before. (That means
I think it deserves more comment! It also means I had to
think about for a few days!) ;-)

Never would I have considered using MOVE in a way that
would normally be considered an error. Showing a sales
total as $995,000.00 one month and $  1,000.00 the next
after an increase of $  6,000.00, is something I would never
want to happen. Because we seek to avoid a loss of digits,
using a MOVE to cause such a loss is counter-intutive.

Nonetheless, it is interesting. The following program may
not be the best or most efficient example; but it is simple.
In one MOVE with three destinations, a date in one format
is converted, truncated, and re-formatted into another. The
trick is in the pictures.

      $set flag"ans85" flagas"s"
       identification division.
       program-id. c-i.
       data division.
       working-storage section.
       01 a-date-yyyymmdd comp pic 9(8).
       01 formatted-date.
         03 formatted-month pic z9pp.
         03 pic x value "/".
         03 formatted-day pic 99.
         03 pic x value "/".
         03 formatted-year pic 9(4)p(4).
       procedure division.
       begin.
           compute a-date-yyyymmdd =
               function numval ( function current-date (1:8) )
           move a-date-yyyymmdd to
              formatted-month
              formatted-day
              formatted-year
           display formatted-date
           stop run
           .
       end program c-i.
------------------
Rick Smith

William M. Klein wrote in message <95483a$cd3$1@nntp9.atl.mindspring.net>...
[...]
>
>If what you really want is TRUNCATION, then do the arithmetic into a field
>"large enough" to hold the full value - then MOVE it to the field where you
>want truncation.  (MOVE "defines" truncation - arithmetic does NOT)
```

###### ↳ ↳ ↳ Re: Using MOVE to Truncate is Counter-Intuitive (was: Re: Wrong calculation in NetExpress v3.0)

_(reply depth: 5)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-05T01:59:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FNnf6.188$4t3.38555@newsread2.prod.itd.earthlink.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <95if88$rl3$1@news.hitter.net>`

```
Eeek!


"Rick Smith" <ricksmith@aiservices.com> wrote in message
news:95if88$rl3$1@news.hitter.net...
> Bill, I was stunned by your comment! I have never seen or
> heard anyone mention anything like it before. (That means
…[43 more quoted lines elided]…
> William M. Klein wrote in message
<95483a$cd3$1@nntp9.atl.mindspring.net>...
> [...]
> >
> >If what you really want is TRUNCATION, then do the arithmetic into
a field
> >"large enough" to hold the full value - then MOVE it to the field
where you
> >want truncation.  (MOVE "defines" truncation - arithmetic does NOT)
>
>
>
>
```

###### ↳ ↳ ↳ Re: Using MOVE to Truncate is Counter-Intuitive (was: Re: Wrong calculation in NetExpress v3.0)

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-02-07T12:46:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95s1ut$2knu$1@news.hitter.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <95if88$rl3$1@news.hitter.net> <FNnf6.188$4t3.38555@newsread2.prod.itd.earthlink.net>`

```

Jerry P wrote in message ...
>Eeek!

You can make the same comment about the results of
performance testing.

I ran 5 tests. Each was run 400 000 times. Two served
as baselines for comparison. Three to test the performance
using different types as the sending field for the MOVE.
The results are given in DOS timer ticks, approximately
55 ms per tick.

Baseline static 3
Baseline move 18
Binary 75
Packed 58
Display 50

Baseline static consists of three moves from numeric
display to numeric-edited (one field) and numeric display
(two fields).

Baseline move consists of, first, moving numeric binary
to numeric display then the three moves of Baseline
static.

The Binary, Packed, and Display tests each used a
single move statement with three destinations; as in
the following:
            move binary-yyyymmdd to
               formatted-month
               formatted-day
               formatted-year
Each of the receiving fields was scaled using P in the
picture clause.

A comparison of the results of the Basline tests shows
how expensive radix conversion can be on a machine
with no hardware assist.

Comparing the single moves to the Baselines shows
how expensive using P in the picture clause can be.

Perhaps the reason truncation with MOVE is seldom
discussed is because there is seldom any benefit.

I used the MF 3.2.24 compiler for testing.
The complete test program follows:
---------
       identification division.
       program-id. date-t.
      * Tests speed for formatting a date using
      * different methods and data types.
      * MS-DOS specific - accesses BIOS data for timing
       data division.
       working-storage section.
       01 binary-yyyymmdd binary pic 9(8).
       01 pd-yyyymmdd packed-decimal pic 9(9).
       01 disp-yyyymmdd pic 9(8).
       01 redefines disp-yyyymmdd.
         03 rd-year pic 9(4).
         03 rd-month pic 99.
         03 rd-day pic 99.
       01 formatted-date.
         03 formatted-month pic z9pp.
         03 pic x value "/".
         03 formatted-day pic 99.
         03 pic x value "/".
         03 formatted-year pic 9(4)p(4).
       01 redefines formatted-date.
         03 rd-formatted-month pic z9.
         03 pic x.
         03 rd-formatted-day pic 99.
         03 pic x.
         03 rd-formatted-year pic 9(4).
       01 test-type pic x(10).
       01 test-time pic zzz9.
       01 start-of-test comp-5 pic x(4).
       01 end-of-test comp-5 pic x(4).
       01 number-of-tests comp-5 pic 9(8) value 400000.
       01 address-of-timer.
         03 timer-location comp-5 pic xx value h"006c".
         03 timer-segment comp-5 pic xx value h"0040".
       01 pointer-to-timer redefines address-of-timer pointer.
       linkage section.
       01 bios-timer comp-5 pic x(4).
       procedure division.
       begin.
           set address of bios-timer to pointer-to-timer
           compute binary-yyyymmdd =
               function numval ( function current-date (1:8) )
           move binary-yyyymmdd to disp-yyyymmdd
           move binary-yyyymmdd to pd-yyyymmdd
           perform baseline-tests
           perform single-move-tests
           stop run
           .
       baseline-tests.
           move bios-timer to start-of-test
           perform baseline-static number-of-tests times
           move bios-timer to end-of-test
           compute test-time = end-of-test - start-of-test
           move "Baseline:" to test-type
           display test-type test-time space formatted-date

           move bios-timer to start-of-test
           perform baseline-move number-of-tests times
           move bios-timer to end-of-test
           compute test-time = end-of-test - start-of-test
           move "BL Move:" to test-type
           display test-type test-time space formatted-date
           .
       baseline-static.
           move rd-month to rd-formatted-month
           move rd-day to rd-formatted-day
           move rd-year to rd-formatted-year
           .
       baseline-move.
           move binary-yyyymmdd to disp-yyyymmdd
           move rd-month to rd-formatted-month
           move rd-day to rd-formatted-day
           move rd-year to rd-formatted-year
           .
       single-move-tests.
           move bios-timer to start-of-test
           perform single-move-binary number-of-tests times
           move bios-timer to end-of-test
           compute test-time = end-of-test - start-of-test
           move "Binary:" to test-type
           display test-type test-time space formatted-date

           move bios-timer to start-of-test
           perform single-move-pd number-of-tests times
           move bios-timer to end-of-test
           compute test-time = end-of-test - start-of-test
           move "Packed:" to test-type
           display test-type test-time space formatted-date

           move bios-timer to start-of-test
           perform single-move-disp number-of-tests times
           move bios-timer to end-of-test
           compute test-time = end-of-test - start-of-test
           move "Display:" to test-type
           display test-type test-time space formatted-date
           .
       single-move-binary.
           move binary-yyyymmdd to
              formatted-month
              formatted-day
              formatted-year
           .
       single-move-pd.
           move pd-yyyymmdd to
              formatted-month
              formatted-day
              formatted-year
           .
       single-move-disp.
           move disp-yyyymmdd to
              formatted-month
              formatted-day
              formatted-year
           .
       end program date-t.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Using MOVE to Truncate is Counter-Intuitive (was: Re: Wrong calculation in NetExpress v3.0)

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-07T12:43:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A81A55B.83426153@brazee.net>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <95if88$rl3$1@news.hitter.net> <FNnf6.188$4t3.38555@newsread2.prod.itd.earthlink.net> <95s1ut$2knu$1@news.hitter.net>`

```
Rick Smith wrote:

> Baseline static 3
> Baseline move 18
…[3 more quoted lines elided]…
>

...


> I used the MF 3.2.24 compiler for testing.
> The complete test program follows:

I would think that the difference between binary and packed arithmetic
(or between signed and unsigned) could be largely influenced by hardware
as well as compiler.  If there is a machine language command for add
packed - or for that matter add decimal, or whether these are emulated
in software could make a big difference.
```

###### ↳ ↳ ↳ Re: Using MOVE to Truncate is Counter-Intuitive (was: Re: Wrong calculation in NetExpress v3.0)

_(reply depth: 5)_

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-02-05T19:18:19
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95n32g$fv3$1@hyperion.mfltd.co.uk>`
- **References:** `<94ruqp$kq2$1@nnrp1.deja.com> <951cp1$3pr$1@hyperion.mfltd.co.uk> <953nd0$jo6$1@nnrp1.deja.com> <95483a$cd3$1@nntp9.atl.mindspring.net> <95if88$rl3$1@news.hitter.net>`

```
Rick,

For some reason the original poster was wanting to truncate his
data in a defined way (only wanted to retain the decimal fraction
after a calculation). Using a MOVE statement is a defined way
to do this. So a specific recomendation for a specific task.

Regards,
Steve.

Rick Smith wrote in message <95if88$rl3$1@news.hitter.net>...
>Bill, I was stunned by your comment! I have never seen or
>heard anyone mention anything like it before. (That means
>I think it deserves more comment! It also means I had to
>think about for a few days!) ;-)
>

...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
