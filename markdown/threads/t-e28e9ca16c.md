[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question for CICS gurus -- CICS CALL statements

_2 messages · 2 participants · 1998-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Question for CICS gurus -- CICS CALL statements

- **From:** "Your Name" <PatronID@glaxowellcome.com>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<01bda8fd$e6656980$c58c3398@us0071826>`
- **References:** `<359AC0B4.F0A9B825@earthlink.com>`

```

I have a similar problem once. It has something to do with how CICS/COBOL
II pass
its working storage address to the called program. COBOL II/CICS programs
cannot call
on OS/VS Cobol programs. Cobol II being "above the 16MB line". Check if
your batch 
COBOL program if it is COBOL II or not.

Aedehl

SM <manjigani@earthlink.com> wrote in article
<359AC0B4.F0A9B825@earthlink.com>...
> Hi,
> 
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Question for CICS gurus -- CICS CALL statements

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<01bda90c$4fbcb1f0$c58c3398@us0071826>`
- **References:** `<359AC0B4.F0A9B825@earthlink.com> <01bda8fd$e6656980$c58c3398@us0071826>`

```

hope these pages from the IBM manuals help you find your answer. That is if
your called batch program is OS/VS Cobol.... being called from COBOL
II/CICS.
that was the situation I was in on a previous project, and what we did is
compiled
the program under COBOL II and use that object on our CICS/COBOL II
programs.

from the IBM Manuals: Programming Guide

In addition to making calls between COBOL for MVS & VM programs, you can
also
make static and dynamic calls between COBOL for MVS & VM and VS COBOL II
programs and, in a non-CICS environment, between COBOL for MVS & VM and
OS/VS COBOL programs. In a CICS environment, you must use EXEC CICS LINK
to transfer control between COBOL for MVS & VM and OS/VS COBOL programs.

When to Use a Dynamic Call
Use a dynamic call statement when any of the following are true:
o  You are concerned about ease of maintenance. Applications do not have to
be
    link-edited again when dynamically called subprograms are changed.

o  The subprograms called are used infrequently or are very large.
    If the subprograms are called on only a few conditions, dynamic calls
can bring
    in the subprogram only when needed.
    If the subprograms are very large or there are many of them, using
static calls 
    might require too much main storage. Less total storage might be
required to
    call and cancel one, then call and cancel another, than to statically
call both.

o  You want to call subprograms in their unused state, and you cannot use
the
    INITIAL attribute.

    When you cannot use the INITIAL attribute to ensure that a subprogram
is
    placed in its unused state each time it is called, you can set the
unused state
    by using the CALL and CANCEL procedure that is described next. (This is
a
    more cumbersome and inefficient procedure, but does provide control of
the
    state, if that is essential).

    For this procedure, use a combination of dynamic CALL and CANCEL
state-ments.
    When you CANCEL the subprogram that was first called by an OS/VS
    COBOL, VS COBOL II or COBOL for MVS & VM program, the next CALL will
    cause the subprogram to be reinitialized to its unused state.

    Using the CANCEL statement to explicitly cancel a subprogram that was
    dynamically loaded and branched to by a non-COBOL program does not
result
    in any action being taken to release the subprogram's storage or to
delete the
    subprogram.

o  You have an OS/VS COBOL or other AMODE(24) program in the same run
    unit with COBOL for MVS & VM programs that you want to run in 31-bit
    addressing mode. OS/VS COBOL, VS COBOL II, and COBOL for MVS & VM
    dynamic CALL processing include AMODE switching for AMODE(24) programs
    calling AMODE(31) programs, and vice versa. To have this implicit AMODE
    switching done, you must use the Language Environment run-time option,
    ALL31(OFF). AMODE switching is not performed when ALL31(ON) is set. For
    details on the ALL31 run-time option, see  Language Environment
Programming
    Reference.

    When AMODE switching is performed, control is passed from the caller to
a
    Language Environment library routine. After the switching is performed,
control
    is passed to the called program, and the library routine's save area
will be posi-tioned 
    between the caller program's save area and called program's save area.

o  The program name to be called is not known until run time.
         � Here, use the format CALL  identifier, where the  identifier is
a data item that
            will contain the name of the called program at run time. In
terms of prac-tical 
           application, you might use CALL  identifier when the program to
be
           called is variable, depending on conditional processing in your
program.
         � CALL  identifier is always dynamic, even if you use the NODYNAM
compiler
            option.

Calls under CICS
If your COBOL program runs under CICS, observe these CALL restrictions and
requirements:
o   You can make calls to and from VS COBOL II and/or COBOL for MVS & VM
     programs.
o   Assembler-language programs that conform to the interface described in
the
     Language Environment Programming Guide are called LE-conforming
assem-bler 
     programs. Ones that do not conform to the interface can be called
     non-LE-conforming assembler programs.

    A COBOL for MVS & VM program can call a non-LE-conforming
assembler-language 
    program. However, a non-LE-conforming assembler program cannot
    call a COBOL for MVS & VM or a VS COBOL II program.

o  Calls to LE-conforming assembler programs are supported. Calls from
    LE-conforming assembler programs are supported with the restriction
that the
    assembler-language program is not a main program.

o  The NODYNAM compiler option must be used if the COBOL program has been
    translated by the CICS translator.

o  CALL  identifier can be used with the NODYNAM compiler option to
dynamically
    call a program. Called programs can contain any function supported by
CICS
    for the language. Dynamically called programs have to be defined in the
CICS
    program processing table (PPT).

o  If you are calling a COBOL program that has been translated, you must
pass
    DFHEIBLK and DFHCOMMAREA as the first two parameters in the CALL
    statement.

****************************************************************************
***********
o  COBOL for MVS & VM and VS COBOL II programs cannot call or be called by
    OS/VS COBOL programs. EXEC CICS LINK must be used instead.
****************************************************************************
***********

o  Support for interlanguage communication (ILC) with other HLL languages
is
    available. For more detailed information on ILC, see  Language
Environment
    Programming Guide. Where ILC is not supported, you can use CICS LINK,
    XCTL, and RETURN instead.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
