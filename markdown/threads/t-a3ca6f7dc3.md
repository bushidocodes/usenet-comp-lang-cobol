[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: A chapter of accidents...

_7 messages · 4 participants · 2021-06_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: A chapter of accidents...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-06-12T22:33:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iil931F2e5jU1@mid.individual.net>`

```
You know how it is...

You're working on things with the usual ups and downs but nothing
untoward, then suddenly, things stop. Your FTP access to your site no
longer works. You can't maintain the web site.

You check your router and Internet, it's fine.

Open a ticket with your Internet provider and get no response.

You've been with him for over 13 years and consider the guy a friend. He
always responds promptly.

You raise another ticket requesting communication.

No response.

After a couple of days, you try phoning. (He is in Wellington, about 300
miles away.)

The phone has been disconnected.

You decide to try and check if he is OK...

Various searches in various places finally reveal that he died a week ago.

This is a bit of a shock but there must be someone managing the
business, right?

No. There isn't.

Everything looks fine at their site because it is all automated. You
could sign up for the service and never know that it was in a state of
slow demise...

Over a period of around 4 weeks I had to watch helplessly as something I
spent over a decade building, disintegrated.

FTP stopped then returned, then stopped again and became "intermittent",
then Control Panel, then Mail, then Web Services... It was really sad.

While this was happening, and whenever FTP was running, I was salvaging
the entire site to an external hard drive on my local machine...

Once I knew he had passed I had to find a new web host.

This is a non trivial exercise, but in case any of you are in the same
boat, here's the bottom line on the extensive searching, conversations,
and tests I did:

Three finalists selected from some 20-odd "possibles":

1. Gator. US based with very good service and support. Excellent pricing.

2. AccuWeb. US based with SSD hosting at a very reasonable cost.

3. A number of Kiwi Hosts who really couldn't match the Americans on
price, but added value with great support and personalized service.

I ruled out major sites like GoDaddy, because I'm not running a
templated site in Word Press; I need Windows hosting for ASP.Net running
on IIS, where I can build and test C# code-behinds and run COBOL COM
components...

I have gone with a site in Auckland called Open Host.

I needed to get the PRIMA domain transferred out of the old hosting and
there was no-one to talk to about it. Open Host were fantastic and
worked with the NZ Domain Authorities to get a new UDAI and stabilize
and protect the domain.

Just over half an hour ago I was able to re-establish the PRIMA Web
Services and get the site public again.

If anyone has had mail to PRIMA returned as undeliverable during the
past 4 weeks, that's the reason. It should be back now, but I have not
yet restored all of the mail accounts.

If you try and access the domain https://primacomputing.co.nz you will
be forbidden (I'll be looking at that in the coming week), however, if
you access the web site via the new landing page:
https://primacomputing.co.nz/primaMetro you should get to the new site.

Not everything that worked on the old site will be working on the new
one, but all of the essential information and freebies should be
accessible. The videos are there and SHOULD be working. I tested a
couple and my favorite one:
https://primacomputing.co.nz/PRIMAMetro/PC2NvP.aspx is working even
better than before... :-)

There are some lessons to learn out of all of this:

1. If you are going to offer people a hosting service, make sure there
are measures in place to protect your clients in the event of your
untimely demise.

2. If you are looking for hosting, try and establish that whoever you go
with is more than a "one man band" and if anything happens to them, you
can easily move your site to alternate hosting. My old host was
brilliant and extremely capable, but when he went, there was no-one to
take over...

For myself, it is my intention to arrange a public notification on the
site with subsequent closure, in the event of my demise, or, if anyone
wants to keep it running, it will be financed through a trust I'll set
up. The main thing is that people should be communicated with.

Pete.






I used to write *COBOL*; now I can do *anything*...
```

#### ↳ Re: OT: A chapter of accidents...

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2021-06-13T03:11:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<iil931F2e5jU1@mid.individual.net>`
- **References:** `<iil931F2e5jU1@mid.individual.net>`

```
On 6/12/2021 9:33 PM, pete dashwood wrote:
› You know how it is...
› (snip)

Pete,

I'm very glad to see that your site is back up! I tried it with Mozilla
Firefox and also Chrome, Edge, and Brave (which are all Chromium based).

You've obviously had a lot to do in a short time. I've only had to
change Hosting services once, and there was ample advance warning.
Normally I always have a current backup of every page and file hosted on
my website, which can save some time.

I am sorry to hear your friend passed away.

Kind regards,

Arnold
```

##### ↳ ↳ Re: OT: A chapter of accidents...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-06-16T06:09:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ca6f7dc3-p2@usenetarchives.gap>`
- **References:** `<iil931F2e5jU1@mid.individual.net> <gap-a3ca6f7dc3-p2@usenetarchives.gap>`

```
On 13/06/2021 19:11, Arnold Trembley wrote:
› On 6/12/2021 9:33 PM, pete dashwood wrote:
›› You know how it is...
…[11 more quoted lines elided]…
› 
The new host backs up the entire site every day...

I also have various copies and snapshots of it on external disk and in
localhost, where I do most of the development.
› I am sorry to hear your friend passed away.

It's funny because we never actually physically met, but we addressed
and worked through a number of problems and over 13 years, became friends.
›
› Kind regards,
…[3 more quoted lines elided]…
›

Thanks for the kind response, Arnold.

As we say in this part of the world: "I'm flat out like a lizard
drinking..." :-)

There are still some things to be addressed.

The actual structure of the site is different on the new server and I
debated whether to get it changed or work with it. I have worked with it
and, in some ways, it is better than before but it does mean that (at
least at the moment) some default pages are not being activated and you
have to put the full URL. It probably needs to have a few virtual
directories marked as web applications and we'll get it sorted pretty soon.

Thanks for accessing.

Pete.

I used to write *COBOL*; now I can do *anything*...
```

#### ↳ Re: OT: A chapter of accidents...

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2021-06-13T17:03:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<iil931F2e5jU1@mid.individual.net>`
- **References:** `<iil931F2e5jU1@mid.individual.net>`

```
In article ,
pete dashwood wrote:
› You know how it is...
 
› [snip]
 
› Various searches in various places finally reveal that he died a week ago.

Somebody got 'hit by a truck'? Not a problem, we were taught that back
when... back when it was so long ago we learned it, practised it, taught
it... and then forgot it.

[snip]

› Just over half an hour ago I was able to re-establish the PRIMA Web
› Services and get the site public again.

Well done, Mr Dashwood.

[snip]

› There are some lessons to learn out of all of this:
 
› [snip]
 
› For myself, it is my intention to arrange a public notification on the 
› site with subsequent closure, in the event of my demise, or, if anyone 
› wants to keep it running, it will be financed through a trust I'll set 
› up. The main thing is that people should be communicated with.

If you find a way to communicate with people from the Great Beyond please
send me a postcard I can pass along to a fellow I know inclined towards
philately.

As for preparations for When Things Blow Up... not that long ago, must've
been about '03, '04... 20, not 19... certainly not 18, the shirt-collars
would've been all wrong... and people were *much* too clean for 17, so 20
it was...

... anyhow, I took a contract with a Federal agency to work on their
payroll system. While I was sitting about waiting for identification
badges, security clearances and other trivialities I was asked to write a
program which would, if given a Division code, would go through the
Payroll Master File and authorise everyone in that Division ten days'
worth of regular salary (also called 'straight 80').

What was the reason for this? First and foremost, Folks Gotta Get Paid...
and shortly before '03, '04 it was 11 September 2001. Folks saw that
nightmare and someone thought 'what would happen if one of our timekeepers
had been in there and didn't certify the employees' timecards?'...

... and if a timekeeper - or someome appropriately designated to assume
the duties of a timekeeper (as specified in that dense, unhumorous prose
which composes Federal regulations) - does not certify the hours worked as
valid the Folks Won't Get Paid... and that is unthinkable.

So... folks didn't think about it for a couple-three years and then they
had this new guy sitting and twiddling his thumbs... so they gave me the
task.

After a bit of analysis I asked 'I'm noticing something about Divisions...
it's ten characters and there seem to be subdivisions, you'll have people
with AA division, then AAA, AAAB, AAAD, AAC, AACZXYWVUT... do you want to
be able to wildcard?'

'You can do that?'

'Not a problem... and while I'm at it, there might be some time when you
don't have a Division but you have a list of people you want to get
straight-80, I can set this up so you can use a list of Social Security
Numbers as input and those people will get processed.'

'You can do that?'

'Well... to make it neat I should limit the input, how about anywhere
between one and five hundred?'

... and I did it... and ever since then the Secretary of this agency gets
their time submitted for pay by this contigency program.

(the rest of the agency gets paid by the Monolith Program I had to
modify... but that's another story)

DD
```

##### ↳ ↳ Re: OT: A chapter of accidents...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-06-16T06:14:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ca6f7dc3-p4@usenetarchives.gap>`
- **References:** `<iil931F2e5jU1@mid.individual.net> <gap-a3ca6f7dc3-p4@usenetarchives.gap>`

```
On 14/06/2021 09:03, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[82 more quoted lines elided]…
› 
Really great story, Doc.

Enjoyed it muchly and you did some cool stuff there.

It is really good to see faces when you suggest something that is really
not so difficult but no-one thought about before.

It's like adding value to the IT Department... :-)

Cheers,

Pete.

I used to write *COBOL*; now I can do *anything*...
```

#### ↳ Re: OT: A chapter of accidents...

- **From:** "kerry.liles" <ua-author-7511031@usenetarchives.gap>
- **Date:** 2021-06-14T12:27:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<iil931F2e5jU1@mid.individual.net>`
- **References:** `<iil931F2e5jU1@mid.individual.net>`

```
On 6/12/2021 10:33 PM, pete dashwood wrote:
› You know how it is...
› 
…[106 more quoted lines elided]…
› 


An *amazing* chronicle... congratulations on apparently getting through
that level of hardship. Condolences about your friend who provided
hosting service. Yes, many of us know lots of "rules" - "backup of
backup", "a backup isn't unless it has been read and verified" etc and
it is even more astonishing how many times I have caught myself ignoring
such sage advice (momentarily) until I come to my limited senses... :)

Glad to hear Prima is getting back on its feet.
Best wishes.

Kerry
```

##### ↳ ↳ Re: OT: A chapter of accidents...

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2021-06-16T06:33:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ca6f7dc3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ca6f7dc3-p6@usenetarchives.gap>`
- **References:** `<iil931F2e5jU1@mid.individual.net> <gap-a3ca6f7dc3-p6@usenetarchives.gap>`

```
On 15/06/2021 04:27, Kerry Liles wrote:
› On 6/12/2021 10:33 PM, pete dashwood wrote:
›› You know how it is...
…[125 more quoted lines elided]…
› 
Thanks, Kerry.

There's a way to go yet and the "official" re-launch is not 'til next
Monday but I reckon most things should be working properly by then.

To make it all enjoyable, I have not been well and with various
attendances to hospital (which I really hate) and being poked, probed,
stabbed, and scanned, I found my sense of humor deserting me. (It's
coming back now as the stress eases... :-))

Fortunately, It looks like I am on the road to recovery.

A warning to all of you:

I was prescribed a very powerful antibiotic for some nasty stomach
bacteria, which were threatening to do terrible things to my digestive
system. I told them I wasn't a fan but they assured me there was no
alternative and 4 weeks on this stuff would knock the little buggers
out. It did, but it killed everything else as well (including, almost,
me...).

Now it turns out that the usual recovery time for this stuff is 3 YEARS!
(Nobody mentioned this when they were persuading me to have it... I just
wish they'd be honest and present a balanced case that I could decide
properly, but they treat us like morons who should do what we are told
with unquestioning obedience... (I've never been good at that :-)) I was
not amused. That was nearly 6 months ago and I am just starting to get
something like normality.

I really love good food and it is a great pleasure in my life.

Bottom LINE:

Unless several different medical opinions tell you your life depends on
it, DON'T take antibiotics and don't TAKE ANYTHING for long periods of
time... NOTHING is safe if you take it long enough...

Cheers,
Pete.

I used to write *COBOL*; now I can do *anything*...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
