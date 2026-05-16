[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inserting into a table

_11 messages · 8 participants · 2000-06_

---

### Inserting into a table

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393BB313.77353D33@cusys.edu>`

```
I have a sorted table and want to insert a field into it.  There are
several ways to do this, including using reference modification of a
redefines to bump the table up.

But this, while being efficient, is maintenance unfriendly.  What method
do you guys recommend?
```

#### ↳ Re: Inserting into a table

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NrV_4.1255$Hs5.167625@dfiatx1-snr1.gtei.net>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Instead of reference modifying, why not use an extra index...

01  FILLER
   05 EXTRA-INDEX     USAGE INDEX

01 THE-TABLE OCCURS whatever INDEXED BY MAIN-INDEX

....

        SET MAIN-INDEX TO END-OF-TABLE-INDEX VALUE
        SET EXTRA INDEX TO MAIN-INDEX
         SET EXTRA-INDEX DOWN BY +1       << look backwards one
        PERFORM
          IF TARGET-VALUE < TABLE-VALUE (MAIN-INDEX) AND  TARGET -VALUE >
TARGET-VALUE (EXTRA-INDEX)
              (shuffle/insert  code, using SET to adjust both indices)
           ELSE
               SET MAIN-INDEX DOWN BY +1
               SET EXTRA-INDEX DOWN BY +1
           END-IF
        END-PERFORM

A bit more source code, but I'd find it more
"maintainance-programmer-friendly"...

MCM
```

##### ↳ ↳ Re: Inserting into a table

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hhg6s0231u@enews4.newsguy.com>`
- **References:** `<393BB313.77353D33@cusys.edu> <NrV_4.1255$Hs5.167625@dfiatx1-snr1.gtei.net>`

```
I like this code, looks good.

I would probably just use some extra REGION and use a temp table or a 'work'
table.  The data is already sorted right?  It's no use "re-sorting it".
Clear the temp table and load it, matching keys to the 'insert' record.
When the keys pass or match, load the insert record to the temp table and
keep incrementing and writing entries from the first table.  Continue till
out of entries.  Duplicates optional.

Jeff

----------
In article <NrV_4.1255$Hs5.167625@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> wrote:


> Instead of reference modifying, why not use an extra index...
>
…[42 more quoted lines elided]…
>
```

#### ↳ Re: Inserting into a table

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qlY_4.778$xc6.72233@news4.mia>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Hi Howard, you are really sharpening your skills!

My suggestion (in PSUEDO-CODE)

01  item-to-insert

01  OLD-TABLE
    05  owhatever-1
    05  owhatever-2
    ...

01  NEW-TABLE
    05  nwhatever-1
    05 n whatever-2
    ...

move 1 to I,J
Perform varying I from 1 by 1 until > old-table-limit
    if item-to-insert < owhatever-1 (I)
        move item-to-insert to nwhatever-1 (J)
        add 1 to J
        move owhatever-1 (I) to nwhatever (J )
...
...
end-Perform

OR, another way -
SELECT SORT-TABLE assign to ?
..
SD SORT-TABLE

SORT SORT-TABLE ON ASCENDING KEY
    SD-WHATEVER-1
INPUT PROCEDURE GET-RECS
OUTPUT PROCEDURE RELOAD-TABLE.

GET-RECS SECTION.
MOVE item-to-insert to SORT-REC
RELEASE SORT-REC
PERFORM VARYINGN I FROM 1 B Y 1
    UNTIL I > old-tablesize
    MOVE owhatever-1 (I) to SORT-REC
   RELEASE SORT-REC
END-PERFORM

RELOAD-TABLE SECTION.
    MOVE  1 TO I
    PERFORM  UNTIL NO-MORE-RETURNS
        RETURN SORT-REC INTO owhatever-1 (I)
          AT END
                SET NO-MORE-RETURNS TO TRUE
        NOT AT END
                ADD 1 TO I
        END-RETURN
    END-PERFORM


Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:393BB313.77353D33@cusys.edu...
> I have a sorted table and want to insert a field into it.  There are
> several ways to do this, including using reference modification of a
…[3 more quoted lines elided]…
> do you guys recommend?
```

#### ↳ Re: Inserting into a table

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393BB489.F4C2413F@cusys.edu>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Howard Brazee wrote:
> 
> I have a sorted table and want to insert a field into it.  There are
…[4 more quoted lines elided]…
> do you guys recommend?

I forgot to say what I did for this - I looped backwards from the
highest value of my sorted table, bumping up a record at a time until I
found where I wanted to insert.
```

##### ↳ ↳ Re: Inserting into a table

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uQ$uavvz$GA.77@cpmsnbbsa08>`
- **References:** `<393BB313.77353D33@cusys.edu> <393BB489.F4C2413F@cusys.edu>`

```
If  your compiler supports table sort insert at end of table and resort the
table.  I have used the same method that you describe.  In some cases I have
written the table to a sequential file along with  the new entry, sorted and
rebuilt the table.  In cases where the table data is in an indexed file I
have added the entry and then rebuilt the file.  Guess it depends on the
situation taking into consideration effeciency and simplicity.

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:393BB489.F4C2413F@cusys.edu...
> Howard Brazee wrote:
> >
…[9 more quoted lines elided]…
> found where I wanted to insert.
```

###### ↳ ↳ ↳ Re: Inserting into a table

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393BC067.815D7467@cusys.edu>`
- **References:** `<393BB313.77353D33@cusys.edu> <393BB489.F4C2413F@cusys.edu> <uQ$uavvz$GA.77@cpmsnbbsa08>`

```


brucepbarrett wrote:
> 
> If  your compiler supports table sort insert at end of table and resort the
> table.  I have used the same method that you describe.  

It doesn't.  Too bad.

> In some cases I have
> written the table to a sequential file along with  the new entry, sorted and
> rebuilt the table.  

I am cloning this program from two other programs.  It used that
technique, but it had two different COBOL sorts, one for the main
process, and one to sort the file it wrote out.  I couldn't figure out
how to do that with my new compiler, but didn't like that solution
anyway.  I suppose I could have written it out as ISAM, and then read it
in.

> In cases where the table data is in an indexed file I
> have added the entry and then rebuilt the file.  Guess it depends on the
> situation taking into consideration effeciency and simplicity.

Which were the criteria which I was considering - with simplicity
pointing towards maintainability.
 
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:393BB489.F4C2413F@cusys.edu...
…[11 more quoted lines elided]…
> > found where I wanted to insert.
```

#### ↳ Re: Inserting into a table

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hgs0t$tsm$1@slb0.atl.mindspring.net>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Howard,
  As I recall, you are on an IBM mainframe, so the following will NOT work -
but in the next Standard it will (and on some implementations it already
does).

I would add how ever many "new" records that I have at the bottom of the
table and use the SORT verb to sort the table.  (Probably not the most
efficient but certainly "self-documenting)
```

#### ↳ Re: Inserting into a table

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393C89A3.CB1F4CD6@mediaone.net>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Howard,

The question is: Why do you need to keep the table sorted? Is it to be able
to look it up using SEARCH ALL? If this is the case, the entire approach is
wrong. SEARCH ALL (i.e. binary search) searches in O(log(N)) time, and
inserting an entry while keeping the table sorted obviously requires O(N)
time. This is both inefficient and complicated. The most natural thing to do
is use an algorithm that both  searches and inserts in O(1), i.e. constant
time, and the only such algorithm is hashing. If your table is not too
large, you can allocate a table several times the number of perspective
entries thus keeping it very sparse and even the simplest hashing scheme -
linear probing - performing times faster than the binary search, to say
nothing of the insertion. Since you undoubtedly know how to code hashing
with linear probing (or double hashing, for that matter, if you are
concerned about memory usage), I am leaving it out. Just wanted to remind
you of this possibility.

Kind regards,
====================
Paul M. Dorfman
Jacksonville, Fl
====================




Howard Brazee wrote:

> I have a sorted table and want to insert a field into it.  There are
> several ways to do this, including using reference modification of a
…[3 more quoted lines elided]…
> do you guys recommend?
```

##### ↳ ↳ Re: Inserting into a table

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393CFDD1.DD95414F@cusys.edu>`
- **References:** `<393BB313.77353D33@cusys.edu> <393C89A3.CB1F4CD6@mediaone.net>`

```
"Paul M. Dorfman" wrote:
> 
> Howard,
…[14 more quoted lines elided]…
> you of this possibility.

Good point to make in a public forum.  But no, it is for some subsequent
match-merge logic.  The program used to have two sorts in it, but our
latest version of COBOL is gagging at the way it was done.  I would do
things differently writing from scratch.
```

#### ↳ Re: Inserting into a table

- **From:** "Rob Kemmer" <rob@tobin-kemmer.freeserve.co.uk>
- **Date:** 2000-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hpb23$5pj$1@news8.svr.pol.co.uk>`
- **References:** `<393BB313.77353D33@cusys.edu>`

```
Assuming a table of size "table-size" and that the table is not already full
try:

perform varying sub from table-size  by -1 until table-value (sub) <
new-value
        move table-value (sub -1) to table-value (sub)
end-perform
move new-value to table-value (sub + 1)

(I think!)

Rob Kemmer

Howard Brazee wrote in message <393BB313.77353D33@cusys.edu>...
>I have a sorted table and want to insert a field into it.  There are
>several ways to do this, including using reference modification of a
…[3 more quoted lines elided]…
>do you guys recommend?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
