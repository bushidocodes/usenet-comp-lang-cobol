[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 105

_7 messages · 3 participants · 2002-03_

---

### Error 105

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2002-03-26T17:20:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA09FC9.99F8F6E6@medecine.unige.ch>`

```
Hello,

I have an error in my program compiled with MSCOBOL 5

+-----------
| Error accessing file: c:\mesobs\test.txt
|
| OBS-PRN Segment RT: Error 105 at Cobol PC 1800
+------------

In my manual: 105 Memory allocation error!

Okay, the exe file is 390'560 bytes, and my memory is 570'000 free
bytes. I use W95 switched to DOS.

If I compile the same program with NetExpress, I dont have any
error, this program run very well on the same platform.

Please give me somme explanation for my problem, It is perhaps a 
problem of link? 

Thank you in advance.

Alain.
```

#### ↳ Re: Error 105

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-27T00:06:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z28o8.21$LI.307@castor.casema.net>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch>`

```
Alain,

I've got no experience with MSCOBOL but shoulden't you add the size of your
data area(ws and fd) to the program size? How big is that part?

Gr. Ronald Leenheer

"Alain Chappuis" <alain.chappuis@medecine.unige.ch> schreef in bericht
news:3CA09FC9.99F8F6E6@medecine.unige.ch...
> Hello,
>
…[30 more quoted lines elided]…
>  /_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
```

##### ↳ ↳ Re: Error 105

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2002-03-28T09:11:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA2D01E.160C2D3F@medecine.unige.ch>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch> <z28o8.21$LI.307@castor.casema.net>`

```
Hello,

ronald leenheer a ï¿½crit :

> I've got no experience with MSCOBOL but shoulden't you add the size of your
> data area(ws and fd) to the program size? How big is that part?

Well, I have in my program:
120 segments, composed by 22 modules (Main and subp)

The $C00 add up 202'593 bytes
    $D00 add up  95'935 bytes
    $I   add up  23'973 bytes
  SORT   add up   6'026 bytes
  CODE   add up   2'250 bytes

  Total         330'777 bytes

> Gr. Ronald Leenheer
> 
…[15 more quoted lines elided]…
> > bytes. I use W95 switched to DOS.
```

#### ↳ Re: Error 105 --> Error 404

- **From:** Didier Morandi <Didier.Morandi@free.fr>
- **Date:** 2002-03-27T06:13:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA15513.7B969DA@free.fr>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch>`

```
http://ebn.unige.ch/www/alain.html

ERROR/ERREUR 404
The server was unable to open the requested document, please check your URL
specification. 


Alain Chappuis wrote:
> 
../..
>  [ CH-1211 Geneve 4     | URL   :http://ebn.unige.ch/www/alain.html]
>  /_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/


Ca va, Alain?
:-)

D.
```

##### ↳ ↳ Re: Error 105 --> Error 404

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2002-03-27T08:47:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA178F8.9B3D39E3@medecine.unige.ch>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch> <3CA15513.7B969DA@free.fr>`

```
Didier Morandi a ï¿½crit :
> 
> http://ebn.unige.ch/www/alain.html
…[11 more quoted lines elided]…
> Ca va, Alain?

Oui merci et toi? It is corrected now ;-) muchas gracias

Alain.
```

###### ↳ ↳ ↳ Re: Error 105 --> Error 404

- **From:** Didier Morandi <Didier.Morandi@free.fr>
- **Date:** 2002-03-27T20:52:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA222EE.8376F834@free.fr>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch> <3CA15513.7B969DA@free.fr> <3CA178F8.9B3D39E3@medecine.unige.ch>`

```
moi je termine demain ï¿½ l'UBS et je n'ai plus rien ï¿½ faire aprï¿½s. T'as pas
besoin d'un programmeur DCL ?

:-)

D.

Alain Chappuis wrote:
> 
> Oui merci et toi? It is corrected now ;-) muchas gracias
```

###### ↳ ↳ ↳ Re: Error 105 --> Error 404

_(reply depth: 4)_

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2002-03-28T08:34:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CA2C77B.3E78A1DF@medecine.unige.ch>`
- **References:** `<3CA09FC9.99F8F6E6@medecine.unige.ch> <3CA15513.7B969DA@free.fr> <3CA178F8.9B3D39E3@medecine.unige.ch> <3CA222EE.8376F834@free.fr>`

```
Didier Morandi a ï¿½crit :
> 
> moi je termine demain ï¿½ l'UBS et je n'ai plus rien ï¿½ faire aprï¿½s. T'as pas
> besoin d'un programmeur DCL ?

Dï¿½solï¿½, mais on arrï¿½te nos systï¿½mes VMS!

Alain.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
