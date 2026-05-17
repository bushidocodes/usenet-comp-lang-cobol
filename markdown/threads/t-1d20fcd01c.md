[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need info on SUPRA

_4 messages · 4 participants · 1998-01_

---

### Need info on SUPRA

- **From:** "sreedhar manjigani" <ua-author-17072780@usenetarchives.gap>
- **Date:** 1998-01-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6919m4$rgh@mtinsc04.worldnet.att.net>`

```

I need some info. on Supra databases. Are they similar to VSAM files?
Do they primary or secondary keys? How are they read from /written to ?

Any help is appreciated.

Sreedhar
```

#### ↳ Re: Need info on SUPRA

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-01-07T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1d20fcd01c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6919m4$rgh@mtinsc04.worldnet.att.net>`
- **References:** `<6919m4$rgh@mtinsc04.worldnet.att.net>`

```

Sreedhar Manjigani wrote:
› 
› I need some info. on Supra databases.  Are they similar to VSAM files?
…[4 more quoted lines elided]…
› Sreedhar

Supra is an SQL type database produced by a company called CINCOM.

Try http://www.cincom.com/supra/aboutsupra.htm

or http://www.cincom.com for information about the company.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

##### ↳ ↳ Re: Need info on SUPRA

- **From:** "sl..." <ua-author-4338670@usenetarchives.gap>
- **Date:** 1998-01-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1d20fcd01c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1d20fcd01c-p2@usenetarchives.gap>`
- **References:** `<6919m4$rgh@mtinsc04.worldnet.att.net> <gap-1d20fcd01c-p2@usenetarchives.gap>`

```

› Sreedhar Manjigani wrote:
››
›› I need some info. on Supra databases. Are they similar to VSAM files?
›› Do they primary or secondary keys? How are they read from /written to ?

Supra is a R based DB engine. Originally designed
by University of Berlin, it was developed by the
old Nixdorf Computer (prior to the Siemens buyout)
and initially marketed as "DB4".
Cincom bought a source licence and used
it as the base for migrating the Mantis development
tool to multiple bases, and have subsequently modified
it considerably.
The original DB4 engine ran on a multiplicity of platforms
from IBM mainframes to Unix to PC's, some implementations
may have used VSAM as a basic access method,
but it has several different support environments.
You could never directly access the database thru VSAM.
Because it is an encapsulated system,
it has a typical System R SQL server based run time environment.
There are also various language interface API's.
You have to use the Runtime environment in order
to read or write records, because of logging, data
integrity etc.
It is a typical Client/Server
design with twophase commit and all the other
Codd and Date stuff.
It is functionally equivalent and similar to DB2 or Oracle.
It is not really an Open System, it is a proprietary
solution. Contact the Suppliers, Cincom.

------------------------------------------------------------------------
Chris Anderson email: sl··.@fas··o.za
Y2K Cinderella Project web··.@cin··o.za
http://www.cinderella.co.za Striving for Year 2000 Compliance
------------------------------------------------------------------------
```

#### ↳ Re: Need info on SUPRA

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-01-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1d20fcd01c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6919m4$rgh@mtinsc04.worldnet.att.net>`
- **References:** `<6919m4$rgh@mtinsc04.worldnet.att.net>`

```

My experience with Supra is a little old but:

Supra is not a relational database it is a network database. It relies
on pointers in the files to find things. eg:

Account contains a pointer to a record in the transactions file.

Each record in the transactions file has a pointer to the next
transaction.

This means that access to records is bery fast but if the database gets
corrupted it is totally stuffed.

I wrote reporting using the COMPRET reporting tool that came with it and
using a view was about four times slower than reading the file as a
sequential file (assuming that you want a single file and 100% of the
records).

As I said my experience is very dated.

Ken

Sreedhar Manjigani wrote:
› 
› I need some info. on Supra databases.  Are they similar to VSAM files?
…[4 more quoted lines elided]…
› Sreedhar
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
