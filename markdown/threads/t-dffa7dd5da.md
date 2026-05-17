[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initializing tables

_17 messages · 4 participants · 2018-09 → 2018-10_

---

### Initializing tables

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T12:53:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com>`

```
Hello:

I'm thinking about how a table can be initialized statically in cobol. Obviously, one simple approach is to use REDEFINES. Here is how I might define the table {4, 9, 6, 3, 5, 1}:

01 barzilay.
05 pic 9 value is 4.
05 pic 9 value is 9.
05 pic 9 value is 6.
05 pic 9 value is 3.
05 pic 9 value is 5.
05 pic 9 value is 1.
01 dina redefines barzilay.
05 digit pic 9 occurs 6 times.

I was surprised that this won't work backwards, i.e., if I were to define

01 dina.
05 digit pic 9 occurs 6 times.
01 barzilay redefines dina.
05 pic 9 value is 4.
05 pic 9 value is 9.
05 pic 9 value is 6.
05 pic 9 value is 3.
05 pic 9 value is 5.
05 pic 9 value is 1.

then gnu cobol (3.0/linux) would have digit(1)...digit(6) initialized to zero. It would seem to me that if cobol were not to treat these two examples the same way, that the compiler should have prevented me from assigning initial values under the REDEFINE line.

Can someone please explain this behaviour?

Thanks,

Mayer
```

#### ↳ Re: Initializing tables

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T13:06:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com>`

```
In any event, here is how I'm planning to use this example:

01 gregorian-months-and-their-days.
05 initial-values.
10 pic 99 value is 31.
10 pic 99 value is 28.
10 pic 99 value is 31.
10 pic 99 value is 30.
10 pic 99 value is 31.
10 pic 99 value is 30.
10 pic 99 value is 31.
10 pic 99 value is 31.
10 pic 99 value is 30.
10 pic 99 value is 31.
10 pic 99 value is 30.
10 pic 99 value is 31.
05 table-definition redefines initial-values.
10 gmonth-max-days pic 99 occurs 12 times.

So I have gmonth-max-days(1) ... gmonth-max-days(12) with the maximum number of days per Gregorian month.
```

##### ↳ ↳ Re: Initializing tables

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:18:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p2@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap>`

```
On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
› In any event, here is how I'm planning to use this example:
› 
…[17 more quoted lines elided]…
› So I have gmonth-max-days(1) ... gmonth-max-days(12) with the maximum number of days per Gregorian month.

You can simplify this because those items are display numeric you can do:

05 initial-values PIC X(24) VALUE "31283130...".

and then redefine this as PIC 99 OCCURS 12.
```

###### ↳ ↳ ↳ Re: Initializing tables

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T14:24:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p3@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 9:18:47 PM UTC+3, Richard wrote:
› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
›› In any event, here is how I'm planning to use this example:
…[24 more quoted lines elided]…
› and then redefine this as PIC 99 OCCURS 12.

Does this mean that display numeric is always represented internally in big-endian?

Thanks,

Mayer
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 4)_

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-09-30T14:38:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p4@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p4@usenetarchives.gap>`

```
On Sun, 30 Sep 2018 11:24:37 -0700 (PDT), Mayer Goldberg
wrote:

› On Sunday, September 30, 2018 at 9:18:47 PM UTC+3, Richard wrote:
›› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
…[27 more quoted lines elided]…
› Does this mean that display numeric is always represented internally in big-endian?

No. "USAGE DISPLAY" items are stored as ASCII (or EBCDIC) characters.
The C equivalent of your example would be "31283130 ..." without the
trailing null character.

"USAGE COMPUTATIONAL" and "USAGE BINARY," to the best of my knowledge,
might be implemented like short and int and long in C. If you redefine
those -- I don't know if you can or not -- then you might have to deal
with what's big-endian and what's not.

Louis
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:50:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p4@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p4@usenetarchives.gap>`

```
On Monday, October 1, 2018 at 7:24:38 AM UTC+13, Mayer Goldberg wrote:
› On Sunday, September 30, 2018 at 9:18:47 PM UTC+3, Richard wrote:
›› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
…[28 more quoted lines elided]…
› 

Yes. It is represented internally as ASCII (or EDCDIC) characters exactly as you would want to see it displayed on a screen or a printer which is why it is called 'display'.
```

###### ↳ ↳ ↳ Re: Initializing tables

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-01T21:48:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p3@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap>`

```
On 1/10/2018 7:18 AM, Richard wrote:
› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
›› In any event, here is how I'm planning to use this example:
…[25 more quoted lines elided]…
› 
The way you have set it out is clear and most COBOL Programmers would be
happy with it.

Richard's simplification should also be acceptable to most people.

Here's a way that some would baulk at, but which I would use:

01 initial-values PIC X(24) VALUE "31283130...".

(Nothing else... no further definitions.)

Then, use refmodding to access it...

February... initial-values(3:2)

April... initial-values(7:2)

a general case derived from month number...
initial-values((monthNum * 2) -1:2)

No need for REDEFINES or OCCURS... and almost certainly more efficient
(depends on compiler optimization and platform...) but perhaps not as
immediately obvious as the original description.

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 4)_

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-10-01T22:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p7@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p7@usenetarchives.gap>`

```
On Tuesday, October 2, 2018 at 4:48:23 AM UTC+3, pete dashwood wrote:
› On 1/10/2018 7:18 AM, Richard wrote:
›› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
…[53 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

I don't see why redefine, which would give you a statically-initialized array, would be any less efficient than a substring computation at run-time, even under the best optimizations. The redefine solution is more general too, and would work with computational rather than Z's and 9's. Even if you wanted to work with fixed points or integers, it would be nicer to be able to define each number separately, possibly skipping any leading zeros... If you were to generalize the string approach, all numbers would have to be initialized using substrings of equal length. This would be annoying.

Mayer
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-02T00:17:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p8@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p7@usenetarchives.gap> <gap-dffa7dd5da-p8@usenetarchives.gap>`

```
On 2/10/2018 3:28 PM, Mayer Goldberg wrote:
› On Tuesday, October 2, 2018 at 4:48:23 AM UTC+3, pete dashwood wrote:
›› On 1/10/2018 7:18 AM, Richard wrote:
…[56 more quoted lines elided]…
› I don't see why redefine, which would give you a statically-initialized array, would be any less efficient than a substring computation at run-time, even under the best optimizations.

Because it ISn't a substring computation at run time for anything other
than the last case noted... Fixed subscripts and references are resolved
at compile time. If you wanted to implement the general case using your
REDEFINEd array, you'd still have to do the calculation and derive a
variable subscript which would then be used to index into the the table.

The redefine solution is more general too, and would work with
computational rather than Z's and 9's. Even if you wanted to work with
fixed points or integers, it would be nicer to be able to define each
number separately, possibly skipping any leading zeros...

Agreed. But that's not the case we are looking at.

If you were to generalize the string approach, all numbers would have
to be initialized using substrings of equal length. This would be annoying.

The values certainly need to be the same length. Whether that is
"annoying" or not is a matter of opinion... I see it as a one-time setup
when coding the data.

Anyway, I'm presenting this approach as being another approach than can
be used, nothing more.

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 4)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-10-02T00:16:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p7@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p7@usenetarchives.gap>`

```
On Tuesday, October 2, 2018 at 2:48:23 PM UTC+13, pete dashwood wrote:
› On 1/10/2018 7:18 AM, Richard wrote:
›› On Monday, October 1, 2018 at 6:06:41 AM UTC+13, Mayer Goldberg wrote:
…[49 more quoted lines elided]…
› immediately obvious as the original description.

I am not sure how you came to the conclusion that an expression with a multiply and subtraction followed by a substring could be "almost certainly more efficient" than a simple index. Anyway the result of the substring is not numeric so in addition it probably needs to be moved to a PIC 99 or such.
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-02T00:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p10@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p7@usenetarchives.gap> <gap-dffa7dd5da-p10@usenetarchives.gap>`

```
On 2/10/2018 5:16 PM, Richard wrote:
› On Tuesday, October 2, 2018 at 2:48:23 PM UTC+13, pete dashwood wrote:
›› On 1/10/2018 7:18 AM, Richard wrote:
…[52 more quoted lines elided]…
› I am not sure how you came to the conclusion that an expression with a multiply and subtraction followed by a substring could be "almost certainly more efficient" than a simple index.

Because I was thinking of the fixed cases which are resolved at compile
time. :-)

I agree that the general case might require more cycles... (You still
have to calculate your subscript for the general case though, so there
wouldn't be that much in it...)

Anyway the result of the substring is not numeric so in addition it
probably needs to be moved to a PIC 99 or such.

That's a very good point and I missed it...

Pete.



I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Initializing tables

_(reply depth: 6)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-10-02T01:15:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p11@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p3@usenetarchives.gap> <gap-dffa7dd5da-p7@usenetarchives.gap> <gap-dffa7dd5da-p10@usenetarchives.gap> <gap-dffa7dd5da-p11@usenetarchives.gap>`

```
On Tuesday, October 2, 2018 at 5:23:52 PM UTC+13, pete dashwood wrote:
› On 2/10/2018 5:16 PM, Richard wrote:
›› On Tuesday, October 2, 2018 at 2:48:23 PM UTC+13, pete dashwood wrote:
…[56 more quoted lines elided]…
› time. :-)

It was the last case that you followed with "almost certainly more efficient".

Why would you use the 'fixed cases'. There is _no_ point in having "move initial-values(5:2) ...' when you could just write "move 31 ..."


› I agree that the general case might require more cycles... (You still
› have to calculate your subscript for the general case though, so there
› wouldn't be that much in it...)

What 'calculation' is required for "move initial-values(month-number) ..."?
There is no multiply and subtract.

›   Anyway the result of the substring is not numeric so in addition it 
› probably needs to be moved to a PIC 99 or such.
…[8 more quoted lines elided]…
› I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Initializing tables

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2018-10-01T22:05:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p2@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap>`

```
On Sun, 30 Sep 2018 10:06:40 -0700 (PDT), Mayer Goldberg
wrote:

› In any event, here is how I'm planning to use this example:
› 
…[17 more quoted lines elided]…
› So I have gmonth-max-days(1) ... gmonth-max-days(12) with the maximum number of days per Gregorian month. 

Keep in mind that there are a mere 450 or so shopping days until 2020,
when you'll have to adjust the number of days in February.

Louis
```

###### ↳ ↳ ↳ Re: Initializing tables

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-10-01T22:18:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p13@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p13@usenetarchives.gap>`

```
On 2/10/2018 3:05 PM, Louis Krupp wrote:
› On Sun, 30 Sep 2018 10:06:40 -0700 (PDT), Mayer Goldberg
›  wrote:
…[26 more quoted lines elided]…
› 
:-) nice one, Louis...

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Initializing tables

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-10-01T22:24:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p13@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p2@usenetarchives.gap> <gap-dffa7dd5da-p13@usenetarchives.gap>`

```
On Tuesday, October 2, 2018 at 5:05:20 AM UTC+3, Louis Krupp wrote:
› On Sun, 30 Sep 2018 10:06:40 -0700 (PDT), Mayer Goldberg
›  wrote:
…[25 more quoted lines elided]…
› Louis

Not worried at all! :-) I would set up another table for leap years. It's cheaper than an if-statement at run-time.
```

#### ↳ Re: Initializing tables

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2018-09-30T14:15:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p16@usenetarchives.gap>`
- **In-Reply-To:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com>`

```
On Monday, October 1, 2018 at 5:53:30 AM UTC+13, Mayer Goldberg wrote:
› Hello:
› 
…[26 more quoted lines elided]…
› Can someone please explain this behaviour?

As the compiler proceeds through the code it creates the data items. In the first example it creates each item with the value specified and then creates the redefines as an alias to the existing items.

In the second example it would create the data items with default values and then find that it could create an alias to those items but can't do anything about the values because the items already have values.

Rather than force compiler writers to do things that are hugely complicated and aren't useful they just put it in the standard to not do that.

Tough. Get over it.
```

##### ↳ ↳ Re: Initializing tables

- **From:** "mayer.goldberg" <ua-author-14501850@usenetarchives.gap>
- **Date:** 2018-09-30T14:23:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dffa7dd5da-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dffa7dd5da-p16@usenetarchives.gap>`
- **References:** `<d5131721-3e85-49fe-b4b0-57eaa209fa89@googlegroups.com> <gap-dffa7dd5da-p16@usenetarchives.gap>`

```
On Sunday, September 30, 2018 at 9:15:41 PM UTC+3, Richard wrote:
› On Monday, October 1, 2018 at 5:53:30 AM UTC+13, Mayer Goldberg wrote:
›› Hello:
…[35 more quoted lines elided]…
› Tough. Get over it.

"I will survive!" :-)

Thanks for the explanation.

Mayer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
