[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Destroying a COBOL array

_60 messages · 26 participants · 2000-03 → 2000-04_

---

### Destroying a COBOL array

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
Hi:

Here's my issue.  I am reading records from a flat file into a variable
length array.  Let's assume this input data:

Name          Order #
---------        -------------
smith, j         1
smith, j          2
smith, j         3
jones, p       1
jones, p       2

...etc

The input file will contain tens of thousands of records (perhaps hundreds
of thousands +), so what I really would like to do is read in all of the
data for a customer (i.e. J. Smith) into a variable length array, then
destroy the array after I'm done processing him, and move on to P. Jones.

In C/C++ this is done with the DELETE command.  After you've created an
array on the heap, you can resize or destroy the array easily, and start a
new one.

I don't want to read in the whole file into one array because it would be a
HUGE array, and the performance would probably be poor.

Is there a way to destroy an array in COBOL once it's been created, this
freeing the memory allotted to it?

I have tried to keep my example simple, so if you need more information I
can elaborate.

-ck
```

#### ↳ Re: Destroying a COBOL array

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8buohg$drp$1@nntp9.atl.mindspring.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
Does the table include an OCCURS DEPENDING ON - or just an OCCURS n TIMES?

If it is the latter, try using the INITIALIZE statement on the table.

Alternatively,  just store the "highest" used value and reset it to zero
before starting a new person.  Then "cover up" the elements as you read in
the new ones - and ignore any left over items (from the last customer)

This isn't the clearest description that I have ever written, but I think is
what you want.
```

##### ↳ ↳ Re: Destroying a COBOL array

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<exFNYVim$GA.156@cpmsnbbsa05>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net>`

```
Bill's recommendation is right on target.  This easiest way to use a table
over and over again is to simply resest the array's index or subscript to 1,
then start loading it from them file, remembering how many you load in on
this particular load operation, and never going beyond that "max" point in
the array (if you do, you'll wind up dealing with a previous person's
information).


"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:8buohg$drp$1@nntp9.atl.mindspring.net...
> Does the table include an OCCURS DEPENDING ON - or just an OCCURS n TIMES?
>
…[6 more quoted lines elided]…
> This isn't the clearest description that I have ever written, but I think
is
> what you want.
>
…[20 more quoted lines elided]…
> > The input file will contain tens of thousands of records (perhaps
hundreds
> > of thousands +), so what I really would like to do is read in all of the
> > data for a customer (i.e. J. Smith) into a variable length array, then
> > destroy the array after I'm done processing him, and move on to P.
Jones.
> >
> > In C/C++ this is done with the DELETE command.  After you've created an
> > array on the heap, you can resize or destroy the array easily, and start
a
> > new one.
> >
> > I don't want to read in the whole file into one array because it would
be a
> > HUGE array, and the performance would probably be poor.
> >
…[3 more quoted lines elided]…
> > I have tried to keep my example simple, so if you need more information
I
> > can elaborate.
> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05>`

```
The problem is, if I use INITIALIZE or reset the subscript to 0, I haven't
really destroyed the array.

I would like to physically destroy the array, not simply empty the array's
contents.

Is this possible?

Thanks!

"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message
news:exFNYVim$GA.156@cpmsnbbsa05...
> Bill's recommendation is right on target.  This easiest way to use a table
> over and over again is to simply resest the array's index or subscript to
1,
> then start loading it from them file, remembering how many you load in on
> this particular load operation, and never going beyond that "max" point in
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 4)_

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E39A38.A885E400@boeing.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`

```
"Cosmic Knight >removethis<" wrote:
> 
> The problem is, if I use INITIALIZE or reset the subscript to 0, I haven't
…[4 more quoted lines elided]…
> 
I reuse tables frequently (load until a key field changes), when I move
spaces to the table area anything that was in it is certainly destroyed
from the programs viewpoint. (I also rest the hold fields (if used) and
reset the current table count to 1).

perhaps I am missing something?

	Susan A
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 5)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xiSE4.11522$Y4.200370@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <38E39A38.A885E400@boeing.com>`

```
Yes, you are not destroying the array, it is now filled with spaces and is
using the same amount of memory.  You are destroying the contents of the
array. I need to destroy the array itself, thus freeing it's allocated
resources.

"Susan Allen" <susan.a.allen@boeing.com> wrote in message
news:38E39A38.A885E400@boeing.com...
> "Cosmic Knight >removethis<" wrote:
> >
> > The problem is, if I use INITIALIZE or reset the subscript to 0, I
haven't
> > really destroyed the array.
> >
> > I would like to physically destroy the array, not simply empty the
array's
> > contents.
> >
…[7 more quoted lines elided]…
> Susan A
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_TUE4.15759$0o4.91258@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <38E39A38.A885E400@boeing.com> <xiSE4.11522$Y4.200370@news1.rdc1.il.home.com>`

```
In article <xiSE4.11522$Y4.200370@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:
>Yes, you are not destroying the array, it is now filled with spaces and is
>using the same amount of memory.  You are destroying the contents of the
>array. I need to destroy the array itself, thus freeing it's allocated
>resources.

That's odd... in the posting quoted by Ms Allen you state 'I would like to
physically destroy the array' and now you state 'I *need* (emphasis
added) to destroy the array itself'.

Might I ask what has changed the situation so?

DD

>
>"Susan Allen" <susan.a.allen@boeing.com> wrote in message
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 7)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pqWE4.12032$Y4.225437@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <38E39A38.A885E400@boeing.com> <xiSE4.11522$Y4.200370@news1.rdc1.il.home.com> <_TUE4.15759$0o4.91258@iad-read.news.verio.net>`

```
Hmmm.  I don't understand your question.  The situation has not changed. I
am merely distinguishing the difference between erasing an array's contents,
and destroying the array itself (physically destroying the array), which are
not the same thing.

<docdwarf@clark.net> wrote in message
news:_TUE4.15759$0o4.91258@iad-read.news.verio.net...
> In article <xiSE4.11522$Y4.200370@news1.rdc1.il.home.com>,
> Cosmic Knight <cosmicknight> wrote:
> >Yes, you are not destroying the array, it is now filled with spaces and
is
> >using the same amount of memory.  You are destroying the contents of the
> >array. I need to destroy the array itself, thus freeing it's allocated
…[15 more quoted lines elided]…
> >> > The problem is, if I use INITIALIZE or reset the subscript to 0, I
haven't
> >> > really destroyed the array.
> >> >
> >> > I would like to physically destroy the array, not simply empty the
array's
> >> > contents.
> >> >
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ly%E4.15805$0o4.92535@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <xiSE4.11522$Y4.200370@news1.rdc1.il.home.com> <_TUE4.15759$0o4.91258@iad-read.news.verio.net> <pqWE4.12032$Y4.225437@news1.rdc1.il.home.com>`

```
In article <pqWE4.12032$Y4.225437@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:
>Hmmm.  I don't understand your question.  The situation has not changed. I
>am merely distinguishing the difference between erasing an array's contents,
>and destroying the array itself (physically destroying the array), which are
>not the same thing.

Yes, but at one time you state it as a matter of desire ('I would like
to') and at another time you state it as a matter of necessity ('I need
to')

Wanting to do something a certain way is fine and dandy, sure, but it
comes down to a matter of humpin' code to get a job done... hence my query
into the difference between wants and needs.  If what exists is a matter
of mere desire then that should not get in the way of completing an
assignment before deadline.

DD

>
><docdwarf@clark.net> wrote in message
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c0d1i$ap7$1@slb7.atl.mindspring.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`

```
I vote with those who are asking WHY you care about storage allocation (from
a program perspective).  I do like the fact that the next COBOL Standard will
allow you to "manually" manipulate storage *IF* you have a really good reason
to do so.  However, (IMHO) this just isn't one.

How many transactions is the maximum number that any single person will ever
have?  If you take that number - multiply by two (to allow for what is never
SUPPOSED to happen) - and then include an error routine for the case that you
ever get even more than that - I just can't believe that your table will take
too much storage for any of the "normal" operating systems where COBOL runs.

Having said that, if you really have some reason that you want to incur  the
OVERHEAD of doing manual storage allocation and freeing, then do tell us
which compiler and operating system you are using, and we can tell you how
(in a NON-portable way) it can be accomplished (if at all).

Note: to the person who thought that their COBOL system was doing "freeing"
when they changed the value of the "object of the OCCURS DEPENDING ON".  It
is ABSOLUTELY true that you cannot access the elements (legally) that occur
after the current setting of your ODO.  HOWEVER, it is also equally true that
the Standard requires that COBOL get the "storage" required for the largest
number of elements - and to keep it thru the entire life of the program.
(This assumes working-storage; there are SLIGHTLY different rules about
linkage section.)
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 5)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kwSE4.11533$Y4.208763@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net>`

```
The amount of input data will vary wildly, but as an example, let's say
there are 200,000 records in a file.

Each record is 2000 chars in length.

So, to suck this whole file into an array would require 400,000,000 bytes.

This is a lot, even for a mainframe.  Perhaps you guys disagree.

Bill, you mentioned the extra overhead involved in dynamically assigning
memory.  You are, of course, correct, but I thik the overhead incurred here
will be negligable when compared to the gains received by not pulling this
huge array into memory. (virtual, or otherwise)

I am trying to figure out exactly which compiler we are running, but I am
pretty sure it is the COB390 compiler, which if I am not mistaken will allow
dynamic allocation of "heaps" via some utilities. These "heaps" are
connected via pointers, much like a link-list.  (This is an AMDAHL MF,
OS390/MVS)

This is as far as I have gotten.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c11fo$hs0$1@news.igs.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com>`

```
There is no need to pull the whole thing into an array, *NOR* is there a
need to dynamically allocate/deallocate.  You can have a fixed array that is
only as big as the most common record.  You seem to have this fixation that
dynamically allocating/deallocating will lessen the  array size.  All it
does is free memory up sooner, no matter what algorithm you use. If you need
400,000,000 bytes, then dynamically allocating it is not going to make it
smaller.  BTW, the smallest *micro* I have is 128,000,000 bytes, and it is a
virtual machine.  400 megs might have been a lot a few years back, but not
any more.

Cosmic Knight >removethis <<@home.com> wrote in message ...
>The amount of input data will vary wildly, but as an example, let's say
>there are 200,000 records in a file.
…[10 more quoted lines elided]…
>huge array into memory. (virtual, or otherwise)

What gains?   You will gain not a single byte, nor a single read statement.
You can use the same static memory over and over again, and gain all that
time you would waste on allocation and delallocation.

>
>I am trying to figure out exactly which compiler we are running, but I am
>pretty sure it is the COB390 compiler, which if I am not mistaken will
allow
>dynamic allocation of "heaps" via some utilities. These "heaps" are
>connected via pointers, much like a link-list.  (This is an AMDAHL MF,
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 7)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net>`

```
My point is, I don't need 400 megs if I can dynamically allocate what I need
for each group of records that need to be processed together from the input
file. (see original post)

Unless I can dynamically assign memory at run time, I am stuck bringing the
whole file into memory, which is what I am trying to avoid.  You are correct
in that if I had no choice but to pull the whole file into memory, whether
the 400 megs was assigned dynamically or not would make no difference.
After all, 400 megs is 400 megs.

I will try to answer several questions here in this post, without typing in
too many details.

Consider this input:

Name          Order #
---------        -------------
smith, j         1
smith, j          2
smith, j         3
jones, p       1
jones, p       2


Without going into the long list of details as to why this needs to be an
array, let's just say I need to process J. Smith in such a way that will
require me to move back and forth between orders 1, 2, and three many times
before I write the output record.  The array needs to be of a variable
length because I have no way of knowing how many orders J. Smith will have
in the file.  It could be two, or 20, etc.  Now that I've thoroughly
confused you... :-)

Ok, so now I am done with Smith and I can move onto Jones.  For efficiency,
I would like to allocate enough memory to handle Smith, destroy it, then
move on and do the same thing for Jones.  If I can't assign this storage
dynamically, I will have to read the whole file into an array to work with
it.  This file could be enormous.  I used 400 megs before, it could be less,
it could be significantly more.  The size of the file is undeterminable.

This leads me to my quandary, and my post here.  I cannot process the file
sequentially, I need to process each "set" (smith, jones) and move on to the
next set.  Within the set, I need to move back and forth between elements in
the set. (orders)

I hope this helps you guys understand my situation better.  If you need more
detail, I can provide it.

Thanks for all of your comments thus far.

"donald tees" <donald@willmack.com> wrote in message
news:8c11fo$hs0$1@news.igs.net...
> There is no need to pull the whole thing into an array, *NOR* is there a
> need to dynamically allocate/deallocate.  You can have a fixed array that
is
> only as big as the most common record.  You seem to have this fixation
that
> dynamically allocating/deallocating will lessen the  array size.  All it
> does is free memory up sooner, no matter what algorithm you use. If you
need
> 400,000,000 bytes, then dynamically allocating it is not going to make it
> smaller.  BTW, the smallest *micro* I have is 128,000,000 bytes, and it is
a
> virtual machine.  400 megs might have been a lot a few years back, but not
> any more.
…[7 more quoted lines elided]…
> >So, to suck this whole file into an array would require 400,000,000
bytes.
> >
> >This is a lot, even for a mainframe.  Perhaps you guys disagree.
> >
> >Bill, you mentioned the extra overhead involved in dynamically assigning
> >memory.  You are, of course, correct, but I thik the overhead incurred
here
> >will be negligable when compared to the gains received by not pulling
this
> >huge array into memory. (virtual, or otherwise)
>
> What gains?   You will gain not a single byte, nor a single read
statement.
> You can use the same static memory over and over again, and gain all that
> time you would waste on allocation and delallocation.
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PC%E4.15806$0o4.92509@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`

```
In article <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:
>My point is, I don't need 400 megs if I can dynamically allocate what I need
>for each group of records that need to be processed together from the input
…[45 more quoted lines elided]…
>Thanks for all of your comments thus far.

Now *this* makes a bit more sense... in simple flatfile terms - 

SORT the 'driver' file into 'name' name/order# sequence.

SORT the 'lookup' file into name/order# sequence.

Get a record from the driver based on name.

Load your table from the lookup file.

Process your driver recs until name-changes.

Clean the table and start on the next.

No need to 'destroy' anything and you load from the lookup only such data
as you'll need for processing.

DD

>
>"donald tees" <donald@willmack.com> wrote in message
…[54 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c26bl$8o6$1@news.igs.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`

```

Cosmic Knight >removethis <<@home.com> wrote in message
<9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>...
>My point is, I don't need 400 megs if I can dynamically allocate what I
need
>for each group of records that need to be processed together from the input
>file. (see original post)
>
>Unless I can dynamically assign memory at run time, I am stuck bringing the
>whole file into memory, which is what I am trying to avoid.  You are
correct
>in that if I had no choice but to pull the whole file into memory, whether
>the 400 megs was assigned dynamically or not would make no difference.
…[26 more quoted lines elided]…
>move on and do the same thing for Jones.  If I can't assign this storage

This is where I get *real* confused. Why do you have to "destroy it then do
the same thing for Jones"?  Why not leave it just exactly as it is, and
*RE-USE* the *SAME* memory for Jones?  I see absolutely no reason whatsoever
to get rid of it, then getting it back again for the next person.  I can see
a whole lot of overhead/potential error.


>dynamically, I will have to read the whole file into an array to work with
>it.  This file could be enormous.  I used 400 megs before, it could be
less,
>it could be significantly more.  The size of the file is undeterminable.
>
>This leads me to my quandary, and my post here.  I cannot process the file
>sequentially, I need to process each "set" (smith, jones) and move on to
the
>next set.  Within the set, I need to move back and forth between elements
in
>the set. (orders)
>
>I hope this helps you guys understand my situation better.  If you need
more
>detail, I can provide it.
>
…[13 more quoted lines elided]…
>> smaller.  BTW, the smallest *micro* I have is 128,000,000 bytes, and it
is
>a
>> virtual machine.  400 megs might have been a lot a few years back, but
not
>> any more.
>>
…[24 more quoted lines elided]…
>> >I am trying to figure out exactly which compiler we are running, but I
am
>> >pretty sure it is the COB390 compiler, which if I am not mistaken will
>> allow
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 9)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net>`

```
In reply to most of the above posts:

I cann't re-use the memory I used to process Smith because there may not be
enough of it.

If I dynamically assign the memory at run time for Smith, usising
OCCURS....DEPENDING ON I will get enough memory for Smith (3 array/table
elements) which may not be enough for Jones.  In my example Jones has 2
elements, but he could have 5, or 50 and I would get a range error.
Therefore, I can't reuse the same memory because I have no idea how much I
will need to porcess the next customer.

As far as I know, COBOL doesn't allow to to resize the arrray once it's
created.

This is why I have been saying I will need to read the whole file into one
array/table to succeed, unless I can dynamically assign the memory I need
each time.

Or, am I inocorrect about the resize issue?
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 10)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c2qu3$jh7$1@news.igs.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>`

```
You allow for the largest.  Saying "I cannot re-use" is wrong. You can
re-use.  You may not have allocated enough, but you can certainly re-use
what you have.

Cosmic Knight >removethis <<@home.com> wrote in message
<0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>...
>In reply to most of the above posts:
>
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 10)_

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E5363E.7E968242@boeing.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>`

```
"Cosmic Knight >removethis<" wrote:

> Therefore, I can't reuse the same memory because I have no idea how much I
> will need to porcess the next customer.
…[8 more quoted lines elided]…
> Or, am I inocorrect about the resize issue?

In my previous comments, I load a working table (until the key changes)
it took a little experimenting to find the maximum number of records for
a table (array) group

in one of my programs that is 575 records per table -- a table can
consist of a single record and there is a test for potential table
overflow (error message) -- the average table runs 6 records with
perhaps 5% of the data falling into very large tables and 80% into very
small tables, the remaining 15% are small tables of about 50 records.  I
allocate a table for the max, set a variable counter (that is reset to 1
each time I reload the table). I can and do read the table a number of
times to perform conditional field changes.  This is all legacy code and
has been untouched for 5 or 10 years (except to introduce new fields or
additional data feeds).

	Susan A
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c2io6$nde$1@slb3.atl.mindspring.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>`

```
There are probably OTHER replies that have already answered this, but you are
correct that you MISUNDERSTAND "occurs depending on".

The way that this works in COBOL is that you *always* get the amount of
storage that is "large enough" to hold the "to n" value in you "OCCURS 1 to N
times Depending ON x".  COBOL does NOT "resize" storage to fit the current
value of "x".  Rather it insures (well sort-of) that you do not have ACCESS
to the X+1 thru Nth elements (until you change the value in "X" - when those
elements "suddenly" (magically) become available again).

OK,  Now the real question is what value to set "N" to.  The algorithm that I
suggested (in an earlier post) was:

1) Find out from your "user" what the LARGEST possible/expected number of
transactions for a single person is.

2) Double that number (to handle things that aren't supposed to happen - but
COBOL programmers ALWAYS know might happen).

3) Write an error routine to handle the case that you actually DO get more
than this larger number (and make certain that you test for it when reading
in transactions).
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 11)_

- **From:** "Cosmic Knight" <cosmicknight>>removethis<<@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net>`

```


> There are probably OTHER replies that have already answered this, but you
are
> correct that you MISUNDERSTAND "occurs depending on".

Ugh.  Actually, there are not. See below.

>
> The way that this works in COBOL is that you *always* get the amount of
> storage that is "large enough" to hold the "to n" value in you "OCCURS 1
to N
> times Depending ON x".  COBOL does NOT "resize" storage to fit the current
> value of "x".  Rather it insures (well sort-of) that you do not have
ACCESS
> to the X+1 thru Nth elements (until you change the value in "X" - when
those
> elements "suddenly" (magically) become available again).

You state as I do, that a COBOL table cannot be resized.  Therefore I
apparently have not misunderstood the OCCURS...DEPENDING ON statement.  I
realize that I will get the proper amount of storage to work with N
elements.  However, incrementing the subscript beyond N will result in a
range error.  Continued...

<snip>

> 1) Find out from your "user" what the LARGEST possible/expected number of
> transactions for a single person is.

This is exactly my point.  There is absolutely no way to know how many
transactions a customer will have.  There isn't a reasonable guess.  It
varies wildly.  I can't say " customer will only have 5000 transactions, so
I will pad the limit of the array to 10,000 so I have some margin for
error."  If this were true, I would have never posted here.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ek5F4.15864$0o4.94469@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
In article <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:

[snip - attributions missing in original]

>> 1) Find out from your "user" what the LARGEST possible/expected number of
>> transactions for a single person is.
>
>This is exactly my point.  There is absolutely no way to know how many
>transactions a customer will have.

Bingo!  *This* is the crucial datum in designing a solution.

>There isn't a reasonable guess.  It
>varies wildly.  I can't say " customer will only have 5000 transactions, so
>I will pad the limit of the array to 10,000 so I have some margin for
>error."  If this were true, I would have never posted here.

Well, there's *usually* a 'reasonable guess'... if, say, your system
assigns a seven-digit transaction number then it is, I would say,
'reasonable' to guess that a customer won't have move than 9,999,999
transactions... but this is a niggling aside.

What I am reading here is that you are attempting to design a solution for
a potentially infinitely large number of transactions.  Such a system
should not be desinged to use tables in COBOL; it should be designed to
use flatfile and match/merge processing.

Remember, back in the Oldene Dayse one was limited to tables of
32K... even 'improved' would, when given something like:

01  TBL.
    05  TBL-REC OCCURS 15000 PIC X(1000).

... would return:

IKF2116I-E     FIXED LENGTH GROUP ITEM IN WORKING-STORAGE OR LINKAGE
SECTION IS GT 131,071 BYTES.
               TRUNCATED TO 131,071.
IKF2198I-E     MAXIMUM LIMIT OF 255 BL, BLL OR SBL CELLS HAS BEEN
EXCEEDED. UNPREDICTABLE RESULTS
               WOULD OCCUR IF EXECUTION ATTEMPTED.

(pardon the wonky formatting... cut-n-paste, you know)
(note also the phrase 'IF EXECUTION IS ATTEMPTED' is kinda mooted by the
-E level diagnostic)

Tables are for small solutions within a finite range, hence such arcana
as:

IF TBL-LOAD-CTR > WS-MAX-ENTRIES-ALLOWED
    MOVE TBL-LOAD-CTR TO DISPLAY-NUMFLD
    DISPLAY '* * * TABLE SIZE EXCEED * * *'
    DISPLAY '* * * LOAD-CTR = ', DISPLAY-NUMFLD
    DISPLAY '* * * CONTACT SYSTEMS GROUP * * *'
    MOVE 666 TO RETURN-CODE
    GO TO Z999-ABEND-BLOW-UP-AND-DIE.

(or so such things used to be written, long ago)

In short - small, almost-predictable amounts of data go into tables and
large, unpredictable amounts of data stay in files.

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OafGmHzm$GA.351@cpmsnbbsa04>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
There is a limit to how many transactions a customer may have, there
always is.

1) if you need the full record for output, write it to a file, (open,
write, close, open,read, close) for each customer (a work file).

2) save the data you NEED to work with in the table. If you don't have
a need for the data while processing the table don't save it. I doubt
that you are processing all the fields in the record.

3) Your 2000 byte record would allow you approx. 8,350 Occurrences in
OS/390.
The maximum number of occurrences will increase as your table element
size decreases.
Take as much as the 16M limit will allow.

4) You can match the table to the work file on output.

Cosmic Knight >removethis <cosmicknight<@home.com> wrote in message
news:Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com...
>
>
> > There are probably OTHER replies that have already answered this,
but you
> are
> > correct that you MISUNDERSTAND "occurs depending on".
…[4 more quoted lines elided]…
> > The way that this works in COBOL is that you *always* get the
amount of
> > storage that is "large enough" to hold the "to n" value in you
"OCCURS 1
> to N
> > times Depending ON x".  COBOL does NOT "resize" storage to fit the
current
> > value of "x".  Rather it insures (well sort-of) that you do not
have
> ACCESS
> > to the X+1 thru Nth elements (until you change the value in "X" -
when
> those
> > elements "suddenly" (magically) become available again).
>
> You state as I do, that a COBOL table cannot be resized.  Therefore
I
> apparently have not misunderstood the OCCURS...DEPENDING ON
statement.  I
> realize that I will get the proper amount of storage to work with N
> elements.  However, incrementing the subscript beyond N will result
in a
> range error.  Continued...
>
> <snip>
>
> > 1) Find out from your "user" what the LARGEST possible/expected
number of
> > transactions for a single person is.
>
> This is exactly my point.  There is absolutely no way to know how
many
> transactions a customer will have.  There isn't a reasonable guess.
It
> varies wildly.  I can't say " customer will only have 5000
transactions, so
> I will pad the limit of the array to 10,000 so I have some margin
for
> error."  If this were true, I would have never posted here.
>
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e61e1c.81507840@news.cox-internet.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
On Fri, 31 Mar 2000 16:26:29 GMT, "Cosmic Knight"
<cosmicknight>>removethis<<@home.com> wrote:


>This is exactly my point.  There is absolutely no way to know how many
>transactions a customer will have.  There isn't a reasonable guess.  It
>varies wildly.  I can't say " customer will only have 5000 transactions, so
>I will pad the limit of the array to 10,000 so I have some margin for
>error."  If this were true, I would have never posted here.

OK, time for a compromise.  I've used this method many times.  In the
olden days I used it because all you could have in memory is 64K for a
table.  I had tables larger than this.  I actually used two methods.

Method 1.  Allocate a table of "max" size.  
                 Load the table.  If it does not overflow, use it as
is.  If it does overflow, write the entire contents of the table to a
temp file as a table image then start loading anew.  Repeat as
necessary, storing upper and lower data items for each table image
stored.  Then when searching determine which image to call into
current memory for the search.  Make your table of adequet size to
handle the average, or slightly larger than average table size.  This
way you get the speed benefit for MOST customers and only suffer
slightly for the larger.

Method 2.  Same basically as above, but when overflowing start writing
to a relative file.  That way you get pure ram for most customers, but
for the largest (the exceptions) you use disk for table entries.  It's
pretty easy to code.  Drawback with method 2 is that you don't get to
use "SEARCH".  Method one works with Search once you determine which
table segment to use.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c5rjn$ptj$1@slb3.atl.mindspring.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com> <38e61e1c.81507840@news.cox-internet.com>`

```
news:38e61e1c.81507840@news.cox-internet.com...
> On Fri, 31 Mar 2000 16:26:29 GMT, "Cosmic Knight"
> <cosmicknight>>removethis<<@home.com> wrote:
…[4 more quoted lines elided]…
> >varies wildly.  I can't say " customer will only have 5000 transactions,
so
> >I will pad the limit of the array to 10,000 so I have some margin for
> >error."  If this were true, I would have never posted here.
>

I know that someone else made this comment a while ago in this thread, but I
*still* think this is an "analsysis" problem and not a programming problem.
With all the years that I have been working with COBOL "business"
applications, I just have NEVER heard of an application where this "truly
unpredictable" transaction size is a reality.  Especially in an environment
where the user seems "fairly confident" that the program will ONLY have a
maximum of 200,000 records (for all people).

I am not saying that such an application may not exist in the world, but I
don't think the description of this environment sounds like such.  Therefore,
if a *reasonable* number were assumed and error processing on overflow were
included, then I really think this would be best.

Let's face it -
  If in reality the program really needs all 2000 bytes of a record for each
transaction and there is the (realistic) chance that all 200,000 records
could be for the same person, then COBOL (particularly on OS/390) simply will
NOT support having all of these available simultaneously in memory. (I
question that C on OS/390 - or even Assembler would - without cross-memory
services).

Therefore, I am back to saying find out the REAL program requirements and
develop accordingly.  (I don't think that we have ever heard why it is
necessary to move backwards and forward within all the records of the same
person - but that might have been answered when I wasn't watching. My guess
is that a "proper sort" would make this unnecessary and get rid of the entire
need for ANY table.)
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P4cF4.18631$QJ3.2904734@dfiatx1-snr1.gtei.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
If you only need one record at one time (as long as you process in the
correct order) , you don't even need a table.

Just use SORT, reading the records, adding a key, RELEASE'ing the records;
then you get 'em back in order using RETURN.

Now your only limit is the size of your SORTWKnn files, which of course you
can change in JCL without even touching the COBOL program.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YgdF4.4774$p13.74167@nnrp1.ptd.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
Cosmic,

I realize this isn't the solution you were looking for, but there is an
easy way to solve the problem in cobol.  Don't use a table at all...

Use an indexed file for your temporary table

OPEN OUTPUT TEMP-INDEXED-FILE

Read the original data same as before, but instead of reading
into table records, write temp-indexed-file records for each
transaction for present customer.

You will have to set up an index field for each record.  I suggest
02 INDEX-NAME  PIC X(12).

Set up a working-storage variable   01 RECORD-COUNTER  PIC 9(12).
This represents the number of records read, so far, for the current
customer.

Can we say that there will be no more than 999,999,999,999 records
for any *one* customer?  If not, you can increase the number of digits!!

Anyway, as each data record is written out to TEMP-INDEXED-FILE,
ADD 1 to RECORD-COUNTER
MOVE RECORD-COUNTER TO INDEX-NAME

When done reading the current customer, CLOSE TEMP-INDEXED-FILE


To do your processing of this customer:

OPEN INPUT TEMP-INDEXED-FILE

MOVE  record-number-you-want TO INDEX-NAME
READ TEMP-INDEXED-FILE

You can move back and forth by specifying the record number

When done with this customer, simply close the file.

When you process the next customer, the same temp-file will
be opened as OUTPUT, so the disk file area will be reused.

The only limitations to the number of records per customer, are:
1) the number of digits specified in RECORD-COUNTER and INDEX-NAME
2) the available disk space

bye for now,

don ferrario
http://www.ferrario.com




Cosmic Knight >removethis <cosmicknight<@home.com> wrote in message
news:Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>
> This is exactly my point.  There is absolutely no way to know how many
> transactions a customer will have.  There isn't a reasonable guess.  It
> varies wildly.  I can't say " customer will only have 5000 transactions,
so
> I will pad the limit of the array to 10,000 so I have some margin for
> error."  If this were true, I would have never posted here.
>
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 13)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vOdF4.15969$0o4.97664@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com> <YgdF4.4774$p13.74167@nnrp1.ptd.net>`

```
In article <YgdF4.4774$p13.74167@nnrp1.ptd.net>,
don ferrario <don@ferrario.com> wrote:
>Cosmic,
>
…[3 more quoted lines elided]…
>Use an indexed file for your temporary table

With all due respect, Mr Ferrario, I'd advise a bit of caution when making
such suggestions.  Leaving aside the fact that I've seen *horrid* amounts
of work generated by a statement beginning with 'All ya gotta do is'...

... what if one is in a shop where temp indexed files are Just Not
Allowed?  Or how about... a place where temp indexed files are Just Not
Allowed *and* internal sorts are forbidden?  What about... a place where
temp indexed files are Just Not Allowed, internal sorts are forbidden
*and* one cannot use SEARCH/SEARCH ALL?

Not, of course, that such places could *ever* exist in the Real
World... and if they *did* exist in the Real World they'd *never* be in,
say, Manhattan... and if they *did* exist in the Real World and *were* in
Manhattan they'd *never* have offices on Park Avenue, in the Ziff-Davis
building...

... but *were* such a place to exist one might learn to do
rather... interesting things with external sorts and flatfile processing
there, aye.

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 14)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HDmF4.19254$QJ3.3057281@dfiatx1-snr1.gtei.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com> <YgdF4.4774$p13.74167@nnrp1.ptd.net> <vOdF4.15969$0o4.97664@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote in message ...
>... what if one is in a shop where temp indexed files are Just Not
>Allowed?  Or how about... a place where temp indexed files are Just Not
…[3 more quoted lines elided]…
>


Well, I would stop worrying about COBOL. I think I might try to teach the
management something else, like, maybe, "how to hunt and kill a wooly
mammoth so that you and the rest of the tribe may eat." Only then would I
move on to more advanced concepts, like "fire."

MCM
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 15)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tt2G4.16202$0o4.105042@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <YgdF4.4774$p13.74167@nnrp1.ptd.net> <vOdF4.15969$0o4.97664@iad-read.news.verio.net> <HDmF4.19254$QJ3.3057281@dfiatx1-snr1.gtei.net>`

```
In article <HDmF4.19254$QJ3.3057281@dfiatx1-snr1.gtei.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
>docdwarf@clark.net wrote in message ...
>>... what if one is in a shop where temp indexed files are Just Not
…[10 more quoted lines elided]…
>move on to more advanced concepts, like "fire."

What, you'd neglect etiquette lessons?... 'Thag, not eat parsley... only
for look!'

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 14)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E89A69.47C21275@cusys.edu>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com> <YgdF4.4774$p13.74167@nnrp1.ptd.net> <vOdF4.15969$0o4.97664@iad-read.news.verio.net>`

```


docdwarf@clark.net wrote:
> 
> In article <YgdF4.4774$p13.74167@nnrp1.ptd.net>,
…[16 more quoted lines elided]…
> *and* one cannot use SEARCH/SEARCH ALL?

But they're no more common than places where using tables for this
problem are not allowed.  Make the best suggestion, and if the customer
chooses not to accept the suggestion, go to the second best suggestion. 
That's all we can do.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 15)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Fv2G4.16203$0o4.105309@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <YgdF4.4774$p13.74167@nnrp1.ptd.net> <vOdF4.15969$0o4.97664@iad-read.news.verio.net> <38E89A69.47C21275@cusys.edu>`

```
In article <38E89A69.47C21275@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, post, them!!> wrote:
>
>
…[24 more quoted lines elided]…
>That's all we can do.

My point precisely, Mr Brazee... and 'here', in this newsgroup, is where
some of the hashing-out and twisting-around of various solutions gets
done.  In some places one can use some techniques, in others places one
can use others... hence the explorations.

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E56312.293D7A53@zip.com.au>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com>`

```
"Cosmic Knight >removethis<" wrote:
> 
> This is exactly my point.  There is absolutely no way to know how
…[4 more quoted lines elided]…
> posted here.

Here is the rub:  Even for a dynamically allocated array you still
need to be able to allocate N elements of that array. If you really
want to do this, which I would NOT, repeat NOT, do you need to build a
linked list.  It is really all in the words in this game.  I am not
phobic about dynamic allocation, I write in C for my linked list
stuff, so don't write this off as 'cobol bluster'.

The problem is with any implementation is that you effectively build
in limitations.  I designed a system a couple of years back and I
'had' to have a memory table.  By the time I had finished the spec and
got the money to do the project (about two months) I had worked out
how to remove it.  No built in limitations, no dynamic tables.

The other thing is that you are talking about buffering a 2000 byte
record.  It is highly unlikely that you need the lot.  Consider what
you would pull out to reduce the overhead.  Once you have done you
flip flop stuff, reread the file and process sequentially getting the
new data.

Now if Cobol had a seek to file position, and tell file position I
would be a happy camper, this would solve some of your problems.

Really think about your implementation and the tools you have to work
with.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 13)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000331223534.26515.00000232@nso-fb.aol.com>`
- **References:** `<38E56312.293D7A53@zip.com.au>`

```
In article <38E56312.293D7A53@zip.com.au>, Ken Foskey <waratah@zip.com.au>
writes:

>
>Now if Cobol had a seek to file position, and tell file position I
>would be a happy camper, this would solve some of your problems.
>
>

Back in my Unisys days, there was a SEEK on sequential flat files.
There also was syntax to interrogate / change record length/blocksize/
total record count/.....
It was real neat stuff to be able to have the file ordered then build a 100 
entry table to do a preliminary binary search isolating which 1% of the file 
would require physical read processing.  Cut some 80% of the previous 
runtime.
I really miss the ability to do that sort of thing.

with pointers
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 13)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IDmF4.19255$QJ3.3057667@dfiatx1-snr1.gtei.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <8c2io6$nde$1@slb3.atl.mindspring.net> <Vk4F4.12580$Y4.258385@news1.rdc1.il.home.com> <38E56312.293D7A53@zip.com.au>`

```
Ken Foskey wrote in message <38E56312.293D7A53@zip.com.au>...
>Now if Cobol had a seek to file position, and tell file position I
>would be a happy camper, this would solve some of your problems.
>


This guy is in an IBM mainframe environment, so if you IDCAMS/REPRO the
input to a VSAM ESDS work file, you can access the file randomly in COBOL
with a relative key. Close enough to "seek?"

MCM
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 14)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000401110855.24055.00000138@nso-cb.aol.com>`
- **References:** `<IDmF4.19255$QJ3.3057667@dfiatx1-snr1.gtei.net>`

```
In article <IDmF4.19255$QJ3.3057667@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> writes:

>
>This guy is in an IBM mainframe environment, so if you IDCAMS/REPRO the
…[4 more quoted lines elided]…
>

Probably works, but you have the extra setup and maintenace of the repro'ed
file
to contend with.  I grew accustomed to the old Burroughs/Unisys SEEK to
position
the file pointers before doing the acutal read.  This permitted the equivalence
of
random access to the flat files.  (This was primarily for READ or REWRITE
operations.  As it is impossible to INSERT records into the middle of a file
without
re-writing the whole file. In a memo-post environment, we added records the 
end of the file and later re-orged to put the new records in the proper order.)
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 15)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hCtF4.19759$QJ3.3170855@dfiatx1-snr1.gtei.net>`
- **References:** `<IDmF4.19255$QJ3.3057667@dfiatx1-snr1.gtei.net> <20000401110855.24055.00000138@nso-cb.aol.com>`

```
Sff5ky wrote in message <20000401110855.24055.00000138@nso-cb.aol.com>...
>In article <IDmF4.19255$QJ3.3057667@dfiatx1-snr1.gtei.net>, "Michael
Mattias"
><michael.mattias@gte.net> writes:
>
…[7 more quoted lines elided]…
>file to contend with.  I grew accustomed to the old Burroughs/Unisys SEEK
to
>position the file pointers before doing the acutal read.  This permitted
the equivalence
>of random access to the flat files....


Well, I've been known to write a couple of lines of BASIC code, and I use
SEEK a lot in BASIC.

But there ain't no SEEK in COBOL for 390 & VM; so I guess we're stuck with
IDCAMS/DEFINE/REPRO and RELATIVE KEY IS....

MCM
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 10)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cm4F4.15851$0o4.94097@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>`

```
In article <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:
>In reply to most of the above posts:
>
…[8 more quoted lines elided]…
>will need to porcess the next customer.

Welllll... you do and you don't.  Remember, coding is *not* 'one size fits
all'; a solution which is fine for volume (x) will be unsatisfactory for
volume (10x).  With that in mind:

Assuming that you need 200 bytes of data from each 'order' record then you
can have (using the Olden Rules of No Tables Greater Than 32K) a maximum
of 160 records per customer, or:

01  WS-ORDREC-TBL.
    05  WS-ORDER-REC OCCURS 160.
        10  WS-ORDER-REC-CUSTNAM PIC X(32).
        10  WS-ORDER-REC-CUSTNO  PIC X(10).
        10  WS-ORDER-REC-THIS    PIC X(05).
        10  WS-ORDER-REC-N-THAT  PIC X(15).
        10  WS-ORDER-REC-N-MORE  PIC X(138).

... and that would give you a fairly large chunk to work with.  Were you
to wish to allocate this 'dynamically' you might use:

01  WS-ORDERC-TBL.
    05  WS-ORDER-REC OCCURS 1 TO 160 DEPENDING ON LOADREC-CTR.

Then, when you load your table, you read a record, increment your counter
and MOVE your data into the table.

The array will be 'resized' while loading... but not really; the compiler
will look at the TO integer and say 'all righty, this is how big she can
get'... and that is what will be 'allocated'; when the load module is
created it will, physically, have a 32K chunk available for
WS-ORDREC-TBL... but hey, core's cheap these days.

>
>As far as I know, COBOL doesn't allow to to resize the arrray once it's
>created.

See the use of OCCURS DEPENDING ON above; the answer is... yes, and no.

>
>This is why I have been saying I will need to read the whole file into one
…[3 more quoted lines elided]…
>Or, am I inocorrect about the resize issue?

I do not see how this becomes an issue, given that *any* time one loads a
table one checks for overflow conditions; after one's processing-volume
exceeds a certain size one moves away from table-loading and into use of
files.  As mentioned earlier you'll want to sort the file you're loading
into an appropriate sequence; that way you'll be able to load all your
JONES recs, process them and move on to the SMITHs.

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 11)_

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c6mgn$mrh$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com> <8c26bl$8o6$1@news.igs.net> <0R3F4.12566$Y4.257570@news1.rdc1.il.home.com> <Cm4F4.15851$0o4.94097@iad-read.news.verio.net>`

```
    So far as I know, the languages that DO support resizing an array do
it the same way we would, ie allocate a new, larger, empty array,
copy the data from old (small) array into new array, and then
free the old array.

     This could be a problem if you are trying to enlarge a very large
array.



<snip>
<> >
> >As far as I know, COBOL doesn't allow to to resize the arrray once it's
> >created.
…[4 more quoted lines elided]…
> >This is why I have been saying I will need to read the whole file into
one
> >array/table to succeed, unless I can dynamically assign the memory I need
> >each time.
> >
> >Or, am I inocorrect about the resize issue?

<snip>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ukLCsHxm$GA.245@cpmsnbbsa03>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`

```
I read your message.
You're tying to do C in COBOL.
Use the OCCURS DEPENDING ON (ODO) option to Dynamically size your
table at run time.
You do NOT HAVE TO clear the table after each use, the next group will
overlay the previous data.
The ODO can be changed repeatedly, resizing as it goes along.

Keep in mind the Table size max in your environment is only 16M.

Read all of your Smiths into the table.
Process smith.
Set your index to 1.
Read all your Jones into the table.
process Jones
Set your index to 1.
Read all your ???? into the table.
process ????



Cosmic Knight >removethis <cosmicknight<@home.com> wrote in message
news:9NWE4.12136$Y4.226484@news1.rdc1.il.home.com...
> My point is, I don't need 400 megs if I can dynamically allocate
what I need
> for each group of records that need to be processed together from
the input
> file. (see original post)
>
> Unless I can dynamically assign memory at run time, I am stuck
bringing the
> whole file into memory, which is what I am trying to avoid.  You are
correct
> in that if I had no choice but to pull the whole file into memory,
whether
> the 400 megs was assigned dynamically or not would make no
difference.
> After all, 400 megs is 400 megs.
>
> I will try to answer several questions here in this post, without
typing in
> too many details.
>
…[11 more quoted lines elided]…
> Without going into the long list of details as to why this needs to
be an
> array, let's just say I need to process J. Smith in such a way that
will
> require me to move back and forth between orders 1, 2, and three
many times
> before I write the output record.  The array needs to be of a
variable
> length because I have no way of knowing how many orders J. Smith
will have
> in the file.  It could be two, or 20, etc.  Now that I've thoroughly
> confused you... :-)
>
> Ok, so now I am done with Smith and I can move onto Jones.  For
efficiency,
> I would like to allocate enough memory to handle Smith, destroy it,
then
> move on and do the same thing for Jones.  If I can't assign this
storage
> dynamically, I will have to read the whole file into an array to
work with
> it.  This file could be enormous.  I used 400 megs before, it could
be less,
> it could be significantly more.  The size of the file is
undeterminable.
>
> This leads me to my quandary, and my post here.  I cannot process
the file
> sequentially, I need to process each "set" (smith, jones) and move
on to the
> next set.  Within the set, I need to move back and forth between
elements in
> the set. (orders)
>
> I hope this helps you guys understand my situation better.  If you
need more
> detail, I can provide it.
>
…[4 more quoted lines elided]…
> > There is no need to pull the whole thing into an array, *NOR* is
there a
> > need to dynamically allocate/deallocate.  You can have a fixed
array that
> is
> > only as big as the most common record.  You seem to have this
fixation
> that
> > dynamically allocating/deallocating will lessen the  array size.
All it
> > does is free memory up sooner, no matter what algorithm you use.
If you
> need
> > 400,000,000 bytes, then dynamically allocating it is not going to
make it
> > smaller.  BTW, the smallest *micro* I have is 128,000,000 bytes,
and it is
> a
> > virtual machine.  400 megs might have been a lot a few years back,
but not
> > any more.
> >
> > Cosmic Knight >removethis <<@home.com> wrote in message ...
> > >The amount of input data will vary wildly, but as an example,
let's say
> > >there are 200,000 records in a file.
> > >
> > >Each record is 2000 chars in length.
> > >
> > >So, to suck this whole file into an array would require
400,000,000
> bytes.
> > >
> > >This is a lot, even for a mainframe.  Perhaps you guys disagree.
> > >
> > >Bill, you mentioned the extra overhead involved in dynamically
assigning
> > >memory.  You are, of course, correct, but I thik the overhead
incurred
> here
> > >will be negligable when compared to the gains received by not
pulling
> this
> > >huge array into memory. (virtual, or otherwise)
…[3 more quoted lines elided]…
> > You can use the same static memory over and over again, and gain
all that
> > time you would waste on allocation and delallocation.
> >
> > >
> > >I am trying to figure out exactly which compiler we are running,
but I am
> > >pretty sure it is the COB390 compiler, which if I am not mistaken
will
> > allow
> > >dynamic allocation of "heaps" via some utilities. These "heaps"
are
> > >connected via pointers, much like a link-list.  (This is an
AMDAHL MF,
> > >OS390/MVS)
> > >
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c2atn$b9p$1@news.igs.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c11fo$hs0$1@news.igs.net> <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`

```

Cosmic Knight said:

<everything snipped>

Further to my last post.  I CAN see an advantage to dynamically allocating
your array.  It gains you the advantage of not needing to know the array
size needed for the largest customer.

Having said that, however, I cannot see any advantage to then releasing the
array, and re-allocating it for the next customer. It is not only more
efficient to reuse the same array, but there is far less potential for
technical screw ups like memory creep, and a fair amount of overhead.

Even if I were writing that code in a language that used dynamic allocation
constantly, it is not the method I would choose to code a function like
that.  You are coding, from what I read in your example, a program that is
essentially batch.  It is going to be over and done with in a very short
period of time, and all memory is going to be re-allocated to the pool as
soon as the program ends.
It would be far more efficient to simply add to the array size until it
matches the number of records for the largest customer, never de-allocating
anything until the end of the program.

There are only four methods:

    method-one.
        perform each-customer. (x times)

    one-customer.
        perform allocate-for-one. (allocating just enough)
        perform one-customer.
        perform release-for-one.

This seems to be what you want to do, and is the least efficient and most
error prone of the four approaches.
**************************************
    method-two.
        perform allocate-for one. (allocating for largest)
        perform each-customer. (x times re-using)
        perform release-for-one.
**************************************
    method-three.
        perform each-customer.  (x times using statically defined memory).
**************************************
    method-four.
        perform each-customer. ( x times, using *different* static memory
for each)
**************************************

You seem to be saying that you have only method four, yet you repeat in your
example (twice), that once you are finished with one customer, you go on to
the next. I think you have a mind block because you are thinking in another
language.

Certainly method four is dumb, and not a good replacement for method one,
the one you appear to want.  However, method three works without *any*
dynamic storage, and uses no more memory than any of the other methods.
(Well, perhaps more than method one as you do not know the largest and you
have to allocate some slack space. But it does not need to hold all
customers, only the largest).
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 8)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000331113240.27297.00000134@nso-ca.aol.com>`
- **References:** `<9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>`

```
In article <9NWE4.12136$Y4.226484@news1.rdc1.il.home.com>, "Cosmic Knight"
<cosmicknight>>removethis<<@home.com> writes:

>Without going into the long list of details as to why this needs to be an
>array, let's just say I need to process J. Smith in such a way that will
…[5 more quoted lines elided]…
>

What exactly is being done with the 'order set' that you have to bounce around
between each record?  Are you summarizing and updating information on every
entry?  There are design issues that could be considered for processing each
entry without any tables IF you are not changing the content of the order
entries.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c155q$ee5$1@slb6.atl.mindspring.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com>`

```
The point is that (from your own definition), you do NOT need all 200,000
records in storage at one time.  What you need to do is create a SINGLE table
that can hold all the records for a single person.  Such a table (even with
2000 byte records) will *not* be too large to fit in an OS/390 environment.

Once you have filled and used the table for one person's records, you then
start over at the beginning of the table and use it for the next person's
records.

This DOES assume that your input file is already sorted in "person" order.
If it isn't (and the file is not "keyed" on the persons id), then you need to
sort it first.  This can be done with either an internal COBOL sort - or an
external sort (Syncsort, DFSort, etc).
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 7)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E4A98D.12BF5520@iinet.net.au>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com> <8c155q$ee5$1@slb6.atl.mindspring.net>`

```

"William M. Klein" wrote:
> 
> The point is that (from your own definition), you do NOT need all 200,000
…[3 more quoted lines elided]…
> 
OK, If you REALLY want to load the data into memory and you have an IBM OS/390 system
try the following:

There is a manual in the OS/390 set called "High Level Language API's" or some such name.
In it you will find described how to Initialize, load and use a HyperSpace using Data
Windowing Services. Use one of these and you will have access to 16 Terabytes of address
space.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KOUE4.15756$0o4.89873@iad-read.news.verio.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <8c0d1i$ap7$1@slb7.atl.mindspring.net> <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com>`

```
In article <kwSE4.11533$Y4.208763@news1.rdc1.il.home.com>,
Cosmic Knight <cosmicknight> wrote:
>The amount of input data will vary wildly, but as an example, let's say
>there are 200,000 records in a file.
…[3 more quoted lines elided]…
>So, to suck this whole file into an array would require 400,000,000 bytes.

That it would... were you to need all 2,000 characters of each and every
200,000 recs to be available immediately and unpredictably.

This is, I believe, the primary advantage of arrays (or 'tables', as some
folks call 'em) - the fact that they allow data to be repeatedly used when
they are needed immediately and unpredictably.  Since you incur
data-center chargebacks based, in part, on CPU use you want to keep your
core down as small and as tight as possible.

Perhaps you might go on a bit more about the application involved; folks
who are used to being limited by (and, when necessary, breaking) a
table-size limit of 32K might be able to offer you a bit of advice.

For example... once, long ago, I had to read a master-file which contained
another file's alternate key... and I found it to be faster to, as part of
housekeeping, build a table of alternate and primary keys so that when a
master-file rec was read the alternate key would be looked up in the table
and the file would be read on primary key; this sped up processing
appreciably.

Similarly... unusual thinking might be applied to your present difficulty
were more known about it.

DD
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OdIE4.15212$QJ3.2365333@dfiatx1-snr1.gtei.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`

```
Cosmic Knight >removethis <<@home.com> wrote in message ...
>The problem is, if I use INITIALIZE or reset the subscript to 0, I haven't
>really destroyed the array.
…[3 more quoted lines elided]…
>


Not in any current release of COBOL, assuming that the table (array) is
created with an OCCURS clause in working-storage.

Next release of COBOL will let you do dynamic memory
allocation/deallocation; when you combine that with pointers, you could do
what you are asking.

Michael Mattias
Tal Systems
Racine WI USA
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bvtvg$4c5$1@news.cerf.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com> <OdIE4.15212$QJ3.2365333@dfiatx1-snr1.gtei.net>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:OdIE4.15212$QJ3.2365333@dfiatx1-snr1.gtei.net...
> Next release of COBOL will let you do dynamic memory
> allocation/deallocation; when you combine that with pointers, you could do
> what you are asking.

You might want to state that the next release you are talking of here is the
next standard, which does not mean that as stroke by a lightening all Cobol
vendors support it.

However, as William Klein has pointed out several times, many vendors
already support dynamic memory, and if this guy is using one of these, he
will be all set to start doing a linked list right away.

Cheesle
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 4)_

- **From:** aflinsch <avflinsch@att.net>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E3636B.5DF9C1F0@att.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`

```
"Cosmic Knight >removethis<" wrote:
> 
> The problem is, if I use INITIALIZE or reset the subscript to 0, I haven't
…[6 more quoted lines elided]…
> 

Not directly, but sort of possible in a roundabout kind of way. 
Note that different OSen may handle this in very different ways.

1 - Move your array processing to a sub program. You will need to code
all
    of the access to the array in this new module, by passing
parameters to it.

2 - Dynamically call the submodule from the main program.

3 - CANCEL the submodule from the calling module.

The key is to dynamically call the module, then cancel it when done.

The main problem is that the array will have to be defined as OCCURS
xx 
or OCCURS xx DEPENDING. Either way, most (if not al) compiliers will
allocate
the maximum amount in working storage.
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

_(reply depth: 4)_

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135942a64cc466a09896c5@news>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <8buohg$drp$1@nntp9.atl.mindspring.net> <exFNYVim$GA.156@cpmsnbbsa05> <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>`

```
[This followup was posted to comp.lang.cobol and a copy was sent to the 
cited author.]

Chris,

why do you want to "destroy" the array ? Are you going to build another 
array for the "next" key....   If so, why not just use the existing table 
and save all the time and resources spent in "allocating and 
deallocating" the table / array...   I would certainly not allocate / 
deallocate in a C or C++ program to do this...  allocate / deallocate 
would serve no purpose...  when you allocate the table, how would you 
determine its size....    perhaps the real issue here is determining the 
maximum size of the table....

In the situation you describe, you could build a table up to 16 Meg in 
COBOL II rel 4 (IBM OS/390 operating system). the program could be coded 
with variable lenght table. The table would not have to be initialized 
ever in the program...   you would just have to initialize every row as 
it was added to the table...  you could still use search all (binary), 
search (sequential) or some other hand crafted search process to search 
the table.  You would have to keep track at all times the number of 
elements in the table which are currently in use....  ( hint --> this 
would be used in the search routines to limit the portion of the table 
which would be searched )....

	Chris,

If the above is not sufficient info...   please email me with the file 
layouts and program specifications....   perhaps I could provide some 
example of the table loading / searching routines...



In article <WRHE4.10617$Y4.179296@news1.rdc1.il.home.com>, "Cosmic 
Knight" <cosmicknight>>removethis<<@home.com> says...
> The problem is, if I use INITIALIZE or reset the subscript to 0, I haven't
> really destroyed the array.
…[22 more quoted lines elided]…
> 
```

#### ↳ Re: Destroying a COBOL array

- **From:** Charles Hammond <ceh1@ritz.cec.wustl.edu>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000330112152.3875B-100000@ritz.cec.wustl.edu>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
Why not just describe the flat file with a record key and use i/o, random
or dynamic file access to search the file like a database.  On the
mainframe we often read various files into a temporary file and sort and
search that file and just overwrite that area later.   Tables are nice,
but you have trouble putting a file with 100,000 records in a table.

Charles Hammond, BSIM Undergraduate Program

On Thu, 30 Mar 2000, it was written:

> Hi:
> 
…[35 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Destroying a COBOL array

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E39AF7.472D7B4E@boeing.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <Pine.SOL.3.96.1000330112152.3875B-100000@ritz.cec.wustl.edu>`

```
Charles Hammond wrote:
> 
  Tables are nice,
> but you have trouble putting a file with 100,000 records in a table.
> 

only for very large records

	Susan
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WQ1F4.253$T9.3677335@news.netdirect.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <Pine.SOL.3.96.1000330112152.3875B-100000@ritz.cec.wustl.edu> <38E39AF7.472D7B4E@boeing.com>`

```
In article <38E39AF7.472D7B4E@boeing.com>, Susan Allen <susan.a.allen@boeing.com> wrote:
>Charles Hammond wrote:
>> 
…[6 more quoted lines elided]…
>        Susan

Even a ten-byte record would produce a megabyte table. Some (many?) compilers 
can't produce object files that large.
```

#### ↳ Re: Destroying a COBOL array

- **From:** shine98@my-deja.com
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c08oo$frr$1@nnrp1.deja.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
Here is how I would do it:
IDENTIFICATION DIVISION.
PROGRAM-ID. SLUTION.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT INPUT-FILE ASSIGN TO UT-FILEIN.
DATA DIVISION.
FILE SECTION.
FD INPUT-FILE
LABEL RECORDS ARE STANDARD
BLOCK CONTAINS 0 RECORDS
DATA RECORDS ARE INPUT-REC.
01 INPUT-REC.
05 IR-MAJ-KEY.
10 IR-NAME PIC X(14).
05 IR-ORDER-NUMBER PIC 9(01).
WORKING-STORAGE SECTION.
01 REC-CNT PIC 9(05) VALUE 0.
01 WS-EOF-SW PIC X(01) VALUE 'N'.
01 CUR-KEY.
05 CUR-MAJ-KEY PIC X(14).
01 PRV-KEY VALUE LOW-VALUES.
05 PRV-MAJ-KEY PIC X(14).
01 TBL-MAX PIC 9(03) VALUE 1000.
01 TBL-NBR-ENTRIES PIC 9(03) VALUE 0.
01 TBL.
05 TBL-ITEM OCCURS 1000 TIMES INDEXED BY TBL-NDX.
10 TBL-NAME PIC X(14).
10 TBL-ORDER-NUMBER PIC 9(01).
PROCEDURE DIVISION.
OPEN INPUT INPUT-FILE
MOVE 0 TO TBL-NBR-ENTRIES
MOVE SPACES TO TBL
PERFORM UNTIL WS-EOF-SW = 'Y'
READ INPUT-FILE AT END
MOVE HIGH-VALUES TO CUR-KEY
MOVE 'Y' TO WS-EOF-SW
END-READ
IF WS-EOF-SW = 'N'
MOVE IR-MAJ-KEY TO CUR-MAJ-KEY
ADD 1 TO REC-CNT
END-IF
IF REC-CNT = 1
MOVE CUR-MAJ-KEY TO PRV-MAJ-KEY
ELSE
IF CUR-MAJ-KEY NOT = PRV-MAJ-KEY
DISPLAY 'TABLE CONTAINS '
TBL-NBR-ENTRIES ' ENTRIES:'
PERFORM VARYING TBL-NDX FROM 1 BY 1
UNTIL TBL-NDX > TBL-NBR-ENTRIES
DISPLAY ' ' TBL-NAME (TBL-NDX)
' ' TBL-ORDER-NUMBER (TBL-NDX)
END-PERFORM
MOVE CUR-MAJ-KEY TO PRV-MAJ-KEY
* DESTROY THE TABLE!
MOVE 0 TO TBL-NBR-ENTRIES
MOVE SPACES TO TBL
END-IF
END-IF
IF WS-EOF-SW = 'N'
ADD 1 TO TBL-NBR-ENTRIES
IF TBL-NBR-ENTRIES > TBL-MAX
DISPLAY 'TBL BOUNDRY ERROR' GOBACK
END-IF
MOVE IR-NAME TO TBL-NAME (TBL-NBR-ENTRIES)
MOVE IR-ORDER-NUMBER
TO TBL-ORDER-NUMBER(TBL-NBR-ENTRIES)
END-IF
END-PERFORM
CLOSE INPUT-FILE
GOBACK.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Destroying a COBOL array

- **From:** shine98@my-deja.com
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c08rl$fub$1@nnrp1.deja.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
Here is how I would do it:
IDENTIFICATION DIVISION.
PROGRAM-ID. SLUTION.
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT INPUT-FILE ASSIGN TO UT-FILEIN.
DATA DIVISION.
FILE SECTION.
FD INPUT-FILE
LABEL RECORDS ARE STANDARD
BLOCK CONTAINS 0 RECORDS
DATA RECORDS ARE INPUT-REC.
01 INPUT-REC.
05 IR-MAJ-KEY.
10 IR-NAME PIC X(14).
05 IR-ORDER-NUMBER PIC 9(01).
WORKING-STORAGE SECTION.
01 REC-CNT PIC 9(05) VALUE 0.
01 WS-EOF-SW PIC X(01) VALUE 'N'.
01 CUR-KEY.
05 CUR-MAJ-KEY PIC X(14).
01 PRV-KEY VALUE LOW-VALUES.
05 PRV-MAJ-KEY PIC X(14).
01 TBL-MAX PIC 9(03) VALUE 1000.
01 TBL-NBR-ENTRIES PIC 9(03) VALUE 0.
01 TBL.
05 TBL-ITEM OCCURS 1000 TIMES INDEXED BY TBL-NDX.
10 TBL-NAME PIC X(14).
10 TBL-ORDER-NUMBER PIC 9(01).
PROCEDURE DIVISION.
OPEN INPUT INPUT-FILE
MOVE 0 TO TBL-NBR-ENTRIES
MOVE SPACES TO TBL
PERFORM UNTIL WS-EOF-SW = 'Y'
READ INPUT-FILE AT END
MOVE HIGH-VALUES TO CUR-KEY
MOVE 'Y' TO WS-EOF-SW
END-READ
IF WS-EOF-SW = 'N'
MOVE IR-MAJ-KEY TO CUR-MAJ-KEY
ADD 1 TO REC-CNT
END-IF
IF REC-CNT = 1
MOVE CUR-MAJ-KEY TO PRV-MAJ-KEY
ELSE
IF CUR-MAJ-KEY NOT = PRV-MAJ-KEY
DISPLAY 'TABLE CONTAINS '
TBL-NBR-ENTRIES ' ENTRIES:'
PERFORM VARYING TBL-NDX FROM 1 BY 1
UNTIL TBL-NDX > TBL-NBR-ENTRIES
DISPLAY ' ' TBL-NAME (TBL-NDX)
' ' TBL-ORDER-NUMBER (TBL-NDX)
END-PERFORM
MOVE CUR-MAJ-KEY TO PRV-MAJ-KEY
* DESTROY THE TABLE!
MOVE 0 TO TBL-NBR-ENTRIES
MOVE SPACES TO TBL
END-IF
END-IF
IF WS-EOF-SW = 'N'
ADD 1 TO TBL-NBR-ENTRIES
IF TBL-NBR-ENTRIES > TBL-MAX
DISPLAY 'TBL BOUNDRY ERROR' GOBACK
END-IF
MOVE IR-NAME TO TBL-NAME (TBL-NBR-ENTRIES)
MOVE IR-ORDER-NUMBER
TO TBL-ORDER-NUMBER(TBL-NBR-ENTRIES)
END-IF
END-PERFORM
CLOSE INPUT-FILE
GOBACK.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Destroying a COBOL array

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GuIE4.94456$Hq3.2462296@news2.rdc1.on.home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
By default COBOL handles all the memory allocation and deallocation for you.
It is typically outside of programmer control with COBOL. This is usually a
blessing. You can do your own memory allocation/deallocation by using system
calls, pointers and the LINKAGE area but it will complicate your program
needlessly.

Stop thinking like a C programmer and ask yourself how you would do
sequential processing with a finite internal array, or no array at all.
Maybe all you need is to sort the input data before processing,  and maybe a
few accumulator variables, rather than an internal array.

- Karl Wagner

"Cosmic Knight >removethis" <cosmicknight<@home.com> wrote in message
news:RnBE4.9926$Y4.172076@news1.rdc1.il.home.com...
> Hi:
>
…[22 more quoted lines elided]…
> I don't want to read in the whole file into one array because it would be
a
> HUGE array, and the performance would probably be poor.
>
…[8 more quoted lines elided]…
>
```

#### ↳ Re: Destroying a COBOL array

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E35EC2.44F79BB3@cusys.edu>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
What type of memory system are you using?  On a mainframe with lots of
virtual memory, I use large fixed length tables.  I move HIGH-VALUES to
MY-TABLE, before creating the table.  Processing treats a record with
HIGH-VALUES as a delimiter.

Depending on your OS, this might be more efficient than using variable
length arrays.

Alternatively, you can use called subprograms or OO.

"Cosmic Knight >removethis<" wrote:
> 
> Hi:
…[32 more quoted lines elided]…
> -ck
```

##### ↳ ↳ Re: Destroying a COBOL array

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000330101143.08424.00000023@ng-cf1.aol.com>`
- **References:** `<38E35EC2.44F79BB3@cusys.edu>`

```
If you are using COBOL on an IBM mainframe, you can use the Language
Environment callable services from COBOL, including:

CEECRHP - create heap
CEEGTSTG - get a storage element from a heap
CEECZST - change the size of a storage element (resize it larger or smaller)

and more.

<ad>

We cover all this and more, in COBOL, Assembler, PL/I, and C, in our course
"Applications Design Using LE Services", three days.

</ad>

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Destroying a COBOL array

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<063c668e.6a3bf462@usw-ex0101-005.remarq.com>`
- **References:** `<38E35EC2.44F79BB3@cusys.edu> <20000330101143.08424.00000023@ng-cf1.aol.com>`

```
If you are using MF COBOL, you can use library routines to
allocate memory and when done, free the memory. The library
routines are CBL_ALLOC_MEM and CBL_FREE_MEM. In working storage,
you would need a memory pointer and then setup you table in the
linkage section and then set the address of you linkage section
01 level to the address of the memory pointer.

By passing the pointer to other program, the memory area can be
used for other functions too.

Regards,
Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Destroying a COBOL array

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38eb6bde.16939167@usenet.acw.vcu.edu>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
If it's as large as you say it is, consider loading the data into a
VSAM file (or ISAM if it's on a PC), then process the data for dynamic
access.  This is the trick I use all the time with large data and I
need to update it.  It beats sequential file merging/updating coding
and the bugs it can produce.

On Thu, 30 Mar 2000 05:13:21 GMT, "Cosmic Knight"
<cosmicknight>>removethis<<@home.com> wrote:

>Hi:
>
…[33 more quoted lines elided]…
>
```

#### ↳ Re: Destroying a COBOL array

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb6359.6685697@news.gw.total-web.net>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com>`

```
This sounds pretty kludgy.  Can't you just sort the file?

I've read that a variable-length table, once established, can not be
released.  I suppose you could put it into s called program and cancel
that program when you're done with "smith" and call it again, but that
would probably use up more time than it's worth.

On Thu, 30 Mar 2000 05:13:21 GMT, "Cosmic Knight"
<cosmicknight>>removethis<<@home.com> wrote:

>Hi:
>
…[32 more quoted lines elided]…
>

---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

##### ↳ ↳ Re: Destroying a COBOL array

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F00245.899F06D3@home.com>`
- **References:** `<RnBE4.9926$Y4.172076@news1.rdc1.il.home.com> <38fb6359.6685697@news.gw.total-web.net>`

```


Paul Knudsen wrote:
> 
> >
…[16 more quoted lines elided]…
> >destroy the array after I'm done processing him, and move on to P. Jones.

I haven't followed this thread because I believe it was a mainframe
problem ? I don't know whether or not Michael Mattias has piped in - but
he favours using relative files as temporary working areas - could that
approach solve your table size problem ?

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
