[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Parsers

_7 messages · 7 participants · 2000-04_

---

### COBOL Parsers

- **From:** "Mark Rickan" <mrickan@home.com>
- **Date:** 2000-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-120@comp.compilers>`

```
Does anyone have any insights/experience on options for parsing COBOL?
I am working on a project where we will need to extract data file
declarations and access these files using other applications using
multiplatform C/C++.

So far we've considered the CobolTransformer Toolkit from Siber
Systems (www.siber.org), the COBOL parser from CocoLab
(http://www.cocolab.de/) or rolling or own using Coco/R
(http://cs.ru.ac.za/homes/cspt/cocor.htm), Visual Parse++ from
Sandstone (www.sand-stone.com).

Any help would be greatly appreciated.

Mark
[There's some stuff in the FAQ.  The grammar for Cobol isn't particularly
complex, but it's very large with an enormous number of different tokens.
-John]
```

#### ↳ Re: COBOL Parsers

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-129@comp.compilers>`
- **References:** `<00-04-120@comp.compilers>`

```
Mark Rickan wrote:
>
> Does anyone have any insights/experience on options for parsing COBOL?
> I am working on a project where we will need to extract data file
> declarations and access these files using other applications using
> multiplatform C/C++.

In fact, grammar of Cobol is fairly tricky at times.

Example: Cobol grammar is non LALR(1), that is it requires lookaheads
of more than one.

Example: to distinguish between 2 forms of PERFORM statement
PERFORM A OF B TIMES COMPUTE X=Y+Z END-PERFORM and
PERFORM A OF B COMPUTE X=Y+Z
we need a lookahead of 4 tokens.

In the 1st form A OF B is data item name
that contains conuter for PERFORM ... TIMES ... END-PERFORM stmt.
In the 2nd form A OF B is paragraph name performed
by PERFORM statement.

It probably can be made with some heavy symbol-table-based trickery,
but it does not really work here, because is some dialects A OF B can
be both paragraph name and data item name (2 diffrent names can have
the same name!).

So really doing your own Cobol grammar -- the one that works -- is too
expensive, as there are many pitfalls on the way.  It tooks us 3 years
to get it right, which I would not qualify as easy.

Vadim Maslov
Siber Systems
```

##### ↳ ↳ Re: COBOL Parsers

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-145@comp.compilers>`
- **References:** `<00-04-120@comp.compilers> <00-04-129@comp.compilers>`

```
Vadim is quite correct. To parse the Cobol 85 nucleus alone, I had to
put many hacks into my code to help the standard tools along.

You can have a look at the details in my pre-pre-alpha Cobol compiler
if you are interested at
http://www.geocities.com/timjosling/cobol.html .

The file that has the description of the hacks is
gcc/cobol/cobctok.def. The grammar is in the same directory cobcprs.y

Similar problems exist in other parts of the language. It is not
actually rocket science but it does make it hard to provide good error
messages.

Tim Josling

> In fact, grammar of Cobol is fairly tricky at times.
>
…[6 more quoted lines elided]…
> we need a lookahead of 4 tokens.
```

###### ↳ ↳ ↳ Re: COBOL Parsers

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-158@comp.compilers>`
- **References:** `<00-04-120@comp.compilers> <00-04-129@comp.compilers> <00-04-145@comp.compilers>`

```
On 20 Apr 2000 01:36:57 -0400, Tim Josling <tej@melbpc.org.au> wrote:
>Similar problems exist in other parts of the language. It is not
>actually rocket science but it does make it hard to provide good error
>messages.

Speaking of error messages, I got an interesting one from the Fujitsu
v5 compiler the other day.  Had me laughing.

What it meant to say was "Required file is missing".  But what it said
(and remember these messages were translated directly from Japanese
into english):

A file that does not exist was found.
```

#### ↳ Re: COBOL Parsers

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-124@comp.compilers>`
- **References:** `<00-04-120@comp.compilers>`

```
Mark Rickan wrote:
>
> Does anyone have any insights/experience on options for parsing COBOL?
> I am working on a project where we will need to extract data file
> declarations and access these files using other applications using
> multiplatform C/C++.

I have one that handles the data division pretty well completely, in
cobol.  I creates a cobol array of the definitions so that you can use
the information gained.  It is freeware, you can use it but any
modifications must come back to the original source.  Bug reports
accepted and corrected as well.

Compiles under Fujitsu V3 (available from www.adtools.com)

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: COBOL Parsers

- **From:** "John H. Lindsay" <eil@kingston.net>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.compilers
- **Message-ID:** `<00-04-130@comp.compilers>`
- **References:** `<00-04-120@comp.compilers>`

```
Hi folks:

This isn't really a compiler problem, but a simple text-processing
one.  Do have a look at the language SNOBOL 4, especially with any of
the Spitbol compilers.  See http://www.Snobol4.com .  Don't laugh if
you thought SNOBOL4 died; it's alive and well and doing the same sort
of amazing things (string processing, pattern recognition, data
structures ...) as always, especially one-off and special purpose jobs
like this one, although some amazing things have been done with it
like a compiler for a PL/I-like system language in ~700 lines!
There's a mailing list available via the above web site if you need
starters.

Mark Rickan wrote:
> Does anyone have any insights/experience on options for parsing COBOL?
> I am working on a project where we will need to extract data file
> declarations and access these files using other applications using
> multiplatform C/C++.
```

#### ↳ Re: COBOL Parsers

- **From:** isaac kattan <i.kattan@liant.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sfmbg6d45c2104@corp.supernews.com>`
- **References:** `<00-04-120@comp.compilers>`

```
mark,
If you are using Micro Focus or RM Cobol you can use a product called 
Relativity.  It makes your COBOL application appear to be a standard ODBC 
data source to your other applications like Crystal reports or MS Access 
etc... You can e-mail me at I.kattan@liant.com if you have any questions.
Thanks
Isaac



Mark Rickan wrote:
> 
> 
…[16 more quoted lines elided]…
> -John]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
