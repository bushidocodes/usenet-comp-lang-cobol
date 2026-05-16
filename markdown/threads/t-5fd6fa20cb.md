[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing sysout messages to specified DD

_1 message · 1 participant · 2004-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Writing sysout messages to specified DD

- **From:** sumit.sengupta@gmail.com (summit)
- **Date:** 2004-12-19T13:02:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e18daabc.0412191302.696213b8@posting.google.com>`

```
Hi,

  I have got a common C module running on OS/390 , which will write to
separate DD SYSOUT files (for different programmes).

We have setup separate DDs for each transaction/programmes 
(for ex:
//PROGAOUT  DD DISP=SHR,DSN= MVSSYS.SUMMIT.OUTPUTA defined in the
startup job of the WLM) , so that the common C module will write to
those SYSOUT DDs depending on whatever DD name is passed into it.

The module is running in the WLM of DB2 . 

Question is, once the DDs have been setup by the system programmers,
how do I write to each DD ? i.e. Can i just issue a
fopen("DD:PROGAOUT","a+") , which will do the trick?

Please note that each caller to this C programme will pass in the DD
name (PROGAOUT in this case).

Please advise.

Summit
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
