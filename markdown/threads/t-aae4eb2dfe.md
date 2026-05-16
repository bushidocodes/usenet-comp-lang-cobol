[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Routine

_1 message · 1 participant · 1998-09_

---

### Re: Right Justify Routine

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<brVI1.113$g04.191952@news3.mia.bellsouth.net>`
- **References:** `<Jl0PnHJ5PvPd-pn2-XiTbHJiS5z0r@Dwight_Miller.iix.com> <o%VH1.3786$gM3.2803875@news4.mia.bellsouth.net> <trYH1.464$I%.1378959@news1.atlantic.net> <HtbI1.5187$eZ3.3317864@news3.mia.bellsouth.net> <BseI1.481$I%.1861130@news1.atlantic.net> <uCwI1.5340$gM3.3883152@news4.mia.bellsouth.net> <xkRI1.695$I%.2804567@news1.atlantic.net>`

```
Rick Smith wrote in message ...
>
>Judson McClendon wrote in message ...
…[7 more quoted lines elided]…
>working with an index speed it up or slow it down?


Very observant! :-)  Yes, I originally wrote a jud1-coded and jud2-coded.
Jud2-coded used indexing instead of reference modification in the loops.
It was somewhat faster then jud1-coded, until I changed the working data
fields to COMP-5, when it was about the same speed.  Below is the program.
The times on my PII400 using MF COBOL 3.2 (DOS) were:

  DISP  COMP-5 Work variable (i,j,k) usage
  100k   500k  Nbr of loops

 11.53  57.28  Rick
  6.21  31.20  Judson
  1.97   0.55  hand-coded
  0.88   0.38  jud1
  0.22   0.38  jud2

Please note that the timer resolution in PCs is only to 0.055 seconds, so
you will see some variations on consecutive runs of the same program.
Surprisingly, jud2 is about 9 times faster than hand-coded, and 4 times
faster than jud1, using display variables, but about the same speed using
comp-5 comp-5 variables.  The lines changed between the two above trials
are marked with '->' in the program below.

       Identification Division.
       Program-Id.  Test3.
      * right justify
       Environment Division.
       Configuration Section.
       Source-Computer.  IBM-PC.
       Object-Computer.  IBM-PC.
       Data Division.
       Working-Storage Section.
       01  input-field               value spaces.
           03  input-char  pic x     occurs 30 times
                                     indexed by icx.
       01  output-field    pic x(30) value spaces.
       01  counter         pic s9(4) comp-5  value 1.
       01 char pic x.

Trial 1:

->     01 i pic s9(4).
->     01 j pic s9(4).
->     01 k pic s9(4).
->     01 loop pic s9(9) comp-5 value 100000.

Trial 2:

->     01 i pic s9(4)    comp-5.
->     01 j pic s9(4)    comp-5.
->     01 k pic s9(4)    comp-5.
->     01 loop pic s9(9) comp-5 value 500000.

       Procedure Division.
       test-3-start.
           display function current-date (13:4)
           perform test3-start-Rick loop times
           display function current-date (13:4)
           perform test3-start-Judson loop times
           display function current-date (13:4)
           perform test3-start-hand-coded loop times
           display function current-date (13:4)
           perform test3-start-jud1-coded loop times
           display function current-date (13:4)
           perform test3-start-jud2-coded loop times
           display function current-date (13:4)
           accept char
           stop run
           .

       test3-start-Rick.
           move "abcdefghijklm" to input-field
           move 1 to counter
           if input-field > spaces
               move function reverse (input-field) to input-field
               inspect input-field tallying counter for leading spaces
               move function reverse (input-field (counter:))
                   to input-field (counter:)
           end-if
           .

       test3-start-Judson.
           move "abcdefghijklm" to input-field
           move 1 to counter
           if input-field not = spaces
               move function reverse(input-field) to output-field
               inspect output-field tallying counter for leading spaces
               string input-field delimited by size
                   into output-field with pointer counter
           end-if
           .

       test3-start-hand-coded.
           move "abcdefghijklm" to input-field
           if input-field not = spaces
               move function length (input-field) to i j
               perform until input-field (i:1) not = space
                   subtract 1 from i
               end-perform
               perform until i = 0
                   move input-field (i:1) to input-field (j:1)
                   subtract 1 from i
                   subtract 1 from j
               end-perform
               if j > 0
                   move spaces to input-field (1:j)
               end-if
           end-if
           .

       test3-start-jud1-coded.
           move "abcdefghijklm" to input-field
           if input-field not = spaces
               move function length (input-field) to i j
               perform until input-field (i:1) not = space
                   subtract 1 from i
               end-perform
               subtract i from j
               add 1 j giving k
               move input-field (1:i) to output-field (k:i)
               if j > 0
                   move spaces to output-field (1:j)
               end-if
           end-if
           .

       test3-start-jud2-coded.
           move "abcdefghijklm" to input-field
           if input-field not = spaces
               move function length (input-field) to j
               perform varying icx
                       from j by -1
                       until input-char (icx) not = space
               end-perform
               set i to icx
               subtract i from j
               add 1 j giving k
               move spaces to output-field
               move input-field (1:i) to output-field (k:i)
           end-if
           .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
