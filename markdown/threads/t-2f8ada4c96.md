[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tools for accessing cobol data files from Windows

_7 messages · 7 participants · 2000-04_

---

### Tools for accessing cobol data files from Windows

- **From:** Marte <fjmNOfjSPAM@mail.telepac.pt.invalid>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
Anybody knows tools for acessing cobol data files from windows?
I know only ACUODBC. I would like import data from Cobol to the
EXCEL spreadsheet.
Please, Help me.

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Tools for accessing cobol data files from Windows

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ef4fad_1@news1.prserv.net>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
Marte,

If you are wanting to access MVS Cobol data files from Windows, our
company offers an API that can be used with Visual Basic, Visual C++, or
Cobol (MF, Fujitsu, Realia) to do various things like this: Transfer
files to/from, obtain catalog listings, obtain dataset attributes,
catalog/rename/delete datasets, submit MVS jobs from the PC, etc.  It
seamlessly interfaces with both standard PDS's and CA-Librarian
libraries.

Please check out our web-site at http://www.c-cubed.net if you are
interested...

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net

C-Cubed Inc.
3629 North Morning Dove
Mesa, AZ  85207

Phone:  (888) 962-8233
Fax:    (888) 962-4658
Web:   http://www.c-cubed.net
Marte <fjmNOfjSPAM@mail.telepac.pt.invalid> wrote in message
news:047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com...
> Anybody knows tools for acessing cobol data files from windows?
> I know only ACUODBC. I would like import data from Cobol to the
…[3 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion
Network *
> The fastest and easiest way to search and participate in Usenet -
Free!
>
```

#### ↳ Re: Tools for accessing cobol data files from Windows

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EF7772.75770F85@siber.com>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
Marte wrote:
> 
> Anybody knows tools for acessing cobol data files from windows?
…[5 more quoted lines elided]…
> The fastest and easiest way to search and participate in Usenet - Free!

DataReaders from Siber Systems http://www.siber.com/sct/datafile/
can do just that -- they can convert Cobol data files to 
DBF files that can be directly imported into Excel spreadsheet.

Regards,
Vadim Maslov
```

#### ↳ Re: Tools for accessing cobol data files from Windows

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EF8F65.4DC2@NOSPAMguysoftware.com>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
Marte wrote:
> 
> Anybody knows tools for acessing cobol data files from windows?
> I know only ACUODBC. I would like import data from Cobol to the
> EXCEL spreadsheet.
> Please, Help me.

You might want to try a generic parser/converter like ParseRat 
(http://www.guysoftware.com/parserat.htm).
```

#### ↳ Re: Tools for accessing cobol data files from Windows

- **From:** John Mosier <jmosier@netzone.com>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EFBB30.5BC5C65@netzone.com>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
We use a product called Data Junction.  It is an EXTREMELY capable system
for data extraction and Data Migration.  It handles MANY data types, both
on the input side and the output side.

We are an Acucobol developer as well as a Data Junction Consultant.

Marte wrote:

> Anybody knows tools for acessing cobol data files from windows?
> I know only ACUODBC. I would like import data from Cobol to the
…[4 more quoted lines elided]…
> The fastest and easiest way to search and participate in Usenet - Free!
```

##### ↳ ↳ Re: Tools for accessing cobol data files from Windows

- **From:** Stefan Meyer <meyerst@my-deja.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8crvec$5qj$1@nnrp1.deja.com>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com> <38EFBB30.5BC5C65@netzone.com>`

```
Hi John,

we're using Parkway Odbc driver to access our Cobol files. If your
Cobol files are residing on a Unix machine it is possible to access the
files through a Server using Tcp/Ip, which is really fast.

Cause it's ODBC you are able to use your files within all ODBC
supporting programms.

To contact Parkway please mailto: parkway_software@compuserve.com or
visit their homepage on www.parkway-software.de (german/english).

HTH - Stefan Meyer

In article <38EFBB30.5BC5C65@netzone.com>,
  John Mosier <jmosier@netzone.com> wrote:
> We use a product called Data Junction.  It is an EXTREMELY capable
system
> for data extraction and Data Migration.  It handles MANY data types,
both
> on the input side and the output side.
>
…[9 more quoted lines elided]…
> > * Sent from RemarQ http://www.remarq.com The Internet's Discussion
Network *
> > The fastest and easiest way to search and participate in Usenet -
Free!
>
> --
> John Mosier,  Excelco      Fax:  (602) 992-2026  Voice: (602) 992-8076
> http://www.swinfo.com
http://www.excelco.com
> 2990 E Northern Ave, Ste A-101, Phoenix, AZ  85028    (800) 553-6911
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Tools for accessing cobol data files from Windows

- **From:** "scoobie" <scoobie@snacks.mmm>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f1dc85.0@nnrp1.news.uk.psi.net>`
- **References:** `<047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com>`

```
try this
http://www.liant.com/products/relativity/

this could help you out.......

Marte <fjmNOfjSPAM@mail.telepac.pt.invalid> wrote in message
news:047a0f63.0ae8e6b7@usw-ex0101-005.remarq.com...
> Anybody knows tools for acessing cobol data files from windows?
> I know only ACUODBC. I would like import data from Cobol to the
…[3 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
