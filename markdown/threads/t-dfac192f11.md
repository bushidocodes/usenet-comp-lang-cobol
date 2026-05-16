[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling StaticW32APi

_2 messages · 2 participants · 2000-05_

---

### Calling StaticW32APi

- **From:** johnglennon@my-deja.com
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8froe9$9st$1@nnrp1.deja.com>`

```
I'm trying to call the windows print manager api directly from a cobol
program.  (Cobol is NetExpress ver. 3.0 under Windows NT 4.0) I have
the 'Call-convention 74 is Staticw32api' statement in Special-Names.
The project has been linked to Winspool.lib and some calls have been
incorporated in the code, for expample "call static32api
'OpenPrinterA'", "call static32api 'WritePrinter'", and "call
static32api 'ClosePrinter'".  What I really need now is the syntax, and
paramters, to open the common dialog box to select from network
printers, and retain the page orientation, and also to invoke the font
selection dialog box.  I have been unable to find a list of functions
contained, and paramters required, in the Winspool.lib.  Any help would
be appreciated.

We do not want to use the Flexus printform for this and the various
PC_PRINT_ routines do not provide the escape sequence handling that we
need.

Thanks.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Calling StaticW32APi

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zsfU4.53738$55.1094698@news2.rdc1.on.home.com>`
- **References:** `<8froe9$9st$1@nnrp1.deja.com>`

```
You're probably looking for PageSetupDlg() in comdlg32.lib. For font
selection you're looking for ChooseFont(), also in comdlg32.lib. The calls
are documented in the MSDN or Microsoft Developers Kit.

<johnglennon@my-deja.com> wrote in message
news:8froe9$9st$1@nnrp1.deja.com...
> I'm trying to call the windows print manager api directly from a cobol
> program.  (Cobol is NetExpress ver. 3.0 under Windows NT 4.0) I have
…[19 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
