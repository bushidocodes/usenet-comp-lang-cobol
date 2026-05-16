[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How access a object COM (DLL) with Cobol

_2 messages · 2 participants · 2001-08_

---

### How access a object COM (DLL) with Cobol

- **From:** "PorTy" <euromercante1@clix.pt>
- **Date:** 2001-08-17T09:39:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uM4f7.16441$XR2.48120982@newsserver.ip.pt>`

```
Hi all,

    I'm having problems accessing a COM object with Fujitsu Cobol or Power
Cobol V6.
    My knowledges of OOCobol  are minimum.
    The COM object that I'm trying to access is a DLL, made in Visual Basic.
This DLL is a class with sub-classes, methods and properties.
    With " Late Binding" gives me no errors accessing the DLL, but the
problems arises when I have to use/access methods or properties. With "
Early Binding" the problems starts on the access of the DLL.
    From what I've been reading, it seems that the " Early Binding" is the
better and easy way to access this DLL.
    If anyone have examples of accessing this kind of COM object, please
send me.

With best regards
```

#### ↳ Re: How access a object COM (DLL) with Cobol

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-08-17T17:36:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iCcf7.5092$2u.50630@www.newsranger.com>`
- **References:** `<uM4f7.16441$XR2.48120982@newsserver.ip.pt>`

```
If it's a "control" you could drop it on a PowerCOBOL form and access it that
way.

If it's just an automation server, use the OLE- calls to access it.  Look at the
Fujitsu samples - specifically Sample17 in the Samples folder under the COBOL
folder of the install.

If you are a COBOL sp2 user you can use the Flexus ActiveX add on if this is a
control and not just a server.

In article <uM4f7.16441$XR2.48120982@newsserver.ip.pt>, PorTy says...
>
>Hi all,
…[20 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
