[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help on CICS/VSE

_20 messages · 12 participants · 1998-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Help on CICS/VSE

- **From:** "news" <ua-author-13363@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`

```

Dear all,
I have never coded in CICS before so this may seem obvious but
I am baffled.

I have coded one CICS program and compiled also but I don't know how to
allocate set transaction id(PCT) for this program.
Can anybody tell me what all procedures I should follow for execution of
the program after compilation.My
system is DOS/VSE.

Thanks in advance.

Biswajit (bis··.@pcm··h.de)
```

#### ↳ Re: Help on CICS/VSE

- **From:** "themix" <ua-author-3650591@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`

```

news wrote
› Dear all,
›   I have never coded in CICS before so this may seem obvious but 
…[6 more quoted lines elided]…
› system is DOS/VSE.
Wo, this is really getting out of hand - never coded CICS before and want
to program and mess around with the system tables. Reading (hopefully
correctly) your Email address I hope you are not out there on an assignment
that you are not qualified to perform. I suggest you get hold of someone
who *knows* what they are doing.
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p2@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p2@usenetarchives.gap>`

```

themix wrote:
› 
› news  wrote
…[13 more quoted lines elided]…
› who *knows* what they are doing.

I bet it's fully conversational too. If the original author does not
know what I just said, he needs to STOP NOW!
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-30T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p2@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p2@usenetarchives.gap>`

```

themix wrote:
› 
› news  wrote
…[13 more quoted lines elided]…
› who *knows* what they are doing.

Well, the vendor (IBM) usually supplies a transaction to do this. Under
big
CICS, that would be "CEDA". Otherwise, you can either edit your CSD
(config)
files to add the PCT entry or (depending on the version) recompile your
CICS
with the appropriate macro to generate the PCT entry (not
recommended)....
```

#### ↳ Re: Help on CICS/VSE

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`

```

news wrote:
› 
› Dear all,
…[10 more quoted lines elided]…
› 

The system you're running on makes no difference, CICS is CICS in this
respect. At a minimum you need a PCT entry, where your transaction ID is
defined and which names the program to invoke; you'll also need at least
one PPT entry (for the program you wrote & compiled - if you're using a
map (BMS or otherwise) you need a PPT entry for the map, too). If you're
processing a new file, you'll also need an FCT entry for it. I'm willing
to bet there's a group somewhere in your installation that maintains
these tables (PCT, PPT & FCT). Find out how to contact them and how to
submit table requests (I'd start with the person who handed me the
assignment).

Someone may need to submit a RACF request to grant you access to the
transaction (especially in production).

Bill Lynch

› Biswajit (bis··.@pcm··h.de)
```

#### ↳ Re: Help on CICS/VSE

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`

```

In article <01bd58b5$6d98d7a0$430··.@eds··h.de>,
news wrote:
› Dear all,
›  I have never coded in CICS before so this may seem obvious but 
› I am baffled.
› 
› I have coded one CICS program
 
› ... now *I* am baffled.
 
› and compiled also but I don't know how to
› allocate set transaction id(PCT) for this program.
› Can anybody tell me what all procedures I should follow for execution of
› the program after compilation.My 
› system is DOS/VSE.

The procedures you should follow are the ones given to you by your
manager; your manager should be working in concert with the System
Operations (lovingly referred to as 'Ops') so that an orderly transition
might be made from the test environment to production (lovingly referred
to as Prod).

This helps, at times, to prevent people who do *not* know what they are
doing from violating the integrity of the system; such violations can
result in Abnormal Endings of programs (hatedly referred to as ADENDs)

DD
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p6@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap>`

```

All of a sudden, doc··.@cl··k.net () wrote:

› In article <01bd58b5$6d98d7a0$430··.@eds··h.de>,
› news  wrote:
…[23 more quoted lines elided]…
› 
or even sometimes as ABENDs....



Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p6@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap>`

```

doc··.@cl··k.net () wrote:

› In article <01bd58b5$6d98d7a0$430··.@eds··h.de>,
› news  wrote:
…[25 more quoted lines elided]…
› 


Doc:

We always called them "ABENDS" but then I don't own a tin foil and egg
salad chapeau which obviously means that the aliens have indeed sucked
all of the knowledge from the tiny pea-brain that I have.


Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p8@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap> <gap-4e5bbb674f-p8@usenetarchives.gap>`

```

In article <351··.@new··r.net>,
Bob Wolfe wrote:
› doc··.@cl··k.net () wrote:
 
› [pre-typo snippage]
 
› 
›› result in Abnormal Endings of programs (hatedly referred to as ADENDs)
…[10 more quoted lines elided]…
› 

Maybe yes, maybe no... some of them Space Aliens have pretty sloppy aim.
Which, then, is the worse conclusion... that your brain has indeed been
sucked dry by the Space Aliens... or that it hasn't?

DD
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

_(reply depth: 4)_

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p9@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap> <gap-4e5bbb674f-p8@usenetarchives.gap> <gap-4e5bbb674f-p9@usenetarchives.gap>`

```

doc··.@cl··k.net () wrote:

[snip]
››› result in Abnormal Endings of programs (hatedly referred to as ADENDs)
››› 
…[13 more quoted lines elided]…
› sucked dry by the Space Aliens... or that it hasn't?

You assume that one is worse than the other. Perhaps there would be
no difference whatsoever in my mental capabilities whether or not my
brain were snatched!


Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

_(reply depth: 5)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p10@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap> <gap-4e5bbb674f-p8@usenetarchives.gap> <gap-4e5bbb674f-p9@usenetarchives.gap> <gap-4e5bbb674f-p10@usenetarchives.gap>`

```

In article <351··.@new··r.net>,
Bob Wolfe wrote:
› doc··.@cl··k.net () wrote:
› 
…[20 more quoted lines elided]…
› brain were snatched!

Oh, *really* now... the question of 'which is worse' makes *no*
assumptions; a perfectly valid responses include 'neither is worse' or
'both are equally bad'. *Think* for a moment... consider the code:

IF A > B
PERFORM A-GT-B THRU AGB-EX
ELSE
IF B > A
PERFORM B-GT-A THRU BGA-EX.

... now be truthful (yes, I know it *is* a stretch for the loiks o'
youse)... would *you* let that code pass review without *demanding* the
removal of the period and the addition of

ELSE
IF A = B
PERFORM A-EQ-B THRU AEB-EX.

(or a rewrite of the code in another form, e.g. EVALUATE, which would
accomplish the same functional end)?

G'wan, gedouddahere.

DD
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

_(reply depth: 6)_

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p11@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap> <gap-4e5bbb674f-p8@usenetarchives.gap> <gap-4e5bbb674f-p9@usenetarchives.gap> <gap-4e5bbb674f-p10@usenetarchives.gap> <gap-4e5bbb674f-p11@usenetarchives.gap>`

```

doc··.@cl··k.net () wrote:

› In article <351··.@new··r.net>,
› Bob Wolfe  wrote:
…[48 more quoted lines elided]…
› 

Touche! (pardon the lack of the accent mark...) I agree with you
completely. The conditional is incomplete without an analysis of
whether the 2 variables are exactly the same value!! How could I
overlook something so completely obvious (please do not feel compelled
to answer this question...it is rhetorical)?

You truly are a genius, however, I would rename the variables from "A"
and "B" to "ALIEN-SNATCHED-BRAIN" and "BRAIN-INTACT" in order to make
the code easier to maintain.



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

_(reply depth: 7)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p12@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p6@usenetarchives.gap> <gap-4e5bbb674f-p8@usenetarchives.gap> <gap-4e5bbb674f-p9@usenetarchives.gap> <gap-4e5bbb674f-p10@usenetarchives.gap> <gap-4e5bbb674f-p11@usenetarchives.gap> <gap-4e5bbb674f-p12@usenetarchives.gap>`

```

In article <351··.@new··r.net>,
Bob Wolfe wrote:
› doc··.@cl··k.net () wrote:
› 
…[60 more quoted lines elided]…
› the code easier to maintain.

Pfoo, t'warn't nothin'... just an obvious thing for... Captain COBOL!

EVALUATE TRUTH
WHEN IN-DOUBT
PERFORM REDUCE-TO-CODE UNTIL ALL-UNCERTAINTY-VANISHES
END-EVALUATE.

DD
```

#### ↳ Re: Help on CICS/VSE

- **From:** "stev..." <ua-author-17074205@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p14@usenetarchives.gap>`
- **In-Reply-To:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de>`

```

On 26 Mar 1998 12:45:29 GMT, "news"
wrote:

› Dear all,
›  I have never coded in CICS before so this may seem obvious but 
…[12 more quoted lines elided]…
› 
I am assuming this is a new program, otherwise you wouldn't be having
the problem you describe. What must be done so that you can execute
your program in CICS is not something you should be doing. Rather it
is the job of your CICS System Administrator. But for the sake of
knowledge, I'll pass this on to you. There are two tables involved.
One is the PPT (Processing Program Table). This table defines the
program name and language type to CICS. The next you may or may not
need depending on what you are doing with this new program. It is
called the PCT (Program Control Table). If your program is executed
in CICS by a transaction id, you need to define the transaction id in
this table and tell CICS to execute your program. Also, if your
program is accessing any files that are new, they too must be defined
in an FCT (File Control Table).

So now maybe you can see why this is something you should not be
doing.

Regards,
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p14@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap>`

```

Alan Yeary wrote:
› 
› (snip)
…[5 more quoted lines elided]…
› entries himself.

I hope not. I've never seen any shop, DOS (I started using CICS back in
the DOS Standard days) or otherwise, that didn't have *someone*
responsible for CICS resource definitions and such. Expecting each
programmer, even the newbies, to do his/her own table entries pretty
much guarantees a lot of downtime for the test region(s), while someone
straightens out the most recent mess. I find it really hard to imagine
turning someone loose with CEDA who doesn't know he needs a PCT & PPT
entry.

Bill Lynch
```

##### ↳ ↳ Re: Help on CICS/VSE

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-29T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p14@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap>`

```

Alan Yeary wrote:

› Some of the replies to this guy's question assume his shop has a huge
› bureaucracy like MVS shops do, with one group of people handling
…[3 more quoted lines elided]…
› entries himself.

I came from a VSE shop. We almost NEVER used the CEDA to define the
resources. We suffered a bit of paranioa there. We liked using the
actual macros and re-assembling to get the entries made. Always a
paper/program backup that way. I wonder, what other experience is out
there? Anyone else afraid of CEDA?
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-03-29T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p16@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap> <gap-4e5bbb674f-p16@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Alan Yeary wrote:
…[12 more quoted lines elided]…
› there?  Anyone else afraid of CEDA?

I work in an unusual environment where my application group has full
CEDA access to our test and production regions. They tech services
department has been trying to take away our access, saying that it
prevents them from keeping all the CICS regions up to date. This
despite the fact that we have been at CICS 3.3 for years and it was only
last weekend they converted three production regions from CICS 2.1.2 to
3.3.

I like CEDA. You can define programs, files, and transactions without
having to recycle the region. We do not share the production CSD file
with the test regions, however. We back up the production CSD, so we
can always restore it if necessary. We have had very few problems
maintaining the production CSD file.

There are three different online utilities for managing the CICS CSD
file:

CEDA - full update capability, with authority to install groups.
CEDB - full update capability, but no authority to install groups
(recycle instead)
CEDC - inquiry access only

There are still some DCT and TCT entries that can only be created by
assembling DFH tables, even in CICS 4.1. But I prefer CEDA and the CSD
file for normal maintenance. The batch CEDA utility is useful for
printing out your definitions, but not particularly user-friendly.

Arnold Trembley
Software Engineer I (Just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

- **From:** "geir" <ua-author-651162@usenetarchives.gap>
- **Date:** 1998-03-29T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p16@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap> <gap-4e5bbb674f-p16@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› 
…[4 more quoted lines elided]…
› there?  Anyone else afraid of CEDA?

Understand your scepticism very well thank you!!

It's a real mess having a bunch of "unstructured" COBOL/CICS programmers
using CEDA!

But you may use the offline utility program DFHCSDUP to define your
entries, (provided if it is delivered with CICS/VSE)

We are using it at our shop (CICS/ESA), and this way you will have a
source-member (in your "utility" dataset) as a sort of documentation of
the entries in the PPT, PCT, FCT etc..

If you only give yourself access to CEDA,.. you sholuld be in full
control.. :-)

****
/Geir
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

_(reply depth: 4)_

- **From:** "stev..." <ua-author-17074205@usenetarchives.gap>
- **Date:** 1998-03-29T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p18@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap> <gap-4e5bbb674f-p16@usenetarchives.gap> <gap-4e5bbb674f-p18@usenetarchives.gap>`

```

On Mon, 30 Mar 1998 17:54:10 +0200, Geir
wrote:

› Thane Hubbell wrote:
›› 
…[23 more quoted lines elided]…
› /Geir

Agreed. Having worked in a DOS/VSE shop for many years (even before
CEDA was born), I can tell you that programmers were not allowed to
make their own entries. It was either the system programmer (in the
early days) or the CICS administator later on. We used to to the
table recompile thing nightly and were extremely happy when CEDA came
along.
```

###### ↳ ↳ ↳ Re: Help on CICS/VSE

- **From:** "anna-karin johansson" <ua-author-17074431@usenetarchives.gap>
- **Date:** 1998-03-31T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4e5bbb674f-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4e5bbb674f-p16@usenetarchives.gap>`
- **References:** `<01bd58b5$6d98d7a0$430394ad@eds-biswajit.ban.bosch.de> <gap-4e5bbb674f-p14@usenetarchives.gap> <gap-4e5bbb674f-p16@usenetarchives.gap>`

```

Afraid of CEDA? NO! Not as long as production and test/development are
keept separate from each other. I'm at a VSE shop where the programmers are
free to use CEDA in the test-CICS. If every programmer had to wait for the
systemprogrammer to make neccesary changes in CEDA, just to be able to test
their programs, then it wouldn't be much done. We have too many programs to
write and very little time to write them.



Thane Hubbell wrote:

› Alan Yeary wrote:
› 
…[11 more quoted lines elided]…
› there?  Anyone else afraid of CEDA?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
