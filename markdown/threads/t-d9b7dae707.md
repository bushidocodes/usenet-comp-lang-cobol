[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexes are overused

_9 messages · 6 participants · 1999-04_

---

### Re: Indexes are overused

- **From:** "William J. Lightner" <calyn@arkansas.net>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3714210D.68104B19@arkansas.net>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com>`

```
An index is defined in most implementations as an offset from a given base
address.  A subscript is defined as a relative location from the start of the
table.  Difference?  An indexed entry is available on most platforms by
dereferncing once (usually a single machine instruction). No math is done.
Fastests possible access to a know address.  A subscript implicitly requires
that the actual index be calculated and then used, based on the relative offset
of the entry in the table that the subscript points to.  This means that the
address calculation must include both the offset, the relative position, and
the length of each individual entry in the table.  Few (if any) machine
architectures can do this and then use the resultant address in the same
instruction. Most also require some additonal housekeeping storag to do the
work.  So unless the index mechanism is not implemented by a given compiler,
using an index is ALWAYS faster than using a subscript.   Some compilers are
smart enough to not re-calculate the value of the index if it hasn't changed,
but that's as good as it gets.

Search all vs. All Comers:  If the table is above a certain minimal size
(something like 7 entries, last time I clocked it on an IBM 9000 running VM),
the Search All will beat any other method hands down.  The bigger the table,
the bigger the gap.  FWIW, the instream perform and the Search matched the
hand-coded goto loop in the same set of tests.  Given the improvements in
optimizing compilers over the last 10 years, any programmer who swears by
hand-coded tricks to get around compiler inefficiencies is completely lost.
Introducing gotos into Cobol code hamstrings the optimizer (read the manual),
and can actually result in slower and less efficient, and (certainly!) code
that is more difficult to maintain.

It is still up to the programmer to get the right algorithm into place.
Without that, all bets are off.  But hand-coding a loop, as well as a few other
"old programmer tricks"  is pointless and ill-advised.  You're better off using
the given verbs of the language so that the next guy (you, in six months?) can
understand what you were trying to do.

Beware 'cute' tricks.  Learn the language, and then use the toolset it
provides.

Later,

John Piggott wrote:

> Whatever the relative merits of indexes vs. subscripts (and this varies
> according to compiler) the coding job is not made any easier by the
…[31 more quoted lines elided]…
> > that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: Indexes are overused

- **From:** pgraham@dynasty.net
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fhlR2.1788$Qi2.3555@newsfeed.slurp.net>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net>`

```
"William J. Lightner" <calyn@arkansas.net> wrote:

| An indexed entry is available on most platforms by
|dereferncing once (usually a single machine instruction). No math is done.
…[4 more quoted lines elided]…
|the length of each individual entry in the table. 

But...  If the index is SET before each usage, the same extended
address calculation must be performed.  Only when the index is used
more than once for each SET, or when the index is manipulated by the
compiler, as in a PERFMORM VARYING or a SEARCH ALL is this overhead
not incurred.

Phil
```

##### ↳ ↳ Re: Indexes are overused

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3716450A.64F2504A@IMN.nl>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net>`

```
pgraham@dynasty.net wrote:

> "William J. Lightner" <calyn@arkansas.net> wrote:
>
…[4 more quoted lines elided]…
> address calculation must be performed.

No, f.e. a SET IDX UP BY is internally translated to "add xxx to idx" (where xxx is
the length in bytes of one element, known by the compiler).

>  Only when the index is used
> more than once for each SET,

No, no, not with the kind of SET I mentioned above.

> or when the index is manipulated by the
> compiler, as in a PERFMORM VARYING or a SEARCH ALL is this overhead
> not incurred.
>
> Phil

COBOL Frog
```

###### ↳ ↳ ↳ Re: Indexes are overused

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl>`

```
This goes back to my point that indexes may be faster for sequential access
e.g. set up by n, or especially when driven by special language constructs
which are already optimized by design e.g. perform incrementing an index,
search and search all, etc. but are most likely not faster for truly random
access because then you have to set, access, set, access, set, access, etc.
and then you may as well use a subscript, and indexes may even be slower in
such cases because it may be less apparent to the compiler what you're
trying to do.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 4)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371BA32B.A25C1924@IMN.nl>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl> <uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com>`

```
"Robert M. Pritchett" wrote:

> This goes back to my point that indexes may be faster for sequential access
> e.g. set up by n, or especially when driven by special language constructs
> which are already optimized by design e.g. perform incrementing an index,
> search and search all, etc.

Yes, indeed then indexes are faster.

> but are most likely not faster for truly random
> access because then you have to set, access, set, access, set, access, etc.
> and then you may as well use a subscript,

Yes, indeed not faster

> and indexes may even be slower in
> such cases because it may be less apparent to the compiler what you're
> trying to do.

No, set index to integer(litOrVar) is always to convert to address as fast
(slow) as subscripting. Only the arithnatic is done some time earlier.

> Robert M. Pritchett, President - RMP Consulting Partners LLC
> http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
…[3 more quoted lines elided]…
> that same contract on a 1099 as a self-employed independent contractor!
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 5)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371e7fed.2029808@netnews>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl> <uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com> <371BA32B.A25C1924@IMN.nl>`

```
'Twas Mon, 19 Apr 1999 23:42:04 +0200, when The COBOL Frog
<H.Klink@IMN.nl> illuminated comp.lang.cobol thusly:

>"Robert M. Pritchett" wrote:
 
>> and indexes may even be slower in
>> such cases because it may be less apparent to the compiler what you're
…[3 more quoted lines elided]…
>(slow) as subscripting. Only the arithnatic is done some time earlier.

If you set the index more times than you use it, then you're executing
that conversion code more times, and the code will be slower.

But this concern over efficiency is misguided.  The efficiency difference
is so small that it's trivial.  Indexes add complexity to the program
source, which causes inefficiency where it matters:  For the maintenance
programmer.
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 6)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371F4EC3.F92@saif.com>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl> <uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com> <371BA32B.A25C1924@IMN.nl> <371e7fed.2029808@netnews>`

```
Randall Bart wrote:
> 
> 'Twas Mon, 19 Apr 1999 23:42:04 +0200, when The COBOL Frog
…[26 more quoted lines elided]…
> l    |/ MS^7=6/28/107     http://users.aol.com/PanicYr00/Sequence.html


I agree with Randall!  Staff time is MUCH more expensive to an
organization than machine time.

Our #1 goal is maintainability, rather than machine efficiency.

Pete
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 7)_

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#Tpo3dSj#GA.355@nih2naac.compuserve.com>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl> <uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com> <371BA32B.A25C1924@IMN.nl> <371e7fed.2029808@netnews> <371F4EC3.F92@saif.com>`

```
Exactly. That's been my main point all along. The efficiency considerations
about subscripts vs. indexes are strictly secondary.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Pete Wirfs wrote in message <371F4EC3.F92@saif.com>...
>Randall Bart wrote:
>>
…[3 more quoted lines elided]…
>> >No, set index to integer(litOrVar) is always to convert to address as
fast
>> >(slow) as subscripting. Only the arithnatic is done some time earlier.
>>
…[3 more quoted lines elided]…
>> But this concern over efficiency is misguided.  The efficiency
difference
>> is so small that it's trivial.  Indexes add complexity to the program
>> source, which causes inefficiency where it matters:  For the maintenance
…[17 more quoted lines elided]…
>Pete
```

###### ↳ ↳ ↳ Re: Indexes are overused

_(reply depth: 8)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3724B954.82A53398@IMN.nl>`
- **References:** `<dbryantF9xosG.74I@netcom.com> <370E4FC7.FA8CCC60@NOSPAMhome.com> <dbryantF9xzqM.MK5@netcom.com> <uCW1CtQh#GA.295@nih2naad.prod2.compuserve.com> <3712BCA4.5241@compuserve.com> <3714210D.68104B19@arkansas.net> <fhlR2.1788$Qi2.3555@newsfeed.slurp.net> <3716450A.64F2504A@IMN.nl> <uU9BnH6h#GA.299@nih2naab.prod2.compuserve.com> <371BA32B.A25C1924@IMN.nl> <371e7fed.2029808@netnews> <371F4EC3.F92@saif.com> <#Tpo3dSj#GA.355@nih2naac.compuserve.com>`

```
As long as I like to compare indexes and subsripts in my private time, I feel
free to use my human time for that! :))

But I immediately agree that indexes serve no goal in 99% of programs. And
where it would, I think another language would be better choice. Subscripting
is readable and fast enough. With indexes it could be faster, though not in all
situations. And it can indeed made slower when wronly used.

I think, in the long run we all agree.

The Frog

"Robert M. Pritchett" wrote:

> Exactly. That's been my main point all along. The efficiency considerations
> about subscripts vs. indexes are strictly secondary.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
