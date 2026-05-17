[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with acronyms or pointer to FAQ please

_3 messages · 3 participants · 1997-04_

**Topics:** [`Help requests and how-to`](../topics.md#help) · [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Help with acronyms or pointer to FAQ please

- **From:** "p..." <ua-author-24913@usenetarchives.gap>
- **Date:** 1997-04-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5j643l$jvu@kew.globalnet.co.uk>`

```


Hello, I am new here.

I have to attend a meeting next Wednesday 23rd April, where some
COBOL programmers will talk about their work. The pre-meeting
material is full of acronyms I don't understand, and I would really
appreciate some interpretation or a pointer to a FAQ so I will be
able to grasp a bit more of what's going on. I have a little
programming experience in C and Pascal, but have never touched
COBOL.

DB2. Is this the same as dBase2, the database that was published by
Ashton-Tate? SQL I understand, but what does it mean to generate a
SQL definition from a DB2 database? Is this a type conversion, and
how would they do this?

Similarly IMS database segments. What does IMS stand for and how is
a segment defined? Conversion to DBD (? my guess- DataBase
Description ?), can you help me understand this process?

BMS screens?

Job Control Language, typically, what is this used for?

VSAM?

MFS?

CICS?

Also, what is a paragraph in COBOL? Just for the flavour of it, can
you show me, or point me towards a simple 'Hello World' type COBOL
program, I would be very grateful.

Many thanks

P Newman
```

#### ↳ Re: Help with acronyms or pointer to FAQ please

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8dd2fc476-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5j643l$jvu@kew.globalnet.co.uk>`
- **References:** `<5j643l$jvu@kew.globalnet.co.uk>`

```

?

Someone else already gave the meanings of most of your questions. The only
overlooked was CICS: Customer Information Control System.

As for a COBOL 'Hello World' program...

IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.
ENVIRONMENT DIVISION.
DATA DIVISION.
PROCEDURE DIVISION.
MAIN SECTION.
SAY-HELLO.
DISPLAY 'HELLO WORLD'.
STOP RUN.

Nine lines: will work in COBOL/400 and VAX/COBOL. And someone said that COBOL
is verbose????????
```

#### ↳ Re: Help with acronyms or pointer to FAQ please

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8dd2fc476-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5j643l$jvu@kew.globalnet.co.uk>`
- **References:** `<5j643l$jvu@kew.globalnet.co.uk>`

```

sounds like an interview to me...

DB2 is the generic for IBM's relational database system, usually referring
to the MVS version, but also exists on other platforms. This has nothing
to do with the ancient Ashton Tate product line.

SQL - Structured Query Language - an ANSI standardized query language,
primarily for accessing Relational Data Base systems (althogh some
versions / extensions can access other DBMS or flat file constructs).
Generating SQL defintion from a DB2 database is a method of mechanically
building COBOL record defintioins that represent rows in a DB2 relational
table.

IMS Information Management System. An IBM program product that is a
combination of a DataBaseManagementSystem and a Data Communication system.
A segment is a record in this heirachial database system. Defined by
utilities to IMS which handles the databases for applications.

BMS screens. Basic Mapping Services - a way to define the data stream
necessary to display images on a 3270 type terminal from IBM's CICS
system.

Job Control Language is used to control the execution of batch jobs on IBM
MVS systems.

VSAM - Virtual Storage Access Method. A file access method on IBM's MVS,
VM and VSE systems.

MFS - Message formatiing services - BMS type functions for IMS.

CICS - A single region teleprocessing monitor for IBM mainframes (with
clones on PC's).

Paragraph in COBOL - a chuch of code, with a label at the start.

Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
