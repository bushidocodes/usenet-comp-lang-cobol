[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SEARCH ALL COMAND

_3 messages · 3 participants · 1997-03_

---

### SEARCH ALL COMAND

- **From:** "10765..." <ua-author-17072833@usenetarchives.gap>
- **Date:** 1997-03-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5g3uco$7ii$1@mhadf.production.compuserve.com>`

```

I have a homework assignment and i was wondering if anyone has
had a similar problem with micro focus when using a search all in
conjunction with an internal table. If anyone can help? Thanks
05 S-ARRAY.
10 FILLER PIC X(7) VALUE 'ALA0500'.
10 FILLER PIC X(7) VALUE 'COL0760'.
10 FILLER PIC X(7) VALUE 'ILL0700'.
10 FILLER PIC X(7) VALUE 'KAS1000'.
10 FILLER PIC X(7) VALUE 'MIZ1360'.
10 FILLER PIC X(7) VALUE 'OHO0800'.
10 FILLER PIC X(7) VALUE 'OKA0560'.
10 FILLER PIC X(7) VALUE 'PEN1500'.
10 FILLER PIC X(7) VALUE 'TEX2050'.
10 FILLER PIC X(7) VALUE 'WAS1900'.
05 S-SINGLE REDEFINES S-ARRAY OCCURS 10 TIMES INDEXED
BY S1.
10 SSTATE PIC X(3).
10 STAX PIC 99V99.


in the procedure division

SEARCH ALL S-SINGLE AT END MOVE 'O' TO ERROR-COUNT
WHEN SSTATE (S1) = INP-STATE <---illegal key 314-S
MOVE STAX (S1) TO STAXOUT

sma··.@com··e.com
```

#### ↳ Re: SEARCH ALL COMAND

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff0ac3fa5b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5g3uco$7ii$1@mhadf.production.compuserve.com>`
- **References:** `<5g3uco$7ii$1@mhadf.production.compuserve.com>`

```

smaxey wrote:
› 
› I have a homework assignment and i was wondering if anyone has
…[25 more quoted lines elided]…
› sma··.@com··e.com

You're almost there. In order for SEARCH ALL to work, your data definition
needs to specify the key:

05 S-SINGLE REDEFINES S-ARRAY
OCCURS 10 TIMES
ASCENDING KEY IS SSTATE
INDEXED BY S1.
› 10 SSTATE PIC X(3).
› 10 STAX PIC 99V99.

If you include the ASCENDING KEY clause, it should work fine. Of course, in
the real world, a table with only 10 entries is too small to realize much
performance improvement from a binary search. A serial search would work
just as well in this example.

Good Luck!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: SEARCH ALL COMAND

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-11T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff0ac3fa5b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5g3uco$7ii$1@mhadf.production.compuserve.com>`
- **References:** `<5g3uco$7ii$1@mhadf.production.compuserve.com>`

```



smaxey <107··.@Com··e.COM> wrote in article
<5g3uco$7ii$1.··.@mha··e.com>...
›            05 S-SINGLE REDEFINES S-ARRAY OCCURS 10 TIMES 
›                    ** ASCENDING KEY IS SSTATE **
…[9 more quoted lines elided]…
›             MOVE STAX (S1) TO STAXOUT                           


In your table definition you need an "ASCENDING KEY IS SSTATE" phrase.
Note where I put it delimited by **.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
