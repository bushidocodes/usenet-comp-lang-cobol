[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating PDF in Cobol

_7 messages · 2 participants · 2009-01_

---

### Re: Creating PDF in Cobol

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-01-26T18:33:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com>`

```
On Jan 27, 2:26 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > So if you do want to write templating it may be better to use OO.
>
…[26 more quoted lines elided]…
> But it works, simple as it is.

It seems to be just putting a simple PDF wrapper around the text file
lines, wouldn't a <pre> ... </pre> do just about the same job of
displaying the text formatted as the program will print it ?
```

#### ↳ Re: Creating PDF in Cobol

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-01-26T21:20:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com>`

```
> wouldn't a <pre> ... </pre> do just about the same job of
> displaying the text formatted as the program will print it?

Just like instead of doing file01.TXT to file01.PDF, do it directly
with file01.HTML with a <pre></pre> tags? Nice idea though.

Yes, except that if it's 'within' a PDF document.... the end-user
could not alter the content prior printing a document in a browser.
Some user will cut/paste document content (especially POs) and re-
print it using a Notepad. It is then that you could add security
method to a PDF.

And you can archive every users PDF (printing) file... which of course
you could do it as well in a text file.
```

##### ↳ ↳ Re: Creating PDF in Cobol

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-01-26T21:36:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3ad4cf1-3471-4946-a8ef-f4ddc757390f@v18g2000pro.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com> <2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com>`

```
On Jan 27, 6:20 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > wouldn't a <pre> ... </pre> do just about the same job of
> > displaying the text formatted as the program will print it?
…[8 more quoted lines elided]…
> method to a PDF.

Do you think that one cannot copy/paste from PDFs ? Probably not with
Adobe reader, but there are several other PDF readers.

> And you can archive every users PDF (printing) file... which of course
> you could do it as well in a text file.
```

###### ↳ ↳ ↳ Re: Creating PDF in Cobol

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-01-26T22:01:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<25d0fb39-20af-4d4d-a82f-75d19aeeecb4@r36g2000prf.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com> <2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com> <f3ad4cf1-3471-4946-a8ef-f4ddc757390f@v18g2000pro.googlegroups.com>`

```
> Do you think that one cannot copy/paste from PDFs ? Probably not with
> Adobe reader, but there are several other PDF readers.

You can, but archiving a PDF copy will not compromise 'control'.

Few things which in most cases happening in a browser-based solution,
and usually we get rid of.

1. Default "File->Print" menu option of the browser. Some browsers has
default margin so you cannot impose the pre-defined format of the
report.

2. In browser-based apps, usually toolbar menus are
'disabled' (especially in IE) and so displaying a PDF file in browser.

So I opted to use PDF displayed report document because of the PDF
reader built-in 'print' button associated with it.
```

###### ↳ ↳ ↳ Re: Creating PDF in Cobol

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2009-01-27T09:38:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fc9953e-1e6d-4007-9da5-ee2cb303fd4b@p2g2000prf.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com> <2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com> <f3ad4cf1-3471-4946-a8ef-f4ddc757390f@v18g2000pro.googlegroups.com> <25d0fb39-20af-4d4d-a82f-75d19aeeecb4@r36g2000prf.googlegroups.com>`

```
On Jan 27, 7:01 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > Do you think that one cannot copy/paste from PDFs ? Probably not with
> > Adobe reader, but there are several other PDF readers.
>
> You can, but archiving a PDF copy will not compromise 'control'.

Nor, as you said, will archiving a text copy, or keeping the data in
the database/isam file where it will be directly accessible.

> Few things which in most cases happening in a browser-based solution,
> and usually we get rid of.
…[9 more quoted lines elided]…
> reader built-in 'print' button associated with it.

Why not only print directly to their printer and avoid interception
without having to fiddle with their browser ? It is not like you will
have random clients allowed to have POs.

(which I assume you do mean Purchase Orders).
```

###### ↳ ↳ ↳ Re: Creating PDF in Cobol

_(reply depth: 5)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-01-27T20:05:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c56c596-e8c7-4d9e-be23-b7ba7d37caa5@w24g2000prd.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com> <2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com> <f3ad4cf1-3471-4946-a8ef-f4ddc757390f@v18g2000pro.googlegroups.com> <25d0fb39-20af-4d4d-a82f-75d19aeeecb4@r36g2000prf.googlegroups.com> <3fc9953e-1e6d-4007-9da5-ee2cb303fd4b@p2g2000prf.googlegroups.com>`

```
>
> Why not only print directly to their printer and avoid interception
…[3 more quoted lines elided]…
> (which I assume you do mean Purchase Orders).

Yes, it is Purchase Orders.

Say a company that has multi-branch or franchises using a browser-
based online application. So franchise in Chicago, and somewhere in
Singapore entering their POs simultaneously using a single ASP/ASPX/
PHP/JSP page.... looking at their screen with different PO entries of
their own sites, then print the PO (their own).

Some online-applications requires ActiveX for them to print from their
printer (client-side) using the information extracted from the IE/
Mozilla browsers.... but then again, it wont be feasible for Linux
users. ActiveX client application can't be installed to a Linux OS.

So browser printing format is needed.... displaying the format in PDF
and directly print it using their "own" client-based printers.
```

###### ↳ ↳ ↳ Re: Creating PDF in Cobol

_(reply depth: 5)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-01-27T20:22:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf71897d-aa37-4ffb-b276-293ea39b4086@z27g2000prd.googlegroups.com>`
- **References:** `<5f676091-5247-4d80-8f32-22d37fb11638@k1g2000prb.googlegroups.com> <2f05ce1c-340d-42fd-92ef-c4640c697204@t26g2000prh.googlegroups.com> <f3ad4cf1-3471-4946-a8ef-f4ddc757390f@v18g2000pro.googlegroups.com> <25d0fb39-20af-4d4d-a82f-75d19aeeecb4@r36g2000prf.googlegroups.com> <3fc9953e-1e6d-4007-9da5-ee2cb303fd4b@p2g2000prf.googlegroups.com>`

```
>
> Why not only print directly to their printer and avoid interception
> without having to fiddle with their browser ? It is not like you will
> have random clients allowed to have POs.
>

Another good example in printing from the browser;

http://infowaters.infodynamicsconsult.com/iNFOWaters.asp

The browser-based application has "Print" and "Process" buttons. Print
means printing the 'selected' content of the HTML into a local
printer... BUT this application is design for IE only, because it
deploys ActiveX print module application to client browser. It cannot
be used in a Linux-based PC.

Thus the best way is PDF for all Windows/Linux/Mac OSs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
