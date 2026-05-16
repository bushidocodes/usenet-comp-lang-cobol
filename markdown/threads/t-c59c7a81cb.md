[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Database Field Setup

_10 messages · 8 participants · 2000-10 → 2000-11_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Database Field Setup

- **From:** Millenium Business Solutions <mbs@labyrinth.net.au>
- **Date:** 2000-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F693F4.448E535E@labyrinth.net.au>`

```
We're redeveloping our systems in Fujitsu Power Cobol and just decided
to also convert our ISAM files to database at the same time.  One
problem we've noticed is that database tables don't seem to be able to
have 'Occurs X times' on a field.  We have a lot of fields in our ISAM
files that use this.  Does anyone know how to emulate this in a database
table without actually typing one field for each occurs?  We're
currently using the Access database.

Thanks in advance,

Robert Garde
mbs@labyrinth.net.au
```

#### ↳ Re: Database Field Setup

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2000-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t6a3f$142$1@venus.telepac.pt>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au>`

```
I am far from being an expert in DataBase programming, but I'll add my 2
bits:
If you have "OCCURS DEPENDING ON...", then, may be, you should set up
another table in wich each row corresponds to an occurrence of the
field/group in the Cobol FD. On the other way, if the occurrences are fixed
size, it is much more explicit for a user using Excel, for instance, have
the columns named correctly instead of "col(1), col(2) ...".
May be someone else in this NG, with more experince and expertise in
DataBase design could give another (probably more elegant) solution.

regards,

Paulo Vieira, Emporsoft

"Millenium Business Solutions" <mbs@labyrinth.net.au> wrote in message
news:39F693F4.448E535E@labyrinth.net.au...
> We're redeveloping our systems in Fujitsu Power Cobol and just decided
> to also convert our ISAM files to database at the same time.  One
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Database Field Setup

- **From:** Ed Stevens <nmmc@my-deja.com>
- **Date:** 2000-10-26T12:34:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t98d9$b1l$1@nnrp1.deja.com>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au>`

```
In article <39F693F4.448E535E@labyrinth.net.au>,
  Millenium Business Solutions <mbs@labyrinth.net.au> wrote:
> We're redeveloping our systems in Fujitsu Power Cobol and just decided
> to also convert our ISAM files to database at the same time.  One
> problem we've noticed is that database tables don't seem to be able to
> have 'Occurs X times' on a field.  We have a lot of fields in our ISAM
> files that use this.  Does anyone know how to emulate this in a
database
> table without actually typing one field for each occurs?  We're
> currently using the Access database.
…[6 more quoted lines elided]…
>
The reason you'll not find any equivilent to "occurs depending on" in
your "database" (and I use the term loosley when referring to Access) is
because it is contrary to one of the fundamental principles of
relational database design. Read up on "data normalization", "First
Normal Form", "Second Normal Form" and "Third Normal Form."  Any time
you have repeating data elements, you will need to break those off to a
separate table when converting to a RDBMS.
```

#### ↳ Re: Database Field Setup

- **From:** cbass2112@my-deja.com
- **Date:** 2000-10-26T20:42:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ta4va$404$1@nnrp1.deja.com>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au>`

```
In article <39F693F4.448E535E@labyrinth.net.au>,
  Millenium Business Solutions <mbs@labyrinth.net.au> wrote:

> We're redeveloping our systems in Fujitsu Power Cobol and just decided
> to also convert our ISAM files to database at the same time.  One
…[7 more quoted lines elided]…
> Thanks in advance,

Nope, there is absolutely no way to have multiple occurrences of the
same field in a relational database table, because the whole point of
the relational database concept is to *****ELIMINATE***** such things.

Use a second table for that field, and link it to the main table using
the appropriate key field(s), so that you have a one-to-many link from
the maintable to the child table.  You may have to read up on relational
database concepts, including normalization, in order to get a better
understanding.

If you don't want to break the multiple occurrence field(s) out into a
seperate table, for whatever reason, then do not use a relational
database. Stick with ISAM or VSAM.


Curtis


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Database Field Setup

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-28T01:38:45+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F99375.454BE6E5@zip.com.au>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com>`

```
cbass2112@my-deja.com wrote:

> In article <39F693F4.448E535E@labyrinth.net.au>,
>   Millenium Business Solutions <mbs@labyrinth.net.au> wrote:
…[25 more quoted lines elided]…
>

Curtis,

This comment is a bit black and white for my liking.   Tables are sometimes
denormalised for efficiency purposes, if there are onyl 6 occurrences that
must occur and occur together then include 6 fields in the original
field.   Admittedly this totally stuffs your SQL queries but it would make
row retrieval and locking easier.

Apart from that, I do agree with what you say.  :-}

The only thing I would add is 'get a real database'.  Access is not a
robust system.  Consider dbx  (Dbase III files) for small systems,   some
sort of sql server for larger systems.  One example is mysql which is a
free database.

Ken

Ken
```

###### ↳ ↳ ↳ Re: Database Field Setup

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-27T09:51:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39F9A48E.7E315C20@brazee.net>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com> <39F99375.454BE6E5@zip.com.au>`

```
Ken Foskey wrote:

> > If you don't want to break the multiple occurrence field(s) out into a
> > seperate table, for whatever reason, then do not use a relational
…[11 more quoted lines elided]…
> Apart from that, I do agree with what you say.  :-}

I agree.  Most data warehouses are denormalized.  And quite often one will keep
7 day-of-the-week buckets on a database record instead of 7 linked records.
Sure, it makes it harder to look at all Fridays, but the savings in I/O for
standard processing is tremendous.
```

###### ↳ ↳ ↳ Re: Database Field Setup

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-10-28T06:53:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FA77D5.A07DD441@home.com>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com> <39F99375.454BE6E5@zip.com.au>`

```


Ken Foskey wrote:
> 
> cbass2112@my-deja.com wrote:
…[44 more quoted lines elided]…
> 

OK Ken. I've seen posted here on previous occasions all the 'pros' for
using DBs - now the other side raises its ugly head. So I have got to
re-think, redesign and drop the following EXTREMELY useful feature of
COBOL before I can bugger around with the following in a DB :-

01 READINGS-record.
   05 READINGS-PrimeKey			pic 9(06).
   05  occurs 10.			*> columns
       10 occurs 24.			*> lines
	  15 READINGS-value		pic 9(03)v9(02) comp-3.

I can read the above as ONE complete table - and I don't give a hoot
about doing an enquiry on one individual field - each field is
inter-related both column (Dates) and by Line (Position of object being
inspected). Using a Dialog I can both display and enter into the COBOL
table by line and column.

Small wonder the BIG oil companies are having problems with their DBs if 
they are 'manipulating' this type of data to 'fit' a DB. In one extreme
case, (and I'm referring to a B-I-G US Oil company), one of my 'cells'
which might contain a decimal inch value of 1.234 - finishes up looking
like this :-

	Key			value
	123456789012345678	01.234

Gawd help us ! And then there's the small matter of increased file size.

Jimmy
```

###### ↳ ↳ ↳ Re: Database Field Setup

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-28T14:32:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39fae234.178509182@207.126.101.100>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com> <39F99375.454BE6E5@zip.com.au> <39FA77D5.A07DD441@home.com>`

```
The whole thing requires "rethinking".  The decimal misplacment was
because someone didn't know what they were doing, not because of any
deficiency in the RDB.   You can't think of an RDB as having
"records".  It has columns and rows.  Hmmm... sounds familiar,
considering your example!  Each COLUMN in your example is an entry in
the RDB - each ROW is an entry under this column.  That's not clear, I
know.  

It's funny to me that the RDB has things called "Tables, Columns and
rows" and we are having trouble putting a table of columns and rows
into an RDB!  

Instead of making ONE record, you would use multiple tables - which is
really what you have.  There's a one to one correspondence, it's
simply defined with different syntax.


On Sat, 28 Oct 2000 06:53:02 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[77 more quoted lines elided]…
>Jimmy

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Database Field Setup

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-10-29T14:38:02+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FB9B9A.7FB8BA6F@zip.com.au>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com> <39F99375.454BE6E5@zip.com.au> <39FA77D5.A07DD441@home.com>`

```
"James J. Gavan" wrote:

>
> OK Ken. I've seen posted here on previous occasions all the 'pros' for
…[27 more quoted lines elided]…
> Jimmy

Struth mate,  this is not quite the case!

Relational database works on (surprise) relationships.   This means that there
are times where you actually create two tables for one VSAM file like this.
This is ONLY because you really want to treat them as entities anyway.

To use Howard's idea of 7 days:

If all I want to do is present 7 sequential days on a screen then it is seven
columns on one row.   If I want to find the day which exceeded $20,000 in sales
then I need a single column to query or I write a horrible query for each of the
seven days.    It depends upon how often I want to do the second query as to
whether I denormalise or not, a slow ugly query once every 6 months for
performance and DASD on a daily basis.

I agree that there is increase file size to do this, however the efficiencies of
locating a relationships between data pays this back.   A simple port to a DBMS
will cost, say, 10% more in run time.  A good port will actually save time.

Things I have learned:

Oracle directly supports arrays or tables.  You can read you data into the
tables directly.

I have used occurs in Cobol with a denormalised table,  I simply coded a lot
more detail in the SQL query.

With a DBMS I have tools for my users that do not require programming time.
They are more functional without a lot of effort on my part.

Ken
```

###### ↳ ↳ ↳ Re: Database Field Setup

- **From:** cbass2112@my-deja.com
- **Date:** 2000-11-03T02:05:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tt6h3$8vd$1@nnrp1.deja.com>`
- **References:** `<39F693F4.448E535E@labyrinth.net.au> <8ta4va$404$1@nnrp1.deja.com> <39F99375.454BE6E5@zip.com.au>`

```
In article <39F99375.454BE6E5@zip.com.au>,
  waratah@spamcop.net wrote:
> cbass2112@my-deja.com wrote:
>
…[18 more quoted lines elided]…
> > things.

-- snip --

> > If you don't want to break the multiple occurrence field(s) out
> > into a seperate table, for whatever reason, then do not use a
…[9 more quoted lines elided]…
> queries but it would make row retrieval and locking easier.

These are valid observations, to be sure. My position is simply this:
Don't Use A Different Technology For The Sake Of Using A Different
Technology.

MBS is redeveloping their systems onto a different compiler/platform,
which is enough of job as it is. There is no good reason to further
complicate things by also changing the underlying data storage
mechanism, especially when the new mechanism (RDBMS) doesn't directly
support the same things that the old one (VSAM/ISAM) supported.

Take things one step at a time.  Think about ramifications, pros, cons,
etc.  Think about the advantages offered by a RDBMS, and whether it's
more feasible to exploit them, or leave well enough alone.

Why use a RDBMS if it doesn't offer any real advantage?

I am just trying to discourage biting off more than one can chew, and
taking the big bite for the wrong reasons. There are few things I find
more discouraging than trying to hammer a technology into an
application for which it is ill-suited.

Curtis


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
