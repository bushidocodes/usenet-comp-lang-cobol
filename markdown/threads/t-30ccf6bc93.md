[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Importing Cobol

_5 messages · 5 participants · 1999-02_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Importing Cobol

- **From:** "Gary Griggs" <gdgriggs@geneseo.net>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79so38$6f3$1@news3.infoave.net>`

```
I have two existing programs written in Cobol.  Can I import the data files
from these pragrams into SQL Server or Access without any modification to
the programs?
```

#### ↳ Re: Importing Cobol

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79urko$ucg$1@nnrp1.dejanews.com>`
- **References:** `<79so38$6f3$1@news3.infoave.net>`

```
though I don't know which ones off the top of my head, you can probably find
an ODBC driver which will allow Access to read these files.  Depending on
their layout, you might even be able to import them into native Access or
SQLServer tables.

In article <79so38$6f3$1@news3.infoave.net>,
  "Gary Griggs" <gdgriggs@geneseo.net> wrote:
> I have two existing programs written in Cobol.  Can I import the data files
> from these pragrams into SQL Server or Access without any modification to
> the programs?
>
>

Ed Stevens
Nissan Motor Mfg. Corp., USA

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Importing Cobol

- **From:** "Calle" <markus.carl@fen.baynet.de>
- **Date:** 1999-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a1pc8$rfr$1@freenet-b.fen.baynet.de>`
- **References:** `<79so38$6f3$1@news3.infoave.net>`

```
Maybe we got the right solution :
we got an ODBC driver for all kinds of COBOL files (e.g. IND, REL, ...).
If you need further information mail to ics-khatib@fen.baynet.de


Gary Griggs schrieb in Nachricht <79so38$6f3$1@news3.infoave.net>...
>I have two existing programs written in Cobol.  Can I import the data files
>from these pragrams into SQL Server or Access without any modification to
>the programs?
>
>
```

##### ↳ ↳ Re: Importing Cobol

- **From:** "Arnold" <arnoldh@home.com>
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hXDx2.359$0A4.1004@news.rdc1.mi.home.com>`
- **References:** `<79so38$6f3$1@news3.infoave.net> <7a1pc8$rfr$1@freenet-b.fen.baynet.de>`

```
You don't state the platform you are working on. You may have to translate
from EBCDIC to ANSI, but you dont' have to change the programs to do that.
Try the EDIT argument in SORT.

Calle wrote in message <7a1pc8$rfr$1@freenet-b.fen.baynet.de>...
>Maybe we got the right solution :
>we got an ODBC driver for all kinds of COBOL files (e.g. IND, REL, ...).
…[4 more quoted lines elided]…
>>I have two existing programs written in Cobol.  Can I import the data
files
>>from these pragrams into SQL Server or Access without any modification to
>>the programs?
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Importing Cobol

- **From:** "John Hicks (Remove \\"nospam\\" from address before replying)" <johnhicks@ibm.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CA4DED.E9F1DFDB@ibm.net>`
- **References:** `<79so38$6f3$1@news3.infoave.net>`

```
Gary--

Check first to see if perchance the files are sequential and: 
--are fixed format 
--contain no binary data 
--have a carriage-return/line-feed after each record
(You can tell by displaying the data on your screen with the DOS TYPE
command. If all the data lines up from line to line, you're probably
OK.)

If so, you can import the files directly into MS Access. It lets you
tell it where each field begins. 

--John

Gary Griggs wrote:
> 
> I have two existing programs written in Cobol.  Can I import the data files
> from these pragrams into SQL Server or Access without any modification to
> the programs?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
