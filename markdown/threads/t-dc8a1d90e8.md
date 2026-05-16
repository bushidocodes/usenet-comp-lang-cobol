[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comments on draft COBOL 2002 Standard

_1 message · 1 participant · 2001-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Comments on draft COBOL 2002 Standard

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2001-04-20T19:53:20+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AE00710.31BE32FB@melbpc.org.au>`

```
Here is a copy of my comments on the draft standard.

My main gripes are

- too many features of dubious value are mandatory (screen,
report writer)
- OO should be put in a new language "Object COBOL" rather than
being mandatory in COBOL2002
- too many ridiculous restrictions eg cannot redefine a pointer.
- too many magic numbers eg line length must be less than 255,
literals must be less than 160 bytes, PIC must be less than 50
etc etc etc
- editorially, there is too much use of undefined terms - the
list of definitions and index need major work
- the tightening of copyright

If the tables below are not lined up, change your browser to a
fixed width font. I will upload html to my web page fairly soon
and post a link.

I am not late submitting this becasue different deadlines apply
outside the USA. However I realise that not many of these
comments will be accepted, apart from the typos.

Tim Josling

                   Date        Document

                   19   April  Comment  on   COBOL 2002

Introduction:

My Name is  Tim Josling. I am developing a free COBOL  compiler
as part of a
world wide team. My  comments are written from that perspective.
I am basing
my  comments  on  the  assumption that  the  standards  body 
would wish  to
encourage implementations of the standard.

My email address is tej at melbpc dot org dot au.

 Comment Clause/ Subclause  Paragraph     Type of
comment            COMMENTS            Proposed change
 Number                      Figure/         (General/
                              Table    Technical/Editorial)

 1       Copyright notice  First       General              The
copyright notice would Add amendment to
                                                           
appear to prevent copying  permit copying for
                                                            the
draft in order to      purpose of review.
                                                           
review it.

 2       Copyright notice  First       General              This
is far more           Allow reasonable
                                                           
restrictive than the       use of excerpts
                                                           
notice in COBOL 85. It     from the standard
                                                            will
make it extremely     in the
                                                           
difficult for us to        documentation for
                                                           
provide adequate           COBOL compilers.
                                                           
documentation as any
                                                           
description of COBOL is
                                                           
almost by definition based
                                                            on
the standard, and
                                                           
therefore potentially in
                                                           
breach of copyright.

 3       Foreword          Last        General             
Patents. The existence of  The committee has
                                                           
patents on parts of the    issued a call for
                                                           
language, and which cannot patents and should
                                                            be
worked around, may      consider amending
                                                           
preclude the development   to standard if
                                                            of a
complete free COBOL   necessary, to
                                                           
compiler. A free compiler  allow full
                                                           
cannot included patented   implementations
                                                           
algorithms                 that are not in
                                                                                      
breach of patents.

 4       Acknowledgement   All         General              Not
clear at all which     The standard
                                                           
material within the        should make clear
                                                           
standard is covered by     which material is
                                                            this
concession.           allowed to be used
                                                                                      
in COBOL manuals.

 5       3.1.1             2nd         Editorial            It is
not specified how to Clarify what is
                                                           
distinguish syntax rules   meant by 'syntax
                                                            from
other rules. Some     rules?. Presumably
                                                            rules
are under headings   any rule under a
                                                            for
syntax rules and       heading 'syntax
                                                           
others under headings for  rule?. However in
                                                           
general rules, but others  at least one case,
                                                            are
under neither. How     this situation can
                                                           
exactly do you distinguish only be
                                                           
syntax rules from other    distinguished at
                                                           
rules.                     run time. See
                                                                                      
comment 138.

 6       3.1.8             1)          Editorial            Term
'language element? is Add a definition.
                                                            not
defined.               In general every
                                                                                      
technical term
                                                                                      
used should be in
                                                                                      
the list of
                                                                                      
definitions which
                                                                                      
should have cross
                                                                                      
references to the
                                                                                      
detailed
                                                                                      
description.

 7       3.1.8             5th         General              The
implication of the     Add requirement
                                                            fact
that implementors are that vendors
                                                            not
required to provide a  provide a
                                                            way
to turn off            mechanism to turn
                                                           
non-standard keywords      off non standard
                                                            means
that it is           keywords. This is
                                                           
impossible to write a      far less onerous
                                                           
program which is           that the other
                                                           
guaranteed to compile      requirement to
                                                            under
a standards          flag use of other
                                                           
conforming compiler. This  extensions.
                                                           
should be changed

 8       3.1.13            1st         General             
Vendors are not required     A. Require
                                                            to
document limits. No          vendors to
                                                           
minimum program size or         document any
                                                           
complexity has to be            limits other
                                                           
supported. This again           than 'total
                                                            makes
it impossible to          available
                                                            write
a program that will       memory?.
                                                            be
sure to work on a            Suggest that
                                                           
conforming compiler.            vendors are
                                                                                           
urged to
                                                                                           
refrain from
                                                                                           
imposing such
                                                                                           
limits.
                                                                                        
B. Specify
                                                                                           
minima for at
                                                                                           
least

                                                                                         
* levels of
                                                                                           
nested
                                                                                           
statements
                                                                                           
(10)
                                                                                         
* number of
                                                                                           
forward
                                                                                           
references
                                                                                           
(100)
                                                                                         
* number of sub
                                                                                           
clauses in
                                                                                           
any statement
                                                                                           
(10)
                                                                                         
* number of
                                                                                           
levels of
                                                                                           
nested data
                                                                                           
definitions
                                                                                           
(10)
                                                                                         
* Other items
                                                                                           
as per
                                                                                           
comments
                                                                                           
below should
                                                                                           
have minimum
                                                                                           
limits of
                                                                                           
1,10,100
                                                                                           
rather than
                                                                                           
various odd
                                                                                           
values.

                                                                                      
- etc

 9       4                 All         Editorial            No
cross references to     Add cross
                                                           
detail about defined items references eg See
                                                                                      
Section 4.1.1 on
                                                                                      
page 77.

 10      4.6               1st         Editorial            Space
character not        Add definition and
                                                           
defined and not mentioned  cross reference
                                                            in
the index

 11      4.11              1st         Editorial            Group
Item not defined and Add definition and
                                                            not
mentioned in index     cross reference.

 12      4.27              2nd         Editorial           
"examaple" (sic)           Correct the
                                                                                      
spelling

 13      4.27              2nd         Editorial            What
does this paragraph   Clarify paragraph.
                                                            mean
and what is it there
                                                            for.

 14      4, also 8.4.2     All         Editorial            Term
'identifier? is       Add definition and
                                                           
widely used but not in the cross reference.
                                                            list
of definitions. It is Change the term to
                                                            also
misleading and its    'data access
                                                            use
has been extended far  expression? or
                                                           
beyond the intuitive       some other
                                                           
meaning of identifier.     appropriate term.

 15      4.97              1st         Editorial            This
definition seems to   Clarify
                                                            be
circular.

 16      4.116             1st         Editorial            The
technical term         Substitute another
                                                           
'rightmost element? is     term or claarify.
                                                            used
but what does it mean
                                                            eg in
a little endian vs
                                                            big
endian world.

 17      4.170             1st         Editorial           
Ambiguous                  After 'last? add
                                                                                      
'and only the
                                                                                      
last?.

 18      4                 All         Editorial            Term
'Separator space? not Add definition and
                                                           
defined though widely used cross reference.

 19      4.176             1st         Editorial            Term
'statement? has no    Add definition and
                                                           
definition though it is    cross reference.
                                                           
widely used.

 20      4                 All         Editorial            I
believe many other terms Scan document
                                                            are
also widely used but   looking for
                                                            not
defined.               undefined terms
                                                                                      
and add
                                                                                      
definitions.

 21      5.1               2nd         Technical           
Requirement for parts of a Remove assumption
                                                           
construct to be in order   that items have to
                                                            is
excessive. For example  be in order, where
                                                            why
does 'redefines? have  possible eg
                                                            to be
first.               clauses of data
                                                                                      
item, at end/not
                                                                                      
at end etc.

 22      5.1.4             1st         Technical            There
is no reason why     Change rule to
                                                            level
numbers must be 1 or state that level
                                                            2
digits. It is yet        numbers must be
                                                           
another rule that adds no  unsigned integers
                                                            value
and makes the        in the specified
                                                           
language more complex. It  ranges.
                                                            also
makes compilers
                                                           
slower due to the
                                                           
requirement to issue
                                                           
warnings.

 23      6                 3a)         Technical           
Another rule which adds no Change rule to
                                                            value
but adds yet another state that the
                                                            magic
number the           compiler shall
                                                           
programmer needs to be     accept lines of
                                                            aware
of, and the compiler length up to at
                                                           
writer needs to check for. least 100, shall
                                                            This
also makes generating document any
                                                            code
by machine more       restriction, and
                                                           
complex.                   need not warn
                                                                                      
about longer
                                                                                      
lines.

 24      6.1.2             "- '-       Technical            Why
are there three        Remove literal
                                                           
literal concatenation      continuation
                                                           
mechanisms (& and "- and   except for fixed
                                                            old
style)? This creates a format legacy
                                                            lot
of complexity and      continuation.
                                                           
corner cases.              Allow literal
                                                                                      
concatenation in
                                                                                      
any context but
                                                                                      
only for
                                                                                      
non-numeric
                                                                                      
literals.

 25      6.1.2.1           7)          Editorial            Term
'ljne? is undefined.  Add definition

 26      6.2               Margin R    Technical            Why
the insistence that    Allow R-margin to
                                                            the R
margin must be       be end of line
                                                           
fixed. The ?85 standard is (require vendor
                                                            not
quite so specific. Why documentation of
                                                            could
the right margin not this).
                                                            be
'end of line? which is
                                                           
usually more natural

 27      6.2.1             1st         Technical            Any
character would seem   Qualify 6 3)b) to
                                                            to
include end of line     allow the vendor
                                                           
character, which seems to  to specify whether
                                                           
preclude text format       control characters
                                                           
compiler input files.      are allowed in the
                                                                                      
sequence area

 28      6.2.4             1)          Editorial            Term
'blank line? is not   Add definition.
                                                           
defined.                   Specify how much
                                                                                      
of the line is
                                                                                      
blank. Are
                                                                                      
comments allowed
                                                                                      
etc.

 29      6.2.4             All         Editorial            This
section is very       Do not allow
                                                           
complex and hard to        continuation of
                                                           
understand.                lines in free
                                                                                      
format and only
                                                                                      
allow COBOL 85
                                                                                      
continuation in
                                                                                      
fixed lines. Then
                                                                                      
people will be
                                                                                      
able to understand
                                                                                      
it.

 30      6.2.4             10th        Editorial            Term
'invocation operator? Add definition
                                                            is
not defined

 31      6.2.4             2nd         Technical            Seems
to imply by use of   Change 'a ?line?
                                                            'a?
that a literal can     to 'one or more
                                                            only
be continued once.    ?lines?

 32      6.3.1             2nd         Technical            I do
not understand why    Remove last
                                                            the
rule that a            sentence of this
                                                           
continuation has to        paragraph ("at
                                                           
contain at least one       least one ?").
                                                           
character of the literal
                                                           
exists. It may not make
                                                            much
sense to do so, but
                                                            why
have this rule? It is
                                                           
another pointless thing
                                                            for
the compiler to check.

 33      6.4               6)          Editorial            Term
'Source Indicator? is Add definition and
                                                            not
in list of definitions cross reference.

 34      7                 Last        Editorial            The
information about when Add details and/or
                                                           
debugging lines are        cross reference
                                                           
processed should be
                                                           
included also in the
                                                           
sections on debugging
                                                            lines

 35      7.1.2.2           9)          Technical            Not
clear what the         Clarify.
                                                           
matching rule is for
                                                           
continued literals. Do
                                                            they
both have to have the
                                                            same
continuation
                                                           
structure, or do they both
                                                            have
to have the same
                                                            value
after pasting the
                                                           
continuations.

 36      7.1.2.2           12)         Technical           
Arbitrary limit of 322     Remove limit.
                                                           
should be removed. Yet
                                                           
another magic number to
                                                           
remember and enforce.

 37      7.1.2.3           11)         Technical            This
is not a necessary    Remove restriction
                                                           
restriction and creates    and specify how
                                                           
significant difficulties   the processing
                                                            for
the programmer.        works using an
                                                                                      
extension of the
                                                                                      
excellent 'stages?
                                                                                      
concept used in
                                                                                      
s7.

 38      7.1.3.3           7a)         Technical           
Keyword 'ALSO? is          Replace by
                                                           
misleading and it is       'REPLACE ?.SAVE?
                                                           
actually 'instead of? and
                                                           
pushes the existing
                                                           
replace on to a stack.

 39      7.2.2.3           3) and 4)   Technical            Why
is there a distinction Allow free form
                                                            as to
when free form       comments after
                                                           
comments can follow a      compiler
                                                           
compiler directive. Yet    directives in all
                                                           
another rule to enforce    cases.
                                                            for
no obvious reason eg
                                                            for
each line one must
                                                           
remember that it was free
                                                            for
fixed format in order
                                                            to
enforce the rules.

 40      7.2.2             8)          Technical            This
seems to presuppose a This should be
                                                           
certain sequence of        reworded in terms
                                                           
processing conceptually at of a conceptual
                                                            least
but it is not clear  sequence of
                                                            at
all what the sequence   operations (eg
                                                            is.
It is just a set of    continued literals
                                                           
arbitrary rules which seem are lasted
                                                            to
make little sense as    together, then
                                                            they
stand.                compiler
                                                                                      
directives are
                                                                                      
processed or
                                                                                      
whatever). This
                                                                                      
was done very
                                                                                      
successfully eg in
                                                                                      
the C language.
                                                                                      
Without it, it is
                                                                                      
very difficult to
                                                                                      
understand what is
                                                                                      
intended.

 41      7.2.5.1           1d)         Technical            This
requirement of        This will be quite
                                                           
checking for division by   difficult to check
                                                            zero
would seem to be a    syntactically.
                                                           
syntax rule that the       Clarify what is
                                                           
compiler must check for.   the requirement of
                                                                                      
the compiler.

 42      7.2.7.1           1c)         Editorial            Term
'defined condition?   Add definition and
                                                            is
not in the definitions  cross reference
                                                            list.

 43      7.2.8             1st         Technical            Why
can?t you specify a    Allow
                                                           
calling convention for     specification of
                                                           
function names?            calling convention
                                                                                      
for function-names
                                                                                      
as well. This
                                                                                      
seems to be
                                                                                      
implied by 7.2.8.2
                                                                                      
(3) which refers
                                                                                      
to functions/

 44      7.2.13.2          3)          Technical            This
rule seems to be a    It would be better
                                                           
consequence of some        is the conceptual
                                                           
conceptual sequence of     sequence of
                                                           
operations.                operations were
                                                                                      
made explicit and
                                                                                      
these rules would
                                                                                      
them follow simply
                                                                                      
from the sequence.

 45      7.2.14.3          2)          Editorial            'or
implied? - how can ON  Remove 'or
                                                            be
implied as it is not    implied?.
                                                            the
default?

 46      7.2.18.2          3)          Editorial           
'test?                     Change to 'text?

 47      7.2.18            1st         Technical           
Programmer has to put a    Allow compiler
                                                           
directive in the source to writer to specify
                                                            turn
on free format.       default format
                                                                                      
externally.
                                                                                      
Otherwise
                                                                                      
programmers will
                                                                                      
be doomed to put
                                                                                      
>>SOURCE FORMAT
                                                                                      
FREE in programs
                                                                                      
forever. This is
                                                                                      
just an extension
                                                                                      
of the fact that
                                                                                      
COPY programs take
                                                                                      
the default mode
                                                                                      
from COPY verb.

 48      8.1.1             2nd         Technical            'at
runtime? is too        Change to 'at
                                                           
prescriptive. Should allow runtime or before?
                                                           
translation before
                                                           
runtime.

 49      8.1.1             2nd         Technical            What
constraints can the   Clarify. Add to
                                                           
implementor put on the     list of
                                                            class
literal?             implementor
                                                                                      
defined elements

 50      8.3.1.1           1st         Technical            Fixed
word size limit of   Replace with
                                                            31 is
yet another magic    statement that
                                                           
number to remember and for implementor must
                                                            the
implementor to         allow words of at
                                                           
enforce.                   least 31
                                                                                      
characters but is
                                                                                      
encouraged not to
                                                                                      
impose any
                                                                                      
specific
                                                                                      
limitation, and
                                                                                      
must document any
                                                                                      
such limitation.

 51      8.3.1.1.1         3)          Editorial            Term
'constant name? not   Add definition and
                                                            in
list of definitions     cross reference.

 52      8.3.1.1.1         5) (second  Technical           
Function pointers not      Allow function
                           group)                          
allowed                    pointers (which
                                                                                      
would have to have
                                                                                      
a prototype
                                                                                      
associated with
                                                                                      
them is they are
                                                                                      
to be used to
                                                                                      
invoke functions.
                                                                                      
This is needed eg
                                                                                      
to interface to C
                                                                                      
programs such as
                                                                                      
qsort, which
                                                                                      
require function
                                                                                      
pointers to be
                                                                                      
passed

 53      8.3.1.1.2         3rd         Technical            Names
including library    Add to last
                                                            names
must be disjoint.    paragraph, except
                                                           
However there is no need   for library-names.
                                                            and
it could be quite
                                                           
disruptive to force
                                                           
library names not to clash
                                                            with
other names.

 54      8.3.1.1.5         1st         Editorial           
'are?                      Should be 'is?

 55      8.3.1.2.1.2       1)          Technical            Limit
of 160 is yet        Remove limitation.
                                                           
another (different) magic  This should be
                                                           
number. Limitation should  covered under the
                                                            be
removed. (Also in       general maxim 'no
                                                           
8.3.1.2.3.2, 8.3.1.2.4.2)  hard coded limits
                                                                                      
if possible?, if
                                                                                      
not, document
                                                                                      
them. Have a
                                                                                      
minimum of 100
                                                                                      
bytes which
                                                                                      
vendors must
                                                                                      
support.

 56      Table of contents             Editorial            Table
of contents in the   Fix
                                                            pdf
version of the
                                                           
document is missing
                                                           
several chapters.

 57      8.3.1.2.1.3       N/a         Editorial            Not
clear from this        Add mention of
                                                           
description that case is   this fact. It is
                                                           
significant in             stated somewhere
                                                           
alphanumeric literals      else but should be
                                                           
though it is not           here also.
                                                           
significant elsewhere.

 58      8.3.2             1)          Editorial            Last
sentence appears to   Make the sentence
                                                            have
no effect but         less enigmatic.
                                                           
presumably is intended to
                                                            have
some effect

 59      8.3.2             All         Technical            The
requirements for       Remove the rule.
                                                           
spaces (eg period comma
                                                            and
semicolon must be
                                                           
followed by space, == must
                                                            be
preceded or followed by
                                                           
space) are often
                                                           
unnecessary and add
                                                           
complexity for programmer
                                                            and
implementor alike.

 60      8.4.1.1.2         5)          Technical            Why
allow duplicate names  Require warning in
                                                            as
long as they are not    case of duplicate
                                                           
referenced? This increases names. Same for
                                                            the
complexity of          data names and 88
                                                           
implementation and         levels.
                                                           
encourages bad programming
                                                           
practices and increases
                                                            the
risk that spelling
                                                           
mistakes will cause
                                                           
incorrect programs to be
                                                            run.

 61      13.16.36.1 (9),   See         Technical            Yet
another different        1. Encourage
         8.4.1.2.2(3)      previous                         magic
number (7 levels of       implementors
                           column                          
occurs is required).            to have no
                                                                                           
arbitrary
                                                                                           
limit
                                                                                        
2. Require at
                                                                                           
least 10
                                                                                           
levels - see
                                                                                           
(8) above;
                                                                                           
this limits
                                                                                           
the number of
                                                                                           
magic numbers
                                                                                           
to 2 easily
                                                                                           
remembered
                                                                                           
numbers- 10
                                                                                           
and 100.

 62      8.4.2.2.1         12a)        Editorial            This
rule should not be    Remove this
                                                            here
but should be covered paragraph.
                                                            by
the general rule for
                                                           
subscripting.

 63      8.4.2.7.2         2)          Technical            'is
not a universal object Another apparent
                                                           
reference?.                technical term
                                                                                      
which is not in
                                                                                      
the list of
                                                                                      
definitions. Add
                                                                                      
definition.

 64      8.4.2.11.2        3a)         Editorial            This
rule should not be    Remove this
                                                            here
but should be covered paragraph.
                                                            by
the general rule for
                                                           
subscripting.

 65      8.4.2.12          All         Technical            For
no obvious reason,     Add function
                                                           
function pointers are not  pointers to
                                                           
allowed. See comment 52.   allowed data
                                                            Rules
seem to exclude      types.
                                                           
program pointers from
                                                           
pointing at functions or
                                                            being
used to invoke them.

 66      8.4.5.1           All         Editorial            Local
Names. Technical     Add definition
                                                            term
is undefined

 67      8.4.5.1           All         Editorial           
Global names. Technical    Change definition
                                                            term
is in list of         so it is a
                                                           
definitions but the        definition not a
                                                           
definition only repeats    description of one
                                                           
paragraph 2 here which     attribute.
                                                            only
states one property
                                                            of
global names and does
                                                            not
define them.

 68      8.4.5.1.(1,2,3,4) All         Editorial           
Repetition of the same     Consolidate the
                                                            rule
for each type wastes  rule so that it is
                                                           
everyone?s time.           only stated once
                                                                                      
(ie for names of
                                                                                      
type X, Y, Z they
                                                                                      
are global if they
                                                                                      
contain the
                                                                                      
globa;l clause).

 69      4                 All         Editorial            Term
'phrase? is not       Add definition.
                                                           
defined

 70      8.4.5.6           1st         Editorial            It is
difficult to         Add a description
                                                           
determine the precise      of the external
                                                           
intended role of the       repository in
                                                           
external repository, even  section C.
                                                            in
the presence of s8.13.

 71      8.6.4             5th         Editorial           
'Lifecycle? technical term Add definition
                                                            is
not defined.

 72      8.8.1.1           Table 4     Technical            Rule
that you cannot have  Remove rule (ie
                                                           
successive unary negatives allow successive
                                                            seems
to be there for no   negatives (eg a -
                                                           
reason, makes the language - b).
                                                            more
complex and is yet
                                                           
another thing the
                                                           
implementer has to check

 73      8.8.1.1           7)          Editorial            Term
'composite? is used   Add definition and
                                                            but
not in list of         cross reference
                                                           
definitions.

 74      8.8.1.3.1.1       All         Technical            31/32
digits of precision  I do not have a
                                                            seems
very arbitrary, and  solution to this
                                                            will
execute very slowly   problem. Possibly
                                                            on
all known hardware.     allow vendors to
                                                                                      
provide a facility
                                                                                      
to allow users to
                                                                                      
specify a specific
                                                                                      
lower level or
                                                                                      
precision such as
                                                                                      
18 digits.

 75      8.8.1.3.6         1(1)        Editorial           
Existence of this blank    Remove
                                                           
paragraph is a typo.

 76      8.8.3.1           1st         Technical            Not
clear where these      Allow
                                                           
expressions are allowed.   concatenation
                                                                                      
expression
                                                                                      
anywhere an
                                                                                      
appropriate
                                                                                      
literal is
                                                                                      
allowed.

 77      8.8.3.2           2)          Technical           
Arbitrary limit of 160.    Remove limit.
                                                            Yet
another magic number.  Require vendors to
                                                                                      
support
                                                                                      
concatenated
                                                                                      
literals of at
                                                                                      
least 100, while
                                                                                      
encouraging 'no
                                                                                      
fixed limit?.

 78      8.8.4.1.3.3       4)          Technical           
Contradicts (1) and (2)    Add 'except in the
                                                                                      
context of (1) or
                                                                                      
(2)??

 79      8.8.4.3           2)          Technical            It is
not quite clear what Clarify.
                                                           
'necessary? means here.
                                                           
Presumably what is meant
                                                            here
is that in specific
                                                           
circumstances parts of a
                                                           
logical expression are not
                                                           
evaluated. I think I know
                                                            what
this means but that
                                                            is
not really quite what
                                                            is
needed. There are in
                                                            fact
various levels of
                                                           
sophistication in
                                                           
analysing logical
                                                           
expressions that allow
                                                           
differing degrees of
                                                           
omission of evaluations.

                                                            Eg

                                                            If
                                                           
(complicated-expression-1)
                                                            OR
not
                                                           
(complicated-expression-1)
                                                            XXX.

                                                           
Because we are evaluating
                                                            OR
expression and its
                                                           
inverse, the end result
                                                            must
be true. Therefore in
                                                            a
sense nothing needs to
                                                            be
evaluated (leaving
                                                            aside
the issue of zero
                                                           
length data items for the
                                                            sake
of simplicity).

 80      8.13              2nd last    Technical            It is
dangerous to allow   Do not require
                                                            users
to suppress warnings provision of a
                                                            about
differences between  mechanism to turn
                                                            the
repository and the     warnings off.
                                                           
source code.

 81      9.1.6             1st         Technical            This
seems to require      Clarify that these
                                                           
implementers to enforce    attributes 'may?
                                                            the
fact that certain      be fixed for the
                                                           
attributes of files cannot life of the file.
                                                           
change while the file
                                                           
exists. Why enforce this?

 82      12.2.4.2          1)          Technical           
Allowing specification of  Remove this
                                                           
source-computer without    paragraph.
                                                            any
details adds
                                                           
complexity for no obvious
                                                           
reason.

 83      12.2.6.2          12)         Editorial            'Thru
and through are      Replace by a rule
                                                           
equivalent? This is        added to section
                                                           
repeated many times        8.9 or some other
                                                           
throughout the document,   suitable place..
                                                            and
is always the case.

 84      12.2.7.1          Format 2    Technical           
Allowing omission of       Remove format 2.
                           (intrinsic)                     
FUNCTION for intrinsic
                                                           
functions, based on a
                                                           
directive earlier in the
                                                           
source file means changing
                                                            the
language?s syntax. To
                                                            me
this is a bad idea, and
                                                            only
seems to be justified
                                                            on
the basis of making
                                                            code
more concise - which
                                                            is
not an apparent design
                                                           
objective of the standard!

 85      12.2.7.3          12)         Technical           
Ability to 'shadow?        Remove ability to
                                                           
intrinsic function names   shadow intrinsic
                                                            makes
programs harder to   function names
                                                           
understand. Every time you with user defined
                                                            see a
reference to an      functions.
                                                           
intrinsic function you
                                                            would
need to check if it
                                                            is
shadowed.

 86      12.3.4.8.3        7)          Technical            Limit
on number of locks   Having a limit of
                                                            shall
be at least one.     one in
                                                                                      
meaningless. It
                                                                                      
would be better
                                                                                      
just to make this
                                                                                      
a software
                                                                                      
dependent feature.

 87      13.6              1st         Technical            Omits
to mention linkage   Add mention of
                                                            can
contain based items.   this fact

 88      13.14.2           22c)        Technical            There
is no obvious reason Remove rule.
                                                            for
this rule; it is
                                                           
another irregularity.

 89      13.16.1           All         Technical            The
layout of the bits in  Specify layout
                                                            the
bytes is not           within a byte or
                                                           
specified. Is this an      specify that it is
                                                           
omission or a deliberate   implementor
                                                           
intention to make this     defined.
                                                           
implementor defined?

 90      13.16.5           All         Technical            It
appears based items can Allow based
                                                            be in
working storage,     storage only in
                                                           
linkage, or local storage. working storage.
                                                            This
is very confusing as
                                                           
linkage and local storage
                                                           
conceptually are for
                                                           
parameters and data items
                                                           
allocate on program entry
                                                           
respectively, which
                                                           
conflicts with the based
                                                           
concept.

 91      13.16.5           All         Technical            It
would have been a good  Allow set address
                                                            ideas
to allow upward      on any item in
                                                           
compatibility with the     linkage, without
                                                           
existing code which allows BASED clause.
                                                            SET
ADDRESS of any linkage Consider removing
                                                            item,
without a based      BASED clause
                                                           
clause.                    entirely. Clarify
                                                                                      
that linkage can
                                                                                      
be for parameters
                                                                                      
or for items whose
                                                                                      
address is set
                                                                                      
with SET ADDRESS.

 92      13.16.9           All         General             
Making character based     Make screen
                                                           
screens a mandatory part   optional.
                                                            of
the language is 15
                                                            years
too late. In any
                                                            case,
because it is
                                                           
hardware/software
                                                           
dependent, the implementor
                                                            has a
loophole allowing
                                                            him
to avoid implementing
                                                            it.

 93      13.16.20          1st         Editorial            First
sentence is a        Replace with a
                                                           
pointless tautology.       sentence that has
                                                                                      
some meaning eg
                                                                                      
replace last word
                                                                                      
with "externally
                                                                                      
visible?.

 94      13.16.20.2        4)          Technical            There
is no reason why     Remove constraint
                                                           
pointer data items cannot
                                                            be
external

 95      13.16.20.3        3)          Technical            'name
of the file?         Specify it is the
                                                           
suggests it is the actual  name of the
                                                           
external file in the OS.   reference to the
                                                                                      
file that is
                                                                                      
visible to other
                                                                                      
programs.

 96      13.16.21.2        1)          Technical           
Restriction to unsigned    Remove
                                                            data
item is not needed.   restriction.
                                                           
Covered by general
                                                           
requirement that the data
                                                            item
be in range.

 97      13.16.22          All         Editorial           
Enigmatic if you have not  Provide cross
                                                            read
Appendix C.           reference to
                                                                                      
discussion in
                                                                                      
Appendix C. Same
                                                                                      
in 13.16.17

 98      13.16.22.3        2c3)        Editorial            This
seems to be repeated  Write the material
                                                            from
elsewhere.            on implicit PICs
                                                                                      
in one place and
                                                                                      
provide cross
                                                                                      
references.
                                                                                      
Otherwise one has
                                                                                      
to reread the
                                                                                      
whole thing in
                                                                                      
case there might
                                                                                      
be some slight
                                                                                      
changes.

 99      13.16.22.3        2c3e)       Technical            It is
not specified how    Clarify that the
                                                            the
usage varies depending first one that can
                                                            on
the magnitude.          hold the value is
                                                                                      
the one used, even
                                                                                      
if the precision
                                                                                      
is less than the
                                                                                      
precision of the
                                                                                      
value, Require a
                                                                                      
warning on lost
                                                                                      
precision.

 100     13.16.25          All         Technical           
Unclear which of the       Clairfy, or
                                                           
possibly many copies of a  preferably forbit
                                                            local
storage item in an   use of IS GLOBAL
                                                           
enclosing program would be for items in local
                                                           
accessed (top one, last    storage.
                                                            one
allocated?). It is
                                                            also
technically difficult
                                                            and
slow to find such
                                                            items
on the stack, and
                                                            may
be unreliable as well
                                                            in a
multi language
                                                           
environment.

 101     13.16.29          All         Editorial           
Enigmatic without having   Provide cross
                                                            read
Appendix C.           reference to
                                                                                      
relevant section
                                                                                      
in Appendix C.

 102     13.16.35          All         General             
Report is mandatory        Make report writer
                                                           
facility, but is far from  facility optional.
                                                            state
of the art (no
                                                           
fonts, images etc) and
                                                            often
not used.

 103     13.16.36.2        (1)         Technical           
Unnecessary limitations.   Remove
                                                                                      
limitations.
                                                                                      
Specify that where
                                                                                      
subordinate tables
                                                                                      
are less than
                                                                                      
maximum size,
                                                                                      
space is still
                                                                                      
there (ie later
                                                                                      
items do not slide
                                                                                      
up).

 104     13.16.36.2        16)         Technical            Why
is this an integer     No change required
                                                           
whereas other similar data here.
                                                            items
have to be unsigned?

 105     13.16.36.3        2)          Technical           
Requiring support for      Replace
                                                            2*max
means that the most  requirement by
                                                           
efficient form for index   requirement to
                                                           
(address) is not possible  support up to
                                                            in
most cases.             max+1 only.

 106     13.16.38.2        4)          Technical            PIC
size limit is 50.      Remove this
                                                           
Another magic number which paragraph.
                                                            is
not needed.

 107     13.16.40          All         General             
Object orientation is a    Make optional.
                                                           
mandatory feature. This is However only
                                                            too
large a jump for a     implementations
                                                           
language and comes at too  that implement it
                                                            high
a runtime and         should be allowed
                                                           
compilation cost for many  to call themselves
                                                           
applications. Eg garbage   'Object COBOL?.
                                                           
collection makes response
                                                            times
unpredictable and
                                                            the
only alternative to GC
                                                            is to
allow storage to
                                                            build
up indefinitely.

 108     13.16.42.2        1)          Technical           
Redefines must follow the  Remove.
                                                            entry
name clause.
                                                           
Unnecessary complication
                                                            for
programmer and
                                                           
implementor.

 109     13.16.42.2        7)          Editorial           
Uniqueness exists not      Change wording to
                                                           
because of the placement   reflect comment.
                                                            of
the clause but because
                                                            of
the fact that the only
                                                            thing
you can redefine is
                                                            the
prior entry at the
                                                            same
level.

 110     13.16.43.2        7)          Technical           
Redefined item may not be  Remove constraint.
                                                            usage
pointer. No need for
                                                            this
limitation.

 111     13.16.43.2        10)         Editorial            Use
of undefined term      Define 'left?
                                                           
'left?. We know what left  somewhere.
                                                            means
but what does it
                                                            mean
in this context?

 112     13.16.47.2        5) through  Technical            There
is no reason for     Remove.
                           7)                               these
restrictions.

 113     13.16.51.2        7)          Technical            Rule
is not needed.        Remove or make the
                                                           
Arithmetic expressions can same as table
                                                            be
distinguished as in     access expression
                                                            table
references (by       rule.
                                                           
exhaustion plus the rule
                                                            that
unary - is not allow
                                                            at
startt of next
                                                           
expression). Why have a
                                                           
different rule here?

 114     13.16.52.1        3)          Technical            Not
clear why you cannot   Change 'shall? to
                                                           
specify individually       'may? and change
                                                           
subscripted items. There   rules below to
                                                            may
be a reason but it is  reflect that if
                                                            not
clear.                 specified it
                                                                                      
refers to the
                                                                                      
individual item.

 115     13.16.55.2        4)          Technical           
Strongly typed items       Add extra
                                                           
should also not redefine   restriction.
                                                           
something else, in
                                                           
addition to the
                                                           
restriction here that they
                                                            not
be redefined?

 116     13.16.58.3        10)         Technical            As
packed decimal          As 'as though?
                                                           
implementation is          qualification.
                                                           
extremely slow on most
                                                           
platforms, allowance
                                                           
should be made to
                                                           
implement in a different
                                                            way,
provided the same
                                                           
results are achieved eg if
                                                            a
data item is not
                                                           
redefined, not accessed as
                                                            part
of a record, nor
                                                           
aliased in any other way,
                                                            it
need not be implemented
                                                            in
this way.

 117     13.16.60          1st         Editorial            'not
arises? is wrong.     Replace by 'does
                                                                                      
not arise?.

 118     13.16.61.2        12)         Technical            Why
is value spaces etc    Remove.
                                                            not
allowed.

 119     13.16.61.2        27a)        Technical           
Unnecessary restriction    Change to greater
                                                            that
upper value has to be than or equal.
                                                           
greater than lower value.
                                                            This
makes automatic
                                                           
generation of code more
                                                           
difficult.

 120     All               All         Editorial            Cross
References in the    Put quotes around
                                                           
document are hard to       cross references
                                                           
distinguish from           and add page
                                                           
surrounding text.          numbers eg see
                                                                                      
"Mumbo Jumbo" on
                                                                                      
in section 2.3.4
                                                                                      
on page 123.

 121     14.2              2)          Technical            Why
cannot alphanumeric    Remove
                                                            items
be by value.         restriction.
                                                                                      
Implementations
                                                                                      
can warn if too
                                                                                      
large.

 122     14.6.2            Heading     Technical            Term
'Imperative           Replace with more
                                                           
Statement" is confusing    exact term eg
                                                            and
misleading.            "imperative or
                                                                                      
terminated
                                                                                      
statement".

 123     14.7.5            1)          Technical           
Standard is over           Make it
                                                           
specifying the interaction implementor
                                                           
between non-COBOL and      defined whether a
                                                            COBOl
modules.             SET statement is
                                                                                      
needed to use a
                                                                                      
locale set outside
                                                                                      
COBOL. See also
                                                                                      
C13.2.1.2

 124     14.7.5            4)          Technical            It is
onerous to maintain  Make results of
                                                           
locale during a sort in    use changing
                                                            the
face of the user       locale during a
                                                           
changing it.               sort undefined.

 125     14.7.11.1         1)          Technical            It is
not clear what       Clarify.
                                                           
'corresponding class
                                                           
condition? is being
                                                           
referred to here.

 126     14.7.22.2.2       All         Editorial            I
found the section on     It may need to be
                                                           
exception handling too     clarified
                                                           
confusing to comment on
                                                           
although I have used
                                                           
exception handling in
                                                            other
languages.

 127     14.8.5            All         Technical            It
should be an error if   Make it is a
                                                           
nothing matches.           syntax error for
                                                                                      
nothing to match.

 128     14.8.6            2) last     Editorial           
'superposition? is not     Clarify.
                           paragraph                       
clearly defined.

 129     14.10.1.2         2)          Technical            Could
be associated with a Remove 'hardware?
                                                           
logical/software device    here and in
                                                            not
just a hardware        subsequent
                                                           
device.                    clauses.

 130     14.10.4.2         5a)         Technical            This
rule appears repeated Move rule
                                                            in
numerous other contexts elsewhere and
                                                            and
is not needed. Rule    refer to it. Move
                                                            for
rounding non-integral  rule should
                                                           
operands is not specified. include
                                                                                      
specification of
                                                                                      
how non integral
                                                                                      
operands are
                                                                                      
converted to
                                                                                      
integral table
                                                                                      
indexes.

 131     14.10.4.2         10          Technical            Same
rule repeated         Move to common
                                                           
elsewhere numerous times.  place and refer to
                                                           
Limitation that data item  common rule.
                                                            not
be a pointer is not    Remove constraint
                                                           
needed.                    about pointers.

 132     14.10.9.1         7b)         Technical            The
locking regime         Add 'or later? at
                                                           
envisioned by this rule is the end. Make the
                                                            non
consistent with many   exact time a lock
                                                           
systems which hold locks   is freed
                                                            until
the unit of work     implementation
                                                            ends.
There seems to be no dependent.
                                                            way
to specify end of work
                                                           
unit.                      It is too late for
                                                                                      
this but a verb to
                                                                                      
specify end of
                                                                                      
work unit should
                                                                                      
be available.

 133     14.10.13.3        4)          Technical           
Silently ignoring a        It should be an
                                                           
statement like EXIT        error condition to
                                                           
PROGRAM is very dangerous  EXIT PROGRAM in
                                                                                      
the main program.

 134     14.10.21.2        2)          Technical            There
is no reason to      Remove
                                                            limit
the receiving items  'elementary?.
                                                            to
elementary items. They
                                                            could
be group display
                                                           
items.

 135     14.10.27.2        7)          Technical            While
it may not make      Remove this rule.
                                                            sense
to have 0 in the by
                                                           
phrase, why have this
                                                            rule?
It will just require
                                                            the
compiler writer to
                                                            code
extra mostly useless
                                                           
checks.

 136     14.10.27.2        10)         Technical           
Another magic number.      Change as follows:

                                                                                        
1. Implementors
                                                                                           
are
                                                                                           
encouraged to
                                                                                           
have no
                                                                                           
arbitrary
                                                                                           
limits on the
                                                                                           
number of
                                                                                           
after
                                                                                           
phrases.
                                                                                        
2. If such a
                                                                                           
limit exists
                                                                                           
it must be
                                                                                           
documented
                                                                                           
and must be
                                                                                           
at least 10.

 137     14.10.29          All         Technical            There
seems to be no       Provide such a
                                                           
mechanism available for    mechanism on
                                                            the
programmer to find out similar lines to
                                                            the
length of the record   the IO status
                                                            which
has been read.       variable.

 138     10.14.30.2        2)          Technical            It
may be difficult for    Rule should be
                                                            the
implementor to check,  changed to say
                                                            as is
required for syntax  that results are
                                                           
errors, that record-name-1 undefined if the
                                                            and
identifier-1 do not    areas overlap.
                                                            share
the same storage
                                                            area
eg if identifier-1 is
                                                            in
linkage or is based.

 139     14.10.33.3        3)          Technical            Why
must the record be     Replace 'operating
                                                           
released to the operating  system? by input
                                                           
system at this time. It    output control
                                                            may
be better to buffer    system.
                                                            it.

 140     C.9               2nd         Editorial            There
are many bad         Remove paragraph.
                                                           
programming practices that
                                                            could
be warned about and
                                                            are
not; pointers can be
                                                            very
useful.

 141     C.10              The three   Editorial            COBOL
code and table are   Change spacing so
                           'Bit                             not
cleanly separated      the tables and
                          
Position?                                                   COBOL
code do not
                          
tables                                                     
overlap.

 142     C.12.2.3          1st         Editorial            Cross
references need a    Add spaces.
                                                            space
before them

 143     C17.2.1           Last code   Editorial            Badly
aligned code         Re align
                           fragment
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
