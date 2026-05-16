[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# comp-x

_4 messages · 4 participants · 2002-05_

---

### comp-x

- **From:** "Tomba" <tombatore@hotmail.com>
- **Date:** 2002-05-14T23:49:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ce18684$0$6951$ba620e4c@news.skynet.be>`

```
hy,

making some screens with microfocus cobol, I wondered what in a pic clause
that COMP-X is standing for.
Does anyone have an idea?

thanks,

 Steven DG
```

#### ↳ Re: comp-x

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-05-15T00:55:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-eL0wcoMyhYSp@thishost>`
- **References:** `<3ce18684$0$6951$ba620e4c@news.skynet.be>`

```
On Tue, 14 May 2002 21:49:49 UTC, "Tomba" <tombatore@hotmail.com> 
wrote:

> hy,
> 
…[7 more quoted lines elided]…
> 

It is used to specify "native binary" 
```

##### ↳ ↳ Re: comp-x

- **From:** cobol@dudleysworld.co.uk (John Dudley)
- **Date:** 2002-05-15T03:49:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ab988303.0205150249.32c15e9b@posting.google.com>`
- **References:** `<3ce18684$0$6951$ba620e4c@news.skynet.be> <ZpzG4UNLyRNq-pn2-eL0wcoMyhYSp@thishost>`

```
COMP-X is not native binary, COMP-5 is.
Byte swapping can occur with COMP-X data items depending on you
processor type, where COMP-5 items are stored in the native format.

lsunley@mb.sympatico.ca wrote in message news:<ZpzG4UNLyRNq-pn2-eL0wcoMyhYSp@thishost>...
> On Tue, 14 May 2002 21:49:49 UTC, "Tomba" <tombatore@hotmail.com> 
> wrote:
…[12 more quoted lines elided]…
> It is used to specify "native binary"
```

#### ↳ Re: comp-x

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-05-15T01:01:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vriE8.38281$Po6.16256@rwcrnsc52.ops.asp.att.net>`
- **References:** `<3ce18684$0$6951$ba620e4c@news.skynet.be>`

```
If you define a field like this

01  YER-NEW-FIELD   PIC X(1) COMP-X.

Then you access it like it's a byte.... 0-255.


Mike



"Tomba" <tombatore@hotmail.com> wrote in message
news:3ce18684$0$6951$ba620e4c@news.skynet.be...
> hy,
>
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
