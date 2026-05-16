[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PIC S9(6)V99 help please

_1 message · 1 participant · 2000-03_

---

### Re: PIC S9(6)V99 help please

- **From:** glendsmith@aol.com (GlenDSmith)
- **Date:** 2000-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000301182125.03640.00002580@ng-cs1.aol.com>`

```
You mention that only 1 record has this value? Why don't you stop guessing what
the data could be and check out the complete definition which will be found in
the program. You need to know exactly which usage it is. Then you can write the
conversion routine that was mentioned. Move picin to picout etc.

More importantly with cobol records you might not even be on the right data
field. To learn how to compute exact field lengths with mixes of packed,
signed, synchronized etc, you should get yourself the cobol ref manual and
spend an evening reading the section on data formats! It may not be as simple a
problem as you seem to describe.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
