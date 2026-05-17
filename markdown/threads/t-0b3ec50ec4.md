[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Non-contiguous fields and alternate record keys...

_3 messages · 3 participants · 2015-05_

---

### Non-contiguous fields and alternate record keys...

- **From:** "user" <ua-author-86839@usenetarchives.gap>
- **Date:** 2015-05-13T17:16:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XnsA499A5A815E7Euserfoobarcominvalid@94.75.214.90>`

```
says you's has a record like so

FILE-CONTROL.
SELECT WORLD-INDEX-FILE ASSIGN TO "WORLD.IDX"
ORGANIZATION IS INDEXED
ACCESS MODE IS RANDOM
RECORD KEY IS IDX-ID-NO
ALTERNATE RECORD KEY IS FULL-NAME WITH DUPLICATES.
* potentially I want something like
* ALTERNATE RECORD KEY IS CITY-AND-STATE WITH DUPLICATES
... whatever

FD WORLD-INDEX-FILE.
01 WORLD-INDEX-RECORD.
05 IDX-ID-NO PIC 9(6).
05 IDX-FIRST-NAME PIC X(11).
05 IDX-LAST-NAME PIC X(13).
05 IDX-COMPANY PIC X(30).
05 IDX-STREET-ADDRESS PIC X(33).
05 IDX-CITY PIC X(30).
05 IDX-COUNTY PIC X(30).
05 IDX-STATE-PROVINCE PIC X(2).
05 IDX-POSTAL-CODE PIC X(8).
05 IDX-PHONE-NO PIC X(12).
05 IDX-MOBILE-NO PIC X(12).
05 IDX-E-MAIL PIC X(43).
05 IDX-WEB-PAGE PIC X(46).
66 FULL-NAME RENAMES IDX-FIRST-NAME THRU IDX-LAST-NAME.

now says you'ze wants to do something likes with IDX-CITY and IDX-
STATE=PROVINCE whats you'ze did with the FULL-NAME RENAMES, any
suggestions?
```

#### ↳ Re: Non-contiguous fields and alternate record keys...

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2015-05-13T19:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3ec50ec4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<XnsA499A5A815E7Euserfoobarcominvalid@94.75.214.90>`
- **References:** `<XnsA499A5A815E7Euserfoobarcominvalid@94.75.214.90>`

```
Mr. Mxyztplk wrote:
› says you's has a record like so
› 
…[29 more quoted lines elided]…
› suggestions?

Refreshing to see an actual use of 66 level. After writing code to cater for
it in several different packages and knowing it is unlikely ever to be
executed, it makes the effort a bit more worthwhile...

Here's my advice:

1. Get yourself sober.

2. Understand that everything you can do with 66 you can also do with
REDEFINES, even though some people claim you can't...

3. Rearrange your record layout like this:

›       01 WORLD-INDEX-RECORD.
›           05 IDX-ID-NO PIC 9(6).
…[13 more quoted lines elided]…
›       66 CITY-AND-STATE  RENAMES IDX-CITY THRU IDX-STATE-PPROVINCE.

... or, (preferred by most, and not requiring either RENAMES OR
REDEFINES...)

›       01 WORLD-INDEX-RECORD.
›           05 IDX-ID-NO PIC 9(6).
…[13 more quoted lines elided]…
›           05 IDX-WEB-PAGE PIC X(46).

4. Add the alternate keys into your SELECT...

ALTERNATE RECORD KEY IS FULL-NAME WITH DUPLICATES
ALTERNATE RECORD KEY IS CITY-AND-STATE WITH DUPLICATES

Now, say aloud: "Kel-tip-zix-um"...

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Non-contiguous fields and alternate record keys...

- **From:** "user" <ua-author-11343173@usenetarchives.gap>
- **Date:** 2015-05-17T08:02:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3ec50ec4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0b3ec50ec4-p2@usenetarchives.gap>`
- **References:** `<XnsA499A5A815E7Euserfoobarcominvalid@94.75.214.90> <gap-0b3ec50ec4-p2@usenetarchives.gap>`

```
Pete Dashwood wrote:

› Mr. Mxyztplk wrote:
›› says you's has a record like so
…[26 more quoted lines elided]…
› Pete.
Yeah, I opted for this
000220 SELECT WORLD-FILE ASSIGN TO "flatfile.idx"
000230 ORGANIZATION IS INDEXED
000240 ACCESS MODE IS DYNAMIC
000250 RECORD KEY IS RECORD-NO
000260 ALTERNATE RECORD KEY IS FULL-NAME WITH DUPLICATES
000270 ALTERNATE RECORD KEY IS CITY-STATE-PROVINCE
000280 WITH DUPLICATES.
...
and
...
000430 01 WORLD-INDEX-RECORD.
000440 05 RECORD-NO PIC 9(6).
000450 05 FULL-NAME.
000460 10 FIRST-NAME PIC X(11).
000470 10 LAST-NAME PIC X(13).
000480 05 COMPANY PIC X(30).
000490 05 STREET-ADDRESS PIC X(33).
000500 05 COUNTY PIC X(30).
000510 05 CITY-STATE-PROVINCE.
000520 10 CITY PIC X(30).
000530 10 STATE-PROVINCE PIC X(2).
000540 05 POSTAL-CODE PIC X(8).
000550 05 PHONE-NO PIC X(12).
000560 05 MOBILE-NO PIC X(12).
000570 05 E-MAIL PIC X(43).
000580 05 WEB-PAGE PIC X(46).

I suppose in a way it is 'homework', but the only entities 'grading' it are
youze peepuhls. Thanks again.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
