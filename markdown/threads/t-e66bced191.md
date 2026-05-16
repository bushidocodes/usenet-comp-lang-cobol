[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# reading a microfocus data file

_11 messages · 6 participants · 2001-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### reading a microfocus data file

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-06T19:37:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c0fc581.27893262@news.libero.it>`

```
I need to read (using Borland C or Delphi) a data file that was
written using MicroFocus Cobol on SCO Unix.

Tha data file has the following structure:

 
       01  MG-REC.
           03  MG-KEY.
               05  MG-CMAG             PIC 99.
               05  MG-CODICE          PIC X(13).
           03  MG-DES                    PIC X(30).
           03  MG-UM1                    PIC XX.
           03  MG-UM2                    PIC XX.
           03  MG-MOLTIPLICA       PIC 9(4)V9(3)    COMP-3.
           03  MG-TEMPOAPP         PIC 9(3)         COMP-3.
ianni *    03  FILLER                    PIC X(4).
ianni      03  Mg-Alimento             pic x.
ianni      03  Mg-Tipo-Vendita       pic x.
ianni      03  Mg-Pezzi-Collo          pic 9999 comp.
           03  MG-SCAPROVV         PIC X.
           03  MG-GRU-MERC         PIC X(4).
           03  MG-CIVA                    PIC 99.
           03  MG-FOR  OCCURS 5    PIC 9(6)        COMP-3.
           03  MG-CSTAT                PIC X(4).
           03  MG-CCONTR             PIC 99.
           03  MG-MESINV              PIC 99.
           03  MG-ARTALT             PIC X(13).
           03  MG-DUC                  PIC 9(6).
           03  FILLER REDEFINES    MG-DUC.
               05  MG-DUCGG          PIC 99.
               05  MG-DUCMM         PIC 99.
               05  MG-DUCAA          PIC 99.
           03  MG-DUS                  PIC 9(6).
           03  FILLER REDEFINES    MG-DUS.
               05  MG-DUSGG          PIC 99.
               05  MG-DUSMM         PIC 99.
               05  MG-DUSAA          PIC 99.
           03  MG-NGIACMED        PIC S9(9)V99    COMP-3.
           03  MG-SCOMIN             PIC 9(7)        COMP-3.
           03  MG-SCOMAX            PIC 9(7)        COMP-3.
ianni *    03  MG-RIORD             PIC 9(7)        COMP-3.
ianni      03  Mg-Peso-Pezzo        PIC 9(5)v99     COMP-3.
           03  MG-MINORD             PIC 9(5)        COMP-3.
           03  MG-UCA                    PIC 9(9)V99     COMP-3.

           03  MG-PUCA00             PIC 9(9)V99     COMP-3.
           03  MG-PROGRESSIVI.
               05  MG-QTAGIACIN    PIC S9(10)V9(5) COMP-3.
               05  MG-VALGIACIN    PIC S9(10)V9(5) COMP-3.
               05  MG-QTACARFOR    PIC S9(10)V9(5) COMP-3.
               05  MG-QTACARDIV    PIC S9(10)V9(5) COMP-3.
               05  MG-VALCAR       PIC S9(10)V9(5) COMP-3.
               05  MG-QTASCAVEN    PIC S9(10)V9(5) COMP-3.
               05  MG-QTASCADIV    PIC S9(10)V9(5) COMP-3.
               05  MG-VALSCA       PIC S9(10)V9(5) COMP-3.
               05  MG-QTAIMP       PIC S9(10)V9(5) COMP-3.
               05  MG-VALIMP       PIC S9(10)V9(5) COMP-3.
               05  MG-QTAORD       PIC S9(10)V9(5) COMP-3.
               05  MG-VALORD       PIC S9(10)V9(5) COMP-3.
           03  FILLER REDEFINES    MG-PROGRESSIVI.
               05 MG-PRG OCCURS 12 PIC S9(10)V9(5) COMP-3.
           03  MG-ESPREC           PIC S9(10)V9(5) COMP-3.
           03  MG-VALACQ00         PIC S9(10)V99   COMP-3.
           03  MG-QTAACQ00         PIC S9(10)V9(5) COMP-3.
           03  MG-QTA3M00          PIC S9(10)V9(5) COMP-3.
           03  MG-VAL3M00          PIC S9(10)V99   COMP-3.
           03  MG-QTAIN00          PIC S9(10)V9(5) COMP-3.
           03  MG-VALIN00          PIC S9(10)V99   COMP-3.
           03  MG-DUC00            PIC 9(6)        COMP-3.
           03  MG-UCA00            PIC 9(9)V99     COMP-3.
           03  MG-FLINV            PIC X.
           03  MG-FLMOV            PIC X.
ianni *    03  FILLER              PIC X(6).
ianni      03  Mg-Cod-Dogana       pic 9(11) comp-3.


If I understand well (I am no Cobol expert), 

PIC X(6) means 6 ASCII characters.
PIC 99 means 2 ASCII digits

I need to know what the following declarations mean:

PIC 9999      	COMP
PIC 9(6)        	COMP-3.
PIC 9(4)V9(3)    	COMP-3.

and how numbers are actually written to the file.

Any help ? 

Thank you

Duilio Foschi
```

#### ↳ R: reading a microfocus data file

- **From:** "matrix" <andateacagaretutti@porcaputtana.al>
- **Date:** 2001-12-06T20:44:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lMQP7.253107$sq5.12267685@news.infostrada.it>`
- **References:** `<3c0fc581.27893262@news.libero.it>`

```
Ciao, mi chiamo Fabrizio e sono un programmatore Cobol.
i vari comp-3 comp-6 eccetera sono formati di compressione
per il risparmio di memoria....cio' sisgnifica che per esempio
un formato comp non utilizza un byte per carattere ma un byte
per 2 caratteri..... ti conviene muovere questi campi in campi numerici
pic 9(n) normali prima di elaborarli
ciao......
se non sono stato abbastanza chiaro scrivi pure
Duilio Foschi <dedalus@yifan.net> wrote in message
3c0fc581.27893262@news.libero.it...
> I need to read (using Borland C or Delphi) a data file that was
> written using MicroFocus Cobol on SCO Unix.
…[91 more quoted lines elided]…
> Duilio Foschi
```

##### ↳ ↳ Re: R: reading a microfocus data file

- **From:** none@none.com (wildman)
- **Date:** 2001-12-07T16:06:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c10da88.2062549@news.uswest.net>`
- **References:** `<3c0fc581.27893262@news.libero.it> <lMQP7.253107$sq5.12267685@news.infostrada.it>`

```
On Thu, 06 Dec 2001 20:44:01 GMT, "matrix"
<andateacagaretutti@porcaputtana.al> wrote:

>Ciao, mi chiamo Fabrizio e sono un programmatore Cobol.
>i vari comp-3 comp-6 eccetera sono formati di compressione
…[103 more quoted lines elided]…
>
COMP is integer.  COMP-3 is like a floating point number written to
disk as binary data which means it does not write ASCII digits (like
PIC 99 would).  Nor is it integer.  It uses the binary number system,
so a large number like S9(10)V99 takes 6 bytes of storage.  If you're
new to COBOL, try thinking of COMP-3 fields as numbers that are
individually zipped - or as we say in COBOL - packed decimal.

I think the formula for COMP-3 was to divide the number by 2 to arrive
at the storage size.  If the length was odd, then round upwards.   For
example, PIC S9(9) COMP-3  is 5 bytes of packed decimal storage.  
The decimal point is always implied by the program picture and is not
written to disk.  

You might write a COBOL program to make things easier.  The MOVE
statement converts for you ...

MOVE  S(9)V99 [COMP-3]  TO  PIC S9(9)V99

You can also specify SIGN LEADING, TRAILING or strip it off with an
'edited' picture clause 9(9).(2) which will include the decimal point
when you write, if you need it.  Importing numbers to the likes of
MS-Access or Sequel Server usually expect the physical decimal point.
```

##### ↳ ↳ Re: R: reading a microfocus data file

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-08T18:55:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c1260ad.29781085@news.libero.it>`
- **References:** `<3c0fc581.27893262@news.libero.it> <lMQP7.253107$sq5.12267685@news.infostrada.it>`

```

>Ciao, mi chiamo Fabrizio e sono un programmatore Cobol.

Fabrizio,

ti ho scritto in email, ma sembra che la tua mail box sia piena.

Ciao

Duilio
```

#### ↳ Re: reading a microfocus data file

- **From:** "Jeff Farkas" <yo_dog40@hotmail.com>
- **Date:** 2001-12-06T16:17:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9uonaf$a1hd5$1@ID-101435.news.dfncis.de>`
- **References:** `<3c0fc581.27893262@news.libero.it>`

```

"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c0fc581.27893262@news.libero.it...
> I need to read (using Borland C or Delphi) a data file that was
> written using MicroFocus Cobol on SCO Unix.
…[83 more quoted lines elided]…
> PIC 9(4)V9(3)    COMP-3.

Those are packed data items. You might be able
to read them in but I would think the best bet is
to use COBOL to re-write the file with the items
un-packed.. IE PIC 9999 and not PIC 9999 COMP.

Jeff..

>
> and how numbers are actually written to the file.
…[5 more quoted lines elided]…
> Duilio Foschi
```

##### ↳ ↳ Re: reading a microfocus data file

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2001-12-07T14:37:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0112071437.25c4570@posting.google.com>`
- **References:** `<3c0fc581.27893262@news.libero.it> <9uonaf$a1hd5$1@ID-101435.news.dfncis.de>`

```
"Jeff Farkas" <yo_dog40@hotmail.com> wrote in message news:<9uonaf$a1hd5$1@ID-101435.news.dfncis.de>...
> "Duilio Foschi" <dedalus@yifan.net> wrote in message
> news:3c0fc581.27893262@news.libero.it...
…[44 more quoted lines elided]…
> > Duilio Foschi

Jeff has taken you part of the way, but you also need to preserve the
signs, where present, of the numeric COMP-3 fields.  Signs are
specified where the S picture character is used, for example, as in
"PIC S999v99  COMP-3".

To do this you need to specify the new numeric fields as "PIC 9(n)
SIGN IS LEADING SEPARATE CHARACTER", where 'n' is the appropriate
equivalent definition for the particular numeric field, including
decimal places where necessary.  Then, when your conversion program
moves the numeric data from the old field to the new fields, the sign
will be stored in the leading separate character.  You could instead
specify the sign as a trailing character, but it doesn't really matter
which way you do it.  Remember that as a result of the conversion the
new data record will occupy more space than the original, so you will
have to specify JCL appropriately.
```

##### ↳ ↳ Re: reading a microfocus data file

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-08T11:05:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c11f24b.1519427@news.libero.it>`
- **References:** `<3c0fc581.27893262@news.libero.it> <9uonaf$a1hd5$1@ID-101435.news.dfncis.de>`

```
Jeff,

>the best bet is to use COBOL to re-write the file with the items
>un-packed.. 


on the old system (SCO UNix)  there is microfocus compiler, but I have
no idea if and how it works.

Which is the Cobol way to write, compile and link a "hello, world"
program ?

Thank you

Duilio
```

#### ↳ Re: reading a microfocus data file

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2001-12-07T19:23:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d736ce324dcf94380d6b1ecdefeb17b9.40368@mygate.mailgate.org>`
- **References:** `<3c0fc581.27893262@news.libero.it>`

```
Ciao Duilio

Sarebbe molto piu' semplice creare un file sequenziale che contiene la
"traduzione"
dei campi COMP in campi INTERI e quindi poterli leggere con qualsiasi
linguaggio.

Se hai il file a disposizione, potrei tentare di generarti un file line 
sequential con i dati totalmente in ASCII..

Gianni
```

##### ↳ ↳ Re: reading a microfocus data file

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-08T19:01:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c1260ec.29843824@news.libero.it>`
- **References:** `<3c0fc581.27893262@news.libero.it> <d736ce324dcf94380d6b1ecdefeb17b9.40368@mygate.mailgate.org>`

```
Gianni,

>Sarebbe molto piu' semplice creare un file sequenziale che contiene la
>"traduzione"

pare proprio che questa sia la soluzione migliore.

Oltre tutto nel vecchio PC c'e' un compilatore MicroFocus che dovrebbe
funzionare.

Mi dici come faccio a testare intanto il funzionamento del compilatore
?

Come si scrive in Cobol un programma di 3 righe che faccia apparire
'ciao" sullo schermo ?

>Se hai il file a disposizione, potrei tentare di generarti un file line 
>sequential con i dati totalmente in ASCII..

il file e' a disposizione, ma stiamo parlando di molti MB.

Non sarebbe meglio cercare di fare tutto in locale, facendo viaggiare
solo un programma di conversione ?

Grazie per la disponibilita'

Duilio
```

###### ↳ ↳ ↳ Re: reading a microfocus data file

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2001-12-14T22:36:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2243ec1fdbe79ab5598966c29809582e.40368@mygate.mailgate.org>`
- **References:** `<3c0fc581.27893262@news.libero.it> <d736ce324dcf94380d6b1ecdefeb17b9.40368@mygate.mailgate.org> <3c1260ec.29843824@news.libero.it>`

```
Ciao Duilio

Mi stai chiedendo la cosa piu' "stupida" e semplice che normalmente
si fa come primo programma (Hello World!) in qualsiasi linguaggio.

Il tutto dipende da che tipo di compilatore cobol usi (Testuale o GUI).

Per far apparire la scritta "ciao" alla riga 12 position 45 dello schermo 
in DOS, prendendo a base l'Acucobol si puo' scrivere:

IDENTIFICATION DIVISION.
PROGRAM-ID.  TEST.
ENVIRONMENT DIVISION.
DATA DIVISION.
PROCEDURE DIVISION.
INIZIO.
    DISPLAY "CIAO" AT 1245 ERASE.
(oppure DISPLAY "CIAO" LINE 12 POSITION 45.)
    STOP RUN.

Per il problema della conversione, se mi fornisci il tracciato record
originale del file, posso provare a crearti un programma in cobol, che
poi dovrai adattare al compilatore dos in tuo possesso.
Cerchero' di mantenere i limiti imposti dagli standard che usano quasi 
tutti i compilatori.

La mia email: softline2000@tin.it

Ciao
Gianni


"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c1260ec.29843824@news.libero.it...

> Gianni,
> 
…[24 more quoted lines elided]…
> Duilio
```

###### ↳ ↳ ↳ Re: reading a microfocus data file

_(reply depth: 4)_

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-22T23:43:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c25177e.6298338@news.libero.it>`
- **References:** `<3c0fc581.27893262@news.libero.it> <d736ce324dcf94380d6b1ecdefeb17b9.40368@mygate.mailgate.org> <3c1260ec.29843824@news.libero.it> <2243ec1fdbe79ab5598966c29809582e.40368@mygate.mailgate.org>`

```

>Mi stai chiedendo la cosa piu' "stupida" e semplice che normalmente
>si fa come primo programma (Hello World!) in qualsiasi linguaggio.

il tuo programma non ha compilato col cobol 650 (un compilatore ANSI
shareware).

Sembra che il cobol abbia problemi di standardizzazione.

>Per il problema della conversione, se mi fornisci il tracciato record
>originale del file, posso provare a crearti un programma in cobol, che
>poi dovrai adattare al compilatore dos in tuo possesso.
>Cerchero' di mantenere i limiti imposti dagli standard che usano quasi 
>tutti i compilatori.


questo e' il primo.

Una volta capito il sistema, cerchero' di fare da solo per gli altri
4-5 formati che rimangono.

A dire il vero, ho gia' cercato di fare da solo: ho studiato il cobol
l'intero giorno.

C'e' un bellissimo tutorial su 

http://members.tripod.co.uk/ZingCOBOL/start.html .

Ho scaricato prima il cobol 650, ma si e' dimostrato ben povera cosa.

Allora ho scaricato il Fujitsu Cobol 3.0, e l'ho smanettato fino a
capire come compilare e linkare.

A dire il vero penso di essere abbastanza vicino alla meta, ma devo
aver fatto qualche piccolo errore... :) (v. il mio thread "first
conversion program: disaster").

Mi dai una mano ?

Grazie

Duilio

fd Mag-Dogana               label record is standard
                                   record contains 256 characters. 
      
       01  Io001-Rec.
           03  Io001-Key.
               05  Io001-Magazzino   pic 99.
               05  Io001-Cod-Articolo pic x(13).
               05  Io001-Numero-Doc  pic x(10).
               05  Io001-Data-Doc    pic 9(6).
               05  Io001-Num-Progr   pic 9(4).
           03  Io001-Registro        pic x(2).
           03  Io001-Serie           pic x(10).
           03  Io001-Ufficio         pic x(10).
           03  Io001-Tipo            pic x(10).
           03  Io001-Cod-Art-Dogana  pic 9(11) comp-3.
           03  Io001-Descrizione     pic x(30).
           03  Io001-Quantita        pic 9(9)v999.
           03  Io001-Tipo-Movimento  pic x.
           03  Io001-Credito-Da-Doc  pic x(10).
           03  Io001-Cod-Cliente     pic 9(6).
           03  Io001-Descr-Motonave  pic x(24).
           03  Io001-Credito-Da-Data pic 9(6).
           03  filler                pic x(94).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
