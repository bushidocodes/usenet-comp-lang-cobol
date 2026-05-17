[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TRUNC(OPT) vs (BIN)

_8 messages · 7 participants · 1998-03_

---

### TRUNC(OPT) vs (BIN)

- **From:** "robin coyle floyd" <ua-author-17072987@usenetarchives.gap>
- **Date:** 1998-03-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd54f6$95673960$5fae6420@winkcf>`

```

I seek help and advice regarding use of these options in MVS, OS/390, and
VSE/ESA environments with either VS COBOL II or COBOL for MVS (or VSE)
compilers.

My company has several large software systems that run in these
environments. We use PIC S9(4) COMP (i.e. halfword) fields quite a bit and
have some usage of fullwords, too. We also unsigned fields, although I try
to discourage that. We depend on these fields holding their full binary
value 32,767, etc. With the ANSI 74 compilers (OS/VS COBOL and DOS/VS
COBOL) we used the noTRUNC option and had no problems.

When we (fairly recently) switched to the ANSI 85 compilers, we used
TRUNC(BIN), since the COBOL manual said that TRUNC(OPT) might truncate
under some circumstances. At the time, I "assumed" that BIN would use the
halfword instructions and generate reasonably efficient code, close to OPT.


I've finally had a chance to run some tests and look at the generated code
(LIST option), and now see that BIN uses a lot of packed data instructions,
and therefore runs quite a bit slower than OPT.

So now I want to start using OPT and am trying to figure out what
'truncation risk' I'll incur. Of course we'll run tests, but might not hit
every special case or be able to duplicate the volume of our customers.
I've coded a test program to simulate the ways we typically use COMP
fields, and haven't seen any truncation so far with OPT.

So I'd like to ask "what's been your experience with OPT" ? Sample code or
descriptions of usage where it truncates (or works correctly) would be
much appreciated.

Thanks in advance.

Ken Floyd
flo··.@i··.net
```

#### ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-20T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd54f6$95673960$5fae6420@winkcf>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf>`

```

Most people writing/maintaining MosT applications in MOST shops will have
absolutely NO problems with TRUNC(OPT) and will gain a LOT of performance
advantages with it. Although the older (and some current) documentation from
IBM talk about using TRUNC(BIN) with DB2, CICS, and PL/I, the new IBM view
is that you only need to do this IF you know the data is going to be bigger
than the PICTURE.

Now, if you KNOW that your data in PIC S9(04) fields is going to be larger
than +9999 but smaller than 32,767, (or is it 5?) then you MUST use
TRUNC(BIN) and suffer the consequences. However, you would actually be
better off changing the PIC (if it is an internal field, i.e. not one in a
file) to match the expected values.
```

##### ↳ ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abf8bf9165-p2@usenetarchives.gap>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf> <gap-abf8bf9165-p2@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Now, if you KNOW that your data in PIC S9(04) fields is going to be larger
…[4 more quoted lines elided]…
› 

Do you.. (or anybody else) know the reason why the default action is to
truncate a *binary* field to it's picture size??

For me that is only sensible for USAGE DISPLAY... but then again... I do
not set COBOL standards..:-)

And why change it to PIC S9(5)? Then you might just as well change it to
PIC S9(8).. as it no longer will be stored as a half-word.. but as a
full-word.

Why on earth should a compiler generate lots of inefficient code for
TRUNC(BIN)???? This should really be a default straight-forward action..
compared to "tons-of-code" to check "overflow" according to PIC size??

Come on.. all COBOL compiler programmers.. Give a good answer please!

****
/Geir
```

###### ↳ ↳ ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abf8bf9165-p3@usenetarchives.gap>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf> <gap-abf8bf9165-p2@usenetarchives.gap> <gap-abf8bf9165-p3@usenetarchives.gap>`

```

2 of the 3 of your questions, I can answer definitively. The other I can
make guesses at.

Answer to 2 first, What Picture you can fit in what storage is VERY
operating system/compiler specific. Let's look at your question. and use
Pic S9(02) vs S9(04). For some historical reason (that I don't know) IBM
mainframe (MVS) COBOLs have never been able to store/handle one-byte binary
fields; the smallest they handle is half-word. ON THE OTHER HAND, most (all
but IBM's?) Intel-targeted and Unix-targeted COBOLs can handle one-byte
binary fields. Historically, there was a LARGE number of architectures
ranging from 6-bit thru 8-bit architectures - so the largest number that
could be stored in a byte or half-word varied greatly.

OK - this brings us to your question 1. Why is truncation done to the
PICTURE clause and not to the amount of storage allocated. Although a
specific vendor/implementor on a specific platform with a specific release
of COBOL may know how much storage any PICTURE will allow, there is no way
the ANSI standard can know this. Therefore, for portability, the definition
of what are the acceptable values in a numeric field with other than USAGE
BINARY is *still* defined by the PICTURE and not the USAGE. This means that
such fields (particularly when used in files) are portable. (but read below
about what is coming in the next Standard).

Now for question 3 about why IBM has done what they did with TRUNC(BIN). I
don't really know. I think (but have not looked up the documentation) that
TRUNC(BIN) is only guaranteed to keep and use the full binary value in
certain cases, e.g. it works in compares, but not as the receiving item in
MOVES (I am NOT saying this is how it really works - I am just giving this
as an example of how it might work in one case but not another). Why would
IBM do this? The reason (and again I am guessing) is that their GOAL is
that any field that comes OUT of a COBOL program will agree with its Picture
clause (even if it came in "bad").

*****

Now for the "good news". The draft of the next Standard *does* introduce
some new binary types. These are defined EXCLUSIVELY by a USAGE clause and
have no PICTURE clause allowed. For example Binary-Char, Binary-Short,
Binary-Long, and Binary-Extended (each with or without a SIGNED option).
These fields are defined to hold the maximum range of values that their
allocated storage will allow. This will give you a portable (don't care
about TRUNC option) way of defining the type of fields that you want.
HOWEVER, it is still entirely implementor defined HOW much storage you will
get with each USAGE and therefore, what range of values you will be able to
put in each. (There are rules about Binary-Long has to be as large or
larger than Binary-Short - and I think there is even a set of "expected"
value ranges - but it is still all VERY implementor defined).

As my personal opinion is that the next Standard will be VERY lucky to be
approved in 2001 and 'we all" will be very lucky to see any conforming
implementations before 2003 or so, I would STRONGLY suggest that you contact
your vendor about implementing the new USAGEs before they implement the full
new Standard. However, if you don't care about a portable solution in the
next 5 years or so, you can just wait and use what they give you today.
```

##### ↳ ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "kenneth c. floyd" <ua-author-17074433@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abf8bf9165-p2@usenetarchives.gap>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf> <gap-abf8bf9165-p2@usenetarchives.gap>`

```

In most of the test cases I've run, TRUNC(OPT) did _not_ truncate. The
tests mostly involved S9(4) COMP fields. I moved data to them from 5 digit
COMP-3, added it, compared it, etc. And so far, no truncation. This was
with the COBOL for VSE compiler. I'm curious as to what behavior has
actually been observed with VS COBOL II and COBOL for MVS. Maybe someone
out their on an MVS machine with one of those compilers would volunteer to
run my test program and return the LIST (assembler) output and results ?

William M. Klein wrote in article
<6f1cf5$l.··.@dfw··m.com>...
› Most people writing/maintaining MosT applications in MOST shops will have
› absolutely NO problems with TRUNC(OPT) and will gain a LOT of performance
…[73 more quoted lines elided]…
›
```

##### ↳ ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-22T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-abf8bf9165-p2@usenetarchives.gap>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf> <gap-abf8bf9165-p2@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Most people writing/maintaining MosT applications in MOST shops will have
…[11 more quoted lines elided]…
› 

William,

Can you detail the behavioural differances between the different TRUC
options?
```

#### ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "rrp..." <ua-author-13513217@usenetarchives.gap>
- **Date:** 1998-03-20T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p7@usenetarchives.gap>`
- **In-Reply-To:** `<01bd54f6$95673960$5fae6420@winkcf>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf>`

```

Robin Coyle Floyd wrote:
› 
› I seek help and advice regarding use of these options in MVS, OS/390, and
…[16 more quoted lines elided]…
› I've finally had a chance to run some tests and look at the generated code
 
› (LIST option), and now see that BIN uses a lot of packed data instructions,
› and therefore runs quite a bit slower than OPT.
…[15 more quoted lines elided]…
› 

I don't know what problems there are with BIN vs. OPT either; but, I'll
be anxiously awaiting an answer from a kind poster! :)
```

#### ↳ Re: TRUNC(OPT) vs (BIN)

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-abf8bf9165-p8@usenetarchives.gap>`
- **In-Reply-To:** `<01bd54f6$95673960$5fae6420@winkcf>`
- **References:** `<01bd54f6$95673960$5fae6420@winkcf>`

```

Robin Coyle Floyd wrote:
›   (snip)
› So now I want to start using OPT and am trying to figure out what
…[9 more quoted lines elided]…
› Thanks in advance.

I believe that behavior of TRUNC(OPT) is to use the more efficient
binary instructions for arithmetic. But you will get truncation to the
picture size on DISPLAY. This should be easy to verify with simple
tests. You should also test MOVEing between different sizes of numeric
fields.

One problem with CICS is that it frequently requires you to use halfword
binary fields, but the new COBOL compilers don't support the old NOTRUNC
option. You can't enlarge your picture clause without creating other
problems with CICS.

I use TRUNC(OPT) in CICS COBOL all the time now. I haven't had a
problem yet.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
