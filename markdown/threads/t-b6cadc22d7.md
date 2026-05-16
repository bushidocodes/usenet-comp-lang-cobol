[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can't find the problem.. (Net Express 4.0)

_10 messages · 7 participants · 2003-11_

---

### Can't find the problem.. (Net Express 4.0)

- **From:** xb00mx <member46895@dbforums.com>
- **Date:** 2003-11-04T02:00:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3556437.1067929248@dbforums.com>`

```

When "stepping" I'm getting this error:

163 Illegal character in numeric field

A:\ANBC02.int



.whenever it reaches MOVE USAGE-AB TO USAGE-PR in 700-DETAIL-LINE.

I can't find out where the problem is, nor can my teacher.



Any help would be great!






       IDENTIFICATION DIVISION.
       PROGRAM-ID. ANBC02.
       AUTHOR. AN BAYE.
       DATE-WRITTEN. NOV 2, 2003.
       DATE-COMPILED.
      *THIS PROGRAM READS A BILLING FILE, CALCULATES USAGE, CHARGES,
      *AND PRINTS A BILLING REPORT.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT DISKIN
               ASSIGN TO "A:\TDSC07"
               ORGANIZATION IS LINE SEQUENTIAL.
           SELECT RPT-OUT
               ASSIGN TO "A:\pfile.txt"
               ORGANIZATION IS LINE SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD  DISKIN
           RECORD CONTAINS 80 CHARACTERS
           LABEL RECORDS ARE STANDARD
           DATA RECORD IS DISK-REC.
       01  DISK-REC.
           05  CUST-NO-DK              PIC X(5).
           05  NAME-DK                 PIC X(15).
           05  METER-NO-DK             PIC 9(5).
           05  PREV-READ-DK            PIC 9(5).
           05  CURR-READ-DK            PIC 9(5).
           05  FILLER                  PIC X(45).
       FD  RPT-OUT
           RECORD CONTAINS 80 CHARACTERS
           LABEL RECORDS ARE OMITTED
           DATA RECORD IS RPT-REC.
       01  RPT-REC                     PIC X(80).
       WORKING-STORAGE SECTION.
       01  INDEPENDENT-ITEMS.
           05  LAST-REC-AB             PIC XXX VALUE "NO ".
           05  USAGE-AB                PIC S9(5) COMP-3.
           05  CHARGES-AB              PIC S9(5)V99 COMP-3.
           05  TOT-USAGE-AB            PIC S9(7) COMP-3.
           05  TOT-CHARGES-AB          PIC S9(5)V99 COMP-3.
       01  ID-LINE.
           05  FILLER                  PIC X(25)
               VALUE "ANBC02 WRITTEN BY AN BAYE".
           05  FILLER                  PIC X(55) VALUE SPACES.
       01  DETAIL-LINE.
           05  FILLER                  PIC X(5) VALUE SPACES.
           05  METER-NO-PR             PIC 9(5).
           05  FILLER                  PIC XXX VALUE SPACES.
           05  NAME-PR                 PIC X(15).
           05  FILLER                  PIC XXX VALUE SPACES.
           05  PREV-READ-PR            PIC ZZ,ZZ9.
           05  FILLER                  PIC XXX VALUE SPACES.
           05  CURR-READ-PR            PIC ZZ,ZZ9.
           05  FILLER                  PIC XXX VALUE SPACES.
           05  USAGE-PR                PIC ZZ,ZZ9.
           05  FILLER                  PIC XXX VALUE SPACES.
           05  CHARGES-PR              PIC $$,$$$.99.
           05  FILLER                  PIC X(13).
       01  TOTAL-LINE.
           05  FILLER                  PIC X(33) VALUE SPACES.
           05  FILLER                  PIC X(12) VALUE "FINAL TOTALS".
           05  FILLER                  PIC XXX VALUE SPACES.
           05  TOT-USAGE-PR            PIC ZZZ,ZZ9.
           05  FILLER                  PIC XX VALUE SPACES.
           05  TOT-CHARGES-PR          PIC $$$,$$$.99.
           05  FILLER                  PIC X(13).
       PROCEDURE DIVISION.
       010-MAINLINE.
           OPEN INPUT DISKIN.
           OPEN OUTPUT RPT-OUT.
           PERFORM 720-HEADINGS.
           READ DISKIN AT END MOVE "YES" TO LAST-REC-AB.
           PERFORM 100-REC-PROC UNTIL LAST-REC-AB = "YES".
           PERFORM 710-TOTAL-RTN.
           CLOSE DISKIN.
           CLOSE RPT-OUT.
           STOP RUN.
       100-REC-PROC.
           PERFORM 700-DETAIL-LINE.
           PERFORM 200-CALC-RTN.
           READ DISKIN AT END MOVE "YES" TO LAST-REC-AB.
       200-CALC-RTN.
           SUBTRACT PREV-READ-DK FROM CURR-READ-DK GIVING USAGE-AB.
           MULTIPLY USAGE-AB BY .06 GIVING CHARGES-AB.
           ADD USAGE-AB TO TOT-USAGE-AB.
           ADD CHARGES-AB TO CHARGES-AB.
       700-DETAIL-LINE.
           MOVE METER-NO-DK TO METER-NO-PR.
           MOVE NAME-DK TO NAME-PR.
           MOVE PREV-READ-DK TO PREV-READ-PR.
           MOVE CURR-READ-DK TO CURR-READ-PR.
           MOVE USAGE-AB TO USAGE-PR.
           MOVE CHARGES-AB TO CHARGES-PR.
           WRITE RPT-REC FROM DETAIL-LINE AFTER ADVANCING 1 LINE.
       710-TOTAL-RTN.
           MOVE TOT-USAGE-AB TO TOT-USAGE-PR.
           MOVE TOT-CHARGES-AB TO TOT-CHARGES-PR.
           WRITE RPT-REC FROM TOTAL-LINE AFTER ADVANCING 2 LINES.
       720-HEADINGS.
           MOVE SPACES TO RPT-REC.
           WRITE RPT-REC AFTER ADVANCING PAGE.
           WRITE RPT-REC FROM ID-LINE AFTER ADVANCING 1 LINE.
           MOVE SPACES TO RPT-REC.
           WRITE RPT-REC AFTER ADVANCING 1 LINE.
```

#### ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2003-11-04T09:44:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bo7ofi$43q$06$1@news.t-online.com>`
- **References:** `<3556437.1067929248@dbforums.com>`

```
I think there is a switch against this error ... like about
setenv COBSW -F  (unix shell)
I use only the compiler and I can find this directive in the
documentation User Guide 11-6. Have you no docu for the high
product 4.0? 


xb00mx wrote:

> 
> When "stepping" I'm getting this error:
…[131 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** "Gael Wilson" <gael.wilson@microfocus.uk.com>
- **Date:** 2003-11-04T09:57:53
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bo7tcg$a5s$1@hyperion.microfocus.com>`
- **References:** `<3556437.1067929248@dbforums.com> <bo7ofi$43q$06$1@news.t-online.com>`

```

"Vaclav Snajdr" <vsn@snajdr.de> wrote in message
news:bo7ofi$43q$06$1@news.t-online.com...
> I think there is a switch against this error ... like about
> setenv COBSW -F  (unix shell)
…[4 more quoted lines elided]…
>

Vaclav,

This suggestion prevents the error from occurring but does not fix the
problem.

xb00mx,

The problem is that the MOVE statement occurs before the value of USAGE-AB
is initialized so it will contain spaces, which are not valid in a numeric
data item. Either declare a VALUE for this in WORKING-STORAGE or INITIALIZE
the variable.

I am amazed that a teacher would not be able to spot this.

By the way, when 'stepping' did you try looking at thge value of the data
item ? That would have given you a clue as to why the value was illegal.
```

###### ↳ ↳ ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** xb00mx <member46895@dbforums.com>
- **Date:** 2003-11-04T09:34:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3557571.1067956462@dbforums.com>`
- **References:** `<3556437.1067929248@dbforums.com> <bo7ofi$43q$06$1@news.t-online.com> <bo7tcg$a5s$1@hyperion.microfocus.com>`

```

Originally posted by Gael Wilson 

> "Vaclav Snajdr" <vsn@snajdr.de> wrote in message

> news:bo7ofi$43q$06$1@news.t-
> online.comnews:bo7ofi$43q$06$1@news.t-online.com...

> > I think there is a switch against this error ... like about

> > setenv COBSW -F  (unix shell)

> > I use only the compiler and I can find this directive in
>     the

> > documentation User Guide 11-6. Have you no docu for the
>     high

> > product 4.0?

>

> Vaclav,

>

> This suggestion prevents the error from occurring but does not fix the

> problem.

>

> xb00mx,

>

> The problem is that the MOVE statement occurs before the value of
> USAGE-AB

> is initialized so it will contain spaces, which are not valid in
> a numeric

> data item. Either declare a VALUE for this in WORKING-STORAGE or
> INITIALIZE

> the variable.

>

> I am amazed that a teacher would not be able to spot this.

>

> By the way, when 'stepping' did you try looking at thge value of
> the data

> item ? That would have given you a clue as to why the value was
> illegal. 





Thanks Gael, sounds right, but how do I go about initializing it? Or
which would way be more efficient? I'm still new to COBOL.



This is a night class & my teacher had been teaching all day, so I'll
cut her some slack :) I'm sure she'll have an answer when I return
tomorrow night.
```

#### ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-11-04T07:31:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3557147.1067949097@dbforums.com>`
- **References:** `<3556437.1067929248@dbforums.com>`

```

use



$set SPZERO

  identification divisio.
```

#### ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-11-04T15:17:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fh9fqvcleukj26lboelqhlcroklhjf41np@4ax.com>`
- **References:** `<3556437.1067929248@dbforums.com>`

```
On Tue, 04 Nov 2003 02:00:48 -0500 xb00mx <member46895@dbforums.com> wrote:

:>When "stepping" I'm getting this error:

:>163 Illegal character in numeric field

:>A:\ANBC02.int

:>.whenever it reaches MOVE USAGE-AB TO USAGE-PR in 700-DETAIL-LINE.

Makes sense.

:>I can't find out where the problem is, nor can my teacher.

First of all, get a new teacher.

After that, ask yourself the following question:

"When is USAGE-AB initialized?"

After that, ask yourself if your program logic makes sense. COBOL will not
execute the paragraphs in numerical order - unless you program it that way.

   [ snipped ]
```

#### ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-04T17:48:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FA7E5F5.EAAD11C4@shaw.ca>`
- **References:** `<3556437.1067929248@dbforums.com>`

```


xb00mx wrote:

> When "stepping" I'm getting this error:
>
…[7 more quoted lines elided]…
>

Go with Gael's suggestions - either put zero values in fields in Working
Storage or INITIALIZE - see the on-line help for INITIALIZE with its
options. Simple example :-
01 SomeFields.
    05 FieldA            pic 9(03).            *> alternative approach
9(03) value 0.
    05 FieldB            pic x(30).            *> ,,
,,            x(30) value spaces.

INITIALIZE SomeFields.

I would recommend against the Directive $set SPZERO - it hides the
problem. While you are learning using N/E 4.0 you might eventually be
working with an IBM, UNISYS, Fujitsu, AcuCOBOL, RM/COBOL etc.... compiler.
No guarantee that the Directive will be available - then you will wonder
what has gone wrong.

Thing to remember - those examples I've given above - if not initial
values or INITIALIZED they contain JUNK when the program is first loaded.

I liked Benyamin's suggestion - but somehow don't think that's an option
for you <G>.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-04T16:11:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311041611.6c7c93a0@posting.google.com>`
- **References:** `<3556437.1067929248@dbforums.com> <3FA7E5F5.EAAD11C4@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote 

> Go with Gael's suggestions - either put zero values in fields in Working
> Storage or INITIALIZE - 
…[5 more quoted lines elided]…
> for you <G>.

Actually, Binyamin's suggestion about 'in sequence' was correct - the
lines:

>           PERFORM 700-DETAIL-LINE.
>           PERFORM 200-CALC-RTN.

Are being done in the wrong order, the calculations should be done
before the results are printed.

No 'zero' or 'initialise' need be done, just get the existing code
executing correctly.
```

###### ↳ ↳ ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-11-05T03:09:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FA868D5.EB76B31E@shaw.ca>`
- **References:** `<3556437.1067929248@dbforums.com> <3FA7E5F5.EAAD11C4@shaw.ca> <217e491a.0311041611.6c7c93a0@posting.google.com>`

```


Richard wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote
>
…[11 more quoted lines elided]…
>

<snip>

Oh Richard..(groannnnn)....... I was referring to his - "First of all, get a
new teacher."

Jimmy
```

#### ↳ Re: Can't find the problem.. (Net Express 4.0)

- **From:** xb00mx <member46895@dbforums.com>
- **Date:** 2003-11-05T01:58:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3561086.1068015491@dbforums.com>`
- **References:** `<3556437.1067929248@dbforums.com>`

```

>           PERFORM 700-DETAIL-LINE.

>           PERFORM 200-CALC-RTN.





Ahhhh no wonder I was getting 0 for the calculations in the first
record! :)

Everything works as planned. Thanks a ton guys.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
