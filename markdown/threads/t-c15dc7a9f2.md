[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DEC COBOL - compiler libraries

_1 message · 1 participant · 1997-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### DEC COBOL - compiler libraries

- **From:** "lindsay smith" <ua-author-602229@usenetarchives.gap>
- **Date:** 1997-07-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc8cce$83fb5710$fe64a8c0@pc-205-207>`

```

Our CC have just installed DEC COBOL on a DEC Alpha system (DEC COBOL
Compiler Driver V2.4-863). We have previously been using MicroFocus on a
HP machine but have now been changed over to the above. Our experience
with DEC COBOL is a bit 'light on', at the moment I am having a problem
compiling (actually during link) due to a missing library file?.

Given a simple program:

identification division.
program-id. test1.
author. lindsay
date-written. Jan 1997.
date-compiled.

environment division.

input-output section.
file-control.

data division.
file section.

working-storage section.


procedure division.
000-main.
Display 'Testing'.
stop run.


If I try to compile this source I get the following result:

› cobol -ansi basic.cbl
ld:
Can't locate file for: -lsort
cobol: Severe: Failed while trying to link

If I compile to just the object file, all is fine:

› cobol -ansi -c basic.cbl
› ls
› basic.cbl basic.o
›

The compiler is based in /usr/lib/cmplrs in two subdirectories:
- the cobol (cobol_240) subdirectory containing the compiler which a
symbolic link from /usr/bin/cobol points to, and
- the cobolrtl (cobolrtl_240) which is presumably the cobol runtime system
containing some libraries but not this sort one. It does contain:
cob_msg.cat libcob.a libcob.so libisam_stub.a
libtps_stub.a

A complete scan of the file system failed to reveal any library file of
the name sort (although presumably it may be in some other library of a
different name). Can anyone help?

Lindsay.
---------------------------------------------------------------------------
--------
Lindsay Smith, Computing Lecturer, Monash University
Gippsland School of Computing & Information Technology
Switchback Rd, Churchill, Victoria, AUSTRALIA 3842
Phone: +61 51 226669 Fax: +61 51 226842
Email: Lin··.@fci··u.au
GSCIT Home Page: http://www-gscit.fcit.monash.edu.au/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
