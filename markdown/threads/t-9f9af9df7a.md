[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# strange output

_9 messages · 7 participants · 2001-09 → 2001-10_

---

### strange output

- **From:** pauldbq@yahoo.com (dbq)
- **Date:** 2001-09-30T10:47:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```
I'm getting some strange output when I run MF Cobol.  I have Animator
2. V.8.2.75 on Windows.  Let me preface this by saying I think that I
have a compiler directive set that I can't set back to the default. 
So my first question is how do you set all the compiler directives
back to their default values?

That said here is the output:

  EMPLOYEE       EMPLOYEE            OFF  MONTHLY SOC. SEC. # OF JOB
   NUMBER          NAME              NUMB SALARY   NUMBER   DEP. CODE

   NU00001  SMITH                    N01B   500Y 123-45-6789D01. 23DE
   NU00002  JONES                    N01B  1000Y 987-65-4321D09. 87DE
            PROGRAM: REV7_IN.DAT                 OUT:  REV7_OUT.DOC


As you can see, the ouput has alphanumeric values that should not be
there.  My input file is as follows:

00001SMITH               010105000012345678901234567890123456789012345
00002JONES               020110000098765432109876543210987654321098765

Note that the input file is a *.DAT file and the output file is a .DOC
file.

So, I suspect I set a compiler directive that is causing this.

Finally, the real issue is the monthly salary field.  If I read and
write it as a PIC X(6) field it is fine, but if I attempt to change
the field to
PIC 9(4)V99 (both read and write), the program fails.

The error message I get is 'RTS0163 Runtime Error, Illegal Character
in Numberic Field (error 163)'.

The line the error message is highlighting is:

           MOVE MONTHLY-SALARY-IN TO MONTHLY-SALARY-OUT

The section of code that is relevant is as follows:


       FILE SECTION.
       FD  PAYROLL-FILE LABEL RECORDS ARE STANDARD.
       01  PAYROLL-REC.
           05  EMPLOYEE-NUMBER-IN                PIC X(5).
           05  EMPLOYEE-NAME-IN                  PIC X(20).
           05  LOCATION-CODE-IN.
               10  TERRITORY-NUMBER-IN           PIC XX.
               10  OFFICE-NUMBER-IN              PIC XX.
           05  MONTHLY-SALARY-IN                 PIC 9(4)V99.
           05  SOCIAL-SECURITY-NUMBER-IN         PIC X(9).
           05  NUMBER-OF-DEPENDENTS-IN           PIC XX.
           05  JOB-CLASSIFICATION-CODE-IN        PIC XX.
           05  UNUSED-IN                         PIC X(22).
       FD  PRINT-FILE LABEL RECORDS ARE STANDARD.
       01  PRINT-REC.
           05                                  PIC X(5).
           05  EMPLOYEE-NUMBER-OUT             PIC X(5) VALUE SPACES.
           05                                  PIC XX.
           05  EMPLOYEE-NAME-OUT               PIC X(20) VALUE SPACES.
           05                                  PIC X.
           05  TERRITORY-NUMBER-OUT            PIC XX VALUE SPACES.
           05                                  PIC X(3).
           05  OFFICE-NUMBER-OUT               PIC XX VALUE SPACES.
           05                                  PIC XX.
           05  MONTHLY-SALARY-OUT              PIC 9(4)V99 VALUE
ZEROS.
           05                                  PIC XX.
           05  SOCIAL-SECURITY-NUMBER-OUT      PIC X(9) VALUE SPACES.
           05                                  PIC XX.
           05  NUMBER-OF-DEPENDENTS-OUT        PIC XX VALUE SPACES.
           05                                  PIC XX.
           05  JOB-CLASSIFICATION-CODE-OUT     PIC XX VALUE SPACES.
           05                                  PIC X(3).

In summary the problem I am running into is having the compiler
recognize that one particular field as a NUMERIC field as opposed to a
ALPHANUMERIC field.
```

#### ↳ Re: strange output

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-09-30T20:29:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010930162926.01328.00000449@nso-mb.aol.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```
In article <b7bceb3e.0109300947.1ff4c76a@posting.google.com>, pauldbq@yahoo.com
(dbq) writes:

>
>I'm getting some strange output when I run MF Cobol.  I have Animator
>2. V.8.2.75 on Windows.  Let me preface this by saying I think that I

>
>That said here is the output:
…[7 more quoted lines elided]…
>
    The output here looks suspiciuosly like an overlayed data situation.
    

>
>As you can see, the ouput has alphanumeric values that should not be
…[15 more quoted lines elided]…
>

  I believe that the print definition should not have an implied decimal.
  try using an actual decimal there.
```

#### ↳ Re: strange output

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-09-30T22:46:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg0frt0dj7kg1feef4hp82tb419e7p52pt@4ax.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```
On 30 Sep 2001 10:47:56 -0700 pauldbq@yahoo.com (dbq) wrote:

:>I'm getting some strange output when I run MF Cobol.  I have Animator
:>2. V.8.2.75 on Windows.  Let me preface this by saying I think that I
:>have a compiler directive set that I can't set back to the default. 
:>So my first question is how do you set all the compiler directives
:>back to their default values?

Not a clue.

:>That said here is the output:

:>  EMPLOYEE       EMPLOYEE            OFF  MONTHLY SOC. SEC. # OF JOB
:>   NUMBER          NAME              NUMB SALARY   NUMBER   DEP. CODE

:>   NU00001  SMITH                    N01B   500Y 123-45-6789D01. 23DE
:>   NU00002  JONES                    N01B  1000Y 987-65-4321D09. 87DE
:>            PROGRAM: REV7_IN.DAT                 OUT:  REV7_OUT.DOC


:>As you can see, the ouput has alphanumeric values that should not be
:>there.  My input file is as follows:

If I recall correctly, the VALUE clause in the FILE SECTION (or LINKAGE
SECTION), when allowed, is merely a comment. The record area in the FILE
SECTION is not really part of your data area, it is a system area mapped to
your program. 

Most programmers would recommend having the detailed output record area in the
WORKING-STORAGE SECTION and just an 01 level in the file section, and to use
WRITE FROM.

:>00001SMITH               010105000012345678901234567890123456789012345
:>00002JONES               020110000098765432109876543210987654321098765

:>Note that the input file is a *.DAT file and the output file is a .DOC
:>file.

:>So, I suspect I set a compiler directive that is causing this.

:>Finally, the real issue is the monthly salary field.  If I read and
:>write it as a PIC X(6) field it is fine, but if I attempt to change
:>the field to
:>PIC 9(4)V99 (both read and write), the program fails.

I don't understand how the trailing zeroes are being suppressed while using
either PIC 9(4)V99 or X(6).

:>The error message I get is 'RTS0163 Runtime Error, Illegal Character
:>in Numberic Field (error 163)'.

:>The line the error message is highlighting is:

I would suggest DISPLAYing PAYROLL-REC or: 

             05  MONTHLY-SALARY-IN-CHAR.
                 10  MONTHLY-SALARY-IN             PIC 9(4)V99.

and DISPLAYing MONTHLY-SALARY-IN-CHAR.


:>           MOVE MONTHLY-SALARY-IN TO MONTHLY-SALARY-OUT

:>The section of code that is relevant is as follows:

I suggest posting the entire program rather than your abstract of the DATA
DIVISION.

   [ snipped ]
```

##### ↳ ↳ Re: strange output

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-02T20:31:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BBA162C.39F0E2CA@Azonic.co.nz>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com> <bg0frt0dj7kg1feef4hp82tb419e7p52pt@4ax.com>`

```
Binyamin Dissen wrote:
> 
> The record area in the FILE
> SECTION is not really part of your data area, it is a system area mapped to
> your program.

That depends on the implementation.  With MF Cobol I believe the record
areas _are_ part of the program.  YMMV.

> Most programmers would recommend having the detailed output record area in the
> WORKING-STORAGE SECTION and just an 01 level in the file section, and to use
> WRITE FROM.

That recommendation may be true of the programmers that you know.
Whether this is 'most' is indeterminate. Personally I see nothing wrong
with an output record being created and written in file section, just
make sure that a MOVE SPACES (or similar) to the record area is done
before the fields are populated. And if I do use a WS area, for example
page headings, I never use WRITE .. FROM, I use a MOVE followed by a
WRITE.  Using a decent editor allows me to duplicate the MOVE x to y
line and change this to WRITE y in less keystrokes than typing the FROM.

> I don't understand how the trailing zeroes are being suppressed while using
> either PIC 9(4)V99 or X(6).

They aren't 'being suppressed', they never existed (most likely), he is
doing an alphanumeric move and has the record misaligned so that he
misses getting the full data item when defined as PIC X(6), or a 163
error when defined as 9(4)V99.
```

#### ↳ Re: strange output

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-30T16:55:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9p84cm$r2k$1@slb1.atl.mindspring.net>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```
As other have already stated,

A) you probably want a numeric-edited rather than numeric field in your
output (print) file, i.e. "." rather than "V" in the PICTURE.

B) VALUE clauses (other than for 88-levels) are ignored in the File section
(when allowed as an extension to the ANSI Standard).

  ***

However, I don't think that EITHER of those would cause the problem that you
are getting.

From your record descriptions and the input data that you show us, I can
think of two possibilities - neither of them real likely - but still
possible.

1) Do you define your input (and probably output) files as "LINE SEQUENTIAL"
in the Select/Assign clause?  If the input file is "delimited" by
carriage-return and line-feed (i.e. a "normal" PC or Unix file) then this
could cause you to get "odd" results and to seem to get non-numeric data in
numeric input fields.

2) When you run the program under Animator, what *IS* the value of
    MONTHLY-SALARY-IN
just before the "problem"?   Is there some chance that you are trying to
"process" a record *after* end-of-file, (i.e. working on a "3rd" record when
you only have 2).  This would cause you to process a "messy buffer" of data
without having a numeric value in in your input field.

 ***

There are run-time (and compiler) features to "get around" 163 errors (with
Micro Focus) - particularly the +/-F switch.  HOWEVER, I don't think you
should "play with that" as you seem to be having some other problem.

HINT:  In the "real world" it is usually a VERY GOOD idea to check numeric
fields with the "IF NUMERIC" test before trying to use them as numeric data.
My guess is that you are very early in your COBOL training, but you will
soon be required to deal with "invalid" input.
```

##### ↳ ↳ Re: strange output

- **From:** pauldbq@yahoo.com (dbq)
- **Date:** 2001-10-03T20:12:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7bceb3e.0110031912.74309508@posting.google.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com> <9p84cm$r2k$1@slb1.atl.mindspring.net>`

```
I want to thank all who helped me resolve this issue.  I particularly
want to thank John for the DEBUG command.  I added the following to my
process module:

          DISPLAY 'DEBUG~ TOTAL >' MONTHLY-SALARY-TOTAL '<'      
          DISPLAY 'DEBUG~ EMPLOYEES >' NUMBER-OF-EMPLOYEES '<'

The above lines allowed me to determine that my INPUT data was
corrupted.  William was right (see below) in that there must have been
some control characters at the end of each record.  I went to the end
of each record and deleted those invisible characters.  (Aside: 
anyway to make them visible?)

<snip>

> A) you probably want a numeric-edited rather than numeric field in your
> output (print) file, i.e. "." rather than "V" in the PICTURE.

William, good idea!  I used a PIC ZZZ9.99 for my output.

<snip>

> 1) Do you define your input (and probably output) files as "LINE SEQUENTIAL"
> in the Select/Assign clause?  If the input file is "delimited" by
> carriage-return and line-feed (i.e. a "normal" PC or Unix file) then this
> could cause you to get "odd" results and to seem to get non-numeric data in
> numeric input fields.

William hit the nail on the head!

<snip>

> HINT:  In the "real world" it is usually a VERY GOOD idea to check numeric
> fields with the "IF NUMERIC" test before trying to use them as numeric data.
> My guess is that you are very early in your COBOL training, but you will
> soon be required to deal with "invalid" input.

<snip>

William is right again.  The 'IF' stuff is coming up.  I'm certainly
not looking forward to dealing with 'invalid input' however.

Again, thanks to all who responded!

Paul
```

#### ↳ Re: strange output

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-01T00:53:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_7Pt7.10547$ev2.16955@www.newsranger.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```
HI Paul,

The unwanted A/N chars in the detail line is the heading line chars that have
not been overlaid by your detail moves. Try moving SPACES to PRINT-REC before
you move the detail data.

The only reason I can think of that could cause an error when using PIC 9(4)V99
is that the field sometimes contains SPACES or other A/N chars. My bet is
SPACES. Does the error occur on the 1st record? As Benjimin suggested DISPLAY
the field, but keep it as PIC X(6). Also write the display like this:

DISPLAY 'DEBUG~ SALARY >' MONTHLY-SALARY-IN '<'                   

This will delimit the display and you can determine if spaces or other non-
displayable chars are in the field.

You may want to check the lengths of the I/P fields before the salary to make
sure they match the field lengths in the I/P. This could be the cause of the
error too.

HTH, Jack. 



In article <b7bceb3e.0109300947.1ff4c76a@posting.google.com>, dbq says...
>
>I'm getting some strange output when I run MF Cobol.  I have Animator
…[77 more quoted lines elided]…
>ALPHANUMERIC field.
```

#### ↳ Re: strange output

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-01T02:51:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB7DB64.51E08D10@home.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```


dbq wrote:

> I'm getting some strange output when I run MF Cobol.  I have Animator
> 2. V.8.2.75 on Windows.  Let me preface this by saying I think that I
> have a compiler directive set that I can't set back to the default.
> So my first question is how do you set all the compiler directives
> back to their default values?

Paul,

Can't think why you would want Directives for this one - just delete them
(the lines starting $set ... in column 7), and the Directives are re-set
to their defaults.

The following works, and I also show the ouput PrintFile. The only change
I've made is to show the PrintFile salary field as numeric edited.

You can give the files any extensions you want "dat", "dta", "doc" or
"text". The only one that M/F is fussy about is that you don't use "idx"
because that signifies the index file for an ISAM data file.

Compare below with what you've done to see if there is a difference. Check
your MOVEs to the print fields.

*>---------------------- payroll.cbl ----------------------------

INPUT-OUTPUT SECTION.

     Select               Payroll-File
     assign               "c:\PayrollFile.dat"
     organization         line sequential
     access               sequential
     file status          FileStatus.

     Select               Print-File
     assign               "c:\PrintFile.dat"
     organization         line sequential
     access               sequential
     file status          FileStatus.


FILE SECTION.
*>00001SMITH               0101050000123456789012345678901234567890
*>00002JONES               0201100000987654321098765432109876543210
*>kkkkknnnnnnnnnnnnnnnnnnnnttoossssssiiiiiiiiiddjjuuuuuuuuuuuuuuuuu

FD  PAYROLL-FILE. *> don't need LABEL RECORDS ARE STANDARD.
01  PAYROLL-REC.
    05  EMPLOYEE-NUMBER-IN                PIC X(5).
    05  EMPLOYEE-NAME-IN                  PIC X(20).
    05  LOCATION-CODE-IN.
        10  TERRITORY-NUMBER-IN           PIC XX.
        10  OFFICE-NUMBER-IN              PIC XX.
    05  MONTHLY-SALARY-IN                 PIC 9(4)V99.
    05  SOCIAL-SECURITY-NUMBER-IN         PIC X(9).
    05  NUMBER-OF-DEPENDENTS-IN           PIC XX.
    05  JOB-CLASSIFICATION-CODE-IN        PIC XX.
    05  UNUSED-IN                         PIC X(22).


FD PRINT-FILE. *> Ditto -  LABEL RECORDS ARE STANDARD.
01 PRINT-REC.
   05                                PIC X(5).
   05  EMPLOYEE-NUMBER-OUT           PIC X(5) VALUE SPACES.
   05                                PIC XX.
   05  EMPLOYEE-NAME-OUT             PIC X(20) VALUE SPACES.
   05                                PIC X.
   05  TERRITORY-NUMBER-OUT          PIC XX VALUE SPACES.
   05                                PIC X(3).
   05  OFFICE-NUMBER-OUT             PIC XX VALUE SPACES.
   05                                PIC XX.
   05  MONTHLY-SALARY-OUT            PIC zzz9.99 Blank when zero.
   05                                PIC XX.
   05  SOCIAL-SECURITY-NUMBER-OUT    PIC X(9) VALUE SPACES.
   05                                PIC XX.
   05  NUMBER-OF-DEPENDENTS-OUT      PIC XX VALUE SPACES.
   05                                PIC XX.
   05  JOB-CLASSIFICATION-CODE-OUT   PIC XX VALUE SPACES.
   05                                PIC X(3).

Working-Storage Section.
01 FileFlag                        pic 9.
    88 FileNotFinished             value 1.
    88 FileFinished                value 0.
01 FileStatus                      pic x(02).

Procedure Division.
 Open INPUT  Payroll-File
 Open OUTPUT Print-File
 set FileNotFinished to true
 perform until FileFinished
   Read Payroll-File next record
      at end
          set FileFinished to true
      not at end
          perform A-PRINT-RECORD
   End-read
 End-Perform
 Close Payroll-File, Print-File
 STOP RUN.

A-PRINT-RECORD.

move EMPLOYEE-NUMBER-IN          to EMPLOYEE-NUMBER-OUT
move EMPLOYEE-NAME-IN            to EMPLOYEE-NAME-OUT
move TERRITORY-NUMBER-IN         to TERRITORY-NUMBER-OUT
move OFFICE-NUMBER-IN            to OFFICE-NUMBER-OUT
move MONTHLY-SALARY-IN           to MONTHLY-SALARY-OUT
move SOCIAL-SECURITY-NUMBER-IN   to SOCIAL-SECURITY-NUMBER-OUT
move NUMBER-OF-DEPENDENTS-IN     to NUMBER-OF-DEPENDENTS-OUT
move JOB-CLASSIFICATION-CODE-IN  to JOB-CLASSIFICATION-CODE-OUT
write PRINT-REC

*> Tip - reference above - check the syntax for MOVE CORRESPONDING.....
.
*>--------------------------------------------------------.
 And your PrintFile looks like :-

     00001  SMITH                01   01   500.00  123456789  01  23
     00002  JONES                02   01  1000.00  987654321  09  87
*>----------------------------------------------------------------------------

Jimmy, Calgary AB
```

#### ↳ Re: strange output

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-01T03:30:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB7E4A0.AADF3F67@home.com>`
- **References:** `<b7bceb3e.0109300947.1ff4c76a@posting.google.com>`

```


dbq wrote:

Paul,

Further thoughts after my  last message. This *may* be what you are doing
incorrectly. Your print layout.

In working storage you want :-

01 HeaderRecord1 pic x(???)
01 HeaderRecord2 pic x(???)
01 DetailRecord .
           05                                  PIC X(5).
           05  EMPLOYEE-NUMBER-OUT             PIC X(5) VALUE SPACES.
           05                                  PIC XX.
           etc.

Then specify your File Print-Rec as pic x(??) for the LARGEST of the
above.

Write Print-Rec from HeaderRecord1
Write Print-Rec from HeaderRecord2
move spces to Print-Rec
write print-rec
Now do the perform read-next and for each incoming record
    MOVE x to y
    write print-rec from Detail-Record

Note you formatted your SSN :-

   987-65-4321 - this is ELEVEN characters not the pic x(09) you specified
for output.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
