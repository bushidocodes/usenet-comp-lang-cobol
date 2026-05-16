[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# eliminating carriage returns from a file

_1 message · 1 participant · 1998-09_

---

### Re: eliminating carriage returns from a file

- **From:** trblshtr@my-dejanews.com
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sooo4$j71$1@nnrp1.dejanews.com>`

```
awk 'BEGIN{RS="\r";ORS=""}{print}' infile > outfile

:-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
