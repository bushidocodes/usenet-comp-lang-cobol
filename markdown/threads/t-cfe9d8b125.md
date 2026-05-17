[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The best programming advice I ever got.

_21 messages · 10 participants · 2012-08_

---

### The best programming advice I ever got.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-08-13T23:29:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8s6p6F22fU1@mid.individual.net>`

```
http://www.informit.com/articles/article.aspx?p=1926692

I came across the above in the course of my normal routine and was blown 
away by it.

Not just the article but also the comments.

I could add a few stories in the same vein but I'm sure that most regulars 
here could too.

Why is computer programming so political?

I got fired once for embarrassing my Boss by helping some people he had 
refused to help. (They worked in the same company and I was unaware of his 
refusal to help them or the fact that he had his own agenda...)

As my horizons broadened and I travelled the World I found that this 
nonsense is not just limited to the Antipodes.

Staying the Hell out of other peoples' code is not something I have ever 
done. But the motivation is not to hurt or embarrass, it is just to get a 
better result. (And, sometimes, to improve my own code by learning from 
others...)

During the last few weeks I've had some people thousands of miles from where 
I'm at, and who I have never met, taking code I wrote apart and bashing it 
with steam hammers (Around 100 specific test plans of their own devising, 
across 4 machines). I am not defensive of it and I was very interested to 
see if it would fall over or not. (It mostly didn't, but they found a couple 
of things that I was surprised by and am currently fixing.)

After completing their evaluation they were very positive and have bought 
the product. (I wish ALL our prospects were as thorough... their tests 
showed up some limits in Microsoft software as well as mine, and it has 
meant some design rethinking. Prior to this no-one had encountered these 
limits, including me...)

The point I'm getting to is that, when it comes to computer programming, it 
isn't about WHO's right, it is about WHAT's right. Leave your ego at the 
door.

It's just plain silly to get "precious" about code you wrote.

If someone can see a way to improve what you wrote, accept it graciously and 
learn from it.

One of the commenters noted that if code is not "owned" by an individual, 
much of the "charge" surrounding it gets dissipated. I think I agree with 
that. I've always circulated team members (including myself, if I have been 
working as a team programmer) around various programs,  for two reasons:

1. Skills transfer is important and it is not a good idea to have only one 
person who understands certain areas of code.
2. The general level of knowledge of the team is raised if they work on 
different applications.

I also like Agile style approaches for the same reasons: If end-users, 
analysts, and programmers are all involved in design workshops (Joint 
Application Design (JAD)) the end result has more "buy-in" by more people, 
and is much more likely to be useful to the Company, than is the case where 
IT develops using Waterfall in an ivory tower.

Don't stay the Hell out of other people's code: see it for what it is: 
instructions to a machine. If it can be made better, go for it.

But don't rub the writer's nose in it if you find there were obvious 
flaws...

A bad winner is just as irritating as a bad loser... :-)

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: The best programming advice I ever got.

- **From:** dansabrservices@yahoo.com
- **Date:** 2012-08-13T04:49:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66170215-f45f-49ed-bf8c-a430bee4606d@googlegroups.com>`
- **In-Reply-To:** `<a8s6p6F22fU1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net>`

```
On Monday, August 13, 2012 7:29:39 AM UTC-4, Pete Dashwood wrote:
> http://www.informit.com/articles/article.aspx?p=1926692 I came across the above in the course of my normal routine and was blown away by it. Not just the article but also the comments. I could add a few stories in the same vein but I'm sure that most regulars here could too. Why is computer programming so political? I got fired once for embarrassing my Boss by helping some people he had refused to help. (They worked in the same company and I was unaware of his refusal to help them or the fact that he had his own agenda...) As my horizons broadened and I travelled the World I found that this nonsense is not just limited to the Antipodes. Staying the Hell out of other peoples' code is not something I have ever done. But the motivation is not to hurt or embarrass, it is just to get a better result. (And, sometimes, to improve my own code by learning from others...) During the last few weeks I've had some people thousands of miles from where I'm at, and who I have never met, taking code I wrote apart and bashing it with steam hammers (Around 100 specific test plans of their own devising, across 4 machines). I am not defensive of it and I was very interested to see if it would fall over or not. (It mostly didn't, but they found a couple of things that I was surprised by and am currently fixing.) After completing their evaluation they were very positive and have bought the product. (I wish ALL our prospects were as thorough... their tests showed up some limits in Microsoft software as well as mine, and it has meant some design rethinking. Prior to this no-one had encountered these limits, including me...) The point I'm getting to is that, when it comes to computer programming, it isn't about WHO's right, it is about WHAT's right. Leave your ego at the door. It's just plain silly to get "precious" about code you wrote. If someone can see a way to improve what you wrote, accept it graciously and learn from it. One of the commenters noted that if code is not "owned" by an individual, much of the "charge" surrounding it gets dissipated. I think I agree with that. I've always circulated team members (including myself, if I have been working as a team programmer) around various programs, for two reasons: 1. Skills transfer is important and it is not a good idea to have only one person who understands certain areas of code. 2. The general level of knowledge of the team is raised if they work on different applications. I also like Agile style approaches for the same reasons: If end-users, analysts, and programmers are all involved in design workshops (Joint Application Design (JAD)) the end result has more "buy-in" by more people, and is much more likely to be useful to the Company, than is the case where IT develops using Waterfall in an ivory tower. Don't stay the Hell out of other people's code: see it for what it is: instructions to a machine. If it can be made better, go for it. But don't rub the writer's nose in it if you find there were obvious flaws... A bad winner is just as irritating as a bad loser... :-) Pete. -- "I used to write COBOL...now I can do anything."

Excellent article.  Please note that this applies not only to new code development, but also to the software maintenance field.  Without getting into too many details, I recently resolved a software problem that had existed for over 3 years (prior to my employment at the client site).  There were processes in place to detect the problem and to force a reset to "resolve" it.  The problem turned out to be a setup problem for a system call that only showed up once the normal proces context was lost.  In other words, standard debugging techniques (print statements etc.) would not work.  Many previous support folks attempted to resolve this without success.  Since I had background at the OS support level, I was able to see and resolve this.  I am not and was not "better" than the others, just experienced in another area.

As alluded to in the article, anyone can be a contributor depending opon his/her experience.  I too always look forward to a discussion about code improvements.  No matter how long wehave been in the business, there is always something to learn.

Dan
```

#### ↳ Re: The best programming advice I ever got.

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-08-13T08:48:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Staying the Hell out of other peoples' code is not something I have
> ever done. But the motivation is not to hurt or embarrass, it is just
> to get a better result. (And, sometimes, to improve my own code by
> learning from others...)

Ah, but how is the "better result" received? (see below)

>
> The point I'm getting to is that, when it comes to computer
…[7 more quoted lines elided]…
>

In my view, programmers are much like dentists! They are both scientifically 
trained, use modern tools, and are rational, logical thinkers.

But they are both artists.

Every stereotypical notion you have about some beatnik living in a garret in 
Greenwich Village holds, to a greater or lesser degree, for programmers (and 
dentists). I've seen code that didn't work, never did work, and couldn't be 
made to work, held up as a shining exemplar and the author gets defensive to 
the point of violence at any criticism.

My granny used to say: "Every momma crow thinks her baby is the blackest." 
(She also often exclaimed "My cow in a rowboat!").

Pride is a very powerful emotion. Use caution when pointing out another's 
flaws.
```

##### ↳ ↳ Re: The best programming advice I ever got.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2012-08-13T10:54:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com>`

```
On Mon, 13 Aug 2012 08:48:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>In my view, programmers are much like dentists! They are both scientifically 
>trained, use modern tools, and are rational, logical thinkers.
>
>But they are both artists.

I don't want an artist working on my teeth, and I don't want an artist
writing my inventory program.

-- 
"In no part of the constitution is more wisdom to be found,
than in the clause which confides the question of war or peace 
to the legislature, and not to the executive department." 

- James Madison
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

- **From:** docdwarf@panix.com ()
- **Date:** 2012-08-13T22:50:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k0c0ba$25i$2@reader1.panix.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com> <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com>`

```
In article <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 13 Aug 2012 08:48:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
>wrote:
…[7 more quoted lines elided]…
>writing my inventory program.

It might be of interest to consider the name of Sun T'zu's work ('The Art 
of War'), Donald Knuth's work ('The Art of Programming') and the 
Latinisation of Hippocrates' observation that 'Art is long, life is 
short')... among other things.

DD
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-08-14T10:39:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tcok289b8l3ph9r71k5hj1sucppegenpap@4ax.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com> <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com> <k0c0ba$25i$2@reader1.panix.com>`

```
On Mon, 13 Aug 2012 22:50:18 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com>,
>Howard Brazee  <howard@brazee.net> wrote:
…[16 more quoted lines elided]…
>DD

Art is long....doesn't apply to programming.  We still have DaVinci
paintings hanging on museum walls.  The famous Mona Lisa was painted
sometime between 1503 and 1506 which makes it between 509 and 512
years old.  A computer program would be lucky if it lasts 5 years much
less 500.

Regards,
-- 

          ////
         (o o)
-oOO--(_)--OOo-
  
"Doctor: A person who kills your ills by pills, and kills you by bills."
-- Unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-08-14T18:52:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ueKdncaPIImiebfNnZ2dnUVZ_uGdnZ2d@earthlink.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com> <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com> <k0c0ba$25i$2@reader1.panix.com> <tcok289b8l3ph9r71k5hj1sucppegenpap@4ax.com>`

```
SkippyPB wrote:
> >
> Art is long....doesn't apply to programming.  We still have DaVinci
…[4 more quoted lines elided]…
>

There are COBOL programs going on sixty years old. Check back in a couple 
hundred years and see if they're still running.
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-08-14T18:53:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rLidnRYm7dELebfNnZ2dnUVZ_sGdnZ2d@earthlink.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com> <89ci2853m8p7uu624sgbmcfnlmfpfafmjs@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 13 Aug 2012 08:48:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[8 more quoted lines elided]…
> writing my inventory program.

Find, then, a dentist who doesn't take pride in his work.

You'll end up with a mouth of Lego-looking choppers.
```

##### ↳ ↳ Re: The best programming advice I ever got.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-08-14T12:26:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8tk94Flh6U1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <DKmdnfJfE8g3mLTNnZ2dnUVZ_vCdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[30 more quoted lines elided]…
> blackest." (She also often exclaimed "My cow in a rowboat!").

:-) LOVE it!

Figures of speech are amazing... Texas and Australia are both rich sources 
and I have spent hours just listening to people from both these cultures :-)

My dentist is an artist, but he is really quite exceptional. Did his basic 
Dental degree at Otago University in the South Island (a seat of Dental 
excellence) then took a PhD from London where he worked on the study of 
tooth regeneration using stem cells. He does facial reconstruction of 
accident victims and is one of  only two (non-British) people ever to have 
been recognised by the Edinburgh Medical Society for his work with implant 
technology. (When he was in Europe he taught Dentists from many countries 
about getting this right.) By an amazing coincidence he ended up in 
Tauranga, so I consider myself lucky to have access to him. In the 
twenty-odd years he has been my dentist (in both Europe and NZ) he has never 
hurt me (or anyone else, as far as I know), so there maybe is a case for 
"artistry" (at least insofar as it being a combination of skill, 
professionalism, creativity, intelligence, and capability) in Dentistry. 
And probably also in computer programming...

>
> Pride is a very powerful emotion. Use caution when pointing out
> another's flaws.

I see criticism much the way I see blame.

They are both useless for fixing things and they just demotivate people.

(I operate on what I perceive to be Axiomatic: No one actually sets out to 
screw things up on purpose.)

If you can learn something by examining the facts around a disaster, that's 
fine. If you can show somebody a better way without being personal about it, 
that's fine too. ("THE code" not "YOUR code"... :-))

But investigating in order to move responsiblity or assign blame is just 
pointless as far as I'm concerned.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: The best programming advice I ever got.

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2012-08-14T00:01:09+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0qi2897k8kt3nq5jlp2htd0nia9ms7pm6@4ax.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net>`

```
On Mon, 13 Aug 2012 23:29:39 +1200 "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

:>http://www.informit.com/articles/article.aspx?p=1926692

:>I came across the above in the course of my normal routine and was blown 
:>away by it.

:>Not just the article but also the comments.

:>I could add a few stories in the same vein but I'm sure that most regulars 
:>here could too.

:>Why is computer programming so political?

I don't know that, but I made a similar mistake when I started out.

I was working in a TSO support department, and automated/fixed things so that
I had little work and could spend my time pretty much as I wished. I allowed
users to perform their own UADS updates so that I did not have to do it. Added
validation of parameters so that then end user got messages like undefined
account and unknown/unauthorized PROC - no more "LOGON FAILED" which meant
that I would get a call. Put in SMP so that operating system changes that
affected my area would cause me to be automatically notified. This was very
early 1980's.

Unfortunately, I still had work coming in from problems in other departments -
where I had to point out that the source of the error was somewhere else. So I
decided that I would fix up those things as well to eliminate more of my work.
I figured, we all work for the same company, so this is best. Unfortunately
that stepped on some high up toes so that my ranking, when merged with other
departments, was pushed down. Thus my raises and bonuses were affected.

All was good in the long run, as I moved into the vendor area.

--
Binyamin Dissen <bdissen@dissensoftware.com>
http://www.dissensoftware.com

Director, Dissen Software, Bar & Grill - Israel


Should you use the mailblocks package and expect a response from me,
you should preauthorize the dissensoftware.com domain.

I very rarely bother responding to challenge/response systems,
especially those from irresponsible companies.
```

##### ↳ ↳ Re: The best programming advice I ever got.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-08-14T11:47:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8ti1bF6m3U1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <f0qi2897k8kt3nq5jlp2htd0nia9ms7pm6@4ax.com>`

```
Binyamin Dissen wrote:
> On Mon, 13 Aug 2012 23:29:39 +1200 "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[33 more quoted lines elided]…
> All was good in the long run, as I moved into the vendor area.

I like the fact that you have always wanted to make your job easier, 
Binyamin.

That leads on to helping others make their job easier (as you did) and in 
the end everybody wins...

I think that if management can't recognise this then it is necessary for 
talented people to  "do their own thing".

I worked with a manager once who complained to me that "smart people are 
lazy" (I had written a program to do a job that was supposed to take me 3 
months of tedious manual program maintenance. It took me three days to write 
and debug, ran for about a minute and the job was done.

I resented the "lazy" slur (I'm not...).

(The Kiwi culture I was raised in evolved out of solid Victorian work ethic; 
(men and women carving a nation from wilderness - a lot like the American 
old West) and we are taught from an early age that "the world does not owe 
you a living...".)

My response to said Manager was: "If it would make you feel better I can 
bill you for the three months... then I'll go and lie in the sun for a 
while."  He never called me lazy again.

Pete.
```

#### ↳ Re: The best programming advice I ever got.

- **From:** docdwarf@panix.com ()
- **Date:** 2012-08-13T22:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k0c02f$25i$1@reader1.panix.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net>`

```
In article <a8s6p6F22fU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>http://www.informit.com/articles/article.aspx?p=1926692

[snip]

>Why is computer programming so political?

Computer programming, Mr Dashwood, is - last I looked - a human activity 
and as far back as Aristotle it was noted that 'Man is by nature a 
political animal'.

(a bit of research might reveal that the root of 'political' is 'polis', 
Ancient Greek for 'city' and a bit more research might result in a 
doctoral thesis)

DD
```

##### ↳ ↳ Re: The best programming advice I ever got.

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-08-14T12:01:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8tiqvFbp9U1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <a8s6p6F22fU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> DD

Never had much time for all that there book larnin'... Gran'pappy allus 
sayed that "Books don' put grits on the table".

He was wrong. We used several books under different legs of our table to 
keep it even and without them, the grits woulder fallen' off...

Anyways, I'se jus' doin' the best I can an' I don't need no books to tell me 
I ain't goin' nowhere.

Politickin' is best left to them brayin' jackasses what has the book 
larnin'.

Yer don' need a weathervane to know which way the wind blows...

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-08-14T10:41:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fqok28dv5bcldbl4mp7bkghil875nmnoqs@4ax.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com> <a8tiqvFbp9U1@mid.individual.net>`

```
On Tue, 14 Aug 2012 12:01:32 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>docdwarf@panix.com wrote:
>> In article <a8s6p6F22fU1@mid.individual.net>,
…[19 more quoted lines elided]…
>

Well if you write a few, and they are successful, you might put lots
of grits on your table!


>He was wrong. We used several books under different legs of our table to 
>keep it even and without them, the grits woulder fallen' off...
…[9 more quoted lines elided]…
>Pete.

Regards,
-- 

          ////
         (o o)
-oOO--(_)--OOo-
  
"Doctor: A person who kills your ills by pills, and kills you by bills."
-- Unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

- **From:** docdwarf@panix.com ()
- **Date:** 2012-08-15T01:50:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k0ev9i$hpk$1@reader1.panix.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com> <a8tiqvFbp9U1@mid.individual.net>`

```
In article <a8tiqvFbp9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <a8s6p6F22fU1@mid.individual.net>,
…[16 more quoted lines elided]…
>sayed that "Books don' put grits on the table".

Gran'pappy can't be argued with... but those who have read what George 
Santayana said about remembering the past are condemned to repeat it.

DD
```

##### ↳ ↳ Re: The best programming advice I ever got.

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2012-08-14T02:01:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a8tprbFnhfU1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com>`

```
In article <k0c02f$25i$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <a8s6p6F22fU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> doctoral thesis)

I always heard the derivation was "poli" meaning "many" and "tics"
meaning "blood sucking parasites".

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

- **From:** docdwarf@panix.com ()
- **Date:** 2012-08-15T01:52:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k0evc5$hpk$2@reader1.panix.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com> <a8tprbFnhfU1@mid.individual.net>`

```
In article <a8tprbFnhfU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <k0c02f$25i$1@reader1.panix.com>,
>	docdwarf@panix.com () writes:
…[17 more quoted lines elided]…
>meaning "blood sucking parasites".

Ummmmm... 'many' is 'polu'; see what kind of mess results from an 
unexpected vowel movement?

DD
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2012-08-15T11:41:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a91g86F15jU1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com> <a8tprbFnhfU1@mid.individual.net> <k0evc5$hpk$2@reader1.panix.com>`

```
In article <k0evc5$hpk$2@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <a8tprbFnhfU1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[22 more quoted lines elided]…
> unexpected vowel movement?

Yes, but my derivation is much closer to reality.

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-08-15T10:48:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e9fbe20-0369-4f04-90f2-74975b73acf3@googlegroups.com>`
- **In-Reply-To:** `<a91g86F15jU1@mid.individual.net>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <k0c02f$25i$1@reader1.panix.com> <a8tprbFnhfU1@mid.individual.net> <k0evc5$hpk$2@reader1.panix.com> <a91g86F15jU1@mid.individual.net>`

```
Don't 

On Wednesday, August 15, 2012 12:41:58 PM UTC+1, Bill Gunshannon wrote:
> In article <k0evc5$hpk$2@reader1.panix.com>, docdwarf@panix.com () writes: > In article <a8tprbFnhfU1@mid.individual.net>, > Bill Gunshannon <billg999@cs.uofs.edu> wrote: >>In article <k0c02f$25i$1@reader1.panix.com>, >> docdwarf@panix.com () writes: >>> In article <a8s6p6F22fU1@mid.individual.net>, >>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote: >>>>http://www.informit.com/articles/article.aspx?p=1926692 >>> >>> [snip] >>> >>>>Why is computer programming so political? >>> >>> Computer programming, Mr Dashwood, is - last I looked - a human activity >>> and as far back as Aristotle it was noted that 'Man is by nature a >>> political animal'. >>> >>> (a bit of research might reveal that the root of 'political' is 'polis', >>> Ancient Greek for 'city' and a bit more research might result in a >>> doctoral thesis) >> >>I always heard the derivation was "poli" meaning "many" and "tics" >>meaning "blood sucking parasites". > > Ummmmm... 'many' is 'polu'; see what kind of mess results from an > unexpected vowel movement? Yes, but my derivation is much closer to reality. 

Don't you mean that your version is closer to your version of reality (whatever that is)?
```

###### ↳ ↳ ↳ Re: The best programming advice I ever got.

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2012-08-16T01:14:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k0hhhc$8m2$1@reader1.panix.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net> <a8tprbFnhfU1@mid.individual.net> <k0evc5$hpk$2@reader1.panix.com> <a91g86F15jU1@mid.individual.net>`

```
In article <a91g86F15jU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <k0evc5$hpk$2@reader1.panix.com>,
>	docdwarf@panix.com () writes:
…[26 more quoted lines elided]…
>Yes, but my derivation is much closer to reality.

I'll take your word on that, Mr Gunshannon; this 'reality' stuff I've 
never claimed to be able to speak much about.

DD
```

#### ↳ Re: The best programming advice I ever got.

- **From:** Louis Krupp <lkrupp@nospam.pssw.com.invalid>
- **Date:** 2012-08-14T21:57:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4o6m28194itcag7m2qpomr2851882os5pv@4ax.com>`
- **References:** `<a8s6p6F22fU1@mid.individual.net>`

```
On Mon, 13 Aug 2012 23:29:39 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>http://www.informit.com/articles/article.aspx?p=1926692
>
…[66 more quoted lines elided]…
>A bad winner is just as irritating as a bad loser... :-)

There are times when it's best to fix it quietly.  If you have to tell
someone, tell the author, or whoever "owns" the code.  Let them take
credit for the improvement if they want to.  Be their ally, not their
enemy.

Be creative.  If having two processes and a socket is important to
someone, find another use for two processes and a socket.  Does the
application need some sort of log?  Wonderful!  Put messages in a
queue and let the second process write the log whenever it gets around
to it.

Anyone read The Psychology of Computer Programming?  I vaguely
remember it talking about situations like this.

Louis
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
