[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP!

_5 messages · 5 participants · 1997-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HELP!

- **From:** "chu kin sun" <ua-author-714865@usenetarchives.gap>
- **Date:** 1997-12-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34A95756.75A0C240@asiaonline.net>`

```

I am studying cobol lang.
I found some diffcuilty in cobol.
1. i want repeatly to read some records, but i want each reading is
start from 1st record.
is it close the file and open again to read from start ?
2. does the search command uses in array or not ?
3. I want more workable examples(COBOL-85) to learn a basic technique in
cobol lang.
Does anyone can help me ?
Thanks a lot !
Best Regards,
Chu Kin Sun.
ch··.@asi··e.net
```

#### ↳ Re: HELP!

- **From:** "joel brighton" <ua-author-17072267@usenetarchives.gap>
- **Date:** 1997-12-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bd2d7b35d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34A95756.75A0C240@asiaonline.net>`
- **References:** `<34A95756.75A0C240@asiaonline.net>`

```

Chu Kin Sun wrote:
›
› 1. i want repeatly to read some records, but i want each reading is
› start from 1st record.
› is it close the file and open again to read from start ?

Yes. However, depending upon the size of your file (number of records,
record length) and the number of times you re-read the same file, you
may want to consider reading the input records into a working storage
table.

› 2. does the search command uses in array or not ? 
 
› Yes, the SEARCH statement does use an array/table.  
 
› 3. I want more workable examples(COBOL-85) to learn a basic technique in
› cobol lang. 

There are many on-line sources - the COBOL Center at
http://www.infogoal.com/cbd/cbdhome.htm is a good starting point. As
with any language, learning COBOL is not just about the syntax; program
design is just as important. I would suggest that once you understand
the basic language constructs you should do some research on good
program design practices. (I personnaly use a sub-set of JSP (Jackson's
Structured Programming) but there are numerous other techniques).

› Does anyone can help me ?
› Thanks a lot !
› Best Regards,
› Chu Kin Sun.
› ch··.@asi··e.net
```

##### ↳ ↳ Re: HELP!

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1997-12-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bd2d7b35d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2bd2d7b35d-p2@usenetarchives.gap>`
- **References:** `<34A95756.75A0C240@asiaonline.net> <gap-2bd2d7b35d-p2@usenetarchives.gap>`

```

Charla J. Williams wrote:
› 
› Joel Brighton answered Chu Kin Sun:
…[13 more quoted lines elided]…
› Regards, Charla

Binary searches are not always more efficient than a sequential search.
There is more overhead in the loop setup for a binary search than for a
sequential search. The rule of thumb used to be to use binary for 1more
than 10 entries.

BTW, when I studied sort algorithms (boy was that a long time ago) most
of the implementations I saw would switch to a simple algorithm
(bubble?) for segments of 10 or fewer records.

Perhaps someone else knows what the current cutoff is today. On the
otherhand, it really ought not to be dependent upon processor speed.
Wayne L. Beavers         mailto:Way··.@Bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"Transforming Legacy Applications"
```

#### ↳ Re: HELP!

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-29T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bd2d7b35d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34A95756.75A0C240@asiaonline.net>`
- **References:** `<34A95756.75A0C240@asiaonline.net>`

```

Check out 'The COBOL Center' at http://www.infogoal.com/cbd/cbdhome.htm.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

Chu Kin Sun  wrote:
> I am studying cobol lang.
> I found some diffcuilty in cobol.
…[10 more quoted lines elided]…
> ch··.@asi··e.net
```

#### ↳ Re: HELP!

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-12-30T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bd2d7b35d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34A95756.75A0C240@asiaonline.net>`
- **References:** `<34A95756.75A0C240@asiaonline.net>`

```

On Wed, 31 Dec 1997 04:19:34 +0800, Chu Kin Sun
wrote:

› I am studying cobol lang.
› I found some diffcuilty in cobol.
…[10 more quoted lines elided]…
› ch··.@asi··e.net
It looks like several useful tips have been offered you, Chu. I can
only offer to a student... sometimes the best way to learn is to
describe what end result you're trying to achieve and how you think it
should be done. That lets us understand the business need - and also
assures us that you've attempted to solve it yourself....

typically, rereading a file from the beginning is questionable and
begs the question of 'what is the goal?' good luck in your
studies... david

David d.s··.@ix.··m.com
____________________________________
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
