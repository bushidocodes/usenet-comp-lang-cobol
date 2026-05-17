[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Report on last ANSI X3J4 meeting

_1 message · 1 participant · 1996-02_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Report on last ANSI X3J4 meeting

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-02-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4gfq1i$akv@gazette.tandem.com>`

```
Report on February 12-17, 1995 ANSI X3J4 COBOL Committee meeting, La
Jolla, California, USA. When a vote is shown, the numbers are for,
against, and abstain (f-a-a).

The primary topic at this meeting was the CALL proposal. Also, there
were several important proposals under consideration and that passed.

The major topics/proposals we discussed were:

1. A web page for the X3J4 committee (about the standard, meeting
schedule, etc.) has been set up on http://www.mfltd.co.uk/Standards.
Another for validated compilers (COBOL and others) on
http://speckle.ncsl.nst.gov/vpl/intro.htm.

2. A proposal on allowing multiple characters for the currency sign
(like CURRENCY SIGN IS "fl" PICTURE SYMBOL "F" -- then you say PIC
FFFFF,99 and, assuming DECIMAL POINT IS COMMA, you get fl123,45 when
you move 123,45 to it) that was passed at the last meeting was
reviewed and approved and the proposal will be added to the base
document.

3. A proposal to define i-o for multi-octet characters (MOCS) was
discussed at length (it was rewritten after discussion at the last
meeting). It adds such things as a SELECT WHEN to figure out what
record description applies on a READ, a POSITION clause for reports
and screens that states in points where to position some text, a
CONVERT clause to state that data is to be converted on i-o, a WRITE
FROM literal, and so on. Note that this proposal works for non-MOCS
as well, as in converting EBCDIC to ASCII with embedded packed-
decimal and binary fields. The proposal was passed and will be added
to the base document.

4. A proposal to clarify multiple-octet characters and the report
writer was discussed. It mainly provides a function that returns the
number of columns (actually, bytes) required to print a MOCS
character.

5. A proposal that clarifies what happens when a literal (mainly a
MOCS one) used at compile time has a different value/collating
sequence at run time. For example, in THROUGH phrases. The proposal
was sent back for rewrite.

6. My proposal to define recovery points for exceptions. It allows
RECOVER in a declarative, USAGE RECOVERY, SET usage-item TO RECOVERY,
ON RECOVERY ... NOT ON RECOVERY ... END-SET. The proposal was
modified and passed. It will be revised and added to the base
document.

7. Some proposals on changing "casting" (like dynamic redefinition)
were discussed. The ideas were rejected. Casting remains as it is
now specified in the base document.

8. The third revision of my proposal on recursive programs was
discussed. The direction in the proposal was changed significantly.
Initial programs cannot be recursive and cannot have static data.
The default data for a method or recursive program is automatic
(initialized on every call), and STATIC can be used to specify static
data. A regular program can have automatic data (to save memory if
never called) by specifying AUTOMATIC. Some basic concepts were
changed and the proposal was sent back for rewrite.

9. The fourth revision of the proposal on CALL was discussed for
over a day. This adds prototypes, user-defined functions, passing
parameters by value, calling other languages easily, optional
parameters, arithmetic expressions as parameters, adds GOBACK, and
more. It was decided to not allow value parameters to be omitted (I
guess because C doesn't). Many more changes were suggested (none
were very substantive). The proposal was passed and will be added to
the base document. However, it will be reviewed again at the next
meeting and will probably result in some changes to the base document
that includes it.

10. A proposal to change ACCEPT ... FROM to return 4-digit years
(like in "ACCEPT frammis FROM DATE YYYYMMDD") was discussed,
modified, passed, and will be added to the base document.

11. A proposal to provide intrinsic functions to convert two-digit
year date formats to four-digit year date formats using a "window"
approach was discussed, modified, passed, and will be added to the
base document.

12. The Object-oriented ad hoc met and decided to remove
parameterized classes and interfaces (they are not well-specified or
well-understood). Once they are worked out, they will be added back,
possibly in an amendment. Most of the rest of their work involved
clarifications and editorial items. All of this will be added to the
base document.

13. My proposal on changing INITIALIZE to affect filler items (like
"INITIALIZE frammis WITH FILLER") was discussed, modified, passed,
and will be added to the base document.

14. The second iteration of the proposal on adding floating-point and
true binary data types was discussed. It was changed to use usages
of BINARY-SHORT, BINARY-CHAR, BINARY-LONG, etc. The optional words
SIGNED or UNSIGNED follow. Formerly it used LONG-SIGNED, LONG-
UNSIGNED, etc. For floating, SHORT-FLOAT and LONG-FLOAT are used.
Lots of changes were made and the proposal will be rewritten.

15. The second iteration of a paper on conditional compilation was
discussed. One defines constants with a CONSTANT directive (these
can be used anywhere in a program, not just in the EVALUATE and IF
directives) and uses EVALUATE and IF directives to delimit code. The
proposal was modified, passed, and will be added to the base
document.

16. My proposals to make continued COBOL words archaic and moves of
nonnumeric figurative constants to numeric items archaic were passed
and will be added to the base document.

17. A proposal to add two functions, HIGHEST-ALGEBRAIC and LOWEST-
ALGEBRAIC, to return the highest or lowest possible value for a data
item were discussed, modified, and will be added to the base
document.

18. A proposal on READ PRIOR and START < was discussed. It was
incomplete, so it was given to me for further development and
rewrite.

19. Lots of editorial papers were passed (about 8) and will be added
to the base document. Nothing very important was done in these.

The next X3J4 meeting will be in Islandia, New York, USA, on April
15-19 1996, with an editing ad hoc meeting on April 14. The main
topic will be critical proposals like recursive programs, pointers,
etc. The base document that results from this meeting is scheduled
to be the one used for the ISO CD (Committee Draft) review. This
means that no major new features can be added after the April meeting
unless required by the ISO review.
Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
