[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: How do I convert������������������

_1 message · 1 participant · 1994-12_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Q: How do I convert������������������

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-02T10:14:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bndk2$rsl@gnat.cs.nyu.edu>`
- **References:** `<89E83EA.09D20000AF.uuout@almac.co.uk> <Czyz28.Gpu@metronet.com> <3bgte5$4ke@powergrid.electriciti.com>`

```
Lawrence, are you saying that:

> : LG> 01  WS-AREA.
> : LG>     05  WS-ALPHA  PIC X(07)  VALUE '67.2503'.
> : LG>     05  WS-ALPHA-9  REDEFINES WS-ALPHA
> : LG>                   PIC 99V9999.

worked and did something reasonable, because if so, the COBOL compiler
on which it did something useful was very seriously broken. As is clear
from the above code, you are overlaying a 7 character field with a 6
character numeric field, and the data in WS-ALPHA-9 is definitely invalid,
since it contains the non-numeric character . as the first digit after the
decimal point. Remember that V's are implied decimal points, they do not
take up space in the picture.

So (a), I have no idea what (incorrect) thought behind the above code is
and (b) is it absolutely clear that with a correctly functioning COBOL
compiler, this code cannot possibly be useful.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
