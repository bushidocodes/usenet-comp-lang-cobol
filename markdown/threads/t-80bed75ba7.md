[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed By and Search in 2 Occurs levels?

_2 messages · 2 participants · 1999-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Indexed By and Search in 2 Occurs levels?

- **From:** "M. Lenz" <Mogens.Lentz@sas.dk>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tht28$9lq$1@news.dknet.dk>`

```
I want to change  the field UCZIPRIO-AREA to Occurs 2.
If I do that, the compiler says something about indexed by must be in level
1 too.
The program that does the search on the table, will in the future get a
field containing either the value 1 or 2. The search should only search the
level which this field tells it to.
How do I accomplish this?

The table definition today:

03  UCZIPRIO-AREA.
  05  PRIO-MAX              PIC 999 VALUE 300.
  05  PRIO-TABLE.
    07  PRIO-TAB  OCCURS 300 TIMES
                  DESCENDING KEY IS PRIO-LINENO
                  INDEXED BY PRIO-IX.
      10  PRIO-LINENO       PIC S9(7)  COMP-3.
      10  PRIO-PRIORITY     PIC 99.

The search statement used today:

SEARCH ALL PRIO-TAB
AT END
  MOVE PRIO-NOT-FOUND TO SUB-STATUS
WHEN PRIO-LINENO (PRIO-IX) = IRS-LINENO
  MOVE PRIO-FOUND TO  SUB-STATUS

  MOVE PRIO-PRIORITY (PRIO-IX) TO IRS-PRIORITY
END-SEARCH
```

#### ↳ Re: Indexed By and Search in 2 Occurs levels?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<751L3.51$7p6.3304@dfiatx1-snr1.gtei.net>`
- **References:** `<7tht28$9lq$1@news.dknet.dk>`

```
M. Lenz wrote in message <7tht28$9lq$1@news.dknet.dk>...
>I want to change  the field UCZIPRIO-AREA to Occurs 2.
>If I do that, the compiler says something about indexed by must be in level
…[23 more quoted lines elided]…
>


If UZCI-PRIOAREA OCCURS 2,  the new search should work fine if you change
all the subordinate references (e.g., PRIO-LINE-NO and PRIO-PRIORITY) to add
the second level of indexing; ie. each of these requires two indices.

SEARCH ALL PRIO-TAB( First-index)
 ...
   WHEN PRIO-LINENO(First-index prio-ix)....
...
END-SEARCH.

(Not tested, but I've done this before without problems)

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
