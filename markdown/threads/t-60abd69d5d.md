[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus COBOL ISAM files - are they C/ISAM compatible?

_9 messages · 9 participants · 2001-11 → 2002-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** "Tzachi Nissim" <tzachi@attunity.co.il>
- **Date:** 2001-11-07T11:45:33+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9savsh$hkg$1@news.netvision.net.il>`

```
Hi,

We are trying to access files created using Micro Focus COBOL on an HP
machine using a CISAM ODBC with partial success. Most files work okay. It
looks like the variable length files are not working.

Does anyone know if MicroFocus COBOL produces CISAM compatible files? If
so - which version of CISAM?

Any help would be appreciated...

Tzachi
```

#### ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-11-07T15:30:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9sc95o$ug6$1@slb0.atl.mindspring.net>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il>`

```
1) "Traditionally" Micro Focus COBOL under HP is a "weird" combination of
Micro Focus and HP technology.  Therefore, what is true of Micro Focus COBOL
in other environments is SOMETIMES not true under HP.

2) "normal" Micro Focus *does* have an OPTION to produce C-ISAM files.

What I would suggest you do is check YOUR compiler documentation (probably
the "User Guide") for the FILE-TYPE directive - and see what it says about
C-ISAM
```

#### ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** charles.godwin@ca.com (Charles Godwin)
- **Date:** 2001-11-08T12:55:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8035ce7.0111081255.3897b337@posting.google.com>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il>`

```
My first question about an ODBC interface to a variable length record
is how do you map fields on the record to a database schema
definition? I always assumed data base "tables" were comprised of
fixed elements or columns and a variable length record by definition
breaks that assumption.

"Tzachi Nissim" <tzachi@attunity.co.il> wrote in message news:<9savsh$hkg$1@news.netvision.net.il>...
> Hi,
> 
…[9 more quoted lines elided]…
> Tzachi
```

##### ↳ ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2001-11-09T01:54:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0111090154.71675d8e@posting.google.com>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il> <c8035ce7.0111081255.3897b337@posting.google.com>`

```
charles.godwin@ca.com (Charles Godwin) wrote in message news:<c8035ce7.0111081255.3897b337@posting.google.com>...
> My first question about an ODBC interface to a variable length record
> is how do you map fields on the record to a database schema
> definition? I always assumed data base "tables" were comprised of
> fixed elements or columns and a variable length record by definition
> breaks that assumption.
My experience with Liant's ODBC driver (formerly Relativity), tells me
that you get a "virtual" table for every diferent record layout
although they reside in the same COBOL file. As you probably have some
kind of flag indicating the type of record, that is of good candidate
for an 88 level.

best regards,
Paulo Vieira, Emporsoft
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2001-11-09T15:27:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZBSG7.7101$dn3.1964256441@newssvr30.news.prodigy.com>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il> <c8035ce7.0111081255.3897b337@posting.google.com> <b5b8d7c7.0111090154.71675d8e@posting.google.com>`

```

"Paulo Vieira" <pvieira@emporsoft.pt> wrote in message
news:b5b8d7c7.0111090154.71675d8e@posting.google.com...
> charles.godwin@ca.com (Charles Godwin) wrote in message
news:<c8035ce7.0111081255.3897b337@posting.google.com>...
> > My first question about an ODBC interface to a variable length record
> > is how do you map fields on the record to a database schema
…[7 more quoted lines elided]…
> for an 88 level.

Relativity is quite flexible in dealing with variable record lengths.

Multiple record types is a common reason for variable length records in a
file, and typically the best way is to use multiple table definitions for
the same physical file.  In this case, each record type usually has a fixed
length; the file is variable record length due to the intermixing of record
types.   Each table definition deals with only one record type, so the
variable record length aspect is not an issue.

There are other reasons for variable length records, however, and Relativity
has techniques to map these as well.

For example, one may have OCCURS ... DEPENDING ON  in the record definition,
making records of the same "type" with  a variable length.  Relativity
automatically normalizes OCCURS by generating multiple rows for the data
subordinate to the OCCURS clause, so in the case of OCCURS ... DEPENDING ON
the number of rows thus generated is different for each physical record
(depending on the DEPENDING ON variable, as it were).

There are other, more arcane ways to generate variable length records (eg
RECORD IS VARYING IN SIZE clause in the File Description entry).  To that
end, one may condition column values based upon the record length of each
record as it is read.  For each of the data items that might be "missing"
(due to a short record), one would define NULL condition based on the actual
record size, so that the column(s) based upon the potentially missing COBOL
data item(s) would return NULL.

Variable length records are only one of the difficulties faced while
providing ODBC access to indexed (and other) 3GL files.  Relativity is a
thorough solution which is available for Micro Focus COBOL on HP and which
has its developers reading comp.lang.cobol regularly -- and of course I
recommend Relativity!

Tom Morrison
Liant Software Corporation
www.liant.com
http://www.liant.com/products/relativity/

P.S.  Relativity is both the former and current name of Liant's ODBC access
product.  There was a short period in the product's history when it had a
different name, but that is behind us now.  :-)

Relativity is a registered trademark of Liant Software Corporation.

Relativity products contain software protected by:
U.S. Pat. No. 5,826,076
British Pat. No. GB2302430
Other Patents Pending
```

#### ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** Cygni.69@libero.it (Cygni.69)
- **Date:** 2001-11-15T11:10:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bebe2ef.22628789@news.interbusiness.it>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il>`

```
On Wed, 7 Nov 2001 11:45:33 +0200, "Tzachi Nissim"
<tzachi@attunity.co.il> wrote:

>Hi,
>
…[5 more quoted lines elided]…
>so - which version of CISAM?

Tray this compiler directives on MF program
IDXFORMAT "n"      where n is
0	Default format for the operating system (same as 3 on Windows)
1	C-ISAM
3	Micro Focus default indexed file format
4	Optimized format for fast duplicate key handling
5	Btrieve with ANSI conformance
6	Btrieve without ANSI conformance
8	Large indexed file format

or alternativly 
FILETYPE "n" where n is
0	System-specific default (for this COBOL system, same as 3).
1	C-ISAM format.
2	Micro Focus Level II format.
3	Micro Focus COBOL format.
4	An optimized form of the format used by this COBOL system, for
fast duplicate key handling.

FILETYPE"integer" sets IDXFORMAT"integer" immediately.

If you can't rebuild your files or your project that produce you
files, try to convert them whit microfocus file converter,  
(I think you must convert them first in Line-Sequential and
subsequently in C-ISAM)  the tool is included in MF WORKBENCH or
NETExpress.

Hi!
```

#### ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2001-11-16T07:50:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BF4C5EB.EDFD5A5C@siber.com>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il>`

```
You can try our DataAccess library taht allows to read Cobol data files
straight into C++ program (or COM program).

http://www.siber.com/sct/datafile/

Vadim Maslov
Siber Systems

Tzachi Nissim wrote:
> 
> Hi,
…[10 more quoted lines elided]…
> Tzachi
```

##### ↳ ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** amine <member@dbforums.com>
- **Date:** 2002-05-29T06:32:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cf475e5$1@usenetgateway.com>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il> <3BF4C5EB.EDFD5A5C@siber.com>`

```
Vadim Maslov  wrote:
  > You can try our DataAccess library taht allows to read Cobol data files
  > straight into C++ program (or COM program).
…[15 more quoted lines elided]…
  > > Tzachi

I serach to connect to microfocus cobol file via ODBC My question :
working on windows 2000, is an insatallation of ISAM driver is necessary
if yes where i will find a freeware driver? any help will be aprreciated
mail : kerkeni_amine@yahoo.com
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL ISAM files - are they C/ISAM compatible?

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-05-29T15:48:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9L6J8.57075$352.3602@sccrnsc02>`
- **References:** `<9savsh$hkg$1@news.netvision.net.il> <3BF4C5EB.EDFD5A5C@siber.com> <3cf475e5$1@usenetgateway.com>`

```
I'm not aware of a freeware driver.... but if you decide you are willing to
pay after all then check out http://www.transoft.com they have an OBDC
driver which may work for you....  look for their U/SQL product.....

Mike


> I serach to connect to microfocus cobol file via ODBC My question :
> working on windows 2000, is an insatallation of ISAM driver is necessary
…[8 more quoted lines elided]…
> http://dbforums.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
