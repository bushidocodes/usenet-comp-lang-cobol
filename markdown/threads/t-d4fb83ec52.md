[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help need with RTS problem.......MF COBOL TOOLSET

_2 messages · 2 participants · 1996-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help need with RTS problem.......MF COBOL TOOLSET

- **From:** "nssi..." <ua-author-17086348@usenetarchives.gap>
- **Date:** 1996-05-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oi8um$378@newsbf02.news.aol.com>`

```

Is there anyone out there who could help me with a Link problem I have.
I am using Micro Focus Cobol Toolset 3.2.43 on a P-100 windows-95
machine.

I have Main which calls SubA and SubB. SubA in turn calls and cancels
SubC.

SubA sorts a file; SubB is an Index File Inquiry Prog and SubC updates
an ISAM file; the same index file Main opens. I have a reference file with
the adis routines called adis.rsp

Its a medium sized DOS based application and therefore I linked it using
the LCOBOL run-time system with
link/nod main +subA+subB +subC+@adis.rsp,,,lcobol+cobapi

The entire program works just fine while I am in the COBOL rts but
gives me Run time library not found when ported to distination.

I have written and produced quite a number of simple programs with the
same LCOBOL rts and not had this problem; however, in the past, I did not
have subs to my main program. What am I doing wrong?

Your help is greatly appreciated.

Thank you...

Cynthia
```

#### ↳ Re: Help need with RTS problem.......MF COBOL TOOLSET

- **From:** "ferr..." <ua-author-17086290@usenetarchives.gap>
- **Date:** 1996-05-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d4fb83ec52-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4oi8um$378@newsbf02.news.aol.com>`
- **References:** `<4oi8um$378@newsbf02.news.aol.com>`

```

In article <4oi8um$3.··.@new··l.com>, nss··.@a··.com
says...
› 
› Its a medium sized DOS based application and therefore I linked it 
…[6 more quoted lines elided]…
› 


If your program is linked using adis, you must also
distribute a copy of the file ADISCTRL, which sets the
parameters for accept/display statements. When you run
the program on your main system, the file is already in
your PATH. When you distribute the program without ADISCTRL,
adis can't run without a setup file.

don
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
