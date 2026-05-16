[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help a poor teacher...

_7 messages · 4 participants · 1998-12_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Help a poor teacher...

- **From:** "Thomas Singleton" <christiane.singleton@skynet.be>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<750po9$ki7$1@news1.skynet.be>`

```
Hello,
A friend of mine has given me all his school books and notes about cobol...
and i started to learn it, tried a few examples then tried to make a useful
program... but then problems started to arise and i finally ended with this
code (see below) and three errors line 48 , 150 and 151 about a missing or
not needed parenthesis... i can't figure this out myself so if somebody
could help, i would be very pleased...

Thanx  a lot
Thomas Singleton

ps: i'm french so my english leaves a bit to be desired...

here's the code, i suppose advanced cobol programmers will figure really
easely what it does, i believe the compiler is from microsoft and is version
4.0 or 5.0...


  identification division.
        program-id. FirstProg.
       data division.
        working-storage section.
        01 TabEtud.
         02 Etud occurs 20.
          03 Identite pic x(20).
          03 CotePr occurs 99.
           04 Non-UtilCote pic x(7).
           04 UtilCote redefines Non-UtilCote.
            05 Numer pic 999.
            05 Char pic x.
            05 Denom pic 999.
          03 CoteTot pic 999v99.
          03 CodeOrg pic x(9).
          03 CoteFin pic 99v99.
          03 CoteFin-Ed pic z9.99.
          03 TotNum pic 999v99.
          03 TotDen pic 999v99.
          03 CoteCalc pic 999v99.
        01 IdMax pic x(20).
        01 CoteMax pic 99v99.
        01 CoteMax-Ed pic z9.99 .
        01 IdMin pic x(20).
        01 CoteMin pic 99v99.
        01 CoteMin-Ed pic z9.99 .
        01 Moyenne pic 99v99.
        01 Moyenne-Ed pic z9.99 .
        01 Total pic 9999v99.
        01 e pic 99.
        01 iCote pic 99.
        01 Existe pic x(4).
        01 NbEtud pic 99.
        01 Mult pic 999.
        01 Divis pic 999.
        01 MultiCoteExs pic x(4).
        01 Ans pic x.
        01 CoteExs pic x(4).
        01 iA pic 99.
        procedure division.
         Main.
           move 1 to iA.
           move 00.00 to CoteMax.
           move 99.99 to CoteMin.
           perform Initia.
           move 1 to e.
           perform Obtention.
           perform until Existe = "faux"
            if MultiCoteExs = "faux" then
             compute CoteFin (e) = ( CoteTot (e) * Mult ) / Divis
            else
           compute CoteFin(e)=( TotNum (e iA) * Mult ) / TotDen (e iA)
                                                                      ->
error here : 48s - "missing or extra right parenthesis"

            end-if
            if CoteFin (e) > CoteMax then
             Move Identite (e) to IdMax
             Move CoteFin (e) to CoteMax
            end-if
            if CoteFin (e) < CoteMin then
             Move Identite (e) to IdMin
             move CoteFin (e) to CoteMin
            end-if
            add CoteFin (e) to Total
            add 1 to NbEtud e
            perform Obtention
           end-perform.
           compute Moyenne = Total / NbEtud.
           perform Sortie.
           stop run.
         Obtention.
           Display "Introduire Id Etud " e ", fin par xyz".
           Accept Identite (e).
           if Identite (e) = "xyz" then
            move "faux" to Existe
           else
            move "vrai" to Existe
            if Ans = "y" then
             display "Introduire la Cote totale de l'etud" e
             accept CoteTot (e)
            else
            add 1 to iA
            perform TrtBis varying iCote from 1 by 1 until CoteExs = "
      -      "faux"
            end-if
            display "Entrez le CodeOrg de l'etudiant" e
            accept CodeOrg (e)
           end-if.

         Sortie.
           display "Tableau des etudiants : ".
           display "========================" .
           display " ".
           display "Num      Nom          Cote/" Mult "       CodeOrg".
           perform Trt varying e from 1 by 1 until e > NbEtud
           move Moyenne to Moyenne-Ed.
           display "Meilleur eleve :" IdMax.
           display "Mauvais eleve :" IdMin.
           display "Moyenne :" Moyenne-Ed.
         Trt.
           move CoteFin (e) to CoteFin-Ed (e).
           display  e  Identite (e)   CoteFin-Ed (e) CodeOrg (e).

         Initia.
           display "Sur combien voulez-vous la cote finale ?".
           accept Mult.
           display "Avez-vous d�j� fait le total ? y/n".
           accept Ans.
           if Ans = "y" then
             display "Sur combien est le total ?"
             Accept Divis
           else
            if Ans = "n" then
             continue
            else
             display "Choix admis : y ou n, relancez"
            end-if
           end-if.
         TrtBis.

           display "Introduire la " iCote "eme cote, format 999/999".
           display "fin par xyz".
           accept Non-UtilCote (e iA).

           if Non-UtilCote (e iA) = "xyz" then
            move "faux" to MultiCoteExs
           else
            move "vrai" to MultiCoteExs
            move Non-UtilCote (e iA) to UtilCote (e iA)
            add Numer (e  iA  Icote)  to TotNum (e iA)        -> error here
: 48s - "missing or extra right parenthesis"
            add Denom (e  iA  Icote)  to TotDen (e iA)       -> error here :
48s - "missing or extra right parenthesis"
           end-if.
```

#### ↳ Re: Help a poor teacher...

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3673f493.0@news1.ibm.net>`
- **References:** `<750po9$ki7$1@news1.skynet.be>`

```
see below in your code...
Thomas Singleton wrote in message <750po9$ki7$1@news1.skynet.be>...
>Hello,
>A friend of mine has given me all his school books and notes about cobol...
…[12 more quoted lines elided]…
>easely what it does, i believe the compiler is from microsoft and is
version
>4.0 or 5.0...
>
…[54 more quoted lines elided]…
>error here : 48s - "missing or extra right parenthesis"

   should have spaces on both sides of =
     compute CoteFin(e) = (TotNum etc

the spaces in the insides of the parentheses- like ( Tot.. - are not needed

>
>            end-if
…[76 more quoted lines elided]…
>            add Denom (e  iA  Icote)  to TotDen (e iA)       -> error here
:
>48s - "missing or extra right parenthesis"


Numer only has two subscripts, so don't use three:  Numer(e, iA, lcote)
same with Denom.  What does lcote do? Shouldn't it be iCote?
Anyway, you can't use it as a third subscript of your table only
has two.

>           end-if.
>
>
>
>
```

##### ↳ ↳ Re: Help a poor teacher...

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3673fb9c.0@news1.ibm.net>`
- **References:** `<750po9$ki7$1@news1.skynet.be> <3673f493.0@news1.ibm.net>`

```
it is worse than I thought; totnum and totden are only one-dimensional,
so the iA subscript should not be there either...

Leif Svalgaard wrote in message <3673f493.0@news1.ibm.net>...
>see below in your code...
>Thomas Singleton wrote in message <750po9$ki7$1@news1.skynet.be>...
>>Hello,
>>A friend of mine has given me all his school books and notes about
cobol...
>>and i started to learn it, tried a few examples then tried to make a
useful
>>program... but then problems started to arise and i finally ended with
this
>>code (see below) and three errors line 48 , 150 and 151 about a missing or
>>not needed parenthesis... i can't figure this out myself so if somebody
…[149 more quoted lines elided]…
>>            add Numer (e  iA  Icote)  to TotNum (e iA)        -> error
here
>>: 48s - "missing or extra right parenthesis"
>>            add Denom (e  iA  Icote)  to TotDen (e iA)       -> error here
…[15 more quoted lines elided]…
>
```

#### ↳ Re: Help a poor teacher...

- **From:** jyazel@freenet.columbus.oh.us (Jack Yazel)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7519le$5dn@login.freenet.columbus.oh.us>`
- **References:** `<750po9$ki7$1@news1.skynet.be>`

```
Thomas Singleton (christiane.singleton@skynet.be) wrote:
:  <SNIP>
: program... but then problems started to arise and i finally ended with this
: code (see below) and three errors line 48 , 150 and 151 about a missing or
: not needed parenthesis... i can't figure this out myself so if somebody
:    <SNIP>
  -------------------------

  The items referred to only have one dimension. The references are using
two subscripts.
```

#### ↳ Re: Help a poor teacher...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<751aer$pdt$1@news.igs.net>`
- **References:** `<750po9$ki7$1@news1.skynet.be>`

```
It took me a couple of minutes, but if you count the characters on line 48,
you will find there are exactly 60.  Add in the 12 for the "area b" start,
and
I will bet that the final ")" is past column 72. The other  two errors may
very
well be similar problems.

Thomas Singleton wrote in message <750po9$ki7$1@news1.skynet.be>...
>Hello,
>A friend of mine has given me all his school books and notes about cobol...
…[12 more quoted lines elided]…
>easely what it does, i believe the compiler is from microsoft and is
version
>4.0 or 5.0...
>
…[133 more quoted lines elided]…
>            add Denom (e  iA  Icote)  to TotDen (e iA)       -> error here
:
>48s - "missing or extra right parenthesis"
>           end-if.
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Help a poor teacher...

- **From:** "Thomas Singleton" <christiane.singleton@skynet.be>
- **Date:** 1998-12-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<753lta$8bv$1@news0.skynet.be>`
- **References:** `<750po9$ki7$1@news1.skynet.be>`

```
Hello,
thanx to all the ppl who answered !!! now it compiles without errors.
there's now a logic problem that is even more difficult to tackle (at least
for me)...
here's a brief description of what i want the prog to do :
it should give me a table with the number, the name, the result on a
introduced by the user base and a small code for additional info.
i want to be able to introduce results of students as well already totalised
and not-totalised:
E.G.
 lets say student Thomas Singleton, with 2 results 25/40 and 25/60... i want
to introduce both these results and the program to calculate the total
(50/100) and the final result on 20 (10/20), and do this for more than one
student.
but i can't seem to make it stop when i have introduced all the singular
results. the part of the code supposed to do it is below. It seems that it
doesn't recognize

>           if Non-UtilCote (e iA) = "xyz" then
>            move "faux" to MultiCoteExs CoteExs

              perform TrtBis varying iCote from 1 by 1 until CoteExs = "
>      -      "faux"

I thought that it should stop asking me for results when i entered xyz as
the last resul, but it doesn't (???)
If anyone could point me to my error

Thanx a lot
Thomas Singleton


Thomas Singleton a �crit dans le message <750po9$ki7$1@news1.skynet.be>...

>            perform TrtBis varying iCote from 1 by 1 until CoteExs = "
>      -      "faux"
…[3 more quoted lines elided]…
>           end-if.


>         TrtBis.
>
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help a poor teacher...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<753p99$8fs$1@news.igs.net>`
- **References:** `<750po9$ki7$1@news1.skynet.be> <753lta$8bv$1@news0.skynet.be>`

```
Thomas Singleton wrote in message <753lta$8bv$1@news0.skynet.be>...
>Hello,
>thanx to all the ppl who answered !!! now it compiles without errors.
>there's now a logic problem that is even more difficult to tackle (at least

When you are checking for equality on any alphabetic string,
you should at the very least make sure that it is not case-dependant.
The easiest way to do that in your code, would be to convert
the input string to upper case (or lower), then check against
the uppercase (or lower) literal.  The code quoted would never
work, if for example, you had the caps lock on when you ran
it.  That may, or may not be your problem, as the code looks
OK to my eye.

Another thing that I think you should change though, is that I
would break the test line after the  "BY 1", and keep the literal
intact.  Continuations of literals is often very unclear to the
eye, because with some compilers it is column dependent. You
may very well be testing against "<blank>faux", and not realize
it. Unless a literal goes over 60 characters, I would never split
one.  It is one of the first places a pro checks for possible
errors of the sort you are experiencing.


>for me)...
>here's a brief description of what i want the prog to do :
>it should give me a table with the number, the name, the result on a
>introduced by the user base and a small code for additional info.
>i want to be able to introduce results of students as well already
totalised
>and not-totalised:
>E.G.
> lets say student Thomas Singleton, with 2 results 25/40 and 25/60... i
want
>to introduce both these results and the program to calculate the total
>(50/100) and the final result on 20 (10/20), and do this for more than one
…[48 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
