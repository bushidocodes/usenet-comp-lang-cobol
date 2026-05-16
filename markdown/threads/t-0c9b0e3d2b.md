[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DDE & MicroFocus

_6 messages · 4 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### DDE & MicroFocus

- **From:** "PDMars" <pdmars@yahoo.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net>`

```
I need to use a VB program to communicate with a MicroFocus program using
DDE.
Any sample code would be greatly appreciated.

Thanks
Paul
```

#### ↳ Re: DDE & MicroFocus

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81jrpf$1kc$1@neptunium.btinternet.com>`
- **References:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net>`

```

PDMars wrote in message <81i4sg$t81$1@fir.prod.itd.earthlink.net>...
>I need to use a VB program to communicate with a MicroFocus program using
>DDE.
…[6 more quoted lines elided]…
>

I dont think that Micro Focus products support DDE,
as I have never used it.

You could use OLE instead though this I have used.

Simon R Hart.
```

##### ↳ ↳ Re: DDE & MicroFocus

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81juob$gpt$3@aklobs.kc.net.nz>`
- **References:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net> <81jrpf$1kc$1@neptunium.btinternet.com>`

```
Simon R Hart <hart1@technologist.com> wrote:

: I dont think that Micro Focus products support DDE,
: as I have never used it.

DDE is in the Windows API.  MF can call the API.  Thus MF can
use DDE when in a Windows environment.

In fact I have used DDE in MF Cobol, but the code is not
available for posting, and not suitable either being in a
production system rather than a simple demo.
```

###### ↳ ↳ ↳ Re: DDE & MicroFocus

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81m5mv$4as$1@uranium.btinternet.com>`
- **References:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net> <81jrpf$1kc$1@neptunium.btinternet.com> <81juob$gpt$3@aklobs.kc.net.nz>`

```

Richard Plinston wrote in message <81juob$gpt$3@aklobs.kc.net.nz>...
>Simon R Hart <hart1@technologist.com> wrote:
>
…[10 more quoted lines elided]…
>

I would hate to think of the code to use DDE under the Win32s
API module.
Much like using Win32s API for ODBC.
It is a total nightmare, more like ASM than a 4gl.
MicroFocus do *not* support DDE in any form. Thats *not* to say
you cant access DDE from the Win32s API's within Cobol.  But I would love
to see a workable commercial Win32s API DDE application up and running.
The fact is I dont think any exists, it would be ten times easier to use
OLE.


Simon R Hart.
```

###### ↳ ↳ ↳ Re: DDE & MicroFocus

_(reply depth: 4)_

- **From:** "PDMars" <pdmars@yahoo.com>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81n9de$4ua$1@fir.prod.itd.earthlink.net>`
- **References:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net> <81jrpf$1kc$1@neptunium.btinternet.com> <81juob$gpt$3@aklobs.kc.net.nz> <81m5mv$4as$1@uranium.btinternet.com>`

```
OK Simon, I'm willing to believe that it could be done with OLE - but could
you furnish an example, starting point, any kind of hint as to how you would
tackle this?

Paul DeMarsh
```

#### ↳ Re: DDE & MicroFocus

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81ibic$pkl$1@news.inet.tele.dk>`
- **References:** `<81i4sg$t81$1@fir.prod.itd.earthlink.net>`

```
See Merant Micro Focus sample area on www.merant.com
Ib

PDMars skrev i meddelelsen <81i4sg$t81$1@fir.prod.itd.earthlink.net>...
>I need to use a VB program to communicate with a MicroFocus program using
>DDE.
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
