[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Version 1.3.1 of CobolTransformer available (has free eval package)

_1 message · 1 participant · 1997-08_

---

### Version 1.3.1 of CobolTransformer available (has free eval package)

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-08-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5tqjat$34e$1@nnrp3.snfc21.pbi.net>`

```


Dear Sirs,

Version 1.3.1 of CobolTransformer is now available.

CobolTransformer is a C++ toolkit that includes:
* High quality Cobol Parser that parses 12 most popular Cobol dialects.
* Tree-based Internal Representation for Cobol programs and
C++ library to manipulate this representation.
* PrettyPrint library that transforms our tree-based Internal Representation
back into beautifully indented human-readable Cobol program.

Cobol Beautifier Cbl-Beau based on this latest version
can be freely downloaded from http://www.siber.com/sct/

Also we made available for free donwload a prototype of
Microfocus Cobol to Fujitsu Cobol converter Mf2Fsc.
It serves as an example of using CobolTransformer
in building real reengineering products.
We would like to hear from you if Mf2Fsc is a product
that your company might buy.

In addition to that we redesigned the CobolTransformer website
http://www.siber.com/sct/, so that it is now much easier
to use it and to navigate it. There is abundance of new information
on CobolTransformer and improved Technical White Paper.

Don't forget to hit the Reload button when you go to our website,
or else you might see the old version.


Vadim Maslov
Siber Systems

-------------------------------------------------------------
NEWS file:


08/21/97: Version 1.3.1
-----------------------

* Major redesign for the CobolTransformer Web site
at http://www.siber.com/sct/

* Implement NOTE statement (OSVS).
This statement is yet another way to have comments in
Procedure Division. Fix several bugs in OSVS dialect
parsing.


08/10/97: Version 1.3
---------------------

* Create mf2fsc -- prototype of MicroFocus Cobol to Fujitsu
Cobol converter. Make this prototype freely available for
download. We expect this prototype to evolve into a
finished product in the near future.


* Considerably enhance expression tree handling functions.
Introduce tree walker function, PICTURE character-string
parser; rewrite SPECIAL-NAMES, ACCEPT, DISPLAY and SCREEN
SECTION clauses tree representation.


* Make separation between CobolTransformer library code and
CobolTransformer user code more explicit and formal.
Require that user code and CobolTransformer code reside
in different directories. Tune makefiles to handle this
correctly.


* Massive MicroFocus dialect parser testing.
CobolTransformer parser was tested on 1.3 million lines of
production MF Cobol code. A number of bugs in the parser
was fixed as a result.



05/16/97: Version 1.2
---------------------

* Completed implementation of full ANSI-85 and MF Cobol
syntax. Specifically, implemented COMMUNICATION SECTION
(ANSI-85), SCREEN SECTION (MF), REPLACE statement.


* Passed CCVS -- Federal Cobol Compiler test suite by
National Institute of Standards and Technology
(NIST). Fixed a number of bugs in lexer and parser to
achieve this. Note: CobolTransformer was not formally
submitted to NIST for testing, because it is not a *full*
compiler. But we made sure that all the Cobol sources in
CCVS are parsed and beautified correctly.


* Ported CobolTransformer and cbl-beau to SUNOS 4.1 (UNIX)
platform. The Cbl-Beau executable also runs on Solaris 2.5.


* Allow separators not to be finished with spaces when
-lang=mf is on. MicroFocus compiler allows constructs like
"AAA>=12" be understood as "AAA >= 12". According to the
standard, though, "AAA>=12" is a single character-string,
not 3 character-strings, because '>' and '=' by itself are
not separators and therefore space separator is required
between "A" and ">=" and between ">=" and "12".
CobolTransformer now can parse constructs like this
according to MF rules.


* Added -gen-max-indent=NNN option. Sets maximum allowable
indentation to column NNN. If your program has too many
levels of statements and/or gen-indent-step is large, then
you can use this option to stop indentation at a specified
position.



03/01/97: Version 1.1
---------------------

* Native compiler (Visual C++ 4.1) support for WIN32 (MS
Windows 95 and NT). In version 1.0 we used CygWIN32
GCC-2.7.2 compiler to compile cbl-beau. As a result,
run-time library CYGWIN.DLL was required to run cbl-beau.

In version 1.1 we switch to Visual C++ version 4.0
compiler. It builds native WIN32 executables that do not
require any extra DLLs to run. Also it produces executable
that has a much better processing of CTRL-C signal.


* Support for Ryan McFarland COBOL-85 was added. Only
RM/COBOL-74 was supported at CobolTransformer version 1.0.


* Cobol generator now generates code that strictly follows
all Area A/B rules. Cobol Reference Format standard
prohibits some language elements (SELECT clause, etc.) from
appearing in Area A, they can only start in Area B. In
version 1.0 some of Area A/B rules were disregarded.




02/01/97: Version 1.0
---------------------

* First publicly available release of CobolTransformer.

* Created CobolTransformer Web site at
http://www.siber.com/sct/


Copyright 1996-1997 by Siber Systems Inc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
