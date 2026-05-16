[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fibonacci program

_7 messages · 4 participants · 2005-10_

---

### Re: Fibonacci program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-10-24T19:49:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Va7f.27284$8Q5.26431@fe08.news.easynews.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <1130166079.791746.296340@o13g2000cwo.googlegroups.com>`

```
I don't think you have told us what compiler (and operating system) you are 
using.  Your code is FULLY ANSI/ISO '85 Standard conforming (I think - I haven't 
compiled it with a standards flagger).

Some *EXTENSION* to THAT Standard that various replies have used include:

1) Inline comments, i.e. lines with
       *> this is a comment
    in them

2) EXIT PERFORM statement

3) conditional expression with only literals (no data-items), e.g.
    Until (1 < 0)

4) Procedure Division with no paragraph names in it.

   ***

Some of those are pretty common extensions to the '85 Standard - and others are 
not.  Several are *Standard* in the 2002 COBOL Standard.

My *personal* recommendation would be to keep coding STRICTLY '85 Standard 
code - until/unless your instructor tells you about certain "extensions" to use. 
You also need to know what IS and is not an extension in the compiler that you 
are using - as they may or may not be the same as what your instructor or other 
students have available.
```

#### ↳ Re: Fibonacci program

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-24T15:05:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <1130166079.791746.296340@o13g2000cwo.googlegroups.com> <2Va7f.27284$8Q5.26431@fe08.news.easynews.com>`

```
Good point, Bill. I keep forgetting that EXIT PERFORM is not a COBOL-85 
standard. Without the EXIT PERFORM, I would change the UNTIL condition as 
well:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.    Fibonacci.
       AUTHOR.        Judson McClendon.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77  Fib             PIC  9(09)  VALUE 1.
       77  Fib-1           PIC  9(09)  VALUE 0.
       77  Fib-2           PIC  9(09)  VALUE 0.
       77  End-Flag        pic  9(01)  VALUE 0.
       PROCEDURE DIVISION.
       DO-IT-TO-IT.
           DISPLAY "Fibonacci"
           DISPLAY "*********"
           PERFORM UNTIL (End-Flag = 1)
               DISPLAY Fib
               MOVE Fib-1 TO Fib-2
               MOVE Fib   TO Fib-1
               COMPUTE Fib = Fib-1 + Fib-2
                   ON SIZE ERROR
                       MOVE 1 TO End-Flag
               END-COMPUTE
           END-PERFORM
           DISPLAY "*********"
           STOP RUN.

Happy now?  ;-)
```

##### ↳ ↳ Re: Fibonacci program

- **From:** spg <stephen.gennard@microfocus.com>
- **Date:** 2005-10-27T17:59:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5d780e23a8e58c7a93478dc321c@hyperion>`
- **References:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net>`

```
Hello Judson,

Q. I thought the fibonacci series started at 0?
```

###### ↳ ↳ ↳ Re: Fibonacci program

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-10-27T17:38:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig88f.320641$oW2.80448@pd7tw1no>`
- **In-Reply-To:** `<a5d780e23a8e58c7a93478dc321c@hyperion>`
- **References:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net> <a5d780e23a8e58c7a93478dc321c@hyperion>`

```
spg wrote:
> Hello Judson,
> 
> Q. I thought the fibonacci series started at 0?

OK you purist :-) Following from just down the road from you - 
University of Guildford, (which was originally the Battersea School of 
Technology, where my wife's brother-in-law started as a lecturer) :-

"...... The Fibonacci numbers are  0, 1, 1, 2, 3, 5, 8, 13, ...  (add 
the last two to get the next)

The golden section numbers are ï¿½0ï¿½61803 39887... and ï¿½1ï¿½61803 39887...

The golden string is 1 0 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 0 1 ...
a sequence of 0s and 1s which is closely related to the Fibonacci 
numbers and the golden section......"

But computer-wise, even starting at zero you still have to fiddle to get 
the initial value of '1'.

Me, I went with Dan Brown's explanation and example as being Gospel. 
Perhaps 'Gospel' ain't a good word to use in association with the "da 
Vinci Code", which generated a whole sub-culture of anti da Vinci 
paperbacks, saying "Yes Brown quotes some historical/religious facts, 
BUT........".


Jimmy
```

###### ↳ ↳ ↳ Re: Fibonacci program

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-27T15:07:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqa8f.11895$wG.630@bignews4.bellsouth.net>`
- **References:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net> <a5d780e23a8e58c7a93478dc321c@hyperion>`

```
"spg" <stephen.gennard@microfocus.com> wrote:
> Hello Judson,
>
> Q. I thought the fibonacci series started at 0?


Impossible, because F(n) = F(n-1) + F(n-2). If F(1) = 0, F(2, ..., infinity) 
also = 0. :-)
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-27T15:21:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pDa8f.11898$wG.8202@bignews4.bellsouth.net>`
- **References:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net> <a5d780e23a8e58c7a93478dc321c@hyperion> <cqa8f.11895$wG.630@bignews4.bellsouth.net>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote:
> "spg" <stephen.gennard@microfocus.com> wrote:
>> Hello Judson,
…[5 more quoted lines elided]…
> infinity) also = 0. :-)

Sorry! Both you and Jimmy are correct. The first two numbers in the 
Fibonacci series are *defined* to be F(0) = 0 and F(1) = 1.
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-10-27T22:59:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gZc8f.321591$oW2.75157@pd7tw1no>`
- **In-Reply-To:** `<pDa8f.11898$wG.8202@bignews4.bellsouth.net>`
- **References:** `<V5b7f.9996$Ha4.8204@bignews1.bellsouth.net> <a5d780e23a8e58c7a93478dc321c@hyperion> <cqa8f.11895$wG.630@bignews4.bellsouth.net> <pDa8f.11898$wG.8202@bignews4.bellsouth.net>`

```
Judson McClendon wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> 
…[12 more quoted lines elided]…
> Fibonacci series are *defined* to be F(0) = 0 and F(1) = 1.

Following on from above, I went back to the U of G for background to
the Fibonacci sequence, (original name, Leonardo of Pisa),  in the real 
world. Yes, from a young girl at the cash desk in a local gas station I 
was aware of  the significance in Nature - (she's studying math at UofC 
- wants to become a math teacher) - and like you mentioned Judson, the 
Fibonacci pattern in the segments of a grapefruit etc.

Any of you math geeks may find the Guildford site both informative and
entertaining :-

www.surrey.ac.uk/search/    - (Enter "Fibonnaci" for your search)

Boy ! If math had been presented in this fashion when I was a kid, I
might not have been such a duffer ! As it was, a class of some 30 boys,
with three or four bright sparks up front, had to listen to a math
teacher who dreamed up crosswords for a quarterly published magazine -
clues and answers were supplied in Latin !!!!!!

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
