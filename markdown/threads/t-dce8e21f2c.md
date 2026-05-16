[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Modify Word Docvariables with Cobol

_2 messages · 2 participants · 2002-01_

---

### Modify Word Docvariables with Cobol

- **From:** "Thomas H���rkens" <thoerkens@rsw-orga.de>
- **Date:** 2002-01-08T09:00:45+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ev8e1a.iho.ln@gw1.rsw-orga.de>`

```
Hello,

i try to modify a Word-Document out of my Cobol-Program. The Application
Word is running and i have open a document. Now I want change some
Docvariables within the Document. Have someone an idea to solve the problem
or have someone an example source code?

I work with the AcuBench 5.2 from ACUCORP

Thanks for your help

Thomas
```

#### ↳ Modify Word Docvariables with Cobol

- **From:** Gisle Forseth <GForseth@acucorp.com>
- **Date:** 2002-01-08T23:57:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9332A1B4B5CED2119FCE00105AD16A4D41725C@hubcap.acucorp.com>`
- **References:** `<ev8e1a.iho.ln@gw1.rsw-orga.de>`

```
Here is a sample of print preview.

       print-preview.
      * Create "Word.Application" object
             create @Application of @Word
                 handle in word-app.

      * Make Word invisible
             modify word-app @Visible = 0.

      * Open file
             modify word-app @Documents::Open(filename,0,1)
                 giving word-doc.

      * Print Preview
             modify word-doc @PrintPreview().
             modify word-app @Visible = 1.

      * Destroy the objects
           destroy word-doc.
           destroy word-app.

Gisle

> From: Thomas H�rkens [mailto:thoerkens@rsw-orga.de]
> Posted At: 8. januar 2002 09:01
…[20 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
