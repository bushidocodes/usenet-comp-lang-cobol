[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (IBM) SHARE - LNGC requirements

_6 messages · 4 participants · 2004-03_

---

### Re: (IBM) SHARE - LNGC requirements

- **From:** robin <robin_v@bigpond.mapson.com>
- **Date:** 2004-03-16T12:53:30+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`

```
From: "Mark Yudkin" <myudkinATcompuserveDOTcom@nospam.org>, CompuServe Interactive Services
Date: Sun, 14 Mar 2004 11:35:38 +0100
.
| Currently, fixed bin and integer is even messier than you seem to realize:
| Under rules(ibm), fixed binary can be scaled,
.
Not really.  Try using the ADD, SUBTRACT, MULTIPLY, DIVIDE
builtins.  They force conversion to FIXED DECIMAL,
which is a real pain.
.
| but under rules(ans), fixed
| binary is exactly integer, as non-zero scale factors are not permitted (see
| the Programming Guide).
.
and the Language Reference.
```

#### ↳ Re: (IBM) SHARE - LNGC requirements

- **From:** "John W. Kennedy" <jwkenne@attglobal.net>
- **Date:** 2004-03-16T15:40:58+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<eeF5c.15172$F17.2200941@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`
- **References:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`

```
robin wrote:

> From: "Mark Yudkin" <myudkinATcompuserveDOTcom@nospam.org>, CompuServe Interactive Services
> Date: Sun, 14 Mar 2004 11:35:38 +0100
…[6 more quoted lines elided]…
> which is a real pain.

No they don't.
```

##### ↳ ↳ Re: (IBM) SHARE - LNGC requirements

- **From:** "James J. Weinkam" <jjw@cs.sfu.ca>
- **Date:** 2004-03-16T19:44:11-08:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<c38hh7$fkc$1@morgoth.sfu.ca>`
- **In-Reply-To:** `<eeF5c.15172$F17.2200941@news4.srv.hcvlny.cv.net>`
- **References:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au> <eeF5c.15172$F17.2200941@news4.srv.hcvlny.cv.net>`

```
John W. Kennedy wrote:
> robin wrote:
> 
…[15 more quoted lines elided]…
> 
Well, that appears to depend on the implementation you are using.  See my 
reply to Robin's message.
```

#### ↳ Re: (IBM) SHARE - LNGC requirements

- **From:** glen herrmannsfeldt <gah@ugcs.caltech.edu>
- **Date:** 2004-03-16T18:51:28+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<Q0I5c.25159$JL2.281399@attbi_s03>`
- **In-Reply-To:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`
- **References:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`

```
robin wrote:

(snip)

> Not really.  Try using the ADD, SUBTRACT, MULTIPLY, DIVIDE
> builtins.  They force conversion to FIXED DECIMAL,
> which is a real pain.

  "The base, scale, and mode of the result are determined by the rules 
for expression evaluation."

Though the fourth argument can only be supplied for FIXED types.

-- glen
```

##### ↳ ↳ Re: (IBM) SHARE - LNGC requirements

- **From:** "James J. Weinkam" <jjw@cs.sfu.ca>
- **Date:** 2004-03-16T19:46:59-08:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<c38hmg$fkc$2@morgoth.sfu.ca>`
- **In-Reply-To:** `<Q0I5c.25159$JL2.281399@attbi_s03>`
- **References:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au> <Q0I5c.25159$JL2.281399@attbi_s03>`

```
glen herrmannsfeldt wrote:
> robin wrote:
> 
…[13 more quoted lines elided]…
> 
Yeah, I thought so too until I tried it.  Just because the final result is 
binary does not guarantee that the computation is carried out in binary.  It 
seems to depend on the compiler being used.  At least the workstation products 
appear to convert to decimal for the actual computation.  Sad.  See my reply 
to Robin's message.
```

#### ↳ Re: (IBM) SHARE - LNGC requirements

- **From:** "James J. Weinkam" <jjw@cs.sfu.ca>
- **Date:** 2004-03-16T19:15:58-08:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<c38fsi$dre$1@morgoth.sfu.ca>`
- **In-Reply-To:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`
- **References:** `<eNC5c.106071$Wa.92831@news-server.bigpond.net.au>`

```
robin wrote:
> From: "Mark Yudkin" <myudkinATcompuserveDOTcom@nospam.org>, CompuServe Interactive Services
> Date: Sun, 14 Mar 2004 11:35:38 +0100
…[6 more quoted lines elided]…
> which is a real pain.

You are right!

Here is a quote from the description of the ADD(x,y,p,q) builtin function from 
the Personal PL/I for OS/2 Reference Manual:

"ADD returns the sum of x and y with a precision specified by p and q. The 
base, scale, and mode of the result are determined by the rules for expression 
evaluation."

Admittedly this does not actually say how the result will be arrived at, but 
if both operands are binary, then according to the rules for expression 
evaluation, the result will be binary, which certainly suggests that the 
operation will be carried out in binary.  Shows how wrong you can be.  Who in 
the world ever came up with such a preposterous idea?

I had always assumed that the purpose of the ADD, SUBTRACT, MULTIPLY, and 
DIVIDE builtin functions is to enable the programmer to deal more or less 
gracefully with situations in which the rules for determining the precision 
and scale factor of intermediate results in fixed point arithmetic are not 
appropriate for the application at hand.  After all, there is no single set of 
rules that is satisfactory for all applications.

This largely defeats the purpose of having the functions in the first place, 
at least for binary operands.  All I can say is STUPID, STUPID, STUPID.

I guess the reason that I have not previously discovered this is that 
virtually all of my uses of these functions have been in DECIMAL.

Did the F and Optimizing Compilers also behave this way?  Before seeing this 
thread, I would have sworn that they computed the result in binary if the 
operands were binary, but I can't remember for sure if I ever actually 
checked, so I could well be mistaken.  Does anyone remember?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
