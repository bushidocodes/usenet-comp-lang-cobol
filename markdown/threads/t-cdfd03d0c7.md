[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Search all

_5 messages · 4 participants · 1999-02_

---

### Search all

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C34EEA.CAE3A2F0@NOSPAMhome.com>`

```
When I create a binary table of unknown size which I want to search a
bunch of times in a program, I fill it with high values (or something to
make it sort right) before I populate it.  This works, but I am
wondering if there's a more efficient way.
```

#### ↳ Re: Search all

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79vjnp$13o@netnews1.apci.com>`
- **References:** `<36C34EEA.CAE3A2F0@NOSPAMhome.com>`

```
The purpose of filling the table with high-values is so that a "SEARCH ALL"
will find the entire contents of the table ascending.  However, one can
instruct the SEARCH verb to only search that portion of the table which you
have populated by adding a OCCURS ... DEPENDING ON ... clause to the table
definition.  Note however, that since a SEARCH ALL is binary a 1000 entry
table only takes 10 compares to find any entry.  If you fill only half (500)
of the table, then DEPENDING ON clause will only reduce the number of
compares to 9, so there is not as much savings as you might think.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer

Howard Brazee wrote in message <36C34EEA.CAE3A2F0@NOSPAMhome.com>...
>When I create a binary table of unknown size which I want to search a
>bunch of times in a program, I fill it with high values (or something to
>make it sort right) before I populate it.  This works, but I am
>wondering if there's a more efficient way.
```

#### ↳ Re: Search all

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-02-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990212062500.03163.00000518@ng18.aol.com>`
- **References:** `<36C34EEA.CAE3A2F0@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com>
On Thu, 11 Feb 1999 14:43:06 -0700
posted 

<< When I create a binary table of unknown size which I want to search a
bunch of times in a program, I fill it with high values (or something to
make it sort right) before I populate it.  This works, but I am
wondering if there's a more efficient way.
>>

In a few cases there is a special trick available.

If your search tokens are comming thru in random order, then this does not
apply. But if you can sort the input on the search argument, then the following
nifty trick applies.

Assume the table is in ascending order. Then sort the input in descending
order.  Use an ODO as suggested by other excellent posters.  

Initially set the table-max value to the actual last valid entry. As you get
hits, process them as you like but also add a trickster adjustment to the
ongoing ODO table-max  - set it to the cell you just hit. By definition no
later record can be in a higher position on the table.

Upon each hit you establish a little less work for the following  searches. You
cannot adjust the ODO object upon misses, but all misses and all hits benefit
from any preceding successful adjustments.

A previous poster concisely explained why you will have a hard time squeezing
much out of a binary search. But you did say that you want to search 'a bunch
of times'.

The actual benefit of the ascending-descending-adjustment trick will depend
upon your data distributions.  In the manner explained, it would be best if you
had few tokens with high keys, and many tokens with low keys.

With this in mind optimizing data conditions can be designed into the system
... but surely this begins to assume much more flexibility then you have yet
indicated.

Keep in mind that the ascending table with descending data sequence, could as
easily be descending table with ascending data sequence. These two just need to
be converse The ODO object, table-max, would decrement in either case.

(As an aside, use of the ODO technique can in cases of a very large table
actually reduce paging. A previous poster rightly suggested that cutting a
table in half only reduces the max iteration count by one.  But the portion of
the table left out constitutes, in some cases, much virtual memory that can be
placed safely out of the way by the OS.  Conversely, always hitting that top
high-values record will demand that page needlessly. ((but not necessarily all
pages from the midpoint to the max point)). ) (((This is all about locality of
reference))).


Further, again assuming a situation in which you can sort the input upon the
search key.  In some applications the search key may be repeated, and such
duplicates or runs might occur many times. When the current key is equal to the
previous key, you can just use the previous results - saving the CPU time to
enter into the search logic, all for the cost of a mere IF statement (and the
overhead of preseving enough from the previous matching hit). 

But note that that IF statement costs a little each time, not just when it
finds a duplicate.  So, here too, data occurence patterns will motivate your
judgement.

One other note. If for any reason you do use an ODO object as a table-max
mechanism to reduce the search, then you really do not need to fill the rest of
the table with high-values.

You are not likely to find a person who likes to see data elements initialized
more than I do. But on large tables there is an issue.  

For in some applications that would search a table a bunch of times, there is
actually a pattern of loading the table quite a few times for different phases.
In such cases the time taken to move the high-values is significant. This is
particularly true in cases where many phases have relatively few real records
and therefore many dummy high-value records.

All of that having been said, still in truth almost all COBOL applications are
I/O bound. It is rare, though possible, that CPU time is your critical factor. 
Storage media spins so slowly compared to the speed of modern chips that you
will have to be a real genius or else be dealing with one very gigantic number
of searches in order to get a return on the effort you have sketched.

Hope that is close enough to your actual situation to be useful.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Search all

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c39333.685146352@news1.ibm.net>`
- **References:** `<36C34EEA.CAE3A2F0@NOSPAMhome.com>`

```
On Thu, 11 Feb 1999 14:43:06 -0700, Howard Brazee
<brazee@NOSPAMhome.com> wrote:

>When I create a binary table of unknown size which I want to search a
>bunch of times in a program, I fill it with high values (or something to
>make it sort right) before I populate it.  This works, but I am
>wondering if there's a more efficient way.

I agree with Allen - make it a variable length table and skip the HV.
```

##### ↳ ↳ Re: Search all

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C83685.20B452DF@NOSPAMhome.com>`
- **References:** `<36C34EEA.CAE3A2F0@NOSPAMhome.com> <36c39333.685146352@news1.ibm.net>`

```
Thane Hubbell wrote:

> >When I create a binary table of unknown size which I want to search a
> >bunch of times in a program, I fill it with high values (or something to
…[3 more quoted lines elided]…
> I agree with Allen - make it a variable length table and skip the HV.

Would you do it this way if the table was only searched a couple of
times?  I am wondering which has the most overhead, variable length
tables or the possibility of an extra search step.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
