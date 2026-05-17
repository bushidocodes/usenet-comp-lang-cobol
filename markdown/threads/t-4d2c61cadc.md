[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Debugging with NetExpress and Distributed CICS

_1 message · 1 participant · 1998-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Debugging with NetExpress and Distributed CICS

- **From:** "gene..." <ua-author-15604922@usenetarchives.gap>
- **Date:** 1998-07-16T12:52:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6olb57$l3$1@nnrp1.dejanews.com>`

```
I needed a way to debug a distributed CICS application compiled with
NetExpress the IBM Systems Center in SouthLake gave me these instructions and
they work fine. This might also be applicable for use with other
environments. What it does is allows you to start the debugger when a call
is made to a program. This could work say if you had a VB program calling a
COBOL DLL or C++ or any other mixed language or application environment. I
would be curious if anyone tries this and gets it to work with other things.

Procedure for enabling Animation of TXSeries (CICS) applications

1. Prepare CICS programs for animation using the following procedure:

cicstran dfhcmnu.ccp
cobol dfhcmnu.cbl anim initcall"CBL_DEBUGBREAK" cobidy".";
cbllink -D -V -L -Mdfhcmnu -Odfhcmnu.cbmfnt dfhcmnu.obj G:
\opt\cics\lib\cicsprCBMFNT.lib
dir dfhcmnu*

2. Check your Windows NT Services entry for the CICS region. From your
Desktop open: My Computer
==> Control Panel
==> Services
Find and double click the service entry for your CICS region
(cics. ). Make sure that CheckBoxes are enabled for:
Log On:
"As System Account"
"Allow Service to Interact with Desktop"

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
