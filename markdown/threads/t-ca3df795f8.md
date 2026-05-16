[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Execute programs with Win32API ?

_2 messages · 2 participants · 2000-07_

---

### Execute programs with Win32API ?

- **From:** rezeerf@my-deja.com
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l14l3$v50$1@nnrp2.deja.com>`

```
Hope someone can help me :

How can i execute an i.e. exe-file with help of win32API out of a
cobol-source (i'm using netexpress 3.0) ?

Are there any other opportunities ?

Thanx in advance

alex


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Execute programs with Win32API ?

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l1hao$77r$1@hyperion.mfltd.co.uk>`
- **References:** `<8l14l3$v50$1@nnrp2.deja.com>`

```
Alex,

I assume you would like to kick-off another EXE program from
within your COBOL program?  If so, then you can do this via the
CBL_EXEC_RUN_UNIT function.  Details of the call can be
found in the Net Express online help.

Hope this helps.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

<rezeerf@my-deja.com> wrote in message news:8l14l3$v50$1@nnrp2.deja.com...
> Hope someone can help me :
>
…[11 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
