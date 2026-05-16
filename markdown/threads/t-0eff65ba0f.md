[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Evaluate Question

_4 messages · 4 participants · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Evaluate Question

- **From:** "Martin Ruston" <martin@nisie-1.demon.co.uk>
- **Date:** 1999-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<921782408.3125.0.nnrp-07.c1ed7479@news.demon.co.uk>`

```
Hello,

I`m new to programming and have been studying Cobol for the last few months now,
I am currently working on a problem which requires a table recording the number
of passes, fails, etc, for an exam to be filled.

I`ve used the following piece of code to evaluate the results, repeated for
paper-2 and paper-3;

EVALUATE PAPER-1
    WHEN 0 THRU 39
        ADD 1 TO W-RESULT-TABLE (1, FAIL)
    WHEN 40 THRU 49
        ADD 1 TO W-RESULT-TABLE (1, PASS)
    WHEN 50 THRU 69
        ADD 1 TO W-RESULT-TABLE (1, CREDIT)
    WHEN 70 THRU 100
        ADD 1 TO W-RESULT-TABLE (1, DISTINCTION)
END-EVALUATE

EVALUATE PAPER-2
    WHEN 0 THRU 39
        ADD 1 TO W-RESULT-TABLE (2, FAIL)
    WHEN 40 THRU 49

etc.

Although this is a simple solution, it does not seem a very elegant one.  Would
it be possible to evaluate each of the three exam papers and fill the relevant
sections of the table from the one EVALUATE statement, and if so how?

The file holding the exam results is as follows;

FD    RESULTS-FILE.
01     RESULTS-REC.
         03 CAND-NO
         03 S-NAME
         03 RESULTS
              05 PAPER-1
              05 PAPER-2
              05 PAPER-3

I hope this problem is not to trivial for everyone, and that some of you can be
of some help.

thanks in advance

Martin.
```

#### ↳ Re: Evaluate Question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-jbBicDRi1E8v@Dwight_Miller.iix.com>`
- **References:** `<921782408.3125.0.nnrp-07.c1ed7479@news.demon.co.uk>`

```
On Thu, 18 Mar 1999 18:40:07, "Martin Ruston" 
<martin@nisie-1.demon.co.uk> wrote:

> Hello,
> 
> I`m new to programming and have been studying Cobol for the last few months now,
> I am currently working on a problem which requires a table recording the number
> of passes, fails, etc, for an exam to be filled.

Three possible methods:

EVALUATE TRUE 
------
EVALUATE Paper-1 Also Paper-2 Also Paper-3
------
Make Paper-1, 2 and 3 a table and then use one Evaluate 3 times.
```

##### ↳ ↳ Re: Evaluate Question

- **From:** edwardw355@aol.com (EdwardW355)
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990319023332.03192.00000346@ng20.aol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-jbBicDRi1E8v@Dwight_Miller.iix.com>`

```
Put the papers in an indexed table, then put the evaluate in a perform loop.

01  grades.
    03  grade
        occurs 100 times
        indexed by g        pic 9(02).

move spaces to grades.
perform 0000-load-grades.
perform 0000-evaluate-grades.
.
.
..
0000-evaluate-grades.
    perform
        varying g from 1 by 1
        until (g > 100)
        or (grade(g) not numeric)
            evaluate grade (g)
                when ....
                when....
                end-evaluate
        end-perform.
```

#### ↳ Re: Evaluate Question

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G4HI2.392$NB5.994060@storm.twcol.com>`
- **References:** `<921782408.3125.0.nnrp-07.c1ed7479@news.demon.co.uk>`

```

FD    RESULTS-FILE.
01     RESULTS-REC.
         03 CAND-NO
         03 S-NAME
         03 RESULTS
              05 PAPER-1
              05 PAPER-2
              05 PAPER-3
         03 filler redefines results.
              05 paper occurs 3 times pic......

...

perform varying counter
        from 1 by 1
        until counter > 3
   EVALUATE PAPER (counter)
      WHEN 0 THRU 39
         ADD 1 TO W-RESULT-TABLE (counter, FAIL)
      WHEN 40 THRU 49
         ADD 1 TO W-RESULT-TABLE (counter, PASS)
      WHEN 50 THRU 69
         ADD 1 TO W-RESULT-TABLE (counter, CREDIT)
      WHEN 70 THRU 100
         ADD 1 TO W-RESULT-TABLE (counter, DISTINCTION)
   END-EVALUATE
end-perform
.

and don't forget to use conditionals.....


FD    RESULTS-FILE.
01     RESULTS-REC.
         03 CAND-NO
         03 S-NAME
         03 RESULTS
              05 PAPER-1
              05 PAPER-2
              05 PAPER-3
         03 filler redefines results.
              05 paper occurs 3 times pic......
                 88 is-fail           values 0 thru 39.
                 88 is-pass           values 40 thru 49.
                 88 is-credit         values 50 thru 69.
                 88 is-distinction    values 70 thru 100.
...

perform varying counter
        from 1 by 1
        until counter > 3
   EVALUATE PAPER (counter)
      WHEN is-fail (counter)
         ADD 1 TO W-RESULT-TABLE (counter, FAIL)
      WHEN is-pass (counter)
         ADD 1 TO W-RESULT-TABLE (counter, PASS)
      WHEN is-credit (counter)
         ADD 1 TO W-RESULT-TABLE (counter, CREDIT)
      WHEN is-distinction (counter)
         ADD 1 TO W-RESULT-TABLE (counter, DISTINCTION)
   END-EVALUATE
end-perform
.

FD    RESULTS-FILE.
01     RESULTS-REC.
         03 CAND-NO
         03 S-NAME
         03 RESULTS
              05 PAPER-1
              05 PAPER-2
              05 PAPER-3
         03 filler redefines results.
              05 paper occurs 3 times pic......
...
working-storage section.
01  filler.
    05 grade-table-data.
       10 filler pic x(10) value '1111111111'.
       10 filler pic x(10) value '1111111111'.
       10 filler pic x(10) value '1111111111'.
       10 filler pic x(10) value '1111111111'.
       10 filler pic x(10) value '2222222222'.
       10 filler pic x(10) value '3333333333'.
       10 filler pic x(10) value '3333333333'.
       10 filler pic x(10) value '4444444444'.
       10 filler pic x(10) value '4444444444'.
       10 filler pic x(10) value '4444444444'.
       10 filler pic x(10) value '4'.
    05 FILLER REDEFINES GRADE=TABLE-DATA.
       10 GRADE OCCURS 101 TIMES PIC 9(01).

perform varying counter
        from 1 by 1
        until counter > 3
   add 1 to W-RESULT-TABLE (COUNTER, GRADE( PAPER (COUNTER) ) )
end-perform
.


Is that simple and elegant?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
