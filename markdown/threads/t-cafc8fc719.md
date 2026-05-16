[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migrating ISAM to Relational Database

_36 messages · 10 participants · 2007-04_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases) · [`VSAM, files, sorting`](../topics.md#files)

---

### Migrating ISAM to Relational Database

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-14T00:08:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<589a52F2g4c1cU1@mid.individual.net>`

```
As promised, I dug around and found some documents that could be useful for 
people considering migration.

The one on Normalization is a revamp of an opriginal paper from MicroSoft. I 
don't know who wrote it but it is crisp and succinct. I revised it 
minimally.

The other two describe some tools I wrote, and in the course of doing so, 
provide some useful background and examples.

Here is a snippet from another thread here...

>> If/when you get a paperback, or articles on design from the Web,
>> concentrate on the term 'Normalization' so that you have a handle on it.
…[9 more quoted lines elided]…
>
This has now been posted... Accessing the following link will reveal 3 
documents that are worth reading if you are considering migrating ISAM to 
RDB....

http://homepages.ihug.co.nz/~dashwood/dashwood/RDBStuff/

Any or all feedback appreciated.

Pete.
```

#### ↳ Re: Migrating ISAM to Relational Database

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-13T23:52:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1320k5l1kvroc05@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:589a52F2g4c1cU1@mid.individual.net...
[snip]
> This has now been posted... Accessing the following link will reveal 3
> documents that are worth reading if you are considering migrating ISAM to
…[4 more quoted lines elided]…
> Any or all feedback appreciated.

In 4.ISAM2RDB.doc,

1. Page 3, Dealing with OCCURS (Repeating Groups),
    items 1 and 3. You seem to disregard the space savings
    that ODO and RECORD VARYING provide.

2. Page 4, ultimate paragraph. You write "COBOL
    supports 3 levels of indexing". That was true of COBOL
    '74. COBOL '85 allowed 7 levels.

3. Page 8, Currency data type (in table). You write "This
    data TYPE is held as 64 bit floating point ...). MS Access
    help states, "Currency variables are stored as 64-bit (8-byte)
    numbers in an integer format, scaled by 10,000 to give a
    fixed-point number with 15 digits to the left of the decimal
    point and 4 digits to the right."
```

##### ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-14T22:37:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58bp6cF2h1f0qU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1320k5l1kvroc05@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[14 more quoted lines elided]…
>    that ODO and RECORD VARYING provide.

Yes, that's probably true, although I would have done so unconsciously.

My personal opinion (and it is ONLY that :-)) is that these constructs are 
just pointless and useless. Unless COBOL dynamically allocates space (and it 
doesn't) the only "saving" that is made with ODO is on external media. 
Internally, an ODO definitition always takes the maximum space that it 
could. The compiler has to allocate the maximum because it can't dynamically 
allocate space at run time.

I don't use this construct, and I discourage others from doing so too. A 
relational DB allows "tables" with "infinite" (limiited only by available 
disk space, and that gets cheaper every year) dimension, so the external 
saving is just unnecessary if you use RDB, anyway.

Never needed it; don't use it. :-)

RECORD VARYING... may have some marginal use and is certainly important when 
processing legacy files.

I honestly don't know what ISAM2RDB does with these constructs. I think it 
iwould be an easy matter to change the ISAM source so that it reflected the 
maximums before presenting it to ISAM2RDB. If I was still interested in 
marketing this stuff I'd fix it to accommodate these constructs.

>
> 2. Page 4, ultimate paragraph. You write "COBOL
>    supports 3 levels of indexing". That was true of COBOL
>    '74. COBOL '85 allowed 7 levels.

Thanks. I didn't know that. I could easily modify ISAM2RDB to take this into 
account. I have never seen a live COBOL program with more than 3 dimensions 
(and even 3 is pretty rare), so I don't see this as a major problem. I guess 
people don't always do what the standard may permit them to.

>
> 3. Page 8, Currency data type (in table). You write "This
…[5 more quoted lines elided]…
>

Hardly worth arguing (floating point is just one intepretation of scaled 
decimal) but I stand corrected. :-)

Thanks for the comments, Rick. I wish I had been able to get someone whose 
opinions I value as much as yours to review these documents before they were 
published. I did the best I could under the circumstances :-).

Pete.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-14T14:48:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7R5Uh.243866$8_1.167513@fe05.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net>`

```
(I found the .DOC file, but don't remember if Pete posted links to the programs 
themselves.  However, a couple of comments on Rick's ideas (and Pete's replies).

1) On the mainframe 4-7 level tables do occur.  Not super often, but do exit.

2) The RECORD VARYING IN SIZE phrase (in an FD) is (IMHO) one of the more useful 
additions of the '85 Standard.  This allowed one to "get" the size of variable 
length record easily and via a "supported" interface.  It also makes "setting" 
the size on output easier as well.

3) Whether or not using ODO would have been a "good idea" would depend on where 
it is used.  In Standard COBOL, one may ONLY specify an ODO as the last "group" 
at the end of a record.  (One may not have data following an ODO at the same 
level, nor may one nested an ODO under another OCCURS - either with or without 
the DEPENDING ON phrase).  Now there is a relatively common extension that 
allows "nested" ODO's and data after an ODO.  HOWEVER, what this actually means 
(semantics) does vary from implementor to implementor.  Check out the Micro 
Focus "ODOSLIDE' directive to see two of the major implementation differences. 
In fact, this SORT-OF answers Pete's "dynamic allocation" issue.  When one uses 
the ODOSLIDE (on) directive, MF doesn't actually do dynamic allocation but DOES 
change the amount of storage "currently in use" (available to the application). 
Again, I don't know if Pete was talking about places that would or would not be 
conforming for ODOs, but (in general) I would agree with him that "avoiding" its 
use unless there is a REALLY good reason to use them, is probably a good idea.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "Joel C. Ewing" <jcREMOVEewing@CAPS.acm.org>
- **Date:** 2007-04-14T15:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`
- **In-Reply-To:** `<58bp6cF2h1f0qU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
> news:1320k5l1kvroc05@corp.supernews.com...
…[34 more quoted lines elided]…
> 
Like so much in this business, it depends.

If ODO saves a significant amount of raw file space to store the data on 
external media this can have a number of beneficial effects that go much 
beyond the mere cost of your DASD media: (1)savings in processor time, 
I/O activity, media, and real time to backup the external data for 
Disaster Recovery; (2)savings in cost of disk media at a DR recovery 
site (which may be expensive or difficult to increase depending on your 
contract); (3)savings in processor time, I/O activity, and real time to 
reorganize or rebuild the database;(4)savings in processor time, I/O, 
and elapsed time to sequentially access a significant percent of the 
database, because more used bytes are transferred with each physical 
block read; (5)savings in the number of buffers required (affecting size 
of working set and real storage requirements) for caching the database 
in order to contain the same number of records in cache and get 
acceptable response time for random access.

If you are in an environment where you are never constrained by 
processor time, real memory, I/O response times, daily batch windows, 
DASD availability, or DR costs, then by all means ODO is irrelevant.  In 
all other cases, one looks for the major resource hogs, or "loved ones" 
with poor response times, and do whatever it takes to address the 
problem, including use of ODO where appropriate.

We too have had COBOL programmers who hated to deal with variable length 
records.  But, the marginal extra cost to manage variable length records 
within a COBOL program can easily be insignificant when compared with 
what is costs to pump unused bytes through the I/O subsystem over and over.

COBOL does not bother to dynamically allocate storage to ODO items at 
run time, because with virtual storage there is no significant savings 
in allocating COBOL ODO data items at anything less than the max 
required.  Unused portions of a large array do not contribute to the 
working set of the program or the real storage required to execute.  In 
the z/OS environment, real 4KiB pages wouldn't even be assigned to 
portions of a large array until the first reference required it.  So 
long as you don't do something silly, like initializing the entire array 
in advance just in case you might need all of it, then the cost of 
unused portions is essentially zero in that environment.

Although it's probable your remarks on ODO were only intended to apply 
to record formats used in I/O, I want others reading this to be clear 
that there are other cases in COBOL where ODO is the only reasonable way 
to go. One case where ODO should ALWAYS be used is for a sorted data 
item array with a variable number of items that will be used repeatedly 
with a SEARCH ALL.  Not only does proper setting of the "depending on" 
variable eliminate the need to initialize unused trailing items in the 
array, but it guarantees the resulting binary search uses the minimal 
number of compares for the search.  For arrays whose max size is much 
greater than their average usage, failure to use ODO here can have a 
significant negative impact on performance.
...
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2007-04-14T14:20:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176585614.919567.229980@e65g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`

```
On Apr 14, 4:29 pm, "Joel C. Ewing" <jcREMOVEew...@CAPS.acm.org>
wrote:
> Pete Dashwood wrote:
> > "Rick Smith" <ricksm...@mfi.net> wrote in message
…[90 more quoted lines elided]…
> Joel C. Ewing, Fort Smith, AR        jREMOVEcCAPSew...@acm.org

Joel

I agree with you, though I think that these days file compression on
the fly is also available in some environments and is probably much
more effective at reducing files sizez.  I quite agree with your
comments on minimising sort requirements, though am mot so sure about
only initiallzing the parts of a table in use.  While I see the
benefits of this there, it also sets a trap for the unwary maintenance
programmer at 3.00 a.m. on a call out, though I can also see that
clear and/or appropriately documented code would minimise the risk.

Have you seen John Piggott's proposal for taking the topic quite a bit
further and now incorporated in the draft standard for the next
revision?  It is very similar to the technique used by the Pick O/S,
though its use for files was left aa a possible future enhancement.
Then people would be able to truly talk about COBOL files, as this
format would then only be able to be read by COBOL programs in non-
Pick operating systems, though I suppose suppliers might also write
some utilities for them.  I would make reading dumps harder and
interpretive debuggers harder to implement and follow.

It will be of great benefit to programs using massive data structures,
though for general use it would probably add unnecessary complexity.

Robert
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-15T00:14:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_7eUh.310456$Wg6.198519@fe07.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com>`

```
"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1176585614.919567.229980@e65g2000hsc.googlegroups.com...
> On Apr 14, 4:29 pm, "Joel C. Ewing" <jcREMOVEew...@CAPS.acm.org>
<much snippage> (and bottom-posted for a change <G>)
>
> Have you seen John Piggott's proposal for taking the topic quite a bit
…[12 more quoted lines elided]…
> Robert

And what has gotten into the draft (WD 1.7) is a MESS  (for ANY LENGTH items 
especially, but many of the same problems also exist for dynamic tables). 
Specifically for the ANYLENGTH items, see:

 http://www.cobolstandard.info/j4/files/07-0060.doc

Dynamic tables are at least "better" (cleaner?)as they don't have the "direct" 
option; stoarage is always "wherever the implementor puts it"
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-15T14:26:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58dgrbF2h7s3aU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com>`

```

"Robert Jones" <rjones0@hotmail.com> wrote in message 
news:1176585614.919567.229980@e65g2000hsc.googlegroups.com...
> On Apr 14, 4:29 pm, "Joel C. Ewing" <jcREMOVEew...@CAPS.acm.org>
> wrote:
…[47 more quoted lines elided]…
>> Like so much in this business, it depends.

Yes. But for me at least, the disadvantages far outweigh the advantages.
>>
>> If ODO saves a significant amount of raw file space to store the data on
>> external media this can have a number of beneficial effects that go much
>> beyond the mere cost of your DASD media:

IF it saves space and SIGNIFICANT space. A RDB in normal form will provide a 
better storage solution, in my opinion. It isn't just about space; it is 
about overall availablity.

>>(1)savings in processor time,

Huh?!! The processor time to deal with ODO is outrageous...compared to fixed 
length.

Awww... I was gonna respond to all of these points below, and then I 
realised it just isn't worth the time. Use ISAM with or without ODO if you 
really believe what you have written; I'll stick to RDB.

>> I/O activity, media, and real time to backup the external data for
>> Disaster Recovery;
 (2)savings in cost of disk media at a DR recovery
>> site (which may be expensive or difficult to increase depending on your
>> contract); (3)savings in processor time, I/O activity, and real time to
…[13 more quoted lines elided]…
>> problem, including use of ODO where appropriate.

Sure, whatever... I just don't see ODO as a solution; I see it as a problem. 
:-)

>>
>> We too have had COBOL programmers who hated to deal with variable length
>> records.

Not me. I don't get emotional about software. I don't use ODO, not because I 
hate variable records, but because it introduces unjustifiable complexity 
and hassle. Besides, you don't need ODO to create varying length records.


>> But, the marginal extra cost to manage variable length records
>> within a COBOL program can easily be insignificant when compared with
…[17 more quoted lines elided]…
>> to go.

Yes, my remarks were intended to apply to record formats used in I/O. But I 
also contest your assertion that it is "the only reasonable way to go"... 
:-)


>> One case where ODO should ALWAYS be used is for a sorted data
>> item array with a variable number of items that will be used repeatedly
…[5 more quoted lines elided]…
>> significant negative impact on performance.

Get a life!  "Can have..." ? "Significant" ?  Sure, and you COULD get hit by 
a meteorite with SIGNIFICANT impact, while walking down the road.  Real life 
example...?  Nope.  In 1960 this might have mattered; in 2007.... I think 
not.

SEARCH ALL will take into account the trailing entries anyway, (provided you 
have them set to high values). You say using ODO  will "eliminate the need 
to initialize unused trailing items in the array"  but this can be done at 
compile time and the table can be loaded initialized. You then say "it 
guarantees the resulting binary search uses the minimal number of compares 
for the search." but the difference in number of compares is binary; it 
isn't one extra compare for every "trailing" entry...

Sorry, I'm not persuaded.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 6)_

- **From:** "Joel C. Ewing" <jcREMOVEewing@CAPS.acm.org>
- **Date:** 2007-04-15T21:56:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IcxUh.21767$PL.195@newsread4.news.pas.earthlink.net>`
- **In-Reply-To:** `<58dgrbF2h7s3aU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Robert Jones" <rjones0@hotmail.com> wrote in message 
> news:1176585614.919567.229980@e65g2000hsc.googlegroups.com...
>> On Apr 14, 4:29 pm, "Joel C. Ewing" <jcREMOVEew...@CAPS.acm.org>
>> wrote:
...
>>> Like so much in this business, it depends.
> 
> Yes. But for me at least, the disadvantages far outweigh the advantages.

>>> If ODO saves a significant amount of raw file space to store the data on
>>> external media this can have a number of beneficial effects that go much
…[9 more quoted lines elided]…
> length.

At least in the z/OS environment, accessing an ODO array of data-items 
which is isolated to its own Level 01 declaration, or which is not 
followed by any other data-items within the same 01 level, introduces 
minimal overhead beyond that associated with handling a fixed array.  On 
the other hand, requesting the Operating System to initiate a physical 
I/O is a service with a very long instruction path.  If you use ODO in 
contexts that do not introduce overhead and as a consequence reduce 
physical I/O, you come out ahead.

> 
> Awww... I was gonna respond to all of these points below, and then I 
…[82 more quoted lines elided]…
> Sorry, I'm not persuaded.

As William Klein aptly observed, I speak from an MVS-z/OS-centric view. 
  What is perhaps less obvious is that I speak from a z/OS Technical 
Support view, not that of a typical COBOL programmer.  Although there 
are exceptions, typically the only COBOL programs I deal with are those 
used in the batch environment which are either causing performance or 
excessive cost problems for the end user, or causing performance or 
excessive resource consumption for the Operating System as a whole. 
This undoubtedly colors my views on COBOL coding practices.

One of the things I've learned over the years is that is doesn't matter 
how fast your processor or I/O subsystem may be or how much real memory 
you have, there will always be some applications massive enough to 
require serious tuning and optimization efforts.  That's as true today 
as it was in 1960 - it's just that since 1960 the bar has been raised 
considerably.  I don't know any one who has been hit by a meteorite, but 
I have seen COBOL application code where the improvement from SEARCH ALL 
with ODO, vs. without, was felt by the end user in his pocket book. 
Perhaps these are pathological cases, but then most of the COBOL code I 
deal with may be pathological in one sense or another.

We are a heavy DB2 shop, so I am by no means opposed to relational 
databases.  They allow us to do many things that were not possible with 
data maintained in VSAM KSDS datasets, not the least of which is the 
ability for better recovery and consistent point-in-time backups, and we 
would never consider going back to the pre-DB2, not-so-good old days. 
However, one thing we did observe as an almost universal truth 
throughout the conversion process:  going from a well optimized VSAM 
KSDS solution to an equivalent-performing relational database solution 
invariably required more storage on external media, more processing 
power, and more real memory to drive the same applications.  The good 
news was that afterwards tuning for higher performance and better 
response time became much easier, as long as you had real memory to 
throw at DB2.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 6)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-16T12:52:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176753130.901742.232580@e65g2000hsc.googlegroups.com>`
- **In-Reply-To:** `<58dgrbF2h7s3aU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net>`

```
On 15 Apr, 03:26, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
>
> Huh?!! The processor time to deal with ODO is outrageous...compared to fixed
> length.
>

I don't wish to get caught in the crossfire between the ODO:Fixed
Length:RDB camps but I have worked with ODO (and had no problems with
it except for the continual need to recalculate field positions, etc.,
and dumps) but has any one got any empirical data to prove their case?

<TUPPENCE WORTH>

I don't see that ODO really would be more cpu intensive than fixed
length unless it is to do with calculating addressability of each
field each time it is accessed (than can be overcome by moving the
fixed length occurrence to a fixed length group field). Perhaps
someone knows how Cobol works better than I do and can enlighten a
poor humble one-time Assembler programmer (and analyst) (shades of
DD).

I can understand how programmers could take a dislike to ODO but when
you use it every day (as I have) then you come to love it ;-). And it
does save space.

It probably is better to use a RDB in an era when all users expect
their data to reside on databases (after all, it isn't important data
if it isn't retained on a DB) but the best recommendation for using a
RDB is not to use it as an extended flat file but to use it for its'
data-connectivity and security features, surely?

</TUPPENCE WORTH>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-16T20:10:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aLQUh.220851$mw4.139149@fe06.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com>`

```
As far as "hard facts" go (and this is for ONE specific compiler - which is a 
couple of releases old - on one platform), you can check out the "performance 
tuning" paper for Enterprise COBOL at:

  http://www-1.ibm.com/support/docview.wss?rs=203&q=7001475&uid=swg27001475

According to pages 32-33

"OCCURS DEPENDING ON

When using OCCURS DEPENDING ON (ODO) data items, ensure that the ODO objects are 
binary (COMP) to avoid unnecessary conversions each time the variable-length 
items are referenced. Some performance degradation is expected when using ODO 
data items since special code must be executed every time a variable-length data 
item is referenced. This code determines the current size of the item every time 
the item is referenced. It also determines the location of variably-located data 
items. Because this special code is out-of-line, it may inhibit some 
optimizations. Furthermore, code to manipulate variable-length data items is 
substantially less efficient than that for fixed-length data items. For example, 
the code to compare or move a variable-length data item may involve calling a 
library routine and is significantly slower than the equivalent code for 
fixed-length data items. If you do use variable-length data items, copying them 
into fixed-length data items prior to a period of high-frequency use can reduce 
some of this overhead.

 Performance considerations for fixed-length vs variable-length tables:

     using variable-length tables is 5% slower then using a fixed-length table
     using a variable-length table that references the first complex ODO element 
is 7% slower then using a fixed-length table
     using a variable-length table that references a complex ODO element other 
than the first is 140% slower  then using a fixed-length table"

   ***

Note well:
  This implementation DOES support the "non-Standard" complex ODO's where ODO's 
can be nested (under fixed or ODO OCURS) and where data can follow an ODO in the 
same record.  I *believe* that this is what adds SOME of the overhead.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T07:09:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176905374.285186.197050@n76g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<aLQUh.220851$mw4.139149@fe06.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <aLQUh.220851$mw4.139149@fe06.news.easynews.com>`

```
On 16 Apr, 21:10, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> As far as "hard facts" go (and this is for ONE specific compiler - which is a
> couple of releases old - on one platform), you can check out the "performance
…[15 more quoted lines elided]…
> same record.  I *believe* that this is what adds SOME of the overhead.

Thanks Bill, I think 7 % is acceptable but 140 % is not.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-16T17:38:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1327rcs6m9u7207@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
news:1176753130.901742.232580@e65g2000hsc.googlegroups.com...
> On 15 Apr, 03:26, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
> >
> > Huh?!! The processor time to deal with ODO is outrageous...compared to
fixed
> > length.
> >
…[4 more quoted lines elided]…
> and dumps) but has any one got any empirical data to prove their case?

Not my case to prove; but ...

Using Micro Focus COBOL 3.2.24 (Jun 1994)
-----
       identification division.
       program-id. A27B08.
       data division.
       working-storage section.
       01 t-start.
         03 t-start-hour pic 99.
         03 t-start-minute pic 99.
         03 t-start-second pic 99v99.
       01 t-end.
         03 t-end-hour pic 99.
         03 t-end-minute pic 99.
         03 t-end-second pic 99v99.
       77 t-elapsed pic 9(7)v99.
       77 t-elapsed-display pic z(6)9.99.

       78 max-size value 8192.
       01 fixed-table.
         03 fixed-entry pic x occurs max-size
               indexed by ft-index.
       77 vt-length pic 9(4) comp-5 value max-size.
       01 variable-table.
         03 variable-entry pic x occurs 0 to max-size
               depending on vt-length
               indexed by vt-index.
       77 repeat-count pic 9(8) comp-5 value 100000.
       procedure division.
       begin.
           accept t-start from time
           perform test-fixed-table
               repeat-count times
           accept t-end from time
           display "fixed    " with no advancing
           perform display-elapsed
           accept t-start from time
           perform test-variable-table
               repeat-count times
           accept t-end from time
           display "variable " with no advancing
           perform display-elapsed
           stop run
           .
       test-fixed-table.
           perform varying ft-index from 1 by 1
                   until ft-index > max-size
               move space to fixed-entry (ft-index)
           end-perform
           .
       test-variable-table.
           perform varying vt-index from 1 by 1
                   until vt-index > max-size
               move space to variable-entry (vt-index)
           end-perform
           .
       display-elapsed.
           if t-start > t-end
               move 86400 to t-elapsed
           else
               move 0 to t-elapsed
           end-if
           compute t-elapsed = t-elapsed
             + (t-end-hour - t-start-hour) * 3600
             + (t-end-minute - t-start-minute) * 60
             + (t-end-second - t-start-second)
           end-compute
           move t-elapsed to t-elapsed-display
           display t-elapsed-display
           .
-----

Results (in seconds)::
----- with BOUND directive
fixed          5.32
variable       4.89
----- with NOBOUND directive
fixed          4.89
variable       4.94
-----

ODO appears to be slightly faster with bounds
checking and slightly slower without.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 8)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-04-17T09:22:32+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f01sjs$s28$03$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:1327rcs6m9u7207@corp.supernews.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
…[99 more quoted lines elided]…
>
Hmm, MF SE 2.2 on Linux :
simlinux:~ # cob -u -C BOUND dw.cob
simlinux:~ # cobrun ./dw
fixed          2.97
variable       2.97
simlinux:~ # cobrun ./dw
fixed          2.97
variable       2.97
simlinux:~ # cob -u -C NOBOUND dw.cob
simlinux:~ # cobrun ./dw
fixed          2.98
variable       2.97
simlinux:~ # cobrun ./dw
fixed          2.98
variable       2.98

No measurable difference there.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-17T10:05:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Z0Vh.410616$8a4.65355@fe03.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com>`

```
Roger and Rick,
  I do NOT think it should matter with this specific code, but are both of you 
using ODOSLIDE or NOODOSLIDE?

I think there MIGHT be more of a difference if you

A) Put in some nested ODO's and/or data following the ODO (this would be in the 
ODO structure - while adding the "same" data after the fixed OCCURS or a nested 
OCCURS in the other example)

 AND THEN tried it with both ODOSLIDE and NOODOSLIDE.

In other words have something like:
 01 fixed-table.
         03 fixed-entry occurs max-size
               indexed by ft-index.
              05  Field1  Pic X.
             05  Nest1 occurs max-size
                   indexed by n1-index.
                      07 elem  Pic x.
            05   Field2  Pic X.

and

01 variable-table.
         03 variable-entry pic x occurs 0 to max-size
               depending on vt-length
               indexed by vt-index
             05  Field3  Pic X.
             05  Nest2 occurs 0 to max-size
                   depending on vt-length2
                   indexed by n2-index.
                      07 elem2  Pic x.
            05   Field4  Pic X

and make certain you move something to Field2 and field4 in the test loops.  (I 
would *expect* ODOSLIDE to be slower, - for variable occurrence tables. 
However, only "real world" tests will prove me right or wrong.)

P.S.  For *NON* Micro Focus users, the use of a 78-level for "max-size" allows 
what LOOKS LIKE a variable name in the occurs depending on clause.  If you want 
to compile this in a "Standard" compiler

 - delete 78 max-size value 8192
     and
 - change max-size to 8192 in the OCCURS clauses.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 10)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-04-17T14:04:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f02d4i$hj0$00$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:_Z0Vh.410616$8a4.65355@fe03.news.easynews.com...
> Roger and Rick,
>  I do NOT think it should matter with this specific code, but are both of 
…[174 more quoted lines elided]…
>

OK. Just tacked on another 03 field after the original 03 occurs entries and
moved something to that field in the perform loops -
simlinux:~ # cob -u -C BOUND -C NOODOSLIDE dw.cob
simlinux:~ # cobrun ./dw
fixed          2.99
variable       2.97
simlinux:~ # cob -u -C BOUND -C ODOSLIDE dw.cob
simlinux:~ # cobrun ./dw
fixed          2.98
variable       6.07

As Bill surmised, a considerable difference.

Roger
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T07:18:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176905892.231022.224940@n76g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<f02d4i$hj0$00$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com> <f02d4i$hj0$00$1@news.t-online.com>`

```
On 17 Apr, 13:04, "Roger While" <s...@sim-basis.de> wrote:
> "William M. Klein" <wmkl...@nospam.netcom.com> schrieb im Newsbeitragnews:_Z0Vh.410616$8a4.65355@fe03.news.easynews.com...
>
…[193 more quoted lines elided]…
> - Show quoted text -

So definitely end of argument. ODO is a cpu hog.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-18T12:06:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<132cgloe2jpnv4e@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com> <f02d4i$hj0$00$1@news.t-online.com> <1176905892.231022.224940@n76g2000hsh.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
news:1176905892.231022.224940@n76g2000hsh.googlegroups.com...
[snip]
> So definitely end of argument. ODO is a cpu hog.

No, not at all! The performance cost of ODO depends
on how it is used, not ODO itself.

ODOSLIDE is particular to implementations and is
non-standard. Comparing the value of an index-name
to a numeric value may be expensive; but comparing
the values of two index-names is not. Don't do these
two things and using ODO is only a few percent
slower than using fixed tables, for the operations
tested. For other operations, it may be faster.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 13)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-04-18T18:31:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f05h4d$1ln$01$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com> <f02d4i$hj0$00$1@news.t-online.com> <1176905892.231022.224940@n76g2000hsh.googlegroups.com> <132cgloe2jpnv4e@corp.supernews.com>`

```
Agreed,
ODOSLIDE is not supported for OC.
With xxx and comparison
simlinux:~ # cobc -x -O2 dw.cob
simlinux:~ # ./dw
fixed          0.69
variable       0.74

:-)

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:132cgloe2jpnv4e@corp.supernews.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 14)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-04-18T18:45:07+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f05huu$onb$02$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com> <f02d4i$hj0$00$1@news.t-online.com> <1176905892.231022.224940@n76g2000hsh.googlegroups.com> <132cgloe2jpnv4e@corp.supernews.com> <f05h4d$1ln$01$1@news.t-online.com>`

```
cob -ux -o dwtest -O dw.cob
cob32: warning: -x overrides -u
simlinux:~ # ./dwtest
fixed          2.97
variable       2.98


"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:f05h4d$1ln$01$1@news.t-online.com...
> Agreed,
> ODOSLIDE is not supported for OC.
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 14)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-04-18T11:40:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<462603B5.6F0F.0085.0@efirstbank.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <f01sjs$s28$03$1@news.t-online.com> <_Z0Vh.410616$8a4.65355@fe03.news.easynews.com> <f02d4i$hj0$00$1@news.t-online.com> <1176905892.231022.224940@n76g2000hsh.googlegroups.com> <132cgloe2jpnv4e@corp.supernews.com> <f05h4d$1ln$01$1@news.t-online.com>`

```
With COBOL for VSE/ESA 1.1.1:

Run 1:
FIXED         
     17.45    
VARIABLE      
     17.80    

Run 2:
FIXED         
     17.68    
VARIABLE      
     17.45    


Hmm, based on this I see no reason not to use ODO.
Though my times seem to be a lot longer than everyone else's.  And on a
mainframe?  Weird.

Frank

n 4/18/2007 at 10:31 AM, in message <f05h4d$1ln$01$1@news.t-online.com>,
Roger While<simrw@sim-basis.de> wrote:
> Agreed,
> ODOSLIDE is not supported for OC.
…[30 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-17T21:31:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<132atenmqampkf7@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:1327rcs6m9u7207@corp.supernews.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
…[35 more quoted lines elided]…
>          03 fixed-entry pic x occurs max-size

I changed pic x to pic x(3)

>                indexed by ft-index.
>        77 vt-length pic 9(4) comp-5 value max-size.
>        01 variable-table.
>          03 variable-entry pic x occurs 0 to max-size

I changed pic x to pic x(3)

>                depending on vt-length
>                indexed by vt-index.
…[25 more quoted lines elided]…
>                    until vt-index > max-size

I changed max-size to vt-length (but see results, later)

>                move space to variable-entry (vt-index)
>            end-perform
…[27 more quoted lines elided]…
> checking and slightly slower without.

New results (in seconds):
----- with NOBOUND directive
fixed         10.00
variable      25.04
-----

After restoring the comparison with max-size
instead of vt-length, the results were:
----- with NOBOUND directive
fixed         10.27
variable      10.27
-----

I then added a second index to each table: ft-limit
and vt-limit, respectively. I also added an appropriate
SET statement at the beginning of the test paragraphs
and changed the comparisons to the respective limits.
The new results were:
----- with NOBOUND directive
fixed          9.83
variable       9.89
-----

What I learned by experimentation is that, if one
tests an index against a non-index, the performance
cost for ODO can be outrageous! At least it was for
the implementation I tested. <g>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 9)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-04-18T08:08:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f04cl0$kiq$00$1@news.t-online.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <132atenmqampkf7@corp.supernews.com>`

```
Rick,
I made the same changes (x ->xxxx and comparison) -
simlinux:~ # cob -u -C NOBOUND dw.cob
simlinux:~ # cobrun ./dw
fixed          2.98
variable       2.97

So, looks like MF SE 2.2 optimizes that better than your version.
Interesting would be to try defining vt-length
as 9(8) COMP-5.

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:132atenmqampkf7@corp.supernews.com...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[141 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-18T05:26:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<132bp8oh44a0ra8@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <132atenmqampkf7@corp.supernews.com> <f04cl0$kiq$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:f04cl0$kiq$00$1@news.t-online.com...
> Rick,
> I made the same changes (x ->xxxx and comparison) -
…[5 more quoted lines elided]…
> So, looks like MF SE 2.2 optimizes that better than your version.

Maybe so; but it is still confusing.

The LRM for 3.2 has the same wording for comparison
as COBOL 2002, page 131, 8.8.4.1.1.10 Comparisons
involving index-names or index data items,

"Relation tests may be made only between
1) two index-names. The result is the same as if the
    corresponding occurrence numbers were compared.
2) an index-name and a numeric data item or numeric
   literal. The occurrence number that corresponds to the
   value of the index-name is compared to the data item
   or literal.
..."

The comparison 'vt-index > vt-length' should involve
overhead to convert vt-index to an occurrence number
before comparison with vt-length. However, the
comparison 'vt-index > vt-limit' would have no such
overhead.

> Interesting would be to try defining vt-length
> as 9(8) COMP-5.

I am using a 16-bit implementation. Using 32-bit items
unnecessarily, slows the program.

>
> Roger
…[9 more quoted lines elided]…
> >> > On 15 Apr, 03:26, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz>
> >> > wrote:
> >> > >
…[8 more quoted lines elided]…
> >> > it except for the continual need to recalculate field positions,
etc.,
> >> > and dumps) but has any one got any empirical data to prove their
case?
> >>
> >> Not my case to prove; but ...
…[124 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-18T19:54:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58m158F2gdg7oU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com> <132atenmqampkf7@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:132atenmqampkf7@corp.supernews.com...
>
>
…[5 more quoted lines elided]…
>
You think?

Quoting from post 4 days ago in this thread:

"Huh?!! The processor time to deal with ODO is outrageous...compared to 
fixed
length.."

And I didn't arrive at this conclusion because an IBM manual told me so, 
although I'm pleased to see they also recommend avoiding it.

I did my experiments 30 years ago and found this to be the case. Nothing 
posted here has caused me to change my mind.

Yes, under certain circumstances it may not be SO bad, and with care over 
subscripts and indexes it can be even better, but why bother?

There is no need for it.

Best avoided.

Pete.



>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-04-18T07:11:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1176905479.882758.107160@b58g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1327rcs6m9u7207@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net> <1176585614.919567.229980@e65g2000hsc.googlegroups.com> <58dgrbF2h7s3aU1@mid.individual.net> <1176753130.901742.232580@e65g2000hsc.googlegroups.com> <1327rcs6m9u7207@corp.supernews.com>`

```
On 16 Apr, 22:38, "Rick Smith" <ricksm...@mfi.net> wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[97 more quoted lines elided]…
> checking and slightly slower without.

Approximately 10 % difference with BOUND. On line with Bill's figures.
Ta.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-04-15T00:10:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4eUh.378709$rN.113785@fe09.news.easynews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`

```
Joel,
  I assume that it would be obvious to some - but not all - other readers from 
terms such as "DASD" "Virtual Storage" and your eventual mention of "z/OS" that 
you are probably MOST familiar with COBOL on a mainframe (and probably an IBM 
MVS-OS/390-z/OS mainframe).

Both how ODO's are handled (object code AND storage vs performance 
considerations) in that COBOL environment are not universal across COBOL 
implementations.

I am not necessarily disagreeing with you (and certainly NOT for z/OS) but I did 
want to point this out - just in case others have not.

P.S.  In fact, under z/OS, the CICS documentation specifically says to avoid 
ODO's as much as possible. See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dfhp3b01/1.4.1.1

which says (in part),

"Statements that produce variable-length areas, such as OCCURS DEPENDING ON, 
should be used with caution within the WORKING-STORAGE SECTION."

Obviously (and for those not familiar with CICS) there is NO "File Section" 
under CICS.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-04-16T12:44:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pug723hsvjmte3qsar6lmjnuulc61odagg@4ax.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`

```
On Sat, 14 Apr 2007 15:29:38 GMT, "Joel C. Ewing"
<jcREMOVEewing@CAPS.acm.org> wrote:

>We too have had COBOL programmers who hated to deal with variable length 
>records.  But, the marginal extra cost to manage variable length records 
>within a COBOL program can easily be insignificant when compared with 
>what is costs to pump unused bytes through the I/O subsystem over and over.

My observations are that variable length records used to be very
common, then were mostly replaced by header and detail records, which
were then mostly replaced by database calls.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-04-16T16:19:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4623A20D.6F0F.0085.0@efirstbank.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <1320k5l1kvroc05@corp.supernews.com> <58bp6cF2h1f0qU1@mid.individual.net> <Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>`

```
>>> On 4/14/2007 at 9:29 AM, in message
<Cr6Uh.21322$PL.11781@newsread4.news.pas.earthlink.net>, Joel C.
Ewing<jcREMOVEewing@CAPS.acm.org> wrote:
> Like so much in this business, it depends.
> 
…[57 more quoted lines elided]…
> significant negative impact on performance.

Here, here!  In fact I am at this moment in the midst of changing a program
from a 'static table' to a 'dynamic table' (or, perhaps more properly, a
'variable occurrence table'.  Instead of having the table 'hard coded' I am
instead reading a file to populate each occurrence of the table.  Just for
the heck of it, here's some relevant code:

 REPLACE                  
     ==:CTMAX:== BY ==20==
     .                    

**                                              
**   TOTAL TABLE BY TRANSACTION AND REJECT CAUSE
**   LEVELS 1-BRANCH  2-BANK, 3-REPORT          
**                                              
 01.                                            
     05  MSC-TOTAL-TABLE OCCURS 3 TIMES.        
         10  MSC-CHF-BEG-ACCTS       PIC 9(7).
*        [some other fields here...]
         10  MSC-CHF-CNT             PIC 9(7)                    
                                     OCCURS 1 TO :CTMAX: TIMES   
                                     DEPENDING ON MSC-CRD-TYP-CNT
                                     INDEXED BY CIDX2.           
                                                                 
 01.                                                             
     05  MSC-CM-ENTRIES              OCCURS 1 TO :CTMAX: TIMES   
                                     DEPENDING ON MSC-CRD-TYP-CNT
                                     INDEXED BY CIDX1.           
         10  MSC-CM-TYPE             PIC X.                      
         10  MSC-CM-DESCR            PIC X(20).                  
         10  MSC-CM-EXPR             PIC 9(05)    COMP-3.        
         10  MSC-CM-CARD-FEE         PIC 9(03)V99 COMP-3.        

     MOVE ZERO                   TO  MSC-CRD-TYP-CNT.       
     PERFORM X-210-READ-CTF      THRU X-210-EXIT.           
     PERFORM VARYING CIDX1 FROM 1 BY 1                      
             UNTIL MSC-CTF-EOF OR (CIDX1 > :CTMAX:)         
         ADD 1                   TO  MSC-CRD-TYP-CNT        
         MOVE CTR-TYPE-CODE      TO  MSC-CM-TYPE (CIDX1)    
         MOVE CTR-LONG-DESCR     TO  MSC-CM-DESCR (CIDX1)   
         MOVE CTR-CM-EXPR        TO  MSC-CM-EXPR (CIDX1)    
         MOVE CTR-CM-CARD-FEE    TO  MSC-CM-CARD-FEE (CIDX1)
         PERFORM X-210-READ-CTF  THRU X-210-EXIT            
         SET CIDX2 TO CIDX1
         MOVE ZERO               TO  MSC-CHF-CNT (1 CIDX2)
                                     MSC-CHF-CNT (2 CIDX2)
                                     MSC-CHF-CNT (3 CIDX2)
     END-PERFORM.                                           
     IF NOT MSC-CTF-EOF                                     
         DISPLAY 'TABLE LENGTH EXCEEDED' UPON CONSOLE       
         GO  TO  Z-900-ABORT                                
     END-IF.                                                

The one thing I don't care for is the need to code a maximum size (see
:CTMAX:).  Right now there are only six card types, and we're extending that
to eight (which is where this project came from), so I figured that 20 is a
pretty good maximum.  But it would be nice if I didn't even have to have
that particular limitation.


     SEARCH MSC-CM-ENTRIES VARYING CIDX2                 
     AT END                                              
         DISPLAY 'UNKNOWN CARD TYPE: ' CHR-CARD-TYPE     
           UPON CONSOLE                                  
         GO  TO  Z-900-ABORT                             
     WHEN CHR-CARD-TYPE = MSC-CM-TYPE (CIDX1)            
         ADD 1                   TO MSC-CHF-CNT (1 CIDX2)
     END-SEARCH.                                         

[Note: the MSC-CHF-CNT fields should probably be in the MSC-CM-ENTRIES
table, but at the time I coded this I was trying to make as few changes as
possible.  I will change this later.]

Anyway, my goal is to make most of the programs so that I do not have to
make changes when new card types are added.  Of course I'm probably spending
more time making these changes than it would to just an a few new 'table
occurrences', but hopefully it will be worth it in the end!

Frank
```

#### ↳ Re: Migrating ISAM to Relational Database

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-14T21:57:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13231o1ltuqjna5@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:589a52F2g4c1cU1@mid.individual.net...
[snip]
> This has now been posted... Accessing the following link will reveal 3
> documents that are worth reading if you are considering migrating ISAM to
…[4 more quoted lines elided]…
> Any or all feedback appreciated.

In DBnormalization.doc, page 2, under "Other
Normalization Forms", you write "Fourth normal
form, also called Boyce Codd Normal Form (BCNF),
...." is incorrect.

< http://en.wikipedia.org/wiki/Boyce-Codd_normal_form >
"Boyce-Codd normal form (or BCNF) is a normal form
used in database normalization. It is a slightly-stronger
version of third normal form (3NF). "

< http://en.wikipedia.org/wiki/Fourth_normal_form >
"4NF is the next level of normalization after Boyce-Codd
normal form (BCNF)."
```

##### ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-15T14:39:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58dhihF2g66j9U1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13231o1ltuqjna5@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[23 more quoted lines elided]…
>

4NF requires the DB to be in BCNF, with all dependencies being functional 
dependencies. I know that now... at the time I reviewed the document, it 
wasn't clear and lines between 3NF and 4NF were blurred (at least as far as 
I was concerned :-))

Thanks for the correction.

Pete.
>
>
```

##### ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-04-15T15:35:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13231o1ltuqjna5@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[25 more quoted lines elided]…
>

While you are basically correct I do not think Pete is totally wrong as some 
consider some BCNF relation to be in 4th normal form.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-04-15T14:53:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1324tbdt04l5e1e@corp.supernews.com>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com> <ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message
news:ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[6 more quoted lines elided]…
> >> documents that are worth reading if you are considering migrating ISAM
to
> >> RDB....
> >>
…[19 more quoted lines elided]…
> While you are basically correct I do not think Pete is totally wrong as
some
> consider some BCNF relation to be in 4th normal form.

I am not certain what you are getting at.

There are six normal forms: 1NF, 2NF, 3NF, BCNF,
4NF, and 5NF. Any relation that does not violate the
rules for any of these normal forms is, by default, 5NF.
This means that a relation that meets 3NF, but violates
BCNF, may, when corrected, become 5NF because
it does not violate the rules for either 4NF or 5NF.
[Some authors use "constraints" where I use "rules".]

If "some consider some BCNF relation to be in 4th
normal form", they may need to understand what 5NF
is and that they are behind the times. <g>
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-16T12:00:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58fsl0F2gl80oU1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com> <ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net> <1324tbdt04l5e1e@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1324tbdt04l5e1e@corp.supernews.com...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message
…[50 more quoted lines elided]…
>
Certainly, the details and constraints and definitions for normalization 
have moved a long way in the last few years. (The underlying relationships 
are still as defined by Codd and Date in the original papers on the 
Relational Model, but more blanks have been filled in and some useful 
amendmendments have been added. Today, it is possible to learn and 
understand the clearly defined differences between normal forms. It wasn't 
always so and  some of us (hangs head and blushes) certainly were NOT up to 
date on this aspect of the theory.) For a long time anything beyond 3NF was 
kind of a "blurred" area with different theories and ideas being proposed.

I don't think it is of great importance when migrating from ISAM to RDB. You 
can acheve this without any knowledge of normalization at all, and still 
have a normalized database, if you use the tools I provided.:-)

And there are many people who use RDB technology every day and do so 
effectively, based entirely on their empirical experience of what works, and 
without any recognition of Boyce, Codd, Date, et al.

Pete.
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 4)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-04-16T00:41:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mDzUh.721$Ut6.623@newsread1.news.pas.earthlink.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com> <ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net> <1324tbdt04l5e1e@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:1324tbdt04l5e1e@corp.supernews.com...
>
> "Charles Hottel" <chottel@earthlink.net> wrote in message
…[51 more quoted lines elided]…
>

From "An Introduction to Database Systems" 6th edition by C. J. Date pages 
290 - 291 paraphrasing:

",,, Codd's original definition of 3NF turned out to suffer from certain 
inadequacies ...A revised and stromger definition, due to Boyce and Codd, 
...stronger, in the sense that any relation that was 3NF by the new 
definition was certainly 3NF by the old, but a relation could be 3NF by the 
old definition and not by the new. The new 3NF is now usually referred to as 
Boyce/Codd normal form (BCNF) ..... Subsequently, Fagin defined a new 
"forth" normal form (4NF) because at that time BCNF was still usually called 
"third". ......As figure 10.2 shows, some BCNF relations are also in 4NF, 
and some 4NF relations are also iin 5NF."
```

###### ↳ ↳ ↳ Re: Migrating ISAM to Relational Database

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-04-16T16:55:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58gdueF2fvqk2U1@mid.individual.net>`
- **References:** `<589a52F2g4c1cU1@mid.individual.net> <13231o1ltuqjna5@corp.supernews.com> <ICrUh.1154$j63.35@newsread2.news.pas.earthlink.net> <1324tbdt04l5e1e@corp.supernews.com> <mDzUh.721$Ut6.623@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:mDzUh.721$Ut6.623@newsread1.news.pas.earthlink.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
…[69 more quoted lines elided]…
> in 4NF, and some 4NF relations are also iin 5NF."
Thanks very much for posting that, Charles. I once had an edition of that 
very book, but it has been mislaid with travelling and moving.

It certainly bears out what I said in my other post...Beyond 3NF was murky 
water (for a number of years).

Fortunately, today it is much clearer :-)

Pete.
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
