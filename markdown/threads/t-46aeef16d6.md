[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# student syntax error

_3 messages · 2 participants · 1999-10_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### student syntax error

- **From:** "old dog" <nospam@itesas.net>
- **Date:** 1999-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t6h8k$tnb@enews3.newsguy.com>`

```
The following is the end of a program that, when compiled with Micro Focus, two error messages occurs as follows (The italic bold font below is the same as the yellow lines in compiler software):

301-S Unreconized verb
348-S Procedure name 330-Close-Files undeclared, line 190 (first usage).  

I have used this same procedure with another program without problems.  I'm stuck.  Any help would be appreciated.  Thanks.  CIS student.

       300-WRAP-UP.
           PERFORM 310-SUMMARY-CALCULATION.
           PERFORM 320-SUMMARY-OUTPUT.
           PERFORM 330-CLOSE-FILES.

       310-SUMMARY-CALCULATION.
           COMPUTE UNIVERSITY-GPA = TOTAL-GRADE-POINTS / TOTAL-STUDENTS.

       320-SUMMARY-OUTPUT.
           MOVE TOTAL-CREDIT-HOURS TO TOTAL-CREDIT-HOURS-OUT
           WRITE REPORT-REC FROM TOTAL-LINE-1 AFTER 2
           MOVE TOTAL-GRADE-POINTS TO TOTAL-GRADE-POINTS-OUT
           WRITE REPORT-REC FROM TOTAL-LINE-2
           MOVE UNIVERSITY-GPA TO UNIVERSITY-GPA-OUT
           WRITE REPORT-REC FROM TOTAL-LINE-3

       330-CLOSE-FILES.
           CLOSE STUDENT-FILE  REPORT-FILE.
```

#### ↳ Re: syntax error fixed

- **From:** "old dog" <nospam@itesas.net>
- **Date:** 1999-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t6jj0$vfc@enews3.newsguy.com>`
- **References:** `<7t6h8k$tnb@enews3.newsguy.com>`

```
I finally realized the module above 320-Close-File did not have periods after the statements.  Sorry for the unneeded post.

Thanks
  old dog <nospam@itesas.net> wrote in message news:7t6h8k$tnb@enews3.newsguy.com...
  The following is the end of a program that, when compiled with Micro Focus, two error messages occurs as follows (The italic bold font below is the same as the yellow lines in compiler software):

  301-S Unreconized verb
  348-S Procedure name 330-Close-Files undeclared, line 190 (first usage).  
   
  I have used this same procedure with another program without problems.  I'm stuck.  Any help would be appreciated.  Thanks.  CIS student.

         300-WRAP-UP.
             PERFORM 310-SUMMARY-CALCULATION.
             PERFORM 320-SUMMARY-OUTPUT.
             PERFORM 330-CLOSE-FILES.

         310-SUMMARY-CALCULATION.
             COMPUTE UNIVERSITY-GPA = TOTAL-GRADE-POINTS / TOTAL-STUDENTS.

         320-SUMMARY-OUTPUT.
             MOVE TOTAL-CREDIT-HOURS TO TOTAL-CREDIT-HOURS-OUT
             WRITE REPORT-REC FROM TOTAL-LINE-1 AFTER 2
             MOVE TOTAL-GRADE-POINTS TO TOTAL-GRADE-POINTS-OUT
             WRITE REPORT-REC FROM TOTAL-LINE-2
             MOVE UNIVERSITY-GPA TO UNIVERSITY-GPA-OUT
             WRITE REPORT-REC FROM TOTAL-LINE-3

         330-CLOSE-FILES.
             CLOSE STUDENT-FILE  REPORT-FILE.
```

#### ↳ Re: student syntax error

- **From:** frederico_fonseca@eudoramail.com (Frederico Fonseca)
- **Date:** 1999-10-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f729ef.1093235@news.indigo.ie>`
- **References:** `<7t6h8k$tnb@enews3.newsguy.com>`

```
>301-S Unreconized verb
>348-S Procedure name 330-Close-Files undeclared, line 190 (first usage).  
>
>
>       320-SUMMARY-OUTPUT.
......
>           MOVE UNIVERSITY-GPA TO UNIVERSITY-GPA-OUT
>           WRITE REPORT-REC FROM TOTAL-LINE-3
----------------------------------------------^ missing "." at the end
of this line.
>
>       330-CLOSE-FILES.
>           CLOSE STUDENT-FILE  REPORT-FILE.

The above should solve it.

FF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
