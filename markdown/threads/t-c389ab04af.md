[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting a three dimensional array

_7 messages · 6 participants · 1996-10_

---

### Sorting a three dimensional array

- **From:** "jim farland" <ua-author-17087174@usenetarchives.gap>
- **Date:** 1996-10-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3260371D.7ED@gte.net>`

```

Hello;

I am developing a report for school and we must use a three dimensional
array to colloct information for a Company by Region-Division by Region
type total analysis report. The records being read in from the database
are in a random order. The information appearing on the report is
broken out by Company/Region-Division/Region, but Region 12 data might
appear before Region 01 data. What is the best way to sort a three
dimensional array? The array appears as follows:

LEVEL 2 ACCUMLATORS TABLE
01 WV-VARIABLES.
05 WS-LVL-2-TBL.
10 WS-COMPANY-GRP OCCURS 8 TIMES
15 WS-CD-CO PIC S9(4) COMP.
15 WS-LVL1-CTR PIC S9(2) COMP.
15 WS-LVL1-GRP OCCURS 50 TIMES
20 WS-CD-REGION-DIV PIC X(3) COMP.
20 WS-LVL12-CTR PIC S9(3) COMP.
20 WS-LVL2-GRP OCCURS 200 TIMES
25 WS-CD-REGION PIC X(3).
25 WS-RES-COUNTER PIC S9(9) COMP.
25 WS-RES-DEP-AMT PIC S9(9)V99 COMP.
25 WS-RES-IN-AMT PIC S9(9)V99 COMP.
25 WS-COM-COUNTER PIC S9(9) COMP.
25 WS-COM-DEP-AMT PIC S9(9)V99 COMP.
25 WS-COM-INT-AMT PIC S9(9)V99 COMP.
25 WS-IND-COUNTER PIC S9(0) COMP.
25 WS-IND-DEP-AMT PIC S9(9)V99 COMP.
25 WS-IND-INT-AMT PIC S9(9)V99 COMP.
25 WS-BILLED-COUNTER PIC S9(9) COMP.
25 WS-BILLED-AMT PIC S9(9)V99
COMP.

Any help is appreciated.

Thank you in advance.
```

#### ↳ Re: Sorting a three dimensional array

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-10-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3260371D.7ED@gte.net>`
- **References:** `<3260371D.7ED@gte.net>`

```

It depends on how you store the data in the array in the first place.
The example is a bit unclear about that.
Company is numeric, region-division is pic x comp, thus presumably also
numeric, region is pic x(3), but you refer to region 01 and 12 data, so
maybe region is also numeric. If so, the array is already sorted.
To write out it do something like this:
perform write-company
varying company-nbr from 1 by 1
until company-nbr > company-count
.

write-company.
perform write-division
varying division-nbr from 1 by 1
until division-nbr > division-count
.

write-division.
perform write-region
varying region-nbr from 1 by 1
until region-nbr > region-count
.

write-region.
display array-stuff (company-nbr, division-nbr, region-nbr)
```

##### ↳ ↳ Re: Sorting a three dimensional array

- **From:** "r.j.grealish" <ua-author-6590566@usenetarchives.gap>
- **Date:** 1996-10-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c389ab04af-p2@usenetarchives.gap>`
- **References:** `<3260371D.7ED@gte.net> <gap-c389ab04af-p2@usenetarchives.gap>`

```

In article <53qs6f$38··.@new··m.net>, lsv··.@i··.net says:

Accepting the assumptions below, the code could be made clearer using
in-line PERFORMS:

perform varying company-nbr from 1 by 1
until company-nbr > company-count
perform varying division-nbr from 1 by 1
until division-nbr > division-count
perform varying region-nbr from 1 by 1
until region-nbr > region-count
display array-stuff (company-nbr, division-nbr, region-nbr)
end-perform
end-perform
end-perform .

› 
› It depends on how you store the data in the array in the first place.
…[4 more quoted lines elided]…
› To write out it do something like this:


---------- out-of-line performs snipped -----------
```

###### ↳ ↳ ↳ Re: Sorting a three dimensional array

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c389ab04af-p3@usenetarchives.gap>`
- **References:** `<3260371D.7ED@gte.net> <gap-c389ab04af-p2@usenetarchives.gap> <gap-c389ab04af-p3@usenetarchives.gap>`

```

It is certainly shorter, but not necessarily CLEARER.
Apart from the fact that not all compilers accept inline performs,
the REAL code for printing the array stuff is likely to be much
more than the one line in my example; this leads to an inline
perform that may sprawl over several pages, something clearly to
avoid.
Splitting the performs into three paragraphs that each does their
thing (write-company, write-division, write-region) makes the
structure crystal clear (especially since the paragraph names say
what they do). Having separate paragrpahs also makes it easier
to reuse some of these in other parts of the program.

Inline performs should only be used for short pieces of code
(a few lines). Anybody out there that disagrees with this,
please step forward.
```

###### ↳ ↳ ↳ Re: Sorting a three dimensional array

- **From:** "jrh..." <ua-author-3336494@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c389ab04af-p3@usenetarchives.gap>`
- **References:** `<3260371D.7ED@gte.net> <gap-c389ab04af-p2@usenetarchives.gap> <gap-c389ab04af-p3@usenetarchives.gap>`

```

In <53tq8i$2.··.@bs3··c.uk>, R.J.Grealish (Rod Grealish) writes:
› In article <53qs6f$38··.@new··m.net>, lsv··.@i··.net says:
› 
…[12 more quoted lines elided]…
› end-perform  .

or:

perform varying company-nbr from 1 by 1
until company-nbr > company-count
after division-nbr from 1 by 1
until division-nbr > division-count
after region-nbr from 1 by 1
until region-nbr > region-count

display array-stuff (company-nbr, division-nbr,
region-nbr)

end-perform
```

#### ↳ Re: Sorting a three dimensional array

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-10-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3260371D.7ED@gte.net>`
- **References:** `<3260371D.7ED@gte.net>`

```

Jim Farland wrote:

› Hello;
 
› I am developing a report for school and we must use a three dimensional
› array to colloct information for a Company by Region-Division by Region
…[4 more quoted lines elided]…
› dimensional array?    The array appears as follows:
 
› LEVEL 2 ACCUMLATORS TABLE
›       01  WV-VARIABLES.
…[20 more quoted lines elided]…
› COMP.            
 
› Any help is appreciated.
 
› Thank you in advance.
lucky for you paper is linear and you report is also.

2 sorts and 2 reports are alot easier as your specs do not indicate
any relationship accross these 'dimensions'
1st report: company region
2nd : division region.
build your logical records properly for the sort and noooooo problem.

jr


and stir with a Runcible spoon...
```

#### ↳ Re: Sorting a three dimensional array

- **From:** "jeff..." <ua-author-34052@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c389ab04af-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3260371D.7ED@gte.net>`
- **References:** `<3260371D.7ED@gte.net>`

```

In article <326··.@g··.net>, Jim Farland writes:

› am developing a report for school and we must use a three dimensional
› array to colloct information for a Company by Region-Division by Region
…[4 more quoted lines elided]…
› dimensional array?    The array appears as follows:

You could use the region as the subscript of dimension in question. Then
your data would already be in the order you desire. In your example you
refer to region 1 and 12, which indicates that your region is numeric,
which makes it a possible candidate for subscripting. So basically store
region 12's data in element 12 of that dimension, region 1's data in
element 1, etc...

Also, I've never seen those PIC X COMP fields before. It that something
new?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
