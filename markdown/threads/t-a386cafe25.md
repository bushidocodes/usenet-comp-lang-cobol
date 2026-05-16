[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interpreting a COBOL numeric field in a raw, fixed width TXT file

_8 messages · 6 participants · 2007-01_

---

### Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "craig" <craigfmitchell@gmail.com>
- **Date:** 2007-01-10T13:21:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com>`

```
Hi,

Please forgive me if this question is too basic.  I've done quite a bit
of searching for an answer without any luck.

I am trying to understand a numeric amount field in a publicly
available federal election campaign finance file from the FEC web site
so that I might correctly load it into various databases.  I won't be
using COBOL to do any of the data loading.

In the raw, fixed width, text form of this data, there is a 7 character
numeric field described like this by the FEC:

     "In the fixed width text file, the amounts
     are in COBOL format. If the value is negative,
     the right most column will contain a special
     character:  ] = -0, j = -1, k = -2, l = -3,
     m = -4, n = -5, o = -6, p = -7, q = -8,
     and r = -9.

     In the database file, the amount field contains
     positive and negative integers."

I don't understand this explanation. Does anything other than a "]"
indicate the decimal should be shifted for the negative number?

This demonstrates my poor understanding:

"0000100" would be + 100
"000100]" would indicate a negative number, but would it be: - 100?
"000100r" would also indicate a negative number, but how would it be
different from the example above?

Any help on this issue will be very appreciated!

       - Thanks,

               Craig

Reference: ftp://ftp.fec.gov/FEC/indiv06.txt
```

#### ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-01-10T17:28:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12qaq9eiaskuh0f@corp.supernews.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com>`

```

"craig" <craigfmitchell@gmail.com> wrote in message
news:1168464083.491639.98290@k58g2000hse.googlegroups.com...
> Hi,
>
…[19 more quoted lines elided]…
>      positive and negative integers."

The characters shown for negative values are actually
the lower case equivalent of the representation of
zoned decimal as they appear in EBCDIC. These are
not a valid COBOL format for any COBOL
implementation I am aware of.

> I don't understand this explanation. Does anything other than a "]"
> indicate the decimal should be shifted for the negative number?
…[6 more quoted lines elided]…
> different from the example above?

When the last position contains a number, place a "+"
before the number.

When the last position contains one of the characters
shown, place a "-" before the number and replace the
character with the correcsponding digit.

"0000100" becomes "+0000100"
"000100]" becomes "-0001000"
"000100r" becomes "-0001009"

Then use the resulting translation.

> Any help on this issue will be very appreciated!
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-01-10T19:51:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12qb60dd3a2us31@news.supernews.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com> <12qaq9eiaskuh0f@corp.supernews.com>`

```
Rick Smith wrote:

>
> The characters shown for negative values are actually
…[3 more quoted lines elided]…
> implementation I am aware of.

The representation is valid for all forms of COBOL wherein the PIC used is 
S9(7).
```

###### ↳ ↳ ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-01-11T00:20:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168503649.618352.104780@i56g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<12qb60dd3a2us31@news.supernews.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com> <12qaq9eiaskuh0f@corp.supernews.com> <12qb60dd3a2us31@news.supernews.com>`

```

HeyBub wrote:
> Rick Smith wrote:

>>    "In the fixed width text file, the amounts
>>     are in COBOL format. If the value is negative,
…[12 more quoted lines elided]…
> S9(7).

What do you mean by 'all' ?  It seems to match none that I know of.
Those characters will certainly be invalid for the ASCII compilers that
I am familiar with and are not the ones that I would associate with
EBCDIC - my references only show '}' and upper-case letters.

Then there may be some of the 'all forms of COBOL' where they use
something completely different for negative.
```

###### ↳ ↳ ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-01-11T16:29:03+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p7icq2psqduavi64jc91sn9d6gvn99n1bf@4ax.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com> <12qaq9eiaskuh0f@corp.supernews.com> <12qb60dd3a2us31@news.supernews.com> <1168503649.618352.104780@i56g2000hsf.googlegroups.com>`

```
On 11 Jan 2007 00:20:49 -0800 "Richard" <riplin@Azonic.co.nz> wrote:

:>HeyBub wrote:
:>> Rick Smith wrote:

:>>>    "In the fixed width text file, the amounts
:>>>     are in COBOL format. If the value is negative,
:>>>     the right most column will contain a special
:>>>     character:  ] = -0, j = -1, k = -2, l = -3,
:>>>     m = -4, n = -5, o = -6, p = -7, q = -8,
:>>>     and r = -9.

:>> > The characters shown for negative values are actually
:>> > the lower case equivalent of the representation of
:>> > zoned decimal as they appear in EBCDIC. These are
:>> > not a valid COBOL format for any COBOL
:>> > implementation I am aware of.

:>> The representation is valid for all forms of COBOL wherein the PIC used is
:>> S9(7).

:>What do you mean by 'all' ?  It seems to match none that I know of.
:>Those characters will certainly be invalid for the ASCII compilers that
:>I am familiar with and are not the ones that I would associate with
:>EBCDIC - my references only show '}' and upper-case letters.

:>Then there may be some of the 'all forms of COBOL' where they use
:>something completely different for negative.

PIC S9(whatever) has the last character defined as carrying the sign.

One would not do a 

     MOVE 99J TO SIGNED-FIELD

one would do

     MOVE -991 TO SIGNED-FIELD
```

###### ↳ ↳ ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-01-11T09:33:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168536832.234083.121140@77g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<p7icq2psqduavi64jc91sn9d6gvn99n1bf@4ax.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com> <12qaq9eiaskuh0f@corp.supernews.com> <12qb60dd3a2us31@news.supernews.com> <1168503649.618352.104780@i56g2000hsf.googlegroups.com> <p7icq2psqduavi64jc91sn9d6gvn99n1bf@4ax.com>`

```

Binyamin Dissen wrote:
> On 11 Jan 2007 00:20:49 -0800 "Richard" <riplin@Azonic.co.nz> wrote:
>
…[8 more quoted lines elided]…
> :>>>     and r = -9.

> One would not do a
>
…[4 more quoted lines elided]…
>      MOVE -991 TO SIGNED-FIELD

And on which system would you get _lower-case_ 'j' in the last postion ?
```

##### ↳ ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "craig" <craigfmitchell@gmail.com>
- **Date:** 2007-01-11T09:30:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168536654.114658.105030@77g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<12qaq9eiaskuh0f@corp.supernews.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com> <12qaq9eiaskuh0f@corp.supernews.com>`

```
Thanks Rick and everyone else.  The explanation Rick gave:

   When the last position contains one of the characters
   shown, place a "-" before the number and replace the
   character with the correcsponding digit.

   "0000100" becomes "+0000100"
   "000100]" becomes "-0001000"
   "000100r" becomes "-0001009"

makes a lot of sense to me, and now I've heard it from more than one
source.  Thanks for all of your efforts.  This group is great!

   - Craig
```

#### ↳ Re: Interpreting a COBOL numeric field in a raw, fixed width TXT file

- **From:** "George" <georgech@hkstar.com>
- **Date:** 2007-01-11T00:28:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168504122.701249.299170@p59g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com>`
- **References:** `<1168464083.491639.98290@k58g2000hse.googlegroups.com>`

```
Dear Craig,

I cannot read the file ftp://ftp.fec.gov/FEC/indiv06.txt. However, I
guess that the negative value is talking about the exponent of the
amount. That is, the decimal place of the amount.
How, do you think?

Yours sincerely,
George

craig 寫道：

> Hi,
>
…[37 more quoted lines elided]…
> Reference: ftp://ftp.fec.gov/FEC/indiv06.txt
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
