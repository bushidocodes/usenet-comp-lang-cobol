[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking RM/Cobol Exports Tools or relationed

_7 messages · 5 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Looking RM/Cobol Exports Tools or relationed

- **From:** "Fco. Javier Garcia Garcia" <MiraEnLaFirma@LookInTheSign.Es>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6slghg$hik$1@talia.mad.ibernet.es>`

```
Hello All,

I have in my office a big aplication that works with RM/COBOL, in a few
months we need export or acces to all data files and export it to another
format, because we are emigrating our aplication.

Did someting know any tools that can help us.

Now, we must to write a lot of programs with Copys, FD and SELECT, to export
the data to ASCII, this is so tedious.

�Someting drivers that allow acces with ODBC?

Thanks, Javi.
```

#### ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6slkhn$qhs$3@news02.btx.dtag.de>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es>`

```
Fco. Javier Garcia Garcia schrieb:

> Hello All,
>
…[20 more quoted lines elided]…
> Lideres en manufacturaciï¿½n de rejillas.

 I've written some (..PASCAL, don't hit me) Programms, that convert
RM-COBOL Files (*.INX) to plain ASCII-Files. only using the
original FD-File (I interprete the COMP-s and the REDEFINITIONS
and the OCCURS) to convert the data.

Does that help?

AS
```

##### ↳ ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** Albert Ratzlaff <albert@infonet.com.py>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EEF5EC.A3558DE9@infonet.com.py>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es> <6slkhn$qhs$3@news02.btx.dtag.de>`

```


Andreas Strzoda wrote:

>  I've written some (..PASCAL, don't hit me) Programms, that convert
> RM-COBOL Files (*.INX) to plain ASCII-Files. only using the
…[4 more quoted lines elided]…
>

What version of RM/COBOL are you working with?

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** "Fco. Javier Garcia Garcia" <MiraEnLaFirma@LookInTheSign.Es>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sovov$b10$1@talia.mad.ibernet.es>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es> <6slkhn$qhs$3@news02.btx.dtag.de> <35EEF5EC.A3558DE9@infonet.com.py>`

```
>What version of RM/COBOL are you working with?

I'm using RMCOBOL 5.3 for MS-DOS And AT&T Unix.

Thanks.
```

##### ↳ ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** "Fco. Javier Garcia Garcia" <MiraEnLaFirma@LookInTheSign.Es>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sp0s3$c14$1@talia.mad.ibernet.es>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es> <6slkhn$qhs$3@news02.btx.dtag.de>`

```
Hello,


> I've written some (..PASCAL, don't hit me) Programms, that convert
>RM-COBOL Files (*.INX) to plain ASCII-Files. only using the
>original FD-File (I interprete the COMP-s and the REDEFINITIONS
>and the OCCURS) to convert the data.

Ohh, but my version of RM/COBOL have not a *.INX files, it only produces
*.DAT files, that contain data and index information inside.

If you send me your utility, i can study, how to use it with *.DAT files, i
don't Konw how transform COMP values, signed values, OCURRS. And i need to
see the delete marc of record and many others thinks.

I'm looking for tool to read *.DAT files (i have all the source fo the
especificaciones of the data files).

I thin that I can make a utility, to read *.CBL and *.CPY, make a CBL,
compile it and extract it (sequential read) the data of the file to ASCII.

Sorry for me English.

Thaks, Javi.
```

#### ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** "Mike Rochford" <miker@easirun.co.za>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6so7dm$5cg$1@news01.iafrica.com>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es>`

```

Fco. Javier Garcia Garcia wrote in message
<6slghg$hik$1@talia.mad.ibernet.es>...
>Hello All,
>

>�Someting drivers that allow acces with ODBC?
>
>Thanks, Javi.
>

Contact Liant and ask about Relational Data Bridge. It a set of ODBC drivers
for RM/Cobol data and is a really slick product.

Mike.
```

#### ↳ Re: Looking RM/Cobol Exports Tools or relationed

- **From:** "John Kos" <john@easysoft.com>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<905192765.4239.0.nnrp-03.c2468fc2@news.demon.co.uk>`
- **References:** `<6slghg$hik$1@talia.mad.ibernet.es>`

```
Try looking at http://www.easysoft.com

Fco. Javier Garcia Garcia wrote in message
<6slghg$hik$1@talia.mad.ibernet.es>...
>Hello All,
>
…[6 more quoted lines elided]…
>Now, we must to write a lot of programs with Copys, FD and SELECT, to
export
>the data to ASCII, this is so tedious.
>
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
