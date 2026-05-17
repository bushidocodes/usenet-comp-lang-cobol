[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Holding you hostage with Math

_17 messages · 11 participants · 2018-07 → 2018-09_

---

### Holding you hostage with Math

- **From:** "jmccue" <ua-author-11340305@usenetarchives.gap>
- **Date:** 2018-07-28T22:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pjj8pg$oo8$1@dont-email.me>`

```
Interesting Article I ran across on Hacker News:

Tiny URL: https://tinyurl.com/y9mjyoqe

Real URL:
https://medium.com/@bellmar/is-cobol-holding-you-hostage-with-math-5498c0eb428b

John
```

#### ↳ Re: Holding you hostage with Math

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-07-29T02:10:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p2@usenetarchives.gap>`
- **In-Reply-To:** `<pjj8pg$oo8$1@dont-email.me>`
- **References:** `<pjj8pg$oo8$1@dont-email.me>`

```
On 7/28/2018 9:29 PM, John McCue wrote:
› Interesting Article I ran across on Hacker News:
› 
…[6 more quoted lines elided]…
› 

That was a fun read!

It turns out that COBOL fixed-point arithmetic is actually pretty
convenient for business accounting, and the Java programmers had no idea.

But you already knew that.

Just wait 'til they find out about block-mode I/O.

Kind regards,

https://www.arnoldtrembley.com/

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

##### ↳ ↳ Re: Holding you hostage with Math

- **From:** "hsweeney" <ua-author-14501823@usenetarchives.gap>
- **Date:** 2018-07-31T05:19:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p2@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p2@usenetarchives.gap>`

```
On Sunday, 29 July 2018 07:10:58 UTC+1, Arnold Trembley wrote:
› On 7/28/2018 9:29 PM, John McCue wrote:
›› Interesting Article I ran across on Hacker News:
…[12 more quoted lines elided]…
› convenient for business accounting, and the Java programmers had no idea.

Apparently somebody saw the need. There's now a java.math.BigDecimal class. (I'm not tryng to start a language war; I still believe that a common business-oriented language, on hardware with a commercial instruction set, will generally do business computation faster than Java.)

...
› Just wait 'til they find out about block-mode I/O.
Luckily, they have: the java.nio package was introduced in JDK 1.4.

Hugh
```

#### ↳ Re: Holding you hostage with Math

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-07-29T20:10:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p4@usenetarchives.gap>`
- **In-Reply-To:** `<pjj8pg$oo8$1@dont-email.me>`
- **References:** `<pjj8pg$oo8$1@dont-email.me>`

```
On 29/07/2018 2:29 PM, John McCue wrote:
› Interesting Article I ran across on Hacker News:
› 
…[6 more quoted lines elided]…
› 
It is indeed interesting.

However, for commercial applications dealing with currency, fixed point
to 4 places does very nicely in all of the commonly used languages.

S9(14)v9(4) represents (in COBOL) the "Currency" type for COM components
written in any language that implements the COM interface.

I don't think COBOL has any real advantage over anything else in this
regard.

The "performance hit" she describes for loading a library to support
decimal would only happen if the library was loaded dynamically, it has
no more impact if it is statically linked than compiled COBOL has.

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Holding you hostage with Math

- **From:** "doctrinsograce" <ua-author-6402540@usenetarchives.gap>
- **Date:** 2018-07-30T09:39:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p4@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap>`

```
It is fun to explain to a Java programmer about packed decimal.

Generally, when they finally understand it, they are quite impressed by it.
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-07-30T21:35:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p5@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p5@usenetarchives.gap>`

```
On 31/07/2018 1:39 AM, Doc Trins O'Grace wrote:
› It is fun to explain to a Java programmer about packed decimal.
›
› Generally, when they finally understand it, they are quite impressed by it.
›
I was impressed when I first encountered it in 1967... :-)

Pete.

I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Holding you hostage with Math

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2018-07-30T10:06:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p4@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap>`

```
On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
wrote:

› On 29/07/2018 2:29 PM, John McCue wrote:
›› Interesting Article I ran across on Hacker News:
…[14 more quoted lines elided]…
› written in any language that implements the COM interface.

PL/1 also has provision for fixed point. 4 decimal places would not
have been accurate enough for at least one of my COBOL programs.

Clark Morris
› 
› I don't think COBOL has any real advantage over anything else in this 
…[6 more quoted lines elided]…
› Pete.
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-07-30T13:36:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p7@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap>`

```
On 07/30/2018 10:06 AM, Clark F Morris wrote:
› On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
›  wrote:
…[31 more quoted lines elided]…
›› Pete.

Most people think 4 decimal places are enough for all money, but
that isn't necessarily true. :-)

bill
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-07-30T21:32:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p8@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap> <gap-2ba8cfa850-p8@usenetarchives.gap>`

```
On 31/07/2018 5:36 AM, Bill Gunshannon wrote:
› On 07/30/2018 10:06 AM, Clark F Morris wrote:
›› On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
…[39 more quoted lines elided]…
› 
I have never needed more than that for handling Dollars or Pounds, but
possibly for statistical reporting on currencies like Rupees or Pesos,
where numbers can be very large...

I'd be interested to see any (real life, not theoretical...) examples
you may have where it isn't enough.

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-07-31T08:06:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p9@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap> <gap-2ba8cfa850-p8@usenetarchives.gap> <gap-2ba8cfa850-p9@usenetarchives.gap>`

```
On 07/30/2018 09:32 PM, pete dashwood wrote:
› On 31/07/2018 5:36 AM, Bill Gunshannon wrote:
›› On 07/30/2018 10:06 AM, Clark F Morris wrote:
…[49 more quoted lines elided]…
› Pete.

It's probably old enough to not even be findable on the
WayBack Machine but there was a news story that made the
rounds on USENET back before the INTERNET was even a dream
about a COBOL Programmer in NYC working for a very large
and well known bank. While programming some of their
accounting software he asked what to do with the
computations beyond mils. He was told "We don't care."
He proceeded to add them to his own personal account.
When you are dealing in millions of dollars a day it
is more than you might think. He got fired. And I doubt
he got to keep the money. He was not charged with theft
as he did what he was told. It was considered unethical,
however. I am sure today financial institutions track
all of it to many decimal places. One hundreth of a
mil (.000001) on a trillion dollars is still $100,000.

bill
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-07-31T11:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p10@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap> <gap-2ba8cfa850-p8@usenetarchives.gap> <gap-2ba8cfa850-p9@usenetarchives.gap> <gap-2ba8cfa850-p10@usenetarchives.gap>`

```
On Tuesday, July 31, 2018 at 8:07:01 AM UTC-4, Bill Gunshannon wrote:
› On 07/30/2018 09:32 PM, pete dashwood wrote:
›› On 31/07/2018 5:36 AM, Bill Gunshannon wrote:
…[68 more quoted lines elided]…
› bill

Looks like the plot from Superman III.

Here's an article that discusses this type of scam.
< https://filmschoolrejects.com/getting-rich-with-richard-pryors-banking-scheme-from-superman-iii-7811840a8a0/ >

Of note is this:

"What about all those fractions of cents?

"Banks and corporations don’t simply truncate the final value,
as Gus’s colleague suggests in Superman III. Instead, the
numbers are preserved internally to five or six decimal places.
Then the value is rounded rather than truncated when a check
is cut or a deposit is made. That means that instead of just
chopping off those fractions of a cent, they round up or down
to the nearest cent."

That is, a claim of "five or six decimal places".
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

_(reply depth: 7)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-07-31T12:56:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p11@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap> <gap-2ba8cfa850-p8@usenetarchives.gap> <gap-2ba8cfa850-p9@usenetarchives.gap> <gap-2ba8cfa850-p10@usenetarchives.gap> <gap-2ba8cfa850-p11@usenetarchives.gap>`

```
On 07/31/2018 11:00 AM, Rick Smith wrote:
› On Tuesday, July 31, 2018 at 8:07:01 AM UTC-4, Bill Gunshannon wrote:
›› On 07/30/2018 09:32 PM, pete dashwood wrote:
…[89 more quoted lines elided]…
› 

I have no doubt the story I mentioned is where they got the
idea. At the time, using COBOL, the money probably would
have been "rounded" if there were only 4 decimal places

But given the ability to add more precision, at that point
in time, one could skim the extra off. I seriously doubt
the same thing could be done today. And, at the time the
real incident happened, it was not considered a scam. Just
poor moral fiber. :-)

bill
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-07-30T21:39:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p7@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap>`

```
On 31/07/2018 2:06 AM, Clark F Morris wrote:
› On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
›  wrote:
…[20 more quoted lines elided]…
› have been accurate enough for at least one of my COBOL programs.

Can you share more details, Clark?

I have worked in a number of Banks and never seen a use case where more
than 4 decimals were required for transactions in real currency (not
management reporting).

I don't doubt what you say, but I'd be interested to see why 4 was not
enough...

Pete.



I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

_(reply depth: 4)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2018-07-31T19:53:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p13@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap> <gap-2ba8cfa850-p13@usenetarchives.gap>`

```
On Tue, 31 Jul 2018 13:39:30 +1200, pete dashwood
wrote:

› On 31/07/2018 2:06 AM, Clark F Morris wrote:
›› On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
…[30 more quoted lines elided]…
› enough...

Since this was in the early to mid 1970s, I think the use was for
ratios between list and net prices on inventory (maybe list and
inventory cost of sales). I also have seen exchange rate calculations
to more than 4 decimal places. See the appropriate online documents
from the United States federal reserve or Bank of Canada. I'm not
certain if I have used more than 4 decimal places when calculating
various figures for my income tax in both those countries (US citizen
living in Canada filing and paying to both countries). I suspect the
primary use would be in calculating various ratios and then applying
them. An oil company I worked for had inventories that could change
with the weather.

While I can't speak for other relational data bases, DB2 allows
specification of decimal data with various precisions.

Clark Morris
›
› Pete.
›
›
```

###### ↳ ↳ ↳ Re: Holding you hostage with Math

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2018-08-01T08:35:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p7@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p4@usenetarchives.gap> <gap-2ba8cfa850-p7@usenetarchives.gap>`

```
On Tuesday, July 31, 2018 at 12:06:47 AM UTC+10, Clark F Morris wrote:
› On Mon, 30 Jul 2018 12:10:55 +1200, pete dashwood
›  wrote:
…[20 more quoted lines elided]…
› have been accurate enough for at least one of my COBOL programs.

PL/I has decimal fixed-point, as well as binary fixed-point.
```

#### ↳ Re: Holding you hostage with Math

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-27T17:46:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p16@usenetarchives.gap>`
- **In-Reply-To:** `<pjj8pg$oo8$1@dont-email.me>`
- **References:** `<pjj8pg$oo8$1@dont-email.me>`

```
A great article! Reminds me that Intel stopped support for BCD in 64bit code. Current microprocessors support BCD in 32-bit mode only. I wonder what effect this might have on COBOL implementations for x86.

Mayer

On Sunday, July 29, 2018 at 5:29:05 AM UTC+3, John McCue wrote:
› Interesting Article I ran across on Hacker News:
› 
…[5 more quoted lines elided]…
› John
```

##### ↳ ↳ Re: Holding you hostage with Math

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2018-09-27T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2ba8cfa850-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2ba8cfa850-p16@usenetarchives.gap>`
- **References:** `<pjj8pg$oo8$1@dont-email.me> <gap-2ba8cfa850-p16@usenetarchives.gap>`

```
On Thu, 27 Sep 2018 14:46:53 -0700 (PDT), Mayer Goldberg
wrote:

› A great article! Reminds me that Intel stopped support for BCD in 64bit code. Current microprocessors support BCD in 32-bit mode only. I wonder what effect this might have on COBOL implementations for x86.
› 
…[10 more quoted lines elided]…
›› John


The six old decimal instructions on x86 were basically useless for
everything. Including implementing decimal math for Cobol (or
anything else), and so their loss does not impact that.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
