[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Order of evaluating EVALUATE (wasRe: Sample "solutions" to the "Right Justify" Question(s)

_2 messages · 2 participants · 1999-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Order of evaluating EVALUATE (wasRe: Sample "solutions" to the "Right Justify" Question(s)

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7s0c4m$rve@lotho.delphi.com>`
- **References:** `<7rnb8v$l32@dfw-ixnews9.ix.netcom.com> <CnMD3.1757$eJ2.18573@news1.mia> <37dfa498@news3.prserv.net> <QnSD3.2465$eJ2.25322@news1.mia> <37e03c3a@news3.prserv.net> <37e03e80@news3.prserv.net> <7rq246$1em$11@ssauraab-i-1.production.compuserve.com> <37e0e12d@news3.prserv.net> <37E0EF39.D8012591@zip.com.au> <37e18a86@news3.prserv.net> <7rsss3$kj0$2@ssauraac-i-1.production.compuserve.com> <7ru7t7$4m2@dfw-ixnews17.ix.netcom.com> <7rvbsd$avk@dfw-ixnews7.ix.netcom.com>`

```
OK - I'm cornfused here. Is (27) below the NEW rule or the OLD rule? 
Tell me it is the new rule, which would make sense. (It is a leadin 
to enumerated data types.) 

it is also the way most current EVALUATEs work. :) 

-Paul

William M. Klein (wmklein@nospam.netcom.com) wrote:
: OK,
:   I knew that I had seen this topic at J4.  I just found the following
: listed as a "Substantive changes potentially affecting existing programs" in
: CD 1.6 (the latest draft of the next Standard),

: "27) EVALUATE statement, sequence of execution. The sequence of evaluation
: of selection subjects and objects is now defined to be from left to right
: and selection objects are evaluated as each WHEN phrase is processed. When a
: WHEN phrase is selected, no more selection objects are evaluated.

: Justification:
: The previous COBOL standard did not define the sequence of evaluation of
: selection subjects and selection objects in an EVALUATE statement. It was as
: if they were evaluated all at once or in some undefined order. Also, the
: rules indicated that all selection objects were evaluated even if an earlier
: WHEN phrase was selected. The only place where the new rules would cause a
: difference is when a RANDOM function is specified in one of the selection
: objects that is no longer evaluated. In addition, some subscript bounds
: conditions or other errors might not occur with the current specifications.

: Because the new rules state that all selection subjects are evaluated at the
: start of execution of the EVALUATE statement, some subscript bounds
: conditions or other errors could occur during this evaluation that might not
: have occurred before.

: This change was made as a result of a request for an interpretation of the
: previous COBOL standard. It is believed that few, if any, programs will be
: affected by this change."

: --
: Bill Klein
:     wmklein <at> ix dot netcom dot com
```

#### ↳ Re: Order of evaluating EVALUATE (wasRe: Sample "solutions" to the "Right Justify" Question(s)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7s0lcm$j04@dfw-ixnews12.ix.netcom.com>`
- **References:** `<7rnb8v$l32@dfw-ixnews9.ix.netcom.com> <CnMD3.1757$eJ2.18573@news1.mia> <37dfa498@news3.prserv.net> <QnSD3.2465$eJ2.25322@news1.mia> <37e03c3a@news3.prserv.net> <37e03e80@news3.prserv.net> <7rq246$1em$11@ssauraab-i-1.production.compuserve.com> <37e0e12d@news3.prserv.net> <37E0EF39.D8012591@zip.com.au> <37e18a86@news3.prserv.net> <7rsss3$kj0$2@ssauraac-i-1.production.compuserve.com> <7ru7t7$4m2@dfw-ixnews17.ix.netcom.com> <7rvbsd$avk@dfw-ixnews7.ix.netcom.com> <7s0c4m$rve@lotho.delphi.com>`

```
paulr <paulr@bix.com> wrote in message news:7s0c4m$rve@lotho.delphi.com...
> OK - I'm cornfused here. Is (27) below the NEW rule or the OLD rule?
> Tell me it is the new rule, which would make sense. (It is a leadin
…[5 more quoted lines elided]…
>

Sorry for the confusion.

It is the NEW (with the NEXT Standard) rule - with a "warning" that it
*MIGHT* impact some existing programs that followed the "letter of the law"
in the '85 Standard.

As others have pointed out, it is questionable that ANY existing
implementations actually do follow the '85 Standard rule.  Furthermore, if
you have such an implementation, then I think that you the user/customer
probably should contact the vendor and "request" that they provide you some
(currently NON-Standard - but soon to be STANDARD) option that works the
"new" way.

A way to test if your compiler works the "letter of the law" way (for Micro
Focus - for example) would be to run with +F (to get 163 run-time errors)
and have the following code:

01  Num-Fields.
   05   NF1  Pic 9.
   05   NF2  Pic 9.

    ....
move 3 to NF1
Move Spaces to Num-Fields (2:1)
Evaluate NF1
    When 3
       Display "Does not follow the 'letter of the law'"
    When NF2
       Display "You should get a 163 before getting here"
End-Evaluate
GoBack
..

If your program does the 1st Display and then ends successfully, your
compiler follows the NEW (not yet Standard) rule; if it gets a 163, then it
follows the strict '85 Standard rule.

One more example of how to test this (on an IBM mainframe compiler)

Set SSRANGE on (compile and run-time) and compile and run the following:

01  Num-Fields.
   05   NF1  Pic 9.
   05   Tabl occurs 3 times.
         10 Elem  Pic 9.
    ....
move 3 to NF1
Move Zero to Elem (3)
Evaluate NF1
    When 3
       Display "Does not follow the 'letter of the law'"
    When Elem (NF1 + 1)
       Display "You should get an SSRANGE error before getting here"
End-Evaluate
GoBack
..

If you get an SSRANGE error when you run the program, then IBM is following
the "letter of the law" - if not they are following the new rule.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
