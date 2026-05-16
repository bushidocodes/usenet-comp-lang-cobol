[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please help -- COBOL Programming Standard

_65 messages · 16 participants · 2003-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-05T17:08:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E669F8D.E69F28E3@attglobal.net>`

```
I have been asked to provide a COBOL programming standard for my
company's applications support organization.  This is a first, but hey,
COBOL has only been out a bit over 40 years.

I would appreciate any input any of you might want to provide concerning
the document content, wording, etc.

I have turned a MS Word doc into a .TXT file, so naturally, some
formatting has been lost, and I may have left some characters that do
not translate to text files.  I also changed my company's name to "CoX",
and my organization to "ORG", so it may look funny in some places.  I
have tried not to leave any other company names, etc. in the document.
If I have, please ignore them!

I am putting on my thick skin, so you may fire away.  I already expect
that some of you will not care for some of the specific standards, and I
do not mind if you say so!

With thanks in advance for your assistance, here is the document:
========

Company X

Owned By: ORG
Revised By: Colin Campbell
Subject  COBOL Programming Standards

Approved By:
Version 1.0
Date 3/28/2003





COBOL Programming Standards




Table of Contents
1 INTRODUCTION 1
2 SCOPE AND APPLICABILITY 1
2.1 SCOPE 1
2.2 APPLICABILITY OF THIS STANDARD 1
3 GENERAL REQUIREMENTS 2
3.1 PROGRAMMING ENVIRONMENT 2
3.2 CONVERSION OF OLD COBOL PROGRAMS 2
3.3 THE STANDARDS 2
4 COBOL PROGRAMMING STANDARDS 3
4.1 IDENTIFICATION DIVISION 3
4.2 ENVIRONMENT DIVISION 4
4.3 DATA DIVISION 5
4.4 PROCEDURE DIVISION 7
4.5 STANDARD CHECKING PROGRAM: 8


1
Introduction
Introduction:
CoX's ORG organization is issuing this and other Programming Standards
for its employees when writing new programs or performing maintenance
on existing programs, in the absence of conflicting standards in use
by a CoX customer.  CoX's objective in issuing programming standards
is to promote a common style and the use of proven techniques that
yield high quality, easy to maintain source programs.  ORG
organizations may add to this standard if they deem it necessary, but
may not delete or replace parts of this standard without ORG management
approval.

COBOL (which is an acronym for Common Business-Oriented Language) was
created in the late 1950's, as a cooperative effort between the United
States Government and industry.  The guiding idea behind COBOL was that
it should be a self documenting, English like language, understandable
even by non-programmers.  Beginning in 1968, the American National
Standards Institute (ANSI) and the International Organization for
Standardization (ISO) have issued standards defining the COBOL
language.  There have been standards issued in 1968, 1975, 1985, and
2002.  The standards define not only the syntax of the language, but
also the behavior of programs written using this syntax.  The result
has been what is arguably the best defined and most portable computer
programming language yet created.

Numerous COBOL compilers have been created for many different
computing platforms.  These compilers generally have been validated as
conforming to the standard using suites of COBOL programs created by
the COBOL Compiler Testing Service (CCTS), a department of the United
States Navy.  The involvement of the US Navy is due to the influence
of the late Admiral Grace Hopper, generally considered the creator of
COBOL.

The current COBOL standard has been influenced by the desire to
provide continuity with previous standards as well as two significant
trends.  The first is Structured Programming, generally attributed to
Edsger W Dijkstra, and the more recent Object Oriented Programming,
generally attributed to the Xerox Palo Alto Research Center (PARC).

This document concentrates on "procedural COBOL" and implementation of
good structured programming practices.  Another section or document
covering Object-Oriented COBOL standards may follow.


2 Scope and Applicability
2.1 Scope
This Standard is to be applied to all COBOL development and
maintenance performed by ORG staff, unless the work is being performed
for a customer which has its own programming standard, and the
customer wishes to use that standard in place of CoX's.

2.2 Applicability of This Standard
The programming standards which follow apply to new programs.
Existing programs which are converted to 1985 or later ANSI/ISO COBOL
in order to take advantage of new features of the language or compiler
will be held to less stringent standards, to be published later.


3 General Requirements
3.1 Programming Environment
Supported COBOL Compilers Only:
In order to ensure that COBOL programs are supported both in
compilation and at execution time, only COBOL compilers based on the
1985 ANSI/ISO Standard or later may be used.  Any CoX ORG organization
that does not have the most current COBOL compiler for the platforms
on which they program must obtain that current compiler, and
programmers must use it.  As soon as 2002 ANSI/ISO compilers are
generally available, programmers must use a current, supported COBOL
compiler that is based on that standard.

Exception:
Older compilers are only to be used in emergency situations, such as
when a production program fails, and must be repaired as quickly as
possible.  After such a program is repaired, it must be converted to
current COBOL and placed into production using a current COBOL
compiler.  Old compilers are to be "hidden" to restrict their usage.

3.2 Conversion of Old COBOL Programs
Programs written to earlier standards (1968 or 1974) must be converted
so that they can be compiled and executed using a current (1985 or
2002) compiler and run time library.  ORG organizations must provide
conversion tools to facilitate meeting this requirement.  If a tool
does not exist for a particular platform, then a tool for a next most
suitable platform, and processes for using that platform and tool must
be provided.  ORG organizations will decide whether to convert
programs en masse or on an "as changed" basis.

3.3 The Standards
In general, all elements of the COBOL language, as defined by the 1985
ANSI/ISO COBOL standard and by the 2002 ANSI/ISO COBOL standard are
allowed, except where specifically prohibited.  The use of vendor
extensions to the COBOL language is discouraged, in order to promote
transportability of COBOL programs.  It is the responsibility of
management to specify when use of a vendor extension to COBOL is
allowed.  If a compiler offers an option to flag the use of language
extensions, programs should be compiled using that option, to provide
visibility of the use of extensions.

The programming standards for COBOL are presented in order according
to the structure of the language (by DIVISION):


4 COBOL Programming Standards
4.1 IDENTIFICATION DIVISION

The 1985 and 2002 ANSI/ISO COBOL Standards both require a PROGRAM-ID
paragraph.  The 1985 standard allows other paragraphs, but all are
treated as comments.  All of the defined paragraphs in the 1985
standard are removed from the 2002 standard.  The 2002 standard
allows one new paragraph, OPTIONS.  Therefore, the ORG standard is to
code PROGRAM-ID, as required, and use comment lines to specify all
other information in the Identification Division, except when using
the OPTIONS paragraph of 2002 ANSI/ISO COBOL.

1. The use of the COMMON attribute for a program is prohibited. COMMON
specifies that 'program-name' is contained within another program, and
it can be called from 'siblings' of this program and from programs
contained within the siblings. Normally, when using nested programs,
only the 'parent' program could call the contained 'child' program.
This structure provides the potential for really mixing up a
maintenance programmer.

2. The INITIAL attribute for a program is to be used with caution.
Initially, information about actual use of this feature will be
recorded. Once the performance implications of using the feature are
fully understood, this rule may be reviewed. INITIAL specifies that
whenever this program is called, it should be entered in its initial
state; that is, data items having VALUE clauses would have the initial
value, GO's modified by ALTER would be in their initial state, PERFORM
stacks would be empty, and files would be closed. This implies extra,
possibly time consuming processing before actually doing what the
source program says to do, and any such needs probably could be
handled better by improving application design.

4.2
ENVIRONMENT DIVISION
The Environment Division consists of the Configuration and Input/Output
sections.  It is suggested that the two section headers always be
coded, but that the various paragraphs in those sections be included
only if necessary.  Some compilers may require that some of the
paragraphs be written.

Configuration section entries are generally not needed.  The
exceptions are the Source-Computer paragraph if the Debugging feature
is being used, Object-Computer if a non-standard collating sequence is
being used, and Special-Names in rare cases.

Input-Output section entries define the files used in the program
(File-Control), and special features related to input / output
processing (I-O-Control).  Each file used must be defined.  In
I-O-Control, many of the entries are either ignored on some platforms,
or can be controlled outside the program using Job Control Language.
Unless an I-O-Control feature or features is required, do not code any
I-O-Control entries.

1. The RESERVE clause is prohibited in the SELECT entry, except on a
platform where buffering cannot be controlled externally, and the
COBOL facility can be used.

2. The PASSWORD clause is prohibited in the SELECT entry, unless a
platform has no external security facility, and the COBOL feature can
be used successfully.

3. The RERUN clause is prohibited in the I-O-CONTROL paragraph, except
where the COBOL facility can be used, and there is not an external
facility to control rerunning a program.

4. The SAME clause is prohibited in the I-O-CONTROL paragraph, unless
it is used on a memory constrained platform, and no external memory /
buffer control facility exists.

4.3 DATA DIVISION

1. Use of the EXTERNAL and GLOBAL clauses is prohibited. EXTERNAL can
be specified on both files and data to allow separately compiled
programs to share the file or data item. GLOBAL can be specified on
data to allow programs included within the one where GLOBAL is
declared to reference the data without having it passed to the
subprogram(s) as an argument. Both of these constructs violate good
structured programming practices.

2. The BLOCK 0 clause is required in the FD for all QSAM (sequential)
files on platforms where blocking can be controlled externally.

3. The COPY statement is the preferred method of including code in
COBOL programs because it is part of the 1985 and 2002 ANSI/ISO
standard, except as required by precompilers such as DB2 or CICS,
which might use a word such as INCLUDE. Including code by use of a
library management tool, such as PanValet or Librarian is not allowed,
to promote independence of source code from library management tools.
The COPY statement is more flexible than such includes, since it
allows replacement of words or quoted strings, so that a copied
record description can, for instance, be given unique names if used
more than once.

4. Records used in multiple programs must be described by a COPY
member (and this COPY member must always be used whenever describing
the record in a program).  This leads to consistent naming of fields
and easier understanding of data and programs in a system. Good
practice also dictates use of the same name to describe the same data
throughout all programs which use it; for example, EMPLOYEE-ID and not
EMPLOYEE-NUMBER, PAYROLL-ID, etc.

5. To describe a record in a file description (FD), in the cases where
a simple elementary 01 is not sufficient, such as a variable length
record, the COPY member describing the record must be used. The
SUPPRESS clause of COPY (available in the 2002 ANSI/ISO standard,
otherwise an extension) may be used to reduce the number of print
lines.  Using the COPY member ensures that when the size of a record
is changed, a COBOL compile will know of the change everywhere in the
program.

The alternative to using a COPY statement is:
01  record-name  PIC X(n).

6. Permissible USAGEs for numeric data items are DISPLAY (implied if
no other usage is explicitly stated), BINARY (or COMP), and
PACKED-DECIMAL (or COMP-3).  BINARY and PACKED-DECIMAL are preferred,
as they are part of the ANSI/ISO Standard, while COMP and COMP-3 are
either 'implementor defined' or extensions.  Use of the standard names
will make a program more transportable. Exceptions are allowed if
required to interface with a product that requires other data usages,
such as floating-point, or because a platform supports other data
formats more efficiently.  This rule applies to non-copied source
code. Once a migration from the older COBOL standards is completed,
the rule will also be applied to code in COPY members.

7. DISPLAY usage data items may be either numeric or alphanumeric
(PICture characters 9 or X); alphabetic (PICture character A) items are
not allowed. PICture descriptions will be validated according to this
rule. If a usage DISPLAY data item may contain only numeric data, it
should be defined as numeric, because this ensures that data usages
will be handled with proper decimal alignment, truncation, etc.

8. BINARY (COMP) usage data items must have PICture descriptions of
S9(4) or S9(8). Specifying 1 to 4 digits defines a binary halfword
(16 bits); 5 to 9 digits defines a binary fullword (32 bits).
Specifying over 9 digits defines a binary doubleword (64 bits).
Depending on the platform, there may be performance implications
attached to the use of different sized items.  Use of a standard
number of digits leads to easier recognition of the size of each
binary field when reading a program. This rule initially applies to
non-copied source code.

9. PACKED-DECIMAL (COMP-3) usage data items must have a PICture
specifying a sign and an odd number of digits, such as S9(7)V99.
Describing the same area without a sign or with an even number of
digits causes less efficient code to be generated.  This rule
initially applies to non-copied source code.


10. Arrays (also called tables) should be defined with the OCCURS ...
DEPENDING clause unless the array is of a fixed length, with the data
defined in the program (such as a table of error messages).  When the
array data is derived from an external source such as an input file,
the array definition should use the DEPENDING clause.  When an array
is to be searched in a particular sequence, the ASCENDING / DESCENDING
KEY clause should be defined.  Since the SEARCH statement requires the
use of Index items, the INDEXED clause should be defined.


11. When a program uses subscripting to reference an array, particular
care should be taken to define the subscript data item in a manner
that is most efficient for the platform.  Generally, this would be
USAGE BINARY, with a signed integer defined in the PICture clause.
Other usages might be more efficient on some platforms.

4.4  PROCEDURE DIVISION

1. Programs should not be overly large or complex, in order to promote
understandability and maintainability. The number of COBOL imperative
statements is not felt to contribute to difficulty in understanding as
much as the number of conditional statements. Therefore, a program may
not contain more than 300 IF and EVALUATE statements.  For purposes of
automated standards checking, a warning will be issued when the count
exceeds 60% of the maximum, and an error when the count exceeds 100%
of the maximum. The actual count will be recorded to allow review of
the maximum number later.

2. Highly complex program logic is discouraged.  The level of nesting
within a procedure must not exceed 12; the preferred limit is 6.
Nesting refers mainly to conditional statements contained within other
conditional statements, such as IF within IF or IF within EVALUATE.
Some compilers show the nesting level on the source code listing.

3. All procedures in a program must be coded either as paragraphs or
as sections; in other words, a mix of sections and paragraphs is not
allowed.

4. The ALTER statement is prohibited.

5. The GO statement is prohibited. Structured programming theory has
told us for twenty years that any program can be coded without using
the GO statement.  New language elements in the 1985 ANSI/ISO COBOL
standard, such as CONTINUE (which can be used where we were once
limited to NEXT SENTENCE), END-IF (to terminate the scope of an IF
without ending a sentence), and NOT AT END (on READ and RETURN
statements) make it easier than before to follow this rule than in
1974 ANSI/ISO COBOL programs.  The 2002 ANSI/ISO COBOL standard adds
EXIT PARAGRAPH and EXIT SECTION, which, while not needed in a well
designed procedure, will at least satisfy the rule against the use of
GO.

6. The EXIT statement is prohibited.  In the case where a procedure is
performed for the sole purpose of satisfying a PERFORM...UNTIL
condition (such as serially searching a table), and no action is
required in the procedure, code the CONTINUE statement in an 'in-line'
PERFORM.

7. A program may have only one entry point. Therefore, the ENTRY
statement is prohibited. This rule means that the PROCEDURE DIVISION
header (using the Program-ID as the name, and receiving arguments via
the USING phrase) is the only point at which entry to a program is
allowed.

8. A program may have only one exit point. Program exit may be
accomplished using either of the following two constructs:
GOBACK or
EXIT PROGRAM (followed immediately by)
STOP RUN.

GOBACK is an extension to 1985 ANSI/ISO COBOL, but has been added to
the 2002 ANSI/ISO standard. Use of the STOP statement and EXIT
PROGRAM are otherwise prohibited.

9. The ACCEPT...FROM CONSOLE statement is prohibited. Operator
communication is felt to be too error prone for use in production jobs.

10. The DISPLAY...UPON CONSOLE statement is allowed, but only where a
utility type of program has no other way (such as a file) to
communicate error conditions. Messages created in this way generally
appear on an operating system job log and in the system message
listing. DISPLAY in any form must not be used in an on-line
environment.

11. The only acceptable methods of controlling a loop in a program are
SEARCH, SEARCH ALL, PERFORM...UNTIL, and PERFORM...TIMES. Note that
1985 ANSI/ISO COBOL allows specification of TEST AFTER and TEST BEFORE
on PERFORM to properly support the structured programming DO...WHILE
and DO...UNTIL constructs.  The in line form of the PERFORM statement
is allowed (in line PERFORM requires use of the END-PERFORM scope
delimiter).

12. THRU or THROUGH used in connection with PERFORM and INPUT or
OUTPUT PROCEDURE in MERGE or SORT statements is prohibited. Use of
this construct can lead to accidental destruction of a program's
structure, such as by moving a block of code into or out of the range
specified by a PERFORM ... THRU.

13. Certain standard subroutines, if used, must be called dynamically.
These subroutines are documented as needing to be called dynamically.
Violation of this instruction will result in an error, due to the
danger that bad results could be obtained if the latest version is not
used. (For IBM mainframe compilers, it will be assumed that the
NODYNAM option is in effect; therefore, this rule applies to all
CALL 'literal' statements.)  Each organization which has such
subroutines should provide the list to its programmers.

14. Certain standard subroutines provided in the past to assist
programmers in developing applications are no longer the best way to
accomplish the required task. Use of one of these subroutines in a new
application will result in an error, with the suggestion of a better
alternative.  Each organization which ahs such subroutines should
provide a list to its programmers.
Examples: For the CompanyY account, DISPLAY, DATE, and DATEN should
not be used.  DATEMGR is the preferred subroutine for obtaining and
handling date and time information.


4.5 Standard Checking Program:

These standards when adopted by a CoX ORG group may be enforced at
compilation time by use of a standard checking program attached to
the compiler. This approach is already in use in some ORG groups,
simplifying the task of enforcing the programming standards.  Those
standards which can be checked automatically can be ignored in code
walkthroughs.  Attaching the standard checker to the compiler ensures
that a programmer will know from the first compile of a program
whether it violates standards, and will therefore not be accepted for
production.

Interested ORG groups may use the standard checker code as a basis for
implementing automated checking for their organization.  Currently,
this code is implemented for the IBM mainframe using the compiler exit
facilities, but it is written in COBOL, so it should be adaptable to
other platforms (although the interface will likely have to be
changed).






8
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-05T21:01:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b46dn5$l7j$1@slb4.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
Colin,
  Looks EXCELLENT as a starting point to me (but then again, I come from an
IBM mainframe background where some of your "unstated" assumptions come
from).  I will study it in more detail - but I do have some initial comments
(some "nits" - some medium - and a couple of  "biggies").

The following comments are NOT in any particular order:

  - I think it is "Panvalet" or "PANVALET" - not "PanValet"

  - Re:
"If a compiler offers an option to flag the use of language extensions,
programs should be compiled using that option, to provide visibility of the
use of extensions."
  If a compiler *is* '85 Standard conforming, then they MUST include such an
option, so you don't need to start with "If a compiler offers an option
...."
  (However, I have more to say about this recommendation below)

 - Re:
 "The BLOCK 0 clause is required in the FD for all QSAM (sequential) files
on platforms where blocking can be controlled externally."
 I understand the recommendation and the reference to QSAM - but this *is*
an IBM mainframe-only "solution".  In fact, if you do the flagging listed
above, you will discover that having "0" in the Block clause is an IBM
extension.  Therefore, I recommend that you modify this sentence to start
saying "If the application is intended to be compiled and run on an IBM
mainframe environment, then the extension Block 0 should be used."

 - QUESTION: Doesn't SMS and QSAM also support RECORD CONTAINS 0 now too?
If so, you might want to consider that as well.

 - Related, to the above you should require the AWO compiler option with IBM
mainframe compiles - along with requiring FASTSRT where available.

- Personally, I would avoid talking about the OPTIONS paragraph of the
Identification Division, until you have some compilers that support it.
(Does Micro Focus do so already?  I am not certain).  If you *do* mention
it, then I think you need to start thinking about ARITHMETIC IS
STANDARD/NATIVE issues.  This is a REAL "pros-and-cons" issue - as
portability of ARITHMETIC IS STANDARD may well end up with SERIOUS
performance implications.  This also may relate to using ARITH(EXTEND) and
the entire question of (not Standard in '85 - but Standard in 2002) 31-digit
numbers.

- Re;
 "These compilers generally have been validated as conforming to the
standard using suites of COBOL programs created by  the COBOL Compiler
Testing Service (CCTS), a department of the United States Navy."
 The last testing organization was "NIST" - but they have stopped doing
certifications of the '85 Standard.  EDS has taken over (a "for profit")
certification process - but to the best of my knowledge
  -- no one has used it
 -- it is still pretty questionable whether this will be available for the
2002 Standard.

The "certification tests" (for the '85 Standard with Intrinsic Functions -
but not the Corrections Amendment) are still available for use.

Re;
 "In order to ensure that COBOL programs are supported both in compilation
and at execution time, only COBOL compilers based on the 1985 ANSI/ISO
Standard or later may be used."
  You should also specify that only '85 Standard "language support" compiler
options/directives should be used. (E.g. for IBM - use NOCMPR2, not CMPR2
... or for Micro Focus use NOMF ... If you really do want ANSI'85 conforming
code.)

 Re:
  "The use of vendor extensions to the COBOL language is discouraged, in
order to promote  transportability of COBOL programs."
  This one really worries me.  There may well be a "bunch" of extensions
that provide significant PERFORMANCE enhancements to your applications.
Similarly, there are some extensions that are common (not universal).  I
would STRONGLY suggest that you do a "bunch" of compiles of existing code
with ANSI flagging turned on to see exactly what this recommendation will
"eliminate".

- INITIAL attribute
  In your discussion of this, you might want to mention that the COBOL
"CANCEL" statement allows a programmer to actually control putting a
subprogram into "initial state" and may be used instead of INITIAL.  On the
other hand, you would also need to indicate that in an IBM mainframe
environment, the (non-Standard) NODYNAM compiler option turns "CANCEL' into
a "no-op".

Re:
 "The Environment Division consists of the Configuration and Input/Output
sections.  It is suggested that the two section headers always be coded, but
that the various paragraphs in those sections be included  only if
necessary."
  Any reason for this?  It won't hurt - but I (personally) find this
"over-kill".  It also (if you have any CICS programs) may actually cause you
problems.

Re:
 "The PASSWORD clause is prohibited in the SELECT entry"
FYI - This is an extension that will be prohibited by other rules.

Re:
 " The SAME clause is prohibited in the I-O-CONTROL paragraph, unless it is
used on a memory constrained platform, and no external memory /  buffer
control facility exists."
 Probably a reasonable "general rule" - but the SAME clause can (actually)
be pretty useful when you are doing a COBOL program that (in part) reads in
a file and writes out a duplicate of many of its records.  Probably this is
"obscure enough" that it isn't worth allowing in your "general rules"

 - Personally, I *like* the EXTERNAL clause on files - as it allows
separately compiled programs (without ENTRY statements) to do the different
I/O statements.  Also as indicated in an earlier thread, it is possible
(again IBM mainframe) to compile with DATA(31) and use EXTERNAL to get
"specific" records below the line.  My recommendation would be that you
would need some type of  "repository" to track EXTERNAL usage - but not
disallow it.

- Concerning GLOBAL, I would disallow the entire ability to use nested
programs if you disallow GLOBAL data.  One of the major advantages of nested
programs is the ability to distinguish between "local and global" data.

Re:
 "SUPPRESS clause of COPY"
Are you aware that the 2002 COBOL Standard and the IBM (and Micro Focus and
Fujitsu and a bunch of others) extension are NOT identical?  Compare
"suppressing" versus "suppress".  You don't talk about nested COPY
statements.  This is an extension to the '85 Standard - but included in the
2002 Standard.  I find it useful - but you might want to decide if this or
isn't a "desirable" extension in your environment.

Re:
  Concerning the permitted USAGEs.  If your "ORG" is going to get into mixed
COBOL and C applications, you may find that you need to expand what you say
about COMP-1 and COMP-2 (or equivalent extension before the 2002 Standard).
The reason that I mention these specifically is that I think it may be
worthwhile in any "internal standards" to say that these should ONLY be used
for inter-language communication (from COBOL) as the usual decimal "exact"
values can be lost when floating-point comes in.

Question:
  Is your "ORG" an international company?  If so, you may want to consider
USAGE NATIONAL and all the related issues of "internationalization".

Re:
 "BINARY (COMP) usage data items must have PICture descriptions of  S9(4) or
S9(8). ..."
All that you say in this section ONLY applies to IBM mainframe, those
environments emulating IBM mainframes (e.g. Micro Focus with SOME settings),
and others with compatible hardware.  *MANY* COBOL environments do support
1, 3, and 5 byte binary fields.  You also don't talk about implications of
the TRUNC (or similar) compiler option.  My recommendation on this really
depends on performance issues.  On IBM mainframe TRUNC(OPT) works *so* much
better than the (much more portable) TRUNC(STD) that I rarely recommend the
latter.  On the other hand, it really DOES violate some of the fundamental
rules of COBOL.

Re:
  ODO's.  Personally, I would "reverse" your recommendation concerning the
default on OCCURS.  I would say that you should use a FIXED table (array)
size - unless the size may vary at run-time.  I would also suggest that you
mention that using an OCCURS DEPENDING ON phrase (other than in the File
Section) does *not* save storage and that the compiler ALWAYS allocates the
maximum size.  Finally, I would explicitly recommend the (IBM, Micro Focus,
etc) extension of allowing an OCCURS DEPENDING ON clause to be nested in
another ODO - or other than the last item in a record.  Use of this
extension (although common in IBM environments) tends to lead to serious
"logic" AND portability problems.

Re:
 "Therefore, a program may  not contain more than 300 IF and EVALUATE
statements.  For purposes of automated standards checking, a warning will be
issued when the count exceeds 60% of the maximum, and an error when the
count exceeds 100%  of the maximum."
  This section bothers me - but I don't know your shop's resources or
"knowledge level".  However, if you ARE going to make this
requirement/recommendation, you need (IMHO) to make a suggestion on what to
do when the "complexity" gets too bad, what should they do?  Make a CALLed
subprogram? (dynamic or static CALL) or something else?  To me, when I got
called in at 3am, I preferred being able to look at a "single program" -
rather than tracing a complex CALL pattern.  However, as I say, this is just
MY opinion.

Question:
  Do you have an opinion or suggestion on internal versus external SORTs?
This may or may not be a "political" question - but having consistency
between applications MAY help maintenance.
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-03-06T10:04:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b482j2$18hj$1@si05.rsvl.unisys.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b46dn5$l7j$1@slb4.atl.mindspring.net...

>   ODO's.  Personally, I would "reverse" your recommendation concerning the
> default on OCCURS.  I would say that you should use a FIXED table (array)
> size - unless the size may vary at run-time.  I would also suggest that
you
> mention that using an OCCURS DEPENDING ON phrase (other than in the File
> Section) does *not* save storage and that the compiler ALWAYS allocates
the
> maximum size.  Finally, I would explicitly recommend the (IBM, Micro
Focus,
> etc) extension of allowing an OCCURS DEPENDING ON clause to be nested in
> another ODO - or other than the last item in a record.  Use of this
> extension (although common in IBM environments) tends to lead to serious
> "logic" AND portability problems.

I agree mostly; I *think* you meant "Finally, I would explicitly recommend
AGAINST the (IBM ...", and if you did, I would agree a great deal more.

 >  "Therefore, a program may  not contain more than 300 IF and EVALUATE
> statements.  For purposes of automated standards checking, a warning will
be
> issued when the count exceeds 60% of the maximum, and an error when the
> count exceeds 100%  of the maximum."
> This section bothers me - but I don't know your shop's resources or
> "knowledge level".

Since the compilers I deal with regularly compile monolithic programs of
VERY dense code with line counts approaching seven figures (not long ago I
resolved a compiler problem that only occurred with monolithic programs with
more than 65K active labels), the imposition of this particular limitation
strikes me as draconian!   To me a program doesn't even begin to qualify as
"large" until it's about 50K lines or so!   I understand the point, but the
limit can, as you point out, make for some complex binding, whether that
binding is a separate step or part of just-in-time run-time support  ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-06T12:39:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b484lf$gjr$1@slb5.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net> <b482j2$18hj$1@si05.rsvl.unisys.com>`

```
OOPS ...
  sorry for missing the "against" in my recommendation intended to say NOT
to use the IBM ODO extensions
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T15:37:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67DBB1.34564158@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net> <b482j2$18hj$1@si05.rsvl.unisys.com>`

```


Chuck Stevens wrote:

> correction to Bill's response snipped.

>
>  >  "Therefore, a program may  not contain more than 300 IF and EVALUATE
…[16 more quoted lines elided]…
>     -Chuck Stevens

Wow!  I sure would enjoy being responsible for those programs.

In our existing Standard Checker program, there is a mechanism for (1) handling
"old" programs, which reduces the severity level of some messages that would
fail a "new" program, and (2) excluding some programs entirely from following
the standards.  Surely your programs would be in the second list.

The lists are based upon the Program-Id, and cause constant pain, because people
clone bad old programs, change the Program-Id, and then cry and moan because
they are expected to follow good programming practices.  I try to tell them to
make the change in the first program, so that it works like it always did unless
a run time parameter, or an optional file, or some other mechanism tells it to
act differently in the new way they want.  The advice usually falls on deaf
ears.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T00:35:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e67bf53.120350433@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net> <b482j2$18hj$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:
>"William M. Klein" <wmklein@ix.netcom.com> wrote in message
>news:b46dn5$l7j$1@slb4.atl.mindspring.net...

> >  "Therefore, a program may  not contain more than 300 IF and EVALUATE
>> statements.  For purposes of automated standards checking, a warning will
…[13 more quoted lines elided]…
>binding is a separate step or part of just-in-time run-time support  ...

It is not draconian, it is anti-monolithic. To me, the threshold of 'large' is
1,000 lines. I generally try to stay under 300 lines -- six screen-fulls. 

I like the concept of measuring program size by decision points rather than
lines of code. I would argue to count each WHEN under an EVALUATE as a decision
point. Also, the UNTIL in a PERFORM should probably get half a point. 

My automated 'program quality calculator', mentioned in an earlier post,
essentially measured 'code density' as (conditionals + computes) / (total
procedural statements). The theory is that MOVEs and PERFORMs just shuffle data
and control around, whereas conditionals and computes produce new information.
In addition to code density, I gave points for 'expressiveness', measured by
average length of a data name. If I were writing it today, I'd spell-check each
fragment of a data name, giving points for words and deducting for
abbreviations. 

Robert
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T15:40:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67DC63.2252A99@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net>`

```
I've responded by e-mail to Bill, and am working on a significant revision of
the document.  My appreciation for his careful reading and many worthwhile
corrections and comments just needs to be on record to the Newsgroup.

We're lucky Bill cares enough to be here!
Colin
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T00:35:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e67b33f.117257158@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b46dn5$l7j$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>- Concerning GLOBAL, I would disallow the entire ability to use nested
>programs if you disallow GLOBAL data.  One of the major advantages of nested
>programs is the ability to distinguish between "local and global" data.

As Colin said, passing data this way violates the rules of structured
programming. If GLOBAL were permitted, some programmers would put it on every
single 01 level and never pass parameters. In the days of ANSI C, doing so was
common practice in C shops. 

>  Concerning the permitted USAGEs.  If your "ORG" is going to get into mixed
>COBOL and C applications, you may find that you need to expand what you say
…[4 more quoted lines elided]…
>values can be lost when floating-point comes in.

Floating point can be necessary when doing mathematical computations where
intermediate results exceed the COBOL limit of 18 digits. This happens, for
instance, when doing linear regression analysis, which is commonly used in the
financial industry. 


>Re:
>  ODO's.  Personally, I would "reverse" your recommendation concerning the
>default on OCCURS.  I would say that you should use a FIXED table (array)
>size - unless the size may vary at run-time.  

All tables vary. Most of them vary at run-time; the remainder, at maintenance
time. Consider a program containing a list of words: 

01  lexicon.
     05  filler value 'alpha'           pic  x(30).
     05  filler value 'beta'             pic x(30).
     .... (500 words)
     05  filler value 'zebra'           pic x(30).
01  filler redefines lexicon.
     05  word-entry occurs 503 indexed x-word pic x(30).

Now a maintenance programmer inserts ten new words, but forgets to change 503 to
513. The program just lost the last ten words in its vocabulary. Or (s)he gets
wrong and sets it to 510. The compiler doesn't issue a warning because the
second table is smaller than the first. Now picture a production support person
trying to figure out why the program doesn't recognize 'some' words. 

I write such tables this way:

01  word-count  value 1000 comp pic s9(04).
01  lexicon.
     05  filler value 'alpha'           pic  x(30).
     05  filler value 'beta'             pic x(30).
     .... (500 words)
     05  filler value 'zebra'           pic x(30).
     05  filler value high-values    pic x(30000).
01  filler redefines lexicon.
     05  word-entry occurs 1 to 1000  indexed x-word pic x(30).

if  word-count equal to 1000
    set x-word to 1
    search word-entry 
        at end display 'Word table too small' goback
        when word-entry (x-index) equal to high-values
             set word-count to x-index
    end-search
end-if

This eliminates the need to maintain a count. 

> To me, when I got
>called in at 3am, I preferred being able to look at a "single program" -
>rather than tracing a complex CALL pattern.  

The environment tells you which program it blew up in, especially when calls are
dynamic.  It is easier to look at a 100 line program than a 50,000 line program.
What you really want to know, of course, is the line number it blew up on. With
appropriate options set, IBM mainframe COBOL will give you that .. with no
penalty in execution speed. In that case, program size is irrelevant. Alas,
Micro Focus and others do not always give the line number. Your options are
running through thousands of records under the debugger, which can be slow, or
figuring it out logically aided by diagnostic DISPLAYs. 

Robert
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-06T04:58:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e66d513.60372784@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:

>I would appreciate any input any of you might want to provide concerning
>the document content, wording, etc.

I _love_ your standard. I'm the 'bad boy' in this newsgroup who protests 'code
police'. I  find nothing objectionable in your standard. I expecially liked the
prohibiton of GO TO rather than waffling around the once 'religious' issue. 

I wish all companies were so enlightened.
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-06T15:04:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303061504.3ba64a40@posting.google.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e66d513.60372784@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> I _love_ your standard. I'm the 'bad boy' in this newsgroup who protests 'code
> police'. 

No. You are the 'bad boy' for several reasons which you would probably
never understand, but one of them is that you want to _be_ the only
'code police'.
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T15:43:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67DD2E.A20FE39B@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e66d513.60372784@news.optonline.net>`

```
Thanks for your response.  I know you have posted some, shall I say, controversial
items here and taken some flack for it.  I want to say that I've read your posts,
and appreciate your efforts.

It remains to be seen whether the company accepts this proposed programming
standard, or, if they do, whether anyone follows it!

Robert Wagner wrote:

> Colin Campbell <cmcampb@attglobal.net> wrote:
>
…[7 more quoted lines elided]…
> I wish all companies were so enlightened.
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-06T17:55:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6789be.106630781@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:
 
>7. DISPLAY usage data items may be either numeric or alphanumeric
>(PICture characters 9 or X); alphabetic (PICture character A) items are
…[3 more quoted lines elided]…
>will be handled with proper decimal alignment, truncation, etc.

Suggested rewrite: 
If usage DISPLAY data item is a mathematical variable, it should be defined as
numeric. Alphanumeric should be used for numeric codes, such as ZIP code and
part 'number', and for compound numbers, such as dates. The reasons for this
rule are to reduce the chance of program termination when the field contains
non-numeric data, such as spaces, and to remove any temptation to convert the
data to BINARY or PACKED-DECIMAL. 

>8. BINARY (COMP) usage data items must have PICture descriptions of
>S9(4) or S9(8). Specifying 1 to 4 digits defines a binary halfword
>(16 bits); 5 to 9 digits defines a binary fullword (32 bits).
>Specifying over 9 digits defines a binary doubleword (64 bits).
>Depending on the platform, there may be performance implications

Typo: change S9(8) to S9(9). 

Omitting the sign may also have performance implications. 

>9. PACKED-DECIMAL (COMP-3) usage data items must have a PICture
>specifying a sign and an odd number of digits, such as S9(7)V99.
>Describing the same area without a sign or with an even number of
>digits causes less efficient code to be generated.  This rule
>initially applies to non-copied source code.

You might point out that more than 15 digits can have performance implications
on IBM mainframes. 

On most non-mainframe platforms, packed is as slow as display, so they might as
well use dispaly.  My standard recommends binary for all numbers in memory,
display for all numbers in files. 

>2. Highly complex program logic is discouraged.  The level of nesting
>within a procedure must not exceed 12; the preferred limit is 6.
>Nesting refers mainly to conditional statements contained within other
>conditional statements, such as IF within IF or IF within EVALUATE.
>Some compilers show the nesting level on the source code listing.

Your automated checker will find _many_ violations where IF .. ELSE IF was used
instead of EVALUATE. You might want to program it to look at the subject of the
IF, skipping statements where the same subject is repeated. 

>3. All procedures in a program must be coded either as paragraphs or
>as sections; in other words, a mix of sections and paragraphs is not
>allowed.

There is no reason to use sections. I would have said they are obsolete. 

>8. A program may have only one exit point.

This is theoretically correct, but inconsistant with earlier permission to use
EXIT PARAGRAPH (and EXIT PERFORM?) If they're allowed to jump out of a paragraph
due to poor structural design, they should be allowed to jump out of a program
as well. 

>9. The ACCEPT...FROM CONSOLE statement is prohibited. Operator
>communication is felt to be too error prone for use in production jobs.
…[6 more quoted lines elided]…
>environment.

These rules apply to batch jobs running on mainframes and large servers. They
don't apply to PC COBOL. 

>11. The only acceptable methods of controlling a loop in a program are
>SEARCH, SEARCH ALL, PERFORM...UNTIL, and PERFORM...TIMES. Note that
…[4 more quoted lines elided]…
>delimiter).

Citing another language in a COBOL standard is bad form. 

>13. Certain standard subroutines, if used, must be called dynamically.
>These subroutines are documented as needing to be called dynamically.
…[5 more quoted lines elided]…
>subroutines should provide the list to its programmers.

Don't limit it to "standard subroutines"; make all calls dynamic. An application
may have callable programs, for example file access modules, called from
hundreds of places. Dynamic call insures they all get the latest version. If a
program  is called by one program only, it should be embedded therein. If it is
separately compiled, that implies more than one caller.

Mainframers don't use make files. They have version control software which _may,
optionally_ know about dependencies. I've never seen that feature used. At every
mainframe shop where I've worked, people just 'remember' which programs need to
be relinked. They don't use version control because it is not accessible to
application developers, only to the administrator, who 'doesn't have time' to
maintain the list. 

> Attaching the standard checker to the compiler ensures
>that a programmer will know from the first compile of a program
>whether it violates standards, and will therefore not be accepted for
>production.

Bravo. All too often, under the old-fashioned process, standards violations are
detected _after_ a program was debugged, documented and tested. With a deadline
approaching (or missed), the revised program was not tested as thoroughly ..
perhaps not tested at all. 

I had a series of programs which had been in quasi-production five months. It
was 'quasi' because of a management freeze on program changes before and after
Y2K. We programmers weren't about to sit on our hands five months, so I ran the
new system myself, on production data. When it was about to go into 'real'
production, a team lead discovered I was using COBOL SORTs. That was 'bad' in
her private, unwritten standard. Probably because she'd had trouble getting a
SORT to work years earlier when she was a programmer, so put it on her list of
features to avoid. It didn't matter that the published shop standard (Merrill
Lynch) explicitly permitted SORT. It didn't matter that we had other production
programs using SORT. She made me restructure the whole system at the last
minute, leaving one day to run perfunctory tests before it went in. 

---------------------------------
Like most, your standard is primarily a list of don'ts. I suggest adding more
dos. After telling them what they're not allowed to do, provide an example of
how to do it right. Programmers prefer examples over words. 

Robert
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-06T19:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b486g8$cln$1@peabody.colorado.edu>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net>`

```

On  6-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> On most non-mainframe platforms, packed is as slow as display, so they might
> as
> well use display.  My standard recommends binary for all numbers in memory,
> display for all numbers in files.

I've read this for Intel, but it would be useful to know specifics here - not
just "most".  What are some of the other platforms Sun?  MacIntosh?


> This is theoretically correct, but inconsistant with earlier permission to use
> EXIT PARAGRAPH (and EXIT PERFORM?) If they're allowed to jump out of a
> paragraph
> due to poor structural design, they should be allowed to jump out of a program
> as well.

I've seen this theory used to disguise where the real problem is.  That is NOT
GOOD.


> They don't use version control because it is not accessible to
> application developers, only to the administrator, who 'doesn't have time' to
> maintain the list.

I wonder how I can bypass procedures in Endevor to become more current to what
mainframers do.


> Bravo. All too often, under the old-fashioned process, standards violations
> are
…[3 more quoted lines elided]…
> perhaps not tested at all.

I wonder how I can get my programs past the change control so that I can become
more current about what mainframers do.


> That was 'bad' in
> her private, unwritten standard. Probably because she'd had trouble getting a
> SORT to work years earlier when she was a programmer, so put it on her list of
> features to avoid.

I have seen that here - people wanting a standard to eliminate periods because
they caused problems years earlier when coding styles were different.
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T16:04:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67E207.42D3443B@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net>`

```
My responses are interspersed below.  Thanks.

Robert Wagner wrote:

> Colin Campbell <cmcampb@attglobal.net> wrote:
>
…[13 more quoted lines elided]…
> data to BINARY or PACKED-DECIMAL.

Not a bad suggestion; I'll work on this section.

>
>
…[6 more quoted lines elided]…
> Typo: change S9(8) to S9(9).

An IBM "performance" document claims that S9(9) can cause poor performance.  You can
find this document at http://www-3.ibm.com/software/awdtools/cobol/, then follow the
Library link.  You should see three performance guides on the next page.

>
>
…[9 more quoted lines elided]…
> on IBM mainframes.

Yes, I'll add that.

>
> On most non-mainframe platforms, packed is as slow as display, so they might as
…[11 more quoted lines elided]…
> IF, skipping statements where the same subject is repeated.

You're right, it does.  However, it also has a mechanism for dealing with "old"
programs.  In addition, converting the "IF ... ELSE" form of the Case statement to
an EVALUATE is quite simple.  Insert an EVALUATE TRUE before the first IF, change
all the IF's to WHEN's, drop the ELSE's, and add END-EVALUATE at the end (replacing
the period that is almost certainly there).

>
> >3. All procedures in a program must be coded either as paragraphs or
…[3 more quoted lines elided]…
> There is no reason to use sections. I would have said they are obsolete.

One possible reason is when using the Debugging Mode.

>
>
…[5 more quoted lines elided]…
> as well.

Gotta be tough with these programmers (part of the time, anyway).

>
>
…[11 more quoted lines elided]…
> don't apply to PC COBOL.

More of my mainframe bias showing.  I'm going to have to figure out how to manage
this in the "multi-platform" standard.

>
>
…[8 more quoted lines elided]…
> Citing another language in a COBOL standard is bad form.

I guess you mean the DO...WHILE and DO...UNTIL.  This is the way Structured
Programming describes looping, as best I can recall.  I didn't mean to pay homage to
PL/1 or other languages.

>
>
…[13 more quoted lines elided]…
> separately compiled, that implies more than one caller.

A blanket statement on CALL's wouldn't be right in my view.  I have seen run units
whose CPU time could be cut by 15% or more by changing dynamic CALLs to static
CALLs.  I think there are implications on other platforms, such as building DLL's
and EXE's, but I'm only a visitor to these environments.

>
>
…[5 more quoted lines elided]…
> maintain the list.

Our shop uses CA-Endevor, and there are plenty of tools that applications progs can
use to search out all users of a subroutine, for example.  In addition, there are
tools for the mainframe, like Edge Portfolio Analyzer, that help with this.  Not
having this tool, I've written programs to show the contents of all load modules in
a library, and easily capture change control information for a subroutine.

>
>
…[25 more quoted lines elided]…
> how to do it right. Programmers prefer examples over words.

You are one of several who have made similar suggestions.  I will ask to be allowed
to supply a "Style Guide" as well as a Programming Standard.  However, I feel that
programmers MUST be told what usages the company will not accept in their code.

>
>
> Robert
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T04:04:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e67ffed.136890801@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:


>> >8. A program may have only one exit point.
>>
>> This is theoretically correct, but inconsistant with earlier permission to
use
>> EXIT PARAGRAPH (and EXIT PERFORM?) If they're allowed to jump out of a
paragraph
>> due to poor structural design, they should be allowed to jump out of a
program
>> as well.
>
>Gotta be tough with these programmers (part of the time, anyway).

They will pick up logical inconstituancies and use them against you. Remember,
they're clutching at straws. 

If EXIT PARAGRAPH is ok, then EXIT PROGRAM or GOBACK should also be ok. I have
no strong opinion on this, just trying to support your effort, which I applaud. 

>> Mainframers don't use make files. They have version control software which
_may,
>> optionally_ know about dependencies. I've never seen that feature used. At
every
>> mainframe shop where I've worked, people just 'remember' which programs need
to
>> be relinked. They don't use version control because it is not accessible to
>> application developers, only to the administrator, who 'doesn't have time' to
>> maintain the list.
>
>Our shop uses CA-Endevor, and there are plenty of tools that applications progs
can
>use to search out all users of a subroutine, for example.  

You didn't mention that your Endevor knows about dependencies. It _could_ but it
doesn't, which is the point I made. 

Endevor keeps source encrypted in VSAM files. Endevor searches are horribly
slow. Most shops keep a copy of source in cleartext to facilitate searching with
widely available tools such as FileAid. 

>In addition, there are
>tools for the mainframe, like Edge Portfolio Analyzer, that help with this.
Not
>having this tool, I've written programs to show the contents of all load
modules in
>a library, and easily capture change control information for a subroutine.

"Not having this tool" is the key phrase. Applications programmers don't have it
either. They must 'remember' (or not) which programs call another. The process
is highly error-prone. Dynamic calls solves the problem. 

>> Like most, your standard is primarily a list of don'ts. I suggest adding more
>> dos. After telling them what they're not allowed to do, provide an example of
>> how to do it right. Programmers prefer examples over words.
>
>You are one of several who have made similar suggestions.  I will ask to be
allowed
>to supply a "Style Guide" as well as a Programming Standard.  However, I feel
that
>programmers MUST be told what usages the company will not accept in their code.

That's necessary in large companies. In medium-sized companies, I prefer a
mentoring approach which teaches them how to do it right rather than slapping
their hands for doing it wrong. 

The threshold for large vs. medium is $1B annual sales. Is your client large or
medium-sized?

Robert
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-03-07T06:46:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6840C6.6A68358C@worldnet.att.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net>`

```
Colin Campbell wrote:
> (snip)
> Robert Wagner wrote:
…[10 more quoted lines elided]…
> and EXE's, but I'm only a visitor to these environments.

I work in a z900 shop with Endevor and the default option is DYNAM for
everything but CICS compile processors.  A colleague of mine did
extensive performance testing of dynamic calls using
Procedure-Pointers and External data, and proved to his satisfaction
that they were faster than static calls.  The CALL overhead was the
same as PERFORMing a paragraph.

I posted something about this in here in clc several months ago, and
eventually had an email exchange with Tom Ross and WMK.  Initially,
Tom Ross (one of the developers of IBM COBOL for OS/390 & VM) was
skeptical that the call was truly dynamic.  It will be if the caller
is compiled with the DYNAM option.  
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-07T21:30:34+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b49lga$id5$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net>`

```
Arnold Trembley wrote:

> I work in a z900 shop with Endevor and the default option is DYNAM for
> everything but CICS compile processors.  A colleague of mine did
…[3 more quoted lines elided]…
> same as PERFORMing a paragraph.

The overhead is on the first CALL to a routine if it has to be dynamically 
loaded.  I can quite believe that once it has been loaded then subsequent 
CALLs will be to the loaded module.

Presumably the use of procedure-pointer was to pre-load the module, CALLs 
using this may be fast, but what was the cost of the load ?
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-03-07T09:18:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E68643C.5D480A9E@worldnet.att.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net> <b49lga$id5$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> Arnold Trembley wrote:
…[13 more quoted lines elided]…
> using this may be fast, but what was the cost of the load ?

I do not know what the cost of the load was, but my colleague's
testing did 100 million calls to the same routine.  He compared the
timing of 100 million dynamic Procedure-pointer calls with external
data, to 100 million dynamic calls with linkage section parameters, to
100 million static calls with linkage section parameters.  The dynamic
procedure pointer calls with external data used the least amount of
CPU time.

> Here's the ranking, from fastest to slowest:
>
…[5 more quoted lines elided]…
> Call Var, Linkage     102.17 CPU seconds (DYNAM, call program-name, linkage section parms)

He tested using IBM COBOL for MVS & VM, release 1.2.2.  I would expect
performance to be almost identical with IBM COBOL for OS/390 & VM, and
IBM Enterprise COBOL for z/OS.  Basically, a repetive DYNAMIC
procedure-pointer call using EXTERNAL data is about twice as fast as a
repetitive static call using linkage section parameters.

Certainly there is some overhead for the SET PROCEDURE-POINTER TO
ENTRY 'MYPROG', but if the subprogram is called repetitively the
initial cost is negligible.  If the subprogram is only called once,
then a dynamic call still might still be preferred to allow separate
compilation and installation of components.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-08T08:13:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4ar67$2hb$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net>`

```
Arnold Trembley wrote:

>> Presumably the use of procedure-pointer was to pre-load the module, CALLs
>> using this may be fast, but what was the cost of the load ?
…[7 more quoted lines elided]…
> CPU time.

Maybe.  But the whole point about dynamic loading is that at the first CALL 
(or when the preload is started) the program is on the disk.  This involves 
all the find and load time plus OS overhead for creating a memory area for 
it.

With static loading the program is part of what is loaded so the load 
overhead is negligable.

For a program that is called a million times (without cancel) the load time 
is irrelevant.  However, many programs may be called just once.

If you use EXTERNAL data then you may be removing re-uability from the 
called program.  On my systems the EXTERNAL data must match exactly in 
size.  You could arrange that each CALLed program had its own EXTERNAL 
block but if the program is to be CALLed in two systems you need to arrange 
somehow that it will match.

The other problem is that it may be necessary to copy data to and from the 
EXTERNAL data while different CALLs with parameters may be able to specify 
different data areas rather than copy.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T01:28:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e694724.65114007@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Arnold Trembley wrote:
>
…[20 more quoted lines elided]…
>is irrelevant.  However, many programs may be called just once.

I have an interactive application which  dynamically-calls 30 programs per
transaction, one time each.. Execution time is less than 100 milliseconds. How
much faster do you want?

If another user runs the same application shortly thereafter, it's much faster
because Unix has cached the callable programs. Memory and cache management is
the operating system's job, not the application programmer's. The days when we
tweaked the machine are gone. Design applications for the business requirement
and let the OS take care of optimization. 

Robert
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-08T16:17:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4bnic$ejq$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net>`

```
Robert Wagner wrote:

> I have an interactive application which  dynamically-calls 30 programs per
> transaction, one time each.. Execution time is less than 100 milliseconds.
> How much faster do you want?

The 'execution time' is the CPU and does not include the disk time required 
for the dynamic load.

> If another user runs the same application shortly thereafter, it's much
> faster because Unix has cached the callable programs. 

It won't be 'much faster' than the 100 ms because they are measuring 
different things.  The cache doesn't save a user program CPU time, only 
clock time.

> Design
> applications for the business requirement and let the OS take care of
> optimization.

While you may well have trivial little applications that only take 100 ms 
to run, some systems may take hours to run each day.  Optimising a system 
so that the run time reduces by a small percentage may make the difference 
between getting the job done every day or not.

In some cases the resource usage (such as time) is part of the 'business 
requirement'.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T04:39:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6973fd.76597340@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[5 more quoted lines elided]…
>for the dynamic load.

Forgive my imprecision. 100 milliseconds is the wall-clock time on a
single-processor Sun server. 

>> Design
>> applications for the business requirement and let the OS take care of
…[5 more quoted lines elided]…
>between getting the job done every day or not.

My 'trivial little application' does in milliseconds what used to take
minutes-to-hours of manual manipulation with Excel and other tools. We're still
doing it manually in Manila, Philippines, at $3/hour. That will change soon.
Here in New York, staff has been reduced 50%.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-08T18:12:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4bu9v$hf3$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6973fd.76597340@news.optonline.net>`

```
Robert Wagner wrote:

>>> Design
>>> applications for the business requirement and let the OS take care of
…[3 more quoted lines elided]…
> minutes-to-hours of manual manipulation 

The point being that design decisions for something that takes a fraction 
of a second, or even a few minutes may well, or in fact should, ignore such 
issues as optimising, as you say.

You, however, appear to want to generalise this 'gem' of advice into all 
areas (as you would) regardless of the actual needs, or the appropriateness 
of your aphorism.

With your: "Execution time is less than 100 milliseconds. How much faster 
do you want?": 

Are you implying that if you were to rewrite Arnold's system that it would 
only take 100 ms to run, instead of hours ?  

Are you bragging that your system is faster than anyone else's (when in 
fact the task of yours is trivial) ?

Have you built static linked versions and demonstrated that these are no 
faster?

Have you used procedure pointers and externals and compared how a few 
million calls would compare ?
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T17:59:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6a20b3.120818208@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6973fd.76597340@news.optonline.net> <b4bu9v$hf3$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>Are you implying that if you were to rewrite Arnold's system that it would 
>only take 100 ms to run, instead of hours ?

Of course not, but I've seen an 18 hour job improved to run in 2 hours. The
changes were in high level design, not low level bit-twiddling.

>Are you bragging that your system is faster than anyone else's (when in 
>fact the task of yours is trivial) ?

A trivial task does not comprise 30 programs embracing 20,000 lines of code. 

>Have you built static linked versions and demonstrated that these are no 
>faster?

No, because static linking is against my religion. :>

When I measured call speed in the past, I found dynamic about five times slower
than static. Code was doing a table lookup on every call to see whether the
target was loaded. You probably would have changed that to a hashing algorithm.
My solution was not abandonment of dynamic calls, it was software which made
them run _faster_ than static calls. It's called 'thinking outside the box.' I'm
pleased to see IBM finally got it right. 

>Have you used procedure pointers and externals and compared how a few 
>million calls would compare ?

Passing parameters via the linker flies in the face of everything holy. If
parameter passing time were an issue, I'd call another entry point with
parameters the first time and have the called program remember them in local
base pointers. This takes no effort because it is normal behavior. On subsequent
calls, I wouldn't pass any parameters. 

Robert (Script Kiddie #4)
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T16:16:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6a0283.113088425@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>While you may well have trivial little applications that only take 100 ms 
>to run, some systems may take hours to run each day.  Optimising a system 
…[4 more quoted lines elided]…
>requirement'.

Here is an example of that kind of thinking, and its antithesis. 

The Sears payroll system handled 400K active US employees. It was written 100%
in assembly language. Files were all sequential. The window for getting checks
out -- the business requirement -- was five hours. If jobs ran longer, checks
would miss airplane schedules. Therefore, the whole system was designed for
maximum speed during the weekly check run.The jobs actually ran in 2-2.5 hours,
on the fastest business-class mainframes in the US .. two running in parallel.
There was time for one rerun. 

Because of Y2K, management decided to move the function to an ERP behemouth:
Peoplesoft using Informix databases. Old-timers laughed, saying it couldn't
possibly run fast enough. They were hysterical when the first volume test
indicated a run time of 1.5 weeks. I should mention that Peoplesoft is written
in COBOL, and the size of the databases was more than double that of any
previous Peoplesoft deployment. 

In the end, Peoplesoft produced checks in 2-3 hours. How? By tuning databases
and distributing the work over twenty machines running in parallel, assisted by
a business decision to issue checks bi-weekly. The five-dollar word for these
solutions  is "scalability".

Old-timers cleaned out their desks and sulked off. 

A related, more generic example comes to mind. It is widely believed that
databases cannot match the speed of ISAM-style files.  Perhaps I should have
said COBOL-style files because of the close association between the language and
file structure. The premise is sometimes false, because database optimizers
split queries into subqueries which can run in parallel. Modern mainframes and
servers typically have 10-50 processors. COBOL programs exploit only one
processor. Moreover, databases are easily optimized by creating new indexes.
Doing the same in COBOL requires changing source code and logic in each affected
program. When the expense of testing and methodology overhead is factored in,
cost usually exceeds benefit. Further, locating optimization opportunities is
more difficult in COBOL, because files are typically administered by application
programmers who lack the prioritization, experience and statistics-gathering
tools to do it effectively. 

Robert (aka Script Kiddie #11)
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-09T06:47:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4dag5$8nh$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net>`

```
Robert Wagner wrote:

> actually ran in 2-2.5 hours, on the fastest business-class mainframes in
> the US .. two running in parallel. There was time for one rerun.
…[9 more quoted lines elided]…
> databases 

Otherwise know as 'optimising', something you said shouldn't be done.

> and distributing the work over twenty machines running in
> parallel, 

> assisted by a business decision to issue checks bi-weekly. The
> five-dollar word for these solutions  is "scalability".

And the ten dollar word is 'cost overrun'.

As you say the process went from 2 machines to 20 machines.  The cost 
increased 10 fold.

Changing to biweekly halved that (based on original being weekly), back to 
only 5 times the cost.  Of course paying two weeks wages produces its own 
problems.  When it changes either the employees just skip a week and suffer 
no money until they get two weeks pay, or the company pays one week arrears 
and one week advance and have to find/borrow a weeks payroll.
 
> Old-timers cleaned out their desks and sulked off.

Mainframe salesmen rolled in their commissions.

Meanwhile other companies, not wanting to spend extra millions on 
computers, give their programmers a few hundred dollars to save some hours.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T20:27:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6a4a3d.131453243@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <b4dag5$8nh$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[10 more quoted lines elided]…
>And the ten dollar word is 'cost overrun'.

There was no overrun. The project completed ahead of schedule.

>As you say the process went from 2 machines to 20 machines.  The cost 
>increased 10 fold.

It went from 2 monster mainframes to 20 Unix machines. There was a significant
reduction in operating expense. The cost of disk storage, alone, saved $50M per
year. Mainframes were not fixed overhead because they weren't company-owned; we
had been buying time and DASD from IBM Global Services. Shortly thereafter, IBM
put Global Services on the auction block. 

>Changing to biweekly halved that (based on original being weekly), back to 
>only 5 times the cost.  Of course paying two weeks wages produces its own 
>problems.  When it changes either the employees just skip a week and suffer 
>no money until they get two weeks pay, or the company pays one week arrears 
>and one week advance and have to find/borrow a weeks payroll.

Yes, they advanced one week and collected it back with deductions over the
following year. 

>> Old-timers cleaned out their desks and sulked off.
>
>Mainframe salesmen rolled in their commissions.

The beneficiaries were Peoplesoft salesmen .. and us contractors. :> Long-term
beneficiaries will be company stockholders.

>Meanwhile other companies, not wanting to spend extra millions on 
>computers, give their programmers a few hundred dollars to save some hours.

In 1999, their programmers were busy fixing Y2K problems caused by .. wait for
it .. the company's own programmers. They could have used Y2K as an opportunity
to modernize _and_ reduce cost _and_ solve the Y2K problem, thereby killing
three birds with one stone. Instead, they stomped out little fires.

Robert
```

###### ↳ ↳ ↳ Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 10)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-03-10T21:51:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6D4112.A746463F@istar.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net>`

```
The posting below brings up several interesting points which I will
address with comments interspersed below.

Robert Wagner wrote:
> 
> Richard Plinston <riplin@Azonic.co.nz> wrote:
…[17 more quoted lines elided]…
> There was time for one rerun.

NOTE that this was probably written in the 1960's or 1970's when a large
system had 16 megabytes and at most 4 processors. The system would have
met the 2.5 hour criteria THEN.  In the late 1990's for that same
volume, the same system would be on one mainframe which might have 8 or
more processors, each of which had more power than the processor complex
of the 1970's and probably took 1 - 1.5 hours running concurrently with
other systems.  Faster disk and more more buffering would have helped.
Tuning might have cut this further.
> 
> Because of Y2K, management decided to move the function to an ERP behemouth:
…[9 more quoted lines elided]…
> solutions  is "scalability".

Lets see, we are now using 20 machines, not one to produce the checks. 
Of course we can't run this on a mainframe with the appropriate database
manager (in 199x, Peoplesoft may not have been ported to the
mainframe).  We are running bi-weekly rather than weekly thus possibly
getting a financial advantage (the company gets to keep its money
longer).  From a sheer performance point of view, for that function
Peoplesoft comes out the loser.  This does not necessarily mean it was a
bad decision although it still may be a bad implementation.  Presumably
Sears upgraded to a combined HR/Payroll system that could produce HR
information in real time.  Since Peoplesoft is known for providing
Enterprise R? P? software, the new system may be providing far more
information that enables the company to assign people better and keep
track of costs better because the time worked, and maybe assigned is
being handled and updated on a daily (or more frequent) basis. The
company gained in being able to outsource the maintenance and updating
of the system to Peoplesoft and by getting the payroll system out of
assembler given the paucity of assembler programmers.   
> 
> Old-timers cleaned out their desks and sulked off.

What you are saying is that assembler programmers didn't want to become
people who just did rote application of changes supplied by Peoplesoft. 
Somehow, I suspect that they were given golden handshakes and took them
gladly in the best scenario or were forced out in the worst.
> 
> A related, more generic example comes to mind. It is widely believed that
…[11 more quoted lines elided]…
> tools to do it effectively.

Let me disabuse the readers on this newsgroup about ISAM files being
COBOL style files.  ISAM (currently implemented as VSAM by IBM) was a
part of the operating environment for IBM mainframes and I would assume
on the Burroughs, Univac, NCR, and RCA systems.  I don't know how VAX
VMS handled them and it would be interesting to hear from people who
used non-IBM systems in the 1960's and 1970's.  ISAM was an add-on to
the Microsoft and Unix systems.  It was added to both systems before
relational databases became generally available or supportable in those
environments.  Indeed the first uses of these file organizations in
those environments were probably by non-COBOL programs.  Since the
environment didn't provide the access method (in the case of Unix
probably because of the scientific and non-business heritage and PC's
because of the original usage), there were many incompatible
implementations of the function.  Relational databases now have
acceptable performance for business functions because of the quantum
leaps in memory available and disk speed increases.  Databases offer a
number of advantages in designing an application, provision of standard
facilities for integrity, and granularity of access.  The query
capabilities are better.  These advantages come at a noticeable CPU
cycle cost and I-O or main memory cost.  These costs are more than
acceptable in most cases because CPUs are much faster as are memory
speeds and I-O speeds, all for less money.  However, note the amount of
tuning that had to be done to tame that Peoplesoft application.  

The individual COBOL CICS or IMS transaction can only use one processor
as can the batch program.  However, many copies of the transactions can
be running concurrently with some versions of CICS being able to use
more than one processor.  In addition COBOL programs accessing DB2 can
take advantage of all the optimization given to SQL statements.  The
single CPU limitation isn't a problem for Peoplesoft (or in-house
database applications) because the operating system takes care of it. 
In the case of 20 servers, how many CPUs were on each server?  

> 
> Robert (aka Script Kiddie #11)
```

###### ↳ ↳ ↳ Re: Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-11T12:39:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6dc0ce.94462376@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <3E6D4112.A746463F@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:

>The posting below brings up several interesting points which I will
>address with comments interspersed below.
>
>Robert Wagner wrote:

>> The Sears payroll system handled 400K active US employees. It was written
>>100% in assembly language. ...
…[8 more quoted lines elided]…
>mainframe).  

They blamed the speed problem on Informix, not Peoplesoft. The solution was to
partition the database with each partition on a separate disk. The reason for
using 20 machines was not so much raw cpu speed, rather so 20 partitions could
be processed in parallel. Yes, it could have been done with 20 tasks running in
a single box, each task on its own cpu. Perhaps it is run that way now. At the
time, with a deadline approaching, we didn't want to take the chance of
encountering another bottleneck. 

They said this wouldn't have been a problem if Sears had chosen Oracle rather
than Informix. The story is that Oracle was the first choice. A Sears VP
requested a personal meeting with Oracle CEO Larry Ellison, which was turned
down. In retaliation for the snub, the company chose Informix. 

At another shop where I worked, we routinely processed Informix databases
containing 30 million rows. Informix is at least as fast as Oracle. I suspect
the real problem was in Peoplesoft table design or database 'extensions'.
Peoplesoft fancies themselves to be database experts and has a division of the
company which does nothing but write add-ons (in C). 

>We are running bi-weekly rather than weekly thus possibly
>getting a financial advantage (the company gets to keep its money
>longer).  

Yes, they cited that as competitive issue, noting that their competitors were
already bi-weekly. 

>> Old-timers cleaned out their desks and sulked off.
>
…[3 more quoted lines elided]…
>gladly in the best scenario or were forced out in the worst.

They were offered training in the Peoplesoft report writer. Some went that way,
others took the golden handshake. 

>> A related, more generic example comes to mind. It is widely believed that
>> databases cannot match the speed of ISAM-style files.  
…[5 more quoted lines elided]…
>the Microsoft and Unix systems. 

VSAM is an add-on to IBM, as well. It was originally developed by a company
named IDC, whose name can still be seen in IDCAMS. Perhaps one of the veterans
here can recall what IDC stood for; I've forgotten. 

For years, VSAM did its own catalog management. If it was part of the operating
system, it would have been using the operating system's directory.

>The
>single CPU limitation isn't a problem for Peoplesoft (or in-house
>database applications) because the operating system takes care of it. 
>In the case of 20 servers, how many CPUs were on each server?  

It's irrelevant because a COBOL program uses only one .. except, as you said,
when doing database access.

Robert
```

###### ↳ ↳ ↳ Re: Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 12)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-11T14:28:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D13904EAEB3AA73D.59C6F01CDC7BCB3E.19F5FC6FA73CDB0E@lp.airnews.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <3E6D4112.A746463F@istar.ca> <3e6dc0ce.94462376@news.optonline.net>`

```
On Tue, 11 Mar 2003 12:39:31 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:
>
…[77 more quoted lines elided]…
>Robert

The first release of VSAM was shipped in 1973. It was introduced with
System/370.  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #109

Program aborting:
Close all that you have worked on.
You ask far too much.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ VSAM and multitasking was Re: Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 12)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-03-18T15:46:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E7777B2.D98D8D35@istar.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <3E6D4112.A746463F@istar.ca> <3e6dc0ce.94462376@news.optonline.net>`

```
Note there will be much snipping leaving just enough of the previous
posting to address the specific disagreements. Because of the IBM
mainframe connection, I am adding bit.listserv.ibm-main to the groups in
case of further clarification by posters more knowledgeable than I
am.    

Robert Wagner wrote:
> 
> "Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:
…[10 more quoted lines elided]…
> others took the golden handshake.

As I said, they didn't want a job downgrade.

> 
> >> A related, more generic example comes to mind. It is widely believed that
…[13 more quoted lines elided]…
> system, it would have been using the operating system's directory.

VSAM was a follow on to ISAM.  At the same time IBM introduced catalogs
to VSE and a new form of catalog to OS-SVS and its follow-on MVS.  The
master catalog for the system had to be a VSAM catalog in MVS.  CVOLs
could only handle non-VSAM.  While VSAM was new and may have been
developed in whole or in part by outside contractors, it was a
fundamental access method starting at its introduction.  The integrated
catalog facility was an improved version of the original function that
was designed to truly supersede both its predecessor and CVOLs.  
> 
> >The
…[5 more quoted lines elided]…
> when doing database access.

I believe that Enterprise COBOL for OS390 and z/OS can multithread. 
Depending on how much multitasking CICS can do multiple instances of the
same transaction code can be running concurrently and the same is
probably true of the data communication (transaction processing
component) part of IMS.
> 
> Robert
```

###### ↳ ↳ ↳ Re: VSAM and multitasking was Re: Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-18T14:21:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b57v3s$udb$1@slb2.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <3E6D4112.A746463F@istar.ca> <3e6dc0ce.94462376@news.optonline.net> <3E7777B2.D98D8D35@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3E7777B2.D98D8D35@istar.ca...
<snip>
> >
> > It's irrelevant because a COBOL program uses only one .. except, as you
said,
> > when doing database access.
>
…[7 more quoted lines elided]…
>

Just to confirm that Enterprise COBOL *does* support Multi-threading.
Furthermore, it supports "serialization" of I/O.  See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/4.4.4
```

###### ↳ ↳ ↳ Re: Optimization was Re: Please help -- COBOL Programming Standard

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-11T14:30:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303111430.5b8b1c79@posting.google.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b49lga$id5$1@aklobs.kc.net.nz> <3E68643C.5D480A9E@worldnet.att.net> <b4ar67$2hb$1@aklobs.kc.net.nz> <3e694724.65114007@news.optonline.net> <b4bnic$ejq$1@aklobs.kc.net.nz> <3e6a0283.113088425@news.optonline.net> <3E6D4112.A746463F@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote

> Let me disabuse the readers on this newsgroup about ISAM files being
> COBOL style files.  ISAM (currently implemented as VSAM by IBM) was a
…[3 more quoted lines elided]…
> used non-IBM systems in the 1960's and 1970's. 

On ICL 1900 the ISAM was 'Direct Access Housekeeping' and was
initially used from the assembler PLAN3 with macros. The Cobol that I
originally used in 1968 (XE13) was ANSI'61 which had no disk access so
the disk files were accessed using CALLs to the DA Housekeeping
package.

ANSI'68 introduced a 'Random Access module' and this was available to
me in ICL compilers (XE20?) around 1970.  ANSI'74 completely replaced
this with 'Indexed I-O' and 'Relative I-O' modules (XEA3).

> ISAM was an add-on to
> the Microsoft and Unix systems.  It was added to both systems before
> relational databases became generally available or supportable in those
> environments.  Indeed the first uses of these file organizations in
> those environments were probably by non-COBOL programs. 

One of the first Unix ISAM file systems that was generally used was
C-ISAM which was the base system for the original Informix (pre-SQL). 
This was primarily used from C programs, as well as from Informix
programs.

C-ISAM was adopted by X-Open and thus found its way into Cobol on
Unix, as well as on some non-Unix Cobols.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T12:21:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e688ec4.17907575@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net>`

```
Arnold Trembley <arnold.trembley@worldnet.att.net> wrote:

>Colin Campbell wrote:
>> (snip)
>> Robert Wagner wrote:
>> > (snip)
>> > Don't limit it to "standard subroutines"; make all calls dynamic. An
application
>> > may have callable programs, for example file access modules, called from
>> > hundreds of places. Dynamic call insures they all get the latest version.
If a
>> > program  is called by one program only, it should be embedded therein. If
it is
>> > separately compiled, that implies more than one caller.
>> 
>> A blanket statement on CALL's wouldn't be right in my view.  I have seen run
units
>> whose CPU time could be cut by 15% or more by changing dynamic CALLs to
static
>> CALLs.  I think there are implications on other platforms, such as building
DLL's
>> and EXE's, but I'm only a visitor to these environments.
>
…[11 more quoted lines elided]…
>is compiled with the DYNAM option.  

It would be interesting to see a comparison of dynamic call vs. CICS LINK. For
the benefit of non-mainframers, LINK is CICS' dynamic call feature.

In the '80s, I wrote a memory manager which front-ended CICS, intercepted LINKS
(and other memory-related functions), turned them into my own version of dynamic
call. The improvement was 120 times faster per call. On the first call, I
reached back and modified inline code so that subsequent calls were similar to
perform.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-03-08T09:19:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E69B601.E94F3B0D@worldnet.att.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net> <3e688ec4.17907575@news.optonline.net>`

```
Robert Wagner wrote:
> (snip)
> It would be interesting to see a comparison of dynamic call vs. CICS LINK. For
…[6 more quoted lines elided]…
> perform.

IBM has been recommending dynamic calls in CICS in place of EXEC CICS
LINK for several years now.  I don't have their performance numbers at
hand right now, but there is a significant performance improvement. 
We have a few critical paths in some of our CICS programs where we
have replaced LINK with dynamic calls.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T17:59:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6a19be.119036595@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net> <3e688ec4.17907575@news.optonline.net> <3E69B601.E94F3B0D@worldnet.att.net>`

```
Arnold Trembley <arnold.trembley@worldnet.att.net> wrote:

>Robert Wagner wrote:
>> (snip)

>> In the '80s, I wrote a memory manager which front-ended CICS, intercepted
LINKS
>> (and other memory-related functions), turned them into my own version of
dynamic
>> call. The improvement was 120 times faster per call. On the first call, I
>> reached back and modified inline code so that subsequent calls were similar
to
>> perform.
>
…[4 more quoted lines elided]…
>have replaced LINK with dynamic calls.

I'm aware of that. IBM also permits vanilla, batch-style file IO. But Back In
The Days, doing these things was a big time hand-slap. Also, they simply didn't
work .. not reliably in a large-scale CICS partition. If they had, there would
have been no need to write my own. 

Do you know how much faster the changed programs run?

Speaking of COBOL and CICS .. one of my friends rewrote CICS in 100% COBOL, then
sold it to Merant, who published it as "CICS for OS/2". Few customers were aware
that it was written in COBOL. It ran significantly faster than IBM's CICS,
written in assembly language, on comparable platforms. It was so much faster
that PCs were outperforming mainframes, causing some customers to run production
on PCs, which were originally intended to be the test environment. Needless to
say, IBM derided the practice as amateurish. An IBM salesman and branch manager
actually tried to get me fired after I showd them test results. Everyone knows
that a 'real professional' throws big bucks into the IBM coffer. Don't they?

Robert (Script Kiddie #3)
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-03-07T09:42:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4allv$8r$1@si05.rsvl.unisys.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <3e6789be.106630781@news.optonline.net> <3E67E207.42D3443B@attglobal.net> <3E6840C6.6A68358C@worldnet.att.net>`

```
"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message
news:3E6840C6.6A68358C@worldnet.att.net...

> I work in a z900 shop with Endevor and the default option is DYNAM for
> everything but CICS compile processors.  A colleague of mine did
…[3 more quoted lines elided]…
> same as PERFORMing a paragraph.

An implementation-specific point, by no means universal.  What I would call
"dynamic" CALLs -- "CALL <dataname>" -- are MUCH, MUCH slower than what I
would call "static" CALLs -- "CALL <literal>" on Unisys MCP/AS systems.  The
latter, once the first CALL has been successfully made and the library
linked, there's no difference between a CALL on an external program and a
CALL on a nested one, and both such CALLs are as efficient as ALGOL/PASCAL
procedure calls.    (Note that that implementation does not use any sort of
pre-execution "bind" process for ANSI-IPC-style CALLS outside the program
*at all*.  Whatever the linkage is occurs at execution time.)

    -Chuck Stevens
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-06T15:31:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b48emp$re8$1@slb9.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
"Colin Campbell" <cmcampb@attglobal.net> wrote in message
news:3E669F8D.E69F28E3@attglobal.net...

  <all of the original note snipped>

I just thought that I would raise some OTHER areas that might be addressed
in this type of document (and knowing the TYPE of shop that Colin is in -
but not knowing his shop's specifics).  These are ONLY items to consider -
not saying that these recommendations would fit ALL or even his shop's
needs.

1) Default compiler options should be used.  When *NOT* used, specific
"sign-off" should be required to explain WHY the default isn't appropriate.
Any required "modifications" to the default options should be recorded
within the source code - as well as in "external" documentation.

2) Programs should be compiled with the HIGHEST level of messages produced
(e.g. FLAG(I,I) in IBM mainframe compiles).
  - Programmers should be required to "sign-off" on understanding all
I-level (informational) messages produced
 - Programmers' MANAGERS should be required to sign-off on all W-level
(warning) messages produced.  (Some of these might turn out to be "common
enough" that they would get a blanket approval - but these are probably few
in number)
 - Production level programs should NEVER be installed with "above" W-level
messages (e.g. by "link-editing with condition code 8 - in IBM mainframe
shops)

3) A "shop standard" should exist for where "modification" changes are
recorded (within the source code).  There should be a consistent method
(e.g. latest always at the top - or always at the bottom) and no modified
program should be placed back into production without management review of
the WORDING of such modification records.

    ***

Because Colin mentioned conformance to both the '85 Standard and use of some
*new* features in the 2002 Standard - and the relationship between these two
and IBM extensions, I would point to the following online documentation:

   "Appendix A. IBM extensions"

at:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR10/APPENDIX
1.1

Chuck, Thane, or others might be able to correct me, but I *believe* that
all of the following are extensions to the '85 ('89 & '91) ANSI/ISO
Standards that become standard in the 2002 ISO COBOL specification. (I am
IGNORING all OO related items - as Colin has explicitly "postponed" that in
his document.) I may also have missed some "extensions" that do become
standard with the 2002 specification.   I am *not* saying that Colin (or
others) *SHOULD* allow them today, but this is a consideration in deciding
which extensions (to the '85 Standard) should and should not be allowed:

 - User-defined words, Computer-name, etc written in DBCS characters
 - Unicode support  (ISO 10646) (literals & other features) - some other
NATIONAL items, not listed below
 -  ADDRESS OF
 - NULL/NULLS (figurative constant)
 - Use of apostrophe (') as an alternative to the quotation mark  (") in
opening and closing  delimiters
 - Hexadecimal notation for alphanumeric literals, defined by opening
delimiters X" and X'
 - National literals N", N', NX", NX' for storing  literal content as
national characters.
 - 19- to 31-digit fixed-point numeric literals
 - Floating-point numeric literals
 - Comment lines before the Identification Division header
 - RECURSIVE clause     (Program-ID paragraph)
 - An alphanumeric literal for program-name in the PROGRAM-ID paragraph
 - The optional order of clauses  (Special-Names paragraph - I am NOT
positive that this got into the 2002 Standard)
 - WITH PICTURE SYMBOL phrase in the CURRENCY SIGN  clause
 - Use of lower-case alphabetic characters as a currency sign
 - LOCAL-STORAGE SECTION
 - The GLOBAL clause in the linkage section
 - Implicit qualification of a key specified without qualifiers when the key
name is not unique
 - Picture symbols N
 -  Picture symbol E and the external floating-point picture format
 - Selecting a currency sign and currency symbol with the CURRENCY compiler
option
 - The maximum of 31 digits for numeric items of  usages DISPLAY and
PACKED-DECIMAL and for  numeric-edited items of USAGE DISPLAY
 - USAGEs - NATIONAL, POINTER, and PROCEDURE-POINTER
 - A VALUE clause in file and linkage sections in  other than condition-name
entries
 - VALUE IS NULL/NULLS
 - PROCEDURE DIVISION Header - The BY VALUE phrase and  The RETURNING phrase
 - Omitting an initial paragraph-name if there are no declaratives
 - Specifying data items of usage or PACKED-DECIMAL in a NUMERIC class test
 - ADD, SUBTRACT, DIVIDE, MULTIPLY  - A composite of operands greater than
18 digits
 - CALL - OMITTED phrase  and BY VALUE phrase
 - CALL -  Specifying an argument defined as a subordinate group item
 - Displaying signed numeric literals and  non-integer numeric literals
 - Specifying EXIT PROGRAM before the last statement in a sequence of
imperative statements
 - SET formats for pointers and procedure-pointers
 - STRING - Reference modification of the data item specified in the INTO
phrase
 - UNSTRING - Reference modification of the sending field
 - New Intrinsic Functions - DATE-TO-YYYYMMDD, DAY-TO-YYYYDDD,  DISPLAY-OF,
and  NATIONAL-OF
 - COPY - The optionality of the syntax "OF library-name"  for specifying a
text-name qualifier (when some COPY statements use it)
 - COPY - Literals for specifying text-name and library-name
 - Nested COPY statements
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-06T15:58:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b48gbd$kq$1@slb5.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net>`

```
Have I got an "interesting" (can you say CONTROVERSIAL) idea for the "group"
to discuss? !!!

I believe that anyone creating NEW "copy" source code should follow these
rules:

1) Place all the "source code" between column 8 (not 7) and the R-margin
(probably column 72)

2) Column 73-80 (or whatever is between the R-margin and the end-of-line)
should be spaces

3) Columns 1-6 should be spaces (except as stated below)

4) The *only* allowed non-space value in column 7 should be "*" (not "/" -
not "D" - and most DEFINITELY not "-")

5) For any line with "*" in column 7, there should also be a "*> " in
columns 1-3

6) If you *must* use a "D" in column 7, then also code a ">>D " in columns
1-4 - but this will need some modification, i.e. removal of the column 7 D,
later.

7) Similarly, if you code "/" in column 7, you can/should code ">>PAGE" in
columns 1-6

   ***

If these rules are followed (even in environments where "free form reference
format" is available already - as an extension to the '85 Standard), then it
GUARANTEES that the copy source code will be "valid" (and mean what you
expect) in any 2002 conforming environment - including BOTH free and fixed
form reference format.

   ****

Personally, I would ALSO follow these rules in creating new "main" (not
COPY) source code.  However, I don't see that as important as "positioning"
copy source code for future use.

P.S.  Yes, I know that for those of you distributing or receiving source
code where "real sequence numbers" in column 1-6 is necessary, this won't
work.  HOWEVER, I think that this is not the case for most programs and
programmers.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-06T23:21:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67D86D.A38C77D2@shaw.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Have I got an "interesting" (can you say CONTROVERSIAL) idea for the "group"
> to discuss? !!!
…[3 more quoted lines elided]…
>

Good ideas - but I guess I've more or less been folloiwng your rules since VISOC
and then Net Express. Free format is OK but when I do print source or copyfiles
I like to print 'portrait' with a margin to left and right. Nice with an HP
laser with my default settings print 'Portrait, back and front'..(I've even
'squished' two pages to a sheet to economize, but I can't read it easily, and if
I sent that to you - you would hit me <G>)

> 1) Place all the "source code" between column 8 (not 7) and the R-margin
> (probably column 72)  *** Yes - 8 to 72. Just one qualifier from the guy who
> doesn't like directives - to activate SQL I have to have "$set...." starting
> in Column 7 - and I think that becomes something like >> starting in Column 7
> (COBOL 2002) ????

> 2) Column 73-80 (or whatever is between the R-margin and the end-of-line)
> should be spaces  *** Very seldom used but I might add a comment *> ....this
> is.

Column 73 onwards - I've only seen it used once in M/F GUI source examples - the
editor allowing for 255 (?) comment statements run off trhe end of the screen -
real pain in the butt - scrolling backwards and forwards. Not too nifty if you
want to print it !

> 3) Columns 1-6 should be spaces (except as stated below)

> 4) The *only* allowed non-space value in column 7 should be "*" (not "/" -
> not "D" - and most DEFINITELY not "-") *** Well have used the "-" to continue
> a literal for print header lines, even though it's in you 'No, No' category.

> 5) For any line with "*" in column 7, there should also be a "*> " in
> columns 1-3     *** I ignore Column 7 except for above - consistently my code
…[27 more quoted lines elided]…
>

However - qualify what I'm doing as it is PC based, so I don't know the
implications of what you recommend for mainframers.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-03-06T23:58:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ssmf6v86l3p4e09htqdi8cgg1ig8aa7fci@4ax.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <3E67D86D.A38C77D2@shaw.ca>`

```
On Thu, 06 Mar 2003 23:21:10 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

>
>
…[3 more quoted lines elided]…
>want to print it !
Very usefull usage in Acucobol.
By using the proper comamand line and values in column 73+ it was(is?)
possible to have code that is only compiled if it has a particular
value after this column.

example.

colu
   1                                      7
789012..................................0123456
*    MOVE ACU-VAR to ACU-VAR1              ACU
     MOVE RM-VAR to RM-VAR1                RM
     MOVE RM-VAR to RM-VAR2                RM
     MOVE ICL-VAR to ICL-VAR1              !ACU
*    MOVE ICOBOL-VAL TO ICOBOL-VAR1        ICOB

by compiling a program with the above with the following options
ccbl -o %1.cob -SI ACU -SX RM -w %1.CBL
the acucobol compiler would compile line 1 only, but if compiled with
the RM compiler only lines 2, 3 and 4 would be compiled


with the following
ccbl -o %1.cob -SI ACU -SI ICOB -w %1.CBL
all lines would be compiled by the acucobol compiler


Did use it a lot while I used different compilers/runtimes.

FF
Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-07T02:13:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E680085.D81CB34F@shaw.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <3E67D86D.A38C77D2@shaw.ca> <ssmf6v86l3p4e09htqdi8cgg1ig8aa7fci@4ax.com>`

```


Frederico Fonseca wrote:

> On Thu, 06 Mar 2003 23:21:10 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> wrote:
…[36 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com

Neat idea Frederico - but still looks a little cumbersome, having to read which are
the "Acu" and "RM" lines. Certainly using the compilation options is an extremely
nifty feature.

I'm not familiar with the Acu compiler but SURE liked the concept of Screen Section
being "dual" - DOS or Windows. But I believe that's now been replaced by a third
party product ?

Better yet with reference to the code - OO. Use flags and invoke specific classes or
methods depending upon whether you want this to operate for Acu or RM. Don Schricker,
Chair of J4, wrote a short article for cobolreport on this particular point some
two/three years ago.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-06T20:27:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4903e$q5v$1@slb4.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <3E67D86D.A38C77D2@shaw.ca> <ssmf6v86l3p4e09htqdi8cgg1ig8aa7fci@4ax.com> <3E680085.D81CB34F@shaw.ca>`

```
For this particular type of code (where you really want to decide at COMPILE
time which set of code to use), the 2002 Standard provides full support for
"conditional compilation" which does exactly this.  (Of course, like Acu,
Micro Focus has had an extension for this for years)
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T16:20:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67E5BF.5AE33318@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <3E67D86D.A38C77D2@shaw.ca>`

```
I wonder how the 2002 compilers are going to show us poor programmers a listing with
what was actually coded once free form input takes hold.  It seems that the listing
would pretty much have to break source lines at a space between COBOL elements
(literals, words, etc.), lest we be unable to see a long source line.  But what
about a really long alphanumeric literal?  Won't those cause problems in listings?

What have the compilers you've used done?

"James J. Gavan" wrote:

> "William M. Klein" wrote:
>
…[69 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-07T02:47:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6808A1.8B5AC8E2@shaw.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <3E67D86D.A38C77D2@shaw.ca> <3E67E5BF.5AE33318@attglobal.net>`

```


Colin Campbell wrote:

> I wonder how the 2002 compilers are going to show us poor programmers a listing with
> what was actually coded once free form input takes hold.  It seems that the listing
…[5 more quoted lines elided]…
>

Colin,

I'm assuming your question above was directed to everybody in general and not aimed at
me. If the latter, I'm not particularly thrilled with free format based on the points I
made about getting decent output based on a portrait page, (8.5 x 11 - or A4 if my
distant memory is not too flaky). Why shouldn't program source look as 'graceful' as any
other official document ?

Evaluate true when FirstChoiice invoke thisClass "doThis" using This andThis
andAnotherThis returning TheseValues If not Kosher invoke SecondClass "HereWeGoAagain"
using..........*> The End-Evaluate appears somewhere in the distance.

Oh my Gawd ! AND don't forget you can read the above because Netscape immediately
wrapped after Line 1 "andThis" and Line 2 "SecondClass"

The above example is absurd - but you *know* and I *know* that some twit will do exactly
that - and be as pleased as Punch with himself !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-03-06T18:57:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<icR9a.7161$Or5.882627@news20.bellglobal.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net>`

```
I know it's petty, but I think you ment "*>D" and "*>PAGE", not ">>D" and
">>PAGE".

Comments follow, with SHOP STANDARD where applicable.

Calin, TORONTO

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b48gbd$kq$1@slb5.atl.mindspring.net...
> Have I got an "interesting" (can you say CONTROVERSIAL) idea for the
"group"
> to discuss? !!!
>
…[7 more quoted lines elided]…
> should be spaces

1-2.  SHOP STANDARD: when we edit/change old programs, we put a YYMMDD in
columns 73-78; easy to find, should probably enforce a " *> YYMMDD ".

> 3) Columns 1-6 should be spaces (except as stated below)
>
…[4 more quoted lines elided]…
> columns 1-3

3-4-5. SHOP STANDARD: sounds good to me, we're now trying to enforce a "use
STRING not -" policy, so far it works OK with everybody; we're not touching
old programs for this only, though.

> 6) If you *must* use a "D" in column 7, then also code a ">>D " in columns
> 1-4 - but this will need some modification, i.e. removal of the column 7
D,
> later.
>
> 7) Similarly, if you code "/" in column 7, you can/should code ">>PAGE" in
> columns 1-6


8-7. No comments on this one, it sounds great!

> If these rules are followed (even in environments where "free form
reference
> format" is available already - as an extension to the '85 Standard), then
it
> GUARANTEES that the copy source code will be "valid" (and mean what you
> expect) in any 2002 conforming environment - including BOTH free and fixed
…[5 more quoted lines elided]…
> COPY) source code.  However, I don't see that as important as
"positioning"
> copy source code for future use.
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-06T18:07:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b48nro$oi6$1@slb9.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <icR9a.7161$Or5.882627@news20.bellglobal.com>`

```
No,
  I really meant

      >>D
         and
       >>PAGE

See the ISO 2002 Standard pages 23 and 55
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-03-10T01:59:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b48gbd$kq$1@slb5.atl.mindspring.net...
> Have I got an "interesting" (can you say CONTROVERSIAL) idea for the
"group"
> to discuss? !!!
>
…[15 more quoted lines elided]…
> columns 1-3

    Wouldn't it work just as well to put a "*" in col 7, and ">" in col 8?
    And leave 1-6 blank.






> 6) If you *must* use a "D" in column 7, then also code a ">>D " in columns
> 1-4 - but this will need some modification, i.e. removal of the column 7
D,
> later.
>
…[5 more quoted lines elided]…
> If these rules are followed (even in environments where "free form
reference
> format" is available already - as an extension to the '85 Standard), then
it
> GUARANTEES that the copy source code will be "valid" (and mean what you
> expect) in any 2002 conforming environment - including BOTH free and fixed
…[5 more quoted lines elided]…
> COPY) source code.  However, I don't see that as important as
"positioning"
> copy source code for future use.
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-10T02:02:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4hgqf$p6g$1@slb1.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com>`

```
"Russell Styles" <RWS0202@comcast.net> wrote in message
news:zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com...
>
> "William M. Klein" <wmklein@ix.netcom.com> wrote in message
…[4 more quoted lines elided]…
> >
 <snip>
> >
> > 5) For any line with "*" in column 7, there should also be a "*> " in
…[5 more quoted lines elided]…
>

Nope,  because in free form, a line with

     *   *>

would look to the compiler like a "multiply" followed by a comment  while a

 *>     *

(with the *> in columns 1-6) would still look like a comment in fixed or
free format)
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-11T07:13:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4ikr3$ic1$1@aklobs.kc.net.nz>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net>`

```
William M. Klein wrote:

> "Russell Styles" <RWS0202@comcast.net> wrote in message

>>     Wouldn't it work just as well to put a "*" in col 7, and ">" in col
>>     8? And leave 1-6 blank.
…[3 more quoted lines elided]…
>      *   *>

In what way is that 'leaving cols 1-6 blank' ?
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 5)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-03-10T14:47:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zFadnbfaRJ-dcfGjXTWcow@comcast.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net>`

```

    What I meant was columns 01 thru 06 blank, "*>" in cols 7 & 8.




"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b4hgqf$p6g$1@slb1.atl.mindspring.net...
> "Russell Styles" <RWS0202@comcast.net> wrote in message
> news:zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com...
…[12 more quoted lines elided]…
> >     Wouldn't it work just as well to put a "*" in col 7, and ">" in col
8?
> >     And leave 1-6 blank.
> >
…[6 more quoted lines elided]…
> would look to the compiler like a "multiply" followed by a comment  while
a
>
>  *>     *
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-10T15:55:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4j1jn$9s3$1@slb4.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com>`

```
Sorry that I misunderstood.  That should do it too.  (Actually, I can't
remember if the 2002 Standard requires a space after the
   *>
or not.  I remember it being discussed, but don't remember the final
decision - and haven't checked it out.  If so, it would need to be
  * in column 7
  > in column 8
        and
  space in column 9
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 7)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-03-10T17:21:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8--dnfAyM6GLjfCjXTWcpw@comcast.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com> <b4j1jn$9s3$1@slb4.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b4j1jn$9s3$1@slb4.atl.mindspring.net...
> Sorry that I misunderstood.  That should do it too.  (Actually, I can't
> remember if the 2002 Standard requires a space after the
…[8 more quoted lines elided]…
> --

    That is an example of the sort of thing that can drive people
crazy when porting from one system to another, at least
when going from a permissive system to one that is not so
permissive.  A small thing in this case, but the aggravations
add up.





> Bill Klein
>  wmklein <at> ix.netcom.com
…[15 more quoted lines elided]…
> > > > > Have I got an "interesting" (can you say CONTROVERSIAL) idea for
the
> > > > "group"
> > > > > to discuss? !!!
…[24 more quoted lines elided]…
> > > (with the *> in columns 1-6) would still look like a comment in fixed
or
> > > free format)
> > >
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-10T16:54:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4j53t$lal$1@slb0.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com> <b4j1jn$9s3$1@slb4.atl.mindspring.net> <8--dnfAyM6GLjfCjXTWcpw@comcast.com>`

```
I don't quite understand what you think is "aggravating".  If these were
followed with *any* ANSI/ISO '85 or 2002 Standard compiler, they would all
treat this as a comment line (regardless of format selected).

It is true that there are OTHER options that might also work to mark a line
as a comment (and that such techniques would be implementation specific),
but my point was that if you followed this technique (or my original idea of
"*" in column 7 and "*> " in columns 1-6, then you have "guaranteed"
portable code.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 9)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-03-11T01:29:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KYacnUypZP72H_CjXTWc3Q@comcast.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com> <b4j1jn$9s3$1@slb4.atl.mindspring.net> <8--dnfAyM6GLjfCjXTWcpw@comcast.com> <b4j53t$lal$1@slb0.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b4j53t$lal$1@slb0.atl.mindspring.net...
> I don't quite understand what you think is "aggravating".  If these were
> followed with *any* ANSI/ISO '85 or 2002 Standard compiler, they would all
> treat this as a comment line (regardless of format selected).
>
    I was referring to things like one compiler requiring a space between
a data name and the left parenthesis, while another allows you to have them
touching.  This has been known to change with just a verson change, much
less a different vendor.  In this case, I was thinking about the bother
if a compiler started complaining about "*>comment" (no space) type
comments.

    I suppose that you could do a global change in editor of course.

    I do like this idea.  It beats the alternatives (conditional compiles)
all hollow.  If you use only "whole line" comments, you could
even work with an "old" compiler.

> It is true that there are OTHER options that might also work to mark a
line
> as a comment (and that such techniques would be implementation specific),
> but my point was that if you followed this technique (or my original idea
of
> "*" in column 7 and "*> " in columns 1-6, then you have "guaranteed"
> portable code.
…[9 more quoted lines elided]…
> > > Sorry that I misunderstood.  That should do it too.  (Actually, I
can't
> > > remember if the 2002 Standard requires a space after the
> > >    *>
…[36 more quoted lines elided]…
> > > > > > > Have I got an "interesting" (can you say CONTROVERSIAL) idea
for
> > the
> > > > > > "group"
…[4 more quoted lines elided]…
> > > > > > > 5) For any line with "*" in column 7, there should also be a
"*>
> "
> > > in
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-11T00:37:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4k06s$gqv$1@slb2.atl.mindspring.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com> <b4j1jn$9s3$1@slb4.atl.mindspring.net> <8--dnfAyM6GLjfCjXTWcpw@comcast.com> <b4j53t$lal$1@slb0.atl.mindspring.net> <KYacnUypZP72H_CjXTWc3Q@comcast.com>`

```
I have now looked up the rule in the final draft of the 2002 Standard and it
says (page 23, SR(1)),

"1) For purposes of analyzing the text of a compilation group, a space is
implied immediately following a floating comment indicator."

which means (I believe) that you do NOT need to put an "explicit" space
following the  "*>" when it is a floating comment-indicator.
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-10T23:08:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E6D1B81.25B9E840@shaw.ca>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net> <b48gbd$kq$1@slb5.atl.mindspring.net> <zsGdnQFWxpJ3qvGjXTWcpQ@comcast.com> <b4hgqf$p6g$1@slb1.atl.mindspring.net> <zFadnbfaRJ-dcfGjXTWcow@comcast.com> <b4j1jn$9s3$1@slb4.atl.mindspring.net> <8--dnfAyM6GLjfCjXTWcpw@comcast.com>`

```


Russell Styles wrote:

> "William M. Klein" <wmklein@ix.netcom.com> wrote in message
> news:b4j1jn$9s3$1@slb4.atl.mindspring.net...
…[16 more quoted lines elided]…
> add up.

Valid point - and I do use a 'permissive' compiler like :-

Method-id. "displayIt".
display 'Hello World"
End Method "displayIt".

Note I wrap the Method-id. in quotes, picking that up from original M/F
examples; but it can appear without the quotes. Following on Bill's comment, I
totally ignore Column 7, always starting in Column 8, so:-

*>-----------------------
Method-id. "displayIt".
*>----------------------
display 'Hello World"
End Method "displayIt".
*>---------------------

Whether in 'true' COBOL 2002 style, there should be a space after the "*>" - I
have no idea.

My comment lines above are my own preference. Again style, but where Donald
inlcudes what M/F christened "red tape', ENVIRONMENT DIVISION, DATA DIVISION
etc., when not really required, given a reasonably lengthy source I would have a
problem picking out the guts of what methods are doing.

Here's another one which sends me squirrly :-

     class-control.
           *> OrderedCollection is class "ordrdcll"
           *> Array is class "array"
           *> Bag is class "bag"
           SortedCollection is class "srtdclln"
           CharacterArray is class "chararry"
           *> ValueSet is class "valueset"
           SortSequence is class "sortsequence" *> this is user's own class

           Fruit is class "fruit" *> this is the source containing the above
entries.
           *> a table of fruits are being used to create different lists
           .
I've just copied that from a recent attachment to an Answer Exchange query.  The

originator has done a 'copy and paste' from an M/F demo on the basics for
collections. But his query was related to SortedCollections. For sure the ones I
have commented out are not used and could be completely removed. Quoting the
classes and not using them doesn't do any harm - but for maintenance -
instinctively you are going to say to yourself where are they used ?

Rather than 'mess around', it appears within the M/F fraternity there are a fair
number of developers doing the simple 'copy and paste'. It's a while back since
I looked, but I got the impression that C programmers do a 'block copy and
paste' for 'includes'.

My own personal rule 'if you wont use 'em, delete 'em'.

As to your observation about portability - Mainframes, maybe yes, OO-wise I've
given up.  I think that so much code will have been written, (in F/J and M/F),
prior to J4 coming out with Standard classes - the latter probably wont have any
relevance to COBOL developers - certainly not without MAJOR changes to their
source..

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-03-06T16:15:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E67E496.F53E222C@attglobal.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <b48emp$re8$1@slb9.atl.mindspring.net>`

```
Holy mackeral!  You're going to cause me to end up 5 - 7 years behind, just like
the COBOL Standards committee!  Don't you ever sleep, eat, or visit other
Newsgroups?

Seriously, more good grist for the mill in this and your follow-on reply (which
I must note, is to yourself!).  I'm still working on the first 20 or so you gave
me yesterday.

By the way, I compiled a program which I have "under construction" using
FLAGSTD(HDS,O).  I think this means to measure against the High level of the
1985 Standard, ignore Debugging and Segmentation, and flag Obsolete items.  I
got 168 messages, and I'm the "expert" here!  Ignorng FIPS flagging, there was
only 1 warning, about a PERFORM that could not be executed, because I haven't
yet written the code that would change a variable from its defined VALUE ZERO.
Colin

"William M. Klein" wrote:

> "Colin Campbell" <cmcampb@attglobal.net> wrote in message
> news:3E669F8D.E69F28E3@attglobal.net...
…[107 more quoted lines elided]…
>  - Nested COPY statements
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-03-07T10:02:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0303071002.585a22e6@posting.google.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
I think it looks great.  Just a few comments...


>4. Records used in multiple programs must be described by a COPY
>member (and this COPY member must always be used whenever describing
…[3 more quoted lines elided]…
>throughout all programs which use it; for example, EMPLOYEE-ID and
not
>EMPLOYEE-NUMBER, PAYROLL-ID, etc.

Regarding variable names, one really cool thing I have seen is a
standard abbreviation dictionary for use in variable names.  This
prevents you from a EMPLOYEE-NUMBER with an ACCOUNT-NUM, a PHONE-NBR
and a BADGE-NO.  It keeps the
XXX-EMPLOYEE-NUMBER in one record from becoming YYY-EMPLOYEE-NBR in
another record.


>1. Programs should not be overly large or complex, in order to
promote
>understandability and maintainability. The number of COBOL imperative
>statements is not felt to contribute to difficulty in understanding
as
>much as the number of conditional statements. Therefore, a program
may
>not contain more than 300 IF and EVALUATE statements.  For purposes
of
>automated standards checking, a warning will be issued when the count
>exceeds 60% of the maximum, and an error when the count exceeds 100%
>of the maximum. The actual count will be recorded to allow review of
>the maximum number later.

and 

>2. Highly complex program logic is discouraged.  The level of nesting
>within a procedure must not exceed 12; the preferred limit is 6.
>Nesting refers mainly to conditional statements contained within
other
>conditional statements, such as IF within IF or IF within EVALUATE.
>Some compilers show the nesting level on the source code listing.

When taken together, 1 and 2 suggest that maybe you should grade the
program on number and nesting.

A simple READ loop program to validate a record with 301 numeric
fields, that is, 1 'IF NUMERIC' check per field would fail your first
condition for excessive IFs, but would hardly be complex.

On the other hand, a program with a few dozen lines can quickly nest
itself into some very hard to understand logic.

Why not weight the number of conditionals by nest level.

Conditional at a zero level = 1.
Conditional at 1 = 2.
Conditional at 2 = 4.
Conditional at 3 = 8.
etc...
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-08T01:09:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6942db.64016945@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <16e2f010.0303071002.585a22e6@posting.google.com>`

```
psychedelic-harry@mindless.com (Joe Zitzelberger) wrote:

>I think it looks great.  Just a few comments...
>
…[15 more quoted lines elided]…
>another record.

COBOL has _qualification_. The syntax is 'employee-number in payroll-master.'
Other languages do qualification by prefixing the data name with an abbreviation
of the file name. 

Please use COBOL-style rather than crippling COBOL to look like other languages.
```

#### ↳ Re: Please help -- COBOL Programming Standard

- **From:** bdhobbs18@acm.org (Bill Hobbs)
- **Date:** 2003-03-17T23:39:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ca5032.0303172339.1cc1c6fc@posting.google.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net>`

```
Drop the history and other extraneous stuff, I wouldn't want to wade
thru anymore stuff then I need to.

The main part of the document should be platform neutral and,
probably, orientated toward a particular COBOL version, possibly 1985
for the time being.  Put platform specific and other COBOL version
information in appendices.  For instance "OpenVMS VAX COBOL V5.7" and
"COBOL 1974".  Version numbers may be necessary, show how to determine
the version.

I really recommend changing from "is prohibited" and "is required" to
"should not use", "is discouraged", "suggested", and "is recommended"
- I'd rather be guided, not forced.  Add a section that if these
suggestions are not followed, explanations will be included as
comments, and management/senior programmer will understand and sign
off on the deviations.  You could also threaten the offender with
being assigned the task of updating this guide to accommodate their
behavior.

Include a form listing the various dos and don'ts.  Possibly the
output of the standard checking program could be used, the machine
checkable parts are filled in, the rest are also printed and left for
the code review team.  Explain what becomes of the form: who signs it,
where copies go, retention period, etc..

Spot checks may be necessary to instill the proper fear into managers
and programmers.

Take a look at "Indian Hill C Style and Coding Standards" as an
example.
http://www.chris-lott.org/resources/cstyle/
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** <&#116;&#114;&#111;&#112;&#105;&#099;&#102;&#108;&#105;&#116;&#101;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;>
- **Date:** 2003-03-19T14:36:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e78c6df_3@news1.prserv.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <74ca5032.0303172339.1cc1c6fc@posting.google.com>`

```
&#116;&#114;&#111;&#112;&#105;&#099;&#102;&#108;&#105;&#116;&#101;&#064;&#12
1;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;
```

##### ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-20T01:31:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e790d3c.33501364@news.optonline.net>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <74ca5032.0303172339.1cc1c6fc@posting.google.com>`

```
bdhobbs18@acm.org (Bill Hobbs) wrote:

>Drop the history and other extraneous stuff, I wouldn't want to wade
>thru anymore stuff then I need to.
…[28 more quoted lines elided]…
>http://www.chris-lott.org/resources/cstyle/

This is my lifetime of experience instilling programming standards in about six
shops. The standard was highly consistant, to the point where you couldn't tell
from reading a section of code who wrote it. Yet there was no coercion. The
published standard covered perhaps two printed pages. It dealt with high-level
objectives, not dos and don'ts.

The techniques to accomplishing this were: 

,,Getting them to agree that a consistant style was desirable. 
..Making them work on others' code. If program A was written by programmer B
three months ago, and now a maintenace change is required, I didn't assign it to
programmer B, I assigned it to programmer C. 
..As a result of the _synergy_, a resulting common shop standard was better than
any individual could have created on his own ,, including me. .They didn't have
to follow my style. Although I was chairman of the committee, so to speak, I was
just another member of the fraternity when it came to style. Nobody will believe
this, but I actuually changed my style because of their persuasive arguments. 
..A precopiler which rated programs on quality. They adopted better practices
just for the satisfaction of getting a 100% grade. 

My point is appeal to the positive rather than the negative. Reward then for
doing it right rather than slapping their hands for doing it wrong. Enlist their
cooperation rather than begrudging compliance. Appeal to their sense of pride
rather than threatening them. Make them think of themselves as Real Programmers,
and they will be. Conversely, make them think of themselves as 'undisciplined
children needing to be controlled' and they'll act accordingly. 

Robert
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-03-20T10:55:12
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e7982b0_1@text-west.newsgroups.com>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <74ca5032.0303172339.1cc1c6fc@posting.google.com> <3e790d3c.33501364@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e790d3c.33501364@news.optonline.net...
> bdhobbs18@acm.org (Bill Hobbs) wrote:
>
…[32 more quoted lines elided]…
> This is my lifetime of experience instilling programming standards in
about six
> shops. The standard was highly consistant, to the point where you couldn't
tell
> from reading a section of code who wrote it. Yet there was no coercion.
The
> published standard covered perhaps two printed pages. It dealt with
high-level
> objectives, not dos and don'ts.
>
…[3 more quoted lines elided]…
> ..Making them work on others' code. If program A was written by programmer
B
> three months ago, and now a maintenace change is required, I didn't assign
it to
> programmer B, I assigned it to programmer C.
> ..As a result of the _synergy_, a resulting common shop standard was
better than
> any individual could have created on his own ,, including me. .They didn't
have
> to follow my style. Although I was chairman of the committee, so to speak,
I was
> just another member of the fraternity when it came to style. Nobody will
believe
> this, but I actuually changed my style because of their persuasive
arguments.
> ..A precopiler which rated programs on quality. They adopted better
practices
> just for the satisfaction of getting a 100% grade.
>
> My point is appeal to the positive rather than the negative. Reward then
for
> doing it right rather than slapping their hands for doing it wrong. Enlist
their
> cooperation rather than begrudging compliance. Appeal to their sense of
pride
> rather than threatening them. Make them think of themselves as Real
Programmers,
> and they will be. Conversely, make them think of themselves as
'undisciplined
> children needing to be controlled' and they'll act accordingly.
>
> Robert
>

I've been managing Programmers for close on 20 years now, and I totally
endorse this approach.

Having worked in both kinds of shops (the rigid "mandatory" approach and the
more relaxed "This is probably a good idea" approach) the results obtained
in the latter far exceed the results obtained in the former.

Programmers do not ALWAYS behave like intelligent adults (there are very few
Humans who do <G>) but they should be treated like intelligent adults
nonetheless.

Robert got this right.

Pete.


>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Please help -- COBOL Programming Standard

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-20T16:29:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5cq9j$cgo$1@peabody.colorado.edu>`
- **References:** `<3E669F8D.E69F28E3@attglobal.net> <74ca5032.0303172339.1cc1c6fc@posting.google.com> <3e790d3c.33501364@news.optonline.net>`

```

On 19-Mar-2003, robert@wagner.net (Robert Wagner) wrote:

> My point is appeal to the positive rather than the negative. Reward then for
> doing it right rather than slapping their hands for doing it wrong. Enlist
…[5 more quoted lines elided]…
> children needing to be controlled' and they'll act accordingly.

And certainly be aware of which programs make good models - when someone is
assigned to write a new program - mention which program he might want to crib
from.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
