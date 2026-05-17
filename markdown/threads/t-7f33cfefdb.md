[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CobolTransformer version 1.1 is available

_1 message · 1 participant · 1997-03_

---

### CobolTransformer version 1.1 is available

- **From:** "va..." <ua-author-13871149@usenetarchives.gap>
- **Date:** 1997-03-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5gijli$5bo@world1.bawave.com>`

```


You can find out more about CobolTransformer at http://www.siber.com/sct/

----------------------------------

The version 1.1 of the CobolTransformer offers the following new features:

* Native compiler support for WIN32 (MS Windows 95 and NT) was added.
In ver 1.0 we used CygWIN32 GCC-2.7.2 compiler to compile cbl-beau.
As a result, run-time library CYGWIN.DLL was required to run cbl-beau.

In ver 1.1 we switch to Visual C++ ver. 4.0 compiler. It builds native
WIN32 executables that do not require any extra DLLs to run.
Also it produces executable that has a much better processing of CTRL-C signal.

* Support for Ryan McFarland COBOL-85 was added.
Only RM/COBOL-74 was supported at CobolTransformer ver 1.0.

* Cobol generator now generates code that strictly follows all Area A/B rules.
Cobol Reference Format standard prohibits some language elements
(SELECT clause, etc.) from appearing in Area A, they can only start in Area B.
In ver 1.0 some of Area A/B rules were disregarded.

* A number of bugs in grammar and code generation were fixed.

----------------------------------

Original announcement:

Siber Systems Inc. is pleased to announce CobolTransformer reengineering
toolkit. It includes the following:

- High quality Cobol Parser capable of parsing the following Cobol
dialects: ANSI-74, ANSI-85, OSVS, VS II, SAA, X/Open, Microsoft,
Microfocus, Ryan McFarland 74 and 85, DOSVS, UNIVAC.

- Internal Representation for Cobol programs (expression trees) and
C++ library to manipulate this representation that includes.

- PrettyPrint library (also in C++) that transforms our internal
representation back into beautifully indented COBOL program with fully
preserved comments. What's most important, pretty-printing is totally
customizable, that is, you can directly encode your COBOL formatting
rules into our table-driven pretty-printer.


So we offer a complete and well-designed Cobol compiler toolkit
written in C++ that lets you focus on particulars of your Cobol
reengineering project (including but not limited to Year 2000
projects) and not worry about handling complexity of quality Cobol
lexing, parsing, and generation.

To learn more about CobolTransformer, please check out
our Web site at http://www.siber.com/sct/


A free demo/evaluation program cbl-beau is available for
immediate download from http://www.siber.com/sct/.

cbl-beau beautifies (pretty prints) your Cobol program.

The primary goal of cbl-beau is to demonstrate speed and versatility
of our parser and code generator.


For pricing and other questions please e-mail to: in··.@si··r.com.

----------------------------------

Plans for the future
====================

* Year 2000 module.

* Port to Sun workstations.

* Add support for IDMS.


----------------------------------


Vadim Maslov
Siber Systems
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
