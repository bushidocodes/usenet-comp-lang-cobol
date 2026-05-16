[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Earley Parser for OO-COBOL?

_4 messages · 4 participants · 2005-12_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Earley Parser for OO-COBOL?

- **From:** "Herwig Huener" <Herwig.Huener@fujitsu-siemens.com>
- **Date:** 2005-12-15T12:14:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dnrj6m$i08$1@nntp.fujitsu-siemens.com>`

```
2005-12-15 12:09:06 MET

Hi,

I was told that there exists a context-free grammar for current
OO-COBOL which can be parsed by the Earley-Algorithm.

Did anyone have a real-life-contact with that sort of thing?

Not that I advocate the use of this algorithm in real-life-compilers
- they require too much resources. And as for a ESQL-Precompiler
on which I work now, I am totally happy with YACC, because the
Parser of a PreCompiler only sees part of COBOL.

For playing with Earley-Parsers, see here:

http://accent.compilertools.net/

I downloaded it and it could be made to run on Linux, on
CygWin and on Reliant Unix without further fuzz.

Herwig
```

#### ↳ Re: Earley Parser for OO-COBOL?

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-12-15T20:59:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OOkof.117977$Gd6.29482@pd7tw3no>`
- **In-Reply-To:** `<dnrj6m$i08$1@nntp.fujitsu-siemens.com>`
- **References:** `<dnrj6m$i08$1@nntp.fujitsu-siemens.com>`

```
Herwig Huener wrote:

Bottom Post :
> 2005-12-15 12:09:06 MET
> 
…[18 more quoted lines elided]…
> 

Herwig,

I've never researched this. The only thing I can think of that even
comes *remotely* close to your query is the class Vocabulary provided by
Micro Focus. Look at the following Net Express V 4.0 on-line manual
Chapter 13 - Requirements-Based Vocabulary - but of course you are
compiling for Windows :-

http://supportline.microfocus.com/supportline/documentation/books/nx40/oppubb.htm

While I have your attention - was it you ages ago pointed us at a site
(Google ?) that has a library of photographs of historical figures ?
I've lost the URL.

Jimmy
```

#### ↳ Re: Earley Parser for OO-COBOL?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-12-15T22:02:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sJlof.1915$lv3.144@clgrps12>`
- **References:** `<dnrj6m$i08$1@nntp.fujitsu-siemens.com>`

```

"Herwig Huener" <Herwig.Huener@fujitsu-siemens.com> wrote in message 
news:dnrj6m$i08$1@nntp.fujitsu-siemens.com...
> 2005-12-15 12:09:06 MET
>
…[17 more quoted lines elided]…
> CygWin and on Reliant Unix without further fuzz.

    For what it's worth, I had to develop my own grammar for COBOL (not OO 
COBOL) manually based on language specification documentation, and it ended 
up NOT being context free (particularly because of the existence of 
abbreviated conditionals).

    As for actual grammars, I only know of one for COBOL, and it's VS COBOL 
II:

http://www.cs.vu.nl/grammars/vs-cobol-ii/

but it comes with the following notice:

<quote>
The grammar should be regarded as a specification (of context-free syntax + 
lexical syntax) rather than a realistic parser + scanner description. So, 
for example, issues usually handled by a pre-processor are not covered by 
the formal definition. Also, the grammar specification is still ambigious.
</quote>

    - Oliver
```

##### ↳ ↳ Re: Earley Parser for OO-COBOL?

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2005-12-20T17:46:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<doa4tr02u5t@enews2.newsguy.com>`
- **References:** `<dnrj6m$i08$1@nntp.fujitsu-siemens.com> <sJlof.1915$lv3.144@clgrps12>`

```

"Oliver Wong" <owong@castortech.com> wrote in message
news:sJlof.1915$lv3.144@clgrps12...
>
> "Herwig Huener" <Herwig.Huener@fujitsu-siemens.com> wrote in message
…[9 more quoted lines elided]…
> COBOL) manually based on language specification documentation, and it
ended
> up NOT being context free (particularly because of the existence of
> abbreviated conditionals).

For what it's worth, we developed our own parser     for COBOL using
GLR parsers.  Completely context free, with some ambiguities that we
resolve in name and type resolution, using attribute grammar evalution
methods.   Unlike Earley parsing, this is fast and *very* practical.
An additional problem is simply the number of COBOL variations out in
industry; we have dialect management to handle this.
See http://www.semanticdesigns.com/Products/FrontEnds/COBOLFrontEnd.html.

>     As for actual grammars, I only know of one for COBOL, and it's VS
COBOL
> II:
>
…[5 more quoted lines elided]…
> The grammar should be regarded as a specification (of context-free syntax
+
> lexical syntax) rather than a realistic parser + scanner description. So,
> for example, issues usually handled by a pre-processor are not covered by
> the formal definition. Also, the grammar specification is still ambigious.
> </quote>

Beyond the foothills are the Himalayas.
Our has the preprocessor.  What is missing from this discussion is full name
and type resolution
(eg., construct the symbol table the compiler would use) which most people
simply
overlook, but you can't do very much without this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
