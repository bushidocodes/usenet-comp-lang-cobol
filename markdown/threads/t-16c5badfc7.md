[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CobolTransformer 2.1 Announce: para renaming tool, success stories

_1 message · 1 participant · 1998-02_

---

### CobolTransformer 2.1 Announce: para renaming tool, success stories

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34eb72f6.0@news.tsoft.net>`

```


Siber Systems is pleased to announce availability
of Version 2.1 of CobolTransformer http://www.siber.com/sct/.

CobolTransformer (SCT) is a next generation Cobol reengineering
and parsing toolkit (SDK) that makes developing applications
that need to parse and generate Cobol source an easy and
satisfying job.

By using standardized CobolTransformer components,
you will be able to develop your Cobol-transforming
(or Cobol-analyzing) product or project *faster* and
it will be of much higher *quality*.

CobolTransformer is a library with API in C++ that includes:

* High quality Cobol Parser that parses 12 most popular
Cobol dialects and that has tremendous error recovery
capability.

* C++ library that client uses to browse and transform the
tree-based Internal Representation of Cobol programs.
Definition-Use links attached to the Program Tree
effectively make it a general case Graph.

* PrettyPrinter that transforms our Internal
Representation back into beautifully indented
human-readable Cobol program.

To get more information, please direct your browser
to http://www.siber.com/sct/


Major New feautures in CobolTransformer 2.1
-------------------------------------------

* The whole Cobol Program is now represented as a single
Expression Tree, which gives you a serious power to
analyze and change your Cobol code.
700,000-line Cobol Program Tree takes only 10Mb in memory.
This means that our approach works for big programs too.
And for even bigger programs we made tree parts swappable
to disk, so there is no memory limit for our technology.

* Introduced Symbol Table, Use-to-Definition and
Definition-to-Use links for Named Objects to give you a
complete control over namespace of your Cobol program.
Effectively we compute a Data Flow Graph that represents
your Cobol Program.

Specifically, for every Name we compute a list of all
Definitions for this Name. For every Use of a Named
Object we have a link to the Definition of this Named
Object, and for every Definition of a Named Object we have
a list of links to all Uses of this Named Object.


* Added parsers and code generators for:
- Wang VS Cobol 85.
- Fujitsu NetCobol (the one that generates Java bytecode).


* Released free Paragraph/Section/Data-Name Renumbering
tool as a part of CobolBeautifier cbl-beau to demonstrate
our Def-Use links capabilities.

The tool correctly handles name collisions and computes
Shortest Qualified Name that uniquely identifies renamed
Named Object.


* Native makefile for WIN32.
WIN32 customers will receive a native WIN32 makefile that
works with Microsoft make program called "nmake".


Satisfied Customers
-------------------

A number of companies are already using CobolTransformer
and this is what they say:

"We use the Siber CobolTransformer product as a *core
technology* in the utility software we have created to
migrate Cobol source code from the mainframe to new
environment. ...

Using a *proven* and *reliable* parsing technology has
made the task of legacy code migration significantly
easier for us and has resulted in the creating of tools
that appear to be much more reliable and easier to
maintain."
Sandy Allinson, Allinson Ross Corporation


"CobolTransformer allowed us to eliminate any work
required for parsing and allowed us to focus our resources
on the actual conversion application. ...

Time to setup & start being productive was pleasantly minimal!"

Aharon Goldman, Software Conversion House

Read full CobolTransformer Success Stories at
http://www.siber.com/sct/success.html.



Happy Partners
--------------

San Jose, California - February 17, 1998.

Fujitsu Software Corporation and Siber Systems,
Inc. announced that Fujitsu will distribute Micro Focus
COBOL to Fujitsu COBOL Converter and other COBOL automated
migration and re-engineering tools developed by Siber
Systems.

"Siber Systems has developed superb COBOL parsing and code
conversion technology that fully complements our COBOL
product strategy," said Todd Yancey, General Manager,
Developer Tools Group for Fujitsu Software Corporation.

"We look forward to having Siber Systems excellent
development team work with us on integrating their
technology with Fujitsu COBOL products."


For full Press Release please direct your browser
to http://www.siber.com/sct/press.html.


Contact Info
------------

If you need pricing information or have any other questions
regarding CobolTransformer, please reply to this message,
or send e-mail to in··.@si··r.com.


Vadim Maslov
Siber Systems
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
