[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform thru question.

_8 messages · 6 participants · 1999-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Perform thru question.

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38298C7E.4B8E0723@NOSPAMhome.com>`

```
I have a program which I need to maintain and move from an earlier ANSI
to COBOL for MVS.

It has the following logic:

-  -  -  -  -  -  -  -  -  -  -  -  -   167 Line(s) not Displayed
     SORT SORTWK ON ASCENDING KEY SORT-ACCT
         INPUT PROCEDURE BUILD-ACCT-TBL THRU END-BLD-ACCTS
         OUTPUT PROCEDURE SELECT-NMONTH THRU END-NMONTH-SELECT.
*
     STOP RUN.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  2 Line(s) not Displayed
 BUILD-ACCT-TBL SECTION.
-  -  -  -  -  -  -  -  -  -  -  -  -  - 14 Line(s) not Displayed
 BLD-ACCTS-10.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  4 Line(s) not Displayed
 BLD-ACCTS-10-CONTN.
-  -  -  -  -  -  -  -  -  -  -  -  -  - 15 Line(s) not Displayed
 BLD-ACCTS-20.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  7 Line(s) not Displayed
 BLD-ACCTS-30.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  3 Line(s) not Displayed
 END-BLD-ACCTS.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  2 Line(s) not Displayed
 READ-SUBCD.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  3 Line(s) not Displayed
 END-SUBCD-RD.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  3 Line(s) not Displayed
 SELECT-NMONTH SECTION.

It's been running for years, and looking at the code, it would have
aborted if it performed the last two paragraphs after it performed
END-BLD-ACCTS.

But I don't know if I can trust it to behave that way with any
compiler.   

What should happen with this ugly code?
```

#### ↳ Re: Perform thru question.

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<urqW3.2171$uk.18958@news3.mia>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com>`

```
Well, it is a valid SORT statement:

This phrase specifies the name of a procedure that is to select or modify
input records before the sorting
operation begins.

procedure-name-1
    Specifies the first (or only) section or paragraph in the INPUT
PROCEDURE.

procedure-name-2
    Identifies the last section or paragraph of the INPUT PROCEDURE.

    The input procedure can consist of any procedure needed to select,
modify, or copy the records that are
    made available one at a time by the RELEASE statement to the file
referenced by file-name-1.  The range
    includes all statements that are executed as the result of a transfer of
control by CALL, EXIT, GO TO, and
    PERFORM statements in the range of the input procedure, as well as all
statements in declarative
    procedures that are executed as a result of the execution of statements
in the range of the input
    procedure.  The range of the input procedure must not cause the
execution of any MERGE, RETURN, or
    SORT statement.

    If an input procedure is specified, control is passed to the input
procedure before the file referenced by
    file-name-1 is sequenced by the SORT statement.  The compiler inserts a
return mechanism at the end of
    the last statement in the input procedure. When control passes the last
statement in the input procedure,
    the records that have been released to the file referenced by
file-name-1 are sorted.

Howard Brazee wrote in message <38298C7E.4B8E0723@NOSPAMhome.com>...
>I have a program which I need to maintain and move from an earlier ANSI
>to COBOL for MVS.
…[35 more quoted lines elided]…
>What should happen with this ugly code?
```

#### ↳ Re: Perform thru question.

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1nW3.327$%3.8901@typhoon01.swbell.net>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com>`

```
I must be missing something. After the program executes
the 2 lines in the END-BLD-ACCTS paragraph, it then
executes the first statement in the SELECT-NMONTH section.
The statements in the READ-SUBCD are not executed
at all.


> -  -  -  -  -  -  -  -  -  -  -  -  -   167 Line(s) not Displayed
>      SORT SORTWK ON ASCENDING KEY SORT-ACCT
…[30 more quoted lines elided]…
> What should happen with this ugly code?
```

##### ↳ ↳ Re: Perform thru question.

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80d4sl$go6$1@nntp1.atl.mindspring.net>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com> <j1nW3.327$%3.8901@typhoon01.swbell.net>`

```
Looks that way - problem seems to start with a perform range starting with a
section
and ending without a para. Seems to confuse the whole issue. But I can say
for sure that
a different compiler would react differently you have clearly defined start
& end tags.

The risk is that someone (like me) would go in & add a conditional
GO TO BUILD-ACCT-TBL-EXIT & add the para at the end of the section. This
then puts
you outside the input procedure range.

If you're in a mainframe environment, wouldn't it be better to split into 2
pgms, and add
something like a SORT between the 2 pgms?

Jerry P <bismail@bisusa.com> wrote in message
news:j1nW3.327$%3.8901@typhoon01.swbell.net...
> I must be missing something. After the program executes
> the 2 lines in the END-BLD-ACCTS paragraph, it then
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform thru question.

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382ADB8B.E19DC0D7@NOSPAMhome.com>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com> <j1nW3.327$%3.8901@typhoon01.swbell.net> <80d4sl$go6$1@nntp1.atl.mindspring.net>`

```
Unbeliever wrote:
> 
> Looks that way - problem seems to start with a perform range starting with a
…[13 more quoted lines elided]…
> something like a SORT between the 2 pgms?

If it was my own program, I would make every effort to have an external
sort.  And if it was my own program, I would not perform sections, nor
perform THRU.  But since I am doing maintenance on an existing program,
my mandate is to avoid restructuring the job and program except where
necessary.  The temptation to re-write is great though.
```

###### ↳ ↳ ↳ Re: Perform thru question.

_(reply depth: 4)_

- **From:** AnhMy Tran <anhmytran@hotmail.com>
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s2p58dbmhsq66@corp.supernews.com>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com> <j1nW3.327$%3.8901@typhoon01.swbell.net> <80d4sl$go6$1@nntp1.atl.mindspring.net> <382ADB8B.E19DC0D7@NOSPAMhome.com>`

```
You are right.

When I first work with COBOL, the temptation to rewright (redesign) is 
great.
But there is nothing wrong with the code. If you do not like it, there is 
only one way to go. It is the old style. That's all.
```

###### ↳ ↳ ↳ Re: Perform thru question.

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80km9d$ai9$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com> <j1nW3.327$%3.8901@typhoon01.swbell.net> <80d4sl$go6$1@nntp1.atl.mindspring.net>`

```
Bottom line - determine what it really does, for sure in proper environment,
then rewrite to "standard" specs.  Document.



Unbeliever <popsider@ix.netcom.com> wrote in message
news:80d4sl$go6$1@nntp1.atl.mindspring.net...
> Looks that way - problem seems to start with a perform range starting with
a
> section
> and ending without a para. Seems to confuse the whole issue. But I can say
> for sure that
> a different compiler would react differently you have clearly defined
start
> & end tags.
<SNIP>
```

##### ↳ ↳ Re: Perform thru question.

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382ADAD0.B5E187CB@NOSPAMhome.com>`
- **References:** `<38298C7E.4B8E0723@NOSPAMhome.com> <j1nW3.327$%3.8901@typhoon01.swbell.net>`

```
That is what happens (well, the READ-SUBCD is performed), but I want to
know if I can trust that to happen with new compilers.  I would NEVER
code it this way, and have never seen anybody else have the end of the
perform thru inside of the section being performed.

Jerry P wrote:
> 
> I must be missing something. After the program executes
…[37 more quoted lines elided]…
> > What should happen with this ugly code?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
