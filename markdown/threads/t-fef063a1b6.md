[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TinyCOBOL release 0.56

_1 message · 1 participant · 2002-01_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### TinyCOBOL release 0.56

- **From:** David Essex <dessex@arvotek.net>
- **Date:** 2002-01-29T12:57:35-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3C56E28F.E765EF54@arvotek.net>`

```
Announce: TinyCOBOL release 0.56

The TinyCOBOL compiler version 0.56 is available at the TinyCOBOL home
page (1) and iBiblio (2).

0.56:
This release contains mainly bugs fixes, and some enhancements.  
It includes updates to the main compiler, run-time, the regression 
test suite.

Support for the CHAIN, GOBACK statements, BLANK WHEN ZERO, 
INITIAL (preliminary), SPECIAL-NAMES (preliminary) clauses, 
COMPUTATIONAL-X type, have been added to the compiler.

The compiler front end has been enhanced to enable TC to create 
an executable directly using the command line.

The command line options have been changed to more closely reflect 
the GCC options.

Preliminary support for the Win32 (native, no emulation layer required)
platform using the MinGW (Mingw32) tool chain. 

A set of utilities have been added to enable TC testing 
for COBOL standard compatibility using the NIST test suite.

General notes:
Bison is the default parser, Berkeley's YACC (byacc) version 1.9.3
is now an option.
The configure script will now handle multiple versions library DB and
C compilers depending on the options selected.

Important note:
Effective with version 0.56, the command line options have been changed
to more closely reflect the GCC options.

The default action when no appropriate command line option is given,
defaults to 'x', create an executable (preprocess, compile, assemble and
link). 

Previous version defaulted to 'S', generate assembler code (preprocess,
compile).


Please report any bugs and/or problems to the TinyCOBOL mailing list. 


1) TinyCOBOL Home Page
   http://tiny-cobol.sourceforge.net/

2) iBiblio (formerly Metalab)
   http://www.ibiblio.org/pub/Linux/devel/lang/cobol/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
