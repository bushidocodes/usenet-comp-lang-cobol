[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Grammar for scanners

_3 messages · 3 participants · 2000-01_

---

### Cobol Grammar for scanners

- **From:** "Antonello Genuario" <antogenuario@libero.it>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8AWf4.2951$D3.36138@news.infostrada.it>`

```
Does anybody knows if exist a cobol grammar definition per scanners like
YACC for free? Please help me to find it.
```

#### ↳ Re: Cobol Grammar for scanners

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85poo8$26jq$1@news.hitter.net>`
- **References:** `<8AWf4.2951$D3.36138@news.infostrada.it>`

```

Antonello Genuario wrote in message
<8AWf4.2951$D3.36138@news.infostrada.it>...
>Does anybody knows if exist a cobol grammar definition per scanners like
>YACC for free? Please help me to find it.


Try < http://www.netsis.it/~asantini/cobcy > first.

If you are unable to access the above site, go to
< http://www.angelfire.com/ar/CompiladoresUCSE/COMPILERS.html >.
Locate COBOL in the section on yacc and download COBOL.zip.
-----------------
Rick Smith
```

#### ↳ Re: Cobol Grammar for scanners

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38807849.786BAFC8@zip.com.au>`
- **References:** `<8AWf4.2951$D3.36138@news.infostrada.it>`

```
Antonello Genuario wrote:
> 
> Does anybody knows if exist a cobol grammar definition per scanners like
> YACC for free? Please help me to find it.

I started one in cobol, full source.   It is very rough and only
really handles the working storage at this time.  Download parser from
my web page.

It tokenises the whole thing based on a keyword list and known working
storage variables.

Needs:  Copybook handling
	Procedure division mapping (lot of work).

If you are interested in working on it, it is public domain so go for
your life.  If you make any corrections / extensions let me know.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
