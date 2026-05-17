[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EQUAL TO in COBOL

_37 messages · 14 participants · 2017-05 → 2018-09_

---

### EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-15T05:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<entbffF1poiU1@mid.individual.net>`

```
I am writing something at the moment that has to process COBOL source.

It parses statements across lines into words and then looks at the
relative positions of Keywords, quotes, and noise to determine whether
something is of interest to the process going on.

There's too much to go into here but the above is the gist of it.

One of the critical factors is the the detection and placement of the
word "TO" in a given COBOL statement.

I thought I had this covered but I realized that people can use "EQUAL
TO" as well as MOVE...TO, SET...TO, CONNECT... TO and GO TO...

This got me to reminiscing and I could not recall a single instance, in
50 years of looking at COBOL, where somebody wrote:

"A EQUAL TO B" or even, "A EQUALS B"

Everybody seems to use " = ".

Most people would rather write less than more...

I'm trying to persuade myself that I don't need to trap it because it
isn't worth the effort... (the old: "Where do I draw the line at error
trapping?" conundrum...) I would need to make this a special exception
and treat it as a special case. That means adding code (complexity) to
something that is already complex... (Although it ISN'T an error as far
as COBOL is concerned, I am using the TO for a specific purpose and this
would be an exception for my code.)

I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
to = ?

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2017-05-15T07:18:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On 5/15/2017 5:42 AM, pete dashwood wrote:
› I am writing something at the moment that has to process COBOL source.
› 
…[31 more quoted lines elided]…
› 

While I have never used EQUAL TO that I can remember, I did work
somewhere once ( a long time ago) where "=" was frowned on (read
not allowed by local standards) and we used EQUAL. I think it was
in support of the notion that COBOL was to be read like English
statements.

bill
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-05-15T07:47:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p2@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p2@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:
› On 5/15/2017 5:42 AM, pete dashwood wrote:
 
› [snip]
 
›› (Although it ISN'T an error as far
›› as COBOL is concerned, I am using the TO for a specific purpose and this
…[8 more quoted lines elided]…
› not allowed by local standards) and we used EQUAL.

My experience is similar to Mr Gunshannon's. Just as a matter of elegance
'=' conveys as much information as 'IS EQUAL TO' in ten fewer keystrokes
but I've worked on sites that had a Do Unnecessary Work phase... they
usually had a lot of PICTURE IS, too.

DD
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T08:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p3@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p2@usenetarchives.gap> <gap-c6d64c8dd4-p3@usenetarchives.gap>`

```
On 15/05/17 11:47 PM, doc··f@pa··x.com wrote:
› In article ,
› Bill Gunshannon   wrote:
…[22 more quoted lines elided]…
› 
Thanks Doc.

Funny you should mention the old noise word "IS"...

The code I mentioned fell over recently when it encountered "IS GLOBAL"
and "IS EXTERNAL", but works fine for "GLOBAL" and "EXTERNAL". I have
fixed it.

I have all the various forms of PICTURE covered. Did you know there was
a Burroughs compiler that allowed "PC" as an abbreviation for "PICTURE"?
Officially, the tool I am writing supports COBOL '85, but nobody seems
to read that, and there are outraged wails if it stumbles on "PC" for
PICTURE... (I have fixed it, but I really should not have...)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-05-22T13:38:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p4@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p2@usenetarchives.gap> <gap-c6d64c8dd4-p3@usenetarchives.gap> <gap-c6d64c8dd4-p4@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 15/05/17 11:47 PM, doc··f@pa··x.com wrote:
 
› [snip]
 
›› My experience is similar to Mr Gunshannon's.  Just as a matter of elegance
›› '=' conveys as much information as 'IS EQUAL TO' in ten fewer keystrokes
…[5 more quoted lines elided]…
› Funny you should mention the old noise word "IS"...

'Old noise word' has also been used to describe many sounds I make.

[snip]

› Did you know there was
› a Burroughs compiler that allowed "PC" as an abbreviation for "PICTURE"?

Never heard of that one before, Mr Dashwood... and I hope to encounter it,
professionaly, even less frequently.

DD
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T08:45:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p2@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p2@usenetarchives.gap>`

```
On 15/05/17 11:18 PM, Bill Gunshannon wrote:
› On 5/15/2017 5:42 AM, pete dashwood wrote:
›› I am writing something at the moment that has to process COBOL source.
…[42 more quoted lines elided]…
› 
Thanks Bill.

"EQUAL" would not be problematic for me; it's just that word TO...

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-05-15T08:56:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p7@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
Hello pete!

Monday May 15 2017 10:42, pete dashwood wrote to All:


> I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
> to = ?

I don't but have a lot of programs in ACAS written from the 60's onwards
that do. If I have to do any mods to them I do change it but still lots
left.

Same does apply to other long winded variants eg IS EQUAL OR GREATER THAN
etc.

End of the day, 'TO' is a noise word if only looking for primary reserved
words there are others :)

I bypass them for my tools such as cobxref and in the example you give as
they are all reserved words I treat the same as I only look for non
reserved words and where they are in program (e.g., division & section
etc).


Vince
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T08:55:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p7@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p7@usenetarchives.gap>`

```
On 16/05/17 12:56 AM, Vince Coen wrote:
› Hello pete!
› 
…[24 more quoted lines elided]…
› 
Thanks Vince.

I hadn't thought about ACAS or ABAPS but, in the context of this tool
(which is concerned primarily with Fujitsu PowerCOBOL) they are not
relevant.

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "doctrinsograce" <ua-author-6402540@usenetarchives.gap>
- **Date:** 2017-05-15T09:52:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p9@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
I still come across it regularly. Although I wore a pretty print that takes it out.

I tend to avoid the superfluous use of comma, too.
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T08:57:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p9@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p9@usenetarchives.gap>`

```
On 16/05/17 1:52 AM, Doc Trins O'Grace wrote:
› I still come across it regularly. Although I wore a pretty print that takes it out.
›
› I tend to avoid the superfluous use of comma, too.
›
:-)

Thanks.

(Keep taking the medicine...)

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2017-05-15T10:49:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p11@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On Mon, 15 May 2017 21:42:04 +1200, pete dashwood
wrote:

› I am writing something at the moment that has to process COBOL source.
› 
…[30 more quoted lines elided]…
› to = ?


I suspect a main driver was the existence of print trains that didn't
have some of the special characters. For example, =, <, and > were
omitted from many of the fast 1403 trains/chains (AN, HN).

Omission of those characters from keypunch machines was probably an
issue too.

That being said, I do see it occasionally.
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-05-17T01:09:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p11@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap>`

```
On 5/15/2017 9:49 AM, Robert Wessel wrote:
› On Mon, 15 May 2017 21:42:04 +1200, pete dashwood
›  wrote:
…[16 more quoted lines elided]…
› 

I used to write IS EQUAL TO (or simply EQUALS) for that exact reason on
an IBM Series/1 in the early 1980's. The band broke on our printer, and
we had to wait for several weeks to get the part replaced. In the
meantime IBM installed a replacement band that had a much more limited
character set. As I recall it was missing all of the following signs:
= > < ( ) + -

Back in those days we still relied on printed compiler listings for
documentation and they were extremely difficult to read without those
symbols.





http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2017-05-17T01:23:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p12@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap>`

```
On Wed, 17 May 2017 00:09:08 -0500, Arnold Trembley
wrote:

› On 5/15/2017 9:49 AM, Robert Wessel wrote:
›› On Mon, 15 May 2017 21:42:04 +1200, pete dashwood
…[24 more quoted lines elided]…
› = > < ( ) + -


The relationals were missing on many/most fast trains (all those not
intended to support programming), and the parenthesis were often
missing as well (although less commonly than the relationals). The
plus and minus, OTOH, were on almost all trains, since negative
amounts are a pretty common thing to print. Which is not to say such
trains didn't exist, take the 40-character XN* train, for example, but
then you were limited to the 36 letters and digits, plus comma, period
dollar and asterisk.


*And frankly, I never saw one in the wild
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 4)_

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2017-05-19T23:23:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p13@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p13@usenetarchives.gap>`

```
On Wednesday, May 17, 2017 at 3:23:20 PM UTC+10, rob··.@ya··o.com wrote:
› On Wed, 17 May 2017 00:09:08 -0500, Arnold Trembley
›  wrote:
…[37 more quoted lines elided]…
› dollar and asterisk.

Curious, we had the opposite experience, a number of times. When the
regular print train on the line printer wore out, it was temporarily
replaced with one that had upper and lower case, with serif characters.
Of course, it ran a lot slower...
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T09:02:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p13@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p13@usenetarchives.gap>`

```
On 17/05/17 5:23 PM, Robert Wessel wrote:
››› That being said, I do see it occasionally.
››› 
…[12 more quoted lines elided]…
› trains didn't exist, take the 40-character XN* train, for example, but

Thanks Robert,

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T09:01:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p12@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap>`

```
On 17/05/17 5:09 PM, Arnold Trembley wrote:
› On 5/15/2017 9:49 AM, Robert Wessel wrote:
›› On Mon, 15 May 2017 21:42:04 +1200, pete dashwood
…[33 more quoted lines elided]…
› 
Thanks for the response. I don't think 1980 print trains are pertinent
to my code, but they certainly are good background as to why people
might use the full words rather than the symbols.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-05-23T08:28:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p16@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p16@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 17/05/17 5:09 PM, Arnold Trembley wrote:
 
› [snip]
 
›› I used to write IS EQUAL TO (or simply EQUALS) for that exact reason on 
›› an IBM Series/1 in the early 1980's.  The band broke on our printer, and 
…[11 more quoted lines elided]…
› might use the full words rather than the symbols.

Have a care, Mr Dashwood... this comes dangerously close to dissemination
of Anciente Wisdome.

DD
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 4)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-05-24T06:37:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p16@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p16@usenetarchives.gap>`

```
Hello pete!

Saturday May 20 2017 14:01, pete dashwood wrote to All:

> On 17/05/17 5:09 PM, Arnold Trembley wrote:
>> On 5/15/2017 9:49 AM, Robert Wessel wrote:
…[37 more quoted lines elided]…
> might use the full words rather than the symbols.


Must admit I do not recall that as a problem on both ICL and IBM kit.

May be the sites I worked at, spent extra to get the full char set chains
but many had more than one printer on a system?


There again I might be forgetful in this matter.. been a long tome ago :)

As for a reason not to do it - If the punch card service was slow for my
needs (Often) I would go and use a spare machine and key them in myself and
using the abbreviations was a lot less keying :)

Same applied if I used the paper tape punch and in both cases for very
small number of changes it was done on a portable punch and it was not that
long ago that I can across my one still sitting in a box in my study. Don't
know what happened to the card punch machine but it was a little larger and
heavier.

Going back to the usage of the comma and the end of a sub clause/s - I was
NEVER a user of such as it was sometimes very difficult to tel them apart
on listings and if some errant card punch operator mis-keyed you could
spend hours/days looking for why the program was not working as expected -
just because of a period incorrectly typed.

On the job form that was supplied with the Cobol source forms I used, I do
seem to recall that mine always had the message that there was NO COMMA'S
in this program along with the coding style used - (see next para). Just to
try and make sure they did not mis-key, which was not often at all.

Oh, and all periods written on forms had a circle around them like wise
zero or was it 'O' had a slash thru it to signify that it was one and not
the other.. Think it was the alpha O that did, with the Z having a hypen
thru and the letter 'I' being fully topped and tailed, but it is a lloonngg
time ago:)

Remember everything was in UPPER CASE.

Vince
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 5)_

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2017-05-24T16:53:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p18@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p16@usenetarchives.gap> <gap-c6d64c8dd4-p18@usenetarchives.gap>`

```
On Wed, 24 May 2017 11:37:22 +0100, "Vince Coen"
wrote:

› Hello pete!
› 
…[47 more quoted lines elided]…
› but many had more than one printer on a system?


Print trains were also usually interchangeable, although operations
would usually try to batch jobs so that the number of changes was
minimized. Certainly if a shop had multiple printers you'd often see
the different trains almost always living in a particular printer,
except in the much less common case when you really had a lot of extra
work of one type (*and* the shop had an extra train of the required
type - I saw a number of shops that had (say) three printers and
exactly three print trains).

The advantage of the more constrained trains was that they printed
fasters. Going from a TN to an AN train would more than double print
speed on a 1403 - although you lost 2/3rds of the possible printable
characters.



› There again I might be forgetful in this matter.. been a long tome ago :)
› 
› As for a reason not to do it - If the punch card service was slow for my
› needs (Often) I would go and use a spare machine and key them in myself and
› using the abbreviations was a lot less keying :)


Back in school... There was a room full of keypunches, mostly 029s,
plus a few 129s and a couple of 026s. The major downside to the 026s
(other than the somewhat inferior keyboard), was that a number of the
special characters were *not* on the keyboard (or on the printer for
the interpretation line). OTOH, the multi-punch sequences for all of
the interesting characters were taped to the front of the machine, so
it's not like they were actually hard to enter.

The 026s almost always sat idle, even if the line of people waiting
for a free keypunch machine was out the door and down the hall, just
because most people couldn't deal with the 026s. So I pretty much got
to use a keypunch machine any time I wanted, with no waiting, and
could completely ignore the "half hour" rule even when the place was
busy.

I also made a few bucks selling people programming cards for the
keypunch machines (for programming purposes, mostly nothing but some
tab stops). You'd think people in programming classes would be able
to figure out how to make an 029 program card. The lab eventually put
the drums under lock and key because people kept breaking the read
mechanism by forcing the drum in or out without releasing the locking
mechanism first (although I managed to lobby them to still have them
available, you just had to ask whoever was managing the lab, and
they'd ask if you knew how to mount the drum).
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-29T04:16:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p19@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p16@usenetarchives.gap> <gap-c6d64c8dd4-p18@usenetarchives.gap> <gap-c6d64c8dd4-p19@usenetarchives.gap>`

```
On 25/05/17 8:53 AM, Robert Wessel wrote:
› On Wed, 24 May 2017 11:37:22 +0100, "Vince Coen" 
› wrote:
…[100 more quoted lines elided]…
› 
Great story, Robert!

I remember the old 026 and 029 key punch machines although I have to
confess, in those days, I was a lot more interested in the girls who
operated them...(Yes, it was before PC and GIRLS punched cards...MEN
punched the odd amendment by hand, on a hand punch, and became adept at
replacing chad with a pencil end when they made mistakes...)

There was an incident involving me and a punch girl in a lift (elevator,
for our American readers) during the Xmas party. The lift arrived at the
ground and we were re-arranging our clothes as the door opened to reveal
the Managing Director who was on his way to the party. Girl blushed and
I stammered a greeting. MD smiled and carried on. Later I found I had
lipstick all over my face so it was pretty obvious why he was smiling...
Whenever I see a punch card to this day, it brings back a number of
happy memories like this... :-)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-29T04:05:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p18@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap> <gap-c6d64c8dd4-p12@usenetarchives.gap> <gap-c6d64c8dd4-p16@usenetarchives.gap> <gap-c6d64c8dd4-p18@usenetarchives.gap>`

```
On 24/05/17 10:37 PM, Vince Coen wrote:
› Hello pete!
› 
…[83 more quoted lines elided]…
› 
Thanks for the memories, Vince. Although it was, as you say, a long
time ago, I need to deal with this today. The code is now written and is
working but I KNOW that if it encounters "EQUAL TO" it will fail...

At the moment I have too many other things to worry about, but once the
pressure is off I know it will just be a matter of time before I break
and rewrite it to handle EQUAL TO... :-)

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T08:58:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p11@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p11@usenetarchives.gap>`

```
On 16/05/17 2:49 AM, Robert Wessel wrote:
› On Mon, 15 May 2017 21:42:04 +1200, pete dashwood
›  wrote:
…[44 more quoted lines elided]…
› 
OK,

Thanks.

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-05-15T13:09:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p23@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On Monday, May 15, 2017 at 5:42:10 AM UTC-4, pete dashwood wrote:

[snip]

› This got me to reminiscing and I could not recall a single instance, in
› 50 years of looking at COBOL, where somebody wrote:
›
› "A EQUAL TO B" or even, "A EQUALS B"

>From your thread, in February, "Simplifying IFs in COBOL".
< https://groups.google.com/d/msg/comp.lang.cobol/SjLGh9i5nRs/G7pdZTqlBgAJ >
-----
Pete's exactly-disliked nested-IF:

IF A EQUAL TO B
IF A EQUAL TO C
-----

[snip]

› I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
› to = ?

Perhaps Mr Woodger?

I saw a lot of "IS EQUAL TO" in the 70s and I may have
used it a few times myself, before switching to COBOL
on PCs.

There was, until the 90s, a US government FIPS requirement,
which, at the low level, prohibited the use of ">", "<",
"=" and "OR" in relational expressions.

Any programmer who had to code to the low-level FIPS
requirement would have quickly adapted and, perhaps,
continued to write code consistent with that requirement.
In other words, "habituation"!
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T09:05:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p23@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p23@usenetarchives.gap>`

```
On 16/05/17 5:09 AM, Rick Smith wrote:
› On Monday, May 15, 2017 at 5:42:10 AM UTC-4, pete dashwood wrote:
› 
…[35 more quoted lines elided]…
› 
Thanks Rick.

I think we have all seen examples of habituation long after it made no
sense at all... :-)

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-20T09:14:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p25@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On 15/05/17 9:42 PM, pete dashwood wrote:
› I am writing something at the moment that has to process COBOL source.
› 
…[32 more quoted lines elided]…
› Pete.
Many thanks to all who responded.

It looks like I don't need to worry about it but there is a part of my
brain that will nag me until I make it "watertight"... :-)

Pete.

I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2017-05-20T14:03:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p25@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p25@usenetarchives.gap>`

```
On Sun, 21 May 2017 01:14:46 +1200, pete dashwood
wrote:

›› snip
› Many thanks to all who responded.
› 
› It looks like I don't need to worry about it but there is a part of my 
› brain that will nag me until I make it "watertight"... :-)

Is "TO" a noise word in all cases other than the construct ADD A B TO
C D?

Clark Morris
›
› Pete.
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2017-05-21T02:01:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p26@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p25@usenetarchives.gap> <gap-c6d64c8dd4-p26@usenetarchives.gap>`

```
On Sat, 20 May 2017 15:03:22 -0300, Clark F Morris
wrote:

› On Sun, 21 May 2017 01:14:46 +1200, pete dashwood
›  wrote:
…[8 more quoted lines elided]…
› C D?


It's not optional in MOVE and SET.
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-29T04:18:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p26@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p25@usenetarchives.gap> <gap-c6d64c8dd4-p26@usenetarchives.gap>`

```
On 21/05/17 6:03 AM, Clark F Morris wrote:
› On Sun, 21 May 2017 01:14:46 +1200, pete dashwood
›  wrote:
…[12 more quoted lines elided]…
›› Pete.
Hell, no.

TO is a KEYWORD; IS is a noise word...

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "bwtiffin" <ua-author-14501766@usenetarchives.gap>
- **Date:** 2017-05-23T21:00:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p29@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On Monday, May 15, 2017 at 5:42:10 AM UTC-4, pete dashwood wrote:

›
› I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
› to = ?
›

Quick count in the GnuCOBOL FAQ

345 occurrences of ' equal ' (might not be all code sample occurrences)

41 occurrences of ' equal to ' (probably all code samples and included in the count above)

17 occurrences of ' is equal to '

6 ' is not equal to ' of which 4 are ' not equal to '

Might not be habitual, but not an unheard of development style.

That compares to 985 ' = ', 83 ' not = ' and 14 ' != ' (mixing C, COBOL and some 30 other language samples in that document).

Having given out those nerdy stats, I try and cover lots of different coding styles in the FAQ, on purpose, to demonstrate the different options inherently available in COBOL.

Cheers,
Brian
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-29T04:24:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p29@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p29@usenetarchives.gap>`

```
On 5/24/17 1:00 PM, bwt··n@gm··l.com wrote:
› On Monday, May 15, 2017 at 5:42:10 AM UTC-4, pete dashwood wrote:
› 
…[23 more quoted lines elided]…
› 
Thanks VERY much, Brian.

Some solid stats are useful to me. 345 compared to 985 makes it pretty
definite that I will "fix" this code as soon as I get a chance.

Cheers,

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "acewaysoftware" <ua-author-14501822@usenetarchives.gap>
- **Date:** 2017-05-24T22:07:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p31@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
On Monday, May 15, 2017 at 7:42:10 PM UTC+10, pete dashwood wrote:
› I am writing something at the moment that has to process COBOL source.
› 
…[34 more quoted lines elided]…
› I used to write COBOL; now I can do anything...

Lots of detail conversation going on here. I did a Cobol program that converted Cobol code and it became specific to the original code. One parses lines and has to attend to full stops over multiple lines of code.

My comment is that Cobol compilers do this complex parsing and it gets very complex for every style of expression. It reinforces my view that Cobol is a chameleon language that is highly adaptable to new environments and is under-rated in the modern world.

Greg
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-05-29T05:04:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p31@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p31@usenetarchives.gap>`

```
On 5/25/17 2:07 PM, ace··e@gm··l.com wrote:
› On Monday, May 15, 2017 at 7:42:10 PM UTC+10, pete dashwood wrote:
›› I am writing something at the moment that has to process COBOL source.
…[42 more quoted lines elided]…
› 
Hi Greg,

thanks for the post.

I also wrote a "COBOL language converter" (called "COSSET" - COBOL
SOURCE STATEMENT EDIT and TRANSLATE) for Control Data Corporation, back
in the early 1970s, using CDC COBOL on the Cyber series. :-) We used it
to convert other people's COBOL into CDC COBOL...Mostly, IBM, ICL, and
some Honeywell. Marketing loved it :-)

The current effort has to do with Fujitsu PowerCOBOL, so at least there
is a decent standard (COBOL '85). It isn't just about parsing full stops
over lines; on PCs there can be tabs and line breaks as well, embedded
in the code, not to mention the fact that COBOL allows lines to be
broken on white space. The first step is to identify the scope of the
construct being processed (terminated by a full stop, a scope delimiter,
or the next COBOL verb), in terms of lines, then get everything on those
lines into an array of strings with a COBOL word in each string. The C#
SPLIT function does this very well and obligingly removes empty entries
caused by multiple spaces between words. Then it comes down to
recognizing keywords, literals, GUI Control names, GUI Attributes,
things I am interested in, and noise words. After that it gets harder... :-)

The object is to convert all of the PowerCOBOL scriptlets for a given
PowerCOBOL GUI sheet (Form), into a single OO COBOL (Fujitsu NetCOBOL)
Class, with a Method that equates to each of the scriptlets - (100%
salvage of the legacy COBOL...), that gets packaged as a COM component
so it can be used by Standard Windows Forms.

We end up with Windows Forms and OO COBOL code-behinds that replicate or
exceed the original functionality and remove the dependency on
PowerCOBOL, which seems to have a very bleak future at the moment.

(Despite the fact that people all over the world are using it, there is
no support from GTS for it and it has been removed from the product list
on their web site. There is no official "migration path" or tools
provided, no chance of running it on 64 bit, and it is reminiscent of
the Micro Focus Visoc fiasco back in the last century, where an entire
user base was just shafted by the vendor (Micro Focus today are a much
better company...))

Users can continue with OO COBOL or they can use C# or VB.Net, or they
can mix languages, so they can gradually evolve their existing systems
without having to do a sudden Migration to a completely new environment.

But all of this "Brave New World" takes a lot of "Brave Old-fashioned
Work" and it is keeping me off the streets at the moment. :-)

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: EQUAL TO in COBOL

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-25T01:50:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p33@usenetarchives.gap>`
- **In-Reply-To:** `<entbffF1poiU1@mid.individual.net>`
- **References:** `<entbffF1poiU1@mid.individual.net>`

```
pete dashwood wrote:

› I am writing something at the moment that has to process COBOL source.
› 
…[32 more quoted lines elided]…
› Pete.
There are always a few pedants around who will go to the extreme,
e.g. writing
IF A IS EQUAL TO B THEN ...
:-D
JLT
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-09-25T09:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p33@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p33@usenetarchives.gap>`

```
On 09/25/2018 01:50 AM, J Leslie Turriff wrote:
› pete dashwood wrote:
› 
…[39 more quoted lines elided]…
› 

Some people continue to do that because it represents the
paradigm that COBOL was designed with, that is, code that
can be more easily read by humans as well as computers.

As compared to the other popular language of the time which
would have written: IF (A.EQ.B)

And, today, space and the cpu time needed to parse the more
verbose statements are pretty much meaningless.

bill
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-25T15:51:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p34@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p33@usenetarchives.gap> <gap-c6d64c8dd4-p34@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:
› On 09/25/2018 01:50 AM, J Leslie Turriff wrote:
›› pete dashwood wrote:
 
›› [snip]
 
››› I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
››› to = ?
…[10 more quoted lines elided]…
› can be more easily read by humans as well as computers.

In some shops I've heard that used to justify Why We Do Things This Way -
'COBOL is supposed to be English-like and this is... Englishier than other
ways so that's Why We Do Things This Way' - but after two, maybe three
bouts of There's More Than One Way it becomes 'We Do Things This Way', if
you want to see it pass Prod Review it needs... ' and that's it.

DD
```

###### ↳ ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "ime" <ua-author-6098869@usenetarchives.gap>
- **Date:** 2018-09-25T18:16:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p34@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p33@usenetarchives.gap> <gap-c6d64c8dd4-p34@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:

› Some people continue to do that because it represents the
› paradigm that COBOL was designed with, that is, code that
…[3 more quoted lines elided]…
› would have written:  IF (A.EQ.B)

That's FORTRAN IV. When Cobol was written, and for many years afterward,
the main US alternative was FORTRAN II :

IF (A-B) 202,204,202
```

##### ↳ ↳ Re: EQUAL TO in COBOL

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2018-09-25T15:33:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6d64c8dd4-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6d64c8dd4-p33@usenetarchives.gap>`
- **References:** `<entbffF1poiU1@mid.individual.net> <gap-c6d64c8dd4-p33@usenetarchives.gap>`

```
In article ,
J Leslie Turriff wrote:
› pete dashwood wrote:
 
› [snip]
 
›› I just wondered if anybody here HABITUALLY uses EQUAL TO in preference
›› to = ?
…[4 more quoted lines elided]…
› IF A IS EQUAL TO B THEN ...

Now gather 'round, youngsters, and try to imagine a time where some very
large, very influential companies would include, as a measure of
productivity, a programmer's Number of Lines of Code Written per (unit
time).

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
