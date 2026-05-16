[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Coding "to the Standard"

_6 messages · 4 participants · 1999-11_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Coding "to the Standard"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<804lhn$kh0$1@nntp4.atl.mindspring.net>`

```
Just some personal opinions related to recent threads on using extensions or
not.  (As usual "your mileage may vary" ...)

1) I can't think of ANY good reason to use non-Standard syntax, when there is
EXACTLY equivalent conforming syntax.  For example, WHY (still) use COMP-3
instead of Packed-Decimal - if you are using an '85 Standard compiler on an
IBM mainframe?  Similarly, using INSPECT CONVERTING instead of TRANSFORM in a
compiler (such as Micro Focus) where both are supported.  (Obviously, if you
are writing code that needs to compile under BOTH an '85 Standard compiler
*and* a '74 Standard compiler - you are "more limited" - but I am afraid, I
just don't have much sympathy for NEW development being limited to '74
Standard functionality.)

2) If you ARE using something from a "newer" Standard/compiler (such as
Intrinsic Functions - where you might also want to port the code to a "base"
'85 Standard compiler - or if you are using '85 Standard syntax - but might
need to port to a '74 Standard compiler)  then you should (probably) at least
DOCUMENT what dependencies there are on the "newer" functionality.  You may
also want to LOOK AT using only the "lower-level" syntax, if there is
something equivalent.  However, (for me personally) avoiding using the
Standard Intrinsic Function routines (if they are available) just because I
*might* some day want to work in a compiler that doesn't have them, seems
silly.  If on the other hand, the "specifications" call for a routine that
will work with either type of compiler, it is silly to code it twice, and you
might as well use the old "brute force" date methods than set up different
copy members or other ways of handling the problem twice.

3) If there is "major" new functionality (non-Standard) that you want to use,
then it is always NICE if you can isolate it to a single routine (paragraph,
section, subprogram, copy-member - or whatever is most appropriate).  This
would probably work for things like screen section vs other UI methodology.
It almost certainly would NOT work for something like OO versus CALLs (which
are really "apples" and "oranges" but ...) Certainly if you have code that
handles 9x file-status codes, I would try to isolate that into a single
"place" in the program (or application) and not have it spread out throughout
the code.

4) I believe that it IS reasonable to use extensions in an application that
are based on a DRAFT Standard - as long as you are well aware that they are a
"moving target" and your implementor may OR MAY NOT provide you easy
"migration paths" to the next/final definition.  There are people (not just
me) who can give you an idea (really a guess) as to what is "stable" and what
isn't in the draft Standard.  On the other hand, it really isn't certain even
WHICH vendors will EVER provide a conforming implementation - even if/when
the draft does become official, so using something from this category is
ALWAYS a risk.

5) I am an INCREDIBLY strong believer in asking vendors to provide support
for functionality from the draft Standard.  I also *know* that any such
request *MUST* be accompanied by user-input on what you expect the vendor to
do if the definition changes in the Standard.  (i.e. do you expect them to
continue to support the "old" definition, once it changes in the Standard -
or do you expect them to provide you with a source code migration tool - or
do you expect them to tell you how YOU can manually change your code.)  What
you say about this *will* impact how willing vendors are to "risk" putting in
code support NOW that may or may NOT turn out to be "correct". (and what they
will charge you for it now - or when a migration tool is needed)

6) It would be "nice" if there were a de facto COBOL standard where "new"
stuff could appear (as it used to when IBM mainframe COBOL *tended* to
dominate what was added). But I don't see that happening again in the future
*even* if we end up with a GNU COBOL and/or an "open source" COBOL or any of
the other things that people hope will "solve" this problem.

7) If your application is "performance sensitive" (and what that means is
ABSOLUTELY a judgment call), you really do need to know HOW to optimize it
for the "platform" (compiler and/or operating system) upon which it will run.
There are still compilers that "optimize" for SECTIONS with priority numbers;
there are certainly situations where COMP-5 will beat BINARY; Obviously, an
EXEC CICS SEND MAP will "beat" a 3270 byte-stream application as far as
maintainability goes and NO-ONE would expect you to limit an IBM online
mainframe application to ANSI Accept/Display statements.

8) Just like there is no such thing (in the real world) as a "one-time"
program (they always end up in production <G>), there is really no such thing
as a program that will NEVER get ported to another compiler/OS.  (Even an
application written for DOS may be upgraded to Windows - or one for MVS may
be upgraded to OS/390.) On the other hand, "experience" in understanding the
"target" (i.e. the person(S) paying for the development) audience will help
you guess the importance of porting vs performance issues - while you are
still in design stage.  In never HURTS to isolate vendor specific "stuff"
(where possible) but if that is going to cause your application to take
longer to develop, longer to run, or be less maintainable, then you really do
need to make a "trade-off" decision at the beginning of application
development.

9) I do think that EVERY developer should run programs thru their vendors
"Standard flagging" mechanism occasionally.  Depending on whether portability
is a design consideration, I wouldn't plan on doing this every time (or even
with every application/program).  On the other hand, I *do* think that
occasionally running with this option can show a programmer what they are
doing that is NOT portable - and cause to (maybe) think about whether there
is an "equally good" way of doing this now, that will be portable in the
future.

     ***

10) A "side-note" about "native language" versus "alien syntax" versus "call
bindings".  These terms are (traditionally) used for such things as:

 "Native Language" support - includes syntax that "looks and feels" like you
are doing a function via the programming language itself, e.g. COBOL SORT
verb (Standard) or AcuCOBOL Accept/Display (non-Standard) or GOBACK and
hex-literals (currently extensions but included in the draft of the next
Standard)

"Alien syntax" support - this includes things like the (old) ENTER statement
(OBSOLETE but still in the Standard - don't confuse with the ENTRY statement
which is just an extension) or EXEC SQL, EXEC CICS, etc Whether such code is
handled by a pre-processor, translator, or the compiler itself, what it
"really does" is "escape" from COBOL native language into a short-detour in
another products syntax - in order to accomplish something.

"Call binding" support - This is where you use the COBOL Standard CALL
statement to invoke (sorry OO people) some other product/feature/whatever to
accomplish a function.  Obviously the CALL itself is Standard (although
calling conventions or parameters may or may not be) but the "functionality"
is done outside the COBOL source code.  One to the GOALS of the draft
Standard is to make it possible to use a growing number of APIs (usually
defined for C-type environments) as "CALL bindings".

A good comparison between the first and last of these types of "support" are
programs that use the COBOL SORT verb versus those that explicitly CALL a
"SORT" program from within their COBOL program.  There is NOTHING "wrong"
with doing the later, but it is not (traditionally) considered using the
"native language" support for sorting.

A good comparison between the second and third of these (for IBMers) is the
difference between using EXEC DLI versus CALL "CBLTDLI".  The first of these
is "alien syntax" while the second  is using a "CALL BINDING".

Now, when it comes to portability ANY of these can be portable from
environment to environment (whether compiler or operating system or
whatever) -  but NONE of them (other than using native Standard syntax) is
"by definition" portable.  Therefore, which of the non-portable "approaches"
you use really depends both on your (individually, person paying your check,
or site-wide) standard/preferences.  If portability is now (or may ever) be
an issue for your application, then I would suggest that you look at the
"breadth" of environments supported by your non-Standard approach (which may
or may not mean checking whether ONLY one vendor supports it - or whether it
really seems to being enhanced/maintained).
```

#### ↳ Re: Coding "to the Standard"

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3826E730.385AC389@NOSPAMhome.com>`
- **References:** `<804lhn$kh0$1@nntp4.atl.mindspring.net>`

```
William M. Klein wrote:

> 1) I can't think of ANY good reason to use non-Standard syntax, when there is
> EXACTLY equivalent conforming syntax.  For example, WHY (still) use COMP-3
…[6 more quoted lines elided]…
> Standard functionality.)

I used this logic when I was in an environment which had both ANSI 68 &
ANSI 72, replacing EXAMINE & INSPECT with TRANSFORM.  It backfired when
TRANSFORM became obsolete.
```

##### ↳ ↳ Re: Coding "to the Standard"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806q2o$u9o$1@nntp3.atl.mindspring.net>`
- **References:** `<804lhn$kh0$1@nntp4.atl.mindspring.net> <3826E730.385AC389@NOSPAMhome.com>`

```
Howard, two MINOR things:

1) You consistently refer to a '72 Standard.  There never was a '72 Standard,
there WAS a '74 Standard.

2) TRANSFORM was *not* a part of the '74 Standard (and I am not positive that
it was even part of the '68 Standard).  I know of LOTS of IBM mainframe
programmers who THINK they are getting the '74 Standard when they use
LANGLVL(2) - but it EXPLICITLY does NOT limit your source code to '74
Standard COBOL.  (What it does is allow ALL of '68 plus ALL of '74 plus ALL
of IBM extensions - except for *TEN* items where it uses the '74 rules
instead of the '68 rules.  These 10 were in an appendix in the OS/VS COBOL
LRM.)
```

###### ↳ ↳ ↳ Re: Coding "to the Standard"

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382702B0.B3A3AA9A@NOSPAMhome.com>`
- **References:** `<804lhn$kh0$1@nntp4.atl.mindspring.net> <3826E730.385AC389@NOSPAMhome.com> <806q2o$u9o$1@nntp3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Howard, two MINOR things:
> 
> 1) You consistently refer to a '72 Standard.  There never was a '72 Standard,
> there WAS a '74 Standard.

I meant '74, I was THINKING '74, but wrote '72.
 
> 2) TRANSFORM was *not* a part of the '74 Standard (and I am not positive that
> it was even part of the '68 Standard).  I know of LOTS of IBM mainframe
…[5 more quoted lines elided]…
> LRM.)

I was converting code from Univac 9030 which was mostly in 1968, to an
IBM environment using 1974.  Instead of translating EXAMINE to INSPECT,
I chose to use the INSPECT command, figuring it was closer to the
meaning and it worked with both systems.  

When you advocated using this logic, I mentioned one time when I used it
(because I agree with it), but it bit me.
```

##### ↳ ↳ Re: Coding "to the Standard"

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<807aar$d32$1@aklobs.kc.net.nz>`
- **References:** `<804lhn$kh0$1@nntp4.atl.mindspring.net> <3826E730.385AC389@NOSPAMhome.com>`

```
Howard Brazee <brazee@nospamhome.com> wrote:
: William M. Klein wrote:

:> 1) I can't think of ANY good reason to use non-Standard syntax, when there is
:> .....
:> just don't have much sympathy for NEW development being limited to '74
:> Standard functionality.)

: I used this logic when I was in an environment which had both ANSI 68 &
: ANSI 72, replacing EXAMINE & INSPECT with TRANSFORM.  It backfired when
: TRANSFORM became obsolete.

But TRANSFORM was not ANSI68 _or_ ANSI74.  It was non-Standard
syntax that was an IBM extension. 
```

#### ↳ Re: Coding "to the Standard"

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NQrV3.143$Av4.5846@typhoon.columbus.rr.com>`
- **References:** `<804lhn$kh0$1@nntp4.atl.mindspring.net>`

```
>3) If there is "major" new functionality (non-Standard) that you want to
use,
>then it is always NICE if you can isolate it to a single routine
(paragraph,
>section, subprogram, copy-member - or whatever is most appropriate).  This
>would probably work for things like screen section vs other UI methodology.
>It almost certainly would NOT work for something like OO versus CALLs
(which
>are really "apples" and "oranges" but ...) Certainly if you have code that
>handles 9x file-status codes, I would try to isolate that into a single
>"place" in the program (or application) and not have it spread out
throughout
>the code.


This is a great standard. I used this in a REXX program on MVS. I then
proceded to port it to PC win95 REGINA to run on a PC. This was all done to
to enormous CPU usage and poor mainframe response time. IT took under an
hour to convert 4 REXX programs and get them running on the PC.

All this because I isolated the platform specific calls to there own
PARAGRAPHS, to use the COBOL term.

The above statement made by Bill Klein holds true for any language. Whether
you expect it to be ported to another platform or not.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
