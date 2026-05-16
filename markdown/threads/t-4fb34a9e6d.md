[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rules Base processing for DB2

_1 message · 1 participant · 2003-02_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Rules Base processing for DB2

- **From:** jvrad@yahoo.com (Jim V)
- **Date:** 2003-02-05T12:23:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f3eaa9c.0302051223.614808b5@posting.google.com>`

```
I am looking for suggestions and/or recommendations on the concept of
rules based processing for a loan guarantee system operating on OS 390
with Cobol and DB2.

We have several edits that are coded in various subprograms with a
single edits driver.  We want to take some or all of these edits and
create rules based processing whereby these edits can be turned on and
off for different lenders.

My initial thought is to create a lender/edit table containin the
lender and all possible edits.  The edits could be turned on and off
by the business partners.  I would use this table to determine what
edits are performed based on the lender in batch processing.

We are trying to avoid excessive I/O and may want to read the table
once and pass the various edit rules to their respective subprograms.

Please responde with any thoughts.  Thanks - Jim
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
