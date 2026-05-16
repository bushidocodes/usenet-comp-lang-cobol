[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using COMREG to get date

_1 message · 1 participant · 1999-08_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### RE: Using COMREG to get date

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-08-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90491CB93918D21189BD00805FBE300B014E2F46@voyager.okc.disa.mil>`

```
I would have thought that you would need to insure the "POINT-COMREG" was at
least initialized to low values.  Isn't the comreg decimal 20 bytes off of
low core?


snip

000210 WORKING-STORAGE SECTION.
000220
000230 01  PAGE-ZERO.
000240     03                           PIC X(20).
000250     03  POINT-COMREG             USAGE POINTER.
000260

snip

000340 LINKAGE SECTION.
000350
000360 01  COMREG.
000370     03  CURRENT-DATE.
000380         05  CURRENT-DATE-MM PIC XX.

snip

000600 PROCEDURE DIVISION.
000610 MAINLINE.
000620          SET ADDRESS OF COMREG TO POINT-COMREG.
000630          MOVE  CURRENT-DATE TO WS-CURRENT-DATE

snip



 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
