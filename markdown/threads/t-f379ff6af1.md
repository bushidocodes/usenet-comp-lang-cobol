[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call Micro Focus Cobol from C++

_3 messages · 3 participants · 1997-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Call Micro Focus Cobol from C++

- **From:** "helmut glitza" <ua-author-17071502@usenetarchives.gap>
- **Date:** 1997-07-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33C47AF8.50C8@cww.de>`

```

Call Micro Focus Cobol from C++

I wand to call some Cobol subprograms from my Dialog in Windows NT.
Cobol: MVS Workbench
C: MS Visual C++ 4.0

On start the Application is missing the CBLSSEG.DLL.
Where can I get this Library.
```

#### ↳ Re: Call Micro Focus Cobol from C++

- **From:** "john reynaert" <ua-author-7876551@usenetarchives.gap>
- **Date:** 1997-07-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f379ff6af1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33C47AF8.50C8@cww.de>`
- **References:** `<33C47AF8.50C8@cww.de>`

```

You did not say which version of Workbench..
I checked on my system
This file exists in my WB 3.2.xx directories
but not in my WB4.0 directory
copy also exists in windows system directory
don't know which install puts in there though...
should be part of the install

maybe you need to run the install and select the
C stuff ???

John

Helmut Glitza wrote in article <33C··.@c··.de>...
› Call Micro Focus Cobol from C++
› 
…[6 more quoted lines elided]…
›
```

#### ↳ Re: Call Micro Focus Cobol from C++

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f379ff6af1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33C47AF8.50C8@cww.de>`
- **References:** `<33C47AF8.50C8@cww.de>`

```

Helmut Glitza wrote:
› 
› Call Micro Focus Cobol from C++
…[6 more quoted lines elided]…
› Where can I get this Library.


It is part of MF Cobol RTS.. that is.. this DLL (and others) must be
loaded when you want to execute some COBOL code from your C/C++
program...

You have to link your COBOL prog. correctly (this depends on which
version of the MF compiler you have.. You must always state such vital
info if you want help!!!) and you must set the MF RTS environment from
your C/C++ program before accessing COBOL..
It is fairly easy using Win API's
LoadLibray/GetProcAddress/SetEnvironment...


Geir Knaplund
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
