[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [Fwd: Re: Using EXEC CICS... as Copybook]

_10 messages · 7 participants · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37958EAC.63D06F26@nbnet.nb.ca>`

```
I am not disagreeing with your answer but I believe that it is absurd
that we still have to do this in 1999. The COBOL compiler should be set
up to call an appropriate translator for every EXEC statement in either
main source or copy book.  If that won't work, the preprocessor should
be set up to be able to parse required copybooks (including correctly
handling COPY REPLACING and nested copy) and pass the translated source
with the translated copybooks to the compiler.  In either case we should
not have to go through unnatural gyrations to do the simple thing.

Clark Morris, CFM Technical Programming Services morrisc@nbnet.nb.ca
Gunnar Opheim wrote:
> snip
>
…[5 more quoted lines elided]…
> Gunnar.
```

#### ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3795BCA2.1C241F83@zip.com.au>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca>`

```
Clark Morris wrote:
> 
> I am not disagreeing with your answer but I believe that it is absurd
…[18 more quoted lines elided]…
> > Gunnar.

Look at some of your tools you have available.  One of them might be
able to expand the copybook before the CICS translator.  For example
if you use CICS and DB2 use EXEC SQL INCLUDE and do your DB2
precompiler first.  The CICS translator will then see the CICS code in
situe.

If you use endevor I think there is a tool that will expand the COPY
statements for you.

Ken
```

##### ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3796DCE0.7E63F9D9@worldnet.att.net>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <3795BCA2.1C241F83@zip.com.au>`

```
Based on a posting in bit.listserv.ibm-main, I looked up the TSO utility
program named ISRLEMX.  After fussing around with the manual, I was able
to run it in a plain old OS/390 batch job.  It's a utility program that
read a COBOL program and expand the copybooks.

I wanted something like it for a different reason.  I haven't tested it
to see if it handles nested copy or copy replacing, but it will search
up to 8 copybook libraries in the order you specify.  Besides COBOL, it
can also be configured to handle Assembler or PL/1.

If anyone is interested I can post a sample of the JCL.
```

###### ↳ ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379800f5.101941961@news1.ibm.net>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <3795BCA2.1C241F83@zip.com.au> <3796DCE0.7E63F9D9@worldnet.att.net>`

```
On Thu, 22 Jul 1999 03:57:04 -0500, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:


>If anyone is interested I can post a sample of the JCL.
>

Please.
```

###### ↳ ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37980522.3DA86491@worldnet.att.net>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <3795BCA2.1C241F83@zip.com.au> <3796DCE0.7E63F9D9@worldnet.att.net> <379800f5.101941961@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On Thu, 22 Jul 1999 03:57:04 -0500, Arnold Trembley
…[5 more quoted lines elided]…
> Please.

Fortunately, I printed off a copy at work today.  Here's what ISRLEMX
would look like:

//****************************************************
//*     EXPAND COBOL COPYBOOKS
//****************************************************
//TRN     EXEC PGM=ISRLEMX,COND=(12,LE),
//        PARM=('COB,progname,B,N,E,5, ,00,ENU,4,7',
//             '1,/,SYSDA)
//*
//*  INSERT A STEPLIB DD HERE IF ISRLEMX IS NOT IN YOUR SYSTEM LIBRARY
//*
//ISRLCODE DD DSN=MY.COBOL.SOURCE.LIB,DISP=SHR
//         DD DSN=TEST.COPYBOOK.LIB1,DISP=SHR
//         DD DSN=TEST.COPYBOOK.LIB2,DISP=SHR
//         DD DSN=TEST.COPYBOOK.LIB3,DISP=SHR
//         DD DSN=PROD.COPYBOOK.LIB,DISP=SHR
//ISRLEXPD DD UNIT=SYSDA,DISP=(NEW,PASS),
//            SPACE=(CYL,(2,2)),DSN=&&TEMP1
//ISRLMSG  DD SYSOUT=*

You might find it easier to put ISLRLEMX into a proc, so you can pass
your 'progname' in as a substitution parameter.  Don't forget the 'E' as
the fifth subparameter!  If you need more than five libraries in your
ISRLCODE search chain, you can go up to nine by putting a '9' after the
'E' in the parameter list.  The 'ENU' just means English.  If you have
questions about the rest of the parameters, e-mail me, or look it up in
the manual (I forgot which one it was, but I think it was ISPF on book
mangler).

The PDS library containing your COBOL source program has to be the first
PDS under the ISRLCODE DD.  All the rest are your copybook libraries. 
You can override them to change the search order as needed.

ISRLEXPD can be directed to any file you want, of course, but you may
just leave it as a temporary so you can pass it into another language
translater, such as the CICS preprocessor, the compiler itself, or in my
case the standards compliance checker.

I've never gotten any messages out of ISRLMSG.  I suppose it's just
there in case of severe errors.  ISRLEMX will insert comment lines
immediately before and after any included copybooks.  We're at OS/390
Release 2.5, but I believe ISRLEMX has been around for a few
releases.      

Good luck!
```

#### ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n4qk3$o9p@dfw-ixnews21.ix.netcom.com>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca>`

```
Out of curiosity, if you think that IBM should have solved this (already),
did you ever submit a "requirement" (GUIDE or SHARE) or REQUEST (via
service) asking for it?  Contrary to popular belief, IBM (like most vendors)
responds to official "enhancement requests" and does NOT "read minds" about
what enhancements users want (and will pay for).
```

##### ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3796288A.1E397699@home.com>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <7n4qk3$o9p@dfw-ixnews21.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Out of curiosity, if you think that IBM should have solved this (already),
…[4 more quoted lines elided]…
> 
What you say is probably true. But "(and will pay for)" - should I
really have to pay for suggesting to them they should put a fourth wheel
on my car ?

How neat - MicroFocus circularized us some two months ago, by e-mail,
"How did we like the product ?" and a series of questions. Don't laugh -
to me it was INNOVATIVE - that's the first time since 1980 anybody has 
asked me what I think about COBOL or Standards. Yes, we have these
computer research reports coming in, don't recall anyone ever phoned me
other than to ask which toohpaste/washing-powder we used.

What about you other people - anybody ever e-mailed or phoned you about
COBOL ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n5cof$994@dfw-ixnews7.ix.netcom.com>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <7n4qk3$o9p@dfw-ixnews21.ix.netcom.com> <3796288A.1E397699@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
  <much snippage>
> What about you other people - anybody ever e-mailed or phoned you about
> COBOL ?
>
> Jimmy, Calgary AB

I don't know about the current SHARE COBOL project, but the old GUIDE COBOL
project did REGULAR email/snail-mail "surveys" of requirements (priorities)
and encouraged users to submit new requirements.
```

###### ↳ ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

_(reply depth: 4)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n65js$ent$1@bgtnsc02.worldnet.att.net>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <7n4qk3$o9p@dfw-ixnews21.ix.netcom.com> <3796288A.1E397699@home.com> <7n5cof$994@dfw-ixnews7.ix.netcom.com>`

```
I will add, Bill, that when CODASYL     had a planning
committee, members were representitives of the various user groups.  These
members took material to the user group meetings, and supplied feedback.
Some were more active than others, but none were
silent.

Warren Simmons
William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7n5cof$994@dfw-ixnews7.ix.netcom.com...
>
> James J. Gavan <jjgavan@home.com> wrote in message
…[6 more quoted lines elided]…
> I don't know about the current SHARE COBOL project, but the old GUIDE
COBOL
> project did REGULAR email/snail-mail "surveys" of requirements
(priorities)
> and encouraged users to submit new requirements.
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: [Fwd: Re: Using EXEC CICS... as Copybook]

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n7mtr$4uo@dfw-ixnews14.ix.netcom.com>`
- **References:** `<37958EAC.63D06F26@nbnet.nb.ca> <7n4qk3$o9p@dfw-ixnews21.ix.netcom.com> <3796288A.1E397699@home.com> <7n5cof$994@dfw-ixnews7.ix.netcom.com> <7n65js$ent$1@bgtnsc02.worldnet.att.net>`

```
When it comes to user groups, J4 (or X3J4) has also included members.  Both
GUIDE (one of IBM's user groups) and DECUS (Dec's user group) *were* (but
are not) members of J4.  The HP user group is a current "liaison" to J4.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
