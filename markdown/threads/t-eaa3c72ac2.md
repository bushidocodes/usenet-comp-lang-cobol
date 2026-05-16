[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Linux/390 and Assembler

_2 messages · 2 participants · 2003-03_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Linux/390 and Assembler

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-03-13T02:31:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4Sba.38297$z54.2011621@twister.austin.rr.com>`

```
This is off topic for this group, but I figure if anyone anywhere knows, it will be someone here. :) 
I need to write assembler under Linux/390 on a mainframe that can access and use some
kind of indexed file system. 

Does anyone know of any indexed file systems that can be used under Linux/390? 
Would AcuCOBOL or MicroFocus license their filesystems for use with assembler? 
I think that C-ISAM is available under Linux/390, but I can not get anyone at IBM 
to admit to it... (*sigh*)

Any help or pointers would be greatly appreciated. 

Thanks
-Paul
```

#### ↳ Re: OT: Linux/390 and Assembler

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-13T04:14:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7004d2.242969004@news.optonline.net>`
- **References:** `<e4Sba.38297$z54.2011621@twister.austin.rr.com>`

```
"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote:

>I need to write assembler under Linux/390 on a mainframe that can access =
>and use some
…[8 more quoted lines elided]…
>to admit to it... (*sigh*)

You want VSAM, which is IBM's preferred indexed file system. It's probably
available on your Linux platform.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
