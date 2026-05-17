[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with MF run units

_5 messages · 4 participants · 1995-06_

---

### Problem with MF run units

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3rn5ru$ev0@wrdis02.robins.af.mil>`

```
I'm having some difficulty with the "CBL_EXEC_RUN_UNIT" call in
Microfocus. The call works fine in DOS/Windows, but when the same code
is moved to Solaris 2.3 and turned into a .gnt, the next screen after
the call is all screwed up.

All I have found out so far is that running the code in the animator
causes the following error to occur and return to the screen in one
example:

Execution error : file 'animator.lbr/animatorx.gnt'
error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 11)

and the following error in another example:

Execution error : file 'cobkeymp'
error code: 166, pc=0, call=20, seg=0
166 Recursive COBOL CALL is illegal

In both cases, the return code from the call is zero, and the
background job kicks off and runs properly, it just messes up the
screen in either animator or when run from the .gnt. It appears that
outside the animator, the errors are still being generated, but they
only appear as line feeds that cause ADIS to mess up. Forcing a screen
refresh doesn't help.

If the CBL_EXEC_RUN_UNIT call is replaced with a call "system" using
the same command line with "cobrun " prepended, the background job
executes properly and the screens work properly.

Any ideas?

Thanks in advance...
Jon R. Wilson
jwi··.@b85··f.mil
```

#### ↳ Re: Problem with MF run units

- **From:** "jo..." <ua-author-17087624@usenetarchives.gap>
- **Date:** 1995-06-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c5bbdfb74-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3rn5ru$ev0@wrdis02.robins.af.mil>`
- **References:** `<3rn5ru$ev0@wrdis02.robins.af.mil>`

```
Jon R. Wilson (jwi··.@b85··f.mil) wrote:
› I'm having some difficulty with the "CBL_EXEC_RUN_UNIT" call in
› Microfocus. The call works fine in DOS/Windows, but when the same code
› is moved to Solaris 2.3 and turned into a .gnt, the next screen after
› the call is all screwed up.
 
› All I have found out so far is that running the code in the animator
› causes the following error to occur and return to the screen in one
› example:
 
› Execution error : file 'animator.lbr/animatorx.gnt'
› error code: 114, pc=0, call=1, seg=0
› 114     Attempt to access item beyond bounds of memory (Signal 11)

[other example deleted]

I got this error when trying to animate a module with MF 3.2 after upgrading
form MF 3.1 on SINIX (from SNI). As there is no CBL_EXEC_RUN_UNIT in this
module, i suspect a general error in MF 3.2 . Are You using MF 3.2 ?

Joerg Ahrens
```

##### ↳ ↳ Re: Problem with MF run units

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-06-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c5bbdfb74-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9c5bbdfb74-p2@usenetarchives.gap>`
- **References:** `<3rn5ru$ev0@wrdis02.robins.af.mil> <gap-9c5bbdfb74-p2@usenetarchives.gap>`

```
jo··.@kph··n.de (Joerg Ahrens) wrote:

› Jon R. Wilson (jwi··.@b85··f.mil) wrote:
 
›› Execution error : file 'animator.lbr/animatorx.gnt'
›› error code: 114, pc=0, call=1, seg=0
›› 114     Attempt to access item beyond bounds of memory (Signal 11)
 
› [other example deleted]
 
› I got this error when trying to animate a module with MF 3.2 after upgrading
› form MF 3.1 on SINIX (from SNI). As there is no CBL_EXEC_RUN_UNIT in this
› module, i suspect a general error in MF 3.2 . Are You using MF 3.2 ?

Yep.

Here is the version info from $COBDIR/cobver:
(to answer someone elses question about determining MF version in
Unix.)

cobol v3.2.20-e
PRN=2XUNS/ZZF:7a.1a.11.01
PTI=NLS

I have also been told that this version is 9 updates behind, which is
odd considering we purchased MF directly from them around January.

I'm trying to get the lastest from them to see if the changes fix the
problem.


Jon R. Wilson
jwi··.@b85··f.mil
```

##### ↳ ↳ Re: Problem with MF run units

- **From:** "ggra..." <ua-author-17087605@usenetarchives.gap>
- **Date:** 1995-06-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c5bbdfb74-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9c5bbdfb74-p2@usenetarchives.gap>`
- **References:** `<3rn5ru$ev0@wrdis02.robins.af.mil> <gap-9c5bbdfb74-p2@usenetarchives.gap>`

```
Joerg Ahrens (jo··.@kph··n.de) wrote:
: Jon R. Wilson (jwi··.@b85··f.mil) wrote:
: >I'm having some difficulty with the "CBL_EXEC_RUN_UNIT" call in
: >Microfocus. The call works fine in DOS/Windows, but when the same code
: >is moved to Solaris 2.3 and turned into a .gnt, the next screen after
: >the call is all screwed up.

: >All I have found out so far is that running the code in the animator
: >causes the following error to occur and return to the screen in one
: >example:

: >Execution error : file 'animator.lbr/animatorx.gnt'
: >error code: 114, pc=0, call=1, seg=0
: >114 Attempt to access item beyond bounds of memory (Signal 11)

: [other example deleted]

: I got this error when trying to animate a module with MF 3.2 after upgrading
: form MF 3.1 on SINIX (from SNI). As there is no CBL_EXEC_RUN_UNIT in this
: module, i suspect a general error in MF 3.2 . Are You using MF 3.2 ?

: Joerg Ahrens

We (at work) have a similar problem (a bit strange tho).
We have two copies of MF, running on two different 6000s. One reports
it's version as being 3.257 (using cob -V), the other reports itself
as being 1.29 ... odd thing is they are both suppose to be 3.2, the
one that reports itself as being 3.257 has from time-to-time (no repeatible)
the above error. The one that reports itself as 1.29 does and has compiled
everything I've thrown at it including dynamic memory allocations and
TYPEDEF's ... ?

Anyone know a feature set to check for to confirm a 3.2 compiler?

Another interesting bug I found, was if you don't leave a blank line
between a data element and a copy command, the code generated will be
truely messed up (it will run, but be very confused) ... put the blank
line in and all is as expected.
```

###### ↳ ↳ ↳ Re: Problem with MF run units

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-06-27T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9c5bbdfb74-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9c5bbdfb74-p4@usenetarchives.gap>`
- **References:** `<3rn5ru$ev0@wrdis02.robins.af.mil> <gap-9c5bbdfb74-p2@usenetarchives.gap> <gap-9c5bbdfb74-p4@usenetarchives.gap>`

```

In article <3s3v4u$m.··.@new··s.net>, ggr··.@cyb··s.net (Greg Granger) writes:
› We have two copies of MF, running on two different 6000s.  One reports
› it's version as being 3.257 (using cob -V), the other reports itself
› as being 1.29 ... odd thing is they are both suppose to be 3.2,
› [snip]
› Anyone know a feature set to check for to confirm a 3.2 compiler?

cat $COBDIR/cobver

You should see a line something like "cobol v3.2.xx" where "xx" is the specific
build number (the base 3.2 release is not neccessarily 0 or 1) which is
incremented for each update release.

The numbers you saw were probably version numbers of individual components.

Cheers,
Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
