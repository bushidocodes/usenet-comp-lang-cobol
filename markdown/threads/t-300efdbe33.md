[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Homework Help

_3 messages · 3 participants · 2001-12_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### COBOL Homework Help

- **From:** KellyTech@techie.com (Kelly Schroeder)
- **Date:** 2001-12-10T13:11:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55021a70.0112101311.30bbe32d@posting.google.com>`

```
I'm using Microfocus Personal COBOL for Win 3.1 with Murach's
Structured COBOL as the textbook.  My assignment (Project 10-1 from
page 762 for any that actually have this book) is to copy a copy
member into a program that validates whether a user inputs a correct
state and corresponding zip code.  The copy member is formated like
this:

01  STATE-TABLE-VALUES.
    05   FILLER    PIC X(12)   VALUE 'AZ1234598765'.

(The VALUE is not exact.)

I'm having problems getting the program to read the .cpy into the
table.  When it compiles, it shows up properly into the code, but I
don't know how to get it from there into the form that I need.  I also
am unsure about what elements I need in everything above the Procedure
division to set up the table and corresponding index.  Generalities in
response are fine.  I don't want any one to do my homework, but I'm
having difficulty with the under-lying principles of tables, indexes
and copy members.  Any help is appreciated.

Kelly Schroeder
```

#### ↳ Re: COBOL Homework Help

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-10T21:37:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dW9R7.53032$C8.3279592@bin4.nnrp.aus1.giganews.com>`
- **References:** `<55021a70.0112101311.30bbe32d@posting.google.com>`

```

"Kelly Schroeder" <KellyTech@techie.com> wrote in message
news:55021a70.0112101311.30bbe32d@posting.google.com...
> I'm using Microfocus Personal COBOL for Win 3.1 with Murach's
> Structured COBOL as the textbook.  My assignment (Project 10-1 from
…[20 more quoted lines elided]…
>

You are aware, of course, that a copy book is of use only at compile time
and, when invoked by the compiler, the resulting situation is as if you had
hand-coded whatever was in the copy book. That is, the copy book itself is
not available at execution time, only what was sucked up by the compiler at
compile time.

That said, pretend you you hand-coded the values found in the copy book and
move them around as you would any other data.

As to what you'll need. You probably need a table. A table is anything with
an OCCURS clause. Like an Excel spreadsheet with one column. Each element in
the table (an Excel row) is referenced by a subscript. For example:

01  MYMONTHS.
   02  THE-MONTH OCCURS 12 PIC X(3).

Presto: a table of twelve entries, each three bytes long. To use:

MOVE 'JanFebMarAprMayJunJulAugSepOctNovDec' TO MYMONTHS.
...
MOVE THE-MONTH(TODAYS-DATE-MONTH) TO PRINT-MONTH

where TODAYS-DATE-MONTH is an integer from 1 through 12.
```

##### ↳ ↳ Re: COBOL Homework Help

- **From:** "ThatGuy" <thatguy@thatguy.net>
- **Date:** 2001-12-14T22:57:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MtvS7.10850$Z24.2863673@typhoon.jacksonville.mediaone.net>`
- **References:** `<55021a70.0112101311.30bbe32d@posting.google.com> <dW9R7.53032$C8.3279592@bin4.nnrp.aus1.giganews.com>`

```

"JerryMouse" <news@bisusa.com> wrote in message
news:dW9R7.53032$C8.3279592@bin4.nnrp.aus1.giganews.com...
>
> "Kelly Schroeder" <KellyTech@techie.com> wrote in message
…[26 more quoted lines elided]…
> and, when invoked by the compiler, the resulting situation is as if you
had
> hand-coded whatever was in the copy book. That is, the copy book itself is
> not available at execution time, only what was sucked up by the compiler
at
> compile time.
>
> That said, pretend you you hand-coded the values found in the copy book
and
> move them around as you would any other data.
>
> As to what you'll need. You probably need a table. A table is anything
with
> an OCCURS clause. Like an Excel spreadsheet with one column. Each element
in
> the table (an Excel row) is referenced by a subscript. For example:
>
…[10 more quoted lines elided]…
>

Sounds like the copy book is just a series of lits which have to be searched
to determine whether state matches zip.  What you need to do is create a
table that redefines it, and use a subscript.
You can then do a PERFORM VARYING to compare whether the zip you're checking
falls within the range provided by the table (coding below spoiler space so
you can try it yourself first).
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.




01  WS-NUMERICS.
       05  STATE-SS                                          PIC 99.

01  WS-SWITCHES.
       05 WS-ZIP-FOUND-SW                           PIC X VALUE 'N'.
             88 ZIP-FOUND                                       VALUE 'Y'.

01  STATE-TABLE-VALUES.
      05 FILLER      PIC X(12) VALUE 'AK9012199999'
      05   FILLER    PIC X(12)   VALUE 'AZ1234512449'.
      05  Etc.

01  WT-STATE-TABLE        REDEFINES STATE-TABLE-VALUES.
      05 WT-STATE-RECS               OCCURS 50 TIMES.
            10 WT-STATE                            PIC XX.
            10 WT-LOW-ZIP                         PIC 9(5).
             10 WT-HIGH-ZIP                        PIC 9(5).

MOVE 'N' TO WS-ZIP-FOUND-SW.
PERFORM XXXX-CHECK-ZIPS
  VARYING STATE-SS FROM 1 BY 1
      UNTIL STATE-SS > 50
         OR ZIP-FOUND.

XXXX-CHECK-ZIPS.
           IF CHK-ZIP NOT < WT-LOW-ZIP(STATE-SS)
            AND CHK-ZIP NOT > WT-HIGH-ZIP(STATE-SS)
              (Do whatever)
               SET ZIP-FOUND TO TRUE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
