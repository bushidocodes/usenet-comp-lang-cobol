[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMTI, CICS, DB2, and ROLLBACK Problems

_1 message · 1 participant · 2001-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### COMTI, CICS, DB2, and ROLLBACK Problems

- **From:** crewschuck@russellcorp.com (Chuck Crews)
- **Date:** 2001-12-31T05:24:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1a743e05.0112310524.2debca01@posting.google.com>`

```
Here is my structure:

COMTI
   program A
      link to program B
      link to program C
      line to program D

If I encounter an error anywhere during the processing of program A, I
issue a syncpoint rollback.    However, we have found that the
syncpoint rollback sometimes fails (i.e. gets a CICS error when
executing) resulting (generally) in an ADPL error.

2 questions:

Is this a sync level 2 problem (like maybe I am not at sync level 2)?
If the CICS rollback fails, does the actual DB2 rollback still occur
and I am just receiving a bad CICS return code?

If the rollback still does occur then I am OK and I can just make sure
my error handling is proper and proceed.

Has anyone had similar experiences.

Chuck Crews
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
