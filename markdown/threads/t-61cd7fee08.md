[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How COPY statement is handled by COBOL complier

_1 message · 1 participant · 1999-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: How COPY statement is handled by COBOL complier

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84gt14$6c3$1@nntp9.atl.mindspring.net>`

```
James wrote (to me outside the NG),

"Actually, you're quite incorrect.  Please read the included portoin of the
current Standard: ..." (see below for the rest of his comments)

UNFORTUNATELY, James, you are thinking that the "COMMITTEE DRAFT" is the
"current Standard".  It isn't - and whether or not it ever becomes one - is a
matter of question.  HOWEVER, let me address your errors on two accounts:

1) For the current ('85 Standard - amended by the '89 and '91 Ammendments)
Standard.  As Tim Josling pointed out an interpretation request was made and
it was EXPLICITLY stated that such statements (COPY and REPLACE) and each
part of them MAY be continued across lines.  If you don't have access to the
published CIB's (COBOL Information Bulletines) then I suggest you contact
ANSI to find out how to get them.  (I can provide you online options to do
this if you are interested.)

Concerning your issue about rules that impact the "contiguous characters
COPY", I think you need to check out page IV-42 of the current ANSI Standard
which EXPLICITLY states that when a "-" appears in the indicator area then
the data in the continued and continuation line are treated as if they are
concatenated - with no intervening space.  (Not the exact words from the
Standard - but what they mean).

2) For CD1.7 (the most current - but still undergoing changes draft of the
next Standard), you are missing a few bits that still make this code valid.

Please see
  6 Reference format (page 36 and following) which states (among other
things),
    "a) A COBOL compiler shall process fixed-form reference format lines as
though the lines had been logically converted from fixed form to free form.
(See 6.4, Logical conversion.)"
       and then (in 6.4)
   "Source text and library text in fixed-form reference format are logically
converted to free-form reference format before the application of replacing
and conditional compilation actions. ... fixed continuation indicator: ..."
(and lots of details on how continuation lines are handled - and the fact
that they include both words and literals.

But probably the most important thing for you to read is both
    6.2.4 Continuation of lines
       and
    6.3.1 Continuation of lines

which explicitly state,

"A COBOL word, literal, or picture character-string may be broken such that
part of it appears on a subsequent line. The subsequent lines are
continuation lines; the line preceding the continuation line is a continued
line."

Note about "levels" in the '85 Standard.  It is true that there are separate
levels of the Standard (both ANSI and FIPS - and they are not identical).
However, there are also rules (in both ANSI and FIPS) that REQUIRE you to
support a feature from a "higher level" in a Standard conforming manner - if
you support it at all.  I think that you will find that VS COBOL II (R4.0)
which is ANSI HIGH level but only FIPS INTERMEDIATE (because it doesn't
support Intrinsic Functions - which is required in FIPS but optional in ANSI)
most certainly DOES support continuation in COPY statements - at any of the
places that I indicate.  (Needless to say, it doesn't even come close to
matching CD 1.7 - even the newer IBM product such as IBM COBOL for OS/390 &
VM - don't claim to do that.)

   ***

James,
  Have you actually tried this with any CONFORMING '85 Standard compiler
(especially one that has passed the FIPS certification tests)?  I think  you
find that they all really DO support this today (and many applications rely
on this feature - although not to the extreme of my example).

Should you have any further questions on where the explicit documentation is
on this in either the current Standard or the draft, please feel free to post
it to the newsgroup.

 **********************************

(Rest of James' private email follows)


!!!!!!!!!!!!!!!!!!!!
7.1.1.1 Compiler directing statements and sentences
The compiler directing statements are the COPY statement and the REPLACE
statement. A compiler directing sentence is a compiler directing statement
terminated by a separator period.
7.1.1.2 Source text and library text
Source text is the primary input to the compiler for a single compilation
group. Library text is secondary input to the compiler as a result of
processing a COPY statement.
The source text and library text processed by text manipulation consists of
indicators, character-strings, comments, and separators. A character-string
is either a text-word or the word 'COPY'.
7.1.1.3 Pseudo-text
Pseudo-text is an operand in the REPLACE statement and in the REPLACING
phrase of the COPY statement. Pseudo-text may be any sequence of zero or
more text-words, comments, and the separator space bounded by, but not
including, pseudo-text delimiters.

ISO/IEC CD 1.7 1989 : yyyy(E)
Text manipulation elements
The opening pseudo-text delimiter and the closing pseudo-text delimiter
consist of the two contiguous COBOL characters '=='.
7.1.1.4 Text-words
A text-word is a character-string in source text or in library text that
constitutes an element processed by text
manipulation. A text-word may be one of the following:
1) a separator, except for: a space; a pseudo-text delimiter; and the
opening and closing delimiters for
alphanumeric, boolean, and national literals. In determining which character
sequences form text-words, the
right parenthesis and left parenthesis characters, regardless ofcontext
within source text or library text, are
treated as separators;
2) an alphanumeric, boolean, or national literal including the opening and
closing delimiters that bound the
literal;
3) any other sequence of contiguous COBOL characters bounded by separators,
except for: comments and the word 'COPY'.
!!!!!!!!!!!!!!!!!!!!  NOTICE 'the word "COPY"' AND the references to
CONTIGUOUS CHARACTERS

    I'll grant you that since psuedo-text-1/2 can be
"13) The length of a text-word within pseudo-text and within library text
shall be from 1 through 322 character
positions.", AND, "10) Character-strings within pseudo-text-1 and
pseudo-text-2 may be continued in accordance with the rules of reference
format."  that PSUEDO-TEXT-1/2 can be continued,
but I respectfully demand proof that the REQUIRED COMPILER DIRECTIVES [COPY,
REPLACE]
can be split.
You can split == == ONLY by

COL12345678
                        COPY mybook  Replacing  =="ABC
                       -            def"==    by a-COBOL- word .

In other words, since the COPY/COPY REPLACING is a LOGICAL replacement and
is
evaluated after the replacing (along with the rest of the source), you must
meet the COBOL
Language Requirements


12) Word-1 or word-2 may be any single COBOL word except 'COPY', the
compiler directive initiator, the floating debug indicator, or the comment
indicator.

ALSO, there are VARYING LEVELS of Conformance as there are VARYING Levels of
SUPPORTED LANGUAGE ELEMENTS:
FRONT_2.7 Industry Standards Used

VS COBOL II supports the following industry standards in the MVS, VM, and
VSE environments, as understood and interpreted by IBM as of September
1989:

1.  ISO 1989:1985, Programming Languages--COBOL.

    ISO 1989:1985 is identical to X3.23-1985, American National Standard
    for Information Systems--Programming Language--COBOL.

    For supported modules, see 2 below.

2.  X3.23-1985, American National Standard for Information
    Systems--Programming Language--COBOL.

    Under MVS and VM, VS COBOL II supports all required modules at the
    highest level defined by the standard.

    Under VSE, VS COBOL II supports all required modules at the
    intermediate level.  It also supports all required modules at the high
    level with the exception of the following language features:

       EXTEND phrase of the OPEN statement (However, OPEN EXTEND for VSAM
        sequential files is supported.)
       REVERSED phrase of the OPEN statement
       OF/IN phrase of the COPY statement.

    In the following list, the shorthand notation describing module levels
    is shown in parentheses.  For example, to summarize module information
    for sequential input/output, the shorthand notation is (2 SEQ 1,2).
    The first digit indicates the level of language elements within the
    module supported by VS COBOL II. Next is the three-character
    abbreviation of the module name as used in the standard.  Finally, the
    two digits separated by a comma indicate the minimum and maximum
    levels of the module.  For example, (2 SEQ 1,2) means that VS COBOL II
    supports the sequential I-O module at level 2, while the range of
    levels in the module is from 1 (minimum) to 2 (maximum).

       Nucleus (2 NUC 1,2)

        Provides internal processing of data within the four basic
        divisions of a program and the capability for defining and
        accessing tables.

       Sequential I-O (2 SEQ 1,2)

        Provides access to records of a file in established sequence.  The
        sequence is established as a result of writing the records to the
        file.

       Relative I-O (2 REL 0,2)

        Provides access to records in either a random or sequential
        manner.  Each record is uniquely identified by an integer
        specifying the record's logical position in a file.

       Indexed I-O (2 INX 0,2)

        Provides access to records in either a random or sequential
        manner.  Each record in an indexed file is uniquely identified by
        the value of a key within that record.

       Sort-Merge (1 SRT 0,1)

        Orders one or more files of records, or combines two or more
        identically ordered files of records, according to a set of
        user-specified keys.

       Inter-Program Communication (2 IPC 1,2)

        Allows a COBOL program to communicate with other programs through
        transfers of control and access to common data items.

       Source Text Manipulation (2 STM 0,2)

        Allows the insertion of source program text as part of the
        compilation of the source program.  COBOL libraries contain texts
        which are available to the compiler at compile time and which can
        be treated by the compiler as part of the source program.

    In addition, the following levels of optional modules are supported:

       Debug (1 DEB 0,2)

        Monitors object program execution through declarative procedures,
        special debugging lines, and a special register, DEBUG-ITEM, which
        gives specific information about execution status.

       Segmentation (2 SEG 0,2)

        Refreshes independent segments when required.

    The following optional modules of the standard are not supported:

       Report Writer
       Communications
       Debug (2 DEB 0,2)
       Intrinsic Functions


3.  FIPS Publication 21-3, Federal Information Processing Standard 21-3,
    COBOL.  VS COBOL II supports the FIPS intermediate subset, and the
    FIPS high subset except for the Intrinsic Functions module.

4.  International Reference Version of the ISO 7-bit code defined in
    International Standard 646, 7-Bit Coded Character Set for Information
    Processing Interchange.

5.  The 7-bit coded character sets defined in American National Standard
    X3.4-1977, Code for Information Interchange.

The COBOL language is developed by the Conference On DAta SYstems
Languages (CODASYL).


Aloha


----- Original Message -----
From: William M. Klein <wmklein@ix.netcom.com>
To: <mangogwr@bellsouth.net>
Sent: Wednesday, December 29, 1999 9:35 PM
Subject: Re: How COPY statement is handled by COBOL complier


> James King <mangogwr@bellsouth.net> wrote in message
> news:Lxxa4.320$zp.4764@news3.mia...
…[4 more quoted lines elided]…
> Sorry, this is another incorrect statement.  The following is perfectly
valid
> in any ANSI'85 conforming compiler:
>
…[8 more quoted lines elided]…
> Now, I am *NOT* recommending anyone to code ANY source statement like
that -
> but the (existing) Standard requires that a conforming implementation MUST
> support such code.
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
