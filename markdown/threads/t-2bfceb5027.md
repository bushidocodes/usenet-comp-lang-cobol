[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC

_10 messages · 6 participants · 2002-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC

- **From:** "Daniel Yataco" <dymcs@earthlink.net>
- **Date:** 2002-06-20T00:20:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net>`

```
is there any odbc driver for RM-Cobol 85?
```

#### ↳ Re: ODBC

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-06-20T09:24:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net>`

```
On Thu, 20 Jun 2002 00:20:51 GMT, "Daniel Yataco"
<dymcs@earthlink.net> wrote:

>is there any odbc driver for RM-Cobol 85?
>
>
Yes.
See www.liant.com and look for Relativity (or Relational Databridge).
```

##### ↳ ↳ Re: ODBC

- **From:** "FELIX GUTIERREZ" <gmt.02@earthlink.net>
- **Date:** 2002-06-20T21:50:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com>`

```
I wenty there but the price is around $5,000.00, so is too expensive for my
pocket, any solution less expensive?.


"Frederico Fonseca" <frederico_fonseca@eudoramail.com> wrote in message
news:k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com...
> On Thu, 20 Jun 2002 00:20:51 GMT, "Daniel Yataco"
> <dymcs@earthlink.net> wrote:
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ODBC

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-06-20T23:19:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net>`

```
On Thu, 20 Jun 2002 21:50:42 GMT, "FELIX GUTIERREZ"
<gmt.02@earthlink.net> wrote:

>I wenty there but the price is around $5,000.00, so is too expensive for my
>pocket, any solution less expensive?.
Maybe,

What are youre requirements exactly? If you give us that then we may
be able to help further.


FF
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 4)_

- **From:** "Daniel Yataco" <dymcs@earthlink.net>
- **Date:** 2002-06-21T01:18:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com>`

```
I have one customer with a Financial application using  RMCobol 85 version
5.24, he wants to migrate the data to SQL database and I dont want to write
programs to create text files from the cobol data files. So it is more easy
using ODBC and DTS from SQL.

"Frederico Fonseca" <frederico_fonseca@eudoramail.com> wrote in message
news:b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com...
> On Thu, 20 Jun 2002 21:50:42 GMT, "FELIX GUTIERREZ"
> <gmt.02@earthlink.net> wrote:
>
> >I wenty there but the price is around $5,000.00, so is too expensive for
my
> >pocket, any solution less expensive?.
> Maybe,
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 5)_

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-06-21T08:15:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com> <J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net>`

```
On Fri, 21 Jun 2002 01:18:33 GMT, "Daniel Yataco"
<dymcs@earthlink.net> wrote:

>I have one customer with a Financial application using  RMCobol 85 version
>5.24, he wants to migrate the data to SQL database and I dont want to write
>programs to create text files from the cobol data files. So it is more easy
>using ODBC and DTS from SQL.
If this is the situation then I would sugest that you do just that. It
is far more cost effective than to set-up all ODBC requirements (e.g.
field definition, record types, nullable fields, date fields and
so on). Some of the other possible solutions would take even more time
than creating the file convertion programs.

If you personally do not have the time or knowledge to do it, then any
COBOL programmer with some experience will be able to to it for a fee.


Regards

FF
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 6)_

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2002-06-21T16:06:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aILQ8.14969$x82.476040@weber.videotron.net>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com> <J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net> <0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com>`

```
> If you personally do not have the time or knowledge to do it, then any
> COBOL programmer with some experience will be able to to it for a fee.
>

I don't think it is because he do not have the time or knowledge, it is
probably because his client do not have thousand of dollar to flip away.
Us, we sold our software 3000 to 15000 $, if we ask them another 5000$ to be
able to do simply ODBC they will look at us as thief.  Client are not
stupid!  They know better the market and they know that for almost any kind
of database or file or whatever things, there is ODBC and this do not cost
5000$$$.

Eric.




"Frederico Fonseca" <frederico_fonseca@eudoramail.com> a �crit dans le
message de news: 0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com...
> On Fri, 21 Jun 2002 01:18:33 GMT, "Daniel Yataco"
> <dymcs@earthlink.net> wrote:
>
> >I have one customer with a Financial application using  RMCobol 85
version
> >5.24, he wants to migrate the data to SQL database and I dont want to
write
> >programs to create text files from the cobol data files. So it is more
easy
> >using ODBC and DTS from SQL.
> If this is the situation then I would sugest that you do just that. It
…[11 more quoted lines elided]…
> FF
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 7)_

- **From:** "Daniel Yataco" <dymcs@earthlink.net>
- **Date:** 2002-06-21T20:59:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ssMQ8.11418$uH2.4078@newsread1.prod.itd.earthlink.net>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com> <J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net> <0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com> <aILQ8.14969$x82.476040@weber.videotron.net>`

```
You really reach the point, severals months ago I did  the same for another
client using CLARION and  I just paid around $249 for the stand alone ODBC
version (http://www.softvelocity.com/products/pr_database_tsodbc.htm).

It's amazing why COBOL is too expensive.


"Eric Gauthier" <ericg@dgcsolutions.qc.ca> wrote in message
news:aILQ8.14969$x82.476040@weber.videotron.net...
> > If you personally do not have the time or knowledge to do it, then any
> > COBOL programmer with some experience will be able to to it for a fee.
…[4 more quoted lines elided]…
> Us, we sold our software 3000 to 15000 $, if we ask them another 5000$ to
be
> able to do simply ODBC they will look at us as thief.  Client are not
> stupid!  They know better the market and they know that for almost any
kind
> of database or file or whatever things, there is ODBC and this do not cost
> 5000$$$.
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-21T23:24:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EAOQ8.1792$cE5.155@nwrddc02.gnilink.net>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com> <J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net> <0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com> <aILQ8.14969$x82.476040@weber.videotron.net> <ssMQ8.11418$uH2.4078@newsread1.prod.itd.earthlink.net>`

```
If you can call the Windows API (and I know someone has posted COBOL
examples of this somewhere), you can download the SDK for free from
Microsoft and write all the ODBC access code yourself. The  ODBC susbsystem
is also free (and included since Win 95/second release as part of the basic
Windows install.)

No out of pocket expense at all!

(You should be able to master the ODBC calls in only, say 50-100 hours.)
(Assuming you are already comfortable with Windows API calls).
```

###### ↳ ↳ ↳ Re: ODBC

_(reply depth: 8)_

- **From:** j.bradley@liant.com (John Bradley)
- **Date:** 2002-06-24T13:10:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<25fb80a6.0206241210.1dffde23@posting.google.com>`
- **References:** `<Dd9Q8.6100$Fv1.640370@newsread2.prod.itd.earthlink.net> <k843hu810q97kqmucji6qo7urhm8n4hbik@4ax.com> <S6sQ8.8993$uH2.2137@newsread1.prod.itd.earthlink.net> <b5l4hukpa903ofmm6igqfkdggm76k34oig@4ax.com> <J9vQ8.9370$uH2.4136@newsread1.prod.itd.earthlink.net> <0ck5hu4e37btef9v066bbt7a86qepl8d3k@4ax.com> <aILQ8.14969$x82.476040@weber.videotron.net> <ssMQ8.11418$uH2.4078@newsread1.prod.itd.earthlink.net>`

```
Daniel,

As Frederico alluded, Relativity is primarily targeted at the COBOL
developer who wants to expose his applications' data as a
(well-normalized) relational database.  It can be used for conversion,
but the cost justification for a one-time conversion is sometimes (but
not always) difficult.

Just to clarify, Relativity is not $5,000, especially for use in a
one-time conversion.  The Data Designer (which is the part that allows
you to remodel a very unrelational COBOL database into a good
relational database) is $2,600 (US list) and the Data Manager (the
actual ODBC Driver) is $150 (US list).  Ordinarily, the (COBOL)
application provider would need the Designer, but their customers
would need only the ODBC driver for $150 (or less).  For a one-time
conversion, you would need both ($2,750).  Whether or not this is
better than the alternative (custom COBOL application) depends on how
complex the COBOL database is.  If it is a typical COBOL application
with hundreds of files, each of which could have dozens of record
types, it is quite often the case that the $2,750 for Relativity and a
few dozen hours of data modeling is much, much less expensive that a
custom application in COBOL.

The thing to remember is that COBOL's "flat files" are anything but
flat, and they are typically not at all normalized.  Unlike many
proprietary 4GL's which have files that correspond to more-or-less
relational tables, COBOL applications typically have very complex
native COBOL structures embedded in the files.  It is the unraveling
of these (and the knowledge of the application necessary to do so)
that is expensive.

Also, we have spent over $5,000,000 developing the ODBC driver, so I
think you would probably have to spend a little more than 50-100 hours
to write your own, even for a single COBOL application.

Good luck, let us know if we can help.

Regards,
John Bradley
Liant Software Corporation


"Daniel Yataco" <dymcs@earthlink.net> wrote in message news:<ssMQ8.11418$uH2.4078@newsread1.prod.itd.earthlink.net>...
> You really reach the point, severals months ago I did  the same for another
> client using CLARION and  I just paid around $249 for the stand alone ODBC
…[53 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
