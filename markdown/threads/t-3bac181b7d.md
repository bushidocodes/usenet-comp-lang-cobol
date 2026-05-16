[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cics tdq

_1 message · 1 participant · 2006-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### cics tdq

- **From:** "seoj" <seojungmin@gmail.com>
- **Date:** 2006-02-14T16:02:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139961752.005311.284110@g47g2000cwa.googlegroups.com>`

```
This is actually a CICS question, not COBOL.  I know that this is not
the perfectly correct place to ask this, but I post this here since
this group seems to be the place that I can get answers on it.

Let's suppose, I have a dd statement in cics startup jcl,

//RDR1 DD SYSOUT=(,INRDR)
//RDR2 DD SYSOUT=Y

and I map these DDs with TDQ1, TDQ2 in my DCT.

then,

1. I try to put JCLs on RDR1 in the following way.

STEP 1) SET TDQUEUE(TDQ1) OPEN
STEP 2) WRITEQ TD QUEUE(TDQ1) FROM(SOMEJCL-BUFFER)
STEP 3) SET TDQUEUE(TDQ1) CLOSE

where SOMEJCL-BUFFER contains my whole JCL with /*EOF.

Then, I wonder when the JCL is actually put into JES. Is it after STEP2
or STEP3? (and, is it the output queue holding the JCL first and the
internal reader next?) And, if I do not do SET TDQ OPEN/CLOSE, when is
the JCL put into JES? perhaps after CICS RETURN?

2. I would like to print out some messages through RDR2 from CICS.

WRITEQ TD QUEUE(TDQ2) FROM(SOMELOG-BUFFER)

If I write TDQ using WRITEQ command, I wonder when the printer actually
prints the my messages. Is it just after WRITEQ TD or after CICS
RETURN? or any other possible command such as SET TDQUEUE, as above?

If I use SPOOLOPEN/WRITE/CLOSE, it is clear how the system behaves, but
the IBM manual is vague on this TDQ extrapartition issue. If you think
that I might have been looking at some wrong manuals, could you
recommend any material on this issue? 

Cheers, 
s
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
