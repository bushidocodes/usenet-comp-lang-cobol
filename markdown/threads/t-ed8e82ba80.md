[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing error using MF COBOL

_2 messages · 2 participants · 1999-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Printing error using MF COBOL

- **From:** "Steven Jones" <Steven11@tesco.net>
- **Date:** 1999-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pa7q9$h0p$1@barcode.tesco.net>`

```
I can not print direct from a  MFCOBOL compiler.  I am using Windows98 and
can print from my File menu

Thanks
Steve
```

#### ↳ Re: Printing error using MF COBOL

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pb2t3$q2f$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7pa7q9$h0p$1@barcode.tesco.net>`

```

Steven Jones <Steven11@tesco.net> wrote in message
news:7pa7q9$h0p$1@barcode.tesco.net...
> I can not print direct from a  MFCOBOL compiler.  I am using Windows98 and
> can print from my File menu
…[4 more quoted lines elided]…
>
    You did not mention which compiler, but try the +P0+L0 runtime switchs.

+P0 makes it use dos instead of bios (you lose the ability to detect printer
status), and the +L0 forces it to return a runtime error instead of abort
retry ignore.  sometimes, a printer error while using +P0 without +L0 will
produce the DOS abort retry ... message.  Abort aborts without closing
files.

    Also - an odd thing - try accessing the printer, from windows or command
line before trying from cobol.  I have had machines that need to be "jump
started" with an echo. or something before allowing normal access.  Mine
even accessed the floppys for some reason.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
