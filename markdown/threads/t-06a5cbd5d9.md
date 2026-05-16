[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How transfer from recorded data in Cobol to another application.

_2 messages · 2 participants · 1998-10_

---

### How transfer from recorded data in Cobol to another application.

- **From:** "JAHF" <dcsa@cma.ulpgc.es>
- **Date:** 1998-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362f9f2c.0@noticias.ulpgc.es>`

```
Hello to all. I need your help.



I am doing a new application for my enterprise to substitute the previous
one, done in cobol. And we need to transfer the recorded data of the old
application (cobol) to the new one (dbase).

I have the description of the fields but it is impossible  to read well the
data because the length of every field doesn't correspond with the length
specified in the definition.

Please I would like to receive veritable information about how doing a
transfer of information from one application to another one.

Thank you at all.

With regards,



C. If you know Spanish, it would be better but not a problem.
```

#### ↳ Re: How transfer from recorded data in Cobol to another application.

- **From:** Scott McKellar <mck9@swbell.net>
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36306644.55A4@swbell.net>`
- **References:** `<362f9f2c.0@noticias.ulpgc.es>`

```
JAHF wrote:
> 
> Hello to all. I need your help.
…[10 more quoted lines elided]…
> transfer of information from one application to another one.

We need to know more about the kind of COBOL which produced the files,
and perhaps how the application was coded.  For example:

When MicroFocus COBOL writes line sequential files which contain binary
data, it adds nul bytes (binary zeros) in front of bytes with values
less than hex 20.  It also removes trailing blanks, and gives special
treatment to tab characters.  There are also ways to suppress these
kinds of data mangling.

(One reason for these quirks is that line sequential files are text
files, whose records are delimited by line feeds or carriage return/
line feed pairs.  The presence of binary data can potentially cause
confusion because a line feed or carriage return can occur as part of
the data.  The extra nul characters enable the reading program to
determine which line feeds are data and which are delimiters.)

Please post again with more detailed information.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
