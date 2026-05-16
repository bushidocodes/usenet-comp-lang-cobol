[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Getting rid of trailing spaces

_2 messages · 2 participants · 1999-08 → 1999-09_

---

### Getting rid of trailing spaces

- **From:** raider4967@my-deja.com
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qhcc2$60a$1@nnrp1.deja.com>`

```
Can someone help me get rid of trailing spaces in COBOL.  I have a file
that the fields are enclosed in quotes and is comma delimited.  And
example is as follows:


Cust#   Address                  Zip

"3534","123 So Ave            ","53436"
"6235","4321 Sesame St        ","84674"

And i want it to look like this:

"3534","123 So Ave","53436"
"6235","4321 Sesame St","84674"


This would no doubt change this to a varible length record, but i can't
seem to find out anything on this in any of my books.  Isint there a
keyword i can use like in Oracle you would use 'RTRIM(field)'  and that
would get rid of the spaces.  Is there anything i can do like that in
COBOL.  Any help would be greatly appreciated.  Thanks!


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Getting rid of trailing spaces

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cf3155@eeyore.callnetuk.com>`
- **References:** `<7qhcc2$60a$1@nnrp1.deja.com>`

```

Some implementations of COBOL allow you to specify removal of trailing
blanks from LINE SEQUENTIAL files by means of an external (run-time)
parameter, or a compiler directive.

This will NOT remove blanks from embedded fields. Neither is it
platform independent. COBOL allows us to write reasonably tight code that
will achieve both.
(The following is ALMOST platform independent; you would need to change the
file definition from LINE SEQUENTIAL to SEQUENTIAL (and specify variable
format  through JCL) if you were to run it on a mainframe...Across the PC
spectrum I believe it will run on any COBOL supported platform.)

       IDENTIFICATION DIVISION.
       PROGRAM-ID. 'STRTEST'.
      *AUTHOR. Peter E. C. Dashwood.
      * This program demonstrates the use of COBOL to remove trailing
      * blanks.
      *DATE_WRITTEN. September,1999.
       ENVIRONMENT DIVISION.
       configuration section.
       source-computer. IBM-PC.
       object-computer. IBM-PC.
       input-output section.
       file-control.
           select INFILE assign "input.csv"
                       organization is line sequential
                       access mode is sequential.
           select OUTFILE assign "output.csv"
                       organization is line sequential
                       access mode is sequential.

      *------------------------  DATA   DIVISION  ---------------------
       DATA DIVISION.
       file section.
       FD   INFILE
                        LABEL RECORDS STANDARD
                        DATA RECORD is INPUT-RECORD.
       01   INPUT-RECORD               pic x(255).



       FD   OUTFILE
                        LABEL RECORDS STANDARD
                        DATA RECORD is OUTPUT-RECORD.
       01   OUTPUT-RECORD              pic x(100).

       WORKING-STORAGE SECTION.
       01  field-1 pic x(7).
       01  field-2 pic x(50).
       01  field-3 pic x(8).

       01  record-counts.
           12 in-count                 pic s9(9) comp-5.
           12 out-count                pic s9(9) comp-5.
           12 display-count            pic 9(9).

       01  end-flag                    pic x.
           88 not-finished             value zero.
           88 finished                 value '1'.

       PROCEDURE DIVISION.
       MAIN SECTION.
       a000.
           perform startup-housekeeping
           perform main-logic until finished
           perform close-down
           .
       a999.
           stop run.
      *-----------------------------------------------------------
       STARTUP-HOUSEKEEPING            section.
       sh000.
           open input INFILE
                output OUTFILE
           initialize record-counts
           set not-finished to TRUE
           .
       sh999.
           exit.
      *-----------------------------------------------------------
       MAIN-LOGIC                      section.
       ml000.
           read INFILE
              at end
                 set finished to TRUE
                 go to ml999
           end-read
           add 1 to in-count
      *
      *   Remove the trailing blanks with COBOL string functions...
      *
           move spaces to field-1
                          field-2
                          field-3
           unstring input-record
              delimited by ','
                into field-1
                     field-2
                     field-3
           end-unstring
      *
      *   Unfortunately, there is a special case where field
      *   2 may terminate with a single space. This will NOT
      *   be removed by delimiting with a double space (which is
      *   the easy option). If it is absolutely necessary to remove
      *   ALL trailing spaces (even when there is only one), then
      *   we can handle it with the following inspect..
      *
           inspect field-2
              replacing all ' "' by '  '

      *
      *   ...this will convert the final space/quote to double space
      *   which will then be handled by the standard stringing.
      *
           move spaces to output-record
           string
             field-1
                 delimited by space
             ','
                 delimited by size
             field-2
                 delimited by '  '
             '",'
                 delimited by size
             field-3
                 delimited by space
                      into output-record
           end-string
           write output-record
           add 1 to out-count
           .
       ml999.
           exit.
      *----------------------------------------------------------
       CLOSE-DOWN                      section.
       cd000.
           close INFILE
                 OUTFILE
           move in-count to display-count
           display "Records read    =" display-count
           move out-count to display-count
           display "Records written =" display-count
           display space
           display "END OF RUN"
           .
       cd999.
           exit.
      *----------------    END OF PROGRAM 'STRTEST' ----------------



raider4967@my-deja.com wrote in message <7qhcc2$60a$1@nnrp1.deja.com>...
>Can someone help me get rid of trailing spaces in COBOL.  I have a file
>that the fields are enclosed in quotes and is comma delimited.  And
…[22 more quoted lines elided]…
>Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
