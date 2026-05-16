[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# match program example

_70 messages · 17 participants · 2003-11 → 2003-12_

---

### match program example

- **From:** gregjohnson@comcast.net
- **Date:** 2003-11-17T19:27:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>`

```
Does anyone have a simple example of a COBOL match program.  I need to
become more familiar with the logic.

Thank you.
```

#### ↳ Re: match program example

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-18T02:18:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>`

```
Read File1
Read File2

do until File1-EOF and File2-EOF
    if File1-key < File2-key
        Perform File1-Process
        Read File1
    else if File2-key < File1-key
        Perform File2-Process
        Read File2
    else
        Perform FileEqual-Process
        Read File1
        Read File2
    end-if
end-do

Obviously pseudo-code, not real COBOL.

The issue of handling end-of-file I leave as an exercise for you.

HTH,

Paul

<gregjohnson@comcast.net> wrote in message
news:v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com...
> Does anyone have a simple example of a COBOL match program.  I need to
> become more familiar with the logic.
>
> Thank you.
```

##### ↳ ↳ Re: match program example

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-18T05:20:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net>`

```

paul <paulpigott@earthlink.net> wrote in message news:akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net...
> Read File1
> Read File2
…[11 more quoted lines elided]…
>         Read File2

File #1 - Payroll Master
Record #1 Hugh Candlin
Record #2 John Smith
Record #3 Paul Pigott

File #2 - Weekly Payroll Detail File
Record #1 Hugh Candlin Base Pay
Record #2 Hugh Candlin Overtime Pay
Record #3 Hugh Candlin Coaching Pay
Record #4 John Smith Base Pay
Record #5 etc etc

Your program has a MAJOR logic error
```

###### ↳ ↳ ↳ Re: match program example

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-19T23:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net>`

```
I tried to reply directly to you (instead of via the newsgroup) but you have
a dummy address.

Always being interested in learning new things, I would appreciate it if you
could point out the flaw that you see.

Thanks,

Paul

"Hugh Candlin" <no@spam.com> wrote in message
news:7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net...
>
> paul <paulpigott@earthlink.net> wrote in message
news:akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net...
> > Read File1
> > Read File2
…[27 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 4)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-19T23:51:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net>`

```

paul <paulpigott@earthlink.net> wrote in message news:RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net...
> I tried to reply directly to you (instead of via the newsgroup) but you have
> a dummy address.
…[6 more quoted lines elided]…
> Paul

I gave you two test files.  All you have to do is to desk-check your logic.
You need to learn to do that.  Now is a good time.

Post back if you don't know how, and we'll explain it to you.

>
> "Hugh Candlin" <no@spam.com> wrote in message
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 5)_

- **From:** Bat Guano <bat.guano@talk21dotcom>
- **Date:** 2003-11-20T01:18:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vro5jon5u4u187@corp.supernews.com>`
- **In-Reply-To:** `<GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net>`

```
Hugh Candlin wrote:

> 
> I gave you two test files.  All you have to do is to desk-check your logic.
…[3 more quoted lines elided]…
> 

Stop trying to be smart, it doesn't suit you. Just answer the question.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-20T14:31:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbc19a8_8@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com>`

```

"Bat Guano" <bat.guano@talk21dotcom> wrote in message
news:vro5jon5u4u187@corp.supernews.com...
> Hugh Candlin wrote:
>
> >
> > I gave you two test files.  All you have to do is to desk-check your
logic.
> > You need to learn to do that.  Now is a good time.
> >
…[4 more quoted lines elided]…
>
Getting someone to look at their code, rather than actually giving them the
solution on a plate, is a more profound and, in the long run, helpful,
approach, than simply demanding an answer.

Hugh's response was reasonable and in the interest of the person concerned.

Yours was rude and inappropriate.

(Hey, if you feel that strongly, why don't YOU post the solution?)

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 7)_

- **From:** Bat Guano <bat.guano@talk21dotcom>
- **Date:** 2003-11-20T12:22:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vrpcgm8s5r1ncd@corp.supernews.com>`
- **In-Reply-To:** `<3fbc19a8_8@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:

> 
> Getting someone to look at their code, rather than actually giving them the
> solution on a plate, is a more profound and, in the long run, helpful,
> approach, than simply demanding an answer.

As far as I could see, paul described the industry-standard solution to 
the 2-file-match problem. As paul has now stated, it looks like Hugh was 
objecting to the logic based on a special (and secret) set of 
circumstances.

> 
> Hugh's response was reasonable and in the interest of the person concerned.

Hugh's response was pompous and unhelpful

> 
> Yours was rude and inappropriate.

Nonsense, I was just trying to get his attention (not yours)

> 
> (Hey, if you feel that strongly, why don't YOU post the solution?)
> 

If I knew what he thought the problem was, I'd be able to discuss the 
solution.

Who died and left you in charge?
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-21T10:54:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbd382e_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com> <vrpcgm8s5r1ncd@corp.supernews.com>`

```

"Bat Guano" <bat.guano@talk21dotcom> wrote in message
news:vrpcgm8s5r1ncd@corp.supernews.com...
> Peter E.C. Dashwood wrote:
>
> >
> > Getting someone to look at their code, rather than actually giving them
the
> > solution on a plate, is a more profound and, in the long run, helpful,
> > approach, than simply demanding an answer.
…[7 more quoted lines elided]…
> > Hugh's response was reasonable and in the interest of the person
concerned.
>
> Hugh's response was pompous and unhelpful
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-21T11:29:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbd407c_4@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com> <vrpcgm8s5r1ncd@corp.supernews.com>`

```

"Bat Guano" <bat.guano@talk21dotcom> wrote in message
news:vrpcgm8s5r1ncd@corp.supernews.com...
> Peter E.C. Dashwood wrote:
>
> >
> > Getting someone to look at their code, rather than actually giving them
the
> > solution on a plate, is a more profound and, in the long run, helpful,
> > approach, than simply demanding an answer.
…[5 more quoted lines elided]…
>
Then you can't see very far. His solution was fundamentally flawed. This is
nothing personal against Paul, and it's good that he posted _A_ solution,
but it was not complete (enough) for someone to use it.
> >
> > Hugh's response was reasonable and in the interest of the person
concerned.
>
> Hugh's response was pompous and unhelpful

OK, that's your opinion, but you weren't the one requesting information.
>
> >
> > Yours was rude and inappropriate.
>
> Nonsense, I was just trying to get his attention (not yours)

OK, that's my opinion. I respect your right to differ. (As a matter of
interest, have you found rudeness to be a successful way of getting people's
attention, or enlisting their co-operation, in the past?)

You got my attention because it is an open forum, and if you post to it, you
will often elicit responses you might rather not have had. Paul's solution
was not adequate. Hugh tried to get him to re-evaluate it. You accused him
of being pompous and me of meddling. Yet you were not involved in the
discussion in the first place and have no more right to be here than I do.
>
> >
…[5 more quoted lines elided]…
>

So you obviously thought Paul's solution was OK. You are therefore NOT able
to discuss a solution, any more than you are able to see the problem. (Waste
of time your being here, really, isn't it?)

> Who died and left you in charge?
>
The same person who never gave you a clip round the ear when you were
growing up, thereby stunting your development...

When your mental age gets above the level of thinking bat shit is a cool
handle, we can possibly have a discussion.

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 9)_

- **From:** Bat Guano <bat.guano@talk21dotcom>
- **Date:** 2003-11-20T23:27:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vrqjenj30o0vc6@corp.supernews.com>`
- **In-Reply-To:** `<3fbd407c_4@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com> <vrpcgm8s5r1ncd@corp.supernews.com> <3fbd407c_4@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> 
> His solution was fundamentally flawed.

In what way?
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 10)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-20T23:57:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zxcvb.16733$86.318689@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com> <vrpcgm8s5r1ncd@corp.supernews.com> <3fbd407c_4@news.athenanews.com> <vrqjenj30o0vc6@corp.supernews.com>`

```
"Bat Guano" <bat.guano@talk21dotcom> wrote in message
news:vrqjenj30o0vc6@corp.supernews.com...
> Peter E.C. Dashwood wrote:
> >
> > His solution was fundamentally flawed.
>
> In what way?

Take the conventional approach and read the thread before commenting.
oh...and do *try* to keep up....

JCE
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 11)_

- **From:** Bat Guano <bat.guano@talk21dotcom>
- **Date:** 2003-11-21T00:03:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vrqljcg8agr0e9@corp.supernews.com>`
- **In-Reply-To:** `<zxcvb.16733$86.318689@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <vro5jon5u4u187@corp.supernews.com> <3fbc19a8_8@news.athenanews.com> <vrpcgm8s5r1ncd@corp.supernews.com> <3fbd407c_4@news.athenanews.com> <vrqjenj30o0vc6@corp.supernews.com> <zxcvb.16733$86.318689@twister.tampabay.rr.com>`

```
jce wrote:

> 
> Take the conventional approach and read the thread before commenting.
> oh...and do *try* to keep up....
> 

I took your advice, but I didn't see anything from Hugh that explains 
what he thinks the problem is with paul's solution. For that matter, I 
didn't see a reply from anyone else that explains what Hugh thinks the 
problem is.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 5)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-20T02:24:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net>`

```
Greetings Mr. Candlin,

I did as you suggested, following the logic with your two datasets.  I
believe I see what you are pointing out, though it would have been helpful
if you had simply described it to begin with.

I believe you are taking issue with the fact that when the file keys are
equal, both input files are then read and the files then become out of
synch.  Given your example, that is true.

But please note that my example was never intended as a complete logical
description of a match-merge process.  It was intended to sketch in the
broad outlines of a standard batch progamming practice, namely the merging
of two files.

Programmers typically have some understanding of the nature of the data that
he/she will be working with.  My example took the lowest common denominator,
simply assuming that one file of sorted records (with unique keys) was being
combined with another sorted file (in the same format, and also with unique
keys).  Your example of a master file, with an associated transaction file,
is also a quite common situation (though not as common as it used to be) but
attempting to keep my example simple, I chose not to delve that deeply.

To handle the situation you describe, the paragraph for FileEqual-Process
could be modified to continue reading File2 until a new key (or end-of-file)
is encountered.  The read for File2 following the FileEqual-Process
execution would then be eliminated.  Minor modifications to be sure, but
ones that can only be done when the programmer has an understanding of what
data is to be processed.

So, Sir, my algorithim (taken broadly) is fine.  You have merely
demonstrated its (possible) lack of suitability for a particular set of
data.

Thank you for your time.

Paul


"Hugh Candlin" <no@spam.com> wrote in message
news:GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net...
>
> paul <paulpigott@earthlink.net> wrote in message
news:RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net...
> > I tried to reply directly to you (instead of via the newsgroup) but you
have
> > a dummy address.
> >
> > Always being interested in learning new things, I would appreciate it if
you
> > could point out the flaw that you see.
> >
…[4 more quoted lines elided]…
> I gave you two test files.  All you have to do is to desk-check your
logic.
> You need to learn to do that.  Now is a good time.
>
…[41 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2003-11-20T09:24:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net>`

```
On Thu, 20 Nov 2003 02:24:00 GMT, "paul" <paulpigott@earthlink.net>
enlightened us:

>Greetings Mr. Candlin,
>
…[31 more quoted lines elided]…
>

Any algorithm for a match/merge logic that doesn't take into account
equal keys is incomplete and wrong.  Hugh was correct in pointing this
out to you.  Whether your solution was broad or thin, there are only 3
possibilities in match/merge logic and you neglected to handle 1 of
the more common.


>Thank you for your time.
>
…[66 more quoted lines elided]…
>

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


Micro$oft Haiku Error Message #113

A crash reduces
Your expensive computer
To a simple stone.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 7)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-20T17:04:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ou6vb.11724$Wy4.9378@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com>`

```

"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
news:ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com...
> On Thu, 20 Nov 2003 02:24:00 GMT, "paul" <paulpigott@earthlink.net>
> enlightened us:
…[4 more quoted lines elided]…
> >believe I see what you are pointing out, though it would have been
helpful
> >if you had simply described it to begin with.
> >
…[6 more quoted lines elided]…
> >broad outlines of a standard batch progamming practice, namely the
merging
> >of two files.
> >
> >Programmers typically have some understanding of the nature of the data
that
> >he/she will be working with.  My example took the lowest common
denominator,
> >simply assuming that one file of sorted records (with unique keys) was
being
> >combined with another sorted file (in the same format, and also with
unique
> >keys).  Your example of a master file, with an associated transaction
file,
> >is also a quite common situation (though not as common as it used to be)
but
> >attempting to keep my example simple, I chose not to delve that deeply.
> >
> >To handle the situation you describe, the paragraph for FileEqual-Process
> >could be modified to continue reading File2 until a new key (or
end-of-file)
> >is encountered.  The read for File2 following the FileEqual-Process
> >execution would then be eliminated.  Minor modifications to be sure, but
> >ones that can only be done when the programmer has an understanding of
what
> >data is to be processed.
> >
…[10 more quoted lines elided]…
>

Alas, no, I didn't forget to handle one of the more common.  Please re-read
my pseudocode again.

Thanks,

Paul


>
> >Thank you for your time.
…[9 more quoted lines elided]…
> >> > I tried to reply directly to you (instead of via the newsgroup) but
you
> >have
> >> > a dummy address.
> >> >
> >> > Always being interested in learning new things, I would appreciate it
if
> >you
> >> > could point out the flaw that you see.
…[69 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-21T00:08:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hIcvb.16788$86.320157@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <Ou6vb.11724$Wy4.9378@newsread2.news.atl.earthlink.net>`

```
"paul" <paulpigott@earthlink.net> wrote in message news:Ou6vb.11724>
"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
> > Any algorithm for a match/merge logic that doesn't take into account
> > equal keys is incomplete and wrong.  Hugh was correct in pointing this
…[3 more quoted lines elided]…
> Alas, no, I didn't forget to handle one of the more common.  Please
re-read
> my pseudocode again.

Maybe Steve should have been more explicit....so I will be fore him...

"possibilities in match/merge logic and you neglected to handle 1 of the
more common [ones correctly and completely]."

If you turned this in to me as part of a homework assignment I can assure
you that your grade would be lower than Pete AND Hugh's.  I may fail them
for sharing their solution on clc but that would make me overly spiteful.  I
didn't see anyone mention the fact that the data needed to be sorted but
what the heck....that's what the curve is for in US schools....

My advice....rather than claim that you are right and you accounted for a
simple case - be it incomplete and obviously flawed- why not read the thread
look at the contributions of people like Pete/Howard et al who are "free of
charge" providing very both detailed information and,  most valuably, a
truck load of experience......Then say thanks...or..I didn't think of
that....or.... that's better than what I did....or just nothing....

JCE
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-11-20T19:46:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpjn8s$5k3$1@panix1.panix.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <Ou6vb.11724$Wy4.9378@newsread2.news.atl.earthlink.net> <hIcvb.16788$86.320157@twister.tampabay.rr.com>`

```
In article <hIcvb.16788$86.320157@twister.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>"paul" <paulpigott@earthlink.net> wrote in message news:Ou6vb.11724>
>"SkippyPB" <swiegand@neo.rr.NOSPAM.com> wrote in message
…[14 more quoted lines elided]…
>you that your grade would be lower than Pete AND Hugh's.

Those durned professors... what do *they* know, anyhow?

DD
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-20T18:56:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vrqoll8u6l6d91@corp.supernews.com>`
- **In-Reply-To:** `<ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com>`

```
I was going to stay out of this, but...

SkippyPB wrote:
> Any algorithm for a match/merge logic that doesn't take into account
> equal keys is incomplete and wrong.  Hugh was correct in pointing this
> out to you.  Whether your solution was broad or thin, there are only 3
> possibilities in match/merge logic and you neglected to handle 1 of
> the more common.

How is it not handled?

>>>>>>Read File1
>>>>>>Read File2
…[11 more quoted lines elided]…
>>>>>>        Read File2

What is the code after second else supposed to handle - if file 1 isn't 
less than file 2, and file 2 isn't less than file 1, then they must be 
equal.

Now, Hugh's example...

>>>>>File #1 - Payroll Master
>>>>>Record #1 Hugh Candlin
…[8 more quoted lines elided]…
>>>>>Record #5 etc etc

Seems more like a control-break process more than a match/merge (which 
has already been discussed at length here).

Am I missing something?  What is so wrong with paul's original 
(high-level) algorithm?
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-21T01:33:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mXdvb.12333$Wy4.90@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com>`

```
Thank you.

Paul

"LX-i" <lxi0007@netscape.net> wrote in message
news:vrqoll8u6l6d91@corp.supernews.com...
> I was going to stay out of this, but...
>
…[59 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-21T15:52:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbd7df9_1@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <mXdvb.12333$Wy4.90@newsread2.news.atl.earthlink.net>`

```

"paul" <paulpigott@earthlink.net> wrote in message
news:mXdvb.12333$Wy4.90@newsread2.news.atl.earthlink.net...
> Thank you.
>
> Paul
>

Paul,

please don't take the discussion personally. I simply want to say three
things:

1. It isn't about who's right; it's about what's right.

2. Computer code and computer algorithms are just that. They have nothing to
do with anyone's value as a person. Don't let your job define your self.

3. Realise that when you post to a public forum like this there will be
people who disagree with you. Realise also, that this is healthy...

Regards,

Pete.



> "LX-i" <lxi0007@netscape.net> wrote in message
> news:vrqoll8u6l6d91@corp.supernews.com...
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 10)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-21T03:10:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hmfvb.12858$Wy4.3640@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <mXdvb.12333$Wy4.90@newsread2.news.atl.earthlink.net> <3fbd7df9_1@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3fbd7df9_1@news.athenanews.com...
>
> "paul" <paulpigott@earthlink.net> wrote in message
…[13 more quoted lines elided]…
> 2. Computer code and computer algorithms are just that. They have nothing
to
> do with anyone's value as a person. Don't let your job define your self.
>
…[6 more quoted lines elided]…
>

FWIW, I agree with you.  Truthfully, I've been doing some serious laughing
over the back and forth that's been occurring on this thread.

I have not been taking this personally, except in one regard.

My algorithim was criticized by Hugh.  He refused to state what the problem
was.  I do not see a "MAJOR" logic hole.  If someone could explain the
"MAJOR" logic hole to me, this might all make perfect sense.

I've been coding for twenty years (give or take) and I'm perfectly willing
to learn from others (still!).  I've certainly made my share of mistakes,
stupid mis-spellings, improper punctuation and misunderstood coding
requirements.  I'm well aware of how useful another pair of eyes can be.  A
flaw was claimed for my algorithim, a flaw I cannot spot, and so far no one
has identified the flaw that is claimed.  It's hard for me to learn when
explanations are not forthcoming.

Regarding codes and algorithims, I have my own style, developed over a
number of years.  Others have their own styles.  So be it.  A good, clear
style should be understandable by any other competent programmer.

As for the disagreeing, people have been doing that with me for years (!).
You develop a thick skin in this business.  One of the side benefits
(maybe).

Regardless, can you tell me what the "MAJOR" logic flaw is that Hugh
claimed?

Thanks,

Paul




>
>
…[6 more quoted lines elided]…
> > > > equal keys is incomplete and wrong.  Hugh was correct in pointing
this
> > > > out to you.  Whether your solution was broad or thin, there are only
3
> > > > possibilities in match/merge logic and you neglected to handle 1 of
> > > > the more common.
…[18 more quoted lines elided]…
> > > What is the code after second else supposed to handle - if file 1
isn't
> > > less than file 2, and file 2 isn't less than file 1, then they must be
> > > equal.
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 11)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-11-21T03:15:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Crfvb.12862$Wy4.11386@newsread2.news.atl.earthlink.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <mXdvb.12333$Wy4.90@newsread2.news.atl.earthlink.net> <3fbd7df9_1@news.athenanews.com> <Hmfvb.12858$Wy4.3640@newsread2.news.atl.earthlink.net>`

```

"paul" <paulpigott@earthlink.net> wrote in message
news:Hmfvb.12858$Wy4.3640@newsread2.news.atl.earthlink.net...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[16 more quoted lines elided]…
> > 2. Computer code and computer algorithms are just that. They have
nothing
> to
> > do with anyone's value as a person. Don't let your job define your self.
…[14 more quoted lines elided]…
> My algorithim was criticized by Hugh.  He refused to state what the
problem
> was.  I do not see a "MAJOR" logic hole.  If someone could explain the
> "MAJOR" logic hole to me, this might all make perfect sense.
…[4 more quoted lines elided]…
> requirements.  I'm well aware of how useful another pair of eyes can be.
A
> flaw was claimed for my algorithim, a flaw I cannot spot, and so far no
one
> has identified the flaw that is claimed.  It's hard for me to learn when
> explanations are not forthcoming.
…[10 more quoted lines elided]…
> claimed?

Woops, my bad.  I didn't read your other post.  Thanks for giving your take
on this LONG LONG LONG thread.

Paul


>
> Thanks,
…[13 more quoted lines elided]…
> > > > > Any algorithm for a match/merge logic that doesn't take into
account
> > > > > equal keys is incomplete and wrong.  Hugh was correct in pointing
> this
> > > > > out to you.  Whether your solution was broad or thin, there are
only
> 3
> > > > > possibilities in match/merge logic and you neglected to handle 1
of
> > > > > the more common.
> > > >
…[19 more quoted lines elided]…
> > > > less than file 2, and file 2 isn't less than file 1, then they must
be
> > > > equal.
> > > >
…[14 more quoted lines elided]…
> > > > Seems more like a control-break process more than a match/merge
(which
> > > > has already been discussed at length here).
> > > >
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-21T15:44:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbd7c35_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message
news:vrqoll8u6l6d91@corp.supernews.com...
> I was going to stay out of this, but...
>

Sometimes Daniel, it is good to follow your instincts...<G>

> SkippyPB wrote:
> > Any algorithm for a match/merge logic that doesn't take into account
…[6 more quoted lines elided]…
>

Yes, the framework provided does recognise that a 3-way split must be
performed. But that is not the WHOLE solution.

The sins are sins of omission.

The following possibilities are not recognised or discussed (yet I believe
they are essential to a proper solution):

1. What happens at end of file on the Master?

The pseudocode says to process until EOF on BOTH Master and Detail, but you
CANNOT unless you set high values in the key of the Master when you reach
EOF on it. The logic is simply wrong.

2. What happens at end of file on the Detail?

As this is a sequential process, you may need to write unmatched master
records across to the output, after having processed all the records in the
range of the details. Again, you need to set high values in the detail key
to force the master records to be written over. If you are not going to do
that, then the solution should note that it doesn't cater for complete
processing.

3. What happens in the EQUAL Branch if there are details with duplicate
keys?

This was the basis of Skippy's objection (and I agree with him completely).
If a proposed "solution" is not going to deal with the possibility of
multiple matched transactions, then it should say so, thereby recognising
that it is not purporting to be a complete solution.

Hugh's supplied transactions covered this so I won't labour it.

>
> What is the code after second else supposed to handle - if file 1 isn't
> less than file 2, and file 2 isn't less than file 1, then they must be
> equal.
>

See above. I have another minor quibble here also... If you are coding a
three way split, you are attempting to show what happens on the 3
possibilities of the detail being HIGH, LOW, or EQUAL against the master. It
is inconsistent to compare the detail against the master, then compare the
master against the detail, for the second compare, even though the desired
effect is the same. With two files, it doesn't really matter, but with more
masters (say, 3 to 5), it adds confusion. (After 5 files, I use a totally
different technique and forget about three way splits altogether...<G>)

> Now, Hugh's example...
>
…[14 more quoted lines elided]…
>

No, it isn't a control break problem. The keys are the same; there IS no
control break.

> Am I missing something?  What is so wrong with paul's original
> (high-level) algorithm?
>
It is simply inadequate. It might just as well have said:

"Match the detail against the master and, depending on the condition,
process the record, then fetch whatever was low."

Like Paul's example, the above is not "wrong" but it is sadly lacking.

Claiming that something is a high level solution is fine, provided it is a
solution. This one was not.

In the interests of completeness, I posted a comprehensive discussion on
three way split logic which even included (Gasp!) a flow chart <G>.  I hope
that anyone lurking here, and wanting to know the full story, will take the
2 minutes needed to access this document. (It is the 640K post under this
thread.)

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-21T07:17:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031121081837.887$hG@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> The following possibilities are not recognised or discussed (yet I believe
…[6 more quoted lines elided]…
> reach EOF on it. The logic is simply wrong.

Small quibble, Pete. I don't trust high values for this purpose. If you happen
to accidentally have high values in one of the file keys, it could cause real
problems. When I'm doing match/merge logic I prefer to add a separate
field at the front of each file key in WS, set to a low value (see code below).
When a read gets EOF on a file, that separate field gets set to a higher value.
This completely avoids even the possibility of an erroneous match on high
values. My philosophy is that garbage data should not trigger any hidden
logic flaws. I don't like code with logic holes, even teeny tiny probably
never to be seen ones. :-)

       01  KEY-COMPARE-AREA.
           03  KCA-MAST-KEY.
               05  KCA-MAST-EOF        PIC  9(01) VALUE 0.
               05  KCA-MAST-FIELD-1    PIC  ?(??).
               05  KCA-MAST-FIELD-2    PIC  ?(??).
                   ...
           03  KCA-TRAN-KEY.
               05  KCA-TRAN-EOF        PIC  9(01) VALUE 0.
               05  KCA-TRAN-FIELD-1    PIC  ?(??).
               05  KCA-TRAN-FIELD-2    PIC  ?(??).
                   ...

           READ MASTER-FILE
               AT END
                   MOVE 1 TO KCA-MAST-EOF.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-21T10:27:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311211027.2a09ddf@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote 

> Small quibble, Pete. I don't trust high values for this purpose. If you happen
> to accidentally have high values in one of the file keys, it could cause real
> problems.

If it is 'accidental' then a match that uses HV as EOF will not
process this 'accidental value'.  In what way would that be a real
problem ?

If an HV transaction is actually processed then it might create an HV
master which could be a worse problem.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 11)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-21T17:12:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311211712.365a39@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <217e491a.0311211027.2a09ddf@posting.google.com>`

```
I think you all are being a bit too hard on Paul. After all he did say
 "The issue of handling end-of-file I leave as an exercise for you."
That should warm Doc's cockles.

And secondly, the FileEqual-Process  pgraph COULD loop through the
trans rec file and apply the matching trans to the current Master rec.
So, the only thing he got wrong was reading the trans rec upon return.

And lastly, after all Greg DID ask for a "simple example".

Regards, Jack. 
 




riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0311211027.2a09ddf@posting.google.com>...
> "Judson McClendon" <judmc@sunvaley0.com> wrote 
> 
…[9 more quoted lines elided]…
> master which could be a worse problem.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 12)_

- **From:** Bat Guano <bat.guano@talk21dotcom>
- **Date:** 2003-11-24T17:18:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vs4fbp2hjobo46@corp.supernews.com>`
- **In-Reply-To:** `<8a2d426e.0311211712.365a39@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <217e491a.0311211027.2a09ddf@posting.google.com> <8a2d426e.0311211712.365a39@posting.google.com>`

```
Jack Sleight wrote:
> I think you all are being a bit too hard on Paul. After all he did say
>  "The issue of handling end-of-file I leave as an exercise for you."
…[7 more quoted lines elided]…
> 

I have to agree. There is no logic error in Paul's solution and it 
happily works with the sample input files. The inclusion of error 
handling, open/close processing, end-of-file processing, etc., would 
only serve to obscure the logic of the simple example as requested by 
the original poster.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 10)_

- **From:** DSlash <Dslash@myisp.co.nz>
- **Date:** 2003-11-22T10:44:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpm18r$o4r$1@lust.ihug.co.nz>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com>`

```
In article <20031121081837.887$hG@news.newsreader.com>, 
judmc@sunvaley0.com says...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > 1. What happens at end of file on the Master?
> >
…[6 more quoted lines elided]…
> problems.

In a 1972 COBOL system I was instructed by the systems analyst to move 
all '9's to the master key at EOF, as it was display numeric format and 
high-values may have changed the field to negative. The top part of the 
key was a date in the form 99/9/9, and I wondered what would happen in 
the year 1999. He told me not to worry about it. I've always thought that 
he was somewhat short-sighted.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 11)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-21T21:46:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311212146.3875980b@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz>`

```
Hi D,

Ah, the dreaded pre-Y2K disaster. I've heard many stories and
speculation like yours and I've wondered how the date field was
usually defined and processed. Most date fields are defined as
something like yymmdd or mmddyy, etc. The month and day portions of
the date were usually defined with 2 digits to accommodate 2 digit
months/days. While a one digit month/day saves 2 bytes of media
storage per date use it complicates date processing. I wonder if there
were situations that made the one digit choice worth it.

I just dismissed it as an "urban legend"; never read anything
confirming it. I guess some shops may have stored their dates as you
describe, but I doubt it. Has anyone heard of that problem rearing its
head pre-Y2K?

Regards, Jack.



DSlash  <Dslash@myisp.co.nz> wrote in message news:<bpm18r$o4r$1@lust.ihug.co.nz>...
> In article <20031121081837.887$hG@news.newsreader.com>, 
> judmc@sunvaley0.com says...
…[17 more quoted lines elided]…
> he was somewhat short-sighted.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 12)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-22T06:24:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ziDvb.24979$86.493274@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com>`

```
The pre-Y2K myth was distributed by...that's right the US businesses. Why?
Because the US sells consulting services to the rest of the world...(This
was I suppose 3 years too early for the major offshore companies to take
advantage of).

Maybe I'm wrong but I think businesses spent way too much effort on a crisis
that was never going go happen...it was the universal project without a
business case.  No one examined the ROI.  I'm sure the old timers on clc
never had it so good though....

Y2K was the technical equivalent to the opening of Al Capone's Vault.

Whilst there may have been 99/9/9 date issues, one wonders how hard that
would really have been to fix.  I personally didn't see one...but I did
waste hours with the "Change YY to YYYY remove 2 from the whitespace"....

JCE


"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0311212146.3875980b@posting.google.com...
> Hi D,
>
…[18 more quoted lines elided]…
> DSlash  <Dslash@myisp.co.nz> wrote in message
news:<bpm18r$o4r$1@lust.ihug.co.nz>...
> > In article <20031121081837.887$hG@news.newsreader.com>,
> > judmc@sunvaley0.com says...
…[4 more quoted lines elided]…
> > > > The pseudocode says to process until EOF on BOTH Master and Detail,
but
> > > > you CANNOT unless you set high values in the key of the Master when
you
> > > > reach EOF on it. The logic is simply wrong.
> > >
> > > Small quibble, Pete. I don't trust high values for this purpose. If
you happen
> > > to accidentally have high values in one of the file keys, it could
cause real
> > > problems.
> >
…[4 more quoted lines elided]…
> > the year 1999. He told me not to worry about it. I've always thought
that
> > he was somewhat short-sighted.
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 13)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-22T07:10:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com>`

```

jce <defaultuser@hotmail.com> wrote in message news:ziDvb.24979$86.493274@twister.tampabay.rr.com...

> Maybe I'm wrong but I think businesses spent way too much effort on a crisis
> that was never going go happen...it was the universal project without a
…[3 more quoted lines elided]…
> Y2K was the technical equivalent to the opening of Al Capone's Vault.

There is no maybe - you are unequivocally wrong.

There was no crisis - unless you wish to call
the remediation effort a crisis - because
businesses did what they needed to do
to prevent a crisis that was going to happen.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-22T06:38:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031122073849.281$2o@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote:
>
> jce <defaultuser@hotmail.com> wrote:
…[13 more quoted lines elided]…
> to prevent a crisis that was going to happen.

Amen. I personally changed hundreds of thousands of lines of code that
WOULD have broken had they not been fixed. I admit I made a ton of
money doing it, but it had to be done, and my rates were much lower
than the 'competition'. I worked myself beyond the point of exhaustion
under that inexorable deadline, and I thank God thousands of others
did their part too, or it would have been a disaster. What was scaring
me around early '98 was seeing the foot dragging to do what had be
done, fearing it would be too little, too late.

The 'bunk' part was not the business software, but the stuff about autos
not running and other such nonsense. Any dummy should know that if
it runs without entering a date in the first place, it's not going to break
when the date rolls over. I was appalled that so many people bought it.
Fortunately, this did help to create an atmosphere of panic, which was
what finally provoked virtually everyone to action. Whew!

COBOL was the major code that had to be fixed because of two main
reasons. First, COBOL IS the major code (60%-80%) in existence.
And secondly, because so many COBOL programs have great longevity,
few programs in any other computer language were old enough to have
exhibited the problems.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 15)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-11-22T13:51:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FBFA21B.47CC5F86@istar.ca>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net> <20031122073849.281$2o@news.newsreader.com>`

```
Judson McClendon wrote:
> 
> "Hugh Candlin" <no@spam.com> wrote:
…[31 more quoted lines elided]…
> what finally provoked virtually everyone to action. Whew!

Embedded systems breaking were not a myth.  The processor for
maintenance cycles in one the fire engines in my town would have shut
down the engine because of long maintenance intervals.  Because many of
the volunteer firemen work for the local car dealership, they would have
been able to bypass the problem but far better to remediate in advance. 
This information was given to me by the town administrator.  Another
company I know of had a problem with a relatively new super tanker that
was discovered before rollover.  I suspect the problem in both cases was
the use of x86 chips from Intel or clones which depend on clocking chips
that keep time in yymmdd/hhmmss etc. format rather than a number of
seconds from some starting point like most computers.  While a large
number of systems were not vulnerable, I can guarantee you from having
heard the report in the Y2K office of one company that did their due
diligence, there were problems with some embedded and process systems.
> 
> COBOL was the major code that had to be fixed because of two main
…[8 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-22T17:43:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031122184429.784$N8@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net> <20031122073849.281$2o@news.newsreader.com> <3FBFA21B.47CC5F86@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:
>
> Embedded systems breaking were not a myth.

I did not mean to imply that all embedded systems were Y2K compliant.
I only said that, if you never have to enter a date in the first place, then
there is no way it is going to fail when the date rolls over. How would
it know, even if it 'wanted' to fail? For example, many people never set
the date on their VCRs, and they work fine, except to time record. Yet
some people were worried about them exploding, or some other such
nonsense.

>  The processor for
> maintenance cycles in one the fire engines in my town would have shut
> down the engine because of long maintenance intervals.

All I have to say is, anyone who makes a design decision to shut down a
fire engine because of overdue maintenance is an imbecile. Let's hope it
is them being burned alive if one actually does shut down for that
reason.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 16)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-23T01:50:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mnUvb.99681$Ec1.4603110@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net> <20031122073849.281$2o@news.newsreader.com> <3FBFA21B.47CC5F86@istar.ca>`

```

Clark F. Morris, Jr. <cfmtech@istar.ca> wrote in message news:3FBFA21B.47CC5F86@istar.ca...
> Judson McClendon wrote:
> >
…[27 more quoted lines elided]…
> diligence, there were problems with some embedded and process systems.

Hmmmm.  How is the UNIX/LINUX remediation effort coming along?
Anybody know?  Has anybody even started?  Probably not.
It won't rollover until '38.  "Not our problem", right?  Right!!
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 14)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-25T07:23:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VrDwb.773$Cv6.506@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message
news:1_Dvb.307887$0v4.18272005@bgtnsc04-news.ops.worldnet.att.net...
>
> jce <defaultuser@hotmail.com> wrote in message
news:ziDvb.24979$86.493274@twister.tampabay.rr.com...
>
> > Maybe I'm wrong but I think businesses spent way too much effort on a
crisis
> > that was never going go happen...it was the universal project without a
> > business case.  No one examined the ROI.  I'm sure the old timers on clc
…[8 more quoted lines elided]…
> to prevent a crisis that was going to happen.
The "crisis" was blown out of all proportion by the USA.
I'd be interested to read a comparative study of Y2K handling....I would
100% certain that the USA per LOC cost of Y2K mitigation strategy would be
much higher than anywhere else assuming a global flat remediation rate.  The
USA sells more consulting services than any other nation and thus had the
most to gain by pressing the issue.   In addition, the legal system in the
USA means that the risks associated with civil claims are that much higher.

Now - there *were* specific items that did need to be addressed.  I will
accept that a certain amount of investigation would be required to ensure
that "high-risk" items were taken care of.  What I also know is that many
things would function just fine and dandy even if the date processing was
not Y2K compliant and millions of dollars were spent on these items.

The only difference between this and any other bug is that it would have
multiple instances at the same time....I don't see any investment in fixing
any "normal" bugs...you know the "every monday..or every second
tuesday"...analysis.....because companies don't care about "errors" they
care about their external appearance to outsiders with regard to "errors".
Big business was afraid of what damage would be done to their reputation
because of the eyes looking....rather than worreid about the problems
themselves.  I'd venture a guess and say that a number of bugs were actually
"introduced" as a result of Y2K experts rushing though 1000s of lines of
code in double time.

I'm terribly big business cynical as you can probably guess.

JCE
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 13)_

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-11-23T01:24:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bq3ned$f2o$8@news.utelfla.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com>`

```
jce <defaultuser@hotmail.com> wrote:

: Whilst there may have been 99/9/9 date issues, one wonders how hard that
: would really have been to fix.  I personally didn't see one...but I did
: waste hours with the "Change YY to YYYY remove 2 from the whitespace"....

I have to say I have never heard of anyone using a four-digit number to
represent a date before... It's always been my experience to have them
declared as alphanumerics.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-01T14:42:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bqfk04$r5l$1@peabody.colorado.edu>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <ziDvb.24979$86.493274@twister.tampabay.rr.com> <bq3ned$f2o$8@news.utelfla.com>`

```

On 22-Nov-2003, weberm@polaris.net (Ubiquitous) wrote:

> I have to say I have never heard of anyone using a four-digit number to
> represent a date before... It's always been my experience to have them
> declared as alphanumerics.

I have seen dates stored packed decimal digits.   I thought this was in the deep
past until I came across a vendor supplied file two weeks ago that did so.

I have also seen them stored as binary.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 12)_

- **From:** DSlash <Dslash@myisp.co.nz>
- **Date:** 2003-11-22T20:52:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpn4t3$4qr$1@lust.ihug.co.nz>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com>`

```
In article <8a2d426e.0311212146.3875980b@posting.google.com>, 
jacksleight@hotmail.com says...
> Hi D,
> 
…[12 more quoted lines elided]…
> head pre-Y2K?

It's more than 30 years ago so the details are a bit hazy. It was an ICL 
tape file and the date was probably of the form yymmdd. It's possible 
that I was instructed to move the date 99/09/09 to that, because that is 
a valid date while 99/99/99 is not. I do recall wondering what would 
happen on 10 Sept 1999, which is a few months earlier than the system 
would need to be changed for the year 2000.
Being a junior programmer at the time I listened to my elders and betters 
and did what they said!
Basically they said that after 28 years the system would have been 
rewritten. But it would have been very easy to include the century in the 
date and stave off the evil day for another 8000 years!

I later discovered that the DP manager was relying on the fact that he 
was the only person who could maintain the heavily patched assembler 
program that updated the main master file, and that he was unhappy that I 
succeeded in rewriting it in COBOL (a task which they gave to all the 
newbies).
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 13)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-22T08:18:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz>`

```

DSlash <Dslash@myisp.co.nz> wrote in message news:bpn4t3$4qr$1@lust.ihug.co.nz...
>
> Basically they said that after 28 years the system would have been
> rewritten.

They had been making similar incorrect predictions
since COBOL was originally developed and put to use.

> But it would have been very easy to include the century in the
> date and stave off the evil day for another 8000 years!

No.  No.  And no.

The problem doesn't roll around every 10,000 years.
The problem doesn't roll around every 1,000 years.
The problem rolls around AT LEAST every 100 years,
with the exact timeframe being dependent upon the value
decided upon for use in the windowing algorithm.

I think that there are some companies that probably
need to start their Y2100 remediation project right about now.
Insurance companies and actuarial companies would be my guess.

But they won't, until they figure it out for themselves,
or until they experience a malfunction related to the year 2100 and up.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-22T06:43:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031122074415.782$DV@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote:
>
> I think that there are some companies that probably
> need to start their Y2100 remediation project right about now.
> Insurance companies and actuarial companies would be my guess.

Ha! No chance of them doing that. What do you want to bet people will
soon began to revert to two digit year again? At least I won't live to see
that one. :-)
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 15)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-23T01:41:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HfUvb.99659$Ec1.4602250@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <20031122074415.782$DV@news.newsreader.com>`

```

Judson McClendon <judmc@sunvaley0.com> wrote in message news:20031122074415.782$DV@news.newsreader.com...
> "Hugh Candlin" <no@spam.com> wrote:
> >
…[4 more quoted lines elided]…
> Ha! No chance of them doing that.

They don't have a choice if they want their systems to work.

Where windowing was chosen as the "solution" - stopgap is a better description -
the problem is further compounded in that the upcoming remediation effort
to resolve the next century processing issue (whoever coined the term
"millennium problem" seriously clouded the issue and did nobody a favor)
will have to deal with not 2 but 3 different century values, as they will for
the first time have 19th century values, 20th century values and 21st century values.

Take the scenario where a property management company
signs up a customer for a new 99 year lease.  They currently have data from
prior to 2000, data for 2000-2099, and will now have to handle 2100 and up.
Goodbye windowing, unless they can figure out a way to retain it and still
calculate century values properly, perhaps by using the system date
as a data creation indicator to determine which century to use, although this
technique is fraught with issues.  I probaly wouldn't do it this way.

> What do you want to bet people will
> soon began to revert to two digit year again?

That thought never crossed my mind, I can honestly say.
But you are correct - it could happen.  I sincerely hope not.

> At least I won't live to seethat one. :-)

I've heard that one before.  Too many times.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-23T06:48:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031123074856.446$xr@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <20031122074415.782$DV@news.newsreader.com> <HfUvb.99659$Ec1.4602250@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote:
> Judson McClendon <judmc@sunvaley0.com> wrote:
> > "Hugh Candlin" <no@spam.com> wrote:
…[7 more quoted lines elided]…
> They don't have a choice if they want their systems to work.


I meant "No chance of them doing that [ahead of time]." :-)

Actually, systems that must deal with three centuries in the past (e.g.
birth dates) are already fixed, or they won't work now. Probably most
archival type databases (e.g. public deed records) were created Y2K
compliant because they already dealt with multiple centuries.

Fortunately, none of my clients tried to window file dates, they all
went for ccyymmdd. I didn't have to urge them very strongly, most had
the attitude "Let's fix this thing, permanently."

I remember a similar, minor 'crisis' in the late 60's when punched card
systems with only one digit year had to be fixed. Fortunately, all the
punched card systems were already being rapidly replaced anyway, so
stopgap measures were acceptable. Those who were not there at the
time simply cannot comprehend how restricted and valuable storage
space and CPU time were in those days. People were cheap, hardware
was expensive, quite the reverse of today. Also, many people fail to
appreciate that, when the whole industry was very young, and things
were changing so rapidly, it was not at all clear that COBOL systems
would last thirty or forty years. Even looking back, that fact is still
incredible to me. I wrote a COBOL client/server based inventory
system in 1986-87 that is still in use today. Initially running under
DOS and now Win32, except for enhancements, the code is virtually
untouched. I don't know of any other language that would have been
anywhere near that stable for so long.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-24T16:20:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bptb3j$bmr$1@peabody.colorado.edu>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <20031122074415.782$DV@news.newsreader.com>`

```

On 22-Nov-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Ha! No chance of them doing that. What do you want to bet people will
> soon began to revert to two digit year again? At least I won't live to see
> that one. :-)

In programs?   Very little.   The only problem is where data entry assumes a
"20" when it stores the date in the first place.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 14)_

- **From:** DSlash <Dslash@myisp.co.nz>
- **Date:** 2003-11-24T01:02:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpq7ub$3tv$1@lust.ihug.co.nz>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <5ZEvb.308172$0v4.18276426@bgtnsc04-
news.ops.worldnet.att.net>, no@spam.com says...
> 
> DSlash <Dslash@myisp.co.nz> wrote:
…[10 more quoted lines elided]…
> decided upon for use in the windowing algorithm.

I don't understand what you are saying.
If the date includes the century, I.e. is held in the form YYYYMMDD,
why would there be any problems before the year 10,000?
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 15)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-23T18:59:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <bpq7ub$3tv$1@lust.ihug.co.nz>`

```

DSlash <Dslash@myisp.co.nz> wrote in message news:bpq7ub$3tv$1@lust.ihug.co.nz...
> In article <5ZEvb.308172$0v4.18276426@bgtnsc04-
> news.ops.worldnet.att.net>, no@spam.com says...
…[16 more quoted lines elided]…
> why would there be any problems before the year 10,000?

It is very simple, if you first understand that your qualifying statement
"If the date includes the century" is not adequately specific.
"The date", as you refer to it, may refer to a date field on an internal dataset,
but that does not necessarily mean that original external source files
also are in the format CCYYMMDD, because Company A cannot always
dictate that Company B must supply the information in that format.
If YYMMDD is what they want to supply, then YYMMDD
is (probably) what you are going to get, unless you are a COSTCO,
WAL*MART, Intel or Microsoft, and CAN dictate in this manner
to your suppliers.  So that is where windowing comes in.
You have to have an algorithm to determine what the CC value should be.

Something like

IF    DATE-YY  <  25
       MOVE    20    TO    DATE-CC
ELSE
       MOVE    19    TO    DATE-CC.

Now stop and think about companies which will soon have dates
in the range 2100 and up.  What do they do, and when do they do it?

My point is that there are many companies who have not yet realized
that it wasn't a "millennium" problem that will not occur again for
another 1000 years, or 10,000 years.  It will have an impact on every
100 year cycle, and the cycle doesn't starts in 2100.

Add your windowing factor to 2000.  In my example, add 25 + 2000 = 2025.
Then back off 5 years or so to allow for remediation and integration testing.

The same lack of foresight and short-sighted cost-cutting is what got the world
into the Y2K mess in the first place.  The current decimation of the employment
ranks and offshore job transfers is another such misguided effort.

I may be the only one in the world who thinks this way,
but I can live with that, quite comfortably.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-24T13:42:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fc1541c_5@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <bpq7ub$3tv$1@lust.ihug.co.nz> <bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net...
>
> DSlash <Dslash@myisp.co.nz> wrote in message
news:bpq7ub$3tv$1@lust.ihug.co.nz...
> > In article <5ZEvb.308172$0v4.18276426@bgtnsc04-
> > news.ops.worldnet.att.net>, no@spam.com says...
…[20 more quoted lines elided]…
> "The date", as you refer to it, may refer to a date field on an internal
dataset,
> but that does not necessarily mean that original external source files
> also are in the format CCYYMMDD, because Company A cannot always
…[23 more quoted lines elided]…
> Then back off 5 years or so to allow for remediation and integration
testing.
>
> The same lack of foresight and short-sighted cost-cutting is what got the
world
> into the Y2K mess in the first place.  The current decimation of the
employment
> ranks and offshore job transfers is another such misguided effort.
>
> I may be the only one in the world who thinks this way,
> but I can live with that, quite comfortably.
>

Hugh, some observations...

1. I share DSlash's confusion as to why using CCYYMMDD won't fix it. I
believe it will. Your discussion above doesn't address that, it introduces
external factors which are perfectly valid, but leaves us NOT knowing
whether you agree that CCYYMMDD is a "proper" solution.

2. You have obviously been exposed to people who used "windowing" as a Y2K
solution. I don't believe that was ever a solution and I said so at the
time. Anyone who implemented it deserves whatever they get...

You are absolutely correct in what you say about short sighted cost cutting
(particularly when it comes to "windowing" as a solution), but that isn't
what got us into the Y2K mess in the first place.

It  is much more complex than that.

Who could have believed when writing commercial code in the 1970s that that
same code might still be around in the year 2000? Given that storage was
incredibly expensive, I don't believe ANYONE could have made and won the
argument to add 2 bytes to every date in every system, in say, 1969... Given
also that even the operating systems returned a 2 digit year, it is
understandable that programmers figured a two digit year was adequate.

What DIDN'T happen was a plan to start implementing 4 digit years by a
certain time, say, 1990. There were just too many other pressures, and by
then we were locked in to our legacy systems. Furthermore, most Managers
were not aware of the implications of the problem (they are, for the most
part, not programmers) and those who were aware had to balance preparing for
Y2K against continuing to provide full service, without an increase in their
budgets or acquiring extra resources.

Only when the Millennium was almost on us and the media started trumpeting
about the Y2K "bug" (it never was a bug; it was intended to be that way...),
did the collective consciousness get raised to the point where it was
realised something HAD to happen. By then it was 1998...<G>

The computer industry as a whole responded valiantly to the challenge, and I
still remember teams going way beyond the call of duty to "get it right".
The same media that bayed for our blood and the general public who perceived
it all as a great con by the computer industry, will never know how close it
was. Those of us who were in it, know. OK, we got paid for it and we
delivered, but for many there was a bitter aftertaste. (If anyone reading
this is in that category, take solace from this: YOU know what it took. It
wasn't your problem and you were not responsible for it, but you fixed it.
And your peers know too.)

3. The recurring problems you outlined above (correct me if I am wrong here)
will only happen on systems where "windowing" was adopted as a "solution"?
(Solutions that bit the bullet and implemented CCYYMMDD, should have no
problems, right?).

I take your point about external systems feeding in, also needing to
implement CCYYMMDD. But, given that that is in place, there would be no
problem?

If you agree with that, then I think DSlash and I would have no arguments
with what you wrote. If you don't, then I for one would need more
explanation.

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 17)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-24T05:37:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DOgwb.104552$Ec1.4736894@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <bpq7ub$3tv$1@lust.ihug.co.nz> <bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net> <3fc1541c_5@news.athenanews.com>`

```

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in message news:3fc1541c_5@news.athenanews.com...
>
> "Hugh Candlin" <no@spam.com> wrote in message
…[71 more quoted lines elided]…
> whether you agree that CCYYMMDD is a "proper" solution.

The use of CCYYMMDD is a "proper" 8000 year stopgap
if every company uses it.  Not all companies do.

If DSlash's company has no external interfaces,
then I agree that a CCYYMMDD date storage format
should be adequate for their purposes.

I was addressing the bigger picture, and have been all along.
If that was the cause of confusion, I do apologise to one and all.
>
> 2. You have obviously been exposed to people who used "windowing" as a Y2K
> solution. I don't believe that was ever a solution and I said so at the
> time. Anyone who implemented it deserves whatever they get...

You are correct.  Many companies did use windowing, including Microsoft
(no connection to Microsoft Windows, the OS).  I think they used more than one
windowing factor in some of their products, if my memory serves me correctly,
so that the result you get could be 100 years apart when a given date is processed
in 2 different applications, such as Access and Excel.  They may have fixed it, though.

>
> You are absolutely correct in what you say about short sighted cost cutting
> (particularly when it comes to "windowing" as a solution), but that isn't
> what got us into the Y2K mess in the first place.

Yes it was.
>
> It  is much more complex than that.

No, it was simple.  They didn't want to spend the money then.
By the year 2000, we'd have flying cars and COBOL would be long gone
and we'd have world peace and a cure for cancer and a way to stop
washing machines from eating socks...........
>
> Who could have believed when writing commercial code in the 1970s that that
> same code might still be around in the year 2000?

I did.  I always did.  I got laughed at.  Guess what?  Some people are still laughing.

> Given that storage was
> incredibly expensive, I don't believe ANYONE could have made and won the
> argument to add 2 bytes to every date in every system, in say, 1969...

It was one of the first suggestions I ever made, earlier than 69, even.
Won?  Hah!  They looked at me like I was an alien from the planet Cheese.

> Given also that even the operating systems returned a 2 digit year, it is
> understandable that programmers figured a two digit year was adequate.

Some did.  Most didn't.  But the intelligent ones weren't calling the shots.
>
> What DIDN'T happen was a plan to start implementing 4 digit years by a
…[25 more quoted lines elided]…
> problems, right?).

CCYYMMDD isn't a solution.  It is an internal data storage format.
The problem is that external data feeds may be and in many cases
are still not compliant.  Therein lies the problem.
>
> I take your point about external systems feeding in, also needing to
> implement CCYYMMDD. But, given that that is in place, there would be no
> problem?

Get rid of windowing, and I can shut up.  Yes, you are correct.

> If you agree with that, then I think DSlash and I would have no arguments
> with what you wrote. If you don't, then I for one would need more
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 18)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-11-25T07:28:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PwDwb.774$Cv6.745@twister.tampabay.rr.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <bpq7ub$3tv$1@lust.ihug.co.nz> <bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net> <3fc1541c_5@news.athenanews.com> <DOgwb.104552$Ec1.4736894@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:DOgwb.104552$Ec1.4736894@bgtnsc05-news.ops.worldnet.att.net...
> You are correct.  Many companies did use windowing, including Microsoft
> (no connection to Microsoft Windows, the OS).  I think they used more than
one
> windowing factor in some of their products, if my memory serves me
correctly,
> so that the result you get could be 100 years apart when a given date is
processed
> in 2 different applications, such as Access and Excel.  They may have
fixed it, though.
They release a new version for us to spend our money on every year....they
could fix it any year they wanted....but I'm sure they're in Redmond
thinking "We're never going to get to 2025 - Linux will have won by
then...."

JCE
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-24T16:22:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bptb8n$cfm$1@peabody.colorado.edu>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com> <bpm18r$o4r$1@lust.ihug.co.nz> <8a2d426e.0311212146.3875980b@posting.google.com> <bpn4t3$4qr$1@lust.ihug.co.nz> <5ZEvb.308172$0v4.18276426@bgtnsc04-news.ops.worldnet.att.net> <bpq7ub$3tv$1@lust.ihug.co.nz> <bs7wb.102594$Ec1.4678239@bgtnsc05-news.ops.worldnet.att.net>`

```

On 23-Nov-2003, "Hugh Candlin" <no@spam.com> wrote:

> It is very simple, if you first understand that your qualifying statement
> "If the date includes the century" is not adequately specific.
…[8 more quoted lines elided]…
> to your suppliers.

EVERYBODY can demand yymmdd dates be supplied to them, unless the supplier is
the U.S. government or one of the above.   And those guys will agree with you.

There is no reason to do windowing other than data entry anymore.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-22T16:45:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbedbee_5@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com> <20031121081837.887$hG@news.newsreader.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031121081837.887$hG@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > The following possibilities are not recognised or discussed (yet I
believe
> > they are essential to a proper solution):
> >
…[6 more quoted lines elided]…
> Small quibble, Pete. I don't trust high values for this purpose. If you
happen
> to accidentally have high values in one of the file keys, it could cause
real
> problems. When I'm doing match/merge logic I prefer to add a separate
> field at the front of each file key in WS, set to a low value (see code
below).
> When a read gets EOF on a file, that separate field gets set to a higher
value.
> This completely avoids even the possibility of an erroneous match on high
> values.

It does, but it is totally unnecessary.

Think about it...

"An ACCIDENTAL key of  HIGH VALUES..."

1. This accident could not occur on the Master, and even if it did, it would
be the last record on the file.

2. For the 3 way split to function correctly, the detail must be sorted, so
the accidental record HAS to be at the end of the Details, i.e. it would be
the last transaction. The only way this would not happen would be if the the
previous SORT step failed. In the code I posted this condition was detected,
so there is NO NEED to do ANYTHING with keys in WS or anywhere else.

This error (in the extremely unlikely event that it happened) would be
picked up because the control totals would be wrong. The number of records
coming out of the SORT would NOT balance to the number of records processed
in the 3 way split.

> My philosophy is that garbage data should not trigger any hidden
> logic flaws. I don't like code with logic holes, even teeny tiny probably
> never to be seen ones. :-)

An admirable point of view, unfortunately not borne out by the code you
posted.

So why did you not detect a sequence error on the input? (Even though this
can never happen unless the previous SORT step fails, sorts have been known
to fail... I think Satan was wearing an anorak when the last one did...<G>)

Doing what you suggest, in my opinion, simply adds complexity for no
realistic gain.

I posted the code sample to illustrate what I mean by checking from top down
and actioning from bottom up. You made no comment. Would you then agree that
this approach eliminates redundant tests for control breaks and EOF (as was
shown in your own code sample), or do you still believe that what you have
is as good as it gets?

It really doesn't matter in practice, but I took the time to post, because
you said you disagreed with this tenet. I was hoping to persuade you... <G>.
A comment from you would indicate whether I did or not <G>.

(I respect your right to do it any way you want to and I won't pursue the
argument. I'd just like to know whether posting code here (which I really
HATE doing) makes any difference...)

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-11-21T18:11:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vrtadist5jnnd7@corp.supernews.com>`
- **In-Reply-To:** `<3fbd7c35_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net> <GlTub.86244$Ec1.4256308@bgtnsc05-news.ops.worldnet.att.net> <4BVub.11030$Wy4.3809@newsread2.news.atl.earthlink.net> <ugjprvseklk6965iij65d5cl3jp5lr62b6@4ax.com> <vrqoll8u6l6d91@corp.supernews.com> <3fbd7c35_9@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message
> news:vrqoll8u6l6d91@corp.supernews.com...
…[5 more quoted lines elided]…
> Sometimes Daniel, it is good to follow your instincts...<G>

heh - but messing up in public is how I learn!  :)

> The sins are sins of omission.
> 
…[24 more quoted lines elided]…
> that it is not purporting to be a complete solution.

okay - I guess I just wan't expecting anything that could be written in 
about 9 lines to be a complete solution anyway.  :)  Whereas everyone 
else saw it and said "Oh, look at all that's missing", I saw it and said 
"Yeah, that's the basic idea".

> It is simply inadequate. It might just as well have said:
> 
…[12 more quoted lines elided]…
> thread.)

I'll look forward to that.  (or back - though I thought I had read this 
thread completely as it happened...)

Thanks for the explanation.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 4)_

- **From:** Paul Knudsen <r459jx602@sneakemail.com>
- **Date:** 2003-11-29T06:12:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<15egsvcvch7m3r1qh802fdd0hg8ajos467@4ax.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <akfub.7247$Wy4.1451@newsread2.news.atl.earthlink.net> <7_hub.280031$0v4.17791674@bgtnsc04-news.ops.worldnet.att.net> <RRSub.9131$Rk5.4790@newsread1.news.atl.earthlink.net>`

```
On Wed, 19 Nov 2003 23:17:05 GMT, "paul" <paulpigott@earthlink.net>
wrote:

>I tried to reply directly to you (instead of via the newsgroup) but you have
>a dummy address.
>
>Always being interested in learning new things, I would appreciate it if you
>could point out the flaw that you see.

There isn't one.  Nobody would be dumb enough to use a Name for a key.
Well...almost nobody.
```

#### ↳ Re: match program example

- **From:** docdwarf@panix.com
- **Date:** 2003-11-17T21:38:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpc0ne$4l8$1@panix1.panix.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>`

```
In article <v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>,
 <gregjohnson@comcast.net> wrote:
>Does anyone have a simple example of a COBOL match program.  I need to
>become more familiar with the logic.

Please do your own homework.

DD
```

##### ↳ ↳ Re: match program example

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-19T14:11:02+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbac348_4@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <bpc0ne$4l8$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bpc0ne$4l8$1@panix1.panix.com...
> In article <v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>,
>  <gregjohnson@comcast.net> wrote:
…[6 more quoted lines elided]…
>
```

#### ↳ Re: match program example

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-11-18T01:12:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0311180112.57823b99@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>`

```
Hi Greg,

When you reach EOF on a file, move hi-vals to the key as well as
setting the EOF switch for the file. That provides a simple solution
the problem of having more recs in one file than the other. Notice
that no change to the primary algorithm is required.

Doc is right about doing your own homework. But in this case you
picked one of the 2 most used algorithms in batch processing, and
using an efficient and consistant solution in these situations s/b
taught (but usually isn't) in the classroom. You'll find yourself
using variations of them constantly.

The other of the 2 is called the control break algorithm. I would
guess that these 2 algorithms could be found in more than 80% of batch
pgms. You'll also come across some variations in on-line pgms and also
see both combined in some pgms.

You'll find yourself using variations of these constantly, and for
that reason I've enclosed a discussion of control a break methodology
below. You may want to study this along with Paul's file match
solution and use them as models whenever the occasion requires.

As you become more familiar with the concepts you may want to change
and improve them or you may find other solutions more to your liking.
The important thing is to adopt a uniform, "canned" solution that can
save you hundreds of hours of pgming time and assure consistent
results.

Regards, Jack   

Control Break Discussion:

Input data is usually presented to a pgm in some sort sequence, e.g:


                    file
                      acct#1
                        product1
                          date1
                          date2
                          etc.
                        product2
                          date1
                          date3
                          date4
                          etc.
                      acct#2
                        product1
                          date3
                          etc.


So you have a file level, an acct level, a product level and a date
level. These levels are important because they are used to process the
breaks in the program.
						                  
The general form is as follows:

		perform level n until level n-1 is finished

For the file described above the perform sequence would be:


	            In the mainline you code: 
                       perform acct-lev until file-is-finished
               	    In the acct-lev you code: 
                       perform prod-lev until acct-is-finished
                    In the prod-lev you code: 
                       perform date-lev until prod-is-finished
                    In the date-lev you code: 
                       perform detl-lev until date-is-finished
                    In the detl-lev you code: 
                       Aggregate all detl recs; aggregate all level
                       totals; etc.
                       Read next I/P detl rec

OK now lets flesh this out. How do we determine when each level is
finished? One way is to expand the function of the read routine to do 
  this:

                    7000-read-rtn.
                        move ws-ip-rec to ws-ip-prev
                        read ip-file into ws-ip-rec 
                          at end set ip-eof to true 
                             move high-values to ws-ip-rec  
                         not at end add +1 to ws-ip-cnt
                       end-read
                       perform 7010-set-breaks
                       .
                    7010-set-breaks.
                        if curr-acct not = prev-acct
                           set acct-is-finished to true
                           set prod-is-finished to true 
                           set date-is-finished to true
                        end-if
                        if curr-prod not = prev-prod
                           set prod-is-finished to true
                           set date-is-finished to true
                        end-if
                        if curr-date not = prev-date
                           set date-is-finished to true
                        end-if


Second question: We haven't read any data yet, how can we test if the
levels are finished? We do a priming read outside of the loops,
usually in the init or mainline section. After this read, if EOF is
detected, an error msg is displayed and the pgm is usually exited
because no input data has been provided.

How can the loops be executed if the "is-finished" switch has already
been set? They can't. So, we reset the switch before executing each
lower level:


                    main-line.
                        perform 7000-read-ip
                        if ip-eof
                           display error msg
                           stop run
                        end-if 
                        perform acct-lev until file-is-finished
                        perform 6900-print-rpt-end
                        perform 9000-end-it
                        stop run
                        .
                    acct-lev.
                        perform 6000-print-rpt-heads
                        set reset-acct-sw to true 
                        perform prod-lev until acct-is-finished
                        perform 6100-print-acct-tots 
                        zero tots, etc. 
                        .
                    prod-lev.
                        set reset-prod-sw to true 
                        perform date-lev until prod-is-finished
                        . 
                    date-lev.
                        set reset-date-sw to true 
                        perform detl-lev until date-is-finished
                        . 
                    detl-lev.
                        move ip data to rpt-line or whatever
                        perform 7000-read-ip
                        .


Note that the form of each level except the detail level is:

Do pre-break stuff (print rpt heads, save data that won't be available
after return from perform, etc.)

Reset the level switch.

Perform the next lower level.

Do post-break stuff (strike and/or zero or roll totals, write total
recs, etc.)

At the detail level process the previous rec and read the next rec
before exiting.

At entry to each level the record has already been read and is ready
for processing.

Here's what a break switch would look like:



                        01 ws-break-switches.
                           05 ws-acct-sw                 pic x(001).
                              88 acct-is-finished            value
'F'.
                              88 reset-acct-sw               value
'R'.
 

This example has 2 break levels so your performs would look like:

                    0000-mainline.
                        . 
                        . 
                        .
                        perform 8000-init
                        perform 7000-read-ip 
                        if ip-eof 
                           display 'no data in i/p file' 
                           stop run 
                        end-if
                        perform 1000-process-codes until ip-eof
                        . 
                        . 
                        . 
                    1000-process-codes.
                        set reset-code-sw to true
                        perform 1100-process-detl until
                             code-is-finished
                        .
                    1100-process-detl.
                        collect data, etc.
                        perform 7000-read-ip
                        .



You have to ask: What do I do before the breaks; what do I do after.
The answers to these questions may differ from project to project, but
the basic concept: the cascading perform process is constant.

There are are other slightly more efficient ways of solving this
problem but I tried to keep my version as "readable" as possible.





gregjohnson@comcast.net wrote in message news:<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com>...
> Does anyone have a simple example of a COBOL match program.  I need to
> become more familiar with the logic.
> 
> Thank you.
```

##### ↳ ↳ Re: match program example

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-19T12:52:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbab0d8_8@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com>`

```

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0311180112.57823b99@posting.google.com...
<snip>>
> Control Break Discussion:
>
Good example, Jack.

It can be paraphrased as:

"Check control breaks from the highest to the lowest (top down); action
control breaks from the lowest to the highest (bottom up)"

I remember a very wise programmer, now sadly departed to the great template
in the sky, imparting these words of wisdom to my youthful ear over 30 years
ago.

<snip of lengthy, but useful, example>

Pete.
```

###### ↳ ↳ ↳ Re: match program example

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-19T15:02:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpg0md$ioj$1@peabody.colorado.edu>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com>`

```

On 18-Nov-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> "Check control breaks from the highest to the lowest (top down); action
> control breaks from the lowest to the highest (bottom up)"

I've coded control breaks without thinking since 1969 without coming across
those terms.   Occasionally match-merge logic requires that I think a moment,
with flow examples.

But I don't know whether I code check control breaks or action control breaks. 
I'm not picturing bottom up logic here either.
```

###### ↳ ↳ ↳ Re: match program example

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-19T12:30:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031119133040.679$F9@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> "Check control breaks from the highest to the lowest (top down); action
> control breaks from the lowest to the highest (bottom up)"

I disagree, Peter. Many years ago I spent over two years doing mostly
writing report programs. During that time I wrote several hundred report
programs, and I took the opportunity to experiment and study every
control break method I could think of and every method anyone else
would suggest. I looked at number of lines of code, clarity, flexibility,
etc. My conclusion was that the method illustrated in the sample code
below is at least as good as, usually better than, any other method I
have ever seen, in all respects.

The code below is for a three level control break, plus a final end of
file control break.  The code was copied from a long running program,
and extraneous stuff stripped out. The items bounded by < > are
descriptive, not specific. Omit any that don't apply in a given case. I
am suffering from a cold and my brain has turned to oatmeal, so please
excuse any typos, and try not to quibble about your particular brand of
coding style; it's the logic I'm trying to illustrate. :-)

       01  CONTROL-BREAK-AREA.
           03  CBA-CURRENT.
               05  CBA-CURR-LEVEL-1.
                   07  CBA-CURR-LEVEL-2.
                       09  CBA-CURR-LEVEL-3.
                           11  CBA-CURR-LEV-3-FIELD  PIC  ?(??).
                       09  CBA-CURR-LEV-2-FIELD      PIC  ?(??).
                   07  CBA-CURR-LEV-1-FIELD          PIC  ?(??).
           03  CBA-PREVIOUS.
               05  CBA-PREV-LEVEL-1.
                   07  CBA-PREV-LEVEL-2.
                       09  CBA-PREV-LEVEL-3.
                           11  CBA-PREV-LEV-3-FIELD  PIC  ?(??).
                       09  CBA-PREV-LEV-2-FIELD      PIC  ?(??).
                   07  CBA-PREV-LEV-1-FIELD          PIC  ?(??).


      INITIALIZE-REPORT.
           OPEN INPUT WORK-FILE.
           READ WORK-FILE
               AT END
                   MOVE 1 TO WS-END-FLAG.
           MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD.
           MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD.
           MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD.
           PERFORM PROCESS-ACTIVITY
               UNTIL (WS-END-FLAG = 1).


       PROCESS-RECORDS.
           MOVE CBA-CURRENT TO CBA-PREVIOUS.
           MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD.
           MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD.
           MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD.
           IF (CBA-CURRENT > CBA-PREVIOUS)
               PERFORM LEVEL-1-BREAK.

           <Process Current Work Record>

           READ WORK-FILE
               AT END
                   MOVE 1 TO WS-END-FLAG.


       LEVEL-1-BREAK.
           <Complete/Print Level 1 Break>

           IF (CBA-CURR-LEVEL-2 > CBA-PREV-LEVEL-2)
               OR
              (WS-END-FLAG = 1)
               PERFORM 029200-LEVEL-2-BREAK.

           <Initialize/Print Next Level 1 Stuff>


       LEVEL-2-BREAK.
           <Complete/Print Level 2 Break>

           IF (CBA-CURR-LEVEL-3 > CBA-PREV-LEVEL-3)
               OR
              (WS-END-FLAG = 1)
               PERFORM LEVEL-3-BREAK.

           <Initialize/Print Next Level 2 Stuff>


       LEVEL-3-BREAK.
           <Complete/Print Level 3 Break>

           IF (WS-END-FLAG = 1)
               PERFORM LEVEL-4-BREAK.


       LEVEL-4-BREAK.
           <Complete/Print Level 4 Break>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-19T14:35:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311191435.4f93f153@posting.google.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote 

> I disagree, Peter.

> Many years ago I spent over two years doing mostly
> writing report programs. During that time I wrote several hundred report
> programs,

20 years ago or so I decided that I just didn't want to do that, so I
wrote one huge report program that does most of the reports based on a
simple script telling it what to do: which files as main and
secondary, what to select, which fields to print and what control
breaks to action.

Now most reports can be created and changed by a few seconds with a
text editor on the report scripts.

*REPORT EXAMPLE
- lines starting - are comments
*TITLE Simple example printing debtors balances in Rep seq
*FILE DB
*COMPUTE
%1TOTAL  = CURR-BAL E 3MTH-BAL
- E operation is 'sum of'
*SELECT
SALESREP IN ?
%1TOTAL  != 0
- the ? indicates that the user will be asked for an entry
- at run time. The 'IN' requires a list, or a single entry.
*COMMENT
Enter a list of SalesReps required comma separated
or press F6 for all SalesReps
*INDEX
SALESREP P
%1TOTAL  -
- sort is to salerep then descending (-) total balance
- new page (P) for each salesrep. All values totalled.
*LINE 01 S
NAME
PHONE
%1TOTAL
CURR-BAL
1MTH-BAL
2MTH-BAL
3MTH-BAL
MTHSALES
*ENDREPORT

Because this had to cater for varying number of control levels (up to
4) on just about any field in the data record or from the calculations
I did have to spend some time making it work in all cases, including
no sorting required or no control breaks at all.  However that was all
so long ago I have forgotten.

It does basically check the levels from the top down and action them
from the bottom up.  As the program had to work in many different ways
it couldn't just integrate the code as you have done, it had to be
much more modular, just as code should be.

I am afraid that I will have to agree with Peter.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-20T13:25:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbc0a4d_7@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <217e491a.0311191435.4f93f153@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0311191435.4f93f153@posting.google.com...
> "Judson McClendon" <judmc@sunvaley0.com> wrote
>
> > I disagree, Peter.
>

>
> I am afraid that I will have to agree with Peter.

Does it really hurt that much, Richard <G>?

It isn't who's right... it's what's right.

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-20T13:18:51+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbc0a3b_7@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message news:20031119133040.679$F9@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
…[10 more quoted lines elided]…
> have ever seen, in all respects.

Yes, I have no quibble with your code.

So where's the disagreement <G>?

The code you posted checks for control breaks from the highest level down, but you action them from the highest level down also. This can require redundant checks (like for EOF, and control breaks within control break levels).

> 
> The code below is for a three level control break, plus a final end of
…[5 more quoted lines elided]…
> coding style; it's the logic I'm trying to illustrate. :-)

Agreed totally. (BTW, I NEVER quibble about style...<G>)

My brain is not oatmeal (I'm off the JD and on a diet at the moment so, although grumpy, my head is clear <G>) and I am enjoying the Spring sunshine, about to go off for a swim in the local mineral pools.

I don't think you disagree as strongly as you may think, Judson. The fundamentals are the same, it is just interpretation and style.

I like the CONTROL logic in a program to be very clear because that is the "coat hanger" for future maintenance.

I don't like posting code to CLC (especially straightforward batch code, which is really pretty trivial) but as both you and Howard seem to have a problem with the statement I made regarding control breaks (and I respect you both enough to try and elucidate), I quickly amended your code into my style. I hope you will grant me the same latitude I granted you <G>

The following does not purport to be definitive. It is intended to show a simple GENERAL control structure for handling reporting in COBOL, based on the tenet: "Check control breaks from the top down; action them from the bottom up."

Changes I have made to Judson's original are not implied criticism, rather just me feeling "comfortable" with my own style.

While I have not investigated this area of Data Processing as thoroughly as Judson apparently has, I have always found the following to be adequate to my needs.

      01  CONTROL-BREAK-AREA.
            03  CBA-CURRENT.
                05  CBA-CURR-LEVEL-1.
                    07  CBA-CURR-LEVEL-2.
                        09  CBA-CURR-LEVEL-3.
                            11  CBA-CURR-LEV-3-FIELD  PIC  ?(??).
                        09  CBA-CURR-LEV-2-FIELD      PIC  ?(??).
                    07  CBA-CURR-LEV-1-FIELD          PIC  ?(??).
            03  CBA-PREVIOUS.
                05  CBA-PREV-LEVEL-1.
                    07  CBA-PREV-LEVEL-2.
                        09  CBA-PREV-LEVEL-3.
                            11  CBA-PREV-LEV-3-FIELD  PIC  ?(??).
                        09  CBA-PREV-LEV-2-FIELD      PIC  ?(??).
                    07  CBA-PREV-LEV-1-FIELD          PIC  ?(??).
 
 
       produce-report.
           OPEN INPUT WORK-FILE output printfile
           perform get-input
           MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD
           MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD
           MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD
      *     <Depending on Application, may need initial headings for each
      *      control level to be printed here>
           PERFORM 
              UNTIL finished
                 MOVE CBA-CURRENT TO CBA-PREVIOUS
                 MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD
                 MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD
                 MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD
                 IF CBA-CURRENT NOT = CBA-PREVIOUS
                    if cba-current < cba-previous
      *                   <notify sequence error on input file and abort>
                    end-if
                    if cba-curr-level-1  = cba-prev-level-1
                       if cba-curr-level-2 = cba-prev-level-2
      * do level 3 break...
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print new level 3 heading>

                       else
      * do level 2 break...
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Print new level 2 and 3 headings>
                       end-if
                    else
      * do level 1 break...
           
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Roll level 1 totals to Grand Totals>
      *                         <Print new headings for all levels>
                    end-if
                 else
                    <process the current record>
                 end-if
                 perform get-input
           end-perform
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Roll level 1 totals to Grand Totals>
      *                         <print Grand Totals>
           close work-file
                 printfile
           stop run
           .
       get-input.
           read work-file
                at end 
                   set finished to TRUE
           end-read
           .

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-20T14:23:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbc1865_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com>`

```
OOPS!

(This is why I hate posting code here...especially when it hasn't been
compiled and tested...)

Something in the back of my head kept telling me to look again... at last it
drowned out the part that was saying: "It's a beautiful day, let's go
swimming..."

There were some glaring (when I took the trouble to look) logic errors in
the code I posted and it is amended as follows:

      01  CONTROL-BREAK-AREA.
            03  CBA-CURRENT.
                05  CBA-CURR-LEVEL-1.
                    07  CBA-CURR-LEVEL-2.
                        09  CBA-CURR-LEVEL-3.
                            11  CBA-CURR-LEV-3-FIELD  PIC  ?(??).
                        09  CBA-CURR-LEV-2-FIELD      PIC  ?(??).
                    07  CBA-CURR-LEV-1-FIELD          PIC  ?(??).
            03  CBA-PREVIOUS.
                05  CBA-PREV-LEVEL-1.
                    07  CBA-PREV-LEVEL-2.
                        09  CBA-PREV-LEVEL-3.
                            11  CBA-PREV-LEV-3-FIELD  PIC  ?(??).
                        09  CBA-PREV-LEV-2-FIELD      PIC  ?(??).
                    07  CBA-PREV-LEV-1-FIELD          PIC  ?(??).


       produce-report.
           OPEN INPUT WORK-FILE output printfile
           perform get-input
           MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD
           MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD
           MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD
      *     <Depending on Application, may need initial headings for each
      *      control level to be printed here>
           PERFORM
              UNTIL finished
                 MOVE CBA-CURRENT TO CBA-PREVIOUS
                 MOVE WORK-LEV-3-FIELD  TO CBA-CURR-LEV-3-FIELD
                 MOVE WORK-LEV-2-FIELD  TO CBA-CURR-LEV-2-FIELD
                 MOVE WORK-LEV-1-FIELD  TO CBA-CURR-LEV-1-FIELD
                 IF CBA-CURRENT NOT = CBA-PREVIOUS
                    if cba-current < cba-previous
      *                   <notify sequence error on input file and abort>
                    end-if
                    if cba-curr-level-1  = cba-prev-level-1
                       if cba-curr-level-2 = cba-prev-level-2
      * do level 3 break...
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print new level 3 heading>

                       else
      * do level 2 break...
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Print new level 2 and 3 headings>
                       end-if
                    else
      * do level 1 break...

      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Print level 1 totals>
      *                         <Roll level 1 totals to Grand Totals>
      *                         <Print new headings for all levels>
                    end-if
                 end-if
                 <process the current record>
                 perform get-input
           end-perform
      *                         <Print level 3 totals>
      *                         <Roll level 3 totals to level 2>
      *                         <Print level 2 totals>
      *                         <Roll level 2 totals to level 1>
      *                         <Print level 1 totals>
      *                         <Roll level 1 totals to Grand Totals>
      *                         <print Grand Totals>
           close work-file
                 printfile
           stop run
           .
       get-input.
           read work-file
                at end
                   set finished to TRUE
           end-read
           .

I'm not claiming this is perfect, but I'm not looking at it again either...

At least it now processes records whether or not there was a control break
<G>.

<Presses SEND, picks up towel and car keys, departs...>

Pete.
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 6)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2003-11-21T03:35:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FBD8710.7090408@optonline.net>`
- **In-Reply-To:** `<3fbc1865_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com> <3fbc1865_9@news.athenanews.com>`

```
Well, Peter, I knew what you ment all along. This exercise is
almost a class exercise from 1954.

Warren (minus the language growth features)

Peter E.C. Dashwood wrote:
> OOPS!
> 
…[102 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-22T00:43:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbdfa9d_7@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com> <3fbc1865_9@news.athenanews.com> <3FBD8710.7090408@optonline.net>`

```
Hi Warren,

nice to see you are still reading and posting.

1954 eh?

I guess you are telling me that these techniques had already been worked out
and absorbed into "standard practice" by then, at least in the USA.

When I came along 11 years later, nobody I met knew about this. We all did
kind of what Judson described...used trial and error and evaluated each
attempt, hoping to make the next one better.

The old programmer who put me on to the idea of checking control breaks from
the top down, processing from the bottom up, was a Canadian who had been
working with computers since the 1940s (initially he used to fly around
North America replacing mercury vapour tubes or something equally
esoteric...). He came out to New Zealand with his wife to retire and get a
concrete boat (which NZ pioneered the construction of). Sadly, he died
before it was completed, but I believe his wife later sailed it back to
Canada, with a delivery crew of Kiwis. This same man clued us in to the
ideas of random access and hashing algorithms and was the first man I ever
met to develop what could truly be called a "database", residing on a
Burroughs drum system. (Removablel disks were still largely in the
laboratory and didn't become widely available in New Zealand until the early
1970s).

I am staggered to hear you actually had classrooms teaching this stuff in
the mid-fifties. It just shows how far we were behind the play.

The first programming "course" I ever did was for the NCR 500 (programmed in
machine language, although they later produced an assembler called "SLIP")
and the course was: "Here's a bunch of audio tapes, Dashwood. Listen to them
in your own time. We want an invoicing program next week...". When I asked
why I couldn't attend the actual course at NCR I was informed that there was
no money available for such flim flam and if I wanted a career in computing
I better get stuck in and do the tapes...

I wonder how many people reading this recognise: "Hi... My name is Bob. I am
your instructor on the NCR 500 programming course. Now listen
carefully...."<G>

Of course we caught up eventually. By the early 70s New Zealand was the
first country to have on-line banking with IBM 7770 voice response units.
You could dial the bank and listen to the voice of a well known Radio/TV
personality tell you your balance. (We thought it was super cool...<G>). We
also had a National system for betting on horses (TAB), powered by some
already obsolete Control Data Corporation mainframes which cost $18,000,000
(a staggering sum in those days), and allowed bets to be placed up to 10
minutes before the start, for any meeting anywhere in the country, from any
TAB anywhere in the country. (I was incidentally involved in that, working
as a senior analyst for CDC at that time, and later as a pre-sales support
analyst to the top CDC Australasian Salesman.)

I'd very much like to hear of your first ventures into programing, Warren.
Care to share it with us?

Pete.


"Warren Simmons" <wsimmons5@optonline.net> wrote in message
news:3FBD8710.7090408@optonline.net...
> Well, Peter, I knew what you ment all along. This exercise is
> almost a class exercise from 1954.
…[9 more quoted lines elided]…
> > Something in the back of my head kept telling me to look again... at
last it
> > drowned out the part that was saying: "It's a beautiful day, let's go
> > swimming..."
> >
> > There were some glaring (when I took the trouble to look) logic errors
in
> > the code I posted and it is amended as follows:
> >
…[23 more quoted lines elided]…
> >       *     <Depending on Application, may need initial headings for
each
> >       *      control level to be printed here>
> >            PERFORM
…[7 more quoted lines elided]…
> >       *                   <notify sequence error on input file and
abort>
> >                     end-if
> >                     if cba-curr-level-1  = cba-prev-level-1
…[47 more quoted lines elided]…
> > I'm not claiming this is perfect, but I'm not looking at it again
either...
> >
> > At least it now processes records whether or not there was a control
break
> > <G>.
> >
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 8)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2003-11-22T22:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OtRvb.10347$Hb.2933638@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<3fbdfa9d_7@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com> <3fbc1865_9@news.athenanews.com> <3FBD8710.7090408@optonline.net> <3fbdfa9d_7@news.athenanews.com>`

```
Very interesting.


And yes, our first programming in C10 on the UI presented us
with the problem as our input was card to tape, sort (which could
take for ever then), and then process. The nature of most of the
files included the need for "breaks" or subtotals. And of course
grand totals. As you said bottom up.

When I first gave COBOL classes prior to books and courses I used
a simple three way merge program as one of my class problems (taken
from experience) to impress upon the newbees that when the cards
were put onto tape, procedural steps must be taken. Hi values was
one. Pre-sorting was another. Learning how to merge was a large part.
Also, it was necessary to stress that given a match the  output shoule
be make in a given order to reflect the correct results. The merge could
have been the last pass on a sort. I may have "class notes on the 
subject yet, if I could find them <G>.

Warren

Peter E.C. Dashwood wrote:
> Hi Warren,
> 
…[192 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 6)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2003-11-21T04:04:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FBD8766.2030201@optonline.net>`
- **In-Reply-To:** `<3fbc1865_9@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com> <3fbc1865_9@news.athenanews.com>`

```
Well, Peter, I knew what you ment all along. This exercise is
almost a class exercise from 1954.

Warren (minus the language growth features)

Peter E.C. Dashwood wrote:
> OOPS!
> 
…[102 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-11-21T06:43:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031121074401.030$9v@news.newsreader.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[20 more quoted lines elided]…
> control break levels).

You are absolutely right, Peter, my apologies. I told you my brain has
turned to oatmeal. Maybe I should stop posting until I'm well. :-)
```

###### ↳ ↳ ↳ Re: match program example

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-22T16:56:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fbede88_4@news.athenanews.com>`
- **References:** `<v8tirv0okog6mm37htpsqaq0vmlbmfgvoc@4ax.com> <8a2d426e.0311180112.57823b99@posting.google.com> <3fbab0d8_8@news.athenanews.com> <20031119133040.679$F9@news.newsreader.com> <3fbc0a3b_7@news.athenanews.com> <20031121074401.030$9v@news.newsreader.com>`

```
Judson,

It is my turn to apologise.

I mixed up my responses and thought you hadn't responded to this. But you
have, and I am very sorry I gave you a hard time in the response above.

If the end result is that all concerned are better informed on 3 way splits
and control breaks, then no harm has been done.

It is good to see you posting here again.

Regards,

Pete.


"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:20031121074401.030$9v@news.newsreader.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > > "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> > > >
> > > > "Check control breaks from the highest to the lowest (top down);
action
> > > > control breaks from the lowest to the highest (bottom up)"
> > >
> > > I disagree, Peter. Many years ago I spent over two years doing mostly
> > > writing report programs. During that time I wrote several hundred
report
> > > programs, and I took the opportunity to experiment and study every
> > > control break method I could think of and every method anyone else
> > > would suggest. I looked at number of lines of code, clarity,
flexibility,
> > > etc. My conclusion was that the method illustrated in the sample code
> > > below is at least as good as, usually better than, any other method I
…[19 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
