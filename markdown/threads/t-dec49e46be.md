[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# need help. tables

_21 messages · 9 participants · 2001-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: need help. tables

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-09T07:56:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A83A2AE.DFD8CB38@Azonic.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com>`

```
Ed Stevens wrote:
> --
> And, while straying from the original question, the next step is what I
…[27 more quoted lines elided]…
> programmer that used this technique.

Some of us don't want to waste 30,000 bytes on a 9 byte table.  I
started on mainframes with 16k words and 20 years ago was using 8bit
micros where the availble program space was around 40Kb.

You do realise that the compiler will allocate a fixed maximum size for
the table don't you ?  While your calculation will establish the logical
size of the table this mechanism is not dynamic and the physical size
won't vary from the maximum.

I just add a dummy entry to my predefined tables and process until I see
that:

> 01 xxx-list.
>    05 pic x(3) value "AAA".
>    05 pic x(3) value "AAA".
>    05 pic x(3) value "AAA".
     05 pic x(3) value high-values.
> 01 xxx-table
>    redefines xxx-list.
>    05 xxx-entry
        occurs 4
>       indexed by ndx.
> 
…[4 more quoted lines elided]…
>     varying ndx from 1 by 1
      until xxx-entry(ndx) = high-values . . .

Yes, I have to adjust the OCCURS, but I could use 78s to do that.  I
don't waste resources.
```

#### ↳ Re: need help. tables

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-02-09T15:01:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95vljj$del$1@hermes.enternet.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz>`

```

Richard Plinston wrote in message <3A83A2AE.DFD8CB38@Azonic.co.nz>...

>Some of us don't want to waste 30,000 bytes on a 9 byte table.

Amen! I was shocked at this...not surprising he's only found one other
programmer who does it that way...<G> (mind you, that's one too many...<G>)
  I
>I just add a dummy entry to my predefined tables and process until I see
>that:
…[20 more quoted lines elided]…
>don't waste resources.

It is interesting, Richard, that for many years I used the same technique as
you describe. (Maybe it's a Kiwi thing..<G>?)

Then I went through a phase of moving the thing I was looking for to the
last entry in the table (where your high-values are) and doing the perform
until I got a match. If the matching index was equal to the number of
entries in the table, then it was not found... Describing it now seems kinda
weird...

Today I use Search...

01 table-search-flag   pic x value space.
     88 found-it      value '1'.
     88 not-found   value '0'.

set ndx to 1
search xxx-entry
      at end
           set not-found to TRUE
           < ...or, do whatever you want for NOT FOUND>
      when  xxx-entry (ndx) = whatever
           set found-it to TRUE
           <...or, do whatever you want for FOUND>
end-search
if not-found.....etc.
else
      move xxx-entry (ndx) to wherever....etc.
end-if

It makes it easier to locate specific table lookups in the code (look for
SEARCH rather than PERFORM (not that you need to do that with MY code of
course..<G>)), and it LOOKS more like COBOL...

For large tables I implement SEARCH...ALL and use the compiler's binary
chop. For exceptionally large or weird tables,  go right back to basics and
implement my own tertiary or skewed chop using PERFORM...<G>

I would recommend SEARCH to the users of this forum.

Pete.
```

##### ↳ ↳ Re: need help. tables

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-02-08T22:39:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95vsd9$uns$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <95vljj$del$1@hermes.enternet.co.nz>`

```
    I would add one feature to all the methods of searching so far.  Before
doing any of these types of searches, compare your previous search argument
and search result with your current search argument.  You oftentimes can
bypass the overhead of searching if what you're looking for is the same
thing you just got done looking for last time.
```

###### ↳ ↳ ↳ Re: need help. tables

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-09T07:11:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A83FA81.E481EDA6@brazee.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <95vljj$del$1@hermes.enternet.co.nz> <95vsd9$uns$1@newssvr05-en0.news.prodigy.com>`

```
Terry Heinze wrote:

>     I would add one feature to all the methods of searching so far.  Before
> doing any of these types of searches, compare your previous search argument
> and search result with your current search argument.  You oftentimes can
> bypass the overhead of searching if what you're looking for is the same
> thing you just got done looking for last time.

Also, for a small table, sometimes it is more efficient to do a linear search
than a binary search just walking the table can be the best solution - but as
you say, not as efficient as no search.
```

##### ↳ ↳ Re: need help. tables

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-09T07:07:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A83F9B1.CAF3A870@brazee.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <95vljj$del$1@hermes.enternet.co.nz>`

```
Large variable length tables can often be re-engineered.   Sometimes the program
could be designed with match/merge logic instead.   Or keyed files or database
records...

Such tables can either waste tremendous amounts of space, can be in danger of
overflow, or both.

Aborts 2 years after you wrote the program due to overflow can do weird and
costly things.
```

#### ↳ Re: need help. tables

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-02-09T09:11:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz>`

```
On Fri, 09 Feb 2001 07:56:30 +0000, Richard Plinston wrote:

>Ed Stevens wrote:
>> --
…[40 more quoted lines elided]…
>that:

I don't agree with you here. The space allocated will be the total space of
the first 01 level, in case of the example 9 bytes. The compiler will give a
warning that the size of the redefine is not equal to the original size and
that's it. You add new 05 levels under the first 01 level and without
changing anything else you're up and running. Not one byte of data storage
wasted, just a little overhead when calculating the tablesize.
>
>> 01 xxx-list.
…[18 more quoted lines elided]…
>don't waste resources.

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

##### ↳ ↳ Re: need help. tables

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-02-10T02:32:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<960u5k$foq$2@hermes.enternet.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es>`

```

Willem Clements wrote in message ...

>I don't agree with you here. The space allocated will be the total space of
>the first 01 level, in case of the example 9 bytes.
<snipped>

Willem,

your post made me think again. I believe you are correct. I offer an
unreserved apology to the original poster.

I still don't like it, but I have to admit that both Richard and myself were
wrong here.
It may be that our joint experience has been with compilers which won't
ALLOW you to have an invalid redefinition and therefore it wouldn't work
UNLESS you originally defined 30,000 bytes.

Given that the compiler accepts it with just a warning, I agree with what
you say.

Pete.
```

###### ↳ ↳ ↳ Re: need help. tables

- **From:** Ed Stevens <ed.stevens@home.com>
- **Date:** 2001-02-09T17:23:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961918$8ed$1@nnrp1.deja.com>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz>`

```
In article <960u5k$foq$2@hermes.enternet.co.nz>,
  "Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
<snip>
>
> your post made me think again. I believe you are correct. I offer an
> unreserved apology to the original poster.
>
> I still don't like it, but I have to admit that both Richard and
myself were
> wrong here.
> It may be that our joint experience has been with compilers which
won't
> ALLOW you to have an invalid redefinition and therefore it wouldn't
work
> UNLESS you originally defined 30,000 bytes.
>
> Given that the compiler accepts it with just a warning, I agree with
what
> you say.
>
> Pete.
>
>
```

###### ↳ ↳ ↳ Re: need help. tables

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-10T11:06:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A85209A.756E46C2@Azonic.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz>`

```
Peter E. C. Dashwood wrote:
> 
> I still don't like it, but I have to admit that both Richard and myself were
> wrong here.

That is quite arrogant of you to attribute wrongness to me.  You may
claim yourself to be wrong as much as you like, but I know that I am
correct insofar as my compiler goes.  If other compilers deal with
non-standard code in different ways then this emphasises why the code
should not be used.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-02-10T13:18:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9624mj$hd1$1@hermes.enternet.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz> <3A85209A.756E46C2@Azonic.co.nz>`

```
Oops! Sorry Richard, I forgot that getting anything wrong is NOT part of
your vocabulary.

As we were both in complete agreement on this particular subject it is very
hard to see how one of us could be wrong and NOT the other.

In my "arrogance" I figured you would also accept that it is not WHO's right
that matters, but WHAT's right.

Guess I got THAT wrong too...

It just isn't my day...<sigh>

Pete.

Richard Plinston wrote in message <3A85209A.756E46C2@Azonic.co.nz>...
>Peter E. C. Dashwood wrote:
>>
>> I still don't like it, but I have to admit that both Richard and myself
were
>> wrong here.
>
…[4 more quoted lines elided]…
>should not be used.
```

###### ↳ ↳ ↳ Re: need help. tables

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-13T17:52:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A897471.CEE2F84B@Azonic.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz>`

```
Peter E. C. Dashwood wrote:
> 
> Willem Clements wrote in message ...
…[3 more quoted lines elided]…
> <snipped>

> It may be that our joint experience has been with compilers which won't
> ALLOW you to have an invalid redefinition and therefore it wouldn't work
…[3 more quoted lines elided]…
> you say.

I just checked this with the Fujitsu compiler version 4.  It also issues
a warning but (as with MF) allocates the 30,000 bytes in spite of the
original area being 9 bytes.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-02-14T01:11:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96baun$vrp$1@hermes.enternet.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz> <3A897471.CEE2F84B@Azonic.co.nz>`

```
OK, Richard.

Your point is taken <G>.

I haven't tried it with V5 or 6 but I expect it does the same.

So, my statement needs to be modified so that it spells out exactly what it
was meant to imply:
>>
>> Given that the compiler accepts it with just a warning, I agree with what
>> you say.

has to become...

>>
>> Given that the compiler accepts it with just a warning (AND DOES NOT
ALLOCATE THE 30,000 bytes), I agree with what
>> you say.

Richard has pointed out that some compilers give a warning but still
allocate 30,000 bytes; Willem says his gives a warning and DOESN'T allocate
30,000 bytes (it allocates the original 9 bytes)

I say, who gives a shit?; I wouldn't do it anyway...<G>

I wonder which compiler Willem is using...? No...I don't...<G>

Positively last post on this....

Pete.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-02-14T01:38:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96bcfk$vu4$1@hermes.enternet.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz> <3A897471.CEE2F84B@Azonic.co.nz>`

```
OK, Richard.

Your point is taken. (I also promise never to include you in any apologies I
may make in the future, even in the fairly unusual event that we are in
total
agreement <G>)

I haven't tried it with V5 or V6 but I expect they do the same.

So, my statement needs to be modified so that it spells out exactly what it
was meant to imply:
>>
>> Given that the compiler accepts it with just a warning, I agree with what
>> you say.

has to become...

>>
>> Given that the compiler accepts it with just a warning (AND DOES NOT
ALLOCATE THE 30,000 bytes), I agree with what
>> you say.

Richard has pointed out that some compilers only give a warning but still
allocate 30,000 bytes; Willem says his gives a warning and DOESN'T allocate
30,000 bytes (it allocates the original 9 bytes).

Richard has, quite properly, asked him to prove it...

I say, who cares?; I wouldn't do it anyway...<G>

I wonder which compiler Willem is using...? No...I don't...interesting to
know though...No, it isn't!...get a Life! <G>

Positively last post on this....

Pete.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 5)_

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-02-25T21:32:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pRem6.970$aw5.1842@www.newsranger.com>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <960u5k$foq$2@hermes.enternet.co.nz> <3A897471.CEE2F84B@Azonic.co.nz> <96bcfk$vu4$1@hermes.enternet.co.nz>`

```
One final note. Sometimes, when using tables, it's advantagous to know the hir
frequency expected for each element in the table. For example, a retail company
may have seasonal items whose sales activity occurs in a 1 or 2 month window.

In this case, IF statements referencing those months before doing the table
search could drasticly reudce the CPU time spent searching the table.

Jack.   





In article <96bcfk$vu4$1@hermes.enternet.co.nz>, Peter E. C. Dashwood says...
>
>OK, Richard.
…[38 more quoted lines elided]…
>
```

##### ↳ ↳ Re: need help. tables

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-10T01:51:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A849EB2.734AD5C4@Azonic.co.nz>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es>`

```
Willem Clements wrote:

> >> refer to as the "self-adjusting table."
> >> =======
…[21 more quoted lines elided]…
> wasted, just a little overhead when calculating the tablesize.

First of all your code is invalid according to -85 rules where
"..neither the original definition nor the redefinition can include an
item whose size is variable as defined in the OCCURS clause.".

MF extensions allow this though, as may others.

The -85 rules also includes the note: "It is important to observe that
the REDEFINES specifies the redefinition of a storage area, not of the
data items occupying the area."

In all compilers that I have used a redfinition at the record (01)
level, whether implicit (FD) or explicit makes the storage area the size
of the largest record.

Running a compile right now of the above code allocated a fixed area of
30,000 bytes.  Changing the logical size of the area by setting the
depending on does not change the size of the area dynamically.

What confirmation, by such means as memory maps, dumps, etc have you
that shows that your compiler does not generate a 30k area ?
```

###### ↳ ↳ ↳ Re: need help. tables

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-02-09T17:44:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <3A849EB2.734AD5C4@Azonic.co.nz>`

```
On Sat, 10 Feb 2001 01:51:46 +0000, Richard Plinston wrote:

>Willem Clements wrote:
>
…[44 more quoted lines elided]…
>that shows that your compiler does not generate a 30k area ?

I agree with you on the implicit define, but I'm pretty sure that the IBM VSE
Cobol compiler allocates the storage based on the original define, not on the
redefine, of course other compilers may behave differently.
I haven't got any proof, because I don't have access to a mainframe anymore
(it took up too much space in the living room)

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-09T12:28:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961cvi$vnp$1@slb4.atl.mindspring.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <3A849EB2.734AD5C4@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es>`

```

"Willem Clements" <willem@horizontes-informatica.com> wrote in message
news:jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es...
> On Sat, 10 Feb 2001 01:51:46 +0000, Richard
 <snip>
> I agree with you on the implicit define, but I'm pretty sure that the IBM
VSE
> Cobol compiler allocates the storage based on the original define, not on
the
> redefine, of course other compilers may behave differently.
> I haven't got any proof, because I don't have access to a mainframe
anymore
> (it took up too much space in the living room)
>

I don't remember what happens with the old DOS/VS COBOL compiler - but with
VS COBOL II and "later" - I think you will find that you get a compile-time
error if you try and redefine a smaller (original) item with a larger
redefinition (at the 01-level)
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-09T11:53:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A843C96.46075268@brazee.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <3A849EB2.734AD5C4@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es> <961cvi$vnp$1@slb4.atl.mindspring.net>`

```

"William M. Klein" wrote:

> I don't remember what happens with the old DOS/VS COBOL compiler - but with
> VS COBOL II and "later" - I think you will find that you get a compile-time
> error if you try and redefine a smaller (original) item with a larger
> redefinition (at the 01-level)

I don't know how serious that error is, but going the other way I have this
with CoBOL for MVS.  The error is in a vendor supplied copy member:

3200  IGYDS1073-I   "BL-LINE-ITEM" redefined a larger item.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-09T16:07:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961plq$di5$1@slb6.atl.mindspring.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <3A849EB2.734AD5C4@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es> <961cvi$vnp$1@slb4.atl.mindspring.net> <3A843C96.46075268@brazee.net>`

```
Redefining a larger by a smaller item is fully ANSI conforming - and your
compiler *must* support it.  It is only redefining a smaller by a larger
that is a problem.
```

###### ↳ ↳ ↳ Re: need help. tables

_(reply depth: 5)_

- **From:** Ed Stevens <ed.stevens@home.com>
- **Date:** 2001-02-09T20:55:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961lf6$klm$1@nnrp1.deja.com>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8hu2r0.pminews@news.wanadoo.es> <3A849EB2.734AD5C4@Azonic.co.nz> <jvyyrzubevmbagrfvasbezngvpnpbz.g8ihtj2.pminews@news.wanadoo.es> <961cvi$vnp$1@slb4.atl.mindspring.net>`

```
In article <961cvi$vnp$1@slb4.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
>
<snip>
> I don't remember what happens with the old DOS/VS COBOL compiler - but
with
> VS COBOL II and "later" - I think you will find that you get a
compile-time
> error if you try and redefine a smaller (original) item with a larger
> redefinition (at the 01-level)
…[5 more quoted lines elided]…
>
```

#### ↳ Re: need help. tables

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-10T01:11:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mz0h6.3597$ZJ5.300609@newsread2.prod.itd.earthlink.net>`
- **References:** `<95m7c4$kia$1@nnrp1.deja.com> <3A7FE2F1.57469509@Azonic.co.nz> <95p8mf$abu$1@nnrp1.deja.com> <3A803836.5DBF074E@home.com> <95u8vh$lm1$1@nnrp1.deja.com> <3A83A2AE.DFD8CB38@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz
>
> Yes, I have to adjust the OCCURS, but I could use 78s to do that.  I
> don't waste resources.
>

On the other hand, if you have a resource available to you - in this
case memory - and you DON'T use it, you have wasted an opportunity
that can never be reclaimed.

"Use it or lose it" is sometimes a good rule.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
