[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Migration Issues

_6 messages · 5 participants · 1996-12_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### COBOL Migration Issues

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1996-12-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32BDB4D3.235B@arlington.net>`

```

Migration issues: COBOL to COBOL II and/or beyond (COBOL for VSE, LE
for VSE, for my shop)

My shop (VSE/ESA) is converting from IBM DOS/VS COBOL to IBM COBOL II.
We completed our online CICS programs, and have the batch programs to
go. The ideal situation might be to avoid COBOL II altogether, and
migrate our batch programs straight to COBOL for VSE. We are suppose to
be getting COBOL for VSE soon.

What are some pitfalls that we should be aware of?

Although I have no first hand proof, I have heard that you should avoid
the INITIALIZE statement because of its overhead. Is this true?

One problem we found was that the use of the RUN-TIME option WSCLEAR
seemed to have a negative impact on response time of our online
applications. So we eliminated that RUN-TIME option, but we had to move
LOW-VALUES to the map at the start of each program that included a map
to avoid an abend.

Joseph Lenz
```

#### ↳ Re: COBOL Migration Issues

- **From:** "seekermike" <ua-author-3832286@usenetarchives.gap>
- **Date:** 1996-12-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdb6769ee1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32BDB4D3.235B@arlington.net>`
- **References:** `<32BDB4D3.235B@arlington.net>`

```

Don't take INITIALIZE away from me, please! It's so much easier than
having to initialize each elementary item separately when some are
numeric and some are alphanumeric. That's one of the great features of
COBOL II and beyond.


Joseph Lenz wrote:
› 
› Migration issues:  COBOL to COBOL II and/or beyond (COBOL for VSE, LE
…[19 more quoted lines elided]…
› Joseph Lenz

Michael Shank
sek··.@ix.··m.com
http://serve.com/seeker/
```

##### ↳ ↳ Re: COBOL Migration Issues

- **From:** "bent hoff s��rensen" <ua-author-6585215@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdb6769ee1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fdb6769ee1-p2@usenetarchives.gap>`
- **References:** `<32BDB4D3.235B@arlington.net> <gap-fdb6769ee1-p2@usenetarchives.gap>`

```

Don't worry seeker!

That's what they used to say about the COMPUTE statement.

Don't take their word for it. Compile with the PMAP option and check the
assembly code (if you're in an IBM shop ((and if you know assembly
language)) ).

Ben

Seekermike skrev i artiklen
<32B··.@ix.··m.com>...
› Don't take INITIALIZE away from me, please!  It's so much easier than
› having to initialize each elementary item separately when some are
…[15 more quoted lines elided]…
›
```

#### ↳ Re: COBOL Migration Issues

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1996-12-22T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdb6769ee1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32BDB4D3.235B@arlington.net>`
- **References:** `<32BDB4D3.235B@arlington.net>`

```

Joseph Lenz wrote:
› 
› Migration issues:  COBOL to COBOL II and/or beyond (COBOL for VSE, LE
…[19 more quoted lines elided]…
› Joseph Lenz

According to Harvey Bookman's "COBOL/370", it is still more efficient to
initialize a table using the old trick of moving overlapping fields. In
some cases INITIALIZE may be somewhat inefficient because it generates a
move statement for each elementary field initialized. Obviously, if you can
initialize a group or record with a single "MOVE SPACES" or "MOVE LOW-VALUES"
there will be less machine code and slightly quicker execution. How often
do you need that much efficiency?

The INITIALIZE verb will NOT initialize elementary FILLER items. This
feature can be used to clear print lines without wiping out embedded
literals. Another advantage of INITIALIZE is that it is less likely to
require modifying procedure code if a record layout or copybook has changed.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard international
St. Louis, Missouri
```

#### ↳ Re: COBOL Migration Issues

- **From:** "inst..." <ua-author-4779510@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdb6769ee1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<32BDB4D3.235B@arlington.net>`
- **References:** `<32BDB4D3.235B@arlington.net>`

```


Subject: COBOL Migration Issues
From: Joseph Lenz
Date: Sun, 22 Dec 1996 16:23:15 -0600
Message-ID: <32B··.@arl··n.net>

Migration issues: COBOL to COBOL II and/or beyond (COBOL for VSE, LE
for VSE, for my shop)

My shop (VSE/ESA) is converting from IBM DOS/VS COBOL to IBM COBOL II.
We completed our online CICS programs, and have the batch programs to
go. The ideal situation might be to avoid COBOL II altogether, and
migrate our batch programs straight to COBOL for VSE. We are suppose to
be getting COBOL for VSE soon.

What are some pitfalls that we should be aware of?

Although I have no first hand proof, I have heard that you should avoid
the INITIALIZE statement because of its overhead. Is this true?

One problem we found was that the use of the RUN-TIME option WSCLEAR
seemed to have a negative impact on response time of our online
applications. So we eliminated that RUN-TIME option, but we had to move
LOW-VALUES to the map at the start of each program that included a map
to avoid an abend.


The INITIALIZE verb requires a lot of overhead to execute and can have a
detrimental effect on run time performance. What the verb was intended to
do was clear ws areas like counters or accumulators in the hopes that
programmers would group these data types together so as to take advantage
of this feature thus making their data sections more organised. What you
should NEVER do is initialize a file record that describes a hundred or
more fields (we've all seen these). Why this is so has to do with the way
INITIALIZE woks.
The working storage section of ANSI 85 COBOL programs is dynamically
generated at the time the program is loaded. Before it was static, the
WSS was generated by the compiler - that's why your CICS programs worked
when you weren't clearing the maps before you used them, the compiler may
have set the WS to low values beforehand; but this was a side effect not a
langauge feature. Newer COBOL programs maintain a list of each data
element's address, length and usage and INITIALIZE uses these lists to
determine how to clear each data item. Each invocation requires it to go
yet again through the list and if there are numerous fields to be
initialized it's going to take time. FILLER is by definition
unaddressable so elements described as such do not appear on the list and
subsequently cannot be initialized. If you were to waste your time
compiling a PMAP of a program that uses the INITIALIZE verb all you would
see is the passing of a parm list to an external module, since the newer
COBOL environments use dynamic callers to "helper modules" to implement
language functionallity, and this tells you nothing about that called
module's performance.

If you want to use the convience of the initialize verb without taking a
performance hit there is no reason why you can't initialize something once
then move it to a save area in WS and move it back into its original
position anytime you want to clear it. I'll bet anyone their boxed lunch
that one logical long move is a whole lot faster than watching a called
module plow through a list of field descriptors.


InstrJCC
```

##### ↳ ↳ Re: COBOL Migration Issues

- **From:** "bent hoff s��rensen" <ua-author-6585215@usenetarchives.gap>
- **Date:** 1996-12-25T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fdb6769ee1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fdb6769ee1-p5@usenetarchives.gap>`
- **References:** `<32BDB4D3.235B@arlington.net> <gap-fdb6769ee1-p5@usenetarchives.gap>`

```



InstrJCC skrev i artiklen
<199··.@lad··l.com>...
› 
› Subject: COBOL Migration Issues
…[31 more quoted lines elided]…
› langauge feature. 

I have found you to be quite knowledgeable instrJCC (why not use your
name?)
but this is a load of bull.
The working storage for a COBOL program in CICS is copied for each instance
of the program running at a given time. Otherwise you could not have a
normal
COBOL program re-entrant. Now back in the 'good old days' when we coded
macro level assembly language/COBOL programs we had to take care of the
dynamic
storage ourselves. But that's history. Along with COMMAND LEVEL CICS came
the
automatic new copy of WS.

› Newer COBOL programs maintain a list of each data
› element's address, length and usage

So did older COBOL programs (I expect you mean compilers ?) The DMAP has
existed for quite a few years now.

› and INITIALIZE uses these lists to
› determine how to clear each data item.  Each invocation requires it to go
› yet again through the list and if there are numerous fields to be
› initialized it's going to take time.

It sounds like something you've dreamed up yourself. The compiler can
easily insert
a MOVE SPACE/ZERO TO FIELDA at compile time. I know for a fact that the
COBOL
generation part of CSP is doing just that (apart from doing an INITIALIZE
as well ).

› FILLER is by definition
› unaddressable so elements described as such do not appear on the list and
…[13 more quoted lines elided]…
› module plow through a list of field descriptors.

Here I think you're absolutely right. But is it really worth the hassle ?
Extra variables.
Extra code. Extra possibilities for errors (when changing one area without
changing
the other one !). Etc. Etc.

›
› InstrJCC
›

I, for one, will definitely keep on using the INITIALIZE verb although
sparingly.

Ben
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
