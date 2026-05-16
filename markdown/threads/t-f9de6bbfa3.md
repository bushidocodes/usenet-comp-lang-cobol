[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for cobol assistance

_11 messages · 5 participants · 2003-01_

---

### Looking for cobol assistance

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-01T10:13:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qbzQ9.55855$R45.2578585@news2.tin.it>`

```
Dear friend,

I am a person of an Italian small company.

I use from about 7-8 years one cobol 45 program that run very right, for the
work of my company;
the program was made only for me by a good boy that now is not here.

My problem is this: all the number price of the program was made without
"dot" (0000000) because with the old money not necessary
(example 100000 lire) ; now there is the ? Euro and the same example is
51,16 Euro.
For this I use again the old money because my program is very important for
me.

I wanted a good person that can modify my program for the use of the "
00000,00"

or , pheraps no possible, that is able to make a program that change all my
video result money in the same result   : 1936,27  (conversion with Euro) .

This my necessity is very very  important for me.

I hope for your answer.

Many thanks for time and consideration.

 Best regards
Celestino Costa

Via Martiri della Libert� 71 Massa Lombarda 48024 Ra Italy
www.costacelestino.it
```

#### ↳ Re: Looking for cobol assistance

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-01-01T13:27:46+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it>`

```
On Wed, 01 Jan 2003 10:13:42 GMT "\(www.teknosoluzioni.it\)" <tatife@tin.it>
wrote:

:>I am a person of an Italian small company.

:>I use from about 7-8 years one cobol 45 program that run very right, for the
:>work of my company;
:>the program was made only for me by a good boy that now is not here.

:>My problem is this: all the number price of the program was made without
:>"dot" (0000000) because with the old money not necessary
:>(example 100000 lire) ; now there is the ? Euro and the same example is
:>51,16 Euro.
:>For this I use again the old money because my program is very important for
:>me.

:>I wanted a good person that can modify my program for the use of the "
:>00000,00"

Change the PICTURE to 999999,99

Note that this will take one more print column (though with the use of the
Euro you may have less digits).

:>or , pheraps no possible, that is able to make a program that change all my
:>video result money in the same result   : 1936,27  (conversion with Euro) .

How would you know the fields? If they have a PICTURE with $ (or whatever the
Italian equivalent is) you could write a program or script to change them.
```

##### ↳ ↳ Re: Looking for cobol assistance

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-01T18:19:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yiGQ9.45395$Q%4.1423886@news1.tin.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com>`

```
Dear Mr. Binyamin Dissen,
the problem is that:  I don't know the program cobol.
I am only the utilizer !
Many thanks for every answer.
     Regards
Celestino Costa


"Binyamin Dissen" <postingid@dissensoftware.com> ha scritto nel messaggio
news:v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com...
> On Wed, 01 Jan 2003 10:13:42 GMT "\(www.teknosoluzioni.it\)"
<tatife@tin.it>
> wrote:
>
> :>I am a person of an Italian small company.
>
> :>I use from about 7-8 years one cobol 45 program that run very right, for
the
> :>work of my company;
> :>the program was made only for me by a good boy that now is not here.
…[5 more quoted lines elided]…
> :>For this I use again the old money because my program is very important
for
> :>me.
>
…[8 more quoted lines elided]…
> :>or , pheraps no possible, that is able to make a program that change all
my
> :>video result money in the same result   : 1936,27  (conversion with
Euro) .
>
> How would you know the fields? If they have a PICTURE with $ (or whatever
the
> Italian equivalent is) you could write a program or script to change them.
>
…[4 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: Looking for cobol assistance

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-01-01T20:33:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com> <yiGQ9.45395$Q%4.1423886@news1.tin.it>`

```
On Wed, 01 Jan 2003 18:19:10 GMT "\(www.teknosoluzioni.it\)" <tatife@tin.it>
wrote:

:>the problem is that:  I don't know the program cobol.
:>I am only the utilizer !
:>Many thanks for every answer.

If you don't have the source code...

If the program is going to print you can redirect the print to disk and then
post process it (as you know which columns you want to play with).

I am not sure what you would do if it is going to a screen.

:>"Binyamin Dissen" <postingid@dissensoftware.com> ha scritto nel messaggio
:>news:v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com...
:>> On Wed, 01 Jan 2003 10:13:42 GMT "\(www.teknosoluzioni.it\)"
:><tatife@tin.it>
:>> wrote:

:>> :>I am a person of an Italian small company.

:>> :>I use from about 7-8 years one cobol 45 program that run very right, for
:>the
:>> :>work of my company;
:>> :>the program was made only for me by a good boy that now is not here.

:>> :>My problem is this: all the number price of the program was made without
:>> :>"dot" (0000000) because with the old money not necessary
:>> :>(example 100000 lire) ; now there is the ? Euro and the same example is
:>> :>51,16 Euro.
:>> :>For this I use again the old money because my program is very important
:>for
:>> :>me.

:>> :>I wanted a good person that can modify my program for the use of the "
:>> :>00000,00"

:>> Change the PICTURE to 999999,99

:>> Note that this will take one more print column (though with the use of the
:>> Euro you may have less digits).

:>> :>or , pheraps no possible, that is able to make a program that change all
:>my
:>> :>video result money in the same result   : 1936,27  (conversion with
:>Euro) .

:>> How would you know the fields? If they have a PICTURE with $ (or whatever
:>the
:>> Italian equivalent is) you could write a program or script to change them.
```

###### ↳ ↳ ↳ Re: Looking for cobol assistance

_(reply depth: 4)_

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-02T20:21:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb1R9.49289$Q%4.1583821@news1.tin.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com> <yiGQ9.45395$Q%4.1423886@news1.tin.it> <vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com>`

```
Dear Binyamin, many thanks for your good idea !!

The program is able to print, so ,if I understand right, is pheraps possible
to capture the record of print and modify it to have the right result in
video and print ?

I will try to find the original cobol code, yet I keep in serious
consideration your possibility.

I write you again.

    Regards
Celestino Costa

"Binyamin Dissen" <postingid@dissensoftware.com> ha scritto nel messaggio
news:vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com...
> On Wed, 01 Jan 2003 18:19:10 GMT "\(www.teknosoluzioni.it\)"
<tatife@tin.it>
> wrote:
>
…[6 more quoted lines elided]…
> If the program is going to print you can redirect the print to disk and
then
> post process it (as you know which columns you want to play with).
>
> I am not sure what you would do if it is going to a screen.
>
> :>"Binyamin Dissen" <postingid@dissensoftware.com> ha scritto nel
messaggio
> :>news:v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com...
> :>> On Wed, 01 Jan 2003 10:13:42 GMT "\(www.teknosoluzioni.it\)"
…[5 more quoted lines elided]…
> :>> :>I use from about 7-8 years one cobol 45 program that run very right,
for
> :>the
> :>> :>work of my company;
> :>> :>the program was made only for me by a good boy that now is not here.
>
> :>> :>My problem is this: all the number price of the program was made
without
> :>> :>"dot" (0000000) because with the old money not necessary
> :>> :>(example 100000 lire) ; now there is the ? Euro and the same example
is
> :>> :>51,16 Euro.
> :>> :>For this I use again the old money because my program is very
important
> :>for
> :>> :>me.
>
> :>> :>I wanted a good person that can modify my program for the use of the
"
> :>> :>00000,00"
>
> :>> Change the PICTURE to 999999,99
>
> :>> Note that this will take one more print column (though with the use of
the
> :>> Euro you may have less digits).
>
> :>> :>or , pheraps no possible, that is able to make a program that change
all
> :>my
> :>> :>video result money in the same result   : 1936,27  (conversion with
> :>Euro) .
>
> :>> How would you know the fields? If they have a PICTURE with $ (or
whatever
> :>the
> :>> Italian equivalent is) you could write a program or script to change
them.
>
> --
…[3 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: Looking for cobol assistance

_(reply depth: 5)_

- **From:** rondos@zahav.net.il (davidc)
- **Date:** 2003-01-03T00:33:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a5699b5.0301030033.338e32ea@posting.google.com>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com> <yiGQ9.45395$Q%4.1423886@news1.tin.it> <vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com> <eb1R9.49289$Q%4.1583821@news1.tin.it>`

```
If You have got the original sources, You do not need to deal with
redirections. You can just change the source and this will solve Your
problems both for the printed reports and for the screen input.

"\(www.teknosoluzioni.it\)" <tatife@tin.it> wrote in message news:<eb1R9.49289$Q%4.1583821@news1.tin.it>...
> Dear Binyamin, many thanks for your good idea !!
> 
…[82 more quoted lines elided]…
> > Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: Looking for cobol assistance

_(reply depth: 6)_

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-03T20:53:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qLmR9.52963$Q%4.1737275@news1.tin.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <v4k51v0nl6641qdj22p1v6do1ffk2tmp7k@4ax.com> <yiGQ9.45395$Q%4.1423886@news1.tin.it> <vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com> <eb1R9.49289$Q%4.1583821@news1.tin.it> <4a5699b5.0301030033.338e32ea@posting.google.com>`

```
Many thanks for the information!


"davidc" <rondos@zahav.net.il> ha scritto nel messaggio
news:4a5699b5.0301030033.338e32ea@posting.google.com...
> If You have got the original sources, You do not need to deal with
> redirections. You can just change the source and this will solve Your
> problems both for the printed reports and for the screen input.
>
> "\(www.teknosoluzioni.it\)" <tatife@tin.it> wrote in message
news:<eb1R9.49289$Q%4.1583821@news1.tin.it>...
> > Dear Binyamin, many thanks for your good idea !!
> >
> > The program is able to print, so ,if I understand right, is pheraps
possible
> > to capture the record of print and modify it to have the right result in
> > video and print ?
…[9 more quoted lines elided]…
> > "Binyamin Dissen" <postingid@dissensoftware.com> ha scritto nel
messaggio
> > news:vuc61vor3eej5fnl3al1eqpgneua9rda3g@4ax.com...
> > > On Wed, 01 Jan 2003 18:19:10 GMT "\(www.teknosoluzioni.it\)"
…[9 more quoted lines elided]…
> > > If the program is going to print you can redirect the print to disk
and
> >  then
> > > post process it (as you know which columns you want to play with).
…[12 more quoted lines elided]…
> > > :>> :>I use from about 7-8 years one cobol 45 program that run very
right,
> >  for
> >  the
> > > :>> :>work of my company;
> > > :>> :>the program was made only for me by a good boy that now is not
here.
> >
> > > :>> :>My problem is this: all the number price of the program was made
> >  without
> > > :>> :>"dot" (0000000) because with the old money not necessary
> > > :>> :>(example 100000 lire) ; now there is the ? Euro and the same
example
> >  is
> > > :>> :>51,16 Euro.
…[5 more quoted lines elided]…
> > > :>> :>I wanted a good person that can modify my program for the use of
the
> >  "
> > > :>> :>00000,00"
…[3 more quoted lines elided]…
> > > :>> Note that this will take one more print column (though with the
use of
> >  the
> > > :>> Euro you may have less digits).
> >
> > > :>> :>or , pheraps no possible, that is able to make a program that
change
> >  all
> >  my
> > > :>> :>video result money in the same result   : 1936,27  (conversion
with
> > > :>Euro) .
> >
…[3 more quoted lines elided]…
> > > :>> Italian equivalent is) you could write a program or script to
change
> >  them.
> > >
…[4 more quoted lines elided]…
> > > Director, Dissen Software, Bar & Grill - Israel
```

#### ↳ Re: Looking for cobol assistance

- **From:** "Fim W���stberg" <fim.wastberg@fimator.se>
- **Date:** 2003-01-01T14:41:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r6DQ9.3562$FF4.216325@newsb.telia.net>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it>`

```

"(www.teknosoluzioni.it)" <tatife@tin.it> skrev i meddelandet
news:qbzQ9.55855$R45.2578585@news2.tin.it...
> Dear friend,
>
> I am a person of an Italian small company.
>
> I use from about 7-8 years one cobol 45 program that run very right, for
the
> work of my company;
> the program was made only for me by a good boy that now is not here.
…[5 more quoted lines elided]…
> For this I use again the old money because my program is very important
for
> me.
>
…[3 more quoted lines elided]…
> or , pheraps no possible, that is able to make a program that change all
my
> video result money in the same result   : 1936,27  (conversion with Euro)
.
>
> This my necessity is very very  important for me.
…[10 more quoted lines elided]…
>

Do you have the source code?
What compiler?
What os, Dos, Windows?

Fim W�stberg
```

##### ↳ ↳ Re: Looking for cobol assistance

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-01T18:19:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wiGQ9.45393$Q%4.1423533@news1.tin.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <r6DQ9.3562$FF4.216325@newsb.telia.net>`

```
Dear Mr. Firm Wastberg

I thank you very much for the swift answer.

In this moment I have not the source code.
I don't know the compiler.
I use the windows, but the program work with the dos.

Can I hope for a possibility ?

  Best regards
Celestino Costa

"Fim W�stberg" <fim.wastberg@fimator.se> ha scritto nel messaggio
news:r6DQ9.3562$FF4.216325@newsb.telia.net...
>
> "(www.teknosoluzioni.it)" <tatife@tin.it> skrev i meddelandet
…[23 more quoted lines elided]…
> > video result money in the same result   : 1936,27  (conversion with
Euro)
> .
> >
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Looking for cobol assistance

- **From:** "Giancarlo Angelini" <gcan@libero.it>
- **Date:** 2003-01-01T17:18:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LpFQ9.68896$Ou4.2277483@twister2.libero.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it>`

```
Ciao,
se hai il sorgente COBOL la modifica si pu� fare. Inoltre che compilatore �
stato usato e per quale sistema operativo ?
Giancarlo

"(www.teknosoluzioni.it)" <tatife@tin.it> ha scritto nel messaggio
news:qbzQ9.55855$R45.2578585@news2.tin.it...
> Dear friend,
>
> I am a person of an Italian small company.
>
> I use from about 7-8 years one cobol 45 program that run very right, for
the
> work of my company;
> the program was made only for me by a good boy that now is not here.
…[5 more quoted lines elided]…
> For this I use again the old money because my program is very important
for
> me.
>
…[3 more quoted lines elided]…
> or , pheraps no possible, that is able to make a program that change all
my
> video result money in the same result   : 1936,27  (conversion with Euro)
.
>
> This my necessity is very very  important for me.
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Looking for cobol assistance

- **From:** "\\(www.teknosoluzioni.it\\)" <tatife@tin.it>
- **Date:** 2003-01-01T18:19:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xiGQ9.45394$Q%4.1423784@news1.tin.it>`
- **References:** `<qbzQ9.55855$R45.2578585@news2.tin.it> <LpFQ9.68896$Ou4.2277483@twister2.libero.it>`

```
Sig Gian Carlo grazie per la risposta,
al momento per� io ho solo il programma con tutti i vari file, ma la
sorgente forse ce l'ha la persona che me lo ha fatto.
Il compilatore non lo s�, quello che s� � che sentivo parlare di cobol 45 e
che il mio programma ha delle schermate bl�, parte con l'echo off tramite un
file bat ,e che � composto da 2 directory: una ove vi sono i file exe che ho
trapiantato da vari computer senza mai problemi ed un'altra ove vi sono i
dati.
Riguardo il sistema operativo, io uso il windows ma questo programma lavora
in dos.

Cosa potrei fare ?

L'ideale per me sarebbe copiare tutto in un disco, darlo a qualcuno che me
lo potesse ridare con le virgole e ritrapiantare tutto nel mio server.

Chiedo troppo ?

Grazie ancora e saluti
  Celestino Costa


"Giancarlo Angelini" <gcan@libero.it> ha scritto nel messaggio
news:LpFQ9.68896$Ou4.2277483@twister2.libero.it...
> Ciao,
> se hai il sorgente COBOL la modifica si pu� fare. Inoltre che compilatore
�
> stato usato e per quale sistema operativo ?
> Giancarlo
…[25 more quoted lines elided]…
> > video result money in the same result   : 1936,27  (conversion with
Euro)
> .
> >
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
