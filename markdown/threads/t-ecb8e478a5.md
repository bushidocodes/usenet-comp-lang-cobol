[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Selecting specific printer

_4 messages · 4 participants · 2003-03_

---

### Selecting specific printer

- **From:** pearson@infonegocio.com (Pamela)
- **Date:** 2003-03-09T16:00:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3146a5b.0303091600.59ec6f80@posting.google.com>`

```
Is it possible to select a specific printer within a 
Cobol program running under DOS?
I have tried assigning a printer file and moving
"LPT1" or "LPT2" to it but no output is produced.
Any help would be greatly appreciated.
```

#### ↳ Re: Selecting specific printer

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-10T13:28:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4gmcq$mm8$1@aklobs.kc.net.nz>`
- **References:** `<a3146a5b.0303091600.59ec6f80@posting.google.com>`

```
Pamela wrote:

> Is it possible to select a specific printer within a
> Cobol program running under DOS?
> I have tried assigning a printer file and moving
> "LPT1" or "LPT2" to it but no output is produced.
> Any help would be greatly appreciated.

Have a look on your disk and se if there is a file 'LPT1' now.

It may be that you have to use LPT1: with a colon.

If you are running in a DOS box under Windows you may also have to ensure 
that the printers are set up to capture print data from DOS programs.
```

#### ↳ Re: Selecting specific printer

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-09T18:50:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dGmdnfOy7KopfPajXTWciQ@giganews.com>`
- **References:** `<a3146a5b.0303091600.59ec6f80@posting.google.com>`

```

"Pamela" <pearson@infonegocio.com> wrote in message
news:a3146a5b.0303091600.59ec6f80@posting.google.com...
> Is it possible to select a specific printer within a
> Cobol program running under DOS?
> I have tried assigning a printer file and moving
> "LPT1" or "LPT2" to it but no output is produced.
> Any help would be greatly appreciated.

If your program is running in a DOS box under Windows, RPV (Report Program
Viewer) is a free re-director to take a DOS print file (on disk) and
redirect it through the Windows print routine.
```

#### ↳ Re: Selecting specific printer

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-03-10T10:39:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2624354.1047292758@dbforums.com>`
- **References:** `<a3146a5b.0303091600.59ec6f80@posting.google.com>`

```

see

assign to dynamic
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
