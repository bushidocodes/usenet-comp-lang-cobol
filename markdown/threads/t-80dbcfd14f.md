[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ex���cution d'un fichier cobol

_6 messages · 3 participants · 2001-03_

---

### ex���cution d'un fichier cobol

- **From:** "Eric Lavoie" <lavoie.eric@uqam.ca>
- **Date:** 2001-03-19T20:51:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DIyt6.1698$r%.37509@weber.videotron.net>`

```
Bonjour � tous,
j'aimerais savoir comment on fait pour ex�cuter un fichier cobol.  Le
fichier cobol est suppos� lire un fichier dat pour d�tecter des erreurs
est-ce que quelqu'un peut m'aider pour savoir comment faire.

Merci
Anik
```

#### ↳ Re: ex���cution d'un fichier cobol

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-20T16:42:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_cQt6.4815$r%.78958@weber.videotron.net>`
- **References:** `<DIyt6.1698$r%.37509@weber.videotron.net>`

```
Anik,

Peux-tu donner un peu plus de detail, du genre :

Quel compilateur utilises-tu?
Exemple, je sais que le compilateur cr�e seulement qu'un objet (.cob) et tu
dois utiliser le runtime, dans le cas de RM-Cobol, tu dois utiliser le
programme Runcobol.exe.

Si c'est un programme (.exe) peut que tu dois sp�cifier le path au long o�
se trouve le fichier .dat.

J'esp�re que �a peut t'aider,
Eric.


"Eric Lavoie" <lavoie.eric@uqam.ca> a �crit dans le message news:
DIyt6.1698$r%.37509@weber.videotron.net...
> Bonjour � tous,
> j'aimerais savoir comment on fait pour ex�cuter un fichier cobol.  Le
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Besoin d'aide

- **From:** "Nancy" <nancy.jeunehomme@skynet.be>
- **Date:** 2001-03-24T22:47:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abd16fc$0$30798$456d72a3@news.skynet.be>`
- **References:** `<DIyt6.1698$r%.37509@weber.videotron.net> <_cQt6.4815$r%.78958@weber.videotron.net>`

```
Enfin, quelqu'un qui parle fran�ais.
Je suis entrain de terminer un prog. en cobol ou j'utilise les fichiers, et
j'ai un probl�me qui me fait tourner en rond depuis quelques jours.
Quelqu'un peut-il m'aider? uniquement � r�soudre ce probl�me.
J'utilise des fichiers index�s et s�quentiel, il s'agit d'une sorte de
gestion de librairie et je n'arrive pas afficher pour un seul auteur, tous
les livres correspondant qu'il a fait. J'en affiche soit un ou tous. Ca
semble flou comme �a, mais si quelqu'un veut m'aider � r�soudre le probl�me
il est le bienvenu.

A+

Nancy

� L'exp�rience est le nom que chacun donne � ses erreurs. �
      Oscar Wilde

"Eric Gauthier" <ericg@dgcsolutions.qc.ca> a �crit dans le message news:
_cQt6.4815$r%.78958@weber.videotron.net...
> Anik,
>
…[3 more quoted lines elided]…
> Exemple, je sais que le compilateur cr�e seulement qu'un objet (.cob) et
tu
> dois utiliser le runtime, dans le cas de RM-Cobol, tu dois utiliser le
> programme Runcobol.exe.
…[16 more quoted lines elided]…
> > Anik
```

###### ↳ ↳ ↳ Re: Besoin d'aide

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-26T09:04:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<82Iv6.2608$nf4.67516@weber.videotron.net>`
- **References:** `<DIyt6.1698$r%.37509@weber.videotron.net> <_cQt6.4815$r%.78958@weber.videotron.net> <3abd16fc$0$30798$456d72a3@news.skynet.be>`

```
Salut Nancy,

C'est vrai qu'il n'y a pas grand monde qui parle fran�ais en informatique en
g�n�ral, mais bon...

Je sais pas � quoi ressemble ton code,
mais assure toi que tu initialise bien ta cl� au d�part, fait un bon START
ou bien un READ avec KEY IS ...
Dans ta boucle, ajoute un test pour v�rifier si la cl� � chang�, et si tel
est le cas sort de ta boucle avec un GO TO 110-Ton-Etiquette...

En esp�rant que �a t'aide un peu,
Eric.




"Nancy" <nancy.jeunehomme@skynet.be> a �crit dans le message news:
3abd16fc$0$30798$456d72a3@news.skynet.be...
> Enfin, quelqu'un qui parle fran�ais.
> Je suis entrain de terminer un prog. en cobol ou j'utilise les fichiers,
et
> j'ai un probl�me qui me fait tourner en rond depuis quelques jours.
> Quelqu'un peut-il m'aider? uniquement � r�soudre ce probl�me.
…[3 more quoted lines elided]…
> semble flou comme �a, mais si quelqu'un veut m'aider � r�soudre le
probl�me
> il est le bienvenu.
>
…[19 more quoted lines elided]…
> > Si c'est un programme (.exe) peut que tu dois sp�cifier le path au long
o�
> > se trouve le fichier .dat.
> >
…[8 more quoted lines elided]…
> > > fichier cobol est suppos� lire un fichier dat pour d�tecter des
erreurs
> > > est-ce que quelqu'un peut m'aider pour savoir comment faire.
> > >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Besoin d'aide

_(reply depth: 4)_

- **From:** "Nancy" <nancy.jeunehomme@skynet.be>
- **Date:** 2001-03-26T23:28:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abfb58d$0$27806$456d72a3@news.skynet.be>`
- **References:** `<DIyt6.1698$r%.37509@weber.videotron.net> <_cQt6.4815$r%.78958@weber.videotron.net> <3abd16fc$0$30798$456d72a3@news.skynet.be> <82Iv6.2608$nf4.67516@weber.videotron.net>`

```
Merci pour la r�ponse, je vais essayer de r�soudre le probl�me. Mon prog.
est presque termin� et il me reste ce probl�me que je tra�ne depuis
plusieurs jours.
Si je n'arrive pas � le r�soudre, peux tu regarder un morceau de mon code,
sans obligation de r�ponse, je dois rendre mon projet ce jeudi et un avis
ext�rieur m'interresse fortement.
```

###### ↳ ↳ ↳ Re: Besoin d'aide

_(reply depth: 5)_

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-26T17:59:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wTPv6.435$FE1.64127@weber.videotron.net>`
- **References:** `<DIyt6.1698$r%.37509@weber.videotron.net> <_cQt6.4815$r%.78958@weber.videotron.net> <3abd16fc$0$30798$456d72a3@news.skynet.be> <82Iv6.2608$nf4.67516@weber.videotron.net> <3abfb58d$0$27806$456d72a3@news.skynet.be>`

```
Si tu as trop de difficult� post le, je prendrai quelques minutes...
Eric.


"Nancy" <nancy.jeunehomme@skynet.be> a �crit dans le message news:
3abfb58d$0$27806$456d72a3@news.skynet.be...
> Merci pour la r�ponse, je vais essayer de r�soudre le probl�me. Mon prog.
> est presque termin� et il me reste ce probl�me que je tra�ne depuis
…[13 more quoted lines elided]…
> > C'est vrai qu'il n'y a pas grand monde qui parle fran�ais en
informatique
> en
> > g�n�ral, mais bon...
> >
> > Je sais pas � quoi ressemble ton code,
> > mais assure toi que tu initialise bien ta cl� au d�part, fait un bon
START
> > ou bien un READ avec KEY IS ...
> > Dans ta boucle, ajoute un test pour v�rifier si la cl� � chang�, et si
tel
> > est le cas sort de ta boucle avec un GO TO 110-Ton-Etiquette...
> >
…[9 more quoted lines elided]…
> > > Je suis entrain de terminer un prog. en cobol ou j'utilise les
fichiers,
> > et
> > > j'ai un probl�me qui me fait tourner en rond depuis quelques jours.
…[4 more quoted lines elided]…
> > > les livres correspondant qu'il a fait. J'en affiche soit un ou tous.
Ca
> > > semble flou comme �a, mais si quelqu'un veut m'aider � r�soudre le
> > probl�me
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
