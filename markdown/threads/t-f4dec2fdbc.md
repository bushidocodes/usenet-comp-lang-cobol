[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# You Might Be In A Bad Program If...

_20 messages · 17 participants · 1998-01_

---

### You Might Be In A Bad Program If...

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1998-01-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

One of my favorites was a program with one paragraph only, in which the
last line was a 'GO TO ....'

But the winner of the 'Programmer Who Found The Worst Code Of The Week'
award was an online routine which searched a 3,000,000 record keyed VSAM
customer file for a match on the primary key (SSN) sequentially from the
beginning. The kicker was that when it found a match it didn't exit the
search loop. It set a flag, and then continued searching until EOF.
Wonderful thing to put into a high use data entry screen.

Also, they could match your nested IF nightmare. One, which was repeated
with minor variations in several dozen CICS programs, was seven pages long,
nested to twenty levels deep. Each of the sets of statements which finally
executed on a pass through this mess was four lines or less long. They
justified it because their CICS guru said straight line code executed
faster in CICS than PERFORMs.

Which just goes to show you don't get what you used to for $35 million
these days (total development, hardware upgrade, and implementation cost).
BTW, the customer company went out of business soon aferwards (unrelated
reasons, right?)

All of these were written by the 'other' Arthur group (A. Young, not A.
Anderson).
-----------------
"Twenty years of schoolin' and they put you on the day shift."
Bob Dylan
```

#### ↳ Re: You Might Be In A Bad Program If...

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-01-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

Gary Lee wrote:
›
› One of my favorites was a program with one paragraph only, in which the
› last line was a 'GO TO ....'

OY! Isn't this the format for the satanic ALTER GO TO?

Bill Lynch
(snip)
```

#### ↳ Re: You Might Be In A Bad Program If...

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-01-17T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

Gary Lee wrote:
›
› One of my favorites was a program with one paragraph only, in which the
› last line was a 'GO TO ....'

That doesn't sound so bad. Do you mean this:

PROCEDURE DIVISION.
1-PARAGRAPH.
OPEN INPUT IN-FILE OUTPUT OUT-FILE.
READ IN-FILE
AT END
CLOSE IN-FILE OUT-FILE
STOP RUN.
WRITE OUT-RECORD FROM IN-RECORD.
GO TO 1-PARAGRAPH.

› But the winner of the 'Programmer Who Found The Worst Code Of The Week'
› award was an online routine which searched a 3,000,000 record keyed VSAM
…[3 more quoted lines elided]…
› Wonderful thing to put into a high use data entry screen.

I know one like that. Host International had a report that ran daily,
which read a database sequentially. The program took over 24 hours to
run, so one days run started before the previous day's had ended. They
suspected the program could be more efficient, so a programmer was
assigned to investigate. He discovered the command to read the database
was effectively "read the database sequentially until you find a record
with a key higher than the last record". He replaced that one line with
a proper sequential read command and cut the execution time to ten
minutes.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p3@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p3@usenetarchives.gap>`

```

On Sun, 18 Jan 1998 11:18:34 -0500,
Jed··.@a.g··y.com (Jedi) wrote:

› You may not believe it,  but all of the Online programs (probably
› hundreds)  in our company's online library are set up to run like this,  
› i.e.  in a continual loop. They run daily all day until we "take" them
› down.
CICS?
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p3@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p3@usenetarchives.gap>`

```

On Sun, 18 Jan 1998 11:18:34 -0500,
Jed··.@a.g··y.com (Jedi) wrote:

› You may not believe it,  but all of the Online programs (probably
› hundreds)  in our company's online library are set up to run like this,  
…[4 more quoted lines elided]…
› 
Ah, I remember the technique well! In 1978 I was upgrading a 1410
simulator environment and discovered that one transaction had been
polling a terminal several hundred miles away that had been
disconnected in 1967 --- and polling it several times per minute --
for 11 years!!!!! LOLOL Ain't life grand?
david :-)

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-24T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p5@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p3@usenetarchives.gap> <gap-f4dec2fdbc-p5@usenetarchives.gap>`

```


David wrote in message <34d··.@nnt··m.com>...
› On Sun, 18 Jan 1998 11:18:34 -0500,
› Jed··.@a.g··y.com (Jedi) wrote:
…[17 more quoted lines elided]…
› 
My favorite one like this comes from the mid-80s.

I was working for a local phone company that was just finishing
"divestiture" (Good-bye Mama Bell) programming. We were also converting
from OS/VS COBOL to VS COBOL II which didn't support the Communications
Section (everyone used CICS and IMS by them).

We had one program that still used Communication Sections and its direct
TCAM interface. Unfortunately, the terminal(s) at the other end of the
system were owned by AT&T and this system was for a process that our company
really had no use for itself - but didn't know whether AT&T still used.

A) We couldn't legally ask anyone at AT&T if they still used the system
B) We couldn't even ask anyone at AT&T if there were still any terminal
out there receiving what we sent

I don't know whatever happened to that application - but when I last left,
it was happily churning away - whether anyone ever got its output or not.
```

#### ↳ Re: You Might Be In A Bad Program If...

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p7@usenetarchives.gap>`
- **In-Reply-To:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

You found a 3M Searcher Too??? I thought I had seen the only one in existance.
Damn... I saw this in an insurance company. The really funny part about this
whole mess was the "high level management meeting" that was convened to
discuss ways of reducing the runtime cost of this "important" program. The
mainframe charge back scheme that this company used assigned a cost of approx
$2500.00 per execution of this program. A task force was assembled (of course)
and I was the lucky chosen programmer. They idiotic management thought I was a
god when I stuck a paragraph of code in to do a key read.... and reduced
runtime from something over three hours to a blink. The mgt had discussed
everything from buying a faster mainframe to rewriting in the techno-fad du
jour.

Gary Lee wrote:

› One of my favorites was a program with one paragraph only, in which the
› last line was a 'GO TO ....'
…[24 more quoted lines elided]…
›    Bob Dylan
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p7@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap>`

```

John M. Saxton, Jr. wrote:
› 
› You found a 3M Searcher Too??? I thought I had seen the only one in
…[14 more quoted lines elided]…
› jour.

Well, if it had been written in one of these new gee-whiz OO languages, no
programmer could have been so stupid, right? ;-)

I remember once being asked to look at a long running program and finding
that
it did a sequential read of a file to find the proper record, but it only
decided the record wasn't in the file after it passed through the file three
times. I suppose the programmer was worried he might have missed it if he
only
read through twice. 8-)
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "je..." <ua-author-6589243@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p8@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p8@usenetarchives.gap>`

```

"Judson McClendon" wrote:


› I remember once being asked to look at a long running program and finding
› that
…[4 more quoted lines elided]…
› read through twice.  8-)



Maybe the programmer was Irish.. The second pass was "to be sure" and
the third pass "to be sure to be sure".. :)
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

_(reply depth: 4)_

- **From:** "graham perkins" <ua-author-900444@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p9@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p8@usenetarchives.gap> <gap-f4dec2fdbc-p9@usenetarchives.gap>`

```

Jeff York wrote:
›› decided the record wasn't in the file after it passed through the file three
›› times.  I suppose the programmer was worried he might have missed it if he
…[6 more quoted lines elided]…
› 

Or American. "It aint there, no way, no how."
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p7@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap>`

```

On Mon, 19 Jan 1998 08:32:41 -0500, "John M. Saxton, Jr."
wrote:

› .....  Â« snippo Â»  The
› mainframe charge back scheme that this company used assigned a cost of approx
…[6 more quoted lines elided]…
› 
Betcha didn't get anything like a $2490.00 tip for your trouble :)
Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p11@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p11@usenetarchives.gap>`

```

I received the hallowed "hardiest handshake and a most heartfelt THANKYOU" from my
bosses boss.


Richard Anderson wrote:

› On Mon, 19 Jan 1998 08:32:41 -0500, "John M. Saxton, Jr."
›  wrote:
…[14 more quoted lines elided]…
› anderson aatt pobox fullstop com



This bit of nonsense brought to you by the annoying spammers who like to troll the
news groups for new people to annoy. Protect yourself and obfuscate your email
address.

Return address is John underscore Saxton at ML dot com
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-01-21T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p12@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p11@usenetarchives.gap> <gap-f4dec2fdbc-p12@usenetarchives.gap>`

```

John M. Saxton, Jr. wrote:
›
› I received the hallowed "hardiest handshake and a most heartfelt THANKYOU" from my
› bosses boss.
›

Right, one "attaboy" to you, then the boss's boss helped himself to a
really fat bonus because "he'd" saved the company an unnecessary
upgrade. If this were a sitcom, we'd all be ROTFL.

Bill Lynch

(snip)
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p7@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap>`

```

› .....   I stuck a paragraph of code in to do a key read.... and reduced
› runtime from something over three hours to a blink.  The mgt had discussed
› everything from buying a faster mainframe to rewriting in the techno-fad du
› jour.
› 

I found something similar once in my consulting days. The original
programmer at least did key reads of the records but for some
reason everytime he did a rewrite he closed the file and re-opened
it for the next read. A single execution of this batch program
opened and closed the same vsam file millions of times. A simple
change to one open and one close reduced the run time from hours
to a few minutes.
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p14@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p14@usenetarchives.gap>`

```

Cit··.@Cr··s.Com, [Ron] wrote:
› 
›› .....   I stuck a paragraph of code in to do a key read.... and reduced
…[11 more quoted lines elided]…
› to a few minutes.

This is obviously a program that was converted from ISAM to VSAM. I have
seen many COBOL programs that used two different files to access the
same ISAM file. One was for direct (random) access and the other was for
skip sequential. Direct access was via BISAM. Skip sequential was via
QISAM. After adding a record it is (was) necessary to CLOSE and OPEN the
"other" file so that the in storage buffers and indices were refreshed.

VSAM fixed all that.

I can't recall if it was still necessary when using the VSAM-ISAM
bridge. But for a program compiled to be using VSAM the program should
be recoded to eliminate the unnecessary CLOSE/OPEN sequence.

BTW, back then it was also common to sort the transaction records into
DESCENDING key sequence. When adding many records to an ISAM file it is
(was) much more efficient to add the records in reverse key sequence.
This was due to the way that overflow areas were chained together. In
VSAM all you get is CI splits and CA splits. I have never measured VSAM
to see if the sort sequence of the inserted records makes a difference.
Wayne L. Beavers         mailto:Way··.@Bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"Transforming Legacy Applications"
```

###### ↳ ↳ ↳ Re: You Might Be In A Bad Program If...

_(reply depth: 4)_

- **From:** "cha..." <ua-author-8441878@usenetarchives.gap>
- **Date:** 1998-01-23T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p15@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap> <gap-f4dec2fdbc-p14@usenetarchives.gap> <gap-f4dec2fdbc-p15@usenetarchives.gap>`

```

Not strictly a bad program, but this one still comes back to mind when
this sort of subject is raised.

My second contract interview, back in 1976, was less of a grilling
that a confessional session.

INTERVIEWER A : Dave, here, and I have been brought in by
the new parent company to take over the DP
department. Quite frankly, it's a mess.
ME :
INTERVIEWER B : Yes, a bit of a mess. We are looking for the
kind of chap who can work on his own and yet
be a part of the team for the next three
months and help straighten out our systems.
ME :
INTERVIEWER A : Would you believe it if I told you that one
of our programs punches out 80,000 cards
every night and the cards are read by the
very next program in the job? I didn't
until Dave here showed me.
ME :

There was more of this but the example has stuck in my mind. I
actually turned the job down because it sounded like a three month
session of JCL writing, and the money was on the low side.


Charles F Hankel
------------------------------------------------------------------
COBOLs: IBM D, E, F, ANS v4, VS, COBOL 2, LE/370, AIX, S/38, OS/2,
PC/MS-DOS, Honeywell GCOS, Burroughs 7000, Tandem, HP3000
all to varying degrees over the past 25 years or so.
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "bill turner, wb4alm" <ua-author-4279623@usenetarchives.gap>
- **Date:** 1998-01-22T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p7@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p7@usenetarchives.gap>`

```

As a reward for a good job, did they give you a percentage of the money saved?

...I thought not.
/s/ Bill Turner, wb4alm

John M. Saxton, Jr. wrote:

› You found a 3M Searcher Too??? I thought I had seen the only one in existance.
› Damn... I saw this in an insurance company. The really funny part about this
…[45 more quoted lines elided]…
› Return address is John underscore Saxton at ML dot com
```

#### ↳ Re: You Might Be In A Bad Program If...

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p18@usenetarchives.gap>`
- **In-Reply-To:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

worst I ever saw and was lucky enough to have a chance to fix
was a 5000 procedure line program with 1200 ALTER .. GO TO's with 300
taget lines (4 alters per target).
The programmer did not use PERFORMS. The program was a structural
mess. I commented on the possible tree his family still lived in and
was called on the carpet.
(wasn't in sales at the time so I could be a little crude)

JR
and stir with a Runcible spoon...
```

##### ↳ ↳ Re: You Might Be In A Bad Program If...

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f4dec2fdbc-p18@usenetarchives.gap>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01> <gap-f4dec2fdbc-p18@usenetarchives.gap>`

```

jra··.@mai··t.net (Jeff Raben) wrote:

› worst I ever saw and was lucky enough to have a chance to fix
› was a 5000 procedure line program with 1200 ALTER .. GO TO's with 300

ok 2nd worst.....

same gov'mt programmer(?) many tape files were unblocked.
I recommended that (due to main-mem limitations) that he block some of
the high volume output (these were print files to be spooled
elsewhere).

He blocked 'em and, after running up overtime running a parallel, he
got a cash award for his effort. (yours and my money)


JR


and stir with a Runcible spoon...
```

#### ↳ Re: You Might Be In A Bad Program If...

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f4dec2fdbc-p20@usenetarchives.gap>`
- **In-Reply-To:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`
- **References:** `<01bd23d7$7cc380d0$2085aac7@sysserve01>`

```

A similar story. We have a dozen plants, each with a 5-digit ID number,
e.g. 10115, 31500, and the like. The highest was 82850. The numbers were
inherited from the days before computers. In Program ''A'', a programmer
wanted to print the full name of a plant. So, he wrote program ''Pre-A''
which created a random access file containing the number and text data for
each of the 12 plants. It also opened disk space for 82,838 empty records.
Then program ''A'' would come up and read a thousand-record transaction
file. For each transaction, he opened the random file, then read it
sequentially until he got a hit, and then closed the file. This programmer
eventually got out of computers and became a letter-carrier.
-------------------
Another pet peeve: User says ''Discontinue the Doohickey Report--we don't
need it any more.'' Programmer goes to Doohickey program, and replaces
''CLOSE PRINTFILE WITH LOCK'' with ''CLOSE PRINTFILE WITH PURGE.''
-------------------
One programmer had Work-Flow (that's Burroughese for JCL) that he was
running in test mode. At the end he wanted to refresh the test data so he
put in a program that deleted all records from the master file. Went he
went live, he went to the previous program and deliberately did a Write on
an Unopened File, causing the job to abort and thus preventing the erasure
of the production master file. A few years later, I got this program for a
trivial change and did a Unit Test on it. ''That's looks ugly,'' I
thought, and removed the illegal Write without a second thought. Bad idea.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
