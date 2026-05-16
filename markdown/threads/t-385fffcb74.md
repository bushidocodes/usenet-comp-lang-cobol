[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL post-VS COBOL II

_2 messages · 2 participants · 2003-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL post-VS COBOL II

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-09T14:01:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<behotu$gen$1@slb5.atl.mindspring.net>`

```
Given a couple of recent threads, I thought that I would "list" the features
that IBM has added to its mainframe (MVS, OS/390, z/OS) compilers since the
(long ago and far away) days of VS COBOL II (their first '85 Standard
compiler).

I believe that many (not all - but probably more than half) of all shops
that ARE running currently supported IBM compilers use in MANY (not all) of
their programs at least SOME of these features. For those "outside" the US
where Unicode/DBCS and/or Euro currency signs are needed, it is almost
CERTAIN that they are using some of these features.  In addition, many sites
used the Y2K support that IBM introduced ONLY in their post-VS COBOL II
compilers.

If you work in a site that has many "fortress COBOL" <in the negative-sense>
mentality programmers - but where the current compilers are available, you
might want to pass this note on to them. You might also want to interest
your management in a course similar to that available (from a CLC
contributor) and described at:

    http://www.trainersfriend.com/d204descr.htm

If you are using a NON-IBM compiler on the Workstation (Windows or Unix) for
developing code intended to run in production on the mainframe, you may want
to ask your "vendor of choice" for which (if any/all) of these they already
support - and how easy it is to "guarantee" that (restrict) code that
compiles on the Workstation to code that *will* port back (correctly) to
your IBM mainframe compiler "of choice".

I have provided online references for where these "highlights" come from.

NOTE:
   IBM SAA AD/CYCLE COBOL/370 manuals are no longer available online (as far
as I can tell).  That was the first compiler with intrinsic functions and LE
support

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGYLR205/FRONT_2.4

The millennium language extensions, enabling compiler-assisted date
processing for dates containing 2-digit and 4-digit years.

For information on the millennium language extensions, see "Millennium
Language Extensions and date fields" in topic 1.7.

New language elements in support of the millennium language extensions:

    -  DATE FORMAT clause in data description entries
    -  Intrinsic functions:
    - DATEVAL
    -  UNDATE
    - YEARWINDOW

 New compiler options in support of the millennium language extensions:

    -  DATEPROC/NODATEPROC
    - YEARWINDOW

 New compiler option, ANALYZE, to check the syntax of imbedded SQL and
CICS(R) statements.

 New date intrinsic functions to cover the recommendation in the Working
Draft for Proposed Revision of ISO 1989:1985 Programming Language COBOL:

    - DATE-TO-YYYYMMDD
    - DAY-TO-YYYYDDD
    - YEAR-TO-YYYY

 Extension of the ACCEPT statement to cover the recommendation in the
Working Draft for Proposed Revision of ISO 1989:1985 Programming Language
COBOL:

    - ACCEPT FROM DATE YYYYMMDD
    - ACCEPT FROM DAY YYYYDDD

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGYLR205/FRONT_2.3

Extensions to support the Euro currency sign in numeric-edited data items.
These extensions introduce a PICTURE SYMBOL phrase to the CURRENCY SIGN
clause in the SPECIAL-NAMES paragraph of the Environment Division. The
PICTURE SYMBOL phrase allows a PICTURE clause currency symbol to represent a
currency sign value that is different from the currency symbol, and not
restricted to a single character. For example, the currency symbol '$' could
be used to represent a code point for the Euro currency sign, or the
characters 'EUR'. The extensions also allow multiple currency symbols and
currency sign values to be defined. For details, see "CURRENCY SIGN clause"
in topic 4.1.7.

Update to the millennium language extensions to allow signed numeric date
fields.

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGYLR205/FRONT_2.2

Enhancements to the millennium language extensions:
    - Additional date patterns for the DATE FORMAT clause, including X
"year-last" dates.
    - DATE FORMAT for binary numeric items.
    - Relaxation of the USING/RETURNING parameter rules for windowed X date
fields.
    - Special semantics for "trigger" and "limit" date values. For more
information, see "Semantics of windowed date fields" in X topic 5.3.6.1.

 New sub-option TRIG/NOTRIG of the DATEPROC compiler option, to enable or
disable trigger and limit processing.

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGYLR205/FRONT_2.1

Enhanced support for decimal data, raising the maximum number of decimal
digits from 18 to 31 and providing an extended-precision mode for arithmetic
calculations ("PICTURE clause" in topic 5.3.11)

 Support for COMP-5 data type extended to OS/390 and VM ("USAGE clause" in
topic 5.3.16)

 Support for line-sequential files extended to OS/390 ("File organization"
in topic 4.2.5.1)

Use of an environment variable in the SELECT ... ASSIGN clause (to specify
file attributes for dynamic allocation at run-time) extended to OS/390
("ASSIGN clause" in topic 4.2.3)

Support for format 5 of the SET statement (SET pointer TO ADDRESS OF
identifier-7) extended to the Working-Storage Section and the Local-Storage
Section ("Format 5: SET for USAGE IS POINTER data items"
X in topic 6.2.33.5)

 The limit on the block size for a QSAM file is raised from 32767 to
2,147,483,647 (2GB - 1) bytes (Appendix A, "Compiler limits" in topic
APPENDIX1.1)

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR10/FRONT_1.6.2

Interoperation of COBOL and Java by means of object-oriented syntax,
permitting COBOL programs to instantiate Java classes, invoke methods on
Java objects, and define Java classes that can be instantiated in Java or
COBOL and whose methods can be invoked in Java or COBOL

Ability to call services provided by the Java Native Interface (JNI) to
obtain additional Java capabilities, with a copybook JNI.cpy and special
register JNIENVPTR to facilitate access

XML support, including a high-speed XML parser that allows programs to
consume inbound XML messages, verify that they are well formed, and
transform their contents into COBOL data structures; with support for XML
files encoded in Unicode UTF-16 or several single-byte EBCDIC or ASCII code
pages

Support for Unicode provided by NATIONAL data type and national (N, NX)
literals, intrinsic functions DISPLAY-OF and NATIONAL-OF for character
conversions, and compiler options NSYMBOL and CODEPAGE
Multithreading: support of POSIX threads and asynchronous signals,
permitting applications with COBOL programs to run on multiple threads
within a process

A 4-byte FUNCTION-POINTER data item that can contain the address of a COBOL
or non-COBOL entry point, providing easier interoperability with C function
pointers

Relaxed rules for using ADDRESS OF in the argument list of a CALL statement
that specifies BY CONTENT or BY VALUE. Such arguments are no longer
restricted to linkage section items, and now can be specified in the linkage
section, working-storage section, or local-storage section. This capability
facilitates interoperability with C/C++ functions that have pointer
parameters.

VALUE clauses for binary data items that permit (in appropriate cases)
numeric literals that have values of magnitude up to the capacity of the
native binary representation, rather than being limited to the values
implied by the number of 9s in the PICTURE clause

***


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR10/FRONT_1.6.1


Java interoperability support has been enhanced:

    - Object references of type jobjectArray are supported for
interoperation between COBOL and Java.
    -  OO applications that begin with a COBOL main factory method can be
invoked with the java command.

            ***

In addition to all of those "language specific" features listed above, one
would need to check EACH of the LE manuals from 1997 (and later) for
enhancements and new features added there.
```

#### ↳ Re: IBM COBOL post-VS COBOL II

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-07-09T23:14:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0307092214.1e6a5cf8@posting.google.com>`
- **References:** `<behotu$gen$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<behotu$gen$1@slb5.atl.mindspring.net>...
> Given a couple of recent threads, I thought that I would "list" the features
> that IBM has added to its mainframe (MVS, OS/390, z/OS) compilers since the
> (long ago and far away) days of VS COBOL II (their first '85 Standard
> compiler).
> 

Message snipped

Thanks for an interesting and informative post

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
