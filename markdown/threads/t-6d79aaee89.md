[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Modular Primary Key

_25 messages · 9 participants · 1999-02_

---

### Modular Primary Key

- **From:** "zoran" <antonicz@EUnet.yu>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu>`

```
Hello
Can you tell me do you use modular number  for PRIMARY KEY of indexed file
Which modul is the best ( 10,11 or 12) ?
Is there  in business aplications any other moduls.
Thanks in advance.
    Zoran Antonic
```

#### ↳ Re: Modular Primary Key

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c8905d.77652054@news1.ibm.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu>`

```
On Mon, 15 Feb 1999 19:44:56 +0100, "zoran" <antonicz@EUnet.yu> wrote:

>Hello
>Can you tell me do you use modular number  for PRIMARY KEY of indexed file
…[3 more quoted lines elided]…
>    Zoran Antonic

Not sure what you are asking here.  I have a technique that I use that
uses a 16 digit number as a "record handle" that gets created when a
record is added.  I then have an "alternate key" that I process as
others would primary key information.  This allows me to do many
interesting things.  (Related records in a secondary file to the
primary file with this record handle, then allow a seemingly primary
key change without losing the reference to the original record).

ie.  You might have a file of names and addresses.  In another file
you might have the detail of all the purchases this person had made.
Common practice is to key the main file by name, and then store this
key in the detail file.  Instead, I make the primary key of the name
file the record handle (Date/Time checked for duplicates at add time -
if data coming from multiple sources, I add a source code number to
this key) - then make the name the first alternate key. The handle
(which NEVER changes) is stored in the detail file instead of the
name.  Then if someone gets married, or changes their name, the
history is not lost.

But no particular modulus is used for the primary key.
```

##### ↳ ↳ Re: Modular Primary Key/Key technics

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7afmob$m6c$1@fenix.maxitel.pt>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net>`

```

Thane Hubbell wrote<36c8905d.77652054@news1.ibm.net>...
>On Mon, 15 Feb 1999 19:44:56 +0100, "zoran" <antonicz@EUnet.yu> wrote:
>>Hello
…[7 more quoted lines elided]…
>Common practice is to key the main file by name, and then store this

1. Why is it so uncommon in cobol world to have files indexed by
auto-incremented primary keys instead of the actual data of the records? Or
isn't it that unusual ? To my mind this should be the standard approach for
relational file handling.

>key in the detail file.  Instead, I make the primary key of the name
>file the record handle (Date/Time checked for duplicates at add time -
…[4 more quoted lines elided]…
>history is not lost.


2. Nonetheless, why do you prefer that way of generating your automatic
primary key instead of just simply having a straight number for that ?
Because of concerns on the way of storing it ?

>(snip)

Rgds
P.Cruz
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7afts5$5v1$1@news.igs.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt>`

```
PAULO CRUZ wrote in message <7afmob$m6c$1@fenix.maxitel.pt>...

>1. Why is it so uncommon in cobol world to have files indexed by
>auto-incremented primary keys instead of the actual data of the records? Or
>isn't it that unusual ? To my mind this should be the standard approach for
>relational file handling.


There is very little need for it, in most cases.  If I need
to do access by customer name, for example, why look
the name up to get a symbolic key, then use the key
to look up the record?

>2. Nonetheless, why do you prefer that way of generating your automatic
>primary key instead of just simply having a straight number for that ?
>Because of concerns on the way of storing it ?


Using the date or time for a key is much simpler than using
a straight number for the simple reason that you do not have
to keep track of what number to use next.  That is not quite
as simple a problem as it might appear when you have hundreds
of simultaneous users. (also faster).
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CC254D.71899E3F@NOSPAMhome.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt>`

```
> 1. Why is it so uncommon in cobol world to have files indexed by
> auto-incremented primary keys instead of the actual data of the records? Or
> isn't it that unusual ? To my mind this should be the standard approach for
> relational file handling.

One file is not relational - at least two are required to relate.  If
you say each record should be stored with an external sequentially
numbered key, what's the point?  We want the records in a particular
order based upon data.  We want to be able to insert a record somewhere
in the middle of the file without lots of overhead.  

I suspect I am not understanding your question.

If I want a phone book file sorted by last name, first name, I can index
by those names.  I can allow for duplicates, look up a name quickly, and
add a new name.  How do you propose to do this with auto-incremented
primary keys?
 
What you describe seems to be more like what I have used relative
datasets to do.  I don't see these very often anymore, but they used to
be very common.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 4)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ahbc1$8f7@lotho.delphi.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com>`

```

Because it is very common to do so in large database systems, though
perhaps excepting COBOL. You use a series of sequential keys that
allow you to relate information all over the place, and you use 
Alternate Indexes to gain access to information in the order you wish. 

Typically, you would assign a new client a sequential account number,
and use that to link all transactional information to the client.
At the same time, you may have alternate indicies on the client file
that allow you to use last name, company name, type of account,
account start date, or any number of other flags to access and
select information very quickly. 

There is some overhead in maintaining the additional keys yes,
but in some, maybe most, systems it pays back quickly. In your 
example, for instance, suppose I wanted to find and present a
pick list of all the clients with account types of 'ABC' - 
if I have an index on it, I can start the file with the 
correct key, and just read on sequentially till the key 
changes value. At the same time, someone else or a separate
process can be adding new records.

This is primarly for online systems of course, old style batch
systems can afford to plow through files via brute force, or 
do a sort operation when needed. If you have a couple hundred people
hammering at a database, looking up and relating customer accounts 
with invoices and invoice details and payments/payment details and
inventory and purchase orders and so forth and so on, it makes a 
lot of sense to have the relation key a simple integer. They are
also faster to sort, and easier to order. 

Also, the overhead in assiging keys is not that great, most applications
do not have truely massive and high speed data input, but even if they
do, you can usually lock the table in memory somehow or another
and it takes very little overhead to use. 

In CICS programs, I use a TABLE instead of a file, so that it remains
memory resident and is very quick to use. 

-Paul


Howard Brazee (brazee@NOSPAMhome.com) wrote:
: > 1. Why is it so uncommon in cobol world to have files indexed by
: > auto-incremented primary keys instead of the actual data of the records? Or
: > isn't it that unusual ? To my mind this should be the standard approach for
: > relational file handling.

: One file is not relational - at least two are required to relate.  If
: you say each record should be stored with an external sequentially
: numbered key, what's the point?  We want the records in a particular
: order based upon data.  We want to be able to insert a record somewhere
: in the middle of the file without lots of overhead.  

: I suspect I am not understanding your question.

: If I want a phone book file sorted by last name, first name, I can index
: by those names.  I can allow for duplicates, look up a name quickly, and
: add a new name.  How do you propose to do this with auto-incremented
: primary keys?
:  
: What you describe seems to be more like what I have used relative
: datasets to do.  I don't see these very often anymore, but they used to
: be very common.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 5)_

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ai5pt$7vu$2@fenix.maxitel.pt>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ahbc1$8f7@lotho.delphi.com>`

```
Paul, I agree with you.
Whereas speaking about structured code is something
nobody gives an hint of ignoring the importance of, it seems the same
doesn't apply when structured data arises as a question of debate...

Rgds
P.Cruz

paulr wrote<7ahbc1$8f7@lotho.delphi.com>...
>
>Because it is very common to do so in large database systems, though
…[31 more quoted lines elided]…
>-Paul
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 4)_

- **From:** "PAULO CRUZ" <scruz_paulo@mail.teleweb.pt>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ai5pn$7vu$1@fenix.maxitel.pt>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com>`

```

Howard Brazee wrote: <36CC254D.71899E3F@NOSPAMhome.com>...
>
>One file is not relational - at least two are required to relate.  If

Many thanks for the enlightenment above...

>you say each record should be stored with an external sequentially
>numbered key, what's the point?  We want the records in a particular
…[6 more quoted lines elided]…
>primary keys?

Even for a situation as the one described (a supposedly non-related file)
I would stick to the auto-incremented-key-technique, for the simple reason
that it would allow me to easily change that field that otherwise you would
assign the primary key to.
Don't you agree it has its conveniences?


>
>What you describe seems to be more like what I have used relative
>datasets to do.  I don't see these very often anymore, but they used to
>be very common.

Now it's my turn not to understand what your point is...sorry.

Rgds
P.Cruz
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CC9C30.746003E2@NOSPAMhome.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt>`

```
> >you say each record should be stored with an external sequentially
> >numbered key, what's the point?  We want the records in a particular
…[12 more quoted lines elided]…
> Don't you agree it has its conveniences?

No.  If I want to change my primary key, I want to change my primary
sort order.  Your method sounds like it wants to be in a FIFO order
unrelated to the data.  In my phone book example, I could change
someone's last name - and you would prefer to keep the record where it
was.  Is it convenient to if my daughter is now an Ellison, that she
still is stored between Brace and Brown?

> >What you describe seems to be more like what I have used relative
> >datasets to do.  I don't see these very often anymore, but they used to
> >be very common.
> 
> Now it's my turn not to understand what your point is...sorry.

Lots of old relative file processing had someone read the first record
to find out what the current record is.  They incremented this counter
and rewrote the first record then skipped directly to the current record
to add more data.  Everything is in the order entered.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ccfaab.125654724@news1.ibm.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <36CC9C30.746003E2@NOSPAMhome.com>`

```
On Thu, 18 Feb 1999 16:03:12 -0700, Howard Brazee
<brazee@NOSPAMhome.com> wrote:


>No.  If I want to change my primary key, I want to change my primary
>sort order.  Your method sounds like it wants to be in a FIFO order
…[4 more quoted lines elided]…
>

You misunderstand I think.  What we are advocating is very powerful.

See below.

Select Personal-Data Assign to Foo 
                                   record key is Record-Handle
                                   alternate key is Phone-Number
                                   alternate key is Full-Name

See where we are getting here.  When the record is initially added, it
has a primary key of Record-Handle - the sequential (or some other
method) number.  This NEVER changes.  This record is ALWAYS associated
with your daughter.  You can now change ANYTHING about this record,
WITHOUT impacting the "Primary" key.  This means that if you have
OTHER files that refer to your daughter - they need only store the
HANDLE, and current and appropriate detail information will be
available.  Reads by name or telephone number will always return
records in the proper sequence.  When I use this, which I often do, I
NEVER read via the real "prime" key.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CD84FB.D7E8FD0E@NOSPAMhome.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <36CC9C30.746003E2@NOSPAMhome.com> <36ccfaab.125654724@news1.ibm.net>`

```
So when you're accessing this file using indexed access methods - not
using SQL to link it with another file.  When you are treating it as a
single file, not a database - what's the advantage of having the
record-handle primary key?  When am I going to access a record by that
key?

I know it's a powerful technique in database design, but we're talking
ISAM or KSDS files here.

Thane Hubbell wrote:
> 
> On Thu, 18 Feb 1999 16:03:12 -0700, Howard Brazee
…[28 more quoted lines elided]…
> NEVER read via the real "prime" key.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-xcbv3OjuiBPF@Dwight_Miller.iix.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <36CC9C30.746003E2@NOSPAMhome.com> <36ccfaab.125654724@news1.ibm.net>`

```
On Fri, 19 Feb 1999 05:50:21, redsky@ibm.net (Thane Hubbell) wrote:

> available.  Reads by name or telephone number will always return
> records in the proper sequence.  When I use this, which I often do, I
> NEVER read via the real "prime" key.
> 

It was late, and I was mistaken.  Of COURSE I read via this prime key 
- when obtained from a referring file!  Sheesh.


-------------------------
Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aifqh$jt9$1@news.igs.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt>`

```
There are many occasions when you do not *want*
the primary key changed.  While I would not denigrate
the use of a relative key where applicable, it is just
as silly to say it should always be used.  You can
cross-reference with any key, not just a relative one.

There are also many cases where the secondary
record needs to know the primary key -- for example
a history file needs a product code.  To force that
program to store a number that points to the product
record and look up the product record to get the
product code is sheer waste. It also makes it doubly
difficult to find history records for specific products.

As another example, I design systems that handle
shipping.  Trucks are in files indexed by a truck number that is
their licence plate. I have about a dozen other files that
reference that truck by licence plate number. Making
all cross-references to an arbitrary record number that
can be used to look up the licence vastly complicates
the system, as there are about thirty computers involved,
and each has it's own list of trucks, each maintained
separately.  Some of those computers are for other
companies, some are at customs, some are at the
ministry of transport.  What should I give them in a
bill of lading record?  A cross-reference to my personal
list of trucks?  A licence plate number works far easier.
That is precisely why Isam superseded relative files
thirty years ago.  It makes life easier.

In cases where the key to the file must be symbolic,
to add your own relative key just duplicates a facility
already built into the Isam element of the language.
It adds a level of complexity, and gains you nothing.

Both techniques have their place.  Certainly with
something like financial records, I have used a
sequential primary key and secondary indices, but
it is not all that common.

PAULO CRUZ wrote in message <7ai5pn$7vu$1@fenix.maxitel.pt>...
>
>Howard Brazee wrote: <36CC254D.71899E3F@NOSPAMhome.com>...
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 6)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aiorb$c1b@lotho.delphi.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net>`

```
Well, actually, it *is* that common. Most SQL database 
systems force you to have a primary key that is unique. 
You can either supply it yourself, or use whatever
autoincrement format is handy.

In your example, there is really no benefit to 
using the license number over an arbitrary key;
the information store is hardly human readably 
anyway. 

And really good database design VERY rarely designs
any relational data structures whre the primary 
key has to be changed. 

I've done some logistics before, and found that
most of the operations are well supported by
relational technology. 

Yours,
-Paul


Donald Tees (donald@willmack.com) wrote:
: There are many occasions when you do not *want*
: the primary key changed.  While I would not denigrate
: the use of a relative key where applicable, it is just
: as silly to say it should always be used.  You can
: cross-reference with any key, not just a relative one.

: There are also many cases where the secondary
: record needs to know the primary key -- for example
: a history file needs a product code.  To force that
: program to store a number that points to the product
: record and look up the product record to get the
: product code is sheer waste. It also makes it doubly
: difficult to find history records for specific products.

: As another example, I design systems that handle
: shipping.  Trucks are in files indexed by a truck number that is
: their licence plate. I have about a dozen other files that
: reference that truck by licence plate number. Making
: all cross-references to an arbitrary record number that
: can be used to look up the licence vastly complicates
: the system, as there are about thirty computers involved,
: and each has it's own list of trucks, each maintained
: separately.  Some of those computers are for other
: companies, some are at customs, some are at the
: ministry of transport.  What should I give them in a
: bill of lading record?  A cross-reference to my personal
: list of trucks?  A licence plate number works far easier.
: That is precisely why Isam superseded relative files
: thirty years ago.  It makes life easier.

: In cases where the key to the file must be symbolic,
: to add your own relative key just duplicates a facility
: already built into the Isam element of the language.
: It adds a level of complexity, and gains you nothing.

: Both techniques have their place.  Certainly with
: something like financial records, I have used a
: sequential primary key and secondary indices, but
: it is not all that common.

: PAULO CRUZ wrote in message <7ai5pn$7vu$1@fenix.maxitel.pt>...
: >
: >Howard Brazee wrote: <36CC254D.71899E3F@NOSPAMhome.com>...
: >>
: >>One file is not relational - at least two are required to relate.  If
: >
: >Many thanks for the enlightenment above...
: >
: >>you say each record should be stored with an external sequentially
: >>numbered key, what's the point?  We want the records in a particular
: >>order based upon data.  We want to be able to insert a record somewhere
: >>in the middle of the file without lots of overhead.
: >>I suspect I am not understanding your question.
: >>If I want a phone book file sorted by last name, first name, I can index
: >>by those names.  I can allow for duplicates, look up a name quickly, and
: >>add a new name.  How do you propose to do this with auto-incremented
: >>primary keys?
: >
: >Even for a situation as the one described (a supposedly non-related file)
: >I would stick to the auto-incremented-key-technique, for the simple reason
: >that it would allow me to easily change that field that otherwise you would
: >assign the primary key to.
: >Don't you agree it has its conveniences?
: >
: >
: >>
: >>What you describe seems to be more like what I have used relative
: >>datasets to do.  I don't see these very often anymore, but they used to
: >>be very common.
: >
: >Now it's my turn not to understand what your point is...sorry.
: >
: >Rgds
: >P.Cruz
: >
: >
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 6)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aiotg$c1b@lotho.delphi.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net>`

```
Oh, and you are mixing up COBOL RELATIVE files
with RELATIONAL files a bit; 

Relational files are almost always INDEXED and
use a DYNAMIC access mode.

-Paul


Donald Tees (donald@willmack.com) wrote:
: There are many occasions when you do not *want*
: the primary key changed.  While I would not denigrate
: the use of a relative key where applicable, it is just
: as silly to say it should always be used.  You can
: cross-reference with any key, not just a relative one.

: There are also many cases where the secondary
: record needs to know the primary key -- for example
: a history file needs a product code.  To force that
: program to store a number that points to the product
: record and look up the product record to get the
: product code is sheer waste. It also makes it doubly
: difficult to find history records for specific products.

: As another example, I design systems that handle
: shipping.  Trucks are in files indexed by a truck number that is
: their licence plate. I have about a dozen other files that
: reference that truck by licence plate number. Making
: all cross-references to an arbitrary record number that
: can be used to look up the licence vastly complicates
: the system, as there are about thirty computers involved,
: and each has it's own list of trucks, each maintained
: separately.  Some of those computers are for other
: companies, some are at customs, some are at the
: ministry of transport.  What should I give them in a
: bill of lading record?  A cross-reference to my personal
: list of trucks?  A licence plate number works far easier.
: That is precisely why Isam superseded relative files
: thirty years ago.  It makes life easier.

: In cases where the key to the file must be symbolic,
: to add your own relative key just duplicates a facility
: already built into the Isam element of the language.
: It adds a level of complexity, and gains you nothing.

: Both techniques have their place.  Certainly with
: something like financial records, I have used a
: sequential primary key and secondary indices, but
: it is not all that common.

: PAULO CRUZ wrote in message <7ai5pn$7vu$1@fenix.maxitel.pt>...
: >
: >Howard Brazee wrote: <36CC254D.71899E3F@NOSPAMhome.com>...
: >>
: >>One file is not relational - at least two are required to relate.  If
: >
: >Many thanks for the enlightenment above...
: >
: >>you say each record should be stored with an external sequentially
: >>numbered key, what's the point?  We want the records in a particular
: >>order based upon data.  We want to be able to insert a record somewhere
: >>in the middle of the file without lots of overhead.
: >>I suspect I am not understanding your question.
: >>If I want a phone book file sorted by last name, first name, I can index
: >>by those names.  I can allow for duplicates, look up a name quickly, and
: >>add a new name.  How do you propose to do this with auto-incremented
: >>primary keys?
: >
: >Even for a situation as the one described (a supposedly non-related file)
: >I would stick to the auto-incremented-key-technique, for the simple reason
: >that it would allow me to easily change that field that otherwise you would
: >assign the primary key to.
: >Don't you agree it has its conveniences?
: >
: >
: >>
: >>What you describe seems to be more like what I have used relative
: >>datasets to do.  I don't see these very often anymore, but they used to
: >>be very common.
: >
: >Now it's my turn not to understand what your point is...sorry.
: >
: >Rgds
: >P.Cruz
: >
: >
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CD8439.1984BE90@NOSPAMhome.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net> <7aiotg$c1b@lotho.delphi.com>`

```
paulr wrote:
> 
> Oh, and you are mixing up COBOL RELATIVE files
…[5 more quoted lines elided]…
> -Paul

Your usage of the word relational, sounds like files used by a
relational database, and usually accessed via SQL.  A single file is not
relational as it does not relate to anything else.  It is just an
indexed file.  If you're not relating a record across files, there is
hardly ever a reason for having an independent key.  Instead, we key on
data fields.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 8)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ak6ds$isg@lotho.delphi.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net> <7aiotg$c1b@lotho.delphi.com> <36CD8439.1984BE90@NOSPAMhome.com>`

```
Not entirely true. You may want to relate that single gile to itself;
or in other words, you might want to have multiple keys. You may want
to have views into the data from a single table, which effectively,
presents a view of more than one table. 

There are lots of valid examples. On the other hand, if the file doesn't
need that klind of flexibilty, or will be used from Batch only, then
it makes more sense to take your point of view. :) 
-Paul


Howard Brazee (brazee@NOSPAMhome.com) wrote:
: paulr wrote:
: > 
: > Oh, and you are mixing up COBOL RELATIVE files
: > with RELATIONAL files a bit;
: > 
: > Relational files are almost always INDEXED and
: > use a DYNAMIC access mode.
: > 
: > -Paul

: Your usage of the word relational, sounds like files used by a
: relational database, and usually accessed via SQL.  A single file is not
: relational as it does not relate to anything else.  It is just an
: indexed file.  If you're not relating a record across files, there is
: hardly ever a reason for having an independent key.  Instead, we key on
: data fields.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7akas5$mlr$1@news.igs.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net> <7aiotg$c1b@lotho.delphi.com>`

```
No, I am not.  If I am going to do all my updating via a
sequentially assigned key, then a relative file is far faster
than using Isam.

Years back, the standard way of doing things was to use
a relative file, then use an entirely separate file for indexing
symbolic keys. The symbolic key (loaded into an array, or
constructed into a tree, or whatever) contained either a
relative key or a random key.  Isam was invented precisely
to make that simple.

Most Isam still works that way internally. What you are
suggesting is that each Isam file should have a symbolic
tree structure for the relative keys, and they should be
visible, imbedded into the record, with secondary indices
for the data oriented keys. I am saying that it should not,
unless there is a valid reason for it.

Sure, there often is.  Particularly with items like names
that can change.  However, there are also places where
there is no advantage, and you are simply increasing
overhead.

As to your admonation that the licence plate number has
no advantage because it is not humanly readable, it is
not machine readable either, if I do not have a copy
of the file that relates the two.  Why would I send a record
to a customs broker 1500 miles away on another computer
that references *my* truck number 12345, and expect their
computer to know that it carries licence plate number XZY-321?

The fact that I can look it up before I send it and change
all the pointers in the record is fact, but far more work than just
creating it (and using it internally) with the symbolic key in the first
place.

paulr wrote in message <7aiotg$c1b@lotho.delphi.com>...
>Oh, and you are mixing up COBOL RELATIVE files
>with RELATIONAL files a bit;
…[61 more quoted lines elided]…
>: >>If I want a phone book file sorted by last name, first name, I can
index
>: >>by those names.  I can allow for duplicates, look up a name quickly,
and
>: >>add a new name.  How do you propose to do this with auto-incremented
>: >>primary keys?
>: >
>: >Even for a situation as the one described (a supposedly non-related
file)
>: >I would stick to the auto-incremented-key-technique, for the simple
reason
>: >that it would allow me to easily change that field that otherwise you
would
>: >assign the primary key to.
>: >Don't you agree it has its conveniences?
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CD834E.5DE7B992@NOSPAMhome.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net>`

```
Donald Tees wrote:
> 
> There are many occasions when you do not *want*
…[3 more quoted lines elided]…
> cross-reference with any key, not just a relative one.

I understand that, and most all of them involve multiple files - which
is why we got the following exchange: 

>>One file is not relational - at least two are required to relate.  If
>
>Many thanks for the enlightenment above...

I caught your sarcasm, but I think you missed why I made that point.

For a single ISAM file, it usually makes sense to key on real data. 
This was my point, and it remains my point.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7akav9$mm4$1@news.igs.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net> <36CD834E.5DE7B992@NOSPAMhome.com>`

```
I agree.

Howard Brazee wrote in message <36CD834E.5DE7B992@NOSPAMhome.com>...
>Donald Tees wrote:
>>
…[16 more quoted lines elided]…
>This was my point, and it remains my point.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-FBO84MdIdrRw@Dwight_Miller.iix.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt> <36CC254D.71899E3F@NOSPAMhome.com> <7ai5pn$7vu$1@fenix.maxitel.pt> <7aifqh$jt9$1@news.igs.net> <36CD834E.5DE7B992@NOSPAMhome.com>`

```
On Fri, 19 Feb 1999 15:29:18, Howard Brazee <brazee@NOSPAMhome.com> 
wrote:

>> For a single ISAM file, it usually makes sense to key on real data.

> This was my point, and it remains my point.

Even in that case, using the "record handle" allows you to change the 
"visible" prime key.

For example:  You key on "customer number" - and for some reason you 
want to change it.  If the "handle" method is used, you can do just 
that - and REWRITE the record instead of doing a delete and an add.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cb90a2.32959605@news1.ibm.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt>`

```
On Wed, 17 Feb 1999 21:39:11 +0100, "PAULO CRUZ"
<scruz_paulo@mail.teleweb.pt> wrote:


>
>2. Nonetheless, why do you prefer that way of generating your automatic
>primary key instead of just simply having a straight number for that ?
>Because of concerns on the way of storing it ?

Very valid question.  Two reasons.

1.  I use the date/time (YYYYMMDDHHMMSShh) as the handle (with an
additional identifyer for source when necessary).  I can tell easily
when the record was initially created.

2.  Because of this scheme, I do not have to have a common "source"
for the sequence number.  By using this method, I do not have the
extra overhead of an additional file I/O simply to assign a number.

-- in fact, at work we have a process that runs on two different
platofrms, feeding an Oracle database - with sequenced records.
Because of the need for a common source for the sequence number - the
data is transfered from one platform to another for processing.
```

###### ↳ ↳ ↳ Re: Modular Primary Key/Key technics

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CC1FA2.2EC38634@zip.com.au>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu> <36c8905d.77652054@news1.ibm.net> <7afmob$m6c$1@fenix.maxitel.pt>`

```
PAULO CRUZ wrote:
> 
> 1. Why is it so uncommon in cobol world to have files indexed by
…[3 more quoted lines elided]…
> 

The answer to this one is simple.  If you have 1,000 users creating the
records and write a program that just checks for the last number you are
going to get problems.  The other problem is automatically finding the
last number quickly.

Common approach for 'magic' numbers is to have a parameter on a
different file and read (checking for locks) and updating / releasing
it.

Quite simply magic keys are a very old idea.  They are handy to cross
relate things but queries are generally done on the real data.

Ken
```

#### ↳ Re: Modular Primary Key

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0EA9D56339666AFE.170F35A8C4640CB6.A4CD1E68EDE7B902@library-proxy.airnews.net>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu>`

```
On Mon, 15 Feb 1999 19:44:56 +0100, "zoran" <antonicz@EUnet.yu>
enlightened us:

>Hello
>Can you tell me do you use modular number  for PRIMARY KEY of indexed file
…[4 more quoted lines elided]…
>

There is no reason why you can't do this.  If your primary key is,
e.g., an account number and the last digit is a calculated check digit
using a modulus 10, 11, 12 or any other scheme, then it could
certainly be the primary key of an indexed file.

There is no best modul to use.  It depends on the range of the base
number and its size.  The only thing is that you must stay consistent.
If you start with a modulus 10, you can't switch to modulus 11, say,
in the middle.

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Middle age is when you choose your cereal for the
fiber, not the toy.

 Steve
```

#### ↳ Re: Modular Primary Key

- **From:** petwir <petwir@saif.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CB6E49.59A@saif.com>`
- **References:** `<7a9pva$hqs$1@SOLAIR2.EUnet.yu>`

```
zoran wrote:
> 
> Hello
…[4 more quoted lines elided]…
>     Zoran Antonic

I really like modul 11.
We use it on an insurance claim number here.
Pete
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
