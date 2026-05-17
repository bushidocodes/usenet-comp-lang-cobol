[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting from COBOL to COBOL II - What's involved ?

_6 messages · 5 participants · 1996-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Converting from COBOL to COBOL II - What's involved ?

- **From:** "jkumar..." <ua-author-4951419@usenetarchives.gap>
- **Date:** 1996-04-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`

```
I have been assigned to investigate on what is involved in converting from
COBOL to COBOL II.

Do we have to make changes to the programs or just recompile etc.?

Are there any tools available to help with conversion?

I will appreciate comments from people who are going through this process
or have gone through it or doing research on it.

Thanks in advance.

JK.
```

#### ↳ Re: Converting from COBOL to COBOL II - What's involved ?

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f94cbaea10-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`
- **References:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`

```
jku··.@ocb··c.edu (JK) wrote:
› I have been assigned to investigate on what is involved in converting from
› COBOL to COBOL II.
…[10 more quoted lines elided]…
› JK.

Woops! I fat-fingered it there, and accidentally sent an unfinished note
to you.

Anyway, if you are interested, I could send you source code for a
converter, but it is oriented towards an IBM mainframe COBOL II
environment. Let me know.

There are a lot of convenient features in COBOL II once you get there.
You can use VALUE clauses under an OCCURS clause. You get explicit scope
terminators, the EVALUATE case structure, and SET condition-name TO TRUE.

My experience suggests that it might be possible to write an OS/VS COBOL
program that would compile cleanly under COBOL II, but it would be very
unlikely to occur in real life. There are several books on COBOL II,
unfortunately I seem to have left all of them at work. There is a book
by a fellow named Kirk which is very good at describing the differences
in terms of what was dropped from old cobol, what works differently in
COBOL II (not very much, mostly related to the effects of certain compile
options), and what is new in COBOL II. You will most likely be concerned
with the first two categories.

Another book which would be helpful is COBOL/370 (for VS COBOL and COBOL
II programmers) by Harvey Bookman, published by McGraw-Hill. It covers
the differences pretty well. It's available through computer book clubs
and I have also seen it (or his previous COBOL II book) in my local
Barnes & Noble store. It should be orderable.

I found that one just now, and looking through it I forgot to mention
that "ON 1 ..." is no longer supported. It wasn't used much where I work
now, but was extremely common at another shop where I worked.

Good luck!

Arnold Trembley
Software Engineer I
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Converting from COBOL to COBOL II - What's involved ?

- **From:** "david_..." <ua-author-3348436@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f94cbaea10-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`
- **References:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`

```
In article <4ku7mf$o.··.@oac··c.edu>,
jku··.@ocb··c.edu says...
› 
› I have been assigned to investigate on what is involved in converting from
…[11 more quoted lines elided]…
› JK.
You should really look at going to cobol/mvs as cobol II is going to
be phased out. Basically, the same things you'd be changing for cobol II,
are needed for cobol/mvs.
```

#### ↳ Re: Converting from COBOL to COBOL II - What's involved ?

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f94cbaea10-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`
- **References:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`

```
jku··.@ocb··c.edu (JK) wrote:
› I have been assigned to investigate on what is involved in converting from
› COBOL to COBOL II.
…[10 more quoted lines elided]…
› JK.

Where I work we went thru a conversion of a large CICS application from
COBOL to COBOL II. You don't say whether you are an IBM mainframe shop,
which could easily change the direction of my comments.

If you have a COBOL II compiler available now, you could try to compile a
program without any changes. Generally you will find that the program
will not compile without some changes.

My experience was that IBM special registers (CURRENT-DATE, TIME-OF-DAY)
are no longer supported, and you have to convert to using ACCEPT ...
FROM. Also just about every clause in the IDENTIFICATION DIVISION, other
than PROGRAM-ID, is now obsolete and should be commented out with an
asterisk in column 7 if you want to keep it in the program.

In the IBM world, EXAMINE and TRANSFORM are no longer supported. INSPECT
replaces EXAMINE, but you can't just substitute INSPECT for EXAMINE,
because some options of the rest of the statement have a different
syntax.

For CICS programs, if you use SERVICE RELOAD to reference 01 records in
the LINKAGE SECTION, you will have to move your BLL cell pointers from
linkage section to working-storage section and change all your SERVICE
RELOAD's to "SET ADDRESS OF linkage-section-01 TO pointer-name".

In COBOL II you should consider using CONTINUE everywhere you used to use
NEXT SENTENCE. But be careful, CONTINUE is a true no-op instruction,
while NEXT SENTENCE is an implied GOTO to the sentence following the next
period!

IBM has a product called CCCA for coverting OS/VS COBOL to COBOL II, but
my company didn't buy. So I wrote a converter in COBOL II. It handles
SERVICE RELOAD, but does not convert TRANSFORM (you need to write logic
to replace a transform), and only does a simple substitution of INSPECT
```

##### ↳ ↳ Re: Converting from COBOL to COBOL II - What's involved ?

- **From:** "mor..." <ua-author-4892761@usenetarchives.gap>
- **Date:** 1996-04-16T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f94cbaea10-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f94cbaea10-p4@usenetarchives.gap>`
- **References:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu> <gap-f94cbaea10-p4@usenetarchives.gap>`

```
In <4kvbef$d.··.@mti··t.net>, Arn Trembley writes:
› jku··.@ocb··c.edu (JK) wrote:
›› I have been assigned to investigate on what is involved in converting from
…[18 more quoted lines elided]…
› 
INSPECT field CONVERTING replaced TRANSFORM. I would look closely at
the code generated by the INSPECT CONVERTING and the TRANSFORM in the
old program before deciding on whether to do the function in another
way.

snip
› IBM has a product called CCCA for coverting OS/VS COBOL to COBOL II, but 
› my company didn't buy.  So I wrote a converter in COBOL II.  It handles 
› SERVICE RELOAD, but does not convert TRANSFORM (you need to write logic 
› to replace a transform), and only does a simple substitution of INSPECT
› 


Clark F. Morris, Jr. - CFM Technical Programming Services
RR#1, 1339 Clarence Road, Bridgetown, Nova Scotia B0S 1C0
cmo··.@fox··n.ca
On assignment in St. John, New Brunswick
mor··.@nbn··b.ca
```

#### ↳ Re: Converting from COBOL to COBOL II - What's involved ?

- **From:** "tro..." <ua-author-3877946@usenetarchives.gap>
- **Date:** 1996-04-15T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f94cbaea10-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`
- **References:** `<4ku7mf$od8@oac2.hsc.uth.tmc.edu>`

```
jku··.@ocb··c.edu (JK) wrote:

› I have been assigned to investigate on what is involved in converting from
› COBOL to COBOL II.
 
› Do we have to make changes to the programs or just recompile etc.?
 
› Are there any tools available to help with conversion?
 
› I will appreciate comments from people who are going through this process
› or have gone through it or doing research on it.
 
› Thanks in advance.
 
› JK.

Hi JK,

You probably won't have to make a lot of changes. Some changes you
won't have to make but will eventually want to. Such as replacing
some massive IF Stmts with the Evaluate verb, or initialization
routines with the Initialize verb.

Heres the list of dropped verbs:

Identification Division
Remarks (use * or / in column 7)

Environment Division
Processing mode clause

Procedure Division
READY TRACE
NOTE
EXHIBIT (use DISPLAY)
EXAMINE (use INSPECT)
CURRENT-DATE (use ACCEPT WS-DATE FROM DATE)
TIME-OF-DAY (use ACCEPT WS-TIME FROM TIME)
TRANSFORM (use INSPECT)
ON statement (use IF...ELSE or EVALUATE)
Write after/before positioning (use just 'WRITE' , drop positioning.


Tim Oxler

TEO Computer Technologies Inc.
tro··.@i··.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
