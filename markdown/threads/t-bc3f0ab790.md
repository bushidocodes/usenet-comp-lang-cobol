[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL1 ==> COBOL2

_5 messages · 5 participants · 1999-10_

---

### COBOL1 ==> COBOL2

- **From:** "Christian MORANDEAU" <xcmo@club-internet.fr>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v8v5f$b6b$1@front7m.grolier.fr>`

```
Pour �crire une petite moulinette charg�e de convertir des programmes Cobol
vers Cobol2,
je recherche les diff�rences essentielles entre les 2 versions (instructions
supprim�es, remplac�es, nouvelles, ect...). Je connais les diff�rences mais
ne les ai pas toutes en t�te.
Merci de votre aide
xcmo@club-internet.fr
```

#### ↳ Re: COBOL1 ==> COBOL2

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38191383.706D459A@worldnet.att.net>`
- **References:** `<7v8v5f$b6b$1@front7m.grolier.fr>`

```
Christian MORANDEAU wrote:
> 
> Pour ï¿½crire une petite moulinette chargï¿½e de convertir des programmes Cobol
…[5 more quoted lines elided]…
> xcmo@club-internet.fr

Well, I could almost puzzle it out on my own, but babelfish says:

To write small a moulinette charged to convert programs COBOL towards
Cobol2,
I seek the essential differences between the 2 versions (removed
instructions, 
replaced, new, ect...). I know the differences but do not have them all
at the 
head.
Thank you for your assistance

from http://babelfish.altavista.digital.com/cgi-bin/translate
```

##### ↳ ↳ Re: COBOL1 ==> COBOL2

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vchge$3kq$1@news.inet.tele.dk>`
- **References:** `<7v8v5f$b6b$1@front7m.grolier.fr> <38191383.706D459A@worldnet.att.net>`

```
Try to get:

OLDBOL to NEWBOL. A Cobol Migration Tutorial for IBM Mainframe Cobols.

The fine author is William M. Klein (ISBN 1-56928-008-8)
The book was/is? published by

Micro Focus Publishing
2465 East Bayshore Road
Palo Alto,
CA 94303-3205

Regards Ib
Arnold Trembley skrev i meddelelsen <38191383.706D459A@worldnet.att.net>...
>Christian MORANDEAU wrote:
>>
>> Pour �crire une petite moulinette charg�e de convertir des programmes
Cobol
>> vers Cobol2,
>> je recherche les diff�rences essentielles entre les 2 versions
(instructions
>> supprim�es, remplac�es, nouvelles, ect...). Je connais les diff�rences
mais
>> ne les ai pas toutes en t�te.
>> Merci de votre aide
…[18 more quoted lines elided]…
>"Y2K?  Because Centuries Happen!"
```

##### ↳ ↳ Re: COBOL1 ==> COBOL2

- **From:** john_mindock@my-deja.com
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vcbnu$q8m$1@nnrp1.deja.com>`
- **References:** `<7v8v5f$b6b$1@front7m.grolier.fr> <38191383.706D459A@worldnet.att.net>`

```

> To write small a moulinette charged to convert programs COBOL towards
> Cobol2,
…[3 more quoted lines elided]…
>
Here's something that might help in the scope or implementation.
Assuming IBM mainframe COBOL '74' to VS COBOL II.  When I did this
years ago, we used an option on the compile step called MIGR on the old
compiles. This told us what statements might be different in the new
version.
No longer have access to documentation about that. I noticed a FLAGMIG
option on the newer compiler documeantation here, which appears to flag
migration issues between versions of COBOL II.

Here's one wierdo I caught in a more recent conversion effort from '74'
to COBOL II, that might slip past the MIGR.

It has to do with the TALLY associated with INSPECT TALLYING. Prior to
each execution of the INSPECT, TALLY is set back to 0 in COBOL 74. In
COBOL II it remained at its previous value. So I had to set it back to
zero in the code. This may have been installation- or compiler- related.
And it might have been the other verb similar to INSPECT on the old
compiler (I forget what that verb is).

The problem with things like the above is that they compile nicely but
run differently across the two compilers.
John


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: COBOL1 ==> COBOL2

- **From:** "Werner Zulli" <werner@log-on.com>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vhd66$fn0$1@news.netvision.net.il>`
- **References:** `<7v8v5f$b6b$1@front7m.grolier.fr> <38191383.706D459A@worldnet.att.net> <7vcbnu$q8m$1@nnrp1.deja.com>`

```
There are tools which can help you convert the source code - and they do it
quite well  for most of the code - there are some corners which are not
covered by the tools - other problems you will only hit when you actually
run the programs and variable files are the big issue we have found in
various cobol conversions we have performed. A good piece of advice would be
to carefully check the various compiler options before you go and compile
the whole set of programs (otherwise you might have to recompile several
times the programs because you haven't thought about using TRUNC(BIN) in
your compiler options for example....)

Werner Zulli
Werner@log-on.com

<john_mindock@my-deja.com> wrote in message
news:7vcbnu$q8m$1@nnrp1.deja.com...
>
> > To write small a moulinette charged to convert programs COBOL towards
…[30 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
