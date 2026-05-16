[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NE 3.0 setting standard-printer

_1 message · 1 participant · 2000-12_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Re: NE 3.0 setting standard-printer

- **From:** James Gavan <jjgavan@home.com>
- **Date:** 2000-12-09T02:22:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A3197E4.63498AC1@home.com>`
- **References:** `<909jun$u0c$1@riker.addcom.de>`

```


Andreas Nehls wrote:

> Hi,
> I am working with NE 3.0 and i am used to read and set variables
…[8 more quoted lines elided]…
>

Andreas,

If you upgrade to N/E Version 3.1 you will see that PC_PRINT routines
now have the ability to set the default printer.
------------------------------------------------------------------------------------

Sets the default printer for all PC_PRINTER_ routines.

call "PC_PRINTER_DEFAULT_NAME" using by value     flags
                                     by reference printer-name
                                     returning    status-code
-------------------------------------------------------------------------------------

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
