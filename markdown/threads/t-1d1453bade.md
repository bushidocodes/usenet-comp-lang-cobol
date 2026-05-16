[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In praise of compiler writers

_8 messages · 4 participants · 2010-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### In praise of compiler writers

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-04-13T06:53:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com>`

```
After getting some complaints from our users about the seeming inefficiency 
of a particular process, I had a look at the code.

The programmer who wrote the code used an internal bubble sort to rearrange 
the data and find duplicates. Some 3,000 entries consumed as much as two 
minutes of clock time.

"Screw this," I cried. I ripped out the couple hundred lines of code 
involved and replaced it with a simple ISAM file which summed the duplicates 
into a single entry.

The process went from the aforementioned two minutes to FOUR SECONDS !

I considered replacing the ISAM stuff with the SORT verb, but I'm not a 
fanatic about micro-efficiency.
```

#### ↳ Re: In praise of compiler writers

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-04-14T00:06:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<82j525Fva8U1@mid.individual.net>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com>`

```
HeyBub wrote:
> After getting some complaints from our users about the seeming
> inefficiency of a particular process, I had a look at the code.
…[12 more quoted lines elided]…
> a fanatic about micro-efficiency.

Good stuff, Jerry!

It is a bit ironic that in this last week I too used an ISAM file as paged 
storage for an internal process. The pages needed to be 8K and SQL Server 
doesn't like columns that big... I also wanted the software to be 
independent of the RDB so ISAM looked pretty obvious. Fortunately the pages 
are completely dynamic, created as needed, deleted when their usefulness is 
over, accessed randomly, and the file gets recreated every day as part of 
start-up housekeeping, so issues of maintenance don't arise.  It made me 
smile because the whole thing is a data base application but without this 
ISAM file it wouldn't work.:-)

They still have their uses.

Pete
```

##### ↳ ↳ Re: In praise of compiler writers

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-04-13T16:30:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<meudnc1hzcUOf1nWnZ2dnUVZ_sSdnZ2d@earthlink.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com> <82j525Fva8U1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> After getting some complaints from our users about the seeming
…[27 more quoted lines elided]…
>

Had my technique not worked, I was going to send all the shit to an 
invisible ListView box, sort by the column I wanted, then read it all back. 
I bet that would be STILL faster than a hand-coded sort (of almost any 
type).

As for temp files, they go in the system temporary folder and all our 
routines delete everything of the form NSxxxxxx.TMP just before exiting. 
We're almost anal about neatness.
```

##### ↳ ↳ Re: In praise of compiler writers

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-04-15T07:18:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RKSdnZPFbNiOmVrWnZ2dnUVZ_hadnZ2d@earthlink.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com> <82j525Fva8U1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> After getting some complaints from our users about the seeming
…[27 more quoted lines elided]…
>

Yep. And as far as "shop standards" are concerned, I'd wager that all my 
processing was done without ever writing anything to the disk - that is, it 
was all done at RAM speed in internal buffers.

Maybe we could use a "CLOSE WITH DELETE" verb - the file (if any) is deleted 
automatically when you're done with it.

As an aside, I was amazed some time back to discover that an ISAM file was 
half the size of the oringingal text file. In spite of additional records 
governing pointers and overflow areas and the like, the file system 
compressed out multiple blanks before committing the data to the disk. 
Inasmuch as this was a text file, with oodles of blanks, the saving was, 
obviously, significant.
```

#### ↳ Re: In praise of compiler writers

- **From:** docdwarf@panix.com ()
- **Date:** 2010-04-13T12:11:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hq1n1g$hrr$1@reader1.panix.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com>`

```
In article <XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>After getting some complaints from our users about the seeming inefficiency 
>of a particular process, I had a look at the code.
…[3 more quoted lines elided]…
>minutes of clock time.

Hmmmm... this sounds like it could have any one of a variety of causes, 
including (but not limited to) 'Look, Ma, I'm a Programmer!' code to 'Oh, 
there'll *never* be more than a couple of those' to 'Yes, you can do that 
in an external SORT step... but (Corner-Office Idiot) doesn't like 
external SORTs so you'll have to code it inline'.

>"Screw this," I cried. I ripped out the couple hundred lines of code 
>involved and replaced it with a simple ISAM file which summed the duplicates 
…[5 more quoted lines elided]…
>fanatic about micro-efficiency. 

I'd say you are fortunate to be working in a shop where such techniques 
are permitted... our experiences, of course, might be different but I have 
worked in places where adding another file to a program required so much 
Committee Overview (a holdover, most likely, from the Dayse of Punch-cards 
and mechanical collators) that the consensus was 'just don't do it, find 
another way...

... have you thought about internally coding a bubble sort?'

(I have some fairly recent code (written seven years ago, last 
compiled five years ago) running in Production using a comb sort routine 
provided by Mr Moseley, similar to that found in 
<http://www.jaymoseley.com/hercules/download/misc/combsort.tgz> )

DD
```

##### ↳ ↳ Re: In praise of compiler writers

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-04-13T07:17:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jr8s5h5758kq1mi63242n83s0i7ehjlqs@4ax.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com> <hq1n1g$hrr$1@reader1.panix.com>`

```
On Tue, 13 Apr 2010 12:11:28 +0000 (UTC), docdwarf@panix.com () wrote:

>... have you thought about internally coding a bubble sort?'
>
…[3 more quoted lines elided]…
><http://www.jaymoseley.com/hercules/download/misc/combsort.tgz> )

I have coded internal comb sorts, because my version of CoBOL doesn't
do table sorts.    It's not very complicated (and structured
programming makes it so that maintenance programmers don't really need
to look at those paragraphs), and it's quick.    That said, if I had a
table sort, I would have used it.
```

###### ↳ ↳ ↳ Re: In praise of compiler writers

- **From:** docdwarf@panix.com ()
- **Date:** 2010-04-13T14:14:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hq1u7d$ar8$1@reader1.panix.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com> <hq1n1g$hrr$1@reader1.panix.com> <9jr8s5h5758kq1mi63242n83s0i7ehjlqs@4ax.com>`

```
In article <9jr8s5h5758kq1mi63242n83s0i7ehjlqs@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 13 Apr 2010 12:11:28 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[11 more quoted lines elided]…
>table sort, I would have used it.

In the words of the Oldene Dayse, Mr Brazee, 'If my Grannie had wheels 
she'd be a trolley-car'.  Even as recently as '03 the IGYCRCTL compiler 
(to the best of my knowledge) did not support table sorts... I seem to 
recall that the version of Microfocus I worked with (1.8.something?) did.

DD
```

###### ↳ ↳ ↳ Re: In praise of compiler writers

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-04-13T09:42:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r049s5dhkj2n7coo6mnf4o50npgt7q68qq@4ax.com>`
- **References:** `<XcadnUpx6KmgxlnWnZ2dnUVZ_uSdnZ2d@earthlink.com> <hq1n1g$hrr$1@reader1.panix.com> <9jr8s5h5758kq1mi63242n83s0i7ehjlqs@4ax.com> <hq1u7d$ar8$1@reader1.panix.com>`

```
On Tue, 13 Apr 2010 14:14:06 +0000 (UTC), docdwarf@panix.com () wrote:

>>I have coded internal comb sorts, because my version of CoBOL doesn't
>>do table sorts.    It's not very complicated (and structured
…[7 more quoted lines elided]…
>recall that the version of Microfocus I worked with (1.8.something?) did.

Also, back in the day, if you needed a sorted table, you read a sorted
table.   And often with SQL, we can still do that.   But in my case, I
had to do a some database walking to build the table that I wanted
sorted.    It's a nice feature, but CoBOL changes come slowly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
