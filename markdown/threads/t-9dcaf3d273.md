[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorts and such...

_21 messages · 7 participants · 1998-12_

---

### Sorts and such...

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74po46$58a@lotho.delphi.com>`

```
Hi guys-
  I'm doing a RAD model of some software that will be ran under CICS,
perhaps with a database backend, and today I ran into a bit of a 
puzzler. Figured I would ask older and wiser heads for a pointer. :) 

  Since I suspect this will have to be hosted in a RDBMs, I've
been treating the COBOL files like db tables, with appropriate 
indcies and so on.  well imagine a pair ot tables like
this:

        fd  fund-master-table.
        01  fund-master-table-record.
            10 fund-number               pic 9(4).
            10 fund-name                 pic x(25).
            10 fund-report-number        pic 9(6).
              .... <more fields> ....

        fd  fund-history-table.
        01  fund-history-table-record.
            10 fh-id-number              pic 9(12).
            10 fd-fund-number            pic 9(4).
            10 fd-fund-date              pic 9(8).
            10 fd-fund-value             pic s9(11)v99.
              .... <more fields> ....

with selects similar to:

            select fund-master-table
              assign to fmt-file
              organization is indexed
              access mode is dynamic
              record      key is fund-number
              alternate   key is fund-name
              alternate   key is fund-report-number with duplicates.

            select fund-history-table
              assign to fht-file
              organization is indexed  
              access mode is dynamic
              record      key is fd-id-number
              alternate   key is fd-fund-number with duplicates
              alternate   key is fd-fund-date with duplicates.

Now the task here is to print those two little buggers out on x number
of separate reports (report number in the master file) by fund, and only
for a particular (user selected) date.

The only way I can think to do it is to sort the history file first,
by fund, then process each record individually in an output procedure.
COnversely, I could use an input and output procedure to a sort, 
selecting by date and outputing to a particualr report queu or 
something. Both of these solutions feel clumsy, and I of course,
cannot get the SQL solution out of my head. 

If someone else knows of an easier way to accomplish this probably
fairly common task, I'd be appreciative of a pointer or two. :) 
I have writing 'clunky' code!

-Paul
```

#### ↳ Re: Sorts and such...

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36706e5b.0@news1.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com>`

```
I would do a start on the history table, with the date given and
a not less condition. If I find a record, I'd check if the date
matches, then do a next record until the date changes.
For each record found, go pick up fund data from the master
based on fund-number.

I don't understand the role of fund-report-number so maybe
I'm off the mark.

paulr wrote in message <74po46$58a@lotho.delphi.com>...
>Hi guys-
>  I'm doing a RAD model of some software that will be ran under CICS,
…[59 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sorts and such...

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74q32h$gqj@lotho.delphi.com>`
- **References:** `<74po46$58a@lotho.delphi.com> <36706e5b.0@news1.ibm.net>`

```
The fund-report-number is a key to the lookup table that says
which report *this* particular fund belongs on. There are a half dozen
or so reports, and certain funds belong on certain reports. 

That is along the same lines of what I first starting thinking
about, but then realized the output has to be sorted by fund (
and associated group subtotals and so forth and so on, all the 
common jazz...) 

Using START I can sort on *either* fd-fund-number ot fd-fund-date,
and of course pick up the relevant data from the FUND-MASTER-TABLE,
but not both at the same time.

In SQL, I would solve that with a query similar to:

SELECT  fd-fund-number, fund-report-number, fd-fund-date,
        ... <all the fields I need > ...
        where fund-number = fd-fund-number   and
              fd-date = '12/10/1998'
        order by fd-fund-number

The WHERE clause causes a UNION to occur between the two tables,
as well as selecting just records that macth the date I need. 

In COBOL, the only way I figured out how to do that was to select
by date in the INPUT procedure to a SORT, and have the SORT order    
the output by FUND-NUMBER. Essentially waht you suggested, just
once pick and choose in the INPUT, and another put *this* in *THAT*
queue in the output. 

But it feels so clumsy, and I blusingly admit, I have not really 
ever used the COBOL SORT verb in a production environment,
though I have encountered it in maintenance. There will be about a
year's worth of data in a many-to-one relationship there. I am
a little concerned about how long it may take to run when the
files are populated.

-Paul

         

Leif Svalgaard (leif@ibm.net) wrote:
: I would do a start on the history table, with the date given and
: a not less condition. If I find a record, I'd check if the date
: matches, then do a next record until the date changes.
: For each record found, go pick up fund data from the master
: based on fund-number.

: I don't understand the role of fund-report-number so maybe
: I'm off the mark.

: paulr wrote in message <74po46$58a@lotho.delphi.com>...
: >Hi guys-
: >  I'm doing a RAD model of some software that will be ran under CICS,
: >perhaps with a database backend, and today I ran into a bit of a
: >puzzler. Figured I would ask older and wiser heads for a pointer. :)
: >
: >  Since I suspect this will have to be hosted in a RDBMs, I've
: >been treating the COBOL files like db tables, with appropriate
: >indcies and so on.  well imagine a pair ot tables like
: >this:
: >
: >        fd  fund-master-table.
: >        01  fund-master-table-record.
: >            10 fund-number               pic 9(4).
: >            10 fund-name                 pic x(25).
: >            10 fund-report-number        pic 9(6).
: >              .... <more fields> ....
: >
: >        fd  fund-history-table.
: >        01  fund-history-table-record.
: >            10 fh-id-number              pic 9(12).
: >            10 fd-fund-number            pic 9(4).
: >            10 fd-fund-date              pic 9(8).
: >            10 fd-fund-value             pic s9(11)v99.
: >              .... <more fields> ....
: >
: >with selects similar to:
: >
: >            select fund-master-table
: >              assign to fmt-file
: >              organization is indexed
: >              access mode is dynamic
: >              record      key is fund-number
: >              alternate   key is fund-name
: >              alternate   key is fund-report-number with duplicates.
: >
: >            select fund-history-table
: >              assign to fht-file
: >              organization is indexed
: >              access mode is dynamic
: >              record      key is fd-id-number
: >              alternate   key is fd-fund-number with duplicates
: >              alternate   key is fd-fund-date with duplicates.
: >
: >Now the task here is to print those two little buggers out on x number
: >of separate reports (report number in the master file) by fund, and only
: >for a particular (user selected) date.
: >
: >The only way I can think to do it is to sort the history file first,
: >by fund, then process each record individually in an output procedure.
: >COnversely, I could use an input and output procedure to a sort,
: >selecting by date and outputing to a particualr report queu or
: >something. Both of these solutions feel clumsy, and I of course,
: >cannot get the SQL solution out of my head.
: >
: >If someone else knows of an easier way to accomplish this probably
: >fairly common task, I'd be appreciative of a pointer or two. :)
: >I have writing 'clunky' code!
: >
: >-Paul
: >
: >
: >
```

###### ↳ ↳ ↳ Re: Sorts and such...

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36712b0b.0@news1.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <36706e5b.0@news1.ibm.net> <74q32h$gqj@lotho.delphi.com>`

```
I would still use the START on date, but read the fund-numbers
into an internal table, then sort that one (can be done in 10 lines
of code with COMBSORT, see: http://www.etk.com/papers ).

paulr wrote in message <74q32h$gqj@lotho.delphi.com>...
>The fund-report-number is a key to the lookup table that says
>which report *this* particular fund belongs on. There are a half dozen
…[113 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sorts and such...

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36715369.C85F9616@yahoo.com>`
- **References:** `<74po46$58a@lotho.delphi.com> <36706e5b.0@news1.ibm.net>`

```
I like Leif's idea of STARTing on a given date, but then you should assemble
all the data needed to print the report detail in one sort record (this
should include report #) and pass this to a sort (this will utilize an input
procedure and output procedure) and process the report in the output
procedure.  If you need summaraization the sort can do this for you but you
must pass a sort control card in a $ORTPARM card in JCL.

Leif Svalgaard wrote:

> I would do a start on the history table, with the date given and
> a not less condition. If I find a record, I'd check if the date
…[69 more quoted lines elided]…
> >
```

#### ↳ Re: Sorts and such...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74q06u$d80$1@news.igs.net>`
- **References:** `<74po46$58a@lotho.delphi.com>`

```
Have you thought of introducing a split key that has date,
fund number in it?  Often in history files, I will have 9-10
different key combinations, reflecting the various combinations
of reports required.

paulr wrote in message <74po46$58a@lotho.delphi.com>...
>Hi guys-
>  I'm doing a RAD model of some software that will be ran under CICS,
…[59 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sorts and such...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3670aef3.86681934@news1.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net>`

```
On Thu, 10 Dec 1998 21:39:00 -0500, "Donald Tees"
<donald@willmack.com> wrote:

>Have you thought of introducing a split key that has date,
>fund number in it?  Often in history files, I will have 9-10
>different key combinations, reflecting the various combinations
>of reports required.

He mentioned CICS - which means VSAM - if he had DB2 he'd just do the
SQL thing.  VSAM does not allow "split keys" --- (It's one of those
"Platform Specific" items in the new standard ... don't you know!) <G>
```

###### ↳ ↳ ↳ Re: Sorts and such...

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3670d454.73652706@news3.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net>`

```
On Fri, 11 Dec 1998 05:35:41 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>On Thu, 10 Dec 1998 21:39:00 -0500, "Donald Tees"
><donald@willmack.com> wrote:
…[8 more quoted lines elided]…
>"Platform Specific" items in the new standard ... don't you know!) <G>


Thane,

I cannot agree fully on this one ... of course CICS does not per se mean VSAM, DB2 is
supported as well.

But.... tere is a big BUT.  The program as stated will never run under CICS at all, as
CICS does not allow FD, SELECT, OPEN, or any other such things!!!!!




with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 4)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74u9hi$b4i@lotho.delphi.com>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net>`

```
Of course CICS doesn't - since the CICS application owns all the files,
straight in from the JCl. :)  But it is FAR more convienent to talk 
about the shape and organization of VSAM files in COBOL syntax, than
it is to talk about them in terms of key starts and extents. <GRIN>

The system will unfortunately, not be able to run with DB2, as the 
corporate standard is AdaBASE, and I want to avoid another level of
support if possible. VSAM should serve just fine in this instance,
which means that essentially all the normal things you do in COBOL
are available with CICS equivalents, and the file structures are
identical. 

I'm also going to have to figure out some way to updates CICS files
from a batch process, oh joy...


-Paul


Volker Bandke (vbandke@ibm.net) wrote:
: On Fri, 11 Dec 1998 05:35:41 GMT, redsky@ibm.net (Thane Hubbell) wrote:

: >On Thu, 10 Dec 1998 21:39:00 -0500, "Donald Tees"
: ><donald@willmack.com> wrote:
: >
: >>Have you thought of introducing a split key that has date,
: >>fund number in it?  Often in history files, I will have 9-10
: >>different key combinations, reflecting the various combinations
: >>of reports required.
: >
: >He mentioned CICS - which means VSAM - if he had DB2 he'd just do the
: >SQL thing.  VSAM does not allow "split keys" --- (It's one of those
: >"Platform Specific" items in the new standard ... don't you know!) <G>


: Thane,

: I cannot agree fully on this one ... of course CICS does not per se mean VSAM, DB2 is
: supported as well.

: But.... tere is a big BUT.  The program as stated will never run under CICS at all, as
: CICS does not allow FD, SELECT, OPEN, or any other such things!!!!!




: with kind regards

: Volker Bandke
: (BSP GmbH)
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367300a8.238694466@news1.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net> <74u9hi$b4i@lotho.delphi.com>`

```
On 12 Dec 1998 17:35:46 GMT, paulr@bix.com (paulr) wrote:


>I'm also going to have to figure out some way to updates CICS files
>from a batch process, oh joy...

One shop I worked at still does this today.  It's really not difficult
- if you don't use the journaling or recovery features of CICS.  Share
option 4.  (No one gasp).
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 6)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<750vn6$bo2@lotho.delphi.com>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net> <74u9hi$b4i@lotho.delphi.com> <367300a8.238694466@news1.ibm.net>`

```
<grin> Now that is thnking outside the usual box. Good thought too.
It would mean I would have to disable any interactive updates while
the batch information was loading (less than 30 seconds per load,
depending upon the scheduler I guess...) and I wonder if there is 
a good way to avoid that.  Guess I could just call up a CICS based program
that uses the input file file and writes to the CIS files with exec CICS,
but I'm not sure how or if that affects CICS ability to rollback 
changes if something goofs up.

-Paul


Thane Hubbell (redsky@ibm.net) wrote:
: On 12 Dec 1998 17:35:46 GMT, paulr@bix.com (paulr) wrote:


: >I'm also going to have to figure out some way to updates CICS files
: >from a batch process, oh joy...

: One shop I worked at still does this today.  It's really not difficult
: - if you don't use the journaling or recovery features of CICS.  Share
: option 4.  (No one gasp).
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 5)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36741080.1844512@news3.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net> <74u9hi$b4i@lotho.delphi.com>`

```
On 12 Dec 1998 17:35:46 GMT, paulr@bix.com (paulr) wrote:


>I'm also going to have to figure out some way to updates CICS files
>from a batch process, oh joy...


If you need to do updates to the VSAM files from inside CICS and from batch, I would
strongly advise AGAINST Shareoption 4....You could either use Shareoption5 (which is a CA
product (yukk)) or, much better, you could use EXCI (External CICS Interface)  to send the
update requests from batch to the owning CICS region and have them done there, by CICS, on
behalf of the batch program.

HTH


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 6)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981213192454.07170.00000772@ngol05.aol.com>`
- **References:** `<36741080.1844512@news3.ibm.net>`

```

In article <36741080.1844512@news3.ibm.net>, vbandke@ibm.net (Volker Bandke)
writes:

>If you need to do updates to the VSAM files from inside CICS and from batch,
>I would
>strongly advise AGAINST Shareoption 4

Yes, there is an I/O penalty for using SHR(4), but we have never experienced
corrupt data due to it.

Our heavily-used in-house stuff is currently in Datacom/DB and we have a lot of
applications using VSAM/Transparency to get to it. It provides the concurrent
batch and online updates but without the heavy I/O penalty. If there is a
transaction abend, when CICS does a backout the updates will automatically be
rolled back. Likewise, if a batch job does some updates and abends, those
updates will be rolled back.

One problem would be if both VSAM and VSAM/T files are updated in batch and an
abend occurs--only the VSAM/T (Datacom/DB) will be rolled back.

Mark A. Young
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3674693f.331018828@news1.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net> <74u9hi$b4i@lotho.delphi.com> <36741080.1844512@news3.ibm.net>`

```
On Sun, 13 Dec 1998 19:11:05 GMT, vbandke@ibm.net (Volker Bandke)
wrote:

>On 12 Dec 1998 17:35:46 GMT, paulr@bix.com (paulr) wrote:
>
…[9 more quoted lines elided]…
>behalf of the batch program.

BTW  - I agree.  Share option 4 does not maintan total data integrity
- but it's a lot better than 3!

Anyway, I never had any problems using Shareoption 4 with Batch and
online updates - so long as only a single batch region/partition
updated the file when CICS had it open.  When 2 batch regions, AND
CICS could update the file we almost ALWAYS had corruptions of the
VSAM file.
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 7)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-12-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3674c2f2.45057178@news3.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <3670aef3.86681934@news1.ibm.net> <3670d454.73652706@news3.ibm.net> <74u9hi$b4i@lotho.delphi.com> <36741080.1844512@news3.ibm.net> <3674693f.331018828@news1.ibm.net>`

```
On Mon, 14 Dec 1998 01:27:56 GMT, redsky@ibm.net (Thane Hubbell) wrote:


>
>BTW  - I agree.  Share option 4 does not maintan total data integrity
…[6 more quoted lines elided]…
>VSAM file.  

Thane,

as far as I know Shareoption 4 does not provide ANY update integrity across address
spaces.  It does provide READ integrity be rereading the VSAM buffers every time a record
is requested (that way defeating LSR and other caching like mechanism that might be
emploied to increase performance).  I believe that Shareoption 4 only means that VSAM
allows two MVS jobs to open the file simultaneously for update, and the users (i.e. the
jobs opening the file) need to provide record locking themselves, using MVS mechanisms (I
do not know anything about VSE, things there might be different)

BTW, how do you handle inserts to a VSAM file with shareoption 4?  You could have CI
splits, changes of the HURBA in one address space, and the data in the new CIs would not
be available to the other address space - all in all I find Shareoption4 to be less then
optimum  <g>


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 8)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981215213038.07764.00001048@ngol08.aol.com>`
- **References:** `<3674c2f2.45057178@news3.ibm.net>`

```

In article <3674c2f2.45057178@news3.ibm.net>, vbandke@ibm.net (Volker Bandke)
writes:

>(I do not know anything about VSE, things there might be different)

In VSE, SHR(3) allows multiple jobs to open the file for update, but has no
mechanism for preventing corruption. (That is up to the application.) SHR(3) is
very dangerous.

SHR(4) allows multiple appliations to open the file for update, and further
provide CI locking and, within a CICS, will also do record-level locking
(record-level only within that CICS but still lock the CI for everything else
outside of that CICS).

Furthermore, on a random read (with or without update intent) SHR(4) will
always reread the sequence set (lowest-level index) CI and reread the data CI
(even when LSR is used). (The reading of the sequence set CI and data CI on
every random read is what gives the high I/O penalty for SHR(4).) Sequential
processing will not reread the CI and can do read-ahead.

We have never experienced any file corruption when using SHR(4), but then we
almost never do inserts from batch while CICS has the file open.

Mark A. Young
```

###### ↳ ↳ ↳ Re: Sorts and such...

_(reply depth: 9)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36776bc7.140279391@news3.ibm.net>`
- **References:** `<3674c2f2.45057178@news3.ibm.net> <19981215213038.07764.00001048@ngol08.aol.com>`

```
On 16 Dec 1998 02:30:38 GMT, mark0young@aol.com (Mark0Young) wrote:

>
>SHR(4) allows multiple appliations to open the file for update, and further
>provide CI locking and, within a CICS, will also do record-level locking
>(record-level only within that CICS but still lock the CI for everything else
>outside of that CICS).
<rest snipped>


Thanks for the enlightenment


with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: Sorts and such...

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ra0o$e6r@lotho.delphi.com>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net>`

```
?? I honestly don't know how to do that in COBOL. You can assign
to or more fields to a single key, as you can in a database?

-Paul
.


Donald Tees (donald@willmack.com) wrote:
: Have you thought of introducing a split key that has date,
: fund number in it?  Often in history files, I will have 9-10
: different key combinations, reflecting the various combinations
: of reports required.

: paulr wrote in message <74po46$58a@lotho.delphi.com>...
: >Hi guys-
: >  I'm doing a RAD model of some software that will be ran under CICS,
: >perhaps with a database backend, and today I ran into a bit of a
: >puzzler. Figured I would ask older and wiser heads for a pointer. :)
: >
: >  Since I suspect this will have to be hosted in a RDBMs, I've
: >been treating the COBOL files like db tables, with appropriate
: >indcies and so on.  well imagine a pair ot tables like
: >this:
: >
: >        fd  fund-master-table.
: >        01  fund-master-table-record.
: >            10 fund-number               pic 9(4).
: >            10 fund-name                 pic x(25).
: >            10 fund-report-number        pic 9(6).
: >              .... <more fields> ....
: >
: >        fd  fund-history-table.
: >        01  fund-history-table-record.
: >            10 fh-id-number              pic 9(12).
: >            10 fd-fund-number            pic 9(4).
: >            10 fd-fund-date              pic 9(8).
: >            10 fd-fund-value             pic s9(11)v99.
: >              .... <more fields> ....
: >
: >with selects similar to:
: >
: >            select fund-master-table
: >              assign to fmt-file
: >              organization is indexed
: >              access mode is dynamic
: >              record      key is fund-number
: >              alternate   key is fund-name
: >              alternate   key is fund-report-number with duplicates.
: >
: >            select fund-history-table
: >              assign to fht-file
: >              organization is indexed
: >              access mode is dynamic
: >              record      key is fd-id-number
: >              alternate   key is fd-fund-number with duplicates
: >              alternate   key is fd-fund-date with duplicates.
: >
: >Now the task here is to print those two little buggers out on x number
: >of separate reports (report number in the master file) by fund, and only
: >for a particular (user selected) date.
: >
: >The only way I can think to do it is to sort the history file first,
: >by fund, then process each record individually in an output procedure.
: >COnversely, I could use an input and output procedure to a sort,
: >selecting by date and outputing to a particualr report queu or
: >something. Both of these solutions feel clumsy, and I of course,
: >cannot get the SQL solution out of my head.
: >
: >If someone else knows of an easier way to accomplish this probably
: >fairly common task, I'd be appreciative of a pointer or two. :)
: >I have writing 'clunky' code!
: >
: >-Paul
: >
: >
: >
```

###### ↳ ↳ ↳ Re: Sorts and such...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rc41$8hj$1@news.igs.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <74ra0o$e6r@lotho.delphi.com>`

```
The split key feature is present is apparently non-standard,
so not all compilers have it.  Both MF and Fujitsu do, though.
A typical select is as below.  (The answer is yes). The code
shown is MF code.  DTRK-INTO-THE-YARD is *not* a field
in the record of the file ... the name appears *only* in the
select clause, and can be used in the normal way in read
statements.  The various fields are concatenated into a
pseudo field which is placed into the index.  Note that with
Fujitsu, you omit the key name, and list the actual fields
when you do the read.

The method will not save you scanning the file, but it will save
you having to do a sort.  You should also note that if you do
a bunch of split key stuff, the index can actually get quite a bit
bigger than the actual data file. I have found it quite a useful
technique, especially for history files as they do not tend to
have a lot of updating. It can also be handy when an existing
file gets a new requirement, as you do not have to change
the file layout, though you would have to re-index and recompile
everything.

  SELECT DTRK-FILE ASSIGN TO DISK
   ORGANIZATION IS INDEXED
   ACCESS IS DYNAMIC
   FILE STATUS IS DTRK-STATUS
   RECORD KEY IS DTRK-KEY
   ALTERNATE KEY IS DTRK-INTO-THE-YARD =
                                DTRK-SHOW, DTRK-TARE-DATE
                                DTRK-IN, DTRK-KEY
   ALTERNATE RECORD KEY IS DTRK-DISPATCH-KEY
    WITH DUPLICATES.

paulr wrote in message <74ra0o$e6r@lotho.delphi.com>...
>?? I honestly don't know how to do that in COBOL. You can assign
>to or more fields to a single key, as you can in a database?
…[75 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sorts and such...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rc6o$8i4$1@news.igs.net>`
- **References:** `<74po46$58a@lotho.delphi.com> <74q06u$d80$1@news.igs.net> <74ra0o$e6r@lotho.delphi.com>`

```
P.S. To that last ... note what Thane says about VSAM ...

paulr wrote in message <74ra0o$e6r@lotho.delphi.com>...
>?? I honestly don't know how to do that in COBOL. You can assign
>to or more fields to a single key, as you can in a database?
…[75 more quoted lines elided]…
>
```

#### ↳ Re: Sorts and such...

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-12-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3671d4ee.73806788@news3.ibm.net>`
- **References:** `<74po46$58a@lotho.delphi.com>`

```
On 11 Dec 1998 00:13:58 GMT, paulr@bix.com (paulr) wrote:

>Hi guys-
>  I'm doing a RAD model of some software that will be ran under CICS,
…[13 more quoted lines elided]…
>              .... <more fields> ....


Paul,

if your program is to run under CICS, then you cannot use FD, SELECT, OPEN, etc in your
program.  You have to use either the native CICS functions (EXEC CICS READ FILE),  or you
should revert to DB2  (EXEC SQL SELECT)


with kind regards

Volker Bandke
(BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
