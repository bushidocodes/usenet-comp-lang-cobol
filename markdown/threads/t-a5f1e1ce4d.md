[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Umstellung COBOL 74 -> COBOL 85 hier COMP-3 Felder

_1 message · 1 participant · 1999-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Re: Umstellung COBOL 74 -> COBOL 85 hier COMP-3 Felder

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37a6e05c@news3.us.ibm.net>`
- **References:** `<7o6bro$eld$1@news08.btx.dtag.de>`

```

Joachim Nacke <rewe.dortmund.nacke@t-online.de> wrote in message > Diese
sind wie folgt definiert:
>     02 FELD-X    PIC S9(5) COMP-3 VALUE ZERO.
> Zur Laufzeit hat dieses Feld den Inhalt "4040404040" und bekommt einen
DATA
> EXCEPTION.
> Kann mir jemand sagen, wie dieser Wert in ein gepacktes Feld kommt und wie
> man dies verhindern kann?

FELD-X is part of a larger structure (because of its level 02). If you move
spaces
to that structure you have the result you describe, e.g.:
01  BIG-FIELD.
    02  FIELD-1      PIC X(25).
    02  FELD-X      PIC S9(5) COMP-3 VALUE ZERO.
    02  FIELD-3      PIC X(10).

MOVE SPACES TO BIG-FIELD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
