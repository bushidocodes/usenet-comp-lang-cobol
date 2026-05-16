[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# To and from Excel

_5 messages · 4 participants · 2000-05_

---

### To and from Excel

- **From:** pvtronin@aol.com (PVTRONIN)
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000515004742.24296.00003087@ng-cd1.aol.com>`

```
I'm trying to learn some suff on my own now tha tthe semester is over.

I'm using windows 98, and RMCOSTAR, and educational compiler. I want to be able
to run a COBOL program on an Excel file, and be able to write to an Excel file.
I can't find any refeerence in my text book, I think it was writen before Excel
was. Can anyone offer guidance or maybe a good refence, a website or book?


PVTRonin
```

#### ↳ Re: To and from Excel

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CuST4.68$xM5.31443@dfiatx1-snr1.gtei.net>`
- **References:** `<20000515004742.24296.00003087@ng-cd1.aol.com>`

```
PVTRONIN <pvtronin@aol.com> wrote in message
news:20000515004742.24296.00003087@ng-cd1.aol.com...
> I'm trying to learn some suff on my own now tha tthe semester is over.
>
> I'm using windows 98, and RMCOSTAR, and educational compiler. I want to be
able
> to run a COBOL program on an Excel file, and be able to write to an Excel
file.
> I can't find any refeerence in my text book, I think it was writen before
Excel
> was. Can anyone offer guidance or maybe a good refence, a website or book?
>

You should be able to find the structure of an Excel file at
http://www.wotsit.org

Alternately, ODBC drivers are available for Excel files; and Excel is both a
DDE server and client. If your compiler can access the Windows API,  these
could be viable options.

MCM
```

##### ↳ ↳ Re: To and from Excel

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39200CA7.1AFD@NOSPAMguysoftware.com>`
- **References:** `<20000515004742.24296.00003087@ng-cd1.aol.com> <CuST4.68$xM5.31443@dfiatx1-snr1.gtei.net>`

```
One problem with writing to handle another "proprietary" format is that the format may 
change with a new version of it's "native" program, and you have to keep upgrading if 
you want to read it.
If you are transferring only data cells (i.e. no formatting, "tombstone" data or 
formulae), you might do better transferring the data in a "standard" format that both 
you program and Excel will understand.  Comma  delimited is one choice that's easy to 
code. DBF files are a bit trickier to code, but are another possibility and the DBF 
files are pretty standard (later enhancements tended to use additonal files and leave 
the original DBF format alone except for a version flag byte in the header).

Michael Mattias wrote:
> 
> PVTRONIN <pvtronin@aol.com> wrote in message
…[19 more quoted lines elided]…
> MCM
```

#### ↳ Re: To and from Excel

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39211C3D.D588225B@zip.com.au>`
- **References:** `<20000515004742.24296.00003087@ng-cd1.aol.com>`

```
PVTRONIN wrote:
> 
> I'm trying to learn some suff on my own now tha tthe semester is over.
…[7 more quoted lines elided]…
> PVTRonin

It is uncommon for excel files to be read and written directly.  It is
more common to write comma separated variable records.

This is a record structure (at it's simplest) which every field is
enclosed in quotes and there is a comma between fields.  If you need a
quote in the field then the quotes are doubled:

"00001","test product","deliver at three o""clock"

Most people get the escaping quotes logic wrong including most
production products I have tested.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: To and from Excel

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3921F5F9.164B@NOSPAMguysoftware.com>`
- **References:** `<20000515004742.24296.00003087@ng-cd1.aol.com> <39211C3D.D588225B@zip.com.au>`

```
Ken Foskey wrote:
> 
> PVTRONIN wrote:
…[21 more quoted lines elided]…
> production products I have tested.

Handling of quotes inside a quoted string depends on the implementation.  As you noted, 
many products get it wrong.  ParseRat looks at the comma as well - if the comma 
(or a lineend) is not there, then it treats the quote as part of the string instead of 
as the string delimiter.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
