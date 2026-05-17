[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 74 vs COBOL 85

_3 messages · 3 participants · 1997-02 → 1997-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL 74 vs COBOL 85

- **From:** "j����rgen defurne" <ua-author-17071894@usenetarchives.gap>
- **Date:** 1997-02-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<330EDAF7.36F8@glo.be>`

```

Hello, everybody,

Since a few weeks I am working as programmer/analyst on a WANG VS
system, using the PACE development environment, supported by COBOL 74.
I am experienced with a few languages (Clipper, Foxpro, C++, Siemens
Step-5) in several environments (administrative, technical,
industrial). This made that I hadn't much trouble learning COBOL 74.

Unfortunately, I miss some features of modern programming languages
which make for smaller and better maintainable programs
- real parameter passing, not just for subprograms, but also for
procedures
- local variables
- functions

That's what my question is about : PACE also supports COBOL 85. I would
like to know :
- how does COBOL 85 compare to COBOL 74 in general ?
- how does it compare concerning the above points ?
- would changing from COBOL 74 to COBOL 85 help with the problem that
the "ACCEPT FROM DATE" statement only returns a format of
the form "YYMMDD" instead of "YYYYMMDD" or does this depend only on the
environment in which the compiler is used ?

I searched the web and usenet for some useful information, but all I
found were mostly advertisements from the compiler builders and computer
companies. I also found two nice articles, which gave me another reason
why COBOL can be learned relatively quick : it's a language to build
applications, and indeed the need not to find standard functions (like
in C/C++) makes quite a difference.

All replies and further questions are welcome.

Jurgen Defurne
Flanders - Belgium
```

#### ↳ Re: COBOL 74 vs COBOL 85

- **From:** "sma..." <ua-author-6589691@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d0abf17f2d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<330EDAF7.36F8@glo.be>`
- **References:** `<330EDAF7.36F8@glo.be>`

```

Jï¿½rgen Defurne wrote:
› 
› Hello, everybody,
…[3 more quoted lines elided]…
› - real parameter passing, not just for subprograms, but also for
you can define entryï¿½s in COBOL 85.
An entry can have a local storage section (even recursion is
possible) an has real parameter parsing.
In fact it is an subprogramm defined in the same source file;
s.a. OO-Cobol where you can define methods with all the above
features

› procedures
› - local variables
…[9 more quoted lines elided]…
› environment in which the compiler is used ?
in MF >= 3.3.50 you can set a switch to control above behaviour
```

#### ↳ Re: COBOL 74 vs COBOL 85

- **From:** "luis a. espinal" <ua-author-12404825@usenetarchives.gap>
- **Date:** 1997-03-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d0abf17f2d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<330EDAF7.36F8@glo.be>`
- **References:** `<330EDAF7.36F8@glo.be>`

```

› I also found two nice articles, which gave me another reason
› why COBOL can be learned relatively quick : it's a language to build
› applications
 
› Jurgen,
Sorry I can't help you with your question; I'm on the same boat learning
COBOL. The two articles that you mention, are they on the Internet? If
so, where so that I can get them?
Thanks.
Luis Espinal
Luis++ = ( les··.@sol··u.edu XOR 
	   lui··.@arm··e.com );
What does not kill us makes us stronger
...abort, retry, ignore ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
