[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How can i connect to COBOL files?

_4 messages · 4 participants · 2002-02_

---

### How can i connect to COBOL files?

- **From:** "jm" <jmpersonal@wanadoo.es>
- **Date:** 2002-02-08T02:35:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3v9e6$mib$1@news.wanadoo.es>`

```
I need to connect to COBOL files throught ODBC. It is possible?. How can i
get the ODBC for COBOL?

The files are RMCOBOL

THANKS.
```

#### ↳ Re: How can i connect to COBOL files?

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-02-07T20:31:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3vd97$41t$1@suaar1aa.prod.compuserve.com>`
- **References:** `<a3v9e6$mib$1@news.wanadoo.es>`

```
Jeez. Connect to COBOL files? You mean a file that was
created by a COBOL program? What kind of file is it?
An ascii file? Use the text ODBC driver.

 There is no such thing as an ODBC for COBOL. But you can
write ODBC *IN* COBOL. It is lots of fun!

I really hope there's some packed decimal, and some zoned
decimal data in this file... just to keep it interesting. ;)
```

#### ↳ Re: How can i connect to COBOL files?

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-02-08T02:42:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FWG88.10452$AV5.118279@rwcrnsc51.ops.asp.att.net>`
- **References:** `<a3v9e6$mib$1@news.wanadoo.es>`

```
Check out http://www.transoft.com
They have a tool for opening up regular old isam files via OBDC but it isn't
cheap.....

Mike


"jm" <jmpersonal@wanadoo.es> wrote in message
news:a3v9e6$mib$1@news.wanadoo.es...
> I need to connect to COBOL files throught ODBC. It is possible?. How can i
> get the ODBC for COBOL?
…[5 more quoted lines elided]…
>
```

#### ↳ Re: How can i connect to COBOL files?

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-02-08T09:30:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3j676ukh5be0v1kddcrp61o4jrscmnbtbf@4ax.com>`
- **References:** `<a3v9e6$mib$1@news.wanadoo.es>`

```
On Fri, 8 Feb 2002 02:35:30 +0100, "jm" <jmpersonal@wanadoo.es> wrote:

>I need to connect to COBOL files throught ODBC. It is possible?. How can i
>get the ODBC for COBOL?
>
>The files are RMCOBOL
go to www.liant.com and search for Relativity (Relational Databridge).
It works with both Native RM/COBOL (made by Liant) and MicroFocus
COBOL.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
