[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMB sort -- sorry it took so long

_3 messages · 2 participants · 1995-04 → 1995-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### COMB sort -- sorry it took so long

- **From:** "rad..." <ua-author-5744355@usenetarchives.gap>
- **Date:** 1995-04-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3npg5u$hok@news.inlink.com>`

```
For everyone who sent me mail requesting the COMB sort code, here it is.
Sorry it took me so long. I've been so busy the last couple of days
this is the first opportunity I've had to catch up on my mail and get
on the net.

WARNING -- WARNING -- WARNING

I did not have a compiler at my convenience when I typed this up. I
had the routine shoved deep within a program and I cut it out in an
effort to make it a stand-alone example. If there's a syntax error or two,
please forgive me. I looked it over as best as a 'human' compiler can.
The logic should be sound and any syntax errors that exist should be
easy to correct. Here goes:


ID DIVISION.
PROGRAM-ID. COMBSORT.
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE.

01 WS-COUNTERS.
05 WS-TABLE-COUNT PIC S9(09) COMP VALUE 10.
05 WS-SWAP-COUNT PIC S9(09) COMP VALUE 0.
05 WS-COMB-SIZE PIC S9(09) COMP VALUE 0.
05 WS-INNER-LOOP-LIMIT PIC S9(09) COMP VALUE 0.
05 WS-SUB1 PIC S9(09) COMP VALUE 0.
05 WS-SUB2 PIC S9(09) COMP VALUE 0.
05 WS-HOLD PIC 99 VALUE 0.

01 WS-DATA.
05 FILLER PIC X(30) VALUE
'10 05 04 08 07 06 03 01 02 09 '.

01 WS-TABLE REDEFINES WS-DATA.
05 WS-TABLE-ROW OCCURS 10.
10 WS-ELEMENT PIC 99.
10 FILLER PIC X.

PROCEDURE DIVISION.

DISPLAY 'COMBSORT: TABLE BEFORE SORT'
DISPLAY '---------------------------'
PERFORM DISPLAY-TABLE

MOVE WS-TABLE-COUNT TO WS-COMB-SIZE

PERFORM WITH TEST AFTER
UNTIL WS-SWAP-COUNT = 0 AND WS-COMB-SIZE = 1
COMPUTE WS-COMB-SIZE = WS-COMB-SIZE / 1.3

EVALUATE WS-COMB-SIZE
WHEN 10 MOVE 11 TO WS-COMB-SIZE
WHEN 9 MOVE 11 TO WS-COMB-SIZE
WHEN 0 MOVE 1 TO WS-COMB-SIZE
END-EVALUATE

MOVE 0 TO WS-SWAP-COUNT

COMPUTE WS-INNER-LOOP-LIMIT = WS-TABLE-COUNT - WS-COMB-SIZE
MOVE WS-COMB-SIZE TO WS-SUB2

PERFORM VARYING WS-SUB1 FROM 1 BY 1
UNTIL WS-SUB1 > WS-INNER-LOOP-LIMIT
ADD 1 TO WS-SUB2
IF WS-NUMBER(WS-SUB1) > WS-NUMBER(WS-SUB2)
MOVE WS-NUMBER(WS-SUB1) TO WS-HOLD
MOVE WS-NUMBER(WS-SUB2) TO WS-NUMBER(WS-SUB1)
MOVE WS-HOLD TO WS-NUMBER(WS-SUB2)
ADD 1 TO WS-SWAP-COUNT
END-IF
END-PERFORM

END-PERFORM

DISPLAY 'COMBSORT: TABLE AFTER SORT'

PERFORM DISPLAY-TABLE

GOBACK.

DISPLAY-TABLE.
DISPLAY SPACES
PERFORM VARYING WS-SUB1 FROM 1 BY 1 UNTIL WS-SUB1 > WS-TABLE-COUNT
DISPLAY 'ELEMENT#: ' WS-SUB1 ' = ' WS-NUMBER(WS-SUB1)
END-PERFORM
DISPLAY SPACES
DISPLAY SPACES.

P.S. You might notice that the comb size reduced each outer-loop iteration
by dividing it by 1.3. You can use other values but Byte magazine
ran lots of statistics and came up with 1.3 as the best all-around
factor. However, other factors are better for different types of
data. I don't remember everything out of the article but thought
the 1.3 factor was interesting. Also, due to additional statistical
analysis, Byte magazine noticed that comb sizes of 10 and 9 were
poor and sort performance was improved by setting them to 11.

Please respond. I'd be interested to know what everyone thinks
when you try it on your own. Also, try it with a HUGE list. I
think you'll be amazed how quickly it performs when compared to
other sorts. And I think everyone will agree, it's pretty simple
to code no matter what language you write it in.

Robert R. Radina
rad··.@vul··k.com
St. Louis, MO
```

#### ↳ Re: COMB sort -- sorry it took so long

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc40ddcf63-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3npg5u$hok@news.inlink.com>`
- **References:** `<3npg5u$hok@news.inlink.com>`

```
I've been trying to post this for a week, but our news server
was in surgery. Here's my contribution to the Comb sort saga.

This is a discussion written by LEIF SVALGAARD:

"Just as we thought that the last word had been said about
sorting, a breakthrough comes along and spoils everything. In
the April 1991 issue of BYTE magazine, Stephen Lacey and
Richard Box show that a simple modification to bubble sort
makes it a fast and efficient sort method on par with heapsort
and quicksort.

"In a bubble sort, each item is compared to the next; if the
two are out of order, they are swapped. This method is slow
because it is susceptible to the appearance of what Box and
Lacey call turtles. A turtle is a relatively low value
located near the end of the table. During a bubble sort, this
element moves only one position for each pass, so a single
turtle can cause maximal slowing. Almost every long table of
items contains a turtle.

"Their simple modification of bubble sort which they call
`combsort' eliminates turtles quickly by allowing the distance
between compared items to be greater than one. This distance
- the JUMP-SIZE - is initially set to the TABLE-SIZE. Before
each pass, the JUMP-SIZE is divided by 1.3 (the shrink
factor). If this causes it to become less than 1, it is
simply set to 1, collapsing combsort into bubble sort. An
exchange of items moves items by JUMP-SIZE positions rather
than only one position, causing turtles to jump rather than
crawl. As with any sort method where the displacement of an
element can be larger than one position, combsort is not
stable - like elements do not keep their relative positions.
This is rarely a problem in practice.

"Successively shrinking the JUMP-SIZE is analogous to combing
long, tangled hair - stroking first with your fingers alone,
then with a pick comb that has widely spaced teeth, followed
by finer combs with progressively closer teeth - hence the
name comb sort. Lacey and Box came up with a shrink factor of
1.3 empirically by testing combsort on over 200,000 random
tables. There is at present no theoretical justification for
this particular value; it just works..."

I assume a table of items, each with a key and some data. The
Comb sort also uses these variables:

01 COMB-SORT-VARIABLES.
02 JUMP-SIZE PIC S9(5) COMP.
02 UPPER-LIMIT PIC S9(5) COMP.
02 SWAP-NBR PIC S9(5) COMP.
02 SWAP-INDICATOR PIC X.
88 NO-MORE-SWAPS VALUE IS SPACE.

SORT-ITEM-DETAILS.
MOVE "SWAP" TO SWAP-INDICATOR
MOVE NBR-OF-ITEMS TO JUMP-SIZE
PERFORM COMB-SORT-ITEM-DETAILS
UNTIL NO-MORE-SWAPS
AND JUMP-SIZE NOT > 1
.

COMB-SORT-ITEM-DETAILS.
COMPUTE JUMP-SIZE = (10 * JUMP-SIZE + 3) / 13
COMPUTE UPPER-LIMIT = NBR-OF-ITEMS - JUMP-SIZE
MOVE SPACE TO SWAP-INDICATOR

PERFORM COMPARE-ITEM-AND-SWAP
VARYING ITEM-NBR FROM 1 BY 1
UNTIL ITEM-NBR > UPPER-LIMIT
.

COMPARE-ITEM-AND-SWAP.
COMPUTE SWAP-NBR = ITEM-NBR + JUMP-SIZE
IF ITEM-NAME (ITEM-NBR) > ITEM-NAME (SWAP-NBR)
MOVE ITEM-DETAILS (ITEM-NBR) TO CUR-DETAILS
MOVE ITEM-DETAILS (SWAP-NBR) TO ITEM-DETAILS (ITEM-NBR)
MOVE CUR-DETAILS TO ITEM-DETAILS (SWAP-NBR)
MOVE "SWAP" TO SWAP-INDICATOR
.
```

##### ↳ ↳ Re: COMB sort -- sorry it took so long

- **From:** "rad..." <ua-author-5744355@usenetarchives.gap>
- **Date:** 1995-05-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc40ddcf63-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dc40ddcf63-p2@usenetarchives.gap>`
- **References:** `<3npg5u$hok@news.inlink.com> <gap-dc40ddcf63-p2@usenetarchives.gap>`

```
i.··.@htk··o.jp wrote:
: In article <3o391s$b.··.@new··U.net> pah··.@eu··t.be (Pieter Hintjens) writes:

: > This is a discussion written by LEIF SVALGAARD:
: >
: > "Just as we thought that the last word had been said about
: > sorting, a breakthrough comes along and spoils everything. In
: > the April 1991 issue of BYTE magazine, Stephen Lacey and
: > Richard Box show that a simple modification to bubble sort
: > makes it a fast and efficient sort method on par with heapsort
: > and quicksort.

: I got interested in comb sort and tested its efficiency in comparison
: with quicksort. The result follows:
: --------------------------------------------------------------------

[test results cut]

: This test shows that comb sort is about half as efficient as quicksort,
: which is really remarkable for the simpleness of its source code.

[source code cut]

Those were precisely my observations. I was amazed at how fast
it was and yet how remarkably simple it was to implement-- no matter
what language you were using.

Sure beats the heck out of a BUBBLE SORT and yet, is no more complex
to code and understand than a BUBBLE SORT.

I think that was the intention when it was published in Byte. Someone
earned their pay that week.

Robert R. Radina
rad··.@vul··k.com
St. Louis, MO
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
