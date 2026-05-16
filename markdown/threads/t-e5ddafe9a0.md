[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# strange limitation in Microfocus COBOL

_1 message · 1 participant · 2003-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### strange limitation in Microfocus COBOL

- **From:** zatlas1@yahoo.com (zatlas1)
- **Date:** 2003-01-28T18:32:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29a6493.0301281832.74ce121a@posting.google.com>`

```
Hi
Is there any known limitation in MicroFocus COBOL so that I may not
CALL a program when this program name exceed 6 characters. Under what
circumstaces do we have this limitation and how could I circumvent it?
I use NetExpress 3.0, but I do not think this is the problem. In past
projects I used 8 characters program-name on regular basis. I believe
I have special circumstances in the current project but I do not know
what are they.
In the current project I use either PRO*COBOL Oracle precompiler or
regular COBOL with ODBC to access the Oracle database. In BOTH cases
COBOL enters the CALLed program somewhere in the middle unless I
truncate the name to 6 characters. I've noticed that the PRO*COBOL
precompiler generated CALLs almost alllways use 6 character
program-names such ad SQLADR or SQLBXE. However, somehow I do not
think that it has anything to do with the Oracle environment (and
again, if it does, how do I circumvent the problem?)
Thanks
ZA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
