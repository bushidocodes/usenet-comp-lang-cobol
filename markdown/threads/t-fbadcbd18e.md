[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# USAGE POINTER at the group level

_1 message · 1 participant · 2002-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### USAGE POINTER at the group level

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-20T20:17:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2fu0j$fsj$1@slb3.atl.mindspring.net>`

```
This has NOTHING to do with

 A) USAGE INDEX at the group level (allowed - I think - in both '85 Standard
and draft Standards)
 B) What various vendors will/do allow (as extensions)

BUT the draft of the next COBOL Standard (aka PROBABLY 2002) has an explicit
rule that says,

"13) A USAGE clause with the OBJECT REFERENCE, POINTER, or PROGRAM-POINTER
phrase may be specified only for an elementary data item with level 1 or
subordinate to a type declaration that includes the STRONG phrase."

(See page 370 of the December draft).

Therefore, *both*

 01 aGroup Pointer.
    05  Ptr1 Usage Pointer.

*and*

01 aGroup Pointer.
   05 Ptr1.


will be "non-conforming" in the next Standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
