[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Rocks

_8 messages · 7 participants · 1998-12_

---

### COBOL Rocks

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ILdltJrB7yj8@Dwight_Miller.iix.com>`

```
I'm sitting here waiting on a big job, flipping through InfoWorld.  An
ad catches my eye - COBOL Rocks.  It's a nice, modern, slick, very 
cool ad from MicroFocus.  They refer to to a website where you can get
an eval version of NetExpress.

This will probably screw up their advertising, but here's the URL:

http://www.microfocus.com/cobolrocks/

No where does it say where I can get one of those cool "COBOL Rocks" 
T-Shirts.  I want one.


-------------------------
Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: COBOL Rocks

- **From:** dbryant@netcom.com (David K. Bryant)
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbryantF3oE1J.Myr@netcom.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-ILdltJrB7yj8@Dwight_Miller.iix.com>`

```
redsky@ibm.net (Thane Hubbell) writes:

>I'm sitting here waiting on a big job, flipping through InfoWorld.  An
>ad catches my eye - COBOL Rocks.

Speaking of...

  I've been writing for a Wang VS oriented e-zine  (www.hotvs.com)
  and lately I've been writing about "application tuning".  This
  means to take a look at your programming style and how it can
  be improved.  In the current issue I show how to, without getting
  real exotic, chop 63% out of a simple batch program.  In following
  issues I'm going to take that to 87.5%.  Just by using some simple
  techniques... no ALTERs or other weird stuff.

  It's generic (non-Wang) enough that you might all benefit.

  You'd be surprized how lame most of the programmers I meet are.
  When I mentioned the potential savings  one said "But then I'd
  have to think too much."  Seriously.

  Anyway it's HotVS  at  www.hotvs.com


>No where does it say where I can get one of those cool "COBOL Rocks" 
>T-Shirts.  I want one.

A custom T-shirt shop maybe?
```

##### ↳ ↳ Re: COBOL Rocks

- **From:** Clifton Ivy <clif@purdue.edu>
- **Date:** 1998-12-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36704C28.585A1B9A@purdue.edu>`
- **References:** `<Jl0PnHJ5PvPd-pn2-ILdltJrB7yj8@Dwight_Miller.iix.com> <dbryantF3oE1J.Myr@netcom.com>`

```
Maybe you already have this is mind, but you can speed up your table
search if you ensure the entries are sorted on ZIP code.

The simplest way is to stop scanning the table when TBL-ZIP (SUBSCRIPT)
> EMP-ZIP.

At this point you are done; you either have found a match, in which case
you have done the "MOVE TBL-NAME (SUBSCRIPT) TO CITY-NAME" statement, or
you aren't going to find a match.

A bigger speed-up would be to do a binary search.

At my IBM big-iron shop, I would use the "SEARCH" verb to do this.  Does
WANG COBOL have that capability?

When the table is defined, you have to define the key to the table (the
field on which the table entries are sorted).

This changes the table definition to:

01  CITY-TABLE.
    05  TABLE-ROWS    OCCURS 250 TIMES
        ASCENDING KEY IS TBL-ZIP
        INDEXED BY TRI.
      10  TBL-ZIP      PIC X(05).
      10  TBL-NAME     PIC X(25).

The "indexed by" is necessary to use the SEARCH verb.

This is ***MUCH*** better than the "PERFORM... nnn times" approach,
because sooner or later the number of entries in the table will change
-- and you will have to find all of the times you coded that "nnn"
throughout the program, and which of those need to change. You don't
have to code the "nnn" with the SEARCH verb, COBOL takes care of it for
you.

The SEARCH statement would be like:

SEARCH ALL TABLE-ROWS
    AT END
        MOVE 'NOT FOUND' TO CITY-NAME
    WHEN EMP-ZIP = TBL-ZIP (TRI)
        MOVE TBL-NAME (TRI) TO CITY-NAME.

The "ALL" above tells COBOL to do a binary search of the table.  You
know: 

try the middle entry of the table; 
  if the value you are looking for is found there, do the "WHEN"; 
  if the value you are looking for is less than the table value, go
half-way down the table and try again;
  if the value you are looking for is greater than the table value, go
half-way up the table and try again;
Keep at this, splitting the remainder of the table in half until you
find a value, or you have run out of "halves" to split.

At least, that is a rude-and-crude explanation of the search.

You should be able to search the table with an average of 9 (8?) "looks"
into the table, instead of the 250 you have been doing.

Have fun with it!


David K. Bryant wrote:

> Speaking of...
> 
…[12 more quoted lines elided]…
>   have to think too much."  Seriously.
snip...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
They're just my opinions...
Clifton Ivy, Mgmt Info, Purdue University
clif@purdue.edu
```

###### ↳ ↳ ↳ Re: COBOL Rocks

- **From:** mrbiueskyz@aol.comatose (MrBIueSkyz)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981211015012.18814.00000710@ng29.aol.com>`
- **References:** `<36704C28.585A1B9A@purdue.edu>`

```
Search all is definitely the way to go when processing
large tables and/or large input files. Remember that the
table entries must be in ascending/descending key
sequence with no duplicates; otherwise a given value
might not be found.

An example of the power of binary searches: Last year
I was a member of the team converting claims records
of another insurance company that our company had
bought. People were complaining about a particular pgm
that was running for four hours. Two tables with several
thousand entries were being searched with perform
varying statements. This processing was being performed
on an input file with hundreds of thousands of rcds. I
added a couple of upstream syncsorts to sort the table
entries into ascending sequence, and then loaded them
into internal tables with occurs depending on & ascending
key clauses, and replaced the perform varying statements
with search alls. Results: clock time & cpu usage were
reduced by 90%. In fairness to the original programmer,
she's a SAS person, doesn't do much COBOL.
```

###### ↳ ↳ ↳ Re: COBOL Rocks

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74qu8h$1cb@sjx-ixn6.ix.netcom.com>`
- **References:** `<36704C28.585A1B9A@purdue.edu> <19981211015012.18814.00000710@ng29.aol.com>`

```

MrBIueSkyz wrote in message <19981211015012.18814.00000710@ng29.aol.com>...
>Search all is definitely the way to go when processing
>large tables and/or large input files. Remember that the
…[3 more quoted lines elided]…
>
  <snip>

Some implementors have already done it and the draft of the next Standard
has it - but SEARCH ALL is really easy with "TABLE SORTS".  This feature
lets you sort the elements of a table using the same old SORT verb that you
already know and love.  This means you don't have to do your own external or
internal sort, but can (in a single statement) sort your table and then use
SEARCH ALL safely (it even defaults - but can be overridden - to sort on the
key fields defined for your SEARCHs.)
```

###### ↳ ↳ ↳ Re: COBOL Rocks

_(reply depth: 4)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367135D8.85A37E53@home.com>`
- **References:** `<36704C28.585A1B9A@purdue.edu> <19981211015012.18814.00000710@ng29.aol.com>`

```
MrBIueSkyz wrote:
> 
> Search all is definitely the way to go when processing
…[3 more quoted lines elided]…
> might not be found.

And if that's not possible, SEARCH is usually better than doing
PERFORMS.  But if the table is real small sometimes it is faster to look
at each element individually.

I agree with you that sorting tables ahead of time can offer tremendous
efficiencies.  Also, sorting files can allow merge logic which can also
be very efficient.  It seems that lots of programmers, some even fairly
senior, don't think about merge logic enough.
```

###### ↳ ↳ ↳ Re: COBOL Rocks

_(reply depth: 4)_

- **From:** WOB@my-dejanews.com
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74smme$rp7$1@nnrp1.dejanews.com>`
- **References:** `<36704C28.585A1B9A@purdue.edu> <19981211015012.18814.00000710@ng29.aol.com>`

```
In article <19981211015012.18814.00000710@ng29.aol.com>,
  mrbiueskyz@aol.comatose (MrBIueSkyz) wrote:
> Search all is definitely the way to go when processing
> large tables and/or large input files. Remember that the
…[19 more quoted lines elided]…
>

Skyz,

A little 'trick' I found was with sorted Ascending Tables having duplicates.
I had a CICS Table (Static Assembler Program) with 3000 sorted entries.
Beginning with entry 2701, the next three hundred entries were High-Values.
My DSECT was an occurs 1 to 3000 depending on high-bound, with the first
high-value entry (nbr 2701) being my high-bound. Using this method, my SEARCH
ALL always worked just fine.

Cheers,

WOB :-)

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: COBOL Rocks

- **From:** dbryant@netcom.com (David K. Bryant)
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbryantF3u7z7.CKo@netcom.com>`
- **References:** `<Jl0PyantF3oE1J.Myr@netcom.com> <36704C28.585A1B9A@purdue.edu>`

```
Clifton Ivy <clif@purdue.edu> writes:

>Maybe you already have this is mind, but you can speed up your table
>search if you ensure the entries are sorted on ZIP code.

All of Clif's suggestions are already scheduled to come 
out in the next two installments of this series.  The material
is presented in digestible increments which take the reader from
the braindead -- I mean -- thoughtless way of doing lookup code
through runtime reductions of 34%, 63%, 68%, 79%, and finally 86.5%.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
