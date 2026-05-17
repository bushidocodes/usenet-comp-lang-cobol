[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# N! in Cobol

_7 messages · 6 participants · 1996-04_

---

### N! in Cobol

- **From:** "10006..." <ua-author-12404258@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`

```
% compthe3.tex 16-4-1996 (9h:6)

+---------------------------------------+
| Philippe Esperet (France) |
| email : 100··.@com··e.com |
+---------------------------------------+

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ref : n! in Cobol

In an introduction to a small course on recursivity, I
should like to begin with a list of "recursive n!" in
different languages (from APL to TeX). I am a mathematician
and I do not know a single word of Cobol. Could somebody
translate for me the :

let rec fact=fun
| 0 -> 1
| n -> n*fact(n-1);;

or

int fact(int n)
{return n==0 ? 1 : n*fact(n-1);}

Thank you if you can help.
Best regards
```

#### ↳ Re: N! in Cobol

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`

```
Esperet wrote:
› 
 
›    In an introduction to a small course on recursivity, I
› should like to begin with a list of "recursive n!" in
…[7 more quoted lines elided]…
› 

Can't be done in standard COBOL, but there is a MF COBOL extension,
local-storage that does the business, so the following works. COBOL
gives the size of the max returned value as 18 digits, I wonder where
your examples will fail?

program-id. dummy.
working-storage section.
01 n pic 9(6) value 3.
01 result pic 9(18).
procedure division.
call "fact" using n result
display "Factorial " n " is " result
stop run
.
end program dummy.

program-id. fact.
local-storage section.
01 n-1 pic 9(6).
linkage section.
01 n pic 9(6).
01 result pic 9(18).
procedure division using n result.
if n = 0
move 1 to result
else
subtract 1 from n giving n-1
call "fact" using n-1 result
multiply n by result
end-if
exit program
.

Martyn      (m.··.@mfl··o.uk)
Phone: +44 (0)1635 565 358, fax +44 (0)1635 565 567
```

#### ↳ Re: N! in Cobol

- **From:** "truh..." <ua-author-17086349@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`

```
In article <4kvdas$o37$1.··.@mha··e.com>, Esperet <100··.@Com··e.COM> writes:
› %  compthe3.tex 16-4-1996 (9h:6)
› 
…[27 more quoted lines elided]…
›  


How about this one. Haven't been programming in Cobol for quite a while, but
here goes.

Maybe I should have used capital letters, but quite a few compilers considers
small letters equivalent to CAPITAL letters. And I don't wish to shout.

This program is not tested, so there might be some things to correct.
Please feel free to correct them, if noticed.

factorial module:
-----------------
identification division.
program id. fact.
* computes factorial of any number.
* well, on overflow (and with negative values) it returns zero.
*author. veli-matti truhponen.
environment division.
data division.
working-storage section.
01 f-counter pic s9(18) comp.
linkage section.
01 factorial pic s9(18) comp.
* I hope 18 digits is enough (or not too much)
procedure division using factorial.
begin-here section.
compute f-counter = factorial - 1
on overflow move -1 to factorial f-counter.
* perform (factorial - 1) or zero times
perform with test before until (f-counter <= 0)
compute factorial = factorial * f-counter
on overflow move 0 to factorial f-counter
compute f-counter = f-counter - 1
end-perform.
* factorial of zero is 1
if (factorial = 0) move 1 to factorial end-if.
* factorial of negative numbers cannot be computed, returning
* zero to calling program.
if (factorial < 0) move 0 to factorial end-if.
return-to-calling-program section.
exit program.
* stop run.
* I always put stop run after exit program. Just in case ;)

calling factorial module (from cobol):
--------------------------------------
identification division.
program-id. callfact.
* demonstrates calling of fact -program.
*author. veli-matti truhponen.
environment division.
data division.
working-storage section.
01 field1 pic s9(18) comp.
01 field2 pic z(17)9+.
01 field3 pic z(17)9+.
procedure division.
begin-here section.
move 0 to field1.
perform try-factorial.

move 10 to field1.
perform try-factorial.

move -9 to field1.
perform try-factorial.
stop-here section.
stop run.

try-factorial section.
move field1 to field2.
call 'fact' using field1.
move field1 to field3.
if (field1 > 0)
display 'factorial of ' field2 ' is ' field3
else
display 'cannot compute factorial of ' field2
end-if.
try-factorial-ex section.

would produce something like (when working correctly ;)
-----------------------------
factorial of 0 is 1+
factorial of 10 is 3628800+
cannot compute factorial of 9-



regards,
Vellu

(former cobol programmer)
v.··.@meg··d.fi
veli-mat··.@ntc··a.com
```

##### ↳ ↳ Re: N! in Cobol

- **From:** "truh..." <ua-author-17086349@usenetarchives.gap>
- **Date:** 1996-04-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7be0f3bcf1-p3@usenetarchives.gap>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com> <gap-7be0f3bcf1-p3@usenetarchives.gap>`

```
› Major problem here:  this is NOT recursive, but iterative.
› A recursive procedure calls itself.  This is a simple loop.
…[6 more quoted lines elided]…
› 

Sorry, didn't read the specs well enough to see that HOW was more important
than WHAT. Apologies.

And, I looked my program again, and it doesn't work with negative numbers
as I planned. But hey, I'm not perfect ,-)

Vellu (no, I don't have an eye patch, my semicolon did not work)

- Once I thought I made a mistake, but I was wrong
```

#### ↳ Re: N! in Cobol

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`

```
Esperet (100··.@Com··e.COM) wrote:
: ref : n! in Cobol
: In an introduction to a small course on recursivity, I
: should like to begin with a list of "recursive n!" in
: different languages (from APL to TeX). I am a mathematician
: and I do not know a single word of Cobol. Could somebody
: translate for me the :

: let rec fact=fun
: | 0 -> 1
: | n -> n*fact(n-1);;

...

It is unfortunate that you imagine this problem to be a
decent example of recursive behaviour. If any programmer
used recursion to compute a factorial, I would fire him/her.
This is the type of problem you solve with a simple loop,
in any language, from APL to TeX, passing through COBOL
and such.

Now, take a look at QuickSort, which is by nature a recursive
algorithm. *This* teaches you something. n! and the towers
of hanoi just teach trivia.

---
Pieter Hintjens,
whose opinions can be a bit strong at times.
```

##### ↳ ↳ Re: N! in Cobol

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-04-16T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7be0f3bcf1-p5@usenetarchives.gap>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com> <gap-7be0f3bcf1-p5@usenetarchives.gap>`

```
In <4l0rh7$k.··.@new··U.net>, pah··.@eu··t.be (Pieter Hintjens) writes:
› Esperet (100··.@Com··e.COM) wrote:
› : ref :  n! in Cobol
…[25 more quoted lines elided]…
› whose opinions can be a bit strong at times.

Hear, hear.
Pieter, Why don't you send him our ETK version of QuickSort
in Cobol? Maybe post it on the net?
```

#### ↳ Re: N! in Cobol

- **From:** "mike giaquinto" <ua-author-13690527@usenetarchives.gap>
- **Date:** 1996-04-18T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7be0f3bcf1-p7@usenetarchives.gap>`
- **In-Reply-To:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`
- **References:** `<4kvdas$o37$1@mhafn.production.compuserve.com>`

```
dlm··.@iqu··t.net (Doug Miller) wrote:
› Esperet <100··.@Com··e.COM> wrote:
›› ref :  n! in Cobol
…[25 more quoted lines elided]…
› 

Does the above code work? In the past I've attempted the above and it has not worked for me
(using an IBM mainframe compiler). The problem is that COBOL does not stack the return
address (there is only one branch at the end of compute-factorial). When the first perform
is invoked, the branch is set to return to the instruction after the fist perform. When the
second perform (recursive) is invoked, it resets the one and only branch to the instruction
after the end-if. When the recursion is over, there is no "unstacking" and the code will
fall through to the paragraph following compute-factorial.

If your compiler is working as I suspect, you could modify it as follows:

n = 3
factorial = 1
PERFORM compute-factorial thru exit-0
display 'factorial = ' factorial
goback.
.
compute-factorial.
IF n > 1
COMPUTE factorial = factorial * n
SUBTRACT 1 FROM n
PERFORM compute-factorial thru exit-n
ELSE
GO TO exit-0
END-IF.

exit-n. exit.
exit-0. exit.

I don't normally use GO TO or EXITs as I'm a strong believer in structured programming,
however this was the only way I found to "fool" the compiler.

I have not tested this code so if it doesn't work, sorry!!!

Mike Giaquinto
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
