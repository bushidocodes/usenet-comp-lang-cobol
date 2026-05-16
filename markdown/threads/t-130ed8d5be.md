[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acu Cobol

_4 messages · 4 participants · 2001-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Acu Cobol

- **From:** "Pierfish" <piero@netgroup.it>
- **Date:** 2001-09-26T13:00:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9osbev$474$1@fe1.cs.interbusiness.it>`

```
I have an application written with AcuCobol and I have necessity to import
my data
in SQL Server.

I HAVE NOT THE DESCRIPTION OF THE TABLES

What I can do?

The software has not been compiled with the option for ODBC!!
```

#### ↳ Re: Acu Cobol

- **From:** frederico_fonseca@eudoramail.com (Frederico Fonseca)
- **Date:** 2001-09-26T06:18:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ea0f9e1.0109260518.31912efc@posting.google.com>`
- **References:** `<9osbev$474$1@fe1.cs.interbusiness.it>`

```
"Pierfish" <piero@netgroup.it> wrote in message news:<9osbev$474$1@fe1.cs.interbusiness.it>...
> I have an application written with AcuCobol and I have necessity to import
> my data
…[4 more quoted lines elided]…
> What I can do?

You can always contract my company (me) to do the work for you.
I'm not overly expensive, and I would love a week off in Italy.

FF
```

#### ↳ Re: Acu Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-09-27T07:27:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB2C6B4.71694948@Azonic.co.nz>`
- **References:** `<9osbev$474$1@fe1.cs.interbusiness.it>`

```
Pierfish wrote:
> 
> I have an application written with AcuCobol and I have necessity to import
…[4 more quoted lines elided]…
> What I can do?

Not a lot.

> The software has not been compiled with the option for ODBC!!

Putting the data into SQL Server will (most likely) not change where the
application looks for the data, it will still access the files that it
currently does.

It may be useful for _other_ purposes to have an extract of the data in
some database, but it would be necessary to extract the data using the
application, say reports 'printed' to disk files.  Then you would have
to pick out the data from the reports and load it into SQL with a
program, and do this on a regular basis to keep it up to date.
```

#### ↳ Re: Acu Cobol

- **From:** "Acucorp News" <shaun_gough@hotmail.com>
- **Date:** 2001-09-28T13:27:39-07:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<1451C740A890D411B65C00104B95B1C03BA9F7@ras.acucorp.com>`
- **References:** `<9osbev$474$1@fe1.cs.interbusiness.it>`

```
Take a look at the Acu4GL for MSSQL product by looking at the following
internet page, that describes the outline of this product and also shows
you how to use the product once you have obtained a copy:

http://www.acucorp.com/Solutions/acu4glmssql.html

Contact your local Acucorp office for more details on purchasing and
using this product, as this will allow you to move data from a Vision
file into a MSSQL table with minimum of effort.

Acucorp also sells a AcuODBC product, so that you can access Vision file
data into a ODBC application. The outline of this product can be located
at:

http://www.acucorp.com/Solutions/acuodbc.html

 

Thanks 
Shaun Gough - Snr Technical Support Representative 
ACUCORP Inc. 
8515 Miralani Drive, San Diego, CA 92126, USA 
E-Mail: sgough@acucorp.com 
Phone: +1 (0)800 399 7220 
Fax: +1 (0)858 689 4552 
http://www.acucorp.com

Please send all responses to support@acucorp.com to ensure prompt
handling of the issue by a technical support representative. If an
existing issue, please mark for my attention.

Coming soon. . .Version 5.2 of extend(tm)5

Version 5.2 includes a full range of modern COBOL development tools as
well as many up-to-date computing technologies, such as Acucorp's
much-anticipated Thin Client deployment capabilities. With Acucorp's
Thin Client Technology, you can display your server-based application on
graphical display hosts. For more information or a copy of our free
evaluation software, please contact a Sales Professional by calling
(800) 262-6585 (within the U.S.) or (858) 689-4500.

"Pierfish" <  <mailto:piero@netgroup.it> piero@netgroup.it> wrote in
message  <news:9osbev$474$1@fe1.cs.interbusiness.it>
news:9osbev$474$1@fe1.cs.interbusiness.it...
> I have an application written with AcuCobol and I have necessity to
import
> my data
> in SQL Server.
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
