[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Extract COBOL records in C

_25 messages · 14 participants · 2001-05_

---

### Extract COBOL records in C

- **From:** "Jeff D. Hamann" <hamannj@ucs.orst.edu>
- **Date:** 2001-05-02T12:25:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cpmus$1oa$1@news.orst.edu>`

```
Hi all, I'm new to the group so be gentle with the flaming, please.

I have a collection of COBOL files (I'm not sure if that's the correct term
as I'm a C programmer) I would like to be able to "export" or translate into
a standard database package and would like to know if there are packages out
there that will help "reverse engineer" COBOL files. I can get the file
formats like


01 NEW-TEMP-1-RECORD.
    05 NT-SUB-KEY-1                    PIC X(10).
    05 NT-SUB-KEY-2                    PIC X(10).
    05 NT-SUB-KEY-3                    PIC X(10).
    05 NT-ALP-SPECIES               PIC X(3).
    05 NT-TOT-LENGHT                PIC -9(9).
     blah, blah, blah....


I just want to open the file, import the records (some file I do have the
file format for and some I don't) and close the file. Are there tools out
therre for doing that?

Thanks,
Jeff.




----------------------------------
Jeff D. Hamann
280 Peavy Hall
Department of Forest Resources
Oregon State University
Corvallis, Oregon 97331-8566 USA
541-740-5988
541-737-2375
hamannj@ucs.orst.edu
http://ucs.orst.edu/~hamannj
http://stimpy.cof.orst.edu

This is the song that never ends
It goes on and on my friends
Somebody started singing it
Not knowing what it was
Now everybody's singing it
And it goes on and on because
This is the song that never ends...
```

#### ↳ Re: Extract COBOL records in C

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-05-02T14:27:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF06DA9.3D349F56@brazee.net>`
- **References:** `<9cpmus$1oa$1@news.orst.edu>`

```


"Jeff D. Hamann" wrote:

> Hi all, I'm new to the group so be gentle with the flaming, please.
>
> I have a collection of COBOL files (I'm not sure if that's the correct term
> as I'm a C programmer)

Pretty much - we call them "files", leaving out the COBOL part.   We can't tell
them apart from programs written by other languages such as EasyTrieve.  Newer
database based languages have meta data to help them out.


> I would like to be able to "export" or translate into
> a standard database package and would like to know if there are packages out
…[13 more quoted lines elided]…
> therre for doing that?

There are - when we get this question, others tell about their favorite products
or the products they produce.

When you have the file file format, it isn't too difficult to convert that file
format into something C can use, or you can write another CoBOL program to
export it in whatever format you like.   If you don't have the file format, you
need to do some work to infer from the way the data look to get a file format.

Another thing you need to know is the computer which created the data.
Different computers handle signs differently.

As long as you don't have packed or binary fields, this should be enough
information.   Otherwise, your work will be tougher.   Do you have a hex editor
to look at your data?    Tell us the computer source, and post some data showing
the hex values.
```

#### ↳ Re: Extract COBOL records in C

- **From:** "Apollo" <swartenbroekxro@wanadoo.be>
- **Date:** 2001-05-02T22:29:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cpqnn$26ui$1@scavenger.euro.net>`
- **References:** `<9cpmus$1oa$1@news.orst.edu>`

```
If you are able to find out how your c compiler reads the file, it maybe
possible. I know the opposite is possible (read c-files with COBOL)



Jeff D. Hamann <hamannj@ucs.orst.edu> schreef in berichtnieuws
9cpmus$1oa$1@news.orst.edu...
> Hi all, I'm new to the group so be gentle with the flaming, please.
>
> I have a collection of COBOL files (I'm not sure if that's the correct
term
> as I'm a C programmer) I would like to be able to "export" or translate
into
> a standard database package and would like to know if there are packages
out
> there that will help "reverse engineer" COBOL files. I can get the file
> formats like
…[39 more quoted lines elided]…
> This is the song that never ends...
```

##### ↳ ↳ Re: Extract COBOL records in C

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-05-02T23:20:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010502192005.10134.00002210@ng-ci1.aol.com>`
- **References:** `<9cpqnn$26ui$1@scavenger.euro.net>`

```
Why do people talk about COBOL records and C records? Data is data. There are
records in a file and you can read just about any data in just about any file
from programs written in just about any language.

Maybe it's a PC thing. On the mainframe, you create a file, using a utility,
basic data entry, or a program written in any language.

The file doesn't give any indication how it was created. The data can be read
by programs in any other language.

You don't need to associate a language with a file.

Regards,

Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-05-02T22:29:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Km3I6.7868$R2.5848796@newsrump.sjc.telocity.net>`
- **References:** `<9cpqnn$26ui$1@scavenger.euro.net> <20010502192005.10134.00002210@ng-ci1.aol.com>`

```
That would be because on 'PC's, most data is stored in a 'Database' (I'm
including spreadsheets here loosely) which contains data that DESCRIBES
the Data that follows.

That's how Version X of Excel / Quattro knows which version you
are trying to read in.  Most 'C' programmers nowadays learned on
PCs and I'd bet a lot of them  only know 'C' and their native language.


S Comstock <scomstock@aol.com> wrote in message
news:20010502192005.10134.00002210@ng-ci1.aol.com...
> Why do people talk about COBOL records and C records? Data is data. There
are
> records in a file and you can read just about any data in just about any
file
> from programs written in just about any language.
>
> Maybe it's a PC thing. On the mainframe, you create a file, using a
utility,
> basic data entry, or a program written in any language.
>
> The file doesn't give any indication how it was created. The data can be
read
> by programs in any other language.
>
…[10 more quoted lines elided]…
> USA
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-02T22:01:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net>`
- **References:** `<9cpqnn$26ui$1@scavenger.euro.net> <20010502192005.10134.00002210@ng-ci1.aol.com>`

```
Steve,
  This is a MAJOR difference between (IBM) mainframe environments and
"workstations" (both WinTel *and* UNIX).

On the IBM Mainframe, "file structures" (corresponding to COBOL sequential,
indexed and relative) are a part of the operating system software
(DFS-whatever).  All the 2nd, 3rd, 4th generation programming languages use
the SAME OS-provided file systems (and "access methods).

On Workstations, there are *usually*
   "line sequential" (carriage-return/line-feed termination for each record)
files

and that is *all* that the operating system REALLY knows about - and that is
all that is portable across "programming languages" (except "ANSI Standard
COBOL that does NOT know about this format).

Each COBOL vendor is *required* to come up with their own way to handle
"record sequential" files (probably easy and relatively portable) and
indexed and relative files (TOTALLY unportable across COBOL
implementations - and even - in some cases - across OS's for the same
compiler vendor).

There are a "couple" of vendors of specific file systems (usually indexed).
I can think of BTRIEVE and C-ISAM - and there may be a few others.  Many of
the workstation COBOL products have OPTIONS to use these systems, but not
all COBOLs support them, and they aren't NEARLY as wide-spread as the
WinTel/Unix systems are.

   ***

Clearly when you get to databases (relational, hierarchical, whatever) these
may or may not be "sold" by the same vendor that sells the compiler or the
operating system or something else.

   ***

Does this help explain the "different world views"?
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-05-03T04:00:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010503000031.02866.00000543@nso-fm.aol.com>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net>`

```
In article <9cqhlt$bcq$1@slb0.atl.mindspring.net>, "William M. Klein"
<wmklein@nospam.ix.netcom.com> writes:

>  This is a MAJOR difference between (IBM) mainframe environments and
>"workstations" (both WinTel *and* UNIX).
…[13 more quoted lines elided]…
>

I am going to have to argue a point here , Bill.
I operate in both the PC and Mainframe world, and have had a brief
exposure to the IBM mainframe world as well.
When dealing with FLAT files, a file is a file is a file.
Granted that most COBOL record/file definitions are Record Sequential
versus the PC-ish default of Line Sequential.  I am certain that it is possible
to read/process record sequential files in any of the current languages.
It is just a matter of understanding how to define the 'structure' in the 
language dujior(?).
Yes Indexed, Relative, and DMS structures are very likely to be implementor
defined, but FLAT files are readable across platforms and languages
if you have an understanding of the record structure and field types.
My experience has been in converting data from multiple vendors on multiple
platforms.  All of which are/were able to produce a flatfile extract readable
either by PC based products written in C, Delphi, or COBOL and mainframe
based products written in C, PL/1, ALGOL, COBOL, RPG.
Even the odd Variable Length Record format file is able to be dealt with.
The biggest area of concern has to do with the hex representation of numeric
data and the BIG vs LITTLE Endian handling of such fields.

Even in the PC environment, you cannot send a dBase file to someone 
and expect them to be able to process the file without some knowledge
of its record composition or an application capable of understanding the
file structure provided in the file header.  dBase may be a poor choice
of an example, but the basic concept is there.  Even from dBase, you normally
would export to a CSV or other text based interchange format.
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 5)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-05-02T21:36:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF0E069.1C3@paralynx.com>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net> <20010503000031.02866.00000543@nso-fm.aol.com>`

```
Sff5ky wrote:
> The biggest area of concern has to do with the hex representation of numeric
> data and the BIG vs LITTLE Endian handling of such fields.

Even that isn't difficult, provided you know what you've got.   Even if you don't, a 
little experimentation soon tells you.

> Even in the PC environment, you cannot send a dBase file to someone
> and expect them to be able to process the file without some knowledge
…[3 more quoted lines elided]…
> would export to a CSV or other text based interchange format.

dBase contains all of the structure information you need in its header record, the 
format of which is widely known and easy to interpret. It identifies field sizes and 
types (including date unambiguous date fields). It's become almost as much of a standard 
as CSV for file exchange because of that. It's main drawback compared with CSV is file 
size, because it uses fixed length records.

You don't have to use any huge DLLs or add-in libraries to read and write it - I wrote 
my own dBase I/O routines for ParseRat (http://www.guysoftware.com/parserat.htm) fairly 
quickly in C++.
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-03T05:42:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9crcmv$4g2$1@slb2.atl.mindspring.net>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net> <20010503000031.02866.00000543@nso-fm.aol.com>`

```
However the USUAL (not only - but "usual") flat file on PC's and Unix is
"line sequential" (with carriage control and/or line feed at the end of each
record).  There are a VARIETY of reasons that this does *not* work correctly
with the ANSI/ISO COBOL "definition" of sequential.  Therefore, you must use
"record sequential" file processing in "Standard" COBOL - which leaves you
with files that canNOT be handled by other PC/Unix software.

Also, as you say, "variable length" flat (sequential files) are often NOT
supported in the OS (although there are SOME ways in which "line sequential"
files work like variable length files and some in which they work like fixed
length).

Bottom-Line:
  (as I originally stated) on Mainframes (at least IBM - and I think others)
the "file system" belongs to the operating system and has everything you
need for all types of "Standard" COBOL files - on PCs and Unix this is NOT
true.
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-05-03T16:58:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF18E7C.30223006@home.com>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net> <20010503000031.02866.00000543@nso-fm.aol.com>`

```


Sff5ky wrote:

> Even in the PC environment, you cannot send a dBase file to someone
> and expect them to be able to process the file without some knowledge
…[3 more quoted lines elided]…
> would export to a CSV or other text based interchange format.

I'm told that DB files are 'portable' - so please tell me more. Can you illustrate
with a (1) A COBOL record format (2) the DB2 structure and (3) MS Access structure
?

Further, can the problem be 'resolved' by holding numerics (e.g. 999.99) as text
fields within the DB records and treating same as 999v99 in the business logic
handling the data ? (I'm assuming here that any 'numeric' handling is done in
'Business' and not DB or SQL computations).

As background I'm currently reading up on SQL and see that DB2 allows for 'decimal'
fields, whereas Access has 'numeric' fields. Currently to overcome latter, I have
specified :-

    Data Type            = Currency
    Format                 = General Number
    Decimals Places    = 1 ( or 2, 3, ......)

the above of course gives me decimal points when I view the Access tables.

Jimmy
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-09T17:16:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3af8d6a2_4@Usenet.com>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net> <20010503000031.02866.00000543@nso-fm.aol.com>`

```
Sff5ky wrote in message <20010503000031.02866.00000543@nso-fm.aol.com>...
>
>Even in the PC environment, you cannot send a dBase file to someone
…[3 more quoted lines elided]…
>of an example, but the basic concept is there.  Even from dBase, you
normally
>would export to a CSV or other text based interchange format.
>
The point that's being missed is that Database "files" contain information
about their own "structure". And that includes DBase. You COULD send a DBase
file to someone else and they WOULD be able to "process it" even WITHOUT any
knowledge of its physical structure, provided they had an ODBC driver for
it. (To be fair, James qualified his statement saying: "or an application
capable of understanding the file structure provided in the file header." It
is important to realise that this is the LOGICAL structure, NOT the
PHYSICAL.

It is quite "wrong" to visualise Databases the same way you would visualise
a "file". The physical structure of the database is irrelevant (except to
DBAs who may want to do some optimizing...I'll qualify my statement:
"...irrelevant to the person or application wanting to use the data.")

Although you CAN use "import/export" to a CSV file, you certainly don't HAVE
to. I have written programs which read  2 ACCESS databases on a PC,  a DB2
database on a mainframe, and wrote records derived from joins of both these
systems to yet a third system on an ORACLE server. (No import/export
involved...direct creation of a new database on the ORACLE server using SQL
CREATE.)  (All systems on the same LAN, of course...<G>)
This can be done in PC COBOL and is no big deal...that's what ODBC is for.

The secret is to use ONLY COBOL and ODBC. DON'T use the binding tools
provided for database illiterate programmers...Data bound grids, ACCESS
BASIC, ORACLE Procedures, etc...in fact, don't use ANYTHING that is platform
specific! Just SQL and COBOL, and connection through an ODBC driver for the
required Database.

I don't want to be too hard on some of the tools (I have used Data bound
grids with Fujitsu PowerCOBOL for GUI DB applications just as an experiment,
and it worked very well), but everything you want to do can be done if you
keep to the simple, basic concept that the database is a repository for data
and you manipulate it with COBOL.

Coming back to the example of DBase, like most RDBs, if you point Crystal
Reports at it, it will immediately analyse the logical structure of the
database and return the tables and fields. It does the same with MSACCESS
and ORACLE and probably anything for which it has an ODBC driver. (I haven't
tried it with EVERYTHING...<G>).

My own DECLGEN software utilises the  logical structural information about
an MS  ACCESS database, which is stored on the database, to produce COBOL
record layouts  and Host Variable definitions for inclusion in COBOL
programs which want to access the DB. The same software can produce code to
maintain the database, making it, in effect, a self maintaining database
(you never need to write SQL to maintain it, only to access it.). This is
all possible because the RDB contains a full picture of the logical database
structure, including the Tables (Relations),  Columns (Fields), Rows
(Tuples), Indexes, Keys, and Relationships (one-to-many;many-to-one, and,
where available, many-to-many).

The important thing to remember is that the LOGICAL structure of a database
is all that matters to the user, and it could be far removed from the
PHYSICAL structure, which, unlike a Flat File, is irrelevant.

A modern Relational Database is as far removed from a Flat File as an F16 is
from a Sopwith Camel. They share common ancestry, are both useful and fun,
but when it comes to capability...don't mess with the F16.

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-09T11:37:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RZ9K6.203$gM.25429@paloalto-snr1.gtei.net>`
- **References:** `<9cqhlt$bcq$1@slb0.atl.mindspring.net> <20010503000031.02866.00000543@nso-fm.aol.com> <3af8d6a2_4@Usenet.com>`

```
Peter E. C. Dashwood <dashwood@free.net.nz> wrote in message
news:3af8d6a2_4@Usenet.com...
> A modern Relational Database is as far removed from a Flat File as an F16
is
> from a Sopwith Camel. They share common ancestry, are both useful and fun,
> but when it comes to capability...don't mess with the F16.


Maybe, but I just could not enjoy Snoopy in the cockpit of an F-16.

(Nice post by the way).

MCM
```

###### ↳ ↳ ↳ Try using ParseRat to extract data

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-05-02T21:26:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF0DE10.5AF5@paralynx.com>`
- **References:** `<9cpqnn$26ui$1@scavenger.euro.net> <20010502192005.10134.00002210@ng-ci1.aol.com>`

```
S Comstock wrote:
> 
> Why do people talk about COBOL records and C records? Data is data. There are
> records in a file and you can read just about any data in just about any file
> from programs written in just about any language.

Very true.  Our ParseRat program (http://www.guysoftware.com/parserat.htm) can extract 
and export data from pretty much anything provided there is SOME structure to the file.

It happens to have been written in C++, but it could have been written in something 
else. I wouldn't really have WANTED to write it in COBOL, though - I can remember 
writing parsing routines in COBOL in the late 60's and it wasn't fun - but it WAS 
better than FORTRAN for text processing.
```

###### ↳ ↳ ↳ Re: Try using ParseRat to extract data

_(reply depth: 4)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-05-16T00:08:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010515200840.23557.00003673@ng-xc1.aol.com>`
- **References:** `<3AF0DE10.5AF5@paralynx.com>`

```
>From: Ed Guy ed_guy@paralynx.com 
>Date: 2001-05-03 00:26 Eastern Daylight Time

>S Comstock wrote:
>> 
…[9 more quoted lines elided]…
>the file.

Well, I don't know anything about C.  But I do know that if you
are converting mainframe data to a SQL format, and if you have
hired some consultants at a zillion dollars per hour to load your 
data into the new format, and if the consultants have written
a program that generates SQL INSERT statements, and if
the consultants decide to forego a full-scale run-through until
the weekend before Go-Live date because everything went so
smoothly in test, and it is Sunday morning before it is realized
that the data has many records which contain a Single Quote
as part of the description field, then you are going to have a 
Monday morning session which is not much like a meeting
but very much like a shouting match. 


Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: Try using ParseRat to extract data

_(reply depth: 5)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-05-15T18:54:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B01DDE4.4E07@paralynx.com>`
- **References:** `<3AF0DE10.5AF5@paralynx.com> <20010515200840.23557.00003673@ng-xc1.aol.com>`

```
Ross Klatte wrote:
> 
> >From: Ed Guy ed_guy@paralynx.com
…[26 more quoted lines elided]…
> but very much like a shouting match.

And if you didn't plan your OWN tests well in advance. Been there, done that, rejected 
the system and postponed the implementation for three months while THEY fixed it, on 
their own nickel.  Also anybody who doesn't allow for names like O'Reilly really hasn't 
grasped the concept.  Or did you mean a single instance of a double quote " like that?
Lots of things break on that. ParseRat isn't bothered by it in CSV input unless it's 
immediately adjacent to a comma - then of course there could be a true ambiguity - is 
it a mistake or not?.
```

###### ↳ ↳ ↳ Re: Try using ParseRat to extract data

_(reply depth: 6)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-05-16T10:18:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010516061836.25461.00000004@ng-ca1.aol.com>`
- **References:** `<3B01DDE4.4E07@paralynx.com>`

```
>From: Ed Guy ed_guy@paralynx.com 
>Date: 2001-05-15 21:54 Eastern Daylight Time

>And if you didn't plan your OWN tests well in advance. Been there, done that,
>rejected 
…[10 more quoted lines elided]…
>it a mistake or not?.

Well, under the American System of Management all blame is
affixed to the lowest ranking person who had any detectible
involvement.  
The story has a happy ending though--both companies have
now gone out of business.  

A similar case of "COBOL data" versus "Visual Basic data"
occurred at the DMV.  Fortunately, it was picked up much
earlier.  
The COBOL side had multiple layouts for different record types.
The VB guys quite rightly asked that each type be dumped
in a separate file.  The COBOL guys said
    IF RECORD-TYPE = NN
        MOVE INPUT-RECORD   TO OUTPUT-RECORD-TYPE-NN
        WRITE OUTPUT-RECORD
So then the VB guys got a brief lesson in the concept of FILLER.
The second time around it was learned that just because a
field *says* PIC 9999 does not mean that *is* PIC 9999.  If
the field was defined back at the design time, but then in fact
never used (or originally used, and then later not used, and
thenceforth ignored), it could be anything.  
I don't think this situation can arise in PC-oriented languages,
can it? 


Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: Try using ParseRat to extract data

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-16T13:52:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICvM6.175$AB1.99598@paloalto-snr1.gtei.net>`
- **References:** `<3B01DDE4.4E07@paralynx.com> <20010516061836.25461.00000004@ng-ca1.aol.com>`

```
Ross Klatte <klatteross@aol.commmm> wrote in message
news:20010516061836.25461.00000004@ng-ca1.aol.com...
> A similar case of "COBOL data" versus "Visual Basic data"
> occurred at the DMV.  Fortunately, it was picked up much
…[9 more quoted lines elided]…
>

Not only "CAN" happen, but "DOES" happen.

Look at the most PC-oriented language possible: Windows itself.

There are numerous Win32-API calls where the size and record definition of
one parameter is contingent on the value of another parameter. There are
also many defined structures (i.e., "01 level records") where a structure
"size in bytes"  is included in the record so you can tell which version of
the structure is in use.
```

#### ↳ Re: Extract COBOL records in C

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-05-02T20:37:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ve_H6.354$X65.153375@dfiatx1-snr1.gtei.net>`
- **References:** `<9cpmus$1oa$1@news.orst.edu>`

```
Read this first:

http://www.flexus.com/ebd2asc.html

As far as tools, I have a Windows/32 DLL to convert from COBOL datatypes to
IEEE datatypes, yours more or less free (you have to answer some questions,
then swear a blood oath to let me know how it works out for you).
(No cash fees are involved).

After reading the article, you should know exactly what to do next.
```

#### ↳ Re: Extract COBOL records in C

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-05-10T01:51:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF9F461.3C4C4E3@siber.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu>`

```
You can do one of two things:

- Get DataAccess library from us and use it
It does just what you want -- it presents Cobol data files in a way
that can be read into a C++ prpgram. OK, C++ is not the sam eas C.
But it is close enough, you (or we) can write a translation layer
that would accomodate C++ to C.

- Convert your Cobol data files to CSV or DBF or other modern format.
You can do it using our tools Data2Flat, Data2Dbf.
Then you can read the converted files into the C program.

More details on both options at http://www.siber.com/sct/datafile/

Some background: Cobol files are hard to read if you are not in Cobol,
very hard.
If you are to do it yourself, it will take like a year and you still may
fail.
Cobol data files are often compressed and are otherwise made hard to
read
by vendors. 

Regards,
Vadim Maslov
Siber Systems


Jeff D. Hamann wrote:
> 
> Hi all, I'm new to the group so be gentle with the flaming, please.
…[40 more quoted lines elided]…
> This is the song that never ends...
```

##### ↳ ↳ Re: Extract COBOL records in C

- **From:** "Charles" <charles@godwin.ca>
- **Date:** 2001-05-10T23:23:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JpFK6.60845$_f3.1153146@news20.bellglobal.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com>`

```
CA-Realia COBOL publishes the format of most of it's file types and provides
a documented C callable FileSystem API for reading, writing and creating
these files. CA-We also publish the internal format of COBOL type numeric
fields. We even provide as freeware a file copy utility to convert files
from one format to another. CA is NOT a company that makes COBOL data hard
to read.

Charles Godwin
Development Masager - Realia
Computer Associates International, Inc.

"Vadim Maslov" <vadik-nws@siber.com> wrote in message
news:3AF9F461.3C4C4E3@siber.com...
> You can do one of two things:
>
…[29 more quoted lines elided]…
> > I have a collection of COBOL files (I'm not sure if that's the correct
term
> > as I'm a C programmer) I would like to be able to "export" or translate
into
> > a standard database package and would like to know if there are packages
out
> > there that will help "reverse engineer" COBOL files. I can get the file
> > formats like
…[9 more quoted lines elided]…
> > I just want to open the file, import the records (some file I do have
the
> > file format for and some I don't) and close the file. Are there tools
out
> > therre for doing that?
> >
…[21 more quoted lines elided]…
> > This is the song that never ends...
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-11T13:25:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3afb4266_6@Usenet.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com> <JpFK6.60845$_f3.1153146@news20.bellglobal.com>`

```
Sorry Charles,

I didn't see this response until AFTER I had responded to Vadim. You endorse
what I said... it is a succinct and fair statement.

Pete.


Charles wrote in message ...
>CA-Realia COBOL publishes the format of most of it's file types and
provides
>a documented C callable FileSystem API for reading, writing and creating
>these files. CA-We also publish the internal format of COBOL type numeric
…[45 more quoted lines elided]…
>> > a standard database package and would like to know if there are
packages
>out
>> > there that will help "reverse engineer" COBOL files. I can get the file
…[39 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Extract COBOL records in C

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-11T13:22:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3afb4260_6@Usenet.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com>`

```
Vadim,

This is a public forum and it is irritating to see advertising unless it is
really pertinent and describes a genuine solution to a problem.

Personally, I have no problem with people "plugging" a product as long as it
is pertinent. (Others here may have much less tolerance...)

So, describe what your product does and leave it at that.

Especially, don't pad the message with vacuous drivel... The people in this
forum for the most part are professional technicians and get enough
Marketing bullshit at their workplaces without having it here.

Comments below.


Vadim Maslov wrote in message <3AF9F461.3C4C4E3@siber.com>...
>You can do one of two things:

[translation - one of these two options will suit US very nicely...]
>
>- Get DataAccess library from us and use it
…[8 more quoted lines elided]…
>
Or you could use a competitor's products, or talk to your own vendor (CA I
think it was..) about what software they offer to do it, or any other option
limited only by your own imagination and diligence.


>More details on both options at http://www.siber.com/sct/datafile/
>

[totally unecessary "Bullshit Section"]


>Some background: Cobol files are hard to read if you are not in Cobol,
>very hard.
COBOL vendors provide utilities to read their file systems and MOST publish
the data formats so they can be read by byte stream IO. The formats are
usually a matter of record.

>If you are to do it yourself, it will take like a year and you still may
>fail.
Well, I don't know about you, but it has never taken me a year to read a
"foreign" COBOL file, even when I HAVEN'T had the vendor's format
description (particularly if I know what data is on the file). As for
failure, there is always a risk of that...even using either of the options
you offered.

>Cobol data files are often compressed and are otherwise made hard to
>read
>by vendors.
Yes, it is common practice to compress ISAM files. This is not to make them
hard to read, it is to save space and it is an OPTION. Given that you take
this option, you will need a decompression function from the vendor. Are you
saying that the software you are recommending is aware of EVERY
decompression provided by EVERY vendor? (If so, that is a valid point which
should have been made outside the "Bullshit Section" of this message.)

[End Bullshit Section]

I don't doubt that the software from Siber Systems is very good. (people
don't stay in business very long if their product ISN'T any good).

My issue is not with the product, it is with the way it has been presented
here.

Pete.

>
>Regards,
…[8 more quoted lines elided]…
>> I have a collection of COBOL files (I'm not sure if that's the correct
term
>> as I'm a C programmer) I would like to be able to "export" or translate
into
>> a standard database package and would like to know if there are packages
out
>> there that will help "reverse engineer" COBOL files. I can get the file
>> formats like
…[34 more quoted lines elided]…
>> This is the song that never ends...


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-05-12T03:03:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AFCA85D.CD8FE5B@siber.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com> <3afb4260_6@Usenet.com>`

```
What is so irritating? Proposing a solution to a problem and
solution is not free? Yeah, we are nasty little bastards, 
we dare to sell our software for money.

So why don't you propose a free solution to this guy,
to close the matter, so to say?

Or, if we look at it from other prospective, is it true
that this forum's sole purpose is to discusss whether
Cobol is dead or when it will be dead?

Just curious.

Vadim Maslov



Peter E. C. Dashwood wrote:
> 
> Vadim,
…[131 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@free.net.nz>
- **Date:** 2001-05-13T00:39:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3afd2e4d_3@Usenet.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com> <3afb4260_6@Usenet.com> <3AFCA85D.CD8FE5B@siber.com>`

```

Vadim Maslov wrote in message <3AFCA85D.CD8FE5B@siber.com>...
>What is so irritating? Proposing a solution to a problem and
>solution is not free? Yeah, we are nasty little bastards,
>we dare to sell our software for money.

No one, least of all me, is questioning your right to sell software for
money. As for being a nasty little bastard...your words, not mine.

It is a question of presenting the capabiilities of your product fairly,
without Marketing hype or trying to put the "frighteners" on people in an
effort to get them to buy your software.

Say what it does, where it can be obtained, and, ideally, what it costs.

Your suggestion that it would take years to do it without your software, and
that COBOL files are generally difficult, is blatantly untrue. And
unnecessary.

It might work with people coming in to your showroom who don't know any
better, but this is a professional forum with  a fair sprinkling of highly
experienced people whose intelligence you insult with this kind of rubbish.

Many of us have done conversions at some point. It didn't take years and we
used tools which are freely available or wrote them if they weren't.

That is not to say there is no place for the software you are offering.
Offer it fairly and let it stand on its own merit. Or do you have a problem
with that?

>
>So why don't you propose a free solution to this guy,
>to close the matter, so to say?
>
I am happy to point out that the two alternatives you offered are not the
ONLY ones...It would have been much better if YOU had done so. Whether he
finally opts for free software or assistance, or buys software such as your
own is none of my business and I really don't care.

My only issue is with the unethical way in which you presented your case...
(but I thought I said that already...)

>Or, if we look at it from other prospective, is it true
>that this forum's sole purpose is to discusss whether
>Cobol is dead or when it will be dead?
>
>Just curious.

Look at it from any perspective you like, discuss anything you like, but if
you are here to sell product, keep it honest.

Pete.

========================== previous correspondence ===================

>Peter E. C. Dashwood wrote:
>>
>> Vadim,
>>
>> This is a public forum and it is irritating to see advertising unless it
is
>> really pertinent and describes a genuine solution to a problem.
>>
>> Personally, I have no problem with people "plugging" a product as long as
it
>> is pertinent. (Others here may have much less tolerance...)
>>
>> So, describe what your product does and leave it at that.
>>
>> Especially, don't pad the message with vacuous drivel... The people in
this
>> forum for the most part are professional technicians and get enough
>> Marketing bullshit at their workplaces without having it here.
…[18 more quoted lines elided]…
>> Or you could use a competitor's products, or talk to your own vendor (CA
I
>> think it was..) about what software they offer to do it, or any other
option
>> limited only by your own imagination and diligence.
>>
…[7 more quoted lines elided]…
>> COBOL vendors provide utilities to read their file systems and MOST
publish
>> the data formats so they can be read by byte stream IO. The formats are
>> usually a matter of record.
…[6 more quoted lines elided]…
>> failure, there is always a risk of that...even using either of the
options
>> you offered.
>>
…[3 more quoted lines elided]…
>> Yes, it is common practice to compress ISAM files. This is not to make
them
>> hard to read, it is to save space and it is an OPTION. Given that you
take
>> this option, you will need a decompression function from the vendor. Are
you
>> saying that the software you are recommending is aware of EVERY
>> decompression provided by EVERY vendor? (If so, that is a valid point
which
>> should have been made outside the "Bullshit Section" of this message.)
>>
…[5 more quoted lines elided]…
>> My issue is not with the product, it is with the way it has been
presented
>> here.
>>
…[14 more quoted lines elided]…
>> >> as I'm a C programmer) I would like to be able to "export" or
translate
>> into
>> >> a standard database package and would like to know if there are
packages
>> out
>> >> there that will help "reverse engineer" COBOL files. I can get the
file
>> >> formats like
>> >>
…[8 more quoted lines elided]…
>> >> I just want to open the file, import the records (some file I do have
the
>> >> file format for and some I don't) and close the file. Are there tools
out
>> >> therre for doing that?
>> >>
…[27 more quoted lines elided]…
>>                 http://www.usenet.com


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Extract COBOL records in C

_(reply depth: 5)_

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-05-14T05:25:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AFF6CA4.7816FAE7@siber.com>`
- **References:** `<9cpmus$1oa$1@news.orst.edu> <3AF9F461.3C4C4E3@siber.com> <3afb4260_6@Usenet.com> <3AFCA85D.CD8FE5B@siber.com> <3afd2e4d_3@Usenet.com>`

```
Peter E. C. Dashwood wrote:
> 
> Vadim Maslov wrote in message <3AFCA85D.CD8FE5B@siber.com>...
…[8 more quoted lines elided]…
> Say what it does, where it can be obtained, and, ideally, what it costs.

This is all stated in URL that was provided.
Giving the entire price list in a posting is a waste of space.
Explaining why people would use the product is not a waste of space.

> 
> Your suggestion that it would take years to do it without your software, and
> that COBOL files are generally difficult, is blatantly untrue. And
> unnecessary.

My post said "like a year" which means "close to a year".
This is more or less true if you want to read compressed
Cobol data file in which non-display field types are used.
Also consider the fact that Cobol compiler vendors do not release
formats of their data files as a rule (Realia appears to be
an exception, but we do not have a Data Reader for Realia
(maybe for this very reason that they made their format public)).

So speaking about "blatantly untrue", you statement about my
statement is way more "blatantly untrue". My statement had some 
marketing in it, but it is not baseless, because I have seen 
Cobol compilers and Cobol file systems and I know them inside. 
Data Readers took more than a year to develop for us,
we started from the user perspective (no isider knowledge), 
and we "are knowledgeable in the art".


> 
> It might work with people coming in to your showroom who don't know any
…[8 more quoted lines elided]…
> with that?

It does stand on its own merit. 
If you converted 80-byte fixed records with DISPLAY data,
it indeed does not take much, no onversion is needed at all. 
But if you had to extract data from a compressed PC Cobol data file 
without having a copybook for it and without knowing what Cobol
compiler produced it, it might take a long time, 
to the point of not being economically feasible for a user.
We make it economically feasible.


> 
> >
…[6 more quoted lines elided]…
> own is none of my business and I really don't care.

Well, did I say that my solution is the only one? No.
And if you indeed cared about "fairness" and what not, 
you would have descirbed competing solutions and 
you would have explained why they are better and cheaper than ours.


Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
