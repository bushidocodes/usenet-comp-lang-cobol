[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please help me!

_14 messages · 8 participants · 2001-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Please help me!

- **From:** "Antoine Daccache" <oahfei@home.com>
- **Date:** 2001-04-13T03:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com>`

```
Hi,

    I am currently writing a program for my COBOL programming class and I am
stuck on the a 'small' mistake (hopefully ;). I am dying for someone to help
me because I have gone over the code MANY times...about 1 hour's worth...I
am just horrible in COBOL...basically my problem is that the
'date-page-line' is currently NOT displaying on the screen, and I have no
idea why! Please help me, I know it's something stupid on my part :(

Thank you
Antoine daccache

----------------------------------------------------------------------------
--------------------------------------------------------------

       IDENTIFICATION DIVISION.
       PROGRAM-ID. RECORD-DISPLAY.



       DATA DIVISION.

       WORKING-STORAGE SECTION.


       01 DATE-PAGE-LINE.
           10  FILLER                   PIC X(6) VALUE "Date:".
           10  RUN-MONTH-DISPLAY-VALUE  PIC X(10).
           10  RUN-DAY-DISPLAY-VALUE    PIC Z9.
           10  FILLER                   PIC X VALUE "/".
           10  RUN-YEAR-DISPLAY-VALUE   PIC 9(4).
           10  FILLER                   PIC X(50).
           10  FILLER                   PIC X(6) VALUE "Page:".

       01 CUSTOMER-SALES-REPORT-LINE.
           10  FILLER                   PIC X(33).
           10  FILLER                   PIC X(47)
                        VALUE "Customer Sales Report".

       01 TEMP-VALUES.
           10 RUN-DATE.
              15 RUN-YEAR          PIC 99.
              15 RUN-MONTH         PIC 99.
              15 RUN-DAY           PIC 99.

           10 CENTURY              PIC 9(4) VALUE 2000.

           10  RUN-MONTH-TABLE     OCCURS 12 TIMES.
               15  JAN                   PIC X(8) VALUE "January".
               15  FEB                   PIC X(9) VALUE "February".
               15  MAR                   PIC X(6) VALUE "March".
               15  APR                   PIC X(6) VALUE "April".
               15  MAY                   PIC X(4) VALUE "May".
               15  JUN                   PIC X(5) VALUE "June".
               15  JUL                   PIC X(5) VALUE "July".
               15  AUG                   PIC X(7) VALUE "August".
               15  SEP                   PIC X(10) VALUE "September".
               15  OCT                   PIC X(8) VALUE "October".
               15  NOV                   PIC X(9) VALUE "November".
               15  DEC                   PIC X(9) VALUE "December".


       PROCEDURE DIVISION.

       000-RECORD-DISPLAY.
           PERFORM 100-INITIALIZE
           PERFORM 200-DISPLAY-HEADINGS
           STOP RUN.

       100-INITIALIZE.
           ACCEPT RUN-DATE FROM DATE
           MOVE RUN-MONTH-TABLE(RUN-DAY) TO RUN-MONTH-DISPLAY-VALUE
           MOVE RUN-DAY TO RUN-DAY-DISPLAY-VALUE
           MOVE RUN-YEAR TO RUN-YEAR-DISPLAY-VALUE
           ADD CENTURY TO RUN-YEAR-DISPLAY-VALUE
           DISPLAY " ", ERASE.

       200-DISPLAY-HEADINGS.
           DISPLAY DATE-PAGE-LINE
           DISPLAY " "
           DISPLAY CUSTOMER-SALES-REPORT-LINE.
```

#### ↳ Re: Please help me!

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-04-12T22:56:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b5tef$49a8$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com>`

```
>            MOVE RUN-MONTH-TABLE(RUN-DAY) TO RUN-MONTH-DISPLAY-VALUE
You appear to be using "day of month" as a subscript to your month table.
Don't you want to use "month" for this?
```

##### ↳ ↳ Re: Please help me!

- **From:** "Antoine Daccache" <oahfei@home.com>
- **Date:** 2001-04-13T19:32:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rvIB6.1788$5E3.898373@news3.rdc1.on.home.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <9b5tef$49a8$1@newssvr05-en0.news.prodigy.com>`

```
Yep, your right, I changed that and now it still isin't working....I ran my
debuger and it's showing that line...but clearnign RIGHT after, even if
'CUSTOMER-SALES-REPORT-LINE' isin't there...and even if there's no more line
of code after...that's what my problem is...I see no reason why it should do
that, and I even checked the width of my "data-page-line" table and it
dosen't exceed the monitor width...I am stuck :(

Thanks,
Antoine Daccache


"Terry Heinze" <terryheinze@prodigy.net> wrote in message
news:9b5tef$49a8$1@newssvr05-en0.news.prodigy.com...
> >            MOVE RUN-MONTH-TABLE(RUN-DAY) TO RUN-MONTH-DISPLAY-VALUE
> You appear to be using "day of month" as a subscript to your month table.
…[10 more quoted lines elided]…
> >     I am currently writing a program for my COBOL programming class and
I
> am
> > stuck on the a 'small' mistake (hopefully ;). I am dying for someone to
> help
> > me because I have gone over the code MANY times...about 1 hour's
worth...I
> > am just horrible in COBOL...basically my problem is that the
> > 'date-page-line' is currently NOT displaying on the screen, and I have
no
> > idea why! Please help me, I know it's something stupid on my part :(
> >
…[78 more quoted lines elided]…
>
```

#### ↳ Re: Please help me!

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-04-13T04:28:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com>`

```
Does the "customer-sales-report-line" show up the screen?

If it does, there is the possibility that the 
"customer-sales-report-line" is being written over the 
"date-page-line". You can see if this is the case by not displaying 
the "customer-sales-report-line".

Lorne

On Fri, 13 Apr 2001 03:36:37, "Antoine Daccache" <oahfei@home.com> 
wrote:

> Hi,
> 
…[81 more quoted lines elided]…
> 
```

##### ↳ ↳ Re: Please help me!

- **From:** "Antoine Daccache" <oahfei@home.com>
- **Date:** 2001-04-13T19:33:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%vIB6.1796$5E3.900066@news3.rdc1.on.home.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver>`

```
I ran my debuger and it's showing that line...but clearnign RIGHT after,
even if 'CUSTOMER-SALES-REPORT-LINE' isin't there...and even if there's no
more line of code after...that's what my problem is...I see no reason why it
should do that, and I even checked the width of my "data-page-line" table
and it dosen't exceed the monitor width...I am stuck :(

Thanks,
Antoine Daccache

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver...
> Does the "customer-sales-report-line" show up the screen?
>
…[12 more quoted lines elided]…
> >     I am currently writing a program for my COBOL programming class and
I am
> > stuck on the a 'small' mistake (hopefully ;). I am dying for someone to
help
> > me because I have gone over the code MANY times...about 1 hour's
worth...I
> > am just horrible in COBOL...basically my problem is that the
> > 'date-page-line' is currently NOT displaying on the screen, and I have
no
> > idea why! Please help me, I know it's something stupid on my part :(
> >
…[4 more quoted lines elided]…
> --------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Please help me!

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-04-13T15:17:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b7mse$jmj$1@slb2.atl.mindspring.net>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver> <%vIB6.1796$5E3.900066@news3.rdc1.on.home.com>`

```
You haven't told us which COBOL compiler you are using - so the following
may or may not work.  Some compilers have as an extension (not "standard")
the ability to specify where you want your display to show up.

Try for example changing your code to:

> > >        200-DISPLAY-HEADINGS.
> > >            DISPLAY DATE-PAGE-LINE
                          At Line 1 Column 1
> > >            DISPLAY " "
                          At Line 2 Column 1
> > >            DISPLAY CUSTOMER-SALES-REPORT-LINE
                          At Line 3 Column 1.
> > >
```

###### ↳ ↳ ↳ Re: Please help me!

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-04-13T20:58:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-3O2tdjKYYs3D@tcpserver>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver> <%vIB6.1796$5E3.900066@news3.rdc1.on.home.com>`

```
The subscript you are using to obtain the transated month is "RUN-DAY"
If the day of the month is more than 12 you will get some arbitrary 
piece of 
binary data rather than the discription from your table. You should 
use
the run-month not the run-day

Also, the run-month-table is not constructed properly. The table
should be an element that occurs 12 times with all being the same 
size.
This table should "REDEFINE" a table of literals with the months in 
them.

10 table-of-literals
  15 filler pic x(10) value "january"
  15 filler pic x(10) value "february"
  15 filler pic x(10) value "march"
(etc etc)
10  run-month-table redefines table-of-literals occurs 12 pic x(10)

Lorne


On Fri, 13 Apr 2001 19:33:15, "Antoine Daccache" <oahfei@home.com> 
wrote:

> I ran my debuger and it's showing that line...but clearnign RIGHT after,
> even if 'CUSTOMER-SALES-REPORT-LINE' isin't there...and even if there's no
…[116 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: Please help me!

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-04-14T00:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wfNB6.975$DW1.48592@iad-read.news.verio.net>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver> <%vIB6.1796$5E3.900066@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-3O2tdjKYYs3D@tcpserver>`

```
In article <ZpzG4UNLyRNq-pn2-3O2tdjKYYs3D@tcpserver>,

[snippage]

>Also, the run-month-table is not constructed properly. The table
>should be an element that occurs 12 times with all being the same 
…[9 more quoted lines elided]…
>10  run-month-table redefines table-of-literals occurs 12 pic x(10)

Hmmmmm... it may be a matter of style, of course, but I disagree; what
you've coded here would result in statements like

MOVE RUN-MONTH-TABLE (MO-NUM) TO HDR-LIN02-MO-LIT.

... or something like that.  The Decent, Good and True way to address this
would be:

10  MO-TBL.
    15  FILLER PIC X(10) VALUE 'JANUARY   '.
    15  FILLER PIC X(10) VALUE 'FEBRUARY  '.
et und cetera
10  MO-LIT REDEFINES MO-TBL OCCURS 12 PIC X(10).

... resulting in Honest, Proper and Maintainable code like:

MOVE MO-LIT (MO-NUM) TO HDR-LIN02-MO-LIT.

DD
```

###### ↳ ↳ ↳ Re: Please help me!

_(reply depth: 5)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-04-14T15:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-f2rRK1wWQM7m@tcpserver>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-KnZTVd9RXfk1@tcpserver> <%vIB6.1796$5E3.900066@news3.rdc1.on.home.com> <ZpzG4UNLyRNq-pn2-3O2tdjKYYs3D@tcpserver> <wfNB6.975$DW1.48592@iad-read.news.verio.net>`

```
On Sat, 14 Apr 2001 00:57:00, docdwarf@clark.net (  NA) wrote:

> In article <ZpzG4UNLyRNq-pn2-3O2tdjKYYs3D@tcpserver>,
> 
…[34 more quoted lines elided]…
> 

A rose by any other name ... :-)
```

#### ↳ Re: Please help me!

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-13T13:19:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1DB6.567967$f36.16914694@news20.bellglobal.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com>`

```
I'd suggest that you are indeed displaying DATA-LINE-PAGE.  However, within
milliseconds, you are also erasing it again, and then stopping.

"Antoine Daccache" <oahfei@home.com> wrote in message
news:9vuB6.90390$XV.23908100@news3.rdc1.on.home.com...
> Hi,
>
>     I am currently writing a program for my COBOL programming class and I
am
> stuck on the a 'small' mistake (hopefully ;). I am dying for someone to
help
> me because I have gone over the code MANY times...about 1 hour's worth...I
> am just horrible in COBOL...basically my problem is that the
…[6 more quoted lines elided]…
> --------------------------------------------------------------------------
```

##### ↳ ↳ Re: Please help me!

- **From:** "Antoine Daccache" <oahfei@home.com>
- **Date:** 2001-04-13T19:32:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UuIB6.1781$5E3.897897@news3.rdc1.on.home.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <e1DB6.567967$f36.16914694@news20.bellglobal.com>`

```
Yep, you are right, I ran my debuger and figured that out...but is there any
way to prevent it from 'clearing' the screen again?

Thank you
Antoine D.

"Donald Tees" <donald_tees@sympatico.ca> wrote in message
news:e1DB6.567967$f36.16914694@news20.bellglobal.com...
> I'd suggest that you are indeed displaying DATA-LINE-PAGE.  However,
within
> milliseconds, you are also erasing it again, and then stopping.
>
…[4 more quoted lines elided]…
> >     I am currently writing a program for my COBOL programming class and
I
> am
> > stuck on the a 'small' mistake (hopefully ;). I am dying for someone to
> help
> > me because I have gone over the code MANY times...about 1 hour's
worth...I
> > am just horrible in COBOL...basically my problem is that the
> > 'date-page-line' is currently NOT displaying on the screen, and I have
no
> > idea why! Please help me, I know it's something stupid on my part :(
> >
…[78 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help me!

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-13T21:27:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mbKB6.572347$Pm2.9244869@news20.bellglobal.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <e1DB6.567967$f36.16914694@news20.bellglobal.com> <UuIB6.1781$5E3.897897@news3.rdc1.on.home.com>`

```
The traditional way is something along the line of:

    DISPLAY SHOW-SOMETHING.
    DISPLAY "Type any key to continue ..." WITH NO ADVANCING.
    ACCEPT ANY-PIC-X.
    DISPLAY CLEAR-SCREEN-MY-COPYRIGHT.
    GOBACK.

"Antoine Daccache" <oahfei@home.com> wrote in message
news:UuIB6.1781$5E3.897897@news3.rdc1.on.home.com...
> Yep, you are right, I ran my debuger and figured that out...but is there
any
> way to prevent it from 'clearing' the screen again?
>
…[13 more quoted lines elided]…
> > >     I am currently writing a program for my COBOL programming class
and
> I
> > am
> > > stuck on the a 'small' mistake (hopefully ;). I am dying for someone
to
> > help
> > > me because I have gone over the code MANY times...about 1 hour's
…[87 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Please help me!

_(reply depth: 4)_

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-04-14T01:32:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oMNB6.5897$FY5.448895@www.newsranger.com>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com> <e1DB6.567967$f36.16914694@news20.bellglobal.com> <UuIB6.1781$5E3.897897@news3.rdc1.on.home.com> <mbKB6.572347$Pm2.9244869@news20.bellglobal.com>`

```
Hi Antoine,

Someone mentioned you were using the wrong subscript to move the month text to
your display field. This could explain why the displays are misbehaving. If the
wrong values are moved to the text of the msg they can be interpreted as
terminal control characters and the system will attempt to execute them, causing
God knows what problems. 

Hope this helps, Jack.



In article <mbKB6.572347$Pm2.9244869@news20.bellglobal.com>, Donald Tees says...
>
>The traditional way is something along the line of:
…[123 more quoted lines elided]…
>
```

#### ↳ Re: Please help me!

- **From:** "David de Jongh" <ddejongh@worldnet.att.net>
- **Date:** 2001-04-22T20:03:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cOGE6.30971$RF1.2593514@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<9vuB6.90390$XV.23908100@news3.rdc1.on.home.com>`

```
You have defined your month table as occurring twelve times.  It should be a
redefines:
01 A.
  05 filler pic x(n) value 'first value'
  05 filler ....                 'second value'
etc.
01 table redefines A.
   05  month-entry   pic x(n) occurs 12 times.

Also, you are subscripting the month table with the day number, instead of
the month number.
Are you saying that the whole line displays as blanks, or that is just
displays the month incorrectly? YOu should be seeing the "Date:" string.
Also, why are you hard-coding the century?  Use ACCEPT DATE YYYYMMDD
instead.

D de J

"Antoine Daccache" <oahfei@home.com> wrote in message
news:9vuB6.90390$XV.23908100@news3.rdc1.on.home.com...
> Hi,
>
>     I am currently writing a program for my COBOL programming class and I
am
> stuck on the a 'small' mistake (hopefully ;). I am dying for someone to
help
> me because I have gone over the code MANY times...about 1 hour's worth...I
> am just horrible in COBOL...basically my problem is that the
…[6 more quoted lines elided]…
> --------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
