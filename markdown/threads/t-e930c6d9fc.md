[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How can I Use win32 API with COBOL ?

_3 messages · 3 participants · 1997-08_

---

### How can I Use win32 API with COBOL ?

- **From:** "rafi ghazarian" <ua-author-12341671@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33F2EE6C.97F6A1A0@uci.edu>`

```

Hi all

I am fairly new to COBOL, and I do programming in C/C++ for Windows95
and I was wondering as to how can I Use win32 API with COBOL ?

Any replies are appreciated...
Rafi
```

#### ↳ Re: How can I Use win32 API with COBOL ?

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-08-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e930c6d9fc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33F2EE6C.97F6A1A0@uci.edu>`
- **References:** `<33F2EE6C.97F6A1A0@uci.edu>`

```

It is the same concept. Here is the general idea:

1.) Special Names section must have:
CALL-CONVENTION 3 IS WINAPI32

Working-storage section.
01 FOCUS-HANDLE PIC S9(4) COMP-5.

In procedure division, issue the following call
CALL WINAPI32 "GETFOCUS"
RETURNING FOCUS-HANDLE.

If the call has pointers passed to it, use BY REFERENCE, for values use BY
VALUE.
Ex.)
CALL WINAPI32 "GetWindowRect" USING
BY VALUE FOCUS-HANDLE
BY REFERENCE FOCUS-COORDS.
This will return the coords of the current focus window.
Rafi ghazarian wrote in article <33F··.@u··.edu>...
› Hi all
› 
…[6 more quoted lines elided]…
›
```

##### ↳ ↳ Re: How can I Use win32 API with COBOL ?

- **From:** "7600..." <ua-author-13442544@usenetarchives.gap>
- **Date:** 1997-08-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e930c6d9fc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e930c6d9fc-p2@usenetarchives.gap>`
- **References:** `<33F2EE6C.97F6A1A0@uci.edu> <gap-e930c6d9fc-p2@usenetarchives.gap>`

```

Note call convention 3 would work if you are pascal running in a 16 bit
Windows or OS/2 for 32 bit API in windows it should be 66 (or if LITLINK
option also required 74).



J.S. wrote in article <5t1fci$d.··.@bli··y.com>...
› It is the same concept.  Here is the general idea:
› 
…[30 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
