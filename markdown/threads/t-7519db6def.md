[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Where can I get a Cobol grammar in yacc?

_3 messages · 3 participants · 1997-12_

---

### Where can I get a Cobol grammar in yacc?

- **From:** "sharad s.gumaste" <ua-author-17071775@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34848BF8.22CB7E46@asna.com>`

```

Is there a FAQ for this newsgroup that tells where I can get a Cobol
grammar in yacc?

Thanks,

--Sharad
sha··.@as··a.com
```

#### ↳ Re: Where can I get a Cobol grammar in yacc?

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7519db6def-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34848BF8.22CB7E46@asna.com>`
- **References:** `<34848BF8.22CB7E46@asna.com>`

```

Sharad S.Gumaste wrote:
›
› Is there a FAQ for this newsgroup that tells where I can get a Cobol
› grammar in yacc?

>From the news:comp.compilers FAQ:

* Where can I get a Cobol grammar in yacc?

This question is asked every few months and there has never, ever, been
any
positive response. Perhaps some of the interested people could get
together
and write one. The commercial PCYACC from Abraxas (see below) comes
with a
bunch of sample grammars including one for Cobol-85.

At http://www.netsis.it/~asantini/cobcy/ you can find a partial Cobol to
C translator with a parser that handles about half of Cobol syntax.
Half
is a lot better than none.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: Where can I get a Cobol grammar in yacc?

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-12-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7519db6def-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7519db6def-p2@usenetarchives.gap>`
- **References:** `<34848BF8.22CB7E46@asna.com> <gap-7519db6def-p2@usenetarchives.gap>`

```

In article <662rf7$8.··.@mti··t.net>,
RandallBart wrote:
› Sharad S.Gumaste wrote:
›› 
…[6 more quoted lines elided]…
› 

Siber Systems sells full Cobol grammar for 12 dialects of Cobol.

In addition to the grammar you get:
- Cobol parser (grammar plus lexer plus rpogram tree generator),
- Program Tree transformation library,
- PrettyPrinted customizable Cobol code generator.

The grammar is in BtYacc. The library is in C++.

For details take a look at http://www.siber.com/sct/

There you would find freebies such as CobolBeautifier and mf2fsc
that demonstrate Cobol parsing and transformations.

Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
