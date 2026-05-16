[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# converting from cobol to other obdc database

_5 messages · 5 participants · 2004-02_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Databases and SQL`](../topics.md#databases)

---

### converting from cobol to other obdc database

- **From:** "Sam" <vermello@terra.es>
- **Date:** 2004-02-24T03:53:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IUz_b.3586832$uj6.10411952@telenews.teleline.es>`

```
I have a very old database in Cobol and now I need to convert to Obdc
database format. I have no idea about Cobol, is there any program to do it?
Can I use other way to do it? Thanks.
```

#### ↳ Re: converting from cobol to other obdc database

- **From:** "Daniel L. Belton" <spam@abuse.gov>
- **Date:** 2004-02-24T13:10:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I2I_b.807$Er4.322@fe2.columbus.rr.com>`
- **References:** `<IUz_b.3586832$uj6.10411952@telenews.teleline.es>`

```

"Sam" <vermello@terra.es> wrote in message
news:IUz_b.3586832$uj6.10411952@telenews.teleline.es...
> I have a very old database in Cobol and now I need to convert to Obdc
> database format. I have no idea about Cobol, is there any program to do
it?
> Can I use other way to do it? Thanks.
>

How you would do this depends on how the actual database is setup.  Cobol
itself isn't a database format, it was just used to access the database.

Do you have any idea what was used to setup the database?  DL/I?  DB/2?
DataComm?
```

#### ↳ Re: converting from cobol to other obdc database

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-02-24T07:28:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0402240728.6c0bc7bb@posting.google.com>`
- **References:** `<IUz_b.3586832$uj6.10411952@telenews.teleline.es>`

```
"Sam" <vermello@terra.es> wrote in message news:<IUz_b.3586832$uj6.10411952@telenews.teleline.es>...
> I have a very old database in Cobol and now I need to convert to Obdc
> database format. I have no idea about Cobol, is there any program to do it?
> Can I use other way to do it? Thanks.

Standard COBOL does not have files or databases specific to it.  They
are provided as facilities available from the operating system on
which the COBOL compilers and programs are run.  At least until the
next standard is issued!

For us to provide more help, we need to know the supplier of the COBOL
compiler your organisation has or used to have to create the database.
 We also need to know the version of the compiler, the operating
system and version (e.g. Windows XP, Linux, MacOS, MVS, VSE, OS390,
etc), and the hardware (e.g. windows PC, Mac PC, mainframe-type, etc).
 We also need more information about the Database software, e.g. name,
supplier, version, database type.  If you don't know all this, then
tell us what the file suffixes are for the database's constituent
files.

There are several useful utilities to do conversions on files and
simple databases, "PARSERAT" is one such (I think it is free, or at
least not very expensive) and can be found by a search on the web. 
Even if such a utility doesn't do all of the job, it may be able to do
a useful part of it.

Regards,

Robert
```

#### ↳ Re: converting from cobol to other obdc database

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-02-24T15:31:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1fqnv$oi8$1@peabody.colorado.edu>`
- **References:** `<IUz_b.3586832$uj6.10411952@telenews.teleline.es>`

```

On 23-Feb-2004, "Sam" <vermello@terra.es> wrote:

> I have a very old database in Cobol and now I need to convert to Obdc
> database format. I have no idea about Cobol, is there any program to do it?
> Can I use other way to do it? Thanks.

While CoBOL an access databases, usually when I see someone ask this question,
that's not what it's doing.   CoBOL was designed before modern databases were
invented and it handles flat files quite well.

Flat files aren't "CoBOL files", they're sort of text files with data in
particular locations on each record (on each line).

What you need to do is to find out where each field is.

e.g.

Washington          George      123456789000bPresident

Read this message with a fixed font.
....5....1....5....1....5....1....5....1....5....1....5.....1....5.....1
This record has last name starting in columns 1-20.   First name is in columns
21-32.   SSN=columns 33-41.   000b looks weird.  It is a signed number.   It may
have an implied decimal point in it that isn't stored.

If you have your CoBOL source code, there's a description somewhere in it that
shows how your fields are defined.

Once you know how they are defined, you can write a program in any language to
read the fields and then write them as you wish, possibly comma delimited for
your PC's database.
```

##### ↳ ↳ Re: converting from cobol to other obdc database

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-02-24T18:43:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gXM_b.18672$W74.93@newsread1.news.atl.earthlink.net>`
- **In-Reply-To:** `<c1fqnv$oi8$1@peabody.colorado.edu>`
- **References:** `<IUz_b.3586832$uj6.10411952@telenews.teleline.es> <c1fqnv$oi8$1@peabody.colorado.edu>`

```
COBOL is a method for processing data!  The method of accessing data is 
not a function of COBOL.  Instead, accessing (and maintaining) data is a 
function of others - the operating system (VSAM, ISAM, BDAM, SEQUENTIAL 
in the mainframe world, .txt on the PC format etc.), or  a "foreign" 
database  (SQL (generic), IMS, CA-IDMS) etc.

For operating system structures, standard IO routines 
(READ/WRITE/MODIFY) apply and that interface is built into COBOL. 
"Foreign" databases manipulation is called/spawned/linked to by COBOL to 
the database itself (through native "calls" and/or ODBC "calls") through 
internally generated statements or through a preprocessor induced 
conversion.

Regardless of how the data is stored ("flat file" or database (any)), 
BEFORE ANY conversion is attempted, a through understanding of the DATA 
(including data relationships) is REQUIRED.  (Trivially, you need to 
know that nbr_CUSTOMER represents the same thing as CLIENT-ID before you 
do anything.   If you don't,  any conversion that takes place will 
either fail outright (hopefully) or "work" and be wrong (worst case).

Continuing, you need to know how the "converted to" database works.  If 
not, your conversion may result in more problems than the "database" 
needing conversion had.

Please do not take this as a slam on your talents,  but things that you 
need to know to accomplish your task.

Dick, a semi-retired database administrator

Howard Brazee wrote:

> On 23-Feb-2004, "Sam" <vermello@terra.es> wrote:
> 
…[30 more quoted lines elided]…
> your PC's database.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
