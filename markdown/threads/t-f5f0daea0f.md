[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Utility or Plugin for AcuCobol to create Adobe Acrobat files

_4 messages · 4 participants · 2002-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Utility or Plugin for AcuCobol to create Adobe Acrobat files

- **From:** "Ronald Royer" <golfron@paonline.com>
- **Date:** 2002-01-22T02:09:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AR338.19786$F01.1137457@nnrp1.ptd.net>`

```
Is there such a Utility, Plugin, or has someone invented the code to create
Adobe Acrobat files, instead of print image, etc.

Unix implementation only

Thanks

Ron
```

#### ↳ Re: Utility or Plugin for AcuCobol to create Adobe Acrobat files

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2002-01-22T02:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W6438.284$EL.35004@newshog.newsread.com>`
- **References:** `<AR338.19786$F01.1137457@nnrp1.ptd.net>`

```
Check out http://hoopajoo.net/projects/ipdf.html

"Ronald Royer" <golfron@paonline.com> wrote in message
news:AR338.19786$F01.1137457@nnrp1.ptd.net...
> Is there such a Utility, Plugin, or has someone invented the code to
create
> Adobe Acrobat files, instead of print image, etc.
>
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Utility or Plugin for AcuCobol to create Adobe Acrobat files

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-01-23T15:07:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xkA38.4545$hb1.1760451691@newssvr11.news.prodigy.com>`
- **References:** `<AR338.19786$F01.1137457@nnrp1.ptd.net>`

```
Ron,

One place to investigate is http://www.pdflib.com/pdflib/index.html.  PDFlib
is a library that is usable on Unix/Linux.  I built a PDFlib interface for
RM/COBOL which is available at http://www.liant.com/support/code/ (first
entry).  If you were to take a similar approach with AcuCOBOL. this solution
would require some recoding in your COBOL programs to use the CALL interface
rather that OPEN/WRITE/CLOSE.  However, you might want to change only one or
a few reports, which might make this option useful.

Another possibility is a subscription to http://createpdf.adobe.com.   I am
sure that one can hack the interface to make it usable from Unix, if you are
connected.

Happy hunting!

Best regards,
Tom Morrison
Liant Software Corporation
www.liant.com

"Ronald Royer" <golfron@paonline.com> wrote in message
news:AR338.19786$F01.1137457@nnrp1.ptd.net...
> Is there such a Utility, Plugin, or has someone invented the code to
create
> Adobe Acrobat files, instead of print image, etc.
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Utility or Plugin for AcuCobol to create Adobe Acrobat files

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2002-01-23T18:06:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c4ef9e1.16320268@news.epix.net>`
- **References:** `<AR338.19786$F01.1137457@nnrp1.ptd.net> <xkA38.4545$hb1.1760451691@newssvr11.news.prodigy.com>`

```
Ron and Tom:

FormPrint can print to the Acrobat PDF Writer (Windows Printer Driver)
and produce Acrobat PDF files.

UNIX isn't a problem either, because the Flexus COBOL Thin Client
supports UNIX servers and FormPrint works very well with Flexus COBOL
Thin Client.  This allows you to run the COBOL application on the UNIX
server and print across a TCP/IP network to a Windows print server. 


"Tom Morrison" <t.morrison@liant.com> wrote:

>Ron,
>
…[33 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
