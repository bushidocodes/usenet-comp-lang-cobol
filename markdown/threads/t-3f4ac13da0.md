[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM CICS - CBLPSHPOP and recursive programs

_7 messages · 3 participants · 2007-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM CICS - CBLPSHPOP and recursive programs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-06T21:54:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com>`

```
I may have already asked this here, but I was wondering if any of the CICS sites 
that are current for COBOL (and LE) have tried both run-time settings for 
CBLPSHPOP with RECURSIVE programs.  (Frank, as I recall, VSE COBOL doesn't have 
that yet - but I could be mistaken). I know that lots of "modern" CICS doesn't 
use HANDLE CONDITIONS - but this does seem like something that SOMEONE must have 
tried by now - but I can't find out either how it does work or how IBM thinks it 
SHOULD work.
```

#### ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-06T21:14:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3qc1e31bv30mt7ha23l81so4qqpnbir9mk@4ax.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com>`

```
On Thu, 06 Sep 2007 21:54:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>I may have already asked this here, but I was wondering if any of the CICS sites 
>that are current for COBOL (and LE) have tried both run-time settings for 
…[4 more quoted lines elided]…
>SHOULD work.

It shouldn't work. The error handler of the deepest recursion will be in effect when the
error happens. If it is not the current stack frame, LE will recognize that and issue an
ASRA.
```

##### ↳ ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-07T16:27:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JZeEi.112021$nT6.107340@fe03.news.easynews.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com> <3qc1e31bv30mt7ha23l81so4qqpnbir9mk@4ax.com>`

```
Robert,
  I assume that you are back to answering questions for an O/S and compiler that 
you don't use and haven't used (since 1998-2001).  I was hoping that someone who 
actually had ACCESS to such an environment (or had even worked in it) might 
answer.
```

#### ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-07T10:10:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46E12388.6F0F.0085.0@efirstbank.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com>`

```
VSE has CBLPSHPOP but does not support recursive programs.

We have CBLPSHPOP(ON) and have never tried turning it off.

What exactly are you looking for?

n 9/6/2007 at 3:54 PM, in message
<_F_Di.49591$M%1.4528@fe10.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
> I may have already asked this here, but I was wondering if any of the 
> CICS sites 
> that are current for COBOL (and LE) have tried both run-time settings for

> 
> CBLPSHPOP with RECURSIVE programs.  (Frank, as I recall, VSE COBOL 
…[7 more quoted lines elided]…
> SHOULD work.
```

##### ↳ ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-07T16:42:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PbfEi.55122$M%1.12629@fe10.news.easynews.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com> <46E12388.6F0F.0085.0@efirstbank.com>`

```
What I am interested in is what happens with HANDLE CONDITIONS in a recursive 
environment (which you don't have)

A sets some condition handling
A calls b (which sets its own condition handling)
B calls A (recursive)
   - what is the status of condition handling in A at this point?
A sets DIFFERENT condition handling
A returns to B
B returns to A
 - what conditions (if any) are set at this point?

CBLPSHPOP is documented as handling (or not depending on setting) the "storing" 
and "restoring" of conditions in non-recursive situations - but I have asked my 
contacts in COBOL, LE, and CICS - and no one has answered as to what happens 
with this type of situation. I *think* that with CBLPSHPOP on, that each 
"instance" of A should have its own condition handling so that on the return to 
A, the original settings should be restored - and that on the "recursive" entry 
none should be set.  I think that with NOCBLPSHPOP, that on each entry (or 
return) to A, that no conditions will be set.

P.S.  Unlike what RW indicated, standard z/OS LE condition handling has always 
been able to handle recursive programs - as PL/I and C/C++ have always needed 
this.  I just don't know if CBLPSHPOP was (or had to be) modified to handle it 
for COBOL under CICS (under  z/OS)
```

###### ↳ ↳ ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-07T22:13:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<igr3e3hoog5ce71l7upp94qkdf87d2o9f3@4ax.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com> <46E12388.6F0F.0085.0@efirstbank.com> <PbfEi.55122$M%1.12629@fe10.news.easynews.com>`

```
On Fri, 07 Sep 2007 16:42:24 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>What I am interested in is what happens with HANDLE CONDITIONS in a recursive 
>environment (which you don't have)
…[4 more quoted lines elided]…
>   - what is the status of condition handling in A at this point?

It is set to A's error handlers.

>A sets DIFFERENT condition handling
>A returns to B
>B returns to A
> - what conditions (if any) are set at this point?

The second instance of A.

>CBLPSHPOP is documented as handling (or not depending on setting) the "storing" 
>and "restoring" of conditions in non-recursive situations - but I have asked my 
…[3 more quoted lines elided]…
>A, the original settings should be restored - 

If condition handlers were automatically restored on return from call, as they are for
LINK, there would be no reason to EVER issue a push or pop handle.

>and that on the "recursive" entry 
>none should be set.  I think that with NOCBLPSHPOP, that on each entry (or 
>return) to A, that no conditions will be set.

That's what C does. LE thinks CEESTART and all its callees are a single program. No so
with Cobol. Even though caller and callee are in the same CICS/LE call stack frame, LE
knows they are separate programs. The important question here is how it knows.

I seriously doubt that none would be set. Cobol doesn't know whether or not you explicitly
called PUSH HANDLE, thereby turning off all handlers.  That's *why* C doesn't let you call
PUSH HANDLE .. because it's going to bypass HANDLE CONDITIONs on recursion.

>P.S.  Unlike what RW indicated, standard z/OS LE condition handling has always 
>been able to handle recursive programs - as PL/I and C/C++ have always needed 
>this.  I just don't know if CBLPSHPOP was (or had to be) modified to handle it 
>for COBOL under CICS (under  z/OS)

If an error occurs in B and CICS tries to call a handler in A, LE will detect a cross
program call and abort the process. 

If an error occurs in A and CICS tries to call a handler in B, same thing.

What happens when an error occurs in A(1) and the last handler was registered by A(2)? I
believe LE will think they are two programs. I doubt it checks same program by comparing
names; it's much more likely it defines a program by its base stack pointer.
```

#### ↳ Re: IBM CICS - CBLPSHPOP and recursive programs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-08T03:41:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4SoEi.31011$qQ1.3111@fe05.news.easynews.com>`
- **References:** `<_F_Di.49591$M%1.4528@fe10.news.easynews.com>`

```
FYI,
  The following is the answer that I just got from my "usually reliable" source 
within IBM.  (Slightly edited to protect the guilty <G>)

"I asked around, and we would PUSH on RECURSIVE calls just as we would on a 
non-recursive call. A->B->C would
have the same PUSH/POP behavior as A->B->A. PUSH on CALLS, POP on returns. If B 
changed the condition handling environment, then it would be saved and restored. 
Whoever B calls would have a new environment, we think. You only get an old 
environment on a return.

For CBLPSHPOP(OFF) we would not save and restore the condition handling 
environment."

This is pretty much what I expected (with the possible exception of the status 
on the entry to the second instance of "A".  I just wasn't certain whether this 
would or wouldn't have any setting - with CBLPSHPOP(ON).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
