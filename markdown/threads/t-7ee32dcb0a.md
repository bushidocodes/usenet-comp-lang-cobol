[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM COBOL with ISAM files

_91 messages · 14 participants · 2010-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-05T22:07:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89dp6aFu90U1@mid.individual.net>`

```
I am led to believe that RM ISAM files are the same format and compatible 
with, Fujitsu ISAM.

I don't have any to try out but I'd like to know if anybody is in a position 
to confirm or deny this?

Also, if anybody is using RM COBOL can you tell me what your overall 
impression of it is, and what COBOL standard was last implemented by it?

Pete.
```

#### ↳ Re: RM COBOL with ISAM files

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-05T13:30:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<992a08c0-2e5a-44a6-9e28-e3c466d9266d@k14g2000pro.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net>`

```
On Jul 5, 10:07 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I am led to believe that RM ISAM files are the same format and compatible
> with, Fujitsu ISAM.

Some Fujitsu .so (shared object==dll) files carry Ryan McFarland
copyright notices. Whether these relate to ISAM file structure is not
established but ISAM files do have the marker 'RMKF'.


> I don't have any to try out but I'd like to know if anybody is in a position
> to confirm or deny this?
…[3 more quoted lines elided]…
>

I doubt that they did anything beyond ANS'1985.
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-06T16:47:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89fqqtFf12U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <992a08c0-2e5a-44a6-9e28-e3c466d9266d@k14g2000pro.googlegroups.com>`

```
Richard wrote:
> On Jul 5, 10:07 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
>>

>
> I doubt that they did anything beyond ANS'1985.

Thanks, Richard.

Appreciated.

Pete.
```

#### ↳ Re: RM COBOL with ISAM files

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-06T23:50:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d38a3b09-d1e6-47c7-accd-3ea473ff1c14@n20g2000prc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net>`

```
On Jul 5, 10:07 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I am led to believe that RM ISAM files are the same format and compatible
> with, Fujitsu ISAM.
…[6 more quoted lines elided]…
>

Some time ago I had purchased at the local market (car boot sale) a
copy of 'Structured COBOL' and the matching 'Start-Up with RM/
COBOL-85' both by Wilson Price. They were only a couple of dollars.
The latter contained a diskette with RM/Cobol limited version.

I have installed this under dosemu and did a simple program that read
a provided sample data and wrote it as an ISAM file. This had a marker
of RMKF, same as Fujitsu.

I compiled a program under Fujitsu for Linux and it successfully read
the file written by RM/COBOL.
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-08T01:50:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89jf1bFtluU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <d38a3b09-d1e6-47c7-accd-3ea473ff1c14@n20g2000prc.googlegroups.com>`

```
Richard wrote:
> On Jul 5, 10:07 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[21 more quoted lines elided]…
> the file written by RM/COBOL.

Excellent! Looks like my informant was correct, although he said he wasn't 
sure.

Thanks for your time on this Richard.

Pete.
```

#### ↳ Re: RM COBOL with ISAM files

- **From:** manolobh <manolobh@yahoo.com.ar>
- **Date:** 2010-07-07T17:40:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1275k$lnh$1@news.eternal-september.org>`
- **In-Reply-To:** `<89dp6aFu90U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net>`

```
El 05/07/2010 12:07, Pete Dashwood escribiï¿½:
> I am led to believe that RM ISAM files are the same format and compatible
> with, Fujitsu ISAM.
…[7 more quoted lines elided]…
> Pete.
Perdï¿½n por no escribir en ingles, pero se me hace muy cuesta arriba.
Los ficheros indexados del Rm-cobol , a nivel de fichero, son 100% 
compatibles con Fujitsu Cobol. Yo los tengo funcionando y los trato 
desde "rm" y "fc" a la vez.
Lo ï¿½nico que hay que hacer desde Fujitsu Cobol es una llamada para 
convertir los numï¿½ricos con signo.
Ej.      CALL "#DEC88TOFJ" USING <nombre campo>.
Espero que os sirva la respuesta.
Un saludo desde Espaï¿½a.
-Manolo-
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-07T11:48:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org>`

```
On Jul 8, 3:40 am, manolobh <manol...@yahoo.com.ar> wrote:
> El 05/07/2010 12:07, Pete Dashwood escribió:> I am led to believe that RM ISAM files are the same format and compatible
> > with, Fujitsu ISAM.
…[18 more quoted lines elided]…
> -Manolo-

From Babel Fish:

Pardon not to write in English, but is made me very uphill. The
indexed files of the Rm-cobol, concerning file, are compatible 100%
with Fujitsu Cobol. Have I them working and them treatment from "rm"
and "fc" simultaneously. The unique thing that there is to do from
Fujitsu Cobol is a call to turn [convert] the numerical ones with
sign. Ex CALL " #DEC88TOFJ" USING <name field>. I hope that it serves
the answer to you.
A greeting from Spain.
-Manolo-
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** manolobh <manolobh@yahoo.com.ar>
- **Date:** 2010-07-08T00:40:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i12vpe$k7o$1@news.eternal-september.org>`
- **In-Reply-To:** `<19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`

```
El 07/07/2010 20:48, Richard escribiï¿½:
> On Jul 8, 3:40 am, manolobh<manol...@yahoo.com.ar>  wrote:
>> El 05/07/2010 12:07, Pete Dashwood escribiï¿½:>  I am led to believe that RM ISAM files are the same format and compatible
…[32 more quoted lines elided]…
>
Thanks for your translation.
-Manolo-
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** Louis Krupp <lkrupp_nospam@indra.com.invalid>
- **Date:** 2010-07-08T02:41:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net>`
- **In-Reply-To:** `<19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`

```
On 7/7/2010 12:48 PM, Richard wrote:
> On Jul 8, 3:40 am, manolobh<manol...@yahoo.com.ar>  wrote:
>> El 05/07/2010 12:07, Pete Dashwood escribiï¿½:>  I am led to believe that RM ISAM files are the same format and compatible
…[32 more quoted lines elided]…
>

As far as I can tell, "se me hace muy cuesta arriba" means "it seems 
very difficult" (me parece muy difï¿½cil).

Louis (Gringo in the People's Republic of Boulder, Colorado)
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-07-08T14:38:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89m67aFi5U6@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com> <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net>`

```
In article <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net>,
	Louis Krupp <lkrupp_nospam@indra.com.invalid> writes:
> On 7/7/2010 12:48 PM, Richard wrote:
>> On Jul 8, 3:40 am, manolobh<manol...@yahoo.com.ar>  wrote:
…[39 more quoted lines elided]…
> 

Anotehr example of how great computers are at natural languages.  The
only thing I use Babelfish for is a good laugh.  But then, I understood
what he said int he first place.  :-)

bill 
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2010-07-08T10:44:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i14o9e$qr1$1@news.eternal-september.org>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com> <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net> <89m67aFi5U6@mid.individual.net>`

```
"Bill Gunshannon" <billg999@cs.uofs.edu> wrote in message 
news:89m67aFi5U6@mid.individual.net...
> In article <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net>,
> Louis Krupp <lkrupp_nospam@indra.com.invalid> writes:
…[48 more quoted lines elided]…
> what he said int he first place.  :-)



I used Google translate to get more or less the same gist as posted from 
Babelfish... Of course there are wide variations, but I usually find Google 
translate a little better at avoiding major gaffes. Technical terms are 
usually brutalized but if you ignore that patch it serves up something that 
is more or less understandable.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-07-08T15:40:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89m9r4Fi5U9@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com> <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net> <89m67aFi5U6@mid.individual.net> <i14o9e$qr1$1@news.eternal-september.org>`

```
In article <i14o9e$qr1$1@news.eternal-september.org>,
	"Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com> writes:
> "Bill Gunshannon" <billg999@cs.uofs.edu> wrote in message 
> news:89m67aFi5U6@mid.individual.net...
…[58 more quoted lines elided]…
> is more or less understandable. 
 
If you want a real hoot, take some block of text (in any language you
can understand) and run it in a circle thru a half-dozen or so of the
supported languages ending in the original.  Ssshould have anybody
rolling on the floor.

bill 
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-07-09T00:26:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CizZn.4904$Zp1.1068@newsfe15.iad>`
- **In-Reply-To:** `<89m9r4Fi5U9@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com> <JvSdnVeGPfnPEqjRnZ2dnUVZ_jSdnZ2d@indra.net> <89m67aFi5U6@mid.individual.net> <i14o9e$qr1$1@news.eternal-september.org> <89m9r4Fi5U9@mid.individual.net>`

```
Bill Gunshannon wrote:
>  
> If you want a real hoot, take some block of text (in any language you
…[3 more quoted lines elided]…
 >
That sort of thing has already happened. Can't recall but say about five 
years back, in here, Oliver Wong (?) A Java programmer seeking advice on 
  COBOL, got into this language thing and said that if you took your 
approach above, what started out as 'A man and his wife' finished up as 
'A man and his bitch' !

Now a goodly ten years ago, young Jose in Portugal wrote here asking for 
help on printing from Net Express V 1.0, which was long dead. To help I 
wrote en Anglais but used BabelFish to translate into Portuguese. Sant 
Iago - he thought he had found a fellow soul who was a UN interpreter !
It then started to get a bit complicated, the technical jargon. So a 
kindly soul from Brazil jumps in to help. He made due effort and when we 
were really getting nowhere, even with our translating machines, he 
summed the translations up, "Oh My God. It isn't English and it isn't 
Portuguese !".

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-08T13:05:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i14ifb$gsn$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>`

```
In article <19e1d067-5b24-4bb8-a41c-bbc32a24a749@m37g2000prc.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Jul 8, 3:40?am, manolobh <manol...@yahoo.com.ar> wrote:
>> El 05/07/2010 12:07, Pete Dashwood escribi?:> I am led to believe that
…[33 more quoted lines elided]…
>

From http://translate.google.com:

--begin quoted text:

Sorry for not writing in English, but I was deeply pained.
The files indexed from Rm-cobol, file-level, 100%
compatible with Fujitsu Cobol. I have them running and the treatment
from "rm" and "k" at a time.
All you have to do from Fujitsu Cobol is a call for
convert numeric sign.
CALL eg "# DEC88TOFJ" USING <field name>.
I hope to serve you the answer.
Greetings from Spain.

--end quoted text

From http://www.freetranslation.com:

--begin quoted text:

Pardon by write not in English, but is done me very uphill.  The card 
indexes index-linked of the Rm-cobol, to level of card index, they are 
100% compatible with Fujitsu Cobol.  I have them functioning and the deal 
since "rm" and "fc" at the same time.  The unique thing that one must do 
from Fujitsu Cobol is a call to convert the numerical with sign.  Ej.  
CALL #DEC88TOFJ" USING <nombre campo>.  I expect that the answer serve 
you.  A greeting from Spain.

--end quoted text

Brings me back to my Kollidj Daze, aye.

DD
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-10T03:48:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89oum6FjrtU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org>`

```
manolobh wrote:
> El 05/07/2010 12:07, Pete Dashwood escribi�:
>> I am led to believe that RM ISAM files are the same format and
…[8 more quoted lines elided]…
> Perd�n por no escribir en ingles, pero se me hace muy cuesta arriba.

No es problemo. Yo vivi en Madrid durante dos anos...
> Los ficheros indexados del Rm-cobol , a nivel de fichero, son 100%
> compatibles con Fujitsu Cobol. Yo los tengo funcionando y los trato
…[3 more quoted lines elided]…
> Ej.      CALL "#DEC88TOFJ" USING <nombre campo>.

Comprendo.

Pero donde  puedo encontrar esta rutina? Cual es la diferencia en el signo?

Por que es el signo un problemo?


> Espero que os sirva la respuesta.

Ha me ayudo, si.

Muchas gracias, Manolo.

> Un saludo desde Espa�a.

... y tambien de Nueva Zelanda :-)

Pete.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** manolobh <manolobh@yahoo.com.ar>
- **Date:** 2010-07-10T10:53:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i19ce9$ab6$1@news.eternal-september.org>`
- **In-Reply-To:** `<89oum6FjrtU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <89oum6FjrtU1@mid.individual.net>`

```
El 09/07/2010 17:48, Pete Dashwood escribiï¿½:
> manolobh wrote:
>> El 05/07/2010 12:07, Pete Dashwood escribiï¿½:
…[36 more quoted lines elided]…
> Pete.
Hola Pete.
La rutina estï¿½ incluida, no hay que hacer nada especial.
Porque con signo? no lo he pensado, pero ayer precisamente tenia un 
-1,00 en un campo pic S9(9)v99 en un as/400 y me lo devolvia como -1,0=
Al ponerle el "call" ya me lo devolvia bien. Asi que "algo tiene que ver".
Un saludo.
-Manolo-
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-13T01:24:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a0jblFejgU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1275k$lnh$1@news.eternal-september.org> <89oum6FjrtU1@mid.individual.net> <i19ce9$ab6$1@news.eternal-september.org>`

```
manolobh wrote:
> El 09/07/2010 17:48, Pete Dashwood escribi�:
>> manolobh wrote:
…[43 more quoted lines elided]…
> -Manolo-

Ah, claro.

Muchas gracias, y felicitaciones por ganancia de la copa mundial :-)

Viva Espana!

Pete.
```

#### ↳ Re: RM COBOL with ISAM files

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-10T12:54:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net>`

```
The use of English and Spanish (I presume; No Habla Espanole) in this
thread has made me wonder about the compilers used in non-English
speaking countries: are they forced to use English or are there
language options which allow the use of local languages?
```

##### ↳ ↳ Non-English compilers(was: RM COBOL with ISAM files

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-10T22:33:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>`

```
"Standard conforming" (even ISO, i.e. INTERNATIONAL) COBOL compilers all use 
English keywords and syntax.  Historically, there have been anumber of 
"pre-" and "co-"processors for non-English syntax support.  The IBM "CCCA" 
productt was originally a preprocessor to allow for French language syntax. 
Similarly, IBM offered "Kanji" support for user-defined words long before 
general "DBCS" support came along.

Micro Focus is "infamous" for allow English (British) speclling for keywords 
(e.g. Background-Colour, Initialise, etc).

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com...
> The use of English and Spanish (I presume; No Habla Espanole) in this
> thread has made me wonder about the compilers used in non-English
> speaking countries: are they forced to use English or are there
> language options which allow the use of local languages?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-11T04:06:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com>`

```
On Jul 11, 4:33 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
wrote:
> "Standard conforming" (even ISO, i.e. INTERNATIONAL) COBOL compilers all use
> English keywords and syntax.  Historically, there have been anumber of
…[6 more quoted lines elided]…
> (e.g. Background-Colour, Initialise, etc).

I like the English (British) spellings; its the Americans who mis-
spell. It used to annoy me that I had to use the word "disk" to refer
to a disc and it gradually became common in GB to use the -k variant
in non-IT contexts until recently when I noticed the -c variant making
a come-back.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-14T12:29:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1kais$eg4$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com>`

```
In article <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 11, 4:33?am, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
>wrote:
…[11 more quoted lines elided]…
>spell.

I recall reading, long ago, that when folks refer to the Oldene Dayse of 
'good English' they'll focus on the 19th century or, at most, 
chronologically, Elisabethan times but *never* advocate a return to 
Chaucer.

With that in mind, Mr Maclean, which Americans were responsible for the 
mis-spellings that changed 'But me was toold, certyne, nat longe agoon is, 
that sith that crist ne wente nevere but onis to weddyng...' to something 
one might find in a proclamation over the signature of HRH William IV?

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-14T10:28:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com>`

```
On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdwarf@panix.com () wrote:

>I recall reading, long ago, that when folks refer to the Oldene Dayse of 
>'good English' they'll focus on the 19th century or, at most, 
>chronologically, Elisabethan times but *never* advocate a return to 
>Chaucer.

It is obvious that God's values have always been those which I was
taught in my formative years.   The values of society before and after
then were corrupted by Satan.

>With that in mind, Mr Maclean, which Americans were responsible for the 
>mis-spellings that changed 'But me was toold, certyne, nat longe agoon is, 
>that sith that crist ne wente nevere but onis to weddyng...' to something 
>one might find in a proclamation over the signature of HRH William IV?

Accents work that way too.    People got upset with an American with
an American accent playing Robin Hood - who did not speak with
anything like any British accent of today.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-14T11:58:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com>`

```
On Jul 14, 5:28 pm, Howard Brazee <how...@brazee.net> wrote:
> On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdw...@panix.com () wrote:
> >I recall reading, long ago, that when folks refer to the Oldene Dayse of
…[16 more quoted lines elided]…
>

Which brings us to the question of who was it who modernised the
English in the King James Bible? But that is another (reigious)
argument.
```

###### ↳ ↳ ↳ OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-15T11:45:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a70fvFmhnU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com>`

```
Alistair wrote:
> On Jul 14, 5:28 pm, Howard Brazee <how...@brazee.net> wrote:
>> On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdw...@panix.com ()
…[23 more quoted lines elided]…
> argument.

Personally, I prefer the KJV to the modern English version, but that's just 
me. There is a richness in the language which modern English is losing, but, 
given that the purpose of language is primarily communication (secondarily 
as entertainment and art), then there was a need for a new version if the 
Bible was to remain relevant to today's generation. (I don't intend to 
discuss whether it SHOULD be relevant to ANY generation... my comments are 
purely about the language.)

Anyone who has ever read the Bible in German knows that that is the language 
God speaks.

The power and might of a Supreme Being is conveyed much better, (especially 
when read aloud), by the sounds of the Teutonic. I was looking for some 
bedtime reading in a hotel room in Dusseldorf one night and found a Bible 
placed by the Gideons. I started reading Genesis in German and it made the 
hair on the back of my neck stand up in a way I have never experienced 
during private reading, or even a church service in English. :-)

As for American spellings, I have Word 2007 set to use an English 
dictionary, because I got a bit tired of being told that "organisation" was 
spelled incorrectly, or that I couldn't say "focussed". Apart from that, it 
doesn't bother me in the least and I think the American rational approach to 
English is fine. I find myself sometimes using American spellings and mixing 
them with English ones. I don't think it matters.

For me, literature is important and there is some beautiful literature (and 
poetry) written in American; the different usage in no way diminishes the 
language.

All languages that are in common use are subject to change over time. Modern 
German (Hochdeutsch) is not the same as German 400 years ago (although it is 
closer than the English of today is to the English of Shakespeare's time), 
neither is modern Spanish and French. Language has to adapt to changing 
environments and perceptions. New words have to be added and older words 
which are not so frequently used get lost. Sometimes words which nobody 
knows the meaning of any more get carried through into modern idiom through 
figures of speech ("hoist with his own petard") or the original meaning has 
changed or gets "mistranslated" into modern idiom ("the exception which 
proves the rule"). In this way old words get kept alive and it is no bad 
thing.

Sadly, for many people, English is a tedious subject which they tried to 
ignore at school when rules of Grammar were pounded into them or they were 
forced to read Shakespeare and couldn't understand much of it. I was 
watching Polanski's production of MacBeth a couple of nights ago and was 
simply entranced by it. He has edited the original play and carefully cut 
some 500 lines from it, but has interpreted Shakespeare's stage directions 
in a wonderful and original way. (At one point, the witches are required to 
"disappear into the Earth". Most productions do this with trapdoors or smoke 
and mirrors; Polanski has them open a door and walk into a Highland style 
turf cottage. Brilliant! This production was financed by Playboy back in the 
seventies so there is some nudity, which doesn't distract from the story. I 
never got to see Diana Rigg naked as Lady Macbeth, on stage at the Old Vic 
in 1972, (one of the very few regrets I allow myself :-)), but Francesca 
Annis is no less attractive and does a good job in the role with and without 
clothes on.)

There was recently a move afoot in the U.K. to withdraw Shakespeare from 
schools as not being relevant. (Fortunately, the RSC, of which I am a 
friend, mounted a fierce (but successful) campaign to increase public 
awareness and I understand many schools will be retaining it.) This is a 
perfect example of  what we are talking about. Shakespeare will ALWAYS be 
relevant as long as there are human beings, but the relevance can be clouded 
by the archaic language. I see two options:

1. Translate it into modern English (not my preference, but "West Side 
Story" did it pretty successfully...)  Still, this has apparently worked for 
the Bible and King James Versions are becoming hard to get.

2. Introduce Shakespeare to kids in a gentle way with the "easier" plays 
("Julius Caesar", "The Taming of the Shrew", "Romeo and Juliet"...)
and make sure that the language is explained in a context of the life and 
times when Shakespeare wrote it. And get them acting it. I remember playing 
in Julius Caesar when I was 11. The school I was at did it in modern dress, 
with everybody dressed as Fascists (lets face it, Ancient Rome was pretty 
much a Fascist state), and actual film of WW II to represent the battle 
scenes. We loved it; 11 year old boys are really into swashbuckling.

The fact is that language, even my beloved English, is a fluid thing.

There is no point in being "precious" about it.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-15T08:09:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hp4u36p220mn7d6bj9ob5gel262lg7qr0c@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com> <8a70fvFmhnU1@mid.individual.net>`

```
On Thu, 15 Jul 2010 11:45:02 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>As for American spellings, I have Word 2007 set to use an English 
>dictionary, because I got a bit tired of being told that "organisation" was 
…[3 more quoted lines elided]…
>them with English ones. I don't think it matters.

Spell checker technology is lacking a lot - but who's going to put in
a lot of work to make it better?

With your German familiarity - how do German spell checkers handle its
compound words?

I'd like to combine English and American dictionaries because I mix
word - I don't want "theatre" to be marked as wrong when I use it. But
then I also use foreign language words.

Features I'd like to see in a spell checker:
1.   A dialog which opens when I add a word that would allow me to
tell it part of speech, whether it is a proper noun, acceptable
plurals, tenses, etc.
2.   The ability to have phrases treated as words.  (Some spell
checkers will recognize "blu-ray", others don't.   I want "hors
d'oeuvre" to be recognized, but only as a single word).
3.  The ability to create my own "bad spelling" - if I always spell
"hors d'oeuvre" as "orderb", then remember that when trying to guess.
4.  Group dictionaries that apply to projects.
5.  Jargon dictionaries that apply to your company.
6.  Document dictionaries that apply to a novel or a directory of
stories or novels.
7.  Context dictionaries.    Maybe a news reader knows whether I am in
a movie discussion or a golf discussion to question whether I meant
"Jack Nicklaus" or "Jack Nicholson".    Maybe looks of "golfer" or
"actor" in the sentence.
8.   Updateable rules in the grammar checker (that might apply to a
particular dictionary).
```

###### ↳ ↳ ↳ Re: OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-16T12:13:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a9mh5Fh0U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com> <8a70fvFmhnU1@mid.individual.net> <hp4u36p220mn7d6bj9ob5gel262lg7qr0c@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 15 Jul 2010 11:45:02 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> compound words?

These days I don't write much German. I keep in touch with German friends by 
Skype video. I don't remember ever using a German spell checker. I'm sure 
there are people in the forum who do though. Perhaps someone from Germany 
could comment?
>
> I'd like to combine English and American dictionaries because I mix
> word - I don't want "theatre" to be marked as wrong when I use it. But
> then I also use foreign language words.

Yes, I think that would be a good idea. Have the checker check BOTH 
spellings, and allow either (but make it configurable if you didn't want 
that...)
>
> Features I'd like to see in a spell checker:
…[17 more quoted lines elided]…
> particular dictionary).

Some really good ideas there, Howard, and it would be the Mother of all 
Spell Checkers... :-)

As you say, it is unlikely anyone will invest to that extent.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 10)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-16T04:05:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ccdf0815-d2f5-41e6-b12a-c4bedc1376ab@q12g2000yqj.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com> <8a70fvFmhnU1@mid.individual.net> <hp4u36p220mn7d6bj9ob5gel262lg7qr0c@4ax.com> <8a9mh5Fh0U1@mid.individual.net>`

```
On Jul 16, 1:13 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Howard Brazee wrote:
> > On Thu, 15 Jul 2010 11:45:02 +1200, "Pete Dashwood"
…[31 more quoted lines elided]…
>

There is no reason why spell-checkers can not cater for variants in
one dictionary. Word allows you to add your variant spelling without
invalidating the original dictionary spelling. One problem: wouldn't
you end up allowing all mis-spellings too? I don't know how modern
spell-checkers work (I last checked it out in 2003) but they are
inherently limited (2003) by their algorithm. The 2003 method involved
weighting each character position and multiplying by a nominal value
for the character, summing all products and then using the sum as an
index to a 4096 table of bits where 1 = valid spelling and 0 =
invalid. It was perfectly possible to calculate a sum for one mis-
spelled word which would point to a bit which indicated (incorrectly)
that the word was valid (even though other calculations could produce
the same displacement).

The book I read didn't tell me how Word checks for grammatical errors.
```

###### ↳ ↳ ↳ Re: OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-17T02:08:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ab7e8FdggU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com> <8a70fvFmhnU1@mid.individual.net> <hp4u36p220mn7d6bj9ob5gel262lg7qr0c@4ax.com> <8a9mh5Fh0U1@mid.individual.net> <ccdf0815-d2f5-41e6-b12a-c4bedc1376ab@q12g2000yqj.googlegroups.com>`

```
Alistair wrote:
> On Jul 16, 1:13 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[47 more quoted lines elided]…
> the same displacement).

I believe that would only work for words up to 12 characters long. Anything 
bigger would be indeterminate.

It sounds similar to a technique of inverted indexing I came across in one 
of the very early database systems (system 2000).

I would be very surprised if MS Word used such a primitive and obviously 
flawed algorithm, but you never know...

>
> The book I read didn't tell me how Word checks for grammatical errors.

I doubt very much that it spell checks that way either. Ms word 2007 uses 
context sensitive spell checking to determine the correct spelling based on 
context as well as dictionary lookup. So, for example:

"He through the dog a bone."  ...would be flagged even though all the words 
are spelled correctly.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Variations in English WAS:Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-16T12:44:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1pk6g$t5p$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <8a70fvFmhnU1@mid.individual.net> <hp4u36p220mn7d6bj9ob5gel262lg7qr0c@4ax.com> <8a9mh5Fh0U1@mid.individual.net>`

```
In article <8a9mh5Fh0U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Howard Brazee wrote:

[snip]

>> I'd like to combine English and American dictionaries because I mix
>> word - I don't want "theatre" to be marked as wrong when I use it. But
>> then I also use foreign language words.

[snip]

>> Features I'd like to see in a spell checker:
>> 1.   A dialog which opens when I add a word that would allow me to
…[21 more quoted lines elided]…
>As you say, it is unlikely anyone will invest to that extent.

No need to be so dark-cloudy about it, Mr Dashwood... perhaps these 
modifications will be easier once compilers accept the DWIM (Do What I 
Mean) imperative.

('No, no, over *there* it is supposed to be 'Manhattan Class Company 
Theater Offices' and over *here* it is supposed to be 'Manhattan Repetory 
Theatre'... why can't this spell-checker Do What I Mean?')

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-14T23:53:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1lil8$13d$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com>`

```
In article <5487a4f5-7c8f-48b4-9099-c88c9130abe0@41g2000yqn.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 14, 5:28?pm, Howard Brazee <how...@brazee.net> wrote:
>> On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdw...@panix.com () wrote:

[snip]

>> >With that in mind, Mr Maclean, which Americans were responsible for the
>> >mis-spellings that changed 'But me was toold, certyne, nat longe agoon is,
…[10 more quoted lines elided]…
>argument.

One which might be addressed, of course, after dealing with what need 
anyone felt to modernise Wycliffe.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-15T04:13:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com>`

```
On Jul 14, 5:28 pm, Howard Brazee <how...@brazee.net> wrote:
> On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdw...@panix.com () wrote:

>
> Accents work that way too.    People got upset with an American with
> an American accent playing Robin Hood - who did not speak with
> anything like any British accent of today.
>

In the days of the mythical Robin Hood (for which there were several
contenders) no-one in England spoke with an accent even remotely like
any modern British accent. So Kevin Costner's American accent would
have been as valid as any other accent (except French).
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-15T08:17:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hl5u36djg8tng4t6sd20bj8bhott5ra6m5@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com>`

```
On Thu, 15 Jul 2010 04:13:15 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Accents work that way too. ï¿½ ï¿½People got upset with an American with
>> an American accent playing Robin Hood - who did not speak with
…[6 more quoted lines elided]…
>have been as valid as any other accent (except French).

But expectations are funny despite the facts.    Viewers accept that
in _Sparticus_, the Roman leaders spoke with English accents, and the
slaves with American accents.

Some people were upset in _Hunt for Red October_ that the Russians
speaking Russian (in English) had American accents, but Sean Connery
had a Scottish accent.   When he was playing a Lithuanian speaking
Russian.   His character's background was sort of like a Scotsman in
the British Navy.  What could be more appropriate?   
```

###### ↳ ↳ ↳ OT: Odd movie accents

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-16T03:54:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0e924ec-bde9-4623-b4dc-b566feeb6aad@u26g2000yqu.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <hl5u36djg8tng4t6sd20bj8bhott5ra6m5@4ax.com>`

```
On Jul 15, 3:17 pm, Howard Brazee <how...@brazee.net> wrote:
> On Thu, 15 Jul 2010 04:13:15 -0700 (PDT), Alistair
>
…[12 more quoted lines elided]…
> slaves with American accents.

Sounds like a thinly veiled referback to the American Revolution.
```

###### ↳ ↳ ↳ Re: OT: Odd movie accents

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-19T08:15:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hen8465d3m1s0mcgstdnj2qem0opndheka@4ax.com>`
- **References:** `<26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <hl5u36djg8tng4t6sd20bj8bhott5ra6m5@4ax.com> <e0e924ec-bde9-4623-b4dc-b566feeb6aad@u26g2000yqu.googlegroups.com>`

```
On Fri, 16 Jul 2010 03:54:38 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> But expectations are funny despite the facts. ï¿½ ï¿½Viewers accept that
>> in _Sparticus_, the Roman leaders spoke with English accents, and the
>> slaves with American accents.
>
>Sounds like a thinly veiled referback to the American Revolution.

It could be.   I was thinking it is a class thing.   All of the
English actors spoke the Queen's English, certainly there were no
Cockneys playing Roman elites.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-07-15T16:12:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a8qc2Flb1U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com>`

```
In article <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com>,
	Alistair <alistair@ld50macca.demon.co.uk> writes:
> On Jul 14, 5:28ï¿½pm, Howard Brazee <how...@brazee.net> wrote:
>> On Wed, 14 Jul 2010 12:29:16 +0000 (UTC), docdw...@panix.com () wrote:
…[8 more quoted lines elided]…
> have been as valid as any other accent (except French).

What do you mean mythical?  Didn't you watch the episode of "Ghost Hunters"
where they contacted Robin Hood's spirit?

bill
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-16T03:56:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com> <c97c2970-346f-4845-9f66-64e253ba598e@y4g2000yqy.googlegroups.com> <i1kais$eg4$1@reader1.panix.com> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net>`

```
On Jul 15, 5:12 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <6a5ca5d9-bb4b-436c-93a6-a5e2a681c...@d37g2000yqm.googlegroups.com>,
>         Alistair <alist...@ld50macca.demon.co.uk> writes:
…[15 more quoted lines elided]…
>

No, I didn't. And as Ghosts (and life after death, generally)
contravene the laws of thermodynamics, I can have no truck with them.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-16T12:49:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1pkgj$t5p$3@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com>`

```
In article <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>No, I didn't. And as Ghosts (and life after death, generally)
>contravene the laws of thermodynamics, I can have no truck with them.

Against your religion, I see... but if the laws of thermodynamics were 
strictly held to, in all spacetimes and at all timespaces, wouldn't life 
as we know it - a violation (temporary, but a violation nonetheless) of 
bits and pieces of Thermodynamic law - never have occurred?

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 10)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-19T08:12:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com>`

```
On Jul 16, 1:49 pm, docdw...@panix.com () wrote:
> In article <62c55b5c-d6dc-4089-b1fa-6ae4b3b74...@k39g2000yqd.googlegroups.com>,
>
…[12 more quoted lines elided]…
> DD

I'm dreading seeing the explanation as to how life is a violation of
the laws of thermodynamics but I have to ask....how so?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-19T15:32:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i21r6j$i7u$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com>`

```
In article <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 16, 1:49?pm, docdw...@panix.com () wrote:
>> In article
…[15 more quoted lines elided]…
>the laws of thermodynamics but I have to ask....how so?

What follows, Mr Maclean, might not be 'the explanation' but more of 'an 
explanation'.

Life, by definition, is an organising of particles; consider embryogenesis 
from haploid gametes to diploid zygote to morula to blastocyst (two 
primary cell cell types) and so on, through the Carnegie stages.  Each 
change is towards greater order, greater differentiation and growth, quite 
the opposite of entropy (a tendency towards disorder).

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-19T12:24:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <i21r6j$i7u$1@reader1.panix.com>`

```
On Jul 19, 4:32 pm, docdw...@panix.com () wrote:
> In article <33db1847-821e-4370-b330-1a032bc73...@k19g2000yqc.googlegroups.com>,
>
…[33 more quoted lines elided]…
> DD- Hide quoted text -

My understanding of the ins and outs of Entropy is limited but I
understand that the application of that law to the non-chaotic
ordering of life-forms is in error as Entropy applies to limited
closed systems and not to the Universe as a whole (or any
insignificant small blue-green planet on the edge of a spiral arm of a
minor galaxy in the middle of nowhere). Regrettably, although I have
seen the explanation for this (Scientific American I think) I am
unable to repeat the proof. Sorry.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-20T14:26:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i24bna$s5m$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <i21r6j$i7u$1@reader1.panix.com> <a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com>`

```
In article <a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 19, 4:32?pm, docdw...@panix.com () wrote:
>> In article
…[36 more quoted lines elided]…
>minor galaxy in the middle of nowhere).

Note that the example given above, Mr Maclean, deals off with two haploid 
gametes and a working uterus; this might appear to be more of a 'limited 
closed system' than 'the Universe as a whole (etc)'.

>Regrettably, although I have
>seen the explanation for this (Scientific American I think) I am
>unable to repeat the proof. Sorry.

No need to apologise, it can be considered as discarded due to lack of 
substantiation.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 14)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-21T03:45:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <i21r6j$i7u$1@reader1.panix.com> <a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com> <i24bna$s5m$1@reader1.panix.com>`

```
On Jul 20, 3:26 pm, docdw...@panix.com () wrote:
> In article <a49ec6f8-084e-44e3-8179-26d0daa1c...@e5g2000yqn.googlegroups.com>,
> >> What follows, Mr Maclean, might not be 'the explanation' but more of 'an
…[18 more quoted lines elided]…
>

Hardly limited as those items garner nutrition from a wider
environment.


> >Regrettably, although I have
> >seen the explanation for this (Scientific American I think) I am
…[4 more quoted lines elided]…
>

But it doesn't stop you from researching the document.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-21T12:19:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i26ok4$n86$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com> <i24bna$s5m$1@reader1.panix.com> <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com>`

```
In article <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 20, 3:26?pm, docdw...@panix.com () wrote:
>> In article <a49ec6f8-084e-44e3-8179-26d0daa1c...@e5g2000yqn.googlegroups.com>,
…[22 more quoted lines elided]…
>environment.

Mr Dashwood, the description was not one of absolute limitation but of 
quality-of-limitedness (perhaps an inverse of 'richness of infity'); I 
believe that possibility might have been covered by the description above 
of 'a working uterus... might appear to be more of a 'limited closed 
system' than 'the Universe as a whole (etc).'

If you're trying to slip in a nigh-Buddhist 'all is connected' viewpoint 
then perhaps the well-gazed-at Navel Reserves might be called out.

>> >Regrettably, although I have
>> >seen the explanation for this (Scientific American I think) I am
…[6 more quoted lines elided]…
>But it doesn't stop you from researching the document.

'The document'?  What 'the document' (note the definite article) is 
'Scientific American I think (sic)'?

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-21T12:20:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i26on9$n86$2@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i24bna$s5m$1@reader1.panix.com> <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com> <i26ok4$n86$1@reader1.panix.com>`

```

Correction - in my response I erroneously addressed Mr Maclean as Mr 
Dashwood; this is mine own error and I offer apologies to all and sundry 
who might feel them necessary, appropriate or worthy of 
saving-and-trading.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-22T13:11:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8apk63FvqvU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i24bna$s5m$1@reader1.panix.com> <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com> <i26ok4$n86$1@reader1.panix.com> <i26on9$n86$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> Correction - in my response I erroneously addressed Mr Maclean as Mr
> Dashwood; this is mine own error and I offer apologies to all and
…[3 more quoted lines elided]…
> DD

Well your half-arsed apology is half-arsed accepted... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-22T12:08:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i29cb5$9ac$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i26ok4$n86$1@reader1.panix.com> <i26on9$n86$2@reader1.panix.com> <8apk63FvqvU1@mid.individual.net>`

```
In article <8apk63FvqvU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> Correction - in my response I erroneously addressed Mr Maclean as Mr
…[4 more quoted lines elided]…
>Well your half-arsed apology is half-arsed accepted... :-)

Folks *do* speak such funny languages in The Antipodes... I might have 
described my apology as half-slow, not half-fast.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-22T13:10:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8apk4kFvj4U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <a49ec6f8-084e-44e3-8179-26d0daa1c0a6@e5g2000yqn.googlegroups.com> <i24bna$s5m$1@reader1.panix.com> <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com> <i26ok4$n86$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <4fb21569-66ed-457e-990d-1a24662782b4@x21g2000yqa.googlegroups.com>,
…[27 more quoted lines elided]…
>> environment.

>
> Mr Dashwood, the description was not one of absolute limitation but of
…[9 more quoted lines elided]…
>
Hey! Not guilty!

You are responding to the wrong poster. I had no problem with your previous 
response.

Pete.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-19T09:47:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com>`

```
On Mon, 19 Jul 2010 08:12:07 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Against your religion, I see... but if the laws of thermodynamics were
>> strictly held to, in all spacetimes and at all timespaces, wouldn't life
…[6 more quoted lines elided]…
>the laws of thermodynamics but I have to ask....how so?

There are some Creationists who use the law of thermodynamics to show
that things cannot become more ordered without a deity making them so.

It couldn't be that our good doctor is playing with us here, could it?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-19T16:24:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i21u8h$muv$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>`

```
In article <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 19 Jul 2010 08:12:07 -0700 (PDT), Alistair
><alistair@ld50macca.demon.co.uk> wrote:
…[12 more quoted lines elided]…
>It couldn't be that our good doctor is playing with us here, could it?

No doctor, good or otherwise, I... jes' ol' Doc and I am full of play and 
joyfulnesses!  I believe this deity-to-get-the-ball-rolling was addressed 
by Pierre-Simon Laplace's 'Je n'avais pas besoin de cette hypothesis' (or 
something like that, as dimly recalled from Kollidj Daze)

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-19T10:48:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com>`

```
On Mon, 19 Jul 2010 16:24:49 +0000 (UTC), docdwarf@panix.com () wrote:

>>It couldn't be that our good doctor is playing with us here, could it?
>
…[3 more quoted lines elided]…
>something like that, as dimly recalled from Kollidj Daze)

Maybe you're a doctor the same way the protagonist of Dr. Who is.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-19T17:24:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i221ov$h57$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com>`

```
In article <rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 19 Jul 2010 16:24:49 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>Maybe you're a doctor the same way the protagonist of Dr. Who is.

I had to research that one... but no, I have never been proclaimed thus 
by a crew of scriptwriters.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 15)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-19T12:26:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com> <i221ov$h57$1@reader1.panix.com>`

```
On Jul 19, 6:24 pm, docdw...@panix.com () wrote:
> In article <rd09465s2i337t38ur6n479ordjc0ov...@4ax.com>,
> Howard Brazee  <how...@brazee.net> wrote:
…[15 more quoted lines elided]…
> DD

Whoa! You had to research the great Dr. Who?! Where have you been the
last 50 years?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-20T14:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i24bpm$s5m$2@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com> <i221ov$h57$1@reader1.panix.com> <58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com>`

```
In article <58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 19, 6:24?pm, docdw...@panix.com () wrote:
>> In article <rd09465s2i337t38ur6n479ordjc0ov...@4ax.com>,
>> Howard Brazee ?<how...@brazee.net> wrote:

[snip]

>> >Maybe you're a doctor the same way the protagonist of Dr. Who is.
>>
…[4 more quoted lines elided]…
>last 50 years?

Among other things... watching different television program(me)s, it 
seems.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 17)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-21T03:47:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2b3a0d9f-6230-425a-9feb-4ed666af2534@w30g2000yqw.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <rd09465s2i337t38ur6n479ordjc0ovi8u@4ax.com> <i221ov$h57$1@reader1.panix.com> <58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com> <i24bpm$s5m$2@reader1.panix.com>`

```
On Jul 20, 3:28 pm, docdw...@panix.com () wrote:
> In article <58814b9e-b2ed-48e9-8a91-b83db3ca1...@k19g2000yqc.googlegroups.com>,
>
…[18 more quoted lines elided]…
> DD

Don't forget the films. The last one bombed (although it was good) but
you must have heard of the Daleks?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-21T12:23:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i26oro$n86$3@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com> <i24bpm$s5m$2@reader1.panix.com> <2b3a0d9f-6230-425a-9feb-4ed666af2534@w30g2000yqw.googlegroups.com>`

```
In article <2b3a0d9f-6230-425a-9feb-4ed666af2534@w30g2000yqw.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Jul 20, 3:28?pm, docdw...@panix.com () wrote:
>> In article
…[21 more quoted lines elided]…
>you must have heard of the Daleks?

I read of the during the research I did for the preceding posting, Mr 
Maclean, and beyond that have no exposure.  I believe I've mentioned 
previously that the talking-pictures I tend to watch are in 
black-and-white and filled with dead people... oh, look, there's Eddie 
Cantor!

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-21T08:38:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2a1e461v1fpn0kpq5p23bqd7bdtls5n2ju@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <58814b9e-b2ed-48e9-8a91-b83db3ca1cd6@k19g2000yqc.googlegroups.com> <i24bpm$s5m$2@reader1.panix.com> <2b3a0d9f-6230-425a-9feb-4ed666af2534@w30g2000yqw.googlegroups.com> <i26oro$n86$3@reader1.panix.com>`

```
On Wed, 21 Jul 2010 12:23:20 +0000 (UTC), docdwarf@panix.com () wrote:

>I read of the during the research I did for the preceding posting, Mr 
>Maclean, and beyond that have no exposure.  I believe I've mentioned 
>previously that the talking-pictures I tend to watch are in 
>black-and-white and filled with dead people... oh, look, there's Eddie 
>Cantor!

My son has his family big on Dr. Who, which is how I know about it.
When I was a teen, I knew all of the TV shows of the three networks,
but was in college by the time my local stations had that show, and I
have only seen scenes of the show while visiting others.

My DvD & Blu-ray library is maybe 1/3 B&W, with only a dozen or so
silent movies.    I'm not sure whether I prefer movies to TV these
days because of the content - or because of some kind of control
issue.   Sure I know I can buy stuff to let me watch the shows when I
want - but I don't *want* to feel a need to see this week's episode.
At any rate, I am very ignorant about popular culture.
```

###### ↳ ↳ ↳ OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-20T11:33:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ak5lqF541U1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>,
> Howard Brazee  <howard@brazee.net> wrote:
…[25 more quoted lines elided]…
> DD

I am currently reading the Dalia Lama's latest book: "Becoming Enlightened"

This is a kind of intricate Buddhist joke because if you are "becoming" you 
cannot be "enlightened"... never mind.

The pertinent thing here is that he describes the main difference between 
Buddhism and other religions as the fact that Buddhism does not postulate a 
supreme being who created the universe and has control over it. Instead the 
DL's view is that everything is interconnected and things are the way they 
are because of everything else. Very much like the Chaos Theory idea that a 
butterfly flapping its wings in the Amazon can cause a typhoon in the South 
China Sea.

The Philosophy he expounds is much more closely linked with Quantum 
Mechanics than it is with Newton.

As I was due to write my column for Bravado  issue 20, I decided to make 
this the theme for it and, although it hasn't been published yet, readers of 
this forum can access it exclusively for a limited period from: 
http://bravado.co.nz/sp20.pdf

It is intended to be light and amusing to a non-scientific audience, but 
there is some serious stuff in there as well.

It mentions Thermodynamics and entropy briefly in passing.

I'm perfectly happy to discuss/clarify points arising from it here... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 14)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-20T03:08:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b40d539-519e-472d-b404-74e45500cff3@s9g2000yqd.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net>`

```
On Jul 20, 12:33 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> As I was due to write my column for Bravado  issue 20, I decided to make
> this the theme for it and, although it hasn't been published yet, readers of
> this forum can access it exclusively for a limited period from:http://bravado.co.nz/sp20.pdf
>

Reddit.

That butterfly (Chaoticus panglobus) seems to get around a bit. Last
year it was in New York and now the Amazon. Sci Am covered the
butterfly effect recently and concluded that it would not start a
hurricane by flapping its wings as the effect produced was too small
to contribute significantly to the starting conditions prevailing at
the time. And yes I do know that small differences in chaotic systems
starting parameters can have major effects (see weather forecasting)
but there are limits to the minimum size needed to effect significant
differences.

Buddhism seems to be an easy religion/philosophy to fall in to the
trap of believing (during my agnostic phase I could have easily become
a Buddhist but four miniature white elephants saved me from that
mistake). If everything were interconnected with everything else then
everything would be affected by every event. Instantaneously? At what
speed and by what mechanism would all events be communicated to
everything? Really, all he says is that for every event there is a
cause (although not necessarily in the order of cause > event) and
every action has a consequence. Which leads to not treading on ants
and wearing face masks to avoid accidentally swallowing flies.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-21T19:41:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8anmm3FkamU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net> <6b40d539-519e-472d-b404-74e45500cff3@s9g2000yqd.googlegroups.com>`

```
Alistair wrote:
> On Jul 20, 12:33 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[26 more quoted lines elided]…
> everything?

A very good question. Check out the Einstein Podalksy Rosen effect (EPR), 
and the possibility of at least 7 other dimensions which may have been 
created at the moment of the Big Bang in the same way that the four we 
recognise were, but which, instead of expanding, actually collapsed to the 
quantum level. That's just 2 ways such communication COULD be possible.

You also need to consider what you mean by "communicated" to everything. If 
everything is just one great whole, then "separation" is an apparency and 
"everything" IS "everything... Much food for thought here.

I don't think believing the teachings of Buddhism is a "trap" (if I weren't 
an Atheist and HAD to subscribe to SOME religion, I'd probably be a 
Buddhist, but that isn't the case,and there are elements of the DL's belief 
system which I don't go along with (Reincarnation would be just one of 
those...))

>Really, all he says is that for every event there is a
> cause (although not necessarily in the order of cause > event) and
> every action has a consequence. Which leads to not treading on ants
> and wearing face masks to avoid accidentally swallowing flies.

I believe that is an oversimplification, although he certainly does say 
that.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-20T14:41:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i24cja$eue$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net>`

```
In article <8ak5lqF541U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> No doctor, good or otherwise, I... jes' ol' Doc and I am full of play
>> and joyfulnesses!  I believe this deity-to-get-the-ball-rolling was
…[7 more quoted lines elided]…
>cannot be "enlightened"... never mind.

I'd noticed, long ago, that the Zen I read had the same kind of wariness 
about a process-continuing-to-completion found in Zeno's paradox; 'coming 
to be' is something calculus handles rather well but geometry (as the 
Ancient Greeks knew it) falls a wee bit shy.

This may be a reason for so much of enlightment being described as more 
metamorphic and less evolutionary... '... and the Master whacked the 
Student a good, sound one 'round the noggin with a shillelagh and caused 
him to fall off the porch into a mud-puddle; at that moment the Student 
became enlightened' or something-like-that is, as I recall, 
more-than-passingly common.

(the koan 'Where are you standing when you jump off a bridge?' comes to 
mind)

DD
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-21T19:46:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8anmu8FlsjU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net> <i24cja$eue$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <8ak5lqF541U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[31 more quoted lines elided]…
> DD

I guess it's pretty difficult to describe the indescribable.

Over centuries, koans have been one mechanism to kind of approach it from 
the side and maybe provide a glimpse...

Certainly, all of the literature I have read (and it has been extensive) 
indicates that enlightenment is a sudden and dramatic process, as you have 
described.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-21T12:59:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i26r0c$8g$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <8ak5lqF541U1@mid.individual.net> <i24cja$eue$1@reader1.panix.com> <8anmu8FlsjU1@mid.individual.net>`

```
In article <8anmu8FlsjU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> This may be a reason for so much of enlightment being described as
>> more metamorphic and less evolutionary... '... and the Master whacked
…[8 more quoted lines elided]…
>I guess it's pretty difficult to describe the indescribable.

Not only 'pretty difficult', Mr Dashwood... were one to succeed it would 
destroy that aspect ('indescribability') of the phenomenon.  Lao Tzu put 
it as 'The Tao which can be spoken of is not the true/eternal/ineffable 
(translations vary on this) Tao.'

DD
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 14)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-07-20T13:50:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8ob46df8ijj4mah95gutlvjjecfi57i56@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net>`

```
On Tue, 20 Jul 2010 11:33:11 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>docdwarf@panix.com wrote:
>> In article <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>,
…[56 more quoted lines elided]…
>Pete.

Just to clarify, and I know this because my wife is a Buddhist,
Buddhism is a philosophy, not a religion.  If you were to go to a
country like Thailand where 90% of the people are Buddhist, you'd find
they also subscribe to Hinduism because Hinduism has "gods".  In
addition there are a lot of Christians that practice Buddhism.  The
two marry together very nicely.

Regards,
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-20T13:46:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n2vb46p39ob8fl8ivajgteg7vu1pm5ijjq@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net> <p8ob46df8ijj4mah95gutlvjjecfi57i56@4ax.com>`

```
On Tue, 20 Jul 2010 13:50:12 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>Just to clarify, and I know this because my wife is a Buddhist,
>Buddhism is a philosophy, not a religion.  If you were to go to a
…[3 more quoted lines elided]…
>two marry together very nicely.

However the people who use Thermodynamics to "disprove" evolution tend
to be the same people who claim atheism as a religion, and would
disbelieve claims that Buddhism is.    Nobody could possibly not be a
theist in his heart.   

They aren't threatened by Hinduism so aren't interested in discussing
whether Brahma created the world - but they might be threatened by
Buddhism if their version of Christians might be interested in it.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-21T20:24:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8anp6mF34uU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net> <p8ob46df8ijj4mah95gutlvjjecfi57i56@4ax.com> <n2vb46p39ob8fl8ivajgteg7vu1pm5ijjq@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 20 Jul 2010 13:50:12 -0400, SkippyPB
> <swiegand@Nospam.neo.rr.com> wrote:
…[11 more quoted lines elided]…
> theist in his heart.

Sorry, Howard, I beg to differ.  I know my heart, and I am not a theist 
(with a small or capital "t").

In my view, God was invented by Man in answer to the needs of Man. There 
never was, never has been, and never will be a Supreme Being who we are 
answerable to, or who created us. Certainly there are things ouside the 
control of Man, but that doesn't mean they are in the domain of God. It is 
the dogmatic, unquestioning, teaching of Religion that has held us back for 
thousands of years and prevented us from growing to the point where we no 
longer need superstition to explain our world.  And it's time we started 
taking responsibility for ourselves instead of blaming God.  I have been in 
situations where my death was imminent; I never felt moved to call on God 
for help. Many people do, and when they survive, they believe it was due to 
Divine Intervention and thenceforth resolve to lead better lives. Not a bad 
result, but God had nothing to do with it. I believe the Universe is a crap 
shoot with random events occurring because they must, not because God 
requires it. It is we who decide what is "good" and what is "bad"; the 
universe is amoral and doesn't care. It is a star factory, going about its 
business of creating and destroying stars without the slightest concern for 
an intelligent life form which happens to have evolved on an insignificant 
planet near the edge of a minor galaxy.

And when the time comes for me to leave this world, I shall do so in the 
certain knowledge I'm not going to a better place, or a worse place, or 
anywhere. I have no problem whatsoever with that; in fact, it strengthens my 
resolve to ensure that my time here is well spent and enjoyable. (And it is 
good to try and leave it a better place than you found it...)

I also realize that all of the above is personal and should not be 
evangelized or proseltyzed to others. Let them work out their own answers 
exactly as I did. Personal belief is exactly that, personal.

I respect the beliefs of others (as long as they don't require me to live in 
accordance with their religious beliefs and as long as they don't kill or 
torture people who are not of their faith), and realize it will be a few 
thousand years yet (if we last that long) before all humans will have enough 
confidence and understanding to be able to walk unaided.

I have lived my life up to the present final chapters of it without needing 
religion as a crutch. So I must vigorously contest your statement. There is 
at least ONE person who "could possibly not be a theist in his heart".

In fact, is DEFINITELY not a theist in his heart.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Entropy and Creationism WAS: Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-21T08:42:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dm1e46psqu4cqm3jro0u98cf1i3sf6posd@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <i21u8h$muv$1@reader1.panix.com> <8ak5lqF541U1@mid.individual.net> <p8ob46df8ijj4mah95gutlvjjecfi57i56@4ax.com> <n2vb46p39ob8fl8ivajgteg7vu1pm5ijjq@4ax.com> <8anp6mF34uU1@mid.individual.net>`

```
On Wed, 21 Jul 2010 20:24:52 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> However the people who use Thermodynamics to "disprove" evolution tend
>> to be the same people who claim atheism as a religion, and would
…[4 more quoted lines elided]…
>(with a small or capital "t").

Don't be sorry.   I wasn't clear in my communication that I was
speaking for them, not myself.   We are in agreement.

And if I did believe in Heaven and not in Hell, then I'd do what I
could to make sure I died instead of being sent to heaven.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-19T12:31:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a93ed8b-749b-4b52-b03e-9803520c672d@z10g2000yqb.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com>`

```
On Jul 19, 4:47 pm, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 19 Jul 2010 08:12:07 -0700 (PDT), Alistair
>
…[13 more quoted lines elided]…
>

Would those creationists be the same ones who quote science to support
their case when it suits them and yet they deny other sciences when it
doesn't suit them?

I saw a superb documentary about jellyfish yesterday. A scientist
described how he watched jellyfish hunting fish. Something that they
could not do as they clearly don't have eyes. Subsequent dissection
found the eyes and a controlling brain. Amazing how the deity created
eyes in jellyfish in order to satisfy the observation and musings of a
humble scientist.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-20T08:53:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r2eb46107l3kielttecrhh8vk2rfmno9mq@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net> <62c55b5c-d6dc-4089-b1fa-6ae4b3b74bad@k39g2000yqd.googlegroups.com> <i1pkgj$t5p$3@reader1.panix.com> <33db1847-821e-4370-b330-1a032bc73d83@k19g2000yqc.googlegroups.com> <7ps8469d7el4b8mjrokgjeslrrnebtbgtp@4ax.com> <5a93ed8b-749b-4b52-b03e-9803520c672d@z10g2000yqb.googlegroups.com>`

```
On Mon, 19 Jul 2010 12:31:29 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>Would those creationists be the same ones who quote science to support
>their case when it suits them and yet they deny other sciences when it
>doesn't suit them?

Or who pick and choose which part of the Old Testament are still valid
(by comparing the scripture to what they already believe)?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-16T12:47:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1pkc4$t5p$2@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <d6pr369u7imgijql1u7iqifhheai98scqu@4ax.com> <6a5ca5d9-bb4b-436c-93a6-a5e2a681cd66@d37g2000yqm.googlegroups.com> <8a8qc2Flb1U1@mid.individual.net>`

```
In article <8a8qc2Flb1U1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>What do you mean mythical?  Didn't you watch the episode of "Ghost Hunters"
>where they contacted Robin Hood's spirit?

I think I've heard of that... all the participants wound up without their 
rings, watches, gold-rimmed spectacles gone and their wallets emptied.

DD
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-12T08:10:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h8m36djhr3t4hqmrfs164gr2osqs0tvs4@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <rYa_n.291024$vX7.170382@en-nntp-11.dc1.easynews.com>`

```
What is foo bar in Greek?
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** Fritz Wuehler <fritz@spamexpire-201007.rodent.frell.theremailer.net>
- **Date:** 2010-07-13T02:31:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aca13835f9e9673d4f959b3ab889a7b7@msgid.frell.theremailer.net>`
- **References:** `<9h8m36djhr3t4hqmrfs164gr2osqs0tvs4@4ax.com>`

```
> What is foo bar in Greek?

You need an APL keyboard for that.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-13T03:19:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8cc1c61-236d-45bb-94b8-df1b19df1035@j13g2000yqj.googlegroups.com>`
- **References:** `<9h8m36djhr3t4hqmrfs164gr2osqs0tvs4@4ax.com> <aca13835f9e9673d4f959b3ab889a7b7@msgid.frell.theremailer.net>`

```
On Jul 13, 1:31 am, Fritz Wuehler
<fr...@spamexpire-201007.rodent.frell.theremailer.net> wrote:
> > What is foo bar in Greek?
>
> You need an APL keyboard for that.

According to Google, Foo Bar in Greek is:



Foo Bar.
```

###### ↳ ↳ ↳ Re: Non-English compilers(was: RM COBOL with ISAM files

_(reply depth: 6)_

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-07-13T11:39:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sx1%n.8830$OU6.6159@newsfe20.iad>`
- **In-Reply-To:** `<c8cc1c61-236d-45bb-94b8-df1b19df1035@j13g2000yqj.googlegroups.com>`
- **References:** `<9h8m36djhr3t4hqmrfs164gr2osqs0tvs4@4ax.com> <aca13835f9e9673d4f959b3ab889a7b7@msgid.frell.theremailer.net> <c8cc1c61-236d-45bb-94b8-df1b19df1035@j13g2000yqj.googlegroups.com>`

```
Alistair wrote:
> On Jul 13, 1:31 am, Fritz Wuehler
> <fr...@spamexpire-201007.rodent.frell.theremailer.net> wrote:
…[10 more quoted lines elided]…
> Foo Bar.

Not according to Babelfish - φραγμός foo. Although one other I tried, 
gave up and came back with foo bar. Interesting that the Thunderbird 
spellchecker took the Babelfish translation and came up with in excess 
of 50 Greek character set options.

Of course I got warned about trying to send mixed text - so you may need 
to go to Babelfish to check what I got.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-07-11T11:21:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89tnqfFcrU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>`

```
In article <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>,
	Alistair <alistair@ld50macca.demon.co.uk> writes:
> The use of English and Spanish (I presume; No Habla Espanole) in this
> thread has made me wonder about the compilers used in non-English
> speaking countries: are they forced to use English or are there
> language options which allow the use of local languages?

If you mean for keywords, I have never seen one and doubt any compnay
has ever produced one.  I have never seen an option for any Open Source
compiler that changed keywords into a lnaguage other than english.  And,
actually, the same goes for Operating Systems.  I have never seen one
with commands in anything but English.

I remember working with a bunch of Turkish Army Officers at the US Army
Programmer school back in 1980.  Imagine trying to offer assistance when
the COBOL statements are in English but all the "meaningful variable
names" are in Turkish.  :-)

bill
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-07-11T12:17:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfrj36tvnc734nl0qrcpkso7atbcntognd@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <89tnqfFcrU1@mid.individual.net>`

```
On 11 Jul 2010 11:21:51 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>In article <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>,
>	Alistair <alistair@ld50macca.demon.co.uk> writes:
…[16 more quoted lines elided]…
>bill

Having worked in many foreign countries, I can say I've never seen a
COBOL compiler with non-English syntax.  What's even harder for some
non-English countries is making data names they can understand when
the local alphabet isn't supported.  This is true with Sanskrit type
languages.  But the programmers all seem to be able to cope.

Regards,
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-12T08:12:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1j8m369kc7ihk8dm5d5lv5s6fgk8metd7s@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <89tnqfFcrU1@mid.individual.net>`

```
On 11 Jul 2010 11:21:51 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>I remember working with a bunch of Turkish Army Officers at the US Army
>Programmer school back in 1980.  Imagine trying to offer assistance when
>the COBOL statements are in English but all the "meaningful variable
>names" are in Turkish.  :-)

I worked on a Vax system that used its English language dictionary
when people created passwords.   A French lady had no problem in
creating passwords she could remember.

(How long will we need to live with passwords? - they aren't safe)
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-07-12T08:13:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58d9d814-efbc-44d6-81f2-657e7981899e@q12g2000yqj.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <89tnqfFcrU1@mid.individual.net>`

```
On Jul 11, 12:21 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <26a0bca1-96a1-4019-b01f-b944d4239...@u26g2000yqu.googlegroups.com>,
>         Alistair <alist...@ld50macca.demon.co.uk> writes:
…[16 more quoted lines elided]…
>

I did some support work for a Greek garage to correct the y2k problem.
One program with English syntax and Greek data-items. So I am aware of
the problem.
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-13T01:30:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a0jo0FgplU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>`

```
Alistair wrote:
> The use of English and Spanish (I presume; No Habla Espanole) in this
> thread has made me wonder about the compilers used in non-English
> speaking countries: are they forced to use English or are there
> language options which allow the use of local languages?

I worked with a French COBOL compiler many years ago (in France, of course). 
I didn't like it, but then I would say that... :-)

I also worked on a site in Germany where they said they had a German COBOL 
compiler. I never saw it and nobody, to my knowledge, ever used it.

I remember an old ICL 1900 COBOL compiler (might have been XEKB or Compact 
COBOL... not sure, it was a long tme ago...) which allowed you to define 
your own keywords, so it would have been quite feasible to compile COBOL in 
ANY language (that used a Western alphabet.)  ICL did a lot of business with 
Eastern Europe so that feature might have been deployed there.

Pete.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-07-12T14:23:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a0mqtFrvU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <8a0jo0FgplU1@mid.individual.net>`

```
In article <8a0jo0FgplU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Alistair wrote:
>> The use of English and Spanish (I presume; No Habla Espanole) in this
…[14 more quoted lines elided]…
> Eastern Europe so that feature might have been deployed there.

Only two comments on all this COBOL/Language discussion.

The only real problem is that unless the Standards Body actually approves
Keyword Tables in other languages programs written using German, French,
Spanish, etc.  would not be COBOL.

And, that being said, with the use of a Pre-processor (like cpp on most
Unix systems) it is actually trivial to write programs using keywords
in other languages.  The only problem would be on coming to an agreement
about what those keywords would be in each language.

Hmmmm.....  Maybe I'll take a shot at COBOL in German and see if it
garners any respect.  :-)

bill
```

##### ↳ ↳ Re: RM COBOL with ISAM files

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-12T08:09:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>`

```
On Sat, 10 Jul 2010 12:54:51 -0700 (PDT), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>The use of English and Spanish (I presume; No Habla Espanole) in this
>thread has made me wonder about the compilers used in non-English
>speaking countries: are they forced to use English or are there
>language options which allow the use of local languages?

I've read that the only place where non-English CoBOL compilers have
been available is France.   I don't know if that is true or ever has
been true.

Similarly, the only International Airport that has air traffic
controllers not speak English is Montreal.  
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-07-12T17:12:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PjN_n.4554$Bh2.1835@newsfe04.iad>`
- **In-Reply-To:** `<qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 10 Jul 2010 12:54:51 -0700 (PDT), Alistair
> <alistair@ld50macca.demon.co.uk> wrote:
…[15 more quoted lines elided]…
> 
Well almost anything can happen in la belle province. What used to be a 
very staunch Catholic province, controlled by the clergy both morally 
and politically, is now fanatically secular. A Jesuit school just 
challenged the Quebec government through the courts and currently won. 
The government demanded that the particular school follow the Provincial 
Education department idea as to what teaching religion is about, one of 
those vanilla flavoured curriculum 'where everybody's religion gets a 
mention'. Needless to say, while the prime emphasis for the Jesuits is 
teaching catholicism, in the modern more 'open' world, they do make 
reference to other religions.

Montreal air traffic - are you speaking from experience when you were a 
USAF flyboy ? I would have thought they could be taken to the cleaners !
I'm thinking of the Quebecois fanaticism about the French language being 
used, (I think they are the only 'country' that uses road sign posts 
painted 'ARRET' instead of 'STOP').  If they want to play the bi-lingual 
card under our Charter of Rights, then legally it follows an 'Anglo' 
could challenge them on not being bi-lingual and using Anglais in an Air 
Traffic tower. Perhaps a complaint, through channels, from a commerical 
pilot from les Etats-Unis ?

As regards versions of the COBOL language. I might have it wrong but I 
think the only COBOL compilers you can get from them are in Japanese 
characters ? The company, Hitachi. I wonder is there a Japanese version 
of Fujitsu in Japan. (Long ago there was an intent that Unisys would 
pick up on Hitachi OO COBOL, on contract, but the idea although 
publicized in the Web came to naught).

I kinda think that both India and China just might be clamouring for 
local versions ? Quite likely in India the emphasis is on English 
because they do a lot of outsourcing work contracted from N. America.
China I would have thought, is more likely to be interested in the 
domestic market, and without any slight intended I would have thought 
Indian education, (those old Empire roots), would be superior to the 
Chinese version ?

Bill's point about language translation. I checked on the VOCABULARY 
feature in Net Express before writing this. At this time it is limited; 
'translations' are strictly to do with OO and you create a 'translation' 
copyfile per Class that is affected. I can't recall, but do remember Tim 
Josling, (the Oz COBOL compiler), complaining some ten years back about 
COBOL RESERVED words - at least some 600 I think. With not too much 
effort the OO approach above could become 'universal' with a Dictionary 
lookup when you run your compiler; would marginally slow down the 
compiler, but not too dramatically I would suggest. Once you've created 
a DLL or EXE it doesn't matter what the original language was.

Here's an extract from the copyfile GUI.if. It's a bit confusing, 
because this is their original style with the word 'object' popping up 
all over the place. I've commented out what is not needed and this is an 
ABSTRACT class with only FACTORY methods - no Object/Instance methods :-

$set hidemessage(731)
  class-id. guibase is external.
   object section.                 <---- comment out 

   class-control.
      Dependent is class "dependnt"
      guibase is class "guibase".
  object.                          <---- comment out
FACTORY.                          <---- comment IN
  method-id. "setEvent".
  linkage section.
  01 lnkeventindex          pic s9(9) comp-5.
  01 lnkeventhandler        usage object reference.
  procedure division using lnkeventindex lnkeventhandler
*> vocabulary
  INVOKED as
  == setEvent
    [using] ([<self>] ,
              <lnkeventindex> ,
              <lnkeventhandler> )
  ==.
  end method "setEvent".
  method-id. "translateEvent".
  linkage section.
  01 lnkeventindex          pic s9(9) comp-5.
  01 lnkTranslatedEvent     pic s9(9) comp-5.
  01 lnkReceiver            usage object reference.
  01 lnkmethodName          usage object reference.
  procedure division using lnkeventindex lnkReceiver
                           lnkTranslatedEvent
*> vocabulary
  INVOKED as
  == map event <lnkeventindex> upon <self>
         to logical event <lnkTranslatedEvent> upon <lnkReceiver>
  ==.
  end method "translateEvent".
  method-id. "setEventTo".
  linkage section.
  01 lnkeventindex        pic s9(9) comp-5.
  01 lnkReceiver          usage object reference.
  01 lnkmethodName        pic x.
  01 lnkParam1            pic x(4).
  01 lnkParam2            pic x(4).
  procedure division using lnkeventindex lnkReceiver lnkMethodName
                           lnkParam1 lnkParam2
*> vocabulary
  INVOKED as
  == map event <lnkeventindex> upon <self>
         to method <lnkMethodName> upon  <lnkReceiver>
              [<lnkParam1>] [<lnkParam2>]
  ==.
  end method "setEventTo".
  END FACTORY.		<-----  comment IN
  end object.            <-----  comment OUT
  *> OBJECT.		<---  these two commented lines are here
  *> END OBJECT.         <---- to show there are no INSTANCE methods 

  end class guibase.

-----------------------------------------------------------------------------

Without thinking about it, I've used above to invoke GUIs, instead of 
the normal context.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-13T12:41:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1hmun$ddm$1@reader1.panix.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <PjN_n.4554$Bh2.1835@newsfe04.iad>`

```
In article <PjN_n.4554$Bh2.1835@newsfe04.iad>,
James Gavan  <jgavan@shaw.ca> wrote:

[snip]

>A Jesuit school just 
>challenged the Quebec government through the courts and currently won. 

And a tired, sad sigh went up, and throughout the land was heard the 
world-weary plaint 'When, *when* will folks realise that You Just Don't 
Mess With the Jesuits?'

From 
<http://groups.google.com/group/comp.lang.cobol/msg/129e29661efb91d3?dmode=source>

--begin quoted text:

(Note - I have nothing but respect for the Jesuit tradition of 
scholarship... and nothing but awe and fear at the ruthless tendencies 
demonstrated historically by these 'soldiers of Christ'.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-13T08:30:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oito3618sog2dell3e5is6v9seg6rm945b@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <PjN_n.4554$Bh2.1835@newsfe04.iad>`

```
On Mon, 12 Jul 2010 17:12:45 -0600, James Gavan <jgavan@shaw.ca>
wrote:

>> Similarly, the only International Airport that has air traffic
>> controllers not speak English is Montreal.  
…[11 more quoted lines elided]…
>reference to other religions.

Interesting problem - literate education requires knowledge of various
religions, their stories, and their beliefs.   And certainly in this
small world, knowing the beliefs of people around the world matters.
At least the handful of large, influential religions.

(I don't care that a particular mountain is sacred to some aboriginal
- let's treat the whole world as if it's sacred).

>Montreal air traffic - are you speaking from experience when you were a 
>USAF flyboy ? 

Not directly (never flew into Canada at all), but via hearsay.   And I
haven't flown in decades.

I have listened on the radio to a pilot talking with ATC - only to
find out later that he didn't speak English enough to converse - only
enough to do his job.

...

>I kinda think that both India and China just might be clamouring for 
>local versions ? Quite likely in India the emphasis is on English 
…[4 more quoted lines elided]…
>Chinese version ?

Also, English is an official language of India.   It is the language
that virtually all Indian businesses larger than family size must be
able to converse in.

But to a lesser extent, it is the lingua franca of the world.   If you
can do business in English, you can do business around the world.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-07-13T10:44:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4luo3616cc5v2oft81otplu6g5ojsgpi1f@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <PjN_n.4554$Bh2.1835@newsfe04.iad> <oito3618sog2dell3e5is6v9seg6rm945b@4ax.com>`

```
On Tue, 13 Jul 2010 08:30:45 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Mon, 12 Jul 2010 17:12:45 -0600, James Gavan <jgavan@shaw.ca>
>wrote:
…[23 more quoted lines elided]…
>

Great point.  If that were true, we wouldn't need environmentalists
and the dodo bird (among others) would not be extinct.


>>Montreal air traffic - are you speaking from experience when you were a 
>>USAF flyboy ? 
…[3 more quoted lines elided]…
>

I was in the Montreal airport in the summer of 2005 and I don't recall
that (no English) being the case.  I was catching a flight to
Switzerland and had about an hour and a half layover.


>I have listened on the radio to a pilot talking with ATC - only to
>find out later that he didn't speak English enough to converse - only
…[15 more quoted lines elided]…
>

Most educated Indians must speak 3 languages; English, Hindi and
whatever the language of their tribe/village is.  Most people in the
USA are lucky they speak some form of English that is understood by
everyone else.

>But to a lesser extent, it is the lingua franca of the world.   If you
>can do business in English, you can do business around the world.

So true.

Regards,
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-13T11:22:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<158p369pitq32ke12gc5lo74t1hhtp8la6@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <PjN_n.4554$Bh2.1835@newsfe04.iad> <oito3618sog2dell3e5is6v9seg6rm945b@4ax.com> <4luo3616cc5v2oft81otplu6g5ojsgpi1f@4ax.com>`

```
On Tue, 13 Jul 2010 10:44:44 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>>>Montreal air traffic - are you speaking from experience when you were a 
>>>USAF flyboy ? 
…[7 more quoted lines elided]…
>Switzerland and had about an hour and a half layover.

Were you listening to the pilots and controllers?
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2010-07-14T11:34:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i6mr36tg814bnunle8elhao6bps6de6v25@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <PjN_n.4554$Bh2.1835@newsfe04.iad> <oito3618sog2dell3e5is6v9seg6rm945b@4ax.com> <4luo3616cc5v2oft81otplu6g5ojsgpi1f@4ax.com> <158p369pitq32ke12gc5lo74t1hhtp8la6@4ax.com>`

```
On Tue, 13 Jul 2010 11:22:07 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Tue, 13 Jul 2010 10:44:44 -0400, SkippyPB
><swiegand@Nospam.neo.rr.com> wrote:
…[12 more quoted lines elided]…
>Were you listening to the pilots and controllers?

No.  I see I misread your earlier post.  Nevermind.

Regards,
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-13T11:19:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a1m7cF7uaU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 10 Jul 2010 12:54:51 -0700 (PDT), Alistair
> <alistair@ld50macca.demon.co.uk> wrote:
…[11 more quoted lines elided]…
> controllers not speak English is Montreal.

I believe you because I know you are ex USAF and up on these things, Howard. 
(And I have respect for your knowledge and integrity, from observing your 
posts here over years.) But, as a private pilot, I find that frightening and 
I would have thought it is also illegal. There are many airports around the 
world where controllers are multilingual, but English HAS to be the first 
language used, as I understand it. I understood there were international 
agreements about this. Have they been revoked for Montreal?

Are you absolutely certain they do "not speak English"?

Pete.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-07-12T23:56:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fd4d743-50c1-41fe-99fb-0f1ced485bcc@p11g2000prf.googlegroups.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <8a1m7cF7uaU1@mid.individual.net>`

```
On Jul 13, 11:19 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Howard Brazee wrote:
> > On Sat, 10 Jul 2010 12:54:51 -0700 (PDT), Alistair
…[26 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

A quick google turns up:

"""I'm a french controller so it will be easy to answer your question:
for now there is no possibility to listen to live atc from France but
i don't think it's illegal.Perhaps in a close future it will be
possible.
 About the langage used by us with the pilots: it's french or
english.In fact a controller speaks at the same time in english to
international pilots and in french with pilots of Air France...that
causes in fact some problems of comprehension because pilots don't
understand all that the controller says... so there is a project (but
it's just a project) which recommends to use only english langage: but
it will not happen before about 10 years I think..."""


"""Good day.  I do listen to Montreal ACC in french and english,
depending on the pilot.  It's fun hearing the weather and ATC
instructions in french.  It's like trying a different flavor."""

So, apparently, Montreal does speak English as well as French, and so
does French ATC.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-07-13T08:32:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6uo36hsdn5b90vm660q36q06upp867gcd@4ax.com>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <8a1m7cF7uaU1@mid.individual.net> <4fd4d743-50c1-41fe-99fb-0f1ced485bcc@p11g2000prf.googlegroups.com>`

```
On Mon, 12 Jul 2010 23:56:51 -0700 (PDT), Richard
<riplin@Azonic.co.nz> wrote:

>So, apparently, Montreal does speak English as well as French, and so
>does French ATC.

Times change, especially when safety is concerned.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-07-14T02:46:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a3cj4FegoU1@mid.individual.net>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com> <8a1m7cF7uaU1@mid.individual.net> <4fd4d743-50c1-41fe-99fb-0f1ced485bcc@p11g2000prf.googlegroups.com>`

```
Richard wrote:
> On Jul 13, 11:19 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[51 more quoted lines elided]…
> does French ATC.

Well, that's a relief... :-)

(Not that I'm likely to be landing myself there any time soon... :-))

Pete.
```

###### ↳ ↳ ↳ Re: RM COBOL with ISAM files

- **From:** "Vince Coen" <VBCoen@gmail.com>
- **Date:** 2010-07-13T17:59:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1279040377@f1.n250.z2.fidonet.ftn>`
- **References:** `<89dp6aFu90U1@mid.individual.net> <26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com> <qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>`

```
<26a0bca1-96a1-4019-b01f-b944d4239e94@u26g2000yqu.googlegroups.com>
<qc8m36lu3amkc38vdotjn3rs673mu5fg1a@4ax.com>
iF6M15)
Hello Howard!

12 Jul 10 15:09, Howard Brazee wrote to All:

 > Similarly, the only International Airport that has air traffic
 > controllers not speak English is Montreal.


I doubt that, the ICAO rules require ALL NATS, ATC etc to speak English on the 
radio abd this is throughout the world. Which is real convenient for me as my 
non-english skills are poor, short of ordering a drink/meal.
 In my travels around almost the whole of Europe including France, Germany, 
The Yugoslav block, Russia, the Anericas, Caribean (where english is not the 
native lang.) etc English is always used.

What the problem is, is that should say a native French pilot be flying at a 
local airfield, french is used, but if you are also using said airfield you 
can request that english be used (so you know where trafic is) they will do 
so.

All that said, some places the english accent is so bad you still struggle to 
understand which can make life intersting when using small airports but there 
again the solution is simple -- only use main international or commercial 
airports. For the USA pilots and unlike the USA, in Europe the cheap places to 
land are the non internation/commercial fields but it's a catch22 situation 
but if it is IFR then the options are somewhat reduced.



Vince
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
