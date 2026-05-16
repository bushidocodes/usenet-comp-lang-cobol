[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# looking for constructive criticisms

_2 messages · 2 participants · 1999-10_

---

### Re: looking for constructive criticisms

- **From:** jasman@theoffice.net
- **Date:** 1999-10-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v33tn$qlt$1@nntp1.atl.mindspring.net>`
- **References:** `<SDYQ3.3505$we.5409@newsfeeds.bigpond.com>`

```
Hi Judy,

As you requested, here are the comments (some minor some significant):

1. I trust that you have not tried to compile this yet or if you have you found
the spelling errors.

2. I was always taught to place 01 WI-MASTER-RECORD in WS and READ MASTER-FILE
INTO WI-MASTER-RECORD instead of working in the FD area.

3. I assume that a missing field name (e.g. last 03 level in FD) is treated by
RM/COBOL as FILLER. If not you need to fix these. I would probably code FILLER
just to be more "standard".

4. Code 01 WW-PRODUCT-TABLE-SIZE PIC S9(04) COMP VALUE +32. immediately before
01 WT-PRODUCT-TABLE. Then you can change WT-INDEX > 32 to WT-INDEX >
WW-PRODUCT-TABLE-SIZE. In a small program like this it is easy to increase the
size of the table and modify all references to the number of occurs, but in a
bigger program being able to quickly change the VALUE clause and the OCCURS
clause that are right next to each other without having to search thru the
PROCEDURE DIVISION can be a real time saver.

5. I'll avoid the question of Why use a table instead of accessing the indexed
file directly. I'm guessing it was part of the problem description.

6. WT-PRODUCT-TABLE does not appear to be initialized. This could be trouble now
or in the future.

7. You seem to be assuming that you will have exactly 32 records to read and
load into the table. What happens if there are only 31, 33 or zero records (EOF
on first read)? Might want to consider performing B-LOAD-MASTER UNTIL you hit
EOF on input file and as you read each record move it to the next unused slot in
the table. See READ x AT END imp-statement in your books.

That should keep you busy for a little while.

Enjoy,
Jim Steelman
```

#### ↳ Re: looking for constructive criticisms

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-10-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MNiR3.77$iz3.536@client>`
- **References:** `<SDYQ3.3505$we.5409@newsfeeds.bigpond.com> <7v33tn$qlt$1@nntp1.atl.mindspring.net>`

```

<jasman@theoffice.net> wrote in message
news:7v33tn$qlt$1@nntp1.atl.mindspring.net...
[snip]
> 3. I assume that a missing field name (e.g. last 03 level in FD) is
treated by
> RM/COBOL as FILLER. If not you need to fix these. I would probably code
FILLER
> just to be more "standard".
[snip]
> Enjoy,
> Jim Steelman

Jim:

RM/COBOL and all the other COBOL compilers purporting to conform to the 1985
ANSI/ISO Standard must treat an omitted data-name or FILLER clause as though
FILLER had been specified (section 5.5 of ANSI X3.23-1985).

Some shops require FILLER in their own standards, but the Standard does not.

Best regards,
Tom Morrison
Liant Software Corporation
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
