[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODO Demo

_14 messages · 6 participants · 2011-11_

---

### ODO Demo

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-11-02T22:12:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com>`

```

This is a program to demonstrate the use of ODO with sort
and intrinsic functions. The Micro Focus compiler used dates
from 1994, but did receive some updates in 1995.

For this simple sort, the SORT statement matches the 2002
standard.

Note that loops and intemediate data items would be required
to obtain the same results as the sort and intrinsic functions.
This would turn 54 lines into several hundred.

=====
       identification division.
       program-id. odo-demo.
      *demonstrates ODO with sort and intrinsic functions
       data division.
       77 odo-count comp pic 9(4) value 10.
       1 odo-group.
        2 odo-table
           occurs 1 to 10 times
           depending on odo-count.
         3 odo-entry pic 9.
       77 result pic z9.
       procedure division.
       begin.
           initialize odo-group
           move 5 to odo-count
           move 9 to odo-entry (1)
           move 7 to odo-entry (2)
           move 5 to odo-entry (3)
           move 3 to odo-entry (4)
           move 1 to odo-entry (5)
           perform display-entries
           sort odo-table
               ascending odo-entry
           perform display-entries
           perform intrinsic-functions
           stop run
           .

       display-entries.
           display odo-entry (1) space
                   odo-entry (2) space
                   odo-entry (3) space
                   odo-entry (4) space
                   odo-entry (5)
           .

       intrinsic-functions.
           compute result = function max (odo-entry (all))
           display result space "max"
           compute result = function mean (odo-entry (all))
           display result space "mean"
           compute result = function median (odo-entry (all))
           display result space "median"
           compute result = function midrange (odo-entry (all))
           display result space "midrange"
           compute result = function ord-max (odo-entry (all))
           display result space "ord-max"
           compute result = function ord-min (odo-entry (all))
           display result space "ord-min"
           compute result = function range (odo-entry (all))
           display result space "range"
           compute result = function sum (odo-entry (all))
           display result space "sum"
           .
=====
9 7 5 3 1
1 3 5 7 9
 9 max
 5 mean
 5 median
 5 midrange
 5 ord-max
 1 ord-min
 8 range
25 sum
=====
```

#### ↳ Re: ODO Demo

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-11-04T02:08:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hfi1sFtqoU1@mid.individual.net>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com>`

```
Rick Smith wrote:
> This is a program to demonstrate the use of ODO with sort
> and intrinsic functions. The Micro Focus compiler used dates
…[75 more quoted lines elided]…
> =====

Good job, Rick!

It is impressive.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: ODO Demo

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-11-04T08:18:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net>`

```
On Nov 3, 8:08 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Rick Smith wrote:
> > This is a program to demonstrate the use of ODO with sort
…[9 more quoted lines elided]…
>
[Program snipped]
>
> Good job, Rick!
>
> It is impressive.

Perhaps you might clarify what you mean by impressive,
or not. <g>

There may be some who may think "I forgot about that"
or "I didn't know that" or "I could have used ...",
but I can't think of anything that would rise to the
level of "impressive".

Anyway, it seems this a continuation of comments made
in March 2008 while discussing ODO. The lead-in was
the value of ODO when using SEARCH and SEARCH ALL.

< http://groups.google.com/group/comp.lang.cobol/msg/484596fb50366bc8?hl=en
>
=====

"Rick Smith" <ricksm...@mfi.net> wrote in message
news:13teonpobo7kve4@corp.supernews.com...
> "Pete Dashwood" <dashw...@removethis.enternet.co.nz> wrote in message
> news:63p2sfF28n6tgU1@mid.individual.net...

>> Next point?

> Intrinsic functions using the ALL subscript will work with
> ODO tables, but likely will not give the correct result when
> using fixed length tables with a variable number of items.

> MAX, MEAN, MEDIAN, MIDRANGE, MIN,
> ORD-MAX, ORD-MIN, PRESENT-VALUE,
> RANGE, STANDARD-DEVIATION, SUM, and
> VARIANCE are those affected.

Fair enough.

Again, facilities I wouldn't use often enough to lose sleep
over... :-)

I don't think I've ever used ALL as a subscript, and MAX, MIN, and SUM
seem
more like SQL to me than COBOL... (I have used those in SQL...). So it
looks
to me as if my COBOL use may be "limited", notwithstanding the fact I
used
it successfully for decades. :-)

=====

For my part, assessing the value ODO for SEARCH and
SEARCH ALL is old and trivial, in comparison with its
value for intrinsic functions.

The bottom-line, simply, is that wholesale rejection
of ODO makes parts of COBOL unavailable, while general
acceptance of ODO gives access to all parts of the
language. Therefore, use of ODO should be encouraged;
not discouraged. <g>
```

###### ↳ ↳ ↳ Re: ODO Demo

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-11-05T12:13:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hj9t5Fu1U1@mid.individual.net>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com>`

```
Rick Smith wrote:
> On Nov 3, 8:08 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[19 more quoted lines elided]…
> or not. <g>

OK. When I looked through the code you posted I was impressed. It is clean, 
simple, and quite elegant.

Even if I might never have the need to use it, I can appreciate (and be 
impressed) by good code when I see it.

For me this comes in that category.

When I was usng COBOL I would not have used this approach, mainly because I 
wasn't aware of it, but also because I have established ways of dealing with 
tables in COBOL which have proven themselves adequate to my needs over 
years. I don't know if  subscripting with ALL was/is available with 
non-Micro Focus implementations and I haven't used Micro Focus for actual 
production work since the days of 16 bit Workbench, DIALOG, and PANELS.
>
> There may be some who may think "I forgot about that"
…[3 more quoted lines elided]…
>
I hope I have clarified this above.

The other thing I found impressive was that this was in response to the 
challenge of swapping fields in COBOL without intermediate storage. In that 
context it is a creative solution and I'm always impressed by creativity and 
imagination. :-)

> Anyway, it seems this a continuation of comments made
> in March 2008 while discussing ODO. The lead-in was
…[26 more quoted lines elided]…
> over... :-)

THERE IT IS...!

I hardly ever have used SEARCH...ALL in COBOL so, for me at least, it isn't 
of pressing importance.

Nowadays I don't use COBOL at all for development.  But, I still have a 
"soft spot" for COBOL after using it for decades, and I am helping people 
remove their dependency on it so it is still of passing interest to me.

>
> I don't think I've ever used ALL as a subscript, and MAX, MIN, and SUM
…[17 more quoted lines elided]…
> not discouraged. <g>

No, I don't advocate making it unavailable. I was one of the few who 
resisted the removal of ALTER from the language, even though by then I had 
no use for it myself. I don't think ANYTHING should be 'unavailable' but I 
am allowed to have an opinion about what I think is useful or not. (And 
others are perfectly free to disagree; it is a discussion forum, not Holy 
Writ or dogma)

Rejecting (or embracing) ODO use is a matter for individuals, just like 
everything else. I have never advocated removing it from the language.

You have shown (very persuasively) that there are some occasions where ODO 
can be useful.

My position has been shifted to the point where I must grant that. :-)

However, I still wouldn't use it. The occasions you have presented are cases 
which I would rarely use and I already have adequate means of dealing with 
them in COBOL, which do not require use of ODO.

In general, I consider it a useless construct that simply causes more 
trouble than it is worth.

But that, (as was recently pointed out) is merely opinion.:-), and, having 
seen your code, I am not as strongly persuaded against it as I was.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 4)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-11-04T19:09:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c461635-df35-4273-a5f7-153eeeb4dcaa@hc5g2000vbb.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net>`

```
On Nov 4, 6:13 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Rick Smith wrote:

> > Perhaps you might clarify what you mean by impressive,
> > or not. <g>
>
> OK. When I looked through the code you posted I was impressed. It is clean,
> simple, and quite elegant.

Be less impressed, please! There was an error of omission.
I failed to include MIN. <g>


> The other thing I found impressive was that this was in response to the
> challenge of swapping fields in COBOL without intermediate storage. In that
> context it is a creative solution and I'm always impressed by creativity and
> imagination. :-)

While it is possible to use a table SORT to conditionally
swap entries in a two entry table and without intermediate
storage, my response was tangential, which is why I changed
the subject. <g>
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-11-04T21:56:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> OK. When I looked through the code you posted I was impressed. It is
…[14 more quoted lines elided]…
>>

I can't see much use for ODO inasmuch as the compiler reserves as much room 
as the largest entry; with one exception.

If you desire to write a variable length record (at least in Fujitsu) it 
comes in handy. Without it, the FJ compiler writes the full record, padded 
with spaces. For example:

01  MYREC.
  02  MYDATA            PIC X(10000).

MOVE 'A' TO MYDATA.
WRITE MYREC.

Will write a 10,000 byte record. Whereas:

01  MYREC.
  02  MYDATA.
    05  FILLER OCCURS 1 TO 10000 DEPENDING ON RECORD-LEN PIC X.

MOVE 1 TO RECORD-LEN.
MOVE 'A' TO MYDATA
WRITE MYREC

writes a 1-byte record.
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 5)_

- **From:** Robert <0robert.jones@gmail.com>
- **Date:** 2011-11-05T03:26:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ed97030c-b473-4b03-b659-fa1fd62a52a0@hc5g2000vbb.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com>`

```
On Nov 5, 2:56 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Pete Dashwood wrote:
>
…[39 more quoted lines elided]…
> writes a 1-byte record.

SEARCH and SORT should also work better with ODO

Robert
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 5)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-11-08T09:10:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d404ac2-e943-4ce3-b609-57d227edce72@u5g2000vbd.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com>`

```
On Nov 4, 9:56 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:

> I can't see much use for ODO inasmuch as the compiler reserves as much room
> as the largest entry; with one exception.

"compiler reserves" is a misnomer when it is, in fact,
"programmer reserves" and without exception.

There are two uses of ODO to consider: table of records
and table of characters.

For table of records, ODO will limit the number of elements
examined for SEARCH, SEARCH ALL, SORT (2002), and intrinsic
functions.

For table of characters (or character array), ODO will limit
the size of the data item when used as a sending or receiving
field for MOVE, STRING, UNSTRING, DISPLAY, etc.

> If you desire to write a variable length record (at least in Fujitsu) it
> comes in handy. Without it, the FJ compiler writes the full record, padded
…[18 more quoted lines elided]…
> writes a 1-byte record.

The COBOL standard (1985) has the RECORD VARYING clause
to address this issue, but despite the similarities there
is no connection to ODO.

=====
       identification division.
       program-id. rec-var.
       environment division.
       input-output section.
       file-control.
           select var-file
               assign to "var-file.dat".
       data division.
       file section.
       fd var-file
           record varying
               from 1 to 10000
               depending on rec-len.
       1 myrec.
        2 mydata pic x(10000).
       working-storage section.
       77 rec-len comp pic 9(8) value 10000.
       procedure division.
       begin.
           open output var-file
           move "A" to mydata
           move 1 to rec-len
           write myrec
           close var-file
           stop run
           .
=====

This program writes a one character record without using ODO.

So, I guess from your initial statement you "can't
see much use for ODO" at all. <g>
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-11-08T10:37:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4722c021-2190-4371-8d0f-d32a5ba0898a@p20g2000prm.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com> <8d404ac2-e943-4ce3-b609-57d227edce72@u5g2000vbd.googlegroups.com>`

```
On Nov 9, 6:10 am, Rick Smith <rs847...@gmail.com> wrote:
> On Nov 4, 9:56 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
>
…[80 more quoted lines elided]…
> This program writes a one character record without using ODO.

What it would actually write is probably a record header containing
the size plus that one character and possibly some padding.


> So, I guess from your initial statement you "can't
> see much use for ODO" at all. <g>
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 7)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-11-08T11:40:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2d78fa43-4780-4f8f-a7fa-5e3819af6702@o5g2000yqa.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com> <8d404ac2-e943-4ce3-b609-57d227edce72@u5g2000vbd.googlegroups.com> <4722c021-2190-4371-8d0f-d32a5ba0898a@p20g2000prm.googlegroups.com>`

```
On Nov 8, 1:37 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Nov 9, 6:10 am, Rick Smith <rs847...@gmail.com> wrote:
>
…[36 more quoted lines elided]…
> the size plus that one character and possibly some padding.

Close! With the Micro Focus system I use, it is a 128 byte
file header, a 4 byte record header, a 1 character record,
and 3 bytes of padding.
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-11-08T10:30:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<228b26d7-a183-4126-a579-452e8dda3da0@t38g2000prg.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com>`

```
On Nov 5, 3:56 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Pete Dashwood wrote:
>
…[17 more quoted lines elided]…
> as the largest entry; with one exception.

Different people may see different things.

In other languages where there is dynamic memory the compiler usually
reserves an area called the heap which is used for data items as they
are created. This can be added to from system or virtual memory if
required. There is a cost in allocating this memory (alloc()) to
objects and a large cost in making objects larger (realloc()). This
heap can also become fragmented after many alloc()s and free()s
leading to wasted memory.

In some language systems there is a need for garbage collection which,
again, has a processing overhead, but without which the memory leakage
would become excessive.

OTOH ODO has almost zero processing overhead.


> If you desire to write a variable length record (at least in Fujitsu) it
> comes in handy. Without it, the FJ compiler writes the full record, padded
…[6 more quoted lines elided]…
> WRITE MYREC.

If you are talking about LINE SEQUENTIAL files then perhaps you
haven't discovered the environment variable:

    CBR_TRAILING_BLANK_RECORD=REMOVE

which, for Fujitsu COBOL since version 3, causes the program to only
write the length of record up to the last non-blank (plus line
terminator).

> Will write a 10,000 byte record. Whereas:
>
…[8 more quoted lines elided]…
> writes a 1-byte record.
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-11-09T02:49:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5cb95ce-d754-40aa-a923-e63c1651fe47@w1g2000vba.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com> <228b26d7-a183-4126-a579-452e8dda3da0@t38g2000prg.googlegroups.com>`

```
On Nov 8, 6:30 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Nov 5, 3:56 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> > Pete Dashwood wrote:
…[6 more quoted lines elided]…
>

Whoops. In comparison to garbage collection, you may be right.
However, ODO attracts considerable overheads in comparison to fixed
length data (ask any assembler programmer). However, whereas Pete may
abhor ODO, I love it (metaphorically speaking).
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-11-09T06:28:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u-dndFSV_Jl7CfTnZ2dnUVZ_uqdnZ2d@earthlink.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com> <228b26d7-a183-4126-a579-452e8dda3da0@t38g2000prg.googlegroups.com>`

```
Richard wrote:
>
>
…[18 more quoted lines elided]…
>

You're right. I completely overlooked that compiler directive. Thanks.
```

###### ↳ ↳ ↳ Re: ODO Demo

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-11-09T10:40:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<178a334b-7989-46c9-b8c4-ecc561372f19@j19g2000pro.googlegroups.com>`
- **References:** `<486e37ce-ba54-49c3-86a5-860968934671@eh5g2000vbb.googlegroups.com> <9hfi1sFtqoU1@mid.individual.net> <130409a5-15e7-4c3c-a43a-3ab2983575bf@x1g2000yqg.googlegroups.com> <9hj9t5Fu1U1@mid.individual.net> <E_2dncwJd8REOCnTnZ2dnUVZ_h2dnZ2d@earthlink.com> <228b26d7-a183-4126-a579-452e8dda3da0@t38g2000prg.googlegroups.com> <7u-dndFSV_Jl7CfTnZ2dnUVZ_uqdnZ2d@earthlink.com>`

```
On Nov 10, 1:28 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Richard wrote:
>
…[19 more quoted lines elided]…
> You're right. I completely overlooked that compiler directive. Thanks.

It's not a compiler directive, which would fix the program's behavior
at compile time. It is a run-time environment variable which affects
the behavior when the program executes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
