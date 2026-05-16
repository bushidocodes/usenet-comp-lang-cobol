[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 4.2 - Print to a dot matrix printer

_2 messages · 2 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu 4.2 - Print to a dot matrix printer

- **From:** <answer1@ibm.net>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374aea5d@news.uk.ibm.net>`

```
Hi out there,

I would like to use a dot matrix printer in a project.

I develop a commercial program for a client.
In that kind of program there is a lot of output to a printer.
I use PowerForm to create the form of a list. I write the code as it is in
the manual.
I compile it . All is ok.
When I run it I have ... a page of graphics and 5 minutes of printing (may
be more).

I rewrite the program wirhout the PowerForm's help in plain COBOL.
When I run it I have ... very small graphics (again ?) and about the same
time of printing.

So far my default printer was "IBM Proprinter III" ,  I changed the default
printer to "Generic/Text only" the result was that the two versions of my
program don't work.

The questions that I want to make are ,
- CAN we print ascii characters to a dot matrix printer using or not using
PowerForm ?
- Can we print invoices with Fujitsu PowerCobol to a dot matrix printer ?
- It is better to return to DOS and use RmCobol or something else ?


Thanks , in advance
Dimitris Kostoulas
answer1@ibm.net
```

#### ↳ Re: Fujitsu 4.2 - Print to a dot matrix printer

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-g2N9dk2d9MWD@Dwight_Miller.iix.com>`
- **References:** `<374aea5d@news.uk.ibm.net>`

```
The only ways I know of to hande this are to write to a file then use 
bytestream routines to send to the printer, or to use COBOL FormPrint 
from Flexus, which DOES support generic text printers.



On Tue, 25 May 1999 18:48:54, <answer1@ibm.net> wrote:

> Hi out there,
> 
…[29 more quoted lines elided]…
> 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
