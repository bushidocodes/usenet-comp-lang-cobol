[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Re-indexing files

_1 message · 1 participant · 1996-04_

---

### Re-indexing files

- **From:** "steve..." <ua-author-6079829@usenetarchives.gap>
- **Date:** 1996-04-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<000027BC00001893@nashville.com>`

```
M> Using the rmcobol compiler for pc (education restricted) I am wondering
M> how (if at all), once I delete a record, I can replace the deleted key
M> field with a new record.
M>


I use RMCobol for Unix, and when you logically delete a record from a file,
whether it be RELATIVE or INDEXED (I assume as much, as you refer to using
a key) you can now WRITE a new record using the previous key. Otherwise,
you must use the REWRITE statement.

Hope this helps.
Stevo
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
