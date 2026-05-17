[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sample data using Fileaid/Syncsort

_3 messages · 3 participants · 1998-08_

---

### Sample data using Fileaid/Syncsort

- **From:** "jos..." <ua-author-13908309@usenetarchives.gap>
- **Date:** 1998-08-07T17:40:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6qfs8b$rt1$1@nnrp1.dejanews.com>`

```
Does any one know select every n th row from a dataset using either fileaid
or Syncsort ? This will give a good sample from the dataset. I know you can
extract x number of rows from a file and even start after n the row. Just
wondering if someone else had a similiar situation. Thanks!!

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: Sample data using Fileaid/Syncsort

- **From:** "darius cooper" <ua-author-16041747@usenetarchives.gap>
- **Date:** 1998-08-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-098bfd99da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6qfs8b$rt1$1@nnrp1.dejanews.com>`
- **References:** `<6qfs8b$rt1$1@nnrp1.dejanews.com>`

```
One way to do this is to SORT the file on a field that contains "random"
data: e.g., on the the milli-second field of a TIMESTAMP field, or the least
significant digits/characters of some other field. In a table that we use,
we have a EMP_ID DECIMAL(11). If we SELECT...

WHERE SUBSTR(DIGITS(EMP_ID),10,2) = '00' or '01'
we get a pretty good 2% sample of our data.

All the best,

- Darius Cooper


jos··.@nat··e.com wrote in message <6qfs8b$rt1$1.··.@nnr··s.com>...
›   Does any one know select every n th row from a dataset using either
› fileaid
…[5 more quoted lines elided]…
› http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Sample data using Fileaid/Syncsort

- **From:** "fyae..." <ua-author-17074334@usenetarchives.gap>
- **Date:** 1998-08-10T12:35:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-098bfd99da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6qfs8b$rt1$1@nnrp1.dejanews.com>`
- **References:** `<6qfs8b$rt1$1@nnrp1.dejanews.com>`

```
In article <6qfs8b$rt1$1.··.@nnr··s.com>,
jos··.@nat··e.com wrote:
› Does any one know select every n th row from a
dataset ...

With DFSORT, you can use OUTFIL and SPLIT to select
every nth record. Here's an example that writes
every 3rd record (1, 4, 7, 10, ...) to the LIVE data
set:

//SKIPN EXEC PGM=ICEMAN
//SYSOUT DD SYSOUT=*
//SORTIN DD DSN=...
//LIVE DD DSN=...
//DEAD1 DD DUMMY
//DEAD2 DD DUMMY
//SYSIN DD *
OPTION COPY
OUTFIL FNAMES=(LIVE,DEAD1,DEAD2),SPLIT
/*

SPLIT writes the input records to the OUTFIL data
sets in rotation, so the first record will go to
LIVE, the second record to DEAD1, the third record
to DEAD2, the fourth record to LIVE, and so on.

Frank L. Yaeger - DFSORT Team
Specialties: ICETOOL, OUTFIL, Y2K
=> DFSORT/MVS is on the WWW at
http://www.ibm.com/storage/dfsort/





-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
