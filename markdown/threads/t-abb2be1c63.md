[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Error Message Assist (MVS)

_14 messages · 10 participants · 2004-02 → 2004-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL Error Message Assist (MVS)

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2004-02-22T08:03:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
Hi, folks...

Wondering if someone has run across this message before... system is MVS,
running "IBM ENTERPRISE COBOL FOR Z/OS AND OS/390 3.2.0":

IGYAS5125-U   THE COMPILATION WAS TERMINATED DUE TO A COMPILER ERROR IN
PHASE ID:  "IGYCASM1".
IGYAS5092-U   OVERFLOW OCCURRED ON TABLE "TRQB".

My error diagnosis says it's an "unrecoverable" error, please contact a
system programmer or IBM support.

I have those options available to me on Monday, but I've got a lot of the
weekend left to finish up a bunch of coding. I suspect it may have something
to do with the number of statements in the program (about 700,000 lines). My
COBOL references say it has a limitation of 999,999 lines, so I'm more
suspicious of maybe another limiatation that's not obvious to me. Compiled
program size is just over 1 meg, so I don't think I'm in trouble there. I've
got a large number of I-level errors and a few W-level statements, but no
E-level or S-level error statements. Been compiling/running fine today until
I just added a fairly large copybook in the procedure division.

Current compiler options in effect:
NOADATA
NOADV
  APOST
  ARITH(COMPAT)
  AWO
  BUFSIZE(23476)
NOCICS
  CODEPAGE(1140)
NOCOMPILE(S)
NOCURRENCY
  DATA(31)
NODATEPROC
NODBCS
NODECK
NODIAGTRUNC
NODLL
NODUMP
  DYNAM
NOEXIT
NOEXPORTALL
  FASTSRT
  FLAG(I,E)
NOFLAGSTD
  INTDATE(ANSI)
  LANGUAGE(UE)
  LIB
  LINECOUNT(80)
NOLIST
  MAP
NONAME
  NSYMBOL(DBCS)
NONUMBER
  NUMPROC(MIG)
  OBJECT
  OFFSET
NOOPTIMIZE
  OUTDD(SYSOUT)
  PGMNAME(COMPAT)
  RENT
  RMODE(AUTO)
  SEQUENCE
  SIZE(MAX)
  SOURCE
  SPACE(1)
NOSQL
NOSSRANGE
  TERM
NOTEST
NOTHREAD
  TRUNC(OPT)
NOVBREF
NOWORD
  XREF(FULL)
  YEARWINDOW(1900)
  ZWB
----------------------


TIA.
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-02-22T09:11:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n_Zb.29563$aH3.932948@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
Top posting, because of the length.

I have never seen an IBM mainframe COBOL compiler crash during 
compilation.  The message seems to be clear enough, but I do not know 
what the "TRQB" table is.

The largest production COBOL program I have ever personally seen was 
just over 24,000 lines, and it called several subprograms.  The fact 
that your source file is over 700,000 lines long, and you just added 
another copybook, and the "TRQB" table overflowed (whatever that is) 
certainly suggests that you have exceeded some kind of compiler 
limitation.  In my experience, a COBOL program that is under 1000 
lines is a short program, and anything over about 6,000 to 8,000 lines 
is a pretty large program.  Large programs can be difficult to 
understand simply because of their size.

Have you tried removing the new copybook to see if your program will 
still compile without it?

Many years ago, I assisted a co-worker in trying to debug problems 
with an IBM Series/1 COBOL compiler.  If the compiler itself abended, 
we tried cutting the source file in half, and compiling until we found 
the one line that caused the compiler to crash.

I know this is probably not what you want to hear, but have you 
considered splitting the program into multiple modules, so that some 
routines can be called from the main module?

I hope that helps!


Gonzo wrote:
> Hi, folks...
> 
…[80 more quoted lines elided]…
> 
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2004-02-22T12:20:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vf0h30dvnqk0jqr5r4m92dtfasdkj8l1ln@4ax.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
On Sun, 22 Feb 2004 08:03:10 GMT "Gonzo" <ckhamel1961.nospam@yahoo.com> wrote:

:>Wondering if someone has run across this message before... system is MVS,
:>running "IBM ENTERPRISE COBOL FOR Z/OS AND OS/390 3.2.0":

:>IGYAS5125-U   THE COMPILATION WAS TERMINATED DUE TO A COMPILER ERROR IN
:>PHASE ID:  "IGYCASM1".
:>IGYAS5092-U   OVERFLOW OCCURRED ON TABLE "TRQB".

:>My error diagnosis says it's an "unrecoverable" error, please contact a
:>system programmer or IBM support.

:>I have those options available to me on Monday, but I've got a lot of the
:>weekend left to finish up a bunch of coding. I suspect it may have something
:>to do with the number of statements in the program (about 700,000 lines).

A single program with 700K lines?

How many are procedure division?
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-02-22T09:46:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0402220946.15a96bc2@posting.google.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote 

> to do with the number of statements in the program (about 700,000 lines). 
> ,,,
>  Been compiling/running fine today until
> I just added a fairly large copybook in the procedure division.

Have you not heard of the CALL statement ?
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-02-22T13:53:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GNSdna_BX_pUlaTdRVn-gg@giganews.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
Gonzo wrote:
> Hi, folks...
>
…[20 more quoted lines elided]…
>

700,000 Lines yielding an executable of 1 meg? That's 1.4 bytes of
executable per line of code!

I can't imagine a program that generates 1.4 bytes of object code per line
of source code. Even assembly language isn't THAT tight.

And we haven't even considered statically linked support modules. If we did,
you'd have a program that generates less than one byte of object code for
every COBOL statement!

I think your computer is drunk.
```

##### ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2004-02-22T22:08:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sv2i30d0t6jsaufadg1ubb8mnb46ch1og4@4ax.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <GNSdna_BX_pUlaTdRVn-gg@giganews.com>`

```
On Sun, 22 Feb 2004 13:53:54 -0600 "JerryMouse" <nospam@bisusa.com> wrote:

:>700,000 Lines yielding an executable of 1 meg? That's 1.4 bytes of
:>executable per line of code!

:>I can't imagine a program that generates 1.4 bytes of object code per line
:>of source code. Even assembly language isn't THAT tight.

Data division.

Comments.

Etc.

That is why I asked as to how many procedure division statements.

:>And we haven't even considered statically linked support modules. If we did,
:>you'd have a program that generates less than one byte of object code for
:>every COBOL statement!

I could do it.

:>I think your computer is drunk.
```

##### ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-02-22T20:42:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vu8_b.355$aq7.127814729@newssvr11.news.prodigy.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <GNSdna_BX_pUlaTdRVn-gg@giganews.com>`

```

LOL - He's probably talking about all division entries, comments,
maintenance history, jokes, names, addresses, and titles.

I've seen some pretty rancid COBOL programs in my time, but I
can recall any of them anywhere close to 700K statements, even
including all the nonsense I mentioned.

He could build another source, consisting only of the divisions,
and the program-id. errmsg. and get the messages from the com-
piler. I don't know if this has already ben suggested, nor if it would
even help, but as I recall, that's how it's done.

I might give a clue as to what limit may have been excluded.


Thanks - Gary



"JerryMouse" <nospam@bisusa.com> wrote in message
news:GNSdna_BX_pUlaTdRVn-gg@giganews.com...
> Gonzo wrote:
> > Hi, folks...
…[29 more quoted lines elided]…
> And we haven't even considered statically linked support modules. If we
did,
> you'd have a program that generates less than one byte of object code for
> every COBOL statement!
…[3 more quoted lines elided]…
>
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2004-02-23T03:27:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Nqe_b.74343$hR.1542319@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
Simplify your EVALUATE statements?

http://www-1.ibm.com/support/docview.wss?uid=swg1PQ44263

http://www-1.ibm.com/support/docview.wss?uid=swg1PQ50823

Gonzo <ckhamel1961.nospam@yahoo.com> wrote in message news:2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com...
> Hi, folks...
>
…[85 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2004-02-24T21:25:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OiP_b.5853$A%1.1876@newssvr23.news.prodigy.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <Nqe_b.74343$hR.1542319@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:Nqe_b.74343$hR.1542319@bgtnsc05-news.ops.worldnet.att.net...
> Simplify your EVALUATE statements?
>
…[3 more quoted lines elided]…
>

Hugh hit it mostly on the nose. It wasn't EVALUATEs, but PERFORMs. Had a
systems programmer look at my program today was aghast at the number of
PERFORMs in the program. One of my programmer assistants was trying to
modularize most of his coding, which would have been fine normally, but my
conversion file layout was much longer and complex than his other
assignments. The COBOL book says you can have over 4 million PERFORM
statements, but now I guess that's only in a "perfect" world. To borrow a
phrase from the "Pirates of the Caribbean" movie, "that thar COBOL rule book
is more like guidelines...... arrrr!"

Gonzo
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** Merlin43PhD@netscape.net (=D=)
- **Date:** 2004-02-23T07:26:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9d3c0262.0402230726.4ae333db@posting.google.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message news:<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>...
> Hi, folks...
> 
…[6 more quoted lines elided]…
> 

Is this program, by any chance, a banking application from some people
in Little Rock?  Although a 700K line procedure division would be
atrocious, desperately needing segmentation, it is not so unusual,
given some organizations habits with copy books to see absolutely
ridiculous data divisions.

The TRQB table is in a module left over from COBOL II and it has
brought its limits  with it.  While I do not remember the exact stuff
that it keeps track of during compilation, but I do recall that it
includes subscripted and implied redefines.  I suspect that, although
the total lines maximum has not been reached, the data divivison has
gone beyond what even the over-generous IBM programmers allowed. 
(Yeah, yeah, I know Billy thought 640K was plenty for a PC.)  I
suggest that you abandon some of the huge copy books and create new
ones that contain much more FILLER and define only those fields
actually used.
I say this having wrestled with some of the unpleasant side effects
from the above alluded vendor's poor code, wherein they often created
a 60-70K line data division for a 280 line procedure division.
```

##### ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2004-02-23T17:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65r_b.5672$WJ3.1628@newssvr23.news.prodigy.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <9d3c0262.0402230726.4ae333db@posting.google.com>`

```

"=D=" <Merlin43PhD@netscape.net> wrote in message
news:9d3c0262.0402230726.4ae333db@posting.google.com...
> Is this program, by any chance, a banking application from some people
> in Little Rock?

Ah, you're talking about my former employer whom I left in '96 after 14
years. I wonder if I'd still be there if I didn't make the move to my newer
employer with all the changes that they've been going through lately. To
answer your question.... no, it's not one of their programs, although it is
reminisent of what they did in some of their applications.

I did figure out what was going on, though. After a night's sleep, I hit
this again and found it was a program size issue. Yes, COBOL can accomodate
999,999 lines of code, but the system that it's compiling on may not like
it. It seems to be a transient problem (my buddy got hit with it at only
100K lines of code), as it didn't happen all the time. The larger the
program now, it won't compile.

I took to the obvious solution and sliced this up into smaller sub-programs
and presto-chango it worked. Of course, what's obvious on a good night's
sleep is not so obvious when sleep-deprived with caffiene-induced
hyperactive coding hallucinations.

I work in conversions where I use a code-generation tool that creates a lot
of code.... and as some guessed, much of it is comment lines for
documentation. Often I have just a couple of weeks to convert a lot of data
very quickly, so the program ain't pretty and usually has a lot of lines of
code (100k-300k lines of code isn't unusual for one of my conversion
programs, although I only "write" a fraction of that... the rest is the
generated code.). Most of the time it's easier (note I said "easier" and not
"better") to code everything in one program, but when I get more time to do
converts I try to make make them better by sub-programming them out. I just
thought I could get away with one very large program this time.... and I
almost did, too.... was just about finished coding.

> I say this having wrestled with some of the unpleasant side effects
> from the above alluded vendor's poor code, wherein they often created
> a 60-70K line data division for a 280 line procedure division.

Another comment about my former employer's applications... it's hard to
break from 1) tradition and 2) the idea of "if it works, don't muck with
it." There was always a constant battle over what was "better" internally.
Traditional coding was "top-down," where GO TOs were good and PERFORMs were
bad, and there were a lot of hangers-on of this old way of coding (me, for
one, I'll have to admit). I've been very slow over the years to see that
structured is better in most cases, and one of the benefits of my breaking
away from my old employer was that I was able to see other ways of doing the
same thing. I also saw them getting burned by clients by introducing new
products that didn't work well when rolled out, so there was always a demand
for keeping the status quo applications, however inefficient they were
becoming.

I really have nothing bad to say about them except that they failed to come
out of the 1960's in the way they coded/produced applications.

Regards,

Gonzo
```

###### ↳ ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** Merlin43PhD@netscape.net (=D=)
- **Date:** 2004-02-23T19:55:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9d3c0262.0402231955.6fc15014@posting.google.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <9d3c0262.0402230726.4ae333db@posting.google.com> <65r_b.5672$WJ3.1628@newssvr23.news.prodigy.com>`

```
"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message news:<65r_b.5672$WJ3.1628@newssvr23.news.prodigy.com>...


[snippage] - which stuff I appreciate, sympathize with, &c.

> ... There was always a constant battle over what was "better" internally.
> ...
> I really have nothing bad to say about them except that they failed to come
> out of the 1960's in the way they coded/produced applications.

That is it in a nutshell.  I met a lot of good (and very smart) folks
while working with that organization, but inertia had gotten the
better of them in some places.  I see similarities in my attempts to
beat Windoze XP into catering to my OS/2 habits.

Anyway, I am drifting off topic, so will leave it at that.
```

###### ↳ ↳ ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "Daniel L. Belton" <spam@abuse.gov>
- **Date:** 2004-02-24T13:07:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W%H_b.806$Er4.701@fe2.columbus.rr.com>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com> <9d3c0262.0402230726.4ae333db@posting.google.com> <65r_b.5672$WJ3.1628@newssvr23.news.prodigy.com>`

```

"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message
news:65r_b.5672$WJ3.1628@newssvr23.news.prodigy.com...
>
> "=D=" <Merlin43PhD@netscape.net> wrote in message
…[5 more quoted lines elided]…
> years. I wonder if I'd still be there if I didn't make the move to my
newer
> employer with all the changes that they've been going through lately. To
> answer your question.... no, it's not one of their programs, although it
is
> reminisent of what they did in some of their applications.


Ahhhh...  Little Rock...  I remember fondly the days I was there working for
harvest foods, and then ibm...
```

#### ↳ Re: COBOL Error Message Assist (MVS)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-03-02T19:14:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_151c.18122$aT1.4549@newsread1.news.pas.earthlink.net>`
- **References:** `<2nZZb.5239$Wq1.48@newssvr23.news.prodigy.com>`

```
FYI - I have contacted my "usually reliable" sources at IBM and they have
indicated that sometimes this is a compiler bug - and sometimes this is simply a
"too large" program.  They also told me that there are some existing APARs in
the database on the message. (I haven't checked for numbers).  The general
consensus is that 700k lines of program is probably "not a good idea" - even if
it does compile sometimes / most of the time. <G>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
