[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: how to execute logic during precompiling phase ?

_8 messages · 7 participants · 1999-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: Q: how to execute logic during precompiling phase ?

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371347BC.678EAA93@NOSPAMhome.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com>`

```
John Piggott wrote:
> 
> I do this all the time. Just code a REPLACE near the start of your
…[7 more quoted lines elided]…
>    .

Hmmm.  This could be used to have a program constant which is
maintainable.  Particularily this could be used to replace :TABLE-LENGTH
with a constant in both the occurs clause and in bounds checking.

I was wondering - can we have a complete program in a copy statement? 
And can the REPLACE command apply to multiple programs in one source
module?

Then we could write a program with pseudo-text, put it in the copy
library, and allow it to be copied in with customizations for a
particular application.
```

#### ↳ Re: Q: how to execute logic during precompiling phase ?

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com>`

```
There's probably a way to do that. This could make a reasonable macro-like
approach, which would be just about the only way I could see allowing
procedure division code in a copybook, other than perhaps substitutable
copy libraries of platform dependent implementations of small standardized
pieces of code - which again would be a wonderful candidate for a
full-blown macro language with conditional compile-time expressions etc.
like in PL/1.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Howard Brazee wrote in message <371347BC.678EAA93@NOSPAMhome.com>...

>Then we could write a program with pseudo-text, put it in the copy
>library, and allow it to be copied in with customizations for a
>particular application.
```

##### ↳ ↳ Re: Q: how to execute logic during precompiling phase ?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f136a$j1m$1@news.igs.net>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com> <#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com>`

```
Actually, I use procedural copies all the time.  All of my date
calculations, for example.  Same for standard reporting, page headers, and
all that jazz. Stood me in good stead for Y2K.

Robert M. Pritchett wrote in message
<#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com>...
>There's probably a way to do that. This could make a reasonable macro-like
>approach, which would be just about the only way I could see allowing
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Q: how to execute logic during precompiling phase ?

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371494C5.EF787DAA@NOSPAMhome.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com> <#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com> <7f136a$j1m$1@news.igs.net>`

```
I bet just about anybody who didn't have procedural copies before Y2K
remediation does now.  But I haven't used multiple programs in one
source member.  What intrigues me is putting an entire program in a copy
member, and using the REPLACE command to customize it to fit the main
program.  

There was once some discussion of having copies within copies.  I wonder
what the priority would be with layers of copies and replace commands. 
Let's say you copy in a called program and use replace to pick what gets
copied in the called program.  I bet replace would be a single pass, but
would love for it to be multiple pass.

Donald Tees wrote:
> 
> Actually, I use procedural copies all the time.  All of my date
…[28 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Q: how to execute logic during precompiling phase ?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f2blj$qs1@dfw-ixnews6.ix.netcom.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com> <#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com> <7f136a$j1m$1@news.igs.net> <371494C5.EF787DAA@NOSPAMhome.com>`

```



Howard Brazee wrote in message <371494C5.EF787DAA@NOSPAMhome.com>...
..
>
>There was once some discussion of having copies within copies.  I wonder
…[3 more quoted lines elided]…
>would love for it to be multiple pass.

This is why the draft Standard prohibits REPLACING with nested COPIES.

Some vendors that allow nested copies today, allow REPLACING - but only
once - either at the top level or bottom-level.
```

###### ↳ ↳ ↳ Re: Q: how to execute logic during precompiling phase ?

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37155a34@news3.us.ibm.net>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com> <#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com> <7f136a$j1m$1@news.igs.net> <371494C5.EF787DAA@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:371494C5.EF787DAA@NOSPAMhome.com...
> I bet just about anybody who didn't have procedural copies before Y2K
> remediation does now.  But I haven't used multiple programs in one
…[8 more quoted lines elided]…
> would love for it to be multiple pass.

try the SYSET preprocessor at http://etk.com  then downloads.

Here is the 'readme':

The ETK Cobol Preprocessor SYSET:

Usage:  syset [filename...] [switch...]

SYSET preprocesses COB, CPY, or CBL files that contain non-portable or
special code. No file extensions should be given, as SYSET looks for .COB,
.CPY, or .CBL implicitly. If no parameters are given, SYSET shows a help
text. SYSET assumes a traditional Cobol source structure with sequence
numbers in columns 1-6, and comments in cols 73-80.

By default, SYSET looks in the current directory for files. You can set an
environment variable ETK to a path list to tell SYSET where to look, e.g.

set etk=d:\myproject1;c:\project2;

The output file is always written to the current directory. The output
file uses TABs. If you do not want this, use the exptab  utility
supplied with this distribution to turn the TABs into spaces.

SYSET allows you to maintain a single version of a file which may have
several
target systems.  Uses for SYSET include: maintaining non-portable sources;
keep one schema or program with embedded versions for several systems;
manage debugging or scaffolding code (e.g. assertions).

SYSET should not be misused as a way of sneaking significant amounts of
non-portable code into a large application.  The problem here is that it is
very difficult to maintain the code for several targets in parallel.

Switches (can also be abbreviated to first letter):

/system:target          Specify target name; default is DEFAULT.

/filter:filename        Produce clean 'filtered' file as output to the file
                        given.

/output:filename        Direct the output to the file instead of changing
the
                        input file in place.

/type:filetype          Force filetype of COB, CPY, or CBL.

/parm:parameter         General parameter value passed to SYSET.

/quiet                  Suppress informational messages.

/restore                Restores defined values to their definitions.

Example:
> syset myprog /system:as400 /filtered:prog400

If you do not use the /filtered switch, SYSET copies the input file to
itself
(with appropriate safeguards against errors) looking for and acting upon
commands in comment lines as follows:

*#SET system...
        Defines the set of valid system names.  You must define
        such a command at the start of the file (e.g. after
        PROGRAM-ID).  Remember that a COBOL program cannot
        start with a comment line.

*#IF [system...] | logical expression
        Starts a block of code to be output if any of the listed
        systems is the current target.  If not, the code up to the
        next #ELSE, #ELIF, #CASE  or #END is commented.  If
        no system is specified, DEFAULT is assumed.

*#IFNOT [system...] | logical expression
        Starts a block of code to be output if none of the listed
        systems is the current target.

*#ELSE
        Includes/excludes the block of code until the next #END
        depending on the inverse of the condition on a previous
        #IF, #IFNOT, #ELIF or #CASE command.

*#ELIF [system...] | logical expression
        Combined #IF and #ELSE.  Note that #IFs and #IFNOTs
        cannot be nested.

*#EF [system...] | logical expression
        Same as #ELIF.

*#CASE [system...] | logical expression
        Like #ELIF, except that the first #IF may be a #CASE.

*#END
        Ends a block of code starting with an #IF, #IFNOT,
        #ELSE, #ELIF or #CASE.

*#END-IF
        Same as #END.

*#.
        Same as #END.

*#DEF definition = value    [ -- any comment text ]
        Defines a substitution value.  The definition must be a
        word with no embedded blanks.  The value can be any
        text, including other definitions (prefixed by #).  If a
        definition value refers to other definitions the substitution
        is made when the #DEF command is processed.  There
        must be white space on both sides of the equal sign.  An
        optional comment can follow a pair of dashes preceded by
        a space beginning at least three characters after the equal
        sign.  The comment extends to the end of the line.

*#FORMAT definition = value format
        Defines a substitution value like the #DEF command
        except that only characters specified in the format string
        are used.  The format string is a mixture of literal
        characters (except digits and the equal-sign which both
        must be escaped by being prefixed by `=') and of ranges
        of the form `from pos':`to pos'.  Characters from the value
        replace the range in the format string.  Example: value
        19951231, with format 5:6/7:8/3:4 results in 12/31/95.

*#LET definition = arithmetic expression
        Defines a substitution value as an arithmetic expression.

*#DROP definition : logical expression
        Defines a condition under which a line containing a
        reference to the definition name should be commented
        out.  A logical expression evaluates to 1 (true) or 0 (false).
        The line is commented out if the condition is true at the
        time when the line is processed.  There must be white
        space on both sides of the colon.  Use the #DROP
        command rather than tedious repetitions of the #IF
        command when several lines are conditioned upon
        definition values.

*#DROP definition relational operator arithmetic expression
        This is a simpler version of the #DROP command.  There
        must be white space on both sides of the relational
        operator.

*#INCLUDE filename [filetype]
        Continue input from the file given (the default filetype is
        that of the original input file) until it is exhausted, then
        return to the original input file where it left off.  Include
        files can be nested, but are meant for processing of pre-
        processor commands only (e.g. #SET, #DEFs, and
        #LETs), and are not copied to the output file.

*#SPACE character | NONE
        The character given is used as a 'hard space' allowing
        leading/trailing spaces in definition values.  NONE
        cancels a previous setting of the hard-space character,
        which is off when SYSET starts.

*#SKIP character | NONE
        The character given is used as a 'skip character' in the
        following sense: when a definition value containing skip
        characters is inserted, a skip character is not output, but
        instead causes the text that follows to be shifted one
        character position to the left, allowing fine control over
        the alignment of the resulting text.  NONE cancels a
        previous setting of the skip-character, which is off when
        SYSET starts.  If you use the #SKIP command, you must
        specify which target system was used when you recover
        the file, because definitions may have different numbers
        of skip characters for different targets.

*#DISPLAY text
        Displays the text even if the /QUIET switch is used.

*#CANCEL {text}
        Cancels the run of SYSET, recovering the original file.
        Displays an optional text even if the /QUIET switch is used.

*#* something
        A comment line which is excluded from filtered output

*# blank line
        A comment line which is excluded from filtered output.

**...
        This is a comment line which is kept in filtered output.

*
        Comment lines beginning with a single asterisk cannot be
        handled correctly by SYSET if the comment appears inside
        a block of code under control of an #IF, #IFNOT, #ELIF,
        #ELSE or #CASE command.

Note, that some command have aliases, e.g. #ELIF and #END, to allow
you to use a form you may feel more comfortable with.

Include files allow targets and definitions to be centrally defined and
managed.

Here is an example of an include file:

*#SET WANG AS400 GCOS7 GCOS8

*#CASE WANG
*#    DEF INTEGER = BINARY
*#    DEF SHORT   = #INTEGER
*#CASE AS400
*#    DEF INTEGER = PIC S9(5)  COMP
*#    DEF SHORT   = PIC S9(4)  BINARY
*#CASE GCOS7
*#    DEF INTEGER = PIC S9(4)  BINARY
*#    DEF SHORT   = #INTEGER
*#CASE GCOS8
*#    DEF INTEGER = COMP-6
*#    DEF SHORT   = COMP-1
*#ELSE
*#    DEF INTEGER = PIC S9(4)  COMP
*#    DEF SHORT   = #INTEGER
*#END

Four target systems are defined by the *#SET command.  Definitions of
INTEGER
and SHORT are then made for each of the four systems and (at the ELSE) for
all
other systems. Note, that at times a SHORT is simply the same as an INTEGER
SHORT = #INTEGER).  Use of another definition in a definition requires the
definition used to be defined first.

A block of code has been highlighted for the AS/400 target.  To improve
readability, SYSET commands can be indented as long as the '#' marker still
appears in column eight.


To recover the original text without substituted definitions, use the
/RESTORE switch (which also overrides a possible /SYSTEM switch):

> syset editpk /restore

A convenient use of the /RESTORE switch is illustrated by the following
MS-DOS
.BAT file:

CALL SYSET %1 /R                     restore original
CALL EDIT  %1                        edit original
CALL SYSET %1 /S:PC                  make PC version
CALL COBOL %1                        compile PC version

If definitions used skip characters, you must specify the original target
system when you recover, eg.:

> syset editpk /system:as400 /restore

The expression used with the #IF, #IFNOT, #ELIF, #LET, and #DROP commands is
evaluated by CALCPK unless it contains strings in which case the value of
the
expression is the text itself.  Logical expressions contain relational
operators (like = or >=) and evaluate to 1 (true) or 0 (false).  The result
of an arithmetic expression is truncated to a signed integer with at most
9 digits.

Here are some examples of the use of expressions:

 ENVIRONMENT DIVISION.
*#SET BULL-TDS BULL-TP8 TEST

 CONFIGURATION SECTION.
*#IF BULL-TDS
*#   LET RECSIZE  = 8192
*#   LET NSIZE    = 510
*#   LET MAXLNK   = 32768 / #NSIZE
*#ELSE
*#   LET RECSIZE  = 8192
*#   LET NSIZE    = 256
*#   LET MAXLNK   = 32768 / #NSIZE
*#END
*#
*#*FIXED VALUES
*#   DEF IDSIZE   = 26    -- SIZE OF ID HEADER
*#
*#*DERIVED VALUES
*#   LET MAXBLK   =  #RECSIZE -  4
*#   LET NOD/REC  = (#RECSIZE -  #IDSIZE) / #NSIZE
*#   LET CTXRFILL = (#RECSIZE -  #IDSIZE) % #NSIZE

 WORKING-STORAGE SECTION.

 01  CTXRIO-DATA.
     02  CTXRIO-KEY              PIC 9(6).
     02  CTXRIO-DATA-PART.
         03  CTXRIO-ID           PIC X(#IDSIZE).
         03  FILLER              REDEFINES  CTXRIO-ID.
             04  CTXRIO-NODE-COUNT
                                 PIC 9(2).
             04  CTXRIO-PROGRAM  PIC X(8).
             04  CTXRIO-USER-ID  PIC X(8).
             04  CTXRIO-HHMMSSCC PIC 9(8).
         03  CTXRIO-NODES                   OCCURS #NOD/REC.
             04  CTXRIO-NODE     PIC X(#NSIZE).
*#IF #CTXRFILL > 0
         03  FILLER              PIC X(#CTXRFILL).
*#END
     02  FILLER                  REDEFINES  CTXRIO-DATA-PART.
         03  CTXRIO-BLOCK-FREE   PIC 9(4).
         03  CTXRIO-BLOCK-MAP    PIC X      OCCURS #MAXBLK TIMES.

You could also have controlled the use of the line with the #CXTRFILL
definition value by declaring a #DROP condition:

*#DROP CTXRFILL :  #CTXRFILL = 0

This is particularly useful if several instances must be conditional;
an even simpler way can be used if the expression does not contain
other definitions:

*#DROP CTXRFILL = 0

The conditions also work with strings, like:

*#IF "#TARGET" = "PC"

There are several built-in standard values that can be used in expressions
(and be redefined at any time):

#SIZE
        This value is increased by the size of each PIC clause
        encountered.  OCCURS and REDEFINES clauses are not
        taken into account.

#LINE
        This value is incremented by one for each line output.

#DATE
        This value contains the date in the form YYYYMMDD.  Use
        the #FORMAT command to define a formatted synonym.

#PARM
        This value contains the general parameter passed from the
        command line.

#TARGET
        Evaluates to the target system specified with the /SYSTEM switch.

Instead of hard-coding IDSIZE in the example above, we could use the #SIZE
value as follows:

 01  CTXRIO-DATA.
     02  CTXRIO-KEY              PIC 9(6).
     02  CTXRIO-DATA-PART.
*#LET SIZE = 0
         03  CTXRIO-NODE-COUNT   PIC 9(2).
         03  CTXRIO-PROGRAM      PIC X(8).
         03  CTXRIO-USER-ID      PIC X(8).
         03  CTXRIO-HHMMSSCC     PIC 9(8).
*#LET NOD/REC  = (#RECSIZE -  #SIZE) / #NSIZE
*#LET CTXRFILL = (#RECSIZE -  #SIZE) % #NSIZE
         03  CTXRIO-NODES                   OCCURS #NOD/REC.
             04  CTXRIO-NODE     PIC X(#NSIZE).

Even better would be to store the value of #SIZE in an appropriate
intermediate
definition and then use that:

*#LET IDSIZE   = #SIZE
*#LET NOD/REC  = (#RECSIZE -  #IDSIZE) / #NSIZE

Definitions are not evaluated in lines beginning with two or more asterisks,
or with `*#', but are evaluated in all other comment lines.  This allows you
to trace the evolution of redefined or calculated definition values by
placing
them in comment lines.

Definitions are not evaluated in strings except if the string is on the
left-hand side of a comparison.

Definitions should not be equal to the beginning of other definitions, nor
should they contain blanks, the punctuation marks (".", ",", ";",
parentheses or
quotes) or the definition introducer itself ("#").  When building
expressions,
you should surround binary operators with white space just as COBOL
requires.

===================

Here is a real-life example: TPMANXX.
I use it like this: syset tpmanxx /f:tpman /s:tp8

===================

Source:

SYSET is written in portable ETK-style Cobol and calls I/O programs
to do I/O.  All such programs have names ending in IO.

SYSET also calls some ETK-packages to perform other non-portable
functions; these programs have names ending in PK.

SYSET is delivered with this distribution.
Contact leif@etk.com for the non-portable stuff if you need them.

All the packages here are coded in the ETK coding style. Click
here to see the rationale for this style.
```

###### ↳ ↳ ↳ Re: Q: how to execute logic during precompiling phase ?

_(reply depth: 4)_

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xb2R2.5258$Ay2.970578@news1.rdc1.on.wave.home.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com> <#5iN6fhh#GA.366@nih2naad.prod2.compuserve.com> <7f136a$j1m$1@news.igs.net> <371494C5.EF787DAA@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:371494C5.EF787DAA@NOSPAMhome.com...
> I bet just about anybody who didn't have procedural copies before Y2K
> remediation does now.  But I haven't used multiple programs in one
> source member.  What intrigues me is putting an entire program in a
copy
> member, and using the REPLACE command to customize it to fit the main
> program.
>
> There was once some discussion of having copies within copies.  I
wonder
> what the priority would be with layers of copies and replace commands.
> Let's say you copy in a called program and use replace to pick what
gets
> copied in the called program.  I bet replace would be a single pass,
but
> would love for it to be multiple pass.
>
<<SNIP>>

*********** WARNING ********
* shameless self-promotion *
*********************************

If you're really interested in this kind of question pick up Paul
Bassett's book, "Framing Software Reuse: Lessons from the Real World" or
visit http://www.netron.com/pbbook.htm. There's a skimpy web page on
.REPLACE which kind of covers replacement scoping, albeit in the context
of Netron's product. It ignores .REPLACE LOCAL (the replacement cannot
be superceded by a parent replacement), and .REPLACE GLOBAL (replacement
in a child changes the value in the parent). It's covered in more detail
in the book.

The sample at http://www.netron.com/frames/examples.htm is a bit
meatier.
```

#### ↳ Re: Q: how to execute logic during precompiling phase ?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37134A4B.B3EA26C4@zip.com.au>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <371379C4.5B6@compuserve.com> <371347BC.678EAA93@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> John Piggott wrote:
…[21 more quoted lines elided]…
> particular application.

I actually looked it up in IBM it is a compiler directing
statement, so theoretically the answer is yes.

Ken
How did I miss this one...  reading the group pays dividends
again...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
