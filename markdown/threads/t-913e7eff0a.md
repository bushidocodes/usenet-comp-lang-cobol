[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cbllink produces a ?-sign

_1 message · 1 participant · 1999-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### cbllink produces a ?-sign

- **From:** dnalor@my-deja.com
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qe1hl$m64$1@nnrp1.deja.com>`

```
Hi!
I should use lots of DLL-Functions. Unfortunately, cbllink produces all
exported functions with a leading "?". This happens, when porting from
16 to 32bit. Exactly: it happens if the function starts witjh an
underscore, as 16bit compilers required it.
eg.:
old function:  _func @24
new function:  ?_func @24

how can I avoid this?
Thanks a lot!
Roland.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
