[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM VS COBOL II - Language Environment problem

_9 messages · 6 participants · 2003-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM VS COBOL II - Language Environment problem

- **From:** ad.tromp@abp.nl (Ad Tromp)
- **Date:** 2003-09-17T06:37:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
Hello IBM COBOL specialists out there!

We have a very specific problem in our conversion from the IBM VS
COBOL II run-time library to IBM Language Environment. At the moment
we are trying to do this by the STEPLIB approach: adding SCEERUN to
the job, without recompiling and do some regression testing.
In our ï¿½old' VS COBOL II programs (ï¿½ 6000 load modules) we do a CALL
to an Assembler program to set the program mask (bits 20 and 21), so
we get an abend 0CA in case of decimal overflow. We do NOT use the
ON-SIZE-ERROR clause in our programs, but rely on the ï¿½change program
mask' method, ï¿½invented' by our system programmers many, many years
ago!
When we add the SCEERUN dataset to the STEPLIB we never get any 0CA
abend in case of a decimal overflow. This is NOT what we want.
To prevent a complete conversion of our old COBOL sources (add the
ON-SIZE-ERROR clause in every ADD, COMPUTE..?) here is my question: Is
there any other way to solve this decimal overflow problem when using
Language Environment, at the best, without code changes or
recompiling?

Thank you very much,

Ad Tromp
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-17T17:31:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030917133139.03448.00000982@mb-m11.aol.com>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
Just a hunch. 

You might be able to continue with your special technology. The runtime
environment is intercepting your execution flow at known points. 
 
It is stomping on your setting in the mask at those points.  If your
application is calling the helper too infrequently, you lose.

You might be able to put in more calls to the helper routine (that will require
source code change, if it is a viable option at all).

The runtime is monitoring your calls to all old style COBOL service modules. It
intercepts them and vectors to replacements. That means that it is intimate
with your code.

Yet, maybe, the only thing you are concerned about is the intercepts that occur
when you CALL one of your own subprograms. 

Placing calls to your helper in all submodules may help (after each entry
point), but actually the return may be mediated by the imposing technology as
well, and you then might need calls to you helper after every CALL in all
drivers.

For this thinking to be useful, you need to isolate how often the mask is
reset. Is it in every service module interface (if so you can't win) Is it only
in the intercepts of your CALLs to your submodules.  If so maybe you can win by
only changing to more frequent calls to helpers.

But there is a reducio here. Your COBOL CALL statement to the helper module may
be mediated by a 'COBOL' service module, that is being vectored. When you
return from your submodule, you may not really be returning to you COBOL
program, but instead to the runtime service module that mediated the invocation
of your helper module.
(and its going to 'fix' the mask on you).

Part of the problem here is that the new environment is encouraging you to do
dynamic links (no matter what you use to do), and that gives the runtime a
chance to impose on you.

There is no migration path for the specific problem you are presenting.
Although systems folks should be able to determine if you product from IBM
allows exits on any of the service module intercepts so that they the mask
might be set there.

Alternatively, use the actual accumulated knowledge of history. You may have
6000+ modules, and maybe dozens of arithmetic statements in each on average. 
But do you really have upwards to a hundred thousand arithmetic statements that
have caused you trouble over the years?

Maybe a divide and couquer approach is worth considering. You indicate that you
want to 
<<
To prevent a complete conversion of our old COBOL sources (add the
ON-SIZE-ERROR clause in every ADD, COMPUTE..?)
>>

But would a complete conversion be necessary? Why not use shop knowledge to
focus on the subset of programs that have been problematic and change only
those, using conventional, supported, COBOL ON SIZE ERROR clauses and abenders.

You problem is finite. Try to look at it as small enough to be economically
doable.  You can insert the clauses in the source and continue to 
compile old style (as long as vendor support for this strategy can be assumed
in your planning)

If you are just relinking without recompile, you might want to get some
opinions on that strategy.  

Also you can take other actions to limit this problem. You can put protection
software infront or behind sensitive programs: programs that examing
inbound/outbound numerics to sense
when overflow might occur in downstream modules. (obviously a lot easier in
batch than online). 

But really, how oftern are you dealing with overflow? Are you getting 6000
overflows? Try to limit the focus, and remediate the system in the area where
the problem is actually likely.

Hope these suggestions are useful,

Bob Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** Colin Campbell <cmcampb@attgloabl.net>
- **Date:** 2003-09-17T10:49:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F689E94.C1A96040@attgloabl.net>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
Ad,
What do you get?  Does the program abnormally terminate?

Language Environment addresses a long time complaint of IBM mainframe
users - namely, that we always had to deal with abend codes such as 0CA,
0C7, etc.  With Language Environment, they tell us to start handling
abends by looking for messages.  LE's default message file is DDname
SYSOUT.  There should be a message issued if a decimal overflow occurs,
and if the program mask is set.

So, do you get a message?

Now, the handling of the "condition", as LE calls it, is determined by LE
run time options.  ABTERMENC needs to be set to ABEND in order for the
process to abnormally terminate.

You can check the run time options by coding RTPOPTS(ON) in the PARM field
of a batch job step.  You might as well code RPTSTG(ON) as well, to see if
your application is using unusual amounts of storage.  For COBOL, these
options are normally at the end of the PARM field, following a slash (/)
which separates the program options from the LE options (that is
controlled by yet another run time option, CBLOPTS).

If everything is as it should be, it is possible that LE is getting
between your program and the PSW changes that the Assembler program
makes.  I don't know how you would get around that, but I'd contact IBM
for assistance.

Good luck,
Colin Campbell

Ad Tromp wrote:

> Hello IBM COBOL specialists out there!
>
…[20 more quoted lines elided]…
> Ad Tromp
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-09-17T21:10:41+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<398hmvodl9qajktdvhbg738m52319k96ef@4ax.com>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
On 17 Sep 2003 06:37:32 -0700 ad.tromp@abp.nl (Ad Tromp) wrote:

:>Hello IBM COBOL specialists out there!

:>We have a very specific problem in our conversion from the IBM VS
:>COBOL II run-time library to IBM Language Environment. At the moment
:>we are trying to do this by the STEPLIB approach: adding SCEERUN to
:>the job, without recompiling and do some regression testing.
:>In our ï¿½old' VS COBOL II programs (ï¿½ 6000 load modules) we do a CALL
:>to an Assembler program to set the program mask (bits 20 and 21), so
:>we get an abend 0CA in case of decimal overflow. We do NOT use the
:>ON-SIZE-ERROR clause in our programs, but rely on the ï¿½change program
:>mask' method, ï¿½invented' by our system programmers many, many years
:>ago!

:>When we add the SCEERUN dataset to the STEPLIB we never get any 0CA
:>abend in case of a decimal overflow. This is NOT what we want.
:>To prevent a complete conversion of our old COBOL sources (add the
:>ON-SIZE-ERROR clause in every ADD, COMPUTE..?) here is my question: Is
:>there any other way to solve this decimal overflow problem when using
:>Language Environment, at the best, without code changes or
:>recompiling?

Look at CEE3SPM.

But be aware that sometimes COBOL will use temporary fields and the overflow
will not be recognized.
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-17T20:18:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hk3ab.27202$Aq2.11267@newsread1.news.atl.earthlink.net>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
Let me share with you the response that I received from one of my usually
reliable sources,

"Bill,
It is illegal and not supported for users to change the program mask while
in COBOL programs. It invalidates the product.

In addition, what this guy says contradicts the COBOL Migration Guide:

(http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg10/APPENDI
X1.4.5 )


Converting programs that change the program mask

When a VS COBOL II program calls an assembler program that changes the
program mask (for example, uses an SPM instruction), the program mask is
restored after the call to the assembler program.

With Enterprise COBOL, the program mask is not restored. Thus, if you change
the program mask in your assembler program, you must restore it before
returning to the COBOL program. Failure to restore the program mask could
result in
undetected data errors, such as fixed-point overflow, decimal overflow,
exponent underflow, and significance exceptions.
It sounds like what they are doing should NOT work under VS COBOL II, but
'work' under LE."

Furthermore, regarding the suggestion to use CEE3SPM
  (see:
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/3.5.14
     and

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2130/3.4.4.1.3 )

I do NOT think that this will work - as you may not make calls to these
services from VS COBOL II programs - only from LE conforming compilers.

   ***

I really DO think that you need to make certain that your "shop" understands
that doing "manual" changes to the program mask makes your entire shop
"unsupported" by IBM.  Of course, from the fact that you are only NOW
converting to LE, that probably won't make much difference UNTIL you
actually have some production problem!!!
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-17T21:18:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uc4ab.27294$Aq2.13385@newsread1.news.atl.earthlink.net>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
My first answer is included in my other note (which basically says FIX your
applications to use SUPPORTED interfaces).  However, I have also come up
with a *possible* (totally UNTESTED and still "outside" the world of
DOCUMENTED/supported interfaces) but MAYBE worth trying.

First, are your VS COBOL II programs compiled with RES or NORES?  Do you
currently call the assembler program that "resets" the program mask
dynamically or statically?

Depending upon the answer to those questions, the following may or may not
stand a better chance of working:

1) Create a NEW assembler program that is LE conforming
(see
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2130/5.2.2.1 )
which has the same name as your existing "program-mask manipulating"
program.  You must use "NAB=NO"
 (see
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea4110/15.1.4.1
 )
to allow the program to be called from VS COBOL II

2) This new Assembler program should use CEE3SPM to "reset" the required
program mask fields
 (see:
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3130/3.5.14

3) Link-edit your COBOL program with the LE link-edit library (SCEELKED - as
I recall) *and* if your existing COBOL program does a STATIC call to the old
assembler routine, now use the new routine.

4) Use the LE run-time library *and* if the existing calls to the Assembler
routine are DYNAMIC, then place the new Assembler routine ahead of where it
used to find the old one - in your Steplib/Joblib

   ***

Although it is not supported (and doesn't really work) to CALL LE services
from VS COBOL II programs, it MIGHT work to call an LE-conforming Assembler
routine from a VS COBOL II program to do what you want.

P.S.  You should also make it a "shop requirement" that new programs and
MODIFIED versions of existing program "switch" to using the IBM supported ON
SIZE feature - or when compiled with an LE-conforming compiler an LE
"condition handler" to do what you want to do.
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-09-17T21:23:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030917172333.06003.00001066@mb-m07.aol.com>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
Ad Tromp writes ...

>Hello IBM COBOL specialists out there!
>
…[19 more quoted lines elided]…
>

Ad,

You got some good responses from other listers. I want to make another
suggestion: you can code your own condition handler to get control for what
used to be S0CA abends; A JCL (or CEEROPT setting for CICS) can register this
condition handler on behalf of your program(s) at runtime, with no change in
source code (you do need to re-compile / bind everything probably). Condition
handlers can be written in Assembler or COBOL or PL/I or C!

We teach this (and a lot more) in our course "Using LE Services in z/OS" (check
out http://www.trainersfriend.com/m512descr.htm for details).

If you want to get a pretty thorough overview of this content, check out my
presenation from last month's SHARE (go to
http://ew.share.org/proceedingmod/abstract.cfm?abstract_id=5296&conference_id=3
if you're a SHARE member; otherwise, email me offlist and I will send you a
copy of that presenation).

Kind regards,

-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-17T21:40:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kx4ab.27373$Aq2.1665@newsread1.news.atl.earthlink.net>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com> <20030917172333.06003.00001066@mb-m07.aol.com>`

```
Minor "clarification" to Steve's statement

 "Condition handlers can be written in Assembler or COBOL or PL/I or C"

This must be LE-conforming COBOL (or PL/I or Assembler).  If you WANTED to
do it in COBOL, you would need to use one of the "currently supported"
COBOL's (e.g. IBM COBOL for OS/390 and VM - or IBM Enterprise COBOL for z/OS
and OS/390).  You could NOT write the condition handler in VS COBOL II (or a
pre-LE PL/I either).

As you say you are doing a (reasonable to me) conversion of the run-time
before introducing the new compiler - then this MIGHT be a constraint to
you.
```

#### ↳ Re: IBM VS COBOL II - Language Environment problem

- **From:** ad.tromp@abp.nl (Ad Tromp)
- **Date:** 2003-09-17T23:32:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<50d43234.0309172232.4d4d9ef6@posting.google.com>`
- **References:** `<50d43234.0309170537.7339f496@posting.google.com>`

```
ad.tromp@abp.nl (Ad Tromp) wrote in message news:<50d43234.0309170537.7339f496@posting.google.com>...
> Hello IBM COBOL specialists out there!
> 
> We have a very specific problem in our conversion from the IBM VS
> COBOL II run-time library to IBM Language Environment.......

Thank you very much for all your suggestions so far. There are some
possible solutions we have to try out in our testing environment.
Also, I can use your comments to convince our management to clean up
our 'old' COBOL environment and to migrate to up-to-date standards!!

Ad Tromp
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
