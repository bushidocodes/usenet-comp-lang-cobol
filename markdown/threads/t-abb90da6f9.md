[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 400 extension

_8 messages · 5 participants · 1998-06_

---

### Cobol 400 extension

- **From:** "bruno kuper" <ua-author-7389241@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ldhbv$84b$1@front6.grolier.fr>`

```

Salut,
je ne trouve pas de documentation sur cette clause cbl 400

MOVE SPACES TO IDENT(N:M)
MOVE IDENT1 TO IDENT2(25:)

I search doc on this statement. How work this index?

merci, thank
```

#### ↳ Re: Cobol 400 extension

- **From:** "c harriott" <ua-author-17074085@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6ldhbv$84b$1@front6.grolier.fr>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr>`

```

Bruno Kuper wrote:

› Salut,
› je ne trouve pas de documentation sur cette clause cbl 400
…[10 more quoted lines elided]…
› e-mail : bku··.@clu··t.fr

jeavo bruno,

this is called 'reference modification'.
the first variable points to the starting point in a string , whilst the
second variable defines the length to use
if a second variable is not supplied then the length is from the start
to the end of the string.

eg
01 teststring pic x(10) value "ABCDEFGHIJ".

Move space to teststring (5:3).
›› teststring now contains       "ABCD   HIJ"
›› MOVE "end" to teststring(4:).
 
›› teststring now contains       "ABC    end"          (right
›› justification)
››                                                   "ABCend
" (left justification)


peace!
```

##### ↳ ↳ Re: Cobol 400 extension

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abb90da6f9-p2@usenetarchives.gap>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr> <gap-abb90da6f9-p2@usenetarchives.gap>`

```

C Harriott wrote:
› 
› Bruno Kuper wrote:
…[35 more quoted lines elided]…
› peace!

Bon soir, Bruno, comment ca va? The first response gave a good
explanation of reference modification, I posted to say that this is not
peculiar to COBOL/400, I have used it in MVS COBOL since 1992 (and I
wasn't an early user of COBOL II), or so.

Bill Lynch

(Sorry about the lack of a cedilla)
```

###### ↳ ↳ ↳ Re: Cobol 400 extension

- **From:** "robert..." <ua-author-7387749@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abb90da6f9-p3@usenetarchives.gap>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr> <gap-abb90da6f9-p2@usenetarchives.gap> <gap-abb90da6f9-p3@usenetarchives.gap>`

```

On Sun, 07 Jun 1998 21:38:36 -0400, Bill Lynch
wrote:

› C Harriott wrote:
›› 
…[4 more quoted lines elided]…
› un gros snip ...
 
› Bon soir, Bruno, comment ca va? The first response gave a good
› explanation of reference modification, I posted to say that this is not
…[5 more quoted lines elided]…
› (Sorry about the lack of a cedilla)

We francophones sincerely appreciate the effort.
I often say that if I didn't already speak French,
I would be horrified at the thought of having to learn it.
But it really is worth the effort -
as a language, it's a pleasure to speak and read.

En passant ( BTW ) the cedilla is ALT-135 ( ï¿½ )

Regards,

Robert Miller
```

###### ↳ ↳ ↳ Re: Cobol 400 extension

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abb90da6f9-p4@usenetarchives.gap>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr> <gap-abb90da6f9-p2@usenetarchives.gap> <gap-abb90da6f9-p3@usenetarchives.gap> <gap-abb90da6f9-p4@usenetarchives.gap>`

```

Robert Miller wrote:
› 
› (le snip)
…[5 more quoted lines elided]…
› as a language, it's a pleasure to speak and read.

Agreed, I took French in college and they used "La Methode Orale", or,
as an American teacher told us on the first day, "This is the last day
you'll use English in class" (our teacher was a Frenchman & his English
wasn't that good). At one point I could converse with French speaking
people who didn't speak English - those days are long gone:-( OTOH, when
I went to Tahiti in 1982 I could get along, but asked others to "parle
lentement et tres simplement". It worked - I had a great vacation.


›
› En passant ( BTW ) the cedilla is ALT-135 ( Ã§ )

Merci. Ã§ - elle se marche!

Bill Lynch

(My French is seriously rusty - is the above correct for "it works"?)

›
› Regards,
›
› Robert Miller
```

###### ↳ ↳ ↳ Re: Cobol 400 extension

_(reply depth: 5)_

- **From:** "robert..." <ua-author-7387749@usenetarchives.gap>
- **Date:** 1998-06-09T13:12:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abb90da6f9-p5@usenetarchives.gap>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr> <gap-abb90da6f9-p2@usenetarchives.gap> <gap-abb90da6f9-p3@usenetarchives.gap> <gap-abb90da6f9-p4@usenetarchives.gap> <gap-abb90da6f9-p5@usenetarchives.gap>`

```

On Mon, 08 Jun 1998 22:56:15 -0400, Bill Lynch
wrote:

› Robert Miller wrote:
›› 
…[10 more quoted lines elided]…
› 
Presque (almost)

"�a marche!" ( you said "she's waling herself" )

Salut,

RM
```

###### ↳ ↳ ↳ Re: Cobol 400 extension

_(reply depth: 6)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-09T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abb90da6f9-p6@usenetarchives.gap>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr> <gap-abb90da6f9-p2@usenetarchives.gap> <gap-abb90da6f9-p3@usenetarchives.gap> <gap-abb90da6f9-p4@usenetarchives.gap> <gap-abb90da6f9-p5@usenetarchives.gap> <gap-abb90da6f9-p6@usenetarchives.gap>`

```

Robert Miller wrote:
››› 
› (snip)
…[6 more quoted lines elided]…
› RM

Robert, thanks.

Bill Lynch
```

#### ↳ Re: Cobol 400 extension

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-06-07T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abb90da6f9-p8@usenetarchives.gap>`
- **In-Reply-To:** `<6ldhbv$84b$1@front6.grolier.fr>`
- **References:** `<6ldhbv$84b$1@front6.grolier.fr>`

```

On Sun, 7 Jun 1998 10:02:12 +0200, "Bruno Kuper"
wrote:

› Salut,
› je ne trouve pas de documentation sur cette clause cbl 400
…[6 more quoted lines elided]…
› merci, thank
This is not an index.

search under Reference Modification.

Best regards

Frederico Fonseca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
