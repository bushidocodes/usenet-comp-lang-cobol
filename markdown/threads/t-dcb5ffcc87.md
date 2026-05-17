[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In-line performs

_7 messages · 7 participants · 1996-12 → 1997-01_

---

### In-line performs

- **From:** "john giddings" <ua-author-43721@usenetarchives.gap>
- **Date:** 1996-12-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32C7E8A9.7520@ix.netcom.com>`

```

Can someone tell me when someone would use an "inline" Perform vice an
"out-of-line" perform? I pretty much understand the difference I just do
not get the philosophy of usage. Once again thank you in advance.
```

#### ↳ Re: In-line performs

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-12-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32C7E8A9.7520@ix.netcom.com>`
- **References:** `<32C7E8A9.7520@ix.netcom.com>`

```



John Giddings wrote in article
<32C··.@ix.··m.com>...
› Can someone tell me when someone would use an "inline" Perform vice an
› "out-of-line" perform? I pretty much understand the difference I just do
› not get the philosophy of usage. Once again thank you in advance.
›

It's just a coding preference. When I have to maintain code with an "out
of line"
perform, that does another perform, that does another perform, and I'm
jumping all over the code to figure out something simple, I get a headache.
This is especially true of a non repeated task.

Therefore here are my general personal preferences:

Inline perform when the task in performed only once in the program, or
where there are subsequent complex performs that will make maintenance
difficult. I also like then for large repetitive array processing. For
example, extraciting information from a large multi dimensional table to
insert into various data records.
```

#### ↳ Re: In-line performs

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1996-12-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32C7E8A9.7520@ix.netcom.com>`
- **References:** `<32C7E8A9.7520@ix.netcom.com>`

```

John Giddings wrote:

› Can someone tell me when someone would use an "inline" Perform vice an
› "out-of-line" perform? I pretty much understand the difference I just do
› not get the philosophy of usage. Once again thank you in advance.

John,

An inline Perform would be better to use when the actions within the
Perform are fairly simple, such as:

PERFORM VARYING SUB FROM 1 BY 1 UNTIL SUB > 4
MOVE SPACES TO XX-MBR-NAME (SUB)
MOVE 0 TO XX-MBR-AGE (SUB)
MOVE 0 TO XX-MBR-ANN-WGS (SUB)
MOVE 0 TO XX-MBR-ANN-OTH (SUB)
MOVE SPACES TO XX-SRC (SUB)
END-PERFORM


An out-of-line Perform is best for whole tasks, such as:

PERFORM PRINT-PAGE-RTN
VARYING SUB FROM 1 BY 1 UNTIL SUB > 55 .

Anything in between, IMO is at the discretion of the programmer. It's
important the flow of the program be consistant. Inlines can clutter
the main logic, but out-of-lines can bat you back and forth like a
tennis ball. Readability and maintainability should be your intent.

My 2 cents.
Hope that helps.

Tim Oxler

TEO Computer Technologies Inc.
tro··.@i··.net
http://www.i1.net/~troxler
http://users.aol.com/TEOcorp
```

#### ↳ Re: In-line performs

- **From:** "dbret..." <ua-author-6588809@usenetarchives.gap>
- **Date:** 1997-01-01T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32C7E8A9.7520@ix.netcom.com>`
- **References:** `<32C7E8A9.7520@ix.netcom.com>`

```

Well, I normally use in-line performs to do initialization of tables, or
when I'm searching a field or table for just one thing......for instance,
if I need to find a comma in a name field.........If I have to check for
multiple conditions in a perform, then I'll make it a separate paragraph.

Dave Bretz
```

#### ↳ Re: In-line performs

- **From:** "skitrash" <ua-author-7277198@usenetarchives.gap>
- **Date:** 1997-01-02T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p5@usenetarchives.gap>`
- **In-Reply-To:** `<32C7E8A9.7520@ix.netcom.com>`
- **References:** `<32C7E8A9.7520@ix.netcom.com>`

```

John Giddings wrote:
›
› Can someone tell me when someone would use an "inline" Perform vice an
› "out-of-line" perform? I pretty much understand the difference I just do
› not get the philosophy of usage. Once again thank you in advance.


Performance ... on many systems, a program will have to page (swap to
disk) in order to get a code segment for an 'out of line perform'. When
an inline perform is executed, no paging should occur. Any good
programmer will tell you that disk reads and writes are a performance
killer. The higher the number of repetitions of the encapsulated code,
the higher the performance penalty.

In a mainframe environment, where many programs share resources like
disk cache, cpu time, etc. a poorly written application can hurt
everyone. In most applications, the question of 'inline / outline
performs' will be minor. If you are coding a routine that will be used a
lot, optimizing the code might be a good idea.

Mike
```

##### ↳ ↳ Re: In-line performs

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcb5ffcc87-p5@usenetarchives.gap>`
- **References:** `<32C7E8A9.7520@ix.netcom.com> <gap-dcb5ffcc87-p5@usenetarchives.gap>`

```

SkiTrash wrote:
› John Giddings wrote:
›› Can someone tell me when someone would use an "inline" Perform vice an
…[3 more quoted lines elided]…
› disk) in order to get a code segment for an 'out of line perform'. When

Of course a good optimizing compiler may obscure this distinction by
automatically converting performs of out-of-line code into inline
performs when the code is only invoked in a relatively "small" number of
places.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

###### ↳ ↳ ↳ Re: In-line performs

- **From:** "t.w..." <ua-author-17072168@usenetarchives.gap>
- **Date:** 1997-01-08T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dcb5ffcc87-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-dcb5ffcc87-p6@usenetarchives.gap>`
- **References:** `<32C7E8A9.7520@ix.netcom.com> <gap-dcb5ffcc87-p5@usenetarchives.gap> <gap-dcb5ffcc87-p6@usenetarchives.gap>`

```

"Joel C. Ewing" wrote:

› SkiTrash wrote:
›› John Giddings wrote:
››› Can someone tell me when someone would use an "inline" Perform vice an
››› "out-of-line" perform? 

You should use inline Performs only if there is a small number of
statements inside. Even then maintenance programmers might blow up
your inline perform until it looks like this (real world example)

PERFORM UNTIL FILE-STAT NOT = ZERO AND NOT = 98
PERFORM 990-READ-DABTEIL-NEXT
IF NO-RECORD OR END-OF-FILE
MOVE SPACE TO H-TEXT-ERROR-MSG
** Aenderung von 12.95 rola, Abfrage ergaenzt wegen 'subscript out of
range'
** wenn komlik-pos weder geoeffnet noch gelesen
IF TAKT OF KOMLIK-POS NUMERIC AND
TAKT OF KOMLIK-POS > ZERO
MOVE 1 TO TAKT OF TAKT-TABELLE
OF VW-NACHRICHT (TAKT OF KOMLIK-POS)
END-IF
** ende
MOVE PICKPOS-CNTR TO PICK-POS-COUNTER OF VW-NACHRICHT
STRING "KVPOS"
WS-PROZESS-KENNZ
" : Anzahl der geschriebenen Pickpos in Takt "
WS-TAKT
" : "
PICKPOS-CNTR
" !"
DELIMITED BY SIZE
INTO H-TEXT-ERROR-MSG
END-STRING
MOVE ZERO TO PICKPOS-CNTR
PERFORM 910-ERR-REPLY
MOVE SPACE TO H-TEXT-ERROR-MSG
STRING "KVPOS"
WS-PROZESS-KENNZ
" : Programm - Ende"
DELIMITED BY SIZE
INTO H-TEXT-ERROR-MSG
END-STRING
ELSE
IF NO-ERROR
MOVE TT OF WS-DATUM TO TAG-3 OF
KOMLIK-POS
MOVE WS-TAKT TO TAKT-3 OF
KOMLIK-POS
MOVE ABTEIL-KEY OF ABTEIL TO S-UN-BST-ABT-3 OF
KOMLIK-POS
PERFORM 920-START-DKOMLIKP
IF NO-RECORD OR END-OF-FILE
MOVE 98 TO FILE-STAT
MOVE SPACE TO WS-LOG-FILE-NAME
** Aenderung von 12.95 rola, Abfrage ergaenzt wegen 'subscript out of
range'
** wenn komlik-pos weder geoeffnet noch gelesen
IF TAKT OF KOMLIK-POS NUMERIC AND
TAKT OF KOMLIK-POS > ZERO
MOVE 1 TO TAKT OF TAKT-TABELLE
OF VW-NACHRICHT (TAKT OF
KOMLIK-POS)
END-IF
** Ende
STRING "KVPOS"
WS-PROZESS-KENNZ
" : Keine Koepfe in Takt "
TAKT-3 OF KOMLIK-POS
" fuer "
ABTEIL-KEY
" zur Bearbeitung vorhanden"
DELIMITED BY SIZE
INTO H-TEXT-ERROR-MSG
END-STRING
PERFORM 911-ERR-REPLY-PROTOKOLL
END-IF
PERFORM BEARB-CASE UNTIL FILE-ERROR
END-IF
END-IF
END-PERFORM.

For easier maintenance it is better to use outline performs and
separate paragraphs. You might even share the code of your 'extra
paragraph' with other parts of your program (i.e. a perform with
different terminating conditions but same statements inside) which is
impossible with inline performs.
Depending on your platform, outline performs can be easier to debug.
Example: PERFORM VARYING IND 1FROM 1 BY 1 UNTIL IND > 500
blablabla
END-PERFORM
the-next-statement

You should be able to enter the loop, debug some steps of 'blablabla',
step over the rest and debug 'the-next-statement' afterwards.

› Performance ... on many systems, a program will have to page (swap to
› disk) in order to get a code segment for an 'out of line perform'. When

Typical COBOL programs spend 95 % of their execution time on database
access, so code performance is *not* that important.





Thomas Wolter
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
