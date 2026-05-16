[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can CA7 scheduler submit a job in my ID?

_1 message · 1 participant · 2002-11_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### Can CA7 scheduler submit a job in my ID?

- **From:** arunprasath420@yahoo.com (Arun Prasath)
- **Date:** 2002-11-17T08:37:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3ef804e.0211170837.2c90650d@posting.google.com>`

```
Hi all,

Every week I run a few JCLs jobs which inturn produce new JCLs from
templates. These new JCLs update some information about our system
into DB2 tables. The original jobs I run each week are the same, but
the new JCLs are different each week in numbers and content, depending
on the information to be loaded into the DB2 tables.

I currently run all these jobs through my maniframe ID. Inorder to run
the new JCLs produced automatically, I have a REXX program which
attaches a stub at the end of the new JCLs, so that when one JCL
finishes running, it submits the next one inline usign REXX code.

//JOBCARD NEW JCL1
//STEP1
//STEP1
//STEP3
//NEW JCL1's code ends here
//*
//STUB (REXX code which submits the next NEW JCL, in IKJEFT01
environment)

I use 'TSO SUBMIT' in the REXX code to submit the next JCL.

I now need to to schedule these jobs in CA7. I can schedule the
original JCLs, but am not sure how to schedule the dynamically
produced NEW JCLs.

One way I thought of is to schedule the triggering JCL (which is the
STUB itself that submits the first job in the sequence)in CA7 and when
this JCL submits the first NEW JCL, it submits this job in my TSOID,
so that from then on, it looks like the jobs run in my TSOID.

Is this feasible, ie; can CA7 submit a job in my TSOID? instead of
USER=CA7?

Thanks in advance,
Arun Prasath
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
