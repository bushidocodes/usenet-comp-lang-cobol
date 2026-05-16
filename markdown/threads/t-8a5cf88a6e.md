[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tables ????

_19 messages · 12 participants · 1999-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Tables ????

- **From:** "Klaas Berend" <kbpoel@concepts.nl>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<7vmg39$bf7$1@news.concepts.nl>`

```
This is my problem.
I have a file called result1.seq In this file you can find the following
information.
Levnumber        ArtId                        Numbersold
1                            01                            100
1                            02                            200
2                            03                            150
2                            04                            300
3                            05                            100
3                            06                             50

Now I have to count the numbersold by each Levnumber.
So like this Levnumber 1               Totalsold 300
The results are output for a new file.
How can I do this???
```

#### ↳ Re: Tables ????

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<381F5F1C.D66DEDE2@home.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl>`

```


Klaas Berend wrote:
> 
> This is my problem.
…[13 more quoted lines elided]…
> How can I do this???

Klaas,

You are going to have to show some source, (that you have done some of
your homework), before you are likely to get any help on this one.

verstaant u ?

Jimmy, Calgary AB
```

#### ↳ Re: Tables ????

- **From:** "George E. Zielinski" <georgezielinski@retired.airforce.net>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<37397D20F96C7408.68179DA6CF4B6B8E.4372853533C3AEB5@lp.airnews.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl>`

```
This looks like a homework assignment, so I will attempt to give you a
pointer in the right direction rather than work it out for you.

First ensure that your file is in order by Levnumber, then read each record.
Accumulate the totals. Only produce an output when the Levnumber changes.
And don't forget to reset your totals to zero after each output.
```

##### ↳ ↳ Re: Tables ????

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<381EFB35.CE150302@NOSPAMhome.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <37397D20F96C7408.68179DA6CF4B6B8E.4372853533C3AEB5@lp.airnews.net>`

```
Now that's how such a question should be answered!  IMHO

George E. Zielinski wrote:
> 
> This looks like a homework assignment, so I will attempt to give you a
…[28 more quoted lines elided]…
> >
```

#### ↳ Re: Tables ????

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991102093219.27555.00000197@ngol03.aol.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl>`

```
In article <7vmg39$bf7$1@news.concepts.nl>, "Klaas Berend" <kbpoel@concepts.nl>
writes:

>This is my problem.
>I have a file called result1.seq In this file you can find the following
…[13 more quoted lines elided]…
>

This doesn't really look like a 'table' process.  As long as the input
file is ALWAYS ordered by LevNumber, you should be able to process
sequentially do your accumulations and on change of LevNumber
print your results.
```

##### ↳ ↳ Re: Tables ????

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31C503F3118A348D.EBBEF5CB76FD493A.2CFA75C549047AC7@lp.airnews.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <19991102093219.27555.00000197@ngol03.aol.com>`

```
On 02 Nov 1999 14:32:19 GMT, sff5ky@aol.comxxx123 (Sff5ky) enlightened
us:

>In article <7vmg39$bf7$1@news.concepts.nl>, "Klaas Berend" <kbpoel@concepts.nl>
>writes:
…[21 more quoted lines elided]…
>print your results.

Another hint.  Control Break logic.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Whenever I find myself in a difficult situation, I ask myself "What
Would Jesus Do?"  The mental image of my opposition being cast into
pits of hellfire for all eternity *is* comforting, but probably not
what the inventors of the phrase had in mind.


Remove nospam to email me.

 Steve
```

##### ↳ ↳ Re: Tables ????

- **From:** "Paul M. Dorfman" <sashole@earthlink.net>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38251EE2.F0A82266@earthlink.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <19991102093219.27555.00000197@ngol03.aol.com>`

```
Sff5ky wrote:
> 
> >This is my problem.
…[12 more quoted lines elided]…
> >The results are output for a new file.

> This doesn't really look like a 'table' process.  As long as the input
> file is ALWAYS ordered by LevNumber, you should be able to process
> sequentially do your accumulations and on change of LevNumber
> print your results.

Not necessarily; it depends on how one approaches the problem and the nature
of the data. If 'levnumber' is represented by positive integers falling in a
limited range, say, 1-1000, there exists a most straightforward sortless
solution not obvious only to minds locked in the 'control break' logic:

1) Create a table with 1000 buckets and initialize their contents to 0.
2) Read the file and for each record, add 'numbersold' to the bucket whose
subscript is the same as 'levnumber'.
3) Loop over the table. If a bucket is empty, skip it; otherwise, write its
number to a file as 'levnumber' and its contents - as 'totalsold'.

One would be surprised how many real-world problems can be solved like that
without ever resorting to sorting (no pun intended). If the range of the
keys is too wide and hence a table capable of accommodating the entire
universe of key values cannot be allocated, one can organize the table as a
hash table instead of the key-indexed table described above. In this case,
the keys need not be integers, they can be anything, and that will always
work faster than anything else will, if the total number of keys in the file
times key length fits into the memory. With contemporary memories it usually
means millions of distinct keys.

That is, if one thinks in terms of sorting, i.e. rearranging data in such a
way that alike keys are brought together as closely as possible (which is
one of the the hardest and most resource-consuming computer tasks), this
does not look like tables are relevant to the problem; but if one thinks in
terms of distribution, i.e. placing keys as separately from each other as
possible, it looks exactly like a 'table' process.

On the same note, when it comes to searching tables, the common mindset
seems to be locked in SEARCH ALL routine just because COBOL provides it free
of charge. More times than I care to recall, I've heard the nonsense (of
course, pronounced in the most authoritative fashion) about binary search
being the fastest and most efficient among existing lookup algorithms, while
in reality, the same COBOL table organized as a key-indexed or hash table
(depending on the keys' nature) searches an order of magnitude faster, to
say nothing of the fact that, to boot, the direct-addressing approaches
require no sorting or unduplication of any kind.     

Kind regards,
===================
Paul M. Dorfman
Jacksonville, FL                    
===================
```

###### ↳ ↳ ↳ Re: Tables ????

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8053un$tou$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <19991102093219.27555.00000197@ngol03.aol.com> <38251EE2.F0A82266@earthlink.net>`

```
In article <38251EE2.F0A82266@earthlink.net>,
  "Paul M. Dorfman" <sashole@earthlink.net> wrote:
> Sff5ky wrote:
> >
> > >This is my problem.
> > >I have a file called result1.seq In this file you can find the
following
> > >information.
> > >Levnumber        ArtId                        Numbersold
…[11 more quoted lines elided]…
> > This doesn't really look like a 'table' process.  As long as the
input
> > file is ALWAYS ordered by LevNumber, you should be able to process
> > sequentially do your accumulations and on change of LevNumber
> > print your results.
>
> Not necessarily; it depends on how one approaches the problem and the
nature
> of the data. If 'levnumber' is represented by positive integers
falling in a
> limited range, say, 1-1000, there exists a most straightforward
sortless
> solution not obvious only to minds locked in the 'control break'
logic:
>
> 1) Create a table with 1000 buckets and initialize their contents to
0.
> 2) Read the file and for each record, add 'numbersold' to the bucket
whose
> subscript is the same as 'levnumber'.
> 3) Loop over the table. If a bucket is empty, skip it; otherwise,
write its
> number to a file as 'levnumber' and its contents - as 'totalsold'.
>
> One would be surprised how many real-world problems can be solved
like that
> without ever resorting to sorting (no pun intended). If the range of
the
> keys is too wide and hence a table capable of accommodating the entire
> universe of key values cannot be allocated, one can organize the
table as a
> hash table instead of the key-indexed table described above. In this
case,
> the keys need not be integers, they can be anything, and that will
always
> work faster than anything else will, if the total number of keys in
the file
> times key length fits into the memory. With contemporary memories it
usually
> means millions of distinct keys.
>
> That is, if one thinks in terms of sorting, i.e. rearranging data in
such a
> way that alike keys are brought together as closely as possible
(which is
> one of the the hardest and most resource-consuming computer tasks),
this
> does not look like tables are relevant to the problem; but if one
thinks in
> terms of distribution, i.e. placing keys as separately from each
other as
> possible, it looks exactly like a 'table' process.
>
> On the same note, when it comes to searching tables, the common
mindset
> seems to be locked in SEARCH ALL routine just because COBOL provides
it free
> of charge. More times than I care to recall, I've heard the nonsense
(of
> course, pronounced in the most authoritative fashion) about binary
search
> being the fastest and most efficient among existing lookup
algorithms, while
> in reality, the same COBOL table organized as a key-indexed or hash
table
> (depending on the keys' nature) searches an order of magnitude
faster, to
> say nothing of the fact that, to boot, the direct-addressing
approaches
> require no sorting or unduplication of any kind.
>
…[6 more quoted lines elided]…
>
If you know approximately how many different numbers there are, rather
than the range, you can make a table which is much smaller than the
whole range.
If the number an vary considerably from execution to exectution, you
might want to use a variable length table.
Also, on an IBM mainframe, a binary search (SEARCH ALL) is more
efficient only if there are more than approximately 75 entries in the
table.  Less than (approximately) 75 entries, the sequential search is
more efficient.

Stephen J Spiro
President, Wizard Systems
Member, J4 COBOL Committee


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 4)_

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38262B8E.F75DEF67@nbnet.nb.ca>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <19991102093219.27555.00000197@ngol03.aol.com> <38251EE2.F0A82266@earthlink.net> <8053un$tou$1@nnrp1.deja.com>`

```
While my reading of the COBOL SEARCH ALL code back in the mid to late
1970's was that the code was poor, is it still that bad on COBOL for MVS
and VM and later?  If I get energetic, I may look at the code and see
how bad it is on the setup.  As I recall at the time the break even
point between our assembler serial sub-routine and our binary search
assembler sub-routine was 16 entries.  These routines were originally
written before the SEARCH verb was available.

Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca

stephen_j_spiro@my-deja.com wrote:
>
>> snip
…[10 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 5)_

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80726e$9k8$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <19991102093219.27555.00000197@ngol03.aol.com> <38251EE2.F0A82266@earthlink.net> <8053un$tou$1@nnrp1.deja.com> <38262B8E.F75DEF67@nbnet.nb.ca>`

```
Clark, 16 table entries is a maximum of 4 lookups in a binary search.
There is just more overhead in the instruction.. 75 was the  number I
heard a long time ago, and I don't imagine they've changed the
algorithm.  I'd be interested in hesaring fromn anyone at IBM who knows
for sure.

Stephen J Spiro
President, Wizard Systems
Member, J4 COBOL Committee


In article <38262B8E.F75DEF67@nbnet.nb.ca>,
  Clark Morris <morrisc@nbnet.nb.ca> wrote:
> While my reading of the COBOL SEARCH ALL code back in the mid to late
> 1970's was that the code was poor, is it still that bad on COBOL for
MVS
> and VM and later?  If I get energetic, I may look at the code and see
> how bad it is on the setup.  As I recall at the time the break even
…[10 more quoted lines elided]…
> > efficient only if there are more than approximately 75 entries in
the
> > table.  Less than (approximately) 75 entries, the sequential search
is
> > more efficient.
> >
> > Stephen J Spiro
> > President, Wizard Systems
> > Member, J4 COBOL Committee


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Tables ????

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<802scm$f68$1@nntp1.atl.mindspring.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl>`

```
Try (Sync)SORTSUM instead of COBOL.

Something like
SORT FIELDS=(1,1,ZD,A)
SUM FIELDS=(4,3,ZD)
OUTREC=(1,1,       Levnumber
                     4,3)      Numbersold


Klaas Berend <kbpoel@concepts.nl> wrote in message
news:7vmg39$bf7$1@news.concepts.nl...
> This is my problem.
> I have a file called result1.seq In this file you can find the following
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Tables ????

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<8072ef$9nc$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net>`

```
An excellent BUSINESS solution, but I'm sure his teacher will not give
him credit unless it is COBOL!

Stephen J Spiro



In article <802scm$f68$1@nntp1.atl.mindspring.net>,
  "Unbeliever" <popsider@ix.netcom.com> wrote:
> Try (Sync)SORTSUM instead of COBOL.
>
…[9 more quoted lines elided]…
> > I have a file called result1.seq In this file you can find the
following
> > information.
> > Levnumber        ArtId                        Numbersold
…[14 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<8082vf$afa$1@nntp4.atl.mindspring.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com>`

```
True - this solution originally came up when I was trying to speed up a
weekly
job, sorting & summing a 30Gig file on an 3090.

NOTE: it wasn't MY idea to do the sort & sum. I wanted to pre-process, to
trim records
and strip zero records, to cut to around 7 Gig.

<stephen_j_spiro@my-deja.com> wrote in message
news:8072ef$9nc$1@nnrp1.deja.com...
> An excellent BUSINESS solution, but I'm sure his teacher will not give
> him credit unless it is COBOL!
…[40 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 4)_

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80a877$lda$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net>`

```
In article <8082vf$afa$1@nntp4.atl.mindspring.net>,
  "Unbeliever" <popsider@ix.netcom.com> wrote:
> True - this solution originally came up when I was trying to speed up
a
> weekly
> job, sorting & summing a 30Gig file on an 3090.
>
> NOTE: it wasn't MY idea to do the sort & sum. I wanted to pre-
process, to
> trim records
> and strip zero records, to cut to around 7 Gig.
…[3 more quoted lines elided]…
> > An excellent BUSINESS solution, but I'm sure his teacher will not
give
> > him credit unless it is COBOL!
> >
> > Stephen J Spiro
I think SyncSort (and by now, maybe DFSORT) will allow you to select
and edit input records, too, to reduce the size of the sorted file.  It
has been a while since I used SyncSort like this; most shops  don't
want consultants to do it, because their own people can't maintain it.

Stephen J Spiro
President, Wizard Systems

> >
> >
…[38 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 5)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80ae76$efv$1@nntp5.atl.mindspring.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net> <80a877$lda$1@nnrp1.deja.com>`

```

<stephen_j_spiro@my-deja.com> wrote in message
news:80a877$lda$1@nnrp1.deja.com...
> In article <8082vf$afa$1@nntp4.atl.mindspring.net>,
>   "Unbeliever" <popsider@ix.netcom.com> wrote:
…[4 more quoted lines elided]…
> >
<SNIP> > >
> > > Stephen J Spiro
> I think SyncSort (and by now, maybe DFSORT) will allow you to select
…[6 more quoted lines elided]…
>
Yepp - I routinely now use INREC & OUTREC.
Last week I had to change a program to increase field sizes in a file.
I also ran synchsort on the existing GDG. I used OUTREC= along
with statements to slice & dice the input record, inserting hex LVs
before each expanded field. I love doing this with MVS utils, because
it's far safer, doesn't require as much coding time as Cobol, runs
faster, and requires no real maintenance, if you want to keep it!
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 6)_

- **From:** john_mindock@my-deja.com
- **Date:** 1999-11-10T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80c55p$19q$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net> <80a877$lda$1@nnrp1.deja.com> <80ae76$efv$1@nntp5.atl.mindspring.net>`

```

> <SNIP> > >
> > >
> Yepp - I routinely now use INREC & OUTREC.
>
For more fun:
Take a look at the options available for Y2K sorting in SYNCSORT
(DFSORT has them too). I.e., you identify a field as a Year and it will
sort '00' after '99', based on a window (which can be floating or
fixed).

John


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 7)_

- **From:** fyaeger@vnet.ibm.com
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80eodb$u51$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net> <80a877$lda$1@nnrp1.deja.com> <80ae76$efv$1@nntp5.atl.mindspring.net> <80c55p$19q$1@nnrp1.deja.com>`

```
In article <80c55p$19q$1@nnrp1.deja.com>,
  john_mindock@my-deja.com wrote:

> For more fun:
> Take a look at the options available for Y2K sorting in SYNCSORT
> (DFSORT has them too). I.e., you identify a field as a Year and it
> will sort '00' after '99', based on a window (which can be floating or
> fixed).

With DFSORT, you can identify either complete date fields (e.g.
C'yymmdd', P'dddyy', etc) or year fields (e.g. C'yy', P'yy', etc) to be
sorted, merged, compared or transformed using a century window.  For
complete details, see the following URL:

http://www.storage.ibm.com/software/sort/srtmy2p.htm

Frank Yaeger - DFSORT Team
DFSORT is on the Web at URL:
http://www.ibm.com/storage/dfsort/


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 8)_

- **From:** "Unbeliever" <popsider@ix.netcom.com>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80fv7h$30j$1@nntp6.atl.mindspring.net>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net> <80a877$lda$1@nnrp1.deja.com> <80ae76$efv$1@nntp5.atl.mindspring.net> <80c55p$19q$1@nnrp1.deja.com> <80eodb$u51$1@nnrp1.deja.com>`

```
Yepp - we've been coding CENTWIN in Syncsort at Amex for a while now,
with  a 60/40 floating window. Seems to work well too!

<fyaeger@vnet.ibm.com> wrote in message news:80eodb$u51$1@nnrp1.deja.com...
> In article <80c55p$19q$1@nnrp1.deja.com>,
>   john_mindock@my-deja.com wrote:
…[20 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Tables ????

_(reply depth: 6)_

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<80g6bb$uu$1@nnrp1.deja.com>`
- **References:** `<7vmg39$bf7$1@news.concepts.nl> <802scm$f68$1@nntp1.atl.mindspring.net> <8072ef$9nc$1@nnrp1.deja.com> <8082vf$afa$1@nntp4.atl.mindspring.net> <80a877$lda$1@nnrp1.deja.com> <80ae76$efv$1@nntp5.atl.mindspring.net>`

```
In article <80ae76$efv$1@nntp5.atl.mindspring.net>,
  "Unbeliever" <popsider@ix.netcom.com> wrote:
>
> <stephen_j_spiro@my-deja.com> wrote in message
…[3 more quoted lines elided]…
> > > True - this solution originally came up when I was trying to
speed up
> > a
> > > weekly
…[5 more quoted lines elided]…
> > and edit input records, too, to reduce the size of the sorted
file.  It
> > has been a while since I used SyncSort like this; most shops  don't
> > want consultants to do it, because their own people can't maintain
it.
> >
> > Stephen J Spiro
…[9 more quoted lines elided]…
>
PLEASE comment your code! If it DOES ever require maintenance, it's a
bitch if there are no notes...  That's the advantage of well-written
COBOL.  If there are multiple edits, under different circumstances...
sheesh!


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
