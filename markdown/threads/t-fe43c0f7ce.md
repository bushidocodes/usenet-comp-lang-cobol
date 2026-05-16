[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Labels .. Pros and Cons

_40 messages · 20 participants · 1999-04 → 1999-05_

---

### Re: Labels .. Pros and Cons

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<OAJUXPqj#GA.312@ntdwwaaw.compuserve.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan>`

```
Impossible? No. Learning structured programming is like learning a new
language, you have to think in that language, you have to think structured.
Unstructured programmers are thinking in terms of where to go to do what
needs to be done, structured programmers are thinking directly in terms of
what needs to be done, it's really much simpler once you get the hang of
it. A large part of the key is modularity and top-down design and coding.

Top-down does NOT mean that the entire program flows from the top to the
bottom of the huge listing or source file. It means that it's designed in
conceptual levels from top to bottom, e.g. first express the program in the
most general terms (using appropriate structures of course), then each of
the very general pseudo-statements becomes (at least conceptually) an
invocation of a more detailed procedure which is defined separately, each
procedure is further broken down recursively until the whole program is
coded as a modular set of nicely structured procedures.

Most languages now provide Break's or other means of helping to avoid
GOTO's, even when they don't, I never use GOTO's in code I get to write
from scratch. Even the OLD Cobol before Cobol II, which didn't have End-If
and the period killed all your If's, had just barely enough support for
structured programming that you could write an entire old Cobol program
with NO GOTO's. Modern structured extensions just make it that much easier.
Pascal of course was designed structured to begin with. So if a structured
programming fanatic like myself can write pure GOTO-less code even in OLD
Cobol, surely you can learn to do it in Pascal. Good luck. It's worth it.

Oh, if you want a really severe example, try Lisp. It's been years since I
had Lisp in school and I never really used it; although there are some GOTO
type of things (which I don't like), everything is basically sort of like a
function call, if's and case's were handled by a function call to a special
function that worked like a case expression, and there's not even a while
statement; all looping was done entirely by recursion. Maybe inefficient
but it sure imposes discipline on your programming approach! If you could
learn to program like that, then regular structured programming in any
language would be a breeze.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


fmb wrote in message <01be8b0a$09868fe0$LocalHost@bunyan>...

if I had not been able to use the goto command
>writing it would have been impossible.
```

#### ↳ Re: Labels .. Pros and Cons

- **From:** Richard Maine <maine@altair.dfrc.nasa.gov>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com>`

```
"Robert M. Pritchett" <NewsCSIbus@rmpcp.com> writes:

> A large part of the key is modularity and top-down design and coding.
  etc.

Yep.  Good stuff.  Agree, etc.

> Most languages now provide Break's or other means of helping to avoid
> GOTO's, ...
> Pascal of course was designed structured to begin with. So if a structured
> programming fanatic like myself can write pure GOTO-less code even in OLD
> Cobol, surely you can learn to do it in Pascal.

Of course, some of my favorite examples of (what I consider to be) bad
code structure come from Pascal.  I'm (also) a big fan of structured code.
Its just that I don't make the identification that you have good
structure if and only if you have no goto's.  Someone who's name I
forget once said (approximately - I paraphrase, having forgotten the
exact words) that a sufficiently obstinate programmer can write
spaghetti code in any language and with any set of constructs.
Good structure cannot be boiled down to a set of statements to use.

My favorite (and certainly not original to me, but its one I see a lot)
"Pascalism" is how to code something where you need an exit from the
middle of a loop (the F90 exit statement is great for the purpose).
You often see a strange abomination done with little reason that I can
ascertain except  to force the code into a preconcieved notion that
good structure means using "do while".

You rotate the code around in the loop so that the exit condition is
at the top, where the "do while" needs it.  Then, before the loop
you add a second copy of the first part of the code to patch things
up so that the loop will work when messed up like that.  (Yes,
very prejudicial wording on my part).  Giving something like

    [extra copy of first part of loop body]
    do while [inverse of the exit condition]
       [second part of loop body]
       [first part of loop body]
    end

You see this a lot in things like processing data from file of
unknown length.  In that case, the 2 parts in their "natural" order
are "read some data from the file" and "process the data you just read".
The exit condition is when there is no more data in the file, which
you typically don't discover until after you try to read it.  For that
kind of case, the above proto-code looks like

   [read some data from the file]
   do while [did not hit an end of file]
     [process the data read in the previous loop cycle]
     [read some more data from the file
   end

I cannot by any stretch of the imagination consider this to be
naturally structured.  This certainly doesn't match how "I" think
of the problem.  I think of a loop that involves reading data,
then processing the data just read.  The only way I'd ever
come up with something like that is by saying "here's what
I need to get done - now how can I contort it to fit this set
of allowed constructs".

The business about having to have 2 copies of the "read some data"
code is a huge red flag of bad structure.  That violates one of the
major principles of good coding - don't write the same thing twice,
particularly if it is important that the 2 parts match.  And
again, I can't imagine any "natural" mental model that starts out with
2 copies of the same stuff.

The above construct is so common that Pascal contorts its notion of
input in order to accomodate it.  (A get doesn't read data from a file
and return that data - instead it returns data from its buffer and
then pre-fetches data for the next read).  This contortion has spawned
a series of hacks to work around its unsuitability to some
applications.  Look into the term "lazy i/o", for example.

But the contortion falls apart anyway when the data input
isn't done by the twisted "get" construct - for example if the
data is input by calling some 3rd party library procedure.
You end up thrown back to the above loop construct with the
loop written "backwards" and part of its code duplicated.
....either that or you go look up how to use a goto in Pascal.
It is possible, although some variants might disallow it, and
it always seemed to me that the language went out of its way
to make the goto awkward.

As is probably evident from the above tirade, I personally don't
consider Pascal well suited to structured coding at all.  Yes,
its possible to code anything in Pascal - I've done a fair amount
of it in my time.  Its even possible to code Pascal in a well-structured
manner; but the language doesn't do what I consider a good job of
encouraging/supporting good code structure -  and I'm not so sure
that much of my own Pascal code was well structured; there were just
too many times that I "gave in" and wrote garbled code because that
was easier than writing it well.

F90/f95 supports the above kind of problem excellently (in my opinion).
It turns into

  data_loop: do
    [read some data]
    if ([hit an end of file]) exit data_loop
    [process the data]
  end do data_loop

I consider that good structure.  Also happens that it doesn't use goto's.

But my main thesis is that the number of goto's is not a plausible
"metric" of good structure.  It is sometimes a reasonable first
approximation, but like so many "metrics", when people go overboard
and chase the metric, it can become counter-productive.  I have seen
people take well-structured code and turn it into spaghetti in the
name of "structured coding", by which they meant nothing more and
nothing less than getting rid of goto's.

Perhaps appropriate to mention again the Fortran compiler (hi, Bob)
that actually implemented the "comefrom" statement as a joke, thus
allowing people to write "well-structured" code by the simple expedient
of replacing all the goto's by corresponding comefroms.

P.S. The above is admitedly highly opinionated.  I threw in my
opinions on it.  But I won't argue about it.
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<3724B946.10355A2B@NOSPAMhome.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
Richard Maine wrote:
>    [read some data from the file]
>    do while [did not hit an end of file]
…[5 more quoted lines elided]…
> naturally structured. 

But it is extremely common in COBOL, and IMHO, better than having a GO
TO exit in the perform paragraph.  It also has an advantage in that it
can be written without saving switches, if you have some type of
integrated file-status switch showing end-of-data.  (the file might be a
database).

Certainly the "fix", replacing the read with PERFORM 9999-READ-ROUTINE
does nothing useful.

I haven't seen maintenance problems with this logic, and I have seen
lots of maintenance problems caused by GO TO exit.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** kaz@ashi.FootPrints.net (Kaz Kylheku)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<slrn7i9gvq.iir.kaz@ashi.FootPrints.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3724B946.10355A2B@NOSPAMhome.com>`

```
On Mon, 26 Apr 1999 13:06:46 -0600, Howard Brazee <brazee@NOSPAMhome.com> wrote:
>Richard Maine wrote:
>>    [read some data from the file]
…[12 more quoted lines elided]…
>database).

It's also the C++ STL way for iterating containers:

	iter = container.begin();

	while (iter != container.end()) {
		// process element indexed by iter
		iter++;
	}

which can be condensed into:

	for (iter = container.begin(); iter != container.end(); iter++) {
		//
	}

When processing a sequence, fetching the first item is a special case that
is different from fetching the next item. Therefore it requires different
logic.  This is evident even in simple loops that increment an integer:

	i = 0;	/* get first value of i */

	while (i < N) {
		/* process value of i set in previous increment */
		i++;	/* get next value of i */
	}

The reasons that we use this logic in these circumstances is that firstly, the
increment step is independent from data retrieval. That is, I can use the value
pointed at by the iterator without causing that iterator to automatically
increment. Secondly, the increment step never fails. To ensure this, we reserve
a special value that the iterator can take on if it is incremented after the
last iteration; the value container.end() or the value N in the case of the
integer loop.

In the case of file input, we do not have these two conditions. 
The iteration variable is the file position indicator. It is initialized
when the file is opened or reset to the beginning. And it is incremented
when data is fetched. The acts of fetching data and the incrementing of
the position indicator are inseparable. Furthermore, this operation
can fail, unlike the increment of iter or i in the above two loops.

Therefore, a different structure makes more sense:

	/* open file (position marker = 0) */

	for (;;) {
		/* fetch data, (position_marker += X, if successful) */

		if (/* error test */)
			break;

		/* process data */
	}

There is no point in doing the data read in two places unless you are using
some crippled programming language that doesn't have structured breaks.

Furthermore, you may be able to test the result of the fetching operation
in the loop guard, resulting in something patterned after the widely
used idiom:

	while ((ch = getchar()) != EOF) {
		/* process ch */	
	}
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** kargl@troutmask.apl.washington.edu (Steven G. Kargl)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g2f38$vto$1@nntp6.u.washington.edu>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
In article <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>,
	Richard Maine <maine@altair.dfrc.nasa.gov> writes:

[some good stuf delete]

> You rotate the code around in the loop so that the exit condition is
> at the top, where the "do while" needs it.  Then, before the loop
…[8 more quoted lines elided]…
>     end

[some other good stuff deleted]

> 
> F90/f95 supports the above kind of problem excellently (in my opinion).
…[6 more quoted lines elided]…
>   end do data_loop

Of the two pseudo-snippets given, which will a good optimizing
parallel compiler probably have problems?  The "do while"
loop (without actually looking at assembly) intuitively seems
to provide a compiler a better chance to optimize the loop
body.  The "do" loop with the "if" statement would cause problems.
In fact, when I'm given code to use that has poor preformance,
one of the first things I do is check that nested loops reference
array indices in the correct order, and eliminate conditionals 
inside loops.

> I consider that good structure.  Also happens that it doesn't use goto's.
> 
…[6 more quoted lines elided]…
> nothing less than getting rid of goto's.

IIRC, Knuth (of TeX fame and assort other things :) has some essay
on the zealous nature of getting rid of GOTOs.

PS:  I can't believe I responding to one of Richard's post.  I tend
    to agree with him on most matters involving Fortran.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** "James Giles" <jamesgiles@worldnet.att.net>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g2ni2$pma$1@bgtnsc02.worldnet.att.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g2f38$vto$1@nntp6.u.washington.edu>`

```

Steven G. Kargl wrote in message <7g2f38$vto$1@nntp6.u.washington.edu>...
>In article <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>,
> Richard Maine <maine@altair.dfrc.nasa.gov> writes:
…[31 more quoted lines elided]…
>body.  The "do" loop with the "if" statement would cause problems.

Actually, many optimizers will turn both into the same thing internally.
For one thing, a "while" loop is often turned into an "until" loop by the
compiler.  The "while" loop

   do while (condition)
    ...
   end while

The compiler might turn this naively into

   on(not(condition)) jump end
start:
    ...
   jump start
end:

It's more efficient for the compiler to generate:

   jump test
start:
    ...
test:
   on(condition) jump start

This leaves only one conditional jump in the loop rather than a
conditional jump and an unconditional one.

As long as it's doing that kind of rearrangement, it can also recognoze
the loop-and-a-half case with the middle exit (which is a common thing)
and rearrange the second of Richard Maine's examples into the first.  Then, all
optimizations on the first are applicable to the second.  Since the middle
exit is easier for (most) people to read and maintain, it has to be regarded
as superior as long as the compiler is smart enought to still optimize it.

>
>> I consider that good structure.  Also happens that it doesn't use goto's.
…[10 more quoted lines elided]…
>on the zealous nature of getting rid of GOTOs.

Structured Programming with GOTO Statements, D. E. Knuth, Computing
Surveys, December 1974, pp. 261-301.  Also widely reprinted.  For example,
in Tutorial: Programming Language Design, A. Wasserman Ed., IEEE Computer
Society Press, 1980; or in Current Trends in Programming Methodology, vol. I,
R. Yeh Ed., Prentice-Hall, 1977.  In this paper he discusses (among other things)
the desirability of having some explicit syntax for loop-and-a-half situations.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Richard Maine <maine@altair.dfrc.nasa.gov>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<ued80rulqh.fsf@altair.dfrc.nasa.gov>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g2f38$vto$1@nntp6.u.washington.edu>`

```
kargl@troutmask.apl.washington.edu (Steven G. Kargl) writes:

> Of the two pseudo-snippets given, which will a good optimizing
> parallel compiler probably have problems?  The "do while"
> loop....
> The "do" loop with the "if" statement..

I'm not enough of a compiler optimization expert to say with any
degree of certainty.

> IIRC, Knuth (of TeX fame and assort other things :) has some essay
> on the zealous nature of getting rid of GOTOs.

Might have been a Knuth essay that I was recalling.  Its at least
believable.  He's someone who's opinions I tend to respect...
no lets rephrase that.  I always respect them, and I tend to agree
with them.

> PS:  I can't believe I responding to one of Richard's post.  I tend
>     to agree with him on most matters involving Fortran.

I didn't see any disagreement above.  You asked whether (in my words)
there might be a performance penalty in the style I suggested.  Legitimate
question.  For all I know the answer might even be "yes".

If the answer is "yes", then I get to repeat some common advice
relating to performance.  Again, certainly not original to me.

1. Consider whether it matters.  Some places performance will
   matter.  Other places it won't.  If performance doesn't matter
   for the loop in question, then code it for clarity.  This will
   be the case many places, even in programs where performance
   is critical, if the loop in question isn't in the critical area.

2. Where it matters, do whatever it takes.  If what it takes is
   something obscure or tricky, non-structured, or whatever, then make
   sure you document it particularly well.  If you've paid attention
   to point 1, then this will probably be a pretty small part of the
   code.

3. Test to make sure the performance is as expected.  And expect
   surprises.  That's why you test.
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Victor Eijkhout <eijkhout@nala.cs.utk.edu>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<omso9n13yk.fsf@nala.cs.utk.edu>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
Richard Maine <maine@altair.dfrc.nasa.gov> writes:

> My favorite (and certainly not original to me, but its one I see a lot)
> "Pascalism" is how to code something where you need an exit from the
> middle of a loop (the F90 exit statement is great for the purpose).

[...]

>    [read some data from the file]
>    do while [did not hit an end of file]
>      [process the data read in the previous loop cycle]
>      [read some more data from the file
>    end

In Pascal that's just as hard to express, not? In Algol68 you 
would write

    do while 
         begin read(item); item-satisfies-condition; end
      process item
    end

In my Pascal days I would implement this by

    do while read-item-satisfies-condition(item)
      process item
    end

where 'read-item-&c' was a boolean function.

I know that some people object to functions that also return arguments,
but I don't see the problem.

> I cannot by any stretch of the imagination consider this to be
> naturally structured.

My solution is a slight abuse of a function call, but I'm basically
emulating the algol solution. Which I guess is also not really
the most natural one. I agree that the EXIT statement is pretty natural.
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** ronkanen@cc.helsinki.fi (Osmo Ronkanen)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g4pfr$o0q@kruuna.Helsinki.FI>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
In article <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>,
Richard Maine  <maine@altair.dfrc.nasa.gov> wrote:
>
>You rotate the code around in the loop so that the exit condition is
…[9 more quoted lines elided]…
>    end


Yes, I hate this kind of code.
...
>
>F90/f95 supports the above kind of problem excellently (in my opinion).
…[7 more quoted lines elided]…
>

This can be done with break in TP 7.0. However, sometimes I would like a
break out of two levels. If that exit test in itself required a loop
then break would break only out of that loop. This is one case where I
use goto.

That is there is for example:

repeat..
  ...
  for i:=1 to n do if a[i]=x then break two levels;
  ...
until false;

Now one could use a flag:

flag:=false;
repeat
 ...
 for i:=1 to n do if a[i]=x then begin flag:=true; break; end;
 if flag then break;
 ...
End;


But IMO that is uglier than direct goto:

repeat
  ...
  for i:=1 to n do if a[i]=x then goto break_repeat;
  ...
until false;

break_repeat:

Sometimes I also use goto when I convert TP 7.0 code to earlier
versions. IMO it does not make sense to use $IFDEF so that one uses
break with 7.0 and goto with earlier versions.

Osmo
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Richard Maine <maine@altair.dfrc.nasa.gov>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<ueaevuvtuy.fsf@altair.dfrc.nasa.gov>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g4pfr$o0q@kruuna.Helsinki.FI>`

```
ronkanen@cc.helsinki.fi (Osmo Ronkanen) writes:
> In article <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>,
> Richard Maine  <maine@altair.dfrc.nasa.gov> wrote:
…[13 more quoted lines elided]…
> use goto.

In f90/f95, the label on the loop allows you to do that.  The label is
the data_loop in the above pseudo-code, but that part of the syntax is
real f90 instead of pseudo.  If you use the label on the exit/cycle,
it will exit/cycle the specified loop regardless of how many levels
up it might be.

It isn't mandatory in the standard to label loops, but my personal
style mandates it in several cases, including any loop that has a
cycle or exit in it.

In f77, where there was neither exit, cycle, or labelled loops, I also
used goto for this kind of construct.

P.S. I see this thread is xposted to several newsgroups.  A bit hard to
pick which ones are relevant to particular postings, but some of
the general principles do seem to go across multiple of the languages,
so I guess I'll keep all the newsgroups in this followup.
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<#rrtF4Sk#GA.310@nih2naac.compuserve.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
The fix for this loop problem with the pascal loop is the generalized loop
structure with the exit(s) in the middle, as I suggested elsewhere, and
would be cleaner than an exit which has to be stuck within an If within the
loop.

Structured programs can be written with goto's, it's just much harder to
ensure that they are and especially remain structured.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Richard Maine wrote in message ...

>My favorite (and certainly not original to me, but its one I see a lot)
>"Pascalism" is how to code something where you need an exit from the
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Clive Page <cgp@nospam.le.ac.uk>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g3ts7$qg1@owl.le.ac.uk>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
In article <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>,
Richard Maine  <maine@altair.dfrc.nasa.gov> wrote:
>
>Perhaps appropriate to mention again the Fortran compiler (hi, Bob)
>that actually implemented the "comefrom" statement as a joke, thus
>allowing people to write "well-structured" code by the simple expedient
>of replacing all the goto's by corresponding comefroms.

Richard

I've read and enjoyed the "COME FROM" paper, and heard rumours of an actual
implementation: can you reveal the secret of who did it?

By the way, I agree with all that you say about the deviousness needed to
code in Pascal.  I once had to write a lot of code in Forth, a language
which simply doesn't have labels.  Horrible contortions were needed to
handle exceptions and aborts when a jump would have made the code much
neater and easier to understand.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Richard Maine <maine@altair.dfrc.nasa.gov>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<ueg15mw1t8.fsf@altair.dfrc.nasa.gov>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g3ts7$qg1@owl.le.ac.uk>`

```
Clive Page <cgp@nospam.le.ac.uk> writes:

> I've read and enjoyed the "COME FROM" paper, and heard rumours of an actual
> implementation: can you reveal the secret of who did it?

It was implemented in the Elxsi Fortran compiler, sometime in the late
'80s.  Bob Corbett was then working for Elxsi (he currently works for
Sun and posts here occasionally).  I recall that Bob suggested,
without saying what I'd find, that I use the debugger to peruse an
area of the compiler executable.  Turned out to be an area with
strings with the names of a lot of familliar-looking Fortran
statements.  The string "comefrom" appeared there.

I can verify first-hand that it worked because I wrote a trivial
program to test it, making the obvious guess of its syntax and
meaning.  It was, of course, undocumented, and I hadn't actually read
the paper at the time.  Rumor has it that it was removed from the
compiler after someone (not me) submitted a bug report about comefrom
loops not optimizing as well as goto loops.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 4)_

- **From:** patchkov@acs1.acs.ucalgary.ca (Serguei Patchkovskii)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g586a$9lg@ds2.acs.ucalgary.ca>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g3ts7$qg1@owl.le.ac.uk> <ueg15mw1t8.fsf@altair.dfrc.nasa.gov>`

```
Richard Maine (maine@altair.dfrc.nasa.gov) wrote:
: It was implemented in the Elxsi Fortran compiler, sometime in the late
: '80s.  Bob Corbett was then working for Elxsi (he currently works for
: Sun and posts here occasionally).  I recall that Bob suggested,
: without saying what I'd find, that I use the debugger to peruse an
: area of the compiler executable.  Turned out to be an area with
: strings with the names of a lot of familliar-looking Fortran
: statements.  The string "comefrom" appeared there.

At least one of the versions of the Fortran compiler (Level F?) on 
IBM System/360 had (a fully documented) 'ON label' statement, which 
acted in the same way. Really handy for debugging, expecially so if
changing your source code requires using batch editor reading its
input from punched cards...

/Serge.P
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 4)_

- **From:** corbett@lupa.eng.sun.com (Robert Corbett)
- **Date:** 1999-04-28T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g5ue9$p0t$1@engnews1.eng.sun.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g3ts7$qg1@owl.le.ac.uk> <ueg15mw1t8.fsf@altair.dfrc.nasa.gov>`

```
In article <ueg15mw1t8.fsf@altair.dfrc.nasa.gov>,
Richard Maine  <maine@altair.dfrc.nasa.gov> wrote:
>Clive Page <cgp@nospam.le.ac.uk> writes:
>
…[20 more quoted lines elided]…
>maine@altair.dfrc.nasa.gov

Yes, ELXSI Fortran implemented both the COME FROM and the conditional
COME FROM statement.  They were implemented by Ralph Merkle of trapdoor
knapsack and nanotech fame.  I don't recall that the COME FROM statement
was ever deleted, although ELXSI Fortran effectively has been.

					Sincerely,
					Bob Corbett
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** "Ing. Franz Glaser" <meg-glaser@eunet.at>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<37259296.10396EB3@eunet.at>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <7g3ts7$qg1@owl.le.ac.uk>`

```
Clive Page wrote:

> I've read and enjoyed the "COME FROM" paper, and heard rumours of an actual
> implementation: can you reveal the secret of who did it?
…[5 more quoted lines elided]…
> neater and easier to understand.

I program with FORTH most of my business programming. I never heared of
this problem. Whenever an exit is necessary, it is performed with QUIT
or one of the ?" text" exits.
I have to make lots of background procedures with FORTH that are invoked
by an hardware event. Here the QUIT is impossible obviously, but FORTH
is extendable, its principle is the customization of the COMPILER, so
this can be handled flawlessly without any JUMP.

Sorry, what do blind people talk about colours painted by van Gogh.

Franz Glaser
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<3725BFC4.5205DB2E@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
Richard Maine wrote:
> 
snipping....

> 
>    [read some data from the file]
…[3 more quoted lines elided]…
>    end

more snipping....
> 
> I cannot by any stretch of the imagination consider this to be
…[9 more quoted lines elided]…
> 
more snipping..

First lets do this without the goto:

perform until EOF
   READ X
     AT END
        SET EOF TO TRUE
     NOT AT END
        Do all sort of stuff.
   END-READ
end-perform

No goto's and your likeable structure.  (Love this group take a
bow whoever taught me this one...)


Ok now lets take your original comments and extend it into a
multiple loop environment.  A mail report with initializations for
each state, totals for each state, initialization for each
postcode (zipcode) and totals for each postcode, one record per
mail piece.  I have done this in both C and Cobol.

the way I like is:

read
initialize grand total
perform until not eof
   initialize state stuff
   perform until not eof or change of state
      initialize postcode
      perform until not eof or change of postcode or change of
state
         tally for postcode ....
         read
      end-perform
      print postcode total
   end-perform
   print state total
end-perform
print grand total

Add some heading and footing logic and away you go.

I challenge you to rewrite this in the other style.

I prefer this, I would agree that it is not entirely natural in
the first place but once you use 'priming read' and realize code
naturally falls out of it then you too will be converted.  I have
used it since I learned pascal 20 years ago.

Ken
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<bLnV2.4020$B55.313802@dfiatx1-snr1>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au>`

```
Note that the way your loops are written will depend a lot on whether or not
you can detect EOF *before* the actual read.

While you can do this with BASIC sequential files, you only get EOF on a
file opened BINARY in BASIC *after* an unsuccessful read. In COBOL, you must
always get an unsuccessful read to detect EOF. Not sure about other
languages, but a factor, for sure.

MCM

Ken Foskey wrote in message <3725BFC4.5205DB2E@zip.com.au>...
>Richard Maine wrote:
>>
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 4)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-28T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<37276129.FC7BA170@IMN.nl>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1>`

```
Michael Mattias wrote:

> Note that the way your loops are written will depend a lot on whether or not
> you can detect EOF *before* the actual read.
…[4 more quoted lines elided]…
> languages, but a factor, for sure.

VERY VERY TRUE. The essence of my other reply.

>
>
> MCM

The Frog
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<3728DD58.D5770059@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1>`

```
Michael

I still challenge you to write the deep looping structure of a
multiple totals with breaks.

Ken
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 5)_

- **From:** monkey@duke.infowave.net (Scratch Monkey)
- **Date:** 1999-04-29T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<7gaor3$eo1$3@remarQ.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au>`

```
On Fri, 30 Apr 1999 08:29:44 +1000, Ken Foskey <waratah@zip.com.au> wrote:
>Michael
>
…[3 more quoted lines elided]…
>Ken

You mean *without* breaks, no? Otherwise...

	void any_loop_will_do()
	{
		int for_real = 1;

		/* ... */

		while (condition()) {
			/* ... */

			for_real = 0;
			break;	/* There is my break */
		just_kidding:
			for_real = 1;

			/* ... */
		}

		if (!for_real)
			goto just_kidding;

		/* ... */
	}
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-29T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<3728e366.72458097@news1.ibm.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au>`

```
On Fri, 30 Apr 1999 08:29:44 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>Michael
>
>I still challenge you to write the deep looping structure of a
>multiple totals with breaks.
>

I missed part of this thread.  Ken, under what conditions are you
talking?  Thanks!
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<3729AF61.C2CB9CA6@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On Fri, 30 Apr 1999 08:29:44 +1000, Ken Foskey <waratah@zip.com.au>
…[9 more quoted lines elided]…
> talking?  Thanks!

I wrote the psuedo code like the following,  The challenge is to
write this in clear concide code with something other than priming
read.

read
initialize grand total
perform until not eof
   initialize state stuff
   perform until not eof or change of state
      initialize postcode
      perform until not eof or change of postcode or change state
         tally for postcode ....
         read
      end-perform
      print postcode total
   end-perform
   print state total
end-perform
print grand total


I fundamentally agree that priming read is a little hard to grasp
at first however once learned most logic just falls out of the
structure.

Ken

PS: Using report writer is not an answer as the report is a simple
thing that other understand.  A lot of logic involves loops within
loops with terminating breaks.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au>`

```
On Fri, 30 Apr 1999 13:25:53, Ken Foskey <waratah@zip.com.au> wrote:

Non COBOL news groups snipped....

> Thane Hubbell wrote:
> > 
…[10 more quoted lines elided]…
> loops with terminating breaks.

I dislike priming reads and find no requirement for them in a control 
break program.   If you want to see a clear, easy, concise program 
that performs multiple levels of control breaks, prints nothing if the
file is empty (I love those programs that perform the heading routines
first thing, then have NOTHING after that because of no data!) check 
out the Advanced reporting chapter of my book.  


-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3729E812.79BD95C3@NOSPAMhome.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com>`

```
> I dislike priming reads and find no requirement for them in a control
> break program.   If you want to see a clear, easy, concise program
…[3 more quoted lines elided]…
> out the Advanced reporting chapter of my book.

I like priming reads.  But the solution I have for the unneeded headings
is to design my print routine so that it does a control break on the
very first detail write.

e.g.  define current-line as 99, or old-name as "garbage".

But sometimes the users WANT a heading routine with no data.  This way
they know they got the report and recognize it easily and know it's
empty.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372C1EB6.C3F6F683@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Fri, 30 Apr 1999 13:25:53, Ken Foskey <waratah@zip.com.au> wrote:
…[19 more quoted lines elided]…
> 

Thane,

I looked at the examples you provided (thanks).  I will summarise
the technique to two things:

1:

when first-record
    perform set-up

when break-3-happens
   perform break-3
   perform break-2
   perform break-1

when break-2-happens
   perform break-2
   perform break-1

... etc

where break-3, 2, 1 are like:

break-3.

   output-break-3-stuff
   initialise break-3

(Please see the real examples for a better description)

The first thing to not is the reverse logic in the break routines,
first output and then initialise.  So there is some
'understanding' problems similar to the priming read anyway.

The second thing is the extra test for first occurence for every
iteration.  If the tests can be exclusive then the priming read
loops can actually reduce the number of tests further.  If my
example the postcode is unique across Australia so I never need to
check for change of state until I have a change of postcode,
saving a test.

The third thing is that the intialisation stuff must be duplicated
a couple of times (once outside in the setup and once in the
controlling loop).  It just does not fall naturally out.

I wish to note that the code provided by Thane is an internal sort
and ay actually require structure like this because the read
cannot be put at the lowest point of the loop.  As stated I have
NEVER coded an internal sort (well maybe once but I don't remember
it now...)  I am to busy to read up on internal sort and recode
the sample into priming read to show it is simpler.

Ken
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372c6c62.213663056@news1.ibm.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au>`

```
On Sun, 02 May 1999 19:45:26 +1000, Ken Foskey <waratah@zip.com.au>
wrote:


>The second thing is the extra test for first occurence for every
>iteration.  If the tests can be exclusive then the priming read
…[4 more quoted lines elided]…
>

This is a valid concern.  I should have changed the Evaluate to put
that test last, and then it would have been more efficient,

>The third thing is that the intialisation stuff must be duplicated
>a couple of times (once outside in the setup and once in the
>controlling loop).  It just does not fall naturally out.

Hmmmmm... I'll have to go back and look at that code.  I'm going to
put together another example to post, and we'll rip it apart.

>
>I wish to note that the code provided by Thane is an internal sort
…[4 more quoted lines elided]…
>the sample into priming read to show it is simpler.

All you need to do is put a priming "Return" in there <G>.
Hang on a few hours and work against my newer example - without the
sort.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372D7699.D353CD58@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c6c62.213663056@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
...
> 
> This is a valid concern.  I should have changed the Evaluate to put
> that test last, and then it would have been more efficient,
> 
....

Here we go the crux of the discussion.  I will run through some
maths and see how we come out on the tests

Thane:

1.  When  Transaction-Dept Not = Save-Dept
  1,000,000  (1 million records)

2.  When  Transaction-Date Not = Save-Date
  999,970   (assume thirty dates)

3.  When  Transaction-Type Not = Save-Type
  999,670   (assume ten transactions for each date)

4.  When  Save-Dept = High-Values
  996,670   (assume ten dept's for each tran for each date)

TOTAL:  3,996,310

Ken:

1. Until All-Done
    10  (ten depts)

2. until transaction-dept not = save-dept

    100 times  (ten depts times ten trans)

3. or all-done
    10 times   (only when the first test suceeds)

4. until transaction-date not = save-date
   3000 times

5. or transaction-dept not = save-dept
   100 times (above)

6. or all-done
   10 times (above)

7. until transaction-type not = save-type
   1,000,000 times (number of records)

8. or transaction-date not = save-date
   3000 times 

9. or transaction-dept not = save-dept
   100 times

10. or all-done
   10 times.

TOTAL:   1,006,340


Factor of tests is about 4 to 1.

Even if we remove the high values test entirely (somehow) the
priming read is still a factor of 3 more efficient.

Did I miss anything?

Ken
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 11)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-VKRzzNxdPC4p@Dwight_Miller.iix.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c6c62.213663056@news1.ibm.net> <372D7699.D353CD58@zip.com.au>`

```
On Mon, 3 May 1999 10:12:41, Ken Foskey <waratah@zip.com.au> wrote:
> TOTAL:  3,996,310
> 
…[8 more quoted lines elided]…
> Did I miss anything?

No, I think you smacked me with the truck full force. <G>

I do maintain that it is much easier with my method to add a new level
of break.  

Also, a lot of this depends on data itself, and on the optimization 
level of the compiler.  Does my solution really mean that number of 
comparisons?  Looks like it, but in a real time sense, how much slower
is it?  I doubt it's 4 times as slow.  *I* find the code easier to 
follow - but that's just me!  

Other opinions?  Interesting Ken, Thanks.


-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37303DF0.8F7D175A@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c6c62.213663056@news1.ibm.net> <372D7699.D353CD58@zip.com.au> <Jl0PnHJ5PvPd-pn2-VKRzzNxdPC4p@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Mon, 3 May 1999 10:12:41, Ken Foskey <waratah@zip.com.au> wrote:
…[12 more quoted lines elided]…
> No, I think you smacked me with the truck full force. <G>

There was an error in this calculation.  The real factor close
enough to 1:1.

The problem is that the UNTIL is really negative and you have to
find the FALSE match for the OR not the TRUE match.  Totally
stuffs my statistics.

But...  If there is a possibility of omitting the checks (eg if
the lowest level keys are 'truly' unique) then the 4:1 is a
possibility.

Ken
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 13)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37307d2f.232045945@news1.ibm.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c6c62.213663056@news1.ibm.net> <372D7699.D353CD58@zip.com.au> <Jl0PnHJ5PvPd-pn2-VKRzzNxdPC4p@Dwight_Miller.iix.com> <37303DF0.8F7D175A@zip.com.au>`

```
On Wed, 05 May 1999 22:47:44 +1000, Ken Foskey <waratah@zip.com.au>
wrote:


>There was an error in this calculation.  The real factor close
>enough to 1:1.
…[7 more quoted lines elided]…
>possibility.

I'm about to do something I talked about in a previous post.

I'm going to switch sides of the arguement <G>.

Ken - we CAN get the comparisons down to about 3-1.

Your check for "all done" in each until matches up to my first
required High Values check.  

However, if you rearrange your input record to match the save-key,
then subdivide the save key so that you have only one compare - (group
level) you can elimiated the extra OR's - except for the "all done".

See what I mean?

If I get a few minutes, I'll rewrite the program and show you.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 11)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372e2978.79519310@news1.ibm.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c6c62.213663056@news1.ibm.net> <372D7699.D353CD58@zip.com.au>`

```
On Mon, 03 May 1999 20:12:41 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>Thane Hubbell wrote:
>> 
…[9 more quoted lines elided]…
>

Let me run some real world data tests and see what kind of runtimes I
get. 

Using Realia COBOL (Where I can get good stats and ASM output) - the
size of the code segment in your solution is 77F  - Mine is 767 -
Pretty darn close.  

I need to dummy up some data - say 2Million records or so.  And run
some repeated tests.  I think there was something misleading in your
counts - the "Until's" have OR's in them - and each OR is an
additional compare - which should inflate your counts to be only
slightly less than mine.  OTOH - My check for High Values MUST come
first (unlike what I coded in the examp.cob), and that will really
increase my comparisons by the number of records.  I have to think
that for that reason alone your method will be more efficient at
runtime.
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372c7628.216165688@news1.ibm.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au>`

```
On Sun, 02 May 1999 19:45:26 +1000, Ken Foskey <waratah@zip.com.au>
wrote:


>The first thing to note is the reverse logic in the break routines,
>first output and then initialise.  So there is some
>'understanding' problems similar to the priming read anyway.
>

I don't understand! <G>  Seriously, I do explain this in the book with
the reasoning behind it.  

>The second thing is the extra test for first occurence for every
>iteration.  If the tests can be exclusive then the priming read
…[4 more quoted lines elided]…
>

This example corrects that by changing the order of the Evaluate.

>The third thing is that the intialisation stuff must be duplicated
>a couple of times (once outside in the setup and once in the
>controlling loop).  It just does not fall naturally out.
>

I think what you are talking about is the move of the fields to the
save fields.  This occurs in two places - once for the first
iteration, and then individually in the break routines.

>I wish to note that the code provided by Thane is an internal sort
>and ay actually require structure like this because the read
…[3 more quoted lines elided]…
>the sample into priming read to show it is simpler.

I've removed the sort and changed the code a bit to avoid violating my
publishers copyright.  

Note:  The perform of the lower level breaks is repeated in the
Evaluate.  One COULD perform the lower level break within each
routine.   IE:  The first thing in the Date-Break paragraph could be a
perform of the Type-Break and so on.  I don't do this because it makes
it more difficult later to insert a new level of break in the middle.

  
000010 @OPTIONS MAIN,TEST
000020 Identification Division.
000030 Program-Id.  Examp.
000031* Control Break Example
000043 Environment Division.
000050 Configuration Section.
000055 Source-Computer.  IBM-PC.
000056 Object-Computer.  IBM-PC.
000061 Input-Output  Section.
000062 File-Control.
000063     Select Input-File Assign To "Input.Dat".
000070     Select Report-File Assign To Printer.
000076 Data Division.
000077 File Section.
000110 Fd  Report-File.
000111 01  Report-Record Pic X(80).
000112 Fd  Input-File.
000113 01  Input-Record.
000114     03  Transaction-Date.
000116         05  Trans-Month    Pic 99.
000117         05  Trans-Day      Pic 99.
000118         05  Trans-Year     Pic 9(4).
000119     03  Transaction-Type   Pic  X(4).
000120     03  Transaction-Dept   Pic  X(8).
000121     03  Transaction-Price  Pic S9(7)v99.
000122     03  Transaction-Qty    Pic  9(3).
000123     03  Filler             Pic  X(40).
000157 Working-Storage Section.
000209 01  Heading-Line-1.
000210     03  Filler      Pic X(12) Value "Created by:".
000211     03  Filler      Pic X(8)  Value "EXAMP".
000212     03  Filler      Pic X(8) Value Spaces.
000213     03  Filler      Pic X(29)
000214         Value "Transaction Detail by Dept.".
000215     03  Filler      Pic X(7) Value Spaces.
000216     03  Filler      Pic X(5)  Value "Page".
000217     03  Page-No     Pic Z(4)9 Value Zeros.
000218 01  Heading-Line-2.
000219     03  Filler      Pic X(12) Value "Created on:".
000220     03  Date-MM     Pic 99.
000221     03  Filler      Pic X     Value "/".
000222     03  Date-DD     Pic 99.
000223     03  Filler      Pic X     Value "/".
000224     03  Date-YY     Pic 99.
000225 01  Heading-Line-3.
000226     03  Filler      Pic X(12) Value "At:".
000227     03  Time-HH     Pic 99.
000228     03  Filler      Pic X     Value ":".
000229     03  Time-MM     Pic 99.
000230     03  Filler      Pic X     Value ":".
000231     03  Time-SS     Pic 99.
000232* Heading Line Must Be Modified.
000235 01  Heading-Line-4.
000236     03  Filler      Pic X(11) Value "Department ".
000238     03  Filler      Pic X(8)  Value "Date   ".
000239     03  Filler      Pic X(7)  Value "Type ".
000240     03  Filler      Pic X(8)  Value "Qty".
000241     03  Filler      Pic X(8)  Value "Amount".
000243 01  Blank-Line      Pic X(80) Value Spaces.
000244* Detail Line Is New.
000253 01  Detail-Line.
000254     03  Detail-Dept         Pic X(4)  Value Spaces.
000255     03  Filler              Pic X(8)  Value Spaces.
000258     03  Detail-Date.
000259         05  Trans-Month     Pic 99.
000260         05  Filler          Pic X Value "/".
000261         05  Trans-Day       Pic 99.
000262         05  Filler          Pic X Value "/".
000263         05  Trans-Year      Pic 9(4).
000264     03  Filler              Pic X     Value Spaces.
000265     03  Detail-Type         Pic X(4)  Value Spaces.
000266     03  Filler              Pic X     Value Spaces.
000267     03  Detail-Qty          Pic Z(4)9.
000268     03  Filler              Pic X     Value Spaces.
000269     03  Detail-Amt          Pic $$$,$$$.99-.
000272 01  Total-Line.
000273     03  Total-Description   Pic X(28)       Value Spaces.
000274     03  Total-Qty           Pic Z(4)9.
000275     03  Filler              Pic X           Value Spaces.
000276     03  Total-Amt           Pic $$$,$$$.99-.
000277     03  Filler              Pic X           Value Spaces.
000278     03  Total-Commission    Pic $$$,$$$.99-.
000279 01  Desc-Type.
000280     03  Filler              Pic X(11) Value "*   Total".
000281     03  Desc-Type-Type      Pic X(4).
000282 01  Desc-Date.
000283     03  Filler              Pic X(11) Value "**  Total".
000284     03  Trans-Month         Pic 99.
000285     03  Filler              Pic X Value "/".
000286     03  Trans-Day           Pic 99.
000287     03  Filler              Pic X Value "/".
000288     03  Trans-Year          Pic 9(4).
000289 01  Desc-Department.
000290     03  Filler              Pic X(11) Value "*** Total".
000291     03  Desc-Dept           Pic X(4).
000292 01  Save-Fields.
000293     03  Save-Dept          Pic X(4)   Value High-Values.
000297     03  Save-Date.
000298         05  Trans-Year     Pic 9(4).
000299         05  Trans-Month    Pic 9(2).
000300         05  Trans-Day      Pic 9(2).
000301     03 Save-Type           Pic X(4)     Value High-Values.
000302 01  Accumulators.
000303     03  Grand-Totals.
000304         05  Total-Qty        Pic 9(5)         Value Zeros.
000305         05  Total-Amt        Pic S9(6)v99     Value Zeros.
000307     03  Dept-Totals.
000308         05  Total-Qty        Pic 9(5)         Value Zeros.
000309         05  Total-Amt        Pic S9(6)v99     Value Zeros.
000311     03  Date-Totals.
000312         05  Total-Qty        Pic 9(5)         Value Zeros.
000313         05  Total-Amt        Pic S9(6)v99     Value Zeros.
000315     03  Type-Totals.
000316         05  Total-Qty        Pic 9(5)         Value Zeros.
000317         05  Total-Amt        Pic S9(6)v99     Value Zeros.
000319 01  Line-Count           Pic 99          Value 99.
000320 01  Page-Count           Pic 9(4)        Value Zeros.
000321 01  Max-Lines            Pic 99          Value 60.
000322 01  Date-And-Time-Area.
000323     03  Work-Date            Pic 9(6).
000324     03  Work-Date-X          Redefines Work-Date.
000325         05  Date-YY          Pic 99.
000326         05  Date-MM          Pic 99.
000327         05  Date-DD          Pic 99.
000328     03  Work-Time            Pic 9(8).
000329     03  Work-Time-X          Redefines Work-Time.
000330         05  Time-HH          Pic 99.
000331         05  Time-MM          Pic 99.
000332         05  Time-SS          Pic 99.
000333         05  Filler           Pic XX.
000335 01  Done-Flag            Pic X Value Spaces.
000336     88  All-Done               Value "Y".
000339 Procedure Division.
000348 Examp-Start.
000399     Open Output Report-File
000400     Move Space To Done-Flag
000401     Perform Fill-Initial-Headings
000402     Perform Process-Records Until All-Done
000403     Close Report-File
000404     Stop Run
000405     .
000406 Process-Records.
000407     Read Input-File
000408            At End
000409               Perform Type-Break
000410               Perform Date-Break
000411               Perform Dept-Break
000412               Perform Print-Grand-Totals
000413               Set All-Done To True
000414            Not At End
000415               Perform Check-For-Break
000416     End-Read
000417     .
000418 Check-For-Break.
000419     Evaluate True
000424        When  Transaction-Dept Not = Save-Dept
000426              Perform Type-Break
000427              Perform Date-Break
000428              Perform Dept-Break
000429        When  Transaction-Date Not = Save-Date
000430              Perform Type-Break
000431              Perform Date-Break
000432        When  Transaction-Type Not = Save-Type
000433              Perform Type-Break
000434        When  Save-Dept = High-Values
000435              Move Transaction-Dept To Save-Dept
000436              Move Transaction-Date To Save-Date
000437              Move Transaction-Type To Save-Type
000439        When  Other
000440              Continue
000441     End-Evaluate
000442     Perform Process-Detail-Record
000443     .
000444 Process-Detail-Record.
000445* New Detail Record Logic
000446     Perform Fill-Write-Detail
000447     Add Transaction-Qty To Total-Qty Of Type-Totals
000449     Compute Total-Amt Of Type-Totals =
000450             Total-Amt Of Type-Totals +
000451             (Transaction-Qty * Transaction-Price)
000452     .
000453 Fill-Write-Detail.
000460     Move Transaction-Dept To Detail-Dept
000483     Move Corresponding Transaction-Date To Detail-Date
000484     Move Transaction-Type To Detail-Type
000485     Move Transaction-Qty  To Detail-Qty
000486     Compute Detail-Amt = Transaction-Qty * Transaction-Price
000488     If Line-Count > Max-Lines
000489        Perform Heading-Routine
000490     End-If
000491     Write Report-Record From Detail-Line After 1
000492     .
000493 Type-Break.
000494     Perform Print-Type-Total
000495     Add Corresponding Type-Totals To Date-Totals
000496     Initialize Type-Totals
000497     Move Transaction-Type To Save-Type
000517     .
000527 Date-Break.
000537     Perform Print-Date-Total
000538     Add Corresponding Date-Totals To Dept-Totals
000539     Initialize Date-Totals
000540     Move Transaction-Date To Save-Date
000542     .
000543 Dept-Break.
000544     Perform Print-Dept-Total
000545     Add Corresponding Dept-Totals To Grand-Totals
000546     Initialize Dept-Totals
000547     Move Transaction-Dept To Save-Dept
000548     .
000549 Print-Type-Total.
000550* Changed This Paragraph To Double Space.
000558     Move Corresponding Type-Totals To Total-Line
000568     Move Save-Type To Desc-Type-Type
000578     Move Desc-Type To Total-Description
000579     If Line-Count > Max-Lines - 2
000580        Perform Heading-Routine
000581     End-If
000582     Write Report-Record From Total-Line After 2
000583     Write Report-Record From Blank-Line After 1
000592     Add 3 To Line-Count
000598     .
000608 Print-Date-Total.
000618     Move Corresponding Date-Totals To Total-Line
000628     Move Corresponding Save-Date   To Desc-Date
000638     Move Desc-Date To Total-Description
000639     If Line-Count > Max-Lines - 1
000640        Perform Heading-Routine
000641     End-If
000648     Write Report-Record From Total-Line After 1
000649     Write Report-Record From Blank-Line After 1
000658     Add 2 To Line-Count
000659     .
000668 Print-Dept-Total.
000678     Move Corresponding Dept-Totals To Total-Line
000715     Move Save-Dept To Desc-Dept
000737     Move Desc-Department To Total-Description
000738     If Line-Count > Max-Lines - 1
000739        Perform Heading-Routine
000740     End-If
000741     Write Report-Record From Total-Line After 1
000742     Write Report-Record From Blank-Line After 1
000743     Add 2 To Line-Count
000748     .
000758 Print-Grand-Totals.
000768     Move Corresponding Grand-Totals To Total-Line
000778     Move "****Grand Totals" To Total-Description
000788     If Line-Count > Max-Lines - 1
000798        Perform Heading-Routine
000808     End-If
000818     Write Report-Record From Total-Line After 2
000828     .
000838 Heading-Routine.
000848     Add 1 To Page-Count
000849     Move Page-Count To Page-No
000858     If Page-Count = 1
000868        Write Report-Record From Heading-Line-1 After Zero
000878     Else
000888        Write Report-Record From Heading-Line-1 After Page
000898     End-If
000908     Write Report-Record From Heading-Line-2 After 1
000918     Write Report-Record From Heading-Line-3 After 1
000919     Write Report-Record From Heading-Line-4 After 2
000920     Write Report-Record From Blank-Line     After 1
000921     Move 6 To Line-Count
000922     .
000932 Fill-Initial-Headings.
000942     Accept Work-Date From Date
000952     Accept Work-Time From Time
000962     Move Corresponding Work-Date-X To
000972                        Heading-Line-2
000982     Move Corresponding Work-Time-X To
000992                        Heading-Line-3
001002     .
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372D72A1.4A88BC10@zip.com.au>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au> <Jl0PnHJ5PvPd-pn2-Uwk5Ls6lqRdb@Dwight_Miller.iix.com> <372C1EB6.C3F6F683@zip.com.au> <372c7628.216165688@news1.ibm.net>`

```
Thane Hubbell wrote:

Lots of stuff and some code for me to directly answer 'the
challenge',  it compiles but I have not tested it any other way:

       @OPTIONS MAIN,TEST
       Identification Division.
       Program-Id.  Exampk.
      * Control Break Example
       Environment Division.
       Input-Output  Section.
       File-Control.
           Select Input-File Assign To "Input.Dat".
           Select Report-File Assign To Printer.
       Data Division.
       File Section.
       Fd  Report-File.
       01  Report-Record Pic X(80).
       Fd  Input-File.
       01  Input-Record.
           03  Transaction-Date.
               05  Trans-Month    Pic 99.
               05  Trans-Day      Pic 99.
               05  Trans-Year     Pic 9(4).
           03  Transaction-Type   Pic  X(4).
           03  Transaction-Dept   Pic  X(8).
           03  Transaction-Price  Pic S9(7)v99.
           03  Transaction-Qty    Pic  9(3).
           03  Filler             Pic  X(40).
       Working-Storage Section.
       01  Heading-Line-1.
           03  Filler      Pic X(12) Value "Created by:".
           03  Filler      Pic X(8)  Value "EXAMP".
           03  Filler      Pic X(8) Value Spaces.
           03  Filler      Pic X(29)
               Value "Transaction Detail by Dept.".
           03  Filler      Pic X(7) Value Spaces.
           03  Filler      Pic X(5)  Value "Page".
           03  Page-No     Pic Z(4)9 Value Zeros.
       01  Heading-Line-2.
           03  Filler      Pic X(12) Value "Created on:".
           03  Date-MM     Pic 99.
           03  Filler      Pic X     Value "/".
           03  Date-DD     Pic 99.
           03  Filler      Pic X     Value "/".
           03  Date-YY     Pic 99.
       01  Heading-Line-3.
           03  Filler      Pic X(12) Value "At:".
           03  Time-HH     Pic 99.
           03  Filler      Pic X     Value ":".
           03  Time-MM     Pic 99.
           03  Filler      Pic X     Value ":".
           03  Time-SS     Pic 99.
      * Heading Line Must Be Modified.
       01  Heading-Line-4.
           03  Filler      Pic X(11) Value "Department ".
           03  Filler      Pic X(8)  Value "Date   ".
           03  Filler      Pic X(7)  Value "Type ".
           03  Filler      Pic X(8)  Value "Qty".
           03  Filler      Pic X(8)  Value "Amount".
       01  Blank-Line      Pic X(80) Value Spaces.
      * Detail Line Is New.
       01  Detail-Line.
           03  Detail-Dept         Pic X(4)  Value Spaces.
           03  Filler              Pic X(8)  Value Spaces.
           03  Detail-Date.
               05  Trans-Month     Pic 99.
               05  Filler          Pic X Value "/".
               05  Trans-Day       Pic 99.
               05  Filler          Pic X Value "/".
               05  Trans-Year      Pic 9(4).
           03  Filler              Pic X     Value Spaces.
           03  Detail-Type         Pic X(4)  Value Spaces.
           03  Filler              Pic X     Value Spaces.
           03  Detail-Qty          Pic Z(4)9.
           03  Filler              Pic X     Value Spaces.
           03  Detail-Amt          Pic $$$,$$$.99-.
       01  Total-Line.
           03  Total-Description   Pic X(28)       Value Spaces.
           03  Total-Qty           Pic Z(4)9.
           03  Filler              Pic X           Value Spaces.
           03  Total-Amt           Pic $$$,$$$.99-.
           03  Filler              Pic X           Value Spaces.
           03  Total-Commission    Pic $$$,$$$.99-.
       01  Desc-Type.
           03  Filler              Pic X(11) Value "*   Total".
           03  Desc-Type-Type      Pic X(4).
       01  Desc-Date.
           03  Filler              Pic X(11) Value "**  Total".
           03  Trans-Month         Pic 99.
           03  Filler              Pic X Value "/".
           03  Trans-Day           Pic 99.
           03  Filler              Pic X Value "/".
           03  Trans-Year          Pic 9(4).
       01  Desc-Department.
           03  Filler              Pic X(11) Value "*** Total".
           03  Desc-Dept           Pic X(4).
       01  Save-Fields.
           03  Save-Dept          Pic X(4)   Value High-Values.
           03  Save-Date.
               05  Trans-Year     Pic 9(4).
               05  Trans-Month    Pic 9(2).
               05  Trans-Day      Pic 9(2).
           03 Save-Type           Pic X(4)     Value High-Values.
       01  Accumulators.
           03  Grand-Totals.
               05  Total-Qty        Pic 9(5)         Value Zeros.
               05  Total-Amt        Pic S9(6)v99     Value Zeros.
           03  Dept-Totals.
               05  Total-Qty        Pic 9(5)         Value Zeros.
               05  Total-Amt        Pic S9(6)v99     Value Zeros.
           03  Date-Totals.
               05  Total-Qty        Pic 9(5)         Value Zeros.
               05  Total-Amt        Pic S9(6)v99     Value Zeros.
           03  Type-Totals.
               05  Total-Qty        Pic 9(5)         Value Zeros.
               05  Total-Amt        Pic S9(6)v99     Value Zeros.
       01  Line-Count           Pic 99          Value 99.
       01  Page-Count           Pic 9(4)        Value Zeros.
       01  Max-Lines            Pic 99          Value 60.
       01  Date-And-Time-Area.
           03  Work-Date            Pic 9(6).
           03  Work-Date-X          Redefines Work-Date.
               05  Date-YY          Pic 99.
               05  Date-MM          Pic 99.
               05  Date-DD          Pic 99.
           03  Work-Time            Pic 9(8).
           03  Work-Time-X          Redefines Work-Time.
               05  Time-HH          Pic 99.
               05  Time-MM          Pic 99.
               05  Time-SS          Pic 99.
               05  Filler           Pic XX.
       01  Done-Flag            Pic X Value Spaces.
           88  All-Done               Value "Y".
       Procedure Division.
       Examp-Start.
           Open Output Report-File
           Move Space To Done-Flag
           Perform Fill-Initial-Headings
           Read Input-File
                  At End
                     Set All-Done To True
           End-Read

           Perform Process-dept
                Until All-Done

           Perform Print-Grand-Totals
           Close Report-File
           Stop Run
           .
       Process-dept.
           Initialize Dept-Totals
           Move Transaction-Dept To Save-Dept

           perform process-type
               until transaction-dept not = save-dept
                  or all-done

           Perform Print-Dept-Total
           Add Corresponding Dept-Totals To Grand-Totals
           .
       Process-date.
           Initialize Date-Totals
           Move Transaction-Date To Save-Date

           perform process-type
               until transaction-date not = save-date
                  or transaction-dept not = save-dept
                  or all-done

           Perform Print-Date-Total
           Add Corresponding Date-Totals To Dept-Totals
           .
       process-type.
           Initialize Type-Totals
           Move Transaction-Type To Save-Type
           perform process-detail-record
               until transaction-type not = save-type
                  or transaction-date not = save-date
                  or transaction-dept not = save-dept
                  or all-done

           Perform Print-Type-Total
           Add Corresponding Type-Totals To Date-Totals
           .
       Process-Detail-Record.
      * New Detail Record Logic
           Perform Fill-Write-Detail
           Add Transaction-Qty To Total-Qty Of Type-Totals
           Compute Total-Amt Of Type-Totals =
                   Total-Amt Of Type-Totals +
                   (Transaction-Qty * Transaction-Price)
           .
       Fill-Write-Detail.
           Move Transaction-Dept To Detail-Dept
           Move Corresponding Transaction-Date To Detail-Date
           Move Transaction-Type To Detail-Type
           Move Transaction-Qty  To Detail-Qty
           Compute Detail-Amt = Transaction-Qty *
Transaction-Price
           If Line-Count > Max-Lines
              Perform Heading-Routine
           End-If
           Write Report-Record From Detail-Line After 1

           Read Input-File
                  At End
                     Set All-Done To True
           End-Read
           .
       Type-Break.
           .
       Print-Type-Total.
      * Changed This Paragraph To Double Space.
           Move Corresponding Type-Totals To Total-Line
           Move Save-Type To Desc-Type-Type
           Move Desc-Type To Total-Description
           If Line-Count > Max-Lines - 2
              Perform Heading-Routine
           End-If
           Write Report-Record From Total-Line After 2
           Write Report-Record From Blank-Line After 1
           Add 3 To Line-Count
           .
       Print-Date-Total.
           Move Corresponding Date-Totals To Total-Line
           Move Corresponding Save-Date   To Desc-Date
           Move Desc-Date To Total-Description
           If Line-Count > Max-Lines - 1
              Perform Heading-Routine
           End-If
           Write Report-Record From Total-Line After 1
           Write Report-Record From Blank-Line After 1
           Add 2 To Line-Count
           .
       Print-Dept-Total.
           Move Corresponding Dept-Totals To Total-Line
           Move Save-Dept To Desc-Dept
           Move Desc-Department To Total-Description
           If Line-Count > Max-Lines - 1
              Perform Heading-Routine
           End-If
           Write Report-Record From Total-Line After 1
           Write Report-Record From Blank-Line After 1
           Add 2 To Line-Count
           .
       Print-Grand-Totals.
           Move Corresponding Grand-Totals To Total-Line
           Move "****Grand Totals" To Total-Description
           If Line-Count > Max-Lines - 1
              Perform Heading-Routine
           End-If
           Write Report-Record From Total-Line After 2
           .
       Heading-Routine.
           Add 1 To Page-Count
           Move Page-Count To Page-No
           If Page-Count = 1
              Write Report-Record From Heading-Line-1 After Zero
           Else
              Write Report-Record From Heading-Line-1 After Page
           End-If
           Write Report-Record From Heading-Line-2 After 1
           Write Report-Record From Heading-Line-3 After 1
           Write Report-Record From Heading-Line-4 After 2
           Write Report-Record From Blank-Line     After 1
           Move 6 To Line-Count
           .
       Fill-Initial-Headings.
           Accept Work-Date From Date
           Accept Work-Time From Time
           Move Corresponding Work-Date-X To
                              Heading-Line-2
           Move Corresponding Work-Time-X To
                              Heading-Line-3
           .
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.cobol
- **Message-ID:** `<7gcjgs$j8u$1@news.igs.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <3725BFC4.5205DB2E@zip.com.au> <bLnV2.4020$B55.313802@dfiatx1-snr1> <3728DD58.D5770059@zip.com.au> <3728e366.72458097@news1.ibm.net> <3729AF61.C2CB9CA6@zip.com.au>`

```
Ken Foskey wrote in message <3729AF61.C2CB9CA6@zip.com.au>...
>
>I fundamentally agree that priming read is a little hard to grasp
>at first however once learned most logic just falls out of the
>structure.


I agree.  Once a person grasps the idea of setting up a loop *before*
entering it, then the logic tends to fall into place quite naturally.
```

##### ↳ ↳ Re: Labels .. Pros and Cons

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-28T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<37275FB7.6E2F664A@IMN.nl>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov>`

```
Richard Maine wrote:

> Of course, some of my favorite examples of (what I consider to be) bad
> code structure come from Pascal.

8< everyone's ability to write spaghetti

> My favorite (and certainly not original to me, but its one I see a lot)
> "Pascalism" is how to code something where you need an exit from the
> middle of a loop (the F90 exit statement is great for the purpose).

What's F90 ???

> You often see a strange abomination done with little reason that I can
> ascertain except  to force the code into a preconcieved notion that
> good structure means using "do while".

May be an until too

> You rotate the code around in the loop so that the exit condition is
> at the top, where the "do while" needs it.

No, to get the exit of a sequence at the bottom of that sequence (the only good
place for exits: one entry - at the top / one exit - at the bottom)

>  Then, before the loop
> you add a second copy of the first part of the code to patch things
> up so that the loop will work when messed up like that.  (Yes,
> very prejudicial wording on my part).

Then, at two places, we put an INVOKATION of the first part of the code stored
at one place, so that the loop will work like the structure of it's driving
datapump.

Data pump? Data pump??? Yes: data pump. I'll explain further on.

>  Giving something like
>
…[7 more quoted lines elided]…
> unknown length.

yep. *because* of the unknown length.

>  In that case, the 2 parts in their "natural" order
> are "read some data from the file" and "process the data you just read".

Indeed: "read some data" and "process it", the "read again some" until it's over
and out.
The read pumps the data for the loop to iterate with.

>
> The exit condition is when there is no more data in the file,

The pump goes dry

> which
> you typically don't discover until after you try to read it.  For that
> kind of case, the above proto-code looks

*NOT* only

> like
>
…[4 more quoted lines elided]…
>    end

*BUT* also possibly like
    [read some]
    do
        [process]
        [read some (more)]
    until [end of file]

> I cannot by any stretch of the imagination consider this to be
> naturally structured.

Sounds natural to me. It even is structured by Bï¿½hm/Jacopine/Jackson ideas! Read
on!

>  This certainly doesn't match how "I" think
> of the problem.

The solution is to think of the structure of the data

>  I think of a loop that involves reading data,
> then processing the data just read.  The only way I'd ever
…[5 more quoted lines elided]…
> code is a huge red flag of bad structure.

Uh oh. Just call/perform/invoke twice the dame read-sub-routine and your 2
copies are one.

>  That violates one of the
> major principles of good coding - don't write the same thing twice,
> particularly if it is important that the 2 parts match.

Solved by subroutine

>  And
> again, I can't imagine any "natural" mental model that starts out with
> 2 copies of the same stuff.

Again my point: one copy, two places, natural because ... her it comes:

To iter over a data source (array/file/stack) of n things (cell/record/entry),
where n is unknown and only a black box grip (n++/read/pop) in the data store
(array/file/stack) is availabe with a fail/success test after that grip(n>max/at
end/empty=true), you have to grip n + 1 times.
But, you get n items, so you process n times, not n + 1.
So there is a difference of one execution more offn the GET part above the
PROCess part.
See, i.s.o.
[GET PROC] / [GET PROC] / ... / [GET PROC] / [GET *jumpMiddleOut* PROC] with an
superfluous PROC at the end,
we shift the phase 180 degrees to read:
[GET] / [PROC GET] / [PROC GET] / ... / [PROC GET] / *exitEndOut*

The exit is test for at the end (do until (1)) when at least one record present,
at start when zero possible (do while (2))
In COBOL
(1)
PERFORM READ-SUB
IF (EOF)
    DISPLAY "UNEXPECTEDLY EMPTY"
ELSE
    PEFORM WITH TEST AFTER UNTIL(EOF)
        PERFORM PROCESS-SUB
        PERFORM READ-SUB
    END-PERFORM
END-IF
(2)
PERFORM READ-SUB
PEFORM WITH TEST BEFORE UNTIL (EOF)
    PERFORM PROCESS-SUB
    PERFORM READ-SUB
END-PERFORM

> The above construct is so common that Pascal contorts its notion of
> input in order to accomodate it.  (A get doesn't read data from a file
…[3 more quoted lines elided]…
> applications.  Look into the term "lazy i/o", for example.

So the Pascal designer built the priming read into the language, now *you* can
code what you prefer, something like:
do begin;
  get() // gets n, prefetches n+1
  process(); // processes n
until (eof==true); // tests n+1 fetch gave eof or not
(get proc / get proc / ...)
but what happens behind the scene is:
get test proc / get test proc / ...

> But the contortion falls apart anyway when the data input
> isn't done by the twisted "get" construct - for example if the
> data is input by calling some 3rd party library procedure.
> You end up thrown back to the above loop construct with the
> loop written "backwards" and part of its code duplicated.

Not duplicated, but from two places called

> ....either that or you go look up how to use a goto in Pascal.
> It is possible, although some variants might disallow it, and
…[4 more quoted lines elided]…
> consider Pascal well suited to structured coding at all.

As may be evident from my reaction, I think that COBOL is well suited for it.
Another example, with array with unknown filled entries:
MOVE 1 TO N *> CALL READ-SUB 1st time
PERFORM WITH TEST BEFORE UNTIL (N > COUNT) *> UNTIL EOF
    PERFORM PROCESS *> process entry(n) / record (n)
    ADD 1 TO N *> The DATA PUMP here i.s.o a read
END-PERFORM
You can see the ADD as the "READ TABLE" here!

>  Yes,
> its possible to code anything in Pascal - I've done a fair amount
…[7 more quoted lines elided]…
> F90/f95 supports the above kind of problem excellently (in my opinion).

Ah. Got it: you mean Fortran (don't you?)

>
> It turns into
…[7 more quoted lines elided]…
> I consider that good structure.  Also happens that it doesn't use goto's.

I consider that bad: exit in the middle. Also the exit is just a "goto
end-of-loop" but is written with an e, an x, an i and a t i.s.o a g, an o, a t
and an o.

> But my main thesis is that the number of goto's is not a plausible
> "metric" of good structure.

That's right.
Consequently doing
  ...
  PERFORM DATAPUMP-SUB.
L1.
  IF (ENDE) GO TO L2.
  PERFORM PROCESS-SUB.
  PERFORM DATAPUMP-SUB.
  GO TO L1.
L2.
  ...
i.s.o.
PERFORM DATAPUMP-SUB
PEFORM WITH TEST BEFORE UNTIL (ENDE)
    PERFORM PROCESS-SUB
    PERFORM DATAPUMP-SUB
END-PERFORM
is structured well as well

>  It is sometimes a reasonable first
> approximation, but like so many "metrics", when people go overboard
…[3 more quoted lines elided]…
> nothing less than getting rid of goto's.

Agreed.

> Perhaps appropriate to mention again the Fortran compiler (hi, Bob)
> that actually implemented the "comefrom" statement as a joke, thus
…[4 more quoted lines elided]…
> opinions on it.  But I won't argue about it.

Why not. Nothing nice like a good argument once in a while. :))

> --
> Richard Maine
> maine@altair.dfrc.nasa.gov

The COBOL Frog (jumping is FUN)
```

###### ↳ ↳ ↳ Re: Labels .. Pros and Cons

- **From:** monkey@duke.infowave.net (Scratch Monkey)
- **Date:** 1999-04-28T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<7g7thh$6n6$1@remarQ.com>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <37275FB7.6E2F664A@IMN.nl>`

```
On Wed, 28 Apr 1999 21:21:28 +0200, The COBOL Frog <H.Klink@IMN.nl> wrote:
>Richard Maine wrote:
>
…[9 more quoted lines elided]…
>What's F90 ???

Fortran 90, I would think.

I can't blame you for not making the association between Fortran
and the year 1990. :)
```

###### ↳ ↳ ↳ What's F90

- **From:** "Kevin G. Rhoads" <T_Rhoads@NoSpam.CLASSIC.MSN.COM>
- **Date:** 1999-04-29T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<01be925d$8e598d80$LocalHost@stupidwin95>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <37275FB7.6E2F664A@IMN.nl>`

```
>What's F90 ???
It seemed really strange seeing a post from the Cobol Frog
in comp.lang.fortran.  This stupid thread is crossposted
all over the place.  Welcome to comp.lang.fortran even
if only by cross-post.

F90 refers to the Fortran90 specification, this is common
shorthand used in comp.lang.fortran.  Just as '74, '85 are 
common shorthands for the Cobol '74, '85 standards in
comp.lang.cobol.  ;-)

I guess a one newsgroup troll wasn't enough for whoever 
started this nonsense.
```

###### ↳ ↳ ↳ Re: What's F90

_(reply depth: 4)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.fortran
- **Message-ID:** `<372E0CC8.FE3FA5AA@IMN.nl>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com> <ueeml7uyyx.fsf@altair.dfrc.nasa.gov> <37275FB7.6E2F664A@IMN.nl> <01be925d$8e598d80$LocalHost@stupidwin95>`

```
"Kevin G. Rhoads" wrote:

> >What's F90 ???
> It seemed really strange seeing a post from the Cobol Frog
…[10 more quoted lines elided]…
> started this nonsense.

The discussion about structure was, however (and IMO), useful.

> --
> Kevin G. Rhoads, Ph.D. (Linearity is a convenient fiction.)
> T_Rhoads@NO_SPAM.MSN.com
> krhoads@NO_SPAM.cmpnetmail.com

The Frog
```

#### ↳ Re: Labels .. Pros and Cons

- **From:** "Tom Lake" <tomlake@slic.com>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.basic.misc,comp.lang.c,comp.lang.cobol,comp.lang.fortran,comp.lang.pascal.borland
- **Message-ID:** `<bkgV2.2129$n5.6167@newsfeed.slurp.net>`
- **References:** `<7fg2f3$1oe8@enews3.newsguy.com> <01be8b0a$09868fe0$LocalHost@bunyan> <OAJUXPqj#GA.312@ntdwwaaw.compuserve.com>`

```
In MS compilers there is a penalty.  The compiler optimizes blocks of
statements but treats a label as a new block.  The fewer the number of
labels, the greater the optimization.  One advantage to labels, though, is
that Ctrl-Break can only be recognized at a label, not in between (since the
compiler optimizes that as a single statement)  So if you want fine control
over where your program is interruptible, use labels.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
