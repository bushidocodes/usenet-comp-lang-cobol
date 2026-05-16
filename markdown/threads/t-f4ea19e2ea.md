[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# demo: huge number calculator and library

_7 messages · 6 participants · 2004-07 → 2004-08_

---

### demo: huge number calculator and library

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-31T00:36:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410ae85f.29667620@news.optonline.net>`

```
*                   Calculator and Huge Number Library
*
* This is a demo of huge integer calculations. Want 10,000-digit numbers?
* The demo uses 200 digits -- 100 to the left and 100 to the right.
*
* The program can be used three ways:
*
* .. Executed from the command line, it prompts for a formula, calculates
*    and displays the answer. Examples:
*    1+1
*    ((17 / 3)+2.7183)*(5!)
*    2^.5
*
* .. Called by a program with a formula and optional values. Example:
*    move '((17/3)+2)*(5!)' to my-formula
*    call 'CALCPARS' using a, b, c, my-formula
*    move c to a
*    move 'a^.5' to my-formula
*    call 'CALCPARS' using a, b, c, my-formula
*    move c to the-answer
*
* .. Low-level functions called by a program. Example:
*    move ... to a
*    move ... to b
*    call 'CALCADD' using a, b, c
*    move c to the-answer
*
* Functions are +, -, *, /, ! and ^ (exponent)
*
* Micro Focus compile commands:
*   cob -xg calc.cbl     # executable to run from command line
*   cob -zg calc.cbl     # callable program (so)
*   cob -xg yourprog ./calc.so   # your program bound to above
*

      $SET SOURCEFORMAT"FREE"
   identification division
*  program-id.                                 CALC
*  author.                                     Robert Wagner
*  date-written.                               07/29/04
*    Huge number function library.
*    Parses formula out of a string.
*    Runs three ways:
*      From command line -- type in formula
*      Call CALCPARS -- to parse and evaluate formula
*      Call CALCxxxx low-level functions
*
*    Negative numbers are nines complement.
*    The left half contains the 'whole number' and the right half contains the
*    fraction.
*
*    Note that everything is relative to the size of 'huge' below.
*    The program would read better if I could equate
*    'mid' to 'length of huge / 2'. I couldn't find a way in Cobol 85.

 . data division
 . working-storage section
 . 01  huge typedef.
 .     05  a-digit occurs 200                        pic  9(01).
 . 01  calcpars-variables
 .     05  p                                 binary  pic s9(04)
 .     05  sp                                binary  pic s9(04)
 .     05   value 'd'                                pic  x(01)
 .          88  debug-mode value 'd'.
 . 01  the-stack
 .     05  stack-entry occurs 10
 .         10  stack-number                          huge
 .         10  stack-operation                       pic  x(01)
 . 01  typein                                        pic  x(128)
 . 01  x                                             huge
 . 01  y                                             huge
 . 01  z                                             huge

 . 01  calchuge-variables
 .     05  i                                 binary  pic s9(04)
 .     05  j                                 binary  pic s9(04)
 .     05  k                                 binary  pic s9(04)
 .     05  l                                 binary  pic s9(04)
 .     05  power                             binary  pic s9(04)
 .     05  factorial                         binary  pic s9(04)
 .     05  temp-s                            binary  pic s9(02)
 .     05  term                                      pic  9(02)
 .     05  overflow-digit                            pic  9(01)
 .     05  two-digits                                pic  9(02)
 .     05    redefines two-digits
 .         10  digit-1                               pic  9(01)
 .         10  digit-2                               pic  9(01)
 .     05  sign-count                                pic  9(01)
 . 01  d                                             huge
 . 01  temp-1                                        huge
 . 01  temp-2                                        huge
 . 01  temp-3                                        huge
 . 01  temp-a                                        huge
 . 01  temp-b                                        huge
 . 01  shifter                                       huge
 . 01  e                                             huge
 . 01  exponent                                      huge

 .  linkage section
 . 01  a                                             huge
 . 01  b                                             huge
 . 01  c                                             huge
 . 01  input-string
 .     05  input-byte occurs 128 indexed x-in        pic  x(01)

* Compiler insists on this USING. There are no parms to main.
 . PROCEDURE DIVISION using a, b, c, input-string.
     move low-values to typein
     perform until typein equal to spaces
         display 'Enter problem'
         accept typein
         move zeros to x, y, z

         call 'CALCPARS' using x, y, z, typein

         display 'the answer is: ' with no advancing
         call 'DISPC' using x, y, z
     end-perform
     stop run


 . entry 'CALCPARS' using a, b, c, input-string.
     move a to x
     move b to y
     move zeros to a, b, c
     move 1 to sp
     move zeros      to stack-number (1)
     move '+' to stack-operation (1)
     set x-in to 1
     perform one-word until x-in greater than 128
     if  sp not equal to 1
         display 'too many left parens'
         perform do-operation until sp = 1
     end-if
     move stack-number (1) to c

     goback

 . one-word.
     evaluate input-byte (x-in)
         when = '+' or '-' or '*' or '/' or '^' or '!'
             move input-byte (x-in) to stack-operation (sp)
             if  input-byte (x-in) equal to '!'
                 perform do-operation
                 move space to stack-operation (sp)
             end-if
         when '0' thru '9'
         when '.'
             perform pickup-number
             perform process-number
         when '('
             perform bump-sp
             move zeros to stack-number (sp)
             move '+' to stack-operation (sp)
         when ')'
             perform do-operation
         when 'a'
             move x to b
             perform process-number
         when 'b'
             move y to b
             perform process-number
         when space
             continue
         when other
             set i to x-in
             display 'invalid input ' input-byte (x-in) ' col ' i
     end-evaluate
     set x-in up by 1
 . pickup-number.
     move zeros to b
     compute p = length of huge / 2
     perform until (input-byte (x-in) less '0' or greater '9') and
         input-byte (x-in) not equal to '.'
         if  input-byte (x-in) equal to '.'
             compute p = (length of huge / 2) + 1
         else
             if  p equal to (length of huge / 2)
                 call 'CALCSHL' using a, b, c
                 move input-byte (x-in) to a-digit in b (length of huge / 2)
             else
                 move input-byte (x-in) to a-digit in b (p)
                 add 1 to p
             end-if
         end-if
         set x-in up by 1
     end-perform
     set x-in down by 1
 . process-number.
     perform bump-sp
     move b to stack-number (sp)
     perform do-operation
 . do-operation.
     if  debug-mode
         if  stack-operation (sp) not equal to '!'
             perform dec-sp
         end-if
         move stack-number (sp) to c
         perform display-c
         display stack-operation (sp)
         if  stack-operation (sp) not equal to '!'
             perform bump-sp
             move stack-number (sp) to c
             perform display-c
         end-if
     end-if

     move stack-number (sp) to b
     if  stack-operation (sp) not equal to '!'
         perform dec-sp
         move stack-number (sp) to a
     end-if
     evaluate stack-operation (sp)
         when '+'
             call 'CALCADD' using a, b, c
         when '-'
             call 'CALCSUB' using a, b, c
         when '*'
             call 'CALCMUL' using a, b, c
         when '/'
             call 'CALCDIV' using a, b, c
         when '^'
             call 'CALCEXP' using a, b, c
         when '!'
             call 'CALCFAC' using a, b, c
         when other
             move b to c
     end-evaluate
     move c to stack-number (sp)

     if  debug-mode
         display '='
         perform display-c
     end-if
 . bump-sp.
     if  sp less than 10
         add 1 to sp
     else
         display 'stack overflow'
     end-if
 . dec-sp.
     if  sp greater than 1
         subtract 1 from sp
     else
         display 'too many right parens'
     end-if
 . display-c.
     if  a-digit in c (1) equal to 9
         call 'CALCNEG' using a, b, c
         display '-' with no advancing
     end-if
     perform varying i from 1 by 1 until
         a-digit in c (i) not = zero or i > 99
         continue
     end-perform
     perform varying i from i by 1 until i > ((length of huge / 2) + 20) or
         (i equal to ((length of huge / 2) + 1) and
          c((length of huge / 2) + 1:length of huge / 2) equal to zero)
          display a-digit in c (i) with no advancing
          if  i equal to (length of huge / 2)
              display '.' with no advancing
          end-if
     end-perform
     display space
 . end-calcpars


* Begin calchuge.
 . entry 'CALCADD' using a, b, c.
     perform compute-a-plus-b
     goback
 . entry 'CALCSUB' using a, b, c.
     perform compute-a-minus-b
     goback
 . entry 'CALCMUL' using a, b, c.
     perform compute-a-times-b
     goback
 . entry 'CALCDIV' using a, b, c.
     perform compute-a-divided-by-b
     goback
 . entry 'CALCEXP' using a, b, c.
     if  b(1:(length of huge / 2) - 2) equal to zero and
         b((length of huge / 2) + 1:length of huge / 2) equal to zero
         perform compute-a-ipower-b
     else
         perform compute-a-power-b
     end-if
     goback
 . entry 'CALCFAC' using a, b, c.
     perform compute-b-factorial
     goback
 . entry 'CALCNEG' using a, b, c.
     perform flip-sign-c
     goback
 . entry 'CALCSHR' using a, b, c.
     perform shift-b-right
     goback
 . entry 'CALCSHL' using a, b, c.
     perform shift-b-left
     goback
 . entry 'DISPC' using a, b, c.
     perform display-c
     goback

 . compute-a-plus-b.
     move zero to overflow-digit
     if  9 not = a-digit in b (1) and a-digit in a (1)
         move 0 to overflow-digit
         perform add-operation
     else
     if  9 = a-digit in b (1) and a-digit in a (1)
         move 1 to overflow-digit
         perform add-operation
     else
         perform flip-sign-b
         perform compute-a-minus-b
     end-if
 . add-operation.
     perform varying i from length of huge by -1 until i less than 1
         compute temp-s =
             a-digit in a (i) + a-digit in b (i) + overflow-digit
         if  temp-s less than 10
             move temp-s to a-digit in c (i)
             move 0 to overflow-digit
         else
             subtract 10 from temp-s giving a-digit in c (i)
             move 1 to overflow-digit
         end-if
     end-perform

 . compute-a-minus-b.
     move zero to overflow-digit
     if  b greater than a
         move 1 to overflow-digit
     end-if
     perform varying i from length of huge by -1 until i less than 1
         compute temp-s =
             a-digit in a (i) - a-digit in b (i) - overflow-digit
         if  temp-s less than zero
             add 10 to temp-s giving a-digit in c (i)
             move 1 to overflow-digit
         else
             move temp-s to a-digit in c (i)
             move 0 to overflow-digit
         end-if
     end-perform

 . compute-a-times-b.
     perform normalize-sign-in
     move zeros to d
     perform varying i from length of huge by -1 until i less than 1
         if  a-digit in b (i) not equal to zero
             compute k = i + (length of huge / 2)
             perform varying j from length of huge by -1 until j less than 1
                 if  a-digit in a (j) not equal to zero and
                     k not less 1 and not greater length of huge
                     compute two-digits =
                         a-digit in a (j) * a-digit in b (i)
                     perform add-two-digits
                 end-if
                 subtract 1 from k
             end-perform
         end-if
     end-perform
     move d to c
     perform normalize-sign-out

 . compute-a-divided-by-b.
     perform normalize-sign-in
     compute k = length of huge / 2
     perform until b not less than a or k = 1
         perform shift-b-left
         subtract 1 from k
     end-perform
     move zeros to d
     perform until k > length of huge
          perform until b greater than a or b = zeros
              move 1 to two-digits
              perform add-two-digits
              perform compute-a-minus-b
              move c to a
          end-perform
          perform shift-b-right
          add 1 to k
     end-perform
     move d to c
     perform normalize-sign-out


 . compute-a-power-b.
* Computing a^b
     move a to temp-a
     move b to temp-b
     if  a-digit in a (1) equal to 9 or a equal to zero
         move zero to c
         exit paragraph
     end-if
*  Get the exponent by repeatedly dividing by e
     move zero to e, exponent
     move '27182818284590452353602874' to e(length of huge / 2:26)
     perform until temp-a not greater than e
         move temp-a to a
         move e to b
         perform compute-a-divided-by-b
         move c to temp-a
         move exponent to a
         move zero to b
         move 1 to a-digit in b (length of huge / 2)
         perform compute-a-plus-b
         move c to exponent
     end-perform
* Compute base e logarithm of the mantissa
* ln(x) = perform varying t from 1 by 2 until delta = zero or t > 90
*           compute ln = ln + ((2 / t) * (((x - 1) / (x + 1)) ^ t))
* where 0 < x < e
     move temp-a to a
     move zero to b
     move 1 to a-digit in b (length of huge / 2)
     perform compute-a-minus-b
     move c to temp-2
     perform compute-a-plus-b
     move temp-2 to a
     move c to b
     perform compute-a-divided-by-b
     move c to temp-2          *> save (x - 1) / (x + 1)
     move zero to temp-3
     move all '1' to b
     perform varying term from 1 by 2 until
         b(1:(length of huge / 2) + 16) = zero or term > 90 or
         b(1:(length of huge / 2) + 16) = all '9'
         move zero to a, b
         move 2 to a-digit in a (length of huge / 2)
         move term to b((length of huge / 2) - 1:2)
         perform compute-a-divided-by-b
         move c to temp-1
         move temp-2 to a
         move zero to b
         move term to b((length of huge / 2) - 1:2)
         perform compute-a-ipower-b
         move temp-1 to a
         move c to b
         perform compute-a-times-b
         move temp-3 to a
         move c to b
         perform compute-a-plus-b
         move c to temp-3
     end-perform
* Add the exponent giving ln(a)
     move c to a
     move exponent to b
     perform compute-a-plus-b
* Multiply by b
     move c      to a
     move temp-b to b
     perform compute-a-times-b
     move c to temp-a
* e^x =   perform varying t from 1 by 1 until delta = zero or t > 90
*           compute exp = exp + ((x ^ t) / t!)
*         add 1 to exp
* Note that ln(a) will be negative when a < 1. In that case, this is
* an alternating series because n^t will be negative half the time.
     move zero to b
     move 1 to a-digit in b (length of huge / 2)
     move b to temp-3
     perform varying term from 1 by 1 until
         b(1:(length of huge / 2) + 16) = zero or term > 90
         move temp-a to a
         move zero to b
         move term to b((length of huge / 2) - 1:2)
         perform compute-a-ipower-b
         move c to temp-1
         move zero to b
         move term to b((length of huge / 2) - 1:2)
         perform compute-b-factorial
         move temp-1 to a
         move c to b
         perform compute-a-divided-by-b
         move temp-3 to a
         move c to b
         perform compute-a-plus-b
         move c to temp-3
     end-perform
* Discard meaningless digits
     if  c ((length of huge / 2) + 17:(length of huge / 2) - 16)
         not equal to zero
         move c to a
         move zero to b
         move 5 to a-digit in b ((length of huge / 2) + 17)
         perform compute-a-plus-b
         move zero to c((length of huge / 2) + 17:(length of huge / 2) - 16)
     end-if
     if  c((length of huge / 2) + 1:6) equal to zero and
         c(1:(length of huge / 2)) not equal to zero
         move zero to c((length of huge / 2) + 7:(length of huge / 2) - 6)
     end-if

* Integer exponent 1-99
 . compute-a-ipower-b.
     move b((length of huge / 2) - 1:2) to two-digits
     move two-digits to power
     move zeros      to b
     move 1 to a-digit in b (length of huge / 2)
     perform power times
         perform compute-a-times-b
         move c to b
     end-perform
     if  c((length of huge / 2) + 1:10) equal to zero and
         c(1:(length of huge / 2)) not equal to zero
         move zero to c((length of huge / 2) + 11:(length of huge / 2) - 10)
     end-if

 . compute-b-factorial.
     move b((length of huge / 2) - 1:2) to two-digits
     move two-digits to power
     move zeros to a, b
     move 1 to a-digit in a (length of huge / 2),
               a-digit in b (length of huge / 2)
     perform varying factorial from 1 by 1 until factorial > power
         move factorial to two-digits
         move two-digits to b((length of huge / 2) - 1:2)
         perform compute-a-times-b
         move c to a
     end-perform

 . flip-sign-a.
     inspect a converting '0123456789'
                       to '9876543210'
 . flip-sign-b.
     inspect b converting '0123456789'
                       to '9876543210'
 . flip-sign-c.
     inspect c converting '0123456789'
                       to '9876543210'

 . shift-b-right.
     move b(1:length of huge - 1) to shifter(2:length of huge - 1)
     move zero to shifter(1:1)
     move shifter to b
 . shift-b-left.
     move b(2:length of huge - 1) to shifter(1:length of huge - 1)
     move zero to shifter(length of huge:1)
     move shifter to b

 . add-two-digits.
     move k to l
     perform until two-digits = zero or l < 1
         add a-digit in d (l) to two-digits
         move digit-2 to a-digit in d (l)
         move digit-1 to digit-2
         move 0 to digit-1
         subtract 1 from l
     end-perform
 . normalize-sign-in.
     move zero to sign-count
     if  a-digit in a (1) equal to 9
         add 1 to sign-count
         perform flip-sign-a
     end-if
     if  a-digit in b (1) equal to 9
         add 1 to sign-count
         perform flip-sign-b
     end-if
 . normalize-sign-out.
     if  sign-count equal to 1
         perform flip-sign-c
     end-if
 .
```

#### ↳ Re: huge number calculator and library

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-31T19:21:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net>`
- **References:** `<410ae85f.29667620@news.optonline.net>`

```
to: C.L.C. (with a CC)

When the Standards committees were extending the required numeric size from 18
digits to 31 digits a question arose as to whether or not anyone KNEW of any
existing "real-world" applications that actually needed 31-digit numbers.  J4
and WG4 went with 31-digits as that is what the (a?) SQL Standard requires (as I
recall).  However, I don't think I ever heard from any users that they really
needed these larger fields.

I am NOT saying that RW's example code is a problem (and I haven't studied it in
detail).  However, I am curious if any participants in comp.lang.cobol have
found serious business needs for greater than 31-digit numbers - and if so for
what types of applications?

P.S.  I am a little confused by the comment:

> *    Note that everything is relative to the size of 'huge' below.
> *    The program would read better if I could equate
> *    'mid' to 'length of huge / 2'. I couldn't find a way in Cobol 85.

This particular code is a VERY odd (to me) mixture of '85 Standard, '02
Standard, and Micro Focus extension syntax, e.g.

 ENTRY - is an extension
 TYPEDEF - is from the '02 Standard
PROGRAM-ID omitted/commented - is (semi-documented) extension

If I were trying to make this a STANDARD example program (for the '02 Standard -
as it uses TYPEDEF), I might make the following changes that would ((I think)
compile with a current Micro Focus compiler:

A) change ENTRY statements to nested programs
B) Change BINARY fields to BINARY-LONG (or SHORT for PIC S9(02)

and would certainly compile the program with FLAGSTD at least once to see what
other extensions are  in use.  However, (again) none of this says anything about
how useful this would be to someone in a Micro Focus-ONLY environment.
```

##### ↳ ↳ Re: huge number calculator and library

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-08-01T00:20:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410c2b8b.112412260@news.optonline.net>`
- **References:** `<410ae85f.29667620@news.optonline.net> <AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>to: C.L.C. (with a CC)
>
…[3 more quoted lines elided]…
>and WG4 went with 31-digits as that is what the (a?) SQL Standard requires (as
I
>recall).  However, I don't think I ever heard from any users that they really
>needed these larger fields.

I have encountered realistic problems that required more than 18 digits. Whether
they required more than 31 digits, I cannot recall. The variables in question
were intermediate in solving Linear Regression, Roots of a Polynomial, etc.
Businesses use these, but the managers you polled were probably 10 years out of
touch with technical details. They were thinking of widgets and balance sheets
rather than mathematical intermediates. 

The demo was an intellectual exercise. 

>I am NOT saying that RW's example code is a problem (and I haven't studied it
in
>detail).  However, I am curious if any participants in comp.lang.cobol have
>found serious business needs for greater than 31-digit numbers - and if so for
>what types of applications?

I would turn it around to ask whether anyone thinks there should be a limit. If
I say PIC 9(10000), why should the compiler raise an objection? It's my
computer. If I'm wasting time foolishly, its not the compiler's job to point
that out.

>P.S.  I am a little confused by the comment:
>
…[7 more quoted lines elided]…
> ENTRY - is an extension

It wouldn't be callable by outsiders if I'd used nested programs.

> TYPEDEF - is from the '02 Standard

The first version was hardcoded for 200 digits. In searching for a way to
abstract the number of digits, TYPEDEF was the only solution available. If Cobol
'85 had better abstraction facilities, I would have used them.

>PROGRAM-ID omitted/commented - is (semi-documented) extension

Whoops. An accident. It should have not been commented.

>and would certainly compile the program with FLAGSTD at least once to see what
>other extensions are  in use.  However, (again) none of this says anything
about
>how useful this would be to someone in a Micro Focus-ONLY environment.

ENTRY is supported by many other compilers, including IBM. Except for ENTRY, it
is dead-stock Standard Cobol.
```

###### ↳ ↳ ↳ Re: huge number calculator and library

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-08-01T02:03:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410C4F3C.2010209@optonline.net>`
- **In-Reply-To:** `<410c2b8b.112412260@news.optonline.net>`
- **References:** `<410ae85f.29667620@news.optonline.net> <AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net> <410c2b8b.112412260@news.optonline.net>`

```
Regarding size, the problem is an old one. IBM's pre 360 systems had 36 
bit words,
and 72 bit double precision. In meetings I attended hosted by IBM at the 
time of the
release of the 360 the point was made that after a large review of user 
needs, that
big a word was not needed.

I know that we used Matrix software to do what we called the circulation 
of variances.
Steve Wright was the author of the software, and because of the slowness 
of the system
as compared to the size of the problems, some customers ran that package 
for days, or
perhaps weeks. There was a stop, and continue feature in the software. 
That application
for us did not need large numbers. Yet our product code was  in the 
realm of 20 characters
in length. It was a collection of groups and sub groups of product.

At that time, we also had a research lab that used analog computers. We 
were into
machine shop control, simulations, and among other things bridge design. 
There was
a whole group that tried to keep up with the operations needs, and not 
just book
keeping.

While this may not be exactly on topic, I remember that the air frame 
industry's needs
were such that FORTRAN may still be their tool for plane design. Through 
CODASYL
a data base extension was developed for FORTRAN.

Some of our plants had computers dedicated to controlling the making of 
steel.
Now days, the system is down to a very few people and few computers. 
However,
size of numbers in floating point did NOT seem to be an issue with us, 
and IBM at
the 360 announcement in Huston assured us that we would not loose 
precision with
the new shorter word size.

I don't believe there was a problem at the David Taylor Model Basin or 
we would
have heard about it.  Yet, with todays travel to the stars, and the size 
of some
data bases today anything is possible.

Warren Simmons



Robert Wagner wrote:

>"William M. Klein" <wmklein@nospam.netcom.com> wrote:
>
…[101 more quoted lines elided]…
>
```

##### ↳ ↳ Re: huge number calculator and library

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2004-08-01T12:03:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p94qg0t8gk9h1im5o1cjldj5sf2akd3vm3@4ax.com>`
- **References:** `<410ae85f.29667620@news.optonline.net> <AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net>`

```
On Sat, 31 Jul 2004 19:21:04 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> enlightened us:

>to: C.L.C. (with a CC)
>
…[11 more quoted lines elided]…
>

I've seen the need in a mainframe environment for a numeric field
larger than 18 digits but don't think I've come across an application
that needed more than 31.  When I used to program in the international
banking environment, I'd come across currency conversion calculations
that could possibly blow the 18 digit restriction right out of the
water.  One that comes to mind is converting U.S. Dollars to Turkish
Lire.  The exchange rate right now is around 1.5 million (yes million)
lire to a single dollar.  It used to be higher.  There were certain
transactions, because we were dealing with a wholesale bank, where the
restriction did become a problem.  They were rare, but they did
happen.

Frankly, I think if you are doing calculations or such and need a
number over the new 31 digit restriction, you should be doing it in
Fortran (better tool) or one of the many statistic languages
available.

<<snip>>

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


Micro$oft Haiku Error Message #116

Having been erased,
The document you're seeking
Must now be retyped.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: huge number calculator and library

- **From:** "Rufio" <Bran_britain@yahoo.com>
- **Date:** 2004-08-01T11:22:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GwaPc.18341$8G6.10097@fed1read04>`
- **References:** `<410ae85f.29667620@news.optonline.net> <AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net> <p94qg0t8gk9h1im5o1cjldj5sf2akd3vm3@4ax.com>`

```

"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
news:p94qg0t8gk9h1im5o1cjldj5sf2akd3vm3@4ax.com...
> On Sat, 31 Jul 2004 19:21:04 GMT, "William M. Klein"
> <wmklein@nospam.netcom.com> enlightened us:
…[3 more quoted lines elided]…
> >When the Standards committees were extending the required numeric size
from 18
> >digits to 31 digits a question arose as to whether or not anyone KNEW of
any
> >existing "real-world" applications that actually needed 31-digit numbers.
J4
> >and WG4 went with 31-digits as that is what the (a?) SQL Standard
requires (as I
> >recall).  However, I don't think I ever heard from any users that they
really
> >needed these larger fields.
> >
> >I am NOT saying that RW's example code is a problem (and I haven't
studied it in
> >detail).  However, I am curious if any participants in comp.lang.cobol
have
> >found serious business needs for greater than 31-digit numbers - and if
so for
> >what types of applications?
> >
…[12 more quoted lines elided]…
>

Certainly saw the need for 16-18 digits, at a credit card company - but they
used scaling factors most of the time, to limit the size - didn't need
(ultra) large dp accuracy. At an online brokerage, it was all in USD,
otherwise it might have gone to 31+ on currency conversion.

So yes - there's certainly the potential to use (at least?) 31 digits. The
online brokerage is investigating an Oracle API - COBOL programs coded with
calls to the API to DIRECTLY UPDATE/READ Oracle.......real cool. But I don't
guess Fortran can do that yet......or can it ?

But right now, I'm a gentelman of leiusure (that's the employee equivilent
of the contractor term "between contracts"), so my numerical needs are much
less o:)

> Frankly, I think if you are doing calculations or such and need a
> number over the new 31 digit restriction, you should be doing it in
…[21 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: huge number calculator and library

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-08-01T18:29:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9E0KBxLuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<410ae85f.29667620@news.optonline.net> <AiSOc.4320$9Y6.2951@newsread1.news.pas.earthlink.net> <p94qg0t8gk9h1im5o1cjldj5sf2akd3vm3@4ax.com>`

```
.    Am  01.08.04
schrieb  swiegand@neo.rr.NOSPAM.com (SkippyPB)
    auf  /COMP/LANG/COBOL
     in  p94qg0t8gk9h1im5o1cjldj5sf2akd3vm3@4ax.com
  ueber  Re: huge number calculator and library

   re 18 or 31 digits:

s>   One that comes to mind is converting U.S. Dollars to Turkish
s> Lire.  The exchange rate right now is around 1.5 million (yes million)
s> lire to a single dollar.

   This is where the "P" in a numeric PICTURE-Clause comes in handy.

   There are certainly no (current) one-Lira coins or notes in  
circulation.

   Also, think about the exchange rates used for the introduction of  
the EURO -- all rates had 6 significant digits, just the decimal point  
was at different places. Deutsche Mark, French Frank, Netherland's  
Guilder had the decimal point after the first digit, the Irish Pound  
before the very first digit, and the Italian Lira had the decimal  
point between the fourth and fifth digit.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Ohne Pressefreiheit, Vereins- und Versammlungsrecht ist keine
Arbeiterbewegung mï¿½glich"        - Friedrich Engels      (Februar 1865)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
