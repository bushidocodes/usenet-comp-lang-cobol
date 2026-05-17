[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Flex, Bison, Ebcdic, IBM/MVS

_17 messages · 9 participants · 1996-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Flex, Bison, Ebcdic, IBM/MVS

- **From:** "bruno...." <ua-author-17086621@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55q1dv$6rf@news1.Belgium.EU.net>`

```

At company I work for, we are developing a tool to check cobol
coding standards. This tool was initially developed in a Windows
NT environment (with flex and bison and using a Microsoft C
compiler). We planned to port this tool to our IBM/MVS mainframe
environment (using the SAS C compiler). We are not yet running
Open Edition on our mainframe.

We were aware of the ASCII - EBCDIC conversion problem, but we
are been faced now with problems that seems quite difficult to
solve.

1. An alternative we investigated was to change, on the
mainframe, the input to flex from EBCDIC to ASCII, in order
to use the same version of flex on both platforms (WinNT +
IBM/MVS). The output of flex then needs again to be translated
back to EBCDIC. This poses us various problems. Flex passes
sometimes information to Bison that is not really what we expect
to be passed. The reason for this is that we suspect that the
ASCII-EBCDIC translation and back is not done on the right places.
This does also seem to be a not so elegant solution.

2. In one of the replies to a thread in the comp.compilers
newsgroup a while ago suggestion was made to port Flex to the target
machine and run it there to produce the scanner. We downloaded
the last flex source code (2.5.3). One of the files in the
distribution package discussses the changes to make to adapt
flex to run on an IBM mainframe. We did this. Several other
changes had to be made in the C programs, in order to cope with
the file system on the mainframe. The patches for flex in the
distribution package date back from the 2.3 release. We are
therefore not sure if they work for the last release. We did not
succeed in compiling the EBCDIC scanner program (scan.c)

I would like to ask if anyone has already succeeded in doing
what I described above. All guidance on this matter is welcome.

Thanks in advance,


Bruno Peeters
Gemeentekrediet
bru··.@gkb··b.be
```

#### ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "cmcam..." <ua-author-17086272@usenetarchives.gap>
- **Date:** 1996-11-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<55q1dv$6rf@news1.Belgium.EU.net>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net>`

```

In <55q1dv$6.··.@new··U.net>, bru··.@gkb··b.be (Bruno Peeters) writes:
› At company I work for, we are developing a tool to check COBOL
› coding standards. This tool was initially developed in a Windows
…[4 more quoted lines elided]…
› 
Bruno,
In my opinion, this is going at the problem backwards.

I wrote our COBOL standards checker using the built in exits to the COBOL
compiler. This way, when someone compiles, the code is checked for standards
compliance. We have a production change control system which does the compile
and link for production, and if the programmer has ignored the messages and
condition code produced by this function, the PCCS doesn't, and the code is
rejected for production.

The IBM COBOL manuals show how to do this, and no doubt you could write the
actual code in C, but it is certainly possible to write it in COBOL. I wrote a
'driver' which invokes the compiler in Assembler, but we could live without it.
(It just allows us to control the compiler options used, etc.) I cannot imagine
having a more maintainable result from C than from COBOL, either, but then, I'm
not a C fan.

The semi-tricky part is parsing COBOL. I do this in COBOL without problems,
using UNSTRING, STRING, etc. I've been using the same code since 1974 ANSI
COBOL. Just code this into a subroutine called 'Get Element', where a COBOL
element is one of the set of integers, non-integer numbers, quoted literals,
reserved words, user words, terminal periods, etc. The caller of 'Get Element'
needs to either look at the individual elements (in Data Division, for example),
or assemble complete statements for later checking (in Procedure Division).

One of the standards of which I am most proud is how we try to control program
complexity. We used to have limits on the number of verbs, which always was a
source of controversy - was 500 enough, or did we need 10,000? Now, we just
count _conditional_ verbs (IF, EVALUATE, etc.), ignoring the MOVE's, ADD's and
the like. We've found that 150 or so is plenty for a program (although our
limit is currently higher). Also, don't forget the checks for data definitions
that make for efficient generated code, such PACKED-DECIMAL items having an odd
number of digits and a sign in the PICTURE.

If you are using both mainframe and PC based COBOL, look at IBM VisualAge
for COBOL for OS/2, (also available for Windows 95 and NT). The same exits are
available as in COBOL for MVS&VM, so the same approach would work in both
places.

You can check this compiler out cheaply by subscribing to the Developer
Connection for OS/2 - only $199US for four issues (supposedly quarterly, but
actually more like four to five months apart). Telephone 1-800-6DEVCON in the
US, or in Europe, there are language dependent numbers in Denmark:
45-48101200 is French, 45-48101500 is English, and there are eight others.

If you want more info, contact me.
Colin Campbell
```

##### ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p2@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap>`

```

cmc··.@ccg··c.com(Colin Campbell) wrote:

› In <55q1dv$6.··.@new··U.net>, bru··.@gkb··b.be (Bruno Peeters) writes:
›› At company I work for, we are developing a tool to check COBOL
…[7 more quoted lines elided]…
› In my opinion, this is going at the problem backwards.
 
› I wrote our COBOL standards checker using the built in exits to the COBOL 
› compiler.  This way, when someone compiles, the code is checked for standards 
…[3 more quoted lines elided]…
› rejected for production.
 
› The IBM COBOL manuals show how to do this, and no doubt you could write the 
› actual code in C, but it is certainly possible to write it in COBOL.  I wrote a 
…[3 more quoted lines elided]…
› not a C fan.
 
› Colin, I would like to get information on the Compiler exits.
 
› The semi-tricky part is parsing COBOL.  I do this in COBOL without problems, 
› using UNSTRING, STRING, etc.  I've been using the same code since 1974 ANSI 
…[4 more quoted lines elided]…
› or assemble complete statements for later checking (in Procedure Division).
 
› One of the standards of which I am most proud is how we try to control program 
› complexity.  We used to have limits on the number of verbs, which always was a 
…[5 more quoted lines elided]…
› number of digits and a sign in the PICTURE.

In the standards checker I wrote, the limit on conditional verbs is 10
per paragraph, but all I do is generate a warning message recommending
the paragraph be subdivided to reduce complexity. We also issue a
warning for nesting IF statements more than 3 levels deep. Recently,
I have enhanced it to check for data type mismatch on MOVE and
comparison statements, and also to require all working-storage items
to be valued. It had checking for IF/ELSE/END-IF alignment, and that
was enhanced to include the other explicit scope terminators.


› If you are using both mainframe and PC based COBOL, look at IBM VisualAge
› for COBOL for OS/2, (also available for Windows 95 and NT).  The same exits are
› available as in COBOL for MVS&VM, so the same approach would work in both
› places.
 
› You can check this compiler out cheaply by subscribing to the Developer 
› Connection for OS/2 - only $199US for four issues (supposedly quarterly, but 
› actually more like four to five months apart).  Telephone 1-800-6DEVCON in the 
› US, or in Europe, there are language dependent numbers in Denmark:
› 45-48101200 is French, 45-48101500 is English, and there are eight others.
 
› If you want more info, contact me.
› Colin Campbell

I would like more information on the exits. I'm also interested in
what kind of standards you enforce (always looking for ideas). Mine
was mostly intended to produce program listings for structured
walkthrus, so it was oriented towards naming conventions (my shop
requires numeric prefixes for data names and paragraph names, and
requires paragraph names to consist of an action verb followed by a
direct object). But I am also interested in any kind of static
analysis that would tend to reduce program defects.

Thanks in advance!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "bruno...." <ua-author-17086621@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p3@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap>`

```

arn··.@wor··t.net (Arnold J. Trembley) wrote:

› I'm also interested in
› what kind of standards you enforce (always looking for ideas).  Mine
…[5 more quoted lines elided]…
› analysis that would tend to reduce program defects.
 
› Thanks in advance!

A nice collection of cobol standards can be found at
http://www.adp.unc.edu/stds/sec600.html

Best regards,

Bruno Peeters
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-11-08T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p3@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap>`

```

Arnold J. Trembley wrote:
› 
› cmc··.@ccg··c.com(Colin Campbell) wrote:
…[82 more quoted lines elided]…
› St. Louis, Missouri


Please post this information concerning the exits. It seems that quite
a few shops have built their own standards checkers, which are a step
ahead of the change control systems currently available. I would
certainly like to modify ours to produce cleaner and more standardized
code. The only problem I foresee is that it will take a month to get
any of our older programs thru a good standards checker.

Keith
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 4)_

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-09T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p5@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap>`

```

Keith Farndon wrote:
› Please post this information concerning the exits.  It seems that quite
› a few shops have built their own standards checkers, which are a step
…[3 more quoted lines elided]…
› any of our older programs thru a good standards checker.
 
› Keith

I tested my standards checker on a very old and ugly program (still in
production) of about 5000 lines, and got over 2500 standards
violations! It would be easier to rewrite it from scratch.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 5)_

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-11-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p6@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap>`

```

Arnold J. Trembley wrote:
› 
› Keith Farndon  wrote:
…[16 more quoted lines elided]…
› St. Louis, Missouri

I would still be interested in any standard checks that you have, as a
lot of programs can be affected by recompiles and if I can turn on the
standards gently then they can be fixed over time. Programs have a much
longer life expectancy than most people think, Year 2000 proves that
point, and if you can clean them up as you go along things should get
easier. I would say that every program in every shop will be recompiled
at least once over the next three years, if only to provide a load
module to test against for Year 2000 projects. I am not sure if you
sell your checker, if you don't then please email me it to me, if you
do, then good luck.
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 6)_

- **From:** "ccam..." <ua-author-17086113@usenetarchives.gap>
- **Date:** 1996-11-10T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p7@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap>`

```

In <328··.@mf··p.com>, Keith Farndon writes:
› Arnold J. Trembley wrote:
›› 
…[21 more quoted lines elided]…
› do, then good luck.

Keith and Arn,
Our approach to getting higher quality programs without "stopping the world" to
upgrade all existing programs was to use a file which contained the names of our
"old" programs, later expanded to include a file of "excluded" programs - such
as those produced by an automated tool such as Prism, ADW, IEF, etc.

We have a Production Change Control System, which predated the standards
checker, so it was easy to capture the program-ids of all of the programs it had
processed as of a certain date.

The excluded programs get a "free ride" - heck, the program which produced them
just won't listen to us. The "old" programs get warnings about things that get
a "new" program errors. A few things get errors in either case - BLOCK 0, for
example.

IBM MVS COBOL Standards:
What follows is one company's shot at a decent set of standards for COBOL. We
used to count lines of code (verbs, actually), and everyone had a better number
than what the standard said. to attempt to address this, we decided that the
_conditional_ verbs were what made programs more complex, so we'd count those.
The number shown below is too large; we've compiled our biggies, and never
reached the warning stage.

Don't start up the GO debate again; while I participated, I'm tired of it, too!
There are more references to structured programming; let them pass if you think
it is all a plot to restrict your freedom.

If you have a set of standards you can share, please do so; we can all learn.

Other constructive criticisms are welcome; e-mail me at
"ccampbe2.cscmail.csc.com".
Colin

SCRIPT/VS 4.0.0: DEVICE 1403SW CHARS MONO
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

The programming standards which follow apply to new programs only. Ex-
ÿ¢§ __________________
ÿ¢§isting programs which are converted to 1985 ANSI COBOL in order to take
ÿ¢§advantage of new features of the language or compiler will be held to
ÿ¢§different standards, to be published later. The programming standards
ÿ¢§for COBOL are presented in order according to the structure of the lan-
ÿ¢§guage (by DIVISION):

ÿ¢§ÿ¢§ IDENTIFICATION DIVISION:

ÿ¢§ 1. The use of the COMMON attribute for a program is prohibited.
ÿ¢§ COMMON specifies that 'program-name' is contained within another
ÿ¢§ program, and it can be called from 'siblings' of the this pro-
ÿ¢§ gram and from programs contained within the siblings. Normally,
ÿ¢§ when using nested programs, only the 'parent' program could call
ÿ¢§ the contained 'child' program. This structure provides the po-
ÿ¢§ tential for really mixing up a maintenance programmer.

ÿ¢§ The INITIAL attribute for a program is to be used with caution.
ÿ¢§ Information about actual use of this feature will be recorded
ÿ¢§ initially. Once the performance implications of using the fea-
ÿ¢§ ture are fully understood, this rule may be reviewed.
ÿ¢§ INITIAL specifies that whenever this program is called, it
ÿ¢§ should be entered in its initial state; that is, data items hav-
ÿ¢§ ing VALUE clauses would have the initial value, GO's modified by
ÿ¢§ ALTER would be in their initial state, PERFORM stacks would be
ÿ¢§ empty, and files would be closed. This is apparently fairly
ÿ¢§ normal in some COBOL environments (or so an HP programmer has
ÿ¢§ told me), but it implies extra, possibly time consuming process-
ÿ¢§ ing before actually doing what the source program says to do,
ÿ¢§ and any such needs probably could be handled better by improving
ÿ¢§ program design.
ÿ¢§

ÿ¢§ÿ¢§ ENVIRONMENT DIVISION:

ÿ¢§ 1. The RESERVE clause is prohibited in the SELECT entry.

ÿ¢§ 2. The PASSWORD clause is prohibited in the SELECT entry.

ÿ¢§ 3. The RERUN clause is prohibited in the I-O-CONTROL paragraph.

ÿ¢§ 4. The SAME clause is prohibited in the I-O-CONTROL paragraph.
ÿ¢§

ÿ¢§ - 1 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ Programming Standards (continued):

ÿ¢§ÿ¢§ DATA DIVISION:

ÿ¢§ 1. Use of the EXTERNAL and GLOBAL clauses is prohibited.
ÿ¢§ EXTERNAL can be specified on both files and data to allow sepa-
ÿ¢§ rately compiled programs to share the file or data item.
ÿ¢§ GLOBAL can be specified on data to allow nested programs subor-
ÿ¢§ dinate to the one where GLOBAL is declared to reference the data
ÿ¢§ without having it passed to the subprogram(s) as an argument.
ÿ¢§ Both of these constructs violate structured programming guide-
ÿ¢§ lines.

ÿ¢§ 2. The BLOCK 0 clause is required in the FD for all QSAM (sequen-
ÿ¢§ tial) files.

ÿ¢§ 3. The COPY verb is the preferred method of including code in COBOL
ÿ¢§ programs because it is part of the 1985 ANSI standard, except as
ÿ¢§ required by precompilers such as DB2 or CICS, which might use a
ÿ¢§ word such as INCLUDE. Including code by use of Panvalet or Li-
ÿ¢§ brarian includes is strongly discouraged, to promote independ-
ÿ¢§ ence of source code from library management tools. In addition,
ÿ¢§ the COPY verb is more flexible than such includes, since it al-
ÿ¢§ lows replacement of words or quoted strings, so that a copied
ÿ¢§ record description can, for instance, be given unique names if
ÿ¢§ used more than once.

ÿ¢§ 4. Records used in multiple programs must be described by a COPY
ÿ¢§ member (and this COPY member must be used whenever describing
ÿ¢§ the record in a program). This leads to consistent naming of
ÿ¢§ fields and easier understanding of data and programs in a sys-
ÿ¢§ tem. Good practice also dictates use of the same name to de-
ÿ¢§ scribe the same data throughout all programs which use it; for
ÿ¢§ example, EMPLOYEE-ID and not EMPLOYEE-NUMBER, PAYROLL-ID, etc.

ÿ¢§ 5. To describe a record in a file description (FD), in the cases
ÿ¢§ where a simple elementary 01 is not sufficient, such as a vari-
 able length record, the COPY member describing the record must
ÿ¢§ ____
ÿ¢§ be used. The SUPPRESS clause of COPY may be used to reduce the
ÿ¢§ number of print lines.

ÿ¢§ 6. Permissible USAGEs for numeric data items are DISPLAY (implied
ÿ¢§ if no other usage is explicitly stated), BINARY (or COMP), and
ÿ¢§ PACKED-DECIMAL (or COMP-3). BINARY and PACKED-DECIMAL are part
ÿ¢§ of the ANSI Standard, while COMP and COMP-3 are IBM extensions.
ÿ¢§ Use of the standard names will make a program more transport-
ÿ¢§ able. The use of floating point data should be limited to
ÿ¢§ places where interfaces with other programs require it (such as
ÿ¢§ CALLs to a graphics package). This rule applies to non-copied
ÿ¢§ source code.

ÿ¢§ - 2 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ 7. DISPLAY usage data items may be either numeric or alphanumeric;
ÿ¢§ alphabetic items are not allowed. PICTURE descriptions will be
ÿ¢§ validated according to this rule.
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§

ÿ¢§ - 3 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ Programming Standards (continued):

ÿ¢§ 8. BINARY (COMP) usage data items must have PICTURE descriptions of
ÿ¢§ S9(4) or S9(9). The first defines a binary halfword; the sec-
ÿ¢§ ond, a binary fullword. Use of a standard number of digits
ÿ¢§ leads to easier recognition of the size of each binary field
ÿ¢§ when reading a program. This rule applies to non-copied source
ÿ¢§ code.

ÿ¢§ 9. PACKED-DECIMAL (COMP-3) usage data items must have a PICTURE
ÿ¢§ specifying a sign and an odd number of digits, such as S9(7)V99.
ÿ¢§ Describing the same area without a sign or with an even number
ÿ¢§ of digits causes less efficient code to be generated. This rule
ÿ¢§ applies to non-copied source code.
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§

ÿ¢§ - 4 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ Programming Standards (continued):

ÿ¢§ÿ¢§ PROCEDURE DIVISION:

ÿ¢§ 1. Programs should not be overly large or complex, in order to pro-
ÿ¢§ mote understandability and maintainability. The number of COBOL
ÿ¢§ imperative statements is not felt to contribute to difficulty in
ÿ¢§ understanding as much as the number of conditional statements.
ÿ¢§ Therefore, a program may not contain more than 500 IF and EVALU-
ÿ¢§ ATE verbs. For purposes of automated standards checking, a
ÿ¢§ warning will be issued when the count exceeds 60% of the maxi-
ÿ¢§ mum, and an error when the count exceeds 100% of the maximum.
ÿ¢§ The actual count will be recorded to allow review of the maximum
ÿ¢§ number later if desired.

ÿ¢§ 2. The level of nesting within a procedure must not exceed 12; the
ÿ¢§ preferred limit is 6.

ÿ¢§ 3. All procedures in a program must be coded either as paragraphs
ÿ¢§ or as sections; the choice is made by the programmer, but con-
ÿ¢§ sistency must be maintained in a program.

ÿ¢§ 4. The ALTER verb is prohibited.

ÿ¢§ 5. The GO verb is prohibited.
ÿ¢§ Structured programming theory has told us for twenty years that
ÿ¢§ any program can be coded without using the GO verb; new language
ÿ¢§ elements in the 1985 ANSI COBOL standard, such as CONTINUE
ÿ¢§ (which can be used where we were once limited to NEXT SENTENCE),
ÿ¢§ END-IF (to terminate the scope of an IF without ending a sen-
ÿ¢§ tence), and NOT AT END (on READ and RETURN verbs) make it easier
ÿ¢§ to follow this rule than in 1974 ANSI COBOL programs.

ÿ¢§ 6. The EXIT verb is prohibited. In the case where a procedure is
ÿ¢§ performed for the sole purpose of satisfying a PERFORM...UNTIL
ÿ¢§ condition (such as serially searching a table), and no action is
ÿ¢§ required in the procedure, use the CONTINUE verb instead of
ÿ¢§ EXIT, or code the CONTINUE verb in an 'in-line' PERFORM.
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§

ÿ¢§ - 5 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ Procedure Division Standards (continued):

ÿ¢§ 7. A program may have only one entry point.
ÿ¢§ Therefore, the ENTRY verb is prohibited. This rule means that
ÿ¢§ the PROCEDURE DIVISION header (using the Program-Id as the name)
ÿ¢§ is the only point at which entry to a program is allowed.

ÿ¢§ 8. A program may have only one exit point.
ÿ¢§ Program exit may be accomplished using either of the following
ÿ¢§ two constructs:
ÿ¢§ GOBACK
ÿ¢§ or
ÿ¢§ EXIT PROGRAM (followed immediately by)
ÿ¢§ STOP RUN
ÿ¢§ GOBACK is an IBM extension to COBOL, so the second choice may be
ÿ¢§ preferred to increase program transportability.
ÿ¢§ The STOP verb and EXIT PROGRAM are otherwise prohibited.

ÿ¢§ 9. The ACCEPT...FROM CONSOLE verb is prohibited. Operator communi-
ÿ¢§ cation is felt to be too error prone for use in production jobs.

ÿ¢§ 10. The DISPLAY...UPON CONSOLE verb is allowed, but only where a
ÿ¢§ utility type of program has no other way (such as a file) to
ÿ¢§ communicate error conditions. Messages created in this way ap-
ÿ¢§ pear on the batch job log and in the system message listing.
 DISPLAY in any form must not be used in an on-line environment.
ÿ¢§ _______________________________________________________________

ÿ¢§ 11. The only acceptable methods of controlling a loop in a program
ÿ¢§ are SEARCH, SEARCH ALL, PERFORM...UNTIL, and PERFORM...TIMES.
ÿ¢§ Note that 1985 COBOL allows specification of TEST AFTER and TEST
ÿ¢§ BEFORE on PERFORM to properly support DO...WHILE and DO...UNTIL
ÿ¢§ constructs, and that in line PERFORMs are allowed (they require
ÿ¢§ use of the END-PERFORM scope delimiter).

ÿ¢§ 12. PERFORM...THRU and THRU used in connection with INPUT or OUTPUT
ÿ¢§ PROCEDURE in MERGE or SORT statements are prohibited.
ÿ¢§ Use of this construct can lead to accidental destruction of a
ÿ¢§ program's structure, such as by moving a block of code into or
ÿ¢§ out of the range specified by the PERFORM.
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§

ÿ¢§ - 6 -
ÿ¢§

ÿ¢§ ANSI 1985 COBOL Programming Standards

ÿ¢§ Overview

ÿ¢§ Procedure Division Standards (continued):

ÿ¢§ 13. Certain standard subroutines, if used, must be called dynam-
ÿ¢§ ically. These subroutines are documented as needing to be
ÿ¢§ called dynamically. Violation of this instruction will result
ÿ¢§ in an error, due to the danger that bad results could be ob-
ÿ¢§ tained if the latest version is not used. (It will be assumed
ÿ¢§ that the NODYNAM option was in effect, since that is the stand-
ÿ¢§ ard; therefore, this rule applies to all CALL 'literal' verbs.)
ÿ¢§ NOTE: A list of these subroutines will be provided as part of
ÿ¢§ this standard; each organization which has such subroutines
ÿ¢§ should submit their names for inclusion in this list.

ÿ¢§ 14. Certain standard subroutines provided in the past to assist pro-
ÿ¢§ grammers in developing applications are no longer the best way
ÿ¢§ to accomplish the required task. Use of one of these subrou-
ÿ¢§ tines in a new application will result in an error, with the
ÿ¢§ suggestion of a better alternative.
ÿ¢§ Examples: DISPLAY, DATE, and DATEN should not be used; DATEMGR
ÿ¢§ is the preferred subroutine for obtaining and handling date and
ÿ¢§ time information.
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§
ÿ¢§

ÿ¢§ - 7 -
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 7)_

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-11T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p8@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap>`

```

cca··.@csc··c.com(Colin Campbell) wrote:
› IBM MVS COBOL Standards:
› What follows is one company's shot at a decent set of standards for COBOL.  We 
…[4 more quoted lines elided]…
› reached the warning stage.

Counting conditional verbs should get you a number very close to the
McCabe Cyclomatic Complexity metric. This number tends to get larger
with longer programs. I try to measure it, but I don't do anything
with it. My general rule of thumb is when this number gets over 300,
the program is pretty complex, and will probably have a large number
of defects in testing, and probably in production too.

› Don't start up the GO debate again; while I participated, I'm tired of it, too!
› There are more references to structured programming; let them pass if you think 
› it is all a plot to restrict your freedom.
 
› If you have a set of standards you can share, please do so; we can all learn.
 
› Other constructive criticisms are welcome; e-mail me at 
› "ccampbe2.cscmail.csc.com".
› Colin
› ÿ¢§ÿ¢§   IDENTIFICATION DIVISION:

We don't restrict COMMON. None of our programmers seem to be aware
that it exists. We have started using IS INITIAL on
pseudo-conversational CICS programs with BMS maps. Along with the
WSCLEAR runtime option, it seems to help prevent residual data
problems. These options are not flagged by our standards checker.
› 
› ÿ¢§ÿ¢§   ENVIRONMENT DIVISION:
…[7 more quoted lines elided]…
› ÿ¢§    4.  The SAME clause is prohibited in the I-O-CONTROL paragraph.

We don't check for these. We do check for SELECT statements that are
commented-out (unless enclosed entirely in "flower boxes") and issue a
warning.

› ÿ¢§ÿ¢§ DATA DIVISION:
›
› ÿ¢§ 1. Use of the EXTERNAL and GLOBAL clauses is prohibited.

We don't check for these (perhaps we should), but no one seems to use
them.

› ÿ¢§ 2. The BLOCK 0 clause is required in the FD for all QSAM (sequen-
› ÿ¢§ tial) files.
We don't check for this, but it is the general practice, and should be
encouraged.

› ÿ¢§ 3. The COPY verb is the preferred method of including code in COBOL
We don't check. I have considered flagging the panvalet ++INCLUDE
usage, because it has frequently been the cause of production copy
data not being moved to production. One problem is that, depending on
how our checker is invoked, the ++INCLUDE is expanded in the reader
queue, and not visible to the standards checker.

Our standards checker enforces our data division number standards,
which are that all datanames within a record must share a 3-digit
numeric prefix (copybooks are allowed to use a 4-character
alphanumeric prefix, but must still be consistent throughout an 01
record).

Although we don't enforce it in the checker, the manual requires the
following usage for data division prefixes:

100-199 program flags and switches
200-299 internal record layouts
300-399 program constants
400-499 arithmetic variables, counters, and calculation results
500-599 internal tables
600-699 program messages
700-799 report layouts (batch), BMS maps (CICS)
800-899 general work areas
900-999 subprogram parameters, abend work areas

I know from past experience that some people object strongly to
numbering datanames and paragraph names. If they don't work for you,
don't use them. I am comfortable with them, and it is relatively easy
to check for them.

› 
› ÿ¢§    6.  Permissible  USAGEs  for numeric data items are DISPLAY (implied
› ÿ¢§        if no other usage is explicitly stated), BINARY (or  COMP),  and
› ÿ¢§        PACKED-DECIMAL  (or COMP-3).  BINARY and PACKED-DECIMAL are part
› ÿ¢§        of the ANSI Standard, while COMP and COMP-3 are IBM  extensions.
We don't check for this. We probably should, since calculations can
be made more efficient if this is enforced. I recently added code to
check for data type mismatch (numeric to alphanumeric) on compares,
moves, and calculations. Also, calculations will be a little more
efficient if they are performed on signed numeric data rather than
unsigned.

› 
› ÿ¢§    8.  BINARY (COMP) usage data items must have PICTURE descriptions of
…[27 more quoted lines elided]…
› ÿ¢§        preferred limit is 6.
We issue a warning when the cyclomatic complexity exceeds 10 for the
paragraph, and recommend subdividing. We issue a warning for
excessive complexity if a single IF statement is nested more than 3
levels deep.
› 
› ÿ¢§    3.  All procedures in a program must be coded either  as  paragraphs
…[14 more quoted lines elided]…
› ÿ¢§        to follow this rule than in 1974 ANSI COBOL programs.
We prohibit GO. If the program is ANSI-85, we flag every use of NEXT
SENTENCE and require CONTINUE instead.
› 
› ÿ¢§    6.  The EXIT verb is prohibited.  In the case where a  procedure  is
…[7 more quoted lines elided]…
› ÿ¢§        Therefore,  the  ENTRY verb is prohibited.
Same here. But we require GOBACK to terminate a program, and there
can be only one.
›
› ÿ¢§ 9. The ACCEPT...FROM CONSOLE verb is prohibited. Operator communi-
› ÿ¢§ cation is felt to be too error prone for use in production jobs.
Not checked for, but our operations staff will not allow it in
production anyway.

In our checker, all paragraph names are required to be numbered.
After the numeric prefix the paragraph name must consist of an
approved action verb followed by a direct object. The verb is checked
against an internal table containing about 200 action verbs developed
from examples of good programming practice. I actually think this is
one of the most helpful rules, as far as making the program easier to
understand. The list of approved action verbs is printed in one
section of the report.

A PERFORM is required to reference a paragraph with a higher line
number. Backwards references are flagged as structure errors.

IF/ELSE/END-IF alignment is checked and reported. Alignment of
explicit scope terminators is checked (but EXEC/END-EXEC on the same
line is allowed).

Numeric and non-numeric literals are prohibited in the procedure
division (except where required by the compiler, or within parentheses
for table-handling and reference modification).

Commas are prohibited (I would use them, but I'm not allowed). The
characters '=', '<', and '>' are prohibited and EQUAL , LESS, and
GREATER are required. (Boy, are we picky!)

Although we don't flag in the standards checker, all company standard
utility subprograms should be dynamically called.

A list of non-referenced datanames (Deaddata) is produced. If the
count exceeds 50, an additional compliance error message is printed on
the report.

Any non-referenced paragraph name will result in a compliance error
message on the report. But we will probably allow non-referenced
condition names in the future, because there is some documentation
value in them.

Some of these rules are enforced because they are relatively easy to
check for. Analyzing the design is much harder. As I said in an
earlier post, we use the report from the standards checker during code
walkthroughs, and it helps us get consistent product even with a
variety of short term contract programmers.

I know from past experience that some standards that my shop requires
can be the subject of intense debates. I am not arguing that
MasterCard's standards are better than anyone else's. I am
comfortable with them, and I appreciate your input on what standards
you check for. If you write your own tool, you can create a
disciplined and repeatable approach within your company. I think
that's worth it.

Thanks again!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 8)_

- **From:** "pkei..." <ua-author-17086679@usenetarchives.gap>
- **Date:** 1996-11-13T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p9@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p9@usenetarchives.gap>`

```

In article cca··.@csc··c.com(Colin Campbell) wrote:
› IBM MVS COBOL Standards:
› What follows is one company's shot at a decent set of standards for COBOL. We

The site I am currently at has one standard (but no standards checker!)
which I quite like.

The last statement in a paragraph must be "CONTINUE.", and the fullstop
terminating this statement must be the only fullstop in the paragraph.
Given their use of sections, this gives a format like:-

BA_Section_name SECTION.
BA00_START.
... ! Body of statements
... ! with NO fullstops
Continue.
BA10_ANOTHER_LABEL.
... ! Body of statements
... ! with NO fullstops
Continue.
BA99_EXIT.
Exit.

The objective is that CUT/COPY/PASTE operations will not inadvertently
place a fullstop in an unwanted position.

It follows from the above that all 'IF' statements must be terminated
by a corresponding 'END-IF'.

<< Please no comments on 'paragraph/section' or 'go to's >>

Regards
Paul
--------------------------------------------------------------------------------
Paul Keirnan                            Title: Database Administrator
TAFE NSW, Australia                  Internet: nos··.@taf··u.au
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 9)_

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-14T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p10@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p9@usenetarchives.gap> <gap-ccc5fae54f-p10@usenetarchives.gap>`

```

pke··.@new··u.au wrote:
› The site I am currently at has one standard (but no standards checker!)
› which I quite like.
 
› The last statement in a paragraph must be "CONTINUE.", and the fullstop
› terminating this statement must be the only fullstop in the paragraph.
› Given their use of sections, this gives a format like:-
 
›        BA_Section_name SECTION.
›        BA00_START.
…[8 more quoted lines elided]…
›           Exit.
 
› The objective is that CUT/COPY/PASTE operations will not inadvertently
› place a fullstop in an unwanted position.
 
› It follows from the above that all 'IF' statements must be terminated
› by a corresponding 'END-IF'.
 
› << Please no comments on 'paragraph/section' or 'go to's    >>
 
› Regards
› Paul
…[3 more quoted lines elided]…
› TAFE NSW, Australia                  Internet: nos··.@taf··u.au

I have seen some people advocate the use of a period on a line by
itself at the end of paragraph. The best argument for this is
cut-and-paste convenience. But I find it unappealing because it
doesn't look like English text.

If you want to have only one period in a paragraph, I like the idea of
terminating the paragraph with "CONTINUE.". It will work, and I
believe it will comply with COBOL ISO standards.

IBM allows you to put "EXIT." as the last verb in a paragraph, but
their COBOL II manual clearly states that this is an IBM extension,
and that the ISO standard requires "EXIT." to be in a paragraph by
itself. According to Harvey Bookman's "COBOL/370", you can put
"EXIT." in the middle of a paragraph and the compiler will turn the
rest of the paragraph into dead code.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 7)_

- **From:** "arn burkhoff" <ua-author-9172704@usenetarchives.gap>
- **Date:** 1996-11-11T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p8@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap>`

```

cca··.@csc··c.com(Colin Campbell)
wrote regarding standards

8. BINARY (COMP) usage data items must have PICTURE descriptions of
Ã S9(4) or S9(9). The first defines a binary halfword; the
sec-
Ã ond, a binary fullword. Use of a standard number of
digits
Ã leads to easier recognition of the size of each binary
field
Ã when reading a program. This rule applies to non-copied
source
Ã code.


I recently had the "opportunity" to determine the reason for poor
performance on some code I compiled with the IBM COBOL II compiler.
Much to my surprise, part of the problem was defining a binary field as
S9(9) comp, which was fine with older IBM compilers but made the COBOL
II compiler generate reams of extra code, including multiply and divide
instructions on simple add statements while it checked for overflows.
According to IBM the compiler was acting correctly. In order to
eliminate the "problem" it is necessary to define fullword binary fields
as S9(8) comp and set NUMPROC(MIG). You can check this out for yourself
by adding 1 to a s9(9) comp field while generating an assembler map
using various compiler and field options. You may decide to change your
standards after viewing the results.
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 8)_

- **From:** "arn burkhoff" <ua-author-9172704@usenetarchives.gap>
- **Date:** 1996-11-12T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p12@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p12@usenetarchives.gap>`

```

Arn Burkhoff wrote:
› I recently had the "opportunity" to determine the reason for poor
› performance on some code I compiled with the IBM COBOL II compiler.
…[9 more quoted lines elided]…
› standards after viewing the results.
Minor correction: the option should be TRUNC(OPT) not NUMPROC(MIG)

Arn
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 9)_

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-14T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p13@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p12@usenetarchives.gap> <gap-ccc5fae54f-p13@usenetarchives.gap>`

```

Arn Burkhoff wrote:

› Arn Burkhoff wrote:
›› I recently had the "opportunity" to determine the reason for poor
…[11 more quoted lines elided]…
› Minor correction: the option should be TRUNC(OPT) not NUMPROC(MIG)
 
› Arn

Thanks for the information. After reading Harvey Bookman's books on
COBOL, I have encouraged other codes in my shop to use NUMPROC(NOPFD)
for maximum S0C7 protection, and TRUNC(BIN) in CICS programs. I will
have to check to see what our defaults are for batch COBOL II
programs.

I have noticed that most programmers in my shop code PIC 9(8) COMP or
PIC S9(8) COMP for fullword binary numbers.

Arnold Trembley
Software Engineer I (just a job title, don't know no math)
MasterCard International
St. Louis, Missouri
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 9)_

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1996-11-15T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p13@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p12@usenetarchives.gap> <gap-ccc5fae54f-p13@usenetarchives.gap>`

```

You DON'T want to use TRUNC(BIN) with IBM's VS COBOL II unless you are
getting bad results. TRUNC(OPT) truncates according to word length when
all fields are binary and according to picture when at least one of the
fields in the operation is not binary. TRUNC(BIN) will truncate to the
actual size of the field. HOWEVER the price you pay is that all
arithmetic and compares done on binary fields results in the operands
being converted to packed decimal for the operations and any arithmetic
results being converted back to binary. Even in CICS there should be no
need to use TRUNC(BIN) and I have put many programs into production with
TRUNC(OPT). Note that this is true on release 4 and should also be true
for COBOL for MVS and VM (or is it now LE). You also should consider
switching from NUMPROC(NOPFD) to NUMPROC(MIG). It won't do as much zone
forcing but you should probably replace the zone forcing with a one time
file cleanup and better edit validation. You may well be getting wrong
answers because a problem is being masked. If a field is supposed to be
numeric it should contain valid numerics and anything else indicates that
something is wrong. NUMPROC(PFD) would probably be dangerous because 123
instead of 12C in S9(3) DISPLAY field will be treated as not numeric
because an F zone is not an operational sign. (Determining whether a hex
F in a packed field on an IBM mainframe is an operational sign is an
exercize in computer theology).

›  
› Arn Burkhoff  wrote: 
…[35 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at morrisc.nbnet.nb.ca
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 7)_

- **From:** "r..." <ua-author-2587243@usenetarchives.gap>
- **Date:** 1996-11-12T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p8@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap>`

```

In article <5682ji$o.··.@hac··c.com>
cca··.@csc··c.com(Colin) "Colin Campbell" writes:
› IBM MVS COBOL Standards: What follows is one company's shot at
› a decent set of [ANSI 1985 programming] standards..
…[5 more quoted lines elided]…
›     generated.  This rule applies to non-copied source code.

While applauding the standards you have so kindly shared with us, I
suggest that 'temporary' recommendations regarding the efficiency
of the compiler, operating system and hardware should be separated
from the 'permanent' standards for program layout and logic.

The reason is that standards are rarely maintained themselves, so
that some absolute rules can persist well beyond their natural
life when the original reasoning is no longer true.

IBM legacy systems seem to be prone to the thinking that there can
be no other way to design hardware or write system software.
COBOL is independent of all that, fortunately.

Maybe there are standards for writing programming standards :-?

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

###### ↳ ↳ ↳ Re: Flex, Bison, Ebcdic, IBM/MVS

_(reply depth: 8)_

- **From:** "ccam..." <ua-author-17086113@usenetarchives.gap>
- **Date:** 1996-11-13T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccc5fae54f-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ccc5fae54f-p16@usenetarchives.gap>`
- **References:** `<55q1dv$6rf@news1.Belgium.EU.net> <gap-ccc5fae54f-p2@usenetarchives.gap> <gap-ccc5fae54f-p3@usenetarchives.gap> <gap-ccc5fae54f-p5@usenetarchives.gap> <gap-ccc5fae54f-p6@usenetarchives.gap> <gap-ccc5fae54f-p7@usenetarchives.gap> <gap-ccc5fae54f-p8@usenetarchives.gap> <gap-ccc5fae54f-p16@usenetarchives.gap>`

```

In <847··.@min··o.uk>, r.··.@min··o.uk (R Ross-Langley) writes:
› In article <5682ji$o.··.@hac··c.com>
› cca··.@csc··c.com(Colin) "Colin Campbell" writes:
…[16 more quoted lines elided]…
› 
Richard,
Your point is well taken, as was the comment about PICtures for BINARY items
posted elsewhere.

This checker has never been migrated to another platform, so 'universal'
thinking hasn't yet intruded on my consciousness.

On the other hand, the COBOL standard itself has come to recognize this
particular format for storing data, regardless of hardware ( the wisdom of which
I wonder about). Therefore, the part about number of digits (and maybe the part
about signs) could apply more widely than it was ever planned to do.
Colin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
