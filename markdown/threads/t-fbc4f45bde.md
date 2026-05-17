[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Int. Sort with mutiple data records of variable lengths, A question.

_5 messages · 5 participants · 1998-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Int. Sort with mutiple data records of variable lengths, A question.

- **From:** "sreedhar manjigani" <ua-author-17072780@usenetarchives.gap>
- **Date:** 1998-02-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`

```
Hi,

Recently I came across an internal sort file with multiple records and
of variable
lengths. The Sort Definition section looks as below.

SD SORTFILE
RECORD CONTAINS 116 TO 240 CHARACTERS
RECORDING MODE V
DATA RECORDS ARE SORT-REC1
SORT-REC2
SORT-REC3.
01 SORT-REC1 PIC X(240).
01 SORT-REC2 PIC X(144).
01 SORT-REC3.
05 SORT-KEY.
10 SR-VAR1 PIC X(10).
10 SR-VAR2 PIC X(09).
10 SR-VAR3 PIC X(08).
88 SR-RCD1 VALUE SPACES.
10 SK-PAYDATE PIC X(6).
88 SR-RCD2 VALUE SPACES.
05 FILLER PIC X(83).


And in procedure division, the sort definition is as follows.

SORT SORTFILE ON ASCENDING KEY SORT-KEY


Here comes the difficult part. Each record is released from a different
WS- record. The release statements (in various paras might look as
below.)

RELEASE SORTREC1 FROM WS-REC1

RELEASE SORTREC2 FROM WS-REC2

RELEASE SORTREC3 FROM WS-REC3.


WS-REC1 has a completely different layout from WS-REC2 & WS-REC3.
(WS-REC2 & WS-REC3 has the same lay out of SORT-REC3.)

My question is, how is the sort performed? What will be the key for
records 1&2 ? Is the sort performed on the first 33 bytes of all
records?

I might have to change the sort order for fields in sort-key. Any
suggestions on it?


Appreciate any help in this matter.
```

#### ↳ Re: Int. Sort with mutiple data records of variable lengths, A question.

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-02-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbc4f45bde-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`
- **References:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`

```

Sreedhar Manjigani wrote:
› 
› Recently I came across an internal sort file with multiple records and
…[45 more quoted lines elided]…
› suggestions on it?

In general, the sort key definition record is only a template to determine
the position of the key fields. As you probably know, every 01 record under
an FD or SD implicitly redefines the first 01 under the FD or SD. As long as
the key fields are in the same position in each record, it shouldn't matter.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

#### ↳ Re: Int. Sort with mutiple data records of variable lengths, A question.

- **From:** "sco..." <ua-author-4518283@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbc4f45bde-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`
- **References:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`

```

Sreedhar Manjigani wrote:

› Hi,
› 
…[11 more quoted lines elided]…
› 

You can have as many different record formats sorted at the same time.
However, the sort key position and length have to be the same in all
records.
```

#### ↳ Re: Int. Sort with mutiple data records of variable lengths, A question.

- **From:** "rwhi..." <ua-author-17074735@usenetarchives.gap>
- **Date:** 1998-02-10T18:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbc4f45bde-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`
- **References:** `<6bi251$dpg@bgtnsc03.worldnet.att.net>`

```

In article <6bi251$d.··.@bgt··t.net>,
Sreedhar Manjigani wrote:
› 
› 
…[83 more quoted lines elided]…
› 
            &nbs
p;             
             &n
bsp;          
› SORT-REC2
›
            &nbs
p;             
             &n
bsp;          
› SORT-REC3.
›        01 
…[8 more quoted lines elided]…
› 
            &nbs
p; 
› 10  SR-VAR1       PIC   
› X(10).
›
            &nbs
p; 
› 10  SR-VAR2       PIC   
› X(09).
›
            &nbs
p; 
› 10  SR-VAR3       PIC   
› X(08).
›
            &nbs
p;       
Please read about implicit redefinitions that occur in FD and SD entries. This
is in the Language Reference Manual.

Each of the record definitions actually occupy the same storage. The
different record lengths are passed into sort. In MVS, these are passed
as variable length RDW's. No record may be shorter than the offset of
that is furthest into the record definition.

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

##### ↳ ↳ Re: Int. Sort with mutiple data records of variable lengths, A question.

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-02-10T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbc4f45bde-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fbc4f45bde-p4@usenetarchives.gap>`
- **References:** `<6bi251$dpg@bgtnsc03.worldnet.att.net> <gap-fbc4f45bde-p4@usenetarchives.gap>`

```

In article <6bi251$d.··.@bgt··t.net>,
Sreedhar Manjigani wrote:

› Hi,
› 
…[42 more quoted lines elided]…
› 
All three sort records occupy the same storage area (see REDEFINES).
The sort will be performed with the first 33 bytes as you suggested
above, no matter which record layout was released, or which you
return.

› I might have to change the sort order for fields in sort-key. Any
› suggestions on it?
›
› Appreciate any help in this matter.
›

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
