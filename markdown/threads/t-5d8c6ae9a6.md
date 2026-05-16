[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# recursive calls

_11 messages · 8 participants · 1999-01_

---

### recursive calls

- **From:** "Deman Carlo" <carlo.deman@village.uunet.be>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76nu8v$olj$1@nickel.uunet.be>`

```
Hi, i'm just a beginner at cobol, and have a big problem.
When i call another program, I can't call back to the original program. How
can i avoid this?
Anyone can tell me how to fix this problem?

Thanx.
```

#### ↳ Re: recursive calls

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76nvkk$sku$1@news.igs.net>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be>`

```
Cobol is not recursive, so you cannot call yourself.  However,
you say "call back".  Is that simply an English problem? You
can return from a subroutine with the exit program statement
if you do not know how to return, but you definitely cannot
call recursively.

Deman Carlo wrote in message <76nu8v$olj$1@nickel.uunet.be>...
>Hi, i'm just a beginner at cobol, and have a big problem.
>When i call another program, I can't call back to the original program. How
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: recursive calls

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76omra$so7@sjx-ixn3.ix.netcom.com>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <76nvkk$sku$1@news.igs.net>`

```

Donald Tees wrote in message <76nvkk$sku$1@news.igs.net>...
>Cobol is not recursive, so you cannot call yourself.  However,
>you say "call back".  Is that simply an English problem? You
>can return from a subroutine with the exit program statement
>if you do not know how to return, but you definitely cannot
>call recursively.

Others will probably point this out (and I don't really want to confuse the
"beginner") BUT,

  A) you can call recursively in many existing implementations (as an
extension)
  B) recursive CALLs will be supported as Standard in the next Standard

However, I agree with Donald, that probably this programmer just wants to
EXIT PROGRAM.

>
>Deman Carlo wrote in message <76nu8v$olj$1@nickel.uunet.be>...
>>Hi, i'm just a beginner at cobol, and have a big problem.
>>When i call another program, I can't call back to the original program.
How
>>can i avoid this?
>>Anyone can tell me how to fix this problem?
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: recursive calls

- **From:** "Deman Carlo" <carlo.deman@village.uunet.be>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76o1p7$r8r$1@nickel.uunet.be>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <76nvkk$sku$1@news.igs.net>`

```
Maybe i didn't explain enough.
Imagine you have 5 programs(prog1,prog2,...).
In every program I wan't to be able to execute the 4 others.
First i call prog2 from prog1. In prog2 i call prog3 and in prog3 i call
prog1 (fatal error of course!! indeed no recursive calls (or "call backs"
like i said, hehe)). How can i deal with this problem?

Donald Tees heeft geschreven in bericht <76nvkk$sku$1@news.igs.net>...
>Cobol is not recursive, so you cannot call yourself.  However,
>you say "call back".  Is that simply an English problem? You
…[6 more quoted lines elided]…
>>When i call another program, I can't call back to the original program.
How
>>can i avoid this?
>>Anyone can tell me how to fix this problem?
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: recursive calls

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76o8i5$bcv$1@server.cntfl.com>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <76nvkk$sku$1@news.igs.net> <76o1p7$r8r$1@nickel.uunet.be>`

```
If all instances of recursion are "tail recursion." then you could
use a program chaining technique. Basically, this requires the
called program to give the name of the next program to call.

For example, in a program "progmain"

        move "prog1" to next-program
        perform until next-program = spaces
            call next-program using next-program
        end-perform

then in each called program use the pattern

        move next-program-name to next-program
        exit program.

If you must actually return control to the calling program, then
you must implement a program call stack in the main program.
Basically, this consists of an array of program names and flags
with code that will control whether and how to return control to
the calling program.

IMO, this technique is so complicated that it should not be
attempted by the beginning programmer and the experienced
programmer would have structured the code so as to prevent
the need for such complications.

If the program chaining technique is not adequate, either
re-structure your application or provide some code samples
so that we may get a better idea of what you intend to
accomplish.

HTH
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >

Deman Carlo wrote in message <76o1p7$r8r$1@nickel.uunet.be>...
>Maybe i didn't explain enough.
>Imagine you have 5 programs(prog1,prog2,...).
…[5 more quoted lines elided]…
>Donald Tees heeft geschreven in bericht <76nvkk$sku$1@news.igs.net>...
[...]
>>
>>Deman Carlo wrote in message <76nu8v$olj$1@nickel.uunet.be>...
>>>Hi, i'm just a beginner at cobol, and have a big problem.
```

###### ↳ ↳ ↳ Re: recursive calls

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UBOj2.5290$Zk.1829364@news3.mia>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <76nvkk$sku$1@news.igs.net> <76o1p7$r8r$1@nickel.uunet.be>`

```
Deman Carlo wrote:
>Maybe i didn't explain enough.
>Imagine you have 5 programs(prog1,prog2,...).
…[3 more quoted lines elided]…
>like i said, hehe)). How can i deal with this problem?

For multiple programs like that, I usually create a little shell program
which calls all the others.  One program can set a value in an EXTERNAL
data field which specifies the next program to call.  Works for me.
```

###### ↳ ↳ ↳ Re: recursive calls

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76odt6$8ao$1@news.igs.net>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <76nvkk$sku$1@news.igs.net> <76o1p7$r8r$1@nickel.uunet.be>`

```
What you are trying to do *is* recursive, and cannot be done in
Cobol. To tell the truth, I cannot really see why.  Just about anything that
can be done with recursion can be done without it.

exception of
Deman Carlo wrote in message <76o1p7$r8r$1@nickel.uunet.be>...
>Maybe i didn't explain enough.
>Imagine you have 5 programs(prog1,prog2,...).
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: recursive calls

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32994.7937.8081@kcbbs.gen.nz>`
- **References:** `<76o1p7$r8r$1@nickel.uunet.be>`

```
In message <<76o1p7$r8r$1@nickel.uunet.be>> "Deman Carlo" <carlo.deman@village.uunet.be> writes:
> Imagine you have 5 programs(prog1,prog2,...).
> In every program I wan't to be able to execute the 4 others.
…[3 more quoted lines elided]…
> 

When you say 'execute the 4 others' do you mean that you want
to be able to 'call and return' or do you actually mean
'jump to'.

Is it that the 5 programs are separate tasks that the user 
may want to jump to: eg one is order entry, another is
debtor enquiry, etc and the user wants to do one of these
at a time in random (unpredicatable) sequence.

If it is just a 'jump to' then you may want to replace
the CALLs with CHAIN.

Or preferably build a simple main program which does
all the calling:

        MOVE "PROG1"      TO Next-Program
        PERFORM
            UNTIL Next-Program = "FINISH"
 
            MOVE Next-Program TO Progarm-Name
            CALL Program-Name
                USING Next-Program
            CANCEL Program-Name
        END-PERFORM
        STOP RUN.

Then in each program:

        LINKAGE SECTION
        01  Next-Program    PIC X(20).

        PROCEDURE DIVISION USING Next-Program.
        .....

                  MOVE "PROGn"    TO Next-Program
                  EXIT PROGRAM.
```

#### ↳ Re: recursive calls

- **From:** WilliamBrinkman@pobox.com
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368f8d4c.1267669@nntp.ix.netcom.com>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be>`

```
You didn't indicate what compiler or version you are using.

However, if you are mainframe and using the IBM Cobol For MVS and VM (aka oo
cobol) you can do recursive calls. Check out SC26-4769-02 and SC26-4767-02.

What you need to do is specify RECURSIVE on the program-id statement after the
program name. There's also a lot of rules that you need to follow.  You can find
all of this in the IBM pubs. You might also want to check out the usages of the
LOCAL-STORAGE SECTION. 

"Deman Carlo" <carlo.deman@village.uunet.be> wrote:

>Hi, i'm just a beginner at cobol, and have a big problem.
>When i call another program, I can't call back to the original program. How
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: recursive calls

- **From:** "Deman Carlo" <carlo.deman@village.uunet.be>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76o3ui$sun$1@nickel.uunet.be>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <368f8d4c.1267669@nntp.ix.netcom.com>`

```
I'm using cobol 4.5 for dos. No mainfraime and no network used. Just a
pentium PC.
WilliamBrinkman@pobox.com heeft geschreven in bericht
<368f8d4c.1267669@nntp.ix.netcom.com>...
>You didn't indicate what compiler or version you are using.
>
>However, if you are mainframe and using the IBM Cobol For MVS and VM (aka
oo
>cobol) you can do recursive calls. Check out SC26-4769-02 and SC26-4767-02.
>
>What you need to do is specify RECURSIVE on the program-id statement after
the
>program name. There's also a lot of rules that you need to follow.  You can
find
>all of this in the IBM pubs. You might also want to check out the usages of
the
>LOCAL-STORAGE SECTION.
>
…[3 more quoted lines elided]…
>>When i call another program, I can't call back to the original program.
How
>>can i avoid this?
>>Anyone can tell me how to fix this problem?
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: recursive calls

- **From:** JVry.NLB@t-online.de
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76qtpa$681$1@nnrp1.dejanews.com>`
- **References:** `<76nu8v$olj$1@nickel.uunet.be> <368f8d4c.1267669@nntp.ix.netcom.com> <76o3ui$sun$1@nickel.uunet.be>`

```
If you use a Realia cobol-compiler release 4.2 you could build recursive
Programs.

If you use an Objektoriented Cobol-compiler like Netexpress you could also
build recursive programs.


Regards

J.V.


-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
