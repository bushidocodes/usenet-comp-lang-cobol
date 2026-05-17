[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Binary Numbers in Vax Cobol

_1 message · 1 participant · 1996-09_

---

### Binary Numbers in Vax Cobol

- **From:** "alan r. johns" <ua-author-16792362@usenetarchives.gap>
- **Date:** 1996-09-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bba66a$ae67c100$060a8586@a_johns.cts.comsat.com>`

```


I use Cobol on a Vax 4106a running VMS 6.2.

If anyone has ever used Cobol to call the Runtime Library function
GETQUI to determine a queue status, then you know that it can return
multiple status codes in one unsigned longword number. You
determine the status of the queue by checking which bits are
set. For example: If the longword is 6, then you know bits 2 & 4
are set. This means the queue is idle(2) and it can handle lowercase(4)
jobs.

My question is: What is the simplest way to convert a longword
number to a binary value where I can check specified bits?

Thanks,

-Alan (joh··.@c··.net)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
