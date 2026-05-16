[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help!

_1 message · 1 participant · 1999-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: Help!

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7evqb5$ln5$1@client2.news.psi.net>`
- **References:** `<7ev02e$q9h$1@wanadoo.fr>`

```
News CICOA wrote in message <7ev02e$q9h$1@wanadoo.fr>...
>I want to know how calculate the length of group data in Cobol 74.
>thanks.
>Laetitia Poulier


I hope you find this helpful:  use INSPECT ... TALLYING.  An example:

identification division.
program-id.  test-length.
data division.
working-storage section.
01 LENGTH-OF-GROUP  PIC 999 VALUE 0.
01 PACK-TABLE PIC X(8) VALUE X"012C45678C00000C".
01 GROUP-ITEM REDEFINES PACK-TABLE.
    05 FIELD1   PIC S999 COMP-3.
    05 FIELD2   PIC S9(5) COMP-3.
    05 FIELD3   PIC S9(3) COMP-3.
    05 FIELD4   PIC S9    COMP-3.
procedure division.
a.
    INSPECT GROUP-ITEM TALLYING LENGTH-OF-GROUP FOR CHARACTERS.
    DISPLAY LENGTH-OF-GROUP.
    stop run.

Tom Morrison
Liant Software Corporation
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
