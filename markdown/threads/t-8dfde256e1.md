[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bad Performance with MfCobol DLL & Vb3

_1 message · 1 participant · 1997-10_

---

### Bad Performance with MfCobol DLL & Vb3

- **From:** "pri..." <ua-author-17072105@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<612c6g$m8@everest.vol.it>`

```

Hello to all Cobol friends, :-)

We are converting some Cobol programs from Dos to DLL & VB using
MFCobol (Version 3.1.31) with VB3 (16bit)

One routine Start and Read Next nolock some 5000 records from a
standard
ISAM database.
However, there are some problems regarding performance. The same
routine
under DOS takes 17 seconds, the same code placed in a MFCobol DLL +
VB3 takes 47 seconds, the same application (16bit) under Windows 95,
takes 10 seconds !!

The Dll is compiled and linked as follows:

cobol %1 optspeed target(386) deffile deffiletype(windows) dll
litlink;

link %1+extfh+mfreused+libinit+cblwinl,%1.DLL,,lcobolw
+lcobol+cobw31,%1.def /nod /noe;

Can you suggest something, in order to get better performaces ?

Thank you very much in advance. 8-)

Ugo , Italy
E-Mail: pri··.@gp··t.it
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
