[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to print a printfile in Windows

_2 messages · 2 participants · 2000-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to print a printfile in Windows

- **From:** "Fernando Kvistgaard" <fek@lr.dk>
- **Date:** 2000-12-29T13:09:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<da%26.58$dR2.2691@news.get2net.dk>`

```
I'm working with NetExpress 3.1 and Flexus Cobol ForPrint.

When I make print document I kan send it direct to the printer or to a file
if the printer is defined to print to a PRN-file.

I'm thinking to make listbox where I read all my PRN-files and from my Cobol
program to print them out  or delete them. My problem now is how to print
the files. I think this kan be done with a sort of ActiveX which I could
call from Cobol with the file name as a parameter, or may be this could be
done with an API call to winspool.drv?

Is there somebody who could help with this.

Thanks

Fernando
```

#### ↳ Re: How to print a printfile in Windows

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-12-29T12:31:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a4c82cd.35214533@news1.attglobal.net>`
- **References:** `<da%26.58$dR2.2691@news.get2net.dk>`

```
You can use a form print call to find the "names" of the printers -
then using that name use a CBL_COPY_FILE call from NetExpress to
"copy" the file to that printer.  One important thing to remember is
that you must have saved the print file as it was sent to the SAME
printer driver that you will be printing it on.  Printer specific
information is in the saved file.

On Fri, 29 Dec 2000 13:09:41 +0100, "Fernando Kvistgaard" <fek@lr.dk>
wrote:

>I'm working with NetExpress 3.1 and Flexus Cobol ForPrint.
>
…[15 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
