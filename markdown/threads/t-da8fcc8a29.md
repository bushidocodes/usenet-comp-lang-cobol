[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Month table??? kinda long

_6 messages · 5 participants · 2001-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Month table??? kinda long

- **From:** "Seekers462" <Seekers462@hotmail.com>
- **Date:** 2001-04-02T21:25:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net>`

```

I am trying to write a program that has a month table as an embedded table.
Ex:
02                                   PICX(3) VALUE "JAN".
Etc....
up to the Dec listed in the table.
The table then has this below:
01 MONTH-TABLE REDEFINES MONTH-TABLE-DATA.
     02 MT-MONTH OCCURS  12 TIMES           PIC X(3).

I am trying to insert the month written out onto my output file as follows:
DD-MMM-YYYY.

The date is gathered from an input record and also have it listed in my
working storage area.

I need some ideas as to how to subscript it into an acceptable data that
will print out on paper. My teacher said to break it down within my input
file which is listed as follows:

01  CUSTOMER-RECORD.
      02  CR-DATE-PURCH                                  PIC9(8).

I am suppose to break the date down and include the subscript here but am
not clear on how to do it. The date on the dat file is listed as MMDDYYYY. I
can do the day part and the year part but how do I subscript the month? Does
it need to be done here or in another part? Any suggestions? Our book only
shows how to display on screen not write. Any help would be appreciated...

: )
```

#### ↳ Re: Month table??? kinda long

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-04-02T22:52:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ssshctsavb45j4thdjf2uqncs1b94p2jt9@4ax.com>`
- **References:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net>`

```
ghItlh "Seekers462" <Seekers462@hotmail.com> 

>
>I am trying to write a program that has a month table as an embedded table.
…[27 more quoted lines elided]…
>: )

I'm not sure why you couldn't do:

01 CUSTOMER-RECORD.
   02 CR-DATE-PURCH.
      03 CR-DATE-PURCH-MM   PIC 99.
      03 CR-DATE-PURCH-DD   PIC 99.
      03 CR-DATE-PURCH-YYYY PIC 9999.

or if you absolutely must keep CR-DATE-PURCH as a display numeric
type:

01 CUSTOMER-RECORD.
   02 CR-DATE-PURCH PIC 9(8).
   02 CR-DATE-PURCH-MMDDYYYY redefines CR-DATE-PURCH.
      03 CR-DATE-PURCH-MM   PIC 99.
      03 CR-DATE-PURCH-DD   PIC 99.
      03 CR-DATE-PURCH-YYYY PIC 9999.

then you can use CR-DATE-PURCH-MM as a subscript for your table.

It might also be good if you did numeric first, and then range checks
second on these values in case you have something stupid on your file;
You don't want a S0C4 or whatever you might get from an out of bounds
table access on your platform.
```

##### ↳ ↳ Re: Month table??? kinda long

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-04-03T01:16:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cw9y6.212$jz.15685@www.newsranger.com>`
- **References:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net> <ssshctsavb45j4thdjf2uqncs1b94p2jt9@4ax.com>`

```
Adding to what qIroS wrote, you might want to rename or redefine
CR-DATE-PURCH-MM again to something more manageable, like MSUB, or move it to
another field called MSUB. It makes the subscripted moves, etc. less cumbersome.


Jack 



In article <ssshctsavb45j4thdjf2uqncs1b94p2jt9@4ax.com>, qIroS says...
>
>ghItlh "Seekers462" <Seekers462@hotmail.com> 
…[56 more quoted lines elided]…
>
```

#### ↳ Re: Month table??? kinda long

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-02T22:33:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC8FDD8.E52E25B3@home.com>`
- **References:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net>`

```


Seekers462 wrote:

> I am trying to write a program that has a month table as an embedded table.
> Ex:
…[24 more quoted lines elided]…
> shows how to display on screen not write. Any help would be appreciated...

As suggested in the earlier reply you could breakdown the reference to the date
into d/m/y levels. But where you are really stuck is comprehending tables -
isn't it.
So two variations on a theme :-

01 MonthTable1 pic x(36) value "JanFebMarAprMayJunJulAugSepOctNovDec".
01 MonthTable2 redefines MonthTable1.
    05 MonthName occurs 12 pic x(03)..

OR :-

01 MonthTable1.
    05 pic x(03) value "Jan".
    05 pic x(03) value  "Feb"
    05 pic x.......
    05 ........
    05 pic x(03) value "Dec".
01 MonthTable2 redefines MonthTable1.
    05 MonthName occurs 12 pic x(03)..

Obviously the first is quicker - shorthand. But if using the first it can get a
little misleading, if you are using numerics. Use commas, colons, semi-colons,
exclamation marks or whatever, so your eye can visually split the values.

01 PayRate1 pic x(24) value "10.50,11.50,12.50,13.50,".
01 PayRate2 redefines PayRate1.
     05 Rate occurs 4.
          10 HourlyRate pic 99.99.
           10 filler           pic x.            *> You don't give a damn what's
in this pic x

So back to your date problem. Good idea to do what is referred to as Xtreme
Programming (1) is the input-date numeric - if No do something (2) is the Month
between 1 and 12 - if No do something.

Given you've got a valid month :

    If your input date is '03292001' then :-

    move MonthName (CR-PURCH-MONTH) to ............, which is
   ( move MonthName (03) to .........)

Your book will actually tell you more than you think <G> - you haven't latched
on to the words to search for. Check the index for TABLES, (Arrays in other
languages), and SUBSCRIPTS/SUBSCRIPTING.

Jimmy, Calgary AB
```

#### ↳ Re: Month table??? kinda long

- **From:** awkisall <awkisall@qwest.net>
- **Date:** 2001-04-02T23:55:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC973F9.32250735@qwest.net>`
- **References:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net>`

```
A simple month array might go:

01 WS-MONTH-ARRAY.
    05 FILLER         PIC X(03)   VALUE  'JAN'
    05 FILLER         PIC X(03)   VALUE  'FEB'
      .
      .
      .
    05 FILLER         PIC X(03)   VALUE  'DEC'
01 WS-MONTH-ARRAY-R   REDEFINES WS-MONTH-ARRAY.
    05 WS-MONTH       PIC X(03) OCCURS 12.

To subscript make a working-storage item (MONTH-SUB?) that can handle the
occurances, ideally with a binary halfword pic.

To re-arrange input dates break them down into 03 (preferably 15) level elements
FD-MM
                   FD-DD
                   FD-CCYY

then move these elements to elements of an WS field with elements under an 01
level layed out as WS-DD
                                        WS-MM
                                        WS-CCYYY
(they need unique identifiers).

You might not need this intermediate step, but...

then use your month array and your FD or re-arranged WS date field to populate
another (your) DD-MMM-YYYY output field, once again moving element to element
under an 01.

MOVE WS-MM                  TO WS-MONTH-SUB

MOVE WS-DD                  TO OT-DD
MOVE WS-MONTH (MONTH-SUB)   TO OT-MMM
MOVE WS-CCYY                TO OT-CCYY








Seekers462 wrote:

> I am trying to write a program that has a month table as an embedded table.
> Ex:
…[29 more quoted lines elided]…
> others here for?
```

#### ↳ Re: Month table??? kinda long

- **From:** "Seekers462" <Seekers462@hotmail.com>
- **Date:** 2001-04-03T17:41:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hXny6.9198$RF1.591066@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<m76y6.6388$rk4.483742@bgtnsc04-news.ops.worldnet.att.net>`

```
Thanks to all that replied..will try the various methods suggested and see
what works best...thanks...
: )
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
