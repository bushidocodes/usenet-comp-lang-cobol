[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

_12 messages · 6 participants · 2006-11 → 2006-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** Andreas Lerch <andreas.lerch@onlinehome.de>
- **Date:** 2006-11-29T18:38:43+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cics.z-os
- **Message-ID:** `<20061129.18384382@rechner12.lerch.xl>`

```
Hello all

System: z/OS and LE for MVS

Why is it possible to compile a COBOL/CICS/DB2 program with the 
options:

NODYNAM . . . ?????

nowerdays thats not the state of the art, because:

IMS could be called dynamic
COBOL and ASSEMBLER could be called dynamic

why not inside of a CICS environment

I asked this question, because i mus used the same sources in two 
environments:

DB2 Batch (IMS/DSN) - one compile and link
DB2 CICS - a second compile and link

i have to manage two sources inside a revision environment!!!

The first source could be compiled with the option: DYNAM for batch - 
and all calls are managed by COBOL and MVS

in CICS, the precompiler sets the COBOL options to NODANM. Therefore i 
need a second source to manage the environment. I must use the 
CICS-link library to link the DSNHLI and i can NOT use the same module 
in IMS/TSO, because they need different HLI's: for IMS propagator 
DSNHLI from IMS for DSN propagator DSNHLI from DB2.

I would link a DB2 module without a specific DSNHLI.......

Is DFHECI unable to be called dynamic? IMS module DFSLI000 could.

Why does DB2 precompiler generate calls like: CALL 'DSNHLI' USING 
PLIST-x, instead of CALL DSNHLI USING PLIST-x, where DSNHLI ist 
defined as a variable inside the working-storage section?

I am not pleased about this situation.

I hope, that you could follow my intention... :-)

i am not so stable in english

Einen schoenen Tag
Andreas Lerch
```

#### ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-11-29T18:14:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22d08$456e1473$d066072d$8128@FUSE.NET>`
- **In-Reply-To:** `<20061129.18384382@rechner12.lerch.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl>`

```
Andreas Lerch wrote:
> Hello all
> 
…[46 more quoted lines elided]…
> Andreas Lerch

Andreas,

I believe the short answer to this is:
1)  Yes, all of the CICS interface components must be static CALLs. 
That is why the preprocessor generates CALL 'literal' statements.
2)  If you need to force your own programs to be dynamically called, 
instead of depending on the DYNAM/NODYNAM option you should change your 
calls to CALL data-name and assign the name of your routine to 
data-name.  This form of the CALL will always be dynamic no matter what 
the setting of DYNAM/NODYNAM.

If you manage your programs and let the preprocessors manage theirs, all 
should work out fine.

Good luck.
Carl
```

#### ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2006-11-30T01:12:21+00:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cics.z-os
- **Message-ID:** `<dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com>`
- **References:** `<20061129.18384382@rechner12.lerch.xl>`

```
On Wed, 29 Nov 2006 18:38:43 GMT, Andreas Lerch
<andreas.lerch@onlinehome.de> wrote:

>Hello all
>
…[5 more quoted lines elided]…
>NODYNAM . . . ?????

The reason is to force all CALL literal statements to bind the called
module to the COBOL program.  This reduces overhead because a dynamic
call takes both more instructions on initial call as well as the
subsequent calls.  This is important in a CICS environment where there
may be many transactions at the same time executing the program.  Also
the cost of the initial call may be a higher percentage of overall
execution in a CICS environment.  You can still dynamically call
modules by using CALL data-name which forces DYNAM for the specific
call.  This can be more efficient than EXEC CICS LINK.
>
>nowerdays thats not the state of the art, because:
…[40 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-11-30T03:23:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eklise$bv7$1@theodyn.ncf.ca>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com>`

```
Clark F Morris (cfmpublic@ns.sympatico.ca) writes:

> execution in a CICS environment.  You can still dynamically call
> modules by using CALL data-name which forces DYNAM for the specific
> call.  This can be more efficient than EXEC CICS LINK.

The advice we got during migration to LE in the early 1990s was that
EXEC CICS LINK or XCTL was 10 times the overhead of a COBOL DYNAMIC CALL.

Has that improved with later versions of CICS and Enterprise COBOL?

We had trouble getting DYNAMIC calls to work during a tuning exercise, so
we ended up using STATIC CALLS. LE had already increased developer familiarity
with using AMBLIST to see what was inside load modules and how to replace
particular CSECTs within a load module using the Linkage Editor. (I never
call it the binder because DB2 developers seem to get confused when I do 
that)
```

###### ↳ ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-11-30T06:04:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Mvubh.393296$QZ1.289914@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<eklise$bv7$1@theodyn.ncf.ca>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com> <eklise$bv7$1@theodyn.ncf.ca>`

```


Kelly Bert Manning wrote:
> Clark F Morris (cfmpublic@ns.sympatico.ca) writes:
> 
…[9 more quoted lines elided]…
> Has that improved with later versions of CICS and Enterprise COBOL?

I don't know if this has improved, but I believe it is still true that 
it is much faster to transfer control from one CICS COBOL program to 
another by a dynamic call, rather than an EXEC CICS LINK or EXEC CICS 
XCTL.

But that really has no bearing on the original question.  Every CICS 
COBOL program must be compiled with the NODYNAM option, because each 
EXEC CICS statement is translated into a CALL 'DFHEI1' USING <variable 
parameter list>.

It is DFHEI1 that must be statically linked to your CICS COBOL program 
in order to execute any CICS services.  Remember, your COBOL program 
is really executing as a subprogram of CICS, and it needs the DFHEI1 
hook in order to connect to CICS.

> 
> We had trouble getting DYNAMIC calls to work during a tuning exercise, so
> we ended up using STATIC CALLS. 

Sorry to hear you had troubles.  I've worked with CICS applications 
that do it successfully, although I don't remember the details without 
the source code in front of me.  It's definitely possible to do.

With kindest regards,
```

###### ↳ ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

_(reply depth: 4)_

- **From:** "Andreas Lerch" <andreas.lerch@onlinehome.de>
- **Date:** 2006-11-30T17:19:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zedBflvOyr8o-pn2-we9Zjd8Kl7Rd@piihost.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com> <eklise$bv7$1@theodyn.ncf.ca> <Mvubh.393296$QZ1.289914@bgtnsc04-news.ops.worldnet.att.net>`

```
> 
> It is DFHEI1 that must be statically linked to your CICS COBOL program 
…[3 more quoted lines elided]…
> 
No - why - CBLTDLI uses the same code sequence and it must not called 
static.

einen schoenen Tag
Andreas Lerch
```

###### ↳ ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

_(reply depth: 5)_

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-11-30T18:28:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5795d$456f690b$d066072d$18864@FUSE.NET>`
- **In-Reply-To:** `<zedBflvOyr8o-pn2-we9Zjd8Kl7Rd@piihost.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com> <eklise$bv7$1@theodyn.ncf.ca> <Mvubh.393296$QZ1.289914@bgtnsc04-news.ops.worldnet.att.net> <zedBflvOyr8o-pn2-we9Zjd8Kl7Rd@piihost.xl>`

```
Andreas Lerch wrote:
>> It is DFHEI1 that must be statically linked to your CICS COBOL program 
>> in order to execute any CICS services.  Remember, your COBOL program 
…[4 more quoted lines elided]…
> static.
One is CICS and one is IMS.  Two totally different architectures that 
just happen to have been made to co-exist.
Carl
```

###### ↳ ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

_(reply depth: 6)_

- **From:** "Andreas Lerch" <andreas.lerch@onlinehome.de>
- **Date:** 2006-12-01T18:32:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zedBflvOyr8o-pn2-xpz3HCtE2Ruu@piihost.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com> <eklise$bv7$1@theodyn.ncf.ca> <Mvubh.393296$QZ1.289914@bgtnsc04-news.ops.worldnet.att.net> <zedBflvOyr8o-pn2-we9Zjd8Kl7Rd@piihost.xl> <5795d$456f690b$d066072d$18864@FUSE.NET>`

```
On Thu, 30 Nov 2006 23:28:11 UTC, CG 
<carl.gehr.RemoveThis@ThisToo.attglobal.net> wrote:

> Andreas Lerch wrote:
> >> It is DFHEI1 that must be statically linked to your CICS COBOL program 
…[8 more quoted lines elided]…
> Carl

Hello Carl

yes, you are right, I forgot this. Since 15 years i use the same code 
in both environments CICS and Batch, with dynamic calls, so i forgot 
this little difference. CICS and IMS have different DFSLI00...... 
Sorry

einen schoenen Tag
Andreas Lerch
```

###### ↳ ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-11-30T01:42:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dabb$456e7d72$d066072d$16441@FUSE.NET>`
- **In-Reply-To:** `<eklise$bv7$1@theodyn.ncf.ca>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com> <eklise$bv7$1@theodyn.ncf.ca>`

```
Kelly Bert Manning wrote:
> Clark F Morris (cfmpublic@ns.sympatico.ca) writes:
> 
…[7 more quoted lines elided]…
> Has that improved with later versions of CICS and Enterprise COBOL?

Dynamic CALLs via CALL data-name are still the recommended linkage 
between user components.

> 
> We had trouble getting DYNAMIC calls to work during a tuning exercise, so
…[4 more quoted lines elided]…
> that)
We have an automatic way to replace user components.  Contact me 
off-list if you want more info.

Carl
```

##### ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** "Andreas Lerch" <andreas.lerch@onlinehome.de>
- **Date:** 2006-11-30T16:37:47+00:00
- **Newsgroups:** ibm.software.cics.z-os,comp.lang.cobol
- **Message-ID:** `<zedBflvOyr8o-pn2-sJen2dKgpHOh@piihost.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <dlbsm2hm3jfkdpf0sjgaq7vhmslpa5r7ti@4ax.com>`

```
> 
> The reason is to force all CALL literal statements to bind the called
…[7 more quoted lines elided]…
> call.  This can be more efficient than EXEC CICS LINK.

I know this, and this is my problem. I have a little load inside CICS,
up to 500.000 transactions a day is the maximum. The avarage response 
time is under 0,01 seconds (some heavy tasks may have more, buts less 
than 1.000). I have no response problems since 10 or 15 years with 
this application.

For CICS/DB2, IMS/DB2 i must have two identical sources and objects, 
the only difference is PROGRAM ID. One for CICS and one for IMS...

All my other subroutines are called by literal, only DSN*-modules are 
called by constant and only inside CICS.
------
If i have a mission critical application, i don't use HLL. I want to 
reduce the maintenace overhead to manage two identical sources. If i 
can use the same module in IMS and CICS, I can save money, but CICS 
precompiler forces the COBOL compiler option to NODYNAM.

The proloque of a DB2-call is a sequence of CALL 'DSNADDR' USING ..., 
CALL 'DSNADDR2' USING .. this could be static, it is used one time for
invocation. CALL DSNHLI USING could be a [0]CALL 
WORKING-STORAGE-FIELD-DSNHLI USING ...
[0] This is what i want. Then I can save the time, to manage TWO ore 
more Sources. This can reduce mistakes, by using the wrong 
INCLUDE-libs for CICS. In the past I have to solve some Problems, that
the developer uses CICS link librarys in batch with 
NODYNAM and DB2 link librarys inside CICS.

I must use:
	CICS-DSNHLI inside CICS --> this is FORCED to NODYNAM by CICS 
precompiler
	IMS-DSNHLI inside IMS --> no change of my COBOL compile parms, I can 
use DYNAM
	DB2-DSNHLI inside RUN DSN --> no change of my COBOL compile parms, I 
can use DYNAM

Thank you for your answer.

einen schoenen Tag
Andreas Lerch
```

#### ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-11-30T13:29:09-08:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cics.z-os
- **Message-ID:** `<3redne2ocaiF0PLYnZ2dnUVZ_rOdnZ2d@adelphia.com>`
- **In-Reply-To:** `<20061129.18384382@rechner12.lerch.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl>`

```
Hallo Andreas,
You state that your two programs are almost entirely common, except for 
the CALL statements and compiler options, due to the restrictions of 
CICS compared to IMS and DB2.

Have you looked into using COBOL's Compiler Directing Statements to 
bring in the needed source code, and specify the needed compiler 
options?  You would still have two source programs, but those programs 
would be mostly COPY statements, and would not change.  The code that 
you COPY into these programs would either be the same, with different 
REPLACING strings on the COPY statements, or there would be some COPY 
members that are unique to each environment (some for CICS, others for 
IMS, etc.).

Then, when you change logic which is common to either environment, you 
would only have one place to make the change -- in the COPY member.

CBL or PROCESS statements in the source code could help you with the 
needed compiler options.

If your shop uses a Configuration Management tool (you mention a 
"revision environment"), it should also be possible to control the 
compile options inside that tool.
Colin

P.S.: Your English was just fine.  One word I noticed, though, was 
"nowerdays", which should be written "nowadays".
```

##### ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM

- **From:** "Andreas Lerch" <andreas.lerch@onlinehome.de>
- **Date:** 2006-12-01T18:14:56+00:00
- **Newsgroups:** ibm.software.cics.z-os,comp.lang.cobol
- **Message-ID:** `<zedBflvOyr8o-pn2-M0s7MouWHBQ0@piihost.xl>`
- **References:** `<20061129.18384382@rechner12.lerch.xl> <3redne2ocaiF0PLYnZ2dnUVZ_rOdnZ2d@adelphia.com>`

```
On Thu, 30 Nov 2006 21:29:09 UTC, Colin Campbell 
<cmcampb@adelphia.net> wrote:

Hello Colin

> Hallo Andreas,
> You state that your two programs are almost entirely common, except for 
> the CALL statements and compiler options, due to the restrictions of 
> CICS compared to IMS and DB2.

no - the CALL statements are identical only the compiler options are 
different

> Have you looked into using COBOL's Compiler Directing Statements to 
> bring in the needed source code, and specify the needed compiler 
…[5 more quoted lines elided]…
> IMS, etc.).

the sequence is:
	DB2 precompiler (batch and CICS) [0]
	CICS precompiler (CICS only) [1]
	LINK 

[0] changes the EXEC SQL .. to CALL 'DSNxxx' using...
[1] changes all DYNAM to NODYNAM

> Then, when you change logic which is common to either environment, you 
> would only have one place to make the change -- in the COPY member.

thats not a solution, it is a solution with COBOL-VS neither in an 
area past COBOL-VS. If i have an indicator inside the calling 
parameter, i can perform different code in CICS and batch --> see 
GOOGLE with search <"Andreas Lerch"  Language-Environment Cobol for 
MVS&VM zOS 1.2> (without bracket), i don't know the message-id - sorry

> CBL or PROCESS statements in the source code could help you with the 
> needed compiler options.

CICS precompiler forcec the CBL-statement to NODYNAM every other 
directive is removed. see  [1] 

> If your shop uses a Configuration Management tool (you mention a 
> "revision environment"), it should also be possible to control the 
> compile options inside that tool.

we use a tool, but also se [1] .

Next week, i will try to connect IBM.

DB2-Team --> to answer the question: Which parameter can be used to 
produce source-code like:
	CALL Working-Storage-Field-DSN USING ..
instead of
	CALL 'DSN....' USING

and CICS-TEAM --> to answer the question: Which reason is neccessary 
to use NODYNAM in a past COBOL-VS area 

i am not amused :-)

einen schoenen Tag
Andreas Lerch

> P.S.: Your English was just fine.  One word I noticed, though, was 
> "nowerdays", which should be written "nowadays".
ok - I will do my very best :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
