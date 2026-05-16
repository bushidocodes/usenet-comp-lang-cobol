[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LOCAL-STORAGE as an efficiency measure?

_9 messages · 5 participants · 2002-06_

---

### LOCAL-STORAGE as an efficiency measure?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2002-06-11T10:55:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D0639A8.99AEA6AA@attglobal.net>`

```
Has anyone ever heard that LOCAL-STORAGE could improve efficiency of a
COBOL program?

I'm working in the IBM mainframe arena, with non-Object Oriented COBOL
programs.  A standard is proposed that says to add LOCAL-STORAGE to
every program, and to move "variables" from WORKING-STORAGE to
LOCAL-STORAGE, while leaving "constants" in WORKING-STORAGE.  VALUE
clauses are to be removed from the "variables", and any existing
"initialization" logic (procedure statements is how I read this) that
sets a value for these items will be deleted.

When I read about LOCAL-STORAGE, I'm bothered by this proposal for
several reasons.
1.  LOCAL-STORAGE is part of the OO language additions made by IBM to
mainframe compilers in advance of these being an adopted standard for OO
COBOL.  To me, this means the LOCAL-STORAGE construct is "non-standard",
and could change, or even disappear, from COBOL.  Also, if a shop wishes
to prohibit use of OO constructs, the compilers offer an option to
accomplish this - WORD(NOOO) - but if this were used, LOCAL-STORAGE
would be disallowed.
2.  In the COBOL for OS/390 & VM Language Reference manual,
LOCAL-STORAGE is described as being "...allocated and freed on a
per-invocation basis.  On each invocation, data items defined ... are
reallocated and initialized to the value assigned in their VALUE
clauses."  This seems to be slower than using WORKING-STORAGE, if
accurate.  However, a test I wrote (where a driver calls a subroutine 1
million times - both non-OO) seems to show that this is not how the
mainframe compiler operates.  A Storage Report after execution did not
show any significant amount of allocation and freeing of storage in the
heap, on the stack, or elsewhere.
3.  Removing VALUE clauses from the "variables" seems downright dumb in
at least some cases.  For example, say I have a counter for the number
of records read and written while processing files.  It seems intuitive
to give these items a value of zero and add to them, without any
initialization logic.  If they really got reallocated, how could I use
them for counting anyway?  On the other hand, if I have a subroutine
which will calculate a present value, I probably wouldn't expect the
target variable to have any initial value.  But what advantage would I
get from locating such a variable in LOCAL-STORAGE versus
WORKING-STORAGE?

This makes me wonder if the proposal I'm reading is what the writer
intended?

Any opinions?
Thanks,
Colin
```

#### ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-06-11T23:08:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2119c$6a3abd40$9491f243@chottel>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net>`

```
LOCAL-STORAGE is not just for OO programming.  There is an example in the
programmer's guide of using LOCAL-STORAGE to implement recursion (factorial
I believe).  Each time the program CALL's itself the current L-S is pushed
on a stack and the new invocation receives a fresh L-S.  Once each 
recusion level ends the L-S is popped of the stack. I do not see how the
proposed use of L-S could be faster than using regular W-S.  I also agree
that some form of variable initialization makes more sense. 

If your driver called a subroutine you probably just got one copy of W-S
and L-S and then returned.  One extra L-S per call is not much extra
overhead.

Exactly what problem is this meant to address?  I tend to doubt that it is
a real problem.  One time initialization (VALUE clauses or executable
statements) does not typically use much space or take much time.  This
sounds to me like a solution looking for a problem.  Your research and
reasoning indicates to me that you are on the right track and your concerns
seem valid to me.

Here is the program from the programmer's guide:

 
CBL nocmpr2,pgmn(lu)
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\ Recursive Program - Factorials
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 Identification Division.
 Program-Id. factorial recursive.
 Environment Division.
 Data Division.
 Working-Storage Section.
�1  numb  pic 9(4)  value 5.
�1  fact  pic 9(8)  value �.
 Local-Storage Section.
�1  num  pic 9(4).
 Procedure Division.
move numb to num.
if numb = �
move 1 to fact
  else
subtract 1 from numb
  call 'factorial'
multiply num by fact
  end-if.
display num '! = ' fact.
  goback.
 End Program factorial.
Figure  8.  Storage Sections Example
Recursive
CALL's:  Main  1 2 3 4 5
------------------------------------
L-S  num  5  4  3  2  1  �
------------------------------------
W-S numb  5  4  3  2  1  �
fact  �  �  �  �  �  �
------------------------------------
Recursive
GOBACK's:  5  4  3  2  1 Main
------------------------------------
L-S  num  �  1  2  3  4  5
------------------------------------
W-S numb  �  �  �  �  �  �
fact  1  1  2  6  24 12�
------------------------------------


Colin Campbell <cmcampb@attglobal.net> wrote in article
<3D0639A8.99AEA6AA@attglobal.net>...
> Has anyone ever heard that LOCAL-STORAGE could improve efficiency of a
> COBOL program?
…[46 more quoted lines elided]…
>
```

#### ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-12T08:24:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D06F74A.22E76328@Azonic.co.nz>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net>`

```
Colin Campbell wrote:
> 
> Has anyone ever heard that LOCAL-STORAGE could improve efficiency of a
> COBOL program?

Working-Storage exists while the program is loaded, Local-Storage is
created when the sub-program is CALLed and is deleted on EXIT PROGRAM
(or GOBACK).  This means that in a program that is many modules being
CALLed and EXITed the total memory requirement is [slightly] less.

If main memory is a significant problem then this may save a few
milliseconds swap time.  Otherwise it just wastes CPU time in creating
and initialising heap storage.

In situations where the program is reentrant or serially-reusable or
threaded then there may be several copies of a 'Local-Storage' existing
at one time, one for each thread that is active in that program.  

> 1.  LOCAL-STORAGE is part of the OO language additions made by IBM to

It is not strictly part of OO as it is in other implementations (such as
MF) independently of OO.  Certainly OO may use it.


> 3.  Removing VALUE clauses from the "variables" seems downright dumb in
> at least some cases.  For example, say I have a counter for the number
…[3 more quoted lines elided]…
> them for counting anyway?  

If you expect the value to survive an EXIT PROGRAM and be available on
the next CALL then DO NOT put it LOCAL-STORAGE, it just won't work.

> This makes me wonder if the proposal I'm reading is what the writer
> intended?

Another clueless manager making technical decisions, or worse, accepting
a 'consultants' report intended to justify his charge out costs by
faking 'efficiencies' or 'savings'.
```

##### ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-11T22:35:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D067BA6.4911D4B4@shaw.ca>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz>`

```


Richard Plinston wrote:

> Colin Campbell wrote:
> >
> > Has anyone ever heard that LOCAL-STORAGE could improve efficiency of a
> > COBOL program?

Whether using Procedural or OO COBOL, the concept of Local-storage is for
'counters' etc., localized to a particular routine - overcomes the nightmare
where you have a counter, say 'n' in Working-Storage, and elsewhere in your
logic, the counter because of poor coding, gets 'changed'.

>
>
…[17 more quoted lines elided]…
>

OO DOES (not may use it). I can't think of too many methods where
Local-storage wouldn't be used, other than say setting a flag in global W/S
as follows :-

Assume following method results from a button click in your Dialog :-

Method-id. "ListboxByName".
*>---------------------------
*> Local-storage section - NOT used
Procedure Division.
    set wsByName to true
    invoke self "prepareListContents"
    invoke theDialog "showListContents" using os-Collection

End Method "ListboxByName".
*>--------------------------------

>
> > 3.  Removing VALUE clauses from the "variables" seems downright dumb in
…[8 more quoted lines elided]…
>

Local-storage results in variables having an 'initial state' each time the
method/function (non-OO User Defined Functions) are invoked. As Richard says,
you lose those values when you EXIT/END METHOD,
unless you have stored them in Working-Storage.

All is not lost. You can have an 'initial value' in Local-storage variables
by using the new (COBOL 2002) syntax - CONSTANT ( Level 78s in current Micro
Focus) :-

Local-storage Section.
01 aCounter    CONSTANT            value 10.
01 aName        CONSTANT            value "Mickey Mouse".

>
> > This makes me wonder if the proposal I'm reading is what the writer
…[4 more quoted lines elided]…
> faking 'efficiencies' or 'savings'.
```

###### ↳ ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-12T13:16:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D073BA4.BA637783@Azonic.co.nz>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz> <3D067BA6.4911D4B4@shaw.ca>`

```
James J. Gavan wrote:

> >   Certainly OO may use it.
> 
…[5 more quoted lines elided]…
> *> Local-storage section - NOT used

So you agree then that it _may_ use it, rather than it being
compulsory.   :)

In fact my 'Certainly OO may use it' is in the context of '.. it may be
implemented independently of OO'.  That is, OO using it does not make it
an 'OO feature'.

> All is not lost. You can have an 'initial value' in Local-storage variables
> by using the new (COBOL 2002) syntax - CONSTANT ( Level 78s in current Micro
…[4 more quoted lines elided]…
> 01 aName        CONSTANT            value "Mickey Mouse".

But that only makes them have the same value each time the routine is
invoked.  This would allow the constants to be moved to Local-Storage,
but doesn't solve the actual problem where, in the new 'standard',
variable data is required to be moved to local-storage regardless of
whether it must survive an EXIT PROGRAM/re-CALL or not.

If efficiency is measured as how many broken programs there are then the
directive will make the system very efficient.
```

###### ↳ ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-06-12T14:01:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae7jt8$lp3$1@peabody.colorado.edu>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz> <3D067BA6.4911D4B4@shaw.ca>`

```

On 11-Jun-2002, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Whether using Procedural or OO COBOL, the concept of Local-storage is for
> 'counters' etc., localized to a particular routine - overcomes the
> nightmare
> where you have a counter, say 'n' in Working-Storage, and elsewhere in
> your logic, the counter because of poor coding, gets 'changed'.

I've never had that nightmare.

I used something similar to local storage on a Univac 90-30.  All the
on-line programs were basically called, with standard storage in the Linkage
Division.  Anything in Working Storage was vulnerable - if we used it it was
only for constants.
```

###### ↳ ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-13T07:59:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D0842D9.CE5BEE1E@Azonic.co.nz>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz> <3D067BA6.4911D4B4@shaw.ca>`

```
James J. Gavan wrote:
> 
> Whether using Procedural or OO COBOL, the concept of Local-storage is for
> 'counters' etc., localized to a particular routine - overcomes the nightmare
> where you have a counter, say 'n' in Working-Storage, and elsewhere in your
> logic, the counter because of poor coding, gets 'changed'.

While that may be true for 'local variables' in general, it is not
necessarily an advantage of LOCAL-STORAGE over WORKING-STORAGE in a
Cobol program.  For each invocation of a routine there is only one W-S
and one L-S.  Apart from initialisation and permanancy issues there is
no distinction between these.  If a program is in a PERFORM loop using a
counter and it PERFORMs another paragraph which overwrites the counter
there is no difference whether this is W-S or L-S.

In the case of nested procedures, they can have their own 'local'
Working-Storage which does act as you describe.

The significant distinction of LOCAL-STORAGE is where there is recursion
or re-entrancy, such as in a Windows API program.  In this case the
program may effectively be 'active' in several places at one time (due
to call backs).  There would then be several copies of Local-Storage
existing, one for each copy.  Corruption of 'counters in W-S' would not
be the result of poor coding as such, but of two copies of the PERFORM
executing at the same time.
```

###### ↳ ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-13T05:23:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D082CBF.E14FF96B@shaw.ca>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz> <3D067BA6.4911D4B4@shaw.ca> <3D0842D9.CE5BEE1E@Azonic.co.nz>`

```


Richard Plinston wrote:

> James J. Gavan wrote:
> >
…[22 more quoted lines elided]…
> executing at the same time.

Picky, picky Richard <G>. The 'counter' was an example, could have been a flag
setting or even a Customer name, which inadvertently gets changed. Remember my
comments below are not 'universal', as I don't try and wear two hats - restricting
myself to OO syntax (classes not programs).

I really did dislike in DOS days have humungous Working-Storage areas containing
heaps of variables - even where you tried to create some order, alphabetizing the
entries etc - still found myself constantly taking a look at W/S to see what I had
called what.

Yes I still have a considerable number of copy files, listed under W/S, but much
of the remainder gets included in Local-storage, which means I can concentrate on
the significance of those variables at the time they are being coded.

Let's go back to my original example, and YES ! This version *DOES* use L/S <G> :-

Method-id. "ListboxByName".
*>---------------------------
Local-storage section.
01 SequenceFlag                        pic 9.
    88 ByName                            value 1.
    88 ByPrimeKey                      value 2.
    88 ByOther                             value 3.
Procedure Division.
    set ByName to true
    invoke self "prepareListContents" using SequenceFlag
    invoke theDialog "showListContents" using os-Collection

End Method "ListboxByName".
*>--------------------------------

Given the previous example the SequenceFlag had to be in global W/S - the danger
there, I might be producing three different lists, and if not careful in coding,
the sequence could be 'disturbed' so that when used later, (say accessing a
record, where ByName indicates 'name' is in positions x to y of the list record.
etc...).

Note this 'local' approach also necessitates the above method passing the
SequenceFlag to "PrepareListContesnts". The alternative, retain the SequenceFlag
in W/S, but given three lists, do SequenceFlag as occurs 3 - but that necessitates
the rather cumbersome construct :-

        set ByName of SequenceFlag (n) to true

Here's another interesting example, "localizing" - rather than have a series of
Tables in W/S, which, like comment above, would necessitate searching back in W/S
to check out - the code and table is 'localized".

C08PIWE   C-BAND ON  8 IN. PIPE (west end)
C08PR06    C-BAND ON  8 IN. PART of a  8 x  6 REDUCER
C10NZ       C-BAND ON 10 IN. NOZZLE

None of the above descriptions are held in either files or DBs.  The eight
character *meaningful* mnemonic generates descriptions required. This shows how
"(west end)"  is accessed for a pipe, indicated by numerics in (2:2)  :-

*>------------------------------------------------------------
Method-id. "pipe-suffix".
*>--------------------------------------------------------------
Working-storage section.
78 s-Kount                       value 19.
01 ws1.                *> see PS at the bottom --->
   05 pic x(20) value "B  ,(bottom)~       ".
   05 pic x(20) value "BN ,BEND~           ".
   05 pic x(20) value "EE ,(east end)~     ".
   05 pic x(20) value "ES ,(east side)~    ".
   05 pic x(20) value "NE ,(north end)~    ".
   05 pic x(20) value "NS ,(north side)~   ".
   05 pic x(20) value "O  ,(outlet)~       ".
   05 pic x(20) value "SE ,(south end)~    ".
   05 pic x(20) value "SS ,(south side)~   ".
   05 pic x(20) value "T  ,(top)~          ".
   05 pic x(20) value "WE ,(west end)~     ".
   05 pic x(20) value "WS ,(west side)~    ".

   05 pic x(20) value "AN ,(around nozzle)~".
   05 pic x(20) value "AF ,(above flange) ~".
   05 pic x(20) value "AR ,(above roof)~   ".
   05 pic x(20) value "BF ,(below flange)~ ".
   05 pic x(20) value "BR ,(below roof)~   ".
   05 pic x(20) value "M  ,(middle)~       ".
   05 pic x(20) value "NXW,(next to weld)~ ".
                                1         2         3         4
                       1234567890123456789012345678901234567890

01 ws-2 redefines ws1.
   05 ws3 occurs s-kount.
      10 ws-key          pic x(03).
      10                 pic x(01).
      10 ws-name         pic x(16).

01 n                     pic x(4) comp-5.

Linkage section.
01 lnk-key4              pic x(04).

Procedure Division using lnk-key4.

  perform varying n from 1 by 1
     until ws-text-suffix <> spaces or n > s-Kount

     if lnk-key4 = ws-key(n)
        move ws-name(n) to ws-text-suffix
     End-if
  End-perform

  if ws-text-suffix = spaces
     evaluate true
       when ItemSubNamesFound
            set suffix-string to true
            invoke self "read-file" using lnk-key4
       when other
            set OtherNotFound to true
     End-evaluate
  End-if

End Method "pipe-suffix".
*>--------------------------------------------------------------

Having got the various elements that make up the description then I STRING them
together to create a 40 character description. Note - M/F doesn't recommend this
type of usage for L/S - but by golly it sure works ! Is the performance lousy - No
- key in the mnemonic for a new Item and the description pops up immediately on
the screen ! (The other reason for doing this - the old MSDOS application used to
hold descriptions for "every* item - storage wise that meant a 40-character
description, times an average of 300 items per plant, times - wait for it - 700
different client/plant combinations !)

PS:  Above use of W/S in methods is disallowed in COBOL 2002 - hopefully they will
introduce CONSTANT syntax at the 01 Group Level which would allow the above W/S to
be called L/S. (Meanwhile - fingers crossed - M/F will continue to provide
backwards compatibility).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: LOCAL-STORAGE as an efficiency measure?

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-06-13T12:55:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aea4dd$4b$1@peabody.colorado.edu>`
- **References:** `<3D0639A8.99AEA6AA@attglobal.net> <3D06F74A.22E76328@Azonic.co.nz> <3D067BA6.4911D4B4@shaw.ca> <3D0842D9.CE5BEE1E@Azonic.co.nz> <3D082CBF.E14FF96B@shaw.ca>`

```

On 12-Jun-2002, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> I really did dislike in DOS days have humungous Working-Storage areas
> containing
…[3 more quoted lines elided]…
> what I had called what.

For me DOS days meant before our IBM 360 went to OS.  When IBM mainframes
caught up with the other mainframes by inventing virtual memory, I stopped
worrying about variables.  Instead of having a generic index, my subscript
variable had a name which made it obvious that I was referring to one
particular table.  Adding on a dozen unique variable names was virtually
free - and safer than worrying whether something else used it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
