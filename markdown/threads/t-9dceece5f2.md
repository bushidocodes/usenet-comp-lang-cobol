[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Algorithm for Page Up and Page Down logic for COBOL

_13 messages · 6 participants · 2005-09_

---

### Algorithm for Page Up and Page Down logic for COBOL

- **From:** "PradeepR" <pradeep.ravle@gmail.com>
- **Date:** 2005-09-05T21:33:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com>`

```
Has anyone worked on the page up and page down logic which has been
implemented in COBOL. Thanks in advance for any hints on the approach.
```

#### ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-09-06T11:57:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vfTe.1056$jE2.954@newssvr19.news.prodigy.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com>`

```
"PradeepR" <pradeep.ravle@gmail.com> wrote in message
news:1125981201.415165.238920@g47g2000cwa.googlegroups.com...
> Has anyone worked on the page up and page down logic which has been
> implemented in COBOL. Thanks in advance for any hints on the approach.

???

"page up" and "page down" are not COBOL concepts, so it could not have been
"implemented in COBOL"

However, many of us have written code which converts specific user actions
into a *logical* page up or page down, sometimes with keystrokes, sometimes
with a pointing device.

And 'what' is supposed to happen on 'page up' or 'page down' depends a lot
on the application.. like is this an application where you have built a
series of screens, each of which is presented to the user as a logical page?
(Example: The "Tour" application at http://www.providerpaymentpartner.com,
click on "tour" link). Or is this a list of text lines, like a text viewer
or editor (e.g, notepad)?  What environment, and what user action triggers a
logical 'page up' or 'page down' action?

'fraid you haven't supplied anywhere near enough info to get you started..
except to recognize that 'page up' and 'page down' are logical actions,
rather than physical actions: User input = change display.

MCM
```

##### ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** docdwarf@panix.com
- **Date:** 2005-09-06T08:59:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfk3ra$kdr$1@panix5.panix.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com>`

```
In article <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:

[snip]

>And 'what' is supposed to happen on 'page up' or 'page down' depends a lot
>on the application.. like is this an application where you have built a
…[3 more quoted lines elided]…
>or editor (e.g, notepad)?

Ahhhhhhh, yes... I recall long, tortured debates about this.  For example: 
given 24 lines per screen with four lines reserved for the header (line 1 
= company name (BUMF, INC.), line = 2 inquiry name (Online Customer SNAFU 
View), line 3 = day/date/time, line 4 = blank/dashes/underlines) and two 
lines reserved for the footer (line 23 = instructions (PF1 = Help, PF3 = 
End, PF7/PF8 = PgUp/PgDn), line 24 = error msgs (KEY UNDEFN'D or something 
equally helpful) you have 18 lines left for display.  Given a full screen 
of something like:

01) ABLE
02) BAKER
03) CHARLIE
...
18) ROMEO

... and the user pages down... what should be the first entry on the next 
screen?  Some say that since screen real-estate is very scarce it should 
be the next entry, others say that in order to maintain continuity the 
last entry on the first page should be repeated as the first entry on the 
second page.  Me, I was of the latter school; in paging down the last 
should become first and in paging up the first last as it seems to cut 
down on calls of 'Hey, what happened to (x) entry, I *know* that they're 
out there!'

In the case above... what if there is, in actuality, no Sierra?  The user 
pages down and the first entry is

01) TANGO

... and the user says 'What happened to Sierra?  I *know* they're out 
there!'... and then the coder gets called and has to fire up FileAid (if 
it is available) to determine that Sierra, in fact, was deleted in last 
week's purge of inactive accounts... in my experience when the second 
screen shows

01) ROMEO
02) TANGO

... such calls happen less often.

(Next week's topic of discussion for The Ergonomics of Screen Design is 
'Flagging Errors: Inverse Video, Flashing - Emphatic Indicator or Sadist's 
Tool?')

DD
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-09-06T13:46:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u4hTe.320$au2.112@newssvr17.news.prodigy.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com> <dfk3ra$kdr$1@panix5.panix.com>`

```
<docdwarf@panix.com> wrote in message news:dfk3ra$kdr$1@panix5.panix.com
wrote...
> Ahhhhhhh, yes... I recall long, tortured debates about this.

[ about sixty lines of *newsgroup* torture]

"Ask YOUR doctor if Valium is right for you...."

MCM
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2005-09-06T10:58:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfkarf$dkk$1@panix5.panix.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com> <dfk3ra$kdr$1@panix5.panix.com> <u4hTe.320$au2.112@newssvr17.news.prodigy.com>`

```
In article <u4hTe.320$au2.112@newssvr17.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@panix.com> wrote in message news:dfk3ra$kdr$1@panix5.panix.com
>wrote...
…[4 more quoted lines elided]…
>"Ask YOUR doctor if Valium is right for you...."

My apologies, Mr Mattias, if questions about screen design strike you as 
'*newsgroup* torture' (emphasis original); you might want to consider 
going back into management.

DD
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-06T15:16:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<epiTe.14266$xl6.10298@tornado.tampabay.rr.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com> <dfk3ra$kdr$1@panix5.panix.com>`

```
DD:

I agree.  I'm of course SOOOO lazy that I cannot be bothered to find out 
what the default is for ISPF "PAGE" option....so I always set it to "CSR" so 
that I know _exactly_ what it's doing....My fear is that it is again costing 
me more effort to be anal retentive than to press F1 and read the help :-)

JCE

TOP Post Only
<docdwarf@panix.com> wrote in message news:dfk3ra$kdr$1@panix5.panix.com...
> In article <3vfTe.1056$jE2.954@newssvr19.news.prodigy.com>,
> Michael Mattias <michael.mattias@gte.net> wrote:
…[55 more quoted lines elided]…
> DD
```

#### ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-06T12:55:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126036540.776389.218990@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com>`

```
> page up and page down logic

Page down for a file of records is relatively easy, you just store the
last line number/record key and then use this to position the file to
read/search forward through the file.

The hard part is the page up.

You could store the first number/key of the current page and use this
to postion the file and then use read previous if this is available,
displaying from bottom to top. Again, store away the key/number of the
first line and last line.

I usually do this with a table of 'page starts', say occurs 100. With
each page display I store the key of the last line in the next element
of this table.  A Page down will use the key to start the file and read
the next few records to the screen.  A Page Up will subtract 2 from the
table index (and check it is at least 1) and display the page.

If the user pages down beyond the end of the array (ie 100 pages) it
will still continue to display correctly but a page up will return to
page 99.  It does have the advantage of being able to go back directly
to a specific page and it also works reasonably well when seaching.
```

#### ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** Dave <MyFakeEmail@EndSpam.com>
- **Date:** 2005-09-06T20:05:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59WdndV1SLlNoYPeRVn_vA@giganews.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com>`

```
> Has anyone worked on the page up and page down logic which has been
> implemented in COBOL. Thanks in advance for any hints on the approach.

Perhaps it would be helpful if you were to first tell us what it is you're
paging up and down. A CICS screen? An ISPF dynamic area? Something else? 
Generally, put the data in a TS queue, table, an RRDS VSAM file etc. and 
roll the record pointer back and forth.
```

##### ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** "PradeepR" <pradeep.ravle@gmail.com>
- **Date:** 2005-09-12T05:31:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126528261.466519.101960@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<59WdndV1SLlNoYPeRVn_vA@giganews.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <59WdndV1SLlNoYPeRVn_vA@giganews.com>`

```
Thanks for the input from all. Here is more detail, I have to develop
an input screen of which will accept 12 rows and 8 columns and fields
this can go upto 999 elements. So there will be more than 1 screens.
Eg.
Heading1
x x x x x x x x
x x x x x x x x
....
             Page 1
After user enters all data he presses F10 and process this data.
I have implemented it now by calculation on table index
1. Initalize row = 3
2. Take input till line no. changes
3. Initialize col no. once line changes
4. Store all this in a single dimension table
Once user presses pageup/down
get the data from the table appropriately.

As I am not showing in update mode it was little easy to handle a bit.
Thanks Richard, Michael, Doc.
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-12T14:35:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg43n1$roo$1@reader1.panix.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <59WdndV1SLlNoYPeRVn_vA@giganews.com> <1126528261.466519.101960@g44g2000cwa.googlegroups.com>`

```
In article <1126528261.466519.101960@g44g2000cwa.googlegroups.com>,
PradeepR <pradeep.ravle@gmail.com> wrote:

[snip]

>Thanks Richard, Michael, Doc.

What's this... thanking me for '*newsgroup* abuse'?  How about a little 
squeal of anquish, then?

You're quite welcome.

DD
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

_(reply depth: 4)_

- **From:** "PradeepR" <pradeep.ravle@gmail.com>
- **Date:** 2005-09-13T01:30:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126600232.989438.321680@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dg43n1$roo$1@reader1.panix.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <59WdndV1SLlNoYPeRVn_vA@giganews.com> <1126528261.466519.101960@g44g2000cwa.googlegroups.com> <dg43n1$roo$1@reader1.panix.com>`

```
I have to say that English is not my first language. I thought there
was quite a bit of good discussion up there. (except the small MCM-DD
screen design discussion skirmish)
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-09-13T12:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5rzVe.410$4T5.131@newssvr17.news.prodigy.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <59WdndV1SLlNoYPeRVn_vA@giganews.com> <1126528261.466519.101960@g44g2000cwa.googlegroups.com> <dg43n1$roo$1@reader1.panix.com> <1126600232.989438.321680@g44g2000cwa.googlegroups.com>`

```
"PradeepR" <pradeep.ravle@gmail.com> wrote in message
news:1126600232.989438.321680@g44g2000cwa.googlegroups.com...
> I have to say that English is not my first language. I thought there
> was quite a bit of good discussion up there. (except the small MCM-DD
> screen design discussion skirmish)

I'll make it bigger next time.

MCM
```

###### ↳ ↳ ↳ Re: Algorithm for Page Up and Page Down logic for COBOL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-09-13T13:15:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg6jdv$cbh$1@reader1.panix.com>`
- **References:** `<1125981201.415165.238920@g47g2000cwa.googlegroups.com> <dg43n1$roo$1@reader1.panix.com> <1126600232.989438.321680@g44g2000cwa.googlegroups.com> <5rzVe.410$4T5.131@newssvr17.news.prodigy.com>`

```
In article <5rzVe.410$4T5.131@newssvr17.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
>"PradeepR" <pradeep.ravle@gmail.com> wrote in message
>news:1126600232.989438.321680@g44g2000cwa.googlegroups.com...
…[4 more quoted lines elided]…
>I'll make it bigger next time.

As the Germans used to say, Mr Mattias... qualitas, non quantitas.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
