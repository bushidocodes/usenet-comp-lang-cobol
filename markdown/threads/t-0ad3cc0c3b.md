[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using embedded SQL in a DLL in MF-VISOC 95 - Help!

_2 messages · 2 participants · 1997-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Using embedded SQL in a DLL in MF-VISOC 95 - Help!

- **From:** "barry carr" <ua-author-8101214@usenetarchives.gap>
- **Date:** 1997-05-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc5cc4$7e217ac0$a60e0923@kids>`

```

Hello,

I'm trying to call a DLL which uses embedded SQL. However, I get a error
'200' internal logic error when the DLL tries to connect to, or access the
ODBC database. The process works fine in animation. (But, of course, I'm
not executing a DLL at that point.) Does anyone know of some limitations
of DLL's created using MF-Visual Object COBOL for Windows 95? File access
out of DLL's seems to be a problem in general.

Any help, or explanation would be appreciated.

I'm running version 1.00.28 (Current according to WebSync) under NT 4.0.

Barry Carr
car··.@pil··u.edu
```

#### ↳ Re: Using embedded SQL in a DLL in MF-VISOC 95 - Help!

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1997-05-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad3cc0c3b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5cc4$7e217ac0$a60e0923@kids>`
- **References:** `<01bc5cc4$7e217ac0$a60e0923@kids>`

```

Barry Carr wrote:
› 
› Hello,
…[13 more quoted lines elided]…
› car··.@pil··u.edu

Are you linking in the file handler routines? Or if dynamic link, are
the libraries in a place where the run time can find them? If you create
a map at link time you should be able to determine which dlls you
need...

just a guess


Computer Programming Unlimited, Inc. (CPU, Inc.)

Return Address: cpu··.@spr··t.com

Solicitations to me must be pre-approved in writing by me after
soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this notice and will send
a certified check forthwith.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
