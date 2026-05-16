[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Performance enhancement by compiling?

_25 messages · 14 participants · 1999-12_

---

### Performance enhancement by compiling?

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<838135$s3s$1@nnrp1.deja.com>`

```
We have some programs (lots of I-O's) which run half an hour and more.

Now that I read the MF-Books about compiling and linking again, I
recognised that linked programs should run faster than GNT-format
programs. Normaly our programs run in gnt-format.

So I compiled one of those programs to gnt and after I linked the
program to a 'standalone' executable.

I used:
cob -uO progname to get the gnt program
cob -Ox progname to get the linked program

My coboptions are set to:
-C ERRLIST
-C FORM=72
-C OPTIONAL-FILE
-C ANS85=SYNTAX
-C NOALTER
-C COMP
-C WARNING=3
-C NOBOUND
-C BOUNDOPT

I use MF Cobol 4.1 on RM 200 (Siemens) running Reliant Unix 5.43 C4001.

After running both programs (one after one) as the only programs running
on those machine, I saw that the linked programs was a bit (30 secs on 8
minutes runtime at all) SLOWER.

I already replaced most compute statements thru add/subtract/divide
statements....

So my question:
How can I improve speed on programs with lots of I-O (please no hardware
tips)?

Many thanks for all hints.

Stefan Meyer, Triumph International


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<838rg1$8n8$1@aklobs.kc.net.nz>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
Stefan.Meyer@triumph-international.de wrote:
: We have some programs (lots of I-O's) which run half an hour and more.

: Now that I read the MF-Books about compiling and linking again, I
: recognised that linked programs should run faster than GNT-format
: programs. Normaly our programs run in gnt-format.

: After running both programs (one after one) as the only programs running
: on those machine, I saw that the linked programs was a bit (30 secs on 8
: minutes runtime at all) SLOWER.

: I already replaced most compute statements thru add/subtract/divide
: statements....

Changing the amount of CPU usage does not affect how fast the
disk drives operate (in general terms).  Your Unix system
should be able to tell you how much CPU time has been used
during the run.  This seems to be an insignificant part of the
run time.

You need to look first at optimising your I-O statements.  This
may require changing, for example, the ISAM Key structure, or
replacing SORTs with another alternate key.

Where there is a large file that may need to be read through to
see if processing is required on 'active' records, it may be
an advantage to create another file of 'required actions'.
That is if a flag is set in the master file (in some way) to
indicate that processing is required then have the programs
that set this flag write it to a small 'flag file' instead.
Then it is only necessary to read through the flag file,
deleting records as the processing is done, rather than
reading though the whole master file.
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
Of course there's the rule:

The fastest I-O is NO I-O.

Look real, real hard at what I-O operations that might be
removed - for example, if you've gotten a record once,
do you really need to get it again? Do you really need
a record or can you guess at what it might contain?
Instead of getting a record, would anyone care (or
notice) if you just used random numbers?

Anyway, once you find the trick that makes the biggest
difference in your application, please share it with the
group.
```

##### ↳ ↳ Re: Performance enhancement by compiling?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3858577A.9A2B7784@home.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net>`

```


Jerry P wrote:
> 
> Of course there's the rule:
…[12 more quoted lines elided]…
> group.

One of the 'tricks' I use to avoid repetitious reads, and a
ws-MyDescrips is used for each file in the routine; sorted records it's
a cinch, but most often used with random :-

01 ws-MyDescrips.
   05 ws-key	pic 9/x
   05 ws-name	pic x(xx)

	initialize ws-MyDescrips
	do some processing
        if     my-key = ws-key
	       move ws-name to .... and continue

	else   move my-key to ws-key
	       read myFile key is my-key
	         invalid key move "^%!@#$$!" to ws-name
			  move ws-name to ......and continue
	         not invalid key
                          move myrec-name to ws-name
	       End-read
	End-if

Jimmy
```

##### ↳ ↳ Re: Performance enhancement by compiling?

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83a7j8$gtg$1@nnrp1.deja.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net>`

```
In article <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net>,
  "Jerry P" <bismail@bisusa.com> wrote:
> Of course there's the rule:
>
…[7 more quoted lines elided]…
> notice) if you just used random numbers?

Yes, I think that someone would care.

As far as I know there are not so many double readings. When I debugged
the code and saw that a record has been read twice or even more, I tried
to avoid this situation (seems to be almost working).

But in some circumstances we really have to read twice.
For example:
When we try to create receipts for delivery from outstanding orders, we
have to check in which order our clients have to be delivered (Depends
on many facts, result is a big sort-file).
Further to see if an order can be delivered, we have to check:
1. How many items can't be delivered
2. The overall percentage must be greater than a client specific
delivery ability.

The first parse is a simulation if everything will be ok. And the second
parse does it.

Unfortunately, we are using C-ISAM files and not a database. So we can't
do a rollback. And of course we don't use FileShare because speed will
be up to 5 (or even more) times slower.

Question: Would reducing the length of a sort-key improve sorting?

In fact the original question was: Is it possible to increase speed by
simply choosing an optimized compile or link run???

> Anyway, once you find the trick that makes the biggest
> difference in your application, please share it with the
> group.

I do my best.

Stefan Meyer




Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VMe64.1383$q54.12613@nnrp2.rcsntx.swbell.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net> <83a7j8$gtg$1@nnrp1.deja.com>`

```
> > Of course there's the rule:
> >
…[4 more quoted lines elided]…
> When we try to create receipts for delivery from outstanding orders,
we
> have to check in which order our clients have to be delivered
(Depends
> on many facts, result is a big sort-file).

> Question: Would reducing the length of a sort-key improve sorting?
>

Which brings us to rule #2: Never sort the master file.

In your question, the length of the key - while of some import - may
not be as time consuming to sort as moving a humongous data
record attached to the field. Have you thought about the following:

Instead of:
1. SORT lots of
   SORT-RECORDS = SORT-KEY + (really big (or part of really big) data
record)
2. Process the returned SORT-RECORDS

Try:
1. SORT lots of:
   SORT-RECORD = SORT-KEY + pointer to record in data file
2. a. Return a SORT-RECORD
    b. Use record pointer in SORT-RECORD to get data
    c. Process data

For example, suppose you have 100k ISAM records whose file key is
a customer number (say 10 bytes). Each of these records is 500 bytes.
You want to sort by ZIP code. So, then, to sort the whole file you
have
SORT-RECORD
   SORT-ZIP        X(5)
   SORT-CUST   X(10).
which works out to 15 x 100k = 15 Meg sort file instead of the
500 x 100k = 50 Meg sort file you get by sorting the whole record.

Remember, it's worse than it looks. Internally, the sort routine
may have to move a record in-and-out dozens of times. The bigger
the sort file or the bigger the sort record, the more moves to
temporary storage.

I apologize for being somewhat flippant in my earlier response
(the part about making up the results), but it was possible you
worked for the government; I wasn't sure. Sorry.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 4)_

- **From:** Stefan Meyer <NospamSMeyer@Triumph-International.de>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3859EF5C.388BFF47@Triumph-International.de>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net> <83a7j8$gtg$1@nnrp1.deja.com> <VMe64.1383$q54.12613@nnrp2.rcsntx.swbell.net>`

```

Jerry P wrote:

>
> > Question: Would reducing the length of a sort-key improve sorting?
…[20 more quoted lines elided]…
>

Already done in this way. I always use a pointer to the original record
and don't move the content of a record into a sort record.

> I apologize for being somewhat flippant in my earlier response
> (the part about making up the results), but it was possible you
> worked for the government; I wasn't sure. Sorry.

Don't care. I didn't recognized <bg>. Do you have some problems with the
government??

Stefan Meyer
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

- **From:** "Michael Burgun" <Michael.Burgun@centrelink-systems.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83d3d6$kof$1@news1.cableinet.co.uk>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net> <83a7j8$gtg$1@nnrp1.deja.com>`

```
It may be a silly question but when was the last time you did a reorg of
these files by using REBUILD to reduce fragmentation?

Have you considered using compression to reduce I/O? Your CPU utilisation 
WILL
increase, but elaped time should reduce if you successfully reduce file 
size. There
is much you can do with different options in Micro Focus's External File 
Handler. 
DO NOT waste too much time looking at reducing CPU as it rarely pays off. 
You 
sometimes get savings of up to 3-4% after complete re-writes focusing on 
CPU issues,
but can normally get savings of at least 50% just looking at how data is 
retrieved. After
working for 16 years as a performance analyst, I have found that far too 
much time is
wasted on peripheral issues ... The first question I ask is: "when was the 
last database
re-org?" In 80% of cases the answer is: "Huh?"

Michael Burgun
Director
Centrelink Systems Ltd
Bristol, UK
Technical@centrelink-systems.notthis.com

>> In article <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net>,
>>   "Jerry P" <bismail@bisusa.com> wrote:
…[14 more quoted lines elided]…
>> the code and saw that a record has been read twice or even more, I 
tried
>> to avoid this situation (seems to be almost working).
>>
…[10 more quoted lines elided]…
>> The first parse is a simulation if everything will be ok. And the 
second
>> parse does it.
>>
>> Unfortunately, we are using C-ISAM files and not a database. So we 
can't
>> do a rollback. And of course we don't use FileShare because speed will
>> be up to 5 (or even more) times slower.
…[18 more quoted lines elided]…
>> Before you buy.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 4)_

- **From:** Stefan Meyer <NospamSMeyer@Triumph-International.de>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385A306B.398ABC4F@Triumph-International.de>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <cZV54.169$A24.3842@nnrp3.rcsntx.swbell.net> <83a7j8$gtg$1@nnrp1.deja.com> <83d3d6$kof$1@news1.cableinet.co.uk>`

```
Very good question: "when was the last database re-org?"

In our case: We reorg all files at least once a week using fhrebuild in all
our countries.

At the moment, we don't use compression in our files. But it's worth thinking
about...I just have to rebuild all the files using key and data compression,
change all File-Select-Copy-Files and will do a full recompile of all sources
to ensure that all progs are using the new file-descriptions.... good idea,
I'll check it out.

Michael Burgun wrote:

> It may be a silly question but when was the last time you did a reorg of
> these files by using REBUILD to reduce fragmentation?
…[24 more quoted lines elided]…
>

mailto:Stefan.Meyer@Triumph-International.de


and visit http://www.triumph-international.de
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
Stefan.Meyer@Triumph-international.de wrote in message
<838135$s3s$1@nnrp1.deja.com>...
>We have some programs (lots of I-O's) which run half an hour and more.
>
…[4 more quoted lines elided]…
>


First of all, 'hardware tips' may be what you need, as I-O is a function of
hardware; so don't rule these out 'out-of-hand'.

Other than 'reducing the number of physical I-Os' I can think of no other
way to noticeably improve the performace of an I-O bound process. The famous
American bank robber, Willie Sutton, was once asked by a reporter, "Willie,
why do you rob banks?"  Willie gave a good answer: "Because that's where
they keep the money."

You have the same situation: to steal processing time, you have to look
where the most processing time is located.

If you are processing sequentially, use blocking or caching; if the
operating system can't or won't handle that for you, you'll need to write
your own caching/blocking mechanism.  Actually re-engineering a system to
reduce I-Os is not a trivial exercise, and you may want to look at an
outside consultant.

Michael Mattias
Tal Systems
Racine WI USA
michael.mattias@gte.net
```

##### ↳ ↳ Re: Performance enhancement by compiling?

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<838i97$97j$1@nnrp1.deja.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net>`

```
In article <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net>,
  "Michael Mattias" <michael.mattias@gte.net> wrote:

> First of all, 'hardware tips' may be what you need, as I-O is a
function of
> hardware; so don't rule these out 'out-of-hand'.

Sure, but I was wondering why a linked program runs slower than a
gnt-program.

> Other than 'reducing the number of physical I-Os' I can think of no
other
> way to noticeably improve the performace of an I-O bound process. The
famous
> American bank robber, Willie Sutton, was once asked by a reporter,
"Willie,
> why do you rob banks?"  Willie gave a good answer: "Because that's
where
> they keep the money."

So I will rob some banks to get enough money <bg>.

>
> You have the same situation: to steal processing time, you have to
look
> where the most processing time is located.
>
> If you are processing sequentially, use blocking or caching; if the
> operating system can't or won't handle that for you, you'll need to
write
> your own caching/blocking mechanism.  Actually re-engineering a system
to
> reduce I-Os is not a trivial exercise, and you may want to look at an
> outside consultant.
>

There's no way to reduce the I-O processes a lot (already done).

Thanks anyway.

Stefan Meyer

> Michael Mattias
> Tal Systems
…[3 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<838rti$8n8$2@aklobs.kc.net.nz>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com>`

```
Stefan.Meyer@triumph-international.de wrote:

: There's no way to reduce the I-O processes a lot (already done).

Correction: There is no way that you can think of to ...

If, for example, you are using ISAM files then the index file
will be using a lot of I-O.  If this could be made to a 
hashed random file then it may reduce the I-O significantly.
(there may however be disadvantages in other areas).

Have you tried making the file access exclusive for these runs
instead of shared ?
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 4)_

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83a5m3$eoa$1@nnrp1.deja.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <838rti$8n8$2@aklobs.kc.net.nz>`

```
In article <838rti$8n8$2@aklobs.kc.net.nz>,
  Richard Plinston <riplin@kcbbs.gen.nz> wrote:
> Stefan.Meyer@triumph-international.de wrote:
>
> : There's no way to reduce the I-O processes a lot (already done).
>
> Correction: There is no way that you can think of to ...

So sorry, your're right!

> If, for example, you are using ISAM files then the index file
> will be using a lot of I-O.  If this could be made to a
> hashed random file then it may reduce the I-O significantly.
> (there may however be disadvantages in other areas).

..and I will have a full redesign of our application. There are about
100 progs accessing those files. And sorry, my predecessor decided to
code the I-O routines in each prog again (and again...). He was one of
those 'programers' who never heard something about using libs etc. This
is a very old code ('go to' is the most used statement) and it's hard
for me to understand or to change a program. Especially when there is no
documentation or inline comment.

We're thinking about to throw away the application and to buy a new one
which meets our requirements. But this sounds easier as it is.

> Have you tried making the file access exclusive for these runs
> instead of shared ?

When ever it is possible, the files are opened exclusive.

Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3858D53F.976E92E8@zip.com.au>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <838rti$8n8$2@aklobs.kc.net.nz> <83a5m3$eoa$1@nnrp1.deja.com>`

```
Stefan.Meyer@Triumph-international.de wrote:
> 
> ..and I will have a full redesign of our application. There are about
> 100 progs accessing those files. And sorry, my predecessor decided to
> code the I-O routines in each prog again (and again...). He was one of
> those 'programers' who never heard something about using libs etc. 

Method 1:

Take one program.  Pull the code outside the program.  Test and
implement.  As you modify other programs call your common module,
updating the common module as required.  Eventually you will have a
single source controlling IO.

Here is the extreme programming bit.  Write a separate program that
simply calls that IO modules interface and comprehensively tests every
function.  When you need to update the code to handle a slightly
different variations for another program you can prove this process
works as designed, implement new tests for the new functions.  Small
steps,  automated tests, test very often, as counter intuitive as it
sounds it is far faster.

Method 2:

Extract and optimize a single program even if it takes a setup cost
more than the saving.  Gradually implement the optimized solution into
other programs and the pay back happens.

Summary:

Think in terms of years not minutes.  Work to a desired goal.  Kent
beck documents that one rewrite he did took 9 years to complete. 
There was a lot of waiting opportunity and inspiration however.

Finally:

Some advice get statistics as you go.  Gradual improvement is not as
impressive as statistically proven figures showing a 20% runtime
improvement over 12 months.

You also asked:
> Question: Would reducing the length of a sort-key improve sorting?

Yes:  Indexing (should/does) really on caching it's own information. 
If you reduce the size of the key you increase the likelihood of that
key being in memory.  Also ISAM generally works on a page basis. 
These pages for VSAM MVS are 4K and possibly similar in you system. 
If you reduce the size of the key, and there data record you increase
the chance that the particular page you are after is already in
memory.

On a large file this increase in chance might be minuscule.

Off beat:  Have you considered splitting the files up.  Recording part
of the record that is regularly read will be faster because you are
loading less data.  May or may not work....  Definitely will increase
DASD usage.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3859028E.AB4F5C25@NOSPAMwebaccess.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <838rti$8n8$2@aklobs.kc.net.nz> <83a5m3$eoa$1@nnrp1.deja.com> <3858D53F.976E92E8@zip.com.au>`

```
Ken Foskey wrote:
> 
> Off beat:  Have you considered splitting the files up.  Recording part
…[3 more quoted lines elided]…
> 

I remember sorting a large file into a half dozen tape drives, then
merging the tape files together into one.  Nowadays we don't HAVE a half
dozen tape drives, but have plenty of temporary work DASD, so we don't
need them.

Still the sort/merge concept is one which newcomers should be more aware
of.  An external sort can be very efficient, and match-merge programs
minimize I-O.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38589F0C.FAF9CB07@worldnet.att.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com>`

```
Stefan.Meyer@Triumph-international.de wrote:
> 
(snip)
> >
> 
> There's no way to reduce the I-O processes a lot (already done).

Does your configuration permit loading the index into memory? Big
potential saving here. On an IBM mainframe this would probably mean
using LSR & genning a big pool (a huge one above the 16MB line, if
possible)

Bill Lynch
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 4)_

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83an30$r0u$1@nnrp1.deja.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <38589F0C.FAF9CB07@worldnet.att.net>`

```
In article <38589F0C.FAF9CB07@worldnet.att.net>,
  wblynch@worldnet.att.net wrote:
> Does your configuration permit loading the index into memory? Big
> potential saving here. On an IBM mainframe this would probably mean
> using LSR & genning a big pool (a huge one above the 16MB line, if
> possible)

Oh, please help. How can I load the index into memory in a fast way? And
how to work with the index in memory?

On the other hand I'm working on data files up to 1 GB of size...

Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3858FFAA.6C6BD862@NOSPAMwebaccess.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <38589F0C.FAF9CB07@worldnet.att.net> <83an30$r0u$1@nnrp1.deja.com>`

```
What makes a file access method efficient when paging is involved is not
necessarily the same as making a file access method efficient when the
whole thing is in memory.

I imagine that's why SEARCH ALL doesn't specify a binary search.  For a
small table, it could be more efficient to do a serial search than to
stop and calculate pointers.

Normally, you calculate I-O's for your critical tasks, I-O's for other
tasks, and then everything else later.  With everything in memory, there
are no I-O's.  

It could be that making the file smaller (by eliminating an index) can
make it fit into memory, with an advantage which is greater than the
loss of the index!!

Relative addressing often requires one I-O to read record 1 to get the
pointer to the next available record (or it also can use chaining), and
then another I-O to get to the record.  This is used when you can't lock
up the file in a multi-user environment.  But what if you can create a
virtual record 1 available for everybody (with periodic background
updating of the file)?

Many operating systems and database management systems are doing stuff
like this transparently to the user.  If it guesses correctly, our
access can be MORE efficient once it moves to production and the
environment decides that it is being used enough to keep it available.
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3859A329.9EEA2188@worldnet.att.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <38589F0C.FAF9CB07@worldnet.att.net> <83an30$r0u$1@nnrp1.deja.com>`

```
Stefan.Meyer@Triumph-international.de wrote:
> 
> In article <38589F0C.FAF9CB07@worldnet.att.net>,
…[7 more quoted lines elided]…
> how to work with the index in memory?

You don't know it's in memory, once it's there references to the index
don't cause any I/O. How you get it into memory depends on your
platform. The for instance I gave above is how you could do it in MVS.

> On the other hand I'm working on data files up to 1 GB of size...

Yes, but how big is the index? Again in MVS, there's also the
possibility of loading your file into memory (yes, the whole thing). An
MVS address space is 2 GB. If that's not enough you can acquire a Data
Space, which is a separate address space for data, only, i.e., you can't
execute code there.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Performance enhancement by compiling?

_(reply depth: 4)_

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83amvb$qot$1@nnrp1.deja.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <4QO54.234$CW3.6417@dfiatx1-snr1.gtei.net> <838i97$97j$1@nnrp1.deja.com> <38589F0C.FAF9CB07@worldnet.att.net>`

```
In article <38589F0C.FAF9CB07@worldnet.att.net>,
  wblynch@worldnet.att.net wrote:
> Does your configuration permit loading the index into memory? Big
> potential saving here. On an IBM mainframe this would probably mean
> using LSR & genning a big pool (a huge one above the 16MB line, if
> possible)

Oh, please help. How can I load the index into memory in a fast way? And
how to work with the index in memory?

On the other hand I'm working on data files up to 1 GB of size...

Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38583f77.94249013@news1.attglobal.net>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
On Wed, 15 Dec 1999 12:20:55 GMT,
Stefan.Meyer@Triumph-international.de wrote:

>We have some programs (lots of I-O's) which run half an hour and more.
>
…[3 more quoted lines elided]…
>

I was never able to get a MF program (16 bit) to run faster than in
GNT format.  Most times GNT and EXE were the same or the GNT was
slightly faster.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Performance enhancement by compiling?

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83a4pv$o1c$2@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <38583f77.94249013@news1.attglobal.net>`

```
    The runtime needed for GNT may handle memory management slightly better
than the EXE runtime.

    Also check the cobol operations manual.  Some version of MF have options
that can increase IO speed, by
increasing the size of buffer the runtime uses.  But the best first bet is
to open exclusive.  Also try to avoid
networks if possible.


Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:38583f77.94249013@news1.attglobal.net...
> On Wed, 15 Dec 1999 12:20:55 GMT,
> Stefan.Meyer@Triumph-international.de wrote:
…[13 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** "Jordaens Robert" <icare@wanadoo.be>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83bl9v$1e74$1@buty.wanadoo.nl>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
use record sequential files
do not use dynamic subroutine calls
compile with as .obj and link


<Stefan.Meyer@Triumph-international.de> schreef in berichtnieuws
838135$s3s$1@nnrp1.deja.com...
> We have some programs (lots of I-O's) which run half an hour and more.
>
…[41 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Performance enhancement by compiling?

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83brol$2ck$1@news.inet.tele.dk>`
- **References:** `<838135$s3s$1@nnrp1.deja.com>`

```
I have looked at the thread and I wonder what kind of operation we are
trying to optimize.

What do you mean with "lots of I-O's"? I am trying to se the picture of what
your programs are doing. I would like at short description like: "we read
file1 and update file2, file3, file4 and file5. File1 is sequential, file2
is indexed with 32 alternat keys.........". I think you get the idea.

I read somewhere, that you by debugging found, that you accessed the same
record more than once, but you were about to fix that problem.

Do you have a statement like this: "write something invalid key rewrite
something". Now what is the most common result of that statement? rewrite?
If so, change to: "rewrite something invalid key write something".

You have said, that files cannot be changed (files are used by many
programs), bu you can evaluate every write or rewrite in the 2 programs in
question.

I will save my breath until you give a short description of the I-O model
for the programs, then i think I might have some ideas.

Regards
Ib


Stefan.Meyer@Triumph-international.de skrev i meddelelsen
<838135$s3s$1@nnrp1.deja.com>...
>We have some programs (lots of I-O's) which run half an hour and more.
>
…[41 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Performance enhancement by compiling?

- **From:** Stefan Meyer <NospamSMeyer@Triumph-International.de>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3859F57A.DBF0B11D@Triumph-International.de>`
- **References:** `<838135$s3s$1@nnrp1.deja.com> <83brol$2ck$1@news.inet.tele.dk>`

```
> I have looked at the thread and I wonder what kind of operation we are
> trying to optimize.
>

The original intended question was: Is it possible to get a better performance
using the best compile/link method?
That's all. In the meantime, some people asked me, what w're doing and of course
how. So I tried to answer and gave some examples.

>
> What do you mean with "lots of I-O's"? I am trying to se the picture of what
…[3 more quoted lines elided]…
>

There are a few programs working like:

- Read the program master file (depends on the program)
- If a record should be processed, read all depended records from detail file
- Sort them (by using key-references to the original record)
- Process the sorted records and write them into a third and fourth table,
completing the new record with datas from different other tables (some records
from the master/detail files will be merged into one new master/detail
relation). By the way mark records in Master and Detail files as processed.

This is a short description of what is done. I think lots of programs are
working in that way...

All files are indexed, some of them have a few (not 32) alternate keys with
duplicates.

>
> I read somewhere, that you by debugging found, that you accessed the same
…[5 more quoted lines elided]…
>

No, when updating a file, I always know, if a record has to be written or
rewritten.


>
> You have said, that files cannot be changed (files are used by many
> programs), bu you can evaluate every write or rewrite in the 2 programs in
> question.
>

Sorry for missunderstanding. I didn't say that files can't be changed.

>
> I will save my breath until you give a short description of the I-O model
> for the programs, then i think I might have some ideas.
>
>

Nice, but I really only wanted to know....see original question.

Regards,
Stefan Meyer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
