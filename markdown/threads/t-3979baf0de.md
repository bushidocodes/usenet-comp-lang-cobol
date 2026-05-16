[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is it possible to put any character (0 to 255) in a PIC X?

_45 messages · 14 participants · 2003-06_

---

### Is it possible to put any character (0 to 255) in a PIC X?

- **From:** emmanuel.ichbiah@bigfoot.com (Emmanuel)
- **Date:** 2003-06-06T23:18:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>`

```
I have a field in a C record that is defined as char,
it is used to store any value between 0 and 255.

I have a corresponding mapping for cobol, with that field defined as PIC X.

Will it work?

Beginner's question, I know! :-)
```

#### ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-06-07T06:42:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0306070542.4f135ebd@posting.google.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>`

```
What matters here is if you want to get at the value as a number.  

Yes - the CHAR goes in a PIC X fine.  If you want to get it as a
number though, how you do it depends on your compiler.

With Micro Focus define it as PIC X COMP-X.

With Realia PIC S9(2) COMP. and set the smallbyte directive.

With Fujitsu use PIC S9(2) COMP-4 and set BINARY(BYTE) directive. 
There may be side effects from these directives depending on how
properly your other binary fields are defined.


emmanuel.ichbiah@bigfoot.com (Emmanuel) wrote in message news:<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>...
> I have a field in a C record that is defined as char,
> it is used to store any value between 0 and 255.
…[5 more quoted lines elided]…
> Beginner's question, I know! :-)
```

##### ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-07T16:38:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbtm0p$6fr$1@slb2.atl.mindspring.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <bfdfc3e8.0306070542.4f135ebd@posting.google.com>`

```
And as stated earlier, with any compiler with the ANSI/ISO Intrinsic
Functions, use the ORD intrinsic function (and subtract 1 - if you want a
value between 0 and 255 - rather than 1 and 256)
```

#### ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-07T08:58:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbsr23$jle$1@slb1.atl.mindspring.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>`

```
Yes it will work.  Look at the COBOL intrinsic functions "ORD" and "CHAR"
for additional information on handling this.
```

#### ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-07T15:13:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EE2474C.4040307@Knology.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>`

```
Emmanuel wrote:
> I have a field in a C record that is defined as char,
> it is used to store any value between 0 and 255.
…[5 more quoted lines elided]…
> Beginner's question, I know! :-)

You can move 0 to 255 characters to a field defined as Pic X(255). 
However, you'll have spaces out the end.  Check out the 
Occurs...Depending On syntax.  According to my manual, you can have 0 in 
this, something like

01  MyTable.
     03  MyTable-Data       Occurs 0 to 255 Times
                              Depending on MySize
                                Pic X(01).
01  MySize                      Pic 9(03).

Then, if you're moving 50 characters into it, move 50 to MySize and move 
your text to MyTable.  It will then be 50 characters, with no spaces on 
the end.
```

#### ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-07T17:43:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EE26A90.10408@Knology.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com>`

```
Emmanuel wrote:
> I have a field in a C record that is defined as char,
> it is used to store any value between 0 and 255.
…[5 more quoted lines elided]…
> Beginner's question, I know! :-)

Okay, I completely misread this question...  Sorry...
```

##### ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-08T12:23:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee28250_4@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net>`

```

"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
news:3EE26A90.10408@Knology.net...
> Emmanuel wrote:
> > I have a field in a C record that is defined as char,
> > it is used to store any value between 0 and 255.
> >
> > I have a corresponding mapping for cobol, with that field defined as PIC
X.
> >
> > Will it work?
…[4 more quoted lines elided]…
>

It happens and most of us do it at some time <G>.

I was more concerned at you recommending OCCURS...DEPENDING (sometimes
referred to as ODO).

On most platforms this is a construct "best avoided" except when there is no
other way (and there usually is...).

It is ugly ( my opinion), prone to error (I have seen more than a couple of
cases where the count field gets clobbered by accident and the programmer
spends many hours looking for non-existent errors elsewhere), and involves
some very nasty overheads (at machine level).

Personally, I will only use it if the incoming data has been written in that
format. I would NEVER use it as a choice in WS.

If I had an application that required completely variable output, I would
change the design if possible, and, if not, use byte stream IO. (This would
have to be read by ODO or byte stream. The answer is not to get in that
situation ion the first place...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-08T19:12:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee38053.205756024@news.optonline.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com>`

```
I agree that ODO isn't very useful in working-storage, where fields are
pre-allocated to their maximum size. But I find it very useful in dynamically
allocated structures such as lines of text or a list of words. Rather than
allocating 512 bytes for every line of text, I allocate its actual size. Rather
than allocating 30 bytes per word, thereby imposing a limit (as COBOL does), I
allocate the word's size. 



"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
…[38 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-09T10:35:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee3baa9_6@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ee38053.205756024@news.optonline.net...
> I agree that ODO isn't very useful in working-storage, where fields are
> pre-allocated to their maximum size. But I find it very useful in
dynamically
> allocated structures such as lines of text or a list of words. Rather than
> allocating 512 bytes for every line of text, I allocate its actual size.
Rather
> than allocating 30 bytes per word, thereby imposing a limit (as COBOL
does), I
> allocate the word's size.
>

COBOL allocates the maximum size anyway. Unless you call API,  malloc, or
GETMAIN (for the mainframe environments)  to do true dynamic allocation,
WHEREVER you use OCCURS...DEPENDING, COBOL allocates the maximum size.

It is a pointless construct that lets people THINK they are being clever.

The only REAL value it has is for reading a variable length file, where
there are count fields on the records. Even then a maximum size buffer is
allocated by COBOL.

Pete.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 5)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-06-09T11:45:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0306091045.62037dd@posting.google.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com>`

```
See notes below

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:<3ee3baa9_6@news.athenanews.com>...
> "Robert Wagner" <robert@wagner.net> wrote in message
> news:3ee38053.205756024@news.optonline.net...
…[21 more quoted lines elided]…
> Pete.

Two potential benefits of using ODO are when sorting and randomly
searching tables that do not always contain the same number of
elements.

When an ODO is a sending operand the compiler should use the defined
size according to the depending on variable to specify the amount of
data to be processed, such a feature can have its uses, though I admit
I haven't used it much if at all except when dealing with variable
length record files.

The rules for receiving operands are similar, but only when the
depending on variable is outside the ODO group that is referenced as a
receiving operand.

Robert
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-10T11:10:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee51434_7@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com>`

```

"Robert Jones" <robert@jones0086.freeserve.co.uk> wrote in message
news:fcd09c56.0306091045.62037dd@posting.google.com...
> See notes below
>
…[4 more quoted lines elided]…
>

You can get the same effect by initializing a table of maximum size to be
high values or whatever, then terminate your search on this value. This has
the added advantage that you can store the entries in sequence with a binary
chop when you load it, and there is no need to sort the table in memory.

(in 37 years I have NEVER sorted a table in memory...but then I'm not a
computer scientist <G>. I don't care about sort algorithms and Fibonnaci
series...)


> When an ODO is a sending operand the compiler should use the defined
> size according to the depending on variable to specify the amount of
…[3 more quoted lines elided]…
>

The overheads in this are unacceptable to me.

> The rules for receiving operands are similar, but only when the
> depending on variable is outside the ODO group that is referenced as a
> receiving operand.
>

You have still failed to demonstrate how this can ONLY be achieved by using
ODO.

It is a pointless and dangerous construct, best avoided.

Pete.

> Robert
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-10T14:25:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc4pop$h76$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com>`

```

On  9-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> (in 37 years I have NEVER sorted a table in memory...but then I'm not a
> computer scientist <G>. I don't care about sort algorithms and Fibonnaci
> series...)

I've only done so a handful of times - but never for "computer science" type
reasons.
```

###### ↳ ↳ ↳ Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-10T14:42:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc5cbk$a0a$1@slb6.atl.mindspring.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:bc4pop$h76$1@peabody.colorado.edu...
>
> On  9-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> I've only done so a handful of times - but never for "computer science"
type
> reasons.

I *know* that I have used a "serial search" when I (sort-of) wanted to do a
binary sort (SEARCH ALL) - because a table was not already "in order".  To
me that is a major advantage of the 2002 Standard "table sort" feature.
Although such a COBOL language "table sort" may perform  (slightly - or not
at all) worse than a "hand-crafted" sort of a table, I have always
questioned the "maintainability" of the latter.  It will be interesting to
me, how much greater use of SEARCH ALL will occur when/if the "table" option
of the SORT statement becomes generally available.

Clearly run-time considerations need to be dealt with when using such
features.  If a table needs to be sorted ONCE in an application's logic but
SEARCHED *many* times, I would think that such would be beneficial.
However, if it is only SEARCHED a "few" times, the overhead of a SORT
(assuming the original input is NOT in sorted order) probably would not be
warranted.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-10T20:02:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc5dgn$pno$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net>`

```
I had to modify a program that already had a CoBOL sort in it.   It produced
detail lines under a header that needed to be sorted by subcode.  There aren't a
lot of detail lines per header, but there were LOTS of header lines.    Detail
lines were saved in a table and the header was created (with such data as
detail-record count).

A better design might be to design header and detail lines with a sort key for
an external sort when done writing.   But that wasn't an option for me.

Meanwhile I wanted to sort the detail lines.   So I wrote a table sort.   An OO
person would have created a table sort object.   I could have called an external
sort routine.   I wrote a simple comb sort (a bubble sort might have been
simpler, and probably about as fast for these small sorts - but adding one line
to turn it into a comb sort didn't cost much).   I added a comment that the next
compiler would probably have a table sort to replace that paragraph.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-06-10T13:52:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc5gdm$i3a$1@si05.rsvl.unisys.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:bc5cbk$a0a$1@slb6.atl.mindspring.net...

> I *know* that I have used a "serial search" when I (sort-of) wanted to do
a
> binary sort (SEARCH ALL) - because a table was not already "in order".  To
> me that is a major advantage of the 2002 Standard "table sort" feature.

I think you meant "... wanted to do a binary search (SEARCH ALL) ...".
Presuming that you did:

A caution.  SEARCH ALL does *NOT* require, or imply, a binary search, or any
other sort of search.  Never did.

ISO/IEC 1989:2002 page 515, 14.8.34, SEARCH statement, GR9:  "A nonserial
type of search operation may take place.  The ... setting of the search
index ... is varied during the search operation in a manner specified by the
implementor ..."

ANSI X3.23-1985 page VI-124, 6.22, SEARCH statement, GR4: "If format 2 of
the SEARCH statement is used, a nonserial type of search operation may take
place; the ... setting of the index-name ... is varied ... in a manner
specified by the implementor ..."

ANSI X3.23-1974 page III-9, 3.3, SEARCH statement, GR3:  same wording as
'85.

Note the use of he word "may" in all three standards.

My personal opinion is that the SEARCH ALL syntax was intended to *allow*
the implementor to provide a fast-locate algorithm (which might or might not
be a binary search) that wouldn't be available with "plain" SEARCH.  But
there is NO requirement in the standard that the search be binary, or in
fact, anything other than serial.  The manner in which the implementor
varies the index can indeed be serially.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-11T13:42:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee68972_9@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:bc5cbk$a0a$1@slb6.atl.mindspring.net...
> "Howard Brazee" <howard@brazee.net> wrote in message
> news:bc4pop$h76$1@peabody.colorado.edu...
…[3 more quoted lines elided]…
> > > (in 37 years I have NEVER sorted a table in memory...but then I'm not
a
> > > computer scientist <G>. I don't care about sort algorithms and
Fibonnaci
> > > series...)
> >
…[4 more quoted lines elided]…
> I *know* that I have used a "serial search" when I (sort-of) wanted to do
a
> binary sort (SEARCH ALL) - because a table was not already "in order".  To
> me that is a major advantage of the 2002 Standard "table sort" feature.
> Although such a COBOL language "table sort" may perform  (slightly - or
not
> at all) worse than a "hand-crafted" sort of a table, I have always
> questioned the "maintainability" of the latter.  It will be interesting to
> me, how much greater use of SEARCH ALL will occur when/if the "table"
option
> of the SORT statement becomes generally available.
>
> Clearly run-time considerations need to be dealt with when using such
> features.  If a table needs to be sorted ONCE in an application's logic
but
> SEARCHED *many* times, I would think that such would be beneficial.
> However, if it is only SEARCHED a "few" times, the overhead of a SORT
> (assuming the original input is NOT in sorted order) probably would not be
> warranted.
>

All fair enough, Bill.

My point was that if you need a table in sequence, then LOAD it that way.
You can accomplish this easily with a binary chop against initialized
high-values. I have some code somewhere that I have used for years (I
remember modifying it to use reference modification to split the table at
the right place so an entry could be inserted, when refmodding became
available - before that I had a variable length MOVE routine written in
Mainframe BAL <G> (I converted the same routine to 8086 MASM when PCs became
available) - I'll have a look around and see if I can find it, then post it
here.)

For me "SORT" has always been a 4 letter word... It conjures up hours on the
night shift watching tapes whirr and then having the bloody thing crash on
pass 7 of 11 and having to  restore from the last successful checkpoint that
was back on pass 5...<G> I don't know how many people here remember IBM's
"SORT 7" (it was used on 360s where it ran in 1401 compatibility mode... The
only good thing was you could turn all the lights out and run it in the
dark...really spooky. Like being on the bridge of Starship Enterprise <G>.)

I was pretty relieved when disks were invented and we could ignore the whole
business by chaining everything into report sequence <G>...

Pete.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-11T14:06:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc7d1f$8o9$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com>`

```

On 10-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> My point was that if you need a table in sequence, then LOAD it that way.
> You can accomplish this easily with a binary chop against initialized
> high-values.

Not all tables can be loaded at all.  Some have to be created on the fly, and
should be created by the program that uses them.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-12T03:25:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee74a30_2@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bc7d1f$8o9$1@peabody.colorado.edu...
>
> On 10-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > My point was that if you need a table in sequence, then LOAD it that
way.
> > You can accomplish this easily with a binary chop against initialized
> > high-values.
>
> Not all tables can be loaded at all.  Some have to be created on the fly,
and
> should be created by the program that uses them.

I don't understand a word of this, Howard.

If a table isn't loaded it can't be used. If a program creates a table it
is, in effect loading it. How could a program OTHER than the program that
created the table load it? (I never suggested any such thing so I can't see
why you wrote this.)

Do we have a terminology problem here, or am I simply missing something you
are trying to say?

Pete.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 12)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-11T11:17:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T1qdnWtBY5OGy3qjXTWcog@giganews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz>
> >
> > Not all tables can be loaded at all.  Some have to be created on the
fly,
> and
> > should be created by the program that uses them.
…[5 more quoted lines elided]…
> created the table load it? (I never suggested any such thing so I can't
see
> why you wrote this.)
>
> Do we have a terminology problem here, or am I simply missing something
you
> are trying to say?

Maybe:

MOVE 'One' TO TABLE(1)
MOVE 'Two' TO TABLE(2)
MOVE 'Three' TO TABLE(3)
...
MOVE 'One Thousand' TO TABLE(1000).
...

?
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-11T20:02:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc81s0$n6b$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com>`

```

On 11-Jun-2003, "JerryMouse" <nospam@bisusa.com> wrote:

> MOVE 'One' TO TABLE(1)
> MOVE 'Two' TO TABLE(2)
> MOVE 'Three' TO TABLE(3)
> ...
> MOVE 'One Thousand' TO TABLE(1000).

Quickly, tell me the numbers from zero to 20 in alphabetical order.

What I meant is print an inventory report showing which parts are available in
which local store, sorted by how far that store is from the store doing the
requesting, which distance gets calculated on-line.   (off the top of my head).
  We don't know the sort order until we massage the data.   We store the detail
data in a table as we summarize data for the header of the report, then we
calculate the key field, sort and print.   (Maybe a better key would be Net
Profit).

If this was a batch job, we could add an artificial prefix to the sort key to
keep the part numbers in order, sort, remove the prefix, and print.  But a table
sort for each part number's detail lines would be more direct.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-12T00:21:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee7aa54.32250143@news.optonline.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:


>What I meant is print an inventory report showing which parts are available in
>which local store, sorted by how far that store is from the store doing the
…[7 more quoted lines elided]…
>keep the part numbers in order, sort, remove the prefix, and print.  But a
table
>sort for each part number's detail lines would be more direct.

One program I support does that by opening output a keyed file, writing the
table to it, then reading it back in sequence. How's that for avoiding a sort?
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-12T14:15:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bca1uv$r5a$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee7aa54.32250143@news.optonline.net>`

```

On 11-Jun-2003, robert@wagner.net (Robert Wagner) wrote:

> >If this was a batch job, we could add an artificial prefix to the sort key to
> >keep the part numbers in order, sort, remove the prefix, and print.  But a
…[4 more quoted lines elided]…
> table to it, then reading it back in sequence. How's that for avoiding a sort?

It depends on how often this needs to be done.  Once is OK.   I'd hate to try
this for 10,000 parts.

I knew of a shop 20 years ago that didn't have a sort utility.  It did ALL of
it's sorts by using keyed files.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-12T21:25:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee8476e_5@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu>`

```
Howard,

Overall, it seems to me like you have a database application waiting to be
built.

If you need dynamic sorted tables that's what RDBs do extremely well. With
dynamic SQL you can create, drop, and order (sort) tables totally on the
fly, without COBOL having to do any of it...

However, given that this is Reality and you have what you have, then I don't
want to have a Religious War about whether it is wrong to sort tables in
memory. (All I am saying is that I have never done it and never need to...)

I already expressed elsewhere how I feel about SORT and this goes back a
long way. That doesn't mean I would NEVER use one (certainly, for external
files, I have coded a handful of COBOL programs with COBOL SORT in them just
so I could  get to understand how it works and the use of sort procedures,
and I have no real preference over using external or internal sorts. Quite
happy to go with the flow and the installation standards or "usual
practice".)

I have some comments below, and finally, a code sample that shows how I deal
with this problem.

"Howard Brazee" <howard@brazee.net> wrote in message
news:bc81s0$n6b$1@peabody.colorado.edu...
>
> On 11-Jun-2003, "JerryMouse" <nospam@bisusa.com> wrote:
…[8 more quoted lines elided]…
>

See code sample below.

> What I meant is print an inventory report showing which parts are
available in
> which local store, sorted by how far that store is from the store doing
the
> requesting, which distance gets calculated on-line.   (off the top of my
head).
>   We don't know the sort order until we massage the data.   We store the
detail
> data in a table as we summarize data for the header of the report, then we
> calculate the key field, sort and print.   (Maybe a better key would be
Net
> Profit).
>

So all these tables need amending when new stores are acquired? (looks like
a case for....RDB Man!!!!)


> If this was a batch job, we could add an artificial prefix to the sort key
to
> keep the part numbers in order, sort, remove the prefix, and print.  But a
table
> sort for each part number's detail lines would be more direct.

As I said above, I don't want this to become a Religious War, but I DO want
to show that you CAN load tables in sequence, with random data, very easily
and efficiently, (much more so than a comb or internal bubble or tournament
sort).

Here's a COBOL solution to your challenge above:

 IDENTIFICATION DIVISION.
 PROGRAM-ID. 'LoadSeqTable'.
*
* AUTHOR. Peter E. C. Dashwood.
* DATE_WRITTEN. June 12, 2003.
*
* This program demonstrates the use of splitting tables to load them
* in sequence, thus obviating the need for in memory sorting of tables.
*
* INPUTS:
*
* 1. A static table in this case, but it could equally well be data
*    from a non sequential file or database.
*
*    (If it was a database we'd probably just use the ORDER BY clause
*     and load the returned data serially, from a cursor.)
*
* OUTPUTS:
*
* 1. A sequentially ordered table.
*
* COMMENTS:
*
* It was suggested for this exercise, that providing the numbers 1
* to 20 in alphabetical order might be a good example. The code below
* gives the numbers 1 to 30.
*
*  Remember that the static table containing the words is not really
*  part of this exercise. It is just a datasource for the exercise.
*
*  it is NOT necessary to have TWO tables for this technique to be
*  implemented.
*
*  When the insertion point for the candidate entry has been arrived
*  at by the binary chop, it is necessary to "bump" the table so as to
*  "make room" for the entry being inserted. I have chosen to do this
*  using a workarea and two refmodded MOVEs. The alternative is a
*  PERFORM... VARYING that moves each cell below the insertion point down
*  one, starting from the bottom of the table. The choice depends on
*  whether you have speed or space as a priority.
*
 ENVIRONMENT DIVISION.
 configuration section.
 source-computer. IBM-PC.
 object-computer. IBM-PC.

*------------------------  DATA   DIVISION  ---------------------
 DATA DIVISION.
 WORKING-STORAGE SECTION.


 01  subscripts usage comp-5.
     12 J  pic s9(3).
     12 K  pic s9(3).
     12 L  pic s9(3).



*
* Static table to be used as a datasource for this exercise.
*
 01  table-of-number-names.
     12 filler            pic x(12) value 'ONE         '.
     12 filler            pic x(12) value 'TWO         '.
     12 filler            pic x(12) value 'THREE       '.
     12 filler            pic x(12) value 'FOUR        '.
     12 filler            pic x(12) value 'FIVE        '.
     12 filler            pic x(12) value 'SIX         '.
     12 filler            pic x(12) value 'SEVEN       '.
     12 filler            pic x(12) value 'EIGHT       '.
     12 filler            pic x(12) value 'NINE        '.
     12 filler            pic x(12) value 'TEN         '.
     12 filler            pic x(12) value 'ELEVEN      '.
     12 filler            pic x(12) value 'TWELVE      '.
     12 filler            pic x(12) value 'THIRTEEN    '.
     12 filler            pic x(12) value 'FOURTEEN    '.
     12 filler            pic x(12) value 'FIFTEEN     '.
     12 filler            pic x(12) value 'SIXTEEN     '.
     12 filler            pic x(12) value 'SEVENTEEN   '.
     12 filler            pic x(12) value 'EIGHTEEN    '.
     12 filler            pic x(12) value 'NINETEEN    '.
     12 filler            pic x(12) value 'TWENTY      '.
     12 filler            pic x(12) value 'TWENTY-ONE  '.
     12 filler            pic x(12) value 'TWENTY-TWO  '.
     12 filler            pic x(12) value 'TWENTY-THREE'.
     12 filler            pic x(12) value 'TWENTY-FOUR '.
     12 filler            pic x(12) value 'TWENTY-FIVE '.
     12 filler            pic x(12) value 'TWENTY-SIX  '.
     12 filler            pic x(12) value 'TWENTY-SEVEN'.
     12 filler            pic x(12) value 'TWENTY-EIGHT'.
     12 filler            pic x(12) value 'TWENTY-NINE '.
     12 filler            pic x(12) value 'THIRTY      '.
 01  NumNames redefines table-of-number-names.
     12 inWord            pic x(12) occurs 30
                                    indexed by iw-x1.


*
* The table to be loaded sequentially...
 01  table-of-alphabetic-numbers.
     12 tan-entry         pic x(12) occurs 30
                                    indexed by tan-x1.
                          *>
                          *> the table has 30 entries
                          *> each entry is 12 bytes
                          *> the table occupies 360 bytes
                          *>

 01  tan-numbers usage comp-5.
     12 tan-size       pic s9(3) value 360.
     12 tan-lo         pic s9(3) value zero.
     12 tan-hi         pic s9(3) value zero.
     12 tan-split      pic s9(3) value zero.
     12 tan-movelen    pic s9(3) value zero.
     12 tan-entry-len  pic s9(3) value 12.

 01  wkarea pic x(360). *> Not required if PERFORM...VARYING
                        *> is used to bump the table. See notes.
 PROCEDURE DIVISION.
 INLINE SECTION.
 a000.
     move HIGH-VALUES to table-of-alphabetic-numbers
     move inWord (1) to tan-entry (1)
     perform
        varying iw-x1
           from 2
             by 1
          until iw-x1 > 30
     *>
     *> binary chop on tan...
     *>
        move 1  to tan-lo
        move 30 to tan-hi
        perform until (tan-hi - tan-lo) NOT > 1
          compute J = (tan-hi + tan-lo) / 2
          set tan-x1 to J
          if inWord (iw-x1) NOT > tan-entry (tan-x1)
             set tan-hi to tan-x1
          else
             set tan-lo to tan-x1
          end-if
          if inWord (iw-x1) NOT > tan-entry (tan-lo)
             move tan-lo to tan-hi
          end-if
        end-perform
        set tan-x1 to tan-hi
      *>
      *> found the place for it...
      *> now bump the table to make room for it.
      *> It is tempting to do this by "rippling"  each entry down 1
      *> with a PERFORM...VARYING. That would work, but a few quick
      *> calculations and a couple of block moves are usually MUCH faster...
      *>
      *> The insertion point ("tan-split") is calculated as:
      *> ((current-entry - 1) * entry-length) + 1
      *>
      *> The "length to move" is calculated as:
      *> table-size - insertion-point + 1
      *>
      *> The destination point is the insertion point + entry length
      *>
      *> NOTE the above formulas are good for ANY size table...
      *>
      *> The downside to this technique is that a work area is required, to
      *> prevent the entry being "bumped", from being propagated right
      *> through the remainder of the table.
      *>
      *>
        set J to tan-x1  *> J represents the current entry...
        compute tan-split = ((J - 1) * tan-entry-len) + 1
        compute tan-movelen   = tan-size - tan-split + 1
        compute K = tan-split + tan-entry-len *> K is the destination...
        move table-of-alphabetic-numbers (tan-split : tan-movelen) to wkarea
        move wkarea (1: tan-movelen) to     table-of-alphabetic-numbers (K:)
        move inWord (iw-x1) to tan-entry (tan-x1)
     end-perform
     .
 a999.
     stop run.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 15)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-12T07:50:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nLicndzoFJ2H6nWjXTWcpQ@giganews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz>
>
>  IDENTIFICATION DIVISION.
…[150 more quoted lines elided]…
>       *> calculations and a couple of block moves are usually MUCH
faster...
>       *>
>       *> The insertion point ("tan-split") is calculated as:
…[9 more quoted lines elided]…
>       *> The downside to this technique is that a work area is required,
to
>       *> prevent the entry being "bumped", from being propagated right
>       *> through the remainder of the table.
…[6 more quoted lines elided]…
>         move table-of-alphabetic-numbers (tan-split : tan-movelen) to
wkarea
>         move wkarea (1: tan-movelen) to     table-of-alphabetic-numbers
(K:)
>         move inWord (iw-x1) to tan-entry (tan-x1)
>      end-perform
>      .
>  a999.
>      stop run.

or

        SORT SortWork on ascending key SORT-KEY
              Input procedure is Sort-In
              Output procedure is Sort-out
...
Sort-In.
        Perform varying J from 1 by 1 until J > 30
                Release SORT-REC from InWord(J)
                End-perform.
Sort-Out.
        Perform varying J from 1 by 1 until J > 30
                Return SortWork into Tan-entry(J)
                end-perform.

Not nearly as elegant as yours, but what's art without suffering?
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-13T02:12:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee88ac2_4@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:nLicndzoFJ2H6nWjXTWcpQ@giganews.com...
>

> or
>
…[14 more quoted lines elided]…
>

That looks good, Jerry.

There are some things here I haven't seen before so I have some questions.

1. What is "SortWork" and where is  SORT-REC and SORT-KEY defined?(Do these
require SD entries?)

2. If the Perform Varying works the way I think it does then this should
gradually build the sorted table entry by entry, right? Where are the sort
work areas? It must have everything sorted SOMEWHERE so it can return sorted
records...

3. Any idea what overheads are incurred with this? (This doesn't bother me
if it is reasonable...)

I can see the idea of using the input table and the output table with
Release and Return, but I can't see how the whole thing could work. Can you
post me (privately maybe) a Fujitsu project that does it? I'd like to do
some further investigation.

Thanks,

Pete.


>
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 17)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-06-12T14:56:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ee88ac2_4@news.athenanews.com...
>
> "JerryMouse" <nospam@bisusa.com> wrote in message
…[7 more quoted lines elided]…
> 1. What is "SortWork" and where is  SORT-REC and SORT-KEY defined?(Do
these
> require SD entries?)

1. SortWork requires SD which looks like FD
SD SortWork
    01   SORT-REC.
         05 SORT-KEY    PIC whatever
        05  rest-of-record PIC whatever.


2. You "are" funning us about not having seen this before, aren't you?  I
only ask because I have come to expect the unexpected.. like the first time
I did some work for a client and the client rep wanted to inspect my source
code when I was done. Client rep had been the primary COBOL programmer (IBM
mainframe environment) for nine (9) years, so imagine my surprise when she
told me the code looked good, except that this was the first time she had
ever seen the SEARCH verb used...

Since then I assume 'nothing' about the experience level of clients...

MCM
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 18)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-06-12T18:47:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nV3Ga.2856$3o3.235478@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com...
| "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
| news:3ee88ac2_4@news.athenanews.com...
…[7 more quoted lines elided]…
| > There are some things here I haven't seen before so I have some
questions.
| >
| > 1. What is "SortWork" and where is  SORT-REC and SORT-KEY defined?(Do
…[11 more quoted lines elided]…
| only ask because I have come to expect the unexpected.. like the first
time
| I did some work for a client and the client rep wanted to inspect my
source
| code when I was done. Client rep had been the primary COBOL programmer
(IBM
| mainframe environment) for nine (9) years, so imagine my surprise when she
| told me the code looked good, except that this was the first time she had
…[3 more quoted lines elided]…
|

WAR STORY: I noticed a programmer coding his own search, so I asked him why
he didn't use the SEARCH verb.
He told me "At my last job there was a bug in the SEARCH verb, so we were
told to code our own search".
I asked him when that was. "Seven years ago" was the reply.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-12T19:05:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcaita$9pu$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com> <nV3Ga.2856$3o3.235478@bgtnsc05-news.ops.worldnet.att.net>`

```

On 12-Jun-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:

> WAR STORY: I noticed a programmer coding his own search, so I asked him why
> he didn't use the SEARCH verb.
> He told me "At my last job there was a bug in the SEARCH verb, so we were
> told to code our own search".
> I asked him when that was. "Seven years ago" was the reply.

Well, I still READ INTO for a similar historical reason.   But the cost of doing
so is different from having user written code to do what the language already
does.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 18)_

- **From:** "Don Leahy" <don.leahy@nospamwhatever.leacom.ca>
- **Date:** 2003-06-12T16:10:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q65Ga.2010$ac.15521@news20.bellglobal.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3ee88ac2_4@news.athenanews.com...
…[7 more quoted lines elided]…
> > There are some things here I haven't seen before so I have some
questions.
> >
> > 1. What is "SortWork" and where is  SORT-REC and SORT-KEY defined?(Do
…[11 more quoted lines elided]…
> only ask because I have come to expect the unexpected.. like the first
time
> I did some work for a client and the client rep wanted to inspect my
source
> code when I was done. Client rep had been the primary COBOL programmer
(IBM
> mainframe environment) for nine (9) years, so imagine my surprise when she
> told me the code looked good, except that this was the first time she had
…[4 more quoted lines elided]…
> MCM

When I started out, it was a shop standard *not* to use SEARCH or SEARCH
ALL.  Instead of SEARCH you were supposed to code a PERFORM UNTIL loop and
scan the table yourself.  Instead of SEARCH ALL, you were supposed to call
an in-house assembler subroutine.

Ah, those were the days...NOT!   :-)
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 18)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-13T12:04:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee91590_9@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3ee88ac2_4@news.athenanews.com...
…[6 more quoted lines elided]…
> only ask because I have come to expect the unexpected.. like the first
time
> I did some work for a client and the client rep wanted to inspect my
source
> code when I was done. Client rep had been the primary COBOL programmer
(IBM
> mainframe environment) for nine (9) years, so imagine my surprise when she
> told me the code looked good, except that this was the first time she had
> ever seen the SEARCH verb used...
>

Nope. I wasn't kidding. I never kid if it involves work for people and I was
genuinely asking for some elucidation.

I have never seen the COBOL SORT used to sort an internal table before. I
still haven't decided whether I would do this or not (I like the code I
posted, but, as Richard says, we all like what is familiar.)

I first used the technique  I described, in 1965 when there WEREN'T a lot of
sorts around. It was shown to me by a guy named Mike Crean at NCR in
Auckland and we used it to sort invoices by number on an NCR 500 with 4.8K.
The original was written in machine language for the NCR 500. COBOL was not
available on that machine.

> Since then I assume 'nothing' about the experience level of clients...
>

There are many fortress sites I have worked on where they never use SEARCH
or STRING or UNSTRING... I would hope that that has changed but it sounds
from your experience like it hasn't.

Thanks for covering the points, Michael. I really didn't know.

Pete.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-13T13:55:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bccl59$jtf$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <hw0Ga.3079$87.1872918@newssrv26.news.prodigy.com> <3ee91590_9@news.athenanews.com>`

```

On 12-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> I have never seen the COBOL SORT used to sort an internal table before. I
> still haven't decided whether I would do this or not (I like the code I
> posted, but, as Richard says, we all like what is familiar.)

I've seen it once.   I wouldn't use it where I needed to do thousands of small
sorts though without doing performance studies.   One large table sort though
can makes sense to be done externally.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 17)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-12T14:17:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qoOcnRfTPoh9THWjXTWJgQ@giganews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> IDENTIFICATION DIVISION.
 PROGRAM-ID. 'LoadSeqTable'.

 ENVIRONMENT DIVISION.
 configuration section.
 source-computer. IBM-PC.
 object-computer. IBM-PC.
 FILE-CONTROL.
     SELECT SORTWORK ASSIGN TO DISK (file status if you like).

*------------------------  DATA   DIVISION  ---------------------
 DATA DIVISION.

FILE SECTION.

SD  SORTWORK.
01  SORTREC.
     05  SORT-KEY   PIC X(12).

 WORKING-STORAGE SECTION.


 01  subscripts usage comp-5.
     12 J  pic s9(3).



*
* Static table to be used as a datasource for this exercise.
*
 01  table-of-number-names.
     12 filler            pic x(12) value 'ONE         '.
     12 filler            pic x(12) value 'TWO         '.
     12 filler            pic x(12) value 'THREE       '.
     12 filler            pic x(12) value 'FOUR        '.
     12 filler            pic x(12) value 'FIVE        '.
     12 filler            pic x(12) value 'SIX         '.
     12 filler            pic x(12) value 'SEVEN       '.
     12 filler            pic x(12) value 'EIGHT       '.
     12 filler            pic x(12) value 'NINE        '.
     12 filler            pic x(12) value 'TEN         '.
     12 filler            pic x(12) value 'ELEVEN      '.
     12 filler            pic x(12) value 'TWELVE      '.
     12 filler            pic x(12) value 'THIRTEEN    '.
     12 filler            pic x(12) value 'FOURTEEN    '.
     12 filler            pic x(12) value 'FIFTEEN     '.
     12 filler            pic x(12) value 'SIXTEEN     '.
     12 filler            pic x(12) value 'SEVENTEEN   '.
     12 filler            pic x(12) value 'EIGHTEEN    '.
     12 filler            pic x(12) value 'NINETEEN    '.
     12 filler            pic x(12) value 'TWENTY      '.
     12 filler            pic x(12) value 'TWENTY-ONE  '.
     12 filler            pic x(12) value 'TWENTY-TWO  '.
     12 filler            pic x(12) value 'TWENTY-THREE'.
     12 filler            pic x(12) value 'TWENTY-FOUR '.
     12 filler            pic x(12) value 'TWENTY-FIVE '.
     12 filler            pic x(12) value 'TWENTY-SIX  '.
     12 filler            pic x(12) value 'TWENTY-SEVEN'.
     12 filler            pic x(12) value 'TWENTY-EIGHT'.
     12 filler            pic x(12) value 'TWENTY-NINE '.
     12 filler            pic x(12) value 'THIRTY      '.
 01  NumNames redefines table-of-number-names.
     12 inWord            pic x(12) occurs 30
                                    indexed by iw-x1.


*
* The table to be loaded sequentially...
 01  table-of-alphabetic-numbers.
     12 tan-entry         pic x(12) occurs 30
                                    indexed by tan-x1.
                          *>
                          *> the table has 30 entries
                          *> each entry is 12 bytes
                          *> the table occupies 360 bytes
                          *>

 PROCEDURE DIVISION.

 a000.
      SORT SortWork on ascending key SORT-KEY
         Input procedure is Sort-In
         Output procedure is Sort-out

 STOP RUN.


Sort-In.
      Perform varying J from 1 by 1 until J > 30
          Release SORT-REC from InWord(J)
          End-perform.
Sort-Out.
      Perform varying J from 1 by 1 until J > 30
          Return SortWork into Tan-entry(J)
          end-perform.

> >
>
…[4 more quoted lines elided]…
> 1. What is "SortWork" and where is  SORT-REC and SORT-KEY defined?(Do
these
> require SD entries?)

Yes.

>
> 2. If the Perform Varying works the way I think it does then this should
> gradually build the sorted table entry by entry, right? Where are the sort
> work areas? It must have everything sorted SOMEWHERE so it can return
sorted
> records...

No. All input records are dumped higgledy-piggledly into a 'magic box' (the
sort routine). They are returned, in order, one at a time. There are no
explicit sort work areas (other than the SortWork spill-file).

>
> 3. Any idea what overheads are incurred with this? (This doesn't bother me
> if it is reasonable...)

Inasmuch as sorting is a frequent activity in commercial applications, I am
confident that significant optimization has been undertaken (by any
compiler) on the SORT routines. For example, SORT makes a dynamic
determination about whether file access is necessary - it tries to do all
the work in memory if possible.

But, there are sorts and there are sorts. Fujitsu's "Standard" sort routine
is not nearly as fast as their development/PowerBSORT product. What's
missing in Fujitsu's documentation is you default to using PowerBSORT on a
development machine, but they send their slower sort when you deploy your
application. There are alternatives to PowerBSORT that are cheaper (like
almost free) and just as fast. You probably can't tell the difference
between the fast and not-so-fast sorts for a few tens-of-thousand records.

>
> I can see the idea of using the input table and the output table with
> Release and Return, but I can't see how the whole thing could work. Can
you
> post me (privately maybe) a Fujitsu project that does it? I'd like to do
> some further investigation.

Whole program. See above.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 18)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-13T12:10:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee916bf_1@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <nLicndzoFJ2H6nWjXTWcpQ@giganews.com> <3ee88ac2_4@news.athenanews.com> <qoOcnRfTPoh9THWjXTWJgQ@giganews.com>`

```
Thanks Jerry.

Pete.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:qoOcnRfTPoh9THWjXTWJgQ@giganews.com...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> IDENTIFICATION DIVISION.
…[19 more quoted lines elided]…
>
<snipped>>
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-12T14:38:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bca38i$rrd$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com>`

```

On 12-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> I have some comments below, and finally, a code sample that shows how I deal
> with this problem.

That was interesting, thanks.   But I don't see any particular advantage over
using a comb sort to order the table.

What we both have shown is that a CoBOL table sort command will be much more
obvious and maintainable by new programmers.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-13T12:30:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee91b94_2@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <T1qdnWtBY5OGy3qjXTWcog@giganews.com> <bc81s0$n6b$1@peabody.colorado.edu> <3ee8476e_5@news.athenanews.com> <bca38i$rrd$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bca38i$rrd$1@peabody.colorado.edu...
>
> On 12-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > I have some comments below, and finally, a code sample that shows how I
deal
> > with this problem.
>
> That was interesting, thanks.   But I don't see any particular advantage
over
> using a comb sort to order the table.
>

The sort requires loading the table then sorting it. The technique I posted
simply loads it sequentially.


> What we both have shown is that a CoBOL table sort command will be much
more
> obvious and maintainable by new programmers.

I disagree <G>.

It is good for newcomers to be exposed to non-obvious ways of doing things.
It stimulates them and makes life more interesting.

You could argue that if people use SEARCH ALL there is no need for them to
be aware of how a binary chop works...

I would reply that it is around 10 lines of code and the KNOWLEDGE itself
may be "leverable" in some as yet unforeseen circumstance. That doesn't mean
that I don't use SEARCH ALL...I do, but it depends on the circumstances.
(Besides, I think it was Chuck who pointed out that SEARCH ALL does not
GUARANTEE a binary chop, it is up to the implementor .)

The code I posted looks a bit intimidating because I put loads of comments
in it. In actual fact, it is very succinct and can be a performed subroutine
to load your table. It has no overheads and guarantees the table will be
loaded in sequence with far fewer accesses than a sort will.

Again, I am not trying to Evangelise the use of it. I really don't care
whether anybody uses SORT or the "Chop and Bump" I posted.

However, I DO refute your statement that posting something YOU are
unfamiliar with, simply reinforces the fact that familiar code  (to YOU)
will be much more "obvious and maintainable by new programmers". I contest
it on the basis that new programmers are not "familiar" with any particular
technique (Thank God...<G>), and that neither SORT nor Chop and Bump require
maintenance anyway.

Pete.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-11T19:51:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bc818p$mqj$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com>`

```

On 11-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> I don't understand a word of this, Howard.
>
…[6 more quoted lines elided]…
> are trying to say?

What I mean is that the table doesn't have to exist before the program runs, in
which case it can't go through an external sort before the program reads it in.
 You said:

> My point was that if you need a table in sequence, then LOAD it that
> way.

I responded that this isn't always possible.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-12T21:42:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee84b68_2@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <bc818p$mqj$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bc818p$mqj$1@peabody.colorado.edu...
>
> On 11-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[3 more quoted lines elided]…
> > If a table isn't loaded it can't be used. If a program creates a table
it
> > is, in effect loading it. How could a program OTHER than the program
that
> > created the table load it? (I never suggested any such thing so I can't
see
> > why you wrote this.)
> >
> > Do we have a terminology problem here, or am I simply missing something
you
> > are trying to say?
>
> What I mean is that the table doesn't have to exist before the program
runs, in
> which case it can't go through an external sort before the program reads
it in.
>  You said:
>
…[3 more quoted lines elided]…
> I responded that this isn't always possible.

Ah, now I understand how the wires got crossed...<G>

I wasn't suggesting that the table data should be externally sorted first
and I understand your point that sometimes programs need to "create" tables.
This is what I was referring to when I said LOAD. COBOL defines the
structure, but the data could well be "filled in" to the table dynamically
at run time. (I call this process LOADing the table.)

When I said if you need it in sequence LOAD it that way, I was referring to
the fact that you can "fill it in" in sequence as you place entries in it.
This obviates the need to do a memory sort and, if you do it carefully, is
actually much more efficient than loading the table, then doing a bubble,
comb, or tournament sort on it. It eliminates the multi-handling of table
entries that an internal sort requires and it requires less code to do it
than a sort typically takes.

I have posted sample code demonstrating this technique in a previous
response to your post in this thread.

(I wrote it very hurriedly as light relief from some serious stuff I was
doing today, so it might not be completely watertight. However, it serves to
demonstrate the approach I am advocating.)

Basically, it involves a binary chop to locate where the next entry is to
go, then a bump of the table to make room for it.

As you can understand, this minimises the access to the table as entries are
added.

(The code is also intended to be of interest to newbies who may find some of
the techniques interesting.)

Pete.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-06-12T14:42:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bca3gp$s1q$1@peabody.colorado.edu>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <bc818p$mqj$1@peabody.colorado.edu> <3ee84b68_2@news.athenanews.com>`

```

On 12-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> When I said if you need it in sequence LOAD it that way, I was referring to
> the fact that you can "fill it in" in sequence as you place entries in it.
…[4 more quoted lines elided]…
> than a sort typically takes.

In my case this would work - but I can conceive of cases where this isn't
possible.   Maybe sort by how far away an amount is from the average value for
all amounts in that table.   Not likely, but conceivable.
```

###### ↳ ↳ ↳ Re: Sort table (was: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-13T12:33:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee91c27_6@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <bc4pop$h76$1@peabody.colorado.edu> <bc5cbk$a0a$1@slb6.atl.mindspring.net> <3ee68972_9@news.athenanews.com> <bc7d1f$8o9$1@peabody.colorado.edu> <3ee74a30_2@news.athenanews.com> <bc818p$mqj$1@peabody.colorado.edu> <3ee84b68_2@news.athenanews.com> <bca3gp$s1q$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bca3gp$s1q$1@peabody.colorado.edu...
>
> On 12-Jun-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > When I said if you need it in sequence LOAD it that way, I was referring
to
> > the fact that you can "fill it in" in sequence as you place entries in
it.
> > This obviates the need to do a memory sort and, if you do it carefully,
is
> > actually much more efficient than loading the table, then doing a
bubble,
> > comb, or tournament sort on it. It eliminates the multi-handling of
table
> > entries that an internal sort requires and it requires less code to do
it
> > than a sort typically takes.
>
> In my case this would work - but I can conceive of cases where this isn't
> possible.   Maybe sort by how far away an amount is from the average value
for
> all amounts in that table.   Not likely, but conceivable.

Good try <G>!

Databases have aggregation functions that do exactly that, on the fly, with
dynamic SQL.

I'll say no more <G>

Pete.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-10T10:44:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hcydndHU2eZEYXijXTWJhA@giganews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz>
>
> (in 37 years I have NEVER sorted a table in memory...but then I'm not a
> computer scientist <G>. I don't care about sort algorithms and Fibonnaci
> series...)
>

Me neither. Takes my time. I prefer to shift costs from program development
to operations.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 8)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-06-10T16:10:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ApnFa.254$3o3.18713@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <hcydndHU2eZEYXijXTWJhA@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:hcydndHU2eZEYXijXTWJhA@giganews.com...
|
| "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
…[6 more quoted lines elided]…
| Me neither. Takes my time. I prefer to shift costs from program
development
| to operations.
|
I don't think you're shifting costs, you're probably reducing costs.

The last time I worked with a program that sorted a table, I had to correct
the sort.
The programmer who wrote it, and designed the system:
1. couldn't program
2. couldn't design either
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-11T13:46:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee68a38_6@news.athenanews.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <fcd09c56.0306091045.62037dd@posting.google.com> <3ee51434_7@news.athenanews.com> <hcydndHU2eZEYXijXTWJhA@giganews.com> <ApnFa.254$3o3.18713@bgtnsc05-news.ops.worldnet.att.net>`

```
LOL!

Good stuff, Dennis...

(Well, it made ME laugh <G>)

Pete.

(nothing further...)
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:ApnFa.254$3o3.18713@bgtnsc05-news.ops.worldnet.att.net...
>
> "JerryMouse" <nospam@bisusa.com> wrote in message
…[4 more quoted lines elided]…
> | > (in 37 years I have NEVER sorted a table in memory...but then I'm not
a
> | > computer scientist <G>. I don't care about sort algorithms and
Fibonnaci
> | > series...)
> | >
…[7 more quoted lines elided]…
> The last time I worked with a program that sorted a table, I had to
correct
> the sort.
> The programmer who wrote it, and designed the system:
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-10T00:22:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee50ce7.86696055@news.optonline.net>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[14 more quoted lines elided]…
>WHEREVER you use OCCURS...DEPENDING, COBOL allocates the maximum size.

"Dynamically allocated structures" implies true dynamic allocation.

>The only REAL value it has is for reading a variable length file, where
>there are count fields on the records. Even then a maximum size buffer is
>allocated by COBOL.

Your argument is 'I tried it once thirty years ago and had a lot of trouble
getting it to work. I thence decided it was a Bad Feature (use negative
adjective of choice: tricky, dangerous, flirting with disaster) and have avoided
it ever since. I strongly urge everyone else to adopt my opinion.'

When I express similar ideas, I'm Wrong. 

ODO is simply a variable length string. Is the concept difficult to understand?
It's not for Pascal programmers, to whom it's the only option available. I use
it routinely without 'unusual' hard-to-find program bugs, without writing over
other data structures, without memory protection abends, and without high
performance hits. 

I do NOT use it for a variable number of complex structures. That's what lists
and database tables are good for.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-10T13:55:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee537b6_4@corp-news.newsgroups.com>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <3ee50ce7.86696055@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ee50ce7.86696055@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> >

>
> Your argument is 'I tried it once thirty years ago and had a lot of
trouble
> getting it to work. I thence decided it was a Bad Feature (use negative
> adjective of choice: tricky, dangerous, flirting with disaster) and have
avoided
> it ever since. I strongly urge everyone else to adopt my opinion.'
>

Nope. That's not true. I used it many times and never had any trouble
getting it to work. I just didn't like the WAY it worked and I saw a number
of cases where people DID have trouble with it. Usually of the form where
the count was clobbered but this was not immediately obvious.A lot of time
can be wasted looking elsewhere for a non-existent bug.

I certainly "strongly urge" people to avoid it, but I have no problem if
they don't take my advice. (Maybe that's where we differ...).
First off, I don't care what people code. Second, I respect their right to
make their own decision about it.
(What would be the point of having an opinion and expressing it, unless you
urged others to agree with it?)

None of this has any bearing on my right to express an opinion, forcefully,
if I want to. If people disagree with it (as you are doing) I'll either
defend it or I'll let it go, consoling myself with the knowledge that I did
my best... I have no desire or intention to enforce my standards and
opinions on the World at large. From private mail I receive, it seems there
are people who NEVER post to this group but read it avidly. On occasion they
find my opinion of some use to them and that is one reason why I'm still
here.

> When I express similar ideas, I'm Wrong.
>

I can't imagine why there would be one rule for you and another for me,
Robert. My experience is that Right and Wrong have nothing to do with the
expression of ideas. One communicates an idea or opinion. It is implicit in
so doing that one believes it to be Right. (Or at least, it works for
one...) OTHER people may decide it is Wrong. Or Right. That is their
prerogative and the interchange can be stimulating and fun. Sometimes, after
such an interchange, one modifies one's original concept (or others do...),
the exercise is of benefit, and everyone moves on to something else.

Can you show an occasion where you expressed a "similar idea" to one I had
expressed, and you were considered Wrong, but I wasn't?


> ODO is simply a variable length string. Is the concept difficult to
understand?

I don't find it so. It is in HOW that concept is implemented that I take
issue. I feel strongly enough about it to avoid using it. As I have never
found a case where I could NOT avoid using it (except for the one we all
agree; incoming data is in that format), I don't have a problem with it.

> It's not for Pascal programmers, to whom it's the only option available. I
use
> it routinely without 'unusual' hard-to-find program bugs, without writing
over
> other data structures, without memory protection abends, and without high
> performance hits.
>
> I do NOT use it for a variable number of complex structures. That's what
lists
> and database tables are good for.
>

So, what's the beef? You do your thing, I'll do mine... Works for me...

Pete.
```

###### ↳ ↳ ↳ Re: Is it possible to put any character (0 to 255) in a PIC X?

_(reply depth: 7)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-06-10T22:41:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c32fa1$6b6495a0$bdcaf943@chottel>`
- **References:** `<2dfb6ff9.0306062218.5b3bdf5c@posting.google.com> <3EE26A90.10408@Knology.net> <3ee28250_4@news.athenanews.com> <3ee38053.205756024@news.optonline.net> <3ee3baa9_6@news.athenanews.com> <3ee50ce7.86696055@news.optonline.net> <3ee537b6_4@corp-news.newsgroups.com>`

```
Just in case RW counts votes again, I agree with Pete on this one.

<snip>


Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3ee537b6_4@corp-news.newsgroups.com>...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
