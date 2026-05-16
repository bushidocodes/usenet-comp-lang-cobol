[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT IBM vers. Siemens-Fujitsu Environment

_9 messages · 7 participants · 2002-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### SORT IBM vers. Siemens-Fujitsu Environment

- **From:** "Manfred L. Stark" <manfred.l.stark@t-online.de>
- **Date:** 2002-12-07T15:27:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<assvsk$oas$07$1@news.t-online.com>`

```
Hallo,

we have just encountered the fact that within the Cobol85 Siemens-Fujitsu
Compiler an internal Sort exists. That SORT sorts internal tables (...
occures ...).
But on the other Hand (the OS/390 site) we have only "external" SORTs.
Because i'ld like to use 1 Programm for both sides, it thought about
programming a 'new', simple sort-algorithmus (like bubble or quicksort)
running on both machines. But i doubt, thats a smart way.

Does someone have a hint, a better way, a comment ?

Thank you
Manfred
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2002-12-07T17:08:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF22D14.7070703@nycap.rr.com>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
IBM COBOL has internal sorts.  Perhaps your IBM OS/390 site 
has a management decision not to allow internal sorts.  Some 
places like all sorts to be a preceeding JCL step, and the 
following program only concerning itself with its designated 
function.  Check management first.

Manfred L. Stark wrote:
> Hallo,
> 
…[13 more quoted lines elided]…
>
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-07T11:28:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212071128.aab7400@posting.google.com>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
"Manfred L. Stark" <manfred.l.stark@t-online.de> wrote

> Because i'ld like to use 1 Programm for both sides, it thought about
> programming a 'new', simple sort-algorithmus (like bubble or quicksort)
> running on both machines. But i doubt, thats a smart way.

For small tables (couple of hundred entries) a bubble sort is
effective and can be coded with 100% reliability in less than a dozen
lines.
For larger tables a quicksort is required for performance reasons. I
have used a copybook for the quicksort code (plus one for internal
variables) and ensured that specific field names were used on the
table (or a redefinition using exact size) and for limits etc so that
the compiled code accessed the table directly.

These are likely to outperform mechanisms such as writing the table to
disk to do a sort or even having a called routine and passing offset
and sizing information.
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-12-07T22:07:32+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ni4vu0t7t919se6rn057mf4c6vqce1thf@4ax.com>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
On Sat, 7 Dec 2002 15:27:20 +0100 "Manfred L. Stark"
<manfred.l.stark@t-online.de> wrote:

:>we have just encountered the fact that within the Cobol85 Siemens-Fujitsu
:>Compiler an internal Sort exists. That SORT sorts internal tables (...
:>occures ...).
:>But on the other Hand (the OS/390 site) we have only "external" SORTs.
:>Because i'ld like to use 1 Programm for both sides, it thought about
:>programming a 'new', simple sort-algorithmus (like bubble or quicksort)
:>running on both machines. But i doubt, thats a smart way.

You can use the "external" sort on a table. 

Simply use the input procedure and output procedure instead of using/giving.
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2002-12-08T00:05:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mKscIAhzo89EwJ2@ld50macca.demon.co.uk>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
On the IBM mainframe environments that I have worked in the sort package
(usually CA-SORT or DFSORT or SYNCSORT) can perform both internal and
external sorts.

Sorry if this seems to be lecturing but: internal sorts will only be
externally evident by references to sort work files. A cobol source
program will have the SD (rather than FD) to which records are written
(output to the internal sort) and from which they are read (input from
the internal sort). 

You almost certainly have the internal sort capability on your system,
it is quite likely that the previous departmental standards have
insisted on external sorts rather than the internal sort being used.

In article <assvsk$oas$07$1@news.t-online.com>, Manfred L. Stark
<manfred.l.stark@t-online.de> writes
>Hallo,
>
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-12-09T06:47:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0212090647.e6e9a9e@posting.google.com>`
- **References:** `<assvsk$oas$07$1@news.t-online.com> <9mKscIAhzo89EwJ2@ld50macca.demon.co.uk>`

```
Alistair,

I think you misunderstood the original post.  This user is talking
about table vs file sorts.  The Fujitsu-Siemens compiler is fairly far
along in implementing the 2002 standard - thus supports the table
sort.  IBM is not so far along.  Were I this user, and I had a
specific interest or more importantly, now a compatibility issue - I
would pressure my compiler vendor (IBM in this case) to implement this
feature of the standard -- or better yet, for compatibility sake, the
entire standard.


Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message news:<9mKscIAhzo89EwJ2@ld50macca.demon.co.uk>...
> On the IBM mainframe environments that I have worked in the sort package
> (usually CA-SORT or DFSORT or SYNCSORT) can perform both internal and
…[29 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-12-09T17:19:56+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q2d9vu49d2al4jefprbcpg7cpjrtlkshce@4ax.com>`
- **References:** `<assvsk$oas$07$1@news.t-online.com> <9mKscIAhzo89EwJ2@ld50macca.demon.co.uk> <bfdfc3e8.0212090647.e6e9a9e@posting.google.com>`

```
On 9 Dec 2002 06:47:59 -0800 thaneh@softwaresimple.com (Thane Hubbell) wrote:

:>I think you misunderstood the original post.  This user is talking
:>about table vs file sorts.  The Fujitsu-Siemens compiler is fairly far
:>along in implementing the 2002 standard - thus supports the table
:>sort.  IBM is not so far along.  Were I this user, and I had a
:>specific interest or more importantly, now a compatibility issue - I
:>would pressure my compiler vendor (IBM in this case) to implement this
:>feature of the standard -- or better yet, for compatibility sake, the
:>entire standard.

While a SORT TABLE verb might be nice, it is easily implemented by using a
"file sort" with input and output procedures.

:>Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message news:<9mKscIAhzo89EwJ2@ld50macca.demon.co.uk>...
:>> On the IBM mainframe environments that I have worked in the sort package
:>> (usually CA-SORT or DFSORT or SYNCSORT) can perform both internal and
:>> external sorts.
:>> 
:>> Sorry if this seems to be lecturing but: internal sorts will only be
:>> externally evident by references to sort work files. A cobol source
:>> program will have the SD (rather than FD) to which records are written
:>> (output to the internal sort) and from which they are read (input from
:>> the internal sort). 
:>> 
:>> You almost certainly have the internal sort capability on your system,
:>> it is quite likely that the previous departmental standards have
:>> insisted on external sorts rather than the internal sort being used.
:>> 
:>> In article <assvsk$oas$07$1@news.t-online.com>, Manfred L. Stark
:>> <manfred.l.stark@t-online.de> writes
:>> >Hallo,
:>> >
:>> >we have just encountered the fact that within the Cobol85 Siemens-Fujitsu
:>> >Compiler an internal Sort exists. That SORT sorts internal tables (...
:>> >occures ...).
:>> >But on the other Hand (the OS/390 site) we have only "external" SORTs.
:>> >Because i'ld like to use 1 Programm for both sides, it thought about
:>> >programming a 'new', simple sort-algorithmus (like bubble or quicksort)
:>> >running on both machines. But i doubt, thats a smart way.
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-09T15:49:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at2e2r$4cr$1@peabody.colorado.edu>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
I know of a shop that didn't buy a sort utility.  It sorted by copying files to
a keyed file and back again.  You might want to benchmark this technique if it
solved your political climate.
```

#### ↳ Re: SORT IBM vers. Siemens-Fujitsu Environment

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-09T15:52:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at2e87$4jp$1@peabody.colorado.edu>`
- **References:** `<assvsk$oas$07$1@news.t-online.com>`

```
I have written comb sorts when I needed to sort a table within a CoBOL program.
It's not hard, and it works fast.

Look at http://world.std.com/~jdveale/combsort.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
