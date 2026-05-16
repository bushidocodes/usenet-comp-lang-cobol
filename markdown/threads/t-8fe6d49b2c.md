[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXTERNAL clarification

_23 messages · 8 participants · 2006-07_

---

### EXTERNAL clarification

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-15T09:57:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9a766$3a4$03$1@news.t-online.com>`

```
According to 2002/2008 standards :
"The EXTERNAL clause specifies that a data item or a file connector is 
external."

Therefore is this legal -
01  WHATEVER.
       03  FLD1  PIC .....
       03  FLD2  PIC ...  EXTERNAL.

Or should the standard(s) be staing "data record".

Roger
```

#### ↳ Re: EXTERNAL clarification

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-15T08:15:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bhn8uds3uih19@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e9a766$3a4$03$1@news.t-online.com...
> According to 2002/2008 standards :
> "The EXTERNAL clause specifies that a data item or a file connector is
…[7 more quoted lines elided]…
> Or should the standard(s) be staing "data record".

For those who may wish to skp the detailed explanation,
the short answer is: No, to both.

13.16.20 EXTERNAL clause,
"The EXTERNAL clause specifies that a data item or a
file connector is external. The constituent data items and
group data items of an external data record are available
in a run unit to every runtime element that describes the
record as external."

13.16.20.2 [EXTERNAL clause] Syntax rules,
"1) The EXTERNAL clause may be specified only in file
description entries or in record description entries in the
working-storage section."

13.10 Record description entry,
"A record description entry consists of a set of data description
entries, the first of which shall have level-number 1,
that describe the characteristics of a particular record. Any
data item that has been described with level-number 1
is a record."
[Later, 77-level data description entry is described as a case
of record description entry.]

Applying SR 1, the example has a syntax error.

Changing the example to:

01  WHATEVER EXTERNAL.
       03  FLD1  PIC ....
       03  FLD2  PIC ....

and applying the definition "4.56 data item: A unit of data
defined by a data description entry or resulting from the
evaluation of an identifier." and substituting "WHATEVER"
for "data item" in the first sentence of the introduction; it
may be understood that "The EXTERNAL clause specifies
that WHATEVER ... is external."

The second sentence of the introduction applies to FLD1,
FLD2, etc., as "constituent data items and group data items
of an external data record".

In my opinion, there is insufficient reason, in this case, to
change the standard(s) from "data item" to "data record".
```

##### ↳ ↳ Re: EXTERNAL clarification

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-15T15:33:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9aqs9$tss$00$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com>`

```
Well Rick and Robert, I would beg to differ about the wording in SR1 -
"IN file description entries or IN record description entries".
It does not say "ON".
In my copies of 2002/2008 it is 13.16.21
So either 13.16.21 is ambiguous or 13.16.21.2 (1) is ambiguous
or both.
It is sort of implied by 13.16.21.3 but not explicitely.

Why not simply refer to the 01 level (and 77 for WS).

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12bhn8uds3uih19@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[59 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-15T11:38:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bi34hl2ctg0a2@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e9aqs9$tss$00$1@news.t-online.com...
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
> news:12bhn8uds3uih19@corp.supernews.com...
> >
> > "Roger While" <simrw@sim-basis.de> wrote in message
> > news:e9a766$3a4$03$1@news.t-online.com...
[snip]
> > 13.16.20.2 [EXTERNAL clause] Syntax rules,
> > "1) The EXTERNAL clause may be specified only in file
…[12 more quoted lines elided]…
> > Applying SR 1, the example has a syntax error.
[snip]
> Well Rick and Robert, I would beg to differ about the wording in SR1 -
> "IN file description entries or IN record description entries".
…[6 more quoted lines elided]…
> Why not simply refer to the 01 level (and 77 for WS).

From 13.10, shown above, one could reason that when
an EXTERNAL clause appears "in" data description entries
with level-numbers of 2 - 49, it (the clause) would not be "in"
a record description entry, since "A record description entry
consists of a set of data description entries, the first of which
shall have level-number 1". This would seem to imply that an
EXTERNAL clause could appear only in a data description
entry whose level-number is 1 (or, for other reasons, 77).

Furthermore, it is only the clauses at level-number 1, that
"describe the characteristics of a particular record." The
EXTERNAL clause describes the characteristics of a
record. This too would seem to imply that an EXTERNAL
clause could appear only in a data description entry whose
level-number is 1 (or, for other reasons, 77).

However, implication makes for wonderful guessing games.

The following was adopted from the GLOBAL clause and
modified as a possible substitute for the EXTERNAL clause,
syntax rule 1. Perhaps this would be more to your liking.

1) The EXTERNAL clause may be specified only in the following
entries:
a) A data description entry whose level-number is 1 or 77 that is
    specified in the working-storage section.
b) A file description entry.
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 4)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-15T21:40:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9bgb8$6mp$01$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12bi34hl2ctg0a2@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[61 more quoted lines elided]…
>
Well exactly - What's wrong with that ?.
There is enough of this "lawyer" english that crept into the standards.
If, after 38 years of Cobol and being an Englishman, even I have
difficulty deciphering what is meant in these standards, then there
is something very wrong going on.

Roger
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-15T20:03:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KSbug.190360$Mn5.34306@pd7tw3no>`
- **In-Reply-To:** `<e9bgb8$6mp$01$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com>`

```
Roger While wrote:
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
> news:12bi34hl2ctg0a2@corp.supernews.com...
…[77 more quoted lines elided]…
> 
Don't get us going on this one Roger, i.e. 'legalese'. Rick pointed out 
that some of Bill's examples didn't work with Micro Focus. Now 
*assuming* what Bill showed were three valid options, apart from a brief 
introduction, the 'legalese' could have been replaced by Bill's three 
examples.

Before he had to quit - recall Chuck Steven's reply to me on this one. 
Even though he was the newest to the J4 team, he got taken in hook line 
and sinker by the legalese approach. I really would be curious to know 
the reaction of vendor developers who actually have to translate the 
'legal' definitions into workable compiler code - and not the people who 
do/did front for them at J4.

Cor mate. Why can't they write in bleedin' English !

Jimmy
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-07-17T01:27:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hut5vF1chr9U1@individual.net>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e9bgb8$6mp$01$1@news.t-online.com...
>
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
…[69 more quoted lines elided]…
> is something very wrong going on.

Gee, Roger... d'you think? ;-)

You should have seen the battle that raged over this very point (the 
verbosity and legalese of the last standard), in this forum, some time ago.

Never mind, water under the bridge. I smile to see that someone else has 
exactly the same problem I had with it some years back.

I don't think any lessons were learned because the new standard is just as 
bad.

Makes you wonder if a standard serves any purpose at all really... It 
certainly doesn't if you can't USE it...

Pete.
>
> Roger
>
>
>
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-16T13:24:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bktp78gos372d@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e9bgb8$6mp$01$1@news.t-online.com...
>
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
> news:12bi34hl2ctg0a2@corp.supernews.com...
[snip]
> > The following was adopted from the GLOBAL clause and
> > modified as a possible substitute for the EXTERNAL clause,
…[13 more quoted lines elided]…
> is something very wrong going on.

Upon further investigation, I can find no intent by J4
to allow the EXTERNAL clause to be used with
level-number 77; but that further investigation revealed
three distinct patterns for expressing the same idea,
one of which contains a usage that is inconsistent with
the rest of the standard. It also revealed a rule that
appears to be incorrect.

Barring unforeseen problems, I will begin working on
the formal document (defect report?) tomorrow; but
I am not certain where to send it (not having done this
since the 2002 standard).
```

###### ↳ ↳ ↳ Defect Reports(was: EXTERNAL clarification

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-16T19:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5iwug.120284$RW2.27442@fe05.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com> <12bktp78gos372d@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12bktp78gos372d@corp.supernews.com...
>
<snip>
> Barring unforeseen problems, I will begin working on
> the formal document (defect report?) tomorrow; but
…[4 more quoted lines elided]…
>

two options:

1) If you want to report it against the US (ANSI) adoption of the ISO Standard, 
then send it to INCITS.

2) If you want to report it against the "base" ISO Standard, you can just send 
it to Don Schricker at his "cox" email ID (for J4 processing).

If you have any problems with this, let me know.
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 6)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-17T08:24:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9fafg$6gk$01$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com> <12bktp78gos372d@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12bktp78gos372d@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[29 more quoted lines elided]…
>

Why not 77 ?
77 is just a special case of 01.

Roger
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-17T04:52:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bmk3ehnnc59f1@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com> <12bktp78gos372d@corp.supernews.com> <e9fafg$6gk$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e9fafg$6gk$01$1@news.t-online.com...
>
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
> news:12bktp78gos372d@corp.supernews.com...
[snip]
> > Upon further investigation, I can find no intent by J4
> > to allow the EXTERNAL clause to be used with
…[3 more quoted lines elided]…
> 77 is just a special case of 01.

I don't disagree; but there seems to be an problem that
occurred between the 1985 and 2002 standards.

The Micro Focus LRMs often quote the standard
verbatim, only changing text where required to reflect
that which is implementor-defined. Following are four
quotes from the LRM for Micro Focus 3.2, all marked
as ANS85, each followed by the text from WD 1.6.

1 -----
"A level 01 data description in the Working-Storage
Section determines the internal or external attribute of
the data record and it subordinate data items."

A level 1 data description entry in the working-storage
section determines the internal or external attribute of the
record and its subordinate data items.

2 -----
"5. The EXTERNAL clause can be specified only in
data description entries in the Working-Storage Section
whose level-number is 01."

[Missing from WD 1.6 and ISO 1989:2002]

3 -----
"1. The EXTERNAL clause can be specified only in
file description entries, or in record description entries
in the Working-Storage Section."

1) The EXTERNAL clause may be specified only in file
description entries or in record description entries in the
working-storage section.

4 -----
"2. In the same program, the data name specified as the
subject of the entry whose level-number is 01 that includes
the EXTERNAL clause must not be the same data-name
specified for any other data description entry which includes
the EXTERNAL clause."

2) In the same source element, the externalized name of
the subject of the entry that includes the EXTERNAL
clause shall not be the same as the externalized name of
any other entry that includes the EXTERNAL clause.
-----

If Micro Focus quoted the 1985 standard, accurately,
then a key rule that would have removed the uncertainty
was dropped during the creation of the 2002 standard.
That being the case, would establish an intent that the
EXTERNAL clause not appear on a data description
entry whose level-number is 77. On the other hand, were
there an intent to allow the EXTERNAL clause with
level-number 77, the first quote would not have retained
a reference to level-number 1.
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 8)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-17T12:28:14+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9foo2$3mg$01$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com> <12bi34hl2ctg0a2@corp.supernews.com> <e9bgb8$6mp$01$1@news.t-online.com> <12bktp78gos372d@corp.supernews.com> <e9fafg$6gk$01$1@news.t-online.com> <12bmk3ehnnc59f1@corp.supernews.com>`

```
Ah, OK Rick, now I understand.

Roger

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:12bmk3ehnnc59f1@corp.supernews.com...
>
> "Roger While" <simrw@sim-basis.de> wrote in message
…[70 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-15T17:22:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gv9ug.220751$SQ6.150233@fe09.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <12bhn8uds3uih19@corp.supernews.com> <e9aqs9$tss$00$1@news.t-online.com>`

```
Did you see ('02 Standard),

Page 251
   "A level 1 data description entry in the working-storage section determines 
the internal or external attribute of the record and its subordinate data 
items."
```

#### ↳ Re: EXTERNAL clarification

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-07-15T05:29:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152966590.985835.303910@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<e9a766$3a4$03$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com>`

```

Roger While wrote:
> According to 2002/2008 standards :
> "The EXTERNAL clause specifies that a data item or a file connector is
…[9 more quoted lines elided]…
> Roger

I think you will find that what you have quoted is from the lead in to
the EXTERNAL clause (13.16.20), when you look at Syntax Rule 1 (SR1)
you will find that it can only be specified for record and file
descriptions, i.e. must be at the FD or 01 level.  You may have a point
in that the lead-in could also have stated the same thing, though
"lead-in"s are usually intended to give a broad description rather than
details. You could make a suggestion to the  J4 committee to tidy this
up.

Robert
```

#### ↳ Re: EXTERNAL clarification

- **From:** Frank Swarbrick <infocat@earthlink.net>
- **Date:** 2006-07-15T16:06:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net>`
- **In-Reply-To:** `<e9a766$3a4$03$1@news.t-online.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com>`

```
Roger While wrote:
> According to 2002/2008 standards :
> "The EXTERNAL clause specifies that a data item or a file connector is 
…[7 more quoted lines elided]…
> Or should the standard(s) be staing "data record".

No answer to this, other than I agree with the others that EXTERNAL 
should be allowed only at the 01 or 77 level.

In a related matter...in your email to me you state "Hmm, looking at 
this again, I think the problem then was that not only
can you have EXTERNAL on an FD, you can also have an EXTERNAL
on the following record-description. (Implied when on the FD)."

Is your meaning that you can have EXTERNAL defined on the 01 level for 
the record-descriptior of a FILE-SECTION item?  Or are you simply 
stating that by making the file-descriptor EXTERNAL then its related 
records are implicitly external?  I would agree with the latter, but not 
with the former.

Frank
```

##### ↳ ↳ Re: EXTERNAL clarification

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-15T17:17:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xq9ug.240001$wA1.57510@fe03.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net>`

```
To clarify, the following three "variations" are all valid (and have been since 
the '85 Standard).

Fd  This-File External.
01 This-Rec  Pic X(100).

   ***

FD  This-File.
01  This-Rec Pic X(100) External.

   ***

FD  This-File External.
01  This-Rec  Pic X(100) External.

  ***

The differences (and even the usefulness) are minimal, but they do exist.
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-15T15:36:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bih72cmf9ns33@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:Xq9ug.240001$wA1.57510@fe03.news.easynews.com...
> To clarify, the following three "variations" are all valid (and have been
since
> the '85 Standard).
>
…[11 more quoted lines elided]…
> 01  This-Rec  Pic X(100) External.

The last two seem to be invalid for Micro Focus. Only the
last is shown here.

* Micro Focus COBOL Version 3.2.24   L2.5 revision 000 15-Jul-06 15:31 Page
1
*                                 C:\CBL-CHAL\EXT-FILE.CBL
* Options: WB EDITOR(MF) LIST() NOOSVS ANS85 NOVSC2 CSI XNIM ENSUITE(2)
CONFIRM
     1$set ans85 flag"ans85" flagas"s"
     2 identification division.
     3 program-id. ext-file.
     4 environment division.
     5 input-output section.
     6 file-control.
     7     select in-file assign to "afile.dat".
     8 data division.
     9 file section.
    10 fd in-file external.
    11 01 in-file-record pic x(80) external.
* 241-S************************************
**    Only allowed in WORKING-STORAGE section
    12 procedure division.
* 205-S*********
**    RECORD missing or has zero size
    13 begin.
    14     read in-file
    15       at end
    16         continue
    17     end-read
    18     exit program.
    19 end program ext-file.
* Micro Focus COBOL Version 3.2.24   L2.5 revision 000
* Last message on page: 1
*
* Total Messages:     2
* Unrecoverable :     0                    Severe  :     2
* Errors        :     0                    Warnings:     0
* Informational :     0                    Flags   :     0
* Data:         652     Code:         211
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 4)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2006-07-15T22:53:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kleug.4935$vO.3302@newsread4.news.pas.earthlink.net>`
- **In-Reply-To:** `<12bih72cmf9ns33@corp.supernews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com> <12bih72cmf9ns33@corp.supernews.com>`

```
Rick Smith wrote:
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
> news:Xq9ug.240001$wA1.57510@fe03.news.easynews.com...
…[59 more quoted lines elided]…
> * Data:         652     Code:         211

Ditto for COBOL for VSE/ESA 1.1.1:
IGYDS1326-S THE "EXTERNAL" CLAUSE WAS SPECIFIED FOR A DATA ITEM WHOSE 
LEVEL-NUMBER WAS NOT AN 01 IN THE "WORKING-STORAGE SECTION".  THE 
"EXTERNAL" CLAUSE WAS DISCARDED.

Frank
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-16T19:09:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4awug.206556$LI3.49716@fe12.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com> <12bih72cmf9ns33@corp.supernews.com>`

```
I must have been confusing it with GLOBAL.  Does that compile cleanly (for all 
3)?
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 5)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2006-07-16T20:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yrxug.768$157.438@newsread3.news.pas.earthlink.net>`
- **In-Reply-To:** `<4awug.206556$LI3.49716@fe12.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com> <12bih72cmf9ns33@corp.supernews.com> <4awug.206556$LI3.49716@fe12.news.easynews.com>`

```
William M. Klein wrote:
> I must have been confusing it with GLOBAL.  Does that compile cleanly (for all 
> 3)?
> 

This works on COBOL/VSE.  GLOBAL for both the FD and the 01 and just 
GLOBAL for the FD appear to work exactly the same.  (In other words, 
GLOBAL at the FD level implicitly makes the related 01 levels global.)

If just the 01 level is declared GLOBAL then only the data area itself 
is global, while the file is not.  This, given the following...

IDENTIFICATION DIVISION.
PROGRAM-ID.    GLOBTST.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
     SELECT MYFILE ASSIGN TO MYFILE.

DATA DIVISION.
FILE SECTION.
FD  MYFILE                      GLOBAL.
01  MYREC                       PIC X(80) GLOBAL.

PROCEDURE DIVISION.
     CALL 'NESTED'
     CLOSE MYFILE
     STOP RUN.


IDENTIFICATION DIVISION.
PROGRAM-ID.    'NESTED'.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  LREC                        PIC X(40).

PROCEDURE DIVISION.
     OPEN I-O MYFILE
     READ MYFILE INTO LREC
     MOVE 'ABCD' TO MYREC
     WRITE MYREC
     EXIT PROGRAM.
END PROGRAM 'NESTED'.

END PROGRAM 'GLOBTST'.

If MYFILE was *not* declared global then the OPEN, READ and WRITE 
statements would not be valid (in the subprogram), while the MOVE 
statement still would be.

This all seems correct to me.  Is there some difference I should be 
expecting with "FD GLOBAL/01 GLOBAL" versus just "FD GLOBAL"?


Frank
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-16T23:38:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6Aug.284326$lC7.189540@fe01.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com> <12bih72cmf9ns33@corp.supernews.com> <4awug.206556$LI3.49716@fe12.news.easynews.com> <Yrxug.768$157.438@newsread3.news.pas.earthlink.net>`

```
Check out the (obscure) GLOBAL phrase in I-O Declaratives.

Also, a GLOBAL for the "record" allows a WRITE (or REWRITE) even if you can't 
OPEN, CLOSE, OR READ it. (Strange but true)
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

_(reply depth: 7)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2006-07-17T00:43:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p2Bug.9109$PE1.7960@newsread2.news.pas.earthlink.net>`
- **In-Reply-To:** `<g6Aug.284326$lC7.189540@fe01.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com> <12bih72cmf9ns33@corp.supernews.com> <4awug.206556$LI3.49716@fe12.news.easynews.com> <Yrxug.768$157.438@newsread3.news.pas.earthlink.net> <g6Aug.284326$lC7.189540@fe01.news.easynews.com>`

```
William M. Klein wrote:
> Check out the (obscure) GLOBAL phrase in I-O Declaratives.

Sorry, Bill, I think you'll have to lead this horse to water...

Are you referring to the GLOBAL phrase of the USE statement?  Even if 
so, I'm still not sure to what you are referring.


> Also, a GLOBAL for the "record" allows a WRITE (or REWRITE) even if you can't 
> OPEN, CLOSE, OR READ it. (Strange but true)

Hmm, I can see that.  Weird, and I can't imagine anyone ever using it, 
but it seems to be allowed "under the letter of the law".

Frank
```

###### ↳ ↳ ↳ Re: EXTERNAL clarification

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2006-07-15T22:44:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdeug.4932$vO.513@newsread4.news.pas.earthlink.net>`
- **In-Reply-To:** `<Xq9ug.240001$wA1.57510@fe03.news.easynews.com>`
- **References:** `<e9a766$3a4$03$1@news.t-online.com> <Pn8ug.8514$PE1.3481@newsread2.news.pas.earthlink.net> <Xq9ug.240001$wA1.57510@fe03.news.easynews.com>`

```
William M. Klein wrote:
> To clarify, the following three "variations" are all valid (and have been since 
> the '85 Standard).
…[16 more quoted lines elided]…
> The differences (and even the usefulness) are minimal, but they do exist.

Hmm, so what are the differences?  And where in the standard do you find 
the language that supports the usage of EXTERNAL on an 01 level data 
item in the file section?  (Not that I don't believe you.  I just cannot 
find it.)

Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
