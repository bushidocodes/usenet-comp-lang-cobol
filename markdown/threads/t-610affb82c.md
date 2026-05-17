[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC interface to Cobol Data Files

_4 messages · 4 participants · 1996-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC interface to Cobol Data Files

- **From:** "aiden j.mccaughey" <ua-author-17087097@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<325512F6.470A@ulst.ac.uk>`

```

Hi,
Does anyone know of an ODBC driver for accessing Cobol datafiles
created with either RMCobol or Microfocus Cobol. (or are all Cobol data
files the same format ?).

Any help would be greatly appreciated. Reply by email if possible.


Aiden McCaughey
___________________________________________________________________________
Aiden J. McCaughey, Faculty of Informatics, University of
Ulster
Magee College, Derry, BT48 7JL, N. Ireland. Tel +44 1504 375334, Fax
375416
____ email: AJ.··.@uls··c.uk, http://www.infm.ulst.ac.uk/~aiden/
___
```

#### ↳ Re: ODBC interface to Cobol Data Files

- **From:** "uwe baemayr" <ua-author-6588910@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-610affb82c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<325512F6.470A@ulst.ac.uk>`
- **References:** `<325512F6.470A@ulst.ac.uk>`

```

Aiden J.McCaughey wrote:
› 
› Hi,
…[6 more quoted lines elided]…
› Aiden McCaughey

Liant Software (Ryan McFarland's parent company) offers exactly what
you're describing for both RM/COBOL and MFCOBOL. The product is
called "Relativity" and there is a version for RM/COBOL and for
MFCOBOL files (and the data formats are *not* remotely the same).
Take a look at

http://www.liant.com/products/relprod.htm

You can also contact our London office at (011 44) 171 799-2434 and
they'll be happy to provide you with all the information you need.

------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Ryan McFarland Corporation | or: jea··.@ccw··s.edu |
| -- a division of Liant Software | Compuserve: 74774,47 / GO LIANT |
------------------------------------------------------------------------
```

#### ↳ Re: ODBC interface to Cobol Data Files

- **From:** "r..." <ua-author-185095@usenetarchives.gap>
- **Date:** 1996-10-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-610affb82c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<325512F6.470A@ulst.ac.uk>`
- **References:** `<325512F6.470A@ulst.ac.uk>`

```

"Aiden J.McCaughey" wrote:

› Hi,
›   Does anyone know of an ODBC driver for accessing Cobol datafiles
› created with either RMCobol or Microfocus Cobol. (or are all Cobol data
› files the same format ?). 
 
› Any help would be greatly appreciated. Reply by email if possible.

1. All COBOL data files are definitely not the same format.
a. Micro Focus (under DOS/Windows) has its own proprietary format,
although an earlier version of C/ISAM may be configured instead
b. Under UNIX, Micro Focus uses an old version of C/ISAM
c. RM COBOL has its own proprietary format - not the same as the
Micro Focus format

2. To the best of my knowledge, there are THREE ODBC drivers
available:
a. Micro Focus has Correlate, currently available only as a 16-bit
product, which allows ODBC access to the Micro Focus proprietary
format files.
b. Liant sells Relativity, which handles either Micro Focus or RM
files (I think that one or two other formats are supported as well).
c. ParkWay in Munich (if you are on Compuserve, search for either
Parkway or Frank Danner) did at one time have ODBC drivers for Micro
Focus.



Robert Essex
Milford Haven
Wales
r.··.@mon··o.uk
```

##### ↳ ↳ Re: ODBC interface to Cobol Data Files

- **From:** "jason" <ua-author-11075@usenetarchives.gap>
- **Date:** 1996-10-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-610affb82c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-610affb82c-p3@usenetarchives.gap>`
- **References:** `<325512F6.470A@ulst.ac.uk> <gap-610affb82c-p3@usenetarchives.gap>`

```

The LIANT product is available for RM/COBOL, MF COBOL and VAX COBOL.
Relativity is available to both 16 and 32 bit ODBC client products.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
