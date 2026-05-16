[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# malformed subscript

_31 messages · 10 participants · 2003-08_

---

### malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-07T16:36:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```
Using netexpress 4.0 I get the following error

   665     ADD 1 TO WS-STAT-LAYT-COUNT
   666           (LAYT-PAPER,((WS-YMD-MM * 100) + WS-YMD-DD) ).
* 309-S*****************************************************           (
3)**
**    Malformed subscript

The field is declared like this.

   390 01  WS-STATISTICS.
   391     03  WS-STAT-PAPER            OCCURS 10.
   392         05  WS-STAT-LAYT-COUNT   PIC 9(4) COMP OCCURS 1231.
   393         05  WS-STAT-VERS-COUNT   PIC 9(4) COMP OCCURS 1231.


According to the documentation this should be allowed.

Any ideas.
```

#### ↳ Re: malformed subscript

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-08-07T18:23:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```

Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message
news:bgtv6d$7i3$1@sparta.btinternet.com...
> Using netexpress 4.0 I get the following error
>
…[16 more quoted lines elided]…
> Any ideas.

How is LAYT-PAPER defined?

It wouldn't be the simple fact of a missing space after LAYT-PAPER, ?
Or perhaps the space between the 2 final parentheses
is considered extraneous, or malformed as they put it.

Try this ?
(LAYT-PAPER, ((WS-YMD-MM * 100) + WS-YMD-DD)).
```

##### ↳ ↳ Re: malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T08:56:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgvoji$5ed$1@hercules.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net...
>
> Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message
…[31 more quoted lines elided]…
>

Nope still errors.
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-08-23T02:16:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030822221626.22063.00001315@mb-m07.aol.com>`
- **References:** `<bgvoji$5ed$1@hercules.btinternet.com>`

```
In this thread
Concerning  Steve Rainbird's <steve.rainbird@nospam.mssint.com>
orginal 'malformed subscript'

"Hugh Candlin" <no@spam.com> wrote in message
news:nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net...

snips
> ...
>
> Try this ?
> (LAYT-PAPER, ((WS-YMD-MM * 100) + WS-YMD-DD)).

Steve Rainbird steve.rainbird@nospam.mssint.com 
replied
Date: 8/8/03 3:56 AM EST
Message-id: <bgvoji$5ed$1@hercules.btinternet.com>

>Nope still errors

That is curious. Independent of the multidimmensional array subscripting snafu
so eloquently discoursed here I am very interested in knowing if the problem is
generalized even to single dimmensional arrays, in the compiler Steve is using.

Like this.

* terminate-previous-statement-clearly
* with a period.

ADD 1 TO
SINGLE-DIM-ARRAY, (simpe-subscript).

With a comma followed by a space in the array reference. If your compiler's
problem is generalized this ought to compile cleanly!

My point is really to disagree with a posting by Bill Klien to the effect that
the compiler ought to know that the item is or is not an array. Well, not
really. This kind of thing is actually type checking which is frequently
defered until _after_parse_ in a compiler. 

So the compiler authors are stuck with trying to sort things out lexically or
syntactically. And regrettably the COBOL comma is the worst thing in the
compiler writers life, a transparency.

In the discussions that have occured here it is definitely surprising that the
orginal poster states that a space after the comma did not solve the problem. 

How general is it? Does it happen in a MOVE as well as an ADD. Will it happen
in a COMPUTE, in the compiler under discussion?

A humorous variation of this inquiry would be what happens if you place the
space in front of the comma?  If we are dealing with internals that are
scanning for lookahead ciphers, then the internal trick needed to make the
comman transparent are good enough to swallow the comma but can't quite see
over the horizon to the following space according to the original posters
response.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-23T03:27:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%aB1b.1912$O03.1529@newsread2.news.atl.earthlink.net>`
- **References:** `<bgvoji$5ed$1@hercules.btinternet.com> <20030822221626.22063.00001315@mb-m07.aol.com>`

```
Just so it is clear, the "comma" is NOT a separator in ANSI/ISO COBOL (any
version - '68, '74, '85 or 2002).  To be a separator, the comma MUST be
followed by a space (in Standard COBOL).  Furthermore, where it IS followed
by a space it has NO special meaning other than that which is valid for a
space by itself.  This has been true in the '85 Standard and the 2002
Standard (I am not positive about earlier ones).  This means that the
following is PERFECTLY valid (Standard-conforming) code (no matter how UGLY)
and will compile with any "'85 Standard compliant" compiler:

 01 B.
    05 D   Pic,  9.
    05 A   Pic X.
    05 C occurs,  5 times Pic X.
        ...
  Move, A, of, B to, C (D, +, 1, )

On the other hand, although some compiler MIGHT allow it, the following is
NOT ANSI/ISO conforming (any version of the Standard):

 01 B.
    05 D   Pic 9.
    05 E   Pic 9.
    05 A   Pic X.
    05 C occurs 5 times.
         10 F   occurs 5 times   Pic X.
        ...
* no space between the comma and E in the following line
  Move A  to  F (D,E)
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 5)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-08-23T12:44:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QHOdnaExuq2XB9qiXTWJkA@comcast.com>`
- **References:** `<bgvoji$5ed$1@hercules.btinternet.com> <20030822221626.22063.00001315@mb-m07.aol.com> <%aB1b.1912$O03.1529@newsread2.news.atl.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:%aB1b.1912$O03.1529@newsread2.news.atl.earthlink.net...
> Just so it is clear, the "comma" is NOT a separator in ANSI/ISO COBOL (any
> version - '68, '74, '85 or 2002).  To be a separator, the comma MUST be
> followed by a space (in Standard COBOL).  Furthermore, where it IS
followed
> by a space it has NO special meaning other than that which is valid for a
> space by itself.  This has been true in the '85 Standard and the 2002
> Standard (I am not positive about earlier ones).  This means that the
> following is PERFECTLY valid (Standard-conforming) code (no matter how
UGLY)
> and will compile with any "'85 Standard compliant" compiler:
>
…[22 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

        Then I do not understand the problem, from the compiler's point of
view.  Unless in a quoted literal, ignore commas.

    Comma space would reduce to space.  If the comma is not followed by a
space,
trigger an error, as is done now.

    Or possibly a warning, and assume a space.


    Seems like life would be easier if they were allowed to make a comma a
separator.  Would that really hurt anything, other than the ability to take
your nonconforming code elsewhere?
```

##### ↳ ↳ Re: malformed subscript

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-23T06:31:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TMOdnYyVMrs2zdqiU-KYvg@giganews.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:
> Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message
> news:bgtv6d$7i3$1@sparta.btinternet.com...
…[19 more quoted lines elided]…
>

Uh,

2(occurances) x 2 (bytes each) x 1231 (entries) =  4924 bytes

4924 x 10 = 49,240-byte table size

Mighten this exceed the 32,000 byte limit sometimes imposed?
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-23T13:09:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308231209.37952923@posting.google.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net> <TMOdnYyVMrs2zdqiU-KYvg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> >>    666           (LAYT-PAPER,((WS-YMD-MM * 100) + WS-YMD-DD) ).
> >> * 309-S*****************************************************

> 4924 x 10 = 49,240-byte table size
> 
> Mighten this exceed the 32,000 byte limit sometimes imposed?

No.  And when was there ever a 32k limit ?  In any case it would have
complained at the OCCURS statement if this was the problem.

The problem was resolved as being the compiler treated the
parenthesized expression as a subscript of Layt-Paper instead of being
the 2nd subscript.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-23T21:16:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_QQ1b.923$jY2.693@newsread1.news.atl.earthlink.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net> <TMOdnYyVMrs2zdqiU-KYvg@giganews.com> <217e491a.0308231209.37952923@posting.google.com>`

```
Richard,
  I can't remember any more.  Were you the person originally reporting the
problem - and if so, did Micro Focus *accept* this as a compiler "bug"?
(They should have, but I just don't know if they have)
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** "Hugh Candlin" <hugh.candlin@worldnet.att.net>
- **Date:** 2003-08-24T08:08:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_n_1b.111764$0v4.7942803@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <nOwYa.91336$0v4.6208142@bgtnsc04-news.ops.worldnet.att.net> <TMOdnYyVMrs2zdqiU-KYvg@giganews.com>`

```
Why did you include my name in a post
when there is nothing attributable to me?

JerryMouse <nospam@bisusa.com> wrote in message
news:TMOdnYyVMrs2zdqiU-KYvg@giganews.com...
> Hugh Candlin wrote:
> > Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message
…[31 more quoted lines elided]…
>
```

#### ↳ Re: malformed subscript

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-08-07T14:52:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TexYa.6457$pq5.867233@news20.bellglobal.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```
Try putting a space before and after the plus sign.

Donald

"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
news:bgtv6d$7i3$1@sparta.btinternet.com...
> Using netexpress 4.0 I get the following error
>
…[30 more quoted lines elided]…
>
```

##### ↳ ↳ Re: malformed subscript

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-07T19:31:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sOxYa.1510$vo2.766@newsread1.news.atl.earthlink.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <TexYa.6457$pq5.867233@news20.bellglobal.com>`

```
The other question is which dialect (directive) are you using?  The syntax
diagram (for the extension of using an arithmetic expression as a subscript)
has MF and ISO2002 "bubbles".
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T08:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgvoks$5g1$1@hercules.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <TexYa.6457$pq5.867233@news20.bellglobal.com> <sOxYa.1510$vo2.766@newsread1.news.atl.earthlink.net>`

```
The default whatever that is.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:sOxYa.1510$vo2.766@newsread1.news.atl.earthlink.net...
> The other question is which dialect (directive) are you using?  The syntax
> diagram (for the extension of using an arithmetic expression as a
subscript)
> has MF and ISO2002 "bubbles".
>
…[15 more quoted lines elided]…
> > > * 309-S*****************************************************
(
> > > 3)**
> > > **    Malformed subscript
…[29 more quoted lines elided]…
>
```

##### ↳ ↳ Re: malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T08:56:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgvok6$5f6$1@hercules.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <TexYa.6457$pq5.867233@news20.bellglobal.com>`

```

"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:TexYa.6457$pq5.867233@news20.bellglobal.com...
> Try putting a space before and after the plus sign.
>
…[38 more quoted lines elided]…
>

There already is a space.
```

#### ↳ Re: malformed subscript

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-07T17:41:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308071641.14051654@posting.google.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote 

>    665     ADD 1 TO WS-STAT-LAYT-COUNT
>    666           (LAYT-PAPER,((WS-YMD-MM * 100) + WS-YMD-DD) ).
> * 309-S*****************************************************           (
> 3)**
> **    Malformed subscript


Try a space after the comma, or replace the comma with a space.

I predict that the parenthesised expression, while valid, is being
treated as a subcript of LAYT-PAPER rather than the 2nd subscript of
WS-STAT-LAYT-COUNT because there is an invalid separator between them.

(ie comma+space is valid, space is valid, comma by itself is not).
```

##### ↳ ↳ Re: malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T08:57:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgvomc$5hp$1@hercules.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <217e491a.0308071641.14051654@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308071641.14051654@posting.google.com...
> "Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote
>
…[13 more quoted lines elided]…
> (ie comma+space is valid, space is valid, comma by itself is not).

Your prediction was wrong but thanks for trying anyway.

Steve
```

#### ↳ Re: malformed subscript

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T08:55:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bgvoi9$nc6$1@sparta.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```

"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
news:bgtv6d$7i3$1@sparta.btinternet.com...
> Using netexpress 4.0 I get the following error
>
…[30 more quoted lines elided]…
>

Thanks for you help everybody.

The answer is to put parentheses around the 1st subscript.

 ((LAYT-PAPER),((WS-YMD-MM * 100) + WS-YMD-DD) )

Do we all agree its a bug?

regards

Steve
```

##### ↳ ↳ Re: malformed subscript

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-08T17:52:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<srRYa.2869$vo2.341@newsread1.news.atl.earthlink.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com>`

```
Steve,
  I think you are CORRECT that this is a BUG in the Micro Focus product.
There is a (semi-)relevant rule in the 2002 COBOL Standard (where using
arithmetic expressions as subscripts were introduced).  It says,

"If the first operator in an arithmetic expression is a unary operator, it
shall be immediately preceded by a left parenthesis if that arithmetic
expression immediately follows an identifier or another arithmetic
expression.

    NOTE For example, when '1' and '+ 2' are used as subscripts for a
two-dimensional table A, the arithmetic expression '+ 2' needs to be
enclosed in parentheses, as in A (1 (+ 2))."

However, I do NOT think that this really impacts your (failing) example of:

    WS-STAT-LAYT-COUNT (LAYT-PAPER ((WS-YMD-MM * 100) + WS-YMD-DD) ).

which works when you code:

   WS-STAT-LAYT-COUNT ((LAYT-PAPER) ((WS-YMD-MM * 100) + WS-YMD-DD) )

*UNLESS* LAYT-PAPER is (itself) a table, you should NOT need to put
parenthesis around it as the  compiler SHOULD know that what follows is
another subscript for the original item, for for this item.

FYI,
  It is true that you MUST put a space after the comma between subscripts
(or put a space instead of a comma).  A comma is ONLY a separator when
immediately followed by a space.  However, you have indicated that is NOT
your current problem.
```

##### ↳ ↳ Re: malformed subscript

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-08T14:59:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308081359.44fc7bb@posting.google.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com>`

```
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote

> The answer is to put parentheses around the 1st subscript.
> 
>  ((LAYT-PAPER),((WS-YMD-MM * 100) + WS-YMD-DD) )

That forces (Layt-Paper) to be treated as an arithmetic expression and
prevents the parenthes around the 2nd expression making the parser
think that it is a subscript of Layt-Paper.

You are correct that the comma is a red-herring.  It is most likely
completely ignored and the compiler is acting as if it wasn't there.

   a.  (X 1)      is obviously 2 subscripts: X and 1
   b.  (X (1))    is one subscript: X which is subscripted by 1
   c.  ((X) (1))  is two subscripts: expressions (X) and (1)

> Do we all agree its a bug?
That is irrelevant, the questions are: 

   Does MF agree it is a bug ?

   How should the compiler disambiguate case b ?
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-08T22:10:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com> <217e491a.0308081359.44fc7bb@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308081359.44fc7bb@posting.google.com...
> "Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote
>
…[20 more quoted lines elided]…
>    How should the compiler disambiguate case b ?


By the time that the compiler "gets" to case B, it should know whether X
requires a subscript or not.  If it requires one, then (1) must be a
subscript; if it does not require a subscript, then (1) must be another
subscript for the original table entry.   If the original table entry does
NOT have two-levels, then it is a source-code error.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-08T18:48:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308081748.383e7b03@posting.google.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com> <217e491a.0308081359.44fc7bb@posting.google.com> <udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote 

> >    b.  (X (1))    is one subscript: X which is subscripted by 1

> By the time that the compiler "gets" to case B, it should know whether X
> requires a subscript or not.  If it requires one, then (1) must be a
> subscript; if it does not require a subscript, then (1) must be another
> subscript for the original table entry.

Exactly.  The parser treated the expression as a subscript to
Layt-Paper and reported it as an error rather than moving on because a
subscript was invalid. This is a 'deficiency', or at least will be if
they claim 2002 conformance.

If the separator comma was actually being actioned instead of
discarded, then it may have guided the parser, but then it still has
to work with just a space separator which is also valid between a
variable and its subscript.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-08-23T22:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030823182122.21183.00000460@mb-m10.aol.com>`
- **References:** `<udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net>`

```
Bill Klien has commented 
(and I have heavily snipped)

>    b.  (X (1))    is one subscript: X 

>By the time that the compiler "gets" to case >B, it should know whether X
requires a subscript or not. 

Well, actually, the compiler does not get to B. It gets to the little pieces of
B one at a time and looks ahead trying to understand what the programmer has
coded. And that is a key note. Compilers need not only compile legitimate code
but they need to help us when we make an error. 

The full context of the original post, if I have grokked it all would be
something like the following:

TWO-DIM-ARRAT ( X (something-Y  

etcetera. Let me put a carat marker where any COBOL compiler writer is going to
have a real challenge:

TWO-DIM-ARRAY ( X ^ (something  

(the ^ carat marks a position in the parse forward scan).

When the parser has digested the two dimmensional array name, the first
parenthesis, and the data name X it is now looking ahead to the second open
parenthesis.

So there are atleast three possibilities. 

First, the second paren is the indication of a subscript of data item X. Bill's
assertion that the compiler 'should know' that X is not a subscripted item is
not exact enough for what compilers must do for us. We may make an error and
subscript X! And we need the compiler to tell us that is an error.

Second, and this has not been discussed. This is not meant to unnecessarily
confuse our valuable interaction. But the compiler writers deserve out fullest
support. The second paren could be the begining of a reference modification in
modern COBOLS. And that cannot be fully determined until it looks even
further-ahead and finds a colon.
And that is not necessarily right after the position of something-Y, if
something-Y is a parenthesized expression. In other words the lookahead
requirements here are not simple. Even if you wouldn't like to see a reference
modification here, a coder could do it, and the compiler has to be able to
parse through it successfully or get very lost.

Thirdly, the other possibility is the one the coder wants the compiler to
'see'.  The coder could be intending that the second paren is the begining of
an expression that has no relation to X. The problem here is that the coder
elected to write that expression as a parenthesized expression, which has
brought forth the ambiguity.

The more I look at this the more I move in the direction that there is no
compiler error here. If the second (or nth) subscript is a parenthesized
expression, you will have to parenthesize the preceeding expression (and that
recurses back to the next preceeding subscript, etc).

So, the notion that the compiler should know the type of the data item in
subscript postion 1, I humbly submit, is not correct for COBOL. And that is
because of the fact that we need the compiler to see those other things we
might do in the subscript area, intended or not, and legal or not, and diagnose
them.

Another possibility would be a mulformed function in subscript 1. The
malformation would be the absence of the word FUNCTION, but the presence of a
function name followed by parenthesized parameters.
(So a person might legitinately want max or min of some expression).

So, all in all, the original problem

TWO-DIM-ARRAY ( X  (something ))

(That is my abbreviated form).

might be said to look exactly like a reference to TWO-DIM-ARRAY with only one
subscript. And that subscipt is an invalidly subscripted variable X.  I think
the compiler was right.

Best Wishes to All
Bob Rayhawk 
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-24T03:27:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%gW1b.2328$jY2.103@newsread1.news.atl.earthlink.net>`
- **References:** `<udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net> <20030823182122.21183.00000460@mb-m10.aol.com>`

```
The 2002 Standard has explicitly CHANGED what is and is not valid as a
"subscript".  If you have the syntax


  Elem (A + (B (C)))

In a program to be compiled with a 2002 conforming compiler, there are LOTS
of things that this could mean and without knowing how many levels "Elem"
requires for subscripting and whether or not B requires subscripting, it is
impossible to parse this correctly (and/or tell if there is a compiler
error).

It is POSSIBLE that Elem requires 2 levels of subscripting and
  - level 1 is the value of A
  - Level 2 is the arithmetic expression "+ B (C)"

It is possible that Elem requires only 1 level of subscripting and
 - the subscript is the arithmetic expression "A + (B (C))"

It is possible that Elem requires NO subscripting or 3 levels of
subscripting and there is a source code error

It is possible that B doesn't require a single level of subscripting and
that there is a compile error

  ***

Again - with the CHANGE in the 2002 Standard allowing arithmetic expressions
as subscripts, it simply is IMPOSSIBLE to tell how to "parse" this phrase
without knowing how the various items  are defined and how many levels of
subscripts each item requires.

As far as the "requirement" for compiler to provide "user-friendly" messages
when there is a source code error, that is NICE when they can do it, but it
is not always possible for the compiler to make even a REASONABLE guess as
to which error you made.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 6)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-08-24T04:17:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030824001743.06755.00001525@mb-m03.aol.com>`
- **References:** `<%gW1b.2328$jY2.103@newsread1.news.atl.earthlink.net>`

```
Yes, so far as what you posted, to wit,


>  Elem (A + (B (C)))

But what will be a problem is 


  Elem (A ( + (B (C))))

If we look ahead and find the plus we are not in difficulty. If we look ahead
and see a paren we are in difficulty. We need to cut the compiler writer some
slack.

In compiler parlance, the second open paren, just past the carat symbol here
below

  Elem (A  ^ (


must associate with A or we are nolonger talking COBOL.  It cannot dissociate
and become another expression, index of Elem or anything else.

Unless, of course we put parens around A, like so, ...

  Elem ((A  ^) (


The A can be reduced to an expression, and then,

  Elem ((A  )^ (


the next open paren is clearly another expression.

You can surround an expression with parens, but if you put that after a
dataname (without protecting the data name  with parens) then the compiler
needs to think you are subscripting, or reference modifying (or even malforming
a function invocation).

I maintain the compiler discussed was write, and the imposition of the parens
around the first subscript is correct (and the only viable solution). There is
no compiler error in the situation originally posted, IMHO.

Best Wishes,
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-24T04:56:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1AX1b.2829$jY2.1378@newsread1.news.atl.earthlink.net>`
- **References:** `<%gW1b.2328$jY2.103@newsread1.news.atl.earthlink.net> <20030824001743.06755.00001525@mb-m03.aol.com>`

```
Given:

 Elem (A ( + (B (C))))

If A requires 1 level of subscripting *and* Elem requires 1 level of
subscripting, then the rules of the 2002 Standard "clearly" state that "( +
(B (C)))" is a valid arithmetic expression and is a valid subscript for A -
and this occurrence of A is the subscript for B.

If, on the other hand, ELEM requires 2 levels of subscripting and A requires
NO subscripting then,

 A is the first subscript
    and
  (+ (B (C))) is the second subscript to identify which occurrence of ELEM
is being reference

If, on the other hand, ELEM requires 2 levels of subscripts *and* A requires
one level of subscript, then this is a source code error and there is NO WAY
for the compiler to tell which subscript is missing - the 2nd one for Elem
or the first one for A.

One may (or may not) LIKE it, but this is simply the way the 2002 Standard
is written.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-08-23T22:24:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0308232124.552a46@posting.google.com>`
- **References:** `<udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net> <20030823182122.21183.00000460@mb-m10.aol.com>`

```
rkrayhawk@aol.com (RKRayhawk) wrote

> Second, and this has not been discussed. This is not meant to unnecessarily
> confuse our valuable interaction. But the compiler writers deserve out fullest
> support. The second paren could be the begining of a reference modification in
> modern COBOLS. And that cannot be fully determined until it looks even
> further-ahead and finds a colon.

I don't think that a reference modified variable can be used as a valid subscript.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-24T19:41:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gx82b.9102$8i2.7924@newsread2.news.atl.earthlink.net>`
- **References:** `<udVYa.4451$vo2.4069@newsread1.news.atl.earthlink.net> <20030823182122.21183.00000460@mb-m10.aol.com> <217e491a.0308232124.552a46@posting.google.com>`

```
The word "function" becomes optional (in certain cases) in the 2002
Standard, so

    Numval  (field-name (reference-start : reference-length)

could be a subscript - but I agree that I don't think a reference modified
item (which is alphanumeric - or National or Boolean) could be a subscript
by itself.  (I have said this without checking all the rules.  I might be
mistaken on this.)
```

###### ↳ ↳ ↳ Re: malformed subscript

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-08-08T22:25:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RrVYa.93297$0v4.6333173@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com> <217e491a.0308081359.44fc7bb@posting.google.com>`

```

Richard <riplin@Azonic.co.nz> wrote in message
news:217e491a.0308081359.44fc7bb@posting.google.com...
> "Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote
>
…[20 more quoted lines elided]…
>    How should the compiler disambiguate case b ?

I asked how LAYT-PAPER was defined, but received no answer.

The answer to your question is simple.  There is no ambiguity.
The definition for LAYT-PAPER will direct
the compiler regarding any possible subscript requirements
when LAYT-PAPER is referenced.  In addition,
the definition of the elementary item dictates the need
for a multi-level subscript when it is referenced.

While I am always extremely cautious of assigning blame
to an OS or to any widely used software component,
I think it is a parse error in the compiler, absent clarification
of the actual definition of LAYT-PAPER itself.
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 4)_

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-08-08T23:34:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bh1c1r$9oc$1@sparta.btinternet.com>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com> <217e491a.0308081359.44fc7bb@posting.google.com> <RrVYa.93297$0v4.6333173@bgtnsc04-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:RrVYa.93297$0v4.6333173@bgtnsc04-news.ops.worldnet.att.net...
>
> Richard <riplin@Azonic.co.nz> wrote in message
…[39 more quoted lines elided]…
>

Hugh,

My apologies. This is the definition.

       01 LAYT-DIRECTORY.
          03 LAYT-PAPER                        PIC S9(2) COMP-3 .
          03 LAYT-DATE                         PIC S9(8) COMP-3 .
          03 LAYT-NAME                         PIC X(12) .
          03 LAYT-IN-USE-STA                   PIC X(8) .
          03 LAYT-STATUS                       PIC S9(2) COMP-3 .

Regards

Steve
```

###### ↳ ↳ ↳ Re: malformed subscript

_(reply depth: 5)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-08-09T02:42:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcZYa.90864$3o3.6287943@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com> <bgvoi9$nc6$1@sparta.btinternet.com> <217e491a.0308081359.44fc7bb@posting.google.com> <RrVYa.93297$0v4.6333173@bgtnsc04-news.ops.worldnet.att.net> <bh1c1r$9oc$1@sparta.btinternet.com>`

```

Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message
news:bh1c1r$9oc$1@sparta.btinternet.com...
>
> "Hugh Candlin" <no@spam.com> wrote in message
…[10 more quoted lines elided]…
> > > That forces (Layt-Paper) to be treated as an arithmetic expression
and
> > > prevents the parenthes around the 2nd expression making the parser
> > > think that it is a subscript of Layt-Paper.
…[40 more quoted lines elided]…
>           03 LAYT-STATUS                       PIC S9(2) COMP-3 .

Thanks.

There is no subscripting required for LAYT-PAPER,
so there is an error in the way the compiler parses.

Those PIC S9(2) COMP-3 should be changed
to PIC S9(3) COMP-3 by the way.  Some
might even suggest using a COMP filed instead.
```

#### ↳ Re: malformed subscript

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-08-08T10:27:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tWKYa.96331$YN5.69014@sccrnsc01>`
- **References:** `<bgtv6d$7i3$1@sparta.btinternet.com>`

```
Steve I don't know net express but in any cobol I have ever used that first
inclusive parenthesis group is the subscript. It seems to include a
computational statement. If LAYT-PAPER is the subscript, and it is the
result of the computation((WS-YMF-MM * 100) + WS-YMD-DD)), try doing the
computation first. COMPUTE LAYT-PAPER =
((WS-YMF-MM * 100) + WS-YMD-DD)). Then just do a simple add to the
subscripted total. ADD 1 TO WS-STAT-LAYT-COUNT (LAYT-PAPER).
Hope this helped.
Bob
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
news:bgtv6d$7i3$1@sparta.btinternet.com...
> Using netexpress 4.0 I get the following error
>
…[30 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
