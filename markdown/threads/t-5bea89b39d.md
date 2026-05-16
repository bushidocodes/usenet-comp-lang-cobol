[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help translating from S/390

_1 message · 1 participant · 2000-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Need help translating from S/390

- **From:** hancock4@bbs.cpcn.com (Lisa nor Jeff)
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89mudm$s8q@netaxs.com>`

```
The right most character is an "overpunch" for the sign field.  It's
there because the field is defined with an "S" (signed).  I presume
you're getting this via a DISPLAY statement.  If you were to print
it out using numeric edited with a sign character, it would look
correct.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
