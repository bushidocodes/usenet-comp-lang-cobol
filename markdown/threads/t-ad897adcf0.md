[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Selecting common records from two files.

_18 messages · 8 participants · 2006-02_

---

### Re: Selecting common records from two files.

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-02-23T18:58:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtl0kp$ilt$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com>`

```
"ashu" (ashutosh_priyadarshi@infosys.com) writes:
> Hi,
> I have two files. I need to select those records from file 'A'
…[7 more quoted lines elided]…
> 
Didn't your instructor cover the Balance Line Algorithim?

http://www.cs.uni.edu/~east/teaching/034/fall03/class_activity/balance_line_algorithm.html

When my wife was taking COBOL course at Simon Fraser University in the early
1980s she found that she had to wait till after the deadline to recycle
them. A number of students hung around the recycling boxes to mine the code
written by students who didn't need to plagarize.
```

#### ↳ Re: Selecting common records from two files.

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-23T21:06:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ItpLf.65776$B94.52647@pd7tw3no>`
- **In-Reply-To:** `<dtl0kp$ilt$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca>`

```
Kelly Bert Manning wrote:
> "ashu" (ashutosh_priyadarshi@infosys.com) writes:

> Didn't your instructor cover the Balance Line Algorithim?
> 
> http://www.cs.uni.edu/~east/teaching/034/fall03/class_activity/balance_line_algorithm.html
> 
Sez to meself, "What's he talking about ?". Checked out your link. Just 
great ! One of the most elementary and *very useful* concepts in 
programming has a name coined for it :-)

Jimmy
```

##### ↳ ↳ Re: Selecting common records from two files.

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-02-24T04:07:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<ItpLf.65776$B94.52647@pd7tw3no>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no>`

```


James J. Gavan wrote:
> Kelly Bert Manning wrote:
> 
…[12 more quoted lines elided]…
> Jimmy

Back when I was taught this in second semester COBOL (in 1979) it was 
called "Sequential Match/Merge" or just "Match/Merge".  It is still a 
useful technique for batch processing of transactions.  It is faster 
to unload KSDS VSAM files to sequential, run match/merge, and reload 
than to perform the same updates directly to the VSAM file by key.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-02-27T04:44:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtu03i$qh5$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley (arnold.trembley@worldnet.att.net) writes:
> 
> Back when I was taught this in second semester COBOL (in 1979) it was 
…[3 more quoted lines elided]…
> than to perform the same updates directly to the VSAM file by key.

Say what? 

Did you mean direct application of unsorted updates or Skip Sequential
processing of sorted updates. I'd look for some analysis and tuning if
I got Skip Sequential VSAM performance as slow as you seem to get.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-02-27T06:22:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<dtu03i$qh5$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca>`

```


Kelly Bert Manning wrote:
> Arnold Trembley (arnold.trembley@worldnet.att.net) writes:
> 
…[11 more quoted lines elided]…
> I got Skip Sequential VSAM performance as slow as you seem to get.

Results might vary depending upon your application, but this KSDS file 
with 16 million records normally received 100,000 to 400,000 updates 
in each night's batch processing.  Besides being faster to process 
against the sequential backup of the file, the sequential file batch 
processing was easier to recover from in the event of any problems.

But I admit it's been many years since this was benchmarked, and it is 
possible that VSAM performance has improved since the late 1980's. 
The sequential process runs in less than 15 minutes and the reload 
file also serves as a backup.  It has been very fast and reliable.

During online processing this particular file is mirrored, so it is 
available for online update 24x7.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-27T10:24:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtuk0g$ghn$1@reader2.panix.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>
>
>Kelly Bert Manning wrote:
>> Arnold Trembley (arnold.trembley@worldnet.att.net) writes:
>> 

[snip]

>>>It is faster 
>>>to unload KSDS VSAM files to sequential, run match/merge, and reload 
…[16 more quoted lines elided]…
>possible that VSAM performance has improved since the late 1980's. 

Bingo... it might be, Mr Trembley, that what was true about hardware nigh 
two decades ago is no longer the case now.  Perhaps, for laffs, a set of 
benchmarks might be run to determine if this is still the case.

DD
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-02-27T09:27:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12066iekfscgnae@news.supernews.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
>> But I admit it's been many years since this was benchmarked, and it
>> is possible that VSAM performance has improved since the late 1980's.
…[4 more quoted lines elided]…
> case.

I don't think the hardware could speed up enough! As I remember ISAM/VSAM 
internals, once the cylinder overflow area fills, the IO routine has to 
chase all the records added sequentially to find a spot to dump the new 
record. That is, in the case where a huge number of records have to be added 
having similar keys, the number of I/O operations per add jumps 
astronomically.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-27T15:38:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtv6dc$7g$1@reader2.panix.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com> <12066iekfscgnae@news.supernews.com>`

```
In article <12066iekfscgnae@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>docdwarf@panix.com wrote:
>>> But I admit it's been many years since this was benchmarked, and it
…[10 more quoted lines elided]…
>record.

... and as I remember being taught CICS one should avoid INSPECT and 
STRING like the plague... but times have changed since then and every once 
in a while re-examining such stuff might be in order.

DD
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 7)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-02-28T05:04:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<du0llq$kj2$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com> <12066iekfscgnae@news.supernews.com>`

```
"HeyBub" (heybubNOSPAM@gmail.com) writes:
> docdwarf@panix.com wrote:
>>> But I admit it's been many years since this was benchmarked, and it
…[13 more quoted lines elided]…
> 
ISAM and VSAM are very different beasts, not just because ISAM is dead.

I've been told that I shouldn't mention ISAM or IEBISAM, etc. because it
dates me.
 
The guy from Seattle who taught us our VSAM for system programmers course
when we converted to Integrate Catalog Facility used a case study of a 
VSAM KSDS with several insertion hot spots. The bottom line was that Control
Area Splits occurring after %CA and %CI freespace were used up were adding
freespace exactly where it was needed to improve performance, so don't sweat.

In any case I still wonder whether the original pathological performance
problem involved a sorted input file and true SKIP SEQUENTIAL processing.

With random update you could be reading and each Data CI repeatedly,
along with Index CIs. With Skip Sequential Update you only read and write
each Data CI of interest once, bypassing ones that aren't updated. The 
metaphor for Index CI processing was a pendulum swinging through the 
Index hierarchy once, from low to High keys. Each Index CI is only retrieved
once, at most.

I saw one circa 1981 conversion from tape master files to IMS and VSAM
which was motivated by adding up the costs of sorts in the tape application
and promising that converting to Direct Update would "save" those costs.

After all, one random read or update to an IMS DB or VSAM KSDS involves
the same CPU and I/O overhead as your average read or write to a 32K
blocked Tape record, doesn't it?

The had other issues, with the PL/I analog of Occurs Depending On, but
kept sneering at the advice to sort their input. "Everybody knows" that
sorting became obsolete with VSAM and databases, so we obviously didn't
know anything about MVS I/O and performance.

After a year or so of whining about processing costs they were told to go
away and stop bothering us until they had:
   sorted their input to physical sequence of the highest I/O dataset
   replaced the PL/I analog of ODO in tables with fixed maximum lengths
   trimed their VSAM AMP allocation, since we were billing for Virtual
       storage occupancy and didn't have nearly enough memory to buffer
       entire datasets at that time. It simply cost them money to have
       CIs sit in buffers for a longer time before being reused for a
       different CI.
Note that none of this involved major changes to their processing logic.

They went away in a huff, apaprently planning to return with the proof
that we didn't know what we were talking about. We never heard from them
again about that, not even to thank us for advice which reduced their
processing costs by about $1000/day in early 1980s dollars. 
 
Processing smarter can make a huge difference in VSAM performance.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-28T07:31:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fin8021vqn5jr9o7cbbrgmhams912avica@4ax.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com> <12066iekfscgnae@news.supernews.com> <du0llq$kj2$1@theodyn.ncf.ca>`

```
On 28 Feb 2006 05:04:58 GMT, bo774@FreeNet.Carleton.CA (Kelly Bert
Manning) wrote:

>ISAM and VSAM are very different beasts, not just because ISAM is dead.

Not to mention that VSAM comes in 3 flavors, flat, relative, and
keyed.     Still they are IBM ways of doing what everybody else does
without the word VSAM.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 9)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-02-28T15:15:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<du1pfa$d1c$1@theodyn.ncf.ca>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com> <12066iekfscgnae@news.supernews.com> <du0llq$kj2$1@theodyn.ncf.ca> <fin8021vqn5jr9o7cbbrgmhams912avica@4ax.com>`

```
Howard Brazee (howard@brazee.net) writes:
> On 28 Feb 2006 05:04:58 GMT, bo774@FreeNet.Carleton.CA (Kelly Bert
> Manning) wrote:
…[4 more quoted lines elided]…
> keyed.

So you regard LINEAR datasets as a special case of ESDS with very long
records?

The discussion was about VSAM performance. I suppose dataset performance
in the non-IBM sphere is so automatically good that it never comes up for
discussion.

I worked with COBOL on HIS series 60 processors from GCOS 2H thru 4Js,
including CODASYL DB DC applications.
 
HIS GCOS had a recurring problem with not writing the last block of a tape
dataset at end of program. We had to impose a peer reviewed standard of
including code to write trailer records enough times to ensure that
a block was actually filled and written to tape.

I have a copy of a "STAR" from their tech support group in Phoenix confirming
that their analog of specifying non-default buffer numers croaked when you
tried to specify more than the default number of buffers for very large
buffer sizes.

Despite that, the console operators could always tell when my batch programs
were running, because I was the only person who could peg the "applause
meter", doing enough sequential Tape and DB I/O to keep the CPU fully 
occupied during overnight batch runs.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 6)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-02-28T06:48:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tnSMf.475292$qk4.306072@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<dtuk0g$ghn$1@reader2.panix.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <GDvLf.2325$Zw.1105@bgtnsc04-news.ops.worldnet.att.net> <dtu03i$qh5$1@theodyn.ncf.ca> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com>`

```


docdwarf@panix.com wrote:

> In article <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net>,
> Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[10 more quoted lines elided]…
> 

I certainly cannot disagree with this advice, but I'm sure you're 
aware of how difficult it can be to budget for this kind of research.

I looked at this application again, and realized this particular large 
VSAM file was converted to DB2 last year.  But it is still unloaded to 
sequential file for large batch processing updates, which primarily 
fall into two categories:

1)  Aging off records based on an expiration date, and
2)  Applying large numbers of inserts, updates, and deletes received 
from external customers as file transfers.  Of course, each external 
customer must receive a file transfer back containing only the results 
for their updates.

Obviously, when it was still a VSAM file, aging off the out of date 
records required examing every record in order to determine if it 
needed to be deleted.

Performance is very good, under five minutes for this batch process. 
The entire batch maintenance window for the online system typically 
runs in less than 75 minutes.  In the late 1980's it was 4 to 8 hours.

Given the nature of the business, the bosses won't want to spend any 
money to make it go faster when it already runs fast enough.

But you point is well taken.  If you want to know which way is faster, 
you have to test both ways.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-28T10:33:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<du18tp$ds3$1@reader2.panix.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <kUwMf.468892$qk4.302374@bgtnsc05-news.ops.worldnet.att.net> <dtuk0g$ghn$1@reader2.panix.com> <tnSMf.475292$qk4.306072@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <tnSMf.475292$qk4.306072@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>
>
…[14 more quoted lines elided]…
>aware of how difficult it can be to budget for this kind of research.

I've worked in enough organisations, Mr Trembley, to have seen the 
equivalent of something I posted over a half-decade back, aye.  From

<http://groups.google.com/group/comp.lang.cobol/msg/883f6fd335911016?dmode=source&hl=en>

--begin quoted text:

A Story:

A gang of carpenters are working on a house; the Foreman (this story is
old enough to have originated in the days when Foremen were Foremen, not
Forefolk), as is the Forman's wont, is wandering about, keeping an eye on
things.  He notices one particular carpenter laboring *mightily* with his
saw and the following dialogue ensues:

F: 'Hey, Joe... what'cha doin'?'

J: 'Sawin' these planks, Boss, just like ya tol' me to.'

F: 'Yup, that ya are... y'know, I can't really tell from this angle but it
looks, to me, like your saw's kinda dull.'

J: 'You sure got a good eye, Boss... I guess that's why you're the
Boss.  Saw sure is dull, duller'n a butterknife.'

F: 'Oh... ummmm, Joe, why don't you sharpen your saw?'

J: 'Sharpen my saw?  I'm too busy cuttin' these planks to sharpen my saw!'

EOS

Now I have told that tale many times, in many places... and many folks
have laughed and nodded while intoning 'Yup, it's *just* that way here,
too'...

... while *my* response, when I first heard it, was to think 'All
right... and now the Foreman says 'Joe, lissen'a me.  I am your
Boss... Direct Order, stop cuttin' the planks and sharpen your saw, *now*,
please?''

--end quoted text

>
>I looked at this application again, and realized this particular large 
…[12 more quoted lines elided]…
>needed to be deleted.

... as opposed to, say, a DELETE FROM TBLNAM WHERE... now *that* might be 
interesting.  How much faster/cheaper is it to do the SQL versus an unload 
to a flatfile, a SORT INCLUDE/OMIT COND, a DROP, a CREATE and a reload?

At any rate... this brings back something earlier, when folks were 
discussing what reasons might be found for treating a database as one 
would treat a VSAM file.

>
>Performance is very good, under five minutes for this batch process. 
>The entire batch maintenance window for the online system typically 
>runs in less than 75 minutes.  In the late 1980's it was 4 to 8 hours.

As mentioned someplace else... the late 1980s were twenty years ago, it 
might be that things have changed in the World of Computing enough since 
then to warrant another look.

>
>Given the nature of the business, the bosses won't want to spend any 
>money to make it go faster when it already runs fast enough.

If the results were known in advance they wouldn't call them 
'experiments'... those who do not budget for them deserve the results they 
don't get.

'I have an idea that might save some money... but it's gonna cost a few 
buck up front, first.'

'Sorry... we only want ideas that'll save money that cost nothing.'

>
>But you point is well taken.  If you want to know which way is faster, 
>you have to test both ways.

It is a good thing, at times, to address the assumptions one brings to 
bear on a task, Mr Trenbley.

DD
```

##### ↳ ↳ Re: Selecting common records from two files.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-24T07:53:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d7uv1png9fg86a8154o73ptptlfrmdrce@4ax.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no>`

```
On Thu, 23 Feb 2006 21:06:48 GMT, "James J. Gavan"
<jgavandeletethis@shaw.ca> wrote:

>> Didn't your instructor cover the Balance Line Algorithim?
>> 
…[4 more quoted lines elided]…
>programming has a name coined for it :-)

So elementary that I never really thought of it as an algorithm.
```

##### ↳ ↳ Re: Selecting common records from two files.

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-02-25T14:37:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<469qnhF9tls0U1@individual.net>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no>`

```

"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
news:ItpLf.65776$B94.52647@pd7tw3no...
> Kelly Bert Manning wrote:
>> "ashu" (ashutosh_priyadarshi@infosys.com) writes:
…[8 more quoted lines elided]…
>
When I learned it, it was called a "Three way split". I like pictures better 
than code so I've posted one here: 
http://www.enternet.co.nz/users/dashwood/3waysplit.doc


And, mindful this is a COBOL forum, here's a sample COBOL program...(Notice 
I said 'sample' not 'example'... some of the code is not exemplary :-)...)

000010 identification division.
000020 program-id.     TWSPLIT.
000030 installation.   Prima Computing.
000040 author.         Peter E. C. Dashwood.
000050 date-written.   Feb 98.
000060*
000070*remarks.
000080*
000090*    This program is an example of the use of "3 way split"
000100*    logic in COBOL.
000110*
000120*    It has been "cloned" from a real program which actually does
000130*    a 3 way split to create a database from two input files.
000140*
000150*    *******************************************************
000160 environment division.
000170 configuration section.
000180 source-computer. IBM-PC.
000190 object-computer. IBM-PC.
000200 special-names.
000210     console is CONSOLE
000220     .
000230 input-output section.
000240 file-control.
000250     select MASTER assign MASTER-path
000260                 access mode is sequential.
000270
000280     select detailz assign DETAIL-path
000290                 access mode is sequential.
000300
000310*------------------------  DATA   DIVISION  ---------------------
000320 data division.
000330 file section.
000340 fd  MASTER
000350     DATA RECORD IS CUSTREC.
000360 01  CUSTREC.
000370     12 CUSTNO    pic x(8).
000380     12 filler   pic x(248).
000390
000400 fd  DETAIL
000410     DATA RECORD IS ACCTREC.
000420 01  ACCTREC.
000430     12 ACCTNO   pic x(8).
000440     12 filler    pic x(248).
000450
000460 working-storage section.
000470
000480 01  MASTER-path pic x(50) value
000490     'h:\elle\source\mfisam01.fxd                       '.
000500
000510
000520 01  DETAIL-path pic x(50) value
000530     'h:\elle\source\mfisam02.fxd                       '.
000540
000550 01  input-path pic x(50) value spaces.
000560
000570
000580 01  control-counts usage comp value low-values.
000590      12 ws-MASTER-count      pic s9(9).
000600      12 ws-DETAIL-count      pic s9(9).
000610      12 ws-MATCH-count       pic s9(9).
000620      12 ws-UNMATCH-count     pic s9(9).
000630
000640 01  display-count            pic z(6)9.
000650
000660
000670*
000680 01  finish-flag pic x value zero.
000690     88 finished         value '1'.
000700*
000710*
000720/
000730 procedure division.
000740 main section.
000750 main-start.
000760     perform a-initialise
000770     perform b-file-processing until finished
000780     perform c-close-down
000790     stop run.
000800 main-exit.
000810     exit.
000820*-----------------------------------------------------------------
000830 a-initialise section.
000840 a-0100.
000850     display "3 WAY SPLIT is running..."
000860     .
000870 a-0150.
000880* Allow users to specify where the MASTER file is...
000890     display space
000900     display "MASTER FILE data path = " MASTER-path
000910     display space
000920     display "Input new path if desired.."
000930     accept input-path from console
000940     display space
000950     display space
000960     if input-path (1:5) NOT = space
000970        move input-path to MASTER-path
000980        move spaces     to input-path
000990        go to a-0150
001000     end-if
001010     .
001020 a-0160.
001030     display space
001040     display "DETAIL FILE data path = " DETAIL-path
001050     display space
001060     display "Input new path if desired.."
001070     accept  input-path from console
001080     display space
001090     display space
001100     if input-path (1:5) NOT = space
001110        move input-path to DETAIL-path
001120        move spaces     to input-path
001130        go to a-0160
001140     end-if
001150     open input MASTER
001160                DETAIL
001170     move zero to finish-flag
001180
001190* Do the "priming reads" [initial fetches...]
001200     perform s000-get-MASTER
001210     perform s010-get-DETAIL
001220     .
001230 a-9999.
001240     exit.
001250*-----------------------------------------------------------------
001260 b-file-processing          section.
001270 b000.
001280*
001290*   3-way-split logic....
001300*
001310*
001320     if ACCTNO < CUSTNO
001330*   detailz is low so can never match...
001340        display "unmatched detailz =" ACCTNO
001350        add 1 to ws-UNMATCH-count
001360        perform s010-get-DETAIL
001370        if finished
001380           go to b999-exit
001390        else
001400           go to b000
001410        end-if
001420     else
001430        if ACCTNO = CUSTNO
001440           display "matched detailz =" ACCTNO
001450           add 1 to ws-MATCH-count
001460*
001470* If MULTIPLE DETAILS can be processed against the same MASTER
001480* comment out the fetch on the MASTER below.
001490*
001500*
001510           perform s000-get-MASTER
001520           perform s010-get-DETAIL
001530           if finished
001540              go to b999-exit
001550           else
001560              go to b000
001570           end-if
001580        else
001590*   detailz is high so fetch master and re-compare...
001600           perform s000-get-MASTER
001610           go to b000
001620        end-if
001630     end-if
001640     .
001650 b999.
001660     exit.
001670*----------------------------------------------------------------
001680 s000-get-MASTER              section.
001690 s000.
001700     read MASTER
001710          at end
001720          move 99999999 to CUSTNO
001730     end-read
001740     if CUSTNO NOT = 99999999
001750        add 1               to ws-CUST-count
001760     end-if
001770     .
001780 s000-exit.
001790     exit.
001800*----------------------------------------------------------------
001810 s010-get-DETAIL              section.
001820 s010.
001830     read DETAIL
001840          at end
001850          set finished to true
001860     end-read
001870     if NOT finished
001880        add 1 to ws-ACCT-count
001890     end-if
001900     .
001910 s010-exit.
001920     exit.
001930*-----------------------------------------------------------------
001940 c-close-down               section.
001950 c0100.
001960
001970     close MASTER
001980           DETAIL
001990     display space
002000     display ' input record counts'
002010     move ws-MASTER-count to display-count
002020     display '    input CUSTOMER count =' display-count
002030     move ws-DETAIL-count to display-count
002040     display '    input ACCOUNT  count =' display-count
002050     display space
002060     display ' output counts'
002070     move ws-MATCH-count to display-count
002080     display '    number of matches      =' display-count
002090     move ws-UNMATCH-count to display-count
002100     display '    number of unmatched    =' display-count
002110     display space
002120     DISPLAY "Program TWSPLIT has terminated..."
002130     .
002140
002150 c0900.
002160
002170     exit.
002180*-----------  end of program  ------------------------------------

Pete.
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-02-25T02:06:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HYOLf.68789$B94.12754@pd7tw3no>`
- **In-Reply-To:** `<469qnhF9tls0U1@individual.net>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no> <469qnhF9tls0U1@individual.net>`

```
Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message 
> news:ItpLf.65776$B94.52647@pd7tw3no...
…[18 more quoted lines elided]…
> 
Yep. The phrase 'Three Way Split' rings a bell with me.
  >
> And, mindful this is a COBOL forum, here's a sample COBOL program...(Notice 
> I said 'sample' not 'example'... some of the code is not exemplary :-)...)
<snip>

You *really* are brave posting that - you know fully well what is going 
to happen now :-)

Jimmy
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

- **From:** epc8@juno.com
- **Date:** 2006-02-24T20:10:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1140840647.364004.151120@e56g2000cwe.googlegroups.com>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no> <469qnhF9tls0U1@individual.net>`

```

Pete Dashwood wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
> news:ItpLf.65776$B94.52647@pd7tw3no...
…[14 more quoted lines elided]…
>

Very nice. Your diagram cut right through it! Perhaps if the
instructors went back to calling it a "three way split" the students
would catch on more.

-- Elliot
```

###### ↳ ↳ ↳ Re: Selecting common records from two files.

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-02-26T01:50:05+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46b240F9tfm1U1@individual.net>`
- **References:** `<1140599370.807157.180590@o13g2000cwo.googlegroups.com> <dtl0kp$ilt$1@theodyn.ncf.ca> <ItpLf.65776$B94.52647@pd7tw3no> <469qnhF9tls0U1@individual.net> <1140840647.364004.151120@e56g2000cwe.googlegroups.com>`

```

<epc8@juno.com> wrote in message 
news:1140840647.364004.151120@e56g2000cwe.googlegroups.com...
>
> Pete Dashwood wrote:
…[24 more quoted lines elided]…
>
Thank you, Elliot. It's nice to know someone found it useful.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
