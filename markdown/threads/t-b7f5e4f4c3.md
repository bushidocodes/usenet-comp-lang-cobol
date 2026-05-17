[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linking MF3.2.50 DOS application for windows

_2 messages · 2 participants · 1998-03_

---

### Linking MF3.2.50 DOS application for windows

- **From:** "sou..." <ua-author-877625@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998032018562700.NAA10087@ladder01.news.aol.com>`

```

I am trying to link an existing shared run-time program to run under windows.
The examples in the manual are pretty clear but I keep getting link errors.
Any suggestions would be helpful.

The problem I am trying to solve with the windows version is:

windows95 will not print my print files to many of the new windows only
printers.

Any suggestions on another way to solve this problem would also be greatly
appreciated.


Steve Campbell
Sou··.@a··.com
```

#### ↳ Re: Linking MF3.2.50 DOS application for windows

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7f5e4f4c3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998032018562700.NAA10087@ladder01.news.aol.com>`
- **References:** `<1998032018562700.NAA10087@ladder01.news.aol.com>`

```

Soups7 wrote:
› 
› I am trying to link an existing shared run-time program to run under windows.
…[12 more quoted lines elided]…
› Sou··.@a··.com

Steve, are you the Steve Campbell that I know?

That aside, you mentioned shared RTS which makes me think Micro Focus.
To get WIN printers to work you need to use the PC_WIN_PRINT calls in
Micro Focus or get a tool like Form Print from http://www.flexus.com.
Anyway, the "Win" printers - oxymoron for sure - won't print from DOS or
any print device that looks like DOS (ie LPT1, PRN, LIST, PRINTER, etc).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
