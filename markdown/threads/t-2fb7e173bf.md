[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What exactly is DMSII and LINC?

_6 messages · 5 participants · 2001-06_

---

### What exactly is DMSII and LINC?

- **From:** "COGNICASE - Patrick Saunderson" <patrick.saunderson@cognicase.com>
- **Date:** 2001-06-06T19:45:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ALvT6.2862$jD6.266530@news>`

```
I would apprecaite a detailed answer to both items.

Thanks,
```

#### ↳ Re: What exactly is DMSII and LINC?

- **From:** "Tim Scrivens" <tim.scrivens@nz.eds.com>
- **Date:** 2001-06-07T09:30:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fm7eb$vmq$1@hermes.nz.eds.com>`
- **References:** `<ALvT6.2862$jD6.266530@news>`

```

"COGNICASE - Patrick Saunderson" <patrick.saunderson@cognicase.com> wrote in
message news:ALvT6.2862$jD6.266530@news...
> I would apprecaite a detailed answer to both items.
>
> Thanks,
>
How detailed is detailed?

Data Management System II
DMSII is a mature, proven database management system designed for
enterprise-wide data management. DMSII supports large databases and
high-volume online transaction processing and accommodates installations of
virtually any size.

DMSII offers exceptional flexibility in accommodating a broad variety of
data models. The database can be a hierarchical, network, or flat structure
or can be normalized to a relational model. You define the database using
the DMSII Data and Structure Definition Language (DASDL) or the
menu-assisted interface that is part of the optional Advanced Data
Dictionary System (ADDS). The ADDS interface eliminates the need to define
database characteristics by using a conventional syntactic language.

DMSII supports a variety of information accessing techniques. It
incorporates validation, audit/recovery, and access control capabilities and
supports several optional utilities for database analysis, monitoring,
integrity certification, online reorganization, and online archiving.

DMSII Extended Edition (DMSII XE)
DMSII SE is a mature, proven database management system designed for
enterprise-wide data management. DMSII SE supports large databases and
high-volume online transaction processing, and it accommodates installations
of virtually any size. DMSII SE offers exceptional flexibility in
accommodating a broad variety of data models-hierarchical, network, flat, or
relational. DMSII SE also supports a variety of information accessing
techniques. It incorporates validation, audit/recovery, and access control
capabilities, as well as supporting optional utilities for database
analysis, monitoring, integrity certification, online reorganization, and
online archiving.

In addition to providing all the specialized programs of DMSII SE, DMSII XE
has three goals:

Linear scalability. As each processor is added to a system, it should
ideally yield the same amount of performance increment as the processor that
preceded it.
Multiterabyte capacity. DMSII XE provides multiterabyte data capacity at the
data set level. Each data set can hold more than 12 terabytes of data. DMSII
XE implements structures with large amounts of data rather than relying on
application logic to piece together several structures with less capacity.
Database availability. DMSII XE seeks to reduce the amount of time during
which a database or structure is unavailable because of required maintenance
or recovery tasks. DMSII XE addresses this goal by providing an online
garbage collection facility for disjoint index sequential sets and subsets.

General Features
Features Common to DMSII SE and DMSII XE
DMSII supports a variety of information accessing techniques. You can store
groups of data records (called data sets) several primary ways, including

A "standard" file structure
Records are generally not ordered in this structure type. To provide
efficient keyed access to a particular data record, indexes are often used.
A single standard data set can have multiple indexes, allowing keyed access
for many different selection conditions.

A direct file structure
Records are stored and accessed by a unique user-supplied "record number,"
eliminating the need for a separate index to find a particular data record.
Direct data sets allow other indexes to be specified, which permits
efficient searches by other keys.

A hashed file structure
A designated key of this record type is hashed and the records are stored in
the hashed order. The hashed file structure provides fast access without an
additional index structure. No indexes are allowed on this structure type.
The hashed key can be alphanumeric as well as numeric.

An ordered file structure
A designated key of this record type is used to order the records as they
are stored.

Records in the data sets must be efficiently located when they need to be
accessed. Records in most data sets can be accessed by using several types
of indexes. Most common are the index sequential and index random access
methods. Index sequential access uses binary searches on multiple levels of
index tables to allow flexible, efficient access to data records. Index
random access uses a hashing algorithm on a key to efficiently locate a
particular data set record.

Information relationships can also be established. Link relationships can be
specified between members of data sets on a one-to-one basis. DMSII also
supports chain relationships, which provide a one-to-many type of
relationship. A number of different link types are available, including
unprotected, verified, self-correcting, symbolic, and counted links.
Selection of the proper type is based on trade-offs among integrity
requirements, volatility, and resource consumption.

DMSII incorporates a variety of validation, audit/recovery, and access
control capabilities. Comprehensive audit/recovery facilities provide
restart information for user programs, automatically recover the database
when faults occur, reconstruct portions of the database, and remove aborted
transactions. Full recovery of all completed transactions is available
within DMSII when it enforces independent transactions. You can synchronize
a COMS audit trail with the DMSII audit trail to provide full synchronized
recovery.

Access control is offered through the Master Control Program (MCP). This
interface permits system access only to authorized requestors. In addition,
you can establish access control to identify the databases a requestor may
access, the data sets that requestor may access within a database, the
records the requestor may access within a data set, and the information
items the requestor is permitted to view within a record. Access control
also can limit a requestor to inquiry-only access as well as limit the DMSII
commands that can be used.

Several DMSII utilities are available that support database analysis,
monitoring, integrity certification, online reorganization, and online
archiving. These products enhance the overall usability of DMSII and help
clients approximate a 24-hour online, 7-day-a-week operation. All DMSII
generated messages use the MultiLingual System (MLS), which allows each site
to translate messages into the local language. The released language is
English.

DMSII XE Extensions
Variable Audit Buffers

Varying the number of audit buffers when audit files are sectioned enables
the database to absorb short periods of intense audit activity. The number
of audit buffers automatically changes as the number of audit file sections
increases or decreases, with approximately 10 audit buffers allocated for
each section. Although the system adjusts the number of audit buffers
automatically, you can also manually assign the number.

Sectioned Audit Files

Sectioned audit files involve the use of multiple physical files that
together form a single logical audit file. You can define up to 63
individual audit sections; however, the combination of all the sections make
up the logical audit file. All sections of an audit file must be present for
DMSII XE to recognize that the audit file is present. Some advantages
offered by sectioned audit files are

Improved audit trail throughput
Concurrent multiple audit file I/Os
Increased bandwidth of the audit trail
Sectioned Data Sets

As with sectioned audit files, a sectioned data set is one in which the
logical data set structure is physically composed of multiple physical
files. You can define up to 255 sections for a data set; however, it is the
combination of all the sections that make up the logical data set.

For HMP 4.0, sectioned data sets are provided for disjoint standard data
sets only. Records in the data set are distributed among the sections using
a round-robin algorithm.

Use of sectioned data sets has the following advantages:

Reduction or elimination of throughput restrictions imposed by the
architecture of internal locks within DMSII.
Increased bandwidth of DMSII physical I/O.
Expanded data set capacity-multiple physical files expand the data set
capacity from 48 gigabytes per structure to 48 gigabytes per section. With a
possible 255 sections per data set, each data set has a potential capacity
of 12 terabytes.
Visibility of existing application program logic-logically, sectioned data
sets appear identical to nonsectioned data sets. Consequently, when
migrating to sectioned data sets, no application program changes are
required. With the exception of the possible appearance of an RSN item
(which is visible to the application only if declared in the DASDL),
application programs are unaware that a data set is sectioned.
Sectioned Sets

A sectioned set is one that has been divided, based on criteria specified in
DASDL, into several discrete components that enable access or manipulation
of each section independently of the other sections.

When multiple application programs access a data set by way of a set, some
contention for set resources occurs. As the number of programs rises, so
does the amount of contention. Set sectioning reduces, or in some cases
eliminates, set resource contention.

Sectioning of sets is critical for achieving scalability on

Systems with many processors
Databases with large data sets
For HMP 4.0, sectioned sets are provided for disjoint indexed sequential
sets only.

TranStamp Locking

TranStamp locking is a new type of locking algorithm for data sets that are
defined in DASDL with a special keyword. The new TranStamp locking algorithm
makes the data record an integral part of the locking process. With the aid
of a unique transaction identifier, TranStamp locking provides a substantial
increase in record-lock related performance.

To allow for ease of migration, the use of TranStamp locking is optional for
nonsectioned data sets. However, the full benefit of TranStamp locking is
not realized unless used by all structures in the database.

Some of the advantages offered by TranStamp locking are

The data record is made part of the locking scheme, which eliminates much of
the overhead required to manage internal lock tables.
The size of the lock table is reduced from one entry per locked record to
one entry per transaction.
The limit on the number of records that can be locked by a single program is
eliminated because the lock table requirements for a given program are
fixed.
The overhead associated with END-TRANSACTION operations is reduced because
all records can be freed by invalidating the TranStamp identifier associated
with the lock (as opposed to freeing each locked record).
Record Serial Numbers (RSNs)

An RSN is a unique number assigned to each data set record. An RSN is
guaranteed to be unique within a data set, but not within the database. That
is, once an RSN is used within a data set, that RSN is never used again
within that data set, but it can be used for a record in another data set.

RSNs enable an internal optimization within sets that allow duplicates but
that do not declare DUPLICATES FIRST or DUPLICATES LAST.

Online Set Garbage Collection

Online Set Garbage Collection returns unused structure space to the system
while your database is up and running.

The following are advantages offered by Online Set Garbage Collection:

Consolidates unused space in sets or subsets
Rebalances index structures to optimize access through sets
When you use garbage collection, the database remains online and available,
and any failure of the garbage collection task has no impact on the
database.


All if this DMSII/DASDL stuff was stolen from:
http://ecc400.com/unisysold/clearpath/sw_datamgmt_cl_dmsiixe.htm

My work uses it as the database for a 100+ G mainframe application, with a
transaction load of just over 2 million transactions/day.

LINC is an NZ invented 3.5 GL.  It has been around sufficiently long that we
are now on version 17.  It has advantages of speed of coding, and is usually
used to create an on-line system (with supporting batch).  Easy to use, fast
to code.  When you "compile" LINC, it creates COBOL (VERY ugly COBOL - 80
characters wide, continuation characters used, and full-stops without going
to a new line - just basically a solid 72 characters of code, right down the
page), and then uses that to compile an object version.

Here is a press release from one of the inventors (for what it is worth, he
is touting a new product in it).

http://www.jade.co.nz/news/prcov1999_hero.htm
```

#### ↳ Re: What exactly is DMSII and LINC?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-07T08:48:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1F31D2.E1A19B2D@Azonic.co.nz>`
- **References:** `<ALvT6.2862$jD6.266530@news>`

```
> I would apprecaite a detailed answer to both items.

LINC is/was a 4GL system developed in New Zealand in the 1970s.  It was
purchased by Burroughs which later became part of Unisys.  The 'LINC
Centre' in Christchurch (I think it was) closed down a few years ago so
the product ran for about 20 years.

It was originally supposed to be a system where the users could define
the system in terms they understood in the LINC language and then LINC
would generate all the file definitions and program source in Cobol.  In
fact just like all the other 4GLs.  It seems that it was quite
successful in a number of situations and many of its users swore by it
(or perhaps they said 'at' it  ;-).

Like all 4GLs they failed because users, even very good ones, only know,
or can only express, 60% to 80%, of what the system they use actually
does.  This means that analysts are needed to dig out (or invent) the
rest.  Also 4GLs usually only generate 80% of what the system is needed
to do, so programmers are needed for the rest.

Now in any project 80% of the work takes 80% of the resources, the last
20% of the projects takes the remaining 80% of the time and and
money.     ;-)

The net result is that 4GLs (an LINC) only produced savings where the
problem matched the solution perfectly.
```

##### ↳ ↳ Re: What exactly is DMSII and LINC?

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-06-06T22:11:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010606181111.11294.00003584@ng-mp1.aol.com>`
- **References:** `<3B1F31D2.E1A19B2D@Azonic.co.nz>`

```
>From: Richard Plinston riplin@Azonic.co.nz 
>Date: 2001-06-07 03:48 Eastern Daylight Time

DMSII is the Burroughs/Unisys database.  
It is a proto-relational database.  
All the tables (called "datasets") are usually separate entities
within the database.  Every dataset must have a primary key
and may have alternate keys.  Keys can be constructed from
disparate fields.  Duplicate keys are permissible as primary
keys.  
All "joins" or "foreign keys" have to be written in the program
code.  
DMSII comes with an ad hoc inquiry program.  Simple
inquiries are simple.  Complex inquiries can get pretty 
damn complicated--suitable for use only by programmers.
There are 3rd party tools that can provide ad hoc inquiries, 
including filters and joins, with at least no more difficulty
than SQL.  
For those seeking the thrill of hierarchical structure, you
can use the "embedded dataset."  

Ross
http://www.geocities.com/ross_klatte/
```

##### ↳ ↳ Re: What exactly is DMSII and LINC?

- **From:** Sean Case <gsc@zip.com.au>
- **Date:** 2001-06-07T21:52:08+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsc-05ED53.21520807062001@nostril.pacific.net.au>`
- **References:** `<ALvT6.2862$jD6.266530@news> <3B1F31D2.E1A19B2D@Azonic.co.nz>`

```
In article <3B1F31D2.E1A19B2D@Azonic.co.nz>,
 Richard Plinston <riplin@Azonic.co.nz> wrote:

> LINC is/was a 4GL system developed in New Zealand in the 1970s.  It was
> purchased by Burroughs which later became part of Unisys.  The 'LINC
> Centre' in Christchurch (I think it was) closed down a few years ago so
> the product ran for about 20 years.

The LINC Development Centre closed down, but LINC development continues.
The product is now based in Sydney, at the Australian Centre for Unisys
Software.

It's also now called Unisys e-@ction Enterprise Application Environment,
but that's another story...

Sean Case
```

#### ↳ Re: What exactly is DMSII and LINC?

- **From:** Sean Case <gsc@zip.com.au>
- **Date:** 2001-06-07T21:47:28+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsc-4E0F71.21472807062001@nostril.pacific.net.au>`
- **References:** `<ALvT6.2862$jD6.266530@news>`

```
In article <ALvT6.2862$jD6.266530@news>,
 "COGNICASE - Patrick Saunderson" <patrick.saunderson@cognicase.com> 
 wrote:

> I would apprecaite a detailed answer to both items.

DMSII is the database management system for the Unisys ClearPath NX
series mainframes (the ex-Burroughs ones).

LINC is a 4GL sold by Unisys for various platforms, including both
their mainframe lines (ex-Burroughs and ex-Sperry), several flavours
of Unix, and Windows NT.

If someone has offered you a job working with both of these, then
they are presumably running LINC on an NX machine.

You can probably get much more information on both these products
in comp.sys.unisys.

Sean Case
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
