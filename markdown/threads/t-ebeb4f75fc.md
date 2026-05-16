[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# search

_13 messages · 8 participants · 2000-01_

---

### search

- **From:** "Gerda Beerda" <g.beerda@wanadoo.nl>
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85qet0$23hl$1@buty.wanadoo.nl>`

```
Hi,

I have 2 records.
PERSON (persnumber, name)
BANK (persnumber, amount)

Now is my question. How do I search all persnumbers in PERSON that are not
in BANK?

Cheers,
Gerda.
```

#### ↳ Re: search

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd638sg32042qakksam0jqql9ondgqqkj3@4ax.com>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl>`

```
On Sat, 15 Jan 2000 19:37:53 +0100 "Gerda Beerda" <g.beerda@wanadoo.nl> wrote:

:>I have 2 records.
:>PERSON (persnumber, name)
:>BANK (persnumber, amount)

:>Now is my question. How do I search all persnumbers in PERSON that are not
:>in BANK?

Assuming files are sequential:

1. Sort both files on person number
2. Read and match
```

#### ↳ Re: search

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38829D54.D3126B14@mediaone.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl>`

```
1. Choose the file having lesser number of records. Suppose it is BANK.
2. Store persnumbers from this file in a hash table (in memory).
3. Read a record from PERSON.
4. Search the table for persnumber coming from it. If it is in the table go to
3. If not, output the record and go to 3.
5. Stop.

This way, you have to sort neither file, and it will work a whole lot faster
than SEARCH ALL, even  without accounting for the time needed to sort the keys
from BANK. If you are not sure how to organize a hash table, consult Knuth,
v.3.

Paul M. Dorfman
Jacksonville, FL

Gerda Beerda wrote:

> Hi,
>
…[8 more quoted lines elided]…
> Gerda.
```

##### ↳ ↳ Re: search

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5mLg4.962$SM.12557@news4.mia>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net>`

```
Paul M. Dorfman wrote:
>1. Choose the file having lesser number of records. Suppose it is BANK.
>2. Store persnumbers from this file in a hash table (in memory).
…[8 more quoted lines elided]…
>v.3.

It's not quite that simple.  Most hashing algorithm can and do generate
synonyms, depending on the key being hashed.  You could get a false
match because you were looking for a key but found a synonym in the
hash table.  Also, setting up *good* hashing algorithms is no trivial
task, because they tend to be very data dependent.  Much better is to
sort the smaller list of keys, possibly in a memory table.  This will
work *every* time.
```

###### ↳ ↳ ↳ Re: search

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388404EC.190F174A@mediaone.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia>`

```


Judson McClendon wrote:

> >Paul M. Dorfman wrote:
> >>1. Choose the file having lesser number of records. Suppose it is BANK.
…[11 more quoted lines elided]…
> >It's not quite that simple.

But not too difficult, either. It is not as esoteric as it may seem. In fact, I
recall seeing it discussed (in all honesty, in the form not too suitable for
in-memory search) in the COBOL books by McCracken et al., and Brown.

>Most hashing algorithm can and do generate
>synonyms, depending on the key being hashed.
>You could get a false match because you were
>looking for a key but found a synonym in thehash table.

Not quite sure what you mean by "algorithm" and "synonyms". If "algorithm" means a
hash function used to map the keys to hash addresses, almost any hash function, no
matter how good, will inevitably hash some distinct keys to the same address in the
table. If by the "synonyms", you mean these collisions, a *good* collision
resolution policy intended to tell colliding keys apart unambiguously (and not the
hash function itself) is the heart of any hashing algorithm. If, looking for the
search key, you get a false match, it simply signifies that the program has a bug.

> >Also, setting up *good* hashing algorithms is no trivial
> >task, because they tend to be very data dependent.

Many algorithms we use routinely without any problems are data dependent. The
question is, what is the probability for the worst case scenario to materialize.
For instance, Quicksort's worst case is sorting in O(N*N) time, no better than that
of bubble sort; however, the chance of having the input arranged in such a way is
no greater than for all molecules in your cube to assemble spontaneously in one
half of it. The same is true for hashing. First of all, it is possible to choose a
hash function (that is what you refer to by "*good* hashing algorithm") called
"universal" that is *guaranteed* to spread the keys evenly across the table
addresses regardless of the input. However, it may be a bit expensive to compute.
For this reason in practice, a simpler and more rapidly calculated hash functions
are used. They result in more collisions, but it is usually faster to resolve the
latter than to spend more time computing a universal function. One of the simplest
approaches is to select a table with the number of nodes M somewhat (say 20%)
greater than the number of the keys N, let M be prime and not too close to a power
of 2, and compute a hash address as a key modulo M, i.e. the remainder of key/M. In
COBOL, this method has the advantage of computing, simultaneously with the
remainder, the quotient which can be used to resolve collisions by open addressing
with double hashing.

> >Much better is to
> >sort the smaller list of keys, possibly in a memory table.  This will
> >work *every* time.

A properly organized hash table will work *every* time as well.(As far as I can
tell, a COBOL compiler using a hash symbol table has no problem distinguishing
between "ws-item-1" and "ws-item-2" and who knows what else in the data division.)
The only difference is that if you have 2**10 (about 1000) keys to search, it takes
the binary search, on the average, 11 comparisons to find or reject the search key,
while it takes a 75% full hash table 1.3 comparisons to succeed and 0.75 (yes, less
than 1) comparisons to fail. If you have 2**20 keys, it will be 20 comparisons for
the binary search but still the same 1.3 and 0.75 for hash. As an icing on the
cake, loading a hash table requires no sorting, and duplicate keys (not "synonyms"
but exact duplicates) are unduplicated automatically.

Kind regards,
==================
Paul M. Dorfman
Jacksonville, FL
==================

>
> --
…[3 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 4)_

- **From:** "Gerda Beerda" <g.beerda@wanadoo.nl>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8613pp$111j$1@buty.wanadoo.nl>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net>`

```
Oh, wow. And I thought it was not that much code.

Gerda


Paul M. Dorfman <sashole@mediaone.net> schreef in berichtnieuws
388404EC.190F174A@mediaone.net...
>
>
…[3 more quoted lines elided]…
> > >>1. Choose the file having lesser number of records. Suppose it is
BANK.
> > >>2. Store persnumbers from this file in a hash table (in memory).
> > >>3. Read a record from PERSON.
> > >>4. Search the table for persnumber coming from it. If it is in the
table go to
> > >>3. If not, output the record and go to 3.
> > >>5. Stop.
> > >>
> > >>This way, you have to sort neither file, and it will work a whole lot
faster
> > >>than SEARCH ALL, even  without accounting for the time needed to sort
the keys
> > >>from BANK. If you are not sure how to organize a hash table, consult
Knuth,
> > >>v.3.
> >
> > >It's not quite that simple.
>
> But not too difficult, either. It is not as esoteric as it may seem. In
fact, I
> recall seeing it discussed (in all honesty, in the form not too suitable
for
> in-memory search) in the COBOL books by McCracken et al., and Brown.
>
…[5 more quoted lines elided]…
> Not quite sure what you mean by "algorithm" and "synonyms". If "algorithm"
means a
> hash function used to map the keys to hash addresses, almost any hash
function, no
> matter how good, will inevitably hash some distinct keys to the same
address in the
> table. If by the "synonyms", you mean these collisions, a *good* collision
> resolution policy intended to tell colliding keys apart unambiguously (and
not the
> hash function itself) is the heart of any hashing algorithm. If, looking
for the
> search key, you get a false match, it simply signifies that the program
has a bug.
>
> > >Also, setting up *good* hashing algorithms is no trivial
> > >task, because they tend to be very data dependent.
>
> Many algorithms we use routinely without any problems are data dependent.
The
> question is, what is the probability for the worst case scenario to
materialize.
> For instance, Quicksort's worst case is sorting in O(N*N) time, no better
than that
> of bubble sort; however, the chance of having the input arranged in such a
way is
> no greater than for all molecules in your cube to assemble spontaneously
in one
> half of it. The same is true for hashing. First of all, it is possible to
choose a
> hash function (that is what you refer to by "*good* hashing algorithm")
called
> "universal" that is *guaranteed* to spread the keys evenly across the
table
> addresses regardless of the input. However, it may be a bit expensive to
compute.
> For this reason in practice, a simpler and more rapidly calculated hash
functions
> are used. They result in more collisions, but it is usually faster to
resolve the
> latter than to spend more time computing a universal function. One of the
simplest
> approaches is to select a table with the number of nodes M somewhat (say
20%)
> greater than the number of the keys N, let M be prime and not too close to
a power
> of 2, and compute a hash address as a key modulo M, i.e. the remainder of
key/M. In
> COBOL, this method has the advantage of computing, simultaneously with the
> remainder, the quotient which can be used to resolve collisions by open
addressing
> with double hashing.
>
…[4 more quoted lines elided]…
> A properly organized hash table will work *every* time as well.(As far as
I can
> tell, a COBOL compiler using a hash symbol table has no problem
distinguishing
> between "ws-item-1" and "ws-item-2" and who knows what else in the data
division.)
> The only difference is that if you have 2**10 (about 1000) keys to search,
it takes
> the binary search, on the average, 11 comparisons to find or reject the
search key,
> while it takes a 75% full hash table 1.3 comparisons to succeed and 0.75
(yes, less
> than 1) comparisons to fail. If you have 2**20 keys, it will be 20
comparisons for
> the binary search but still the same 1.3 and 0.75 for hash. As an icing on
the
> cake, loading a hash table requires no sorting, and duplicate keys (not
"synonyms"
> but exact duplicates) are unduplicated automatically.
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hW_g4.3246$wk.43393@news1.mia>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net>`

```
Paul M. Dorfman wrote:
>Judson McClendon wrote:
>> >Paul M. Dorfman wrote:
…[14 more quoted lines elided]…
>But not too difficult, either. It is not as esoteric as it may seem.

Hashing isn't 'esoteric', or 'difficult', but it is 'subtle'.  Because
hashing algorithms are so sensitive to data, it is rarely, if ever,
possible to select a good hashing algorithm without some analysis,
and perhaps testing real sample data.  This is particularly true if
you want to use storage space effectively.

>In fact, I recall seeing it discussed (in all honesty, in the form
>not too suitable for in-memory search) in the COBOL books by
>McCracken et al., and Brown.

Sorry, I assumed you were making a particular mistake, but I see that
you are making a different one instead.  Hashing algorithms are very
inefficient in the use of their 'hashing address space'.  It would be
a terrible way to store a large table in computer memory, and if the
table is small, it hardly deserves a hash table, no?  Once again, the
best solution to this type of problem is either:

A. If the table is small enough to load into memory, load it into
   a memory table and sort it, perhaps by doing an insertion sort
   while loading, pass the other file and match using binary search.

B. If the table is too large for memory, then sort both files and
   do a match, or create a key index for one file, and do a match
   using the key index.

Both those solutions are simpler, and more efficient than hashing,
for this particular application. :-)

Also, you should bear in mind that many authors, and most academics,
have never designed and written applications in the 'real world', and
often have little understanding of maintaining systems over time.
Real world applications are seldom as simplistic as examples given
in books, and frequently get very messy, because of peculiar design
requirements. :-)
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 5)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388561FB.7A70714@mediaone.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia>`

```


Judson McClendon wrote:

> Paul M. Dorfman wrote:
> >Judson McClendon wrote:
…[20 more quoted lines elided]…
> and perhaps testing real sample data...

But of course, it is possible. It is done all the time. I have already tried to explain
that hashing is no more sensitive to the input than other popular algorithms like
quicksort widely used without ever questioning their worst-case behavior since it
practically never occurs. I doubt that your COBOL compiler gathers all the identifiers
in the working storage and tests their distribution as keys to decide whether to store
them in a symbol table (organized exactly in the form of a hash table) or not. It
simply does, and judging from the speed even very large programs compile, it does it
fairly efficiently.

> >In fact, I recall seeing it discussed (in all honesty, in the form
> >not too suitable for in-memory search) in the COBOL books by
…[3 more quoted lines elided]…
> you are making a different one instead.

Frankly, I fail to comprehend. Which "mistakes" you are alluding to?

>  Hashing algorithms are very
> inefficient in the use of their 'hashing address space'.

Let us see. If one wants to search 1,000,000 keys 8 byte each, an ordered table for
binary search will consume 8,000,000 bytes. It will use 20 comparisons between keys, on
the average, for either a successful or unsuccessful search. A 25% sparse hash table
with 1,250,000 elements consuming 10,000,000 bytes will need, on the average, 1
comparison to do the same work. 250,000 bytes of memory is hardly anything, by modern
standards, to pay for performance better by an order of magnitude. However, if one is
really concerned about the "inefficient use of address space", even 99% full hash table
will use 1.5  comparisons to find the search key and 0.99 - to reject it (given that
the collisions are resolved by coalesced list chaining).

> It would be
> a terrible way to store a large table in computer memory,

About 25% more terrible than in the case of binary search, with the advantage of
searching 10 times faster.

> .and if the table is small, it hardly deserves a hash table, no?

And why not? Define "small". If the number of keys is small, the memory considerations
become irrelevant altogether, and we can use a 90% sparse hash table! A successful
search would hardly occur faster (the same 1 comparison), yet only 1 comparison per 10
unsuccessful searches would be needed, and that would be quite welcome if most search
keys, as it often happens, are not in the table!

>  Once again, the
> best solution to this type of problem is either:
…[3 more quoted lines elided]…
>    while loading, pass the other file and match using binary search.

Once again, define "small". Insertion sort is a lovely simple algorithm; however, it
sorts in O(N*N) time, and is hardly of any practical use for more that a couple of
dozen of keys, or if the input is already somewhat ordered (for instance, through a
partial partitioning quicksort scheme). As to the binary search, the faith in this
algorithm borders on religious, even though in the plain everyday activity, nobody
ventures to use it. Looking for "Aaron" in a dictionary, do you open it in the middle
or closer to the beginning? A computer algorithm paralleling it, the "interpolation
search", actually manages to search in log(log(N)) time, as opposed to log(N) time for
the binary search (i.e. 5 comparisons instead of 20 for 1,000,000 keys). However,
*that* is really input-dependent...

> B. If the table is too large for memory, then sort both files and
>    do a match, or create a key index for one file, and do a match
>    using the key index.

No doubt about that... even though with the speed hashing provides, it may be faster to
repeatedly hash in chunks writing an unmatched part for the time being and rehashing
again, than to sort both files, especially if the bigger one is burdened with a long
satellite tail.

Both those solutions are simpler, and more efficient than hashing,

> for this particular application. :-)

"Simpler" is a matter of opinion; as far as efficiency goes, let me respectfully
disagree.

> Also, you should bear in mind that many authors, and most academics,
> have never designed and written applications in the 'real world', and
> often have little understanding of maintaining systems over time.

Thank you, I will try to keep it in mind. Actually, I only mentioned the discussions of
hashing in the COBOL books to emphasize that hashing is not all that foreign to a COBOL
programmer. I am not sure whether McCracken and Gary DeWard Brown are those "academics"
who never written and designed an application in the "real world". Maybe. I simply do
not know. However, I can tell from my own experience of writing and maintaining hashing
programs in a number of tongues (including SAS, COBOL, PL/I, C, and, God forbid,
Algol-60 - circa 1972) that they are not all that horrible, and in any case, those two
or three hashing paragraphs are much more simplistic than many legacy applications'
routines I have been unfortunate to encounter at 3 o'clock in the morning.

> Real world applications are seldom as simplistic as examples given
> in books, and frequently get very messy, because of peculiar design
> requirements. :-)

Or, often times, without any requirements at all! :-)

Kind regards,
=========================
Paul M. Dorfman
AT&T Universal Card
Jacksonville, Fl
=========================
"Though this be madness, yet there is method in't".
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 6)_

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s7eh4.448$x3.694@wormhole.dimensional.com>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia> <388561FB.7A70714@mediaone.net>`

```
The problem with using working storage tables of any sort with this method
is that the keys must be stored.  Most COBOL's have a limit on the size of
an 01 level and it is wasteful of system resources to code huge working
storage tables.  In an application I support we have exceeded the 01 level
size limitations several times recently.  I hate arbitrary limitations
imposed by sizes of tables.  I suppose you could code to fill the hash list
to a certain point and process the second file in stages, eliminating as
many records as possible each pass.  But then you have added a whole new
layer of complexity to the process.

If the hash list resolves collisions by quadratic probing it will degrade to
worse than a simple sequential search since each hit on an occupied node not
equal to the searched for key must continue probing until an empty node is
hit, or all nodes have been probed.  And quadratic probing is better than
secondary hashing functions.

If the hash list resolves collisions by chaining, then it will do better,
however not nearly as well as you have stated.   Each hit on an occupied
node will require a search of the full sublist chain to ensure the key does
not exist.  If the hash algorithm has a good distribution this will still
beat binary searches by at least log2(hash list size) compares, but keep in
mind the overhead of hashing a key well is very likely to be greater than
the overhead of adjusting the index for a binary search.  I once benchmarked
SEARCH vs. SEARCH ALL and the results were surprising!  Even the modest
overhead of the binary search's index adjustment moved the break even point
of the binary search from the theoretical 5 items to 32 items.  It is quite
probable the hashing overhead will eat away some of the minimum compare
advantages the hash list enjoys for lists resolving collisions through
chaining.

To use a dictionary hash list without storing the keys the best you can do
is hit an empty node and know the key does not exist.  If the node is not
empty the key may or may not exist.

In any event, hash lists are indeed sensitive to the data volume and key
cardinalities.  Without solid information about the files and the
requirements of the process being developed sorting the files and then
processing them simply is the best alternative.  These files may be quite
large or have high growth rates, or have very large keys or very high key
cardinality.  The process may be a one-shot, in which case the effort to
code and test the hash list solution is excessive, or it may be an ongoing
reconciliation which changing characteristics of the files may require the
program implementing the hashed list solution to be re-visited periodically
for tuning of the list.  It may also be that one of the files is already in
the correct sort order.

All in all the sorting and filtering solution is simpler, more stable, less
complicated, easier to test and maintain.  Its performance will not vary as
much with changing data characteristics, either.  Unless there is a pressing
need for optimal speed I do not see the hashing solution as viable other
than as an academic or ego exercise for the person coding it.  The clever
way is often not the best way in the long term, and even in the short term
the clever way is often excessively clever.

Glenn Gordon



"Paul M. Dorfman" <sashole@mediaone.net> wrote in message
news:388561FB.7A70714@mediaone.net...
> Judson McClendon wrote:
> > Paul M. Dorfman wrote:
> > >Judson McClendon wrote:
> > >> >Paul M. Dorfman wrote:
> > >> >>1. Choose the file having lesser number of records. Suppose it is
BANK.
> > >> >>2. Store persnumbers from this file in a hash table (in memory).
> > >> >>3. Read a record from PERSON.
> > >> >>4. Search the table for persnumber coming from it. If it is in the
table go to
> > >> >>3. If not, output the record and go to 3.
> > >> >>5. Stop.
> > >> >>
> > >> >>This way, you have to sort neither file, and it will work a whole
lot faster
> > >> >>than SEARCH ALL, even  without accounting for the time needed to
sort the keys
> > >> >>from BANK. If you are not sure how to organize a hash table,
consult Knuth,
> > >> >>v.3.
...
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3885C5AD.D576A6F8@NOSPAMwebaccess.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia> <388561FB.7A70714@mediaone.net> <s7eh4.448$x3.694@wormhole.dimensional.com>`

```


Glenn Gordon wrote:
> 
> The problem with using working storage tables of any sort with this method
> is that the keys must be stored.  Most COBOL's have a limit on the size of
> an 01 level and it is wasteful of system resources to code huge working
> storage tables.  

That makes sense.  But what is the real cost of this "waste" nowadays? 
Every once in a while I need to reevaluate my old assumptions of cost. 
While the cost of maintaining a table which has new limits beyond what
analysis predicted is still high, I would like some feedback on what
currently are the costs of having a large working storage table compared
to alternatives - on mainframes and other environments.

If I stick a huge table in a COBOL program, am I costing my employer
anything significant?
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 8)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ynkh4.19678$Dv1.486996@news2.rdc1.on.home.com>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia> <388561FB.7A70714@mediaone.net> <s7eh4.448$x3.694@wormhole.dimensional.com> <3885C5AD.D576A6F8@NOSPAMwebaccess.net>`

```

"Howard Brazee" <brazee@NOSPAMwebaccess.net> wrote in message
news:3885C5AD.D576A6F8@NOSPAMwebaccess.net...
>
>
> Glenn Gordon wrote:
> >
> > The problem with using working storage tables of any sort with this
method
> > is that the keys must be stored.  Most COBOL's have a limit on the size
of
> > an 01 level and it is wasteful of system resources to code huge working
> > storage tables.
…[9 more quoted lines elided]…
> anything significant?

At some point, the time taken to manage and/or search a table exceeds the
time taken to retrieve the record from an indexed file or relational table.
Since it is now possible to cache the entire data store, this point is lower
than in the past when the data store resided on disk. So, for really large
tables, consider using traditional I/O methods rather than writing your own
caching routines. As an added bonus, if the table resides in a relational
database, referential integrity rules become the problem of the database and
not your program.

Karl Wagner
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 7)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3886B7F7.3B8368CB@mediaone.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia> <388561FB.7A70714@mediaone.net> <s7eh4.448$x3.694@wormhole.dimensional.com>`

```
Glenn Gordon wrote:

> The problem with using working storage tables of any sort with this method
> is that the keys must be stored.  Most COBOL's have a limit on the size of
…[6 more quoted lines elided]…
> layer of complexity to the process.

Right. I'd better reserve hashing (or an ordered table search, for that matter)
for the cases when a table can be organized completely in memory.

> If the hash list resolves collisions by quadratic probing it will degrade to
> worse than a simple sequential search since each hit on an occupied node not
> equal to the searched for key must continue probing until an empty node is
> hit, or all nodes have been probed.

Not *will* but rather *could*. The performance of any collision resolution
policy degrades appreciably as the table gets fuller. But even the linear
probing - the simplest and slowest scheme - performs acceptably for tables with
the load factor below 60%.

>  And quadratic probing is better than
> secondary hashing functions.

This is inaccurate. Open addressing with double hashing (if this is what you
mean by "secondary hashing function") is much faster since it randomizes probing
sequences much better than quadratic probing, the latter exhibiting secondary
clustering, and the former not. If a table is 25% sparse, double hashing, by the
very nature of the algorithm, is guaranteed - no matter  how many keys are
actually stored in the table - to use no more than 2 probes to find a search key
and no more than 4 to have it rejected if it is not in the table.

> If the hash list resolves collisions by chaining, then it will do better,
> however not nearly as well as you have stated.

What I stated is not a theoretically derived conjecture but experimental results
obtained in various languages on many platforms and with wide variety of
real-world, real-size data. Hash search coded in 3- and 4GLs has been compared
with binary search coded in the underlying software (e.g. Search All in COBOL,
formats in SAS, etc.) and always wins the bigger, the more keys are  to be
searched. It should be noted, though, that the experimental results corroborate
theoretical ones quite well, and in fact, in practice hash search runs even
slightly faster than predicted by the theory.

>   Each hit on an occupied
> node will require a search of the full sublist chain to ensure the key does
> not exist.

Right. However, how big is the sublist on the average? If there are more nodes
than keys, it is less than 1 key, so an unsuccessful search requires less than 1
comparison. Sure some addresses will contains several keys, and others none, yet
even the simplest hash function like mod(key, hashtablesize) virtually
guarantees that no sublist will be longer than several keys, and therefore can
be efficiently searched serially. Of course, to make that happen, the hash table
size should prime and not too close to the power of 2, but what is the problem
of choosing it this way?

>  If the hash algorithm has a good distribution this will still
> beat binary searches by at least log2(hash list size) compares, but keep in
…[7 more quoted lines elided]…
> chaining.

And how great is the hashing overhead compared to that of binary search? In each
iteration of the latter, there are two computations: one calculating a midpoint
and one addition (subtraction) to adjust the index. For an unsuccessful search,
this has to be done full log2(N) times; for a successful search, same but on the
average. On the other hand, if it is decided to hash using a modulo and resolve
collisions by chaining, hashing *always*  incorporates a single division per
given key to search for. It is all computational overhead it has, for if the
remainder points to an empty node, the key is not in the table, and the
algorithm stops. Otherwise, as you have indicated above, it has to go through
the sublist of the keys attached to the node whose average length is less than
1. I have studied distributions of real-world keys using the modulo function
with the divisor chosen according to the above simple rule, and it is quite rare
to find a mere couple of nodes per million with more than 8 keys colliding in
it, even if the table is nearly full, while Your own conclusion tells that such
short lists are best searched sequentially, plus the vast majority of the keys
occupy their seats alone. In the worst-case scenario of 8 colliding keys, 8
moves would have to be made to adjust the links, and less than 1 on the average.
However, binary search has its own data movement overhead having to move the
midpoint adjusted up or down by unity to the low/ high index, only it has to do
it, on the average, not once, log2(N) times. If double hashing were used, it
would have an extra subtraction to step through the table (2 on the average per
key searched). Seemingly, another division would be needed to compute the probe
decrement, but it is exactly in COBOL where it is not necessary, since the
quotient already obtained as a result of the first division can be utilized for
this purpose. So, all in all, whose overhead is higher?

> To use a dictionary hash list without storing the keys the best you can do
> is hit an empty node and know the key does not exist.  If the node is not
> empty the key may or may not exist.

You are referring to key-indexed search. This is the fastest existing search
scheme, indeed, and so should always be used when applicable. Unfortunately,
key-indexing requires that memory must be abundant to swallow the entire
universe of key values. This is OK if the keys are say 5-digit integers but
generally rarely possible, and certainly not if the keys are long character
strings. However, when it can be used, key-indexing is the same old hash again,
only with an infinitely sparse table and constant hash function.

> In any event, hash lists are indeed sensitive to the data volume and key
> cardinalities.  Without solid information about the files and the
…[8 more quoted lines elided]…
> the correct sort order.

The effort of coding and testing a "hashing solution" is no greater than
anything else in data processing, and any competent programmer capable of coding
a bubble sort can implement it in a matter of an hour or two by simply literally
following one of the algorithms provided by Knuth. This is especially true if it
has already been coded and tested great many times, in which case it is a
cut-and-paste effort hardly even qualifiying for a coding effort. I routinely
run a number of such matching "solutions" in production where hash tables are
populated afresh daily with the keys from a vendor driver files, every time
different. I have never had to re-visit the programs or tune it for a particular
driver, yet they consistently run in the same specific (i.e. relative to the
number of keys in the other file) time.

> All in all the sorting and filtering solution is simpler, more stable, less
> complicated, easier to test and maintain.  Its performance will not vary as
…[4 more quoted lines elided]…
> the clever way is often excessively clever.

A need for optimal speed is always there, and now more than ever. As data
processing is headed in the direction of data warehousing and OLAP, and business
forecasting is based more and more on time series analyses relying on literally
years of transactional data history, quick methods of data extraction,
validation, scrubbing and so on become a paramount necessity rather than an
"academic or ego exercise". Such exercises per se, by the way, are not all that
harmful. After all, "simple" and KISS methods we are taking now for granted,
were academic or ego exercises at some point. (However, hashing has hardly ever
qualified for such an exercise since it was originated, theoretically grounded,
and developed into a practical method of data searching in the depths of Big
Blue in fifties.) The saying that the most practical thing is a good theory
belongs to one of the greatest experimental physicists of all time.

Kind regards,
==================
Paul M. Dorfman,
Jacksonville, Fl
==================

> Glenn Gordon
>
…[22 more quoted lines elided]…
> ...
```

###### ↳ ↳ ↳ Re: search

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8643nq$1bga$1@news.hitter.net>`
- **References:** `<85qet0$23hl$1@buty.wanadoo.nl> <38829D54.D3126B14@mediaone.net> <5mLg4.962$SM.12557@news4.mia> <388404EC.190F174A@mediaone.net> <hW_g4.3246$wk.43393@news1.mia> <388561FB.7A70714@mediaone.net>`

```

Paul M. Dorfman wrote in message <388561FB.7A70714@mediaone.net>...
>
>Judson McClendon wrote:
[...]
>>  Hashing algorithms are very
>> inefficient in the use of their 'hashing address space'.
>
>Let us see. If one wants to search 1,000,000 keys 8 byte each, an ordered
table for
>binary search will consume 8,000,000 bytes. It will use 20 comparisons
between keys, on
>the average, for either a successful or unsuccessful search. A 25% sparse
hash table
>with 1,250,000 elements consuming 10,000,000 bytes will need, on the
average, 1
>comparison to do the same work. 250,000 bytes of memory is hardly anything,
by modern
>standards, to pay for performance better by an order of magnitude. However,
if one is
>really concerned about the "inefficient use of address space", even 99%
full hash table
>will use 1.5  comparisons to find the search key and 0.99 - to reject it
(given that
>the collisions are resolved by coalesced list chaining).
>
…[3 more quoted lines elided]…
>About 25% more terrible than in the case of binary search, with the
advantage of
>searching 10 times faster.

10,000,000 - 8,000,000 = 2,000,000 not 250,000; but still 25%
memory overhead.

Adding a four byte field for list chaining yields

15,000,000 - 8,000,000 = 7,000,000 or 87.5% memory overhead.

I think using a hash table for the problem, as described, is
overkill.
------------------
Rick Smith
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
