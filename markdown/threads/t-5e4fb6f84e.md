[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# excel from cobol

_10 messages · 7 participants · 2001-11_

---

### excel from cobol

- **From:** im4liberty@aol.com (Im4Liberty)
- **Date:** 2001-11-06T02:57:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
Hello,

Has anyone ever successfully updated an excel spreadsheet from a NetExpress
COBOL program?   I've been able to "connect" to the spreadsheet via ODBC, but
I'm not sure how to get data into the cells.   INSERT/UPDATE commands don't
seem to work, as I'm not sure what the "table" name is (I tried using "sheet1"
to no avail).   Is there a way to update the 'sheet directly, without going
through ODBC?

Any input would be appreciated.

Bill
```

#### ↳ Re: excel from cobol

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2001-11-06T01:34:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0111060134.2631539c@posting.google.com>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
im4liberty@aol.com (Im4Liberty) wrote in message news:<20011105215718.03573.00001375@mb-mw.aol.com>...
> Hello,
> 
…[9 more quoted lines elided]…
> Bill

Hello Bill
Yes there is a much simpler way. I haven't done it in NetExpress, but
with Fujitsu; but I'm shure since Microfocus is able to invoke OLE
objects, that it is not a problem.
First thing you must know is the OLE name of Excel:
"excel.application".
In Fujitsu we have a special class to handle OLE comunication, so a
write:
INVOKE OLE "CREATE-OBJECT" USING APP-NAME RETURNING OLE-HANDLE
where:
-OLE is my special class for OLE objects 
-APP-NAME is a PIC X(17) value "excel.application"
-OLE-HANDLE is an OBJECT REFERENCE OF CLASS OLE

After you have established a handle to Excel, there is a LOT of things
you can do:
Open Workbooks, open specific spreadsheets in a workbook, GET and SET
values for a cell or range of cells, etc.. That, of course, you'll
have to learn from the Microsoft Documentation.
By the way, if you happen to go this way, don't follow Microsoft
examples for VB, since there you can have something like:
   app-name.Workbook(dumb.xls).sheet(sheet1).range(A2).value = val
that, in COBOL, translate to 7 calls
   invoke OLE "CREATE-OBJECT" using app-nm returning excel
   invoke excel "GET-Workbooks" returning Workbook
   invoke Workbook "Open" using fileName UpdateLinks returning
workbook
   invoke workbook "GET-worksheets" returning sheets
   invoke sheets "GET-Item" using sheetName returning worksheet
and then
   move 2 to arrayRow
   move 1 to arrayCol
   invoke worksheet "GET-cells" using arrayRow arrayCol returning cell
   invoke cell "SET-Value" using val

and so on

regards, 
Paulo
```

#### ↳ Re: excel from cobol

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2001-11-06T06:16:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0111060616.1991940f@posting.google.com>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
There is an example of this in the Net Express\Base\Demo\oledemos
directory. There are demos for accessing Excel as well as MSWord
through OLE calls.

im4liberty@aol.com (Im4Liberty) wrote in message news:<20011105215718.03573.00001375@mb-mw.aol.com>...
> Hello,
> 
…[9 more quoted lines elided]…
> Bill
```

##### ↳ ↳ Re: excel from cobol

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-06T14:47:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r0XF7.14381$bf1.1737540@news20.bellglobal.com>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com> <260cd566.0111060616.1991940f@posting.google.com>`

```
"Chris Glazier" <chris.glazier@microfocus.com> wrote in message
news:260cd566.0111060616.1991940f@posting.google.com...
> There is an example of this in the Net Express\Base\Demo\oledemos
> directory. There are demos for accessing Excel as well as MSWord
> through OLE calls.
>
> im4liberty@aol.com (Im4Liberty) wrote in message
news:<20011105215718.03573.00001375@mb-mw.aol.com>...
> > Hello,
> >
> > Has anyone ever successfully updated an excel spreadsheet from a
NetExpress
> > COBOL program?   I've been able to "connect" to the spreadsheet via
ODBC, but
> > I'm not sure how to get data into the cells.   INSERT/UPDATE commands
don't
> > seem to work, as I'm not sure what the "table" name is (I tried using
"sheet1"
> > to no avail).   Is there a way to update the 'sheet directly, without
going
> > through ODBC?
> >
> > Any input would be appreciated.
> >
> > Bill

As a related subject to above, does any-one know of a good reference source
for the various MS OLE objects?
```

###### ↳ ↳ ↳ Re: excel from cobol

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-11-07T19:36:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9scp17117r7@enews2.newsguy.com>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com> <260cd566.0111060616.1991940f@posting.google.com> <r0XF7.14381$bf1.1737540@news20.bellglobal.com>`

```

"Donald Tees" <donald_tees@sympatico.ca> wrote in message
news:r0XF7.14381$bf1.1737540@news20.bellglobal.com...
> "Chris Glazier" <chris.glazier@microfocus.com> wrote in
message
> news:260cd566.0111060616.1991940f@posting.google.com...
> > There is an example of this in the Net
Express\Base\Demo\oledemos
> > directory. There are demos for accessing Excel as well as
MSWord
> > through OLE calls.
> >
…[4 more quoted lines elided]…
> > > Has anyone ever successfully updated an excel spreadsheet
from a
> NetExpress
> > > COBOL program?   I've been able to "connect" to the
spreadsheet via
> ODBC, but
> > > I'm not sure how to get data into the cells.
INSERT/UPDATE commands
> don't
> > > seem to work, as I'm not sure what the "table" name is (I
tried using
> "sheet1"
> > > to no avail).   Is there a way to update the 'sheet
directly, without
> going
> > > through ODBC?
…[5 more quoted lines elided]…
> As a related subject to above, does any-one know of a good
reference source
> for the various MS OLE objects?

The online help guides that come with the product, in this case
Excel, details the object model quite well.
```

#### ↳ Re: excel from cobol

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2001-11-06T17:30:19+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9s8vo1$j87$1@usenet.otenet.gr>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
I have never succeeded in using Excel and ODBC together so I switched to OLE
Automation also.

You can see a demo of a Cobol application sending data to Excel (and some
more) in the following address. You are welcome to download anything you
want :

www.syntax.gr/departments/cobolsolutions/files/downloads/demos.htm


regards

Panos



"Im4Liberty" <im4liberty@aol.com> wrote in message
news:20011105215718.03573.00001375@mb-mw.aol.com...
> Hello,
>
> Has anyone ever successfully updated an excel spreadsheet from a
NetExpress
> COBOL program?   I've been able to "connect" to the spreadsheet via ODBC,
but
> I'm not sure how to get data into the cells.   INSERT/UPDATE commands
don't
> seem to work, as I'm not sure what the "table" name is (I tried using
"sheet1"
> to no avail).   Is there a way to update the 'sheet directly, without
going
> through ODBC?
>
> Any input would be appreciated.
>
> Bill
```

##### ↳ ↳ Re: excel from cobol

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-11-07T11:16:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3be86192_4@news.newsgroups.com>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com> <9s8vo1$j87$1@usenet.otenet.gr>`

```
Hmmm... posted 3 times, Panos?

"...Just the place for a Snark,
  That should encourage the crew,
  Just the place for a Snark,
   There, I've said it three times
   What I tell you three times
   Is true."

Lewis Carroll (The Hunting of the Snark)

Don't worry, my mailer screws me every so often too...<G>

Pete.


"Panos Zotos" <pzotos@syntax.gr> wrote in message
news:9s8vo1$j87$1@usenet.otenet.gr...
> I have never succeeded in using Excel and ODBC together so I switched to
OLE
> Automation also.
>
…[19 more quoted lines elided]…
> > COBOL program?   I've been able to "connect" to the spreadsheet via
ODBC,
> but
> > I'm not sure how to get data into the cells.   INSERT/UPDATE commands
…[11 more quoted lines elided]…
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: excel from cobol

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2001-11-13T15:36:04+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9sr7j7$skj$1@usenet.otenet.gr>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com> <9s8vo1$j87$1@usenet.otenet.gr> <3be86192_4@news.newsgroups.com>`

```
Sorry Pete !!!

In fact it is not the mailer but my company's proxy server that does all
these wonderful things.

Panos

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3be86192_4@news.newsgroups.com...
> Hmmm... posted 3 times, Panos?
>
…[20 more quoted lines elided]…
> > You can see a demo of a Cobol application sending data to Excel (and
some
> > more) in the following address. You are welcome to download anything you
> > want :
…[38 more quoted lines elided]…
> -----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

#### ↳ Re: excel from cobol

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2001-11-06T17:30:19+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9s8vpv$jdt$1@usenet.otenet.gr>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
I have never succeeded in using Excel and ODBC together so I switched to OLE
Automation also.

You can see a demo of a Cobol application sending data to Excel (and some
more) in the following address. You are welcome to download anything you
want :

www.syntax.gr/departments/cobolsolutions/files/downloads/demos.htm


regards

Panos



"Im4Liberty" <im4liberty@aol.com> wrote in message
news:20011105215718.03573.00001375@mb-mw.aol.com...
> Hello,
>
> Has anyone ever successfully updated an excel spreadsheet from a
NetExpress
> COBOL program?   I've been able to "connect" to the spreadsheet via ODBC,
but
> I'm not sure how to get data into the cells.   INSERT/UPDATE commands
don't
> seem to work, as I'm not sure what the "table" name is (I tried using
"sheet1"
> to no avail).   Is there a way to update the 'sheet directly, without
going
> through ODBC?
>
> Any input would be appreciated.
>
> Bill
```

#### ↳ Re: excel from cobol

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2001-11-06T17:30:19+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9s8vsg$jfl$1@usenet.otenet.gr>`
- **References:** `<20011105215718.03573.00001375@mb-mw.aol.com>`

```
I have never succeeded in using Excel and ODBC together so I switched to OLE
Automation also.

You can see a demo of a Cobol application sending data to Excel (and some
more) in the following address. You are welcome to download anything you
want :

www.syntax.gr/departments/cobolsolutions/files/downloads/demos.htm


regards

Panos



"Im4Liberty" <im4liberty@aol.com> wrote in message
news:20011105215718.03573.00001375@mb-mw.aol.com...
> Hello,
>
> Has anyone ever successfully updated an excel spreadsheet from a
NetExpress
> COBOL program?   I've been able to "connect" to the spreadsheet via ODBC,
but
> I'm not sure how to get data into the cells.   INSERT/UPDATE commands
don't
> seem to work, as I'm not sure what the "table" name is (I tried using
"sheet1"
> to no avail).   Is there a way to update the 'sheet directly, without
going
> through ODBC?
>
> Any input would be appreciated.
>
> Bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
