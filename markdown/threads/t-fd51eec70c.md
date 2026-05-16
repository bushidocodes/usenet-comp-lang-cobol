[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fonction current-date

_14 messages · 6 participants · 2005-09_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T17:25:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net>`

```
Je d�bute en COBOL et je dois mettre la date dans mon programme au format
jjmmaaaa en utilisant la fonction current-date.
Dois je mettre cette fonction dans lexique dans screen section ou proc�dure
division.
Merci d'avance

Alex
```

#### ↳ Re: fonction current-date

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-22T15:36:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dguj15$n9j$1@reader1.panix.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net>`

```
In article <n1AYe.36336$hV3.16626@nntpserver.swip.net>,
G�rard <gerard.gley@tele2.fr> wrote:
>Je d�bute en COBOL et je dois mettre la date dans mon programme au format
>jjmmaaaa en utilisant la fonction current-date.
>Dois je mettre cette fonction dans lexique dans screen section ou proc�dure
>division.
>Merci d'avance

La fonction CURRENT-DATE donne ce format: AAAAMMJJ.

<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.3.8.5.2?SHELF=&DT=20020923143836&CASE=&FS=TRUE>

DD
```

##### ↳ ↳ Re: fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T20:14:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dwCYe.36406$hV3.16684@nntpserver.swip.net>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dguj15$n9j$1@reader1.panix.com>`

```
Thank you
Alex


<docdwarf@panix.com> a �crit dans le message de news:
dguj15$n9j$1@reader1.panix.com...
> In article <n1AYe.36336$hV3.16626@nntpserver.swip.net>,
> G�rard <gerard.gley@tele2.fr> wrote:
> >Je d�bute en COBOL et je dois mettre la date dans mon programme au format
> >jjmmaaaa en utilisant la fonction current-date.
> >Dois je mettre cette fonction dans lexique dans screen section ou
proc�dure
> >division.
> >Merci d'avance
…[3 more quoted lines elided]…
>
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.3.8.5
.2?SHELF=&DT=20020923143836&CASE=&FS=TRUE>
>
> DD
>
```

##### ↳ ↳ Re: fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T20:14:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wwCYe.36407$hV3.16668@nntpserver.swip.net>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dguj15$n9j$1@reader1.panix.com>`

```
Thank you
Alex


<docdwarf@panix.com> a �crit dans le message de news:
dguj15$n9j$1@reader1.panix.com...
> In article <n1AYe.36336$hV3.16626@nntpserver.swip.net>,
> G�rard <gerard.gley@tele2.fr> wrote:
> >Je d�bute en COBOL et je dois mettre la date dans mon programme au format
> >jjmmaaaa en utilisant la fonction current-date.
> >Dois je mettre cette fonction dans lexique dans screen section ou
proc�dure
> >division.
> >Merci d'avance
…[3 more quoted lines elided]…
>
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.3.8.5
.2?SHELF=&DT=20020923143836&CASE=&FS=TRUE>
>
> DD
>
```

#### ↳ Re: fonction current-date

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-22T08:45:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgujg4$2ol5$1@si05.rsvl.unisys.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net>`

```

"G�rard" <gerard.gley@tele2.fr> wrote in message
news:n1AYe.36336$hV3.16626@nntpserver.swip.net...
> Je d�bute en COBOL et je dois mettre la date dans mon programme au format
> jjmmaaaa en utilisant la fonction current-date.
> Dois je mettre cette fonction dans lexique dans screen section ou
proc�dure
> division.
> Merci d'avance
>
> Alex

Courtesy of http://world.altavista.com/tr, I get "I begin in COBOL and I
must put the date in my program at the format jjmmaaaa by using the function
current-date.  Must I put this function in lexicon in screen section or
procedure division."

Function CURRENT-DATE, for all compilers that support it, is coded in the
PROCEDURE DIVISION and need not be mentioned elsewhere.  It needs a place to
put its returned information; the full response to this function is 21
characters but eight is sufficient.  However, the calendar portion of the
response is in the format aaaammjj; as the (admittedly remote) possibility
of getting different dates for successive executions of the function does
exist, I would suggest calling the function once to provide a sending field
in the format aaaammjj, and then using reference modification and the STRING
statement to rearrange the information into a different destination.

This program seems to work in my ANSI-85 COBOL environment:

 IDENTIFICATION DIVISION.
 ENVIRONMENT DIVISION.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 77  INDATE PIC X(8).
 77  OUTDATE PIC X(8).
 PROCEDURE DIVISION.
 MAIN-PARAGRAPH.
     MOVE FUNCTION CURRENT-DATE TO INDATE.
     DISPLAY INDATE.
     STRING INDATE (7:2), INDATE (5:2), INDATE (1:4)
          DELIMITED BY SIZE
          INTO OUTDATE.
     DISPLAY OUTDATE.
     STOP RUN.

There are other ways to accomplish this -- the function can go into a group
that has the year, month and day fields defined, and another group can have
the same field names, allowing you to use MOVE CORRESPONDING., for example.
The way I chose seemed to me clearer and more straightforward, although
there may be ways that are less processor-intensive in one or another
implementation.

To forestall potential attacks by Certain Curmudgeons in this group, I'd
suggest *next* time dig a little deeper into your class materials before
asking others to do the Hard Part of your homework ... ;-)

    -Chuck Stevens
```

##### ↳ ↳ Re: fonction current-date

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-22T16:09:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgukvu$l2f$1@reader1.panix.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com>`

```
In article <dgujg4$2ol5$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
>"G�rard" <gerard.gley@tele2.fr> wrote in message
…[13 more quoted lines elided]…
>procedure division."

[snip]

>To forestall potential attacks by Certain Curmudgeons in this group, I'd
>suggest *next* time dig a little deeper into your class materials before
>asking others to do the Hard Part of your homework ... ;-)

Courtesy of http://babelfish.altavista.com:

--begin quoted text:

Pour devancer des attaques de potentiel par Certain Curmudgeons dans ce 
groupe, je sugg�rerais * apr�s * la fouille de temps plus profond dans vos 
mat�riaux de classe avant de demander d'autres pour faire la partie dure 
de votre travail... ; -)

--end quoted text

Mais non, mon tres cher fromage du chevre... c'est rien!

DD
```

###### ↳ ↳ ↳ Re: fonction current-date

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-22T09:55:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dguni9$2r1b$1@si05.rsvl.unisys.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com> <dgukvu$l2f$1@reader1.panix.com>`

```
Well, I've heard of people being addressed as little cabbages, but not as
goat cheese ...

Alas, my French is pretty much limited to the motto from Chateau
Mouton-Rothschild, some lines from a chorus (or should I say *the* chorus)
from "La Grande-Duchesse du Gerolstein" and a few snippets from Carmen's
chorus parts, and a parentally-induced cringe every time I see (or hear)
"chaise lounge", so I'm not sure exactly what it is that's nothing!  ;-)
Some other languages I do rather better at ...

    -Chuck Stevens

<docdwarf@panix.com> wrote in message news:dgukvu$l2f$1@reader1.panix.com...
> In article <dgujg4$2ol5$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
…[3 more quoted lines elided]…
> >> Je d�bute en COBOL et je dois mettre la date dans mon programme au
format
> >> jjmmaaaa en utilisant la fonction current-date.
> >> Dois je mettre cette fonction dans lexique dans screen section ou
…[7 more quoted lines elided]…
> >must put the date in my program at the format jjmmaaaa by using the
function
> >current-date.  Must I put this function in lexicon in screen section or
> >procedure division."
…[21 more quoted lines elided]…
>
```

##### ↳ ↳ Re: fonction current-date

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-22T16:17:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sOAYe.244396$9A2.210815@edtnps89>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dgujg4$2ol5$1@si05.rsvl.unisys.com...
>
> "G�rard" <gerard.gley@tele2.fr> wrote in message
…[14 more quoted lines elided]…
> procedure division."

    As a person who speaks French, I claim this is essentially a correct 
translation, with perhaps the minor addition that "jjmmaaaa" could be 
translated to "ddmmyyyy".

    - Oliver
```

###### ↳ ↳ ↳ Re: fonction current-date

- **From:** howard.brazee@cusys.edu
- **Date:** 2005-09-22T10:52:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7o5j1df2772sb8fu0ppn6905sae3fqms1@4ax.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com> <sOAYe.244396$9A2.210815@edtnps89>`

```
On Thu, 22 Sep 2005 16:17:28 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>> Courtesy of http://world.altavista.com/tr, I get "I begin in COBOL and I
>> must put the date in my program at the format jjmmaaaa by using the 
…[6 more quoted lines elided]…
>translated to "ddmmyyyy".

I inferred that, but it reminded me of all of those movie Mexicans who
can speak English pretty well, but have never learned how to say "yes"
or "mister".
```

##### ↳ ↳ Re: fonction current-date

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-22T16:32:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70BYe.244401$9A2.3525@edtnps89>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dgujg4$2ol5$1@si05.rsvl.unisys.com...
>
> "G�rard" <gerard.gley@tele2.fr> wrote in message
…[8 more quoted lines elided]…
>> Alex

    Alex,

    je ne suis pas un "pro", ni en COBOL ni en francais, mais au cas ou vous 
ne comprenez pas l'anglais, voici mon essai pour une traduction du reponse 
de Chuck Stevens (aussi, je n'ai pas de clavier francais, allors y'a pas 
d'accent dans mon message):

> Function CURRENT-DATE, for all compilers that support it, is coded in the
> PROCEDURE DIVISION and need not be mentioned elsewhere.  It needs a place 
…[11 more quoted lines elided]…
> This program seems to work in my ANSI-85 COBOL environment:

La fonction CURREN-DATE, pour les compilateurs qui la supportent, dois etre 
ecrit dans la PROCEDURE DIVISION et n'a pas besoin d'etre mentionee ailleur. 
Elle at besoin d'une location pour metre l'information qu'elle retourne. La 
valeur retourne par cette fonction mesure 21 lettre, mais 8 est suffisant. 
Par contre, la portion calendriere de la reponse est dans la format 
"aaaammjj". Comme il y a une risque que la fonction peut retourner deux 
valeur different si on l'appelle deux fois, je suggere que vous appelez la 
fonction une fois, sauve-gardez la valleur dans le format aaaammjj, et 
utilizez "reference modification" et le commande STRING pour rearranger 
l'information dans une autre destination.

Cette programme marche dans mon environment de ANSI-85 COBOL:

> IDENTIFICATION DIVISION.
> ENVIRONMENT DIVISION.
…[12 more quoted lines elided]…
>     STOP RUN.

> There are other ways to accomplish this -- the function can go into a 
> group
…[6 more quoted lines elided]…
> implementation.

Il y a d'autre methode pour accomplir la meme choise -- l'information du 
fonction peut etre mis dans un "group" qui a l'anne, le mois et le jour 
defini dans des "fields" individuelles, et un autre group peut avoir les 
meme fields. Ainsi, vous pouvez utilize MOVE CORRESPONDING pour copier 
l'information de l'un group a l'autre. La maniere que j'ai choisi semblait 
etre plus clair, mais il peut exister d'autre implementations qui 
besoindront moin the temp sur le processeur.

> To forestall potential attacks by Certain Curmudgeons in this group, I'd
> suggest *next* time dig a little deeper into your class materials before
> asking others to do the Hard Part of your homework ... ;-)

Pour eviter le risque d'un attack par les Avares de cette groupe, je suggere 
que la prochaine fois, vous feriez un peu plus de recherches dans vos notes 
de lecture avant de demander d'autre a fair vos devoirs pour vous.

    - Oliver
```

###### ↳ ↳ ↳ Re: fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T20:21:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1GCYe.36414$hV3.16617@nntpserver.swip.net>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com> <70BYe.244401$9A2.3525@edtnps89>`

```
Thank you

Alex

"Oliver Wong" <owong@castortech.com> a �crit dans le message de news:
70BYe.244401$9A2.3525@edtnps89...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
> news:dgujg4$2ol5$1@si05.rsvl.unisys.com...
…[3 more quoted lines elided]…
> >> Je d�bute en COBOL et je dois mettre la date dans mon programme au
format
> >> jjmmaaaa en utilisant la fonction current-date.
> >> Dois je mettre cette fonction dans lexique dans screen section ou
…[8 more quoted lines elided]…
>     je ne suis pas un "pro", ni en COBOL ni en francais, mais au cas ou
vous
> ne comprenez pas l'anglais, voici mon essai pour une traduction du reponse
> de Chuck Stevens (aussi, je n'ai pas de clavier francais, allors y'a pas
> d'accent dans mon message):
>
> > Function CURRENT-DATE, for all compilers that support it, is coded in
the
> > PROCEDURE DIVISION and need not be mentioned elsewhere.  It needs a
place
> > to
> > put its returned information; the full response to this function is 21
> > characters but eight is sufficient.  However, the calendar portion of
the
> > response is in the format aaaammjj; as the (admittedly remote)
possibility
> > of getting different dates for successive executions of the function
does
> > exist, I would suggest calling the function once to provide a sending
> > field
…[6 more quoted lines elided]…
> La fonction CURREN-DATE, pour les compilateurs qui la supportent, dois
etre
> ecrit dans la PROCEDURE DIVISION et n'a pas besoin d'etre mentionee
ailleur.
> Elle at besoin d'une location pour metre l'information qu'elle retourne.
La
> valeur retourne par cette fonction mesure 21 lettre, mais 8 est suffisant.
> Par contre, la portion calendriere de la reponse est dans la format
…[46 more quoted lines elided]…
> Pour eviter le risque d'un attack par les Avares de cette groupe, je
suggere
> que la prochaine fois, vous feriez un peu plus de recherches dans vos
notes
> de lecture avant de demander d'autre a fair vos devoirs pour vous.
>
>     - Oliver
>
>
```

##### ↳ ↳ Re: fonction current-date

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-22T16:58:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CoBYe.141$1v5.8@fe03.news.easynews.com>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com>`

```
Ignoring the fact that my French isn't good enough to handle this reply.

Chuck (for additional information)
  I *believe* that an '02 conforming compiler with support for the Screen 
Section, *must* support the Intrinsic Function Current-Date in a FROM field in 
the (processor dependent) Screen Section (just as they must support in as a 
Source in the Report Section - which is NOT processor dependent).

However, unless reference modification were used, then it would not come in in 
the "correct format".

It is my impression that some, but not all, compilers that do support intrinsic 
functions AND (as an extension to the '85 Standard) Screen Section, already 
support functions there in a FROM clause (but not, of course, in a USING clause)
```

###### ↳ ↳ ↳ Re: fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T20:23:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2GCYe.36415$hV3.16617@nntpserver.swip.net>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com> <CoBYe.141$1v5.8@fe03.news.easynews.com>`

```
Thank You

Alex

"William M. Klein" <wmklein@nospam.netcom.com> a �crit dans le message de
news: CoBYe.141$1v5.8@fe03.news.easynews.com...
> Ignoring the fact that my French isn't good enough to handle this reply.
>
> Chuck (for additional information)
>   I *believe* that an '02 conforming compiler with support for the Screen
> Section, *must* support the Intrinsic Function Current-Date in a FROM
field in
> the (processor dependent) Screen Section (just as they must support in as
a
> Source in the Report Section - which is NOT processor dependent).
>
> However, unless reference modification were used, then it would not come
in in
> the "correct format".
>
> It is my impression that some, but not all, compilers that do support
intrinsic
> functions AND (as an extension to the '85 Standard) Screen Section,
already
> support functions there in a FROM clause (but not, of course, in a USING
clause)
>
> --
…[7 more quoted lines elided]…
> >> Je d�bute en COBOL et je dois mettre la date dans mon programme au
format
> >> jjmmaaaa en utilisant la fonction current-date.
> >> Dois je mettre cette fonction dans lexique dans screen section ou
…[7 more quoted lines elided]…
> > must put the date in my program at the format jjmmaaaa by using the
function
> > current-date.  Must I put this function in lexicon in screen section or
> > procedure division."
> >
> > Function CURRENT-DATE, for all compilers that support it, is coded in
the
> > PROCEDURE DIVISION and need not be mentioned elsewhere.  It needs a
place to
> > put its returned information; the full response to this function is 21
> > characters but eight is sufficient.  However, the calendar portion of
the
> > response is in the format aaaammjj; as the (admittedly remote)
possibility
> > of getting different dates for successive executions of the function
does
> > exist, I would suggest calling the function once to provide a sending
field
> > in the format aaaammjj, and then using reference modification and the
STRING
> > statement to rearrange the information into a different destination.
> >
…[18 more quoted lines elided]…
> > There are other ways to accomplish this -- the function can go into a
group
> > that has the year, month and day fields defined, and another group can
have
> > the same field names, allowing you to use MOVE CORRESPONDING., for
example.
> > The way I chose seemed to me clearer and more straightforward, although
> > there may be ways that are less processor-intensive in one or another
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: fonction current-date

- **From:** "G���rard" <gerard.gley@tele2.fr>
- **Date:** 2005-09-22T20:19:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LACYe.36410$hV3.16507@nntpserver.swip.net>`
- **References:** `<n1AYe.36336$hV3.16626@nntpserver.swip.net> <dgujg4$2ol5$1@si05.rsvl.unisys.com>`

```
IDENTIFICATION DIVISION.
 ENVIRONMENT DIVISION.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 77  INDATE PIC X(8).
 77  OUTDATE PIC X(8).
 PROCEDURE DIVISION.
 MAIN-PARAGRAPH.
     MOVE FUNCTION CURRENT-DATE TO INDATE.
     DISPLAY INDATE.
     STRING INDATE (7:2), INDATE (5:2), INDATE (1:4)
          DELIMITED BY SIZE
          INTO OUTDATE.
     DISPLAY OUTDATE.
     STOP RUN.


Alex



"Chuck Stevens" <charles.stevens@unisys.com> a �crit dans le message de
news: dgujg4$2ol5$1@si05.rsvl.unisys.com...
>
> "G�rard" <gerard.gley@tele2.fr> wrote in message
> news:n1AYe.36336$hV3.16626@nntpserver.swip.net...
> > Je d�bute en COBOL et je dois mettre la date dans mon programme au
format
> > jjmmaaaa en utilisant la fonction current-date.
> > Dois je mettre cette fonction dans lexique dans screen section ou
…[7 more quoted lines elided]…
> must put the date in my program at the format jjmmaaaa by using the
function
> current-date.  Must I put this function in lexicon in screen section or
> procedure division."
>
> Function CURRENT-DATE, for all compilers that support it, is coded in the
> PROCEDURE DIVISION and need not be mentioned elsewhere.  It needs a place
to
> put its returned information; the full response to this function is 21
> characters but eight is sufficient.  However, the calendar portion of the
> response is in the format aaaammjj; as the (admittedly remote) possibility
> of getting different dates for successive executions of the function does
> exist, I would suggest calling the function once to provide a sending
field
> in the format aaaammjj, and then using reference modification and the
STRING
> statement to rearrange the information into a different destination.
>
…[18 more quoted lines elided]…
> There are other ways to accomplish this -- the function can go into a
group
> that has the year, month and day fields defined, and another group can
have
> the same field names, allowing you to use MOVE CORRESPONDING., for
example.
> The way I chose seemed to me clearer and more straightforward, although
> there may be ways that are less processor-intensive in one or another
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
