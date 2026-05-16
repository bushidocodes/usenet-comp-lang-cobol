[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol for Windows Development

_11 messages · 5 participants · 1999-05_

---

### Cobol for Windows Development

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea5f2$b3610060$4a0870c3@email>`

```
All beta fixes have now been incorporated into Casegen Cobol for Windows
Professional including improved support for Microsoft Access databases.

The "Introductory Price" of $125 (or $50 to upgrade from a paid earlier
release) is still valid and if you are looking to develop or convert to
Windows GUI systems in Cobol this could well be your best development tool
as performance and simplicity are the main design objectives. Full access
is provided to ODBC databases though our point-and-click SQL builder.

Please contact me for more details.

Simon Cordingley
Technical Manager
Casegen Systems Ltd
www.casegen.co.uk
```

#### ↳ Re: Cobol for Windows Development

- **From:** John <jchafin@cgwinc.com>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ich4j$khu$1@nnrp1.deja.com>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email>`

```
Simon,

Tell me more.

John Chafin

In article <01bea5f2$b3610060$4a0870c3@email>,
  "Simon Cordingley" <simon@casegen.co.uk> wrote:
> All beta fixes have now been incorporated into Casegen Cobol for
Windows
> Professional including improved support for Microsoft Access
databases.
>
> The "Introductory Price" of $125 (or $50 to upgrade from a paid
earlier
> release) is still valid and if you are looking to develop or convert
to
> Windows GUI systems in Cobol this could well be your best development
tool
> as performance and simplicity are the main design objectives. Full
access
> is provided to ODBC databases though our point-and-click SQL builder.
>
…[6 more quoted lines elided]…
>


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

##### ↳ ↳ Re: Cobol for Windows Development

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea690$2ba83d20$6b0870c3@email>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com>`

```
Hi John

The Casegen COBOL for Windows Professional product is a Windows development
tool that allows Cobol programs to simply and easily build effective
Windows GUI programs and thir associated logic in Cobol.

Its like "Visual Basic", but simpler and the language used is standard
Cobol, together with our EXEC GUI statements to do things with Windows such
as disable a control on the Windows form or hide a bitmap .

Casegen is very easy to use, we believe the easiest there is. You
just drop controls on the Windows form with the mouse, then add "event"
code in Cobol such as the processing that takes place when a button is
clicked. There are lots of different controls with full support for
dynamically-loaded bitmaps and bitmaps on buttons (and therefore the
appearance of a toolbar).

When you are finished, or think you are, just press one button and Casegen
generates all the Cobol code necessary and loads and runs the program in as
little as one second! Under the covers its compiling and linking the Cobol
using the Fujitsu compilier, version 3 or 4.

The "Professional" product now includes ODBC support. This means that you
can press a single button and import table information from any defined
32-bit ODBC Data Source. You can then build the SQL just by specifying the
Table, Call Type(Select, Insert, Update, Delete or Cursor) and the name of
the Cobol paragraph to generate the SQL call into. The full SQL is then
displayed which you can customise using the mouse. There is full support
for most types of SQL including joins. Even if Casegen cannot build exactly
the SQL you want, it just drops the current SQL into an editor for you to
edit.

Casegen then generates the full SQL for you, you just PERFORM the paragraph
from within event code, checking the results as normal. (The Fujitsu
compiler version 4 converts this "Embedded SQL" into ODBC calls
automatically).

We (and others) have tried Casegen with Microsoft Access, DB2, Sybase SQL
Anywhere and  Microfocus XDB. Of course any ODBC-compliant database should
work OK.

All the EXEC GUI calls are fully documented and mostly have only two or
three parms. All can be copy/pasted out of the help facility into the
Casegen editor which has full Cobol syntax highlighting.

Windows 95/98/NT supported.

Good Points: 
1) Generates the fastest possible Windows application.
2) Easy to use
3) Uses standard Cobol
4) All the power of Fujitsu facilities are available
5) Easy to specify and use SQL/ODBC
6) No restrictions - if we don't support it, you can issue your own Windows
calls until we do!
7) Tried and tested in medium-size applications
8) Very inexpensive
9) Double-click on a generator or compiler error takes you straight to the
line in error
10) High specification Cobol editor.
11) Full Cut/Copy/Paste between the same or other forms
12) Full Cobol subroutine support
13) Supports multiple instances of Casegen
14) No need to understand compile/link command lines
15) Support for DLLs

Bad Points
1) No support for ActiveX controls
2) Not as many controls as VB
3) SQL/ODBC facility requires Fujitsu Version 4 (see www.adtools.com for
ordering details)        

The CD comes with Fujitsu Version 4 (courtesy of Fujitsu) and a 60-day
evaluation copy of SQL Anywhere (courtesy of Sybase), losts of examples and
electronic documentation for $125 including delivery with a money-back
guarantee (less postage costs).

Printed "Getting Started" - add $10.

We have many testamonials available on request. Please send email for
ordering details.


Best regards

Simon Cordingley
simon@casegen.co.uk
Visit our web page at
www.casegen.co.uk


John <jchafin@cgwinc.com> wrote in article <7ich4j$khu$1@nnrp1.deja.com>...
> Simon,
> 
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

- **From:** "David Mowat" <david@dandm.co.nz>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NGv23.9197$vM1.14884@ozemail.com.au>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email>`

```
Does anybody know if MicroFocus is courteous enough to throw in their 32bit
compiler with any products? I would be interested.

Simon Cordingley wrote : The CD comes with Fujitsu Version 4 (courtesy of
Fujitsu)

David.


Simon Cordingley wrote in message <01bea690$2ba83d20$6b0870c3@email>...
>Hi John
>
…[124 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

_(reply depth: 4)_

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea6be$369230a0$3a0870c3@email>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email> <NGv23.9197$vM1.14884@ozemail.com.au>`

```
Correction:

My apologies that should have read:

"The CD comes with Fujitsu Version 3 (courtesy of
 Fujitsu)". 

However, this is still a 32-bit compiler, and is also available with Cobol
books and direct from Fujitsu themselves. 

Version 4 must be purchased from Fujitsu at www.adtools.com.

We are considering providing a version that works with Microfocus
NetExpress.

Simon Cordingley
Casegen Systems Ltd
simon@casegen.co.uk


David Mowat <david@dandm.co.nz> wrote in article
<NGv23.9197$vM1.14884@ozemail.com.au>...
> Does anybody know if MicroFocus is courteous enough to throw in their
32bit
> compiler with any products? I would be interested.
> 
…[9 more quoted lines elided]…
> >The Casegen COBOL for Windows Professional product is a Windows
development
> >tool that allows Cobol programs to simply and easily build effective
> >Windows GUI programs and thir associated logic in Cobol.
> >
> >Its like "Visual Basic", but simpler and the language used is standard
> >Cobol, together with our EXEC GUI statements to do things with Windows
such
> >as disable a control on the Windows form or hide a bitmap .
> >
…[7 more quoted lines elided]…
> >When you are finished, or think you are, just press one button and
Casegen
> >generates all the Cobol code necessary and loads and runs the program in
as
> >little as one second! Under the covers its compiling and linking the
Cobol
> >using the Fujitsu compilier, version 3 or 4.
> >
> >The "Professional" product now includes ODBC support. This means that
you
> >can press a single button and import table information from any defined
> >32-bit ODBC Data Source. You can then build the SQL just by specifying
the
> >Table, Call Type(Select, Insert, Update, Delete or Cursor) and the name
of
> >the Cobol paragraph to generate the SQL call into. The full SQL is then
> >displayed which you can customise using the mouse. There is full support
> >for most types of SQL including joins. Even if Casegen cannot build
exactly
> >the SQL you want, it just drops the current SQL into an editor for you
to
> >edit.
> >
> >Casegen then generates the full SQL for you, you just PERFORM the
paragraph
> >from within event code, checking the results as normal. (The Fujitsu
> >compiler version 4 converts this "Embedded SQL" into ODBC calls
> >automatically).
> >
> >We (and others) have tried Casegen with Microsoft Access, DB2, Sybase
SQL
> >Anywhere and  Microfocus XDB. Of course any ODBC-compliant database
should
> >work OK.
> >
…[12 more quoted lines elided]…
> >6) No restrictions - if we don't support it, you can issue your own
Windows
> >calls until we do!
> >7) Tried and tested in medium-size applications
> >8) Very inexpensive
> >9) Double-click on a generator or compiler error takes you straight to
the
> >line in error
> >10) High specification Cobol editor.
…[13 more quoted lines elided]…
> >evaluation copy of SQL Anywhere (courtesy of Sybase), losts of examples
and
> >electronic documentation for $125 including delivery with a money-back
> >guarantee (less postage costs).
…[15 more quoted lines elided]…
> >John <jchafin@cgwinc.com> wrote in article
<7ich4j$khu$1@nnrp1.deja.com>...
> >> Simon,
> >>
…[15 more quoted lines elided]…
> >> > Windows GUI systems in Cobol this could well be your best
development
> >> tool
> >> > as performance and simplicity are the main design objectives. Full
> >> access
> >> > is provided to ODBC databases though our point-and-click SQL
builder.
> >> >
> >> > Please contact me for more details.
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

- **From:** mgauci@hotmail.com (Ta' Werwer)
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374c0d39.53844456@cnews.newsguy.com>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email>`

```
Do you have a version that works fine with RM/Cobol 85 Win95/NT 32bit
version


On 25 May 1999 10:28:41 +0100, "Simon Cordingley"
<simon@casegen.co.uk> wrote:

>Hi John
>
…[124 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

_(reply depth: 4)_

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea75c$3cf6f540$810870c3@email>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email> <374c0d39.53844456@cnews.newsguy.com>`

```
Not specifically, but the Cobol we generate should work with most compilers
its just a matter of telling us what changes YOU require for your compiler.

We would have to also make adjustments to the display of the compiler error
messages, we need to know the format because you can double-click on them
to take you to the original line in error irrespective of the block of
event code that was typed.

Of course, why not use Fujitsu? Version 3 is free and Version 4 very
inexpensive!

Regards

Simon Cordingley
Casegen Systems Ltd
www.casegen.co.uk

Ta' Werwer <mgauci@hotmail.com> wrote in article
<374c0d39.53844456@cnews.newsguy.com>...
> Do you have a version that works fine with RM/Cobol 85 Win95/NT 32bit
> version
…[7 more quoted lines elided]…
> >The Casegen COBOL for Windows Professional product is a Windows
development
> >tool that allows Cobol programs to simply and easily build effective
> >Windows GUI programs and thir associated logic in Cobol.
> >
> >Its like "Visual Basic", but simpler and the language used is standard
> >Cobol, together with our EXEC GUI statements to do things with Windows
such
> >as disable a control on the Windows form or hide a bitmap .
> >
…[7 more quoted lines elided]…
> >When you are finished, or think you are, just press one button and
Casegen
> >generates all the Cobol code necessary and loads and runs the program in
as
> >little as one second! Under the covers its compiling and linking the
Cobol
> >using the Fujitsu compilier, version 3 or 4.
> >
> >The "Professional" product now includes ODBC support. This means that
you
> >can press a single button and import table information from any defined
> >32-bit ODBC Data Source. You can then build the SQL just by specifying
the
> >Table, Call Type(Select, Insert, Update, Delete or Cursor) and the name
of
> >the Cobol paragraph to generate the SQL call into. The full SQL is then
> >displayed which you can customise using the mouse. There is full support
> >for most types of SQL including joins. Even if Casegen cannot build
exactly
> >the SQL you want, it just drops the current SQL into an editor for you
to
> >edit.
> >
> >Casegen then generates the full SQL for you, you just PERFORM the
paragraph
> >from within event code, checking the results as normal. (The Fujitsu
> >compiler version 4 converts this "Embedded SQL" into ODBC calls
> >automatically).
> >
> >We (and others) have tried Casegen with Microsoft Access, DB2, Sybase
SQL
> >Anywhere and  Microfocus XDB. Of course any ODBC-compliant database
should
> >work OK.
> >
…[12 more quoted lines elided]…
> >6) No restrictions - if we don't support it, you can issue your own
Windows
> >calls until we do!
> >7) Tried and tested in medium-size applications
> >8) Very inexpensive
> >9) Double-click on a generator or compiler error takes you straight to
the
> >line in error
> >10) High specification Cobol editor.
…[13 more quoted lines elided]…
> >evaluation copy of SQL Anywhere (courtesy of Sybase), losts of examples
and
> >electronic documentation for $125 including delivery with a money-back
> >guarantee (less postage costs).
…[15 more quoted lines elided]…
> >John <jchafin@cgwinc.com> wrote in article
<7ich4j$khu$1@nnrp1.deja.com>...
> >> Simon,
> >> 
…[15 more quoted lines elided]…
> >> > Windows GUI systems in Cobol this could well be your best
development
> >> tool
> >> > as performance and simplicity are the main design objectives. Full
> >> access
> >> > is provided to ODBC databases though our point-and-click SQL
builder.
> >> >
> >> > Please contact me for more details.
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

_(reply depth: 5)_

- **From:** mgauci@hotmail.com (Ta' Werwer)
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374d5ecf.63124193@cnews.newsguy.com>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email> <374c0d39.53844456@cnews.newsguy.com> <01bea75c$3cf6f540$810870c3@email>`

```
Thanks for the info.

Is there any chance of acquiring a demo or a trial pack of the
software so that we may evaluate it.

Thanks



On 26 May 1999 10:49:30 +0100, "Simon Cordingley"
<simon@casegen.co.uk> wrote:

>Not specifically, but the Cobol we generate should work with most compilers
>its just a matter of telling us what changes YOU require for your compiler.
…[171 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Cobol for Windows Development

_(reply depth: 6)_

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea844$415b5660$030870c3@email>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <7ich4j$khu$1@nnrp1.deja.com> <01bea690$2ba83d20$6b0870c3@email> <374c0d39.53844456@cnews.newsguy.com> <01bea75c$3cf6f540$810870c3@email> <374d5ecf.63124193@cnews.newsguy.com>`

```
I am sorry, the price is so low ($125) that we cannot afford to do this
although we hope to have a sharware version sometime in the future that can
be downloaded from our web site.

Ta' Werwer <mgauci@hotmail.com> wrote in article
<374d5ecf.63124193@cnews.newsguy.com>...
> Thanks for the info.
> 
…[10 more quoted lines elided]…
> >Not specifically, but the Cobol we generate should work with most
compilers
> >its just a matter of telling us what changes YOU require for your
compiler.
> >
> >We would have to also make adjustments to the display of the compiler
error
> >messages, we need to know the format because you can double-click on
them
> >to take you to the original line in error irrespective of the block of
> >event code that was typed.
…[26 more quoted lines elided]…
> >> >Its like "Visual Basic", but simpler and the language used is
standard
> >> >Cobol, together with our EXEC GUI statements to do things with
Windows
> >such
> >> >as disable a control on the Windows form or hide a bitmap .
> >> >
> >> >Casegen is very easy to use, we believe the easiest there is. You
> >> >just drop controls on the Windows form with the mouse, then add
"event"
> >> >code in Cobol such as the processing that takes place when a button
is
> >> >clicked. There are lots of different controls with full support for
> >> >dynamically-loaded bitmaps and bitmaps on buttons (and therefore the
…[4 more quoted lines elided]…
> >> >generates all the Cobol code necessary and loads and runs the program
in
> >as
> >> >little as one second! Under the covers its compiling and linking the
…[5 more quoted lines elided]…
> >> >can press a single button and import table information from any
defined
> >> >32-bit ODBC Data Source. You can then build the SQL just by
specifying
> >the
> >> >Table, Call Type(Select, Insert, Update, Delete or Cursor) and the
name
> >of
> >> >the Cobol paragraph to generate the SQL call into. The full SQL is
then
> >> >displayed which you can customise using the mouse. There is full
support
> >> >for most types of SQL including joins. Even if Casegen cannot build
> >exactly
> >> >the SQL you want, it just drops the current SQL into an editor for
you
> >to
> >> >edit.
…[13 more quoted lines elided]…
> >> >All the EXEC GUI calls are fully documented and mostly have only two
or
> >> >three parms. All can be copy/pasted out of the help facility into the
> >> >Casegen editor which has full Cobol syntax highlighting.
…[14 more quoted lines elided]…
> >> >9) Double-click on a generator or compiler error takes you straight
to
> >the
> >> >line in error
…[10 more quoted lines elided]…
> >> >3) SQL/ODBC facility requires Fujitsu Version 4 (see www.adtools.com
for
> >> >ordering details)        
> >> >
> >> >The CD comes with Fujitsu Version 4 (courtesy of Fujitsu) and a
60-day
> >> >evaluation copy of SQL Anywhere (courtesy of Sybase), losts of
examples
> >and
> >> >electronic documentation for $125 including delivery with a
money-back
> >> >guarantee (less postage costs).
> >> >
…[31 more quoted lines elided]…
> >> >> > release) is still valid and if you are looking to develop or
convert
> >> >> to
> >> >> > Windows GUI systems in Cobol this could well be your best
> >development
> >> >> tool
> >> >> > as performance and simplicity are the main design objectives.
Full
> >> >> access
> >> >> > is provided to ODBC databases though our point-and-click SQL
…[17 more quoted lines elided]…
>
```

#### ↳ Re: Cobol for Windows Development

- **From:** SiD <sdawson@netspace.net.au>
- **Date:** 1999-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374EAB4D.9FCF1823@netspace.net.au>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email>`

```
Simon,

    Can we still use our existing Oracle databases? i.e. is it compatible with
Oracle?

    And, is the code converted completely or is a certain amount of "tweaking"
of the new code required?

Simon

Simon Cordingley wrote:

> All beta fixes have now been incorporated into Casegen Cobol for Windows
> Professional including improved support for Microsoft Access databases.
…[12 more quoted lines elided]…
> www.casegen.co.uk
```

##### ↳ ↳ Re: Cobol for Windows Development

- **From:** "Simon Cordingley" <simon@casegen.co.uk>
- **Date:** 1999-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bea9af$762d3e00$b40870c3@casegen.casegen.co.uk>`
- **References:** `<01bea5f2$b3610060$4a0870c3@email> <374EAB4D.9FCF1823@netspace.net.au>`

```
Hi Simon

One of our customers uses Oracle in our batch product,  but we have not
tried it with Casegen Cobol for Windows Professional. Fujitsu Version 4
documentation says that it is supported and as we generate and compile
using Fujitsu - it should work.

From my little knowledge of Oracle, I believe there is two choices -
(please let me know if I am wrong anybody):

1) Use the Oracle precompiler to convert EXEC SQL statements to cobol
statements and calls to an Oracle stub, then compile with Fujitsu then link
with the stub. We already do this with CICS, and we have experience of
doing this with DB2.
2) Use ODBC with Oracle just another 32-bit data source. However, who
provides the 32-bit ODBC driver? In this situation, we do not even know
that the database is Oracle - its just another ODBC database.

Option 2 will just work with Casegen provided the ODBC driver follows the
rules. Option 1 would require the precompiler presumably supplied by
Oracle. We would have to make some small changes in our build process
(automatic generate/compile/link) but we have allowed for this in the
design with configuration files.   

If you are converting an old application to GUI, it would be normal to cut
and paste blocks of code directly into the Casegen event code. Subroutines
are just reused without change. The important thing to understand is to
make sure you get the design right!

Fujitsu seems very flexible, so it should handle most variants of the
standard, depending upon your existing compiler.

Hope this helps.

Best regards

Simon Cordingley

SiD <sdawson@netspace.net.au> wrote in article
<374EAB4D.9FCF1823@netspace.net.au>...
> Simon,
> 
>     Can we still use our existing Oracle databases? i.e. is it compatible
with
> Oracle?
> 
>     And, is the code converted completely or is a certain amount of
"tweaking"
> of the new code required?
> 
…[4 more quoted lines elided]…
> > All beta fixes have now been incorporated into Casegen Cobol for
Windows
> > Professional including improved support for Microsoft Access databases.
> >
> > The "Introductory Price" of $125 (or $50 to upgrade from a paid earlier
> > release) is still valid and if you are looking to develop or convert to
> > Windows GUI systems in Cobol this could well be your best development
tool
> > as performance and simplicity are the main design objectives. Full
access
> > is provided to ODBC databases though our point-and-click SQL builder.
> >
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
