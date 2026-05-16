[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help

_31 messages · 17 participants · 1998-10 → 1998-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help

- **From:** Kelly Wakeley <kwake@cnetech.com>
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3637FC43.EF006A87@cnetech.com>`

```
If anyone can answer these please let me know.
              1.  If you move a I to a subscript, what will it contain?
              2.  If you set an index to 1, what will it contain?
              3.  A binary search is more efficient and saves time by?
              4.  What causes a SOC7 abend code?
              5.   What is used to relate files within the program to
JCL file descriptions?

I am trying to learn COBOL on my own and have come across these
questions that I can't seem to find the answers to.  They are probably
quite simple but i have yet to understand them.  Please feel free to
e-mail any suggestions.  Thank you.
```

#### ↳ Re: help

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7196dm$kcb$1@supernews.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com>`

```
As far as SOC7 check out this site.  It has tons of completion codes along
with what could be causing them.
http://isqs.ba.ttu.edu/classes/lieb/Ibmsysc1.htm#0C7
```

#### ↳ Re: help

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363b8caf.4344531@news-server>`
- **References:** `<3637FC43.EF006A87@cnetech.com>`

```
On Wed, 28 Oct 1998 21:25:23 -0800, Kelly Wakeley <kwake@cnetech.com>
enlightened us:

>If anyone can answer these please let me know.
>              1.  If you move a I to a subscript, what will it contain?
                                       1
>              2.  If you set an index to 1, what will it contain?
                                       1
>              3.  A binary search is more efficient and saves time by?
                     It divides the array in half and either goes up
or down depending on the comparison.  It is efficient for very large
table/array searches where you might program the search to start at
the first entry and keep looking at the next until you get a match or
hit end of table.  If ,eg, your table contained 500,000 entries this
could take quite a lot of time.  Using a binary search you would find
the match or end much faster.  The caveat here is that the table is in
some logical order either ascending or descending.

>              4.  What causes a SOC7 abend code?
                      This is an MVS error and says you have a data
exception.  The primary cause of such an error, at least in the
MVS/VSE IBM mainframe world, is trying to perform arithemetic on a
field that does not contain numeric data, e.g., it contain alpha
characters or spaces or hex zeroes or other "garbage".  Note the data
must also be in packed format.


>              5.   What is used to relate files within the program to
>JCL file descriptions?
                      Select statements and FD entries.


>
>I am trying to learn COBOL on my own and have come across these
…[4 more quoted lines elided]…
>
Good luck.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Cats know how we feel. They don't give a damn, but they know.
 Steve
```

##### ↳ ↳ Re: help

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server>`

```
On Thu, 29 Oct 1998 15:53:52, swiegand@neo.rr.com (SkippyPB) wrote:

> On Wed, 28 Oct 1998 21:25:23 -0800, Kelly Wakeley <kwake@cnetech.com>
> enlightened us:
…[5 more quoted lines elided]…
>                                        1

You fail the test! <G>
Answer 2 is incorrect.
```

###### ↳ ↳ ↳ Re: help

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3638AF80.5C31@compaq.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>`

```
You may all fail the test depending on the implementation.  In some it 
is one "span". In some it is zero.  In some it is one.
```

###### ↳ ↳ ↳ Re: help

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298301.81464.25763@kcbbs.gen.nz>`
- **References:** `<Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>`

```
In message <<Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>> redsky@ibm.net  writes:
> 
> > On Wed, 28 Oct 1998 21:25:23 -0800, Kelly Wakeley <kwake@cnetech.com>
…[9 more quoted lines elided]…
> Answer 2 is incorrect.

Actually answer 2 may be correct or incorrect or irrelevant
depending on far too many thing to identify here, but
including:
       Compiler vendor
       machine environment
       compiler options settings
       compiler version
       
It may be incorrect for your particular combination of
these, but may be correct for other's.  

A compiler that uses INDEXes as a numeric type as if they
were subscripts will still conform exactly to the standard.
```

###### ↳ ↳ ↳ Re: help

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3638A020.9F819A9A@home.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>`

```
> > >If anyone can answer these please let me know.
> > >              1.  If you move a I to a subscript, what will it contain?
…[5 more quoted lines elided]…
> Answer 2 is incorrect.


And answer #1 is correct?  How did you find out what the value is of the
variable I?
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-edbemwWXTMvd@Dwight_Miller.iix.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <3638A020.9F819A9A@home.com>`

```
On Thu, 29 Oct 1998 17:04:32, Howard Brazee <NOSPAMbrazee@home.com> 
wrote:

> > > >If anyone can answer these please let me know.
> > > >              1.  If you move a I to a subscript, what will it contain?
…[9 more quoted lines elided]…
> variable I?

I read the l as 1.  

This Week's COBOL Tip:
Alter is the most powerful Verb in COBOL, and if ever use it
you may find your employment status altered.
```

###### ↳ ↳ ↳ An ALTER Horror Story (was: Re: help)

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71ab6q$hbo$1@mail.pl.unisys.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <3638A020.9F819A9A@home.com> <Jl0PnHJ5PvPd-pn2-edbemwWXTMvd@Dwight_Miller.iix.com>`

```
The worst COBOL program I ever saw was a cross-reference-and-flowchart
utility for COBOL source programs written by a programmer who was clearly
fluent in FORTRAN, and who had equally clearly decided to make maximum use
of COBOL's ALTER verb presumably because using it was intellectually
stimulating.

Sometime after it was written, the flowcharting part was disabled and
largely ripped out, but the nature of the program was such that significant
pieces of this logic remained in odd corners of the program.

I actually managed to patch the program to correct a problem I encountered
with it, but nobody else could figure out well enough how the program worked
to permit the patch to be peer-reviewed.  Ultimately the problem was
circumvented by documenting it ...

    -Chuck Stevens

Thane Hubbell wrote :

>This Week's COBOL Tip:
>Alter is the most powerful Verb in COBOL, and if ever use it
>you may find your employment status altered.
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 5)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3638b12c.0@news1.ibm.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <3638A020.9F819A9A@home.com> <Jl0PnHJ5PvPd-pn2-edbemwWXTMvd@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Thu, 29 Oct 1998 17:04:32, Howard Brazee <NOSPAMbrazee@home.com>
>> > > >              1.  If you move a I to a subscript, what will it
contain?
>I read the l as 1.
>
>This Week's COBOL Tip:
>Alter is the most powerful Verb in COBOL, and if ever use it
>you may find your employment status altered.


Go To is the 2nd-most powerful verb. And both Alter and Go To
are much too powerful for normal use.
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 5)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363ae164.4338313@news-server>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <3638A020.9F819A9A@home.com> <Jl0PnHJ5PvPd-pn2-edbemwWXTMvd@Dwight_Miller.iix.com>`

```
On 29 Oct 98 19:23:52 GMT, redsky@ibm.net (Thane Hubbell) enlightened
us:

>On Thu, 29 Oct 1998 17:04:32, Howard Brazee <NOSPAMbrazee@home.com> 
>wrote:
…[18 more quoted lines elided]…
>you may find your employment status altered.

Yeah, I read the I in #1 as a 1.  In fact, you cannot move I to a
subscript at least in the MVS/VSE Mainframe world.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Think. It's good practice for when the computer is down.
 Steve
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71cpom$vuv$1@callisto.clark.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <3638A020.9F819A9A@home.com> <Jl0PnHJ5PvPd-pn2-edbemwWXTMvd@Dwight_Miller.iix.com> <363ae164.4338313@news-server>`

```
In article <363ae164.4338313@news-server>,
SkippyPB <swiegand@neo.rr.com> wrote:
>On 29 Oct 98 19:23:52 GMT, redsky@ibm.net (Thane Hubbell) enlightened
>us:
…[20 more quoted lines elided]…
>subscript at least in the MVS/VSE Mainframe world.

Oh dear... consider:

01  I    PIC 99 VALUE 10.
01  SUB1 PIC 99 VALUE ZEROES.

MOVE I TO SUB1.

... are you confusing I with 'I'?

DD
```

###### ↳ ↳ ↳ Re: help

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363FE3B4.E4A@bellsouth.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Thu, 29 Oct 1998 15:53:52, swiegand@neo.rr.com (SkippyPB) wrote:
…[13 more quoted lines elided]…
> 

What about question 2?  I thought it was 1, but I found this in my very
first COBOL textbook:
"Indexes contain displacement values, whereas subscripts are used for
the storage of occurrence numbers.  Displacement refers to the number of
positions away from the starting position of the table."

So, if you set an index to 1, is it zero?  And if the picture clause is
PIC X(5), if you set index up by 1, will the index contain 5?  

If you put 'THIS-INDEX     USAGE IS INDEX' in Working-Storage instead of
using 'OCCURS 25 TIMES INDEXED BY THIS-INDEX' and you say 'SET
THIS-INDEX TO 1' (in working-storage), can you display the contents of
THIS-INDEX?  (I was gonna try this today but our system was down.)
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71pl8u$f13$1@news.igs.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net>`

```

Kitty Carr wrote in message <363FE3B4.E4A@bellsouth.net>...

>So, if you set an index to 1, is it zero?  And if the picture clause is
>PIC X(5), if you set index up by 1, will the index contain 5?


A data name, usage index, is just a data representation that is best
for subscripting for a specific machine implementation. Probably
16 or 32 bit binary.

A table index could be anything that the compiler designer decides,
from an offset like you mention, to an actual memory address, to
a fairly standard subscript type of value.
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 4)_

- **From:** "Thane Hubbell" <redsky@ibm.net>
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be07ae$66f3a4e0$f7bc48a6@default>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net>`

```


Kitty Carr <kcarr1@bellsouth.net> wrote in article
<363FE3B4.E4A@bellsouth.net>...
> Thane Hubbell wrote:
> > 
…[6 more quoted lines elided]…
> > > >              1.  If you move a I to a subscript, what will it
contain?
> > >                                        1
> > > >              2.  If you set an index to 1, what will it contain?
…[20 more quoted lines elided]…
> 

A usage index item set to 1 will have a value of 1.  However, an INDEX to a
table, which is a related but different animal will have a value of ???? -
who cares - the vendor/platform determine the contents, and it is one
(usually) that is most efficient for access.

You can USE a Usage Index item to determine WHAT value is in the index
however.

IE:

01  The-Table.
      03  Table-Element Pic X(5) Occurs 5 times Indexed by Table-Index.
01  Index-Value Usage Index.  (No picture clause).

You can then MOVE this value to a field - ala:

Set Index-Value to Table-Index
Move Index-Value to Pic-9-item
Display Pic-9-item.

some compilers I played with had 'strange' values in there, but most had an
absolute character offset in the table.  IE when the Table-Index was set to
3 and Index-Value was set to Table-Index, the value of Index-Value was 11.

Go figure.

The bottom like is that if you set an index to a value, it may not ACTUALLY
contain that value.
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MgW%1.12$Tk.29140@news2.mia.bellsouth.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <01be07ae$66f3a4e0$f7bc48a6@default>`

```
Thane Hubbell wrote:
>
>01  The-Table.
…[7 more quoted lines elided]…
>Display Pic-9-item.

You should not be able to move a USAGE IS INDEX field to anywhere, or
to SET it to anything but to an INDEX NAME or another USAGE IS INDEX
field.  To check it out, I ran the above syntax with Micro Focus and
it flagged this:

               Move Index-Value to Pic-9-item
    *  49-S********************
    **    Illegal use of Index-name or Index Data-item

You get a similar error if you try this:

               Set Pic-9-item to Index-Value
    * 307-S*********************************
    **    Wrong combination of data-types

This makes sense, because the value of an index data item is only
meaningful when associated with a specific table.
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-lhV4e11kqgDG@Dwight_Miller.iix.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <01be07ae$66f3a4e0$f7bc48a6@default> <MgW%1.12$Tk.29140@news2.mia.bellsouth.net>`

```
On Wed, 4 Nov 1998 10:47:08, "Judson McClendon" 
<judmc123@bellsouth.net> wrote:

> 
> You should not be able to move a USAGE IS INDEX field to anywhere, or
> to SET it to anything but to an INDEX NAME or another USAGE IS INDEX
> field.  To check it out, I ran the above syntax with Micro Focus and
> it flagged this:


Whoops.  You are right.  Here's some interesting stuff.

Identification Division.
Program-Id.  Test4.
Environment Division.
Configuration Section.
Data Division.
Working-Storage Section.
01 THE-TABLE.
   03  TABLE-ENTRIES PIC X(5) OCCURS 20 TIMES INDEXED BY FIELD-4.
01 FIELD-2 USAGE INDEX.
Procedure Division.
test-4-start.
    SET FIELD-4 TO 10
    SET FIELD-2 TO FIELD-4
    DISPLAY FIELD-2
    Stop Run
    .


Under Realia this program displays a 00045.

Under VMS you have to say Display Field-2 with Conversion and it 
displays 10.

It won't compiler under MVS COBOL for this and that.

Under Fujitsu 3.0 - 16 and 32 bit  - it displays 000000045


I can't get "at" the value under MVS - but I can store it in a file!
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 4)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364141E0.7082B9F5@att.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net>`

```
Kitty Carr wrote:
> 
(snip)
> What about question 2?  I thought it was 1, but I found this in my very
> first COBOL textbook:
…[10 more quoted lines elided]…
> THIS-INDEX?  (I was gonna try this today but our system was down.)

I think this is a good example where understanding S/360+ Assembler
helps. In my mind (and I suspect this is correct) a COBOL index (e.g.,
blah-blah-blah  occurs many times indexed by in-dex) is an Assembler
index register. This means that the value of the index to the first
occurrence is zero. If the table entry is 128 (decimal) bytes long, the
index (register) will contain 128 (decimal) for the 2nd entry, 256 for
the 3rd, 368 for the 4th, etc. 'Don't recall seeing any indexes in a
dump, just at Xpediter breakpoints (where Xpediter doesn't show the raw
contents of the index, but interprets it for us).

Bill Lynch
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 5)_

- **From:** Kitty Carr <kcarr1@bellsouth.net>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36428B4D.3E09@bellsouth.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <364141E0.7082B9F5@att.net>`

```
William Lynch wrote:
> 
> Kitty Carr wrote:
…[26 more quoted lines elided]…
> Bill Lynch

And I've beat this horse to death!  From a 1977 book, "The actual
contents of the index are compiler dependent.  In System/370, the index
contains the relative byte location of the element within the table. 
Indexes make debugging harder, because they cannot appear in Display or
Exhibit statements."  I've been playing with these indexes for the past
few days at work, because I'm having problems dialing in from home.  So
now when my boss walks by he asks me 'are you doing real work?  Or still
obsessing on indexes?'  'You knew I was obsessive when you hired me 20
years ago.'  'Yeah, but we thought you'd change.'  'After 20 years? 
What real work have you got for me?'  'We're out of coffee.'

When I first came to work here, our mainframe was a 370.  Big, blue,
knobs and dials.  Is that what is meant by System/370?  Why now do we
have COBOL/370?  Is there a tie-in somewhere, or does IBM just lack
imagination?
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-3l8q5drbCVEL@Dwight_Miller.iix.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <364141E0.7082B9F5@att.net> <36428B4D.3E09@bellsouth.net>`

```
On Fri, 6 Nov 1998 03:45:11, Kitty Carr <kcarr1@bellsouth.net> wrote:

> When I first came to work here, our mainframe was a 370.  Big, blue,
> knobs and dials.  Is that what is meant by System/370?  Why now do we
> have COBOL/370?  Is there a tie-in somewhere, or does IBM just lack
> imagination?

370 was the address you put in the dial to IPL.

We have 2 OS/390 machines here at the present - and I can't find that 
darn dial on either one.
```

###### ↳ ↳ ↳ help needed

_(reply depth: 6)_

- **From:** Wei Lu <luw@me.udel.edu>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.95.981106002131.1739A-100000@me.udel.edu>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <364141E0.7082B9F5@att.net> <36428B4D.3E09@bellsouth.net>`

```
hi, could you tell me 

where I could download the good utilities/softwares for COBOL
compile/debug/run  ?
good web-site for COBOL , DB2, CICS ?

THANKS,
```

###### ↳ ↳ ↳ Re: help needed

_(reply depth: 7)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364518ce.3824041@news-server>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <363b8caf.4344531@news-server> <Jl0PnHJ5PvPd-pn2-ySDdqFQYB6bn@Dwight_Miller.iix.com> <363FE3B4.E4A@bellsouth.net> <364141E0.7082B9F5@att.net> <36428B4D.3E09@bellsouth.net> <Pine.SOL.3.95.981106002131.1739A-100000@me.udel.edu>`

```
On Fri, 6 Nov 1998 00:21:49 -0500, Wei Lu <luw@me.udel.edu>
enlightened us:

>hi, could you tell me 
>
…[5 more quoted lines elided]…
>

Hah!  I see the student we bashed many postings ago is back!!

Check the FAQ.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Q:  What was the first question they asked Linda Tripp at her make over?
A:  Paper or plastic!

 Steve
```

###### ↳ ↳ ↳ Re: help needed

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<729v4u$8ik$1@clarknet.clark.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <364141E0.7082B9F5@att.net> <36428B4D.3E09@bellsouth.net> <Pine.SOL.3.95.981106002131.1739A-100000@me.udel.edu>`

```
In article <Pine.SOL.3.95.981106002131.1739A-100000@me.udel.edu>,
Wei Lu  <luw@me.udel.edu> wrote:
>hi, could you tell me 
>
>where I could download the good utilities/softwares for COBOL
>compile/debug/run  ?
>good web-site for COBOL , DB2, CICS ?

Have your friend ask us, instead?

DD
```

#### ↳ Re: help

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71a7bg$pmh$1@clarknet.clark.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com>`

```
In article <3637FC43.EF006A87@cnetech.com>,
Kelly Wakeley  <kwake@cnetech.com> wrote:
>If anyone can answer these please let me know.
>              1.  If you move a I to a subscript, what will it contain?
…[7 more quoted lines elided]…
>questions that I can't seem to find the answers to.

Hmmmm... this is one step beyond 'do your own homework'... seems like
'pass your own interview'.

You're on your own.

DD
```

#### ↳ Re: help

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71908t$dg6@dfw-ixnews3.ix.netcom.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com>`

```
I CAN HELP!!

On Wed, 28 Oct 1998 21:25:23 -0800, Kelly Wakeley
<kwake@cnetech.com> wrote:

>If anyone can answer these please let me know.
>              1.  If you move a I to a subscript, what will it contain?
                      APPLES
>              2.  If you set an index to 1, what will it contain?
                      ORANGES
>              3.  A binary search is more efficient and saves time by?
                      USING APPLES INSTEAD OF ORANGES [*]
>              4.  What causes a SOC7 abend code?
                      COMPARING APPLES TO ORANGES
>              5.   What is used to relate files within the program to
>JCL file descriptions?
                      CHARACTER STRINGS
>
>I am trying to learn COBOL on my own and have come across these
>questions that I can't seem to find the answers to.  They are probably
>quite simple but i have yet to understand them.  Please feel free to
>e-mail any suggestions.  Thank you.

     YOU ARE WELCOME!

* -- I KNEW that you would see that the correct answer is the
reverse of this.  Just checking.
```

#### ↳ Re: help

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36395847.781398E1@att.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com>`

```
Kelly Wakeley wrote:
> 
> If anyone can answer these please let me know.
>               1.  If you move a I to a subscript, what will it contain?

Strictly speaking, you cannot move an I to a subscript, you must SET the
subscript to I. The contents will be the same, but expressed
differently. (I'm assuming you didn't intend this as a trick
question<g>)

HTH,
Bill Lynch
```

##### ↳ ↳ Re: help

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639CC72.160D7233@home.com>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <36395847.781398E1@att.net>`

```
I move values to subscripts all the time.  I set values to indices.

William Lynch wrote:
> 
> Kelly Wakeley wrote:
…[10 more quoted lines elided]…
> Bill Lynch
```

###### ↳ ↳ ↳ Re: help

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363C2A65.DA98CE87@att.net>`
- **References:** `<3637FC43.EF006A87@cnetech.com> <36395847.781398E1@att.net> <3639CC72.160D7233@home.com>`

```
Howard Brazee wrote:
> 
> I move values to subscripts all the time.  I set values to indices.
…[10 more quoted lines elided]…
> > differently.
(snip)

This turned into quite a thread. I took Kelly's statement to mean she
wanted to move an index (a I) to a subscript. In the MVS/COBOL II world
(at least) a field with USAGE INDEX is not legal in any move, see the
clips below:

 -------  Defining the index (I) & the subscript (SS-1) --

       01  BINARY-STUFF                BINARY  SYNC.
           05  SS-1                    PIC  S9(9).

       01  STJ-TABLE.
           05  STJ-COUNT               PIC  S9(9)  BINARY  SYNC.
           05  STJ-ENTRY               OCCURS  1 TO 99999 TIMES
                                       DEPENDING ON STJ-COUNT
                                       ASCENDING KEY STJT-SEQNO
                                       INDEXED BY  I.
               10  STJ-STJ-NO.
                   15  FILLER          PIC  X(9).
                   15  STJT-SEQNO      PIC  9(5).
                   15  FILLER          PIC  XX.
               10  STJ-LASER-SEQNO     PIC  9(5).

  -------  Manipulating the index (I) & the subscript (SS-1) --

                SET   I                     TO  +1
                SET   I                     TO  SS-1

                MOVE  I                     TO  SS-1

IGYPS2074-S "I" was defined as a type that was invalid in this context. 
The
            statement was discarded.

                MOVE  SS-1                  TO  I

IGYPS2074-S "I" was defined as a type that was invalid in this context. 
The
            statement was discarded.


I think if we have another go around on this thread, I'll volunteer now
to he "Hitler".

Bill Lynch
```

##### ↳ ↳ Re: help

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298302.64136.16312@kcbbs.gen.nz>`
- **References:** `<36395847.781398E1@att.net>`

```
In message <<36395847.781398E1@att.net>> William Lynch <wblynch@att.net> writes:
> > 
> > If anyone can answer these please let me know.
…[5 more quoted lines elided]…
> question<g>)

You are confused.  A subscript is simply a numeric item and
is only a subscript when it is used to access an array.
It is INDEXes which require the SET.
```

###### ↳ ↳ ↳ Re: help

- **From:** d.s.kirk@ix.netcom.com (David)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363ba74c.29830643@nntp.ix.netcom.com>`
- **References:** `<36395847.781398E1@att.net> <3298302.64136.16312@kcbbs.gen.nz>`

```
On 30 Oct 98 17:48:56 GMT, riplin@kcbbs.gen.nz (Richard Plinston)
wrote:

>In message <<36395847.781398E1@att.net>> William Lynch <wblynch@att.net> writes:
>> > 
…[11 more quoted lines elided]…
>
I concur. subscripts are just numeric items (COMP for best efficiency
with PIC S9(4) for half-word boundary....)  A subscript will always
contain the numeric value assigned to it. for example, if you 
    MOVE 10 TO SUB-X     the value will be 10.   

HOWEVER..... subscripts and indexes are equivalent in performance
*ONLY* if the value changes for each instruction execution.  Where an
index improves performance is where you have multiple variables
addressed by the setting of index or subscript. In this case,
generated object code will favor the use of indexes. Where you are
executing only one instruction per change of index or subscript, the
execution code will be equivalent. 

Oops... one correction. If using cobol/mvs with OPTIMIZE compile
option, performance will be improved but not as clear-cut on index vs.
subscript.  
david

p.s. i don't understand the original question. how do you move an "I"
to a subscript?  Was the original post referring to the binary value
of an "I"?  doesn't make sense (to me) otherwise...
```

###### ↳ ↳ ↳ Re: help

_(reply depth: 4)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298304.64558.15949@kcbbs.gen.nz>`
- **References:** `<363ba74c.29830643@nntp.ix.netcom.com>`

```
In message <<363ba74c.29830643@nntp.ix.netcom.com>> d.s.kirk@ix.netcom.com  writes:
> 
> HOWEVER..... subscripts and indexes are equivalent in performance
…[5 more quoted lines elided]…
> execution code will be equivalent. 

You are describing a specific implementation's behaviour as
if it were a generalisation.  A Cobol implementation that
treats INDEX exactly like numeric items used as subscripts
may be fully conforming to the standard.

Compiler optimisation could also extract subscript calculations
and perform this once for a block of code using a particular
subscript or index value.

It is likely that an index will be more efficient in many
cases, but this is by no means assured.  It is unlikely
that it would be less efficient, but could be if there
was more manipulation of the index than usage of it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
