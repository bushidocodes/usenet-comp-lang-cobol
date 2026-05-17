[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Software Security

_3 messages · 2 participants · 2012-08_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Software Security

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2012-08-14T17:55:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BZCdnX-Z-tLPVLfNnZ2dnUVZ_ridnZ2d@earthlink.com>`

```
I thought some of you might be interest in this.  Note SAFECode stands for 
Software Assurance Forum foe Excellence in Code and is a vendor consortium.

Practical Security Stories and Security Tasks for Agile Development 
Environments:

     http://www.safecode.org/publications/SAFECode_Agile_Dev_Security0712.pdf


Fundamental Practices for Secure Software Development:

    http://www.safecode.org/publications/SAFECode_Dev_Practices0211.pdf
```

#### ↳ Re: Software Security

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-08-24T03:13:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9mvljFp1lU1@mid.individual.net>`
- **References:** `<BZCdnX-Z-tLPVLfNnZ2dnUVZ_ridnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> I thought some of you might be interest in this.  Note SAFECode
> stands for Software Assurance Forum foe Excellence in Code and is a
…[10 more quoted lines elided]…
>    http://www.safecode.org/publications/SAFECode_Dev_Practices0211.pdf

This is a topic that has to be of interest to most software developers who 
are planning or hoping to sell their product to others.

I didn't have time to read it until just now.

I have been a fan of Agile style development since the early 1990s (before 
it was officially "Agile"...) when I first used time-boxed, iterative, 
interactive development for a pilot project in a major UK corporation. I was 
amazed at how much better it was than the Waterfall (so was everybody 
else...) and I have used this approach for all software development projects 
since. (It is especially good if Object Oriented development is being used, 
and, for me, that is always the case.)

The article is all very good but it seems over the top to me.

I think quite a few of the stories could be eliminated or left to standard 
software infrastructure. But different people have different degrees of 
paranoia... :-)

I'd prefer to see developers focussing on application stories and delivering 
functionality, rather than worrying about how many connections they are 
going to support, or what the maximum data transfer is going to be.

These things vary in the real world and if they prove too constraining in 
actuality, there are measures you can take that have absolutely nothing to 
do with software development.

It's interesting because I have developed systems that are public and run on 
my own web server. Every so often, someone tries to attack them.  (It isn't 
always malicious; I had one case where a student in Israel was just trying 
to see how a web service worked. So he bombarded it with around 2000 
transactions a second... :-) It didn't fall over, but the alarming growth of 
the log file got my attention... I made some changes and have had no trouble 
since. Just yesterday I found some attempted SQL injection attacks on 
another web service, which really made me smile. It's pretty obvious that 
these are by script kiddies who don't really know what they're doing. Once 
the perpetrators realize they are never going to work, they tend to go away. 
(It was interesting that they come from all over the world...)

I guess it comes down to balance and interest. I don't believe that ANY 
public system can be impenetrable, even if you applied every one of the 
stories noted... but you have to take a balance and decide what you can live 
with.

There are a few basic things that can help:

1. Use server side code wherever possible. (I really like ASP.NET because I 
can write C# code-behinds that run on the server and are not subject to easy 
modification like Javascript can be on an infected client.)

2. Keep things as simple as possible. (Complexity is much more difficult to 
fix if someone does manage to break it...)

Use existing server infrastructure. Use components. Develop security code 
and reuse it across different systems.

I think secure deployment is actually more important than secure 
development. It's pretty heart-breaking to see the work of years being 
ripped off because it wasn't properly protected after deployment.

I spent some time last year looking at this, and all PRIMA software is now 
protected by a system that prevents any unauthorised user from running it. 
It doesn't utilize authorization or security codes, so there is nothing that 
can be obtained from a crack site. Also, you can deploy to a virtual machine 
without problem, but it will only run on that host, so there's no point in 
putting it on a memory stick and trying it on a different host... So far it 
hasn't failed and I'll probably release it as a product package to other 
software houses/developers once it has a decent track record in live 
deployment.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Software Security

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2012-08-23T12:26:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3rOdnc3IYb4BxKvNnZ2dnUVZ_rqdnZ2d@earthlink.com>`
- **References:** `<BZCdnX-Z-tLPVLfNnZ2dnUVZ_ridnZ2d@earthlink.com> <a9mvljFp1lU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:a9mvljFp1lU1@mid.individual.net...
> Charles Hottel wrote:
>> I thought some of you might be interest in this.  Note SAFECode
…[88 more quoted lines elided]…
>

Thanks for the interesting response.  I always look forward to hearing your 
opinions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
