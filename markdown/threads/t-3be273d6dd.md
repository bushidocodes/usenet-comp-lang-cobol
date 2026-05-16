[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help, please

_1 message · 1 participant · 1994-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: Help, please

- **From:** walterm@hprctbs3.rose.hp.com (Walter Murray)
- **Date:** 1994-12-01T18:56:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bl693$slk@hpchase.rose.hp.com>`
- **References:** `<D03DLr.CA7@bfsec.bt.co.uk>`

```
PaulGordon wrote:
: I have a six bit field  that is passed to me as a variable with 
: a PICTURE clause of PIC X. I want to convert this six 
: bit field into a 2 digit number ( 2^6 = 64 so it can't be bigger
: than two digits). How would this be done ?

I'd suggest the standard COBOL function ORD.

      01  BIT-FIELD         PIC X.
      01  NUMERIC-VALUE     PIC 99.

      COMPUTE NUMERIC-VALUE = FUNCTION ORD (BIT-FIELD) - 1

Walter
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
