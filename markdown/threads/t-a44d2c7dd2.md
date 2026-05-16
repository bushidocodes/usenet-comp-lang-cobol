[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Power Cobol (OCX)

_5 messages · 3 participants · 2002-07_

---

### Power Cobol (OCX)

- **From:** Carlos Lages <clages@attglobal.net>
- **Date:** 2002-07-13T22:58:11-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D30DAB3.D2799384@attglobal.net>`

```
Hi, Its me again

I did an Ocx ( a Forms ) that contains only one field
   in this field  i check  everything i need, and dblclick  open a
Browse where
  the user can select one of them.
   this OCX  works  with a File  (read )
   testing it alone Works  fine.

When I put  this OCX Forms inside another Forms
 i got the following  situation
  Dblclick  doesnt  Work ( I got Ilegal  function call)
  And how can i move the field of the  OCX  to  a Field  of the main
Forms?

any help ?

Tks

Carlos lages
```

#### ↳ Re: Power Cobol (OCX)

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-15T02:44:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KGqY8.89433$iB1.5150417@bin4.nnrp.aus1.giganews.com>`
- **References:** `<3D30DAB3.D2799384@attglobal.net>`

```

"Carlos Lages" <clages@attglobal.net> wrote in message
news:3D30DAB3.D2799384@attglobal.net...
> Hi, Its me again
>
…[14 more quoted lines elided]…
>

Did you:

REGSVR32 module-name

OCXs must be registered.

Also, why an OCX? Why not just another form?
```

##### ↳ ↳ Re: Power Cobol (OCX)

- **From:** Carlos Lages <clages@attglobal.net>
- **Date:** 2002-07-15T13:45:10-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D32FC16.8A6599D9@attglobal.net>`
- **References:** `<3D30DAB3.D2799384@attglobal.net> <KGqY8.89433$iB1.5150417@bin4.nnrp.aus1.giganews.com>`

```
Did you:

REGSVR32 module-name , yes, i did, remember , the OCX works fine
exeption in the case below.

I am trying an OCX because I can not Put on Forms inside Other, only
  changing this forms to an OCX ( thats what i am trying to do)

Carlos Lages


JerryMouse gravada:

> "Carlos Lages" <clages@attglobal.net> wrote in message
> news:3D30DAB3.D2799384@attglobal.net...
…[24 more quoted lines elided]…
> Also, why an OCX? Why not just another form?
```

###### ↳ ↳ ↳ Re: Power Cobol (OCX)

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-15T22:00:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hCHY8.121454$iX5.5795840@bin3.nnrp.aus1.giganews.com>`
- **References:** `<3D30DAB3.D2799384@attglobal.net> <KGqY8.89433$iB1.5150417@bin4.nnrp.aus1.giganews.com> <3D32FC16.8A6599D9@attglobal.net>`

```

"Carlos Lages" <clages@attglobal.net> wrote in message
news:3D32FC16.8A6599D9@attglobal.net...
> Did you:
>
…[6 more quoted lines elided]…
> Carlos Lages

Sure you can. Inside the called form you'll have:

MOVE 'TEXT' OF MYFIELD TO DATANAME.

Where

01  DATANAME   PIC X(30) GLOBAL EXTERNAL.

in Working-Storage for both forms.

In fact, the called form doesn't even have to be visible (obviously the
called form must be visible for your application). It gets loaded, does it's
thing (maybe retrieve a record), and goes away.
```

#### ↳ Re: Power Cobol (OCX)

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2002-07-15T02:06:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0207150106.9b9717d@posting.google.com>`
- **References:** `<3D30DAB3.D2799384@attglobal.net>`

```
Carlos Lages <clages@attglobal.net> wrote in message news:<3D30DAB3.D2799384@attglobal.net>...
> Hi, Its me again
> 
…[17 more quoted lines elided]…
> Carlos lages


Let's assume that I have a single field Form called "Customer" which
has a text field in it. That form by itself will use another OCX
control wich takes care of Database access for the customers table(s).
This Form ("Customer") will have at least 2 propreties: ID, Code, (and
probably Name).
Whenever a user inputs something in the field, the code in the form
will:
- Validate input for format
- Validate input against the Database using the DbAccess OCX
- Fill in the properties if aplicable
- Fire the "Customer_Changed" custom event

In the containing Form, I will write code to handle that event.

My reasons:
The visual object "Customer" will be used whenever a form needs it. 
Using it as an OCX instead of an OLE server let's me trap the events
of the OCX, something I can't do with an OLE server (invoked as such).
Using properties instead of method parameters is easier because every
time a new field is required, I don't have to recompile all the other
modules that use that interface; only the ones that will use the new
field.
If I, later, decide to add funcionality to the "Customer" Form (adding
help for instance, or a "browse" form to pickup customers based on
some strange criteria), that funcionality will be available to all
Forms that already use the "Customer" Form.

regards

Paulo Vieira, Emporsoft
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
