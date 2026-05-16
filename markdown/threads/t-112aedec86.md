[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Windows 2000 and Terminal Server

_3 messages · 2 participants · 2000-07_

---

### Windows 2000 and Terminal Server

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kepir$354$1@hyperion.mfltd.co.uk>`

```
Folks,

Someone asked a question on the alt.cobol newsgroup about Windows 2000
and Terminal Server.  I am repeating the information here as I thought it
may
be of interest to other MERANT COBOL users.

MERANT has tested and supports Net Express 3.0 with Service Pack 1
on Windows 2000.  However, we do not support the use of Microsoft's
Terminal Server with this version of Net Express.

If you want to use Windows 2000 and/or Terminal Server then you should
upgrade to Net Express 3.1.

I hope the above is of help.

All the best.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.
```

#### ↳ Re: Windows 2000 and Terminal Server

- **From:** Fred Young <fred@perfectcircle.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396E1C58.394E2639@perfectcircle.com>`
- **References:** `<8kepir$354$1@hyperion.mfltd.co.uk>`

```


Paddy Coleman wrote:

> MERANT has tested and supports Net Express 3.0 with Service Pack 1
> on Windows 2000.  However, we do not support the use of Microsoft's
…[4 more quoted lines elided]…
>

Thanks for the info Paddy.
We have been using Net Express 3.0 on Terminal Server using Citrix MetaFrame
in a production environment for about a year now.  The only problems we've
had were discrepancies between Merants 16 and 32 bit versions.

Yes, we still use the 16 bit compiler.  We have to, 32 bit code runs much
slower on Win98, as the 16 bit code runs much slower on NT.  I assume Win9x
"thunks" 32 bit code, while NT "wows" 16 bit code, causing the performance
discrepancy.  I thought Merant was a bit quick to sundown the 16 bit product
while we had a major operating system which is still uses 16 bit internals.
```

##### ↳ ↳ Re: Windows 2000 and Terminal Server

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kmuom$14h$1@hyperion.mfltd.co.uk>`
- **References:** `<8kepir$354$1@hyperion.mfltd.co.uk> <396E1C58.394E2639@perfectcircle.com>`

```
Fred,

I am glad to hear that you have been able to use NE 3.0 in your
TS environment without too much trouble.  As I said, we simply
have not tested with this version and therefore cannot guarntee it
will work without problem on TS/MF.

Your comments about 16/32 bit are spot on and tie in with
Microsoft's own recommendations on which operating system
a particular Customer should use.

Have a great weekend.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

Fred Young <fred@perfectcircle.com> wrote in message
news:396E1C58.394E2639@perfectcircle.com...
>
>
…[11 more quoted lines elided]…
> We have been using Net Express 3.0 on Terminal Server using Citrix
MetaFrame
> in a production environment for about a year now.  The only problems we've
> had were discrepancies between Merants 16 and 32 bit versions.
>
> Yes, we still use the 16 bit compiler.  We have to, 32 bit code runs much
> slower on Win98, as the 16 bit code runs much slower on NT.  I assume
Win9x
> "thunks" 32 bit code, while NT "wows" 16 bit code, causing the performance
> discrepancy.  I thought Merant was a bit quick to sundown the 16 bit
product
> while we had a major operating system which is still uses 16 bit
internals.
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
