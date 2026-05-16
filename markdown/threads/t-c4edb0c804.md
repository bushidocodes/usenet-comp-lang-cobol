[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# open dialog in acu cobol

_2 messages · 1 participant · 2008-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### open dialog in acu cobol

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-08-04T01:00:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10d66371-86d1-4424-aace-05a2bc37774f@79g2000hsk.googlegroups.com>`

```
Hi i´m using acuBench 7 and i´m looking for a nice solution to let the
user choose a file to import in my database,
is there anything that starts the "small" version of Windows Explorer
as known in all other applications ...  file-open choose by clicking

thanks a lot
mario
```

#### ↳ Re: open dialog in acu cobol

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-08-04T02:24:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fe0a95e-69a2-45f3-971c-00676a1556af@25g2000hsx.googlegroups.com>`
- **References:** `<10d66371-86d1-4424-aace-05a2bc37774f@79g2000hsk.googlegroups.com>`

```
for those who have the same problem,
i´ve done it with

 INITIALIZE OPENSAVE-DATA
           MOVE
              "Tab files (*.tab)|*.tab|All files (*.*)|*.*"
              TO OPNSAV-FILTERS
           MOVE "tab" TO OPNSAV-DEFAULT-EXT
           CALL "C$OPENSAVEBOX" USING OPENSAVE-SAVE-BOX,
                                 OPENSAVE-DATA
                           GIVING OPENSAVE-STATUS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
