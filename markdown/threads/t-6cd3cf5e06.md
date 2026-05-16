[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing from MF NetExpress COBOL

_2 messages · 2 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Printing from MF NetExpress COBOL

- **From:** philhickling@my-dejanews.com
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g1pu7$ao5$1@nnrp1.dejanews.com>`

```
I am having problems printing control characters from MicroFocus NetExpress.
In the past I have successfully sent control characters to the printer, to
switch bold, underlining on/off, to change fonts, etc.  This works with using
files defined ASSIGN TO PRINTER, but does not work using the command
PC_PRINTER_WRITE, nor PC_PRINT_FILE.

According to MF Support, I have a problem with the printer driver in between
my COBOL aplication and the printer.  Can anyone tell me more, or suggest
what I should do?  Please.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Printing from MF NetExpress COBOL

- **From:** smayer@t-online.de (Sebastian Mayer)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3724EF19.7FF3BFD0@t-online.de>`
- **References:** `<7g1pu7$ao5$1@nnrp1.dejanews.com>`

```


philhickling@my-dejanews.com schrieb:
> 
> I am having problems printing control characters from MicroFocus NetExpress.
…[8 more quoted lines elided]…
> 

as far as I know, the "PC_PRINTER..."-Routines are calling winapi
functions. I think, that PC_PRINTER_WRITE calls the textout routine
which can only print text. If you like to use bold you must call the
equivalent winapi routine or more easy "PC_PRINTER_SET_FONT"

regards 
Sebastian
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
