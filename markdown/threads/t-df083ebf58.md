[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 2008 FUNCTION TRIM

_10 messages · 5 participants · 2006-05_

---

### 2008 FUNCTION TRIM

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-23T11:08:18+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4uje2$mlg$03$1@news.t-online.com>`

```
FUNCTION TRIM (arg   [LEADING/TRAILING])

Aaaagh, who thought that one up ?
Optional syntax as part of the argument list ??!!!

Roger
```

#### ↳ Re: 2008 FUNCTION TRIM

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-23T09:16:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dgnakF1a7gajU2@individual.net>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com>`

```
 Roger While<simrw@sim-basis.de> 05/23/06 3:08 AM >>>
>FUNCTION TRIM (arg   [LEADING/TRAILING])
>
>Aaaagh, who thought that one up ?
>Optional syntax as part of the argument list ??!!!

Hmm, isn't it actually
FUNCTION TRIM(arg [LEFT/RIGHT])

In any case, are you saying you'd prefer three separate functions, eg
FUNCTION TRIM(arg)
FUNCTION TRIM-LEFT(arg)
FUNCTION TRIM-RIGHT(arg)

Anyway, can't you just code it as

cobc_intr_trim(unsigned char *arg, int type)

Where type is, say, 0 for both, 1 for left and 2 for right?

Not that I know anything about compiler building, but I have been looking
through the source code.  :-)

Frank



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: 2008 FUNCTION TRIM

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-23T19:32:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4vgul$veg$02$1@news.t-online.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> schrieb im Newsbeitrag 
news:4dgnakF1a7gajU2@individual.net...
> Roger While<simrw@sim-basis.de> 05/23/06 3:08 AM >>>
>>FUNCTION TRIM (arg   [LEADING/TRAILING])
…[6 more quoted lines elided]…
>

Not according to the complete 2008 pdf mentioned in a post above -
"Specifically, http://www.cobolportal.com/j4/files/std.zip"


> In any case, are you saying you'd prefer three separate functions, eg
> FUNCTION TRIM(arg)
> FUNCTION TRIM-LEFT(arg)
> FUNCTION TRIM-RIGHT(arg)
>

Yes.
What on earth has the LEADING/TRAILING to do with the argument list ?
Answer - Nothing, they do NOT belong in between the parentheses.
Ridiculous. Does this read well ? ->
FUNCTION TRIM (FUNCTION TRIM (FUNCTION REVERSE (fld) LEADING) TRAILING)

> Anyway, can't you just code it as
>
…[6 more quoted lines elided]…
>

Oh, sure anything's doable. It's a question how.
:-)


Roger
```

###### ↳ ↳ ↳ Re: 2008 FUNCTION TRIM

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-05-23T10:57:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4vidv$2mn4$1@si05.rsvl.unisys.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net> <e4vgul$veg$02$1@news.t-online.com>`

```
As I recall, LEFT and RIGHT were disparaged on the grounds that they weren't 
well-defined in terms of a character string and the addressing of memory in 
a given platform.

Note that TRIM(x) in WD 1.6 returns a string with BOTH the leading and 
trailing spaces removed; TRIM (x, LEADING) leaves trailing spaces intact, 
and TRIM(x, TRAILING) leaves leading spaces intact.

Based on what I see in WD 1.5, I think there's a conflict between the syntax 
*diagram* and the syntax *rules* anyhow.  My guess is that "LEFT" should 
have been underlined as well; the absence of the underlining implies that it 
represents the default and may be omitted, and the returned values rules 
don't reflect that.

Optional arguments to procedures and functions are hardly new to computers; 
ALGOL's had them for a very, very long time.

    -Chuck Stevens

<top post, no more below>

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e4vgul$veg$02$1@news.t-online.com...
>
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> schrieb im Newsbeitrag 
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: 2008 FUNCTION TRIM

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-23T22:32:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24Mcg.14163$9j.11642@fe08.news.easynews.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net> <e4vgul$veg$02$1@news.t-online.com> <e4vidv$2mn4$1@si05.rsvl.unisys.com>`

```
Also, TRIM is not the only intrinsic function with "optional arguments".

The (older) RANDOM function could take ZERO or 1 argument

NUMVAL-C in the 2002 Standard has both LOCALE and ANYCASE as (optional) keywords

And LOWER-CASE and UPPER-CASE are also modified in the '08 draft to include the 
LOCALE keyword
```

###### ↳ ↳ ↳ Re: 2008 FUNCTION TRIM

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-24T07:47:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e50s0r$27u$01$1@news.t-online.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net> <e4vgul$veg$02$1@news.t-online.com> <e4vidv$2mn4$1@si05.rsvl.unisys.com> <24Mcg.14163$9j.11642@fe08.news.easynews.com>`

```
I am NOT arguing optional and/or variable argument lists.
That, of course, is perfectly OK.
What I object to is having an attribute of the function itself
as an argument. This really is not consistent.
So there should be
TRIM-LEADING, TRIM-TRAILING, LOCALE-NUMVAL-C,
LOCALE-LOWER-CASE, LOCALE-UPPER-CASE etc.

The current syntax is misleading in that it reads as though the
"function atrribute" (eg. LEADING, LOCALE) applies to the
argument to the function and not as a "directive" to the function.

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:24Mcg.14163$9j.11642@fe08.news.easynews.com...
> Also, TRIM is not the only intrinsic function with "optional arguments".
>
…[85 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: 2008 FUNCTION TRIM

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-24T07:13:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EITcg.23859$p_1.11361@fe03.news.easynews.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net> <e4vgul$veg$02$1@news.t-online.com> <e4vidv$2mn4$1@si05.rsvl.unisys.com> <24Mcg.14163$9j.11642@fe08.news.easynews.com> <e50s0r$27u$01$1@news.t-online.com>`

```
Notice that the Standards ('02 and draft '08) explicitly call these "keyword 
arguments".  Whether you like them or not, they do exist and I don't think there 
is any real chance of changing this.  You can, however, send in comments to J4 
or your "national body" for WG4.  Make certain that you comment on it during 
public review.
```

###### ↳ ↳ ↳ Re: 2008 FUNCTION TRIM

_(reply depth: 7)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-24T12:55:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e51e2h$fp5$00$1@news.t-online.com>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <4dgnakF1a7gajU2@individual.net> <e4vgul$veg$02$1@news.t-online.com> <e4vidv$2mn4$1@si05.rsvl.unisys.com> <24Mcg.14163$9j.11642@fe08.news.easynews.com> <e50s0r$27u$01$1@news.t-online.com> <EITcg.23859$p_1.11361@fe03.news.easynews.com>`

```
As a slight aside, with the advent of FUNCTION-ID,
it "should" be possible to code FUNCTIONS as
Cobol coded FUNCTION-ID modules  :-)
Of course, you can't as there is no definition for argument counts
and, even if, what do you do/pass with "keyword arguments"  :-)

OpenCOBOL has NUMBER-OF-CALL-PARAMETERS :-)

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:EITcg.23859$p_1.11361@fe03.news.easynews.com...
> Notice that the Standards ('02 and draft '08) explicitly call these 
> "keyword arguments".  Whether you like them or not, they do exist and I 
…[117 more quoted lines elided]…
>
```

#### ↳ Re: 2008 FUNCTION TRIM

- **From:** Peter Lacey <lacey@mts.net>
- **Date:** 2006-05-23T10:43:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44732D9E.6741FBAC@mts.net>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com>`

```
Roger While wrote:
> 
> FUNCTION TRIM (arg   [LEADING/TRAILING])
…[4 more quoted lines elided]…
> Roger

Nothing new about that.  Depending on the way it's implemented, it's no
problem flagging the last argument in some way so that the called
routine can determine that important fact.  In BAL, it used to be (and
may well still be) that the arguments were passed on by a series of
address constants,the last one of which had the high-order bit set on -
whether the called routine needed it or not.  Piece of cake.

PL
```

##### ↳ ↳ Re: 2008 FUNCTION TRIM

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-23T16:41:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dhhcrF19rf8mU1@individual.net>`
- **References:** `<e4uje2$mlg$03$1@news.t-online.com> <44732D9E.6741FBAC@mts.net>`

```
Peter Lacey<lacey@mts.net> 05/23/06 9:43 AM >>>
>Roger While wrote:
>> 
…[12 more quoted lines elided]…
>whether the called routine needed it or not.  Piece of cake.

If you mean z/Architecture Basic Assembly Language (and it's ancestors),
that is still the case.  COBOL (on z/Arch) follows this same standard.
Now if only COBOL could check for that high-order bit being set to allow for
easy 'variable argument' calls!
:-)

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
