[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS coding..read a VSAM file

_8 messages · 7 participants · 1998-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### CICS coding..read a VSAM file

- **From:** "stephen mcvarnock" <ua-author-17075276@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`

```

Dear all,
I have never coded in CICS before so this may seem obvious but
I am baffled.

A VSAM file exists which I want to read in a sequential manner.
The VSAM file holds a bunch of record structures but at the time
of reading I do not know the key of each record. I just want to read
it into memory and do a compare against one of the fields in the key.

Can anybody send the code for this particular job if they can. I think the
code begins with the line EXEC CICS READ or something.

Thanks.

Steve (sti··.@hot··l.com)
```

#### ↳ Re: CICS coding..read a VSAM file

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`

```

Stephen McVarnock wrote:
›
 
› Can anybody send the code for this particular job if they can. I think the
› code begins with the line EXEC CICS READ or something.
›

What you are looking for is a STARTBR. Do that first with low values in
the RIDFLD then use the READNEXT to read it sequentially. Note: If
this is a very large file, this is not the way to do this. You also
didn't specify if the file was KSDS, RSDS or ESDS. Since you did
mention the work KEY I assumed KSDS. If ESDS you need a different
approach.
```

#### ↳ Re: CICS coding..read a VSAM file

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`

```

In article <01bd57df$e88696e0$d14··.@nes··o.uk>,
Stephen McVarnock wrote:
› Dear all,
› I have never coded in CICS before so this may seem obvious but
› I am baffled.

Would I be thought rude were I to inquire why you are trying to write code
in something you do not understand without first studying it?

›
 
› [snippage of difficulty]
 
›
› Can anybody send the code for this particular job if they can. I think the
› code begins with the line EXEC CICS READ or something.

Are you *sure* about that syntax... 'EXEC CICS READ or something'...
something there doesn't look quite right to me, what does your manual say?

DD
```

##### ↳ ↳ Re: CICS coding..read a VSAM file

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3db22b8d4d-p3@usenetarchives.gap>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk> <gap-3db22b8d4d-p3@usenetarchives.gap>`

```

I'm gonna interject on this one, because I am in just about the
same position. It is HELLISHLY hard to find information at the
novice level about CICs. Everyone assumes you know EVERYTHING.
Give this guy a break, he asked an honest question and it is
NOT an easy question to answer, at least in terms novices like
us understand.

I would suggest perusing the IBM WebSites regarding CICS. They
are very helpful. The IBM people are also very helpful. I don't think
you could find a better resource than the CIC's mailing list either,
which I don't have the address for at this location, but I will
post the address for as well.

There are some people on this list as well who will probably offer
help. I would advise listening to them, they make awfully good sense. :)

-Paul


-Paul





doc··.@cl··k.net wrote:
: In article <01bd57df$e88696e0$d14··.@nes··o.uk>,
: Stephen McVarnock wrote:
: >Dear all,
: > I have never coded in CICS before so this may seem obvious but
: >I am baffled.

: Would I be thought rude were I to inquire why you are trying to write code
: in something you do not understand without first studying it?

: >

: [snippage of difficulty]

: >
: >Can anybody send the code for this particular job if they can. I think the
: >code begins with the line EXEC CICS READ or something.

: Are you *sure* about that syntax... 'EXEC CICS READ or something'...
: something there doesn't look quite right to me, what does your manual say?

: DD
```

###### ↳ ↳ ↳ Re: CICS coding..read a VSAM file

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3db22b8d4d-p4@usenetarchives.gap>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk> <gap-3db22b8d4d-p3@usenetarchives.gap> <gap-3db22b8d4d-p4@usenetarchives.gap>`

```

paulr wrote:
› 
› I'm gonna interject on this one, because I am in just about the
…[5 more quoted lines elided]…
› 

It sounded like a homework assignment (although his organisation says
"BT Labs"). Is there *no one* where you work (like the person who gave
you this assignment) who can give you some hints or pointers? Maybe an
existing program that does what you need, but to a different file, or
part of a different application? I do understand how easy it is to
flounder a bit in a new job / new environment, but saying "EXEC CICS
READ or something" smacks of a green student or someone who's lied his
way into a CICS programming slot.

Anyway, someone already mentioned STARTBR, I'll continue the assist with
"READNEXT". Even if the original poster has no manuals, they're
available free on the Net (no charge to read them, can't speak for his
Net access).

Bill Lynch

(snipped)
```

###### ↳ ↳ ↳ Re: CICS coding..read a VSAM file

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3db22b8d4d-p4@usenetarchives.gap>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk> <gap-3db22b8d4d-p3@usenetarchives.gap> <gap-3db22b8d4d-p4@usenetarchives.gap>`

```

In article <6fbln2$q.··.@lot··i.com>, paulr wrote:
› I'm gonna interject on this one, because I am in just about the
› same position.
 
› Come on in, the water's fine!
 
› It is HELLISHLY hard to find information at the 
› novice level about CICs.

Ahhhh. *there's* the rub... what constitutes 'novice'? In no wise do I
consider myself an expert in many things... but I'm pretty good at
*research*. It reminds me of a posting a while back along the lines of 'I
don't know anything about COBOL but I've just been assigned to Production
Support'... I am constantly amazed by two things:

1) The assigning of Complex Technical... Stuff by management to those who
are neither trained nor experienced in dealing with said... Stuff.

2) The utter lack of willingness of said assignees to say 'Hey, I don't
know this and I never said I knew this... I'll give it a whack, sure, but
I *am* going to screw up Big Time.'

› Everyone assumes you know EVERYTHING.
 
› At times to disabuse someone of a false notion is a Good Thing.
 
› Give this guy a break, he asked an honest question and it is 
› NOT an easy question to answer, at least in terms novices like
› us understand. 

An honest question, sure... but in the asking he showed no indication of
initiative or research outside of that which could be overheard, phrases
which bounce around the tile walls and stall-dividers of the lavatory.
EXEC CICS READ or something? A rank newbie usually has the texts from a
recently-completed course, if not access to manuals.

[snippage of generally Good Advice]

DD
```

###### ↳ ↳ ↳ Re: CICS coding..read a VSAM file

- **From:** "geir" <ua-author-651162@usenetarchives.gap>
- **Date:** 1998-03-25T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3db22b8d4d-p4@usenetarchives.gap>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk> <gap-3db22b8d4d-p3@usenetarchives.gap> <gap-3db22b8d4d-p4@usenetarchives.gap>`

```

paulr wrote:
› 
› I'm gonna interject on this one, because I am in just about the
…[5 more quoted lines elided]…
› 

Must disagree with you here...

His posting was (like too many in this group) pretty much:

"I'm a lazy slob.. Do not want to do any research.. Here is my problem..
Post the code to me and I can relax some more." :-)

This may also be considered a smart thing to do,.. but it should be no
surprise that this offends some "old" hard-working COBOL/CICS people..
;-)

As you (and others) points out.. it should be no big problem to find
on-line documentation on the IBM sites.

Another thing..
I find it very hard to believe that someone is assigned such a task in a
shop running CICS.., and there is no manuals???
The manuals exists to be used!!!!!!!

And this is not "HELLISHLY" difficult..
It is actually *very* easy!!

**************************************************************

EXEC CICS STARTBR
FILE(yourfile)
RIDFLD(startkey)
GTEQ
REQID(1)
END-EXEC

PERFORM WITH TEST AFTER
UNTIL eibrcode <> LOW-VALUES (better more specific.. read the
manuals)

EXEC CICS READNEXT
FILE(yourfile)
INTO(copyarea)
RIDFLD(startkey)
REQID(1)
END-EXEC


--> PERFORM something-useful

END-PERFORM

EXEC CICS ENDBR
FILE(yourfile)
REQID(1)
END-EXEC

****************************************************************

Not pre-processed.. not compiled.. not tested.., but this is basically
all there is to it.

BTW:
"..or something" is a famous phrase from a very intelligent character in
a MTV cartoon ..
(Butthead was the name I recall...) :-)


****
/Geir
```

#### ↳ Re: CICS coding..read a VSAM file

- **From:** "gra..." <ua-author-17084123@usenetarchives.gap>
- **Date:** 1998-03-25T12:43:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3db22b8d4d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`
- **References:** `<01bd57df$e88696e0$d1429284@nesbitt.bfsec.bt.co.uk>`

```

In article <01bd57df$e88696e0$d14··.@nes··o.uk>,
"Stephen McVarnock" wrote:
› 
› Dear all,
…[11 more quoted lines elided]…
› Thanks.


You are BROWSING the file. You have to do a STARTBR (start browse) followed
by READNEXTs to get the records. READ is intended for sepcific redords.
›
› Steve (sti··.@hot··l.com)
›


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
