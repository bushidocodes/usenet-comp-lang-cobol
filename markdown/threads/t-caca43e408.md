[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu error handling

_6 messages · 4 participants · 1998-10 → 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu error handling

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71d09m$a7b$1@news.igs.net>`

```
I am converting some code from MF to Fujitsu,
and I am try to save myself some work.  The problem
is the default error handling on files.  On MF, once
you declare a file status, the run time will simply
return it on errors. Under Fujitsu, the built in error
handling still cuts in unless you put in a declaratives
section.

I can make the code behave pretty well the same
by putting in a declarative use statement for every
file that consists of an exit statement, but was
wondering if anybody knew of a compiler directive
that does the same thing.  That would make life much
easier.
```

#### ↳ Re: Fujitsu error handling

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981030164831.28289.00001321@ng76.aol.com>`
- **References:** `<71d09m$a7b$1@news.igs.net>`

```
The behavior you describe for MF compilers is identical to what I see with IBM
mainframe COBOL-85 compilers.  I do not know the standards on this issue, but
the synchrony of MF and IBM seems to suggest that the present of the
FILE-STATUS phrase should thence forth intercept all error handling and utterly
disengage the default error handling.

(It is a fact that this is a source of some big surprises in the supposed easy
migration from COBOL-74 to COBOL-85).

Any way, my question is, are both MF and Fujitsu claiming to be COBOL-85?  Is
there a switch for your target Fujitsu tool that looks something like '1985
standard' instead of the specific syntax issue you have first encountered (FILE
STATUS)? Hope that helps in your search for a parm.

Another idea from migration experience may help, but from you description I
doubt it.
In our experience coding FILE STATUS did disable the default error handling all
over the place, but this created problems for poorly migrated modules in spots
that had no error checking or lacked exhaustive error checking.  
(the problem was unexpected fallthru in places that used to cause abends; hard
to detect in testing because the coditions rarely happened).
 
I could imagine a vendor trying to compensate for this, by re-engaging default
error handling in statements that appear to lack exhaustive checks. It would be
too ambitious to try that with a scope of a paragraph, much less a whole
program.

But one could image some well intentioned (if misguided) attempts to catch
READS without AT END clauses, or perhaps some READS lacking INVALID KEY
clauses.

In other words the default error handling may not be fully re-engaged. There
may just be specific compensation in certain places according to some 'scheme'
that is less than obvious.

Some compilers have 'migrate' options. That try to bridge semantics for you. I
have never seen a discription of one that involves partial engagement of file
error handling, however.

Nonetheless, there is one compensation that would not be misguided at all. This
is very comparable to a global optimization.  If you code the FILE-STATUS
phrase, but never reference the field, then (speaking in simple terms) the
compiler is justified in assuming you are in trouble. I do not know if the
standard addresses this. But a defensive response by the compiler is
justifyable, according to a certain way of thinking.

One other thought, and don't be offended at the simplicity of this. It helps to
look even for simple possibilities.  Have you specified FILE STATUS for every
single file in the program?  Iif you have CALLs, then for every single file in
the run unit? Yes, I know you probably looked for that ;-).

(( Grasping at the thinest of straws, have you checked that every file has a
FILE-STATUS phrase and that the object field of that phrase is referred to
atleast once in the program.))

(((Grasping at shear ether, have you check to see if you are getting a strange
effect from oprimization. Code can be eliminated, even entire paragraphs can be
considered unexecutable.  You got any of those? IF such a things gets optimized
out, AND it is the only source code with reference to the FILE-STATUS field,
then it goes numb, and the compiler could get defensive.  Have you tried
shunting all possible optimization?)))

I certainly empathize with you, it seems a rude imposition to have to intruduce
declaratives for this.  Was this known when Fujitsu was selected as the tool?
Is there still time to panic, or is it too late?



 

Robert Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: Fujitsu error handling

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71dfjd$jfd$1@news.igs.net>`
- **References:** `<71d09m$a7b$1@news.igs.net> <19981030164831.28289.00001321@ng76.aol.com>`

```
RKRayhawk wrote in message <19981030164831.28289.00001321@ng76.aol.com>...

I will check and see if there is an 85-standard type of switch, that well
may do
the trick.  I appreciate your advise re ending up with a bunch of unchecked
errors, but I know that will not be a problem.  The code has been running
for 18 years now, 12 hours per day, in 75 installations. Every file access
is contained in the same copy that goes into a real tight loop displaying my
phone number whenever an unexplained error status occurs. I can recite
"code 39 means exit to DOS, run the error recovery, and restart" without
waking up at night.<G>  In fact, I had to change some code a bit to test it,
and
was a bit startled to have that damned windows box jump up and inform
me that I had a share error. (continue yes/no).  I fixed it for the test
case
with declaratives, but really do not want to have to go in and change over
a hundred programs with declaratives that are complete no-ops, unless
there is no easy way.

>The behavior you describe for MF compilers is identical to what I see with
IBM
>mainframe COBOL-85 compilers.  I do not know the standards on this issue,
but
>the synchrony of MF and IBM seems to suggest that the present of the
>FILE-STATUS phrase should thence forth intercept all error handling and
utterly
>disengage the default error handling.
>
>(It is a fact that this is a source of some big surprises in the supposed
easy
>migration from COBOL-74 to COBOL-85).
>
>Any way, my question is, are both MF and Fujitsu claiming to be COBOL-85?
Is
>there a switch for your target Fujitsu tool that looks something like '1985
>standard' instead of the specific syntax issue you have first encountered
(FILE
>STATUS)? Hope that helps in your search for a parm.
>
>Another idea from migration experience may help, but from you description I
>doubt it.
>In our experience coding FILE STATUS did disable the default error handling
all
>over the place, but this created problems for poorly migrated modules in
spots
>that had no error checking or lacked exhaustive error checking.
>(the problem was unexpected fallthru in places that used to cause abends;
hard
>to detect in testing because the coditions rarely happened).
>
>I could imagine a vendor trying to compensate for this, by re-engaging
default
>error handling in statements that appear to lack exhaustive checks. It
would be
>too ambitious to try that with a scope of a paragraph, much less a whole
>program.
…[5 more quoted lines elided]…
>In other words the default error handling may not be fully re-engaged.
There
>may just be specific compensation in certain places according to some
'scheme'
>that is less than obvious.
>
>Some compilers have 'migrate' options. That try to bridge semantics for
you. I
>have never seen a discription of one that involves partial engagement of
file
>error handling, however.
>
>Nonetheless, there is one compensation that would not be misguided at all.
This
>is very comparable to a global optimization.  If you code the FILE-STATUS
>phrase, but never reference the field, then (speaking in simple terms) the
…[4 more quoted lines elided]…
>One other thought, and don't be offended at the simplicity of this. It
helps to
>look even for simple possibilities.  Have you specified FILE STATUS for
every
>single file in the program?  Iif you have CALLs, then for every single file
in
>the run unit? Yes, I know you probably looked for that ;-).
>
>(( Grasping at the thinest of straws, have you checked that every file has
a
>FILE-STATUS phrase and that the object field of that phrase is referred to
>atleast once in the program.))
>
>(((Grasping at shear ether, have you check to see if you are getting a
strange
>effect from oprimization. Code can be eliminated, even entire paragraphs
can be
>considered unexecutable.  You got any of those? IF such a things gets
optimized
>out, AND it is the only source code with reference to the FILE-STATUS
field,
>then it goes numb, and the compiler could get defensive.  Have you tried
>shunting all possible optimization?)))
>
>I certainly empathize with you, it seems a rude imposition to have to
intruduce
>declaratives for this.  Was this known when Fujitsu was selected as the
tool?
>Is there still time to panic, or is it too late?
>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fujitsu error handling

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298304.62732.14896@kcbbs.gen.nz>`
- **References:** `<71dfjd$jfd$1@news.igs.net>`

```
In message <<71dfjd$jfd$1@news.igs.net>> "Donald Tees" <donald@willmack.com> writes:

> for 18 years now, 12 hours per day, in 75 installations. Every file access
> is contained in the same copy that goes into a real tight loop displaying my
> phone number whenever an unexplained error status occurs. I can recite

I trust that the 'tight loop' includes an OS despatch in every
cycle (DOS INTx2F,AX=x1680 or Windows PeekMessage or equivalent).
```

###### ↳ ↳ ↳ Re: Fujitsu error handling

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71ifh3$42s$1@news.igs.net>`
- **References:** `<71dfjd$jfd$1@news.igs.net> <3298304.62732.14896@kcbbs.gen.nz>`

```

Richard Plinston wrote in message <3298304.62732.14896@kcbbs.gen.nz>...
>In message <<71dfjd$jfd$1@news.igs.net>> "Donald Tees"
<donald@willmack.com> writes:
>
>I trust that the 'tight loop' includes an OS despatch in every
>cycle (DOS INTx2F,AX=x1680 or Windows PeekMessage or equivalent).


That depends on the error.  And not under DOS, after all that is
a single user system, and a display by itself has a hook.  Under
Windows 95, I have a programmed 500 millisecond delay for sharing
errors, but lock up tighter than a drum if the files are damaged
structurally(and quite deliberately).  I do not want the user doing
*anything* further until the files are rebuilt.
```

##### ↳ ↳ Re: Fujitsu error handling

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-OzTJOzCeeWxL@Dwight_Miller.iix.com>`
- **References:** `<71d09m$a7b$1@news.igs.net> <19981030164831.28289.00001321@ng76.aol.com>`

```
On Fri, 30 Oct 1998 21:48:31, rkrayhawk@aol.com (RKRayhawk) wrote:

> The behavior you describe for MF compilers is identical to what I see with IBM
> mainframe COBOL-85 compilers.  I do not know the standards on this issue, but
…[3 more quoted lines elided]…
> 

Maybe in a perfect world.

However, in reality the IBM and MicroFocus compilers violate the COBOL
standard in this respect, where Fujitsu does not.

The PRESENT standard requires either coding Invalid Key or 
Declaratives - one of the two is required.

That said - Fujitsu has a simple runtime option to turn of the 
reporting of the offending errors, and it will behave as you describe 
the others behaving.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
