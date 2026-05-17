[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC COBOL 6.50 query

_2 messages · 2 participants · 1994-11_

---

### PC COBOL 6.50 query

- **From:** "schow" <ua-author-11601651@usenetarchives.gap>
- **Date:** 1994-11-28T22:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3be68c$51n@news.tamu.edu>`

```
I have been able to compile some of the demo code included with the
PC COBOL package, and it seems to generate a .OBJ file and a text file
with the code numbered by line.

OK, but what's next? The documentation says something about LINKing
and creating a .EXE file, but there's no such LINK command. Any clues
or advice would be appreciated, thanks!
```

#### ↳ Re: PC COBOL 6.50 query

- **From:** "stae..." <ua-author-5439109@usenetarchives.gap>
- **Date:** 1994-11-29T06:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6eed63a6e6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3be68c$51n@news.tamu.edu>`
- **References:** `<3be68c$51n@news.tamu.edu>`

```
In article <3be68c$5.··.@new··u.edu>, schow@PROBLEM_WITH_INEWS_DOMAIN_FILE (Steve Schowiak) says:
› 
› I have been able to compile some of the demo code included with the
…[6 more quoted lines elided]…
› 

The following is from the faq for this group:

How do I link my objects ?

There is no linker with the COBOL 6.50 compiler. To link objects you need to use the linker from
MS-DOS v3.3 or earlier.

Ralf Laemmel adds :

You can use newer linkers, especially from newer Microsoft compiler products, too.

And Peter Mikalajunas has found that :

Tlink compiled with obj files without complaint, but the exe's were useless. What did
work was Link version 5.31.009 which comes with Visual Basic for DOS. It compiled
all obj files I tried and the exe's ran perfectly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
