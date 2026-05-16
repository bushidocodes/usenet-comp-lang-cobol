[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fibonacci program

_2 messages · 2 participants · 2005-10_

---

### Re: Fibonacci program

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-24T11:20:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5P77f.27$wG.8@bignews4.bellsouth.net>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <1130166079.791746.296340@o13g2000cwo.googlegroups.com>`

```
Good first try, but you didn't use ON SIZE ERROR. Since you did your own 
work, I don't mind helping you more. Check out this version and see if you 
like it better:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.    Fibonacci.
       AUTHOR.        Judson McClendon.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77  Fib             PIC  9(09)  VALUE 1.
       77  Fib-1           PIC  9(09)  VALUE 0.
       77  Fib-2           PIC  9(09)  VALUE 0.
       PROCEDURE DIVISION.
       DO-IT-TO-IT.
           DISPLAY "Fibonacci"
           DISPLAY "*********"
           PERFORM UNTIL (1 < 0)
               DISPLAY Fib
               MOVE Fib-1 TO Fib-2
               MOVE Fib   TO Fib-1
               COMPUTE Fib = Fib-1 + Fib-2
                   ON SIZE ERROR
                       EXIT PERFORM
               END-COMPUTE
           END-PERFORM
           DISPLAY "*********"
           STOP RUN.
```

#### ↳ Re: Fibonacci program

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-10-24T18:31:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aM97f.283001$oW2.248340@pd7tw1no>`
- **In-Reply-To:** `<5P77f.27$wG.8@bignews4.bellsouth.net>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <1130166079.791746.296340@o13g2000cwo.googlegroups.com> <5P77f.27$wG.8@bignews4.bellsouth.net>`

```
Judson McClendon wrote:
> Good first try, but you didn't use ON SIZE ERROR. Since you did your own 
> work, I don't mind helping you more. Check out this version and see if you 
…[24 more quoted lines elided]…
>            STOP RUN.

Good on you Spartacus for figuring it out. Just for info, here's mine to 
compare to what Judson produced - not too dissimilar :-

        Program-id.     Fibonacci.

        WORKING-STORAGE SECTION.

        01 n                   pic 9(09).
        01 ANumber occurs 3    pic 9(09).
        01 ws-display          pic zzz,zzz,zzz blank when zero.

        01 ProgramFlag         pic 9.
           88 ContinueProgram  value 0.
           88 CancelProgram    value 1.

        PROCEDURE DIVISION.

        *> Note : I have a 'forever' PERFORM - it will never
        *> achieve CancelProgram. My reasoning - if your
        *> Instructor said 'Now change the fileds to pic 9(12)
        *> and the ws-display", it will work up to the current
        *> maximum  of pic 9(18).

        set ContinueProgram to true
        Move 1      to ANumber(1)
        move zeroes to ANumber(2)
        perform varying n from 1 by 1 until CancelProgram

           COMPUTE  ANumber(3) = ANumber(1) + ANumber(2)
                    On Size Error
                       compute ws-display = n - 1

        *> The on size error occurs on the 44th,
        *> not 45th iteration

                       Display " "
                       Display "There were", ws-display
                       " Iterations before exceeding 999,999,999"
                       EXIT PERFORM
                    Not On size Error
                       move ANumber(3) to ws-display
                       display ws-display
           END-COMPUTE

           move ANumber(2) to ANumber(1)
           move ANumber(3) to ANumber(2)

        End-perform

        STOP RUN.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
